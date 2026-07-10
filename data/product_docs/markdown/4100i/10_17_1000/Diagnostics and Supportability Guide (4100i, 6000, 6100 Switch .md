AOS-CX 10.17.xxxx Diagnostics and Supportability Guide (4100i,
6000, 6100 Switch series)

Published: February 2026

AOS-CX 10.17.xxxx Diagnostics and Supportability Guide (4100i,
6000, 6100 Switch series)

Published: February 2026

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

AOS-CX 10.17.xxxx Diagnostics and Supportability G...

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
7
.
x
x
x
x

D
i
a
g
n
o
s
t
i
c
s

a
n
d

S
u
p
p
o
r
t
a
b
i
l
i
t
y

G
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.17.xxxx Diagnostics and Supportability G...

Table of contents

About this document..................................................................................................................................................................................9

Applicable products........................................................................................................................................................................9

What's new in this release...........................................................................................................................................................9

Latest version available online..............................................................................................................................................10

Command syntax notation conventions..........................................................................................................................10

About the examples.................................................................................................................................................................... 12

Identifying switch ports and interfaces........................................................................................................................... 12

Debug logging.............................................................................................................................................................................................13

Debug logging commands.......................................................................................................................................................13

Debug logging commands..........................................................................................................................................14

clear debug buffer ............................................................................................................................................. 14

debug {all | <MODULE-NAME>} ...............................................................................................................15

debug db .................................................................................................................................................................17

debug destination ............................................................................................................................................. 20

diag event-trap-disable ..................................................................................................................................22

show debug ...........................................................................................................................................................23

show debug buffer ............................................................................................................................................ 24

show debug destination .................................................................................................................................26

Log Rotation.................................................................................................................................................................................................27

Log file paths...................................................................................................................................................................................27

About rotated log files...............................................................................................................................................................28

Changing the size of the log rotation file........................................................................................................................28

Changing the time frequency for log rotation............................................................................................................. 28

Resetting the time frequency to daily.............................................................................................................................. 29

Identifying a remote host for receiving rotated log files....................................................................................... 29

Remote transfer of rotated log files...................................................................................................................................30

Resetting the remote host for receiving rotated log files..................................................................................... 30

Resetting the size of the log rotation file....................................................................................................................... 31

Verifying the log rotation parameters.............................................................................................................................. 31

Log rotation troubleshooting.................................................................................................................................................31

Log files not transferred remotely......................................................................................................................... 32

Log rotation not occurring immediately after max file size.................................................................... 32

Log rotation not occurring regardless of period............................................................................................32

Log rotation commands............................................................................................................................................................33

Public

Table of contents 4

Log rotation commands............................................................................................................................................... 33

logging threshold ...............................................................................................................................................33

logrotate maxsize ...............................................................................................................................................35

logrotate period .................................................................................................................................................. 36

logrotate target ...................................................................................................................................................38

show logrotate .....................................................................................................................................................39

Event Logs.....................................................................................................................................................................................................40

Showing and clearing events................................................................................................................................................. 40

Client Filter.................................................................................................................................................................................................... 41

Log messages................................................................................................................................................................................. 41

Cable Diagnostics...................................................................................................................................................................................... 41

How TDR works on platforms............................................................................................................................................... 42

Cable diagnostics tests..............................................................................................................................................................42

Cable diagnostic commands...................................................................................................................................................44

diag cable-diagnostic ................................................................................................................................................... 44

Supportability Copy..................................................................................................................................................................................47

Supportability copy commands............................................................................................................................................48

copy checkpoint ...............................................................................................................................................................49

copy command-output ................................................................................................................................................50

copy diag-dump feature <FEATURE> ................................................................................................................52

copy diag-dump local-file .......................................................................................................................................... 53

copy <IMAGE> ..................................................................................................................................................................55

copy running-config ......................................................................................................................................................57

copy show-tech feature ...............................................................................................................................................58

copy show-tech local-file ............................................................................................................................................60

copy startup-config .......................................................................................................................................................61

copy support-files ...........................................................................................................................................................63

copy support-files local-file ...................................................................................................................................... 65

copy support-log .............................................................................................................................................................67

Traceroute......................................................................................................................................................................................................69

Traceroute commands............................................................................................................................................................... 69

traceroute ............................................................................................................................................................................69

traceroute6 .........................................................................................................................................................................72

Ping....................................................................................................................................................................................................................75

Ping commands..............................................................................................................................................................................75

Ping commands.................................................................................................................................................................75

ping ............................................................................................................................................................................ 75

ping6 ......................................................................................................................................................................... 82

Public

Table of contents 5

Troubleshooting................................................................................................................................................................86

Operation not permitted.................................................................................................................................86

Network is unreachable...................................................................................................................................87

Destination host unreachable......................................................................................................................87

Troubleshooting............................................................................................................................................................................ 88

Operation not permitted..............................................................................................................................................88

Network is unreachable................................................................................................................................................89

Destination host unreachable...................................................................................................................................89

Using classifier policies for traffic capture and analysis..................................................................................................... 90

Remote syslog............................................................................................................................................................................................. 97

Remote syslog commands.......................................................................................................................................................97

clear accounting-logs ................................................................................................................................................... 97

diag persistent-storage ...............................................................................................................................................99

logging ............................................................................................................................................................................... 101

logging accounting-format-native .....................................................................................................................104

logging filter ................................................................................................................................................................... 105

logging facility ...............................................................................................................................................................109

logging persistent-storage .....................................................................................................................................110

Runtime Diagnostics.............................................................................................................................................................................112

Runtime diagnostic commands......................................................................................................................................... 112

diagnostic monitor ......................................................................................................................................................113

diag on-demand ........................................................................................................................................................... 114

show diagnostic ............................................................................................................................................................115

show diagnostic events ............................................................................................................................................118

Service OS...................................................................................................................................................................................................119

Service OS CLI login ................................................................................................................................................................120

Service OS user accounts......................................................................................................................................................122

Service OS boot menu.............................................................................................................................................................122

Console configuration............................................................................................................................................................. 123

AOS-CX boot................................................................................................................................................................................ 123

File system access..................................................................................................................................................................... 124

Service of OS mount failure................................................................................................................................................. 125

Service OS CLI command list .............................................................................................................................................125

Service OS CLI features and limitations........................................................................................................................126

Service OS CLI commands....................................................................................................................................................127

boot ......................................................................................................................................................................................128

cat ......................................................................................................................................................................................... 129

cd path ............................................................................................................................................................................... 130

Public

Table of contents 6

config-clear ..................................................................................................................................................................... 131

cp ...........................................................................................................................................................................................132

du .......................................................................................................................................................................................... 133

erase zeroize ...................................................................................................................................................................135

exit ........................................................................................................................................................................................136

format .................................................................................................................................................................................137

identify ...............................................................................................................................................................................138

ls ............................................................................................................................................................................................ 139

md5sum .............................................................................................................................................................................141

mkdir ................................................................................................................................................................................... 142

mount ................................................................................................................................................................................. 143

mv ......................................................................................................................................................................................... 144

password (svos) ............................................................................................................................................................145

pwd ...................................................................................................................................................................................... 146

reboot ................................................................................................................................................................................. 147

rm ..........................................................................................................................................................................................148

rmdir ....................................................................................................................................................................................149

secure-mode ...................................................................................................................................................................150

sh ...........................................................................................................................................................................................152

system serviceos password-prompt ................................................................................................................. 153

umount ...............................................................................................................................................................................153

update ................................................................................................................................................................................ 155

tftp ........................................................................................................................................................................................156

version ................................................................................................................................................................................158

In-System Programming.....................................................................................................................................................................159

Show tech command list for the ISP feature..............................................................................................................159

In-System Programming commands...............................................................................................................................159

clear update-log ........................................................................................................................................................... 159

show needed-updates .............................................................................................................................................. 160

Selftest..........................................................................................................................................................................................................161

Selftest commands....................................................................................................................................................................161

fastboot ............................................................................................................................................................................. 161

show selftest ...................................................................................................................................................................164

Zeroization..................................................................................................................................................................................................166

Zeroization commands........................................................................................................................................................... 167

erase all zeroize ............................................................................................................................................................ 167

Terminal Monitor.....................................................................................................................................................................................169

Terminal monitor commands.............................................................................................................................................. 170

Public

Table of contents 7

logging console {notify | severity | filter} .......................................................................................................170

show terminal-monitor ............................................................................................................................................. 172

terminal-monitor {notify | severity | filter} ....................................................................................................173

Troubleshooting Web UI and REST API Access Issues.....................................................................................................174

HTTP 404 error when accessing the switch URL.................................................................................................. 174

HTTP 401 error "Login failed: session limit reached".......................................................................................... 175

Support and Other Resources.........................................................................................................................................................176

Accessing HPE Aruba Networking Support...............................................................................................................176

Accessing Updates....................................................................................................................................................................177

Warranty Information.............................................................................................................................................................. 178

Regulatory Information.......................................................................................................................................................... 178

Documentation Feedback.....................................................................................................................................................178

Public

Table of contents 8

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Applicable products
What's new in this release
Latest version available online
Command syntax notation conventions
About the examples
Identifying switch ports and interfaces

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

•  HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A,

S4R20A, S4R21A, S4R22A, S4R23A, S4R24A, S4R25A, S4R26A, S4R27A, S4R28, S4R29A)

•  HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

What's new in this release

The following commands were added or modified in AOS-CX 10.17.xxxx.

NOTE

For more information on new features introduced see the HPE Aruba
Networking Airheads Broadcasting channel on Youtube.

Public

About this document 9

Commands introduced or modified in 10.17.1000

Command

Description

The ipfix protocol parameter was introduced on 410
0i, 6000, and 6100 Switch Series.

Monitoring commands introduced on 4100i, 6000, a
nd 6100 Switch Series.

Command introduced on 4100i, 5420, 6000, 6100,
6200, 6300, and 6400 Switch Series. This command
allows application based policies (ABP) to use secure
updates by default.

Command introduced on 4100i, 5420, 6000, 6100,
6200, 6300, and 6400 Switch Series. This command
allows group based policies (GBP) to use secure upd
ates by default.

Command introduced on 4100i, 5420, 6000, 6100,
6200, 6300, and 6400 Switch Series. This command
allows port-access policies to use secure updates by
default.

Command introduced that enables the system to d
etect and prevent loops using LLDP neighbor inform
ation.

Physical memory, reserved memory, used memory, an
d free memory usage fields were added.

show system resource-utilization

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Public

Latest version available online 10

Convention

example‐text

example‐text

Any of the following:

•  <example‐text>
•  <example‐text>
•  example‐text
•  example‐text

|

{ }

[ ]

… or

...

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

In code and screen examples, indicates text entered
by a user.

Identifies a placeholder—such as a parameter or a va
riable—that you must substitute with an actual valu
e in a command or in code:

•  For output formats where italic text cannot be di
splayed, variables are enclosed in angle brackets
(< >). Substitute the text—including the enclosin
g angle brackets—with an actual value.

•  For output formats where italic text can be displ
ayed, variables might or might not be enclosed i
n angle brackets. Substitute the text including th
e enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple ite
ms from which you can choose only one.

Any spaces that are on either side of the vertical bar
are included for readability and are not a required pa
rt of the command syntax.

Braces. Indicates that at least one of the enclosed ite
ms is required.

Brackets. Indicates that the enclosed item or items a
re optional.

Ellipsis:

•

•

In code and screen examples, a vertical or horizo
ntal ellipsis indicates an omission of information.
In syntax using brackets and braces, an ellipsis i
ndicates items that can be repeated. When an ite
m followed by ellipses is enclosed in brackets, ze
ro or more items can be specified.

Public

Command syntax notation conventions 11

About the examples

Examples in this document are representative and might not match your particular switch or environment.

The slot and port numbers in this document are for illustration only and might be unavailable on your switch.

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

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 4100i Switch Series

•  member: Always 1. VSF is not supported on this switch.

Public

About the examples 12

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

Debug logging

The debug logging framework provides an improved, customizable, and conditional logging framework with
feature and entity based filtering options. Debug logging is a verbose, on-demand logging mechanism which
customers and support can enable in order to obtain more information that will assist with troubleshooting.

Each debug logging event has both a Severity and a Module. Customers/support are required to enable a
given Module in order to have those events logged. The log operation is not run when a Module is not
enabled. All debug log events classified with a Severity of Error and above will always be logged. This
ensures that both support and customers will be able to see these important events even when their
respective debug log Module isn’t enabled.

NOTE

Debug logging is disabled by default.

Subtopics

Debug logging commands

Debug logging commands

Subtopics

Debug logging commands

Public

Debug logging 13

Debug logging commands

Select a command from the list in the left navigation menu.

Subtopics

clear debug buffer
debug {all | <MODULE-NAME>}
debug db
debug destination
diag event-trap-disable
show debug
show debug buffer
show debug destination

clear debug buffer

Syntax

clear debug buffer

Description

Clears all debug logs. Using the show debug buffer command will only display the logs generated after the
clear debug buffer command.

Examples

Clearing all generated debug logs:

switch# show debug buffer

----------------------------------------------------------------------------

----------------------------------
show debug buffer

----------------------------------------------------------------------------

----------------------------------

2018-10-14:09:10:58.558710|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_CONFIG|No Port

cfg changes

2018-10-14:09:10:58.558737|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_EVENT|

lldpd_stats_run entered at time 8257199

2018-10-14:09:10:58.569317|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_CONFIG|No Port

cfg changes

2018-10-14:09:11:21.881907|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|

Sysmon poll interval changed to 32

Public

Debug logging commands 14

switch# clear debug buffer

switch# show debug buffer

----------------------------------------------------------------------------

----------------------------------

show debug buffer

----------------------------------------------------------------------------

----------------------------------

2018-10-14:09:13:24.481407|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|

Sysmon poll interval changed to 51

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

debug {all | <MODULE-NAME>}

Syntax

debug {all | <MODULE-NAME>} [<SUBMODULE-NAME>] [severity
   (emer|crit|alert|err|notice|warning|info|debug)] {port <PORT-NAME> |

    vlan <VLAN-ID> | ip <IP-ADDRESS> | mac <MAC-ADDRESS> |

    vrf <VRF-NAME> | instance <INSTANCE-ID>}

no debug {all | <MODULE-NAME>} [<SUBMODULE-NAME>] {port | vlan | ip | mac |

    vrf | instance}

Description

Enables debug logging for modules or submodules by name, with optional filtering by specific criteria.

The no form of this command disables debug logging.

Public

debug {all | <MODULE-NAME>} 15

Parameter

 all

Description

Enables debug logging for all modules.

<MODULE‐NAME>

<SUBMODULE‐NAME>

severity (emer|crit|alert|

err|

  notice|warning|info|

debug)

emer

crit

alert

err

notice

warning

info

debug

port

Enables debug logging for a specific module. For a list of suppo
rted modules, enter the debug command followed by a space a
nd a question mark (?).

Enables debug logging for a specific submodule. For a list of s
upported submodules, enter the debug <MODULE‐NAME> co
mmand followed by a space and a question mark (?).

Selects the minimum severity log level for the destination. If a s
everity is not provided, the default log level is debug. Optional.

Specifies storage of debug logs with a severity level of emerge
ncy only.

Specifies storage of debug logs with severity level of critical an
d above.

Specifies storage of debug logs with severity level of alert and
above.

Specifies storage of debug logs with severity level of error and
above.

Specifies storage of debug logs with severity level of notice and
above.

Specifies storage of debug logs with severity level of warning a
nd above.

Specifies storage of debug logs with severity level of info and a
bove.

Specifies storage of debug logs with severity level of debug (de
fault).

Displays debug logs for the specified port, for example 1/1/1.

vlan <VLAN‐ID>

Displays debug logs for the specified VLAN. Provide a VLAN f
rom 1 to 4094.

Public

debug {all | <MODULE-NAME>} 16

Parameter

Description

ip <IP‐ADDRESS>

Displays debug logs for the specified IP Address.

mac <MAC‐ADDRESS>

Displays debug logs for the specified MAC Address, for example
A:B:C:D:E:F.

vrf <VRF‐NAME>

Displays debug logs for the specified VRF.

instance <INSTANCE‐ID>

Displays debug logs for the specified instance. Provide an insta
nce ID from 1 to 255.

Examples

switch# debug all

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

debug db

Syntax

debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]

no debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]

Description

Enables or disables debug logging for a db module or submodules, with an option to filter by specific criteria.

The no form of this command disables debug logging for the db module or submodule.

Public

debug db 17

Parameter

all

sub‐module

filter

severity (emer|crit|alert|

err|

  notice|warning|info|

debug)

emer

crit

alert

err

notice

warning

info

debug

Usage

Description

Enables all submodules for the db log.

Enables debug logging for supported submodules. Specify rx or
tx debug logs.

Specifies supported filters for the db log. Specify table, column,
or client. Optional

Selects the minimum severity log level for the destination. If a s
everity is not provided, the default log level is debug. Optional.

Specifies storage of debug logs with a severity level of emerge
ncy only.

Specifies storage of debug logs with severity level of critical an
d above.

Specifies storage of debug logs with severity level of alert and
above.

Specifies storage of debug logs with severity level of error and
above.

Specifies storage of debug logs with severity level of notice and
above.

Specifies storage of debug logs with severity level of warning a
nd above.

Specifies storage of debug logs with severity level of info and a
bove.

Specifies storage of debug logs with severity level of debug (de
fault).

DBlog is a high performance, configuration, and state database server logging infrastructure where a user
can log the transactions which are sent or received by clients to the configuration and state database server.
It can be enabled through the CLI and REST, and also supports filters where a user can filter out logs on the
basis of table, column, or client. It is helpful for debugging when the user wants to debug an issue with a
particular client, table, or column combination. It is not enabled by default. A combination of filters can also
be applied to filter out messages based on table, column, and client.

Public

debug db 18

There are three submodules for the "db" module:

1.  all: When All is enabled, no filters are applied to any of the debug logs, even if other submodules are

configured with filters.

2.  tx: If enabled, only the replies and notifications sent out for the initial and incremental updates are

logged.

3.  rx: If enabled, only the transactions sent to the configuration and state database server are logged.

The keyword all may be used to enable or disable debug logging for all sub-modules. Also a combination of
filters can be used to filter the message types.

If the table or client filter is applied, then the messages belonging to this specific table or client will be
logged. The column filter can also be applied to further filter messages on a table, providing a mechanism to
filter messages on a column. The table and client filter can be used in combination or separately, but column
can only be used in conjunction with table.

Examples

Configuring all submodules with severity debug:

switch# debug db all severity debug

Configuring the tx submodule with table Interface filter and severity debug:

switch# debug db tx table Interface severity debug

Configuring the rx submodule with table Interface column statistics filter and severity debug:

switch# debug db rx table Interface column statistics severity debug

Disabling the rx submodule:

switch# no debug db rx

Disabling the tx submodule table Interface:

switch# no debug db tx table Interface

Command History

Release

Modification

10.07 or earlier

‐‐

Public

debug db 19

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

debug destination

Syntax

debug destination {syslog | file | console | buffer} [severity (emer|crit|

alert|err|notice|warning|info|debug)]

no debug destination {syslog | file | console}

Description

Sets the destination for debug logs and the minimum severity level for each destination

The no form of this command unsets the destination for debug logs.

Parameter

Description

{syslog | file | console |

Selects the destination to store debug logs. Required.

buffer}

syslog

file

console

buffer

severity (emer|crit|alert|

err|

  notice|warning|info|

debug)

emer

Specifies that the debug logs are stored in the syslog.

Specifies that debug logs are stored in file.

Specifies that debug logs are stored in console.

Specifies that debug logs are stored in buffer (default).

Selects the minimum severity log level for the destination. If a s
everity is not provided, the default log level isdebug. Optional.

Specifies storage of debug logs with a severity level of emerge
ncy only.

Public

debug destination 20

Parameter

crit

alert

err

notice

warning

info

debug

Usage

Description

Specifies storage of debug logs with severity level of critical an
d above.

Specifies storage of debug logs with severity level of alert and
above.

Specifies storage of debug logs with severity level of error and
above.

Specifies storage of debug logs with severity level of notice and
above.

Specifies storage of debug logs with severity level of warning a
nd above.

Specifies storage of debug logs with severity level of info and a
bove.

Specifies storage of debug logs with severity level of debug (de
fault).

Events that have a severity equal to or higher than the configured severity level are stored in the designated
destination. The product defaults to buffer for destination and debug as a severity level.

Examples

switch# debug destination syslog severity alert

switch# debug destination console severity info

switch# debug destination file severity warning

switch# debug destination buffer severity err

Command History

Release

Modification

10.07 or earlier

‐‐

Public

debug destination 21

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

diag event-trap-disable

Syntax

diag event-trap-disable <EVENT-IDS>

no diag event-trap-disable <EVENT-IDS>

Description

Prevents the specific event notifications from being sent as traps to the SNMP management stations.

The no form of this command disables this feature and reenables the notification of events to be sent as
traps.

Parameter

<EVENT‐IDS>

Usage

Description

Specify up to five comma separated Event IDs

To modify the traps to be disabled, such as changing the existing list of event IDs or removing an event
ID from the blocked trap list, first completely remove previously configured disabled traps using the CLI
command no diag event-trap-disable <EVENT-ID>. After that, reconfigure the new event IDs or set of event
IDs for the changes to take effect.

The command to disable traps cannot be issued via network management systems such as SNMP, the
REST API, HPE Aruba Networking Fabric Composer or HPE Aruba Networking Central. The configuration to
disable event-traps is not persistent across reboots, and traps will be enabled again after the switch reboots.

NOTE
Do not disable default event trap IDs, as this can cause conflicts with a switch
configuration with default traps enabled.

Examples

Disable and then reenable event traps 1223 and 1224.

Public

diag event-trap-disable 22

switch# diagnostics

switch# diag event-trap-disable 1223,1224

switch# no diag event-trap-disable 1223,1224
Change the list of disabled event traps.

switch# diagnostics

switch# diag event-trap-disable 1223,1224

switch# no diag event-trap-disable 1223,1224

switch# diag event-trap-disable 1225,1226

Command History

Release

10.15.1010

Modification

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

show debug

Syntax

show debug

Description

Displays the enabled debug types.

Examples

switch# show debug
----------------------------------------------------------------------------
-------

module sub_module severity vlan port    ip        mac

instance  vrf

----------------------------------------------------------------------------

Public

show debug 23

-------

all     all          err    1   1/1/1   10.0.0.1  1a:2b:3c:4d:5e:6f

2         abcd

switch# show debug

----------------------------------------------------------------------------

--------

module sub_module severity vlan port   ip        mac

instance vrf

----------------------------------------------------------------------------

--------

all     all          err    1   1/1/1  10.0.0.1  1a:2b:3c:4d:5e:6f

2        default

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

show debug buffer

Syntax

show debug buffer [module <MODULE-NAME> | severity (emer|crit|alert|err|

notice|warning|info|debug)]

Description

Displays debug logs stored in the specified debug buffer with optional filtering by module or severity.

Public

show debug buffer 24

Parameter

Description

Filters debug logs displayed by the specified module name.

<MODULE‐NAME>

severity (emer|crit|alert|

err|

  notice|warning|info|

debug)

emer

crit

alert

err

notice

warning

info

debug

Examples

Displays debug logs with a specified severity level. Defaults tod
ebug. Optional.

Displays debug logs with a severity level of emergency only.

Displays debug logs with a severity level of critical and above.

Displays debug logs with a severity level of alert and above.

Specifies storage of debug logs with severity level of error and
above.

Specifies storage of debug logs with severity level of notice and
above.

Displays debug logs with a severity level of warning and above.

Displays debug logs with a severity level of info and above.

Displays debug logs with a severity level of debug (default).

switch# show debug buffer

----------------------------------------------------------------------------
--

show debug buffer

----------------------------------------------------------------------------

--

2017-03-06:06:51:15.089967|hpe-sysmond|SYSMON|SYSMON_CONFIG|LOG_INFO|Sysmon

poll interval changed to 20

Public

show debug buffer 25

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

show debug destination

Syntax

show debug destination

Description

Displays the configured debug destination and severity.

Examples

switch# show debug destination

---------------------------------------------------------------------

show debug destination

---------------------------------------------------------------------

 CONSOLE:info

 FILE:warning

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show debug destination 26

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Log Rotation

Log rotation provides you with the ability to systematically rotate and archive any log files produced by the
system. Log rotation reduces log space required on the switch. Log rotation rotates and compresses the log
files based on size and/or period. Rotated log files are stored locally or transferred to a remote host using
TFTP.

Optionally, notifications can be triggered if a log buffer percent full threshold is exceeded, giving you the
opportunity to save the logs elsewhere before the buffers are rotated with the oldest data being overwritten.

Subtopics

Log file paths
About rotated log files
Changing the size of the log rotation file
Changing the time frequency for log rotation
Resetting the time frequency to daily
Identifying a remote host for receiving rotated log files
Remote transfer of rotated log files
Resetting the remote host for receiving rotated log files
Resetting the size of the log rotation file
Verifying the log rotation parameters
Log rotation troubleshooting
Log rotation commands

Log file paths

Logs stored in the following files are rotated:

•  Audit logs are stored in file  /var/log/audit/audit.log .

•  Authentication logs are stored in file  /var/log/auth.log .

•  Event logs are stored in file  /var/log/event.log .

Public

Log Rotation 27

•  HTTPS server logs are stored in file  /var/log/nginx.log .

•  NTP logs are stored in file  /var/log/ntp.log .

•  Logs of bad login attempts are stored in  /var/log/btmp .

•  Logs of the last login sessions are stored in  /var/log/wtmp .

About rotated log files

Rotated log files are compressed and stored locally in  /var/log/ , regardless of the remote host
configuration. Rotated log files are stored with respective time extension to the granularity of hour in the
format  file1–YYYYMMDDHH.gz  (for example,  messages-2015080715.gz ). Rotated log files
are replaced when the number of old rotated log files exceeds three. The newly rotated log file replaces the
oldest rotated log file.

TFTP, SFTP, or SCP are used to transfer rotated log files to a remote host. Only newly rotated log files are
transferred to the remote host during the log rotation. Previously rotated log files are not re-transferred.
After a log file is successfully transferred, it is removed from the switch.

Changing the size of the log rotation file

By default, the product rotates the log files when the maximum file size exceeds 100 MB. When the size of
the log file exceeds the configured value, the rotation is triggered for that particular log file. Log rotation
does not occur immediately after the maximum file size for the log file is reached since the cron job runs with
an hourly periodicity.

logrotate maxsize <10-200 MB>
If you are planning to transfer the log rotation file by TFTP, set the log rotation file to no more than 32 MB.

Prerequisites

You must be in the configuration context:

switch(config)#

Changing the time frequency for log rotation

By default, the product rotates the log files daily. Enter the command at the configuration context in the CLI.

Prerequisites

You must be in the configuration context:

Public

About rotated log files 28

switch(config)#

Procedure

At the configuration context, enter:

logrotate period {daily | hourly | weekly | monthly }

daily: Rotates the log files daily. It is the default option.

hourly: Rotates the log files hourly.

weekly: Rotates the log files every week.

monthly: Rotates the log files every month.

Example command

switch(config)# logrotate period weekly

Resetting the time frequency to daily

Prerequisites

You must be in the configuration context:

switch(config)#

Procedure

At configuration context, enter the  no  form of the  logrotate period  command:

switch(config)# no logrotate period

Identifying a remote host for receiving rotated log files

You can send the rotated log files to a specified remote host Universal Resource Identifier (URI) by using the
TFTP protocol. If no URI is specified, the rotated and compressed log files are stored locally in  /var/log
/ . Only the TFTP protocol is supported for remote transfer, and the log rotation file cannot be more than 32
MB. Use the Linux TFTP command to transfer the file. Rotated log files are removed from the local path  /v
ar/log/  when it is moved to TFTP server.

Prerequisites

You must be in the configuration context:

switch(config)#

Public

Resetting the time frequency to daily 29

I
d
e
n
t
i
f
y
i
n
g

a

r
e
m
o
t
e

h
o
s
t

f
o
r

r
e
c
e
i
v
i
n
g

r
o
t
a
t
e
d

l
o
.
.
.

Procedure

Provide the target IP address (IPv4 or IPv6) at the configuration context in the CLI:

switch(config)# logrotate target {tftp://A.B.C.D | tftp://X:X::X:X}
IPv4 Example

switch(config)# logrotate target tftp://192.168.1.132
IPv6 Example

switch(config)# logrotate target tftp://2001:db8:0:1::128

Remote transfer of rotated log files

Only the TFTP protocol is supported for remote transfer, and both IPv4 and IPv6 addresses are supported.

Only newly rotated log files are transferred to the remote host during the log rotation. Previously rotated log
files are not transferred. After a file is successfully transferred, it is removed from the switch local path.

Packet level failures with TFTP are handled in the protocol itself. With each TFTP session failure, TFTP
retries the file transfer three times. Retries have a timeout of five seconds.

Resetting the remote host for receiving rotated log files

Prerequisites

You must be in the configuration context:

switch(config)#

Procedure

At configuration context, enter the  no  form of the  logrotate target  command:

switch(config)# no logrotate target
Example:

switch(config)# logrotate target tftp://1.1.1.1

switch(config)# do show logrotate

Logrotate configurations :

Period            : daily

Maxsize           : 10MB
Target            : tftp://1.1.1.1
switch(config)# no logrotate target

switch(config)# do show logrotate

Logrotate configurations :

Public

Remote transfer of rotated log files 30

R
e
s
e
t
t
i
n
g

t
h
e

r
e
m
o
t
e

h
o
s
t

f
o
r

r
e
c
e
i
v
i
n
g

r
o
t
a
t
e
d

l
o
.
.
.

Period            : daily

Maxsize           : 10MB

switch(config)#

Resetting the size of the log rotation file

Prerequisites

You must be in the configuration context:

switch(config)#

Procedure

At configuration context, enter the  no  form of the  logrotate maxsize  command:

switch(config)# no logrotate maxsize

Verifying the log rotation parameters

At the command prompt, enter:

switch# show logrotate
Example output

switch# show logrotate

Logrotate configurations :

Period            : daily

Maxsize           : 100MB

Target            : local

switch#

Log rotation troubleshooting

Some common log file rotation troubleshooting items are as follows.

Subtopics

Log files not transferred remotely
Log rotation not occurring immediately after max file size
Log rotation not occurring regardless of period

Public

Resetting the size of the log rotation file 31

Log files not transferred remotely

Symptom

Rotated log files are not transferred to a remote host.

Cause

•  The remote host might not be reachable.

•  The TFTP server on the remote host might not have sufficient privileges for file creation.

Action

1.  Verify that the remote host is reachable.

2.  Ensure that the TFTP server is configured with the required file creation permissions.

3.  For example, on the TFTPD-HPA server, change the configuration file in  /etc/default/tftpd-h
pa  to include  -c  in  TFTP_OPTIONS . (for example,  TFTP_OPTIONS="--secure -c .).

Log rotation not occurring immediately after max file size

Symptom

Log rotation does not occur immediately after the maximum file size for the log file is reached.

Cause

The log rotation checks the size of the file on the first minute of every hour. If the maximum file size is
reached in the meantime, the log rotation does not occur until the next hourly check of the file size.

Action

Log rotation is working as designed. The log rotation feature is designed to check the file size on an hourly
basis.

Log rotation not occurring regardless of period

Symptom

Log rotation is not happening regardless of the  period  value.

Public

Log files not transferred remotely 32

L
o
g

r
o
t
a
t
i
o
n

n
o
t

o
c
c
u
r
r
i
n
g

i
m
m
e
d
i
a
t
e
l
y

a
f
t
e
r

m
a
x

f
.
.
.

Cause

Log files are not rotated when they are empty files (the log file size is zero).

Action

Log rotation occurs when the log file size is greater than zero.

Log rotation commands

Subtopics

Log rotation commands

Log rotation commands

Select a command from the list in the left navigation menu.

Subtopics

logging threshold
logrotate maxsize
logrotate period
logrotate target
show logrotate

logging threshold

Syntax

logging threshold {audit-log | auth-log | commands-log |event-log |

             | https-server-log} <THRESHOLD%>

no logging threshold {audit-log | auth-log | commands-log | event-log |

             | https-server-log} [<THRESHOLD%>]

Description

Selects the logging buffer notification threshold for the specified logging buffer. Whenever the
logging buffer space consumption exceeds the selected threshold (percent of buffer capacity), a
LOG_BUFFER_ALMOST_FULL event and SNMP RMON trap is triggered. This gives you the opportunity
to save the logs elsewhere before the buffers are rotated with the oldest data being overwritten.

Public

Log rotation commands 33

Also, a LOG_BUFFER_WRAPPED event and SNMP RMON trap is triggered if the logging buffer capacity is
fully consumed and the log buffer is rotated with the oldest data being overwritten.

The no form of this command resets the logging buffer warning threshold to its default. All logs except
audit-log have a default of 90 (percent) and audit-log has a default of 50 (percent).

NOTE

The largest REST payload that can be sent to RADIUS/TACACS servers is 1024
characters, and the maximum REST payload that can be sent to syslog servers is
3500 characters. Once this limit is exceeded, the log will display three dots ( …) to
indicate the the message has exceeded the character limit and is incomplete. .

Parameter

audit‐log

auth‐log

commands‐log

event‐log

Description

Selects the audit log.

Selects the authentication log.

Configure the logging threshold for commands log buffer

Selects the event log.

https‐server‐log

Selects the HTTPS server log.

<THRESHOLD%>

Selects the notification threshold as a percent that the selected
logging buffer is full.

Available percent values for all logs except  audit‐log :  15
30 50 70 90 100

Available percent values for  audit‐log :  50 100

Examples

Setting the audit log threshold:

switch(config)# logging threshold audit-log 100

Setting the authentication log threshold:

switch(config)# logging threshold auth-log 50

Setting the event log threshold:

switch(config)# logging threshold event-log 70

Setting the HTTPS server log threshold:

Public

logging threshold 34

switch(config)# logging threshold https-server-log 50

Resetting the audit log threshold to its default of 50:

switch(config)# no logging threshold audit-log

Resetting the authentication log threshold to its default of 90:

switch(config)# no logging threshold auth-log

Resetting the event log threshold to its default of 90:

switch(config)# no logging threshold event-log

Resetting the HTTPS server log threshold to its default of 90:

switch(config)# no logging threshold https-server-log

Command History

Release

10.11

10.09

Modification

Introduced the commands‐log parameter.

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logrotate maxsize

Syntax

logrotate maxsize <MAX-SIZE>

no logrotate maxsize

Public

logrotate maxsize 35

Description

Specifies the maximum allowed log file size.

A log file that exceeds either the logrotate maxsize or the logrotate period (whichever happens first),
triggers rotation of the log file.

The no form of this command resets the size of the log file to the default (100 MB).

Parameter

Description

<MAX‐SIZE>

Specifies the allowed size the log file can reach before it is com
pressed and stored locally or transferred to a remote host. Rang
e: 10 to 200 MB. Default: 100 MB.

Examples

Setting the maximum log file size:

switch(config)# logrotate maxsize 24

Resetting the maximum log file size to its default of 100 MB:

switch(config)# no logrotate maxsize

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logrotate period

Public

logrotate period 36

Syntax

logrotate period {daily | hourly | monthly | weekly}

no logrotate period

Description

Sets the log file rotation time period. Defaults to daily.

A log file that exceeds either the logrotate maxsize or the logrotate period (whichever happens first),
triggers rotation of the log file.

The no form of this command resets the log rotation period to the default of daily.

Parameter

daily

hourly

monthly

weekly

Examples

Description

Rotates log files on a daily basis (default) at 0:01.

Rotates log files every hour at the first second of the hour.

Rotates log files monthly on the first day of the month at 00:01
.

Rotates log files once a week on Sunday at 00:01.

Setting a weekly period:

switch(config)# logrotate period weekly

Resetting the period to its default of daily:

switch(config)# no logrotate period

Command History

Release

Modification

10.07 or earlier

‐‐

Public

logrotate period 37

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logrotate target

Syntax

logrotate target <URI> [vrf <VRF_NAME>]

no logrotate target [<URI>] [vrf <VRF_NAME>]

Description

Using TFTP, sends the rotated log files to a specified remote host identified by Universal Resource Identifier
(URI).

The no form of this command resets the target to the default, which stores the rotated and compressed log
files locally in /var/log/.

Command context

Parameter

<URI>

Description

Specifies the URI of the remote host. The default directory is  l
ocal .

tftp://{{<IPV4_ADDR>|IPV6_ADDR>}|HOST}[/
<DIRECTORY>]

<VRF_NAME>

Specifies the VRF name (Default:  default ).

Usage

•  Rotated log files are compressed and stored locally in the path /var/log/ regardless of the remote host

configuration.

Examples

Setting an IPv4 target:

Public

logrotate target 38

switch(config)# logrotate target tftp://192.168.1.132

Setting an IPv4 target with a directory:

switch(config)# logrotate target tftp://192.168.1.132/logrotate/

Setting an IPv4 target with the default VRF:

switch(config)# logrotate target tftp://192.168.1.132 vrf mgmt

Setting an IPv6 target with the default VRF:

switch(config)# logrotate target tftp://2001:db8:0:1::128 vrf default

Resetting the target to local:

switch(config)# no logrotate target

Command History

Release

10.09

Modification

Updated the syntax and examples.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

show logrotate

Syntax

show logrotate

Public

show logrotate 39

Description

Shows the log rotate configuration.

Examples

switch# show logrotate

Logrotate configurations :

Period            : weekly

Maxsize           : 20MB

Target            : tftp://2001:db8:0:1::128 vrf mgmt

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Event Logs

Event logging logs events generated by daemons, processes, and plug-ins running within the switch
software. The event logging framework captures the event logs in a system journal by updating the journal
fields and meta data.

Subtopics

Showing and clearing events

Showing and clearing events

The  clear events  command is used to clear the event log of all events. The  show events
command is used to show all event logs generated by the switch since the last reboot. See the Switch system
and hardware commands chapter chapter of the Fundamentals Guide for information on these commands.

Public

Event Logs 40

The time stamp for event log messages generated from the Service OS indicates when the event log
messages were transferred to the event log after a switch boot and not when the issue occurred.

See the for information about accounting logs.

Client Filter

Event log client filter provides the ability to filter event logs for specific IP or MAC addresses. This enables
the REST client to query event logs from the switch's journal while filtering for IP or MAC address values.

New keys for IP and MAC addresses are added to the switch's journal of pre-existing keys (for example ID
and Category).

Subtopics

Log messages

Log messages

Log messages are generated to record various events occurring within the system. Each message contains a
unique ID to represent an event and its attributes such as category, module ID or module role. The unique ID
can then be used to filter for specific event types from a switch's journal.

NOTE

•  REST API can filter for all events occurring on a specific IP or MAC address.

•  REST API can filter for a specific event occurring on a specific IP or MAC

address.

•  REST API can filter for events based on a list of IPs and MACs.

CAUTION
Event log client filter does not support Go language daemons. Only C daemons
are supported.

Cable Diagnostics

Public

Client Filter 41

The Time-Domain Reflectometer (TDR) feature helps characterize and locate cable faults in an Ethernet
cable. TDR involves showing a reflection at any impedance change within the cable when a low voltage pulse
is sent into the cable. TDR measures the time between release and return of the low voltage pulse from
any reflections. The distance to the reflection can be calculated by measuring the time and the transmission
velocity of the pulse.

TDR or Cable Diagnostics is a port feature supported on some switches running software. TDR is used to
detect cable faults on the following ports:

Table 1. Cable fault detection on supported ports types
1GbT
Platforms

5G‐SmartRate

10G‐SmartRate

4100i

6000

6100

Yes

Yes

Yes

‐

‐

‐

‐

‐

‐

TDR or Cable Diagnostics can also be run from the API.

Subtopics

How TDR works on platforms
Cable diagnostics tests
Cable diagnostic commands

How TDR works on platforms

The implementation of TDR in platforms is dependent on the physical layer chips (PHYs) that are part of the
front-end network ports hardware. switches activate TDR on the PHY when a user enters the  diag cabl
e-diagnostic  command. The switch waits for the report about TDR measurements from the PHY. The
switch then reads the results and reports the values to the user.

Cable diagnostics tests

NOTE
The cable diagnostics test will bring down the link, which will take more time to
complete the test.

Public

How TDR works on platforms 42

The TDR cable diagnostic test allows an operator to test twisted pair cables for faults without physically
disconnecting the cables from the switch. It helps in troubleshooting connectivity or monitoring performance
on one or more switch ports.

The  diag cable-diagnostic  command can be used to run cable diagnostic tests and display the
test results.

The following table provides the cable status messages and their descriptions.

Status

good

open

intra‐short

inter_short

high_imp

low_imp

unknown

Meaning

The MDI pair is good.

The MDI pair is not terminated with a link partner or
has an open circuit.

The MDI pair is shorted within itself.

The MDI pair is shorted with another pair.

The MDI pair has high‐impedance mismatch and is
not guaranteed to link up.

The MDI pair has low‐impedance mismatch and is
not guaranteed to link up.

The MDI pair has failed the cable diagnostic test.

The following table provides the possible cable diagnostic failure reasons for port types.

Port Type

1GbT

5G‐SmartRate

10G‐SmartRate

Reasons

Interface is busy

Interface is busy

Interface is busy

The following table provides the cable length accuracy for port types.

Port Type

1GbT

Reasons

When diagnostic status is "good", cable length is re
ported.

Public

Cable diagnostics tests 43

Port Type

5G‐SmartRate

10G‐SmartRate

Reasons

When diagnostic status is "good", cable length is not
reported.

When diagnostic status is "good", cable length is not
reported.

The following table provides the distance to fault accuracy for port types.

Port Type

1GbT

5G‐SmartRate

10G‐SmartRate

Reasons

When diagnostic status is not "good" or "failed", dista
nce to fault is reported within +/‐10m.

When diagnostic status is not "good" or "failed", dista
nce to fault is reported within +/‐5m.

When diagnostic status is not "good" or "failed", dista
nce to fault is reported within +/‐5m.

Cable diagnostic commands

Select a command from the list in the left navigation menu.

Subtopics

diag cable-diagnostic

diag cable-diagnostic

Syntax

diag cable-diagnostic

   test <IF-NAME>

   show <IF-NAME>
   clear <IF-NAME>

Description

Provides information about the cable health after running a diagnostic test on an interface.

Public

Cable diagnostic commands 44

If you run a new cable diagnostic command when a cable diagnostic is in progress for the interface, the new
cable diagnostic command fails to execute. In such a scenario, an error message is displayed.

On executing a cable diagnostic test command, it automatically clears the old test results before the new
test starts.

Parameter

Description

Specifies the name of the interface.

<IF‐NAME>

test <IF‐NAME>

Runs a cable diagnostic test on an interface.

show <IF‐NAME>

clear <IF‐NAME>

Examples

Displays the diagnostic test result for an interface.

Clears the cable diagnostic test results for an interface.

The following example displays running a cable diagnostic test on interface  1/3/1 :

switch# diag cable-diagnostic test 1/3/1

This command will cause a loss of link on the port under test and will take

several seconds to complete.

Continue (y/n)? y

The following example displays the error message on executing a cable diagnostic command while the
current diagnostic test is in progress:

switch# diag cable-diagnostic test 1/3/1

A cable diagnostic test for interface 1/3/1 is already in progress.
The following example displays the error message when cable diagnostic test is requested for an
unsupported port:

switch# diag cable-diagnostic test 1/3/1

Cable diagnostic is not supported on interface 1/3/1.
The following examples display the cable diagnostic test result for 1GbT interface:

switch# diag cable-diagnostic show 1/3/1

                          Cable        Impedance   Distance*   MDI

Interface        Pinout   Status       (Ohms)      (Meters)    Mode
--------------------------------------------------------------------

1/3/1            1-2      good         85-115       10 +/- 10  mdi

(1GbT)           3-6      good         85-115       10 +/- 10  mdi

                 4-5      good         85-115        5 +/- 10  mdi

Public

diag cable-diagnostic 45

7-8      good         85-115        3 +/- 10  mdi

* Full cable length for good cables or distance to fault for faulty cables.

Cable status legend (1GbT):

Cable        Impedance

Status       (Ohms)     Description

----------------------------------------------------------------

good         85-115     No cable faults found

open         >115       Open circuit detected

intra-short  <85        Short circuit within the same wire pair

inter-short  <85        Short circuit with another wire pair

high-imp     >115       Cable impedance higher than expected

low-imp      <85        Cable impedance lower than expected

unknown      --         Cable test inconclusive
The following examples display the cable diagnostic test result for 5G-SmartRate interface:

switch# diag cable-diagnostic show 1/1/20

                          Cable        Impedance   Distance*   MDI

Interface        Pinout   Status       (Ohms)      (Meters)    Mode

--------------------------------------------------------------------

1/1/20           1-2      good         85-115          --      mdi

(5G-SmartRate)   3-6      open         >300          4 +/- 5   mdi

                 4-5      open         >300          4 +/- 5   mdi

                 7-8      high-imp     >115          3 +/- 5   mdi

* Full cable length for good cables or distance to fault for faulty cables.

Cable status legend (5G-SmartRate):

Cable        Impedance

Status       (Ohms)     Description

----------------------------------------------------------------

good         85-115     No cable faults found

open         >300       Open circuit detected

intra-short  <30        Short circuit within the same wire pair

inter-short  <30        Short circuit with another wire pair

high-imp     >115       Cable impedance higher than expected

low-imp      <85        Cable impedance lower than expected

unknown      --         Cable test inconclusive
The following example displays the error message when you execute a cable diagnostic command while the
current diagnostic test is in progress:

switch# diag cable-diagnostic show 1/3/1

A cable diagnostic test for interface 1/3/1 is currently in progress.
The following example displays the error message when cable diagnostic test result is not available:

switch# diag cable-diagnostic show 1/3/1

Cable diagnostic test results for interface 1/3/1 are not available.
The following example clears the cable diagnostic test results for the specified interface:

Public

diag cable-diagnostic 46

switch# diag cable-diagnostic clear 1/3/1

The following example displays the error message when you execute a cable diagnostic command while the
current diagnostic test is in progress:

switch# diag cable-diagnostic clear 1/3/1

A cable diagnostic test for interface 1/3/1 is currently in progress.

NOTE

Running a cable diagnostic test will result in a brief interruption in connectivity
on all tested ports.

Command History

Release

10.11

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

Supportability Copy

To effectively diagnose various issues arising at the switch, different types of data are copied out using copy
commands for further analysis.

Use the copy core-dump command to copy the core-dump of a daemon crash.

Use the copy show-tech command to capture the status of the feature.

If there is feature misbehavior, use the copy support-files feature command to copy all feature related
information for further analysis. Additionally use copy support-log and copy diag-dump to copy
information that helps to analyze the internal behavior of a feature/daemon.

Use copy command-output to copy any show command's output to remote destinations or USB storage.

Public

Supportability Copy 47

These files can be copied to a remote destination using sftp/tftp, additionally they can also be stored in the
USB storage.

TFTP VxLAN Support

TFTP is supported over VxLAN tunnels with IPv4 underlay.

NOTE

Limitations

Running-config, check-point config and startup-config will not be copied fully to destination file in TFTP
server (only partial configuration will be copied) even though TFTP shows the transfer was successful. This
is because fragmentation/ressembly/MTU discovery are not supported on VxLAN paths. Packets exceeding
1500 bytes are dropped when the TFTP transfer is done with default TFTP block size or default MTU size.

Workaround

Increase the MTU size (JUMBO) on all interfaces between the TFTP client and TFTP server or use a custom
block size of 1375 or less for TFTP transfers.

Example of a custom blocksize configuration:

copy running-config tftp://72.1.1.100;blocksize=1374/runv4 cli vrf vrf1

copy running-config tftp://[20:2:100];blocksize=1374/runv6 cli vrf vrf1

Subtopics

Supportability copy commands

Supportability copy commands

Select a command from the list in the left navigation menu.

Subtopics

copy checkpoint
copy command-output
copy diag-dump feature <FEATURE>
copy diag-dump local-file
copy <IMAGE>
copy running-config
copy show-tech feature
copy show-tech local-file
copy startup-config
copy support-files
copy support-files local-file

Public

Supportability copy commands 48

copy support-log

copy checkpoint

Syntax

copy checkpoint <CHECKPOINT-NAME> {<STORAGE-URL> | <REMOTE-URL>}

Description

Copies the checkpoint using TFTP, SFTP, SCP, or USB.

Parameter

Description

Specifies the checkpoint name.

<CHECKPOINT‐NAME>

{<STORAGE‐URL> | <REMOTE‐
URL>}

Select either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

<STORAGE‐URL>

<REMOTE‐URL>

Specifies the USB to copy command output.

Syntax:

{usb}:/ <FILE>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

Examples

Copying checkpoint chpt to a remote URL:

switch# copy checkpoint chpt scp://root@10.0.1.1/config vrf mgmt

Public

copy checkpoint 49

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this co
mmand from the auditor context (auditor>) only.

copy command-output

Syntax

copy command-output "<COMMAND>" {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-

NAME>]}

Description

Copies the specified command output using TFTP, SFTP, SCP, USB, or local.

Parameter

Description

<COMMAND>

Specifies the command from which you want to obtain its outpu
t. Required. Users with auditor rights can specify these two com
mands only:

show accounting log

show events

{<STORAGE‐URL> | <REMOTE‐
URL>
  [vrf <VRF‐NAME>]}

Select either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

Specifies the USB to copy command output.

Syntax:

Public

copy command-output 50

Parameter

<STORAGE‐URL>

Description

{usb}:/ <FILE>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/ <FILE>

Specifies the VRF name. The default VRF name is default. Optio
nal.

<REMOTE‐URL>

   vrf  <VRF‐NAME>

Examples

Copying the output from the show events command to a remote URL:

switch# copy command-output "show events" tftp://10.100.0.12/file

Copying the output from the show tech command to a remote URL with a VRF named mgmt:

switch# copy command-output "show tech" scp://user@10.100.0.12/file vrf mgmt

switch# copy command-output "show tech" tftp://10.100.0.12/file vrf mgmt

Copying the output from the show events command to a file named events on a USB drive:

switch# copy command-output "show events" usb:/events

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Public

copy command-output 51

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this co
mmand from the auditor context (auditor>) only.

copy diag-dump feature <FEATURE>

Syntax

copy diag-dump feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-

URL>}

Description

Copies the specified diagnostic information using TFTP, SFTP, SCP, USB, or local.

Parameter

Description

The name of a feature, for example aaa or vrrp. Required.

<FEATURE>

{<REMOTE‐URL> [vrf <VRF‐
NAME> |<STORAGE‐URL>]}

Select either the remote URL or the storage URL for the destin
ation of the copied command output. Required.

Specifies the remote destination URL. Required. The syntax of t
he URL is the following:

<REMOTE‐URL>

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

   vrf <VRF‐NAME>

Specifies the VRF name. If no VRF name is provided, the VRF n
amed default is used. Optional.

Specifies the USB to copy command output. Required.

Syntax:  {usb}:/<FILE>

Public

copy diag-dump feature <FEATURE> 52

Description

Parameter

<STORAGE‐URL>

Examples

Copying the output from the aaa feature to a remote URL with a specified VRF:

switch# copy diag-dump feature aaa tftp://10.100.0.12/diagdump.txt vrf mgmt

Copying the output from the aaa feature to a remote URL with a specified VRF:

switch# copy diag-dump feature aaa scp://user@10.100.0.12/diagdump.txt vrf

mgmt

switch# copy diag-dump feature vrrp usb:/diagdump.txt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy diag-dump local-file

Syntax

copy diag-dump local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies the diagnostic information stored in a local file using TFTP, SFTP, SCP, USB, or local.

Public

copy diag-dump local-file 53

Parameter

Description

{<REMOTE‐URL> [vrf <VRF‐
NAME>] |<STORAGE‐URL>}

Select either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

<REMOTE‐URL>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

   vrf <VRF‐NAME>

Specifies the VRF name. The default VRF name is default. Optio
nal.

Specifies the USB to copy command output.

Syntax: {usb}:/ <FILE>

<STORAGE‐URL>

Usage

The copy diag-dump local-file command can be used only after the information is captured. Run the
diag-dump <FEATURE-NAME> basic local-file command before you enter the copy diag-dump local-file
command to capture the diagnostic information for the specified feature into the local file.

Examples

Copying the output from the local file to a remote URL:

switch# diag-dump aaa basic local-file

switch# copy diag-dump local-file tftp://10.100.0.12/diagdump.txt

Copying the output from the local file to a remote URL:

switch# diag-dump aaa basic local-file

switch# copy diag-dump local-file scp://user@10.100.0.12/diagdump.txt

Copying the output from the local file to a USB drive:

switch# diag-dump aaa basic local-file

switch# copy diag-dump local-file usb:/diagdump.txt

Public

copy diag-dump local-file 54

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy <IMAGE>

Syntax

copy <IMAGE> {<STORAGE-URL> | <REMOTE-URL>} <FILE-NAME> [vrf <VRF-NAME>]

Description

Copies the image using TFTP, SFTP, SCP, or USB.

Parameter

<IMAGE>

Description

Specifies the image.

{<STORAGE‐URL> | <REMOTE‐
URL>}

Select either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

Specifies the USB to copy command output.

<STORAGE‐URL>

Syntax:

{usb}:/ <FILE>

Specifies the URL to copy the command output.

Syntax:

Public

copy <IMAGE> 55

Parameter

<REMOTE‐URL>

<FILE‐NAME>

vrf  <VRF‐NAME>

Description

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

Specifies the file name.

Specifies the VRF name. The default VRF name is default. Optio
nal.

Examples

Copying the image to a remote URL:

switch# copy scp://root@20.0.1.1/primary.swi primary vrf mgmt

Copying the secondary image to a remote URL:

switch# copy secondary scp://root@20.0.1.1/primary.swi vrf mgmt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this co
mmand from the auditor context (auditor>) only.

Public

copy <IMAGE> 56

copy running-config

Syntax

copy running-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME>

[vrf <VRF-NAME>]

Description

Copies the running configuration using TFTP, SFTP, SCP, or USB.

Parameter

Description

{<STORAGE‐URL> | <REMOTE‐
URL>}

Select either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

<STORAGE‐URL>

<REMOTE‐URL>

Specifies the USB to copy command output.

Syntax:

{usb}:/ <FILE>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{<IP> | <HOST>}[:<PORT>][;bl

ocksize=<VAL>]/<FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

config <CONFIG‐NAME>

Specifies the running configuration.

vrf  <VRF‐NAME>

overwrite

Usage

Specifies the VRF name. The default VRF name is default. Optio
nal.

The configuration is only applied to the running configuration if
all commands succeed without errors.

By default, the CLI configuration contained in the remote file is applied on top of the running configuration,
and all the CLI commands in the file are applied line-by-line. If a particular CLI command fails, the failure is
logged in the event log and the next line in the CLI configuration is processed.

When using the optional overwrite parameter, the configuration is only applied to running configuration
if all the commands succeeded without errors. If errors are present, the existing running-config will remain
intact. You can then inspect the event logs to check and fix the errors and retry the operation. If more than
20 errors are present, the operation stops processing any further commands, and will display the errors at

Public

copy running-config 57

that point in the event logs. For more information on this feature, refer to the video on the HPE Aruba
Networking Airheads Broadcasting Channel.

Examples

Copying the running configuration to a remote URL:

switch# copy running-config scp://root@10.0.1.1/config cli vrf mgmt

Command History

Release

10.15

10.08

Modification

The overwrite parameter is introduced.

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this co
mmand from the auditor context (auditor>) only.

copy show-tech feature

Syntax

copy show-tech feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-

URL>}

Description

Copies show tech output using TFTP, SFTP, SCP, USB, or local.

Public

copy show-tech feature 58

Parameter

Description

{<REMOTE‐URL> [vrf <VRF‐
NAME> | <STORAGE‐URL>]}

Select either the remote URL or the storage URL for the destin
ation of the copied command output. Required.

Specifies the URL to copy the command output. Required.

<REMOTE‐URL>

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

   vrf <VRF‐NAME>

Specifies the VRF name. The default VRF name is default. Optio
nal.

Specifies the USB to copy command output. Required.

Syntax: {usb}:/ <FILE>

<STORAGE‐URL>

Example

Copying show tech output of the aaa feature using SCP:

switch# copy show-tech feature aaa scp://user@10.0.0.12/file.txt vrf mgmt

Copying show tech output of the  config  feature using SFTP on the  mgmt  VRF:

switch# copy show-tech feature config sftp://root@10.0.0.1/tech.txt vrf mgmt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Public

copy show-tech feature 59

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy show-tech local-file

Syntax

copy show-tech local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies show tech output stored in a local file.

Parameter

Description

{<REMOTE‐URL> [vrf <VRF‐
NAME>] | <STORAGE‐URL> ]}

Select either the remote URL or the storage URL for the destin
ation of the copied command output. Required.

<REMOTE‐URL>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

   vrf <VRF‐NAME>

Specifies the VRF name. The default VRF name is default. Optio
nal.

Specifies the USB to copy command output.

Syntax: {usb}:/ <FILE>

<STORAGE‐URL>

Usage

Before entering the copy show-tech local-file command, run the show tech command with the local-file
parameter for the specified feature.

Public

copy show-tech local-file 60

Examples

Copying the output to a remote URL:

switch# copy show-tech local-file tftp://10.100.0.12/file.txt

Copying the output to a remote URL:

switch# copy show-tech local-file scp://user@10.100.0.12/file.txt

Copying the output to a remote URL with a VRF:

switch# copy show-tech local-file tftp://10.100.0.12/file.txt vrf mgmt

Copying the output to a USB:

switch# copy show-tech local-file usb:/file

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy startup-config

Syntax

copy startup-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME>
[vrf <VRF-NAME>]

Description

Copies the running configuration using TFTP, SFTP, SCP, or USB.

Public

copy startup-config 61

Parameter

Description

{<STORAGE‐URL> | <REMOTE‐
URL>}

Select either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

<STORAGE‐URL>

<REMOTE‐URL>

Specifies the USB to copy command output.

Syntax:

{usb}:/ <FILE>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

config <CONFIG‐NAME>

Specifies the startup configuration.

vrf  <VRF‐NAME>

Specifies the VRF name. The default VRF name is default. Optio
nal.

Examples

Copying the startup configuration to a remote URL:

switch# copy startup-config scp://root@10.0.1.1/config json vrf mgmt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Public

copy startup-config 62

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this co
mmand from the auditor context (auditor>) only.

copy support-files

Syntax

copy support-files

   <REMOTE-URL> [vrf <VRF-NAME>]

   <STORAGE-URL>

   all <REMOTE-URL> [vrf <VRF-NAME>]

   all <STORAGE-URL>

   feature <FEATURE-NAME>

            <STORAGE-URL>

   previous-boot <REMOTE-URL> [vrf <VRF-NAME>]

   previous-boot <STORAGE-URL>

Description

Copies a set of support files to a compressed file in tar.gz format using TFTP, SFTP, SCP, or USB or to a
directory over SFTP, USB, or local.

NOTE
Do not press Control + Z at the password prompt while copying support files, as
this will prevent the console from executing other commands.

Parameter

Description

The feature name, for example,  aaa .

<FEATURE‐NAME>

{<REMOTE‐URL> [vrf <VRF‐
NAME>] | <STORAGE‐URL> ]}

Select either the remote URL or the storage URL for the destin
ation of the copied command output. Required.

Public

copy support-files 63

Parameter

Description

<REMOTE‐URL>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/ <

FILE>

   vrf <VRF‐NAME>

Specifies the VRF name. The default VRF name is default. Optio
nal.

Specifies the USB to copy command output.

Syntax: {usb}:/ <FILE>

<STORAGE‐URL>

Usage

If feature name is not provided, the command collects generic system-specific support information. If a
feature name is provided, the command collects feature-specific support information.

Examples

Copying the support files to a remote URL:

switch# copy support-files tftp://10.100.0.12/file.tar.gz

Copying the support files of the lldp feature to a remote URL with a specified VRF:

switch# copy support-files feature lldp tftp://10.100.0.12/file.tar.gz vrf

mgmt

Copying the support files from the previous boot to a remote URL with a specified VRF:

switch# copy support-files previous-boot scp://user@10.0.14.206/file.tar.gz

vrf mgmt

Copying the support files to a USB:

switch# copy support-files usb:/file.tar.gz

Copying all the support files to a remote URL:

switch# copy support-files all sftp://root@10.0.14.216/file.tar.gz vrf mgmt

Copying the support files of the config feature to a USB:

Public

copy support-files 64

switch# copy support-files feature config usb:/file.tar.gz

NOTE

Copying support files as a directory will not be allowed when system memory is
insufficient. In the event this type of copy operation is attempted with low system
memory, the command-line interface may display the error message: Failed to
collect support files due to insufficient system memory.

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy support-files local-file

Syntax

copy support-files [feature <FEATURE-NAME> | previous-boot | all

            ] local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Stores a set of support files as a compressed file in the switch locally and copies the preserved support files
to a directory using TFTP, SFTP, SCP, USB, or local. . You can store only one copy of the support file locally.
When you store a new support file, it overwrites the existing support file

NOTE
Do not press Control + Z at the password prompt while copying support files, as
this will prevent the console from executing other commands.

Public

copy support-files local-file 65

Parameter

Description

Specifies the feature for the support files.

<FEATURE‐NAME>

<SLOT‐ID>

<MEMBER‐ID>

<REMOTE‐URL>

<STORAGE‐URL>

<VRF‐NAME>

Usage

Specifies the module slot number identifier for the support files.
Range: 1/1‐1/4, 1/7‐1/10

Specifies the VSF member identifier for the support files. Range
: 1‐10

Specifies the URL to copy the support files.

Specifies the USB to copy the support files.

Specifies the VRF name. The default VRF name is default.

If the copy of the support files to the destination fails, an alternate option is prompted to store the
collected data in the local file. This helps us to retry the copy process using copy support-files local-file
<REMOTE-URL/STORAGE-URL> without the need of regenerating the file.

Examples

Copying support file to the local file:

switch# copy support-files local-file
switch# copy support-files feature lldp local-file
switch# copy support-files previous-boot local-file

switch# copy support-files all local-file

The operation to copy all support files could take a while to complete.

Do you want to continue (y/n)?

Public

copy support-files local-file 66

Copying local support file to a remote URL and storage URL:

switch# copy support-files local-file usb:/support_files_dir_path/

switch# copy support-files local-file scp://root@10.0.14.206//

support_files_dir_path/abc.tar.gz vrf mgmt

NOTE

Copying support files as a directory will not be allowed when system memory is
insufficient. In the event this type of copy operation is attempted with low system
memory, the command-line interface may display the error message: Failed to
collect support files due to insufficient system memory.

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy support-log

Syntax

Description

Copies the specified support log for a daemon TFTP, SFTP, SCP, USB, or local.

Parameter

<DAEMON‐NAME>

Description

Specifies the name of the daemon. Required.

Public

copy support-log 67

Parameter

Description

{<STORAGE‐URL> | <REMOTE‐
URL> [vrf <VRF‐NAME>]}

Selects either the storage URL or the remote URL for the destin
ation of the copied command output. Required.

<STORAGE‐URL>

Specifies the USB to copy command output.

Syntax: {usb}:/ <FILE>

<REMOTE‐URL>

Specifies the URL to copy the command output.

Syntax:

•  {tftp://}{ <IP> | <HOST> }[: <PORT> ][;blocksize= <VAL> ]

/ <FILE>

•  {sftp:// | scp:// <USER> @}{ <IP> | <HOST> }[: <PORT> ]/

<FILE>

vrf <VRF‐NAME>

Specifies the VRF name. If no VRF name is provided, the VRF n
amed default is used. Optional.

Usage

Fast log is a high performance, per-daemon binary logging infrastructure used to debug daemon level
issues by precisely capturing the per daemon/module/functionalities debug traces in real time. Fast log, also
referred to as support logs, helps users to understand the feature internals and its specific happenings. The
fast logs from one daemon are not overwritten by other daemon logs because fast logs are captured as part
of a daemon core dump. Fast logs are enabled by default.

Examples

Copying the support log from the daemon hpe-fand to a remote URL:

switch# copy support-log hpe-fand tftp://10.100.0.12/file

Copying the support log from the daemon fand to a remote URL with a VRF named mgmt:

switch# copy support-log fand scp://user@10.100.0.12/file vrf mgmt

Copying the support log from the daemon hpe-fand to a remote URL with a VRF named mgmt:

switch# copy support-log hpe-fand tftp://10.100.0.12/file vrf mgmt

Copying the support log from the daemon hpe-fand to a USB:

switch# copy support-log hpe-fand usb:/support-log

Public

copy support-log 68

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Traceroute

Traceroute is a computer network diagnostic tool for displaying the route (path), and measuring transit
delays of packets across an Internet Protocol (IP) network. It sends a sequence of User Datagram Protocol
(UDP) packets addressed to a destination host. The time-to-live (TTL) value, also known as hop limit, is used
in determining the intermediate routers being traversed towards the destination.

Subtopics

Traceroute commands

Traceroute commands

Select a command from the list in the left navigation menu.

Subtopics

traceroute
traceroute6

traceroute

Public

Traceroute 69

Syntax

traceroute {<IPV4-ADDR> | <HOSTNAME>} [ip-option loosesourceroute <IPV4-

ADDR>] [dstport <NUMBER> | maxttl <NUMBER> | minttl <NUMBER> | probes

<NUMBER> | timeout <TIME>] [vrf <VRF-NAME>] source {<IPV4-ADDR> | <IFNAME>}

Description

Uses traceroute for the specified IPv4 address or hostname with or without optional parameters.

Parameter

Description

IPv4‐address <IPV4‐ADDR>

Specifies the IPv4 address.

hostname

ip‐option

Specifies the hostname of the device to traceroute.

Specifies the IP option.

loosesourceroute <IPV4‐
ADDR>

Specifies the route for loose source record route. Enter one or m
ore intermediate router IP addresses separated by ',' for loose so
urce routing.

dstport <NUMBER>

Specifies the destination port, <1‐34000>. Default: 33434

maxttl <NUMBER>

minttl <NUMBER>

Specifies the maximum number of hops to reach the destinatio
n, <1‐255>. Default: 30

Specifies the Minimum number of hops to reach the destination
, <1‐255>. Default: 1

probes <NUMBER>

Specifies the number of probes, <1‐5>. Default: 3

timeout <TIME>

Specifies the traceroute timeout in seconds, <1‐60>. Default:
3 seconds

vrf <VRF‐NAME>

Specifies the virtual routing and forwarding (VRF) to use .

source {<IPV4‐ADDR> |
<IFNAME>}

Usage

Specifies the source IPv4 address or interface name.

Traceroute is a computer network diagnostic tool for displaying the route (path), and measuring transit
delays of packets across an Internet Protocol (IP) network. It sends a sequence of User Datagram Protocol
(UDP) packets addressed to a destination host. The time-to-live (TTL) value, also known as hop limit, is used
in determining the intermediate routers being traversed towards the destination.

Public

traceroute 70

Examples

switch#

traceroute 10.0.10.1
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

traceroute localhost
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 127.0.0.1 0.018ms
0.006ms 0.003ms switch#

traceroute 10.0.10.1 maxttl 20
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 3 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

traceroute 10.0.10.1 minttl 1
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

traceroute 10.0.10.1 dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

traceroute 10.0.10.1 probes 2
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 2 probes 1 10.0.40.2
0.002ms 0.002ms 2 10.0.30.1 0.002ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms switch#

traceroute 10.0.10.1 timeout 5
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 5 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

traceroute localhost vrf red
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 127.0.0.1 0.003ms
0.002ms 0.001ms switch#

traceroute localhost mgmt
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 127.0.0.1 0.018ms
0.006ms 0.003ms switch#

traceroute 10.0.10.1 maxttl 20 timeout 5 minttl 1 probes 3 dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms switch#

Public

traceroute 71

traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2 maxttl 20 timeout 5 minttl 1 probes 3
dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3 probes 1 10.0.40.2
0.002ms 0.002ms 0.001ms 2 10.0.30.1 0.002ms 0.001ms 0.001ms 3 10.0.10.1 0.001ms 0.002ms
0.002ms

switch# traceroute 10.0.0.2 source 10.0.0.1

traceroute to 10.0.0.2 (10.0.0.2), 30 hops max

  1   10.0.0.2  0.299ms  0.155ms  0.115ms

switch# traceroute 10.0.0.2 source 1/1/1

traceroute to 10.0.0.2 (10.0.0.2), 30 hops max

  1   10.0.0.2  0.479ms  0.222ms  0.171ms

Command History

Release

10.08

Modification

Added  source IP address  and  source interface name  para
meters.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

traceroute6

Syntax

traceroute6 {<IPV6-ADDR> | <HOSTNAME>} [dstport <NUMBER> | maxttl <NUMBER>

| probes <NUMBER> | timeout <TIME>] [vrf <VRF-NAME>] source {<IPV6-ADDR> |

<IFNAME>}

Description

Uses traceroute for the specified IPv6 address or hostname with or without optional parameters.

Public

traceroute6 72

Parameter

Description

IPv6‐address <IPV6‐ADDR>

Specifies the IPv6 address.

hostname

Specifies the hostname of the device to traceroute.

dstport <NUMBER>

Specifies the destination port, <1‐34000>. Default: 33434

maxttl <NUMBER>

Specifies the maximum number of hops to reach the destinatio
n, <1‐255>. Default: 30

probes <NUMBER>

Specifies the number of probes, <1‐5>. Default: 3

timeout <TIME>

vrf <VRF‐NAME>

source {<IPV6‐ADDR> |
<IFNAME>}

Usage

Specifies the traceroute timeout in seconds, <1‐60>. Default:
3 seconds

Specifies the virtual routing and forwarding (VRF) to use, <VRF
‐NAME>.

Specifies the source IPv6 address or interface name.

Traceroute is a computer network diagnostic tool for displaying the route (path), and measuring transit
delays of packets across an Internet Protocol (IP) network. It sends a sequence of User Datagram Protocol
(UDP) packets addressed to a destination host. The time-to-live (TTL) value, also known as hop limit, is used
in determining the intermediate routers being traversed towards the destination.

Examples

switch#

traceroute6 0:0::0:1
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.117 ms 0.032 ms 0.021 ms switch#

traceroute6 localhost
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.089 ms 0.03 ms 0.014 ms switch#

traceroute6 0:0::0:1 maxttl 30
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.117 ms 0.032 ms 0.021 ms switch#

traceroute6 0:0::0:1 dsrport 33434
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.117 ms 0.032 ms 0.021 ms switch#

Public

traceroute6 73

traceroute6 0:0::0:1 probes 2
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 2 probes, 24 byte packets 1 localhost (::1)
0.117 ms 0.032 ms switch#

traceroute6 0:0::0:1 timeout 3
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.117 ms 0.032 ms 0.021 ms switch#

traceroute6 localhost vrf red
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.077 ms 0.051 ms 0.054 ms switch#

traceroute6 localhost mgmt
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.089 ms 0.03 ms 0.014 ms switch#

traceroute6 0:0::0:1 maxttl 30 timeout 3 probes 3 dstport 33434
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24 byte packets 1 localhost (::1)
0.117 ms 0.032 ms 0.021 ms

switch# traceroute6 2001::2 source 2001::1

traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout,

3 probes, 24 byte packets

1  2001::2 (2001::2)  0.4331 ms  0.3186 ms  0.1874 ms

switch# traceroute6 2001::2 source 1/1/1

traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout,

3 probes, 24 byte  packets

1  2001::2 (2001::2)  0.6145 ms  0.4165 ms  0.1620 ms

Command History

Release

10.08

Modification

Added source IP address and source interface name parameters.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Public

traceroute6 74

Ping

The ping (Packet Internet Groper) command is a common method for troubleshooting the accessibility of
devices. It uses Internet Control Message Protocol (ICMP) echo requests and ICMP echo replies to determine
if the other device is alive. It also measures the amount of time the request takes to receive a reply from
the specified destination. The ping command is mostly used to verify IP connectivity between two endpoints
which could be switch to switch, host to host, or host to switch. The reply packet tells if the host received the
ping and the amount of time it took to return the packet.

Subtopics

Ping commands
Troubleshooting

Ping commands

Subtopics

Ping commands
Troubleshooting

Ping commands

Select a command from the list in the left navigation menu.

Subtopics

ping
ping6

ping

Syntax

ping <IPv4-ADDR> | <hostname> [data-fill <pattern> | datagram-size <size> |
   interval <time> | repetitions <number> | timeout <time> | tos <number> |
   ip-option {include-timestamp | include-timestamp-and-address | record-

route} |

   vrf <vrfname> | do-not-fragment][source {IPv4-ADDR | IFNAME}]

Public

Ping 75

Description

Pings the specified IPv4 address or hostname with or without optional parameters.

Parameter

Description

ping <IPv4‐ADDR>

Selects the IPv4 address to ping.

<HOSTNAME>

data‐fill <PATTERN>

Selects the hostname to ping. Range: 1‐256 characters

Specifies the data pattern in hexadecimal digits to send. A maxi
mum of 16 "pad" bytes can be specified to fill out the ICMP pac
ket. Default: AB

datagram‐size <SIZE>

Specifies the ping datagram size. Range: 0‐65399, default: 10
0.

interval <TIME>

Specifies the interval between successive ping requests in seco
nds. Range: 1‐60 seconds, default: 1 second.

repetitions <NUMBER>

Specifies the number of packets to send. Range: 1‐10000 pac
kets, default: Five packets.

Specifies the ping timeout in seconds. Range: 1‐60 seconds, d
efault: 2 seconds.

Specifies the IP Type of Service to be used in Ping request. Ran
ge: 0‐255

Specifies an IP option (record‐route or timestamp option).

timeout <TIME>

tos <NUMBER>

ip‐option {include‐
timestamp |
  include‐timestamp‐and‐
address |
  record‐route}

include‐timestamp

Specifies the intermediate router time stamp.

include‐timestamp‐and‐
address

record‐route

vrf  <VRF‐NAME>

Specifies the intermediate router time stamp and IP address.

Specifies the intermediate router addresses.

Specifies the virtual routing and forwarding (VRF) to use. When
VRF option is not given, the default VRF is used.

Public

ping 76

Parameter

Description

source {IPv4‐ADDR | IFNAME}

Specifies the source IPv4 address or interface to use.

do‐not‐fragment

Specifies the do‐not‐fragment (DF) bit in IP header of the P
ing packet. This option does not allow the packet to be fragmen
ted when it has to go through a segment with a smaller maximu
m transmission unit (MTU).

Examples

Pinging an IPv4 address:

switch# ping 10.0.0.0

PING 10.0.0.0 (10.0.0.0) 100(128) bytes of data.

108 bytes from 10.0.0.0: icmp_seq=1 ttl=64 time=0.035 ms

108 bytes from 10.0.0.0: icmp_seq=2 ttl=64 time=0.034 ms

108 bytes from 10.0.0.0: icmp_seq=3 ttl=64 time=0.034 ms

108 bytes from 10.0.0.0: icmp_seq=4 ttl=64 time=0.034 ms

108 bytes from 10.0.0.0: icmp_seq=5 ttl=64 time=0.033 ms

--- 10.0.0.0 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.033/0.034/0.035/0.000 ms
Pinging the localhost:

switch# ping localhost

PING localhost (127.0.0.1) 100(128) bytes of data.

108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.060 ms

108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.035 ms

108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.043 ms

108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.041 ms

108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.034 ms

--- localhost ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3998ms
rtt min/avg/max/mdev = 0.034/0.042/0.060/0.011 ms
Pinging a server with a data pattern:

switch# ping 10.0.0.2 data-fill 1234123412341234acde123456789012

PATTERN: 0x1234123412341234acde123456789012

PING 10.0.0.2 (10.0.0.2) 100(128) bytes of data.

108 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.207 ms

108 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.187 ms
108 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.225 ms

108 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.197 ms

108 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.210 ms

--- 10.0.0.2 ping statistics ---

Public

ping 77

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.187/0.205/0.225/0.015 ms
Pinging a server with a datagram size:

switch# ping 10.0.0.0 datagram-size 200

PING 10.0.0.0 (10.0.0.0) 200(228) bytes of data.

208 bytes from 10.0.0.0: icmp_seq=1 ttl=64 time=0.202 ms

208 bytes from 10.0.0.0: icmp_seq=2 ttl=64 time=0.194 ms

208 bytes from 10.0.0.0: icmp_seq=3 ttl=64 time=0.201 ms

208 bytes from 10.0.0.0: icmp_seq=4 ttl=64 time=0.200 ms

208 bytes from 10.0.0.0: icmp_seq=5 ttl=64 time=0.186 ms

--- 10.0.0.0 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4000ms

rtt min/avg/max/mdev = 0.186/0.196/0.202/0.016 ms
Pinging a server with an interval specified:

switch# ping 9.0.0.2 interval 2

PING 9.0.0.2 (9.0.0.2) 100(128) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.199 ms

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.192 ms

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.208 ms

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.182 ms

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.194 ms

--- 9.0.0.2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 7999ms

rtt min/avg/max/mdev = 0.182/0.195/0.208/0.008 ms
Pinging a server with a specified number of packets to send:

switch# ping 9.0.0.2 repetitions 10

PING 9.0.0.2 (9.0.0.2) 100(128) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.213 ms

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.204 ms

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.201 ms

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.184 ms

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.202 ms

108 bytes from 9.0.0.2: icmp_seq=6 ttl=64 time=0.184 ms

108 bytes from 9.0.0.2: icmp_seq=7 ttl=64 time=0.193 ms

108 bytes from 9.0.0.2: icmp_seq=8 ttl=64 time=0.196 ms

108 bytes from 9.0.0.2: icmp_seq=9 ttl=64 time=0.193 ms

108 bytes from 9.0.0.2: icmp_seq=10 ttl=64 time=0.200 ms

--- 9.0.0.2 ping statistics ---

10 packets transmitted, 10 received, 0% packet loss, time 8999ms

rtt min/avg/max/mdev = 0.184/0.197/0.213/0.008 ms
Pinging a server with a specified timeout:

Public

ping 78

switch# ping 9.0.0.2 timeout 3

PING 9.0.0.2 (9.0.0.2) 100(128) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.175 ms

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.192 ms

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.190 ms

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.181 ms

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.197 ms

--- 9.0.0.2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4000ms

rtt min/avg/max/mdev = 0.175/0.187/0.197/0.007 ms
Pinging a server with the specified IP Type of Service:

switch# ping 9.0.0.2 tos 2

PING 9.0.0.2 (9.0.0.2) 100(128) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.033 ms

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.034 ms

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.031 ms

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.034 ms

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.031 ms

--- 9.0.0.2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.031/0.032/0.034/0.006 ms

switch# ping localhost vrf red

PING localhost (127.0.0.1) 100(128) bytes of data.

108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.048 ms

108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.052 ms

108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.044 ms

108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.036 ms

108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.055 ms

--- localhost ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4005ms

rtt min/avg/max/mdev = 0.036/0.047/0.055/0.006 ms

switch# ping localhost vrf mgmt

PING localhost (127.0.0.1) 100(128) bytes of data.

108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.085 ms

108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.057 ms

108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.047 ms

108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.038 ms

108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.059 ms

--- localhost ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.038/0.057/0.085/0.016 ms
Pinging a server with the intermediate router time stamp:

Public

ping 79

switch# ping 9.0.0.2 ip-option include-timestamp

PING 9.0.0.2 (9.0.0.2) 100(168) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.031 ms

TS:     59909005 absolute

        0

        0

        0

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.034 ms

TS:     59910005 absolute

        0

        0

        0

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.038 ms

TS:     59911005 absolute

        0

        0

        0

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.035 ms

TS:     59912005 absolute

        0

        0

        0

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.037 ms

TS:     59913005 absolute

        0

        0

        0

--- 9.0.0.2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.031/0.035/0.038/0.002 ms
Pinging a server with the intermediate router time stamp and address:

switch# ping 9.0.0.2 ip-option include-timestamp-and-address

PING 9.0.0.2 (9.0.0.2) 100(168) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.030 ms

TS:     9.0.0.2 60007355 absolute

        9.0.0.2 0

        9.0.0.2 0

        9.0.0.2 0

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.037 ms

TS:     9.0.0.2 60008355 absolute

        9.0.0.2 0

        9.0.0.2 0

        9.0.0.2 0

Public

ping 80

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.037 ms

TS:     9.0.0.2 60009355 absolute

        9.0.0.2 0

        9.0.0.2 0

        9.0.0.2 0

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.038 ms

TS:     9.0.0.2 60010355 absolute

        9.0.0.2 0

        9.0.0.2 0

        9.0.0.2 0

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.039 ms

TS:     9.0.0.2 60011355 absolute

        9.0.0.2 0

        9.0.0.2 0

        9.0.0.2 0

--- 9.0.0.2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.030/0.036/0.039/0.005 ms
Pinging a server with the intermediate router address:

switch# ping 9.0.0.2 ip-option record-route

PING 9.0.0.2 (9.0.0.2) 100(168) bytes of data.

108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.034 ms

RR:     9.0.0.2

        9.0.0.2

        9.0.0.2

        9.0.0.2

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.038 ms (same route)

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.036 ms (same route)

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.037 ms (same route)

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.035 ms (same route)

--- 9.0.0.2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.034/0.036/0.038/0.001 ms
Pinging a server with do-not-fragment:

switch# ping 192.168.1.8 datagram-size 2000 do-not-fragment

PING 192.168.1.8 (192.168.1.8) 2000(2028) bytes of data.

2008 bytes from 192.168.1.8: icmp_seq=1 ttl=64 time=0.721 ms

2008 bytes from 192.168.1.8: icmp_seq=2 ttl=64 time=0.792 ms
2008 bytes from 192.168.1.8: icmp_seq=3 ttl=64 time=0.857 ms
2008 bytes from 192.168.1.8: icmp_seq=4 ttl=64 time=0.833 ms

2008 bytes from 192.168.1.8: icmp_seq=5 ttl=64 time=0.836 ms

--- 192.168.1.8 ping statistics ---

Public

ping 81

5 packets transmitted, 5 received, 0% packet loss, time 4056ms

rtt min/avg/max/mdev = 0.721/0.807/0.857/0.048 ms

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

ping6

Syntax

ping6 {<IPv6-ADDR> | <HOSTNAME>} [data-fill <PATTERN> | datagram-size

<SIZE> |

   interval <TIME> | repetitions <NUMBER> | timeout <TIME>

             |

   vrf <VRF-NAME> | source <IPv6-ADDR> | <IFNAME>]

Description

Pings the specified IPv6 address or hostname with or without optional parameters.

Parameter

IPv6‐ADDR

HOSTNAME

data‐fill <PATTERN>

Description

Selects the IPv6 address to ping.

Selects the hostname to ping. Range: 1‐256 characters

Specifies the data pattern in hexadecimal digits to send. A maxi
mum of 16 "pad" bytes can be specified to fill out the ICMP pac
ket. Default: AB

Public

ping6 82

Parameter

Description

datagram‐size <SIZE>

Specifies the ping datagram size. Range: 0‐65399, default: 10
0.

interval <TIME>

Specifies the interval between successive ping requests in seco
nds. Range: 1‐60 seconds, default: 1 second.

repetitions <NUMBER>

Specifies the number of packets to send. Range: 1‐10000 pac
kets, default: Five packets.

Specifies the ping timeout in seconds. Range: 1‐60 seconds, d
efault: 2 seconds.

Specifies the virtual routing and forwarding (VRF) to use. When
this option is not provided, the default VRF is used.

Specifies the source IPv6 address or interface to use.

timeout <TIME>

vrf <VRF‐NAME>

source <IPv6‐ADDR> |
<IFNAME>

Examples

Pinging an IPv6 address:

switch# ping6 2020::2

PING 2020::2(2020::2) 100 data bytes

108 bytes from 2020::2: icmp_seq=1 ttl=64 time=0.386 ms

108 bytes from 2020::2: icmp_seq=2 ttl=64 time=0.235 ms

108 bytes from 2020::2: icmp_seq=3 ttl=64 time=0.249 ms

108 bytes from 2020::2: icmp_seq=4 ttl=64 time=0.240 ms

108 bytes from 2020::2: icmp_seq=5 ttl=64 time=0.252 ms

--- 2020::2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4000ms

rtt min/avg/max/mdev = 0.235/0.272/0.386/0.059 ms
Pinging the localhost:

switch# ping6 localhost

PING localhost(localhost) 100 data bytes

108 bytes from localhost: icmp_seq=1 ttl=64 time=0.093 ms

108 bytes from localhost: icmp_seq=2 ttl=64 time=0.051 ms

108 bytes from localhost: icmp_seq=3 ttl=64 time=0.055 ms

108 bytes from localhost: icmp_seq=4 ttl=64 time=0.046 ms
108 bytes from localhost: icmp_seq=5 ttl=64 time=0.048 ms

--- localhost ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3998ms

rtt min/avg/max/mdev = 0.046/0.058/0.093/0.019 ms

Public

ping6 83

Pinging a server with a data pattern:

switch# ping6 2020::2 data-fill ab

PATTERN: 0xab

PING 2020::2(2020::2) 100 data bytes

108 bytes from 2020::2: icmp_seq=1 ttl=64 time=0.038 ms

108 bytes from 2020::2: icmp_seq=2 ttl=64 time=0.074 ms

108 bytes from 2020::2: icmp_seq=3 ttl=64 time=0.076 ms

108 bytes from 2020::2: icmp_seq=4 ttl=64 time=0.075 ms

108 bytes from 2020::2: icmp_seq=5 ttl=64 time=0.077 ms

--- 2020::2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.038/0.068/0.077/0.015 ms
Pinging a server with a datagram size:

switch# ping6 2020::2 datagram-size 200

PING 2020::2(2020::2) 200 data bytes

208 bytes from 2020::2: icmp_seq=1 ttl=64 time=0.037 ms

208 bytes from 2020::2: icmp_seq=2 ttl=64 time=0.076 ms

208 bytes from 2020::2: icmp_seq=3 ttl=64 time=0.076 ms

208 bytes from 2020::2: icmp_seq=4 ttl=64 time=0.077 ms

208 bytes from 2020::2: icmp_seq=5 ttl=64 time=0.066 ms

--- 2020::2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3999ms

rtt min/avg/max/mdev = 0.037/0.066/0.077/0.016 ms
Pinging a server with an interval specified:

switch# ping6 2020::2 interval 5

PING 2020::2(2020::2) 100 data bytes

108 bytes from 2020::2: icmp_seq=1 ttl=64 time=0.043 ms

108 bytes from 2020::2: icmp_seq=2 ttl=64 time=0.075 ms

108 bytes from 2020::2: icmp_seq=3 ttl=64 time=0.074 ms

108 bytes from 2020::2: icmp_seq=4 ttl=64 time=0.075 ms

108 bytes from 2020::2: icmp_seq=5 ttl=64 time=0.075 ms

--- 2020::2 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 19999ms

rtt min/avg/max/mdev = 0.043/0.068/0.075/0.014 ms
Pinging a server with a specified number of packets to send:

switch# ping6 2020::2 repetitions 6

PING 2020::2(2020::2) 100 data bytes

108 bytes from 2020::2: icmp_seq=1 ttl=64 time=0.039 ms
108 bytes from 2020::2: icmp_seq=2 ttl=64 time=0.070 ms

108 bytes from 2020::2: icmp_seq=3 ttl=64 time=0.076 ms

108 bytes from 2020::2: icmp_seq=4 ttl=64 time=0.076 ms

108 bytes from 2020::2: icmp_seq=5 ttl=64 time=0.071 ms

Public

ping6 84

108 bytes from 2020::2: icmp_seq=6 ttl=64 time=0.078 ms

--- 2020::2 ping statistics ---

6 packets transmitted, 6 received, 0% packet loss, time 4999ms

rtt min/avg/max/mdev = 0.039/0.068/0.078/0.015 ms

switch# ping6 localhost vrf red

PING localhost(localhost) 100 data bytes

108 bytes from localhost: icmp_seq=1 ttl=64 time=0.038 ms

108 bytes from localhost: icmp_seq=2 ttl=64 time=0.050 ms

108 bytes from localhost: icmp_seq=3 ttl=64 time=0.039 ms

108 bytes from localhost: icmp_seq=4 ttl=64 time=0.040 ms

108 bytes from localhost: icmp_seq=5 ttl=64 time=0.027 ms

--- localhost ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4001ms

rtt min/avg/max/mdev = 0.027/0.038/0.050/0.010 ms

switch# ping6 localhost vrf mgmt

PING localhost(localhost) 100 data bytes

108 bytes from localhost: icmp_seq=1 ttl=64 time=0.032 ms

108 bytes from localhost: icmp_seq=2 ttl=64 time=0.022 ms

108 bytes from localhost: icmp_seq=3 ttl=64 time=0.040 ms

108 bytes from localhost: icmp_seq=4 ttl=64 time=0.022 ms

108 bytes from localhost: icmp_seq=5 ttl=64 time=0.046 ms

--- localhost ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 3998ms

rtt min/avg/max/mdev = 0.022/0.032/0.046/0.010 ms

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Public

ping6 85

Troubleshooting

Subtopics

Operation not permitted
Network is unreachable
Destination host unreachable

Operation not permitted

Symptom

The switch displays an  operation not permitted  message when a user attempts to send a ping
request.

Example:

switch# ping 100.1.2.10

PING 100.1.2.10 (100.1.2.10) 100(128) bytes of data

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

--- 100.1.2.10 ping statistics ---

5 packets transmitted, 0 received, 100% packet loss, time 4000ms

Cause

When an ACL is applied to the Control Plane, sending a ping request may be denied. If the ping packet
matches a drop entry in the ACL, applying a Control Plane may block traffic sent from the switch CLI ping
command.

When this situation occurs, the following error message is displayed:  ping: sendmsg: Operation
not permitted . The message indicates that the ICMP echo request packet has not been sent and is
blocked by the Control Plane ACL.

When this message is not displayed, the ping request packet has been sent correctly. A ping failure in this
case represents a failure to receive the ICMP echo reply packet.

Action

1.  Modify the ACL to allow the ping traffic.

2.  Unapply the ACL from egress (8400/8320/8325/9300/9300S switches) or Control Plane.

Public

Troubleshooting 86

3.  Ping a destination which is not matched by the ACL. For example, if the ACL is blocking traffic based

on destination IP. Depending on the ACL content, this might not always be possible like when the ACL
blocks all ICMP packets.

Network is unreachable

Symptom

User receives a "network is unreachable" message on sending a ping request.

Cause

The ping packet did not get sent, because the switch cannot find an interface with a route that leads to the
destination for one of the following reasons:

•  A configuration error, such as an interface having an incorrect IP address or subnet defined.

•  DHCP having failed to assign an address at all.

•  The user meant to ping out the management vrf, but forgot to add  vrf mgmt  to the ping command.

Action

Adjust the switch configuration to ensure that a route to the destination network exists.

Destination host unreachable

Symptom

User receives a  Destination host unreachable  message on sending a ping request.

Cause

This issue typically indicates that the host is down or otherwise not returning ICMP echo requests. It is also
possible that an intermediate network hop is dropping the packets.

Action

Investigate whether an intermediate hop is not returning pings by using the traceroute command. Check the
intermediate hop, and then the endpoint. If the destination is another switch, it is possible that Ingress ACLs
on that switch are blocking ping packets. In such cases, the configuration option on the destination switch
should be examined.

Public

Network is unreachable 87

Troubleshooting

Subtopics

Operation not permitted
Network is unreachable
Destination host unreachable

Operation not permitted

Symptom

The switch displays an  operation not permitted  message when a user attempts to send a ping
request.

Example:

switch# ping 100.1.2.10

PING 100.1.2.10 (100.1.2.10) 100(128) bytes of data

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

ping: sendmsg: Operation not permitted

--- 100.1.2.10 ping statistics ---

5 packets transmitted, 0 received, 100% packet loss, time 4000ms

Cause

When an ACL is applied to the Control Plane, sending a ping request may be denied. If the ping packet
matches a drop entry in the ACL, applying a Control Plane may block traffic sent from the switch CLI ping
command.

When this situation occurs, the following error message is displayed:  ping: sendmsg: Operation
not permitted . The message indicates that the ICMP echo request packet has not been sent and is
blocked by the Control Plane ACL.

When this message is not displayed, the ping request packet has been sent correctly. A ping failure in this
case represents a failure to receive the ICMP echo reply packet.

Action

1.  Modify the ACL to allow the ping traffic.

2.  Unapply the ACL from egress (8400/8320/8325/9300/9300S switches) or Control Plane.

Public

Troubleshooting 88

3.  Ping a destination which is not matched by the ACL. For example, if the ACL is blocking traffic based

on destination IP. Depending on the ACL content, this might not always be possible like when the ACL
blocks all ICMP packets.

Network is unreachable

Symptom

User receives a "network is unreachable" message on sending a ping request.

Cause

The ping packet did not get sent, because the switch cannot find an interface with a route that leads to the
destination for one of the following reasons:

•  A configuration error, such as an interface having an incorrect IP address or subnet defined.

•  DHCP having failed to assign an address at all.

•  The user meant to ping out the management vrf, but forgot to add  vrf mgmt  to the ping command.

Action

Adjust the switch configuration to ensure that a route to the destination network exists.

Destination host unreachable

Symptom

User receives a  Destination host unreachable  message on sending a ping request.

Cause

This issue typically indicates that the host is down or otherwise not returning ICMP echo requests. It is also
possible that an intermediate network hop is dropping the packets.

Action

Investigate whether an intermediate hop is not returning pings by using the traceroute command. Check the
intermediate hop, and then the endpoint. If the destination is another switch, it is possible that Ingress ACLs
on that switch are blocking ping packets. In such cases, the configuration option on the destination switch
should be examined.

Public

Network is unreachable 89

U
s
i
n
g

c
l
a
s
s
i
fi
e
r

p
o
l
i
c
i
e
s

f
o
r

t
r
a
ff
i
c

c
a
p
t
u
r
e

a
n
d

.
.
.

Using classifier policies for traffic capture and analysis

AOS-CX can use a classifier policy to troubleshooting network issues by mirroring packets for capture and
analysis.

The process to filter mirrored traffic requires hardware resources, and this process may compete for these
resources with other configured features, including existing Classifier Policies and Access Control Lists
(ACLs). Prior to configuring and installing a policy for troubleshooting purposes, issue the show policy
commands and show resources commands to determine what existing features are consuming hardware
resources on the switch. This will also help to ensure that configurations created for troubleshooting are not
overriding existing configurations. If a switch already has a classifier policy applied to one context (applied
globally, interface, VLAN), consider adding entries to that policy, temporarily unapplying the existing policy,
or applying the troubleshooting policy to a different context.

NOTE

Classifier Policies cannot capture traffic on the out-of-band management port. If
the port is out-of-band, its packets do not enter or leave through the switch ASIC,
which is required for mirroring operations.

Step one: create a traffic class

The following example creates a traffic class to match traffic to be mirrored for future evaluation. In this
example:

•  TCP and UDP protocols should include entries for both source and destination port matches in order to

mirror traffic either to or from that port number.

•  traffic utilizes HTTPS and therefore will match that entry.

•

In this example, the count keyword is included so that hit counts can be monitored to verify that traffic is
matching the class entries.

•  The last entry (ignore any any any count) is included to count packets of all other traffic types passing
through the device, and to confirm other traffic is reaching the policy for evaluation, and not being
mirrored.

•  Sequence numbers (for example, 10, 20, 30) are not mandatory when creating class entries, and will be

auto-generated if not manually specified.

•  Comment lines are optional for functionality but included for clarity.

switch(config)# class ip support-mirror

  10 comment OSPF protocol
  10 match ospf any any count
  20 comment GRE protocol

  20 match gre any any count

  30 comment BGP dst port

  30 match tcp any any eq bgp count

Public

Using classifier policies for traffic capture and ... 90

40 comment BGP src port

  40 match tcp any eq bgp any count

  50 comment VxLAN dst port

  50 match udp any any eq vxlan count

  60 comment VxLAN src port

  60 match udp any eq vxlan any count

  70 comment RADIUS authentication dst port

  70 match udp any any eq radius count

  80 comment RADIUS authentication src port

  80 match udp any eq radius any count

  90 comment HTTPS dst port

  90 match tcp any any eq https count

  100 comment HTTPS src port

  100 match tcp any eq https any count

  110 comment HTTP dst port

  110 match tcp any any eq http count

  120 comment HTTP src port

  120 match tcp any eq http any count

  130 comment ICMP Echo (Ping)

  130 match icmp any any icmp-type echo count

  140 comment ICMP Echo (Ping) Reply

  140 match icmp any any icmp-type echo-reply count

  150 comment Count all other traffic

  150 ignore any any any count

exit

Step two: create a policy

Create a policy that uses the class created in the previous step and sends matching traffic to mirror session
1:

switch(config)# policy support-mirror

10 class ip support-mirror action mirror 1
exit

Step three: apply the policy

If you do not know which interface or VLAN the relevant traffic uses to enter the switch, apply the policy
globally. Alternatively, you can apply the policy to one ore more specific contexts. Note that while it is
possible to apply policies to multiple interfaces, interface types, and directions, each application consume a
hardware resources and may not be successful if resources are exhausted.

Apply the policy globally in the ingress (in) direction:

apply policy support-mirror in
Apply a policy to a specific physical interface in the ingress (in) direction:

Public

Using classifier policies for traffic capture and ... 91

switch (config)# interface 1/1/1

switch(config-if)# apply policy support-mirror in
Apply a policy to a specific physical interface in Egress (out) direction:

NOTE

4100i, 6000 and 6100 Switch series do not support egress physical interface
policies.

switch (config)#interface 1/1/1

switch(config-if)# apply policy support-mirror out
Apply a policy to a specific LAG in Ingress (in) direction:

switch (config)# interface lag 1

switch(config-lag-if)# apply policy support-mirror in
Apply a policy to a specific LAG in Egress (out) direction:

NOTE

4100i, 6000 and 6100 Switch series do not support egress physical interface
policies.

switch (config)# interface lag 1

switch(config-lag-if)# apply policy support-mirror out
Apply a policy to a specific VLAN in Ingress (in) direction:

switch (config)# vlan 100

switch(config-if-vlan)# apply policy support-mirror in
Apply a policy to a specific VLAN in Egress (out) direction:

NOTE

4100i, 6000 and 6100 Switch series do not support egress physical interface
policies.

switch (config)# vlan 100

switch(config-if-vlan)# apply policy support-mirror out

Step four: confirm policy Installation

The output of the show class and show policy commands should include the configuration that was
configured in the previous steps. The output must not include any lines starting with an exclamation point
(!), such as:

! policy support-mirror user configuration does not match active

configuration.

Public

Using classifier policies for traffic capture and ... 92

A message that starts with exclamation point (!), indicates a policy installation failure, possibly due to
hardware resource limitations.

Step five: confirm policy resource consumption

Next, confirm that the ingress global policy lookup process is consuming TCAM entries. If the switch is a
chassis, each module should show resources consumed, as this policy is installed on the ASIC in each line
card. The following example of shows the output of a show resources command issued on a 6300 switch:

6300(config)# show resources

Resource Usage:

Mod  Description

Resource                                   Used Reserved    Free

----------------------------------------------------------------------------

--

1/1  Ingress Global Policy Lookup

Ingress TCAM Entries                         35     2048

Total

Ingress TCAM Entries                         35     2048   18432

Egress TCAM Entries                           0        0    8192

Ingress Lookups                               1                8

Ingress Flex Lookups                          0                1

Egress Lookups                                0                4

Ingress Policers                              0             2047

Egress Policers                               0             2047
Hardware resources will be consumed on each module that has a policy applied to an interface. Ingress and
egress policies consume separate hardware resources. The following example shows the output of a show
resources command issued on a 6300 switch with a policy applied to a physical interface in both in and out
directions:

6300(config)# show resources

Resource Usage:

Mod  Description

Resource                                   Used Reserved    Free

----------------------------------------------------------------------------

--

1/1  Ingress Port Policy Lookup

Ingress TCAM Entries                         37     2048

Egress Port Policy Lookup

Egress TCAM Entries                          37     2048

Total

Ingress TCAM Entries                         37     2048   18432

Egress TCAM Entries                          37     2048    6144

Ingress Lookups                               1                8

Ingress Flex Lookups                          0                1

Egress Lookups                                1                3

Public

Using classifier policies for traffic capture and ... 93

Ingress Policers                              0             2047

Egress Policers                               0             2047

Step six: configure a mirror session

In this example, the mirror session will be configured to send traffic to the switch CPU for capture:

switch(config)# mirror session 1

switch(config-mirror-1) destination cpu

switch(config-mirror-1) enable
You may also choose to mirror packets to an external capture host, such as a workstation running Wireshark
for live packet analysis and further filtering. See .

Step seven: start packet capture

Start a packet capture using TShark.

switch# diag utilities tshark
Traffic should be captured and dumped to screen. The following example displays partial TShark output
when a ping packet is sent through the switch:

switch# diag utilities tshark

Inspecting traffic mirrored to the CPU until Ctrl-C is entered.

Frame 1: 98 bytes on wire (784 bits), 98 bytes captured (784 bits) on

interface MirrorRxNet, id 0

Interface id: 0 (MirrorRxNet)

Interface name: MirrorRxNet

Encapsulation type: Ethernet (1)

Arrival Time: Jul 18, 2023 22:45:21.213862080 UTC

[Time shift for this packet: 0.000000000 seconds]

Epoch Time: 1689720321.213862080 seconds

[Time delta from previous captured frame: 0.000000000 seconds]

[Time delta from previous displayed frame: 0.000000000 seconds]

[Time since reference or first frame: 0.000000000 seconds]

Frame Number: 1
Frame Length: 98 bytes (784 bits)

Capture Length: 98 bytes (784 bits)

[Frame is marked: False]

[Frame is ignored: False]

[Protocols in frame: eth:ethertype:ip:icmp:data]

...

Step eight: capture packets to a file or mirror it to a host

Once basic policy configuration is confirmed as working as expected, you can use the diag utilities tshark
file command to capture the TShark output to a file.

Public

Using classifier policies for traffic capture and ... 94

switch# diag utilities tshark file

NOTE

This command will store packets to a circular file; only the most recent 32MB of
traffic will be captured.

Use the following command to copy a pcap file to a remote device:

switch# copy tshark-pcap ?

REMOTE_URL  URL syntax - sftp://USER@{IP|HOST}[:PORT]/FILE or

tftp://{IP|HOST}[:PORT][;blocksize=VAL]/FILE
If you do not want to capture the TShark output to a file, you can mirror it to an external capture host. In the
following example, packets are mirrored to external capture host (such as a workstation with WireShark) is
connected to interface 1/1/2:

switch(config)# mirror session 1

switch(config-mirror-1)# destination interface 1/1/2

switch(config-mirror-1)# enable

Step nine: check packet hit counts

Use the show policy hitcounts command to confirm that the policy is evaluating traffic.

switch(config)# show policy hitcounts
In the following example, no ICMP echo reply packets are captured, as the policy globally is applied to
ingress traffic only. Remember, AOS-CX does not support applying policies globally in the

egress direction; You must apply a policy to a specific context (an interface, VLAN, or LAG) to monitor egress
traffic.

switch# show policy hitcounts support-mirror

Statistics for Policy support-mirror:

global (in):

Matched Packets  Configuration

10 class ip support-mirror action mirror 1

0  10 match ospf any any count
0  20 match gre any any count

0  30 match tcp any any eq bgp count

0  40 match tcp any eq bgp any count

0  50 match udp any any eq vxlan count

0  60 match udp any eq vxlan any count

0  70 match udp any any eq radius count

0  80 match udp any eq radius any count

0  90 match tcp any any eq https count

0  100 match tcp any eq https any count

0  110 match tcp any any eq http count

0  120 match tcp any eq http any count

5  130 match icmp any any icmp-type echo count

Public

Using classifier policies for traffic capture and ... 95

0  140 match icmp any any icmp-type echo-reply count

0  150 ignore any any any count
In this example, hit counts will be shown separately for each application of a policy and will reflect the
direction of the traffic (that is, ICMP echo packets entering the switch and ICMP echo reply packets leaving
the switch.)

6300(config-if)# show policy hitcounts support-mirror

 Statistics for Policy support-mirror:

 Interface 1/1/1 (in):

 Matched Packets  Configuration

     0    10 class ip support-mirror action mirror 1

     0  10 match ospf any any count

     0  20 match gre any any count

     0  30 match tcp any any eq bgp count

     0  40 match tcp any eq bgp any count

     0  50 match udp any any eq vxlan count

     0  60 match udp any eq vxlan any count

     0  70 match udp any any eq radius count

     0  80 match udp any eq radius any count

     0  90 match tcp any any eq https count

     0  100 match tcp any eq https any count

     0  110 match tcp any any eq http count

     0  120 match tcp any eq http any count

     0  130 match icmp any any icmp-type echo count

     0  140 match icmp any any icmp-type echo-reply count

     0  150 ignore any any any count

 Interface 1/1/1 (out):

 Matched Packets  Configuration

     10 class ip support-mirror action mirror 1

     0  10 match ospf any any count

     0  20 match gre any any count

     0  30 match tcp any any eq bgp count

     0  40 match tcp any eq bgp any count
     0  50 match udp any any eq vxlan count

     0  60 match udp any eq vxlan any count

     0  70 match udp any any eq radius count

     0  80 match udp any eq radius any count

     0  90 match tcp any any eq https count

     0  100 match tcp any eq https any count

     0  110 match tcp any any eq http count

     0  120 match tcp any eq http any count

     0  130 match icmp any any icmp-type echo count

     5  140 match icmp any any icmp-type echo-reply count

     0  150 ignore any any any count

Public

Using classifier policies for traffic capture and ... 96

Remote syslog

Remote syslog enables the forwarding of syslog messages to the remote syslog server. The feature supports
a maximum of eight remote syslog servers. Only one configuration per remote syslog server is allowed.
The remote syslog server supports TCP and UDP transport protocols and TLS to establish a connection. In
addition to forwarding logs to the remote server, they can also be preserved in local storage.

When the client certificate associated with the syslog client is updated, the syslog client is restarted and a
new TLS connection is established using the updated client certificate.

Syslog over VXLAN support

Syslog message is supported over VxLAN with IPv4 or IPv6 underlay.

Subtopics

Remote syslog commands

Remote syslog commands

Select a command from the list in the left navigation menu.

Subtopics

clear accounting-logs
diag persistent-storage
logging
logging accounting-format-native
logging filter
logging facility
logging persistent-storage

clear accounting-logs

Syntax

clear accounting-logs

Public

Remote syslog 97

Description

Use this command to clear accounting logs. Once issued, only logs generated after this command is run will
be displayed in the output of the show accounting log commands.

NOTE

This command will not clear logs when the logging accounting-format-native
feature is configured. To clear accounting logs on switches with this feature
enabled, users should first revert the native accounting format back to the
default AOS-CX format by executing the no logging accounting-format-native
command.

Example

switch(config)# clear accounting-logs

The following example shows that accounting logs cannot be cleared using the clear accounting-logs
command if the logging accounting-native-format command has been enabled, and that disabling this
option with the no logging accounting-format-native command again allows the accounting logs to be
cleared.

switch# logging audit-format-native

switch# clear accounting-logs

Warning: Clear accounting-logs is not supported for 'audit-format-native'.

switch# no logging audit-format-native

switch# clear accounting-logs

switch# show accounting log last 5

---------------------------------------------------

Command logs from current boot

---------------------------------------------------

No command logs has been logged in the system

Command History

Release

10.11

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Administrators or local user group members with execution righ
ts for this command.

Public

clear accounting-logs 98

diag persistent-storage

Syntax

diag persistent-storage enable [{severity <LEVEL> | timeout <TIMEOUT> |

filter <FILTER_NAME> | storage-writes <STORAGE_WRITES> | usb <STORAGE_URL>}]

diag persistent-storage disable

Description

Enables or disables storage of logs in storage. Only logs of the specified severity and above will be preserved
in the storage.

NOTE

To switch the persistent storage setting from one option (e.g., USB) to another
(e.g., storage-writes), you must first disable persistent storage by running the
command diag persistent-storage disable. that the storage-writes option applies
only to local storage and does not work with USB.

Parameter

enable

disable

Description

Enable persistent logging.

Disable persistent logging.

severity <LEVEL>

Specifies the severity of the syslog messages:

•  alert: Preserves syslog messages with the severity of alert

(6) and emergency (7)

•  crit: Preserves syslog messages with the severity of critical

(5) and above. Default.

•  debug: Preserves syslog messages with the severity of deb

ug (0) and above.

•  emer: Preserves syslog messages with the severity of eme

rgency (7) only.

•  err: Preserves syslog messages with the severity of err (4)

•

and above.
info: Preserves syslog messages with the severity of info (1
) and above.

•  notice: Preserves syslog messages with the severity of noti

ce (2) and above.

Public

diag persistent-storage 99

Parameter

Description

•  warn: Preserves syslog messages with the severity of warn

ing (3) and above.

filter <FILTER_NAME>

Preserve logs for specified filter name.

timeout <TIMEOUT>

Preserve logs for specified duration. Range: 1 to 60 minutes. De
fault: 20 minutes.

storage‐writes
<STORAGE_WRITES>

Limit the amount of storage writes.

usb <STORAGE_URL>

Preserve logs in the USB storage.

Examples

Enabling storage of logs in storage with severity err and timeout 30 minutes:

switch(config)#diag persistent-storage enable severity err timeout 30

Logs will be written to storage. Prolonged usage of persistent logging can

affect lifetime of storage. Hence enable persistent logging only for short

duration and also for the right severity.

Do you want to continue (y/n)? y
Enabling storage of logs in storage with severity err and timeout 30 minutes and 512 storage-writes:

switch(config)#diag persistent-storage enable severity err timeout 30

storage-writes 512

Logs will be written to storage. Prolonged usage of persistent logging can

affect lifetime of storage. Hence enable persistent logging only for short

duration and also for the right severity.

Do you want to continue (y/n)? y
Disabling log storage:

switch(config)# diag persistent-storage disable

Command History

Release

10.17

Modification

Command introduced.

Public

diag persistent-storage 100

Command Information

Platforms

Command context

Authority

All platforms

config

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

logging

Syntax

logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} {udp [<PORT-NUM>]}|

{tcp [<PORT-NUM>]}|{|tls [<PORT-NUM>]}

   auth-mode {certificate|subject-name}

   disable

   filter <FILTER-NAME>

   include-auditable-events

   legacy-tls-renegotiation]

   rate-limit-burst <BURST>

   rate-limit-interval <INTERVAL>] ]

   severity <LEVEL>]

   vrf <VRF-NAME>]

no logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME> }

Description

Enables syslog forwarding to a remote syslog server.

The no form of this command disables syslog forwarding to a remote syslog server.

Starting with AOS-CX 10.11, payload information is present in accounting logs.

The maximum REST payload that can be sent to RADIUS/TACACS server is 1024 characters, and the
maximum of REST payload that can be sent to syslog server is 3500 characters. If this limit is is reached, the
log will display three dots (...) to indicate that the log an exceeded the character limit and is incomplete.

Parameter

Description

{<IPV4‐ADDR> | <IPV6‐ADDR>
| <HOSTNAME>}

Selects the IPv4 address, IPv6 address, or host name of the rem
ote syslog server. Required.

Public

logging 101

Parameter

Description

[udp [<PORT‐NUM>] | tcp
[<PORT‐NUM> |
  tls [<PORT‐NUM>]]

Specifies the UDP port, TCP port, or TLS port of the remote sysl
og server to receive the forwarded syslog messages.

   udp [<PORT‐NUM>]

Range: 1 to 65535. Default: 514

   tcp [<PORT‐NUM>]

Range: 1 to 65535. Default: 1470

   tls [<PORT‐NUM>]

Range: 1 to 65535. Default: 6514

auth‐mode

disable

Specifies the TLS authentication mode used to validate the cert
ificate.

•  certificate: Validates the peer using trust anchor certificate

based authentication. Default.

•  subject‐name: Validates the peer using trust anchor certif

icates as well as subject‐name based authentication.

Disable remote syslog confguration. This does not delete the co
nfiguration, just disables/pauses the forwarding of syslog mess
agesto the remote server. The config/forwarding can be reenabl
ed (un‐paused) again using the no logging <hostname> disa
ble command.

filter <FILTER‐NAME>

Specifies the name of the filter to be applied on the syslog mes
sages.

include‐auditable‐events

Specifies that auditable messages are also logged to the remote
syslog server.

legacy‐tls‐renegotiation

Enables the TLS connection with a remote syslog server suppor
ting legacy renegotiation.

rate‐limit‐burst <BURST>

Specifies the rate limit for the messages sent to the remote sysl
og server.

rate‐limit‐interval
<INTERVAL>

Specifies the rate limit interval in seconds. Default: 30 Seconds

severity <LEVEL>

Specifies the severity of the syslog messages:

•  alert: Forwards syslog messages with the severity of alert

(6) and emergency (7).

•  crit: Forwards syslog messages with the severity of critical

(5) and above.

Public

logging 102

Parameter

Description

•  debug: Forwards syslog messages with the severity of deb

ug (0) and above.

•  emerg: Forwards syslog messages with the severity of eme

rgency (7) only.

•  err: Forwards syslog messages with the severity of err (4) a

•

nd above
info: Forwards syslog messages with the severity of info (1
) and above. Default.

•  notice: Forwards syslog messages with the severity of notic

e (2) and above.

•  warning: Forwards syslog messages with the severity of wa

rning (3) and above.

Specifies the VRF used to connect to the syslog server. Optional
. Default:  default

vrf <VRF‐NAME>

Examples

Enabling the syslog forwarding to remote syslog server 10.0.10.2:

switch(config)# logging 10.0.10.2

Enabling the syslog forwarding of messages with a severity of err (4) and above to TCP port 4242 on
remote syslog server 10.0.10.9 with VRF lab_vrf:

switch(config)# logging 10.0.10.9 tcp 4242 severity err vrf lab_vrf

Disabling syslog forwarding to a remote syslog server:

switch(config)# no logging

Enabling syslog forwarding over TLS to a remote syslog server using subject-name authentication mode:

switch(config)#logging example.com tls auth-mode subject-name

Applying log filtering for syslog server forwarding:

switch(config)# logging 10.0.10.6 severity info filter filter_lldp_logs vrf

mgmt

Applying log filtering and enabling the rate limit for syslog server forwarding over TCP port:

switch(config)# logging 10.0.10.2 tcp 3440 severity err vrf mgmt include-

auditable-events filter filter_lldp_logs rate-limit-burst 3 rate-limit-

Public

logging 103

interval 35

Command History

Release

Modification

10.12.1000

The disable parameter is introduced

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logging accounting-format-native

Syntax

logging accounting-format-native

[no] logging accounting-format-native

Description

Change the accounting log message format to native Linux format. (Default: AOS-CX format)

The 'no' form of this command will change the accounting log message format to AOS-CX format.

Usage

This option enables the switch to show all types of accounting records to the user. When configured, the
same format will be used while sending messages to syslog servers. When upgrading to this version of from
AOS-CX 10.10 or earlier versions, if native accounting logs are preferred, then best practices is to issue this
command as a part of the upgrade. If the switch upgrades from AOS-CX 10.10 or earlier without configuring
this setting, by default, the accounting log message format will be AOS-CX Format.

Example

This example changes the accounting log message format to native Linux format.

Public

logging accounting-format-native 104

switch(config)# logging accounting-format-native

The following example returns the accounting log message format to the default AOS-CX format.

switch(config)# no logging accounting-format-native

Command History

Release

10.11

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logging filter

Syntax

logging filter <FILTER-NAME>

   [{enable | disable}]

   [<SEQUENCE-ID>] {permit | deny} [event-id <EVENT-ID-RANGE>] [includes

<REGEX>] [severity <COMPARISON-OPERATOR>

            <LEVEL>]

   no <SEQUENCE-ID>

   resequence <OLD-SEQUENCE-ID>

            <NEW-SEQUENCE-ID>

no logging filter <FILTER-NAME>

Description

Creates a filter to restrict what event or debug logs are logged. A filter can be used to either permit or deny:

•  The event logs from being generated on the switch, or

•  The event or debug logs generated on the switch from being forwarded to a syslog server.

Public

logging filter 105

A filter is identified by a filter name and can have up to 20 rules or entries, each with a different sequence
number, matching criteria, and corresponding action (deny or permit). When a filter is applied on a log, the
log is matched against the criteria mentioned in the rules or entries in ascending numerical order of their
sequence numbers until a matching entry is found. Once a matching entry is found, its corresponding action
is applied on the log. If no matching rule is found, the default action (permit) is applied.

The no form of this command removes the filter.

Parameter

Description

Specifies the unique name to identify the filter.

<FILTER‐NAME>

enable

Filter event logs generated on the switch.

<SEQUENCE‐ID>

deny

permit

<event‐id>

Specifies the filter criteria sequence number. Default: Incremen
ts by 10 from the largest sequence‐id currently used in this fil
ter.

Prevents the matching log from being logged.

Allows the matching log.

Matches logs by event ID. Specify an event ID or a range of eve
nt IDs. It supports a maximum of 100 event IDs.

includes <REGEX>

Matches the log message against a regular expression string.

severity

Matches the logs by severity level.

The following options are used to compare the severity:

•  eq: Match events of severity equal to the specified.
•  ge: Match events of severity greater than or equal to the sp

ecified.

•  gt: Match events of severity greater than the specified.
•

le: Match events of severity lesser than or equal to the spec
ified.
lt: Match events of severity lesser than the specified.

•

The following are the severity levels:

•  alert: Logs with the severity alert (6).

Public

logging filter 106

Parameter

Description

•  crit: Logs with the severity critical (5).
•  debug: Logs with the severity debug (0).
•  emerg: Logs with the severity emergency (7).
•  err: Logs with the severity err (4).
•
info: Logs with the severity info (1).
•  notice: Logs with the severity notice (2).
•  warning: Logs with the severity warning (3).

Usage

Filtering event logs on the switch: To permit or deny event logs from being generated on the switch.
In this case, the matching event logs are filtered at generation. The denied event logs are neither logged
to the switch events nor forwarded to any remote syslog servers. Multiple filters can be configured, but
only one filter can be applied to filter the events on the switch. Such a filter can be chosen by adding the
enable command under its configuration. Configuring the enable command under a new filter automatically
removes it from the filter where it was previously used.

For example:

logging filter low_severity_logs

enable

10 deny severity lt info
This configuration denies the event logs which have a severity less than info.

NOTE
If a filter contains enable command, it is not recommended to configure this
filter in the logging command used for remote syslog server configuration. This
is because, any event logs denied by the filter are already not available for
forwarding to a remote server.

A filter with enable command will not affect debug logs. Consider the configuration in the following example
of a filter with enable command and two rules applied 10 permit severity ge info and 20 deny. This implies
permit only those event logs which have severity greater than or equal to info.

Example:

            logging filter low_severity_logs

enable

10 permit severity ge info

20 deny

Filtering event or debug logs when forwarding to a remote syslog server: The filter name must be
configured in the logging command that is used to configure remote syslog server. The logs will be

Public

logging filter 107

generated on the switch and the filter only decides whether to deny or permit the syslog forwarding for the
matching log. For example: logging 10.0.10.6 filter filter_lldp_logs

NOTE
The filter affects debug logs only when the command debug destination syslog
is configured on the switch.

NOTE

The severity mentioned in the remote syslog server configuration using logging
command under configuration context has more precedence than the severity
mentioned in a filter entry. If a log with warning severity is permitted by a filter,
but the remote syslog configuration has severity err mentioned in it, the log will
not be forwarded to the remote syslog server (since warning(3) is lesser than
err(4)). On the other hand, if a log with err severity is permitted by a filter and
the remote syslog configuration has severity warning mentioned in it, the log will
be forwarded to the remote syslog server.

Examples

Configuring a new logging filter:

switch(config)# logging filter example_filter

To deny logs having event ID 1301 and a range of event IDs from 1305 to 1309:

switch(config-logging-filter)# 20 deny event-id 1301,1305-1309

To permit logs having event ID 1300:

switch(config-logging-filter)# 30 permit event-id 1300

To permit logs with severity greater than or equal to  err :

switch(config-logging-filter)# 30 permit severity ge err

To deny logs with severity greater than info:

switch(config-logging-filter)# 30 deny severity gt info

To deny logs with event ID 1024 and a message matching the regular expression LLDP:

switch(config-logging-filter)# 40 deny event-id 1024 includes LLDP

Denying all logs:

Public

logging filter 108

switch(config-logging-filter)# 40 deny

Changing the sequence ID of an existing rule:

switch(config-logging-filter)# resequence 20 70

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config  and  config
‐logging‐filter

Administrators or local user group members with execution righ
ts for this command.

logging facility

Syntax

logging facility {local0 | local1 | local2 | local3 | local4 | local5 |

local6 | local7}

no logging facility

Description

Sets the logging facility to be used for remote syslog messages. Default:  local7

The no form of this command disables the logging facility to be used for remote syslog messages.

Parameter

Description

{local0 | local1 | local2 |

  local3 | local4 | local5

Selects the logging facility to be used for remote syslog messag
es. Required.

Specifies the severity of the syslog messages:

Public

logging facility 109

Parameter

|

  local6 | local7}

Description

•
•
•
•
•
•
•
•

local0
local1
local2
local3
local4
local5
local6
local7

Examples

Sets the local5 logging facility to be used for remote syslog messages:

switch(config)# logging facility local5

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logging persistent-storage

Syntax

logging persistent-storage [severity {alert|crit|debug|emerg|err|info|
notice|warning}]
no logging persistent-storage

Public

logging persistent-storage 110

Description

Enables or disables storage of logs in storage. Only logs of the specified severity and above will be preserved
in the storage.

The no form of this command disables storage of logs in storage.

NOTE

This command is deprecated. Please use "diag persistent-storage" command to
preserve logs in storage.

Parameter

Description

severity <LEVEL>

Specifies the severity of the syslog messages:

•  alert: Preserves syslog messages with the severity of alert

(6) and emergency (7)

•  crit: Preserves syslog messages with the severity of critical

(5) and above. Default.

•  debug: Preserves syslog messages with the severity of deb

ug (0) and above.

•  emerg: Preserves syslog messages with the severity of em

ergency (7) only.

•  err: Preserves syslog messages with the severity of err (4)

•

and above.
info: Preserves syslog messages with the severity of info (1
) and above.

•  notice: Preserves syslog messages with the severity of noti

ce (2) and above.

•  warning: Preserves syslog messages with the severity of

warning (3) and above.

Usage

These logs can be copied out by using the copy support-files all or copy support-files previous-boot.

Examples

Enabling storage of logs in storage with severity info:

switch(config)#logging persistent-storage severity info
Logs will be written to storage and made available across reboot.

Do you want to continue (y/n)?
Disabling storage of logs in storage:

Public

logging persistent-storage 111

switch(config)# no logging persistent-storage

Command History

Release

10.17

Modification

Command deprecated.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Runtime Diagnostics

Run Time diagnostics framework is intended to monitor and validate the health of different hardware
components present in the system. It uses a set of safe hardware diagnostics test cases to validate
the health of different hardware components. These diagnostics test cases are run periodically at every
predetermined interval. Additionally, these hardware diagnostics test cases can be run on demand.

Subtopics

Runtime diagnostic commands

Runtime diagnostic commands

Select a command from the list in the left navigation menu.

Subtopics

diagnostic monitor
diag on-demand
show diagnostic
show diagnostic events

Public

Runtime Diagnostics 112

diagnostic monitor

Syntax

diagnostic monitor {line-module | management-module} [<SLOT-ID>]

no diagnostic monitor {line-module | management-module} [<SLOT-ID>]

Description

Enables runtime diagnostics for all modules or for a specified module. This feature is enabled by default for
all modules.

The no form of this command disables runtime diagnostics for all modules or for a specified module.

Parameter

line‐module

Description

Specifies the enabling of diagnostic monitoring specific to a line
module.

management‐module

Specifies the enabling of diagnostic monitoring specific to a ma
nagement module.

Specifies the slot ID of a module. Format: member/slot.

<SLOT‐ID>

Usage

When no parameters are used in the command (diagnostic monitor or no diagnostic monitor), the
command applies to all modules. This command impacts the diagnostics that run periodically. It does not
affect on-demand diagnostics.

Example

Enabling runtime diagnostics for a specified module:

switch(config)# diagnostic monitor management-module 1/1

Command History

Release

Modification

10.07 or earlier

‐‐

Public

diagnostic monitor 113

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

diag on-demand

Syntax

diag on-demand {line-module | management-module} [<SLOT-ID>]

Description

Runs the diagnostic tests for all modules or for a specified module.

Parameter

Description

[line‐module | management‐
module]

Selects the options for enabling or disabling run‐time diagno
stics for a specific module.

Specifies the enabling of diagnostic monitoring specific to a line
module.

Specifies the enabling of diagnostic monitoring specific to a ma
nagement module.

Specifies the member/slot for management modules (1/1) and li
ne modules (1/1).

line‐module

management‐module

<SLOT‐ID>

Usage

When no parameters are used in the command (diag on-demand), the command applies to all modules.

Examples

Running diagnostic tests for all modules on a 6100 switch:

Public

diag on-demand 114

switch# diag on-demand

Fetching Test results.  Please wait ...

Module               ID    Diagnostics Success

                           Performed

-------------------- ----- ----------- -------

LineModule           1/1           13     100%

ManagementModule     1/1           13     100%
Running diagnostic tests for a specific module on a 6100 switch:

switch# diag on-demand management-module 1/1

Performing diagnostic tests.  Please wait ...

Fetching Test results.  Please wait ...

Module               ID    Diagnostics Success

                           Performed

-------------------- ----- ----------- -------

ManagementModule     1/1           13     100%

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

show diagnostic

Syntax

show diagnostic {line-module | management-module} [<SLOT-ID>] {brief |
detail}

Public

show diagnostic 115

Description

Displays the diagnostic test results for all modules or for a specified module.

Parameter

Description

[line‐module | management‐
module]

Selects the options for enabling or disabling runtime diagnosti
cs for a specific module.

   line‐module

Specifies the enabling of diagnostic monitoring specific to a line
module.

   management‐module

Specifies the enabling of diagnostic monitoring specific to a ma
nagement module.

<SLOT‐ID>

Usage

Specifies the member/slot for management modules (1/1) and li
ne modules (1/1)

When no parameters are used in the command (show diagnostic), the command applies to all modules.

Example

Showing diagnostic test results in brief format for all modules on a 6100 switch:

switch# show diagnostic brief

Module               ID    Diagnostics Success

                           Performed

-------------------- ----- ----------- -------

ManagementModule     1/1           13     100%

LineModule           1/1           13     100%
Showing diagnostic test results in brief format for a specified module on a 6100 switch:

switch# show diagnostic line-module brief

Module               ID    Diagnostics Success

                           Performed

-------------------- ----- ----------- -------

LineModule           1/1           13     100%
Showing diagnostic test results in detail format for all modules on a 6100 switch:

switch# show diagnostic detail

Module : ManagementModule 1/1
Diagnostic     Status Error Code History Code Successive    Total Failure
Total      Last Run Timestamp   First Run Timestamp

                                              Failure Count Count

Iteration

-------------- ------ ---------- ------------ ------------- -------------

Public

show diagnostic 116

---------  -------------------- -------------------

ddr_cecount    Pass   0x0        0x0                      0

0       109  2019-07-31 16:43:38  2019-07-31 07:44:55

emmc           Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

fan_ctrlr      Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

fepld          Pass   0x0        0x0                      0

0       109  2019-07-31 16:43:38  2019-07-31 07:44:54

fru_eeprom     Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:54

fru_eeprom_ul  Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:54

mm_lcb         Pass   0x0        0x0                      0

0       109  2019-07-31 16:43:37  2019-07-31 07:44:54

pmc            Pass   0x0        0x0                      0

0       109  2019-07-31 16:43:37  2019-07-31 07:44:54

rdimm_spd      Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

rdimm_tmp      Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

rtc            Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

tmp1           Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

tmp2           Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:04  2019-07-31 07:44:55

Module : LineModule 1/1

Diagnostic     Status Error Code History Code Successive    Total Failure

Total      Last Run Timestamp   First Run Timestamp

                                              Failure Count Count

Iteration
-------------- ------ ---------- ------------ ------------- -------------

---------  -------------------- -------------------

lc_asic        Pass   0x0        0x0                      0

0       108  2019-07-31 16:43:37  2019-07-31 07:46:03

poe_ctrlr_1_q1 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:03

poe_ctrlr_1_q2 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:04

poe_ctrlr_1_q3 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:04

poe_ctrlr_2_q1 Pass   0x0        0x0                      0

Public

show diagnostic 117

0         4  2019-07-31 16:08:16  2019-07-31 07:46:05

poe_ctrlr_2_q2 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:05

poe_ctrlr_2_q3 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:05

poe_ctrlr_3_q1 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:06

poe_ctrlr_3_q2 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:16  2019-07-31 07:46:06

poe_ctrlr_3_q3 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:17  2019-07-31 07:46:06

poe_ctrlr_4_q1 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:17  2019-07-31 07:46:07

poe_ctrlr_4_q2 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:17  2019-07-31 07:46:07

poe_ctrlr_4_q3 Pass   0x0        0x0                      0

0         4  2019-07-31 16:08:17  2019-07-31 07:46:08

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

show diagnostic events

Syntax

show diagnostic events

Public

show diagnostic events 118

Description

Displays the diagnostic related event logs.

Example

Showing diagnostic related event logs:

switch# show diagnostic events

2019-08-07:17:19:21.214532|hhmd|106001|ERR|

Diagnostic mm_mcbe failed with error code 0x380 on management module 1/1

2019-08-07:17:19:21.214554|hhmd|106001|ERR|

Diagnostic pmc failed with error code 0x4 on management module 1/1

2019-08-07:17:19:21.215532|hhmd|106001|ERR|

Diagnostic ledpld failed with error code 0x4 on management module 1/1

2019-08-07:17:19:21.353221|hhmd|106001|ERR|

Diagnostic mm_mcbe failed with error code 0x380 on management module 1/1

2019-08-07:17:19:21.354421|hhmd|106001|ERR|

Diagnostic pmc failed with error code 0x4 on management module 1/1

2019-08-07:17:19:21.453221|hhmd|106001|ERR|

Diagnostic ledpld failed with error code 0x4 on management module 1/1

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

Service OS

Service OS is an operating system that the customer only uses to fix filesystem corruption, download and
update firmware, and other support related issues. HPE Service OS is a Linux distribution that acts as a

Public

Service OS 119

standalone bootloader and recovery OS for -based switches. It is only accessible if the user is consoled into
the switch. The main high level features provided include:

•  Access to file system partitions for retrieval of logs, coredumps, and configuration for supportability

purposes.

•  Filesystem utilities to format and partition a corrupted storage disk.

•  Management interface networking with TFTP to download and update a product image.

•  Ability to boot primary and secondary firmware images (.SWI file) on the storage disk.

•  Support for clearing the startup-config.

•  Ability to not only clear the admin password for , but also change it in SVOS.

•  Ability to set the secure mode to enhanced or standard.

This document covers the customer CLI commands available in Service OS, as well as a few non-CLI features.

Subtopics

Service OS CLI login
Service OS user accounts
Service OS boot menu
Console configuration
AOS-CX boot
File system access
Service of OS mount failure
Service OS CLI command list
Service OS CLI features and limitations
Service OS CLI commands

Service OS CLI login

Description

If the user enters 0 at the boot menu prompt, they will be presented with a Service OS CLI login prompt. The
user must enter the login account "admin" to log in. By default, Service OS does not require a password.

To reboot without logging in, enter reboot as the login user name.

There are two additional login accounts that execute a command without requiring a password: reboot
and zeroize. Enter the login account reboot to reboot the management module and zeroize to initiate a
zeroization process. The zeroize user account helps a user reset the admin user account's password.

Public

Service OS CLI login 120

Example

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: admin

SVOS>

-----------

-----------

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: reboot

reboot: Restarting system

.

.

Looking for SVOS.

Primary SvOS:  Checking...Loading...Finding...Verifying...Booting...

ServiceOS Information:

    Version:          PL.01.07.0004-internal

    Build Date:       2020-11-23 18:07:42 PST

    Build ID:         ServiceOS:PL.01.07.0004-

internal:133137f635df:202011231807

    SHA:              133137f635dff5778bf3e109eb75825b68d64789

------------------

------------------

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: zeroize

This will securely erase all customer data, including passwords, and

reset the switch to factory defaults.

This action requires proof of physical access via a USB drive.

  * Create a FAT32 formatted USB drive

  * Create a file in the root directory of the USB drive named zeroize.txt

  * Type the following serial number into the zeroize.txt file: CN9ZKRK273

  * Insert the USB drive into the target module

  * Confirm the following prompt to continue

Continue (y/n)? y

############################WARNING############################

This will securely erase all customer data and reset the switch

to factory defaults. This will initiate a reboot and render the

switch unavailable until the zeroization is complete.

This should take several minutes to one hour to complete.

############################WARNING############################

Continue (y/n)? y

reboot: Restarting system

Public

Service OS CLI login 121

Service OS user accounts

Service OS provides a single admin login account. By default, no password is required to log in. Service OS
will require a password if the Service OS admin user account password feature is enabled. This setting can
be enabled or disabled in .

Service OS boot menu

Description

On boot, the user is presented with a Service OS version banner with version, build date, build time, build ID,
and SHA strings.

The user is then shown the boot image profiles.

•  Enter 0 to boot the Service OS login CLI.

•  Enter 1 to boot the primary firmware image.

•  Enter 2 to boot the secondary firmware image.

•

If no input is given within 5 seconds, the default boot profile is selected. Alternatively, press Enter to
select the default boot profile.

The image selected by the user during boot is a run-time decision only and will not persist across reboots.
The default image can be configured using the  boot set-default  command.

Example

ServiceOS Information:

    Version:          PL.01.07.0004-internal

    Build Date:       2020-11-23 18:07:42 PST

    Build ID:         ServiceOS:PL.01.07.0004-

internal:133137f635df:202011231807
    SHA:              133137f635dff5778bf3e109eb75825b68d64789

Boot Profiles:

0. Service OS Console

1. Primary Software Image [PL.10.xx.xxxxx]

2. Secondary Software Image [PL.10.xx.xxxxx]

Select profile(secondary):

ServiceOS Information:
    Version:          RL.01.07.0004-internal
    Build Date:       2020-11-23 18:07:42 PST

    Build ID:         ServiceOS:RL.01.07.0004-

internal:133137f635df:202011231807

Public

Service OS user accounts 122

SHA:              133137f635dff5778bf3e109eb75825b68d64789

Boot Profiles:

0. Service OS Console

1. Primary Software Image [RL.10.xx.xxxxx]

2. Secondary Software Image [RL.10.xx.xxxxx]

Select profile(secondary):

NOTE

The (primary) string in the boot menu displays the default boot profile that will
be booted after the timeout period. This string will change to (secondary) or
(Service OS) depending on the current default boot option.

Console configuration

During boot, Service OS communicates with the USB console port connected to the management module
console port, input will automatically be switched over to use the USB console. Automatic switching to USB is
consistent with the USB console behavior.

AOS-CX boot

Description

After the user has input a boot profile selection at the boot menu or the 5-second selection timeout has
expired, Service OS will boot an AOS-CX image.

Service OS displays the following boot strings embedded in the product image header:

•

Image name

•

Image version

•  Build ID

•  Build date

Service OS will then present status and boot the image.

Example

Booting primary software image...
Verifying Image...

Image Info:

        Name: AOS-CX

Public

Console configuration 123

Version: XL.01.01.0001

    Build Id: AOS-CX:XL.01.01.0001:1a36111da4e0:201707171452

  Build Date: 2017-07-17 14:52:27 PDT

Extracting Image...

Loading Image...

Done.

kexec: Starting new kernel

File system access

Description

When the user logs in to the Service OS CLI, they are presented with a limited file system. The user can use
standard file system commands of cd, ls, and pwd to view and move through the file system.

On login, the user is first placed in the /home directory:

(C) Copyright 2017 Hewlett Packard Enterprise Development LP

                      RESTRICTED RIGHTS LEGEND

Confidential computer software. Valid license from Hewlett Packard

Enterprise

Development LP required for possession, use or copying. Consistent with FAR

12.211 and 12.212, Commercial Computer Software, Computer Software

Documentation, and Technical Data for Commercial Items are licensed to the

U.S. Government under vendor's standard commercial license.

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: admin

SVOS> pwd

/home

SVOS>
The home directory and the USB device (/mnt/usb and any sub directory) are the only writable directories
available. These directories can be used as a staging location for downloading product images using TFTP. /
home can also be used as temporary storage before copying files from the management module through
TFTP or USB. Any changes made to /home will not persist across reboots or after booting an AOS-CX image.

The root / directory displays viewable directories:

SVOS> ls /

bin       coredump  lib       mnt       selftest

cli       home      logs      nos

SVOS>
The directories coredump, selftest, nos, and logs each provide the user access to an eMMC partition mount.
The user may read, but not write any file on these partitions.

Public

File system access 124

These mount points allow the user to copy files on the eMMC to a USB storage device or upload files using
TFTP. Copying files from the eMMC is intended to be used under the guidance of a support engineer (to
upload logs or coredumps to HPE support).

USB storage device access is provided through the mount at /mnt/usb.

The remaining directories in the root file system bin, cli, and lib are not intended to be used by the customer.

Service of OS mount failure

Description

If the eMMC is detected as missing or any of the partitions could not be mounted, Service OS will force the
user to boot to the Service OS console and display an error message indicating that recovery should be
attempted using the format command.

Example

(C) Copyright 2017 Hewlett Packard Enterprise Development LP

                      RESTRICTED RIGHTS LEGEND

Confidential computer software. Valid license from Hewlett Packard

Enterprise

Development LP required for possession, use or copying. Consistent with FAR

12.211 and 12.212, Commercial Computer Software, Computer Software

Documentation, and Technical Data for Commercial Items are licensed to the

U.S. Government under vendor's standard commercial license.

To reboot without logging in, enter 'reboot' as the login user name.

 Error, Could not mount the primary storage device.

 This may be due to filesystem or device corruption.

 Please attempt to recover using the "format" command.

ServiceOS login:

Service OS CLI command list

Description

After login to Service OS CLI, the user may enter the commands help or ? to get a full list of commands and
a terse description for each command. The user may also enter <command> followed by --help to get more
detailed help and usage for a specific command.

Public

Service of OS mount failure 125

Example

SVOS> ?

Available Commands:

                   ? - Display help screen

                  cd - Change the working directory

                 pwd - Print the current working directory

                help - Display help screen

allow-unsafe-updates - Allow non-failsafe updates for a limited amount of

time

                boot - Boot a product image

        config-clear - Clears the startup-config

                diag - Run diagnostic commands

               erase - Securely erase storage devices on the management

module

              format - Formats and partitions the primary storage device

            identify - Prints hardware identification information

               mount - Mount a storage device

            password - Set the admin account password

              reboot - Reboots the Management Module

         secure-mode - Set or retrieve the secure mode setting

                  sh - Launch support shell

              umount - Unmounts a storage device

              update - Update a product image

             version - Prints ServiceOS release version information

                 cat - Prints files to stdout

                  cp - Copy files and directories

                  du - Estimate file space usage

                  ls - List directory contents

              md5sum - Compute and check md5 message digest

               mkdir - Make directories

                  mv - Move (rename) files

                  rm - Remove files or directories

               rmdir - Remove empty directories

                exit - Logout

Enter '<command> --help' for more info

Service OS CLI features and limitations

The Service OS CLI provides basic shell functionality that allows you to execute commands and pass
arguments to those commands only. The following features are not available:

•

Input/output redirection (<, >, >>)

Public

Service OS CLI features and limitations 126

•  Job control (&, fg, bg)

•  Process piping (|)

•  File globbing (\*)

NOTE

Even though the Service OS CLI does not provide file globbing capabilities,
some commands may provide this functionality internally. An example is the  ls
command.

The following common features are available:

•  Command history (Up Arrow) and search (Ctrl-R)

•  Tab completion for file and folder names (not CLI commands)

•  Command abort using Ctrl-C

Service OS CLI commands

Select a command from the list in the left navigation menu.

Subtopics

boot
cat
cd path
config-clear
cp
du
erase zeroize
exit
format
identify
ls
md5sum
mkdir
mount
mv
password (svos)
pwd
reboot
rm

Public

Service OS CLI commands 127

rmdir
secure-mode
sh
system serviceos password-prompt
umount
update
tftp
version

boot

Syntax

boot

Description

Presents you with the boot menu prompt. You can then specify which boot profile: primary, secondary, or
Service OS console.

Example

Presenting the boot menu prompt:

SVOS> boot

ServiceOS Information:

    Version:          PL.01.07.0004-internal

    Build Date:       2020-11-23 18:07:42 PST

    Build ID:         ServiceOS:PL.01.07.0004-

internal:133137f635df:202011231807

    SHA:              133137f635dff5778bf3e109eb75825b68d64789

Boot Profiles:
0. Service OS Console

1. Primary Software Image [PL.10.06.0001]

2. Secondary Software Image [PL.10.08.0000-168-g3089099c34e6]

Select profile(primary):

Command History

Release

Modification

10.07 or earlier

‐‐

Public

boot 128

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

cat

Syntax

cat <FILENAME/DIRECTORY-NAME>

Description

Prints the contents of a file to the console. The Service OS does not allow command output redirection, so
this command is only useful for reading short text files.

Parameter

Description

Shows the contents of the specified file or directory.

<FILENAME/DIRECTORY‐NAME>

Example

Showing the contents of /nos/hosts:

SVOS> cat /nos/hosts

127.0.0.1       localhost.localdomain           localhost

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Public

cat 129

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

cd path

Syntax

cd path

Description

Changes the current working directory.

Example

Changing the current working directory:

cd /

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

cd path 130

config-clear

Syntax

config-clear

Description

Configures the switch to set all configuration settings to factory default when the switch is restarted. The
next time the switch starts, the current startup-config is renamed to startup-config-fixme, and a new
startup-config is created with factory default settings.

NOTE

Using this command is not the same as performing zeroization, which securely
erases the entire primary storage and other devices, and not just the
configuration.

Example

Configuring the system to clear the switch configuration:

SVOS> config-clear

The switch configuration will be cleared.

Continue (y/n)? y

The system has been configured to clear the startup-config on the next

boot. Please execute the 'boot' command to complete this action.

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

config-clear 131

cp

Syntax

cp [options] <SOURCE-FILENAME/SOURCE-DIRECTORY>

            <DESTINATION-FLENAME/DESTINATION-DIRECTORY>

Description

Copies files or directories.

Parameter

[options]

   ‐d,‐P

   ‐a

   R,‐r

    ‐L

    ‐H

    ‐p

   ‐f

   ‐i

Description

Selects the options for the command.

Specifies the preservation of symlinks (default if ‐R).

Same as ‐dpR.

Specifies recursiveness, all files, and subdirectories are copied.

Specifies the following of all symlinks.

Specifies the following of symlinks on command line.

Specifies the preservation of file attributes if possible.

Specifies the overwriting of a file or directory.

Specifies the prompting before an overwrite.

   ‐l,‐s

Specifies the creation of (sym) links.

Specifies the name of the source file or directory.

<SOURCE‐FILENAME/SOURCE‐
DIRECTORY>

<DESTINATION‐FLENAME/
DESTINATION‐DIRECTORY>

Specifies the name of the destination file or directory.

Public

cp 132

Example

Copying /home/customers directory to the /home/clients directory:

SVOS> cp /home/customers /home/clients

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

du

Syntax

du [options] <FILENAME/DIRECTORY-NAME>...

Description

Shows estimated disk space used for each file or directory or both.

Parameter

[options]

   ‐a

   ‐L

   ‐H

   ‐d, N

Description

Selects the options for the command.

Show file sizes.

Shows all symlinks.

Shows symlinks on a command line.

Shows limited output to directories (and files with ‐a) of dept
h less than N.

Public

du 133

Parameter

   ‐c

   ‐l

   ‐s

   ‐x

   ‐h

   ‐m

   ‐k

Description

Shows the total disk space usage of all files or directories or bot
h.

Shows the count sizes if hard linked.

Shows only a total for each argument.

Does not show directories on different file systems.

Show sizes in human readable format (1K, 243M, and 2G).

Show sizes in megabytes.

Show sizes in kilobytes (default).

Specifies the file or directory or both for displaying a size estim
ate.

<FILENAME/DIRECTORY‐NAME>

Example

Estimating disk space for the /nos directory:

SVOS> du -ah /nos

196.4M  /nos/primary.swi

196.4M  /nos

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

du 134

erase zeroize

Syntax

erase zeroize

Description

Securely erases any user data contained on the eMMC or other storage devices on the management module.

NOTE

Back up all data before running this command or all user/config data will be lost.

Usage

Use this command to securely erase all customer data and restore the software environment to factory
default. When you issue this command:

•  Software images are copied to RAM to be restored on completion.

•  All bits undergo a 0>1>0 transition to completely zeroize data. This data is not recoverable.

•  This feature can be used to remove all configuration settings or system alterations for debugging or

troubleshooting.

•  The zeroization process takes approximately two minutes.

NOTE

All logs and data are lost in the zeroization process. Best practices is to collect all
applicable data before performing zeroization.

Example

Erasing user data:

SVOS> SVOS> erase --help

Usage: erase zeroize

Securely erases storage devices on the management module.

SVOS>

```

```

SVOS> erase zeroize
############################WARNING############################

This will securely erase all customer data and reset the switch

to factory defaults. This will initiate a reboot and render the

switch unavailable until the zeroization is complete.

Public

erase zeroize 135

This should take several minutes to one hour to complete.

############################WARNING############################

Continue (y/n)? y

reboot: Restarting system

 ServiceOS Information:

    Version: PL.01.07.0004-internal

    Build Date: 2020-11-23 18:07:42 PST

    Build ID: ServiceOS:PL.01.07.0004-internal:133137f635df:202011231807

    SHA: 133137f635dff5778bf3e109eb75825b68d64789

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

exit

Syntax

exit

Description

Logs the user out from the  SVOS>  prompt.

Example

Loging the user out from the  SVOS>  prompt:

SVOS> exit
(C) Copyright  Hewlett Packard Enterprise Development LP

                      RESTRICTED RIGHTS LEGEND

Confidential computer software. Valid license from Hewlett Packard

Enterprise

Public

exit 136

Development LP required for possession, use or copying. Consistent with FAR

12.211 and 12.212, Commercial Computer Software, Computer Software

Documentation, and Technical Data for Commercial Items are licensed to the

U.S. Government under vendor's standard commercial license.

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login:

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

format

Syntax

format

Description

Configures the primary storage device with the correct partition and file system formatting. This command
removes all pre-existing data on the primary storage device.

Example

Configuring the primary storage device with the correct partition and file system formatting:

SVOS> format

##################WARNING####################

The following action will cause all data on
the primary storage device to be lost. After

formatting has completed, a reboot will be

initiated to complete storage initialization.

##################WARNING####################

Public

format 137

Continue? (y/n): y

Working...This may take a few minutes...

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

identify

Syntax

identify

Description

Prints the version of the SVOS and of the UEFI BIOS.

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

identify 138

ls

Syntax

ls [<OPTIONS>] [<FILE-NME>]

Description

This command lists directory contents.

Parameter

Description

Specifies options for the command.

<OPTIONS>

   ‐1

   ‐a

   ‐A

   ‐C

   ‐x

   ‐d

   ‐L

   ‐H

   ‐R

   ‐p

   ‐F

   ‐l

   ‐i

Shows one‐column output.

Shows entries which start with a period (.).

Shows output similar to ‐a, but excludes a period (.) and a dou
ble period (..).

Shows output list by columns.

Shows output list by lines.

Shows listing of directory entries instead of contents

Follows symlinks.

Follows symlinks on the command line.

Recurse.

Appends a slash (/) to directory entries.

Appends an indicator to entries. An indicator can be as an aster
isk (*) or slash (/) or equal sign (=) or at sign (@) or pipe (|).

Shows the output in a long listing format.

Shows the list inode numbers.

Public

ls 139

Parameter

Description

   ‐n

   ‐s

   ‐e

   ‐h

   ‐r

   ‐S

   ‐X

   ‐v

   ‐c

   ‐t

   ‐u

   ‐c

Shows a list of numeric UIDs and GIDs instead of names.

Shows a list of allocated blocks.

Shows in one column a list with the full date and time.

Shows list sizes in human readable format (1K, 243M, 2G) with
a one‐column output.

Shows in one column a sort in reverse order.

Shows in one column a sort by size.

Shows in the output sort by extension.

Shows in one column a sort by version.

With ‐l, it shows a sort in one column by ctime.

With ‐l, it shows a sort by mtime.

With ‐l, sort by atime.

With ‐l, it shows a sort in one column by ctime

   ‐w <N>

Assumes that the terminal has the number of columns wide as
specified by <N>.

   ‐‐color[={always |
never | auto}]

Controls color in the output.

Specifies the name of the file to list.

<FILE‐NAME>

Example

Listing directory contents:

SVOS> ls -la /nos

drwxr-xr-x    3 0        0             4096 Nov 21 03:19 .
drwxr-xr-x   11 0        0              220 Nov 21 03:21 ..

drwx------    2 0        0            16384 Nov 21 03:20 lost+found

Public

ls 140

-rwxr-xr-x    1 0        0        205957424 Nov 21 03:19 primary.swi

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

md5sum

Syntax

md5sum [-c | -s | -w] [<FILE-NAME>]

Description

This command computes and checks the MD5 message digest.

Parameter

[‐c | ‐s | ‐w]

Description

Selects the options for the command.

   ‐c

   ‐s

   ‐w

<FILE‐NAME>

Specifies to check the sums against the list in files.

Specifies not output anything, status code shows success.

Specifies to warn about improperly formatted checksum lines.

Specifies the file name to run the checksum against.

Public

md5sum 141

Example

Computing and checking the MD5 message digest for /nos/primary.swi:

SVOS> md5sum /nos/primary.swi

93ffc89e7ec357854704d8e450c4b7ab  /nos/primary.swi

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

mkdir

Syntax

mkdir [-m | -p] [<DIRECTORY-NAME>]

Description

This command makes directories.

Parameter

[‐m | ‐p]

   ‐m

   ‐p

Description

Specifies the options for the command.

Specifies the mode.

Specifies to make parent directories as needed with no errors fo
r pre‐existing directories.

Specifies the directory to create.

Public

mkdir 142

Parameter

<DIRECTORY‐NAME>

Description

Example

Making the dir directory:

SVOS> mkdir dir

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

mount

Syntax

mount <DEVICE>

Description

This command mounts the eMMC partitions to the following locations: /coredump, /logs, /nos, /selftest,
and mounts the USB device to /mnt/usb.

Users can mount USB flash drives formatted as either FAT16 or FAT32 with a single partition.

Public

mount 143

Parameter

Description

Specifies the device to be mounted. Supported device options i
nclude  all  and  usb .

<DEVICE>

Examples

Mounting all of the eMMC partitions:

SVOS> mount all

SVOS> mount usb

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

mv

Syntax

mv [-f | -i | -n] <TARGET-DIRECTORY>

Description

This command moves (renames) files.

Public

mv 144

| Parameter |     | Description                                 |     |     |
| --------- | --- | ------------------------------------------- | --- | --- |
| ‐f        |     | Specifies not to prompt before overwriting. |     |     |
Specifies to prompt before overwriting.
‐i
| ‐n  |     | Specifies to not overwrite an existing file. |     |     |
| --- | --- | -------------------------------------------- | --- | --- |
Example
Moving the file named myfile:
SVOS> mv myfile

Command History
Release Modification
10.07 or earlier ‐‐
Command Information
| Platforms | Command context | Authority |     |     |
| --------- | --------------- | --------- | --- | --- |
All platforms ServiceOS (SVOS> ) Administrators or local user group members with execution righ
ts for this command.

password (svos)
Syntax
password
Description
Sets the admin user account password for both Service OS and once the user boots into and saves the
configuration. This will overwrite the previous password if one exists. User input is masked with asterisks.
This command is not available if enhanced secure mode is set.
|     | Public |     | password (svos) | 145 |
| --- | ------ | --- | --------------- | --- |

Example

Setting the admin account password:

SVOS> password

Enter password:********

Confirm password:********

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

pwd

Syntax

pwd

Description

Displays the current working directory.

Example

Displaying the current working directory:

SVOS> pwd

/home

SVOS>

Public

pwd 146

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

reboot

Syntax

reboot

Description

Reboots the Management Module.

Example

Rebooting the management module:

SVOS> reboot

reboot: Restarting system

Command History

Release

Modification

10.07 or earlier

‐‐

Public

reboot 147

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

rm

Syntax

rm [-f | -i | -R | -r] <FILE-NAME>

Description

Removes files or directories.

Parameter

Description

[‐f | ‐i | ‐R | ‐r]

Selects the options for removing files or directories.

   ‐f

   ‐i

Never prompt before removing files or directories.

Always prompt before removing files or directories.

   ‐R | ‐r

Recursive.

Example

Removing the file named foo:

SVOS> rm foo

Command History

Release

Modification

10.07 or earlier

‐‐

Public

rm 148

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

rmdir

Syntax

rmdir [-p] <DIRECTORY-NAME>

Description

Removes empty directories.

Parameter

 ‐p

Example

Removing the empty foo directory:

SVOS> rmdir foo

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Description

Specifies to remove parent directories.

Public

rmdir 149

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

secure-mode

Syntax

secure-mode <enhanced | standard | status>

Description

Sets the secure mode to enhanced or standard secure mode. Also can display the current secure mode. A
zeroization is required before switching between enhanced and standard secure modes.

The command also displays a message notifying the user that they are already in the targeted secure mode.

Example

Setting the secure mode to enhanced or standard:

SVOS> secure-mode --help

Usage: secure-mode <enhanced | standard | status>

Set or retrieve the secure mode setting. Requires a zeroization to change

modes.

SVOS>

```

```

SVOS> secure-mode enhanced

############################WARNING############################

This will set the switch into enhanced secure mode.  Before

enhanced secure mode is enabled, the switch must securely erase

all customer data and reset the switch to factory defaults.

This will initiate a reboot and render the switch unavailable

until the zeroization is complete.

This should take several minutes to one hour to complete.

############################WARNING############################

Continue (y/n)? y

reboot: Restarting system

```

Public

secure-mode 150

```

SVOS> secure-mode standard

############################WARNING############################

This will set the switch into standard secure mode.  Before

standard secure mode is enabled, the switch must securely erase

all customer data and reset the switch to factory defaults.

This will initiate a reboot and render the switch unavailable

until the zeroization is complete.

This should take several minutes to one hour to complete.

############################WARNING############################

Continue (y/n)? y

reboot: Restarting system

```

```

SVOS> secure-mode standard

############################WARNING############################

Secure mode is already set to standard.  Setting it again will

repeat the zeroization process.  The switch must securely erase

all customer data and reset the switch to factory defaults.

This will initiate a reboot and render the switch unavailable

until the zeroization is complete.

This should take several minutes to one hour to complete.

############################WARNING############################

Continue (y/n)? y

reboot: Restarting system

```

```

SVOS> secure-mode status

enhanced secure mode is set.

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Public

secure-mode 151

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

sh

Syntax

sh

Description

Launches a bash shell for support purposes. To quit bash, enter exit.

This command is not available if enhanced secure mode is set.

Example

Launching a bash shell:

SVOS> sh

switch:/cli/fs/home#

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

sh 152

system serviceos password-prompt

Syntax

system serviceos password-prompt

no system serviceos password-prompt

Description

Use this command to enable password authentication for ServiceOS. By default, the ServiceOS shell
(accessible only from the local switch console port) requires no password to login as an admin use.

When this setting is enabled, the same password used to authenticate the admin user in the AOS-CX CLI
or WebUI can be used to log in to the ServiceOS shell. If this setting is enabled, a forgotten admin user
password cannot be reset using ServiceOS; if there are no other local or RADIUS/TACACS user accounts with
administrator-level access, the switch must be zeroized by entering the username zeroize command at the
ServiceOS login prompt to restore administrator access.

serviceos password-prompt cannot be enabled if the built-in admin user has been disabled.

The admin cannot be disabled while serviceos password-prompt is enabled.

Example

Enablling password authentication for ServiceOS

switch(config)# system serviceos password-prompt

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

umount

Public

system serviceos password-prompt 153

Syntax

umount <DEVICE>

Description

Unmounts the eMMC partitions mounted to the following locations: /coredump, /logs, /nos, /selftest, and
unmounts the USB device mounted to /mnt/usb.

Parameter

Description

Specifies the device to be unmounted. Supported device option
s include all and usb.

<DEVICE>

Examples

Unmounting all devices:

SVOS> umount all

SVOS> umount usb
Unmounting a USB device:

SVOS> umount all

SVOS> umount usb

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

umount 154

update

Syntax

update {primary | secondary} <IMAGE>

Description

Verifies and installs a product image. The user can select the primary or secondary boot profile to update
and the location of the file.

Parameter

Description

{primary | secondary}

Selects either the primary or secondary image.

Specifies the image name.

<IMAGE>

Examples

Updating the software image using TFTP:

NOTE
The OOBM port is disabled on first boot and must be enabled using the ip
command.

SVOS> ip dhcp

SVOS> ip show

Interface  : Link Up

IP Address : 192.0.2.22
Subnet Mask: 255.255.200.20

Gateway    : 10.0.24.1

SVOS> tftp -g -r XL.10.00.0001.swi -l image.swi 192.4.8.10

XL.10.00.0001.swi 100% |*******************************|   178M  0:00:00 ETA

SVOS> ls

image.swi

SVOS> update primary image.swi

Updating primary software image...

Verifying image...

Done

Public

update 155

Update the software image using USB:

NOTE

This example assumes that the user has preloaded a USB flash drive with the
image to be updated. The image name on the flash drive is not important.

SVOS> mount usb

SVOS> ls /mnt/usb

image.swi

SVOS> update primary /mnt/usb/image.swi

Updating primary software image...

Verifying image...

Done

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

tftp

Syntax

tftp {-b | -g | -l <LOCAL-FILE> | -p | -r <REMOTE-FILE>} host [<PORT>]

Description

Transfers files to and from a remote machine (TFTP a file).

Public

tftp 156

Parameter

Description

{‐b | ‐g | ‐l | ‐p | ‐r
<REMOTE‐FILE>}

Selects the options for transferring a file.

‐b

‐g

‐l

‐p

Specifies the transfer blocks of size octets. The default blocksi
ze is set to 1468, which can be overridden with the ‐b option.

Specifies to get a file.

Specifies a local file.

Specifies to put a file in remote location.

‐r <REMOTE‐FILE>

Specifies a remote file.

Specifies the port for transfer. If no port option is specified, TFT
P uses the standard UDP port 69 by default.

<PORT>

Example

Transferring files:

SVOS> tftp -b 65464 -g -r XL.10.00.0002.swi.swi 192.0.2.1

XL.10.00.0002 100% |*******************************|   178M  0:00:00 ETA

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

tftp 157

version

Syntax

version

Description

Displays the following build strings:

•  Version.

•  Build date.

•  Build time.

•  Build ID.

•  SHA.

Example

Displaying version build strings:

SVOS> version

ServiceOS Information:

    Version:          GT.01.01.0001

    Build Date:       2017-07-19 14:52:31 PDT

    Build ID:         ServiceOS:GT.01.01.0001:461519208911:201707191452

    SHA:              46151920891195cdb2267ea6889a3c6cbc3d4193

SVOS>

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS ( SVOS> )

Administrators or local user group members with execution righ
ts for this command.

Public

version 158

In-System Programming

The ISP (In-System Programming) feature provides an automated way to roll out updates to various
programmable devices in an network switch, after the product has shipped. ISP is intended to run
automatically either at boot time or as new modules are inserted into the chassis at runtime.

Subtopics

Show tech command list for the ISP feature
In-System Programming commands

Show tech command list for the ISP feature

Task

Command

Displaying versions of all present programmable devi
ces.

show tech isp

Displaying stored log files from any ISP updates on t
he system.

show tech update‐log

See the for additional information about the  show tech  commands.

In-System Programming commands

Select a command from the list in the left navigation menu.

Subtopics

clear update-log
show needed-updates

clear update-log

Syntax

clear update-log

Public

In-System Programming 159

Description

Clears stored log files of any In-System Programming updates on the system.

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

show needed-updates

Syntax

show needed-updates [next-boot [primary|secondary]]

Description

Displays whether any programmable devices are in need of an update.

Without the next-boot parameter, this command displays needed updates relative to the currently running
image.

With the next-boot parameter, this command displays needed updates relative to an image file in the
persistent storage of the switch, which might be different from the currently running image. If either the
primary or secondary parameter is specified, this command queries that specific image file. Otherwise, it
queries the default image file as set by the most recent boot system or boot set-default command.

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show needed-updates 160

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Selftest

Power On Self Test (POST) is the first task which verifies the hardware functionality of various modules
during boot-up. Based on the criticality of the test, the selftest module decides whether to go ahead with the
boot-up sequence of a particular subsystem or interface during a POST failure.

POST comprises of the following:

•  Front-end Port Loopback tests

This is to verify the physical port front-end interface.

These tests check if a particular interface can function properly. A test failure would mean that the
particular interface is marked as "Failed" and thus it would become unavailable for use.

This test is run when "no fastboot" is configured.

Subtopics

Selftest commands

Selftest commands

Select a command from the list in the left navigation menu.

Subtopics

fastboot
show selftest

fastboot

Public

Selftest 161

Syntax

fastboot

no fastboot

Description

Enables fastboot for the system.

The no form of this command disables fastboot for the system.

Usage

When fastboot is enabled, most tests under a Power On Self Test (POST) are skipped. By default, fastboot is
enabled.

After disabling fastboot, save switch configurations and then reboot for POST to run. POST verifies the
hardware functionality of various modules during boot-up. Based on the criticality of the test, the selftest
module decides whether to go ahead with the boot-up sequence of a particular subsystem or interface
during a POST failure.

POST runs memory built-in selftest (BISTs) and front-end port loopback tests. Memory BISTs verify the
internal and external memory blocks present in the module. The memory tables are critical for proper
functionality of the system so any failures in these tests results in the corresponding subsystem to be
marked as "Failed" and thus that subsystem is not available for use.

Front-end port loopback tests verify the physical port front-end interface. These tests check if a particular
interface can function properly. A test failure means that a particular interface has been marked as "Failed"
and is now unavailable for use.

Examples

Enabling fastboot:

switch# configure terminal

switch(config)# fastboot

switch(config)# end

switch# show running-config

Current configuration:
!

!Version

             ML.10.06.0001

module 1/1 product-number jl726a!Version

             FL.10.06.0001

module 1/1 product-number jl661a!Version

             XL.10.00.0002

module 1/1 product-number jl363a!Version

Public

fastboot 162

PL.10.06.0001

module 1/1 product-number jl677a

!

!

!

!

!

!

!

vlan 1

interface 1/1/1

    no shutdown

Disabling fastboot:

switch# configure terminal

switch(config)# no fastboot

switch(config)# end

switch(config)# write mem

Configuration changes will take time to process, please be patient.

switch# show running-config

Current configuration:

!

!Version

             ML.10.06.0001

module 1/1 product-number jl726a!Version

             FL.10.06.0001

module 1/1 product-number jl661a!Version

             XL.10.00.0002

module 1/1 product-number jl363a!Version

             PL.10.06.0001

module 1/1 product-number jl677a

!

!

!

no fastboot

!

!

Public

fastboot 163

!

!

vlan 1

interface 1/1/1

    no shutdown

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

show selftest

Syntax

show selftest [brief]

show selftest line-module <SLOT-ID>

show selftest line-module <SLOT-ID> interface [brief]
show selftest interface [<PORT-NUM>]

Description

Displays selftest results.

Parameter

[brief]

Description

Shows the selftest results as a brief description. Default.

line‐module

Shows the selftest results for a line module.

Public

show selftest 164

Parameter

Description

Shows the selftest results for the slot ID of the line or fabric m
odule.

<SLOT‐ID>

<PORT‐NUM>

Examples

Shows the selftest results for the port number.

Displaying the output when fastboot is enabled:

switch# show selftest

Name       Id   Status         ErrorCode  LastRunTime

---------- ---- -------------- ---------- -------------------

LineModule 1/1  passed         0x0

LineModule 1/2  passed         0x0

switch# show selftest line-module

Name       Id   Status         ErrorCode LastRunTime

---------- ---- -------------- --------- -------------------

LineModule 1/1  passed         0x0

LineModule 1/2  passed         0x0

switch# show selftest line-module 1/1

Name       Id   Status         ErrorCode LastRunTime

---------- ---- -------------- --------- -------------------

LineModule 1/1  passed         0x0
Displaying the output when fastboot is enabled:

switch# show selftest interface 1/1/2

Name    Status         ErrorCode LastRunTime
------- -------------- --------- -------------------

1/1/2   skipped        0x0

switch# show selftest line-module 1/1 interface

Name    Status         ErrorCode LastRunTime

------- -------------- --------- -------------------

1/1/1   skipped        0x0

1/1/2   skipped        0x0

1/1/3   skipped        0x0

1/1/31  skipped        0x0
Displaying the output when fastboot is disabled:

Public

show selftest 165

Testing to register read/write:

NOTE

This test is run irrespective of fastboot being enabled or disabled.

switch# show selftest

Name       Id   Status         ErrorCode  LastRunTime

---------- ---- -------------- ---------- -------------------

LineModule 1/1  passed         0x0        2018-02-16 18:15:53

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Zeroization

Device zeroization lets you remove all user files from flash storage, including embedded MultiMediaCard
(eMMC) . User files cannot be retrieved after the zeroization is complete.

NOTE
Zeroization can occur in both and Service OS. This section covers zeroization
and . For information about zeroization and Support OS, see erase zeroize .

Zeroization preserves the primary and secondary software images on the eMMC. Zeroization also preserves
manufacturing information.

The sensitive user files stored on an eMMC or SPI flash/EEPROM storage or both include:

•  Switch configurations.

Public

Zeroization 166

•  System generated private keys.

•  User installed private keys.

•  Admin/operator password files.

Using CLI, you can change the switch settings from standard secure mode to enhanced secure mode. Setting
the switch back to standard secure mode can only be performed through Service OS. For more information
on how to change switch settings using Server OS, see Service OS.

Enhance secure mode is used to enhance the switch security. In enhanced security mode, the switch
(Product OS)  start-shell  command is disabled for security purpose except through ServiceOS.

Subtopics

Zeroization commands

Zeroization commands

Select a command from the list in the left navigation menu.

Subtopics

erase all zeroize

erase all zeroize

Syntax

erase [all] zeroize

Description

Restores the switch to its factory default configuration. You will be prompted before the procedure starts.
Once complete, the switch will restart from the primary image with factory default settings.

Usage

The erase all command is always available in the CLI. On running the erase all command, the switch is
restored to a factory default settings, but retains the enhanced secure mode settings.

The erase all zeroize command is not available in the CLI when enhanced secure mode is enabled. This
command restore the switch to a factory default settings. On running the erase all zeroize command in

Public

Zeroization commands 167

enhanced secure mode, displays a notification stating that the command is unavailable in enhanced secure
mode.

NOTE

Back up all data before running this command as all configuration settings will be
lost.

Example

Restoring the switch to factory default configuration, except for the enhance secure mode settings:

switch# erase all

This command will erase all data and reset the switch to factory

defaults, with the exception of the secure mode setting. This process

will take several minutes to an hour to complete and the switch will

be unavailable during that time.

Continue (y/n)?

ServiceOS Information:

Version: GT.01.01.0007

Build Date: 2017-12-07 11:48:44 PST

Build ID: ServiceOS:GT.01.01.0007:42c7d15cf7e5:201712071148

SHA: 42c7d15cf7e5af5bf1c7d8764ff673471084c2a4

################ Preparing for zeroization #################

################ Storage zeroization #######################

################ WARNING: DO NOT POWER OFF UNTIL ##########

################ ZEROIZATION IS COMPLETE ##########

################ This should take several minutes ##########

################ to one hour to complete ##########

################ Restoring files ###########################
Restoring the switch to factory default configuration only when enhance secure mode settings is disabled.

switch# erase all zeroize

This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the

switch unavailable until the zeroization is complete.

This should take several minutes to one hour to complete.

Continue (y/n)? y

The system is going down for zeroization.

...

################ Preparing for zeroization #################

################ Storage zeroization #######################

################ WARNING: DO NOT POWER OFF UNTIL  ##########

################          ZEROIZATION IS COMPLETE ##########

################ This should take several minutes ##########

################ to one hour to complete          ##########

Public

erase all zeroize 168

################ Restoring files ###########################

...

We'd like to keep you up to date about:

  * Software feature updates

  * New product announcements

  * Special events

Please register your products now at: https://networkingsupport.hpe.com

NOTE

When you log in after zeroization, you get a prompt to create a password for the
administrator account. You can set the password as blank (to set the password
as blank, hit enter at the prompt) or type 1 to 32 printable ASCII characters,
excluding spaces and question marks (?). For more information on password
requirements, see Password requirements in the .

switch login: admin

Password:

Please configure the 'admin' user account password.

Enter new password: *****

Confirm new password: *****

Command History

Release

Modification

10.11.1010

Introduced erase all CLI command

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Terminal Monitor

Public

Terminal Monitor 169

The terminal monitor is used to display selective logs dynamically on the VTYSH session. When the terminal
monitor feature is enabled on the switch, it displays only the live or active logs. These logs are displayed on
the SSH session or console session. If required, you can enable the terminal monitoring on multiple sessions.

It is important to monitor the logs dynamically while debugging, so that you can co-relate the issues. The
logs can be filtered by type (event or debug), severity, or keyword. The terminal monitor runs in synchronous
mode, where the user enters any command, the log display pauses until the command execution is complete.
This ensures that the logs will not appear in between other CLI outputs or while the user is typing.

NOTE

Terminal monitoring is not persistent in the SSH session. If the SSH session is
terminated, the terminal monitor is no longer valid. However, logging console is
persistent and is added to the switch configuration, so it will persist between
telnet sessions.

Subtopics

Terminal monitor commands

Terminal monitor commands

Select a command from the list in the left navigation menu.

Subtopics

logging console {notify | severity | filter}
show terminal-monitor
terminal-monitor {notify | severity | filter}

logging console {notify | severity | filter}

Syntax

logging console{notify <event|debug|all> | severity <level> | filter

keyword}

no logging console

Description

Enables the logging console feature in the console session. It display all debug log or event log or both
debug and event log messages. Monitoring can be filtered with the severity options or with the help of
keywords. Enabling terminal monitor without options displays both debug and event log with a severity
error. This command is persistent across reboot.

Public

Terminal monitor commands 170

The no form of this command disables the terminal monitor configuration.

Parameter

Description

notify <event|debug|all>

Specifies the type of log notification.

severity <level>

•  Event: Displays the event log messages. (Default)
•  Debug: Displays the debug log messages.
•  All: Displays both event and debug log messages.

Specifies the severity level for the logs. The different severity l
evels are emergency, critical, error, warning, notice, information
(default), alert, and debug (shows all severities).

filter <keyword>

Specifies the filter by applying keyword for the logs.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring console logging in the console session:

switch(config)# logging console

Terminal-monitor is enabled successfully

switch(config)# logging console notify all

Terminal-monitor is enabled successfully

switch(config)# logging console notify event severity info

Terminal-monitor is enabled successfully

switch(config)# logging console filter lldp

Terminal-monitor is enabled successfully

Command History

Release

10.08

Modification

Feature introduced.

Public

logging console {notify | severity | filter} 171

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

show terminal-monitor

Syntax

show terminal-monitor

Description

Shows whether the terminal monitoring is enabled or disabled.

NOTE

This command will not show any information about console logging.

Examples

Displaying terminal monitor when enabled:

switch# show terminal-monitor

Terminal-monitor is enabled

-------------------------------------

Notify     | Severity   | Filter

-------------------------------------

event        debug        lldp
-------------------------------------
Displaying terminal monitor when disabled:

switch# show terminal-monitor

Terminal-monitor is disabled

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show terminal-monitor 172

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

terminal-monitor {notify | severity | filter}

Syntax

terminal-monitor {notify <event|debug|all> | severity <level> | filter

<keyword>}

no terminal-monitor

Description

Enables and saves the terminal monitor feature in the switch configuration. It displays all debug log or event
log or both debug and event log messages. Terminal monitoring can be filtered with the severity options
or with the help of keywords. Enabling terminal monitor without options displays both debug and event log
with a severity error.

The no form of this command removes the terminal monitor feature from the switch configuration and the
command will not persist.

Parameter

Description

notify <event|debug|all>

Specifies the type of log notification.

severity <level>

•  Event: Displays the event log messages. (Default)
•  Debug: Displays the debug log messages.
•  All: Displays both event and debug log messages.

Specifies the severity level for the logs. The different severity l
evels are emergency, critical, error, warning, notice, information
(default), alert, and debug (shows all severities).

filter <keyword>

Specifies the filter by applying keyword for the logs.

Authority

Administrators or local user group members with execution rights for this command.

Public

terminal-monitor {notify | severity | filter} 173

Examples

Enabling terminal monitor:

switch# terminal-monitor

Terminal-monitor is enabled successfully

switch# terminal-monitor notify all

Terminal-monitor is enabled successfully

switch# terminal-monitor notify event severity info

Terminal-monitor is enabled successfully

switch# terminal-monitor filter lldp

Terminal-monitor is enabled successfully

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Troubleshooting Web UI and REST API Access Issues

The following section describes symptoms, causes and corrective actions for 401 or 404 errors.

Subtopics

HTTP 404 error when accessing the switch URL
HTTP 401 error "Login failed: session limit reached"

HTTP 404 error when accessing the switch URL

Public

Troubleshooting Web UI and REST API Access Issues 174

Symptom

The switch is operational and you are using the correct URL for the switch, but attempts to access the REST
API or Web UI result in an HTTP 404 "Page not found" error.

Cause

REST API access is not enabled on the VRF that corresponds to the access port you are using. For example,
you are attempting to access the REST API or Web UI from the management (OOBM) port, and access is not
enabled on the  mgmt  VRF. The 6100 switch does not have a  mgmt  VRF, so https-server is enabled on
the  default  VRF.

Action

Use the https-server vrf command to enable REST API access on the specified VRF.

For example:

switch(config)# https-server vrf default

HTTP 401 error "Login failed: session limit reached"

Symptom

A REST request or Web UI login attempt returns response code 401 and the response body contains the
following text string:

Login failed: session limit reached

Cause

A user attempted to log into the REST API or the Web UI, but that user already has the maximum number of
concurrent sessions running.

Action

1.  Log out from one of the existing sessions.

Browsers share a single session cookie across multiple tabs or even windows. However, scripts that
POST to the login resource and later do not POST to the logout resource can easily create the maximum
number of concurrent sessions.

2.

If the session cookie is lost and it is not possible to log out of the session, then wait for the session idle
time limit to expire.
When the session idle timeout expires, the session is terminated automatically.

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time limit
to expire, you can stop all HTTPS sessions using the https-server session close all command.

Public

HTTP 401 error "Login failed: session limit reache... 175

H
T
T
P

4
0
1

e
r
r
o
r

"
L
o
g
i
n

f
a
i
l
e
d
:

s
e
s
s
i
o
n

l
i
m
i
t

r
e
a
c
h
e
.
.
.

This command stops and starts the hpe-restd service, so using this command affects all existing REST
sessions, Web UI sessions, and real-time notification subscriptions.

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

AOS‐CX Switch Software Documentation Portal

https://www.hpe.com/us/en/networking/hpe‐aru
ba‐networking‐support‐services.html

https://arubanetworking.hpe.com/techdocs/Aruba
DocPortal/content/new-portal/aoscx.html

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

Public

Support and Other Resources 176

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

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

Public

Accessing Updates 177

https://networkingsupport.hpe./notifications/subscriptions (requires an active HPE Aruba Networking
Support Portal account to manage subscriptions). Security notices are viewable without an HPE Aruba
Networking Support Portal account.

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

Warranty Information 178