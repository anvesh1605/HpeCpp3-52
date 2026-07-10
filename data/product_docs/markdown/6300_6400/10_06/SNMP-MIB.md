AOS-CX 10.06 SNMP/MIB Guide
6100, 6200, 6300, 6400, 8320, 8325, 8360, 8400 Switch Series

Part Number: 5200-7725a
Published: January 2021
Edition: 2

© Copyright 2020, 2021 Hewlett Packard Enterprise Development LP

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
Enterprise has no control over and is not responsible for information outside the Hewlett Packard Enterprise
website.

Contents

Chapter 1 About this document...................................................................... 4
Applicable products........................................................................................................................................4
Latest version available online......................................................................................................................4
About the examples....................................................................................................................................... 4
Switch prompts in examples......................................................................................................................... 5

Chapter 2 SNMP...................................................................................................6
Configuring SNMP.......................................................................................................................................... 6
SNMP commands........................................................................................................................................... 7
event-trap-enable.........................................................................................................................7
rmon alarm........................................................................................................................................ 8
rmon alarm {enable | disable} {index | all}.............................................................. 9
show rmon alarm........................................................................................................................... 10
show snmp agent-port................................................................................................................11
show snmp community.................................................................................................................. 11
show snmp system.........................................................................................................................12
show snmp trap............................................................................................................................. 13
show snmp vrf............................................................................................................................... 13
show snmpv3 context.................................................................................................................. 14
show snmpv3 engine-id............................................................................................................. 14
show snmpv3 security-level.................................................................................................. 15
show snmpv3 users...................................................................................................................... 15
snmp-server agent-port........................................................................................................... 16
snmp-server community............................................................................................................. 16
snmp-server historical-counters-monitor.....................................................................17
snmp-server host.........................................................................................................................17
snmp-server system-contact.................................................................................................. 19
snmp-server system-description......................................................................................... 20
snmp-server system-location................................................................................................ 21
snmp-server vrf........................................................................................................................... 21
snmp-server trap-source interface vrf......................................................................... 22
snmpv3 context............................................................................................................................. 23
snmpv3 engine-id.........................................................................................................................24
snmpv3 security-level............................................................................................................. 24
snmpv3 user.................................................................................................................................... 25

Chapter 3 Entity MIB support........................................................................ 28
Location of the MIB files on the web......................................................................................................... 28
Newly introduced MIBs and Traps for 10.06............................................................................................. 28

Chapter 4 Support and other resources...................................................... 38
Accessing Aruba Support............................................................................................................................ 38
Accessing updates........................................................................................................................................ 38
Warranty information.................................................................................................................................. 39
Regulatory information............................................................................................................................... 39
Documentation feedback............................................................................................................................ 39

Contents

3

Chapter 1
About this document

Applicable products
This document applies to the following products:

• Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

• Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

• Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A, JL667A,

JL668A, JL762A)

• Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

• Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

• Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

• Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A, JL711A)

• Aruba 8400 Switch Series (JL375A, JL376A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

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

4

AOS-CX 10.06 SNMP/MIB Guide

switch(config-if)#

Identifies the interface context.

Variable information in CLI prompts

In certain configuration contexts, the prompt may include variable information. For example, when in
the VLAN configuration context, a VLAN number appears in the prompt:

switch(config-vlan-100)#

When referring to this context, this document uses the syntax:

switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Switch prompts in examples
The switch prompts used in this document are examples and might not match your particular switch or
environment.

In examples:

• The switch prompt starts with the word switch.

• The switch prompt also indicates the command context.

For example:

switch>

Indicates the operator command context.

switch#

Indicates the manager command context.

switch(config)#

Indicates the global configuration context.

In your environment, the switch prompt can vary because the prompt is user-configurable.

◦ Typically, the switch prompt begins with the host name of the switch.

◦ The switch prompt contains specifier in certain configuration command contexts, such as interface

name or VLAN ID. For example: switch(config-vlan-100)#

In these cases, examples in this document might contain placeholders such as n or if.

Chapter 1 About this document

5

Chapter 2
SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing and modifying information about
managed devices on IP networks.

Configuring SNMP
The SNMP agent provides read-only access in this release.

Procedure

1. SNMP is not enabled on the switch by default, unless the user enables it over any available VRF or with

the default/mgmt VRF using the command snmp-server vrf <NAME>. For example, use the command
snmp-server vrf mgmt to enable SNMP on the management interface. Use the command snmp-
server vrf default to enable SNMP on the default VRF. Use the command snmp-server vrf
<USERDEFINED_VRF_NAME> to enable SNMP on the user created VRF.

2. Set the system contact, location, and description for the switch with the following commands:

• snmp-server system-contact

• snmp-server system-location

• snmp-server system-description

3. If required, change the default SNMP port on which the agent listens for requests with the command

snmp-server agent-port.

4. By default, the agent uses the community string public to protect access through SNMPv1/v2c. Set a

new community string with the command snmp-server community.

5. Configure the trap receivers to which the SNMP agent will send trap notifications with the command

snmp-server host.

6. Create an SNMPv3 context and associate it with any available SNMPv3 user to perform context specific v3

MIB polling using the command snmpv3 user <V3_USERNAME> context <CONTEXT_NAME>.

7. Create an SNMPv3 context and associate it with an available SNMPv1/v2c community string to perform
context specific v1/v2c MIB polling using the command snmpv3 context <CONTEXT_NAME> vrf
<VRF_NAME> community <COMMUNITY_NAME>.

8. Review your SNMP configuration settings with the following commands:

• show snmp agent-port

• show snmp community

• show snmp system

• show snmpv3 context

6

AOS-CX 10.06 SNMP/MIB Guide

• show snmp trap

• show snmp vrf

• show snmpv3 users

• show tech snmp

Example
Example 1

This example creates the following configuration:

• Enables SNMP on the out-of-band management interface (VRF mgmt).

• Sets the contact, location, and description for the switch to: JaniceM, Building2, LabSwitch.

• Sets the community string to Lab8899X.

switch(config)# snmp-server vrf mgmt
switch(config)# snmp-server system-contact JaniceM
switch(config)# snmp-server system-location Building2
switch(config)# snmp-server system-description LabSwitch
switch(config)# snmp-server community Lab8899X

Example 2

This example creates the following configuration:

• Creates an SNMPv3 user named Admin using sha authentication with the plaintext password

mypassword and using des security with the plaintext password myprivpass.

• Associates the SNMPv3 user Admin with a context named newContext.

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
     priv-pass plaintext myprivpass
switch(config)# snmpv3 user Admin context newContext

SNMP commands

event-trap-enable

Syntax

event-trap-enable

no event-trap-enable

Description

Enables the notification of events to be sent as traps to the SNMP management stations. It is enabled by
default.

The no form of this command disables the event traps.

Chapter 2 SNMP

7

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the event traps:

switch(config)# event-trap-enable

Disabling the event traps:

switch(config)# no event-trap-enable

rmon alarm

Syntax

rmon alarm index <INDEX> snmp-oid <SNMP-OID> rising-threshold <RISING-THRESHOLD>
     falling-threshold <FALLING-THRESHOLD> [sample-interval <SAMPLE-INTERVAL>] [sample-type <ABSOLUTE|DELTA>]

no rmon alarm [index <INDEX>]

Description

Stores configuration entries in an alarm table that defines the sample interval, sample-type, and threshold
parameters for an SNMP MIB object. Only the SNMP MIB objects that resolve to an ASN.1 primitive type of
INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge32, or TimeTicks) will be monitored.

The no form of this command removes all RMON alarms and allows you to specify an index to remove a
particular RMON alarm.

Command context

config

Parameters
index <INDEX>

Specifies the RMON alarm index. Range: 1 to 20.

snmp-oid <SNMP-OID>

Specifies the SNMP MIB object to be monitored by RMON.

rising-threshold <RISING-THRESHOLD>

Specifies the upper threshold value for the RMON alarm.

falling-threshold <FALLING-THRESHOLD>

Specifies the falling threshold value for the RMON alarm. The falling threshold must be less than the
rising threshold.

sample-interval <SAMPLE-INTERVAL>

Sample interval in seconds. Default: 30.

sample-type <ABSOLUTE|DELTA>

Specifies the method of sampling of the SNMP MIB object. Default: Absolute.

8

AOS-CX 10.06 SNMP/MIB Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring RMON for the MIB object ifOutErrors.15 with an index 1, rising threshold of 2147483647
and falling threshold of -2134 using absolute sampling for a sample interval of 100 seconds:

switch(config)# rmon alarm index 1 snmp-oid ifOutErrors.15 rising-threshold 2147483647
     falling-threshold -2134 sample-type absolute sample-interval 100

Removing RMON alarm with the index 5:

switch(config)# no rmon alarm index 5

rmon alarm {enable | disable} {index | all}

Syntax

rmon alarm {enable | disable} {index <INDEX> | all}

Description

Enables and disables the RMON alarm and its index. RMON alarm is enabled by default.

Command context

config

Parameters
enable

Enables the RMON alarm index

disable

Disables the RMON alarm index.

index <INDEX>

Specifies the RMON alarm index. Range: 1 to 20.

all

Specifies all the RMON alarms.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling or disabling all the RMON alarm:

switch(config)# rmon alarm enable all
switch(config)# rmon alarm disable all

Enabling or disabling RMON alarm by index:

switch(config)# rmon alarm enable index 1
switch(config)# rmon alarm disable index 1

Chapter 2 SNMP

9

show rmon alarm

Syntax

show rmon alarm [index <INDEX>]

Description

Displays the RMON alarm configurations.

Command context

config

Parameters
index <INDEX>

Specifies the RMON alarm index. Range: 1 to 20.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing all RMON alarm configurations:

switch# show rmon alarm
Index              : 1
Enabled            : true
Status             : valid
MIB object         : ifOutErrors.15
Sample type        : delta
Sampling interval  : 6535 seconds
Rising threshold   : 100
Falling threshold  : 10
Last sampled value : 0
Last sample time   : 2020-09-21 05:58:11

Index              : 3
Enabled            : true
Status             : invalid
MIB object         : IF-MIB::ifDescr.19
Sample type        : absolute
Sampling interval  : 10000 seconds
Rising threshold   : 4000
Falling threshold  : 10
Last sampled value : 0

Showing RMON alarm with alarm index 1:

switch# show rmon alarm index 1
Index              : 1
Enabled            : true
Status             : valid
MIB object         : ifOutErrors.15
Sample type        : delta
Sampling interval  : 6535 seconds
Rising threshold   : 100
Falling threshold  : 10
Last sampled value : 0
Last sample time   : 2020-06-21 05:58:11

10

AOS-CX 10.06 SNMP/MIB Guide

Showing disabled RMON alarm information:

switch# show  rmon   alarm
Index              : 1
Enabled            : false
Status             : valid
MIB object         : ifOutErrors.15
Sample type        : delta
Sampling interval  : 6535 seconds
Rising threshold   : 100
Falling threshold  : 10
Last sampled value : 0
Last sample time   : 2020-09-21 05:58:11

Index              : 3
Enabled            : false
Status             : invalid
MIB object         : IF-MIB::ifDescr.19
Sample type        : absolute
Sampling interval  : 10000 seconds
Rising threshold   : 4000
Falling threshold  : 10
Last sampled value : 0

show snmp agent-port

Syntax

show snmp agent-port

Description

Displays SNMP agent UDP port number.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying SNMP agent UDP port number:

switch# show snmp agent-port
SNMP agent port : 161

show snmp community

Syntax

show snmp community

Description

Displays a list of all configured SNMPv1/v2c communities.

Chapter 2 SNMP

11

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

Displays SNMP description, location, and contact information.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying SNMP description, location, and contact information:

switch# show snmp system
SNMP system information
----------------------------
System description : Aggregation router
System location : Main lab
System contact : John Smith, Lab Admin

12

AOS-CX 10.06 SNMP/MIB Guide

show snmp trap

Syntax

show snmp trap

Description

Displays all configured SNMP traps/informs receivers.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying all configured SNMP trap and informs receivers:

switch# show snmp trap
HOST                                    PORT  TYPE   VER COMMUNITY/USER NAME VRF
------------------------------------------------------------------------------------
10.10.10.10                             162   trap   v1  public              default
10.10.10.10                             162   inform v2c public              default
10.10.10.10                             162   inform v3  name                default

show snmp vrf

Syntax

show snmp vrf

Description

Displays the VRF on which the SNMP agent service is running.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying SNMP services enabled on VRF:

switch#show snmp vrf
SNMP enabled VRF
----------------------------
mgmt
default

Chapter 2 SNMP

13

show snmpv3 context

Syntax

show snmpv3 context

Description

Displays all configured SNMP contexts.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying all configured SNMP contexts:

switch# show snmpv3 context
--------------------------------------------------------------------------
name                            vrf                             community
--------------------------------------------------------------------------
contextA                        default                         private
contextB                        vrf_A                           public

switch# show snmpv3 context
--------------------------------------------------------------------------
Name           vrf             Community          ype[Instance_id]
------------------------------------------------------------------
A              default         public             vrf
switch#

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

14

AOS-CX 10.06 SNMP/MIB Guide

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

Description

Displays all configured SNMPv3 users.

For more details on the user enabled status, see snmpv3 security-level.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying all configured SNMPv3 users:

switch# show snmpv3 users
---------------------------------------------------------------------
User                            AuthMode  PrivMode  Context  Enabled
---------------------------------------------------------------------
name                            md5       none      none     False
name2                           sha       aes       none     True

Chapter 2 SNMP

15

snmp-server agent-port

Syntax

snmp-server agent-port <PORT>

no snmp-server agent-port [<PORT>]

Description

Sets the UDP port number that the SNMP master agent uses to communicate. UDP port 161 is the default
port.

The no form of this command sets the SNMP master agent port to the default value.

Command context

config

Parameters
<PORT>

Specifies the UDP port number that the SNMP master agent will use. Range: 1 to 65535. Default: 161.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the SNMP master agent port to 2000:

switch(config)# snmp-server agent-port 2000

Resetting the SNMP master agent port to the default value:

switch(config-schedule)# no snmp-server agent-port 2000

snmp-server community

Syntax

snmp-server community <STRING>

no snmp-server community <STRING>

Description

Adds an SNMPv1/SNMPv2c community string. A community string is a password that controls read access to
the SNMP agent. A network management program must supply this name when attempting to get SNMP
information from the switch. A maximum of 10 community strings are supported. Once you create your own
community string, the default community string (public) is deleted.

The no form of this command removes the specified SNMPv1/SNMPv2c community string. When no
community string exists, a default community string with the value public is automatically defined.

Command context

config

16

AOS-CX 10.06 SNMP/MIB Guide

Parameters
<STRING>

Specifies the SNMPv1/SNMPv2c community string. Range: 1 to 32 printable ASCII characters, excluding
space and question mark.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the SNMPv1/SNMPv2c community string to private:

switch(config)# snmp-server community private

Removing SNMPv1/SNMPv2c community string private:

switch(config)# no snmp-server community private

snmp-server historical-counters-monitor

Syntax

snmp-server historical-counters-monitor

no snmp-server historical-counters-monitor

Description

Enables the Remote Network Monitoring agent (rmond) to start collecting historical interface statistics. The
no form of this command stops the historical interface statistics collection.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Enabling the rmond agent to start historical interface statistics collection:

switch(config)# snmp-server historical-counters-monitor

Disabling the rmond agent to stop historical interface statistics collection:

switch(config)# no snmp-server historical-counters-monitor

snmp-server host

Syntax

snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

Chapter 2 SNMP

17

snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user <NAME>
[port <UDP-PORT>] [<VRF-NAME>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user <NAME>
[port <UDP-PORT>] [<VRF-NAME>]

Description

Configures a trap/informs receiver to which the SNMP agent can send SNMP v1/v2c/v3 traps or v2c informs.
A maximum of 30 SNMP traps/informs receivers can be configured.

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

18

AOS-CX 10.06 SNMP/MIB Guide

Examples

switch(config)# snmp-server host 10.10.10.10 trap version v1
switch(config)# no snmp-server host 10.10.10.10 trap version v1

switch(config)# snmp-server host a:b::c:d trap version v1
switch(config)# no snmp-server host a:b::c:d trap version v1

switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public

switch(config)# snmp-server host a:b::c:d trap version v2c community public
switch(config)# no snmp-server host a:b::c:d trap version v2c community public

switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port 5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public port 5000

switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port 5000 vrf default

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public port 5000 vrf default

switch(config)# snmp-server host a:b::c:d trap version v2c community public port 5000
switch(config)# no snmp-server host a:b::c:d trap version v2c community public port 5000

switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public

switch(config)# snmp-server host a:b::c:d inform version v2c community public
switch(config)# no snmp-server host a:b::c:d inform version v2c community public

switch(config)# snmp-server host 10.10.10.10 inform version v2c community public port 5000
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public port 5000

switch(config)# snmp-server host 10.10.10.10 inform version v2c community public port 5000 vrf default

switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public port 5000 vrf default

switch(config)# snmp-server host a:b::c:d inform version v2c community public port 5000
switch(config)# no snmp-server host a:b::c:d inform version v2c community public port 5000

switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin

switch(config)# snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin

switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port 2000

switch(config)# snmp-server host a:b::c:d trap version v3 user Admin port 2000
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin port 2000

snmp-server system-contact

Syntax

snmp-server system-contact <INFO>

no snmp-server system-contact [<INFO>]

Description

Sets SNMP contact information.

The no form of this command removes the SNMP contact information.

Command context

config

Chapter 2 SNMP

19

Parameters
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

• Hardware type of the system

• Software operating system

• Networking software

Range: 1 to 64 printable ASCII characters, except for the question mark (?).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the SNMP system description to be mainSwitch:

switch(config)# snmp-server system-description mainSwitch

20

AOS-CX 10.06 SNMP/MIB Guide

Removes the SNMP system description:

switch(config)# no snmp-server system-description mainSwitch

snmp-server system-location

Syntax

snmp-server system-location <INFO>

no snmp-server system-location

Description

Sets the SNMP location information.

The no form of this command removes the SNMP location information.

Command context

config

Parameters
<INFO>

Specifies the SNMP location information. Range: 1 to 128 printable ASCII characters, except for the
question mark (?).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the SNMP location information to be Main Lab:

switch(config)# snmp-server system-location Main Lab

Removes the SNMP location information:

switch(config)# no snmp-server system-location

snmp-server vrf

Syntax

snmp-server vrf <VRF-NAME>

no snmp-server vrf <VRF-NAME>

Description

Configures a VRF on which the SNMP agent listens for incoming requests. By default, the SNMP agent does
not listen on any VRF. 6100 only supports default VRF. The SNMP agent can listen on multiple VRFs.

The no form of this command stops the SNMP agent from listening for incoming requests on the specified
VRF.

Command context

config

Chapter 2 SNMP

21

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

snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf <VRF-NAME>]

no snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf <VRF-NAME>]

Description

Configures SNMP trap source interface or IP address for a VRF.

The no form of this command removes the SNMP trap-source configuration for a VRF.

Command context

config

Parameters
<IF-NAME>

Specifies the source interface name. Interface name can be physical interface, loopback interface, LAG
interface, or VLAN interface.

<IPv4-Address>

Specifies the IPv4 address of source interface for the SNMP trap.

<IPv6-Address>

Specifies the IPv6 address of source interface for the SNMP trap.

<VRF-NAME>

Specifies the name of a VRF associated to the source interface for the SNMP trap.

22

AOS-CX 10.06 SNMP/MIB Guide

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

snmpv3 context

Syntax

snmpv3 context <NAME> vrf <VRF-NAME> [community <STRING>]

no snmpv3 context <NAME> [vrf <VRF-NAME>]

Description

Creates an SNMPv3 context on the specified VRF.

The no form of this command removes the specified SNMP context.

Command context

config

Parameters
<NAME>

Specifies the name of the context. Range: 1 to 32 printable ASCII characters, excluding space and
question mark (?).

vrf <VRF-NAME>

Specifies the VRF associated with the context. Default: default.

community <STRING>

Specifies the SNMP community string associated with the context. Range: 1 to 32 printable ASCII
characters, excluding space and question mark. Default: public.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating an SNMPv3 context named newContext:

switch(config)# snmpv3 context newContext

Creating an SNMPv3 context named newContext on VRF myVrf and with community string private.

switch(config)# snmpv3 context newContext vrf myVrf community private

Chapter 2 SNMP

23

Removing the SNMPv3 context named newContext on VRF myVrf:

switch(config)# no snmpv3 context newContext vrf myVrf

snmpv3 engine-id

Syntax

snmpv3 engine-id <ENGINE-ID>

no snmpv3 engine-id <ENGINE-ID>

Description

Configures the SNMPv3 SNMP engine-id allowing an administrator to configure a unique SNMP engine-id for
the switch. This engine-id is used by the NMS management tool to identify and distinguish multiple switches
on the same network.

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
  WORD  SNMPv3 snmp engine-id in colon seperated hexadecimal notation
switch(config)# snmpv3 engine-id 01:23:45:67:89:ab:cd:ef:01:23:45:67

Restoring the default SNMPv3 engine-id:

switch(config)# no snmpv3 engine-id

snmpv3 security-level

Syntax

snmpv3 security-level {auth | auth-privacy}

no snmpv3 security-level {auth | auth-privacy}

Description

Configures the SNMPv3 security level. The security level determines which SMNPv3 users defined by the
command snmpv3 user are able to connect.

The no form of this command changes the security level as follows:

24

AOS-CX 10.06 SNMP/MIB Guide

• no snmpv3 security-level auth: Sets the security level to auth-privacy.

• no snmpv3 security-level auth-privacy: Sets the security level to no authentication or privacy,

allowing any SNMP user to connect.

Command context

config

Parameters
auth

SNMPv3 users that support authentication, or authentication and privacy are allowed.

auth-privacy

Only SNMPv3 users with both authentication and privacy are allowed. This is the highest level of SNMPv3
security. Default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the SNMPv3 security level to authentication and privacy:

switch(config)# snmpv3 security-level auth-privacy

Setting the SNMPv3 security level to authentication only:

switch(config)# snmpv3 security-level auth

Setting the SNMPv3 security level to no authentication and no privacy:

switch(config)# no snmpv3 security-level auth-privacy

Restoring the default SNMPv3 security level to authentication and privacy:

switch(config)# no snmpv3 security-level auth

snmpv3 user

Syntax

snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass {plaintext | ciphertext}
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass {plaintext | ciphertext} <PRIV-PWORD>] ]

no snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass <PRIV-PWORD>] ]

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context. The no form of this command removes the
specified SNMPv3 user.

For more details on the user enabled status, see snmpv3 security-level.

Command context

config

Chapter 2 SNMP

25

Parameters
<NAME>

Specifies the SNMPv3 username. Range 1 to 32 printable ASCII characters, excluding space and question
mark (?).

auth <AUTH-PROTOCOL>

Specifies the authentication protocol used to validate user logins. Available options are: md5 or sha.

auth-pass {plaintext | ciphertext} <AUTH-PWORD>

Specifies the SNMPv3 user password. Range for plaintext is 8 to32 printable ASCII characters,
excluding space and question mark (?).

Range for ciphertext is 1 to 120 printable ASCII characters. This option is only used when copying user
configuration settings between switches. It enables you to duplicate a user's configuration on another
switch without having to know their password.

priv <PRIV-PROTOCOL>

Specifies the SNMPv3 security protocol (encryption method). Available options are: aes or des.

priv-pass {plaintext | ciphertext} <PRIV-PWORD>

Specifies the SNMPv3 user privacy passphrase. Range for plaintext is 8 to 32 printable ASCII
characters, excluding space and question mark (?).

Range for ciphertext is 1 to 120 printable ASCII characters. This option is only used when copying user
configuration settings between switches. It enables you to duplicate a user's configuration on another
switch without having to know their password.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password mypassword
and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des priv-pass plaintext myprivpass

Removing an SNMPv3 user named Admin:

switch(config)# no snmpv3 user Admin

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password mypassword
and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des priv-pass plaintext myprivpass

Copying an SNMP user from switch 1 to switch 2.

On switch 1, configure a user called Admin, then issue the show running-config command to display
switch configuration settings. The snmpv3 user command uses the ciphertext option to protect the
users's passwords.

switch1(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword
priv des priv-pass plaintext myprivpass
switch1(config)# exit
switch1# show running-config
Current configuration:
!
!Version ArubaOS-CX XL.10.04.0001AD
!
!
!

26

AOS-CX 10.06 SNMP/MIB Guide

snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
priv des priv-pass ciphertext AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
ssh server vrf mgmtdefault
!
!
!
!
interface mgmtinterface vlan 1
    no shutdown
    ip dhcp
vlan 1

On switch 2, execute the snmpv3 user command that was displayed by show running-config on switch
1. This creates the user on switch 2 with the same configuration settings.

switch1(config)# snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
priv des priv-pass ciphertext AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=

Chapter 2 SNMP

27

Chapter 3
Entity MIB support

The Entity MIB, rfc 6933, allows network managers to retrieve physical containment and logical relationships
for devices in the network. The entconfigChange trap is sent to configured SNMP-server hosts when a
change occurs. The trap is configured to send notifications no more than once every 5 seconds. We will be
supporting the Entity MIB for read-only.

Physical components that are supported include:

• Chassis

•

•

•

•

Fabric cards

Fan trays

Fans

Line cards and their interfaces

• Management modules and the intake temperature sensor

• Power supplies

The slots for any removable component are also represented.

The logical table of the Entity MIB represents configured VLANs and the associated ports.

entConfigChange trap/notification is sent to configurated snmp-server hosts.

Location of the MIB files on the web
The MIB files for Aruba switches can be found on the Aruba Service Portal. You can apply the various filters
to filter by product series, software versions, and software release types.

Newly introduced MIBs and Traps for 10.06
The following table contains the newly introduced MIBs and Traps for each software feature. Software is
provided along with the MIB and Traps supported name.

28

AOS-CX 10.06 SNMP/MIB Guide

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

Networkin
g OID

ARUBAWIRED-
NETWORKING-OID

arubaWiredSwitchJL675A

N

NA

arubaWiredSwitchJL676A

arubaWiredSwitchJL677A

arubaWiredSwitchJL678A

arubaWiredSwitchJL679A

arubaWiredSwitchModuleJL675A

arubaWiredSwitchModuleJL676A

arubaWiredSwitchModuleJL677A

arubaWiredSwitchModuleJL678A

arubaWiredSwitchModuleJL679A

arubaWiredSwitchJL717A

arubaWiredSwitchJL718A

arubaWiredSwitchJL719A

arubaWiredSwitchJL720A

arubaWiredSwitchJL721A

arubaWiredSwitchJL722A

arubaWiredSwitchModuleJL717A

arubaWiredSwitchModuleJL718A

arubaWiredSwitchModuleJL719A

arubaWiredSwitchModuleJL720A

arubaWiredSwitchModuleJL721A

arubaWiredSwitchModuleJL722A

arubaWiredSwitchNonPoEPowerSupplyU
nit

arubaWiredSwitchPoEPowerSupplyUnit

arubaWiredSwitch8360FanTraySlot

arubaWiredSwitch8360PowerSupplySlot

arubaWiredSwitchPowerSupplyUnitJL600
A

Chapter 3 Entity MIB support

Table Continued

29

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

arubaWiredSwitchPowerSupplyUnitJL601
A

arubaWiredSwitchPowerSupplyUnitJL712
A

arubaWiredSwitchPowerSupplyUnitJL713
A

arubaWiredSwitchFanTrayJL714A

arubaWiredSwitchFanTrayJL715A

arubaWiredSwitch36WPowerSupplyUnit

arubaWiredSwitch65WPowerSupplyUnit

arubaWiredSwitch165WPowerSupplyUnit

arubaWiredSwitch500WPowerSupplyUnit

MDNS

ARUBAWIRED-MDNS-MIB arubaWiredMdnsAdminState

N

NA

arubaWiredMdnsServicetable

arubaWiredMdnsServiceName

arubaWiredMdnsServiceIdIndex

arubaWiredMdnsServiceId

arubaWiredMdnsProfileTable

arubaWiredMdnsProfileName

arubaWiredMdnsProfileVIDList

arubaWiredMdnsProfilePermitCount

arubaWiredMdnsProfileDenyCount

arubaWiredMdnsProfileFilterRuleTabl
e

arubaWiredMdnsProfileFilterRuleProfileN
ame

arubaWiredMdnsProfileFilterRuleIndex

arubaWiredMdnsProfileFilterRuleService
Name

arubaWiredMdnsProfileFilterRuleInstanc
eName

30

AOS-CX 10.06 SNMP/MIB Guide

Table Continued

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

arubaWiredMdnsProfileFilterRuleAction

arubaWiredMdnsPortTable

arubaWiredMdnsPortVlanId

arubaWiredMdnsPortMdnsEnabled

arubaWiredMdnsPortTxProfileName

arubaWiredMdnsPortRxProfileName

arubaWiredMdnsServiceProviderTable

arubaWiredMdnsServiceProviderServiceI
d

arubaWiredMdnsServiceProviderServiceI
dIndex

arubaWiredMdnsServiceProviderServiceI
nstanceName

arubaWiredMdnsServiceProviderVlanId

arubaWiredMdnsServiceProviderMacAdd
ress

arubaWiredMdnsServiceProviderHostna
me

arubaWiredMdnsServiceProviderIpAddre
ss

arubaWiredMdnsServiceProviderTtl

arubaWiredMdnsServiceProviderExpireTi
me

Table Continued

Chapter 3 Entity MIB support

31

| Software | MIB files | Implemented MIB objects | Traps     | Traps list |
| -------- | --------- | ----------------------- | --------- | ---------- |
| feature  |           |                         | supported |            |
(Y/N)
| MSTP | ARUBAWIRED-MSTP-MIB | arubaWiredMstpBpduGuardTimeout | N   | NA  |
| ---- | ------------------- | ------------------------------ | --- | --- |
arubaWiredMstpPortTable
arubaWiredMstpPortIndex
arubaWiredMstpPortAdminEdge
arubaWiredMstpPortAdminPointToPoint
arubaWiredMstpPortAutoEdge
arubaWiredMstpPortBpduFiltering
arubaWiredMstpPortRestrictedTcn
arubaWiredMstpPortRootGuard
arubaWiredMstpPortLoopGuard
arubaWiredMstpPortBpduProtection
arubaWiredMstpPortRpvstProtection
arubaWiredMstpPortRpvstFiltering
RPVST ARUBAWIRED-RPVST-MIB arubaWiredRpvstBpduGuardTimeout N NA
Table Continued
| 32  |     | AOS-CX 10.06 SNMP/MIB Guide |     |     |
| --- | --- | --------------------------- | --- | --- |

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

VSFv2

ARUBAWIRED-VSFv2-MIB

arubaWiredVsfv2TrapEnable

Y

arubaWiredVsfv2SplitDetectConfigure
d

arubaWiredVsfv2OperStatus

arubaWiredVsfv2Topology

arubaWiredVsfv2StackMacAddr

arubaWiredVsfv2DomainId

arubaWiredVsfv2MemberTable

arubaWiredVsfv2MemberIndex

arubaWiredVsfv2MemberRole

arubaWiredVsfv2MemberStatus

arubaWiredVsfv2MemberPartNumber

arubaWiredVsfv2MemberMacAddr

arubaWiredVsfv2MemberProductName

arubaWiredVsfv2MemberSerialNum

arubaWiredVsfv2MemberBootImage

arubaWiredVsfv2MemberCpuUtil

arubaWiredVsfv2MemberMemoryUtil

arubaWiredVsfv2MemberBootTime

arubaWiredVsfv2MemberBootRomVersio
n

arubaWiredVsfv2MemberTotalMemory

arubaWiredVsfv2MemberCurrentUsage

arubaWiredVsfv2LinkTable

arubaWiredVsfv2LinkOperStatus

arubaWiredVsfv2LinkPeerMemberId

arubaWiredVsfv2LinkPeerLinkId

arubaWiredVsfv2LinkPortList

arubaWire
dVsfv2Me
mberStatu
sChange

arubaWire
dVsfv2Fra
gmentStat
usChange

Table Continued

Chapter 3 Entity MIB support

33

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

802.1X

IEEE8021-SECY-MIB.mib

ieee8021XPaePortTable

N

NA

secyIfInterfaceIndex

secyIfMaxPeerSCs

secyIfRxMaxKeys

secyIfRxMaxKeys

secyIfProtectFramesEnable

secyIfValidateFrames

secyIfReplayProtectEnable

secyIfReplayProtectWindow

secyIfCurrentCipherSuite

secyIfAdminPt2PtMAC

secyIfOperPt2PtMAC

secyIfIncludeSCIEnable

secyIfUseESEnable

secyIfUseSCBEnable

secyIfIncludingSCI

secyIfMaxTSCs

secyTxSCTable

secyTxSCI

secyTxSCState

secyTxSCEncodingSA

secyTxSCEncipheringSA

secyTxSCCreatedTime

secyTxSCStartedTime

secyTxSCStoppedTime

secyTxSATable

secyTxSAState

secyTxSANextPN

secyTxSAConfidentiality

34

AOS-CX 10.06 SNMP/MIB Guide

Table Continued

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

secyTxSASAKUnchanged

secyTxSACreatedTime

secyTxSAStartedTime

secyTxSAStoppedTime

secyRxSCTable

secyRxSCState

secyRxSCCurrentSA

secyRxSCCreatedTime

secyRxSCStartedTime

secyRxSCStoppedTime

secyRxSATable

secyRxSAState

secyRxSANextPN

secyRxSASAKUnchanged

secyRxSACreatedTime

secyRxSAStartedTime

secyRxSAStoppedTime

secyRxSANextXPN

secyRxSALowestXPN

secyRxSAKeyIdentifier

secyRxSASSCI

secyTxSAStatsTable

secyTxSAStatsProtectedPkts

secyTxSAStatsEncryptedPkts

secyRxSAStatsTable

secyRxSAStatsUnusedSAPkts

secyRxSAStatsNoUsingSAPkts

secyRxSAStatsNotValidPkts

secyRxSAStatsInvalidPkts

Chapter 3 Entity MIB support

Table Continued

35

Software
feature

MIB files

Implemented MIB objects

Traps list

Traps
supported
(Y/N)

secyRxSAStatsOKPkts

secyTxSCStatsTable

secyTxSCStatsProtectedPkts

secyTxSCStatsEncryptedPkts

secyTxSCStatsOctetsProtected

secyTxSCStatsOctetsEncrypted

secyRxSCStatsTable

secyRxSCStatsUnusedSAPkts

secyRxSCStatsNoUsingSAPkts

secyRxSCStatsLatePkts

secyRxSCStatsNotValidPkts

secyRxSCStatsInvalidPkts

secyRxSCStatsDelayedPkts

secyRxSCStatsUncheckedPkts

secyRxSCStatsOKPkts

secyStatsTable

secyStatsTxUntaggedPkts

secyStatsTxTooLongPkts

secyStatsRxUntaggedPkts

secyStatsRxNoTagPkts

secyStatsRxBadTagPkts

secyStatsRxUnknownSCIPkts

secyStatsRxNoSCIPkts

secyStatsRxOverrunPkts

Q-BRIDGE Q-Bridge.mib

dot1qFdbTable

N

NA

dot1qFdbId

dot1qFdbDynamicCount

dot1qTpFdbTable

dot1qTpFdbAddress

36

AOS-CX 10.06 SNMP/MIB Guide

| Software | MIB files | Implemented MIB objects | Traps     | Traps list |
| -------- | --------- | ----------------------- | --------- | ---------- |
| feature  |           |                         | supported |            |
(Y/N)
dot1qTpFdbPort
dot1qTpFdbStatus
Chapter 3 Entity MIB support 37

Chapter 4
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

• Technical support registration number (if applicable)

• Product name, model or version, and serial number

• Operating system name and version

•

Firmware version

• Error messages

• Product-specific reports and logs

• Add-on products or components

• Third-party products or components

Other useful sites

Other websites that can be used to find information:

Airheads social forums and
Knowledge Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and
documentation

https://asp.arubanetworks.com/downloads

Accessing updates
To download product updates:

38

AOS-CX 10.06 SNMP/MIB Guide

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My Networking,
where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to the
Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

https://support.hpe.com/portal/site/hpsc/aae/home/

IMPORTANT: Access to some updates might require product entitlement when accessed
through the Hewlett Packard Enterprise Support Center. You must have an HP Passport set up
with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal
(ASP) account to manage subscriptions). Security notices are viewable without an ASP account.

Warranty information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory information
To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs, product
recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For more
information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

Chapter 4 Support and other resources

39