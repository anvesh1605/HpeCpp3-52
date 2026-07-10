AOS-CX 10.14.xxxx
| Diagnostics |     | and |
| ----------- | --- | --- |
Supportability Guide
| 8400 | Switch | Series |
| ---- | ------ | ------ |
Published:March,2024
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

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

3

Contents
| About                                             | this document                                      | 9   |
| ------------------------------------------------- | -------------------------------------------------- | --- |
| Applicableproducts                                |                                                    | 9   |
| Latestversionavailableonline                      |                                                    | 9   |
| Commandsyntaxnotationconventions                  |                                                    | 9   |
| Abouttheexamples                                  |                                                    | 10  |
| Identifyingswitchportsandinterfaces               |                                                    | 10  |
| Identifyingmodularswitchcomponents                |                                                    | 11  |
| Debug                                             | logging                                            | 12  |
| Debugloggingcommands                              |                                                    | 12  |
|                                                   | cleardebugbuffer                                   | 12  |
|                                                   | debug{all|<MODULE-NAME>}                           | 13  |
|                                                   | debugdb                                            | 14  |
|                                                   | debugdestination                                   | 16  |
|                                                   | diagevent-trap-disable                             | 18  |
|                                                   | showdebug                                          | 19  |
|                                                   | showdebugbuffer                                    | 20  |
|                                                   | showdebugdestination                               | 21  |
| Log Rotation                                      |                                                    | 22  |
| Logfilepaths                                      |                                                    | 22  |
| Aboutrotatedlogfiles                              |                                                    | 22  |
| Changingthesizeofthelogrotationfile               |                                                    | 22  |
| Changingthetimefrequencyforlogrotation            |                                                    | 23  |
| Resettingthetimefrequencytodaily                  |                                                    | 23  |
| Identifyingaremotehostforreceivingrotatedlogfiles |                                                    | 23  |
| Remotetransferofrotatedlogfiles                   |                                                    | 24  |
| Resettingtheremotehostforreceivingrotatedlogfiles |                                                    | 24  |
| Resettingthesizeofthelogrotationfile              |                                                    | 25  |
| Verifyingthelogrotationparameters                 |                                                    | 25  |
| Logrotationtroubleshooting                        |                                                    | 26  |
|                                                   | Logfilesnottransferredremotely                     | 26  |
|                                                   | Logrotationnotoccurringimmediatelyaftermaxfilesize | 26  |
|                                                   | Logrotationnotoccurringregardlessofperiod          | 26  |
| Logrotationcommands                               |                                                    | 27  |
|                                                   | loggingthreshold                                   | 27  |
|                                                   | logrotatemaxsize                                   | 29  |
|                                                   | logrotateperiod                                    | 29  |
|                                                   | logrotatetarget                                    | 30  |
|                                                   | showlogrotate                                      | 32  |
| Reboot                                            | reasons                                            | 33  |
| Event                                             | Logs                                               | 35  |
| Showingandclearingevents                          |                                                    | 35  |
| Client                                            | Filter                                             | 36  |
| Logmessages                                       |                                                    | 36  |
5
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide| (8400SwitchSeries)

| Network                                | Configuration                                   | Validator | 37  |
| -------------------------------------- | ----------------------------------------------- | --------- | --- |
| Showingandclearingevents               |                                                 |           | 37  |
| Networkconfigurationvalidationcommands |                                                 |           | 37  |
|                                        | switchconfig-validator                          |           | 37  |
| Supportability                         | Copy                                            |           | 39  |
| TFTPVxLANSupport                       |                                                 |           | 39  |
| Supportabilitycopycommands             |                                                 |           | 39  |
|                                        | copycheckpoint                                  |           | 39  |
|                                        | copycommand-output                              |           | 40  |
|                                        | copycore-dump[<MEMBER/SLOT>]daemon              |           | 42  |
|                                        | copycore-dump[<MEMBER/SLOT>]kernel              |           | 43  |
|                                        | copycore-dump[<MEMBER/SLOT>]kernel<STORAGE-URL> |           | 44  |
|                                        | copycore-dumpvsfmemberdaemon                    |           | 45  |
|                                        | copycore-dumpvsfmemberkernel                    |           | 46  |
|                                        | copydiag-dumpfeature<FEATURE>                   |           | 47  |
|                                        | copydiag-dumplocal-file                         |           | 48  |
|                                        | copy<IMAGE>                                     |           | 49  |
|                                        | copyrunning-config                              |           | 50  |
|                                        | copyshow-techfeature                            |           | 51  |
|                                        | copyshow-techlocal-file                         |           | 52  |
|                                        | copystartup-config                              |           | 53  |
|                                        | copysupport-files                               |           | 54  |
|                                        | copysupport-fileslocal-file                     |           | 56  |
|                                        | copysupport-log                                 |           | 57  |
| Traceroute                             |                                                 |           | 60  |
| Traceroutecommands                     |                                                 |           | 60  |
|                                        | traceroute                                      |           | 60  |
|                                        | traceroute6                                     |           | 63  |
| Ping                                   |                                                 |           | 66  |
| Pingcommands                           |                                                 |           | 66  |
|                                        | ping                                            |           | 66  |
|                                        | ping6                                           |           | 72  |
| Troubleshooting                        |                                                 |           | 75  |
|                                        | Operationnotpermitted                           |           | 75  |
|                                        | Networkisunreachable                            |           | 76  |
|                                        | Destinationhostunreachable                      |           | 76  |
Using classifier policies for traffic capture and analysis 78
| Stepone:createatrafficclass                      |                      |     | 78  |
| ------------------------------------------------ | -------------------- | --- | --- |
| Steptwo:createapolicy                            |                      |     | 79  |
| Stepthree:applythepolicy                         |                      |     | 79  |
| Stepfour:confirmpolicyInstallation               |                      |     | 80  |
| Stepfive:confirmpolicyresourceconsumption        |                      |     | 80  |
| Stepsix:configureamirrorsession                  |                      |     | 81  |
| Stepseven:startpacketcapture                     |                      |     | 81  |
| Stepeight:capturepacketstoafileormirrorittoahost |                      |     | 82  |
| Stepnine:checkpackethitcounts                    |                      |     | 82  |
| Remote                                           | syslog               |     | 85  |
| SyslogoverVXLAN support                          |                      |     | 85  |
| Remotesyslogcommands                             |                      |     | 85  |
|                                                  | clearaccounting-logs |     | 85  |
|6

|                                    | logging                         | 86  |
| ---------------------------------- | ------------------------------- | --- |
|                                    | loggingaccounting-format-native | 89  |
|                                    | loggingfilter                   | 89  |
|                                    | loggingfacility                 | 92  |
|                                    | loggingpersistent-storage       | 93  |
| Runtime                            | Diagnostics                     | 95  |
| Runtimediagnosticcommands          |                                 | 95  |
|                                    | diagnosticmonitor               | 95  |
|                                    | diagon-demand                   | 96  |
|                                    | showdiagnostic                  | 98  |
|                                    | showdiagnosticevents            | 106 |
| Service                            | OS                              | 108 |
| ServiceOSCLIlogin                  |                                 | 108 |
| ServiceOSuseraccounts              |                                 | 109 |
| ServiceOSbootmenu                  |                                 | 109 |
| Consoleconfiguration               |                                 | 110 |
| AOS-CXboot                         |                                 | 110 |
| Filesystemaccess                   |                                 | 111 |
| ServiceOSmountfailure              |                                 | 112 |
| MissingRearDisplayModuleFailure    |                                 | 112 |
| ServiceOSCLIcommandlist            |                                 | 113 |
| ServiceOSCLIfeaturesandlimitations |                                 | 113 |
| ServiceOSCLIcommands               |                                 | 114 |
|                                    | boot                            | 114 |
|                                    | cat                             | 114 |
|                                    | cdpath                          | 115 |
|                                    | config-clear                    | 116 |
|                                    | cp                              | 116 |
|                                    | du                              | 117 |
|                                    | erasezeroize                    | 118 |
|                                    | exit                            | 120 |
|                                    | format                          | 121 |
|                                    | identify                        | 121 |
|                                    | ip                              | 122 |
|                                    | ls                              | 123 |
|                                    | md5sum                          | 125 |
|                                    | mkdir                           | 126 |
|                                    | mount                           | 126 |
|                                    | mv                              | 127 |
|                                    | password(svos)                  | 128 |
|                                    | ping                            | 128 |
|                                    | pwd                             | 129 |
|                                    | reboot                          | 129 |
|                                    | rm                              | 130 |
|                                    | rmdir                           | 131 |
|                                    | secure-mode                     | 131 |
|                                    | sh                              | 133 |
|                                    | systemserviceospassword-prompt  | 133 |
|                                    | umount                          | 134 |
|                                    | update                          | 135 |
|                                    | tftp                            | 136 |
|                                    | version                         | 137 |
| In-System                          | Programming                     | 138 |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 7

| ShowtechcommandlistfortheISPfeature           |                                          |           |             |            |        | 138 |
| --------------------------------------------- | ---------------------------------------- | --------- | ----------- | ---------- | ------ | --- |
| In-SystemProgrammingcommands                  |                                          |           |             |            |        | 138 |
|                                               | clearupdate-log                          |           |             |            |        | 138 |
|                                               | showneeded-updates                       |           |             |            |        | 138 |
| Selftest                                      |                                          |           |             |            |        | 140 |
| Selftestcommands                              |                                          |           |             |            |        | 140 |
|                                               | fastboot                                 |           |             |            |        | 140 |
|                                               | showselftest                             |           |             |            |        | 142 |
| Zeroization                                   |                                          |           |             |            |        | 145 |
| Zeroizationcommands                           |                                          |           |             |            |        | 145 |
|                                               | eraseallzeroize                          |           |             |            |        | 145 |
| Terminal                                      | Monitor                                  |           |             |            |        | 148 |
| Terminalmonitorcommands                       |                                          |           |             |            |        | 148 |
|                                               | loggingconsole{notify|severity|filter}   |           |             |            |        | 148 |
|                                               | showterminal-monitor                     |           |             |            |        | 149 |
|                                               | terminal-monitor{notify|severity|filter} |           |             |            |        | 150 |
| Troubleshooting                               |                                          | Web       | UI and REST | API Access | Issues | 152 |
| HTTP404errorwhenaccessingtheswitchURL         |                                          |           |             |            |        | 152 |
| HTTP401error"Loginfailed:sessionlimitreached" |                                          |           |             |            |        | 152 |
| Support                                       | and Other                                | Resources |             |            |        | 154 |
| AccessingHPEArubaNetworkingSupport            |                                          |           |             |            |        | 154 |
| AccessingUpdates                              |                                          |           |             |            |        | 155 |
| WarrantyInformation                           |                                          |           |             |            |        | 155 |
| RegulatoryInformation                         |                                          |           |             |            |        | 155 |
| DocumentationFeedback                         |                                          |           |             |            |        | 155 |
|8

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

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

|

{ }

[ ]

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

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

9

Convention

… or

...

Usage

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

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the Aruba 8400 Switch Series

About this document | 10

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

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

11

Chapter 2
Debug logging
| Debug | logging |     |     |
| ----- | ------- | --- | --- |
Thedebugloggingframeworkprovidesanimproved,customizable,andconditionalloggingframework
withfeatureandentitybasedfilteringoptions.Debugloggingisaverbose,on-demandlogging
mechanismwhichcustomersandsupportcanenableinordertoobtainmoreinformationthatwillassist
withtroubleshooting.
EachdebugloggingeventhasbothaSeverityandaModule.Customers/supportarerequiredtoenable
agivenModuleinordertohavethoseeventslogged.ThelogoperationisnotrunwhenaModuleisnot
enabled.AlldebuglogeventsclassifiedwithaSeverityofErrorandabovewillalwaysbelogged.This
ensuresthatbothsupportandcustomerswillbeabletoseetheseimportanteventsevenwhentheir
respectivedebuglogModuleisn’tenabled.
Debugloggingisdisabledbydefault.
| Debug       | logging | commands |     |
| ----------- | ------- | -------- | --- |
| clear       | debug   | buffer   |     |
| clear debug | buffer  |          |     |
Description
Clearsalldebuglogs.Usingtheshow debug buffercommandwillonlydisplaythelogsgeneratedafter
| theclear | debug | buffercommand. |     |
| -------- | ----- | -------------- | --- |
Examples
Clearingallgenerateddebuglogs:
| switch# | show | debug buffer |     |
| ------- | ---- | ------------ | --- |
----------------------------------------------------------------------------------
----------------------------
| show | debug | buffer |     |
| ---- | ----- | ------ | --- |
----------------------------------------------------------------------------------
----------------------------
2018-10-14:09:10:58.558710|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_CONFIG|No Port cfg
changes
2018-10-14:09:10:58.558737|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_EVENT|lldpd_stats_run
| entered | at  | time 8257199 |     |
| ------- | --- | ------------ | --- |
2018-10-14:09:10:58.569317|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_CONFIG|No Port cfg
changes
2018-10-14:09:11:21.881907|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|Sysmon
| poll    | interval | changed      | to 32 |
| ------- | -------- | ------------ | ----- |
| switch# | clear    | debug buffer |       |
switch#
|     | show | debug buffer |     |
| --- | ---- | ------------ | --- |
----------------------------------------------------------------------------------
----------------------------
12
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

| show | debug buffer |     |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------
2018-10-14:09:13:24.481407|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|Sysmon
| poll           | interval    | changed | to 51   |              |     |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- | --- |
| Command        | History     |         |         |              |     |     |
| Release        |             |         |         | Modification |     |     |
| 10.07orearlier |             |         |         | --           |     |     |
| Command        | Information |         |         |              |     |     |
| Platforms      |             | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| debug      | {all |           | <MODULE-NAME>} |                    |     |           |     |
| ---------- | ---------------- | -------------- | ------------------ | --- | --------- | --- |
| debug {all | | <MODULE-NAME>} |                | [<SUBMODULE-NAME>] |     | [severity |     |
(emer|crit|alert|err|notice|warning|info|debug)] {port <PORT-NAME> |
| vlan | <VLAN-ID>  | | ip <IP-ADDRESS> |                | | mac <MAC-ADDRESS> |     | |   |
| ---- | ---------- | ----------------- | -------------- | ------------------- | --- | --- |
| vrf  | <VRF-NAME> | | instance        | <INSTANCE-ID>} |                     |     |     |
no debug {all | <MODULE-NAME>} [<SUBMODULE-NAME>] {port | vlan | ip | mac |
| vrf | | instance} |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- |
Description
Enablesdebugloggingformodulesorsubmodulesbyname,withoptionalfilteringbyspecificcriteria.
Thenoformofthiscommanddisablesdebuglogging.
| Parameter |     |     |     | Description                       |     |     |
| --------- | --- | --- | --- | --------------------------------- | --- | --- |
| all       |     |     |     | Enablesdebugloggingforallmodules. |     |     |
<MODULE-NAME>
Enablesdebugloggingforaspecificmodule.Foralistof
supportedmodules,enterthedebugcommandfollowedbya
spaceandaquestionmark(?).
<SUBMODULE-NAME> Enablesdebugloggingforaspecificsubmodule.Foralistof
supportedsubmodules,enterthedebug<MODULE-NAME>
commandfollowedbyaspaceandaquestionmark(?).
severity (emer|crit|alert|err| Selectstheminimumseverityloglevelforthedestination.Ifa
notice|warning|info|debug) severityisnotprovided,thedefaultloglevelisdebug.Optional.
emer
Specifiesstorageofdebuglogswithaseveritylevelofemergency
only.
crit Specifiesstorageofdebuglogswithseveritylevelofcriticaland
above.
| alert |     |     |     | Specifiesstorageofdebuglogswithseveritylevelofalertand |     |     |
| ----- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
Debuglogging|13

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
above.
| err |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |
| --- | --- | --- | ------------------------------------------------------ |
above.
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning
Specifiesstorageofdebuglogswithseveritylevelofwarningand
above.
| info |     |     | Specifiesstorageofdebuglogswithseveritylevelofinfoand |
| ---- | --- | --- | ----------------------------------------------------- |
above.
| debug |     |     | Specifiesstorageofdebuglogswithseveritylevelofdebug |
| ----- | --- | --- | --------------------------------------------------- |
(default).
| port |     |     | Displaysdebuglogsforthespecifiedport,forexample1/1/1. |
| ---- | --- | --- | ----------------------------------------------------- |
vlan <VLAN-ID> DisplaysdebuglogsforthespecifiedVLAN.ProvideaVLANfrom1
to4094.
ip <IP-ADDRESS>
DisplaysdebuglogsforthespecifiedIPAddress.
mac <MAC-ADDRESS> DisplaysdebuglogsforthespecifiedMACAddress,forexample
A:B:C:D:E:F.
vrf <VRF-NAME>
DisplaysdebuglogsforthespecifiedVRF.
instance <INSTANCE-ID> Displaysdebuglogsforthespecifiedinstance.Provideaninstance
IDfrom1to255.
Examples
| switch# debug       | all     |         |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
debug db
debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]
no debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 14

Description

Enables or disables debug logging for a db module or submodules, with an option to filter by specific
criteria.

The no form of this command disables debug logging for the db module or submodule.

Parameter

all

sub-module

filter

Description

Enables all submodules for the db log.

Enables debug logging for supported submodules. Specify rx or
tx debug logs.

Specifies supported filters for the db log. Specify table, column,
or client. Optional

severity (emer|crit|alert|err|
notice|warning|info|debug)

Selects the minimum severity log level for the destination. If a
severity is not provided, the default log level is debug. Optional.

emer

crit

alert

err

notice

warning

info

debug

Usage

Specifies storage of debug logs with a severity level of emergency
only.

Specifies storage of debug logs with severity level of critical and
above.

Specifies storage of debug logs with severity level of alert and
above.

Specifies storage of debug logs with severity level of error and
above.

Specifies storage of debug logs with severity level of notice and
above.

Specifies storage of debug logs with severity level of warning and
above.

Specifies storage of debug logs with severity level of info and
above.

Specifies storage of debug logs with severity level of debug
(default).

DBlog is a high performance, configuration, and state database server logging infrastructure where a
user can log the transactions which are sent or received by clients to the configuration and state
database server. It can be enabled through the CLI and REST, and also supports filters where a user can
filter out logs on the basis of table, column, or client. It is helpful for debugging when the user wants to
debug an issue with a particular client, table, or column combination. It is not enabled by default. A
combination of filters can also be applied to filter out messages based on table, column, and client.

There are three submodules for the "db" module:

1. all: When All is enabled, no filters are applied to any of the debug logs, even if other submodules

are configured with filters.

2. tx: If enabled, only the replies and notifications sent out for the initial and incremental updates

are logged.

Debug logging | 15

3. rx:Ifenabled,onlythetransactionssenttotheconfigurationandstatedatabaseserverare
logged.
Thekeywordallmaybeusedtoenableordisabledebugloggingforallsub-modules.Alsoa
combinationoffilterscanbeusedtofilterthemessagetypes.
Ifthetableorclientfilterisapplied,thenthemessagesbelongingtothisspecifictableorclientwillbe
logged.Thecolumnfiltercanalsobeappliedtofurtherfiltermessagesonatable,providinga
mechanismtofiltermessagesonacolumn.Thetableandclientfiltercanbeusedincombinationor
separately,butcolumncanonlybeusedinconjunctionwithtable.
Examples
Configuringallsubmoduleswithseveritydebug:
| switch# | debug | db all | severity | debug |     |     |
| ------- | ----- | ------ | -------- | ----- | --- | --- |
Configuringthetxsubmodulewithtable Interfacefilterandseveritydebug:
| switch# | debug | db tx | table Interface |     | severity debug |     |
| ------- | ----- | ----- | --------------- | --- | -------------- | --- |
Configuringtherxsubmodulewithtable Interface column statisticsfilterandseveritydebug:
switch# debug db rx table Interface column statistics severity debug
Disablingtherxsubmodule:
| switch#                      | no debug    | db  | rx         |           |              |     |
| ---------------------------- | ----------- | --- | ---------- | --------- | ------------ | --- |
| Disablingthetxsubmoduletable |             |     | Interface: |           |              |     |
| switch#                      | no debug    | db  | tx table   | Interface |              |     |
| Command                      | History     |     |            |           |              |     |
| Release                      |             |     |            |           | Modification |     |
| 10.07orearlier               |             |     |            |           | --           |     |
| Command                      | Information |     |            |           |              |     |
| Platforms                    | Command     |     | context    |           | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| debug destination |     |         |        |           |           |           |
| ----------------- | --- | ------- | ------ | --------- | --------- | --------- |
| debug destination |     | {syslog | | file | | console | | buffer} | [severity |
(emer|crit|alert|err|notice|warning|info|debug)]
| no debug destination |     | {syslog | |   | file | | console} |     |
| -------------------- | --- | ------- | --- | ---- | ---------- | --- |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 16

Description
Setsthedestinationfordebuglogsandtheminimumseveritylevelforeachdestination
Thenoformofthiscommandunsetsthedestinationfordebuglogs.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{syslog | file | console | buffer} Selectsthedestinationtostoredebuglogs.Required.
| syslog  |     |     | Specifiesthatthedebuglogsarestoredinthesyslog.    |
| ------- | --- | --- | ------------------------------------------------- |
| file    |     |     | Specifiesthatdebuglogsarestoredinfile.            |
| console |     |     | Specifiesthatdebuglogsarestoredinconsole.         |
| buffer  |     |     | Specifiesthatdebuglogsarestoredinbuffer(default). |
severity (emer|crit|alert|err| Selectstheminimumseverityloglevelforthedestination.Ifa
notice|warning|info|debug) severityisnotprovided,thedefaultloglevelisdebug.
Optional.
| emer |     |     | Specifiesstorageofdebuglogswithaseveritylevelof |
| ---- | --- | --- | ----------------------------------------------- |
emergencyonly.
crit
Specifiesstorageofdebuglogswithseveritylevelofcritical
andabove.
| alert |     |     | Specifiesstorageofdebuglogswithseveritylevelofalertand |
| ----- | --- | --- | ------------------------------------------------------ |
above.
| err |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |
| --- | --- | --- | ------------------------------------------------------ |
above.
| notice |     |     | Specifiesstorageofdebuglogswithseveritylevelofnotice |
| ------ | --- | --- | ---------------------------------------------------- |
andabove.
warning Specifiesstorageofdebuglogswithseveritylevelofwarning
andabove.
info
Specifiesstorageofdebuglogswithseveritylevelofinfoand
above.
| debug |     |     | Specifiesstorageofdebuglogswithseveritylevelofdebug |
| ----- | --- | --- | --------------------------------------------------- |
(default).
Usage
Eventsthathaveaseverityequaltoorhigherthantheconfiguredseveritylevelarestoredinthe
designateddestination.Theproductdefaultstobufferfordestinationanddebugasaseveritylevel.
Examples
| switch# debug | destination | syslog severity  | alert   |
| ------------- | ----------- | ---------------- | ------- |
| switch# debug | destination | console severity | info    |
| switch# debug | destination | file severity    | warning |
Debuglogging|17

| switch#        | debug destination | buffer  | severity     | err |
| -------------- | ----------------- | ------- | ------------ | --- |
| Command        | History           |         |              |     |
| Release        |                   |         | Modification |     |
| 10.07orearlier |                   |         | --           |     |
| Command        | Information       |         |              |     |
| Platforms      | Command           | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
diag event-trap-disable
| diag event-trap-disable    |     | <EVENT-IDS> |     |     |
| -------------------------- | --- | ----------- | --- | --- |
| no diag event-trap-disable |     | <EVENT-IDS> |     |     |
Description
PreventsthespecificeventnotificationsfrombeingsentastrapstotheSNMPmanagementstations.
Thenoformofthiscommanddisablesthisfeatureandreenablesthenotificationofeventstobesent
astraps.
| Parameter   |     |     | Description                           |     |
| ----------- | --- | --- | ------------------------------------- | --- |
| <EVENT-IDS> |     |     | SpecifyuptofivecommaseparatedEventIDs |     |
Usage
Tomodifythetrapstobedisabled,suchaschangingtheexistinglistofeventIDsorremovinganevent
IDfromtheblockedtraplist,firstcompletelyremovepreviouslyconfigureddisabledtrapsusingtheCLI
commandno diag event-trap-disable <EVENT-ID>.Afterthat,reconfiguretheneweventIDsorsetof
eventIDsforthechangestotakeeffect.
Examples
Disableandthenreenableeventtraps1223and1224.
| switch# | diagnostics                |     |           |     |
| ------- | -------------------------- | --- | --------- | --- |
| switch# | diag event-trap-disable    |     | 1223,1224 |     |
| switch# | no diag event-trap-disable |     | 1223,1224 |     |
Changethelistofdisabledeventtraps.
| switch# | diagnostics                |     |           |     |
| ------- | -------------------------- | --- | --------- | --- |
| switch# | diag event-trap-disable    |     | 1223,1224 |     |
| switch# | no diag event-trap-disable |     | 1223,1224 |     |
| switch# | diag event-trap-disable    |     | 1225,1226 |     |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 18

| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.14.1000          |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show debug
| show debug [vsx-peer] |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
Description
Displaystheenableddebugtypes.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
switch#
show debug
----------------------------------------------------------------------------------
-
| module sub_module |     | severity vlan | port ip | mac | instance | vrf |
| ----------------- | --- | ------------- | ------- | --- | -------- | --- |
----------------------------------------------------------------------------------
-
| all all |     | err 1 | 1/1/1 10.0.0.1 | 1a:2b:3c:4d:5e:6f | 2   |     |
| ------- | --- | ----- | -------------- | ----------------- | --- | --- |
abcd
| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Debuglogging|19

| show       | debug buffer   |               |            |
| ---------- | -------------- | ------------- | ---------- |
| show debug | buffer [module | <MODULE-NAME> | | severity |
(emer|crit|alert|err|notice|warning|info|debug)]
Description
Displaysdebuglogsstoredinthespecifieddebugbufferwithoptionalfilteringbymoduleorseverity.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MODULE-NAME> Filtersdebuglogsdisplayedbythespecifiedmodulename.
severity (emer|crit|alert|err| Displaysdebuglogswithaspecifiedseveritylevel.Defaults
| notice|warning|info|debug) |     |     | todebug.Optional.                                      |
| -------------------------- | --- | --- | ------------------------------------------------------ |
| emer                       |     |     | Displaysdebuglogswithaseveritylevelofemergencyonly.    |
| crit                       |     |     | Displaysdebuglogswithaseveritylevelofcriticalandabove. |
| alert                      |     |     | Displaysdebuglogswithaseveritylevelofalertandabove.    |
| err                        |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |
above.
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning Displaysdebuglogswithaseveritylevelofwarningandabove.
info
Displaysdebuglogswithaseveritylevelofinfoandabove.
| debug |     |     | Displaysdebuglogswithaseveritylevelofdebug(default). |
| ----- | --- | --- | ---------------------------------------------------- |
Examples
| switch# | show debug | buffer |     |
| ------- | ---------- | ------ | --- |
------------------------------------------------------------------------------
| show | debug buffer |     |     |
| ---- | ------------ | --- | --- |
------------------------------------------------------------------------------
2017-03-06:06:51:15.089967|hpe-sysmond|SYSMON|SYSMON_CONFIG|LOG_INFO|Sysmon poll
| interval       | changed to  | 20      |              |
| -------------- | ----------- | ------- | ------------ |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 20

| show       | debug destination |            |     |
| ---------- | ----------------- | ---------- | --- |
| show debug | destination       | [vsx-peer] |     |
Description
Displaystheconfigureddebugdestinationandseverity.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# | show debug | destination |     |
| ------- | ---------- | ----------- | --- |
---------------------------------------------------------------------
| show | debug destination |     |     |
| ---- | ----------------- | --- | --- |
---------------------------------------------------------------------
CONSOLE:info
FILE:warning
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Debuglogging|21

Chapter 3
Log Rotation
Log Rotation
Logrotationprovidesyouwiththeabilitytosystematicallyrotateandarchiveanylogfilesproducedby
thesystem.Logrotationreduceslogspacerequiredontheswitch.Logrotationrotatesandcompresses
thelogfilesbasedonsizeand/orperiod.Rotatedlogfilesarestoredlocallyortransferredtoaremote
hostusingTFTP.
Startingfrom10.14.1050,notificationscanbeoptionallytriggeredifalogbufferpercentfullthresholdis
exceeded,givingyoutheopportunitytosavethelogselsewherebeforethebuffersarerotatedwiththe
oldestdatabeingoverwritten.
| Log file | paths |     |     |     |
| -------- | ----- | --- | --- | --- |
Logsstoredinthefollowingfilesarerotated:
| n Auditlogsarestoredinfile          |     | /var/log/audit/audit.log. |                     |     |
| ----------------------------------- | --- | ------------------------- | ------------------- | --- |
| n Authenticationlogsarestoredinfile |     |                           | /var/log/auth.log.  |     |
| n Eventlogsarestoredinfile          |     | /var/log/event.log.       |                     |     |
| HTTPSserverlogsarestoredinfile      |     |                           | /var/log/nginx.log. |     |
n
n NTPlogsarestoredinfile/var/log/ntp.log.
n Logsofbadloginattemptsarestoredin/var/log/btmp.
n Logsofthelastloginsessionsarestoredin/var/log/wtmp.
| About | rotated | log files |     |     |
| ----- | ------- | --------- | --- | --- |
Rotatedlogfilesarecompressedandstoredlocallyin/var/log/,regardlessoftheremotehost
configuration.Rotatedlogfilesarestoredwithrespectivetimeextensiontothegranularityofhourin
theformatfile1–YYYYMMDDHH.gz(forexample,messages-2015080715.gz).Rotatedlogfilesarereplaced
whenthenumberofoldrotatedlogfilesexceedsthree.Thenewlyrotatedlogfilereplacestheoldest
rotatedlogfile.
TFTP,SFTP,orSCPareusedtotransferrotatedlogfilestoaremotehost.Onlynewlyrotatedlogfilesare
transferredtotheremotehostduringthelogrotation.Previouslyrotatedlogfilesarenotre-transferred.
Afteralogfileissuccessfullytransferred,itisremovedfromtheswitch.
| Changing | the | size of the | log rotation | file |
| -------- | --- | ----------- | ------------ | ---- |
Bydefault,theproductrotatesthelogfileswhenthemaximumfilesizeexceeds100MB.Whenthesize
ofthelogfileexceedstheconfiguredvalue,therotationistriggeredforthatparticularlogfile.Log
rotationdoesnotoccurimmediatelyafterthemaximumfilesizeforthelogfileisreachedsincethecron
jobrunswithanhourlyperiodicity.
| logrotate | maxsize <10-200 | MB> |     |     |
| --------- | --------------- | --- | --- | --- |
IfyouareplanningtotransferthelogrotationfilebyTFTP,setthelogrotationfiletonomorethan32
MB.
Prerequisites
22
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

You must be in the configuration context:
switch(config)#

Changing the time frequency for log rotation

By default, the product rotates the log files daily. Enter the command at the configuration context in the
CLI.

Prerequisites

You must be in the configuration context:
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

At configuration context, enter the no form of the logrotate period command:

switch(config)# no logrotate period

Identifying a remote host for receiving rotated log files

You can send the rotated log files to a specified remote host Universal Resource Identifier (URI) by using
the TFTP protocol. If no URI is specified, the rotated and compressed log files are stored locally in
/var/log/. Only the TFTP protocol is supported for remote transfer, and the log rotation file cannot be
more than 32 MB. Use the Linux TFTP command to transfer the file. Rotated log files are removed from
the local path /var/log/ when it is moved to TFTP server.

Prerequisites

You must be in the configuration context:
switch(config)#

Log Rotation | 23

Procedure
ProvidethetargetIPaddress(IPv4orIPv6)attheconfigurationcontextintheCLI:
switch(config)# logrotate target {tftp://A.B.C.D | tftp://X:X::X:X}
IPv4 Example
| switch(config)# | logrotate | target tftp://192.168.1.132 |     |     |     |
| --------------- | --------- | --------------------------- | --- | --- | --- |
IPv6 Example
| switch(config)# | logrotate | target tftp://2001:db8:0:1::128 |           |     |     |
| --------------- | --------- | ------------------------------- | --------- | --- | --- |
| Remote          | transfer  | of rotated                      | log files |     |     |
OnlytheTFTPprotocolissupportedforremotetransfer,andbothIPv4andIPv6addressesare
supported.
Onlynewlyrotatedlogfilesaretransferredtotheremotehostduringthelogrotation.Previously
rotatedlogfilesarenottransferred.Afterafileissuccessfullytransferred,itisremovedfromtheswitch
localpath.
PacketlevelfailureswithTFTParehandledintheprotocolitself.WitheachTFTPsessionfailure,TFTP
retriesthefiletransferthreetimes.Retrieshaveatimeoutoffiveseconds.
| Resetting | the remote | host | for receiving | rotated | log files |
| --------- | ---------- | ---- | ------------- | ------- | --------- |
Prerequisites
Youmustbeintheconfigurationcontext:
switch(config)#
Procedure
Atconfigurationcontext,enterthenoformofthelogrotate targetcommand:
| switch(config)# | no  | logrotate target |     |     |     |
| --------------- | --- | ---------------- | --- | --- | --- |
Example:
| switch(config)# | logrotate      | target tftp://1.1.1.1 |     |     |     |
| --------------- | -------------- | --------------------- | --- | --- | --- |
| switch(config)# | do             | show logrotate        |     |     |     |
| Logrotate       | configurations | :                     |     |     |     |
| Period          | :              | daily                 |     |     |     |
| Maxsize         | :              | 10MB                  |     |     |     |
| Target          | :              | tftp://1.1.1.1        |     |     |     |
| switch(config)# | no             | logrotate target      |     |     |     |
| switch(config)# | do             | show logrotate        |     |     |     |
| Logrotate       | configurations | :                     |     |     |     |
| Period          | :              | daily                 |     |     |     |
| Maxsize         | :              | 10MB                  |     |     |     |
switch(config)#
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 24

| Resetting | the | size | of the | log rotation | file |
| --------- | --- | ---- | ------ | ------------ | ---- |
Prerequisites
Youmustbeintheconfigurationcontext:
switch(config)#
Procedure
Atconfigurationcontext,enterthenoformofthelogrotate maxsizecommand:
| switch(config)# |     | no logrotate | maxsize  |            |     |
| --------------- | --- | ------------ | -------- | ---------- | --- |
| Verifying       | the | log          | rotation | parameters |     |
Atthecommandprompt,enter:
| switch# show | logrotate |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
Exampleoutput
| switch#   | show           | logrotate |       |     |     |
| --------- | -------------- | --------- | ----- | --- | --- |
| Logrotate | configurations |           | :     |     |     |
| Period    |                | :         | daily |     |     |
| Maxsize   |                | :         | 10MB  |     |     |
switch#
LogRotation|25

Log rotation troubleshooting

Some common log file rotation troubleshooting items are as follows.

Log files not transferred remotely

Symptom

Rotated log files are not transferred to a remote host.

Cause

n The remote host might not be reachable.

n The TFTP server on the remote host might not have sufficient privileges for file creation.

Action

1. Verify that the remote host is reachable.

2. Ensure that the TFTP server is configured with the required file creation permissions.

3. For example, on the TFTPD-HPA server, change the configuration file in /etc/default/tftpd-hpa

to include -c in TFTP_OPTIONS. (for example, TFTP_OPTIONS="--secure -c.).

Log rotation not occurring immediately after max file size

Symptom

Log rotation does not occur immediately after the maximum file size for the log file is reached.

Cause

The log rotation checks the size of the file on the first minute of every hour. If the maximum file size is
reached in the meantime, the log rotation does not occur until the next hourly check of the file size.

Action

Log rotation is working as designed. The log rotation feature is designed to check the file size on an
hourly basis.

Log rotation not occurring regardless of period

Symptom

Log rotation is not happening regardless of the period value.

Cause

Log files are not rotated when they are empty files (the log file size is zero).

Action

Log rotation occurs when the log file size is greater than zero.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

26

| Log rotation | commands |     |     |
| ------------ | -------- | --- | --- |
logging threshold
logging threshold {audit-log | auth-log | commands-log |event-log | | https-server-log}
<THRESHOLD%>
no logging threshold {audit-log | auth-log | commands-log | event-log | | https-server-
log} [<THRESHOLD%>]
Description
Selectstheloggingbuffernotificationthresholdforthespecifiedloggingbuffer.Wheneverthelogging
bufferspaceconsumptionexceedstheselectedthreshold(percentofbuffercapacity),aLOG_BUFFER_
ALMOST_FULLeventandSNMPRMONtrapistriggered.Thisgivesyoutheopportunitytosavethelogs
elsewherebeforethebuffersarerotatedwiththeoldestdatabeingoverwritten.
Also,aLOG_BUFFER_WRAPPEDeventandSNMPRMONtrapistriggerediftheloggingbuffercapacityis
fullyconsumedandthelogbufferisrotatedwiththeoldestdatabeingoverwritten.
Thenoformofthiscommandresetstheloggingbufferwarningthresholdtoitsdefault.Alllogsexcept
audit-loghaveadefaultof90(percent)andaudit-loghasadefaultof50(percent).
ThelargestRESTpayloadthatcanbesenttoRADIUS/TACACSserversis1024characters,andthemaximumREST
payloadthatcanbesenttosyslogserversis3500characters.Oncethislimitisexceeded,thelogwilldisplay
threedots( …)toindicatethethemessagehasexceededthecharacterlimitandisincomplete..
| Parameter |     | Description                  |     |
| --------- | --- | ---------------------------- | --- |
| audit-log |     | Selectstheauditlog.          |     |
| auth-log  |     | Selectstheauthenticationlog. |     |
commands-log Configuretheloggingthresholdforcommandslogbuffer
| event-log        |     | Selectstheeventlog.       |     |
| ---------------- | --- | ------------------------- | --- |
| https-server-log |     | SelectstheHTTPSserverlog. |     |
<THRESHOLD%> Selectsthenotificationthresholdasapercentthattheselected
loggingbufferisfull.
Availablepercentvaluesforalllogsexceptaudit-log:15 30 50
70 90 100
Availablepercentvaluesforaudit-log:50 100
Examples
Settingtheauditlogthreshold:
| switch(config)# | logging threshold | audit-log | 100 |
| --------------- | ----------------- | --------- | --- |
Settingtheauthenticationlogthreshold:
switch(config)#
|     | logging threshold | auth-log | 50  |
| --- | ----------------- | -------- | --- |
LogRotation|27

Settingtheeventlogthreshold:
| switch(config)# | logging | threshold | event-log | 70  |
| --------------- | ------- | --------- | --------- | --- |
SettingtheHTTPSserverlogthreshold:
| switch(config)# | logging | threshold | https-server-log | 50  |
| --------------- | ------- | --------- | ---------------- | --- |
Resettingtheauditlogthresholdtoitsdefaultof50:
switch(config)#
|     | no  | logging threshold | audit-log |     |
| --- | --- | ----------------- | --------- | --- |
Resettingtheauthenticationlogthresholdtoitsdefaultof90:
| switch(config)# | no  | logging threshold | auth-log |     |
| --------------- | --- | ----------------- | -------- | --- |
Resettingtheeventlogthresholdtoitsdefaultof90:
| switch(config)# | no  | logging threshold | event-log |     |
| --------------- | --- | ----------------- | --------- | --- |
ResettingtheHTTPSserverlogthresholdtoitsdefaultof90:
| switch(config)#     | no      | logging threshold | https-server-log                    |     |
| ------------------- | ------- | ----------------- | ----------------------------------- | --- |
| Command History     |         |                   |                                     |     |
| Release             |         |                   | Modification                        |     |
| 10.11               |         |                   | Introducedthecommands-logparameter. |     |
| 10.09               |         |                   | Commandintroduced.                  |     |
| Command Information |         |                   |                                     |     |
| Platforms           | Command | context           | Authority                           |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 28

| logrotate    |         | maxsize    |     |     |     |     |
| ------------ | ------- | ---------- | --- | --- | --- | --- |
| logrotate    | maxsize | <MAX-SIZE> |     |     |     |     |
| no logrotate |         | maxsize    |     |     |     |     |
Description
Specifiesthemaximumallowedlogfilesize.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappensfirst),
triggersrotationofthelogfile.
Thenoformofthiscommandresetsthesizeofthelogfiletothedefault(100MB).
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MAX-SIZE>
Specifiestheallowedsizethelogfilecanreachbeforeitis
compressedandstoredlocallyortransferredtoaremotehost.
Range:10to200MB.Default:100MB.
Examples
Settingthemaximumlogfilesize:
| switch(config)# |     | logrotate |     | maxsize | 24  |     |
| --------------- | --- | --------- | --- | ------- | --- | --- |
Resettingthemaximumlogfilesizetoitsdefaultof100MB:
| switch(config)# |             | no      | logrotate |     | maxsize      |     |
| --------------- | ----------- | ------- | --------- | --- | ------------ | --- |
| Command         | History     |         |           |     |              |     |
| Release         |             |         |           |     | Modification |     |
| 10.07orearlier  |             |         |           |     | --           |     |
| Command         | Information |         |           |     |              |     |
| Platforms       |             | Command | context   |     | Authority    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logrotate    |        | period |     |        |           |           |
| ------------ | ------ | ------ | --- | ------ | --------- | --------- |
| logrotate    | period | {daily | |   | hourly | | monthly | | weekly} |
| no logrotate |        | period |     |        |           |           |
Description
Setsthelogfilerotationtimeperiod.Defaultstodaily.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappensfirst),
triggersrotationofthelogfile.
Thenoformofthiscommandresetsthelogrotationperiodtothedefaultofdaily.
LogRotation|29

| Parameter |     |     |     |     | Description                                        |
| --------- | --- | --- | --- | --- | -------------------------------------------------- |
| daily     |     |     |     |     | Rotateslogfilesonadailybasis(default)at0:01.       |
| hourly    |     |     |     |     | Rotateslogfileseveryhouratthefirstsecondofthehour. |
monthly Rotateslogfilesmonthlyonthefirstdayofthemonthat00:01.
| weekly |     |     |     |     | RotateslogfilesonceaweekonSundayat00:01. |
| ------ | --- | --- | --- | --- | ---------------------------------------- |
Examples
Settingaweeklyperiod:
| switch(config)# |     |     | logrotate | period | weekly |
| --------------- | --- | --- | --------- | ------ | ------ |
Resettingtheperiodtoitsdefaultofdaily:
| switch(config)# |             |         | no logrotate | period  |              |
| --------------- | ----------- | ------- | ------------ | ------- | ------------ |
| Command         | History     |         |              |         |              |
| Release         |             |         |              |         | Modification |
| 10.07orearlier  |             |         |              |         | --           |
| Command         | Information |         |              |         |              |
| Platforms       |             | Command |              | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logrotate    |        | target |         |                  |     |
| ------------ | ------ | ------ | ------- | ---------------- | --- |
| logrotate    | target | <URI>  | [vrf    | <VRF_NAME>]      |     |
| no logrotate |        | target | [<URI>] | [vrf <VRF_NAME>] |     |
Description
UsingTFTP,sendstherotatedlogfilestoaspecifiedremotehostidentifiedbyUniversalResource
Identifier(URI).
Thenoformofthiscommandresetsthetargettothedefault,whichstorestherotatedandcompressed
logfileslocallyin/var/log/.
| Command   | context |     |     |     |                                                      |
| --------- | ------- | --- | --- | --- | ---------------------------------------------------- |
| Parameter |         |     |     |     | Description                                          |
| <URI>     |         |     |     |     | SpecifiestheURIoftheremotehost.Thedefaultdirectoryis |
local.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 30

Parameter Description
tftp://{{<IPV4_ADDR>|IPV6_ADDR>}|HOST}
[/<DIRECTORY>]
<VRF_NAME> SpecifiestheVRFname(Default:default).
Usage
n Rotatedlogfilesarecompressedandstoredlocallyinthepath/var/log/regardlessoftheremote
hostconfiguration.
Examples
SettinganIPv4target:
| switch(config)# | logrotate |     | target tftp://192.168.1.132 |     |
| --------------- | --------- | --- | --------------------------- | --- |
SettinganIPv4targetwithadirectory:
switch(config)# logrotate target tftp://192.168.1.132/logrotate/
SettinganIPv4targetwiththedefaultVRF:
| switch(config)# | logrotate |     | target tftp://192.168.1.132 | vrf mgmt |
| --------------- | --------- | --- | --------------------------- | -------- |
SettinganIPv6targetwiththedefaultVRF:
switch(config)#
|     | logrotate |     | target tftp://2001:db8:0:1::128 | vrf default |
| --- | --------- | --- | ------------------------------- | ----------- |
Resettingthetargettolocal:
| switch(config)#     | no      | logrotate | target                       |     |
| ------------------- | ------- | --------- | ---------------------------- | --- |
| Command History     |         |           |                              |     |
| Release             |         |           | Modification                 |     |
| 10.09               |         |           | Updatedthesyntaxandexamples. |     |
| 10.07orearlier      |         |           | --                           |     |
| Command Information |         |           |                              |     |
| Platforms           | Command | context   | Authority                    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
LogRotation|31

show logrotate
| show logrotate | [vsx-peer] |     |     |     |
| -------------- | ---------- | --- | --- | --- |
Description
Showsthelogrotateconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#        | show logrotate |                          |              |          |
| -------------- | -------------- | ------------------------ | ------------ | -------- |
| Logrotate      | configurations | :                        |              |          |
| Period         | :              | weekly                   |              |          |
| Maxsize        | :              | 20MB                     |              |          |
| Target         | :              | tftp://2001:db8:0:1::128 |              | vrf mgmt |
| Command        | History        |                          |              |          |
| Release        |                |                          | Modification |          |
| 10.07orearlier |                |                          | --           |          |
| Command        | Information    |                          |              |          |
| Platforms      | Command        | context                  | Authority    |          |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 32

Chapter 4

Reboot reasons

Reboot reasons

The show boot-history command displays the following reboot reasons for the management module
and line module:

Reboot reasons for management module

Figure 1 Reboots handled through database

Parameter

Description

Reboot requested by user

A user requested a switch reboot through the CLI or web UI.

Reset button pressed

The switch detected a short-press of the reset button.

Backplane fault

A backplane fault occured.

Configuration change

A configuration change resulted in a reboot.

Console error

Fabric fault

Console failed to start.

A fabric fault occurred.

All line modules faulted

A zero line card condition occurred.

Redundacy switchover requested

A user requested a redundancy switchover.

Redundant Management communication

The standby management module has taken over from an

timeout

unresponsive active management module.

Redundant Management election timeout

A failure to elect a standby management module in the

alloted time.

Critical service fault (error)

A daemon critical to switch operation has stopped

functioning. An extra error string may be present to describe

the error in detail.

VSX software update

Reset triggered by a VSX software update.

Chassis critical temperature

Chassis operating temperature exceeded.

Chassis insufficient fans

Insufficient fans to cool the chassis.

Chassis unsupported PSUs/fans

Unsupported or misconfigured PSUs or system fans.

Management module critical temperature

Management module operating temperature exceeded.

Uncontrolled reboots

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

33

n ops-switchd crashed

n ovsdb-server crashed

n Reset

o Software thermal reset

o Power on reset

o Watchdog reset

o CPU request reset

o cold reset

o Long press reset

o Jumper reset

n switchd_agent crashed

Reboot reasons for line module

n Line module reboot

n Line module crashed

Reboot reasons | 34

Chapter 5

Event Logs

Event Logs

Event logging logs events generated by daemons, processes, and plug-ins running within the switch
software. The event logging framework captures the event logs in a system journal by updating the
journal fields and meta data.

Showing and clearing events

The clear events command is used to clear the event log of all events. The show events command is
used to show all event logs generated by the switch since the last reboot. See the Switch system and
hardware commands chapter chapter of the Fundamentals Guide for information on these commands.

The time stamp for event log messages generated from the Service OS indicates when the event log
messages were transferred to the event log after a switch boot and not when the issue occurred.

Messages generated from CPUs on modules other than the management module (MM) are transferred
immediately to the active event log on the MM. You can view standby logs by entering the show event –
m standby command on the active MM. You can also view the event logs for a standby MM by accessing
the standby context and entering the show events command.

See the Security Guide for information about accounting logs.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

35

Chapter 6

Client Filter

Client Filter

Event log client filter provides the ability to filter event logs for specific IP or MAC addresses. This enables
the REST client to query event logs from the switch's journal while filtering for IP or MAC address values.

New keys for IP and MAC addresses are added to the switch's journal of pre-existing keys (for example
ID and Category).

Log messages

Log messages are generated to record various events occurring within the system. Each message
contains a unique ID to represent an event and its attributes such as category, module ID or module
role. The unique ID can then be used to filter for specific event types from a switch's journal.

n REST API can filter for all events occurring on a specific IP or MAC address.

n REST API can filter for a specific event occurring on a specific IP or MAC address.

n REST API can filter for events based on a list of IPs and MACs.

Event log client filter does not support Go language daemons. Only C daemons are supported.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

36

Chapter 7
|         |               |           | Network | Configuration | Validator |
| ------- | ------------- | --------- | ------- | ------------- | --------- |
| Network | Configuration | Validator |         |               |           |
Networkconfigurationvalidator(NCV) isaconfigurationtroubleshootingtoolthathelpstodetectswitch
configurationanomaliesusingasetoffeatureconfigurationtemplates.NCVhelpstodetect
misconfigurations,identityincompleteorinter-dependentconfigurations,andmutuallyexclusive
configurations.
NCVonlydisplayspossiblewarningsanddoesnotrecommendanyconfigurationchanges.NCVdoesnot
detectconfigurationissuesbasedonnetworktopologies.
| Showing | and clearing |     | events |     |     |
| ------- | ------------ | --- | ------ | --- | --- |
Theclear eventscommandisusedtocleartheeventlogofallevents.Theshow eventscommandis
usedtoshowalleventlogsgeneratedbytheswitchsincethelastreboot.SeetheSwitchsystemand
hardwarecommandschapterchapteroftheFundamentalsGuideforinformationonthesecommands.
ThetimestampforeventlogmessagesgeneratedfromtheServiceOSindicateswhentheeventlog
messagesweretransferredtotheeventlogafteraswitchbootandnotwhentheissueoccurred.
MessagesgeneratedfromCPUsonmodulesotherthanthemanagementmodule(MM)aretransferred
immediatelytotheactiveeventlogontheMM.Youcanviewstandbylogsbyenteringtheshow event –
m standbycommandontheactiveMM.YoucanalsoviewtheeventlogsforastandbyMMbyaccessing
| thestandbycontextandenteringtheshow |     |     | eventscommand. |     |     |
| ----------------------------------- | --- | --- | -------------- | --- | --- |
SeetheSecurityGuideforinformationaboutaccountinglogs.
| Network | configuration    |     | validation | commands |     |
| ------- | ---------------- | --- | ---------- | -------- | --- |
| switch  | config-validator |     |            |          |     |
switch config-validator [config <CONFIG-NAME>] [feature <feature>] [mode {consistency |
| vsx-sync}] | [format {cli | | json}] |     |     |     |
| ---------- | ------------ | -------- | --- | --- | --- |
Description
Runsconfigurationvalidationtodetectconfigurationanomalies.
| Parameter |     |     | Description                                    |     |     |
| --------- | --- | --- | ---------------------------------------------- | --- | --- |
| config    |     |     | Specifiesconfigurationtobevalidated.Thedefault |     |     |
configurationisrunning-config.
| feature<feature> |     |     | Specifiesthenameofthefeaturetobevalidated.        |     |     |
| ---------------- | --- | --- | ------------------------------------------------- | --- | --- |
| mode             |     |     | Specifiesconfigurationvalidationmode.Thedefaultis |     |     |
consistency.
37
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
consistency Validatesfeatureconfigurationforconsistencycheck.
| vsx-sync |     |     | ValidatesVSX configurationsynchronizationbetweenVSX |
| -------- | --- | --- | --------------------------------------------------- |
peersforVSXenabledfeatures.
| format |     |     | Specifiestheresultsdisplayformat.Thedefaultiscli. |
| ------ | --- | --- | ------------------------------------------------- |
Examples
Runningconfigurationvalidationwithswitchesforthevsxfeature.
switch (config)# switch config-validator config running-config feature vsx
Line number 36: Configuration `system-mac <VSX_SYSTEM_MAC>` is recommended
Line number 36: Multi chassis configuration is recommended for VSX redundancy
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.10               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
NetworkConfigurationValidator|38

Chapter 8

Supportability Copy

Supportability Copy

To effectively diagnose various issues arising at the switch, different types of data are copied out using
copy commands for further analysis.

Use the copy core-dump command to copy the core-dump of a daemon crash.

Use the copy show-tech command to capture the status of the feature.

If there is feature misbehavior, use the copy support-files feature command to copy all feature
related information for further analysis. Additionally use copy support-log and copy diag-dump to copy
information that helps to analyze the internal behavior of a feature/daemon.

Use copy command-output to copy any show command's output to remote destinations or USB storage.

These files can be copied to a remote destination using sftp/tftp, additionally they can also be stored in
the USB storage.

In the standby management module, data can only be copied to the USB storage.

TFTP VxLAN Support

TFTP is supported over VxLAN tunnels with IPv4 underlay.

Limitations

Running-config, check-point config and startup-config will not be copied fully to destination file in TFTP
server (only partial configuration will be copied) even though TFTP shows the transfer was successful.
This is because fragmentation/ressembly/MTU discovery are not supported on VxLAN paths. Packets
exceeding 1500 bytes are dropped when the TFTP transfer is done with default TFTP block size or default
MTU size.

Workaround

Increase the MTU size (JUMBO) on all interfaces between the TFTP client and TFTP server or use a
custom block size of 1375 or less for TFTP transfers.

Example of a custom blocksize configuration:

copy running-config tftp://72.1.1.100;blocksize=1374/runv4 cli vrf vrf1
copy running-config tftp://[20:2:100];blocksize=1374/runv6 cli vrf vrf1

Supportability copy commands

copy checkpoint
copy checkpoint <CHECKPOINT-NAME> {<STORAGE-URL> | <REMOTE-URL>}

Description

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

39

CopiesthecheckpointusingTFTP,SFTP,SCP,orUSB.
| Parameter         |     |     | Description                 |     |
| ----------------- | --- | --- | --------------------------- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesthecheckpointname. |     |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |
| ------------- | --- | --- | ----------------------------------- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |
| ------------ | --- | --- | -------------------------------------- | --- |
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
{sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
n
Examples
CopyingcheckpointchpttoaremoteURL:
switch#
|                | copy checkpoint | chpt scp://root@10.0.1.1/config |                   | vrf mgmt |
| -------------- | --------------- | ------------------------------- | ----------------- | -------- |
| Command        | History         |                                 |                   |          |
| Release        |                 |                                 | Modification      |          |
| 10.08          |                 |                                 | AddedSCP support. |          |
| 10.07orearlier |                 |                                 | --                |          |
| Command        | Information     |                                 |                   |          |
| Platforms      | Command         | context                         | Authority         |          |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy command-output
copy command-output "<COMMAND>" {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}
Description
CopiesthespecifiedcommandoutputusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<COMMAND> Specifiesthecommandfromwhichyouwanttoobtainitsoutput.
Required.Userswithauditorrightscanspecifythesetwo
commandsonly:
showaccountinglog
SupportabilityCopy|40

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
showevents
{<STORAGE-URL> | <REMOTE-URL> SelecteitherthestorageURLortheremoteURLforthe
[vrf <VRF-NAME>]}
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |
| ------------- | --- | --- | ----------------------------------- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | --- | -------------------------------------- |
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
| Copyingtheoutputfromtheshow |     | eventscommandtoaremoteURL: |     |
| --------------------------- | --- | -------------------------- | --- |
switch# copy command-output "show events" tftp://10.100.0.12/file
Copyingtheoutputfromtheshow techcommandtoaremoteURLwithaVRFnamedmgmt:
switch# copy command-output "show tech" scp://user@10.100.0.12/file vrf mgmt
Copyingtheoutputfromtheshow techcommandtoaremoteURLwithaVRFnamedmgmt:
switch# copy command-output "show tech" tftp://10.100.0.12/file vrf mgmt
Copyingtheoutputfromtheshow eventscommandtoafilenamedeventsonaUSBdrive:
| switch# copy        | command-output | "show   | events" usb:/events |
| ------------------- | -------------- | ------- | ------------------- |
| Command History     |                |         |                     |
| Release             |                |         | Modification        |
| 10.08               |                |         | AddedSCP support.   |
| 10.07orearlier      |                |         | --                  |
| Command Information |                |         |                     |
| Platforms           | Command        | context | Authority           |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 41

| copy core-dump | [<MEMBER/SLOT>] |     | daemon |
| -------------- | --------------- | --- | ------ |
copy core-dump [<MEMBER/SLOT>] daemon <DAEMON-NAME>[:<INSTANCE-ID>] <REMOTE-URL> [vrf
<VRF-NAME>]
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<MEMBER/SLOT> SpecifiestheslotIDonan8400or6400switch.Required.
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
| <DAEMON-NAME> |     | Specifiesthenameofthedaemon.Required. |     |
| ------------- | --- | ------------------------------------- | --- |
[:<INSTANCE-ID>]
Specifiestheinstanceofthedaemoncoredump.Optional.
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRF
nameddefaultisused.Optional.
Examples
Copyingthecoredumpfromdaemonops-vlandtoaremoteURLwithaVRFnamedmgmt:
switch# copy core-dump daemon ops-vland sftp://abc@10.0.14.211/vland_coredump.xz
vrf mgmt
Copyingthecoredumpfromdaemonops-vlandtoaremoteURLwithaVRFnamedmgmt:
switch# copy core-dump daemon ops-vland scp://abc@10.0.14.211/vland_coredump.xz
vrf mgmt
Copyingthecoredumpfromdaemonops-switchdtoaUSBdrive:
| switch# copy | core-dump | daemon ops-switchd | usb:/switchd |
| ------------ | --------- | ------------------ | ------------ |
CopyingthecoredumpwithslotID1/1fromdaemonhpe-sysmondtoaremoteURL:
switch# copy core-dump 1/1 daemon hpe-sysmond sftp://abc@10.0.14.206/core.hpe-
| sysmond.xz | vrf mgmt |     |     |
| ---------- | -------- | --- | --- |
Copyingthecoredumpfromthehpe-configprocesstoaUSBdrive:
| switch# copy    | core-dump | daemon hpe-config | usb:/config_core |
| --------------- | --------- | ----------------- | ---------------- |
| Command History |           |                   |                  |
SupportabilityCopy|42

| Release             |         |         | Modification                                       |
| ------------------- | ------- | ------- | -------------------------------------------------- |
| 10.08               |         |         | AddedSCP support.                                  |
| 10.07orearlier      |         |         | --                                                 |
| Command Information |         |         |                                                    |
| Platforms           | Command | context | Authority                                          |
| 8400                |         |         | Administratorsorlocalusergroupmemberswithexecution |
Manager(#)
rightsforthiscommand.
| copy core-dump | [<MEMBER/SLOT>] |     | kernel |
| -------------- | --------------- | --- | ------ |
copy core-dump [<MEMBER/SLOT>] kernel <REMOTE-URL> [vrf <VRF-NAME>]
Description
CopiesakernelcoredumpusingTFTP,SFTP,orSCP.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MEMBER/SLOT>
SpecifiestheslotIDonan8400or6400switch.Required.
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput.Required. |
| ------------ | --- | --- | ----------------------------------------------- |
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME>
SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthekernelcoredumptotheURL:
switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz
CopyingthekernelcoredumptotheURLwiththeVRFnamedmgmt:
switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz vrf mgmt
CopyingthekernelcoredumpfromslotID1/1totheURLwiththeVRFnamedmgmt:
switch# copy core-dump 1/1 kernel sftp://abc@10.0.14.206/kernel_dump.tar.gz vrf
mgmt
CopyingthekernelcoredumpfromslotID1/1totheURLwiththeVRFnamedmgmt:
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 43

switch# copy core-dump 1/1 kernel scp://abc@10.0.14.206/kernel_dump.tar.gz vrf
mgmt
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | AddedSCP support. |     |
| 10.07orearlier      |         |         | --                |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy core-dump |                 | [<MEMBER/SLOT>] |                      | kernel <STORAGE-URL> |
| -------------- | --------------- | --------------- | -------------------- | -------------------- |
| copy core-dump | [<MEMBER/SLOT>] |                 | kernel <STORAGE-URL> |                      |
Description
CopiesthekernelcoredumptoaUSBdrive.
| Parameter     |     |     | Description                  |     |
| ------------- | --- | --- | ---------------------------- | --- |
| <MEMBER/SLOT> |     |     | SpecifiestheslotID.Required. |     |
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.Required.
Syntax:{usb]:/<FILE>
Examples
CopyingthekernelcoredumptoaUSBdrive:
| switch#             | copy core-dump | kernel  | usb:/kernel.tar.gz |     |
| ------------------- | -------------- | ------- | ------------------ | --- |
| Command History     |                |         |                    |     |
| Release             |                |         | Modification       |     |
| 10.07orearlier      |                |         | --                 |     |
| Command Information |                |         |                    |     |
| Platforms           | Command        | context | Authority          |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
SupportabilityCopy|44

| copy core-dump | vsf              | member                         | daemon |
| -------------- | ---------------- | ------------------------------ | ------ |
| copy core-dump | vsf member       | <MEMBER-ID>                    |        |
| daemon         | [<DAEMON-NAME>   | | <DAEMON-NAME>:<INSTANCE-ID>] |        |
| <REMOTE-URL>   | [vrf <VRF-NAME>] |                                |        |
| copy core-dump | vsf member       | <MEMBER-ID>                    |        |
| daemon         | [<DAEMON-NAME>   | | <DAEMON-NAME>:<INSTANCE-ID>] |        |
<STORAGE-URL>
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsf member <MEMBER-ID> Specifiesthemember-idoftheVSFmember.Required.
| <DAEMON-NAME> |     |     | Specifiesthenameofthedaemon.Required. |
| ------------- | --- | --- | ------------------------------------- |
[:<INSTANCE-ID>] Specifiestheinstanceofthedaemoncoredump.Optional.
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRF
nameddefaultisused.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput.Required. |
| ------------- | --- | --- | -------------------------------------------- |
Syntax:{usb}:/<FILE>
Examples
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch#                          | copy core-dump | vsf member | 1 daemon hpe-sysmond |
| -------------------------------- | -------------- | ---------- | -------------------- |
| sftp://abc@10.0.14.206/sysmon.xz |                |            | vrf mgmt             |
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch#                          | copy core-dump | vsf member | 2 daemon hpe-sysmond |
| -------------------------------- | -------------- | ---------- | -------------------- |
| scp://user@10.0.14.206/sysmon.xz |                |            | vrf mgmt             |
| Command History                  |                |            |                      |
| Release                          |                |            | Modification         |
| 10.08                            |                |            | AddedSCP support.    |
| 10.07orearlier                   |                |            | --                   |
| Command Information              |                |            |                      |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 45

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy core-dump | vsf | member | kernel |
| -------------- | --- | ------ | ------ |
copy core-dump vsf member <MEMBER-ID> kernel <REMOTE-URL> [vrf <VRF-NAME>]
| copy core-dump | vsf member | <MEMBER-ID> | kernel <STORAGE-URL> |
| -------------- | ---------- | ----------- | -------------------- |
Description
Copiesthekernelcore-dumpusingTFTP,SFTP,SCP,orUSB.
| Parameter   |     |     | Description                                   |
| ----------- | --- | --- | --------------------------------------------- |
| <MEMBER-ID> |     |     | Specifiesthemember-idoftheVSFmember.Required. |
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRF
nameddefaultisused.Optional.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.Required.
Syntax:{usb}:/<FILE>
Examples
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel sftp://abc@10.0.14.206/kernel.tar.gz
| vrf mgmt |     |     |     |
| -------- | --- | --- | --- |
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel scp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
| Command History     |     |     |                   |
| ------------------- | --- | --- | ----------------- |
| Release             |     |     | Modification      |
| 10.08               |     |     | AddedSCP support. |
| 10.07orearlier      |     |     | --                |
| Command Information |     |     |                   |
SupportabilityCopy|46

Platforms

Command context

Authority

8400

Manager (#)

Administrators or local user group members with execution
rights for this command.

copy diag-dump feature <FEATURE>
copy diag-dump feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies the specified diagnostic information using TFTP, SFTP, SCP, or USB.

Parameter

<FEATURE>

{<REMOTE-URL> [vrf <VRF-NAME> |<STORAGE-URL>]}

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

Examples

Description

The name of a feature, for example aaa or
vrrp. Required.

Select either the remote URL or the storage
URL for the destination of the copied
command output. Required.

Specifies the remote destination URL.
Required. The syntax of the URL is the
following:
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}

[:<PORT>]/<FILE>

Specifies the VRF name. If no VRF name is
provided, the VRF named default is used.
Optional.

Specifies the USB to copy command output.
Required.
Syntax: {usb}:/<FILE>

Copying the output from the aaa feature to a remote URL with a specified VRF:

switch# copy diag-dump feature aaa tftp://10.100.0.12/diagdump.txt vrf mgmt

Copying the output from the aaa feature to a remote URL with a specified VRF:

switch# copy diag-dump feature aaa scp://user@10.100.0.12/diagdump.txt vrf mgmt

Copying the output from the vrrp feature to a USB drive:

switch# copy diag-dump feature vrrp usb:/diagdump.txt

Command History

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

47

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| copy diag-dump |     | local-file |     |
| -------------- | --- | ---------- | --- |
copy diag-dump local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,orUSB.
Parameter Description
| {<REMOTE-URL> | [vrf | <VRF-NAME>] | |<STORAGE-URL>} |
| ------------- | ---- | ----------- | --------------- |
SelecteitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
<REMOTE-URL> SpecifiestheURLtocopythecommand
output.
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}
[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFname
isdefault.Optional.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Syntax:{usb}:/<FILE>
Usage
Thecopy diag-dump local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump local-
filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# diag-dump |     | aaa basic | local-file |
| ----------------- | --- | --------- | ---------- |
switch# copy diag-dump local-file tftp://10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
SupportabilityCopy|48

| switch# | diag-dump | aaa | basic | local-file |     |
| ------- | --------- | --- | ----- | ---------- | --- |
switch#
|     | copy | diag-dump | local-file |     | scp://user@10.100.0.12/diagdump.txt |
| --- | ---- | --------- | ---------- | --- | ----------------------------------- |
CopyingtheoutputfromthelocalfiletoaUSBdrive:
| switch#        | diag-dump   | aaa       | basic      | local-file |                   |
| -------------- | ----------- | --------- | ---------- | ---------- | ----------------- |
| switch#        | copy        | diag-dump | local-file |            | usb:/diagdump.txt |
| Command        | History     |           |            |            |                   |
| Release        |             |           |            |            | Modification      |
| 10.08          |             |           |            |            | AddedSCP support. |
| 10.07orearlier |             |           |            |            | --                |
| Command        | Information |           |            |            |                   |
| Platforms      |             | Command   | context    |            | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <IMAGE>
copy <IMAGE> {<STORAGE-URL> | <REMOTE-URL>} <FILE-NAME> [vrf <VRF-NAME>]
Description
CopiestheimageusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     |     |     | Description        |
| --------- | --- | --- | --- | --- | ------------------ |
| <IMAGE>   |     |     |     |     | Specifiestheimage. |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     |     |     | SpecifiestheUSBtocopycommandoutput. |
| ------------- | --- | --- | --- | --- | ----------------------------------- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     |     |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | --- | --- | --- | -------------------------------------- |
Syntax:
|             |     |     |     |     | n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE> |
| ----------- | --- | --- | --- | --- | ---------------------------------------------------------- |
|             |     |     |     |     | n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>     |
| <FILE-NAME> |     |     |     |     | Specifiesthefilename.                                      |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingtheimagetoaremoteURL:
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 49

| switch# copy | scp://root@20.0.1.1/primary.swi |     |     | primary vrf | mgmt |
| ------------ | ------------------------------- | --- | --- | ----------- | ---- |
CopyingthesecondaryimagetoaremoteURL:
switch# copy secondary scp://root@20.0.1.1/primary.swi vrf mgmt
| Command History     |         |         |                   |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- |
| Release             |         |         | Modification      |     |     |
| 10.08               |         |         | AddedSCP support. |     |     |
| 10.07orearlier      |         |         | --                |     |     |
| Command Information |         |         |                   |     |     |
| Platforms           | Command | context | Authority         |     |     |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy running-config
copy running-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     | Specifiestherunningconfiguration. |     |     |
| -------------------- | --- | --- | --------------------------------- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingtherunningconfigurationtoaremoteURL:
SupportabilityCopy|50

switch# copy running-config scp://root@10.0.1.1/config cli vrf mgmt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

--

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this
command from the auditor context (auditor>) only.

copy show-tech feature
copy show-tech feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies show tech output using TFTP, SFTP, SCP, and USB.

Parameter

Description

{<REMOTE-URL> [vrf <VRF-NAME> | <STORAGE-URL>]}

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

Select either the remote URL or the storage
URL for the destination of the copied
command output. Required.

Specifies the URL to copy the command
output. Required.

Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}

[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF
name is default. Optional.

Specifies the USB to copy command output.
Required.
Syntax: {usb}:/<FILE>

Example

Copying show tech output of the aaa feature using SCP:

switch# copy show-tech feature aaa scp://user@10.0.0.12/file.txt vrf mgmt

Copying show tech output of the config feature using SFTP on the mgmt VRF:

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

51

switch# copy show-tech feature config sftp://root@10.0.0.1/tech.txt vrf mgmt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

--

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

copy show-tech local-file
copy show-tech local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies show tech output stored in a local file.

Parameter

Description

{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]}

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

Usage

Select either the remote URL or the
storage URL for the destination of the
copied command output. Required.

Specifies the URL to copy the command
output.
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> |

<HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF
name is default. Optional.

Specifies the USB to copy command
output.
Syntax: {usb}:/<FILE>

Before entering the copy show-tech local-file command, run the show tech command with the local-
file parameter for the specified feature.

Examples

Copying the output to a remote URL:

Supportability Copy | 52

| switch# copy | show-tech | local-file | tftp://10.100.0.12/file.txt |
| ------------ | --------- | ---------- | --------------------------- |
CopyingtheoutputtoaremoteURL:
switch# copy show-tech local-file scp://user@10.100.0.12/file.txt
CopyingtheoutputtoaremoteURLwithaVRF:
switch# copy show-tech local-file tftp://10.100.0.12/file.txt vrf mgmt
CopyingtheoutputtoaUSB:
| switch# copy        | show-tech | local-file | usb:/file         |
| ------------------- | --------- | ---------- | ----------------- |
| Command History     |           |            |                   |
| Release             |           |            | Modification      |
| 10.08               |           |            | AddedSCP support. |
| 10.07orearlier      |           |            | --                |
| Command Information |           |            |                   |
| Platforms           | Command   | context    | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy startup-config
copy startup-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationusingTFTP,SFTP,SCP,orUSB.
| Parameter      |                 |     | Description |
| -------------- | --------------- | --- | ----------- |
| {<STORAGE-URL> | | <REMOTE-URL>} |     |             |
SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |
| ------------- | --- | --- | ----------------------------------- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | --- | -------------------------------------- |
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 53

| Parameter            |     |     | Description                       |
| -------------------- | --- | --- | --------------------------------- |
| config <CONFIG-NAME> |     |     | Specifiesthestartupconfiguration. |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthestartupconfigurationtoaremoteURL:
switch# copy startup-config scp://root@10.0.1.1/config json vrf mgmt
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy support-files
copy support-files
| <REMOTE-URL> | [vrf <VRF-NAME>] |     |     |
| ------------ | ---------------- | --- | --- |
<STORAGE-URL>
| all <REMOTE-URL> | [vrf | <VRF-NAME>] |     |
| ---------------- | ---- | ----------- | --- |
all <STORAGE-URL>
| feature <FEATURE-NAME> |               | <STORAGE-URL>    |                  |
| ---------------------- | ------------- | ---------------- | ---------------- |
| previous-boot          | <REMOTE-URL>  |                  | [vrf <VRF-NAME>] |
| previous-boot          | <STORAGE-URL> |                  |                  |
| module <SLOT-ID>       | <REMOTE-URL>  |                  | [vrf <VRF-NAME>] |
| module <SLOT-ID>       | <STORAGE-URL> |                  |                  |
| standby <REMOTE-URL>   |               | [vrf <VRF-NAME>] |                  |
Description
Copiesasetofsupportfilestoacompressedfileintar.gzformatusingTFTP,SFTP,SCP,orUSBortoa
directoryoverSFTPorUSB.\
DonotpressControl+Zatthepasswordpromptwhilecopyingsupportfiles,asthiswillpreventtheconsole
fromexecutingothercommands.
SupportabilityCopy|54

Parameter

<FEATURE-NAME>

{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]}

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

<SLOT-ID>

Usage

Description

The feature name, for example, aaa.

Select either the remote URL or the storage
URL for the destination of the copied
command output. Required.

Specifies the URL to copy the command
output.
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> |

<HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF
name is default. Optional.

Specifies the USB to copy command
output.
Syntax: {usb}:/<FILE>

Specifies the slot ID on 8400 switches.
Optional.
Syntax: Slot number for line (1/1-1/4, 1/7-
1/10) MM(1/5 or 1/6)

If feature name is not provided, the command collects generic system-specific support information. If a
feature name is provided, the command collects feature-specific support information.

In order to collect data from the standby swtich, the command will prompt for the local user password once.

Examples

Copying the support files to a remote URL:

switch# copy support-files tftp://10.100.0.12/file.tar.gz

Copying the support files of the lldp feature to a remote URL with a specified VRF:

switch# copy support-files feature lldp tftp://10.100.0.12/file.tar.gz vrf mgmt

Copying the support files from the previous boot to a remote URL with a specified VRF:

switch# copy support-files previous-boot scp://user@10.0.14.206/file.tar.gz vrf
mgmt

Copying the support files to a USB:

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

55

| switch# | copy | support-files | usb:/file.tar.gz |     |     |
| ------- | ---- | ------------- | ---------------- | --- | --- |
CopyingthefilesfromamoduletoaremoteURLwithaspecifiedVRFonan8400or6400switch:
switch# copy support-files module 1/1 tftp://10.100.0.12/file.tar.gz vrf mgmt
CopyingthefilesfromastandbymoduletoaremoteURLwithaspecifiedVRFonan8400or6400
switch:
switch# copy support-files standby sftp://root@10.0.14.216/file.tar.gz vrf mgmt
CopyingallthesupportfilestoaremoteURL:
switch# copy support-files all sftp://root@10.0.14.216/file.tar.gz vrf mgmt
CopyingthesupportfilesoftheconfigfeaturetoaUSB:
| switch#        | copy        | support-files | feature | config            | usb:/file.tar.gz |
| -------------- | ----------- | ------------- | ------- | ----------------- | ---------------- |
| Command        | History     |               |         |                   |                  |
| Release        |             |               |         | Modification      |                  |
| 10.08          |             |               |         | AddedSCP support. |                  |
| 10.07orearlier |             |               |         | --                |                  |
| Command        | Information |               |         |                   |                  |
| Platforms      |             | Command       | context | Authority         |                  |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy | support-files |     | local-file |     |     |
| ---- | ------------- | --- | ---------- | --- | --- |
copy support-files [feature <FEATURE-NAME> | previous-boot | all ] local-file {<REMOTE-
| URL> [vrf | <VRF-NAME>] |     | | <STORAGE-URL>} |     |     |
| --------- | ----------- | --- | ---------------- | --- | --- |
Description
Storesasetofsupportfilesasacompressedfileintheswitchlocallyandcopiesthepreservedsupport
filestoadirectoryusingTFTP,SFTP,SCP,orUSB.Youcanstoreonlyonecopyofthesupportfilelocally.
Whenyoustoreanewsupportfile,itoverwritestheexistingsupportfile
DonotpressControl+Zatthepasswordpromptwhilecopyingsupportfiles,asthiswillpreventtheconsole
fromexecutingothercommands.
SupportabilityCopy|56

| Parameter      |     |     | Description                            |     |
| -------------- | --- | --- | -------------------------------------- | --- |
| <FEATURE-NAME> |     |     | Specifiesthefeatureforthesupportfiles. |     |
<SLOT-ID> Specifiesthemoduleslotnumberidentifierforthesupportfiles.
Range:1/1-1/4,1/7-1/10
<MEMBER-ID> SpecifiestheVSFmemberidentifierforthesupportfiles.Range:1-
10
| <REMOTE-URL>  |     |     | SpecifiestheURLtocopythesupportfiles.           |     |
| ------------- | --- | --- | ----------------------------------------------- | --- |
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopythesupportfiles.           |     |
| <VRF-NAME>    |     |     | SpecifiestheVRFname.ThedefaultVRFnameisdefault. |     |
Usage
Ifthecopyofthesupportfilestothedestinationfails,analternateoptionispromptedtostorethe
collecteddatainthelocalfile.Thishelpsustoretrythecopyprocessusingcopy support-files local-file
<REMOTE-URL/STORAGE-URL>withouttheneedofregeneratingthefile.
Examples
Copyingsupportfiletothelocalfile:
| switch# copy | support-files | local-file    |            |            |
| ------------ | ------------- | ------------- | ---------- | ---------- |
| switch# copy | support-files | feature       | lldp       | local-file |
| switch# copy | support-files | previous-boot |            | local-file |
| switch# copy | support-files | all           | local-file |            |
The operation to copy all support files could take a while to complete.
| Do you want | to continue | (y/n)? |     |     |
| ----------- | ----------- | ------ | --- | --- |
CopyinglocalsupportfiletoaremoteURLandstorageURL:
switch# copy support-files local-file usb:/support_files_dir_path/
switch# copy support-files local-file scp://root@10.0.14.206//support_files_dir_
| path/abc.tar.gz     | vrf     | mgmt    |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Command History     |         |         |              |     |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy support-log
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 57

copy support-log <DAEMON-NAME> [<MEMBER/SLOT>] {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-
NAME>]}

Description

Copies the specified support log for a daemon TFTP, SFTP, SCP, or USB.

Parameter

<MEMBER/SLOT>

Description

Specifies the slot ID on an 8400 or 6400
switch. Optional.
Syntax: Slot number for line (1/1-1/4, 1/7-
1/10) MM(1/5 or 1/6)

<DAEMON-NAME>

Specifies the name of the daemon. Required.

{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}

<STORAGE-URL>

<REMOTE-URL>

vrf <VRF-NAME>

Usage

Selects either the storage URL or the remote
URL for the destination of the copied
command output. Required.

Specifies the USB to copy command output.
Syntax: {usb}:/<FILE>

Specifies the URL to copy the command
output.
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> |

<HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. If no VRF name is
provided, the VRF named default is used.
Optional.

Fast log is a high performance, per-daemon binary logging infrastructure used to debug daemon level
issues by precisely capturing the per daemon/module/functionalities debug traces in real time. Fast log,
also referred to as support logs, helps users to understand the feature internals and its specific
happenings. The fast logs from one daemon are not overwritten by other daemon logs because fast
logs are captured as part of a daemon core dump. Fast logs are enabled by default.

Examples

Copying the support log from the daemon hpe-fand to a remote URL:

switch# copy support-log hpe-fand tftp://10.100.0.12/file

Copying the support log from the daemon fand to a remote URL with a VRF named mgmt:

switch# copy support-log fand scp://user@10.100.0.12/file vrf mgmt

Copying the support log from the daemon hpe-fand to a remote URL with a VRF named mgmt:

Supportability Copy | 58

switch# copy support-log hpe-fand tftp://10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaUSB:
| switch# copy | support-log | hpe-fand | usb:/support-log |
| ------------ | ----------- | -------- | ---------------- |
Copyingthesupportlogfromthedaemoncrash-handlerforamember/slot1/1toaremoteURLwitha
VRFnamedmgmt:
switch# copy support-log crash-handler 1/1 sftp://user@10.0.14.206/cras_3_8 vrf
mgmt
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 59

Chapter 9
Traceroute
Traceroute
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
Protocol(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashop
limit,isusedindeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
| Traceroute | over VXLAN |     |
| ---------- | ---------- | --- |
Tracerouteandtraceroute6aresupportedoverVXLANfromVTEPtoVTEP,VTEPtohost,andhostto
VTEPoverL2VNI/L3VNI.AuniqueIPonVTEPshouldbeusedasthetraceroutesourceanddestination.
BothsourceanddestinationVTEPsrequireAOS-CX10.8orlaterforthisfeaturetowork.Tracerouteand
traceroute6overVXLANcannotbeusedtotracktheunderlayhopsbetweenVTEPs.
Tracerouteandtraceroute6aresupportedonallplatformswithnon-VXLAN.
Tracerouteandtraceroute6aresupportedonallplatformswithVXLANIPv4underlaysupport.
Tracerouteandtraceroute6aresupportedon6300,6400,8100,and8360withVXLAN IPv6underlay.
| Traceroute | commands |     |
| ---------- | -------- | --- |
traceroute
traceroute {<IPV4-ADDR> | <HOSTNAME>} [ip-option loosesourceroute <IPV4-ADDR>] [dstport
<NUMBER> | maxttl <NUMBER> | minttl <NUMBER> | probes <NUMBER> | timeout <TIME>] [vrf
| <VRF-NAME>] | source {<IPV4-ADDR> | | <IFNAME>} |
| ----------- | ------------------- | ----------- |
TracerouteoverVXLANwithip-option loosesourcerouteonL3VNIisnotsupported.
Description
UsestracerouteforthespecifiedIPv4addressorhostnamewithorwithoutoptionalparameters.
| Parameter    |             | Description                                  |
| ------------ | ----------- | -------------------------------------------- |
| IPv4-address | <IPV4-ADDR> | SpecifiestheIPv4address.                     |
| hostname     |             | Specifiesthehostnameofthedevicetotraceroute. |
| ip-option    |             | SpecifiestheIPoption.                        |
loosesourceroute <IPV4-ADDR> Specifiestherouteforloosesourcerecordroute.Enteroneor
moreintermediaterouterIPaddressesseparatedby','forloose
sourcerouting.
60
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

| Parameter |     | Description |
| --------- | --- | ----------- |
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
maxttl <NUMBER> Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
minttl <NUMBER> SpecifiestheMinimumnumberofhopstoreachthedestination,
<1-255>.Default:1
probes <NUMBER>
Specifiesthenumberofprobes,<1-5>.Default:3
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.
source {<IPV4-ADDR> | <IFNAME>} SpecifiesthesourceIPv4addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
Protocol(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashop
limit,isusedindeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
Examples
| switch# traceroute | 10.0.10.1 |     |
| ------------------ | --------- | --- |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 10.0.40.2        | 0.002ms   | 0.002ms 0.001ms |
| ------------------ | --------- | --------------- |
| 2 10.0.30.1        | 0.002ms   | 0.001ms 0.001ms |
| 3 10.0.10.1        | 0.001ms   | 0.002ms 0.002ms |
| switch# traceroute | localhost |                 |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 127.0.0.1        | 0.018ms   | 0.006ms 0.003ms |
| ------------------ | --------- | --------------- |
| switch# traceroute | 10.0.10.1 | maxttl 20       |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 3 sec. timeout, 3
probes
| 1 10.0.40.2        | 0.002ms   | 0.002ms 0.001ms |
| ------------------ | --------- | --------------- |
| 2 10.0.30.1        | 0.002ms   | 0.001ms 0.001ms |
| 3 10.0.10.1        | 0.001ms   | 0.002ms 0.002ms |
| switch# traceroute | 10.0.10.1 | minttl 1        |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 10.0.40.2        | 0.002ms   | 0.002ms 0.001ms |
| ------------------ | --------- | --------------- |
| 2 10.0.30.1        | 0.002ms   | 0.001ms 0.001ms |
| 3 10.0.10.1        | 0.001ms   | 0.002ms 0.002ms |
| switch# traceroute | 10.0.10.1 | dstport 33434   |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 10.0.40.2 | 0.002ms | 0.002ms 0.001ms |
| ----------- | ------- | --------------- |
| 2 10.0.30.1 | 0.002ms | 0.001ms 0.001ms |
Traceroute|61

| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms | 0.002ms |     |     |     |
| ------- | ---------- | --------- | --- | ------- | ------- | --- | --- | --- |
| switch# | traceroute | 10.0.10.1 |     | probes  | 2       |     |     |     |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 2
probes
| 1       | 10.0.40.2  | 0.002ms   |     | 0.002ms |     |     |     |     |
| ------- | ---------- | --------- | --- | ------- | --- | --- | --- | --- |
| 2       | 10.0.30.1  | 0.002ms   |     | 0.001ms |     |     |     |     |
| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms |     |     |     |     |
| switch# | traceroute | 10.0.10.1 |     | timeout | 5   |     |     |     |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 5 sec. timeout, 3
probes
| 1       | 10.0.40.2  | 0.002ms   |     | 0.002ms | 0.001ms |     |     |     |
| ------- | ---------- | --------- | --- | ------- | ------- | --- | --- | --- |
| 2       | 10.0.30.1  | 0.002ms   |     | 0.001ms | 0.001ms |     |     |     |
| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms | 0.002ms |     |     |     |
| switch# | traceroute | localhost |     | vrf     | red     |     |     |     |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1   | 127.0.0.1 | 0.003ms |     | 0.002ms | 0.001ms |     |     |     |
| --- | --------- | ------- | --- | ------- | ------- | --- | --- | --- |
switch#
|     | traceroute | localhost |     | mgmt |     |     |     |     |
| --- | ---------- | --------- | --- | ---- | --- | --- | --- | --- |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1   | 127.0.0.1 | 0.018ms |     | 0.006ms | 0.003ms |     |     |     |
| --- | --------- | ------- | --- | ------- | ------- | --- | --- | --- |
switch# traceroute 10.0.10.1 maxttl 20 timeout 5 minttl 1 probes 3 dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1   | 10.0.40.2 | 0.002ms |     | 0.002ms | 0.001ms |     |     |     |
| --- | --------- | ------- | --- | ------- | ------- | --- | --- | --- |
| 2   | 10.0.30.1 | 0.002ms |     | 0.001ms | 0.001ms |     |     |     |
| 3   | 10.0.10.1 | 0.001ms |     | 0.002ms | 0.002ms |     |     |     |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1   | 10.0.40.2 | 0.002ms |     | 0.002ms | 0.001ms |     |     |     |
| --- | --------- | ------- | --- | ------- | ------- | --- | --- | --- |
| 2   | 10.0.30.1 | 0.002ms |     | 0.001ms | 0.001ms |     |     |     |
| 3   | 10.0.10.1 | 0.001ms |     | 0.002ms | 0.002ms |     |     |     |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2 maxttl 20
| timeout | 5 minttl | 1 probes |     | 3 dstport | 33434 |     |     |     |
| ------- | -------- | -------- | --- | --------- | ----- | --- | --- | --- |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1          | 10.0.40.2  | 0.002ms  |             | 0.002ms | 0.001ms      |                     |           |      |
| ---------- | ---------- | -------- | ----------- | ------- | ------------ | ------------------- | --------- | ---- |
| 2          | 10.0.30.1  | 0.002ms  |             | 0.001ms | 0.001ms      |                     |           |      |
| 3          | 10.0.10.1  | 0.001ms  |             | 0.002ms | 0.002ms      |                     |           |      |
| switch#    | traceroute | 10.0.0.2 |             | source  | 10.0.0.1     |                     |           |      |
| traceroute | to         | 10.0.0.2 | (10.0.0.2), |         | 30 hops      | max                 |           |      |
| 1          | 10.0.0.2   | 0.299ms  | 0.155ms     |         | 0.115ms      |                     |           |      |
| switch#    | traceroute | 10.0.0.2 |             | source  | 1/1/1        |                     |           |      |
| traceroute | to         | 10.0.0.2 | (10.0.0.2), |         | 30 hops      | max                 |           |      |
| 1          | 10.0.0.2   | 0.479ms  | 0.222ms     |         | 0.171ms      |                     |           |      |
| Command    | History    |          |             |         |              |                     |           |      |
| Release    |            |          |             |         | Modification |                     |           |      |
| 10.08      |            |          |             |         | Addedsource  | IP addressandsource | interface | name |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 62

| Release |     |     | Modification |
| ------- | --- | --- | ------------ |
parameters.
| 10.07orearlier |             |         | --        |
| -------------- | ----------- | ------- | --------- |
| Command        | Information |         |           |
| Platforms      | Command     | context | Authority |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
traceroute6
traceroute6 {<IPV6-ADDR> | <HOSTNAME>} [dstport <NUMBER> | maxttl <NUMBER> | probes
<NUMBER> | timeout <TIME>] [vrf <VRF-NAME>] source {<IPV6-ADDR> | <IFNAME>}
Description
UsestracerouteforthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.
| Parameter    |             |     | Description                                  |
| ------------ | ----------- | --- | -------------------------------------------- |
| IPv6-address | <IPV6-ADDR> |     | SpecifiestheIPv6address.                     |
| hostname     |             |     | Specifiesthehostnameofthedevicetotraceroute. |
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
maxttl <NUMBER> Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
| probes <NUMBER> |     |     | Specifiesthenumberofprobes,<1-5>.Default:3 |
| --------------- | --- | --- | ------------------------------------------ |
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse,<VRF-
NAME>.
| source {<IPV6-ADDR> | |   | <IFNAME>} |     |
| ------------------- | --- | --------- | --- |
SpecifiesthesourceIPv6addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
Protocol(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashop
limit,isusedindeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
Examples
| switch# | traceroute6 | 0:0::0:1 |     |
| ------- | ----------- | -------- | --- |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
Traceroute|63

| 1 localhost | (::1)       | 0.117     | ms  | 0.032 | ms 0.021 | ms  |
| ----------- | ----------- | --------- | --- | ----- | -------- | --- |
| switch#     | traceroute6 | localhost |     |       |          |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.089    | ms     | 0.03 ms | 0.014 | ms  |
| ----------- | ----------- | -------- | ------ | ------- | ----- | --- |
| switch#     | traceroute6 | 0:0::0:1 | maxttl | 30      |       |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms      | 0.032 | ms 0.021 | ms  |
| ----------- | ----------- | -------- | ------- | ----- | -------- | --- |
| switch#     | traceroute6 | 0:0::0:1 | dsrport |       | 33434    |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms     | 0.032 | ms 0.021 | ms  |
| ----------- | ----------- | -------- | ------ | ----- | -------- | --- |
| switch#     | traceroute6 | 0:0::0:1 | probes | 2     |          |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 2 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms      | 0.032 | ms  |     |
| ----------- | ----------- | -------- | ------- | ----- | --- | --- |
| switch#     | traceroute6 | 0:0::0:1 | timeout |       | 3   |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117     | ms  | 0.032   | ms 0.021 | ms  |
| ----------- | ----------- | --------- | --- | ------- | -------- | --- |
| switch#     | traceroute6 | localhost |     | vrf red |          |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.077     | ms  | 0.051 | ms 0.054 | ms  |
| ----------- | ----------- | --------- | --- | ----- | -------- | --- |
| switch#     | traceroute6 | localhost |     | mgmt  |          |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1) | 0.089 | ms  | 0.03 ms | 0.014 | ms  |
| ----------- | ----- | ----- | --- | ------- | ----- | --- |
switch# traceroute6 0:0::0:1 maxttl 30 timeout 3 probes 3 dstport 33434
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117   | ms     | 0.032   | ms 0.021 | ms  |
| ----------- | ----------- | ------- | ------ | ------- | -------- | --- |
| switch#     | traceroute6 | 2001::2 | source | 2001::1 |          |     |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3
| probes,   | 24 byte packets |         |        |        |     |           |
| --------- | --------------- | ------- | ------ | ------ | --- | --------- |
| 1 2001::2 | (2001::2)       | 0.4331  | ms     | 0.3186 | ms  | 0.1874 ms |
| switch#   | traceroute6     | 2001::2 | source | 1/1/1  |     |           |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3
| probes,   | 24 byte   | packets |     |                                            |     |           |
| --------- | --------- | ------- | --- | ------------------------------------------ | --- | --------- |
| 1 2001::2 | (2001::2) | 0.6145  | ms  | 0.4165                                     | ms  | 0.1620 ms |
| Command   | History   |         |     |                                            |     |           |
| Release   |           |         |     | Modification                               |     |           |
| 10.08     |           |         |     | AddedsourceIPaddressandsourceinterfacename |     |           |
parameters.
| 10.07orearlier |             |     |     | --  |     |     |
| -------------- | ----------- | --- | --- | --- | --- | --- |
| Command        | Information |     |     |     |     |     |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 64

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

Traceroute | 65

Chapter 10

Ping

Ping

The ping (Packet Internet Groper) command is a common method for troubleshooting the accessibility
of devices. It uses Internet Control Message Protocol (ICMP) echo requests and ICMP echo replies to
determine if the other device is alive. It also measures the amount of time the request takes to receive a
reply from the specified destination. The ping command is mostly used to verify IP connectivity between
two endpoints which could be switch to switch, host to host, or host to switch. The reply packet tells if
the host received the ping and the amount of time it took to return the packet.

Ping over VXLAN

Ping and ping6 are supported over VXLAN (with both IPv4 and IPv6 underlay) from VTEP to VTEP, VTEP to
host, and host to VTEP over L2 VNI/L3 VNI. A unique IP on VTEP should be used as the source and
destination. Both source and destination VTEPs require AOS-CX 10.8 or later for this feature to work.
Ping and ping6 over VXLAN with IPv4 underlay is supported on all platforms with VXLAN support.

Ping and ping6 over VXLAN with IPv6 underlay is supported on 6300, 6400, 8100, and 8360 Switch Series. IPv6

underlay is supported starting from 10.12.1000 version.

Ping with a large datagram size will not work as fragmentation, reassembly, and MTU discovery on the
VXLAN paths are not supported. The default MTU size for an underlay port is 1500. When a packet is
encapsulated via VXLAN , a VXLAN header of 50 bytes is added. With the default MTU size set on ports,
packets larger than 1422 size is not expected to go over the VXLAN tunnel and is dropped. To user larger
datagram size packets, the MTU must be increased.

Ping commands

ping
ping <IPv4-ADDR> | <hostname> [data-fill <pattern> | datagram-size <size> |
interval <time> | repetitions <number> | timeout <time> | tos <number> |
ip-option {include-timestamp | include-timestamp-and-address | record-route} |
vrf <vrfname> | do-not-fragment][source {IPv4-ADDR | IFNAME}]

Ping on VXLAN with ip-option such as include-timestamp-and-address, include-timestamp and
record-route is not supported.

Description

Pings the specified IPv4 address or hostname with or without optional parameters.

Parameter

Description

ping <IPv4-ADDR>

Selects the IPv4 address to ping.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

66

| Parameter  |     |     |     | Description                                    |     |     |     |
| ---------- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| <HOSTNAME> |     |     |     | Selectsthehostnametoping.Range:1-256characters |     |     |     |
data-fill <PATTERN> Specifiesthedatapatterninhexadecimaldigitstosend.A
maximumof16"pad"bytescanbespecifiedtofillouttheICMP
packet.Default:AB
datagram-size <SIZE> Specifiesthepingdatagramsize.Range:0-65399,default:100.
interval <TIME>
Specifiestheintervalbetweensuccessivepingrequestsin
seconds.Range:1-60seconds,default:1second.
repetitions <NUMBER> Specifiesthenumberofpacketstosend.Range:1-10000
packets,default:Fivepackets.
timeout <TIME> Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
tos <NUMBER> SpecifiestheIPTypeofServicetobeusedinPingrequest.
Range:0-255
ip-option {include-timestamp | SpecifiesanIPoption(record-routeortimestampoption).
| include-timestamp-and-address |     |     | |   |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
record-route}
| include-timestamp |     |     |     | Specifiestheintermediateroutertimestamp. |     |     |     |
| ----------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
include-timestamp-and-address SpecifiestheintermediateroutertimestampandIPaddress.
| record-route |     |     |     | Specifiestheintermediaterouteraddresses. |     |     |     |
| ------------ | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.When
VRFoptionisnotgiven,thedefaultVRFisused.
source {IPv4-ADDR | IFNAME} SpecifiesthesourceIPv4addressorinterfacetouse.
do-not-fragment Specifiesthedo-not-fragment(DF)bitinIPheaderofthePing
packet.Thisoptiondoesnotallowthepackettobefragmented
whenithastogothroughasegmentwithasmallermaximum
transmissionunit(MTU).
Examples
PinginganIPv4address:
switch#
ping 10.0.0.0
| PING 10.0.0.0        | (10.0.0.0)     | 100(128)                  |     | bytes  | of data.   |       |             |
| -------------------- | -------------- | ------------------------- | --- | ------ | ---------- | ----- | ----------- |
| 108 bytes            | from 10.0.0.0: | icmp_seq=1                |     | ttl=64 | time=0.035 |       | ms          |
| 108 bytes            | from 10.0.0.0: | icmp_seq=2                |     | ttl=64 | time=0.034 |       | ms          |
| 108 bytes            | from 10.0.0.0: | icmp_seq=3                |     | ttl=64 | time=0.034 |       | ms          |
| 108 bytes            | from 10.0.0.0: | icmp_seq=4                |     | ttl=64 | time=0.034 |       | ms          |
| 108 bytes            | from 10.0.0.0: | icmp_seq=5                |     | ttl=64 | time=0.033 |       | ms          |
| --- 10.0.0.0         | ping           | statistics                | --- |        |            |       |             |
| 5 packets            | transmitted,   | 5 received,               |     | 0%     | packet     | loss, | time 3999ms |
| rtt min/avg/max/mdev |                | = 0.033/0.034/0.035/0.000 |     |        |            | ms    |             |
Pingingthelocalhost:
Ping|67

| switch#        | ping | localhost   |     |          |       |     |          |     |
| -------------- | ---- | ----------- | --- | -------- | ----- | --- | -------- | --- |
| PING localhost |      | (127.0.0.1) |     | 100(128) | bytes |     | of data. |     |
108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.060 ms
108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.035 ms
108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.043 ms
108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.041 ms
108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.034 ms
| --- localhost        |              | ping | statistics                | ---       |     |        |       |             |
| -------------------- | ------------ | ---- | ------------------------- | --------- | --- | ------ | ----- | ----------- |
| 5 packets            | transmitted, |      | 5                         | received, | 0%  | packet | loss, | time 3998ms |
| rtt min/avg/max/mdev |              |      | = 0.034/0.042/0.060/0.011 |           |     |        | ms    |             |
Pingingaserverwithadatapattern:
switch# ping 10.0.0.2 data-fill 1234123412341234acde123456789012
| PATTERN:             | 0x1234123412341234acde123456789012 |            |                           |            |        |        |            |             |
| -------------------- | ---------------------------------- | ---------- | ------------------------- | ---------- | ------ | ------ | ---------- | ----------- |
| PING 10.0.0.2        |                                    | (10.0.0.2) |                           | 100(128)   | bytes  | of     | data.      |             |
| 108 bytes            | from                               | 10.0.0.2:  |                           | icmp_seq=1 | ttl=64 |        | time=0.207 | ms          |
| 108 bytes            | from                               | 10.0.0.2:  |                           | icmp_seq=2 | ttl=64 |        | time=0.187 | ms          |
| 108 bytes            | from                               | 10.0.0.2:  |                           | icmp_seq=3 | ttl=64 |        | time=0.225 | ms          |
| 108 bytes            | from                               | 10.0.0.2:  |                           | icmp_seq=4 | ttl=64 |        | time=0.197 | ms          |
| 108 bytes            | from                               | 10.0.0.2:  |                           | icmp_seq=5 | ttl=64 |        | time=0.210 | ms          |
| --- 10.0.0.2         |                                    | ping       | statistics                | ---        |        |        |            |             |
| 5 packets            | transmitted,                       |            | 5                         | received,  | 0%     | packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |                                    |            | = 0.187/0.205/0.225/0.015 |            |        |        | ms         |             |
Pingingaserverwithadatagramsize:
| switch#              | ping         | 10.0.0.0   | datagram-size             |            | 200    |        |            |             |
| -------------------- | ------------ | ---------- | ------------------------- | ---------- | ------ | ------ | ---------- | ----------- |
| PING 10.0.0.0        |              | (10.0.0.0) |                           | 200(228)   | bytes  | of     | data.      |             |
| 208 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=1 | ttl=64 |        | time=0.202 | ms          |
| 208 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=2 | ttl=64 |        | time=0.194 | ms          |
| 208 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=3 | ttl=64 |        | time=0.201 | ms          |
| 208 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=4 | ttl=64 |        | time=0.200 | ms          |
| 208 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=5 | ttl=64 |        | time=0.186 | ms          |
| --- 10.0.0.0         |              | ping       | statistics                | ---        |        |        |            |             |
| 5 packets            | transmitted, |            | 5                         | received,  | 0%     | packet | loss,      | time 4000ms |
| rtt min/avg/max/mdev |              |            | = 0.186/0.196/0.202/0.016 |            |        |        | ms         |             |
Pingingaserverwithanintervalspecified:
| switch#              | ping         | 9.0.0.2         | interval                  | 2          |        |          |            |             |
| -------------------- | ------------ | --------------- | ------------------------- | ---------- | ------ | -------- | ---------- | ----------- |
| PING 9.0.0.2         |              | (9.0.0.2)       | 100(128)                  |            | bytes  | of data. |            |             |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=1 | ttl=64 |          | time=0.199 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=2 | ttl=64 |          | time=0.192 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=3 | ttl=64 |          | time=0.208 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=4 | ttl=64 |          | time=0.182 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=5 | ttl=64 |          | time=0.194 | ms          |
| --- 9.0.0.2          |              | ping statistics |                           | ---        |        |          |            |             |
| 5 packets            | transmitted, |                 | 5                         | received,  | 0%     | packet   | loss,      | time 7999ms |
| rtt min/avg/max/mdev |              |                 | = 0.182/0.195/0.208/0.008 |            |        |          | ms         |             |
Pingingaserverwithaspecifiednumberofpacketstosend:
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 68

| switch#      | ping | 9.0.0.2         | repetitions |             | 10    |          |            |     |
| ------------ | ---- | --------------- | ----------- | ----------- | ----- | -------- | ---------- | --- |
| PING 9.0.0.2 |      | (9.0.0.2)       | 100(128)    |             | bytes | of data. |            |     |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=1  |       | ttl=64   | time=0.213 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=2  |       | ttl=64   | time=0.204 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=3  |       | ttl=64   | time=0.201 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=4  |       | ttl=64   | time=0.184 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=5  |       | ttl=64   | time=0.202 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=6  |       | ttl=64   | time=0.184 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=7  |       | ttl=64   | time=0.193 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=8  |       | ttl=64   | time=0.196 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=9  |       | ttl=64   | time=0.193 | ms  |
| 108 bytes    | from | 9.0.0.2:        |             | icmp_seq=10 |       | ttl=64   | time=0.200 | ms  |
| --- 9.0.0.2  |      | ping statistics |             | ---         |       |          |            |     |
10 packets transmitted, 10 received, 0% packet loss, time 8999ms
| rtt min/avg/max/mdev |     |     | = 0.184/0.197/0.213/0.008 |     |     |     | ms  |     |
| -------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
Pingingaserverwithaspecifiedtimeout:
| switch#              | ping         | 9.0.0.2         | timeout                   | 3          |       |           |            |             |
| -------------------- | ------------ | --------------- | ------------------------- | ---------- | ----- | --------- | ---------- | ----------- |
| PING 9.0.0.2         |              | (9.0.0.2)       | 100(128)                  |            | bytes | of data.  |            |             |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=1 |       | ttl=64    | time=0.175 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=2 |       | ttl=64    | time=0.192 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=3 |       | ttl=64    | time=0.190 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=4 |       | ttl=64    | time=0.181 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=5 |       | ttl=64    | time=0.197 | ms          |
| --- 9.0.0.2          |              | ping statistics |                           | ---        |       |           |            |             |
| 5 packets            | transmitted, |                 | 5                         | received,  |       | 0% packet | loss,      | time 4000ms |
| rtt min/avg/max/mdev |              |                 | = 0.175/0.187/0.197/0.007 |            |       |           | ms         |             |
PingingaserverwiththespecifiedIPTypeofService:
switch#
|                      | ping         | 9.0.0.2         | tos                       | 2          |       |           |            |             |
| -------------------- | ------------ | --------------- | ------------------------- | ---------- | ----- | --------- | ---------- | ----------- |
| PING 9.0.0.2         |              | (9.0.0.2)       | 100(128)                  |            | bytes | of data.  |            |             |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=1 |       | ttl=64    | time=0.033 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=2 |       | ttl=64    | time=0.034 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=3 |       | ttl=64    | time=0.031 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=4 |       | ttl=64    | time=0.034 | ms          |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=5 |       | ttl=64    | time=0.031 | ms          |
| --- 9.0.0.2          |              | ping statistics |                           | ---        |       |           |            |             |
| 5 packets            | transmitted, |                 | 5                         | received,  |       | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |              |                 | = 0.031/0.032/0.034/0.006 |            |       |           | ms         |             |
PingingalocalhostwiththespecifiedVRF.
| switch#        | ping | localhost   | vrf | red      |     |       |          |     |
| -------------- | ---- | ----------- | --- | -------- | --- | ----- | -------- | --- |
| PING localhost |      | (127.0.0.1) |     | 100(128) |     | bytes | of data. |     |
108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.048 ms
108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.052 ms
108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.044 ms
108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.036 ms
108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.055 ms
| --- localhost |     | ping | statistics |     | --- |     |     |     |
| ------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- |
Ping|69

5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 0.036/0.047/0.055/0.006 ms

Pinging the localhost with the default VRF:

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

switch# ping 9.0.0.2 ip-option include-timestamp
PING 9.0.0.2 (9.0.0.2) 100(168) bytes of data.
108 bytes from 9.0.0.2: icmp_seq=1 ttl=64 time=0.031 ms
TS:

59909005 absolute
0
0
0

108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.034 ms
TS:

59910005 absolute
0
0
0

108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.038 ms
TS:

59911005 absolute
0
0
0

108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.035 ms
TS:

59912005 absolute
0
0
0

108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.037 ms
TS:

59913005 absolute
0
0
0

--- 9.0.0.2 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 3999ms
rtt min/avg/max/mdev = 0.031/0.035/0.038/0.002 ms

Pinging a server with the intermediate router time stamp and address:

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

70

| switch#      | ping 9.0.0.2     | ip-option  | include-timestamp-and-address |                |            |     |
| ------------ | ---------------- | ---------- | ----------------------------- | -------------- | ---------- | --- |
| PING 9.0.0.2 | (9.0.0.2)        | 100(168)   |                               | bytes of data. |            |     |
| 108 bytes    | from 9.0.0.2:    | icmp_seq=1 |                               | ttl=64         | time=0.030 | ms  |
| TS:          | 9.0.0.2 60007355 |            | absolute                      |                |            |     |
9.0.0.2 0
9.0.0.2 0
9.0.0.2 0
| 108 bytes | from 9.0.0.2:    | icmp_seq=2 |          | ttl=64 | time=0.037 | ms  |
| --------- | ---------------- | ---------- | -------- | ------ | ---------- | --- |
| TS:       | 9.0.0.2 60008355 |            | absolute |        |            |     |
9.0.0.2 0
9.0.0.2 0
9.0.0.2 0
| 108 bytes | from 9.0.0.2:    | icmp_seq=3 |          | ttl=64 | time=0.037 | ms  |
| --------- | ---------------- | ---------- | -------- | ------ | ---------- | --- |
| TS:       | 9.0.0.2 60009355 |            | absolute |        |            |     |
9.0.0.2 0
9.0.0.2 0
9.0.0.2 0
| 108 bytes | from 9.0.0.2:    | icmp_seq=4 |          | ttl=64 | time=0.038 | ms  |
| --------- | ---------------- | ---------- | -------- | ------ | ---------- | --- |
| TS:       | 9.0.0.2 60010355 |            | absolute |        |            |     |
9.0.0.2 0
9.0.0.2 0
9.0.0.2 0
| 108 bytes | from 9.0.0.2:    | icmp_seq=5 |          | ttl=64 | time=0.039 | ms  |
| --------- | ---------------- | ---------- | -------- | ------ | ---------- | --- |
| TS:       | 9.0.0.2 60011355 |            | absolute |        |            |     |
9.0.0.2 0
9.0.0.2 0
9.0.0.2 0
| --- 9.0.0.2          | ping statistics |                           | ---       |           |       |             |
| -------------------- | --------------- | ------------------------- | --------- | --------- | ----- | ----------- |
| 5 packets            | transmitted,    | 5                         | received, | 0% packet | loss, | time 3999ms |
| rtt min/avg/max/mdev |                 | = 0.030/0.036/0.039/0.005 |           |           | ms    |             |
Pingingaserverwiththeintermediaterouteraddress:
| switch#      | ping 9.0.0.2  | ip-option  | record-route |                |            |     |
| ------------ | ------------- | ---------- | ------------ | -------------- | ---------- | --- |
| PING 9.0.0.2 | (9.0.0.2)     | 100(168)   |              | bytes of data. |            |     |
| 108 bytes    | from 9.0.0.2: | icmp_seq=1 |              | ttl=64         | time=0.034 | ms  |
| RR:          | 9.0.0.2       |            |              |                |            |     |
9.0.0.2
9.0.0.2
9.0.0.2
108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.038 ms (same route)
108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.036 ms (same route)
108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.037 ms (same route)
108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.035 ms (same route)
| --- 9.0.0.2          | ping statistics |                           | ---       |           |       |             |
| -------------------- | --------------- | ------------------------- | --------- | --------- | ----- | ----------- |
| 5 packets            | transmitted,    | 5                         | received, | 0% packet | loss, | time 3999ms |
| rtt min/avg/max/mdev |                 | = 0.034/0.036/0.038/0.001 |           |           | ms    |             |
Pingingaserverwithdo-not-fragment:
| switch# | ping 192.168.1.8 |     | datagram-size | 2000 | do-not-fragment |     |
| ------- | ---------------- | --- | ------------- | ---- | --------------- | --- |
Ping|71

| PING 192.168.1.8     |              | (192.168.1.8) |                           |            | 2000(2028)   |        | bytes of data. |        |
| -------------------- | ------------ | ------------- | ------------------------- | ---------- | ------------ | ------ | -------------- | ------ |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=1 |              | ttl=64 | time=0.721     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=2 |              | ttl=64 | time=0.792     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=3 |              | ttl=64 | time=0.857     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=4 |              | ttl=64 | time=0.833     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=5 |              | ttl=64 | time=0.836     | ms     |
| --- 192.168.1.8      |              | ping          | statistics                |            | ---          |        |                |        |
| 5 packets            | transmitted, |               | 5 received,               |            | 0%           | packet | loss, time     | 4056ms |
| rtt min/avg/max/mdev |              |               | = 0.721/0.807/0.857/0.048 |            |              |        | ms             |        |
| Command              | History      |               |                           |            |              |        |                |        |
| Release              |              |               |                           |            | Modification |        |                |        |
| 10.07orearlier       |              |               |                           |            | --           |        |                |        |
| Command              | Information  |               |                           |            |              |        |                |        |
| Platforms            | Command      |               | context                   |            | Authority    |        |                |        |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
ping6
ping6 {<IPv6-ADDR> | <HOSTNAME>} [data-fill <PATTERN> | datagram-size <SIZE> |
interval <TIME> | repetitions <NUMBER> | timeout <TIME> | vrrp <VRID> |
| vrf <VRF-NAME> |     | | source | <IPv6-ADDR> |     | |   | <IFNAME>] |     |     |
| -------------- | --- | -------- | ----------- | --- | --- | --------- | --- | --- |
Description
PingsthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.TheVRRPoptionis
providedtoself-pingtheconfiguredlink-localaddressontheVRRPgroup.
| Parameter |     |     |     |     | Description                                    |     |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| IPv6-ADDR |     |     |     |     | SelectstheIPv6addresstoping.                   |     |     |     |
| HOSTNAME  |     |     |     |     | Selectsthehostnametoping.Range:1-256characters |     |     |     |
data-fill <PATTERN> Specifiesthedatapatterninhexadecimaldigitstosend.A
maximumof16"pad"bytescanbespecifiedtofillouttheICMP
packet.Default:AB
datagram-size <SIZE> Specifiesthepingdatagramsize.Range:0-65399,default:100.
interval <TIME> Specifiestheintervalbetweensuccessivepingrequestsin
seconds.Range:1-60seconds,default:1second.
repetitions <NUMBER> Specifiesthenumberofpacketstosend.Range:1-10000packets,
default:Fivepackets.
| timeout <TIME> |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 72

| Parameter   |     |     |     |     |     | Description              |     |     |
| ----------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- |
| vrrp <VRID> |     |     |     |     |     | SpecifiestheVRRPgroupID. |     |     |
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.When
thisoptionisnotprovided,thedefaultVRFisused.
source <IPv6-ADDR> | <IFNAME> SpecifiesthesourceIPv6addressorinterfacetouse.
Examples
PinginganIPv6address:
| switch#              | ping6            | 2020::2         |     |                         |       |           |            |             |
| -------------------- | ---------------- | --------------- | --- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PING                 | 2020::2(2020::2) |                 | 100 | data                    | bytes |           |            |             |
| 108 bytes            | from             | 2020::2:        |     | icmp_seq=1              |       | ttl=64    | time=0.386 | ms          |
| 108 bytes            | from             | 2020::2:        |     | icmp_seq=2              |       | ttl=64    | time=0.235 | ms          |
| 108 bytes            | from             | 2020::2:        |     | icmp_seq=3              |       | ttl=64    | time=0.249 | ms          |
| 108 bytes            | from             | 2020::2:        |     | icmp_seq=4              |       | ttl=64    | time=0.240 | ms          |
| 108 bytes            | from             | 2020::2:        |     | icmp_seq=5              |       | ttl=64    | time=0.252 | ms          |
| --- 2020::2          |                  | ping statistics |     | ---                     |       |           |            |             |
| 5 packets            | transmitted,     |                 |     | 5 received,             |       | 0% packet | loss,      | time 4000ms |
| rtt min/avg/max/mdev |                  |                 | =   | 0.235/0.272/0.386/0.059 |       |           | ms         |             |
Pingingthelocalhost:
| switch#              | ping6                | localhost  |            |                         |      |           |            |             |
| -------------------- | -------------------- | ---------- | ---------- | ----------------------- | ---- | --------- | ---------- | ----------- |
| PING                 | localhost(localhost) |            |            | 100                     | data | bytes     |            |             |
| 108 bytes            | from                 | localhost: |            | icmp_seq=1              |      | ttl=64    | time=0.093 | ms          |
| 108 bytes            | from                 | localhost: |            | icmp_seq=2              |      | ttl=64    | time=0.051 | ms          |
| 108 bytes            | from                 | localhost: |            | icmp_seq=3              |      | ttl=64    | time=0.055 | ms          |
| 108 bytes            | from                 | localhost: |            | icmp_seq=4              |      | ttl=64    | time=0.046 | ms          |
| 108 bytes            | from                 | localhost: |            | icmp_seq=5              |      | ttl=64    | time=0.048 | ms          |
| --- localhost        |                      | ping       | statistics |                         | ---  |           |            |             |
| 5 packets            | transmitted,         |            |            | 5 received,             |      | 0% packet | loss,      | time 3998ms |
| rtt min/avg/max/mdev |                      |            | =          | 0.046/0.058/0.093/0.019 |      |           | ms         |             |
Pingingaserverwithadatapattern:
switch#
|                      | ping6            | 2020::2         | data-fill |                         | ab    |           |            |             |
| -------------------- | ---------------- | --------------- | --------- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PATTERN:             | 0xab             |                 |           |                         |       |           |            |             |
| PING                 | 2020::2(2020::2) |                 | 100       | data                    | bytes |           |            |             |
| 108 bytes            | from             | 2020::2:        |           | icmp_seq=1              |       | ttl=64    | time=0.038 | ms          |
| 108 bytes            | from             | 2020::2:        |           | icmp_seq=2              |       | ttl=64    | time=0.074 | ms          |
| 108 bytes            | from             | 2020::2:        |           | icmp_seq=3              |       | ttl=64    | time=0.076 | ms          |
| 108 bytes            | from             | 2020::2:        |           | icmp_seq=4              |       | ttl=64    | time=0.075 | ms          |
| 108 bytes            | from             | 2020::2:        |           | icmp_seq=5              |       | ttl=64    | time=0.077 | ms          |
| --- 2020::2          |                  | ping statistics |           | ---                     |       |           |            |             |
| 5 packets            | transmitted,     |                 |           | 5 received,             |       | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |                  |                 | =         | 0.038/0.068/0.077/0.015 |       |           | ms         |             |
Pingingaserverwithadatagramsize:
Ping|73

| switch#               | ping6 2020::2   | datagram-size |                         |       | 200       |            |             |
| --------------------- | --------------- | ------------- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PING 2020::2(2020::2) |                 | 200           | data                    | bytes |           |            |             |
| 208 bytes             | from 2020::2:   |               | icmp_seq=1              |       | ttl=64    | time=0.037 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=2              |       | ttl=64    | time=0.076 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=3              |       | ttl=64    | time=0.076 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=4              |       | ttl=64    | time=0.077 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=5              |       | ttl=64    | time=0.066 | ms          |
| --- 2020::2           | ping statistics |               |                         | ---   |           |            |             |
| 5 packets             | transmitted,    |               | 5 received,             |       | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev  |                 | =             | 0.037/0.066/0.077/0.016 |       |           | ms         |             |
Pingingaserverwithanintervalspecified:
| switch#               | ping6 2020::2   | interval |            | 5     |        |            |     |
| --------------------- | --------------- | -------- | ---------- | ----- | ------ | ---------- | --- |
| PING 2020::2(2020::2) |                 | 100      | data       | bytes |        |            |     |
| 108 bytes             | from 2020::2:   |          | icmp_seq=1 |       | ttl=64 | time=0.043 | ms  |
| 108 bytes             | from 2020::2:   |          | icmp_seq=2 |       | ttl=64 | time=0.075 | ms  |
| 108 bytes             | from 2020::2:   |          | icmp_seq=3 |       | ttl=64 | time=0.074 | ms  |
| 108 bytes             | from 2020::2:   |          | icmp_seq=4 |       | ttl=64 | time=0.075 | ms  |
| 108 bytes             | from 2020::2:   |          | icmp_seq=5 |       | ttl=64 | time=0.075 | ms  |
| --- 2020::2           | ping statistics |          |            | ---   |        |            |     |
5 packets transmitted, 5 received, 0% packet loss, time 19999ms
| rtt min/avg/max/mdev |     | =   | 0.043/0.068/0.075/0.014 |     |     | ms  |     |
| -------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
Pingingaserverwithaspecifiednumberofpacketstosend:
| switch#               | ping6 2020::2   | repetitions |                         |       | 6         |            |             |
| --------------------- | --------------- | ----------- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PING 2020::2(2020::2) |                 | 100         | data                    | bytes |           |            |             |
| 108 bytes             | from 2020::2:   |             | icmp_seq=1              |       | ttl=64    | time=0.039 | ms          |
| 108 bytes             | from 2020::2:   |             | icmp_seq=2              |       | ttl=64    | time=0.070 | ms          |
| 108 bytes             | from 2020::2:   |             | icmp_seq=3              |       | ttl=64    | time=0.076 | ms          |
| 108 bytes             | from 2020::2:   |             | icmp_seq=4              |       | ttl=64    | time=0.076 | ms          |
| 108 bytes             | from 2020::2:   |             | icmp_seq=5              |       | ttl=64    | time=0.071 | ms          |
| 108 bytes             | from 2020::2:   |             | icmp_seq=6              |       | ttl=64    | time=0.078 | ms          |
| --- 2020::2           | ping statistics |             |                         | ---   |           |            |             |
| 6 packets             | transmitted,    |             | 6 received,             |       | 0% packet | loss,      | time 4999ms |
| rtt min/avg/max/mdev  |                 | =           | 0.039/0.068/0.078/0.015 |       |           | ms         |             |
PingingalocalhostwiththespecifiedVRF.
| switch#                   | ping6 localhost |            | vrf                     | red  |           |            |             |
| ------------------------- | --------------- | ---------- | ----------------------- | ---- | --------- | ---------- | ----------- |
| PING localhost(localhost) |                 |            | 100                     | data | bytes     |            |             |
| 108 bytes                 | from localhost: |            | icmp_seq=1              |      | ttl=64    | time=0.038 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=2              |      | ttl=64    | time=0.050 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=3              |      | ttl=64    | time=0.039 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=4              |      | ttl=64    | time=0.040 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=5              |      | ttl=64    | time=0.027 | ms          |
| --- localhost             | ping            | statistics |                         | ---  |           |            |             |
| 5 packets                 | transmitted,    |            | 5 received,             |      | 0% packet | loss,      | time 4001ms |
| rtt min/avg/max/mdev      |                 | =          | 0.027/0.038/0.050/0.010 |      |           | ms         |             |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 74

PingingthelocalhostwiththedefaultVRF:
| switch#                   | ping6        | localhost  |            | vrf                     | mgmt |              |            |        |
| ------------------------- | ------------ | ---------- | ---------- | ----------------------- | ---- | ------------ | ---------- | ------ |
| PING localhost(localhost) |              |            |            | 100                     | data | bytes        |            |        |
| 108 bytes                 | from         | localhost: |            | icmp_seq=1              |      | ttl=64       | time=0.032 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=2              |      | ttl=64       | time=0.022 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=3              |      | ttl=64       | time=0.040 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=4              |      | ttl=64       | time=0.022 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=5              |      | ttl=64       | time=0.046 | ms     |
| --- localhost             |              | ping       | statistics |                         | ---  |              |            |        |
| 5 packets                 | transmitted, |            |            | 5 received,             |      | 0% packet    | loss, time | 3998ms |
| rtt min/avg/max/mdev      |              |            | =          | 0.022/0.032/0.046/0.010 |      |              | ms         |        |
| Command                   | History      |            |            |                         |      |              |            |        |
| Release                   |              |            |            |                         |      | Modification |            |        |
| 10.07orearlier            |              |            |            |                         |      | --           |            |        |
| Command                   | Information  |            |            |                         |      |              |            |        |
| Platforms                 |              | Command    | context    |                         |      | Authority    |            |        |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
Troubleshooting
| Operation | not | permitted |     |     |     |     |     |     |
| --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
Symptom
Theswitchdisplaysanoperation not permittedmessagewhenauserattemptstosendaping
request.
Example:
| switch#         | ping | 100.1.2.10   |            |     |           |       |         |     |
| --------------- | ---- | ------------ | ---------- | --- | --------- | ----- | ------- | --- |
| PING 100.1.2.10 |      | (100.1.2.10) |            |     | 100(128)  | bytes | of data |     |
| ping: sendmsg:  |      | Operation    |            | not | permitted |       |         |     |
| ping: sendmsg:  |      | Operation    |            | not | permitted |       |         |     |
| ping: sendmsg:  |      | Operation    |            | not | permitted |       |         |     |
| ping: sendmsg:  |      | Operation    |            | not | permitted |       |         |     |
| ping: sendmsg:  |      | Operation    |            | not | permitted |       |         |     |
| --- 100.1.2.10  |      | ping         | statistics |     | ---       |       |         |     |
5 packets transmitted, 0 received, 100% packet loss, time 4000ms
Cause
Ping|75

When an ACL is applied to the Control Plane, sending a ping request may be denied. If the ping packet
matches a drop entry in the ACL, applying a Control Plane may block traffic sent from the switch CLI ping
command.

When this situation occurs, the following error message is displayed: ping: sendmsg: Operation not
permitted. The message indicates that the ICMP echo request packet has not been sent and is blocked
by the Control Plane ACL.

When this message is not displayed, the ping request packet has been sent correctly. A ping failure in
this case represents a failure to receive the ICMP echo reply packet.

This message may also be displayed on the switch when an egress ACL is applied and is blocking the ping.

Action

1. Modify the ACL to allow the ping traffic.

2. Unapply the ACL from egress (8400/8320/8325/9300 switches) or Control Plane.

3. Ping a destination which is not matched by the ACL. For example, if the ACL is blocking traffic
based on destination IP. Depending on the ACL content, this might not always be possible like
when the ACL blocks all ICMP packets.

Network is unreachable

Symptom

User receives a "network is unreachable" message on sending a ping request.

Cause

The ping packet did not get sent, because the switch cannot find an interface with a route that leads to
the destination for one of the following reasons:

n A configuration error, such as an interface having an incorrect IP address or subnet defined.

n DHCP having failed to assign an address at all.

n The user meant to ping out the management vrf, but forgot to add vrf mgmt to the ping command.

Action

Adjust the switch configuration to ensure that a route to the destination network exists.

Destination host unreachable

Symptom

User receives a Destination host unreachable message on sending a ping request.

Cause

This issue typically indicates that the host is down or otherwise not returning ICMP echo requests. It is
also possible that an intermediate network hop is dropping the packets.

Action

Investigate whether an intermediate hop is not returning pings by using the traceroute command.
Check the intermediate hop, and then the endpoint. If the destination is another Aruba switch, it is

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

76

possible that Ingress ACLs on that switch are blocking ping packets. In such cases, the configuration
option on the destination switch should be examined.

Ping | 77

Chapter 11
|       | Using      | classifier |     | policies        | for traffic  | capture | and analysis |
| ----- | ---------- | ---------- | --- | --------------- | ------------ | ------- | ------------ |
| Using | classifier | policies   | for | traffic capture | and analysis |         |              |
AOS-CXcanuseaclassifierpolicytotroubleshootingnetworkissuesbymirroringpacketsforcapture
andanalysis.
Theprocesstofiltermirroredtrafficrequireshardwareresources,andthisprocessmaycompetefor
theseresourceswithotherconfiguredfeatures,includingexistingClassifierPoliciesandAccessControl
Lists(ACLs).Priortoconfiguringandinstallingapolicyfortroubleshootingpurposes,issue theshow
policycommandsandshow resourcescommandstodeterminewhatexistingfeaturesareconsuming
hardwareresourcesontheswitch.Thiswillalsohelptoensurethatconfigurationscreatedfor
troubleshootingarenotoverridingexistingconfigurations.Ifaswitchalreadyhasaclassifierpolicy
appliedtoonecontext(appliedglobally,interface,VLAN),consideraddingentriestothatpolicy,
temporarilyunapplyingtheexistingpolicy,orapplyingthetroubleshootingpolicytoadifferentcontext.
ClassifierPoliciescannotcapturetrafficontheout-of-bandmanagementport.Iftheportisout-of-band,its
packetsdonotenterorleavethroughtheswitchASIC,whichisrequiredformirroringoperations.
| Step | one: | create | a traffic | class |     |     |     |
| ---- | ---- | ------ | --------- | ----- | --- | --- | --- |
Thefollowingexamplecreatesatrafficclasstomatchtraffictobemirroredforfutureevaluation.Inthis
example:
n TCPandUDPprotocolsshouldincludeentriesforbothsourceanddestinationportmatchesinorder
tomirrortrafficeithertoorfromthatportnumber.
n ArubaCentraltrafficutilizesHTTPSandthereforewillmatchthatentry.
n Inthisexample,thecountkeywordisincludedsothathitcountscanbemonitoredtoverifythat
trafficismatchingtheclassentries.
n Thelastentry(ignore any any any count)isincludedtocountpacketsofallothertraffictypes
passingthroughthedevice,andtoconfirmothertrafficisreachingthepolicyforevaluation,andnot
beingmirrored.
Sequencenumbers(forexample,10,20,30)arenotmandatorywhencreatingclassentries,andwill
n
beauto-generatedifnotmanuallyspecified.
n Commentlinesareoptionalforfunctionalitybutincludedforclarity.
| switch(config)# |            | class        | ip support-mirror |             |     |     |     |
| --------------- | ---------- | ------------ | ----------------- | ----------- | --- | --- | --- |
|                 | 10 comment | OSPF         | protocol          |             |     |     |     |
|                 | 10 match   | ospf any     | any count         |             |     |     |     |
|                 | 20 comment | GRE protocol |                   |             |     |     |     |
|                 | 20 match   | gre any      | any count         |             |     |     |     |
|                 | 30 comment | BGP dst      | port              |             |     |     |     |
|                 | 30 match   | tcp any      | any eq            | bgp count   |     |     |     |
|                 | 40 comment | BGP src      | port              |             |     |     |     |
|                 | 40 match   | tcp any      | eq bgp            | any count   |     |     |     |
|                 | 50 comment | VxLAN        | dst port          |             |     |     |     |
|                 | 50 match   | udp any      | any eq            | vxlan count |     |     |     |
|                 | 60 comment | VxLAN        | src port          |             |     |     |     |
78
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

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

Create a policy that uses the class created in the previous step and sends matching traffic to mirror
session 1:

switch(config)# policy support-mirror
10 class ip support-mirror action mirror 1
exit

Step three: apply the policy

If you do not know which interface or VLAN the relevant traffic uses to enter the switch, apply the policy
globally. Alternatively, you can apply the policy to one ore more specific contexts. Note that while it is
possible to apply policies to multiple interfaces, interface types, and directions, each application
consume a hardware resources and may not be successful if resources are exhausted.

Apply the policy globally in the ingress (in) direction:

apply policy support-mirror in

AOS-CX does not allow you to apply a policy globally in the egress direction; apply a policy to a specific interface,

VLAN, or LAG if egress traffic is required.

Apply a policy to a specific physical interface in the ingress (in) direction:

switch (config)# interface 1/1/1
switch(config-if)# apply policy support-mirror in

Apply a policy to a specific physical interface in Egress (out) direction:

Using classifier policies for traffic capture and analysis | 79

| switch (config)#interface |     |       | 1/1/1  |                |     |     |     |     |
| ------------------------- | --- | ----- | ------ | -------------- | --- | --- | --- | --- |
| switch(config-if)#        |     | apply | policy | support-mirror |     | out |     |     |
ApplyapolicytoaspecificLAGinIngress(in)direction:
| switch (config)#       |     | interface | lag   | 1      |                |     |     |     |
| ---------------------- | --- | --------- | ----- | ------ | -------------- | --- | --- | --- |
| switch(config-lag-if)# |     |           | apply | policy | support-mirror |     | in  |     |
ApplyapolicytoaspecificLAGinEgress(out)direction:
| switch (config)#       |     | interface | lag   | 1      |                |     |     |     |
| ---------------------- | --- | --------- | ----- | ------ | -------------- | --- | --- | --- |
| switch(config-lag-if)# |     |           | apply | policy | support-mirror |     | out |     |
ApplyapolicytoaspecificVLANinIngress(in)direction:
| switch (config)#        |     | vlan | 100   |        |                |     |     |     |
| ----------------------- | --- | ---- | ----- | ------ | -------------- | --- | --- | --- |
| switch(config-if-vlan)# |     |      | apply | policy | support-mirror |     | in  |     |
ApplyapolicytoaspecificVLANinEgress(out)direction:
| switch (config)#        |         | vlan | 100    |        |                |     |     |     |
| ----------------------- | ------- | ---- | ------ | ------ | -------------- | --- | --- | --- |
| switch(config-if-vlan)# |         |      | apply  | policy | support-mirror |     | out |     |
| Step four:              | confirm |      | policy |        | Installation   |     |     |     |
Theoutputoftheshow classandshow policycommandsshouldincludetheconfigurationthatwas
configuredintheprevioussteps.Theoutputmustnotincludeanylinesstartingwithanexclamation
| point(!), suchas: |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
! policy support-mirror user configuration does not match active configuration.
Amessagethatstartswithexclamationpoint(!),indicatesapolicyinstallationfailure,possiblydueto
hardwareresourcelimitations.
| Step five: | confirm |     | policy | resource |     | consumption |     |     |
| ---------- | ------- | --- | ------ | -------- | --- | ----------- | --- | --- |
Next,confirmthattheingressglobalpolicylookupprocessisconsumingTCAMentries.Iftheswitchisa
chassis,eachmoduleshouldshowresourcesconsumed,asthispolicyisinstalledontheASICineach
linecard.Thefollowingexampleofshowstheoutputofashow resourcescommandissuedona6300
switch:
| 6300(config)#   |        | show resources |     |     |     |      |          |      |
| --------------- | ------ | -------------- | --- | --- | --- | ---- | -------- | ---- |
| Resource        | Usage: |                |     |     |     |      |          |      |
| Mod Description |        |                |     |     |     |      |          |      |
| Resource        |        |                |     |     |     | Used | Reserved | Free |
------------------------------------------------------------------------------
| 1/1 Ingress | Global |     | Policy Lookup |     |     |     |     |     |
| ----------- | ------ | --- | ------------- | --- | --- | --- | --- | --- |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 80

| Ingress | TCAM | Entries |     |     |     | 35 2048 |     |
| ------- | ---- | ------- | --- | --- | --- | ------- | --- |
Total
| Ingress | TCAM         | Entries |     |     |     | 35 2048 | 18432 |
| ------- | ------------ | ------- | --- | --- | --- | ------- | ----- |
| Egress  | TCAM Entries |         |     |     |     | 0 0     | 8192  |
| Ingress | Lookups      |         |     |     |     | 1       | 8     |
| Ingress | Flex         | Lookups |     |     |     | 0       | 1     |
| Egress  | Lookups      |         |     |     |     | 0       | 4     |
| Ingress | Policers     |         |     |     |     | 0       | 2047  |
| Egress  | Policers     |         |     |     |     | 0       | 2047  |
Hardwareresourceswillbeconsumedoneachmodulethathasapolicyappliedtoaninterface.Ingress
andegresspoliciesconsumeseparatehardwareresources.Thefollowingexampleshowstheoutputof
ashow resourcescommandissuedona6300switchwithapolicyappliedtoaphysicalinterfacein
bothinandoutdirections:
| 6300(config)#   |        | show resources |     |     |     |               |      |
| --------------- | ------ | -------------- | --- | --- | --- | ------------- | ---- |
| Resource        | Usage: |                |     |     |     |               |      |
| Mod Description |        |                |     |     |     |               |      |
| Resource        |        |                |     |     |     | Used Reserved | Free |
------------------------------------------------------------------------------
| 1/1 Ingress |              | Port Policy | Lookup |     |     |         |     |
| ----------- | ------------ | ----------- | ------ | --- | --- | ------- | --- |
| Ingress     | TCAM         | Entries     |        |     |     | 37 2048 |     |
| Egress      | Port Policy  | Lookup      |        |     |     |         |     |
| Egress      | TCAM Entries |             |        |     |     | 37 2048 |     |
Total
| Ingress   | TCAM         | Entries |     |        |         | 37 2048 | 18432 |
| --------- | ------------ | ------- | --- | ------ | ------- | ------- | ----- |
| Egress    | TCAM Entries |         |     |        |         | 37 2048 | 6144  |
| Ingress   | Lookups      |         |     |        |         | 1       | 8     |
| Ingress   | Flex         | Lookups |     |        |         | 0       | 1     |
| Egress    | Lookups      |         |     |        |         | 1       | 3     |
| Ingress   | Policers     |         |     |        |         | 0       | 2047  |
| Egress    | Policers     |         |     |        |         | 0       | 2047  |
| Step six: | configure    |         | a   | mirror | session |         |       |
Inthisexample,themirrorsessionwillbeconfiguredtosendtraffictotheswitchCPUforcapture:
| switch(config)#         |     | mirror | session     | 1   |     |     |     |
| ----------------------- | --- | ------ | ----------- | --- | --- | --- | --- |
| switch(config-mirror-1) |     |        | destination |     | cpu |     |     |
| switch(config-mirror-1) |     |        | enable      |     |     |     |     |
Youmayalsochoosetomirrorpacketstoanexternalcapturehost,suchasaworkstationrunning
Wiresharkforlivepacketanalysisandfurtherfiltering.SeeStepeight:capturepacketstoafileormirror
ittoahost.
| Step seven: |     | start | packet |     | capture |     |     |
| ----------- | --- | ----- | ------ | --- | ------- | --- | --- |
StartapacketcaptureusingTShark.
| switch# | diag | utilities | tshark |     |     |     |     |
| ------- | ---- | --------- | ------ | --- | --- | --- | --- |
Trafficshouldbecapturedanddumpedtoscreen.ThefollowingexampledisplayspartialTSharkoutput
whenapingpacketissentthroughtheswitch:
|     |     |     |     |     |     | Usingclassifier | policiesfortrafficcaptureandanalysis|81 |
| --- | --- | --- | --- | --- | --- | --------------- | --------------------------------------- |

| switch# | diag | utilities |     | tshark |     |     |     |     |     |     |     |     |
| ------- | ---- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Inspecting traffic mirrored to the CPU until Ctrl-C is entered.
Frame 1: 98 bytes on wire (784 bits), 98 bytes captured (784 bits) on interface
| MirrorRxNet,  |                      | id 0            |          |                    |             |        |             |     |          |     |     |     |
| ------------- | -------------------- | --------------- | -------- | ------------------ | ----------- | ------ | ----------- | --- | -------- | --- | --- | --- |
| Interface     | id:                  | 0 (MirrorRxNet) |          |                    |             |        |             |     |          |     |     |     |
| Interface     | name:                | MirrorRxNet     |          |                    |             |        |             |     |          |     |     |     |
| Encapsulation |                      | type:           | Ethernet |                    | (1)         |        |             |     |          |     |     |     |
| Arrival       | Time:                | Jul             | 18, 2023 | 22:45:21.213862080 |             |        |             | UTC |          |     |     |     |
| [Time shift   | for                  | this            | packet:  |                    | 0.000000000 |        | seconds]    |     |          |     |     |     |
| Epoch Time:   | 1689720321.213862080 |                 |          |                    | seconds     |        |             |     |          |     |     |     |
| [Time delta   | from                 | previous        |          | captured           |             | frame: | 0.000000000 |     | seconds] |     |     |     |
[Time delta from previous displayed frame: 0.000000000 seconds]
| [Time since   | reference |          | or                          | first | frame: | 0.000000000 |     | seconds] |     |     |     |     |
| ------------- | --------- | -------- | --------------------------- | ----- | ------ | ----------- | --- | -------- | --- | --- | --- | --- |
| Frame Number: |           | 1        |                             |       |        |             |     |          |     |     |     |     |
| Frame Length: |           | 98 bytes |                             | (784  | bits)  |             |     |          |     |     |     |     |
| Capture       | Length:   | 98       | bytes                       | (784  | bits)  |             |     |          |     |     |     |     |
| [Frame is     | marked:   |          | False]                      |       |        |             |     |          |     |     |     |     |
| [Frame is     | ignored:  |          | False]                      |       |        |             |     |          |     |     |     |     |
| [Protocols    | in        | frame:   | eth:ethertype:ip:icmp:data] |       |        |             |     |          |     |     |     |     |
...
| Step eight: |     | capture |     | packets |     | to  | a   | file | or mirror |     | it to | a host |
| ----------- | --- | ------- | --- | ------- | --- | --- | --- | ---- | --------- | --- | ----- | ------ |
Oncebasicpolicyconfigurationisconfirmedasworkingasexpected,youcanusethediag utilities
tshark filecommandtocapturetheTSharkoutputtoafile.
| switch# | diag | utilities |     | tshark | file |     |     |     |     |     |     |     |
| ------- | ---- | --------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
Thiscommandwillstorepacketstoacircularfile;onlythemostrecent32MBoftrafficwillbecaptured.
Usethefollowingcommandtocopyapcapfiletoaremotedevice:
| switch#    | copy | tshark-pcap |     | ?                                   |     |     |     |     |     |     |     |     |
| ---------- | ---- | ----------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| REMOTE_URL | URL  | syntax      |     | - sftp://USER@{IP|HOST}[:PORT]/FILE |     |     |     |     |     | or  |     |     |
tftp://{IP|HOST}[:PORT][;blocksize=VAL]/FILE
IfyoudonotwanttocapturetheTSharkoutputtoafile,youcanmirrorittoanexternalcapturehost.In
thefollowingexample,packetsaremirroredtoexternalcapturehost(suchasaworkstationwith
WireShark)isconnectedtointerface1/1/2:
| switch(config)#          |       | mirror |        | session     | 1   |           |     |       |     |     |     |     |
| ------------------------ | ----- | ------ | ------ | ----------- | --- | --------- | --- | ----- | --- | --- | --- | --- |
| switch(config-mirror-1)# |       |        |        | destination |     | interface |     | 1/1/2 |     |     |     |     |
| switch(config-mirror-1)# |       |        |        | enable      |     |           |     |       |     |     |     |     |
| Step nine:               | check |        | packet |             | hit | counts    |     |       |     |     |     |     |
Usetheshow policy hitcountscommandtoconfirmthatthepolicyisevaluatingtraffic.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 82

switch(config)# show policy hitcounts

In the following example, no ICMP echo reply packets are captured, as the policy globally is applied to
ingress traffic only. Remember, AOS-CX does not support applying policies globally in the

egress direction; You must apply a policy to a specific context (an interface, VLAN, or LAG) to monitor
egress traffic.

Configuration

switch# show policy hitcounts support-mirror
Statistics for Policy support-mirror:
global (in):
Matched Packets
10 class ip support-mirror action mirror 1
0 10 match ospf any any count
0 20 match gre any any count
0 30 match tcp any any eq bgp count
0 40 match tcp any eq bgp any count
0 50 match udp any any eq vxlan count
0 60 match udp any eq vxlan any count
0 70 match udp any any eq radius count
0 80 match udp any eq radius any count
0 90 match tcp any any eq https count
0 100 match tcp any eq https any count
0 110 match tcp any any eq http count
0 120 match tcp any eq http any count
5 130 match icmp any any icmp-type echo count
0 140 match icmp any any icmp-type echo-reply count
0 150 ignore any any any count

In this example, hit counts will be shown separately for each application of a policy and will reflect the
direction of the traffic (that is, ICMP echo packets entering the switch and ICMP echo reply packets
leaving the switch.)

6300(config-if)# show policy hitcounts support-mirror

Statistics for Policy support-mirror:
Interface 1/1/1 (in):
Matched Packets

Configuration

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

10 class ip support-mirror action mirror 1

10 match ospf any any count
20 match gre any any count
30 match tcp any any eq bgp count
40 match tcp any eq bgp any count
50 match udp any any eq vxlan count
60 match udp any eq vxlan any count
70 match udp any any eq radius count
80 match udp any eq radius any count
90 match tcp any any eq https count
100 match tcp any eq https any count
110 match tcp any any eq http count
120 match tcp any eq http any count
130 match icmp any any icmp-type echo count
140 match icmp any any icmp-type echo-reply count
150 ignore any any any count

Interface 1/1/1 (out):
Matched Packets

Configuration

10 class ip support-mirror action mirror 1
0
0
0

10 match ospf any any count
20 match gre any any count
30 match tcp any any eq bgp count

Using classifier policies for traffic capture and analysis | 83

| 0 40 match   | tcp any  | eq bgp any    | count      |       |
| ------------ | -------- | ------------- | ---------- | ----- |
| 0 50 match   | udp any  | any eq vxlan  | count      |       |
| 0 60 match   | udp any  | eq vxlan any  | count      |       |
| 0 70 match   | udp any  | any eq radius | count      |       |
| 0 80 match   | udp any  | eq radius     | any count  |       |
| 0 90 match   | tcp any  | any eq https  | count      |       |
| 0 100 match  | tcp any  | eq https      | any count  |       |
| 0 110 match  | tcp any  | any eq http   | count      |       |
| 0 120 match  | tcp any  | eq http any   | count      |       |
| 0 130 match  | icmp any | any icmp-type | echo count |       |
| 5 140 match  | icmp any | any icmp-type | echo-reply | count |
| 0 150 ignore | any any  | any count     |            |       |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 84

Chapter 12
Remote syslog
| Remote | syslog |     |     |     |
| ------ | ------ | --- | --- | --- |
Remotesyslogenablestheforwardingofsyslogmessagestotheremotesyslogserver.Thefeature
supportsamaximumoffourremotesyslogservers.Onlyoneconfigurationperremotesyslogserveris
allowed.TheremotesyslogserversupportsTCPandUDPtransportprotocolsandTLStoestablisha
connection.Inadditiontoforwardinglogstotheremoteserver,theycanalsobepreservedinlocal
storage.
Whentheclientcertificateassociatedwiththesyslogclientisupdated,thesyslogclientisrestartedand
anewTLSconnectionisestablishedusingtheupdatedclientcertificate.
| Syslog | over VXLAN support |     |     |     |
| ------ | ------------------ | --- | --- | --- |
SyslogmessageissupportedoverVxLANwithIPv4orIPv6underlay.
| Remote | syslog | commands |     |     |
| ------ | ------ | -------- | --- | --- |
clear accounting-logs
clear accounting-logs
Description
Usethiscommandtoclearaccountinglogs.Onceissued,onlylogsgeneratedafterthiscommandisrun
| willbedisplayedintheoutputoftheshow |     |     | accounting | logcommands. |
| ----------------------------------- | --- | --- | ---------- | ------------ |
Thiscommandwillnotclearlogswhentheloggingaccounting-format-nativefeatureisconfigured.Toclear
accountinglogsonswitcheswiththisfeatureenabled,usersshouldfirstrevertthenativeaccountingformatback
tothedefaultAOS-CXformatbyexecutingthenologgingaccounting-format-nativecommand.
Example
| switch(config)# |     | clear accounting-logs |     |     |
| --------------- | --- | --------------------- | --- | --- |
Thefollowingexampleshowsthataccountinglogscannotbeclearedusingtheclearaccounting-logs
commandifthelogging accounting-native-formatcommandhasbeenenabled,andthatdisabling
thisoptionwiththeno logging accounting-format-nativecommandagainallowstheaccountinglogs
tobecleared.
| switch# | logging               | audit-format-native |     |     |
| ------- | --------------------- | ------------------- | --- | --- |
| switch# | clear accounting-logs |                     |     |     |
Warning: Clear accounting-logs is not supported for 'audit-format-native'.
| switch# | no logging            | audit-format-native |     |     |
| ------- | --------------------- | ------------------- | --- | --- |
| switch# | clear accounting-logs |                     |     |     |
85
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

| switch# | show | accounting |     | log | last 5 |     |     |
| ------- | ---- | ---------- | --- | --- | ------ | --- | --- |
---------------------------------------------------
| Command | logs | from | current | boot |     |     |     |
| ------- | ---- | ---- | ------- | ---- | --- | --- | --- |
---------------------------------------------------
| No command |             | logs    | has been | logged  | in the system      |     |     |
| ---------- | ----------- | ------- | -------- | ------- | ------------------ | --- | --- |
| Command    | History     |         |          |         |                    |     |     |
| Release    |             |         |          |         | Modification       |     |     |
| 10.11      |             |         |          |         | Commandintroduced. |     |     |
| Command    | Information |         |          |         |                    |     |     |
| Platforms  |             | Command |          | context | Authority          |     |     |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|     |     | (#) |     |     | rightsforthiscommand. |     |     |
| --- | --- | --- | --- | --- | --------------------- | --- | --- |
logging
logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} {udp [<PORT-NUM>]}|{tcp [<PORT-
| NUM>]}|{|tls |                            | [<PORT-NUM>]} |     |     |     |     |     |
| ------------ | -------------------------- | ------------- | --- | --- | --- | --- | --- |
| auth-mode    | {certificate|subject-name} |               |     |     |     |     |     |
disable
| filter | <FILTER-NAME> |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- | --- |
include-auditable-events
legacy-tls-renegotiation]
| rate-limit-burst    |          |     | <BURST>     |     |     |     |     |
| ------------------- | -------- | --- | ----------- | --- | --- | --- | --- |
| rate-limit-interval |          |     | <INTERVAL>] |     | ]   |     |     |
| severity            | <LEVEL>] |     |             |     |     |     |     |
vrf <VRF-NAME>]
| no logging | {<IPV4-ADDR> |     | |   | <IPV6-ADDR> | | <FQDN | | HOSTNAME> | }   |
| ---------- | ------------ | --- | --- | ----------- | ------- | ----------- | --- |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
StartingwithAOS-CX10.11,payloadinformationispresentinaccountinglogs.
ThemaximumRESTpayloadthatcanbesenttoRADIUS/TACACSserveris1024characters,andthe
maximumofRESTpayloadthatcanbesenttosyslogserveris3500characters.Ifthislimitisisreached,
thelogwilldisplaythreedots(...)toindicatethattheloganexceededthecharacterlimitandis
incomplete.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
{<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>} SelectstheIPv4address,IPv6address,orhostnameof
theremotesyslogserver.Required.
[udp [<PORT-NUM>] | tcp [<PORT-NUM> | SpecifiestheUDPport,TCPport,orTLSportofthe
tls [<PORT-NUM>]] remotesyslogservertoreceivetheforwardedsyslog
messages.
Remotesyslog|86

Parameter

Description

udp [<PORT-NUM>]

tcp [<PORT-NUM>]

tls [<PORT-NUM>]

auth-mode

disable

filter <FILTER-NAME>

include-auditable-events

legacy-tls-renegotiation

rate-limit-burst <BURST>

rate-limit-interval <INTERVAL>

severity <LEVEL>

Range: 1 to 65535. Default: 514

Range: 1 to 65535. Default: 1470

Range: 1 to 65535. Default: 6514

Specifies the TLS authentication mode used to validate
the certificate.

n certificate: Validates the peer using trust anchor

certificate based authentication. Default.
n subject-name: Validates the peer using trust

anchor certificates as well as subject-name based

authentication.

Disable remote syslog confguration. This does not
delete the configuration, just disables/pauses the
forwarding of syslog messagesto the remote server.
The config/forwarding can be reenabled (un-paused)
again using the no logging <hostname> disable
command.

Specifies the name of the filter to be applied on the
syslog messages.

Specifies that auditable messages are also logged to
the remote syslog server.

Enables the TLS connection with a remote syslog
server supporting legacy renegotiation.

Specifies the rate limit for the messages sent to the
remote syslog server.

Specifies the rate limit interval in seconds. Default: 30
Seconds

Specifies the severity of the syslog messages:

n alert: Forwards syslog messages with the severity

of alert (6) and emergency (7).

n crit: Forwards syslog messages with the severity of

critical (5) and above.

n debug: Forwards syslog messages with the severity

of debug (0) and above.

n emerg: Forwards syslog messages with the severity

of emergency (7) only.

n err: Forwards syslog messages with the severity of

err (4) and above

n info: Forwards syslog messages with the severity of

info (1) and above. Default.

n notice: Forwards syslog messages with the severity

of notice (2) and above.

n warning: Forwards syslog messages with the

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

87

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
severityofwarning(3)andabove.
vrf <VRF-NAME> SpecifiestheVRFusedtoconnecttothesyslogserver.
Optional.Default:default
Examples
Enablingthesyslogforwardingtoremotesyslogserver10.0.10.2:
| switch(config)# | logging | 10.0.10.2 |     |     |     |
| --------------- | ------- | --------- | --- | --- | --- |
Enablingthesyslogforwardingofmessageswithaseverityoferr (4)andabovetoTCPport4242on
remotesyslogserver10.0.10.9withVRFlab_vrf:
switch(config)# logging 10.0.10.9 tcp 4242 severity err vrf lab_vrf
Disablingsyslogforwardingtoaremotesyslogserver:
| switch(config)# | no  | logging |     |     |     |
| --------------- | --- | ------- | --- | --- | --- |
EnablingsyslogforwardingoverTLStoaremotesyslogserverusingsubject-nameauthenticationmode:
| switch(config)#logging |     | example.com | tls auth-mode | subject-name |     |
| ---------------------- | --- | ----------- | ------------- | ------------ | --- |
Applyinglogfilteringforsyslogserverforwarding:
switch(config)# logging 10.0.10.6 severity info filter filter_lldp_logs vrf mgmt
ApplyinglogfilteringandenablingtheratelimitforsyslogserverforwardingoverTCPport:
switch(config)#
|     | logging | 10.0.10.2 | tcp 3440 severity | err vrf mgmt | include- |
| --- | ------- | --------- | ----------------- | ------------ | -------- |
auditable-events filter filter_lldp_logs rate-limit-burst 3 rate-limit-interval 35
| Command History |     |     |              |     |     |
| --------------- | --- | --- | ------------ | --- | --- |
| Release         |     |     | Modification |     |     |
Thedisableparameterisintroduced
10.12.1000
| 10.07orearlier      |         |         | --        |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Command Information |         |         |           |     |     |
| Platforms           | Command | context | Authority |     |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Remotesyslog|88

| logging | accounting-format-native |     |     |     |     |
| ------- | ------------------------ | --- | --- | --- | --- |
logging accounting-format-native
| [no] logging | accounting-format-native |     |     |     |     |
| ------------ | ------------------------ | --- | --- | --- | --- |
Description
ChangetheaccountinglogmessageformattonativeLinuxformat.(Default:ArubaOS-CXformat)
The'no'formofthiscommandwillchangetheaccountinglogmessageformattoArubaOS-CXformat.
Usage
Thisoptionenablestheswitchtoshowalltypesofaccountingrecordstotheuser.Whenconfigured,the
sameformatwillbeusedwhilesendingmessagestosyslogservers.Whenupgradingfromanearlier
versionofAOS-CXtoAOS-CX10.11orlaterversions,ifnativeaccountinglogsarepreferred,thenbest
practicesistoissuethiscommandasapartoftheupgrade.Iftheswitchupgradesfromanearlier
versiontoAOS-CX10.11orlaterwithoutconfiguringthissetting,bydefault,theaccountinglogmessage
formatwillbeArubaOS-CXFormat.
Example
ThisexamplechangestheaccountinglogmessageformattonativeLinuxformat.
| switch(config)# |     | logging |     | accounting-format-native |     |
| --------------- | --- | ------- | --- | ------------------------ | --- |
ThefollowingexamplereturnstheaccountinglogmessageformattothedefaultArubaOS-CXformat.
| switch(config)# |             | no  | logging | accounting-format-native |                    |
| --------------- | ----------- | --- | ------- | ------------------------ | ------------------ |
| Command         | History     |     |         |                          |                    |
| Release         |             |     |         |                          | Modification       |
| 10.11           |             |     |         |                          | Commandintroduced. |
| Command         | Information |     |         |                          |                    |
| Platforms       | Command     |     | context |                          | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logging        | filter        |     |     |     |     |
| -------------- | ------------- | --- | --- | --- | --- |
| logging filter | <FILTER-NAME> |     |     |     |     |
| [{enable       | | disable}]   |     |     |     |     |
[<SEQUENCE-ID>] {permit | deny} [event-id <EVENT-ID-RANGE>] [includes <REGEX>]
| [severity | <COMPARISON-OPERATOR> |     |     |     | <LEVEL>] |
| --------- | --------------------- | --- | --- | --- | -------- |
no <SEQUENCE-ID>
| resequence | <OLD-SEQUENCE-ID> |     |     | <NEW-SEQUENCE-ID> |     |
| ---------- | ----------------- | --- | --- | ----------------- | --- |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 89

no logging filter <FILTER-NAME>

Description

Creates a filter to restrict what event or debug logs are logged. A filter can be used to either permit or
deny:

n The event logs from being generated on the switch, or

n The event or debug logs generated on the switch from being forwarded to a syslog server.

A filter is identified by a filter name and can have up to 20 rules or entries, each with a different
sequence number, matching criteria, and corresponding action (deny or permit). When a filter is applied
on a log, the log is matched against the criteria mentioned in the rules or entries in ascending numerical
order of their sequence numbers until a matching entry is found. Once a matching entry is found, its
corresponding action is applied on the log. If no matching rule is found, the default action (permit) is
applied.

The no form of this command removes the filter.

Parameter

<FILTER-NAME>

enable

<SEQUENCE-ID>

deny

permit

<event-id>

Description

Specifies the unique name to identify the filter.

Filter event logs generated on the switch.

Specifies the filter criteria sequence number. Default: Increments
by 10 from the largest sequence-id currently used in this filter.

Prevents the matching log from being logged.

Allows the matching log.

Matches logs by event ID. Specify an event ID or a range of event
IDs. It supports a maximum of 100 event IDs.

includes <REGEX>

Matches the log message against a regular expression string.

severity

Usage

Matches the logs by severity level.
The following options are used to compare the severity:

n eq: Match events of severity equal to the specified.
n ge: Match events of severity greater than or equal to the

specified.

n gt: Match events of severity greater than the specified.
n le: Match events of severity lesser than or equal to the

specified.

n lt: Match events of severity lesser than the specified.
The following are the severity levels:

n alert: Logs with the severity alert (6).
n crit: Logs with the severity critical (5).
n debug: Logs with the severity debug (0).
n emerg: Logs with the severity emergency (7).
n err: Logs with the severity err (4).
n info: Logs with the severity info (1).
n notice: Logs with the severity notice (2).
n warning: Logs with the severity warning (3).

Remote syslog | 90

Filtering event logs on the switch: To permit or deny event logs from being generated on the switch.
In this case, the matching event logs are filtered at generation. The denied event logs are neither logged
to the switch events nor forwarded to any remote syslog servers. Multiple filters can be configured, but
only one filter can be applied to filter the events on the switch. Such a filter can be chosen by adding the
enable command under its configuration. Configuring the enable command under a new filter
automatically removes it from the filter where it was previously used.

For example:

logging filter low_severity_logs

enable

10 deny severity lt info

This configuration denies the event logs which have a severity less than info.

If a filter contains enable command, it is not recommended to configure this filter in the logging command used

for remote syslog server configuration. This is because, any event logs denied by the filter are already not

available for forwarding to a remote server.

A filter with enable command will not affect debug logs. Consider the configuration in the following
example of a filter with enable command and two rules applied 10 permit severity ge info and 20
deny. This implies permit only those event logs which have severity greater than or equal to info.
Example:

logging filter low_severity_logs
enable
10 permit severity ge info
20 deny

Filtering event or debug logs when forwarding to a remote syslog server: The filter name must be
configured in the logging command that is used to configure remote syslog server. The logs will be
generated on the switch and the filter only decides whether to deny or permit the syslog forwarding for
the matching log. For example: logging 10.0.10.6 filter filter_lldp_logs

The filter affects debug logs only when the command debug destination syslog is configured on the switch.

The severity mentioned in the remote syslog server configuration using logging command under configuration

context has more precedence than the severity mentioned in a filter entry. If a log with warning severity is

permitted by a filter, but the remote syslog configuration has severity err mentioned in it, the log will not be

forwarded to the remote syslog server (since warning(3) is lesser than err(4)). On the other hand, if a log with err

severity is permitted by a filter and the remote syslog configuration has severity warning mentioned in it, the log

will be forwarded to the remote syslog server.

Examples

Configuring a new logging filter:

switch(config)# logging filter example_filter

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

91

TodenylogshavingeventID1301andarangeofeventIDsfrom1305to1309:
| switch(config-logging-filter)# |     |     | 20 deny event-id | 1301,1305-1309 |
| ------------------------------ | --- | --- | ---------------- | -------------- |
TopermitlogshavingeventID1300:
| switch(config-logging-filter)# |     |     | 30 permit event-id | 1300 |
| ------------------------------ | --- | --- | ------------------ | ---- |
Topermitlogswithseveritygreaterthanorequaltoerr:
switch(config-logging-filter)#
|     |     |     | 30 permit severity | ge err |
| --- | --- | --- | ------------------ | ------ |
Todenylogswithseveritygreaterthaninfo:
| switch(config-logging-filter)# |     |     | 30 deny severity | gt info |
| ------------------------------ | --- | --- | ---------------- | ------- |
TodenylogswitheventID1024andamessagematchingtheregularexpressionLLDP:
switch(config-logging-filter)# 40 deny event-id 1024 includes LLDP
Denyingalllogs:
| switch(config-logging-filter)# |     |     | 40 deny |     |
| ------------------------------ | --- | --- | ------- | --- |
ChangingthesequenceIDofanexistingrule:
| switch(config-logging-filter)# |         |         | resequence 20 | 70  |
| ------------------------------ | ------- | ------- | ------------- | --- |
| Command History                |         |         |               |     |
| Release                        |         |         | Modification  |     |
| 10.07orearlier                 |         |         | --            |     |
| Command Information            |         |         |               |     |
| Platforms                      | Command | context | Authority     |     |
Allplatforms configandconfig- Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
logging-filter
| logging facility |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
logging facility {local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7}
| no logging facility |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Description
Setstheloggingfacilitytobeusedforremotesyslogmessages.Default:local7
Remotesyslog|92

Thenoformofthiscommanddisablestheloggingfacilitytobeusedforremotesyslogmessages.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{local0 | local1 | local2 | Selectstheloggingfacilitytobeusedforremotesyslogmessages.
| local3 | | local4 | local5 | |   | Required.                                |
| -------- | --------------- | --- | ---------------------------------------- |
| local6 | | local7}         |     | Specifiestheseverityofthesyslogmessages: |
n local0
local1
n
n local2
n local3
n local4
n local5
n local6
n local7
Examples
Setsthelocal5loggingfacilitytobeusedforremotesyslogmessages:
| switch(config)#     | logging | facility | local5       |
| ------------------- | ------- | -------- | ------------ |
| Command History     |         |          |              |
| Release             |         |          | Modification |
| 10.07orearlier      |         |          | --           |
| Command Information |         |          |              |
| Platforms           | Command | context  | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logging persistent-storage |     |     |     |
| -------------------------- | --- | --- | --- |
logging persistent-storage [severity {alert|crit|debug|emerg|err|info|notice|warning}]
| no logging persistent-storage |     |     |     |
| ----------------------------- | --- | --- | --- |
Description
Enablesordisablesstorageoflogsinstorage.Onlylogsofthespecifiedseverityandabovewillbe
preservedinthestorage.
Thenoformofthiscommanddisablesstorageoflogsinstorage.
| Parameter        |     |     | Description                              |
| ---------------- | --- | --- | ---------------------------------------- |
| severity <LEVEL> |     |     | Specifiestheseverityofthesyslogmessages: |
n alert:Preservessyslogmessageswiththeseverityofalert(6)
andemergency(7)
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 93

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
n crit:Preservessyslogmessageswiththeseverityofcritical(5)
andabove.Default.
n debug:Preservessyslogmessageswiththeseverityofdebug
(0)andabove.
n emerg:Preservessyslogmessageswiththeseverityof
emergency(7)only.
n err:Preservessyslogmessageswiththeseverityoferr(4)and
above.
n info:Preservessyslogmessageswiththeseverityofinfo(1)
andabove.
n notice:Preservessyslogmessageswiththeseverityofnotice
(2)andabove.
n warning:Preservessyslogmessageswiththeseverityof
warning(3)andabove.
Usage
Theselogscanbecopiedoutbyusingthecopy support-files allorcopy support-files previous-boot.
Examples
Enablingstorageoflogsinstoragewithseverityinfo:
| switch(config)#logging |     | persistent-storage |     | severity info |
| ---------------------- | --- | ------------------ | --- | ------------- |
Logs will be written to storage and made available across reboot.
| Do you want | to continue | (y/n)? |     |     |
| ----------- | ----------- | ------ | --- | --- |
Disablingstorageoflogsinstorage:
| switch(config)#     | no      | logging persistent-storage |              |     |
| ------------------- | ------- | -------------------------- | ------------ | --- |
| Command History     |         |                            |              |     |
| Release             |         |                            | Modification |     |
| 10.07orearlier      |         |                            | --           |     |
| Command Information |         |                            |              |     |
| Platforms           | Command | context                    | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Remotesyslog|94

Chapter 13

Runtime Diagnostics

Runtime Diagnostics

Run Time diagnostics framework is intended to monitor and validate the health of different hardware
components present in the system. It uses a set of safe hardware diagnostics test cases to validate the
health of different hardware components. These diagnostics test cases are run periodically at every
predetermined interval. Additionally, these hardware diagnostics test cases can be run on demand.

Runtime diagnostic commands

diagnostic monitor
diagnostic monitor {fan-tray
no diagnostic monitor {fan-tray

| line-module | management-module} [<SLOT-ID>]

| line-module | management-module} [<SLOT-ID>]

For 8400 switches only:
diagnostic monitor {fabric <SLOT-ID> | rear-display-module}
no diagnostic monitor {fabric <SLOT-ID> | rear-display-module}

Description

Enables runtime diagnostics for all modules or for a specified module. This feature is enabled by default
for all modules.

The no form of this command disables runtime diagnostics for all modules or for a specified module.

Parameter

fan-tray

line-module

Description

Specifies the enabling of diagnostic monitoring specific to a fan
tray.

Specifies the enabling of diagnostic monitoring specific to a line
module.

management-module

Specifies the enabling of diagnostic monitoring specific to a
management module.

<SLOT-ID>

fabric

Specifies the slot ID of a module. Format: member/slot.

Specifies the enabling of diagnostic monitoring specific to a fabric
module on an 8400 switch.

rear-display-module

Specifies the enabling of diagnostic monitoring specific to the rear
display module on an 8400 switch.

Usage

When no parameters are used in the command (diagnostic monitor or no diagnostic monitor), the
command applies to all modules. This command impacts the diagnostics that run periodically. It does
not affect on-demand diagnostics.

Example

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

95

Enablingruntimediagnosticsforaspecifiedmodule:
| switch(config)#     | diagnostic |         | monitor management-module | 1/5 |
| ------------------- | ---------- | ------- | ------------------------- | --- |
| Command History     |            |         |                           |     |
| Release             |            |         | Modification              |     |
| 10.07orearlier      |            |         | --                        |     |
| Command Information |            |         |                           |     |
| Platforms           | Command    | context | Authority                 |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
diag on-demand
diag on-demand {fan-tray | line-module | management-module} [<SLOT-ID>]
For8400switchesonly:
| diag on-demand | {fabric | <SLOT-ID> | | rear-display-module} |     |
| -------------- | ------- | --------- | ---------------------- | --- |
Description
Runsthediagnostictestsforallmodulesorforaspecifiedmodule.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
[fan-tray | line-module | management-module] Selectstheoptionsforenablingordisablingrun-
timediagnosticsforaspecificmodule.
| fan-tray |     |     | Specifiestheenablingofdiagnosticmonitoring |     |
| -------- | --- | --- | ------------------------------------------ | --- |
specifictoafantray.
| line-module |     |     | Specifiestheenablingofdiagnosticmonitoring |     |
| ----------- | --- | --- | ------------------------------------------ | --- |
specifictoalinemodule.
| management-module |     |     | Specifiestheenablingofdiagnosticmonitoring |     |
| ----------------- | --- | --- | ------------------------------------------ | --- |
specifictoamanagementmodule.
fabric
Specifiestheenablingofdiagnosticmonitoring
specifictoafabricmoduleonan8400switch.
| <SLOT-ID> |     |     | Specifiesthemember/slotformanagement |     |
| --------- | --- | --- | ------------------------------------ | --- |
modules(1/5or1/6),linemodules(1/1-1/4,1/7-
1/10),fantrays(1/1-1/3),andfabricmodules(1/1-
1/3).
rear-display-module Specifiestheenablingofdiagnosticmonitoring
specifictothereardisplaymoduleonan8400
switch.
Usage
RuntimeDiagnostics|96

Whennoparametersareusedinthecommand(diag on-demand),thecommandappliestoall
modules.
Examples
Runningdiagnostictestsforallmodulesonan8400switch:
| switch#  | diag on-demand |     |                |     |         |     |
| -------- | -------------- | --- | -------------- | --- | ------- | --- |
| Fetching | Test results.  |     | Please wait    | ... |         |     |
| Module   |                |     | ID Diagnostics |     | Success |     |
Performed
| -------------------- |     |     | ----- ----------- |     | ------- |     |
| -------------------- | --- | --- | ----------------- | --- | ------- | --- |
| ManagementModule     |     |     | 1/5               | 13  | 100%    |     |
| LineModule           |     |     | 1/3               | 12  | 100%    |     |
| FanTray              |     |     | 1/3               | 14  | 100%    |     |
| FanTray              |     |     | 1/1               | 14  | 100%    |     |
| LineModule           |     |     | 1/1               | 12  | 100%    |     |
| RearDisplayModule    |     |     | 1/RDC             | 2   | 100%    |     |
| LineModule           |     |     | 1/2               | 12  | 100%    |     |
| Fabric               |     |     | 1/1               | 8   | 100%    |     |
| FanTray              |     |     | 1/2               | 14  | 100%    |     |
| Fabric               |     |     | 1/3               | 8   | 100%    |     |
| Fabric               |     |     | 1/2               | 8   | 100%    |     |
Runningdiagnostictestsforfabricsonan8400switch:
| switch# | diag on-demand |     | fabric         |     |         |     |
| ------- | -------------- | --- | -------------- | --- | ------- | --- |
| Module  |                |     | ID Diagnostics |     | Success |     |
Performed
| -------------------- |     |     | ----- ----------- |     | ------- |     |
| -------------------- | --- | --- | ----------------- | --- | ------- | --- |
| Fabric               |     |     | 1/1               | 8   | 100%    |     |
| Fabric               |     |     | 1/2               | 8   | 100%    |     |
| Fabric               |     |     | 1/3               | 8   | 100%    |     |
Runningdiagnostictestsforaspecificmoduleonan8400switch:
| switch#            | diag on-demand |       | management-module     |              | 1/5 |         |
| ------------------ | -------------- | ----- | --------------------- | ------------ | --- | ------- |
| Performing         | diagnostic     |       | tests. Please         | wait         | ... |         |
| Fetching           | Test results.  |       | Please wait           | ...          |     |         |
| Module             |                | ID    | Diagnostics           | Performed    |     | Success |
| ------------------ |                | ----- | --------------------- |              |     | ------- |
| ManagementModule   |                | 1/5   |                       |              |     | 13 100% |
| Command            | History        |       |                       |              |     |         |
| Release            |                |       |                       | Modification |     |         |
| 10.07orearlier     |                |       |                       | --           |     |         |
| Command            | Information    |       |                       |              |     |         |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 97

Platforms

Command context

Authority

8400

Manager (#)

Administrators or local user group members with execution
rights for this command.

show diagnostic
show diagnostic {fan-tray
detail} [vsx-peer]

| line-module | management-module} [<SLOT-ID>] {brief |

For 8400 switches only:
show diagnostic {fabric <SLOT-ID> | rear-display-module}{brief | detail}[vsx-peer]

Description

Displays the diagnostic test results for all modules or for a specified module.

Parameter

Description

[fan-tray | line-module | management-module]

line-module

management-module

fabric

<SLOT-ID>

rear-display-module

vsx-peer

Usage

Selects the options for enabling or disabling
runtime diagnostics for a specific module.

Specifies the enabling of diagnostic monitoring
specific to a line module.

Specifies the enabling of diagnostic monitoring
specific to a management module.

Specifies the enabling of diagnostic monitoring
specific to a fabric module on an 8400 switch.

Specifies the member/slot for management
modules (1/5 or 1/6), line modules (1/1-1/4, 1/7-
1/10), fan trays (1/1-1/3), and fabric modules(1/1-
1/3).

Specifies the enabling of diagnostic monitoring
specific to the rear display module on an 8400
switch.

Shows the output from the VSX peer switch. If the
switches do not have the VSX configuration or the
ISL is down, the output from the VSX peer switch
is not displayed. This parameter is available on
switches that support VSX.

When no parameters are used in the command (show diagnostic), the command applies to all modules.

Example

Showing diagnostic test results in brief format for all modules on an 8400 switch:

switch# show diagnostic brief

Module

ID

Diagnostics Success
Performed

-------------------- ----- ----------- -------

Runtime Diagnostics | 98

| ManagementModule  |     | 1/5   | 13  | 100%   |     |     |
| ----------------- | --- | ----- | --- | ------ | --- | --- |
| LineModule        |     | 1/1   | 12  | 100%   |     |     |
| LineModule        |     | 1/2   | 12  | 100%   |     |     |
| LineModule        |     | 1/4   | 12  | 100%   |     |     |
| Fabric            |     | 1/1   |     | 8 100% |     |     |
| Fabric            |     | 1/2   |     | 8 100% |     |     |
| Fabric            |     | 1/3   |     | 8 100% |     |     |
| FanTray           |     | 1/1   | 14  | 100%   |     |     |
| FanTray           |     | 1/2   | 14  | 100%   |     |     |
| FanTray           |     | 1/3   | 14  | 100%   |     |     |
| RearDisplayModule |     | 1/RDC |     | 2 100% |     |     |
Showingdiagnostictestresultsinbriefformatforfabricsonan8400switch:
| switch# show | diagnostic | fabric         | brief |         |     |     |
| ------------ | ---------- | -------------- | ----- | ------- | --- | --- |
| Module       |            | ID Diagnostics |       | Success |     |     |
Performed
| -------------------- |     | ----- ----------- |     | ------- |     |     |
| -------------------- | --- | ----------------- | --- | ------- | --- | --- |
| Fabric               |     | 1/1               |     | 8 100%  |     |     |
| Fabric               |     | 1/2               |     | 8 100%  |     |     |
| Fabric               |     | 1/3               |     | 8 100%  |     |     |
Showingdiagnostictestresultsinbriefformatforaspecifiedmoduleonan8400switch:
| switch# show | diagnostic | management-module |     | brief   |     |     |
| ------------ | ---------- | ----------------- | --- | ------- | --- | --- |
| Module       |            | ID Diagnostics    |     | Success |     |     |
Performed
| -------------------- |     | ----- ----------- |     | ------- |     |     |
| -------------------- | --- | ----------------- | --- | ------- | --- | --- |
| ManagementModule     |     | 1/5               | 13  | 100%    |     |     |
Showingdiagnostictestresultsindetailformatforallmodulesonan8400switch:
switch#
| show                      | diagnostic | detail |     |     |     |     |
| ------------------------- | ---------- | ------ | --- | --- | --- | --- |
| Module : ManagementModule |            | 1/5    |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --- |
|          |           |           |           | Failure Count | Count |     |
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
| 1 2019-09-16           | 03:57:43 | 2019-09-16          | 03:57:43 |          |     |     |
| eeprom                 | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
| 1 2019-09-16           | 03:57:43 | 2019-09-16          | 03:57:43 |          |     |     |
| fru_eeprom             | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
| 1 2019-09-16           | 03:57:43 | 2019-09-16          | 03:57:43 |          |     |     |
| ledpld                 | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
| 15 2019-09-16          | 05:14:33 | 2019-09-16          |          | 03:57:42 |     |     |
| lsb_altmcbl            | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
| 15 2019-09-16          | 05:14:33 | 2019-09-16          |          | 03:57:43 |     |     |
| lsb_altpmc             | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
| 15 2019-09-16          | 05:14:33 | 2019-09-16          |          | 03:57:43 |     |     |
| mm_mcbe                | Pass     | 0x0                 | 0x0      |          | 0   | 0   |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 99

| 15 2019-09-16       | 05:14:32 | 2019-09-16 | 03:57:42 |     |     |
| ------------------- | -------- | ---------- | -------- | --- | --- |
| mm_mcbl             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 15 2019-09-16       | 05:14:32 | 2019-09-16 | 03:57:42 |     |     |
| pmc                 | Pass     | 0x0        | 0x0      | 0   | 0   |
| 15 2019-09-16       | 05:14:33 | 2019-09-16 | 03:57:42 |     |     |
| tmp1                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 03:57:43 | 2019-09-16 | 03:57:43 |     |     |
| tmp2                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 03:57:43 | 2019-09-16 | 03:57:43 |     |     |
| tmp3                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 03:57:43 | 2019-09-16 | 03:57:43 |     |     |
| tmp4                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 03:57:43 | 2019-09-16 | 03:57:43 |     |     |
| Module : LineModule |          | 1/1        |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:32 |     |     |
| fru_eeprom             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:33 |     |     |
| jericho_tmp            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:32 |     |     |
| kbp_tmp                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:32 |     |     |
| lc_lcb                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 13 2019-09-16          | 05:13:32 | 2019-09-16          | 04:13:32 |     |     |
| lc_lcbiox              | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 13 2019-09-16          | 05:13:32 | 2019-09-16          | 04:13:32 |     |     |
| lsb_lc_lcb             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 13 2019-09-16          | 05:13:32 | 2019-09-16          | 04:13:33 |     |     |
| tmp1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:33 |     |     |
| tmp2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:33 |     |     |
| tmp3                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:33 |     |     |
| tmp4                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:09 | 2019-09-16          | 04:13:33 |     |     |
| tmp5                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:09 | 2019-09-16          | 04:13:33 |     |     |
| Module : LineModule    |          | 1/2                 |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:05:44 | 2019-09-16          | 04:05:44 |     |     |
| fru_eeprom             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:05:44 | 2019-09-16          | 04:05:44 |     |     |
| jericho_tmp            | Pass     | 0x0                 | 0x0      | 0   | 0   |
RuntimeDiagnostics|100

| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| ------------------- | -------- | ---------- | -------- | --- | --- |
| kbp_tmp             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| lc_lcb              | Pass     | 0x0        | 0x0      | 0   | 0   |
| 15 2019-09-16       | 05:17:34 | 2019-09-16 | 04:05:44 |     |     |
| lc_lcbiox           | Pass     | 0x0        | 0x0      | 0   | 0   |
| 15 2019-09-16       | 05:17:34 | 2019-09-16 | 04:05:44 |     |     |
| lsb_lc_lcb          | Pass     | 0x0        | 0x0      | 0   | 0   |
| 15 2019-09-16       | 05:17:34 | 2019-09-16 | 04:05:45 |     |     |
| tmp1                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| tmp2                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| tmp3                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| tmp4                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| tmp5                | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16        | 04:05:44 | 2019-09-16 | 04:05:44 |     |     |
| Module : LineModule |          | 1/4        |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| fru_eeprom             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| jericho_tmp            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| kbp_tmp                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| lc_lcb                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 13 2019-09-16          | 05:14:32 | 2019-09-16          | 04:13:27 |     |     |
| lc_lcbiox              | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 13 2019-09-16          | 05:14:32 | 2019-09-16          | 04:13:27 |     |     |
| lsb_lc_lcb             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 13 2019-09-16          | 05:14:32 | 2019-09-16          | 04:13:27 |     |     |
| tmp1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| tmp2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| tmp3                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| tmp4                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| tmp5                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 04:13:27 | 2019-09-16          | 04:13:27 |     |     |
| Module : Fabric        | 1/1      |                     |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 101

| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| eeprom_1               | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| fc_fcb                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:36 |     |     |
| lsb_fc_fcb             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:37 |     |     |
| tmp1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:36 | 2019-09-16          | 03:58:36 |     |     |
| tmp2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:36 | 2019-09-16          | 03:58:36 |     |     |
| tmp3                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| tmp4                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| Module : Fabric        | 1/2      |                     |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:42 | 2019-09-16          | 03:58:42 |     |     |
| eeprom_1               | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:42 | 2019-09-16          | 03:58:42 |     |     |
| fc_fcb                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:42 |     |     |
| lsb_fc_fcb             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:42 |     |     |
| tmp1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:42 | 2019-09-16          | 03:58:42 |     |     |
| tmp2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:42 | 2019-09-16          | 03:58:42 |     |     |
| tmp3                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:42 | 2019-09-16          | 03:58:42 |     |     |
| tmp4                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:42 | 2019-09-16          | 03:58:42 |     |     |
| Module : Fabric        | 1/3      |                     |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:41 | 2019-09-16          | 03:58:41 |     |     |
| eeprom_1               | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:41 | 2019-09-16          | 03:58:41 |     |     |
| fc_fcb                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:41 |     |     |
| lsb_fc_fcb             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:41 |     |     |
| tmp1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
RuntimeDiagnostics|102

| 1 2019-09-16     | 03:58:41 | 2019-09-16 | 03:58:41 |     |     |
| ---------------- | -------- | ---------- | -------- | --- | --- |
| tmp2             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:58:41 | 2019-09-16 | 03:58:41 |     |     |
| tmp3             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:58:41 | 2019-09-16 | 03:58:41 |     |     |
| tmp4             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:58:41 | 2019-09-16 | 03:58:41 |     |     |
| Module : FanTray | 1/1      |            |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| fan1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| fan1_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| fan2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| fan2_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| fan3                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan3_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan4                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan4_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan5                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan5_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan6                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| fan6_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:40 | 2019-09-16          | 03:57:40 |     |     |
| ft_eeprom              | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| icb_ft                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:14:32 | 2019-09-16          | 03:57:39 |     |     |
| Module : FanTray       | 1/2      |                     |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| fan1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:41 | 2019-09-16          | 03:57:41 |     |     |
| fan1_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:41 | 2019-09-16          | 03:57:41 |     |     |
| fan2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:41 | 2019-09-16          | 03:57:41 |     |     |
| fan2_eeprom            | Pass     | 0x0                 | 0x0      | 0   | 0   |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 103

| 1 2019-09-16     | 03:57:41 | 2019-09-16 | 03:57:41 |     |     |
| ---------------- | -------- | ---------- | -------- | --- | --- |
| fan3             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:41 | 2019-09-16 | 03:57:41 |     |     |
| fan3_eeprom      | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| fan4             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| fan4_eeprom      | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| fan5             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| fan5_eeprom      | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| fan6             | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| fan6_eeprom      | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:42 | 2019-09-16 | 03:57:42 |     |     |
| ft_eeprom        | Pass     | 0x0        | 0x0      | 0   | 0   |
| 1 2019-09-16     | 03:57:41 | 2019-09-16 | 03:57:41 |     |     |
| icb_ft           | Pass     | 0x0        | 0x0      | 0   | 0   |
| 15 2019-09-16    | 05:14:32 | 2019-09-16 | 03:57:41 |     |     |
| Module : FanTray | 1/3      |            |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |
| -------- | --------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - --------------------     |          | ------------------- |          |     |     |
| -------------------------- | -------- | ------------------- | -------- | --- | --- |
| fan1                       | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| fan1_eeprom                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| fan2                       | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| fan2_eeprom                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| fan3                       | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| fan3_eeprom                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| fan4                       | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:38 | 2019-09-16          | 03:57:38 |     |     |
| fan4_eeprom                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:38 | 2019-09-16          | 03:57:38 |     |     |
| fan5                       | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:38 | 2019-09-16          | 03:57:38 |     |     |
| fan5_eeprom                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:38 | 2019-09-16          | 03:57:38 |     |     |
| fan6                       | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| fan6_eeprom                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:39 | 2019-09-16          | 03:57:39 |     |     |
| ft_eeprom                  | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16               | 03:57:37 | 2019-09-16          | 03:57:37 |     |     |
| icb_ft                     | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16              | 05:14:32 | 2019-09-16          | 03:57:36 |     |     |
| Module : RearDisplayModule |          | 1/RDC               |          |     |     |
RuntimeDiagnostics|104

Diagnostic Status Error Code History Code Successive Total Failure Total
| Last | Run Timestamp | First Run | Timestamp |     |     |
| ---- | ------------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| icb_rdc                | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:14:32 | 2019-09-16          | 03:57:47 |     |     |
| rdc_eeprom             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:57:47 | 2019-09-16          | 03:57:47 |     |     |
Showingdiagnostictestresultsindetailformatforfabricsonan8400switch:
| switch# | show diagnostic | fabric | 1/1 detail |     |     |
| ------- | --------------- | ------ | ---------- | --- | --- |
| Module  | : Fabric 1/1    |        |            |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last | Run Timestamp | First Run | Timestamp |     |     |
| ---- | ------------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| eeprom_1               | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| fc_fcb                 | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:36 |     |     |
| lsb_fc_fcb             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 15 2019-09-16          | 05:15:33 | 2019-09-16          | 03:58:37 |     |     |
| tmp1                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:36 | 2019-09-16          | 03:58:36 |     |     |
| tmp2                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:36 | 2019-09-16          | 03:58:36 |     |     |
| tmp3                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
| tmp4                   | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 1 2019-09-16           | 03:58:37 | 2019-09-16          | 03:58:37 |     |     |
Showingdiagnostictestresultsindetailformatforaspecifiedmoduleonan8400switch:
switch#
|        | show diagnostic | line-module | 1/1 detail |     |     |
| ------ | --------------- | ----------- | ---------- | --- | --- |
| Module | : LineModule    | 1/1         |            |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last | Run Timestamp | First Run | Timestamp |     |     |
| ---- | ------------- | --------- | --------- | --- | --- |
Failure Count Count
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- |
| curr_sensor            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:32 |     |     |
| fru_eeprom             | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:33 |     |     |
| jericho_tmp            | Pass     | 0x0                 | 0x0      | 0   | 0   |
| 2 2019-09-16           | 04:23:08 | 2019-09-16          | 04:13:32 |     |     |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 105

| kbp_tmp             | Pass     | 0x0        | 0x0          | 0   | 0   |
| ------------------- | -------- | ---------- | ------------ | --- | --- |
| 2 2019-09-16        | 04:23:08 | 2019-09-16 | 04:13:32     |     |     |
| lc_lcb              | Pass     | 0x0        | 0x0          | 0   | 0   |
| 14 2019-09-16       | 05:18:34 | 2019-09-16 | 04:13:32     |     |     |
| lc_lcbiox           | Pass     | 0x0        | 0x0          | 0   | 0   |
| 14 2019-09-16       | 05:18:34 | 2019-09-16 | 04:13:32     |     |     |
| lsb_lc_lcb          | Pass     | 0x0        | 0x0          | 0   | 0   |
| 14 2019-09-16       | 05:18:34 | 2019-09-16 | 04:13:33     |     |     |
| tmp1                | Pass     | 0x0        | 0x0          | 0   | 0   |
| 2 2019-09-16        | 04:23:08 | 2019-09-16 | 04:13:33     |     |     |
| tmp2                | Pass     | 0x0        | 0x0          | 0   | 0   |
| 2 2019-09-16        | 04:23:08 | 2019-09-16 | 04:13:33     |     |     |
| tmp3                | Pass     | 0x0        | 0x0          | 0   | 0   |
| 2 2019-09-16        | 04:23:08 | 2019-09-16 | 04:13:33     |     |     |
| tmp4                | Pass     | 0x0        | 0x0          | 0   | 0   |
| 2 2019-09-16        | 04:23:09 | 2019-09-16 | 04:13:33     |     |     |
| tmp5                | Pass     | 0x0        | 0x0          | 0   | 0   |
| 2 2019-09-16        | 04:23:09 | 2019-09-16 | 04:13:33     |     |     |
| Command History     |          |            |              |     |     |
| Release             |          |            | Modification |     |     |
| 10.07orearlier      |          |            | --           |     |     |
| Command Information |          |            |              |     |     |
| Platforms           | Command  | context    | Authority    |     |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show diagnostic |        | events |     |     |     |
| --------------- | ------ | ------ | --- | --- | --- |
| show diagnostic | events |        |     |     |     |
Description
Displaysthediagnosticrelatedeventlogs.
Example
Showingdiagnosticrelatedeventlogs:
switch#
| show | diagnostic | events |     |     |     |
| ---- | ---------- | ------ | --- | --- | --- |
2019-08-07:17:19:21.214532|hhmd|106001|ERR|
Diagnostic mm_mcbe failed with error code 0x380 on management module 1/5
2019-08-07:17:19:21.214554|hhmd|106001|ERR|
Diagnostic pmc failed with error code 0x4 on management module 1/5
2019-08-07:17:19:21.215532|hhmd|106001|ERR|
Diagnostic ledpld failed with error code 0x4 on management module 1/5
2019-08-07:17:19:21.353221|hhmd|106001|ERR|
Diagnostic mm_mcbe failed with error code 0x380 on management module 1/5
2019-08-07:17:19:21.354421|hhmd|106001|ERR|
Diagnostic pmc failed with error code 0x4 on management module 1/5
2019-08-07:17:19:21.453221|hhmd|106001|ERR|
Diagnostic ledpld failed with error code 0x4 on management module 1/5
RuntimeDiagnostics|106

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 107

Chapter 14

Service OS

Service OS

Service OS is an operating system that the customer only uses to fix filesystem corruption, download
and update firmware, and other support related issues. HPE Service OS is a Linux distribution that acts
as a standalone bootloader and recovery OS for AOS-CX-based switches. It is only accessible if the user
is consoled into the switch. The main high level features provided include:

n Access to file system partitions for retrieval of logs, coredumps, and configuration for supportability

purposes.

n Filesystem utilities to format and partition a corrupted storage disk.

n Management interface networking with TFTP to download and update a product image.

n Ability to boot primary and secondary firmware images (.SWI file) on the storage disk.

n Support for clearing the AOS-CX startup-config.

n Support for securely erasing the storage devices on the management module (zeroization). It clears
chassis information associated with the management module that is stored on part of the rear
display module.

n Ability to not only clear the admin password for AOS-CX, but also change it in SVOS.

n Ability to set the secure mode to enhanced or standard.

This document covers the customer CLI commands available in Service OS, as well as a few non-CLI
features.

Service OS CLI login

Description

If the user enters 0 at the boot menu prompt, they will be presented with a Service OS CLI login prompt.
The user must enter the login account "admin" to log in. By default, Service OS does not require a
password.

To reboot without logging in, enter reboot as the login user name.

There are two additional login accounts that execute a command without requiring a password: reboot
and zeroize. Enter the login account reboot to reboot the management module and zeroize to initiate a
zeroization process. The zeroize user account helps a user reset the admin user account's password.

Example

ServiceOS GT.01.01.0001 switch ttyS0

To reboot without logging in, enter 'reboot' as the login user name.

switch login: admin

Hewlett Packard
Enterprise

SVOS>

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

108

```

```
ServiceOS GT.01.01.0001 switch ttyS0

To reboot without logging in, enter 'reboot' as the login user name.

switch login: reboot

Hewlett Packard
Enterprise

reboot: Restarting system
```

```
ServiceOS login: zeroize
This will securely erase all customer data, including passwords, and
reset the switch to factory defaults.
This action requires proof of physical access via a USB drive.

* Create a FAT32 formatted USB drive
* Create a file in the root directory of the USB drive named zeroize.txt
* Type the following serial number into the zeroize.txt file: 772632X1830018
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

Service OS user accounts

Service OS provides a single admin login account. By default, no password is required to log in. Service
OS will require a password if the Service OS admin user account password feature is enabled. This
setting can be enabled or disabled in AOS-CX.

Service OS boot menu

Description

On boot, the user is presented with a Service OS version banner with version, build date, build time,
build ID, and SHA strings.

The user is then shown the boot image profiles.

n Enter 0 to boot the Service OS login CLI.

n Enter 1 to boot the primary firmware image.

n Enter 2 to boot the secondary firmware image.

n If no input is given within 5 seconds, the default boot profile is selected. Alternatively, press Enter to

select the default boot profile.

Service OS | 109

Theimageselectedbytheuserduringbootisarun-timedecisiononlyandwillnotpersistacross
reboots.Thedefaultimagecanbeconfiguredusingtheboot set-defaultcommand.
Example
| ServiceOS | Information: |                                                   |              |
| --------- | ------------ | ------------------------------------------------- | ------------ |
| Version:  |              | GT.01.01.0001                                     |              |
| Build     | Date:        | 2017-07-19                                        | 14:52:31 PDT |
| Build     | ID:          | ServiceOS:GT.01.01.0001:461519208911:201707191452 |              |
| SHA:      |              | 46151920891195cdb2267ea6889a3c6cbc3d4193          |              |
Boot Profiles:
| 0. Service   | OS Console |       |                 |
| ------------ | ---------- | ----- | --------------- |
| 1. Primary   | Software   | Image | [XL.10.xx.xxxx] |
| 2. Secondary | Software   | Image | [XL.10.xx.xxxx] |
Select profile(primary):
The(primary)stringinthebootmenudisplaysthedefaultbootprofilethatwillbebootedafterthetimeout
period.Thisstringwillchangeto(secondary)or(ServiceOS)dependingonthecurrentdefaultbootoption.
| Console | configuration |     |     |
| ------- | ------------- | --- | --- |
Duringboot,ServiceOScommunicateswiththeRJ45serialconsolewithabaudrateof115200.Thereis
nooptiontochangethebaudrateduringboot.
Additionally,ifaUSBconsoleisconnectedtothemanagementmoduleconsoleport,inputwill
automaticallybeswitchedovertousetheUSBconsole.AutomaticswitchingtoUSBisconsistentwith
theAOS-CXUSBconsolebehavior.
ConsoleoutputalwaysdisplaysonboththeRJ45consoleportandtheUSBconsoleport.
| AOS-CX | boot |     |     |
| ------ | ---- | --- | --- |
Description
Aftertheuserhasinputabootprofileselectionatthebootmenuorthe5-secondselectiontimeouthas
expired,ServiceOSwillbootanAOS-CXimage.
ServiceOSdisplaysthefollowingbootstringsembeddedintheproductimageheader:
n Imagename
n Imageversion
n BuildID
n Builddate
ServiceOSwillthenpresentstatusandboottheimage.
Example
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 110

| Booting   | primary  | software | image... |     |     |     |     |
| --------- | -------- | -------- | -------- | --- | --- | --- | --- |
| Verifying | Image... |          |          |     |     |     |     |
Image Info:
Name: AOS-CX
| Version:   |          | XL.01.01.0001                                  |          |     |     |     |     |
| ---------- | -------- | ---------------------------------------------- | -------- | --- | --- | --- | --- |
| Build      | Id:      | AOS-CX:XL.01.01.0001:1a36111da4e0:201707171452 |          |     |     |     |     |
| Build      | Date:    | 2017-07-17                                     | 14:52:27 | PDT |     |     |     |
| Extracting | Image... |                                                |          |     |     |     |     |
| Loading    | Image... |                                                |          |     |     |     |     |
Done.
| kexec:      | Starting | new kernel |     |     |     |     |     |
| ----------- | -------- | ---------- | --- | --- | --- | --- | --- |
| File system |          | access     |     |     |     |     |     |
Description
WhentheuserlogsintotheServiceOSCLI,theyarepresentedwithalimitedfilesystem.Theusercan
usestandardfilesystemcommandsofcd,ls,andpwdtoviewandmovethroughthefilesystem.
Onlogin,theuserisfirstplacedinthe/homedirectory:
| (C) Copyright |     | 2017 Hewlett | Packard    | Enterprise | Development |     | LP  |
| ------------- | --- | ------------ | ---------- | ---------- | ----------- | --- | --- |
|               |     |              | RESTRICTED | RIGHTS     | LEGEND      |     |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. Government |     | under | vendor's | standard | commercial | license. |     |
| --------------- | --- | ----- | -------- | -------- | ---------- | -------- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
| ServiceOS | login: | admin |     |     |     |     |     |
| --------- | ------ | ----- | --- | --- | --- | --- | --- |
SVOS> pwd
/home
SVOS>
ThehomedirectoryandtheUSBdevice(/mnt/usbandanysubdirectory)aretheonlywritable
directoriesavailable.Thesedirectoriescanbeusedasastaginglocationfordownloadingproduct
imagesusingTFTP./homecanalsobeusedastemporarystoragebeforecopyingfilesfromthe
managementmodulethroughTFTPorUSB.Anychangesmadeto/homewillnotpersistacrossreboots
orafterbootinganAOS-CXimage.
Theroot/directorydisplaysviewabledirectories:
| SVOS> ls | /        |      |     |     |          |     |     |
| -------- | -------- | ---- | --- | --- | -------- | --- | --- |
| bin      | coredump | lib  |     | mnt | selftest |     |     |
| cli      | home     | logs |     | nos |          |     |     |
SVOS>
Thedirectoriescoredump,selftest,nos,andlogseachprovidetheuseraccesstoanSSD partition
mount.Theusermayread,butnotwriteanyfileonthesepartitions.
ServiceOS|111

ThesemountpointsallowtheusertocopyfilesontheSSD toaUSBstoragedeviceoruploadfiles
usingTFTP.CopyingfilesfromtheSSD isintendedtobeusedundertheguidanceofasupport
engineer(touploadlogsorcoredumpstoHPEsupport).
USBstoragedeviceaccessisprovidedthroughthemountat/mnt/usb.
Theremainingdirectoriesintherootfilesystembin,cli,andlibarenotintendedtobeusedbythe
customer.
| Service |     | OS  | mount | failure |     |     |     |     |     |     |
| ------- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- |
Description
IftheSSD isdetectedasmissingoranyofthepartitionscouldnotbemounted,ServiceOSwillforcethe
usertoboottotheServiceOSconsoleanddisplayanerrormessageindicatingthatrecoveryshouldbe
attemptedusingtheformatcommand.
Example
|     | (C) Copyright |     | 2017 Hewlett | Packard    |     | Enterprise |        | Development |     | LP  |
| --- | ------------- | --- | ------------ | ---------- | --- | ---------- | ------ | ----------- | --- | --- |
|     |               |     |              | RESTRICTED |     | RIGHTS     | LEGEND |             |     |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
|     | U.S. | Government | under | vendor's | standard |     | commercial |     | license. |     |
| --- | ---- | ---------- | ----- | -------- | -------- | --- | ---------- | --- | -------- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
|         | Error,    | Could   | not mount  | the        | primary | storage      |             | device.  |     |     |
| ------- | --------- | ------- | ---------- | ---------- | ------- | ------------ | ----------- | -------- | --- | --- |
|         | This      | may     | be due to  | filesystem | or      | device       | corruption. |          |     |     |
|         | Please    | attempt | to recover | using      |         | the "format" |             | command. |     |     |
|         | ServiceOS |         | login:     |            |         |              |             |          |     |     |
| Missing |           | Rear    | Display    |            | Module  |              | Failure     |          |     |     |
Description
Thereardisplaymodulestoresthechassisidentityandisrequiredtobootaproductimage.IfService
OSdetectsthatthereardisplaymoduleisnotinsertedatboottime,amessagewillbeprintedand
ServiceOSwillforceboottotheServiceOSconsole.
Example
|     | ServiceOS |     | GT.01.01.0001 | switch | ttyS0 |     |     |     |     |     |
| --- | --------- | --- | ------------- | ------ | ----- | --- | --- | --- | --- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
Warning: no rear display module detected. A rear display module must be
inserted to boot a product image. Check that a module is inserted and
|     | fully  | seated, | then | reboot | the management |     |     | module. |     |     |
| --- | ------ | ------- | ---- | ------ | -------------- | --- | --- | ------- | --- | --- |
|     | switch | login:  |      |        |                |     |     |         |     |     |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 112

Service OS CLI command list

Description

After login to Service OS CLI, the user may enter the commands help or ? to get a full list of commands
and a terse description for each command. The user may also enter <command> followed by --help to
get more detailed help and usage for a specific command.

Example

SVOS> ?
Available Commands:

? - Display help screen

cd - Change the working directory

pwd - Print the current working directory

help - Display help screen
boot - Boot a product image

config-clear - Clears the startup-config

erase - Securely erase storage devices on the management module

format - Formats and partitions the primary storage device

identify - Prints hardware identification information

ip - Sets the OOBM Port Network Configuration

mount - Mount a storage device

ping - Send ICMP ECHO_REQUEST to network hosts (IPv4)

reboot - Reboots the Management Module
password - Set the admin account password

secure-mode - Sets or retrieves the secure mode setting

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

tftp - Allows transfer of files to/from a remote machine
exit - Logout

Enter '<command> --help' for more info

Service OS CLI features and limitations

The Service OS CLI provides basic shell functionality that allows you to execute commands and pass
arguments to those commands only. The following features are not available:

n Input/output redirection (<, >, >>)

n Job control (&, fg, bg)

n Process piping (|)

n File globbing (\*)

Service OS | 113

EventhoughtheServiceOSCLIdoesnotprovidefileglobbingcapabilities,somecommandsmayprovidethis
functionalityinternally.Anexampleisthelscommand.
Thefollowingcommonfeaturesareavailable:
n Commandhistory(UpArrow)andsearch(Ctrl-R)
n Tabcompletionforfileandfoldernames(notCLIcommands)
n CommandabortusingCtrl-C
| Service |     | OS CLI | commands |     |     |
| ------- | --- | ------ | -------- | --- | --- |
boot
boot
Description
Presentsyouwiththebootmenuprompt.Youcanthenspecifywhichbootprofile:primary,secondary,
orServiceOSconsole.
Example
Presentingthebootmenuprompt:
| SVOS>          | boot              |              |                                                   |                 |              |
| -------------- | ----------------- | ------------ | ------------------------------------------------- | --------------- | ------------ |
| ServiceOS      |                   | Information: |                                                   |                 |              |
|                | Version:          |              | GT.01.01.0005                                     |                 |              |
|                | Build             | Date:        | 2017-07-19                                        |                 | 14:52:31 PDT |
|                | Build             | ID:          | ServiceOS:GT.01.01.0001:461519208911:201707191452 |                 |              |
|                | SHA:              |              | 46151920891195cdb2267ea6889a3c6cbc3d4193          |                 |              |
| Boot           | Profiles:         |              |                                                   |                 |              |
| 0.             | Service           | OS Console   |                                                   |                 |              |
| 1.             | Primary           | Software     | Image                                             | [XL.01.01.0001] |              |
| 2.             | Secondary         | Software     | Image                                             | [XL.01.01.0001] |              |
| Select         | profile(primary): |              |                                                   |                 |              |
| Command        |                   | History      |                                                   |                 |              |
| Release        |                   |              |                                                   |                 | Modification |
| 10.07orearlier |                   |              |                                                   |                 | --           |
| Command        |                   | Information  |                                                   |                 |              |
| Platforms      |                   | Command      | context                                           |                 | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
cat
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 114

cat <FILENAME/DIRECTORY-NAME>
Description
Printsthecontentsofafiletotheconsole.TheServiceOSdoesnotallowcommandoutputredirection,
sothiscommandisonlyusefulforreadingshorttextfiles.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<FILENAME/DIRECTORY-NAME>
Showsthecontentsofthespecifiedfileordirectory.
Example
Showingthecontentsof/nos/hosts:
| SVOS> cat | /nos/hosts            |     |     |           |
| --------- | --------------------- | --- | --- | --------- |
| 127.0.0.1 | localhost.localdomain |     |     | localhost |
SVOS>
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
cd path
cd path
Description
Changesthecurrentworkingdirectory.
Example
Changingthecurrentworkingdirectory:
cd /
| Command History     |     |     |              |     |
| ------------------- | --- | --- | ------------ | --- |
| Release             |     |     | Modification |     |
| 10.07orearlier      |     |     | --           |     |
| Command Information |     |     |              |     |
ServiceOS|115

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
config-clear
config-clear
Description
Configurestheswitchtosetallconfigurationsettingstofactorydefaultwhentheswitchisrestarted.The
nexttimetheswitchstarts,thecurrentstartup-configisrenamedtostartup-config-fixme,andanew
startup-configiscreatedwithfactorydefaultsettings.
Usingthiscommandisnotthesameasperformingzeroization,whichsecurelyerasestheentireprimarystorage
andotherdevices,andnotjusttheconfiguration.
Example
Configuringthesystemtocleartheswitchconfiguration:
| SVOS> config-clear |               |         |          |
| ------------------ | ------------- | ------- | -------- |
| The switch         | configuration | will be | cleared. |
| Continue           | (y/n)? y      |         |          |
The system has been configured to clear the startup-config on the next
boot. Please execute the 'boot' command to complete this action.
SVOS>
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
cp
cp [options] <SOURCE-FILENAME/SOURCE-DIRECTORY> <DESTINATION-FLENAME/DESTINATION-
DIRECTORY>
Description
Copiesfilesordirectories.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 116

Parameter Description
[options] Selectstheoptionsforthecommand.
-d,-P Specifiesthepreservationofsymlinks(defaultif-
R).
-a Sameas-dpR.
R,-r
Specifiesrecursiveness,allfiles,andsubdirectories
arecopied.
-L Specifiesthefollowingofallsymlinks.
-H
Specifiesthefollowingofsymlinksoncommand
line.
-p Specifiesthepreservationoffileattributesif
possible.
-f Specifiestheoverwritingofafileordirectory.
-i Specifiesthepromptingbeforeanoverwrite.
-l,-s Specifiesthecreationof(sym)links.
<SOURCE-FILENAME/SOURCE-DIRECTORY> Specifiesthenameofthesourcefileordirectory.
<DESTINATION-FLENAME/DESTINATION-DIRECTORY> Specifiesthenameofthedestinationfileor
directory.
Example
Copying/home/customersdirectorytothe/home/clientsdirectory:
| SVOS> cp            | /home/customers | /home/clients |              |
| ------------------- | --------------- | ------------- | ------------ |
| Command History     |                 |               |              |
| Release             |                 |               | Modification |
| 10.07orearlier      |                 |               | --           |
| Command Information |                 |               |              |
| Platforms           | Command         | context       | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
du
| du [options] | <FILENAME/DIRECTORY-NAME>... |     |     |
| ------------ | ---------------------------- | --- | --- |
Description
Showsestimateddiskspaceusedforeachfileordirectoryorboth.
ServiceOS|117

| Parameter |     |     | Description                     |
| --------- | --- | --- | ------------------------------- |
| [options] |     |     | Selectstheoptionsforthecommand. |
| -a        |     |     | Showfilesizes.                  |
| -L        |     |     | Showsallsymlinks.               |
| -H        |     |     | Showssymlinksonacommandline.    |
-d, N Showslimitedoutputtodirectories(andfileswith-a)ofdepthless
thanN.
-c
Showsthetotaldiskspaceusageofallfilesordirectoriesorboth.
| -l  |     |     | Showsthecountsizesifhardlinked. |
| --- | --- | --- | ------------------------------- |
-s
Showsonlyatotalforeachargument.
| -x  |     |     | Doesnotshowdirectoriesondifferentfilesystems. |
| --- | --- | --- | --------------------------------------------- |
-h
Showsizesinhumanreadableformat(1K,243M,and2G).
| -m  |     |     | Showsizesinmegabytes. |
| --- | --- | --- | --------------------- |
-k
Showsizesinkilobytes(default).
<FILENAME/DIRECTORY-NAME> Specifiesthefileordirectoryorbothfordisplayingasizeestimate.
Example
Estimatingdiskspaceforthe/nosdirectory:
| SVOS> du                | -ah /nos |     |     |
| ----------------------- | -------- | --- | --- |
| 196.4M /nos/primary.swi |          |     |     |
| 196.4M /nos             |          |     |     |
SVOS>
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
erase zeroize
erase zeroize
Description
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 118

Securely erases any user data contained on the SSD or other storage devices on the management
module.

Back up all data before running this command or all user/config data will be lost.

Usage

Use this command to securely erase all customer data and restore the software environment to factory
default. When you issue this command:

nSoftware images are copied to RAM to be restored on completion.

nAll bits undergo a 0>1>0 transition to completely zeroize data. This data is not recoverable.

nThis feature can be used to remove all configuration settings or system alterations for debugging or
troubleshooting.

nThe zeroization process takes approximately two minutes.

All logs and data are lost in the zeroization process. Best practices is to collect all applicable data before
performing zeroization.

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
This should take several minutes to one hour to complete.
############################WARNING############################

Continue (y/n)? y
reboot: Restarting system

ServiceOS Information:

Version:
Build Date:
Build ID:
SHA:

GT.01.01.0001
2017-07-19 14:52:31 PDT
ServiceOS:GT.01.01.0001:461519208911:201707191452
46151920891195cdb2267ea6889a3c6cbc3d4193

################ Preparing for zeroization #################

################ Storage zeroization #######################
################ WARNING: DO NOT POWER OFF UNTIL
##########
ZEROIZATION IS COMPLETE ##########
################
################ This should take several minutes ##########
##########
################ to one hour to complete

Service OS | 119

| ################    |         | Restoring | files | ########################### |     |     |
| ------------------- | ------- | --------- | ----- | --------------------------- | --- | --- |
| Command History     |         |           |       |                             |     |     |
| Release             |         |           |       | Modification                |     |     |
| 10.07orearlier      |         |           |       | --                          |     |     |
| Command Information |         |           |       |                             |     |     |
| Platforms           | Command | context   |       | Authority                   |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
exit
exit
Description
LogstheuseroutfromtheSVOS>prompt.
Example
LogingtheuseroutfromtheSVOS>prompt:
| SVOS> exit    |     |              |         |               |             |     |
| ------------- | --- | ------------ | ------- | ------------- | ----------- | --- |
| (C) Copyright |     | 2025 Hewlett | Packard | Enterprise    | Development | LP  |
|               |     | RESTRICTED   |         | RIGHTS LEGEND |             |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. Government |     | under vendor's |     | standard commercial | license. |     |
| --------------- | --- | -------------- | --- | ------------------- | -------- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
| ServiceOS           | login:  |         |     |              |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- |
| Command History     |         |         |     |              |     |     |
| Release             |         |         |     | Modification |     |     |
| 10.07orearlier      |         |         |     | --           |     |     |
| Command Information |         |         |     |              |     |     |
| Platforms           | Command | context |     | Authority    |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 120

format
format
Description
Configurestheprimarystoragedevicewiththecorrectpartitionandfilesystemformatting.This
commandremovesallpre-existingdataontheprimarystoragedevice.
Example
Configuringtheprimarystoragedevicewiththecorrectpartitionandfilesystemformatting:
| SVOS> format |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
##################WARNING####################
| The following |     | action     | will    | cause           | all   | data on |
| ------------- | --- | ---------- | ------- | --------------- | ----- | ------- |
| the primary   |     | storage    | device  | to be           | lost. | After   |
| formatting    | has | completed, |         | a reboot        | will  | be      |
| initiated     | to  | complete   | storage | initialization. |       |         |
##################WARNING####################
| Continue?      | (y/n):      | y       |         |                  |              |     |
| -------------- | ----------- | ------- | ------- | ---------------- | ------------ | --- |
| Working...This |             | may     | take    | a few minutes... |              |     |
| Command        | History     |         |         |                  |              |     |
| Release        |             |         |         |                  | Modification |     |
| 10.07orearlier |             |         |         |                  | --           |     |
| Command        | Information |         |         |                  |              |     |
| Platforms      |             | Command | context |                  | Authority    |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
identify
identify
Description
Printstheversionandserialnumberinformationofhardwaredevicesonthemanagementmodule(for
example,FPGAS,PLDs).
Printingversionandserialnumberinformationofhardwaredevicesonthemanagementmodule:
Outputfroman8400switch:
| SVOS> identify    |     |     |     |                 |     |     |
| ----------------- | --- | --- | --- | --------------- | --- | --- |
| mc svos_primary   |     |     |     | : GT.01.01.0007 |     |     |
| mc svos_secondary |     |     |     | : GT.01.01.0007 |     |     |
| mc uefi           |     |     |     | : GT-01-0021    |     |     |
| mc pciesw         |     |     |     | : 0x5           |     |     |
| mc oobm_single    |     |     |     | : 3.25_800005CD |     |     |
| mc xgig_single    |     |     |     | : 1.13_800006A8 |     |     |
ServiceOS|121

| mc mcbl_single    |             | : 0xE       |              |
| ----------------- | ----------- | ----------- | ------------ |
| mc mcbl_primary   |             | : 0xE       |              |
| mc mcbl_secondary |             | : 0xE       |              |
| mc mcbl_factory   |             | : 0x1       |              |
| mc mcbe_single    |             | : 0xE       |              |
| mc mcbe_primary   |             | : 0xE       |              |
| mc mcbe_secondary |             | : 0xE       |              |
| mc mcbe_factory   |             | : 0x1       |              |
| mc pmc_single     |             | : 0xA       |              |
| mc pmc_primary    |             | : 0xA       |              |
| mc pmc_secondary  |             | : 0xA       |              |
| mc ledpld         |             | : 0x5       |              |
| mc vmon/1         |             | : 8         |              |
| mc vreg_cpu       |             | : 5A        |              |
| mc tpm            |             | : 0x102420F |              |
| mc ssd            |             | : HPS4      |              |
| chassis           | tpm         | : 0x102420E |              |
| Support           | Info        | : SE:1      |              |
| Command           | History     |             |              |
| Release           |             |             | Modification |
| 10.07orearlier    |             |             | --           |
| Command           | Information |             |              |
| Platforms         | Command     | context     | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip
| ip {show | | dhcp | disable | | addr <ADDR-NETMASK-GATEWAY>} |     |
| -------- | ---------------- | ------------------------------ | --- |
Description
ShowsorconfigurestheportwithastaticIPaddress(IPv4only)orenablestheDHCPclientontheport.
AnaddressissetonlyifaDHCPserverisavailabletoprovideone.
Parameter Description
| {show | | dhcp | disable | | addr <ADDR-NETMASK-GATEWAY>} |     |
| ----- | ---------------- | ------------------------------ | --- |
SelectstheoptionsfortheOOBM
port.
show ShowstheOOBMport.
dhcp ConfigurestheportwithaDHCP
address.
disable DisablestheOOBMport.
| addr | <ADDR-NETMASK-GATEWAY> |     | ConfigurestheportwithastaticIP |
| ---- | ---------------------- | --- | ------------------------------ |
address(IPv4only).Specifyaddress,
netmask,andgatewayasA.B.C.D.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 122

Example
ConfiguringtheportwithaDHCPIPaddress:
SVOS>
ip dhcp
| SVOS> ip     | show          |     |     |
| ------------ | ------------- | --- | --- |
| Interface    | : Link Up     |     |     |
| IP Address   | : 10.0.26.17  |     |     |
| Subnet Mask: | 255.255.252.0 |     |     |
| Gateway      | : 10.0.24.1   |     |     |
| SVOS> ip     | disable       |     |     |
| SVOS> ip     | show          |     |     |
| Interface    | : Disabled    |     |     |
SVOS>
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ls
| ls [<OPTIONS>] | [<FILE-NME>] |     |     |
| -------------- | ------------ | --- | --- |
Description
Thiscommandlistsdirectorycontents.
| Parameter |     |     | Description                                      |
| --------- | --- | --- | ------------------------------------------------ |
| <OPTIONS> |     |     | Specifiesoptionsforthecommand.                   |
| -1        |     |     | Showsone-columnoutput.                           |
| -a        |     |     | Showsentrieswhichstartwithaperiod(.).            |
| -A        |     |     | Showsoutputsimilarto-a,butexcludesaperiod(.)anda |
doubleperiod(..).
| -C  |     |     | Showsoutputlistbycolumns.                       |
| --- | --- | --- | ----------------------------------------------- |
| -x  |     |     | Showsoutputlistbylines.                         |
| -d  |     |     | Showslistingofdirectoryentriesinsteadofcontents |
| -L  |     |     | Followssymlinks.                                |
ServiceOS|123

| Parameter |     |     | Description                                      |     |     |
| --------- | --- | --- | ------------------------------------------------ | --- | --- |
| -H        |     |     | Followssymlinksonthecommandline.                 |     |     |
| -R        |     |     | Recurse.                                         |     |     |
| -p        |     |     | Appendsaslash(/)todirectoryentries.              |     |     |
| -F        |     |     | Appendsanindicatortoentries.Anindicatorcanbeasan |     |     |
asterisk(*)orslash(/)orequalsign(=)oratsign(@)orpipe
(|).
| -l  |     |     | Showstheoutputinalonglistingformat. |     |     |
| --- | --- | --- | ----------------------------------- | --- | --- |
-i
Showsthelistinodenumbers.
| -n  |     |     | ShowsalistofnumericUIDsandGIDsinsteadofnames. |     |     |
| --- | --- | --- | --------------------------------------------- | --- | --- |
-s
Showsalistofallocatedblocks.
| -e  |     |     | Showsinonecolumnalistwiththefulldateandtime. |     |     |
| --- | --- | --- | -------------------------------------------- | --- | --- |
-h
Showslistsizesinhumanreadableformat(1K,243M,2G)
withaone-columnoutput.
| -r     |     |     | Showsinonecolumnasortinreverseorder.            |     |     |
| ------ | --- | --- | ----------------------------------------------- | --- | --- |
| -S     |     |     | Showsinonecolumnasortbysize.                    |     |     |
| -X     |     |     | Showsintheoutputsortbyextension.                |     |     |
| -v     |     |     | Showsinonecolumnasortbyversion.                 |     |     |
| -c     |     |     | With-l,itshowsasortinonecolumnbyctime.          |     |     |
| -t     |     |     | With-l,itshowsasortbymtime.                     |     |     |
| -u     |     |     | With-l,sortbyatime.                             |     |     |
| -c     |     |     | With-l,itshowsasortinonecolumnbyctime           |     |     |
| -w <N> |     |     | Assumesthattheterminalhasthenumberofcolumnswide |     |     |
asspecifiedby<N>.
| --color[={always | | never | | auto}] | Controlscolorintheoutput.        |     |     |
| ---------------- | ------- | -------- | -------------------------------- | --- | --- |
| <FILE-NAME>      |         |          | Specifiesthenameofthefiletolist. |     |     |
Example
Listingdirectorycontents:
| SVOS> ls -la | /nos |             |           |          |             |
| ------------ | ---- | ----------- | --------- | -------- | ----------- |
| drwxr-xr-x   | 3 0  | 0           | 4096 Nov  | 21 03:19 | .           |
| drwxr-xr-x   | 11 0 | 0           | 220 Nov   | 21 03:21 | ..          |
| drwx------   | 2 0  | 0           | 16384 Nov | 21 03:20 | lost+found  |
| -rwxr-xr-x   | 1 0  | 0 205957424 | Nov       | 21 03:19 | primary.swi |
SVOS>
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 124

| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
md5sum
| md5sum [-c | | -s | -w] | [<FILE-NAME>] |     |
| ---------- | ---------- | ------------- | --- |
Description
ThiscommandcomputesandcheckstheMD5messagedigest.
| Parameter   |          |     | Description                                           |
| ----------- | -------- | --- | ----------------------------------------------------- |
| [-c |       | -s | -w] |     | Selectstheoptionsforthecommand.                       |
| -c          |          |     | Specifiestocheckthesumsagainstthelistinfiles.         |
| -s          |          |     | Specifiesnotoutputanything,statuscodeshowssuccess.    |
| -w          |          |     | Specifiestowarnaboutimproperlyformattedchecksumlines. |
| <FILE-NAME> |          |     | Specifiesthefilenametorunthechecksumagainst.          |
Example
ComputingandcheckingtheMD5messagedigestfor/nos/primary.swi:
| SVOS>                            | md5sum /nos/primary.swi |     |                  |
| -------------------------------- | ----------------------- | --- | ---------------- |
| 93ffc89e7ec357854704d8e450c4b7ab |                         |     | /nos/primary.swi |
SVOS>
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ServiceOS|125

mkdir
| mkdir [-m | | -p] [<DIRECTORY-NAME>] |     |     |
| ----------- | ---------------------- | --- | --- |
Description
Thiscommandmakesdirectories.
| Parameter |     |     | Description                       |
| --------- | --- | --- | --------------------------------- |
| [-m | -p] |     |     | Specifiestheoptionsforthecommand. |
-m
Specifiesthemode.
| -p  |     |     | Specifiestomakeparentdirectoriesasneededwithnoerrorsfor |
| --- | --- | --- | ------------------------------------------------------- |
pre-existingdirectories.
| <DIRECTORY-NAME> |     |     | Specifiesthedirectorytocreate. |
| ---------------- | --- | --- | ------------------------------ |
Example
Makingthedirdirectory:
| SVOS> mkdir         | dir     |         |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
mount
mount <DEVICE>
Description
ThiscommandmountstheSSD partitionstothefollowinglocations:/coredump,/logs,/nos,/selftest,
andmountstheUSBdeviceto/mnt/usb.
UserscanmountUSBflashdrivesformattedaseitherFAT16orFAT32withasinglepartition.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<DEVICE> Specifiesthedevicetobemounted.Supporteddeviceoptions
includeallandusb.
Examples
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 126

| MountingalloftheSSD | partitions: |         |              |
| ------------------- | ----------- | ------- | ------------ |
| SVOS> mount         | all         |         |              |
| SVOS> mount         | usb         |         |              |
| Command History     |             |         |              |
| Release             |             |         | Modification |
| 10.07orearlier      |             |         | --           |
| Command Information |             |         |              |
| Platforms           | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
mv
| mv [-f | -i | | -n] <TARGET-DIRECTORY> |     |     |
| ----------- | ------------------------ | --- | --- |
Description
Thiscommandmoves(renames)files.
| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
| -f        |     |     | Specifiesnottopromptbeforeoverwriting. |
| -i        |     |     | Specifiestopromptbeforeoverwriting.    |
| -n        |     |     | Specifiestonotoverwriteanexistingfile. |
Example
Movingthefilenamedmyfile:
| SVOS> mv            | myfile  |         |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ServiceOS|127

| password | (svos) |     |     |     |
| -------- | ------ | --- | --- | --- |
password
Description
SetstheadminuseraccountpasswordforbothServiceOSandAOS-CXoncetheuserbootsintoAOS-CX
andsavestheconfiguration.Thiswilloverwritethepreviouspasswordifoneexists.Userinputis
maskedwithasterisks.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Settingtheadminaccountpassword:
| SVOS> password            |     |     |     |     |
| ------------------------- | --- | --- | --- | --- |
| Enter password:********   |     |     |     |     |
| Confirm password:******** |     |     |     |     |
SVOS>
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ping
ping <HOST-IP-ADDRESS>
Description
Pingsnetworkhostsfordebugpurposes.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<HOST-IP-ADDRESS>
SpecifiesthehostIPaddress.
Example
Pinginganetworkhost:
| SVOS> ping     | 10.0.8.10       |       |                   |     |
| -------------- | --------------- | ----- | ----------------- | --- |
| PING 10.0.8.10 | (10.0.8.10):    | 56    | data bytes        |     |
| 64 bytes       | from 10.0.8.10: | seq=0 | ttl=63 time=3.496 | ms  |
| 64 bytes       | from 10.0.8.10: | seq=1 | ttl=63 time=0.367 | ms  |
| 64 bytes       | from 10.0.8.10: | seq=2 | ttl=63 time=0.380 | ms  |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 128

| 64 bytes | from 10.0.8.10: | seq=3 | ttl=63 | time=0.282 | ms  |
| -------- | --------------- | ----- | ------ | ---------- | --- |
| 64 bytes | from 10.0.8.10: | seq=4 | ttl=63 | time=0.669 | ms  |
^C
| --- 10.0.8.10 | ping         | statistics          | ---       |     |             |
| ------------- | ------------ | ------------------- | --------- | --- | ----------- |
| 5 packets     | transmitted, | 5 packets           | received, | 0%  | packet loss |
| round-trip    | min/avg/max  | = 0.282/1.038/3.496 |           | ms  |             |
SVOS>
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
8400 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
pwd
pwd
Description
Displaysthecurrentworkingdirectory.
Example
Displayingthecurrentworkingdirectory:
| SVOS> pwd |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
/home
SVOS>
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
reboot
reboot
ServiceOS|129

Description
RebootstheManagementModule.
Example
Rebootingthemanagementmodule:
| SVOS>          | reboot      |         |              |
| -------------- | ----------- | ------- | ------------ |
| reboot:        | Restarting  | system  |              |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
rm
| rm [-f | | -i | -R | -r] | <FILE-NAME> |     |
| -------- | ------------- | ----------- | --- |
Description
Removesfilesordirectories.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
[-f | -i | -R | -r] Selectstheoptionsforremovingfilesordirectories.
| -f   |     |     | Neverpromptbeforeremovingfilesordirectories.  |
| ---- | --- | --- | --------------------------------------------- |
| -i   |     |     | Alwayspromptbeforeremovingfilesordirectories. |
| -R | | -r  |     | Recursive.                                    |
Example
Removingthefilenamedfoo:
| SVOS>          | rm foo  |     |              |
| -------------- | ------- | --- | ------------ |
| Command        | History |     |              |
| Release        |         |     | Modification |
| 10.07orearlier |         |     | --           |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 130

| Command   | Information |         |           |
| --------- | ----------- | ------- | --------- |
| Platforms | Command     | context | Authority |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
rmdir
| rmdir [-p] | <DIRECTORY-NAME> |     |     |
| ---------- | ---------------- | --- | --- |
Description
Removesemptydirectories.
| Parameter |     |     | Description                         |
| --------- | --- | --- | ----------------------------------- |
| -p        |     |     | Specifiestoremoveparentdirectories. |
Example
Removingtheemptyfoodirectory:
| SVOS> | rmdir foo |     |     |
| ----- | --------- | --- | --- |
SVOS>
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
ServiceOS(SVOS>)
rightsforthiscommand.
secure-mode
| secure-mode | <enhanced | | standard | | status> |
| ----------- | --------- | ---------- | --------- |
Description
Setsthesecuremodetoenhancedorstandardsecuremode.Alsocandisplaythecurrentsecuremode.
Azeroizationisrequiredbeforeswitchingbetweenenhancedandstandardsecuremodes.
Thecommandalsodisplaysamessagenotifyingtheuserthattheyarealreadyinthetargetedsecure
mode.
Example
Settingthesecuremodetoenhancedorstandard:
ServiceOS|131

| SVOS> secure-mode |             | --help    |     |            |           |     |     |
| ----------------- | ----------- | --------- | --- | ---------- | --------- | --- | --- |
| Usage:            | secure-mode | <enhanced |     | | standard | | status> |     |     |
Set or retrieve the secure mode setting. Requires a zeroization to change modes.
SVOS>
```
```
| SVOS> secure-mode |     | enhanced |     |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| This will | set the | switch | into | enhanced | secure | mode. | Before |
| --------- | ------- | ------ | ---- | -------- | ------ | ----- | ------ |
enhanced secure mode is enabled, the switch must securely erase
| all customer | data        | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | ----------- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This will    | initiate    | a reboot | and          | render | the switch |              | unavailable |
| until the    | zeroization |          | is complete. |        |            |              |             |
| This should  | take        | several  | minutes      | to     | one hour   | to complete. |             |
############################WARNING############################
| Continue | (y/n)?     | y      |     |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |     |
```
```
| SVOS> secure-mode |     | standard |     |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| This will | set the | switch | into | standard | secure | mode. | Before |
| --------- | ------- | ------ | ---- | -------- | ------ | ----- | ------ |
standard secure mode is enabled, the switch must securely erase
| all customer | data        | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | ----------- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This will    | initiate    | a reboot | and          | render | the switch |              | unavailable |
| until the    | zeroization |          | is complete. |        |            |              |             |
| This should  | take        | several  | minutes      | to     | one hour   | to complete. |             |
############################WARNING############################
| Continue | (y/n)?     | y      |     |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |     |
```
```
| SVOS> secure-mode |     | standard |     |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| Secure | mode is already |     | set to | standard. | Setting | it  | again will |
| ------ | --------------- | --- | ------ | --------- | ------- | --- | ---------- |
repeat the zeroization process. The switch must securely erase
| all customer | data        | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | ----------- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This will    | initiate    | a reboot | and          | render | the switch |              | unavailable |
| until the    | zeroization |          | is complete. |        |            |              |             |
| This should  | take        | several  | minutes      | to     | one hour   | to complete. |             |
############################WARNING############################
| Continue | (y/n)?     | y      |     |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |     |
```
```
| SVOS> secure-mode |        | status  |      |     |     |     |     |
| ----------------- | ------ | ------- | ---- | --- | --- | --- | --- |
| enhanced          | secure | mode is | set. |     |     |     |     |
SVOS>
| Command | History |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 132

| Release        |             |         |         | Modification |
| -------------- | ----------- | ------- | ------- | ------------ |
| 10.07orearlier |             |         |         | --           |
| Command        | Information |         |         |              |
| Platforms      |             | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sh
sh
Description
Launchesabashshellforsupportpurposes.Toquitbash,enterexit.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Launchingabashshell:
| SVOS> | sh  |     |     |     |
| ----- | --- | --- | --- | --- |
switch:/cli/fs/home#
| Command        | History     |         |         |              |
| -------------- | ----------- | ------- | ------- | ------------ |
| Release        |             |         |         | Modification |
| 10.07orearlier |             |         |         | --           |
| Command        | Information |         |         |              |
| Platforms      |             | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| system    | serviceos |                 | password-prompt |     |
| --------- | --------- | --------------- | --------------- | --- |
| system    | serviceos | password-prompt |                 |     |
| no system | serviceos |                 | password-prompt |     |
Description
UsethiscommandtoenablepasswordauthenticationforServiceOS.Bydefault,theServiceOSshell
(accessibleonlyfromthelocalswitchconsoleport)requiresnopasswordtologinasanadminuse.
Whenthissettingisenabled,thesamepasswordusedtoauthenticatetheadminuserintheAOS-CXCLI
orWeUIcanbeusedtologintotheServiceOSshell.Ifthissettingisenabled,aforgottenadminuser
passwordcannotberesetusingServiceOS;iftherearenootherlocalorRADIUS/TACACSuseraccounts
withadministrator-levelaccess,theswitchmustbezeroizedbyenteringtheusername zeroize
commandattheServiceOSloginprompttorestoreadministratoraccess.
ServiceOS|133

Example
EnabllingpasswordauthenticationforServiceOS
| switch(config)#     | system  | serviceos | password-prompt |
| ------------------- | ------- | --------- | --------------- |
| Command History     |         |           |                 |
| Release             |         |           | Modification    |
| 10.07orearlier      |         |           | --              |
| Command Information |         |           |                 |
| Platforms           | Command | context   | Authority       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
umount
umount <DEVICE>
Description
UnmountstheSSD partitionsmountedtothefollowinglocations:/coredump,/logs,/nos,/selftest,
andunmountstheUSBdevicemountedto/mnt/usb.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<DEVICE> Specifiesthedevicetobeunmounted.Supporteddeviceoptions
includeallandusb.
Examples
Unmountingalldevices:
| SVOS> umount | all |     |     |
| ------------ | --- | --- | --- |
| SVOS> umount | usb |     |     |
UnmountingaUSBdevice:
| SVOS> umount    | all |     |              |
| --------------- | --- | --- | ------------ |
| SVOS> umount    | usb |     |              |
| Command History |     |     |              |
| Release         |     |     | Modification |
| 10.07orearlier  |     |     | --           |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 134

| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
update
| update {primary | | secondary} | <IMAGE> |     |     |
| --------------- | ------------ | ------- | --- | --- |
Description
Verifiesandinstallsaproductimage.Theusercanselecttheprimaryorsecondarybootprofileto
updateandthelocationofthefile.
| Parameter  |            |     | Description |     |
| ---------- | ---------- | --- | ----------- | --- |
| {primary | | secondary} |     |             |     |
Selectseithertheprimaryorsecondaryimage.
| <IMAGE> |     |     | Specifiestheimagename. |     |
| ------- | --- | --- | ---------------------- | --- |
Examples
UpdatingthesoftwareimageusingTFTP:
TheOOBMportisdisabledonfirstbootandmustbeenabledusingtheipcommand.
SVOS>
ip dhcp
| SVOS> ip     | show                    |     |              |            |
| ------------ | ----------------------- | --- | ------------ | ---------- |
| Interface    | : Link Up               |     |              |            |
| IP Address   | : 192.0.2.22            |     |              |            |
| Subnet Mask: | 255.255.200.20          |     |              |            |
| Gateway      | : 10.0.24.1             |     |              |            |
| SVOS> tftp   | -g -r XL.10.00.0001.swi |     | -l image.swi | 192.4.8.10 |
XL.10.00.0001.swi 100% |*******************************| 178M 0:00:00 ETA
| SVOS> ls |     |     |     |     |
| -------- | --- | --- | --- | --- |
image.swi
SVOS>
| update    | primary          | image.swi |     |     |
| --------- | ---------------- | --------- | --- | --- |
| Updating  | primary software | image...  |     |     |
| Verifying | image...         |           |     |     |
Done
UpdatethesoftwareimageusingUSB:
ThisexampleassumesthattheuserhaspreloadedaUSBflashdrivewiththeimagetobeupdated.Theimage
nameontheflashdriveisnotimportant.
| SVOS> mount | usb      |     |     |     |
| ----------- | -------- | --- | --- | --- |
| SVOS> ls    | /mnt/usb |     |     |     |
image.swi
| SVOS> update | primary          | /mnt/usb/image.swi |     |     |
| ------------ | ---------------- | ------------------ | --- | --- |
| Updating     | primary software | image...           |     |     |
ServiceOS|135

| Verifying | image... |     |     |     |
| --------- | -------- | --- | --- | --- |
Done
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
tftp
tftp {-b | -g | -l <LOCAL-FILE> | -p | -r <REMOTE-FILE>} host [<PORT>]
Description
Transfersfilestoandfromaremotemachine(TFTPafile).
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{-b | -g | -l | -p | -r <REMOTE-FILE>} Selectstheoptionsfortransferringafile.
| -b  |     |     | Specifiesthetransferblocksofsizeoctets.Thedefault |     |
| --- | --- | --- | ------------------------------------------------- | --- |
blocksizeissetto1468,whichcanbeoverriddenwiththe
-boption.
-g
Specifiestogetafile.
| -l  |     |     | Specifiesalocalfile. |     |
| --- | --- | --- | -------------------- | --- |
-p
Specifiestoputafileinremotelocation.
| -r <REMOTE-FILE> |     |     | Specifiesaremotefile. |     |
| ---------------- | --- | --- | --------------------- | --- |
<PORT>
Specifiestheportfortransfer.Ifnoportoptionis
specified,TFTPusesthestandardUDPport69bydefault.
Example
Transferringfiles:
SVOS>
| tftp | -b 65464 | -g -r XL.10.00.0002.swi.swi |     | 192.0.2.1 |
| ---- | -------- | --------------------------- | --- | --------- |
XL.10.00.0002 100% |*******************************| 178M 0:00:00 ETA
SVOS>
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 136

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
version
version
Description
Displaysthefollowingbuildstrings:
n Version.
n Builddate.
n Buildtime.
n BuildID.
n SHA.
Example
Displayingversionbuildstrings:
| SVOS> version |              |                                                   |              |
| ------------- | ------------ | ------------------------------------------------- | ------------ |
| ServiceOS     | Information: |                                                   |              |
| Version:      |              | GT.01.01.0001                                     |              |
| Build         | Date:        | 2017-07-19                                        | 14:52:31 PDT |
| Build         | ID:          | ServiceOS:GT.01.01.0001:461519208911:201707191452 |              |
| SHA:          |              | 46151920891195cdb2267ea6889a3c6cbc3d4193          |              |
SVOS>
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ServiceOS|137

Chapter 15
In-System Programming
| In-System | Programming |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
TheISP(In-SystemProgramming)featureprovidesanautomatedwaytorolloutupdatestovarious
programmabledevicesinanAOS-CXnetworkswitch,aftertheproducthasshipped.ISPisintendedto
runautomaticallyeitheratboottimeorasnewmodulesareinsertedintothechassisatruntime.
| Show tech | command |     | list for | the ISP | feature |
| --------- | ------- | --- | -------- | ------- | ------- |
| Task      |         |     |          |         | Command |
show tech isp
Displayingversionsofallpresentprogrammabledevices.
show tech update-log
DisplayingstoredlogfilesfromanyISPupdatesonthesystem.
SeetheCommand-LineInterfaceGuideforadditionalinformationabouttheshow techcommands.
| In-System | Programming |     | commands |     |     |
| --------- | ----------- | --- | -------- | --- | --- |
clear update-log
clear update-log
Description
ClearsstoredlogfilesofanyIn-SystemProgrammingupdatesonthesystem.
Whenrunontheactivemanagementmodule,thiscommandalsoclearslogfilesfrommostotherCPUs
inthesystem.Itmustberunseparatelyinstandbycontexttoclearlogfilesonthestandbymanagement
module.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show needed-updates
| show needed-updates | [next-boot |     | [primary|secondary]] |     |     |
| ------------------- | ---------- | --- | -------------------- | --- | --- |
138
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

Description
Displayswhetheranyprogrammabledevicesareinneedofanupdate.
Withoutthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetothecurrently
runningAOS-CXimage.
Withthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetoanAOS-CXimagefile
inthepersistentstorageoftheswitch,whichmightbedifferentfromthecurrentlyrunningimage.If
eithertheprimaryorsecondaryparameterisspecified,thiscommandqueriesthatspecificAOS-CX
imagefile.Otherwise,itqueriesthedefaultAOS-CXimagefileassetbythemostrecentboot systemor
boot set-defaultcommand.
Whenrunontheactivemanagementmodule,thiscommandalsoretrievesinformationfrommost
otherCPUsinthesystem,butitmustberunseparatelyinstandbycontexttodisplayinformationabout
thestandbymanagementmodule.
Whenrunonthestandbymanagementmodule,thiscommandonlydisplaysinformationondevices
specifictothestandbymanagementmoduleandnotothermodulesinthesystem.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
In-SystemProgramming|139

Chapter 16

Selftest

Selftest

Diagnostics involve four important sub-categories.

n Boot-up Diagnostics (Power On Selftest aka POST)

n Run-time Diagnostics (Hardware Health Monitoring)

n Online Diagnostics

n Offline Diagnostics

Power On Self Test (POST) is the first task which verifies the hardware functionality of various modules
during boot-up. Based on the criticality of the test, the selftest module decides whether to go ahead with
the boot-up sequence of a particular subsystem or interface during a POST failure.

POST comprises of the following:

n Memory BISTs (Built-in Self Test)

This is to verify the memory block(s) present in the module and involves both internal and external
memories.

The memory tables are critical for proper functionality of the system, so any failures in these tests
will result in the corresponding subsystem to be marked as "Failed" and thus that subsystem will not
be available for use.

n Front-end Port Loopback tests

This is to verify the physical port front-end interface.

These tests check if a particular interface can function properly. A test failure would mean that the
particular interface is marked as "Failed" and thus it would become unavailable for use.

This test is run when "no fastboot" is configured.

Selftest commands

fastboot
fastboot
no fastboot

Description

Enables fastboot for the system.

The no form of this command disables fastboot for the system.

Usage

When fastboot is enabled, most tests under a Power On Self Test (POST) are skipped. By default,
fastboot is enabled.

After disabling fastboot, save switch configurations and then reboot for POST to run. POST verifies the
hardware functionality of various modules during boot-up. Based on the criticality of the test, the
selftest module decides whether to go ahead with the boot-up sequence of a particular subsystem or
interface during a POST failure.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

140

POSTrunsmemorybuilt-inselftest(BISTs)andfront-endportloopbacktests.MemoryBISTsverifythe
internalandexternalmemoryblockspresentinthemodule.Thememorytablesarecriticalforproper
functionalityofthesystemsoanyfailuresinthesetestsresultsinthecorrespondingsubsystemtobe
markedas"Failed"andthusthatsubsystemisnotavailableforuse.
Front-endportloopbacktestsverifythephysicalportfront-endinterface.Thesetestscheckifa
particularinterfacecanfunctionproperly.Atestfailuremeansthataparticularinterfacehasbeen
markedas"Failed"andisnowunavailableforuse.
Examples
Enablingfastboot:
| switch#         | configure terminal  |     |     |
| --------------- | ------------------- | --- | --- |
| switch(config)# | fastboot            |     |     |
| switch(config)# | end                 |     |     |
| switch#         | show running-config |     |     |
| Current         | configuration:      |     |     |
!
| !Version   | AOS-CX ML.10.06.0001 |                |                      |
| ---------- | -------------------- | -------------- | -------------------- |
| module 1/1 | product-number       | jl726a!Version | AOS-CX FL.10.06.0001 |
| module 1/1 | product-number       | jl661a!Version | AOS-CX XL.10.00.0002 |
| module 1/1 | product-number       | jl363a!Version | AOS-CX PL.10.06.0001 |
| module 1/1 | product-number       | jl677a         |                      |
!
!
!
!
!
!
!
vlan 1
| interface | 1/1/1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
no routing
Disablingfastboot:
| switch#         | configure terminal |     |     |
| --------------- | ------------------ | --- | --- |
| switch(config)# | no fastboot        |     |     |
| switch(config)# | end                |     |     |
| switch(config)# | write mem          |     |     |
Configuration changes will take time to process, please be patient.
| switch# | show running-config |     |     |
| ------- | ------------------- | --- | --- |
| Current | configuration:      |     |     |
!
| !Version   | AOS-CX ML.10.06.0001 |                |                      |
| ---------- | -------------------- | -------------- | -------------------- |
| module 1/1 | product-number       | jl726a!Version | AOS-CX FL.10.06.0001 |
| module 1/1 | product-number       | jl661a!Version | AOS-CX XL.10.00.0002 |
| module 1/1 | product-number       | jl363a!Version | AOS-CX PL.10.06.0001 |
| module 1/1 | product-number       | jl677a         |                      |
!
!
!
no fastboot
!
!
!
!
vlan 1
Selftest|141

| interface | 1/1/1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
no routing
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show selftest |             |            |     |
| ------------- | ----------- | ---------- | --- |
| show selftest | [brief]     | [vsx-peer] |     |
| show selftest | line-module | <SLOT-ID>  |     |
show selftest line-module <SLOT-ID> interface [brief] [vsx-peer]
| show selftest | interface | [<PORT-NUM>] | [vsx-peer] |
| ------------- | --------- | ------------ | ---------- |
For8400and6400switchesonly:
show selftest {line-module | fabric-module} [<SLOT-ID>] [brief] [vsx-peer]
Description
Displaysselftestresults.
| Parameter   |     |     | Description                                         |
| ----------- | --- | --- | --------------------------------------------------- |
| [brief]     |     |     | Showstheselftestresultsasabriefdescription.Default. |
| line-module |     |     | Showstheselftestresultsforalinemodule.              |
fabric-module Showstheselftestresultsforafabricmodule.Applicableonlyfor
8400and6400switches.
<SLOT-ID> ShowstheselftestresultsfortheslotIDofthelineorfabric
module.
| <PORT-NUM> |     |     | Showstheselftestresultsfortheportnumber. |
| ---------- | --- | --- | ---------------------------------------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Displayingtheoutputwhenfastbootisdisabledonan8400ora6400switch:
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 142

| switch#         | show selftest       |               |                     |                     |          |
| --------------- | ------------------- | ------------- | ------------------- | ------------------- | -------- |
| Name            | Id Status           |               | ErrorCode           | LastRunTime         |          |
| ----------      | ---- -------------- |               | ----------          | ------------------- |          |
| LineModule      | 1/1 passed          |               | 0x0                 | 2016-10-15          | 10:10:09 |
| LineModule      | 1/2 failed          |               | 0x09                | 2016-10-15          | 10:10:56 |
| Fabric 1/1      | passed              |               | 0x0                 | 2016-10-15          | 10:10:09 |
| Fabric 1/2      | failed              |               | 0x1E                | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | line-module   |                     |                     |          |
| Name            | Id Status           |               | ErrorCode           | LastRunTime         |          |
| ----------      | ---- -------------- |               | ---------           | ------------------- |          |
| LineModule      | 1/1 passed          |               | 0x0                 | 2016-10-15          | 10:10:09 |
| LineModule      | 1/2 failed          |               | 0x09                | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | fabric-module |                     |                     |          |
| Name Id         | Status              |               | ErrorCode           | LastRunTime         |          |
| ------ -------- | --------------      |               | ---------           | ------------------- |          |
| Fabric 1/1      | passed              |               | 0x0                 | 2016-10-15          | 10:10:09 |
| Fabric 1/2      | failed              |               | 0x1E                | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | fabric-module | 1/2                 |                     |          |
| Name Id         | Status              |               | ErrorCode           | LastRunTime         |          |
| ------ -------- | --------------      |               | ---------           | ------------------- |          |
| Fabric 1/2      | failed              |               | 0x11                | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | line-module   | 1/10                |                     |          |
| Name            | Id Status           |               | ErrorCode           | LastRunTime         |          |
| ----------      | ---- -------------- |               | ---------           | ------------------- |          |
| LineModule      | 1/10 failed         |               | 0x1A                | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | interface     | 1/2/2               |                     |          |
| Name            | Status              | ErrorCode     | LastRunTime         |                     |          |
| -------         | --------------      | ---------     | ------------------- |                     |          |
| 1/2/2           | passed              | 0x0           | 2016-11-19          | 05:10:11            |          |
| switch#         | show selftest       | line-module   | 1/3                 | interface           |          |
| Name            | Status              | ErrorCode     | LastRunTime         |                     |          |
| -------         | --------------      | ---------     | ------------------- |                     |          |
| 1/3/1           | passed              | 0x0           | 2016-11-19          | 05:10:11            |          |
| 1/3/2           | passed              | 0x0           | 2016-11-19          | 05:10:11            |          |
| 1/3/3           | passed              | 0x0           | 2016-11-19          | 05:10:11            |          |
| 1/3/31          | failed              | 0x20          | 2016-11-19          | 05:10:11            |          |
Displayingtheoutputwhenfastbootisenabled:
| switch#    | show selftest       |               |            |                     |     |
| ---------- | ------------------- | ------------- | ---------- | ------------------- | --- |
| Name       | Id Status           |               | ErrorCode  | LastRunTime         |     |
| ---------- | ---- -------------- |               | ---------- | ------------------- |     |
| LineModule | 1/1 skipped         |               | 0x0        |                     |     |
| LineModule | 1/2 skipped         |               | 0x0        |                     |     |
| Fabric     | 1/1 skipped         |               | 0x0        |                     |     |
| Fabric     | 1/2 skipped         |               | 0x0        |                     |     |
| switch#    | show selftest       | line-module   |            |                     |     |
| Name       | Id Status           |               | ErrorCode  | LastRunTime         |     |
| ---------- | ---- -------------- |               | ---------  | ------------------- |     |
| LineModule | 1/1 skipped         |               | 0x0        |                     |     |
| LineModule | 1/2 skipped         |               | 0x0        |                     |     |
| switch#    | show selftest       | fabric-module |            |                     |     |
| Name       | Id Status           |               | ErrorCode  | LastRunTime         |     |
Selftest|143

| ---------- |          | ---- -------------- |               | ---------- |      | ------------------- |
| ---------- | -------- | ------------------- | ------------- | ---------- | ---- | ------------------- |
| Fabric     |          | 1/1 skipped         |               | 0x0        |      |                     |
| Fabric     |          | 1/2 skipped         |               | 0x0        |      |                     |
| Fabric     |          | 1/3 skipped         |               | 0x0        |      |                     |
| switch#    | show     | selftest            | fabric-module |            | 1/2  |                     |
| Name       | Id       | Status              |               | ErrorCode  |      | LastRunTime         |
| ------     | -------- | --------------      |               | ---------  |      | ------------------- |
| Fabric     | 1/2      | skipped             |               | 0x0        |      |                     |
| switch#    | show     | selftest            | line-module   |            | 1/10 |                     |
| Name       |          | Id Status           |               | ErrorCode  |      | LastRunTime         |
| ---------- |          | ---- -------------- |               | ---------  |      | ------------------- |
| LineModule |          | 1/10 skipped        |               | 0x0        |      |                     |
Displayingtheoutputwhenfastbootisenabled:
| switch# | show           | selftest | interface | 1/1/2 |                     |     |
| ------- | -------------- | -------- | --------- | ----- | ------------------- | --- |
| Name    | Status         |          | ErrorCode |       | LastRunTime         |     |
| ------- | -------------- |          | --------- |       | ------------------- |     |
| 1/1/2   | skipped        |          | 0x0       |       |                     |     |
switch#
|                | show           | selftest | line-module |     | 1/1                 | interface |
| -------------- | -------------- | -------- | ----------- | --- | ------------------- | --------- |
| Name           | Status         |          | ErrorCode   |     | LastRunTime         |           |
| -------        | -------------- |          | ---------   |     | ------------------- |           |
| 1/1/1          | skipped        |          | 0x0         |     |                     |           |
| 1/1/2          | skipped        |          | 0x0         |     |                     |           |
| 1/1/3          | skipped        |          | 0x0         |     |                     |           |
| 1/1/31         | skipped        |          | 0x0         |     |                     |           |
| Command        | History        |          |             |     |                     |           |
| Release        |                |          |             |     | Modification        |           |
| 10.07orearlier |                |          |             |     | --                  |           |
| Command        | Information    |          |             |     |                     |           |
| Platforms      |                | Command  | context     |     | Authority           |           |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 144

Chapter 17

Zeroization

Zeroization

Device zeroization lets you remove all user files from flash storage, including solid-state drives (SSDs).
User files cannot be retrieved after the zeroization is complete.

Zeroization can occur in both AOS-CX and Service OS. This section covers zeroization and AOS-CX. For information

about zeroization and Support OS, see erase zeroize.

Zeroization preserves the primary and secondary software images on the SSD. Zeroization also
preserves manufacturing information.

The sensitive user files stored on an SSD or SPI flash/EEPROM storage or both include:

n Switch configurations.

n System generated private keys.

n User installed private keys.

n Admin/operator password files.

Using CLI, you can change the switch settings from standard secure mode to enhanced secure mode.
Setting the switch back to standard secure mode can only be performed through Service OS. For more
information on how to change switch settings using Server OS, see Service OS.

Enhance secure mode is used to enhance the switch security. In enhanced security mode, the switch
(Product OS) start-shell command is disabled for security purpose except through ServiceOS.

Zeroization commands

erase all zeroize
erase [all] zeroize

Description

Restores the switch to its factory default configuration. You will be prompted before the procedure
starts. Once complete, the switch will restart from the primary image with factory default settings.

Usage

The erase all command is always available in the CLI. On running the erase all command, the switch is
restored to a factory default settings, but retains the enhanced secure mode settings.

The erase all zeroize command is not available in the CLI when enhanced secure mode is enabled. This
command restore the switch to a factory default settings. On running the erase all zeroize command in
enhanced secure mode, displays a notification stating that the command is unavailable in enhanced
secure mode.

Back up all data before running this command as all configuration settings will be lost.

Example

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

145

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

Restoring the switch to factory default configuration only when enhance secure mode settings is
disabled.

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
################ WARNING: DO NOT POWER OFF UNTIL
##########
ZEROIZATION IS COMPLETE ##########
################
################ This should take several minutes ##########
##########
################ to one hour to complete

################ Restoring files ###########################

...

We'd like to keep you up to date about:

* Software feature updates
* New product announcements
* Special events

Please register your products now at: https://networkingsupport.hpe.com

Zeroization | 146

Whenyouloginafterzeroization,yougetaprompttocreateapasswordfortheadministratoraccount.Youcan
setthepasswordasblank(tosetthepasswordasblank,hitenterattheprompt)ortype1to32printableASCII
characters,excludingspacesandquestionmarks(?).Formoreinformationonpasswordrequirements,see
PasswordrequirementsintheSecurityGuide.
| switch | login: | admin |     |     |
| ------ | ------ | ----- | --- | --- |
Password:
| Please         | configure     | the 'admin' | user account                 | password. |
| -------------- | ------------- | ----------- | ---------------------------- | --------- |
| Enter new      | password:     | *****       |                              |           |
| Confirm        | new password: | *****       |                              |           |
| Command        | History       |             |                              |           |
| Release        |               |             | Modification                 |           |
| 10.11.1010     |               |             | IntroducederaseallCLIcommand |           |
| 10.07orearlier |               |             | --                           |           |
| Command        | Information   |             |                              |           |
| Platforms      | Command       | context     | Authority                    |           |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 147

Chapter 18
Terminal Monitor
| Terminal | Monitor |     |     |     |
| -------- | ------- | --- | --- | --- |
TheterminalmonitorisusedtodisplayselectivelogsdynamicallyontheVTYSHsession.Whenthe
terminalmonitorfeatureisenabledontheswitch,itdisplaysonlytheliveoractivelogs.Theselogsare
displayedontheSSHsessionorconsolesession.Ifrequired,youcanenabletheterminalmonitoringon
multiplesessions.
Itisimportanttomonitorthelogsdynamicallywhiledebugging,sothatyoucanco-relatetheissues.The
logscanbefilteredbytype(eventordebug),severity,orkeyword.Theterminalmonitorrunsin
synchronousmode,wheretheuserentersanycommand,thelogdisplaypausesuntilthecommand
executioniscomplete.ThisensuresthatthelogswillnotappearinbetweenotherCLIoutputsorwhile
theuseristyping.
TerminalmonitoringisnotpersistentintheSSH session.IftheSSHsessionisterminated,theterminalmonitoris
nolongervalid.However,loggingconsoleispersistentandisaddedtotheswitchconfiguration,soitwillpersist
betweentelnetsessions.
| Terminal | monitor |         | commands   |           |
| -------- | ------- | ------- | ---------- | --------- |
| logging  | console | {notify | | severity | | filter} |
logging console{notify <event|debug|all> | severity <level> | filter keyword}
| no logging | console |     |     |     |
| ---------- | ------- | --- | --- | --- |
Description
Enablestheloggingconsolefeatureintheconsolesession.Itdisplayalldebuglogoreventlogorboth
debugandeventlogmessages.Monitoringcanbefilteredwiththeseverityoptionsorwiththehelpof
keywords.Enablingterminalmonitorwithoutoptionsdisplaysbothdebugandeventlogwithaseverity
error.Thiscommandispersistentacrossreboot.
Thenoformofthiscommanddisablestheterminalmonitorconfiguration.
| Parameter |                   |     | Description |     |
| --------- | ----------------- | --- | ----------- | --- |
| notify    | <event|debug|all> |     |             |     |
Specifiesthetypeoflognotification.
|     |     |     | n Event:Displaystheeventlogmessages.(Default) |     |
| --- | --- | --- | --------------------------------------------- | --- |
|     |     |     | n Debug:Displaysthedebuglogmessages.          |     |
|     |     |     | n All:Displaysbotheventanddebuglogmessages.   |     |
severity <level> Specifiestheseveritylevelforthelogs.Thedifferentseveritylevels
areemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
| filter | <keyword> |     |     |     |
| ------ | --------- | --- | --- | --- |
Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
148
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries)

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringconsoleloggingintheconsolesession:
| switch(config)#  |             | logging | console |              |                    |               |
| ---------------- | ----------- | ------- | ------- | ------------ | ------------------ | ------------- |
| Terminal-monitor |             | is      | enabled | successfully |                    |               |
| switch(config)#  |             | logging | console |              | notify all         |               |
| Terminal-monitor |             | is      | enabled | successfully |                    |               |
| switch(config)#  |             | logging | console |              | notify event       | severity info |
| Terminal-monitor |             | is      | enabled | successfully |                    |               |
| switch(config)#  |             | logging | console |              | filter lldp        |               |
| Terminal-monitor |             | is      | enabled | successfully |                    |               |
| Command          | History     |         |         |              |                    |               |
| Release          |             |         |         |              | Modification       |               |
| 10.08            |             |         |         |              | Featureintroduced. |               |
| Command          | Information |         |         |              |                    |               |
| Platforms        | Command     |         | context |              | Authority          |               |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show terminal-monitor
show terminal-monitor
Description
Showswhethertheterminalmonitoringisenabledordisabled.
Thiscommandwillnotshowanyinformationaboutconsolelogging.
Examples
Displayingterminalmonitorwhenenabled:
| switch#          | show | terminal-monitor |         |     |     |     |
| ---------------- | ---- | ---------------- | ------- | --- | --- | --- |
| Terminal-monitor |      | is               | enabled |     |     |     |
-------------------------------------
| Notify | |   | Severity | |   | Filter |     |     |
| ------ | --- | -------- | --- | ------ | --- | --- |
-------------------------------------
| event |     | debug |     | lldp |     |     |
| ----- | --- | ----- | --- | ---- | --- | --- |
-------------------------------------
Displayingterminalmonitorwhendisabled:
TerminalMonitor|149

| switch# show        | terminal-monitor |          |              |     |
| ------------------- | ---------------- | -------- | ------------ | --- |
| Terminal-monitor    | is               | disabled |              |     |
| Command History     |                  |          |              |     |
| Release             |                  |          | Modification |     |
| 10.07orearlier      |                  |          | --           |     |
| Command Information |                  |          |              |     |
| Platforms           | Command          | context  | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| terminal-monitor |     | {notify | | severity | | filter} |
| ---------------- | --- | --------- | -------- | --------- |
terminal-monitor {notify <event|debug|all> | severity <level> | filter <keyword>}
no terminal-monitor
Description
Enablesandsavestheterminalmonitorfeatureintheswitchconfiguration.Itdisplaysalldebuglogor
eventlogorbothdebugandeventlogmessages.Terminalmonitoringcanbefilteredwiththeseverity
optionsorwiththehelpofkeywords.Enablingterminalmonitorwithoutoptionsdisplaysbothdebug
andeventlogwithaseverityerror.
Thenoformofthiscommandremovestheterminalmonitorfeaturefromtheswitchconfigurationand
thecommandwillnotpersist.
| Parameter                |     |     | Description                        |     |
| ------------------------ | --- | --- | ---------------------------------- | --- |
| notify <event|debug|all> |     |     | Specifiesthetypeoflognotification. |     |
n Event:Displaystheeventlogmessages.(Default)
n Debug:Displaysthedebuglogmessages.
n All:Displaysbotheventanddebuglogmessages.
severity <level> Specifiestheseveritylevelforthelogs.Thedifferentseverity
levelsareemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
filter <keyword> Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingterminalmonitor:
AOS-CX10.14.xxxxDiagnosticsandSupportabilityGuide|(8400SwitchSeries) 150

| switch# terminal-monitor |         |         |              |                     |
| ------------------------ | ------- | ------- | ------------ | ------------------- |
| Terminal-monitor         | is      | enabled | successfully |                     |
| switch# terminal-monitor |         |         | notify       | all                 |
| Terminal-monitor         | is      | enabled | successfully |                     |
| switch# terminal-monitor |         |         | notify       | event severity info |
| Terminal-monitor         | is      | enabled | successfully |                     |
| switch# terminal-monitor |         |         | filter       | lldp                |
| Terminal-monitor         | is      | enabled | successfully |                     |
| Command History          |         |         |              |                     |
| Release                  |         |         |              | Modification        |
| 10.07orearlier           |         |         |              | --                  |
| Command Information      |         |         |              |                     |
| Platforms                | Command | context |              | Authority           |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
TerminalMonitor|151

Troubleshooting Web UI and REST API Access Issues

Chapter 19

Troubleshooting Web UI and REST API Access Issues

The following section describes symptoms, causes and corrective actions for 401 or 404 errors.

HTTP 404 error when accessing the switch URL

Symptom

The switch is operational and you are using the correct URL for the switch, but attempts to access the
REST API or Web UI result in an HTTP 404 "Page not found" error.

Cause

REST API access is not enabled on the VRF that corresponds to the access port you are using. For
example, you are attempting to access the REST API or Web UI from the management (OOBM) port, and
access is not enabled on the mgmt VRF.

Action

Use the https-server vrf command to enable REST API access on the specified VRF.

For example:

switch(config)# https-server vrf mgmt

HTTP 401 error "Login failed: session limit reached"

Symptom

A REST request or Web UI login attempt returns response code 401 and the response body contains the
following text string:
Login failed: session limit reached

Cause

A user attempted to log into the REST API or the Web UI, but that user already has the maximum
number of concurrent sessions running.

Action

1. Log out from one of the existing sessions.

Browsers share a single session cookie across multiple tabs or even windows. However, scripts
that POST to the login resource and later do not POST to the logout resource can easily create the
maximum number of concurrent sessions.

2.

If the session cookie is lost and it is not possible to log out of the session, then wait for the session
idle time limit to expire.

When the session idle timeout expires, the session is terminated automatically.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

152

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions, Web UI sessions, and real-time notification subscriptions.

Troubleshooting Web UI and REST API Access Issues | 153

Chapter 20

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

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

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

HPE Aruba
Networking
Hardware

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

154

Documentation
and Translations
Portal

HPE Aruba
Networking
software

Software
licensing and
Feature Packs

End-of-Life
information

https://networkingsupport.hpe.com/downloads

https://lms.arubanetworks.com/

https://www.arubanetworks.com/support-services/end-of-life/

Accessing Updates

You can access updates from the HPE Aruba Networking Support Portal at
https://networkingsupport.hpe.com.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://networkingsupport.hpe./notifications/subscriptions (requires an active HPE Aruba Networking
Support Portal account to manage subscriptions). Security notices are viewable without an HPE Aruba
Networking Support Portal account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

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

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us
improve the documentation, send any errors, suggestions, or comments to Documentation Feedback
(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help

Support and Other Resources | 155

content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.14.xxxx Diagnostics and Supportability Guide | (8400 Switch Series)

156