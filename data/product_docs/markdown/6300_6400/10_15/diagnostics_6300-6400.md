| AOS-CX         |      | 10.15.xxxx |        |
| -------------- | ---- | ---------- | ------ |
| Diagnostics    |      |            | and    |
| Supportability |      |            | Guide  |
| 6300,          | 6400 | Switch     | Series |
Published:March2025
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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

3

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

| 4

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
|                                                   | debugdb                                            | 15  |
|                                                   | debugdestination                                   | 17  |
|                                                   | diagevent-trap-disable                             | 18  |
|                                                   | showdebug                                          | 19  |
|                                                   | showdebugbuffer                                    | 20  |
|                                                   | showdebugbuffervsf                                 | 21  |
|                                                   | showdebugdestination                               | 22  |
| Log Rotation                                      |                                                    | 24  |
| Logfilepaths                                      |                                                    | 24  |
| Aboutrotatedlogfiles                              |                                                    | 24  |
| Changingthesizeofthelogrotationfile               |                                                    | 24  |
| Changingthetimefrequencyforlogrotation            |                                                    | 25  |
| Resettingthetimefrequencytodaily                  |                                                    | 25  |
| Identifyingaremotehostforreceivingrotatedlogfiles |                                                    | 25  |
| Remotetransferofrotatedlogfiles                   |                                                    | 26  |
| Resettingtheremotehostforreceivingrotatedlogfiles |                                                    | 26  |
| Resettingthesizeofthelogrotationfile              |                                                    | 27  |
| Verifyingthelogrotationparameters                 |                                                    | 27  |
| Logrotationtroubleshooting                        |                                                    | 28  |
|                                                   | Logfilesnottransferredremotely                     | 28  |
|                                                   | Logrotationnotoccurringimmediatelyaftermaxfilesize | 28  |
|                                                   | Logrotationnotoccurringregardlessofperiod          | 28  |
| Logrotationcommands                               |                                                    | 29  |
|                                                   | loggingthreshold                                   | 29  |
|                                                   | logrotatemaxsize                                   | 32  |
|                                                   | logrotateperiod                                    | 32  |
|                                                   | logrotatetarget                                    | 33  |
|                                                   | showlogrotate                                      | 35  |
| Reboot                                            | reasons                                            | 36  |
| Event                                             | Logs                                               | 38  |
| Showingandclearingevents                          |                                                    | 38  |
| Client                                            | Filter                                             | 39  |
5
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Logmessages                            |                                                 |           | 39  |
| -------------------------------------- | ----------------------------------------------- | --------- | --- |
| Network                                | Configuration                                   | Validator | 40  |
| Showingandclearingevents               |                                                 |           | 40  |
| Networkconfigurationvalidationcommands |                                                 |           | 40  |
|                                        | switchconfig-validator                          |           | 40  |
| Cable Diagnostics                      |                                                 |           | 42  |
| HowTDRworksonAOS-CXplatforms           |                                                 |           | 42  |
| Cablediagnosticstests                  |                                                 |           | 42  |
| Cablediagnosticcommands                |                                                 |           | 43  |
|                                        | diagcable-diagnostic                            |           | 43  |
| Supportability                         | Copy                                            |           | 47  |
| TFTPVxLANSupport                       |                                                 |           | 47  |
| Supportabilitycopycommands             |                                                 |           | 47  |
|                                        | copycheckpoint                                  |           | 47  |
|                                        | copycommand-output                              |           | 48  |
|                                        | copycore-dump[<MEMBER/SLOT>]daemon              |           | 50  |
|                                        | copycore-dump[<MEMBER/SLOT>]kernel              |           | 51  |
|                                        | copycore-dump[<MEMBER/SLOT>]kernel<STORAGE-URL> |           | 52  |
|                                        | copycore-dumpvsfmemberdaemon                    |           | 53  |
|                                        | copycore-dumpvsfmemberkernel                    |           | 54  |
|                                        | copydiag-dumpfeature<FEATURE>                   |           | 55  |
|                                        | copydiag-dumplocal-file                         |           | 57  |
|                                        | copydiag-dumpvsfmemberlocal-file                |           | 58  |
|                                        | copy<IMAGE>                                     |           | 59  |
|                                        | copyrunning-config                              |           | 60  |
|                                        | copyshow-techfeature                            |           | 62  |
|                                        | copyshow-techlocal-file                         |           | 63  |
|                                        | copyshow-techvsfmemberlocal-file                |           | 64  |
|                                        | copystartup-config                              |           | 65  |
|                                        | copysupport-files                               |           | 66  |
|                                        | copysupport-fileslocal-file                     |           | 69  |
|                                        | copysupport-filesvsfmember                      |           | 70  |
|                                        | copysupport-log                                 |           | 72  |
|                                        | copysupport-logvsfmember                        |           | 73  |
| Traceroute                             |                                                 |           | 76  |
| Traceroutecommands                     |                                                 |           | 76  |
|                                        | traceroute                                      |           | 76  |
|                                        | traceroute6                                     |           | 79  |
| Ping                                   |                                                 |           | 82  |
| Pingcommands                           |                                                 |           | 82  |
|                                        | ping                                            |           | 82  |
|                                        | ping6                                           |           | 88  |
| Troubleshooting                        |                                                 |           | 91  |
|                                        | Operationnotpermitted                           |           | 91  |
|                                        | Networkisunreachable                            |           | 92  |
|                                        | Destinationhostunreachable                      |           | 92  |
Using classifier policies for traffic capture and analysis 94
| Stepone:createatrafficclass |     |     | 94  |
| --------------------------- | --- | --- | --- |
| Steptwo:createapolicy       |     |     | 95  |
|6

| Stepthree:applythepolicy                         |                                 | 95  |
| ------------------------------------------------ | ------------------------------- | --- |
| Stepfour:confirmpolicyInstallation               |                                 | 96  |
| Stepfive:confirmpolicyresourceconsumption        |                                 | 96  |
| Stepsix:configureamirrorsession                  |                                 | 97  |
| Stepseven:startpacketcapture                     |                                 | 97  |
| Stepeight:capturepacketstoafileormirrorittoahost |                                 | 98  |
| Stepnine:checkpackethitcounts                    |                                 | 98  |
|                                                  | showforwarding-info             | 100 |
| Remote                                           | syslog                          | 113 |
| SyslogoverVXLAN support                          |                                 | 113 |
| Remotesyslogcommands                             |                                 | 113 |
|                                                  | clearaccounting-logs            | 113 |
|                                                  | logging                         | 114 |
|                                                  | loggingaccounting-format-native | 117 |
|                                                  | loggingfilter                   | 118 |
|                                                  | loggingfacility                 | 121 |
|                                                  | loggingpersistent-storage       | 122 |
| Runtime                                          | Diagnostics                     | 124 |
| Runtimediagnosticcommands                        |                                 | 124 |
|                                                  | diagnosticmonitor               | 124 |
|                                                  | diagon-demand                   | 125 |
|                                                  | showdiagnostic                  | 127 |
|                                                  | showdiagnosticevents            | 132 |
| Service                                          | OS                              | 134 |
| ServiceOSCLIlogin                                |                                 | 134 |
| ServiceOSuseraccounts                            |                                 | 135 |
| ServiceOSbootmenu                                |                                 | 135 |
| Consoleconfiguration                             |                                 | 136 |
| AOS-CXboot                                       |                                 | 136 |
| Filesystemaccess                                 |                                 | 137 |
| ServiceOSmountfailure                            |                                 | 138 |
| ServiceOSCLIcommandlist                          |                                 | 138 |
| ServiceOSCLIfeaturesandlimitations               |                                 | 139 |
| ServiceOSCLIcommands                             |                                 | 139 |
|                                                  | boot                            | 139 |
|                                                  | cat                             | 140 |
|                                                  | cdpath                          | 141 |
|                                                  | config-clear                    | 142 |
|                                                  | cp                              | 142 |
|                                                  | du                              | 143 |
|                                                  | erasezeroize                    | 145 |
|                                                  | exit(svos)                      | 146 |
|                                                  | format                          | 147 |
|                                                  | identify                        | 148 |
|                                                  | ip                              | 148 |
|                                                  | ls                              | 149 |
|                                                  | md5sum                          | 151 |
|                                                  | mkdir                           | 152 |
|                                                  | mount                           | 153 |
|                                                  | mv                              | 154 |
|                                                  | password(svos)                  | 154 |
|                                                  | ping(svos)                      | 155 |
|                                                  | pwd                             | 156 |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 7

|                                               | reboot                                   |           |             |            |        | 157 |
| --------------------------------------------- | ---------------------------------------- | --------- | ----------- | ---------- | ------ | --- |
|                                               | rm                                       |           |             |            |        | 157 |
|                                               | rmdir                                    |           |             |            |        | 158 |
|                                               | secure-mode(ServiceOS)                   |           |             |            |        | 159 |
|                                               | sh                                       |           |             |            |        | 160 |
|                                               | systemserviceospassword-prompt           |           |             |            |        | 161 |
|                                               | umount                                   |           |             |            |        | 162 |
|                                               | update                                   |           |             |            |        | 162 |
|                                               | tftp                                     |           |             |            |        | 164 |
|                                               | version(ServiceOS)                       |           |             |            |        | 165 |
| In-System                                     | Programming                              |           |             |            |        | 166 |
| ShowtechcommandlistfortheISPfeature           |                                          |           |             |            |        | 166 |
| In-SystemProgrammingcommands                  |                                          |           |             |            |        | 166 |
|                                               | clearupdate-log                          |           |             |            |        | 166 |
|                                               | showneeded-updates                       |           |             |            |        | 166 |
| Selftest                                      |                                          |           |             |            |        | 168 |
| Selftestcommands                              |                                          |           |             |            |        | 168 |
|                                               | fastboot                                 |           |             |            |        | 168 |
|                                               | showselftest                             |           |             |            |        | 170 |
| Zeroization                                   |                                          |           |             |            |        | 174 |
| Zeroizationcommands                           |                                          |           |             |            |        | 174 |
|                                               | eraseallzeroize                          |           |             |            |        | 174 |
| Terminal                                      | Monitor                                  |           |             |            |        | 177 |
| Terminalmonitorcommands                       |                                          |           |             |            |        | 177 |
|                                               | loggingconsole{notify|severity|filter}   |           |             |            |        | 177 |
|                                               | showterminal-monitor                     |           |             |            |        | 178 |
|                                               | terminal-monitor{notify|severity|filter} |           |             |            |        | 179 |
| Troubleshooting                               |                                          | Web       | UI and REST | API Access | Issues | 181 |
| HTTP404errorwhenaccessingtheswitchURL         |                                          |           |             |            |        | 181 |
| HTTP401error"Loginfailed:sessionlimitreached" |                                          |           |             |            |        | 181 |
| Support                                       | and Other                                | Resources |             |            |        | 183 |
| AccessingHPEArubaNetworkingSupport            |                                          |           |             |            |        | 183 |
| AccessingUpdates                              |                                          |           |             |            |        | 184 |
| WarrantyInformation                           |                                          |           |             |            |        | 184 |
| RegulatoryInformation                         |                                          |           |             |            |        | 184 |
| DocumentationFeedback                         |                                          |           |             |            |        | 184 |
|8

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
S3L76A, S3L77A)

n HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,
R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

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

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

|

Vertical bar. A logical OR that separates multiple items from which you can

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

9

Convention

Usage

{ }

[ ]

… or

...

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

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

About this document | 10

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

| show | debug buffer |     |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------
2018-10-14:09:13:24.481407|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|Sysmon
| poll | interval | changed | to 51 |     |     |     |
| ---- | -------- | ------- | ----- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |         |              |     |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- | --- |
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
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
all
Enablesdebugloggingforallmodules.
<MODULE-NAME> Enablesdebugloggingforaspecificmodule.Foralistof
supportedmodules,enterthedebugcommandfollowedbya
spaceandaquestionmark(?).
<SUBMODULE-NAME> Enablesdebugloggingforaspecificsubmodule.Foralistof
supportedsubmodules,enterthedebug<MODULE-NAME>
commandfollowedbyaspaceandaquestionmark(?).
severity (emer|crit|alert|err| Selectstheminimumseverityloglevelforthedestination.Ifa
notice|warning|info|debug)
severityisnotprovided,thedefaultloglevelisdebug.Optional.
emer Specifiesstorageofdebuglogswithaseveritylevelofemergency
only.
Debuglogging|13

Parameter

Description

crit

alert

err

notice

warning

info

debug

port

vlan <VLAN-ID>

ip <IP-ADDRESS>

mac <MAC-ADDRESS>

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

Displays debug logs for the specified port, for example 1/1/1.

Displays debug logs for the specified VLAN. Provide a VLAN from 1
to 4094.

Displays debug logs for the specified IP Address.

Displays debug logs for the specified MAC Address, for example
A:B:C:D:E:F.

vrf <VRF-NAME>

Displays debug logs for the specified VRF.

instance <INSTANCE-ID>

Displays debug logs for the specified instance. Provide an instance
ID from 1 to 255.

Examples

switch# debug all

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

14

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

debug db
debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]

no debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]

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

Debug logging | 15

filter out logs on the basis of table, column, or client. It is helpful for debugging when the user wants to
debug an issue with a particular client, table, or column combination. It is not enabled by default. A
combination of filters can also be applied to filter out messages based on table, column, and client.

There are three submodules for the "db" module:

1. all: When All is enabled, no filters are applied to any of the debug logs, even if other submodules

are configured with filters.

2. tx: If enabled, only the replies and notifications sent out for the initial and incremental updates

are logged.

3. rx: If enabled, only the transactions sent to the configuration and state database server are

logged.

The keyword all may be used to enable or disable debug logging for all sub-modules. Also a
combination of filters can be used to filter the message types.

If the table or client filter is applied, then the messages belonging to this specific table or client will be
logged. The column filter can also be applied to further filter messages on a table, providing a
mechanism to filter messages on a column. The table and client filter can be used in combination or
separately, but column can only be used in conjunction with table.

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

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

16

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| debug destination |         |          |                   |           |
| ----------------- | ------- | -------- | ----------------- | --------- |
| debug destination | {syslog | | file | | console | buffer} | [severity |
(emer|crit|alert|err|notice|warning|info|debug)]
| no debug destination | {syslog | | file | | console} |     |
| -------------------- | ------- | ------ | ---------- | --- |
Description
Setsthedestinationfordebuglogsandtheminimumseveritylevelforeachdestination
Thenoformofthiscommandunsetsthedestinationfordebuglogs.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{syslog | file | console | buffer} Selectsthedestinationtostoredebuglogs.Required.
| syslog  |     |     | Specifiesthatthedebuglogsarestoredinthesyslog.    |     |
| ------- | --- | --- | ------------------------------------------------- | --- |
| file    |     |     | Specifiesthatdebuglogsarestoredinfile.            |     |
| console |     |     | Specifiesthatdebuglogsarestoredinconsole.         |     |
| buffer  |     |     | Specifiesthatdebuglogsarestoredinbuffer(default). |     |
severity (emer|crit|alert|err| Selectstheminimumseverityloglevelforthedestination.Ifa
notice|warning|info|debug)
severityisnotprovided,thedefaultloglevelisdebug.
Optional.
| emer |     |     | Specifiesstorageofdebuglogswithaseveritylevelof |     |
| ---- | --- | --- | ----------------------------------------------- | --- |
emergencyonly.
| crit |     |     | Specifiesstorageofdebuglogswithseveritylevelofcritical |     |
| ---- | --- | --- | ------------------------------------------------------ | --- |
andabove.
| alert |     |     | Specifiesstorageofdebuglogswithseveritylevelofalertand |     |
| ----- | --- | --- | ------------------------------------------------------ | --- |
above.
| err |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |     |
| --- | --- | --- | ------------------------------------------------------ | --- |
above.
notice
Specifiesstorageofdebuglogswithseveritylevelofnotice
andabove.
warning Specifiesstorageofdebuglogswithseveritylevelofwarning
andabove.
| info |     |     | Specifiesstorageofdebuglogswithseveritylevelofinfoand |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
Debuglogging|17

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
above.
| debug |     |     | Specifiesstorageofdebuglogswithseveritylevelofdebug |     |
| ----- | --- | --- | --------------------------------------------------- | --- |
(default).
Usage
Eventsthathaveaseverityequaltoorhigherthantheconfiguredseveritylevelarestoredinthe
designateddestination.Theproductdefaultstobufferfordestinationanddebugasaseveritylevel.
Examples
| switch# | debug destination | syslog  | severity | alert   |
| ------- | ----------------- | ------- | -------- | ------- |
| switch# | debug destination | console | severity | info    |
| switch# | debug destination | file    | severity | warning |
switch#
|     | debug destination | buffer | severity | err |
| --- | ----------------- | ------ | -------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
diag event-trap-disable
| diag event-trap-disable |                    | <EVENT-IDS> |     |     |
| ----------------------- | ------------------ | ----------- | --- | --- |
| no diag                 | event-trap-disable | <EVENT-IDS> |     |     |
Description
PreventsthespecificeventnotificationsfrombeingsentastrapstotheSNMPmanagementstations.
Thenoformofthiscommanddisablesthisfeatureandreenablesthenotificationofeventstobesent
astraps.
| Parameter   |     |     | Description                           |     |
| ----------- | --- | --- | ------------------------------------- | --- |
| <EVENT-IDS> |     |     | SpecifyuptofivecommaseparatedEventIDs |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 18

Usage
Tomodifythetrapstobedisabled,suchaschangingtheexistinglistofeventIDsorremovinganevent
IDfromtheblockedtraplist,firstcompletelyremovepreviouslyconfigureddisabledtrapsusingtheCLI
commandno diag event-trap-disable <EVENT-ID>.Afterthat,reconfiguretheneweventIDsorsetof
eventIDsforthechangestotakeeffect.
Examples
Disableandthenreenableeventtraps1223and1224.
| switch# | diagnostics                |     |           |
| ------- | -------------------------- | --- | --------- |
| switch# | diag event-trap-disable    |     | 1223,1224 |
| switch# | no diag event-trap-disable |     | 1223,1224 |
Changethelistofdisabledeventtraps.
| switch# | diagnostics                |     |           |
| ------- | -------------------------- | --- | --------- |
| switch# | diag event-trap-disable    |     | 1223,1224 |
| switch# | no diag event-trap-disable |     | 1223,1224 |
| switch# | diag event-trap-disable    |     | 1225,1226 |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command    | History     |         |              |
| ---------- | ----------- | ------- | ------------ |
| Release    |             |         | Modification |
| 10.15.1010 |             |         | --           |
| Command    | Information |         |              |
| Platforms  | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show debug
| show debug | [vsx-peer] |     |     |
| ---------- | ---------- | --- | --- |
Description
Displaystheenableddebugtypes.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Debuglogging|19

Examples
| switch# | show debug |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
-
| module | sub_module | severity vlan | port ip | mac | instance | vrf |
| ------ | ---------- | ------------- | ------- | --- | -------- | --- |
----------------------------------------------------------------------------------
-
| all | all | err 1 | 1/1/1 10.0.0.1 | 1a:2b:3c:4d:5e:6f | 2   |     |
| --- | --- | ----- | -------------- | ----------------- | --- | --- |
abcd
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show       | debug buffer |                       |            |     |     |     |
| ---------- | ------------ | --------------------- | ---------- | --- | --- | --- |
| show debug | buffer       | [module <MODULE-NAME> | | severity |     |     |     |
(emer|crit|alert|err|notice|warning|info|debug)]
Description
Displaysdebuglogsstoredinthespecifieddebugbufferwithoptionalfilteringbymoduleorseverity.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<MODULE-NAME> Filtersdebuglogsdisplayedbythespecifiedmodulename.
severity (emer|crit|alert|err| Displaysdebuglogswithaspecifiedseveritylevel.Defaults
notice|warning|info|debug)
todebug.Optional.
| emer |     |     | Displaysdebuglogswithaseveritylevelofemergencyonly. |     |     |     |
| ---- | --- | --- | --------------------------------------------------- | --- | --- | --- |
crit
Displaysdebuglogswithaseveritylevelofcriticalandabove.
| alert |     |     | Displaysdebuglogswithaseveritylevelofalertandabove. |     |     |     |
| ----- | --- | --- | --------------------------------------------------- | --- | --- | --- |
err
Specifiesstorageofdebuglogswithseverityleveloferrorand
above.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 20

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning
Displaysdebuglogswithaseveritylevelofwarningandabove.
| info |     |     | Displaysdebuglogswithaseveritylevelofinfoandabove. |
| ---- | --- | --- | -------------------------------------------------- |
debug
Displaysdebuglogswithaseveritylevelofdebug(default).
Examples
| switch# show | debug | buffer |     |
| ------------ | ----- | ------ | --- |
------------------------------------------------------------------------------
| show debug | buffer |     |     |
| ---------- | ------ | --- | --- |
------------------------------------------------------------------------------
2017-03-06:06:51:15.089967|hpe-sysmond|SYSMON|SYSMON_CONFIG|LOG_INFO|Sysmon poll
| interval | changed to | 20  |     |
| -------- | ---------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show debug | buffer | vsf |     |
| ---------- | ------ | --- | --- |
Applicablefor6300switchesonly.
show debug buffer vsf [member <MEMBER-ID>] [{conductor | standby}]
Description
DisplaysVSFmemberdebuglogsstoredinthedebugbuffer,withanoptiontofilterbyVSFmemberand
role.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MEMBER-ID> Displaysdebuglogsforthespecifiedmember-id.Optional.Range:
Debuglogging|21

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
1-10.
| conductor |     |     |     |     | DisplaydebuglogsfortheVSFconductor. |
| --------- | --- | --- | --- | --- | ----------------------------------- |
| standby   |     |     |     |     | DisplaydebuglogsfortheVSFstandby.   |
Examples
DisplayingVSFmemberdebuglogswithmember-id1:
| switch# | show | debug | buffer | vsf member | 1   |
| ------- | ---- | ----- | ------ | ---------- | --- |
------------------------------------------------------------------------------
| show | debug | buffer |     |     |     |
| ---- | ----- | ------ | --- | --- | --- |
------------------------------------------------------------------------------
2020-12-14:07:53:17.217919|hpe-ledarbd|LOG_DEBUG|MMBR|2|LED|LED|ledarbd_vsf_mbrs_
| check: | Checking |     | VSF_Member | table |     |
| ------ | -------- | --- | ---------- | ----- | --- |
DisplayingVSFmemberdebuglogsformemberstateconductor:
| switch# | show | debug | buffer | vsf conductor |     |
| ------- | ---- | ----- | ------ | ------------- | --- |
------------------------------------------------------------------------------
| show | debug | buffer |     |     |     |
| ---- | ----- | ------ | --- | --- | --- |
------------------------------------------------------------------------------
2020-12-14:07:54:20.469024|hpe-ledarbd|LOG_DEBUG|CDTR|1|LED|LED|ledarbd_pd_
| subsystems_check: |     |     | Checking | Subsystem | table |
| ----------------- | --- | --- | -------- | --------- | ----- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |         |     |                                           |
| -------------- | ----------- | ------- | ------- | --- | ----------------------------------------- |
| Release        |             |         |         |     | Modification                              |
| 10.09          |             |         |         |     | Updatedparameternameforinclusivelanguage. |
| 10.07orearlier |             |         |         |     | --                                        |
| Command        | Information |         |         |     |                                           |
| Platforms      |             | Command | context |     | Authority                                 |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show       | debug       | destination |            |     |     |
| ---------- | ----------- | ----------- | ---------- | --- | --- |
| show debug | destination |             | [vsx-peer] |     |     |
Description
Displaystheconfigureddebugdestinationandseverity.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 22

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# show | debug | destination |     |
| ------------ | ----- | ----------- | --- |
---------------------------------------------------------------------
| show debug | destination |     |     |
| ---------- | ----------- | --- | --- |
---------------------------------------------------------------------
CONSOLE:info
FILE:warning
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Debuglogging|23

Chapter 3
Log Rotation
Log Rotation
Logrotationprovidesyouwiththeabilitytosystematicallyrotateandarchiveanylogfilesproducedby
thesystem.Logrotationreduceslogspacerequiredontheswitch.Logrotationrotatesandcompresses
thelogfilesbasedonsizeand/orperiod.Rotatedlogfilesarestoredlocallyortransferredtoaremote
hostusingTFTP.
Startingfrom10.15.1010,notificationscanbeoptionallytriggeredifalogbufferpercentfullthresholdis
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
| n Securitylogsarestoredinfile |     | /var/log/security.log. |     |     |
| ----------------------------- | --- | ---------------------- | --- | --- |
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
24
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

Prerequisites

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

Log Rotation | 25

switch(config)#
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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 26

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
LogRotation|27

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

28

| Log rotation | commands |     |     |
| ------------ | -------- | --- | --- |
logging threshold
logging threshold {audit-log | auth-log | commands-log |event-log | security-log | https-
server-log} <THRESHOLD%>
no logging threshold {audit-log | auth-log | commands-log | event-log | security-log |
| https-server-log} | [<THRESHOLD%>] |     |     |
| ----------------- | -------------- | --- | --- |
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
| security-log     |     | Selectsthesecuritylog.    |     |
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
LogRotation|29

| switch(config)# | logging | threshold | auth-log 50 |     |
| --------------- | ------- | --------- | ----------- | --- |
Settingtheeventlogthreshold:
| switch(config)# | logging | threshold | event-log | 70  |
| --------------- | ------- | --------- | --------- | --- |
SettingtheHTTPSserverlogthreshold:
| switch(config)# | logging | threshold | https-server-log | 50  |
| --------------- | ------- | --------- | ---------------- | --- |
Settingthesecuritylogthreshold:
| switch(config)# | logging | threshold | security-log | 70  |
| --------------- | ------- | --------- | ------------ | --- |
Resettingtheauditlogthresholdtoitsdefaultof50:
| switch(config)# | no logging | threshold | audit-log |     |
| --------------- | ---------- | --------- | --------- | --- |
Resettingtheauthenticationlogthresholdtoitsdefaultof90:
| switch(config)# | no logging | threshold | auth-log |     |
| --------------- | ---------- | --------- | -------- | --- |
Resettingtheeventlogthresholdtoitsdefaultof90:
| switch(config)# | no logging | threshold | event-log |     |
| --------------- | ---------- | --------- | --------- | --- |
ResettingtheHTTPSserverlogthresholdtoitsdefaultof90:
switch(config)#
|     | no logging | threshold | https-server-log |     |
| --- | ---------- | --------- | ---------------- | --- |
Resettingthesecuritylogthresholdtoitsdefaultof90:
| switch(config)# | no logging | threshold | security-log |     |
| --------------- | ---------- | --------- | ------------ | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
Command History
| Release |     |     | Modification                        |     |
| ------- | --- | --- | ----------------------------------- | --- |
| 10.11   |     |     | Introducedthecommands-logparameter. |     |
| 10.09   |     |     | Commandintroduced.                  |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 30

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
LogRotation|31

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
| switch(config)# |     | no  | logrotate |     | maxsize |     |
| --------------- | --- | --- | --------- | --- | ------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logrotate    |        | period |     |        |           |           |
| ------------ | ------ | ------ | --- | ------ | --------- | --------- |
| logrotate    | period | {daily | |   | hourly | | monthly | | weekly} |
| no logrotate |        | period |     |        |           |           |
Description
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 32

Setsthelogfilerotationtimeperiod.Defaultstodaily.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappensfirst),
triggersrotationofthelogfile.
Thenoformofthiscommandresetsthelogrotationperiodtothedefaultofdaily.
| Parameter |     |     |     |     | Description                                  |
| --------- | --- | --- | --- | --- | -------------------------------------------- |
| daily     |     |     |     |     | Rotateslogfilesonadailybasis(default)at0:01. |
hourly
Rotateslogfileseveryhouratthefirstsecondofthehour.
monthly Rotateslogfilesmonthlyonthefirstdayofthemonthat00:01.
weekly
RotateslogfilesonceaweekonSundayat00:01.
Examples
Settingaweeklyperiod:
| switch(config)# |     |     | logrotate | period | weekly |
| --------------- | --- | --- | --------- | ------ | ------ |
Resettingtheperiodtoitsdefaultofdaily:
| switch(config)# |     |     | no logrotate | period |     |
| --------------- | --- | --- | ------------ | ------ | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |     |         |              |
| -------------- | ----------- | ------- | --- | ------- | ------------ |
| Release        |             |         |     |         | Modification |
| 10.07orearlier |             |         |     |         | --           |
| Command        | Information |         |     |         |              |
| Platforms      |             | Command |     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logrotate    |        | target |         |                  |     |
| ------------ | ------ | ------ | ------- | ---------------- | --- |
| logrotate    | target | <URI>  | [vrf    | <VRF_NAME>]      |     |
| no logrotate |        | target | [<URI>] | [vrf <VRF_NAME>] |     |
Description
UsingTFTP,sendstherotatedlogfilestoaspecifiedremotehostidentifiedbyUniversalResource
Identifier(URI).
LogRotation|33

The no form of this command resets the target to the default, which stores the rotated and compressed
log files locally in /var/log/.

Command context

Parameter

<URI>

<VRF_NAME>

Usage

Description

Specifies the URI of the remote host. The default directory is
local.
tftp://{{<IPV4_ADDR>|IPV6_ADDR>}|HOST}
[/<DIRECTORY>]

Specifies the VRF name (Default: default).

n Rotated log files are compressed and stored locally in the path /var/log/ regardless of the remote

host configuration.

Examples

Setting an IPv4 target:

switch(config)# logrotate target tftp://192.168.1.132

Setting an IPv4 target with a directory:

switch(config)# logrotate target tftp://192.168.1.132/logrotate/

Setting an IPv4 target with the default VRF:

switch(config)# logrotate target tftp://192.168.1.132 vrf mgmt

Setting an IPv6 target with the default VRF:

switch(config)# logrotate target tftp://2001:db8:0:1::128 vrf default

Resetting the target to local:

switch(config)# no logrotate target

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

34

| Release        |             |         | Modification                 |     |
| -------------- | ----------- | ------- | ---------------------------- | --- |
| 10.09          |             |         | Updatedthesyntaxandexamples. |     |
| 10.07orearlier |             |         | --                           |     |
| Command        | Information |         |                              |     |
| Platforms      | Command     | context | Authority                    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show logrotate
| show logrotate | [vsx-peer] |     |     |     |
| -------------- | ---------- | --- | --- | --- |
Description
Showsthelogrotateconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#   | show logrotate |                          |     |          |
| --------- | -------------- | ------------------------ | --- | -------- |
| Logrotate | configurations | :                        |     |          |
| Period    | :              | weekly                   |     |          |
| Maxsize   | :              | 20MB                     |     |          |
| Target    | :              | tftp://2001:db8:0:1::128 |     | vrf mgmt |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
LogRotation|35

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

VSF autojoin renumber

Reset triggered by VSF autojoin.

NOTE: VSF is not applicable for 6400 Switch
series.

VSF member renumbered

An user requested a renumber of a VSF member.

VSF switchover requested

An user requested a VSF switchover.

VSX software update

Reset triggered by a VSX software update.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

36

Parameter

Description

NOTE: Not applicable for 6300 Switch series.

Chassis critical temperature

Chassis operating temperature exceeded.

Chassis insufficient fans

Insufficient fans to cool the chassis.

Chassis unsupported PSUs/fans

Unsupported or misconfigured PSUs or system fans.

Management module critical temperature

Management module operating temperature exceeded.

Uncontrolled reboots

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

n Power down due to hibernation and wake-up due to RTC trigger

n Power down due to hibernation and wake-up due to Button Mode trigger

n Hardware thermal reset

Reboot reasons for line module

n Line module reboot

n Line module crashed

The line module is not applicable for 6300 Switch series.

Reboot reasons | 37

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

See the Security Guide for information about accounting logs.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

38

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

39

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
SeetheSecurityGuideforinformationaboutaccountinglogs.
| Network | configuration    |     | validation | commands |     |
| ------- | ---------------- | --- | ---------- | -------- | --- |
| switch  | config-validator |     |            |          |     |
switch config-validator [config <CONFIG-NAME>] [feature <feature>] [mode {consistency |
| vsx-sync}] | [format {cli | | json}] |     |     |     |
| ---------- | ------------ | -------- | --- | --- | --- |
modevsx-syncisnotsupportedontheHPEArubaNetworking6300Switchseries.
Description
Runsconfigurationvalidationtodetectconfigurationanomalies.
| Parameter |     |     | Description                                    |     |     |
| --------- | --- | --- | ---------------------------------------------- | --- | --- |
| config    |     |     | Specifiesconfigurationtobevalidated.Thedefault |     |     |
configurationisrunning-config.
| feature | <feature> |     | Specifiesthenameofthefeaturetobevalidated. |     |     |
| ------- | --------- | --- | ------------------------------------------ | --- | --- |
NOTE:Availablefeaturesvarybyswitchtype.TheHPEAruba
Networking6300Switchseriessupportsvsfasanoptionforthe
featureparameter,andthe6400SeriesSwitchsupportsvsxasan
optionforthefeatureparameter.
| mode |     |     | Specifiesconfigurationvalidationmode.Thedefaultis |     |     |
| ---- | --- | --- | ------------------------------------------------- | --- | --- |
40
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
consistency.
consistency Validatesfeatureconfigurationforconsistencycheck.
| vsx-sync |     |     | ValidatesVSX configurationsynchronizationbetweenVSX |     |
| -------- | --- | --- | --------------------------------------------------- | --- |
peersforVSXenabledfeatures.vsx-syncisnotsupported
ontheHPEArubaNetworking6300Switchseries.
| format |     |     | Specifiestheresultsdisplayformat.Thedefaultiscli. |     |
| ------ | --- | --- | ------------------------------------------------- | --- |
Examples
Runningconfigurationvalidationwithalldefaultvalues.(HPEArubaNetworking6300SwitchSeries)
| switch# | switch config-validator |     |     |     |
| ------- | ----------------------- | --- | --- | --- |
Line number 15: Split detect (MAD) is recommended for vsf stack.
Line number 18: VSF interface should be configured in the VSF link and the
| interface | should | be up. |     |     |
| --------- | ------ | ------ | --- | --- |
Line number 34: Configuration 'associate role <ROLE_NAME> is missing.
| Line number | 38: Configuration |     | 'enable' | is recommended. |
| ----------- | ----------------- | --- | -------- | --------------- |
| Line number | 43: Configuration |     | 'enable' | is recommended. |
Line number 45: A group (LLDP, CDP, MAC) should be associated with only one device
profile.
Runningconfigurationvalidationwithswitchesforthevsxfeature.(HPEArubaNetworking6400Switch
Series)
switch (config)# switch config-validator config running-config feature vsx
Line number 36: Configuration `system-mac <VSX_SYSTEM_MAC>` is recommended
Line number 36: Multi chassis configuration is recommended for VSX redundancy
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command   | History     |         |                    |     |
| --------- | ----------- | ------- | ------------------ | --- |
| Release   |             |         | Modification       |     |
| 10.10     |             |         | Commandintroduced. |     |
| Command   | Information |         |                    |     |
| Platforms | Command     | context | Authority          |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
NetworkConfigurationValidator|41

Chapter 8
Cable Diagnostics
Cable Diagnostics
TheTime-DomainReflectometer(TDR)featurehelpscharacterizeandlocatecablefaultsinanEthernet
cable.TDRinvolvesshowingareflectionatanyimpedancechangewithinthecablewhenalowvoltage
pulseissentintothecable.TDRmeasuresthetimebetweenreleaseandreturnofthelowvoltagepulse
fromanyreflections.Thedistancetothereflectioncanbecalculatedbymeasuringthetimeandthe
transmissionvelocityofthepulse.
TDRorCableDiagnosticsisaportfeaturesupportedonsomeswitchesrunningAOS-CXsoftware.TDRis
usedtodetectcablefaultsonthefollowingports:
Table1:Cablefaultdetectiononsupportedportstypes
|           |      | 5G-       | 10G-      |
| --------- | ---- | --------- | --------- |
| Platforms | 1GbT |           |           |
|           |      | SmartRate | SmartRate |
| 6300      | Yes  | Yes       | Yes       |
| 6400      | Yes  | Yes       | Yes       |
TDRorCableDiagnosticscanalsoberunfromtheAOS-CXAPI.
| How TDR | works | on AOS-CX | platforms |
| ------- | ----- | --------- | --------- |
TheimplementationofTDRinAOS-CXplatformsisdependentonthephysicallayerchips(PHYs)thatare
partofthefront-endnetworkportshardware.AOS-CXswitchesactivateTDRonthePHYwhenauser
entersthediag cable-diagnosticcommand.TheswitchwaitsforthereportaboutTDRmeasurements
fromthePHY.Theswitchthenreadstheresultsandreportsthevaluestotheuser.
| Cable diagnostics |     | tests |     |
| ----------------- | --- | ----- | --- |
Thecablediagnosticstestwillbringdownthelink,whichwilltakemoretimetocompletethetest.
TheTDRcablediagnostictestallowsanoperatortotesttwistedpaircablesforfaultswithoutphysically
disconnectingthecablesfromtheswitch.Ithelpsintroubleshootingconnectivityormonitoring
performanceononeormoreswitchports.
Thediag cable-diagnosticcommandcanbeusedtoruncablediagnostictestsanddisplaythetest
results.
Thefollowingtableprovidesthecablestatusmessagesandtheirdescriptions.
| Status |     | Meaning                                          |     |
| ------ | --- | ------------------------------------------------ | --- |
| good   |     | TheMDIpairisgood.                                |     |
| open   |     | TheMDIpairisnotterminatedwithalinkpartnerorhasan |     |
opencircuit.
42
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

Status

Meaning

intra-short

The MDI pair is shorted within itself.

inter_short

The MDI pair is shorted with another pair.

high_imp

low_imp

The MDI pair has high-impedance mismatch and is not
guaranteed to link up.

The MDI pair has low-impedance mismatch and is not
guaranteed to link up.

unknown

The MDI pair has failed the cable diagnostic test.

The following table provides the possible cable diagnostic failure reasons for port types.

Port Type

Reasons

1GbT

Interface is busy

5G-SmartRate

Interface is busy

10G-SmartRate

Interface is busy

The following table provides the cable length accuracy for port types.

Port Type

1GbT

5G-SmartRate

10G-SmartRate

Reasons

When diagnostic status is "good", cable length is
reported.

When diagnostic status is "good", cable length is
not reported.

When diagnostic status is "good", cable length is
not reported.

The following table provides the distance to fault accuracy for port types.

Port Type

1GbT

5G-SmartRate

10G-SmartRate

Reasons

When diagnostic status is not "good" or "failed", distance
to fault is reported within +/-10m.

When diagnostic status is not "good" or "failed", distance
to fault is reported within +/-5m.

When diagnostic status is not "good" or "failed", distance
to fault is reported within +/-5m.

Cable diagnostic commands

diag cable-diagnostic
diag cable-diagnostic

Cable Diagnostics | 43

test <IF-NAME>
show <IF-NAME>
clear <IF-NAME>
Description
Providesinformationaboutthecablehealthafterrunningadiagnostictestonaninterface.
Ifyourunanewcablediagnosticcommandwhenacablediagnosticisinprogressfortheinterface,the
newcablediagnosticcommandfailstoexecute.Insuchascenario,anerrormessageisdisplayed.
Onexecutingacablediagnostictestcommand,itautomaticallyclearstheoldtestresultsbeforethe
newteststarts.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
<IF-NAME>
Specifiesthenameoftheinterface.
| test <IF-NAME> |     | Runsacablediagnostictestonaninterface. |     |     |     |
| -------------- | --- | -------------------------------------- | --- | --- | --- |
show <IF-NAME>
Displaysthediagnostictestresultforaninterface.
clear <IF-NAME> Clearsthecablediagnostictestresultsforaninterface.
Examples
OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
Thefollowingexampledisplaysrunningacablediagnostictestoninterface1/3/1:
| switch# diag | cable-diagnostic | test 1/3/1 |     |     |     |
| ------------ | ---------------- | ---------- | --- | --- | --- |
This command will cause a loss of link on the port under test and will take
| several seconds | to complete. |     |     |     |     |
| --------------- | ------------ | --- | --- | --- | --- |
| Continue (y/n)? | y            |     |     |     |     |
Thefollowingexampledisplaystheerrormessageonexecutingacablediagnosticcommandwhilethe
currentdiagnostictestisinprogress:
| switch# diag | cable-diagnostic | test 1/3/1 |     |     |     |
| ------------ | ---------------- | ---------- | --- | --- | --- |
A cable diagnostic test for interface 1/3/1 is already in progress.
Thefollowingexampledisplaystheerrormessagewhencablediagnostictestisrequestedforan
unsupportedport:
| switch# diag     | cable-diagnostic | test 1/3/1   |                  |     |     |
| ---------------- | ---------------- | ------------ | ---------------- | --- | --- |
| Cable diagnostic | is not           | supported on | interface 1/3/1. |     |     |
Thefollowingexamplesdisplaythecablediagnostictestresultfor1GbTinterface:
| switch# diag | cable-diagnostic | show 1/3/1 |           |           |      |
| ------------ | ---------------- | ---------- | --------- | --------- | ---- |
|              |                  | Cable      | Impedance | Distance* | MDI  |
| Interface    | Pinout           | Status     | (Ohms)    | (Meters)  | Mode |
--------------------------------------------------------------------
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 44

| 1/3/1  | 1-2 | good |     |     | 85-115 |     | 10 +/- 10 | mdi |
| ------ | --- | ---- | --- | --- | ------ | --- | --------- | --- |
| (1GbT) | 3-6 | good |     |     | 85-115 |     | 10 +/- 10 | mdi |
|        | 4-5 | good |     |     | 85-115 |     | 5 +/- 10  | mdi |
|        | 7-8 | good |     |     | 85-115 |     | 3 +/- 10  | mdi |
* Full cable length for good cables or distance to fault for faulty cables.
| Cable status | legend (1GbT): |             |     |     |     |     |     |     |
| ------------ | -------------- | ----------- | --- | --- | --- | --- | --- | --- |
| Cable        | Impedance      |             |     |     |     |     |     |     |
| Status       | (Ohms)         | Description |     |     |     |     |     |     |
----------------------------------------------------------------
| good        | 85-115 | No    | cable     | faults       | found        |               |           |     |
| ----------- | ------ | ----- | --------- | ------------ | ------------ | ------------- | --------- | --- |
| open        | >115   | Open  | circuit   |              | detected     |               |           |     |
| intra-short | <85    | Short | circuit   |              | within the   | same          | wire pair |     |
| inter-short | <85    | Short | circuit   |              | with another | wire          | pair      |     |
| high-imp    | >115   | Cable | impedance |              | higher       | than          | expected  |     |
| low-imp     | <85    | Cable | impedance |              | lower        | than expected |           |     |
| unknown     | --     | Cable | test      | inconclusive |              |               |           |     |
Thefollowingexamplesdisplaythecablediagnostictestresultfor5G-SmartRateinterface:
switch#
| diag      | cable-diagnostic |        | show | 1/1/20 |           |           |     |      |
| --------- | ---------------- | ------ | ---- | ------ | --------- | --------- | --- | ---- |
|           |                  | Cable  |      |        | Impedance | Distance* |     | MDI  |
| Interface | Pinout           | Status |      |        | (Ohms)    | (Meters)  |     | Mode |
--------------------------------------------------------------------
| 1/1/20         | 1-2 | good     |     |     | 85-115 |     | --      | mdi |
| -------------- | --- | -------- | --- | --- | ------ | --- | ------- | --- |
| (5G-SmartRate) | 3-6 | open     |     |     | >300   |     | 4 +/- 5 | mdi |
|                | 4-5 | open     |     |     | >300   |     | 4 +/- 5 | mdi |
|                | 7-8 | high-imp |     |     | >115   |     | 3 +/- 5 | mdi |
* Full cable length for good cables or distance to fault for faulty cables.
| Cable status | legend (5G-SmartRate): |             |     |     |     |     |     |     |
| ------------ | ---------------------- | ----------- | --- | --- | --- | --- | --- | --- |
| Cable        | Impedance              |             |     |     |     |     |     |     |
| Status       | (Ohms)                 | Description |     |     |     |     |     |     |
----------------------------------------------------------------
| good        | 85-115 | No    | cable     | faults       | found        |               |           |     |
| ----------- | ------ | ----- | --------- | ------------ | ------------ | ------------- | --------- | --- |
| open        | >300   | Open  | circuit   |              | detected     |               |           |     |
| intra-short | <30    | Short | circuit   |              | within the   | same          | wire pair |     |
| inter-short | <30    | Short | circuit   |              | with another | wire          | pair      |     |
| high-imp    | >115   | Cable | impedance |              | higher       | than          | expected  |     |
| low-imp     | <85    | Cable | impedance |              | lower        | than expected |           |     |
| unknown     | --     | Cable | test      | inconclusive |              |               |           |     |
Thefollowingexampledisplaystheerrormessagewhenyouexecuteacablediagnosticcommandwhile
thecurrentdiagnostictestisinprogress:
| switch# diag | cable-diagnostic |     | show | 1/3/1 |     |     |     |     |
| ------------ | ---------------- | --- | ---- | ----- | --- | --- | --- | --- |
A cable diagnostic test for interface 1/3/1 is currently in progress.
Thefollowingexampledisplaystheerrormessagewhencablediagnostictestresultisnotavailable:
CableDiagnostics|45

| switch# diag | cable-diagnostic | show | 1/3/1 |
| ------------ | ---------------- | ---- | ----- |
Cable diagnostic test results for interface 1/3/1 are not available.
Thefollowingexampleclearsthecablediagnostictestresultsforthespecifiedinterface:
| switch# diag | cable-diagnostic | clear | 1/3/1 |
| ------------ | ---------------- | ----- | ----- |
Thefollowingexampledisplaystheerrormessagewhenyouexecuteacablediagnosticcommandwhile
thecurrentdiagnostictestisinprogress:
| switch# diag | cable-diagnostic | clear | 1/3/1 |
| ------------ | ---------------- | ----- | ----- |
A cable diagnostic test for interface 1/3/1 is currently in progress.
Runningacablediagnostictestwillresultinabriefinterruptioninconnectivityonalltestedports.
IfagoodcableisusedontheSmartRateports,theDistancetoFault(Meters)valueis0.
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.11               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 46

Chapter 9

Supportability Copy

Supportability Copy

To effectively diagnose various issues arising at the switch, different types of data are copied out using
copy commands for further analysis.

Use the copy core-dump command to copy the core-dump of a daemon crash.

Use the copy show-tech command to capture the status of the feature.

If there is feature misbehavior, use the copy support-files feature command to copy all feature related
information for further analysis. Additionally use copy support-log and copy diag-dump to copy
information that helps to analyze the internal behavior of a feature/daemon.

Use copy command-output to copy any show command's output to remote destinations or USB
storage.

These files can be copied to a remote destination using sftp/tftp, additionally they can also be stored in
the USB storage.

TFTP VxLAN Support

TFTP is supported over VxLAN tunnels with IPv4 or IPv6 underlay.

TFTP over VxLAN tunnels with IPv6 underlay is only supported on the HPE Aruba Networking 8100 and 8360

Switch Series.

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

47

Description
CopiesthecheckpointusingTFTP,SFTP,SCP,orUSB.
| Parameter         |     |     | Description                 |
| ----------------- | --- | --- | --------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesthecheckpointname. |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Syntax:
{usb}:/<FILE>
<REMOTE-URL>
SpecifiestheURLtocopythecommandoutput.
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
Examples
CopyingcheckpointchpttoaremoteURL:
switch# copy checkpoint chpt scp://root@10.0.1.1/config vrf mgmt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
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
copy command-output
copy command-output "<COMMAND>" {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}
Description
CopiesthespecifiedcommandoutputusingTFTP,SFTP,SCP,USB,orlocal.
SupportabilityCopy|48

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<COMMAND> Specifiesthecommandfromwhichyouwanttoobtainitsoutput.
Required.Userswithauditorrightscanspecifythesetwo
commandsonly:
showaccountinglog
showevents
{<STORAGE-URL> | <REMOTE-URL> SelecteitherthestorageURLortheremoteURLforthe
[vrf <VRF-NAME>]} destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     | SpecifiestheUSBtocopycommandoutput. |     |
| ------------- | --- | ----------------------------------- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     | SpecifiestheURLtocopythecommandoutput. |     |
| ------------ | --- | -------------------------------------- | --- |
Syntax:
|     |     | n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE> |     |
| --- | --- | ---------------------------------------------------------- | --- |
|     |     | n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>     |     |
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
| switch# copy | command-output | "show events" | usb:/events |
| ------------ | -------------- | ------------- | ----------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History |     |                   |     |
| --------------- | --- | ----------------- | --- |
| Release         |     | Modification      |     |
| 10.08           |     | AddedSCP support. |     |
| 10.07orearlier  |     | --                |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 49

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this
command from the auditor context (auditor>) only.

copy core-dump [<MEMBER/SLOT>] daemon
copy core-dump [<MEMBER/SLOT>] daemon <DAEMON-NAME>[:<INSTANCE-ID>] <REMOTE-URL> [vrf
<VRF-NAME>]

Description

Copies the core-dump from the specified daemon using TFTP, SFTP, SCP, or USB.

Parameter

<MEMBER/SLOT>

<DAEMON-NAME>

[:<INSTANCE-ID>]

<REMOTE_URL>

vrf <VRF-NAME>

Examples

Description

Specifies the slot ID on an 8400 or 6400 switch. Required.
Syntax: Slot number for line (1/1-1/4, 1/7-1/10) MM(1/5 or 1/6)

Specifies the name of the daemon. Required.

Specifies the instance of the daemon core dump. Optional.

Specifies the remote destination URL. Required. The syntax of the
URL is the following:
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. If no VRF name is provided, the VRF
named default is used. Optional.

Copying the core dump from daemon ops-vland to a remote URL with a VRF named mgmt:

switch# copy core-dump daemon ops-vland sftp://abc@10.0.14.211/vland_coredump.xz
vrf mgmt

Copying the core dump from daemon ops-vland to a remote URL with a VRF named mgmt:

switch# copy core-dump daemon ops-vland scp://abc@10.0.14.211/vland_coredump.xz
vrf mgmt

Copying the core dump from daemon ops-switchd to a USB drive:

switch# copy core-dump daemon ops-switchd usb:/switchd

Copying the core dump with slot ID 1/1 from daemon hpe-sysmond to a remote URL:

Supportability Copy | 50

switch# copy core-dump 1/1 daemon hpe-sysmond sftp://abc@10.0.14.206/core.hpe-
| sysmond.xz | vrf mgmt |     |     |     |
| ---------- | -------- | --- | --- | --- |
Copyingthecoredumpfromthehpe-configprocesstoaUSBdrive:
| switch# copy | core-dump | daemon hpe-config |     | usb:/config_core |
| ------------ | --------- | ----------------- | --- | ---------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | AddedSCP support. |     |
| 10.07orearlier      |         |         | --                |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
6400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy core-dump | [<MEMBER/SLOT>] |     |     | kernel |
| -------------- | --------------- | --- | --- | ------ |
copy core-dump [<MEMBER/SLOT>] kernel <REMOTE-URL> [vrf <VRF-NAME>]
Description
CopiesakernelcoredumpusingTFTP,SFTP,orSCP.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<MEMBER/SLOT>
SpecifiestheslotIDonan8400or6400switch.Required.
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput.Required. |     |
| ------------ | --- | --- | ----------------------------------------------- | --- |
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthekernelcoredumptotheURL:
switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 51

CopyingthekernelcoredumptotheURLwiththeVRFnamedmgmt:
switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz vrf mgmt
CopyingthekernelcoredumpfromslotID1/1totheURLwiththeVRFnamedmgmt:
switch# copy core-dump 1/1 kernel sftp://abc@10.0.14.206/kernel_dump.tar.gz vrf
mgmt
CopyingthekernelcoredumpfromslotID1/1totheURLwiththeVRFnamedmgmt:
switch# copy core-dump 1/1 kernel scp://abc@10.0.14.206/kernel_dump.tar.gz vrf
mgmt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | AddedSCP support. |     |
| 10.07orearlier      |         |         | --                |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
6400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
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
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput.Required. |     |
| ------------- | --- | --- | -------------------------------------------- | --- |
Syntax:{usb]:/<FILE>
Examples
CopyingthekernelcoredumptoaUSBdrive:
SupportabilityCopy|52

| switch# | copy core-dump | kernel usb:/kernel.tar.gz |     |
| ------- | -------------- | ------------------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy core-dump |     | vsf member | daemon |
| -------------- | --- | ---------- | ------ |
Applicablefor6300switchesonly.
| copy core-dump | vsf            | member <MEMBER-ID>             |     |
| -------------- | -------------- | ------------------------------ | --- |
| daemon         | [<DAEMON-NAME> | | <DAEMON-NAME>:<INSTANCE-ID>] |     |
| <REMOTE-URL>   | [vrf           | <VRF-NAME>]                    |     |
| copy core-dump | vsf            | member <MEMBER-ID>             |     |
| daemon         | [<DAEMON-NAME> | | <DAEMON-NAME>:<INSTANCE-ID>] |     |
<STORAGE-URL>
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,USB,orlocal.
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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 53

Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch#                          | copy core-dump | vsf member | 1 daemon hpe-sysmond |
| -------------------------------- | -------------- | ---------- | -------------------- |
| sftp://abc@10.0.14.206/sysmon.xz |                |            | vrf mgmt             |
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch#                          | copy core-dump | vsf member | 2 daemon hpe-sysmond |
| -------------------------------- | -------------- | ---------- | -------------------- |
| scp://user@10.0.14.206/sysmon.xz |                |            | vrf mgmt             |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy core-dump |     | vsf member | kernel |
| -------------- | --- | ---------- | ------ |
Applicablefor6300switchesonly.
copy core-dump vsf member <MEMBER-ID> kernel <REMOTE-URL> [vrf <VRF-NAME>]
| copy core-dump | vsf | member <MEMBER-ID> | kernel <STORAGE-URL> |
| -------------- | --- | ------------------ | -------------------- |
Description
Copiesthekernelcore-dumpusingTFTP,SFTP,SCP,USB,orlocal.
| Parameter   |     |     | Description                                   |
| ----------- | --- | --- | --------------------------------------------- |
| <MEMBER-ID> |     |     | Specifiesthemember-idoftheVSFmember.Required. |
<REMOTE_URL>
SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRF
nameddefaultisused.Optional.
SupportabilityCopy|54

| Parameter     |     |     | Description                                  |
| ------------- | --- | --- | -------------------------------------------- |
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput.Required. |
Syntax:{usb}:/<FILE>
Examples
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel sftp://abc@10.0.14.206/kernel.tar.gz
vrf mgmt
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel scp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy diag-dump | feature | <FEATURE> |     |
| -------------- | ------- | --------- | --- |
copy diag-dump feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesthespecifieddiagnosticinformationusingTFTP,SFTP,SCP,USB,orlocal.
Parameter Description
<FEATURE> Thenameofafeature,forexampleaaaor
vrrp.Required.
{<REMOTE-URL> [vrf <VRF-NAME> |<STORAGE-URL>]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopied
commandoutput.Required.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 55

Parameter Description
<REMOTE-URL> SpecifiestheremotedestinationURL.
Required.ThesyntaxoftheURListhe
following:
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}
[:<PORT>]/<FILE>
vrf <VRF-NAME>
SpecifiestheVRFname.IfnoVRFnameis
provided,theVRFnameddefaultisused.
Optional.
<STORAGE-URL> SpecifiestheUSBtocopycommandoutput.
Required.
Syntax:{usb}:/<FILE>
Examples
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa tftp://10.100.0.12/diagdump.txt vrf mgmt
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa scp://user@10.100.0.12/diagdump.txt vrf mgmt
CopyingtheoutputfromthevrrpfeaturetoaUSBdrive:
switch#
|     | copy diag-dump | feature | vrrp usb:/diagdump.txt |
| --- | -------------- | ------- | ---------------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |                   |
| -------------- | ----------- | ------- | ----------------- |
| Release        |             |         | Modification      |
| 10.08          |             |         | AddedSCP support. |
| 10.07orearlier |             |         | --                |
| Command        | Information |         |                   |
| Platforms      | Command     | context | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
SupportabilityCopy|56

copy diag-dump local-file
copy diag-dump local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies the diagnostic information stored in a local file using TFTP, SFTP, SCP, USB, or local.

Parameter

Description

{<REMOTE-URL> [vrf <VRF-NAME>] |<STORAGE-URL>}

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

Usage

Select either the storage URL or the remote
URL for the destination of the copied
command output. Required.

Specifies the URL to copy the command
output.
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}

[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF name
is default. Optional.

Specifies the USB to copy command output.
Syntax: {usb}:/<FILE>

The copy diag-dump local-file command can be used only after the information is captured. Run the
diag-dump <FEATURE-NAME> basic local-file command before you enter the copy diag-dump local-
file command to capture the diagnostic information for the specified feature into the local file.

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

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

57

| Command        | History     |         |                   |     |
| -------------- | ----------- | ------- | ----------------- | --- |
| Release        |             |         | Modification      |     |
| 10.08          |             |         | AddedSCP support. |     |
| 10.07orearlier |             |         | --                |     |
| Command        | Information |         |                   |     |
| Platforms      | Command     | context | Authority         |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy diag-dump | vsf | member | local-file |     |
| -------------- | --- | ------ | ---------- | --- |
Applicablefor6300switchesonly.
copy diag-dump vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] |
<STORAGE-URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,USB,orlocal.
| Parameter  |             |     |     | Description                          |
| ---------- | ----------- | --- | --- | ------------------------------------ |
| vsf member | <MEMBER-ID> |     |     | Specifiesthemember-idoftheVSFmember. |
Required.
{<REMOTE-URL> [vrf <VRF-NAME>] |<STORAGE-URL>} SelecteitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommand |
| ------------ | --- | --- | --- | ------------------------------- |
output.
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}
[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.ThedefaultVRFname |
| -------------- | --- | --- | --- | ------------------------------------- |
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
SupportabilityCopy|58

| switch# diag-dump | aaa | basic local-file |     |
| ----------------- | --- | ---------------- | --- |
switch#
copy diag-dump vsf member 2 local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# diag-dump | aaa | basic local-file |     |
| ----------------- | --- | ---------------- | --- |
switch# copy diag-dump vsf member 2 local-file tftp://10.100.0.12/diagdump.txt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <IMAGE>
copy <IMAGE> {<STORAGE-URL> | <REMOTE-URL>} <FILE-NAME> [vrf <VRF-NAME>]
Description
CopiestheimageusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IMAGE>
Specifiestheimage.
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
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
| <FILE-NAME> |     |     | Specifiesthefilename. |
| ----------- | --- | --- | --------------------- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 59

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingtheimagetoaremoteURL:
| switch# copy | scp://root@20.0.1.1/primary.swi |     |     | primary vrf | mgmt |
| ------------ | ------------------------------- | --- | --- | ----------- | ---- |
CopyingthesecondaryimagetoaremoteURL:
switch# copy secondary scp://root@20.0.1.1/primary.swi vrf mgmt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
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
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Syntax:
{usb}:/<FILE>
<REMOTE-URL>
SpecifiestheURLtocopythecommandoutput.
SupportabilityCopy|60

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     | Specifiestherunningconfiguration. |
| -------------------- | --- | --- | --------------------------------- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
overwrite Theconfigurationisonlyappliedtotherunningconfigurationifall
commandssucceedwithouterrors.
Usage
Bydefault,theCLIconfigurationcontainedintheremotefileisappliedontopoftherunning
configuration,andalltheCLIcommandsinthefileareappliedline-by-line.IfaparticularCLIcommand
fails,thefailureisloggedintheeventlogandthenextlineintheCLIconfigurationisprocessed.
Whenusingtheoptionaloverwriteparameter,theconfigurationisonlyappliedtorunning
configurationifallthecommandssucceededwithouterrors.Iferrorsarepresent,theexistingrunning-
configwillremainintact.Youcantheninspecttheeventlogstocheckandfixtheerrorsandretrythe
operation.Ifmorethan20errorsarepresent,theoperationstopsprocessinganyfurthercommands,
andwilldisplaytheerrorsatthatpointintheeventlogs.Formoreinformationonthisfeature,referto
thevideoontheHPEArubaNetworkingAirheadsBroadcastingChannel.
Examples
CopyingtherunningconfigurationtoaremoteURL:
switch# copy running-config scp://root@10.0.1.1/config cli vrf mgmt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                                    |
| ------------------- | ------- | ------- | ---------------------------------- |
| Release             |         |         | Modification                       |
| 10.15               |         |         | Theoverwriteparameterisintroduced. |
| 10.08               |         |         | AddedSCP support.                  |
| 10.07orearlier      |         |         | --                                 |
| Command Information |         |         |                                    |
| Platforms           | Command | context | Authority                          |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 61

copy show-tech feature
copy show-tech feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}

Description

Copies show tech output using TFTP, SFTP, SCP, USB, or local.

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

n {sftp:// | scp:// <USER>@}{<IP> |

<HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF
name is default. Optional.

Specifies the USB to copy command output.
Required.
Syntax: {usb}:/<FILE>

Example

Copying show tech output of the aaa feature using SCP:

switch# copy show-tech feature aaa scp://user@10.0.0.12/file.txt vrf mgmt

Copying show tech output of the config feature using SFTP on the mgmt VRF:

switch# copy show-tech feature config sftp://root@10.0.0.1/tech.txt vrf mgmt

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

--

Command Information

Supportability Copy | 62

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

Before entering the copy show-tech local-file command, run the show tech command with the local-
file parameter for the specified feature.

Examples

Copying the output to a remote URL:

switch# copy show-tech local-file tftp://10.100.0.12/file.txt

Copying the output to a remote URL:

switch# copy show-tech local-file scp://user@10.100.0.12/file.txt

Copying the output to a remote URL with a VRF:

switch# copy show-tech local-file tftp://10.100.0.12/file.txt vrf mgmt

Copying the output to a USB:

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

63

| switch# | copy show-tech | local-file | usb:/file |     |     |
| ------- | -------------- | ---------- | --------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |                   |     |     |
| -------------- | ----------- | ------- | ----------------- | --- | --- |
| Release        |             |         | Modification      |     |     |
| 10.08          |             |         | AddedSCP support. |     |     |
| 10.07orearlier |             |         | --                |     |     |
| Command        | Information |         |                   |     |     |
| Platforms      | Command     | context | Authority         |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy show-tech |     | vsf member | local-file |     |     |
| -------------- | --- | ---------- | ---------- | --- | --- |
Applicablefor6300switchesonly.
copy show-tech vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] |
<STORAGE-URL>}
Description
Copiesshowtechoutputstoredinalocalfile.
| Parameter  |             |     |     |     | Description                   |
| ---------- | ----------- | --- | --- | --- | ----------------------------- |
| vsf member | <MEMBER-ID> |     |     |     | Specifiesthemember-idoftheVSF |
member.Required.
| {<REMOTE-URL> | [vrf | <VRF-NAME>] | | <STORAGE-URL> | ]}  |     |
| ------------- | ---- | ----------- | --------------- | --- | --- |
SelecteithertheremoteURLorthe
storageURLforthedestinationofthe
copiedcommandoutput.Required.
| <REMOTE-URL> |     |     |     |     | SpecifiestheURLtocopythecommand |
| ------------ | --- | --- | --- | --- | ------------------------------- |
output.
Syntax:
|     |     |     |     |     | n {tftp://}{<IP>|<HOST>}[:<PORT>] |
| --- | --- | --- | --- | --- | --------------------------------- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     |     | n {sftp://|scp://<USER>@}{<IP>| |
| --- | --- | --- | --- | --- | ------------------------------- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     |     | SpecifiestheVRFname.ThedefaultVRF |
| -------------- | --- | --- | --- | --- | --------------------------------- |
nameisdefault.Optional.
<STORAGE-URL>
SpecifiestheUSBtocopycommand
output.
Syntax:{usb}:/<FILE>
SupportabilityCopy|64

Usage
Beforeenteringthecopy local-filecommand,runtheshow techcommandwiththe
show-tech
local-fileparameterforthespecifiedfeature.
Examples
CopyingtheoutputtoaremoteURLwithaVRF:
switch# copy show-tech vsf member 2 local-file tftp://10.100.0.12/showtech.txt vrf
mgmt
CopyingtheoutputtoaUSB:
| switch# copy | show-tech | vsf member | 2 local-file | usb:/file |
| ------------ | --------- | ---------- | ------------ | --------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | AddedSCP support. |     |
| 10.07orearlier      |         |         | --                |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy startup-config
copy startup-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |
| ------------- | --- | --- | ----------------------------------- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |
| ------------ | --- | --- | -------------------------------------- | --- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 65

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>][;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|<HOST>}[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     |     |     | Specifiesthestartupconfiguration. |
| -------------------- | --- | --- | --- | --- | --------------------------------- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthestartupconfigurationtoaremoteURL:
switch# copy startup-config scp://root@10.0.1.1/config json vrf mgmt
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |     |         |     |                   |
| -------------- | ----------- | --- | ------- | --- | ----------------- |
| Release        |             |     |         |     | Modification      |
| 10.08          |             |     |         |     | AddedSCP support. |
| 10.07orearlier |             |     |         |     | --                |
| Command        | Information |     |         |     |                   |
| Platforms      | Command     |     | context |     | Authority         |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy support-files
copy support-files
| <REMOTE-URL> | [vrf | <VRF-NAME>] |     |     |     |
| ------------ | ---- | ----------- | --- | --- | --- |
<STORAGE-URL>
| all <REMOTE-URL> |     | [vrf | <VRF-NAME>] |     |     |
| ---------------- | --- | ---- | ----------- | --- | --- |
all <STORAGE-URL>
| feature       | <FEATURE-NAME> |               | <STORAGE-URL> |                  |     |
| ------------- | -------------- | ------------- | ------------- | ---------------- | --- |
| previous-boot |                | <REMOTE-URL>  |               | [vrf <VRF-NAME>] |     |
| previous-boot |                | <STORAGE-URL> |               |                  |     |
Forthe6400switchonly:
| module <SLOT-ID> |              | <REMOTE-URL>  |                  | [vrf | <VRF-NAME>] |
| ---------------- | ------------ | ------------- | ---------------- | ---- | ----------- |
| module <SLOT-ID> |              | <STORAGE-URL> |                  |      |             |
| standby          | <REMOTE-URL> |               | [vrf <VRF-NAME>] |      |             |
Forthe6300switchonly:
| vsf member | <MEMBER-ID> |     | <REMOTE-URL>  |     | {vrf <VRF-NAME>} |
| ---------- | ----------- | --- | ------------- | --- | ---------------- |
| vsf member | <MEMBER-ID> |     | <STORAGE-URL> |     |                  |
SupportabilityCopy|66

Description

Copies a set of support files to a compressed file in tar.gz format using TFTP, SFTP, SCP, or USB or to a
directory over SFTP, USB, or local.

Do not press Control + Z at the password prompt while copying support files, as this will prevent the console

from executing other commands.

This command does not support TFTP transfer on 6300 switches.

Parameter

<FEATURE-NAME>

{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]}

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

<MEMBER-ID>

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

The member ID in the VSF stack. Range 1-
10.

Specifies the slot ID on 6400 switches.
Optional.
Syntax: Slot number for line (1/1-1/4, 1/7-
1/10) MM(1/5 or 1/6)

If feature name is not provided, the command collects generic system-specific support information. If a
feature name is provided, the command collects feature-specific support information.

In order to collect data from standby and member in a VSF stack, the command will prompt for the local user

password once.

In order to collect data from the standby 6400 swtich, the command will prompt for the local user password

once.

Examples

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

67

CopyingthesupportfilestoaremoteURL:
| switch# copy | support-files | tftp://10.100.0.12/file.tar.gz |     |
| ------------ | ------------- | ------------------------------ | --- |
CopyingthesupportfilesofthelldpfeaturetoaremoteURLwithaspecifiedVRF:
switch# copy support-files feature lldp tftp://10.100.0.12/file.tar.gz vrf mgmt
CopyingthesupportfilesfromthepreviousboottoaremoteURLwithaspecifiedVRF:
switch#
copy support-files previous-boot scp://user@10.0.14.206/file.tar.gz vrf
mgmt
CopyingthesupportfilestoaUSB:
| switch# copy | support-files | usb:/file.tar.gz |     |
| ------------ | ------------- | ---------------- | --- |
CopyingthefilesfromamoduletoaremoteURLwithaspecifiedVRFonan8400or6400switch:
switch# copy support-files module 1/1 tftp://10.100.0.12/file.tar.gz vrf mgmt
CopyingthefilesfromastandbymoduletoaremoteURLwithaspecifiedVRFonan8400or6400
switch:
switch# copy support-files standby sftp://root@10.0.14.216/file.tar.gz vrf mgmt
CopyingallthesupportfilestoaremoteURL:
switch#
copy support-files all sftp://root@10.0.14.216/file.tar.gz vrf mgmt
CopyingthesupportfilesoftheconfigfeaturetoaUSB:
| switch# copy | support-files | feature config | usb:/file.tar.gz |
| ------------ | ------------- | -------------- | ---------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |     |                   |     |
| ------------------- | --- | ----------------- | --- |
| Release             |     | Modification      |     |
| 10.08               |     | AddedSCP support. |     |
| 10.07orearlier      |     | --                |     |
| Command Information |     |                   |     |
SupportabilityCopy|68

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy support-files |     | local-file |     |     |
| ------------------ | --- | ---------- | --- | --- |
copy support-files [feature <FEATURE-NAME> | previous-boot | all | module <SLOT-ID> |
standby | vsf member <MEMBER-ID>] local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-
URL>}
Themoduleandstandbyaresupportedonlyon6400switch.Thevsfmemberissupportedonlyon6300switch.
Description
Storesasetofsupportfilesasacompressedfileintheswitchlocallyandcopiesthepreservedsupport
filestoadirectoryusingTFTP,SFTP,SCP,USB,orlocal..Youcanstoreonlyonecopyofthesupportfile
locally.Whenyoustoreanewsupportfile,itoverwritestheexistingsupportfile
DonotpressControl+Zatthepasswordpromptwhilecopyingsupportfiles,asthiswillpreventtheconsole
fromexecutingothercommands.
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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 69

The operation to copy all support files could take a while to complete.
| Do you want  | to continue   | (y/n)?  |                     |
| ------------ | ------------- | ------- | ------------------- |
| switch# copy | support-files | module  | 1/1 local-file      |
| switch# copy | support-files | standby | local-file          |
| switch# copy | support-files | vsf     | member 7 local-file |
CopyinglocalsupportfiletoaremoteURLandstorageURL:
switch# copy support-files local-file usb:/support_files_dir_path/
switch# copy support-files local-file scp://root@10.0.14.206//support_files_dir_
| path/abc.tar.gz | vrf | mgmt |     |
| --------------- | --- | ---- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy support-files |     | vsf member |     |
| ------------------ | --- | ---------- | --- |
Applicablefor6300switchesonly.
copy support-files vsf member <MEMBER-ID> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesasetofsupportfilesusingTFTP,SFTP,SCP,USB,orlocal.
DonotpressControl+Zatthepasswordpromptwhilecopyingsupportfiles,asthiswillpreventtheconsole
fromexecutingothercommands.
Parameter Description
<MEMBER-ID>
Specifiedthemember-idoftheVSFmember.
Required.
{<REMOTE-URL> [vrf <VRF-NAME> | <STORAGE-URL>]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopied
commandoutput.Required.
<REMOTE-URL> SpecifiestheURLtocopythecommand
SupportabilityCopy|70

Parameter Description
output.
Syntax:
n {tftp://}{<IP>|<HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://|scp://<USER>@}{<IP>|
<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRF
nameisdefault.Optional.
<STORAGE-URL> SpecifiestheUSBtocopycommandoutput.
Syntax:{usb}:/<FILE>
Usage
Iffeaturenameisnotprovided,thecommandcollectsgenericsystem-specificsupportinformation.Ifa
featurenameisprovided,thecommandcollectsfeature-specificsupportinformation.
Examples
CopyingthesupportfilestoaUSB:
| switch# copy | support-files | vsf member | 2 usb:/file.tar.gz |
| ------------ | ------------- | ---------- | ------------------ |
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch# copy support-files vsf member 2 scp://user@10.100.0.12/file.tar.gz/ vrf
mgmt
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch# copy support-files vsf member 2 sftp://user@10.100.0.12/support_files_dir_
| path/ vrf | mgmt |     |     |
| --------- | ---- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |     |                   |     |
| ------------------- | --- | ----------------- | --- |
| Release             |     | Modification      |     |
| 10.08               |     | AddedSCP support. |     |
| 10.07orearlier      |     | --                |     |
| Command Information |     |                   |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 71

Platforms

Command context

Authority

6300

Manager (#)

Administrators or local user group members with execution
rights for this command.

copy support-log
copy support-log <DAEMON-NAME> [<MEMBER/SLOT>] {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-
NAME>]}

Description

Copies the specified support log for a daemon TFTP, SFTP, SCP, USB, or local.

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

Supportability Copy | 72

switch# copy support-log fand scp://user@10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log hpe-fand tftp://10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaUSB:
| switch# copy | support-log | hpe-fand | usb:/support-log |
| ------------ | ----------- | -------- | ---------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| copy support-log |     | vsf member |     |
| ---------------- | --- | ---------- | --- |
Applicablefor6300switchesonly.
copy support-log vsf member <MEMBER-ID> <DAEMON-NAME> {<STORAGE-URL> | <REMOTE-URL> [vrf
<VRF-NAME>]}
Description
CopiesthespecifiedsupportlogforadaemonusingTFTP,SFTP,SCP,USB,orlocal.
Parameter Description
<MEMBER-ID>
Specifiesthemember-idoftheVSFmember.
Required.
<DAEMON-NAME> Specifiesthenameofthedaemon.Required.
{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]} SelectseitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
<STORAGE-URL> SpecifiestheUSBtocopycommandoutput.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 73

Parameter

<REMOTE-URL>

vrf <VRF-NAME>

Usage

Description

Syntax: {usb}:/<FILE>

Specifies the URL to copy the command
output.
Syntax:

n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}

[:<PORT>]/<FILE>

Specifies the VRF name. If no VRF name is
provided, the VRF named default is used.
Optional.

Fast log is a high performance, per-daemon binary logging infrastructure used to debug daemon level
issues by precisely capturing the per daemon/module/functionalities debug traces in real time. Fast log,
also referred to as support logs, helps users to understand the feature internals and its specific
happenings. The fast logs from one daemon are not overwritten by other daemon logs because fast
logs are captured as part of a daemon core dump. Fast logs are enabled by default.

Examples

Copying the support log from the daemon hpe-fand to a remote URL with a VRF named mgmt:

switch# copy support-log vsf member 2 hpe-fand tftp://10.100.0.12/file vrf mgmt

Copying the support log from the daemon hpe-fand to a remote URL with a VRF named mgmt:

switch# copy support-log vsf member 2 hpe-fand scp://user@10.100.0.12/file vrf
mgmt

Copying the support log from the daemon hpe-fand to a USB:

switch# copy support-log vsf member 2 hpe-fand usb:/support-log

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

--

Command Information

Supportability Copy | 74

Platforms

Command context

Authority

6300

Manager (#)

Administrators or local user group members with execution
rights for this command.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

75

Chapter 10
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
76
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

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
Traceroute|77

| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms | 0.002ms |
| ------- | ---------- | --------- | --- | ------- | ------- |
| switch# | traceroute | 10.0.10.1 |     | probes  | 2       |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 2
probes
| 1       | 10.0.40.2  | 0.002ms   |     | 0.002ms |     |
| ------- | ---------- | --------- | --- | ------- | --- |
| 2       | 10.0.30.1  | 0.002ms   |     | 0.001ms |     |
| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms |     |
| switch# | traceroute | 10.0.10.1 |     | timeout | 5   |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 5 sec. timeout, 3
probes
| 1       | 10.0.40.2  | 0.002ms   |     | 0.002ms | 0.001ms |
| ------- | ---------- | --------- | --- | ------- | ------- |
| 2       | 10.0.30.1  | 0.002ms   |     | 0.001ms | 0.001ms |
| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms | 0.002ms |
| switch# | traceroute | localhost |     | vrf     | red     |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1   | 127.0.0.1 | 0.003ms |     | 0.002ms | 0.001ms |
| --- | --------- | ------- | --- | ------- | ------- |
switch#
|     | traceroute | localhost |     | mgmt |     |
| --- | ---------- | --------- | --- | ---- | --- |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1   | 127.0.0.1 | 0.018ms |     | 0.006ms | 0.003ms |
| --- | --------- | ------- | --- | ------- | ------- |
switch# traceroute 10.0.10.1 maxttl 20 timeout 5 minttl 1 probes 3 dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1   | 10.0.40.2 | 0.002ms |     | 0.002ms | 0.001ms |
| --- | --------- | ------- | --- | ------- | ------- |
| 2   | 10.0.30.1 | 0.002ms |     | 0.001ms | 0.001ms |
| 3   | 10.0.10.1 | 0.001ms |     | 0.002ms | 0.002ms |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1   | 10.0.40.2 | 0.002ms |     | 0.002ms | 0.001ms |
| --- | --------- | ------- | --- | ------- | ------- |
| 2   | 10.0.30.1 | 0.002ms |     | 0.001ms | 0.001ms |
| 3   | 10.0.10.1 | 0.001ms |     | 0.002ms | 0.002ms |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2 maxttl 20
| timeout | 5 minttl | 1 probes |     | 3 dstport | 33434 |
| ------- | -------- | -------- | --- | --------- | ----- |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1          | 10.0.40.2  | 0.002ms  |             | 0.002ms | 0.001ms     |
| ---------- | ---------- | -------- | ----------- | ------- | ----------- |
| 2          | 10.0.30.1  | 0.002ms  |             | 0.001ms | 0.001ms     |
| 3          | 10.0.10.1  | 0.001ms  |             | 0.002ms | 0.002ms     |
| switch#    | traceroute | 10.0.0.2 |             | source  | 10.0.0.1    |
| traceroute | to         | 10.0.0.2 | (10.0.0.2), |         | 30 hops max |
| 1          | 10.0.0.2   | 0.299ms  | 0.155ms     |         | 0.115ms     |
| switch#    | traceroute | 10.0.0.2 |             | source  | 1/1/1       |
| traceroute | to         | 10.0.0.2 | (10.0.0.2), |         | 30 hops max |
| 1          | 10.0.0.2   | 0.479ms  | 0.222ms     |         | 0.171ms     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command | History |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 78

| Release |     |     | Modification |                     |           |      |
| ------- | --- | --- | ------------ | ------------------- | --------- | ---- |
| 10.08   |     |     | Addedsource  | IP addressandsource | interface | name |
parameters.
| 10.07orearlier |             |         | --        |     |     |     |
| -------------- | ----------- | ------- | --------- | --- | --- | --- |
| Command        | Information |         |           |     |     |     |
| Platforms      | Command     | context | Authority |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
traceroute6
traceroute6 {<IPV6-ADDR> | <HOSTNAME>} [dstport <NUMBER> | maxttl <NUMBER> | probes
<NUMBER> | timeout <TIME>] [vrf <VRF-NAME>] source {<IPV6-ADDR> | <IFNAME>}
Description
UsestracerouteforthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.
| Parameter    |             |     | Description                                  |     |     |     |
| ------------ | ----------- | --- | -------------------------------------------- | --- | --- | --- |
| IPv6-address | <IPV6-ADDR> |     | SpecifiestheIPv6address.                     |     |     |     |
| hostname     |             |     | Specifiesthehostnameofthedevicetotraceroute. |     |     |     |
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
maxttl <NUMBER> Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
| probes <NUMBER> |     |     | Specifiesthenumberofprobes,<1-5>.Default:3 |     |     |     |
| --------------- | --- | --- | ------------------------------------------ | --- | --- | --- |
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse,<VRF-
NAME>.
source {<IPV6-ADDR> | <IFNAME>} SpecifiesthesourceIPv6addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
Protocol(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashop
limit,isusedindeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
Examples
Traceroute|79

| switch# | traceroute6 | 0:0::0:1 |     |     |     |     |
| ------- | ----------- | -------- | --- | --- | --- | --- |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
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
| probes,   | 24 byte   | packets |     |        |     |           |
| --------- | --------- | ------- | --- | ------ | --- | --------- |
| 1 2001::2 | (2001::2) | 0.6145  | ms  | 0.4165 | ms  | 0.1620 ms |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 80

| Release |     |     | Modification                               |
| ------- | --- | --- | ------------------------------------------ |
| 10.08   |     |     | AddedsourceIPaddressandsourceinterfacename |
parameters.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Traceroute|81

Chapter 11

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

82

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
Ping|83

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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 84

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
Ping|85

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

86

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
Ping|87

| PING 192.168.1.8     |              | (192.168.1.8) |                           |            | 2000(2028) |        | bytes of data. |        |
| -------------------- | ------------ | ------------- | ------------------------- | ---------- | ---------- | ------ | -------------- | ------ |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=1 |            | ttl=64 | time=0.721     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=2 |            | ttl=64 | time=0.792     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=3 |            | ttl=64 | time=0.857     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=4 |            | ttl=64 | time=0.833     | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=5 |            | ttl=64 | time=0.836     | ms     |
| --- 192.168.1.8      |              | ping          | statistics                |            | ---        |        |                |        |
| 5 packets            | transmitted, |               | 5 received,               |            | 0%         | packet | loss, time     | 4056ms |
| rtt min/avg/max/mdev |              |               | = 0.721/0.807/0.857/0.048 |            |            |        | ms             |        |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |     |         |     |              |     |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- |
| Release        |             |     |         |     | Modification |     |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |     |
| Command        | Information |     |         |     |              |     |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
ping6
ping6 {<IPv6-ADDR> | <HOSTNAME>} [data-fill <PATTERN> | datagram-size <SIZE> |
interval <TIME> | repetitions <NUMBER> | timeout <TIME> | vrrp <VRID> |
| vrf <VRF-NAME> |     | | source | <IPv6-ADDR> |     | |   | <IFNAME>] |     |     |
| -------------- | --- | -------- | ----------- | --- | --- | --------- | --- | --- |
Description
PingsthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.TheVRRPoptionis
providedtoself-pingtheconfiguredlink-localaddressontheVRRPgroup.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
IPv6-ADDR
SelectstheIPv6addresstoping.
| HOSTNAME  |           |     |     |     | Selectsthehostnametoping.Range:1-256characters |     |     |     |
| --------- | --------- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| data-fill | <PATTERN> |     |     |     |                                                |     |     |     |
Specifiesthedatapatterninhexadecimaldigitstosend.A
maximumof16"pad"bytescanbespecifiedtofillouttheICMP
packet.Default:AB
datagram-size <SIZE> Specifiesthepingdatagramsize.Range:0-65399,default:100.
interval <TIME> Specifiestheintervalbetweensuccessivepingrequestsin
seconds.Range:1-60seconds,default:1second.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 88

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
repetitions <NUMBER> Specifiesthenumberofpacketstosend.Range:1-10000packets,
default:Fivepackets.
timeout <TIME>
Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
| vrrp <VRID> |     |     |     |     | SpecifiestheVRRPgroupID. |     |     |
| ----------- | --- | --- | --- | --- | ------------------------ | --- | --- |
vrf <VRF-NAME>
Specifiesthevirtualroutingandforwarding(VRF)touse.When
thisoptionisnotprovided,thedefaultVRFisused.
source <IPv6-ADDR> | <IFNAME> SpecifiesthesourceIPv6addressorinterfacetouse.
Examples
PinginganIPv6address:
| switch#               | ping6 2020::2   |     |                         |       |           |            |             |
| --------------------- | --------------- | --- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PING 2020::2(2020::2) |                 | 100 | data                    | bytes |           |            |             |
| 108 bytes             | from 2020::2:   |     | icmp_seq=1              |       | ttl=64    | time=0.386 | ms          |
| 108 bytes             | from 2020::2:   |     | icmp_seq=2              |       | ttl=64    | time=0.235 | ms          |
| 108 bytes             | from 2020::2:   |     | icmp_seq=3              |       | ttl=64    | time=0.249 | ms          |
| 108 bytes             | from 2020::2:   |     | icmp_seq=4              |       | ttl=64    | time=0.240 | ms          |
| 108 bytes             | from 2020::2:   |     | icmp_seq=5              |       | ttl=64    | time=0.252 | ms          |
| --- 2020::2           | ping statistics |     | ---                     |       |           |            |             |
| 5 packets             | transmitted,    |     | 5 received,             |       | 0% packet | loss,      | time 4000ms |
| rtt min/avg/max/mdev  |                 | =   | 0.235/0.272/0.386/0.059 |       |           | ms         |             |
Pingingthelocalhost:
| switch#                   | ping6 localhost |            |                         |      |           |            |             |
| ------------------------- | --------------- | ---------- | ----------------------- | ---- | --------- | ---------- | ----------- |
| PING localhost(localhost) |                 |            | 100                     | data | bytes     |            |             |
| 108 bytes                 | from localhost: |            | icmp_seq=1              |      | ttl=64    | time=0.093 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=2              |      | ttl=64    | time=0.051 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=3              |      | ttl=64    | time=0.055 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=4              |      | ttl=64    | time=0.046 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=5              |      | ttl=64    | time=0.048 | ms          |
| --- localhost             | ping            | statistics |                         | ---  |           |            |             |
| 5 packets                 | transmitted,    |            | 5 received,             |      | 0% packet | loss,      | time 3998ms |
| rtt min/avg/max/mdev      |                 | =          | 0.046/0.058/0.093/0.019 |      |           | ms         |             |
Pingingaserverwithadatapattern:
| switch#               | ping6 2020::2   | data-fill |            | ab    |        |            |     |
| --------------------- | --------------- | --------- | ---------- | ----- | ------ | ---------- | --- |
| PATTERN:              | 0xab            |           |            |       |        |            |     |
| PING 2020::2(2020::2) |                 | 100       | data       | bytes |        |            |     |
| 108 bytes             | from 2020::2:   |           | icmp_seq=1 |       | ttl=64 | time=0.038 | ms  |
| 108 bytes             | from 2020::2:   |           | icmp_seq=2 |       | ttl=64 | time=0.074 | ms  |
| 108 bytes             | from 2020::2:   |           | icmp_seq=3 |       | ttl=64 | time=0.076 | ms  |
| 108 bytes             | from 2020::2:   |           | icmp_seq=4 |       | ttl=64 | time=0.075 | ms  |
| 108 bytes             | from 2020::2:   |           | icmp_seq=5 |       | ttl=64 | time=0.077 | ms  |
| --- 2020::2           | ping statistics |           | ---        |       |        |            |     |
Ping|89

| 5 packets            | transmitted, |     | 5 received,             |     | 0% packet | loss, | time 3999ms |
| -------------------- | ------------ | --- | ----------------------- | --- | --------- | ----- | ----------- |
| rtt min/avg/max/mdev |              | =   | 0.038/0.068/0.077/0.015 |     |           | ms    |             |
Pingingaserverwithadatagramsize:
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
| switch#                   | ping6 localhost |     | vrf        | red  |        |            |     |
| ------------------------- | --------------- | --- | ---------- | ---- | ------ | ---------- | --- |
| PING localhost(localhost) |                 |     | 100        | data | bytes  |            |     |
| 108 bytes                 | from localhost: |     | icmp_seq=1 |      | ttl=64 | time=0.038 | ms  |
| 108 bytes                 | from localhost: |     | icmp_seq=2 |      | ttl=64 | time=0.050 | ms  |
| 108 bytes                 | from localhost: |     | icmp_seq=3 |      | ttl=64 | time=0.039 | ms  |
| 108 bytes                 | from localhost: |     | icmp_seq=4 |      | ttl=64 | time=0.040 | ms  |
| 108 bytes                 | from localhost: |     | icmp_seq=5 |      | ttl=64 | time=0.027 | ms  |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 90

| --- localhost        |              | ping | statistics | ---                     |           |            |        |
| -------------------- | ------------ | ---- | ---------- | ----------------------- | --------- | ---------- | ------ |
| 5 packets            | transmitted, |      |            | 5 received,             | 0% packet | loss, time | 4001ms |
| rtt min/avg/max/mdev |              |      | =          | 0.027/0.038/0.050/0.010 |           | ms         |        |
PingingthelocalhostwiththedefaultVRF:
| switch#                   | ping6        | localhost  |            | vrf mgmt                |           |            |        |
| ------------------------- | ------------ | ---------- | ---------- | ----------------------- | --------- | ---------- | ------ |
| PING localhost(localhost) |              |            |            | 100 data                | bytes     |            |        |
| 108 bytes                 | from         | localhost: |            | icmp_seq=1              | ttl=64    | time=0.032 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=2              | ttl=64    | time=0.022 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=3              | ttl=64    | time=0.040 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=4              | ttl=64    | time=0.022 | ms     |
| 108 bytes                 | from         | localhost: |            | icmp_seq=5              | ttl=64    | time=0.046 | ms     |
| --- localhost             |              | ping       | statistics | ---                     |           |            |        |
| 5 packets                 | transmitted, |            |            | 5 received,             | 0% packet | loss, time | 3998ms |
| rtt min/avg/max/mdev      |              |            | =          | 0.022/0.032/0.046/0.010 |           | ms         |        |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |         |     |              |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |         |     | Modification |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
Troubleshooting
| Operation | not | permitted |     |     |     |     |     |
| --------- | --- | --------- | --- | --- | --- | --- | --- |
Symptom
Theswitchdisplaysanoperation not permittedmessagewhenauserattemptstosendaping
request.
Example:
| switch#         | ping | 100.1.2.10   |     |               |       |         |     |
| --------------- | ---- | ------------ | --- | ------------- | ----- | ------- | --- |
| PING 100.1.2.10 |      | (100.1.2.10) |     | 100(128)      | bytes | of data |     |
| ping: sendmsg:  |      | Operation    |     | not permitted |       |         |     |
| ping: sendmsg:  |      | Operation    |     | not permitted |       |         |     |
| ping: sendmsg:  |      | Operation    |     | not permitted |       |         |     |
Ping|91

ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted

--- 100.1.2.10 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 4000ms

Cause

When an ACL is applied to the Control Plane, sending a ping request may be denied. If the ping packet
matches a drop entry in the ACL, applying a Control Plane may block traffic sent from the switch CLI ping
command.

When this situation occurs, the following error message is displayed: ping: sendmsg: Operation not
permitted. The message indicates that the ICMP echo request packet has not been sent and is blocked
by the Control Plane ACL.

When this message is not displayed, the ping request packet has been sent correctly. A ping failure in
this case represents a failure to receive the ICMP echo reply packet.

Action

1. Modify the ACL to allow the ping traffic.

2. Unapply the ACL from egress (8400/8320/8325/9300/9300S switches) or Control Plane.

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

92

Action

Investigate whether an intermediate hop is not returning pings by using the traceroute command.
Check the intermediate hop, and then the endpoint. If the destination is another HPE Aruba Networking
switch, it is possible that Ingress ACLs on that switch are blocking ping packets. In such cases, the
configuration option on the destination switch should be examined.

Ping | 93

Chapter 12
|                  |          |             | Using   | classifier   | policies | for traffic |
| ---------------- | -------- | ----------- | ------- | ------------ | -------- | ----------- |
| Using classifier | policies | for traffic | capture | and analysis |          |             |
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
| Step one: | create | a traffic | class |     |     |     |
| --------- | ------ | --------- | ----- | --- | --- | --- |
Thefollowingexamplecreatesatrafficclasstomatchtraffictobemirroredforfutureevaluation.Inthis
example:
n TCPandUDPprotocolsshouldincludeentriesforbothsourceanddestinationportmatchesinorder
tomirrortrafficeithertoorfromthatportnumber.
n HPEArubaNetworkingCentraltrafficutilizesHTTPSandthereforewillmatchthatentry.
n Inthisexample,thecountkeywordisincludedsothathitcountscanbemonitoredtoverifythat
trafficismatchingtheclassentries.
n Thelastentry(ignore any any any count)isincludedtocountpacketsofallothertraffictypes
passingthroughthedevice,andtoconfirmothertrafficisreachingthepolicyforevaluation,andnot
beingmirrored.
Sequencenumbers(forexample,10,20,30)arenotmandatorywhencreatingclassentries,andwill
n
beauto-generatedifnotmanuallyspecified.
n Commentlinesareoptionalforfunctionalitybutincludedforclarity.
| switch(config)# | class        | ip support-mirror |       |     |     |     |
| --------------- | ------------ | ----------------- | ----- | --- | --- | --- |
| 10 comment      | OSPF         | protocol          |       |     |     |     |
| 10 match        | ospf any     | any count         |       |     |     |     |
| 20 comment      | GRE protocol |                   |       |     |     |     |
| 20 match        | gre any      | any count         |       |     |     |     |
| 30 comment      | BGP dst      | port              |       |     |     |     |
| 30 match        | tcp any      | any eq bgp count  |       |     |     |     |
| 40 comment      | BGP src      | port              |       |     |     |     |
| 40 match        | tcp any      | eq bgp any count  |       |     |     |     |
| 50 comment      | VxLAN        | dst port          |       |     |     |     |
| 50 match        | udp any      | any eq vxlan      | count |     |     |     |
| 60 comment      | VxLAN        | src port          |       |     |     |     |
94
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

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

Using classifier policies for traffic capture and analysis | 95

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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 96

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
|     |     |     |     |     |     | Usingclassifier | policiesfortrafficcaptureandanalysis|97 |
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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 98

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

Using classifier policies for traffic capture and analysis | 99

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
| 0 130 match  | icmp any | any icmp-type | echo       | count |
| 5 140 match  | icmp any | any icmp-type | echo-reply | count |
| 0 150 ignore | any any  | any count     |            |       |
show forwarding-info
show forwarding-info mac ingress-interface <IFNAME> source-mac-address <MAC-ADDR>
destination-mac-address <MAC-ADDR> [vlan <VLAN-ID>] [timeout <TIMEOUT>]
| [ethertype <ETHERTYPE>] |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
show forwarding-info mac-ip ingress-interface <IFNAME> source-mac-address <MAC-ADDR>
| destination-mac-address |     | <MAC-ADDR> |     |     |
| ----------------------- | --- | ---------- | --- | --- |
{source-ip-address <IP-ADDR> destination-ip-address <IP-ADDR>] |
source-ipv6-address <IPV6-ADDR> destination-ipv6-address <IPV6-ADDR>}
| [vlan <VLAN-ID>]     | [transport-protocol |                      | <TR-PROT-NUM>] |              |
| -------------------- | ------------------- | -------------------- | -------------- | ------------ |
| [source-l4-port      | <L4-PORT>           | destination-l4-port  |                | <L4-PORT>]   |
| [vrf <VRF-NAME>]     | [timeout            | <TIMEOUT>][ethertype |                | <ETHERTYPE>] |
| show forwarding-info | ip                  |                      |                |              |
{source-ip-address <IP-ADDR> destination-ip-address <IP-ADDR>] |
source-ipv6-address <IPV6-ADDR> destination-ipV6-address <IPV6-ADDR>}
| [ingress-interface | <IFNAME>][transport-protocol |                     |     | <TR-PROT-NUM>] |
| ------------------ | ---------------------------- | ------------------- | --- | -------------- |
| [source-l4-port    | <L4-PORT>                    | destination-l4-port |     | <L4-PORT>]     |
| [vrf <VRF-NAME>]   | [timeout                     | <TIMEOUT>]          |     |                |
Description
Showstheforwardinginformationbasedoncurrentsystemconfigurationsandhardwarestatesfor
forwardinglookups.Giventheuserpacketinformation,thiscommandshowstheegressphysical
interfaceofthepacket.L3hashmodeandL4hashmodearesupportedforLAG.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ingress-interface <IFNAME> Specifiestheingressinterface(forexample:1/1/1).
source-mac-address <MAC-ADDR> SpecifiesthesourceMAC address.Format:
AA:BB:CC:DD:EE:FF.
| destination-mac-address | <MAC-ADDR> |     |     |     |
| ----------------------- | ---------- | --- | --- | --- |
SpecifiesthedestinationMAC address.Format:
AA:BB:CC:DD:EE:FF.
vlan <VLAN-ID>
SpecifiestheegressVLAN.Default1.Range:1to4094.
timeout <TIMEOUT> Specifiestheresponsetimeoutinseconds.Default:3.
Range:1to60.
ethertype <ETHERTYPE>
(For6300/6400and8360Switchseries)Specifythe
ethertypevaluetodeterminetheegressinterface.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 100

Parameter

Description

source-ip-address <IP-ADDR>

Specifies the source IPv4 address. Format: A.B.C.D

destination-ip-address <IP-ADDR>]

Specifies the destination IPv4 address. Format: A.B.C.D

source-ipv6-address <IPV6-ADDR>

Specifies the source IPv6 address. Format: X:X::X:X

destination-ipv6-address <IPV6-ADDR>

Specifies the destination IPv6 address. Format: X:X::X:X

transport-protocol <TR-PROT-NUM>

Specifies the transport protocol number. Range 1 to 255.
For example, use 6 for TCP, 17 for UDP, 1 for ICMP, 2 for
IGMP.

source-l4-port <L4-PORT>

Specifies the L4 source port. Range 1 to 65535.

destination-l4-port <L4-PORT>

Specifies the L4 destination port. Range 1 to 65535.

vrf <VRF-NAME>

Specifies the egress VRF name. Default: default.

Usage

The following limitations need to be considered:

n The forwarding-information feature is not applicable for broadcast, multicast, and unknown packets.

n Sub-interfaces and tunnel interfaces (VXLAN and MPLS) in both ingress and egress are not

supported. However, in AOS-CX 10.15.1000, VXLAN is supported as an egress interface on 6300 and
8360 switches.

It is recommended to use only the mac-ip option of the forwarding info command in VXLAN scenarios as it

ensures that all dependent parameters are included and that an accurate output is generated.

n Ingress interfaces are limited to the physical interfaces.

n The vlan and vrf parameters must be used for packet forwarding information wherever applicable. If

these parameters are not specified, their indicated defaults are used.

n The mac and mac-ip parameters are not supported for LAGs in L2 hash mode for both bridged and

routed traffic.

n When a LAG is in L3 hash mode, the L2 data is not used for hashing.

n For bridged traffic, the mac or mac-ip parameters must be used. For routed traffic, the ip or mac-ip

parameters must be used.

n For bridged traffic, ensure that the VLAN membership of the ingress port parameter matches the

value of the VLAN parameter.

n When using L3 hashing, the show forwarding-info mac form of this command is not applicable.

n When a LAG is in L3 hashing mode it will only hash L3 data. As a result, the L2 data displayed in the

output of the show forwarding-info mac-ip command is ignored.

n This command does not display data for unsupported egress interfaces, such as a tunnel or sub-

interface. The egress interface must be a physical port or a LAG.

n When ISL redirection occurs for a packet, the forwarding information does not show the correct

egress interface in the VSX MCLAG. Note that VXLAN forwarding information for VSX is not
supported.

Using classifier policies for traffic capture and analysis | 101

n TheforwardinginformationoutputofthiscommanddoesnotreflectthePBRpolicyforthe
destinationroute.
Examples
ShowingforwardinginformationwhenLAGisinL3hashmode(thedefault):
| interface | lag 1 |     |
| --------- | ----- | --- |
no shutdown
no routing
| vlan | access 1 |     |
| ---- | -------- | --- |
exit
show forwarding-info mac ingress-interface 1/1/4 source-mac-address
00:00:00:00:00:01 destination-mac-address 00:00:00:00:00:02 vlan 1
| Ingress-interface:  | 1/1/4             |                   |
| ------------------- | ----------------- | ----------------- |
| Source mac-address: | 00:00:00:00:00:01 |                   |
| Destination         | mac-address:      | 00:00:00:00:00:02 |
VLAN: 1
Forwarding info lookup needs IP inputs when lag is in L3 hash mode.
ShowingforwardinginformationwhenLAGisinL4hashmode:
| interface | lag 1 |     |
| --------- | ----- | --- |
no shutdown
no routing
| vlan | access 1   |     |
| ---- | ---------- | --- |
| hash | l4-src-dst |     |
exit
show forwarding-info mac ingress-interface 1/1/4 source-mac-address
00:00:00:00:00:01 destination-mac-address 00:00:00:00:00:02 vlan 1
| Ingress-interface:  | 1/1/4             |                   |
| ------------------- | ----------------- | ----------------- |
| Source mac-address: | 00:00:00:00:00:01 |                   |
| Destination         | mac-address:      | 00:00:00:00:00:02 |
VLAN: 1
| Egress interface: | lag1 | -> 1/1/1 |
| ----------------- | ---- | -------- |
ShowingforwardinginformationwhenLAGisinL2hashmode:
| interface | lag 1 |     |
| --------- | ----- | --- |
no shutdown
no routing
| vlan | access 1   |     |
| ---- | ---------- | --- |
| hash | l2-src-dst |     |
exit
show forwarding-info mac ingress-interface 1/1/4 source-mac-address
00:00:00:00:00:01 destination-mac-address 00:00:00:00:00:02 vlan 1
| Ingress-interface:  | 1/1/4             |                   |
| ------------------- | ----------------- | ----------------- |
| Source mac-address: | 00:00:00:00:00:01 |                   |
| Destination         | mac-address:      | 00:00:00:00:00:02 |
VLAN: 1
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 102

Forwarding info lookup on lag port is unsupported when lag is in L2 hash mode.
Showingforwardinginformationwhentheegressinterfaceisaphysicalport:
show mac-address-table
| MAC age-time |                  | : 300 seconds |     |      |
| ------------ | ---------------- | ------------- | --- | ---- |
| Number       | of MAC addresses | : 1           |     |      |
| MAC Address  |                  | VLAN Type     |     | Port |
--------------------------------------------------------------
| 00:00:00:00:00:02 |     | 1 static |     | lag1  |
| ----------------- | --- | -------- | --- | ----- |
| 00:00:00:00:00:03 |     | 1 static |     | 1/1/5 |
show forwarding-info mac ingress-interface 1/1/4 source-mac-address
00:00:00:00:00:01 destination-mac-address 00:00:00:00:00:03 vlan 1
| Ingress-interface: |              | 1/1/4             |     |     |
| ------------------ | ------------ | ----------------- | --- | --- |
| Source             | mac-address: | 00:00:00:00:00:01 |     |     |
| Destination        | mac-address: | 00:00:00:00:00:03 |     |     |
VLAN: 1
| Egress | interface: | 1/1/5 |     |     |
| ------ | ---------- | ----- | --- | --- |
ShowingforwardinginformationforwhentheingressinterfaceisROP:
| show forwarding-info |     | mac-ip ingress-interface | 1/1/14 |     |
| -------------------- | --- | ------------------------ | ------ | --- |
source-mac-address 00:11:01:00:00:01 destination-mac-address b8:d4:e7:dd:d3:00
source-ip-address 101.0.0.2 destination-ip-address 201.0.0.2 vrf default
| Ingress-interface: |              | 1/1/14            |     |     |
| ------------------ | ------------ | ----------------- | --- | --- |
| Source             | mac-address: | 00:11:01:00:00:01 |     |     |
| Destination        | mac-address: | b8:d4:e7:dd:d3:00 |     |     |
VLAN: 1
VRF: default
| Source      | IP: 101.0.0.2 |     |     |     |
| ----------- | ------------- | --- | --- | --- |
| Destination | IP: 201.0.0.2 |     |     |     |
L2 Warning: Port is routing enabled. Please use the 'show forwarding-info ip'
command.
| Egress | interface: | ECMP 1/1/17 |     |     |
| ------ | ---------- | ----------- | --- | --- |
ShowingforwardinginformationwithROPandSVI:
| interface | 1/1/4 |     |     |     |
| --------- | ----- | --- | --- | --- |
no routing
no shutdown
| vlan      | trunk native          | 1   |                 |                                          |
| --------- | --------------------- | --- | --------------- | ---------------------------------------- |
| vlan      | trunk allowed         | all |                 |                                          |
| interface | 1/1/6                 |     |                 |                                          |
| no        | shutdown              |     |                 |                                          |
| ip        | address 10.10.10.2/24 |     |                 |                                          |
| show ip   | route                 |     |                 |                                          |
|           |                       |     | Usingclassifier | policiesfortrafficcaptureandanalysis|103 |

| Displaying    | ipv4 routes    | selected | for    | forwarding |         |     |
| ------------- | -------------- | -------- | ------ | ---------- | ------- | --- |
| Origin Codes: | C - connected, |          | S -    | static, L  | - local |     |
|               | R - RIP,       | B -      | BGP, O | - OSPF, D  | - DHCP  |     |
Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN
|     | IA - OSPF | internal |     | area, E1 - | OSPF external type | 1   |
| --- | --------- | -------- | --- | ---------- | ------------------ | --- |
|     | E2 - OSPF | external |     | type 2     |                    |     |
VRF: default
Prefix           Nexthop     Interface  VRF(egress)   Origin/   Distance/    Age
                                                      Type      Metric
----------------------------------------------------------------------------------
-
10.10.10.0/24    -           1/1/6     - C         [0/0]        -
10.10.10.2/32    -           1/1/6     -              L         [0/0]        -
show forwarding-info ip source-ip-address 10.10.10.1 destination-ip-address
10.10.10.4
| Source IP:        | 10.10.10.1     |     |     |     |     |     |
| ----------------- | -------------- | --- | --- | --- | --- | --- |
| Destination       | IP: 10.10.10.4 |     |     |     |     |     |
| Egress interface: | 1/1/6          |     |     |     |     |     |
| interface         | 1/1/4          |     |     |     |     |     |
no routing
no shutdown
| vlan      | trunk native                | 1   |     |       |     |     |
| --------- | --------------------------- | --- | --- | ----- | --- | --- |
| vlan      | trunk allowed               | all |     |       |     |     |
| interface | 1/1/7                       |     |     |       |     |     |
| no        | routing                     |     |     |       |     |     |
| no        | shutdown                    |     |     |       |     |     |
| vlan      | access 2                    |     |     |       |     |     |
| interface | vlan 2                      |     |     |       |     |     |
| ip        | address 2.2.2.2/24interface |     |     | 1/1/4 |     |     |
no routing
no shutdown
| vlan          | trunk native       | 1        |        |            |         |     |
| ------------- | ------------------ | -------- | ------ | ---------- | ------- | --- |
| vlan          | trunk allowed      | all      |        |            |         |     |
| interface     | 1/1/7              |          |        |            |         |     |
| no            | routing            |          |        |            |         |     |
| no            | shutdown           |          |        |            |         |     |
| vlan          | access 2           |          |        |            |         |     |
| interface     | vlan 2             |          |        |            |         |     |
| ip            | address 2.2.2.2/24 |          |        |            |         |     |
| show ip       | route              |          |        |            |         |     |
| Displaying    | ipv4 routes        | selected | for    | forwarding |         |     |
| Origin Codes: | C - connected,     |          | S -    | static, L  | - local |     |
|               | R - RIP,           | B -      | BGP, O | - OSPF, D  | - DHCP  |     |
Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN
|     | IA - OSPF | internal |     | area, E1 - | OSPF external type | 1   |
| --- | --------- | -------- | --- | ---------- | ------------------ | --- |
|     | E2 - OSPF | external |     | type 2     |                    |     |
VRF: default
Prefix           Nexthop     Interface  VRF(egress)   Origin/   Distance/    Age
                                                      Type      Metric
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 104

----------------------------------------------------------------------------------
-
2.2.2.0/24    -           vlan2     -             C         [0/0]        -
2.2.2.2/32    -           vlan2     -             L         [0/0]        -
show forwarding-info ip source-ip-address 2.2.2.1 destination-ip-address 2.2.2.4
| Source IP:        | 2.2.2.1     |          |     |
| ----------------- | ----------- | -------- | --- |
| Destination       | IP: 2.2.2.4 |          |     |
| Egress interface: | vlan2       | -> 1/1/7 |     |
ShowingforwardinginformationinL4hashmodewithROPLAG:
| switch# show | forwarding-info | mac-ip ingress-interface | 1/1/1 |
| ------------ | --------------- | ------------------------ | ----- |
source-mac-address 00:00:00:00:01 destination-mac-address 00:00:00:00:00:02
source-ip-address 10.10.10.10 destination-ip-address 10.10.10.11
transport-protocol 6 source-l4-port 1234 destination-l4-port 5678 vrf default
| Ingress interface: | 1/1/1                      |                   |     |
| ------------------ | -------------------------- | ----------------- | --- |
| Source MAC         | address: 00:00:00:00:00:01 |                   |     |
| Destination        | MAC address:               | 00:00:00:00:00:02 |     |
VLAN: 1
VRF: default
| Source IP:        | 10.10.10.10     |          |     |
| ----------------- | --------------- | -------- | --- |
| Destination       | IP: 10.10.10.11 |          |     |
| Protocol:         | TCP(6)          |          |     |
| Source L4         | Port: 1234      |          |     |
| Destination       | L4 Port: 5678   |          |     |
| Egress interface: | lag1            | -> 1/1/2 |     |
ShowingforwardinginformationinECMPhashmodewithROPLAG:
| switch# show | forwarding-info | mac-ip ingress-interface | 1/1/1 |
| ------------ | --------------- | ------------------------ | ----- |
source-mac-address 00:00:00:00:01 destination-mac-address 00:00:00:00:00:02
| source-ip-address | 10.10.10.10 | destination-ip-address | 200.0.0.1 |
| ----------------- | ----------- | ---------------------- | --------- |
transport-protocol 6 source-l4-port 1234 destination-l4-port 5678 vrf default
| Ingress interface: | 1/1/1                      |                   |     |
| ------------------ | -------------------------- | ----------------- | --- |
| Source MAC         | address: 00:00:00:00:00:01 |                   |     |
| Destination        | MAC address:               | 00:00:00:00:00:02 |     |
VLAN: 1
VRF: default
| Source IP:        | 10.10.10.10   |               |     |
| ----------------- | ------------- | ------------- | --- |
| Destination       | IP: 200.0.0.1 |               |     |
| Protocol:         | TCP(6)        |               |     |
| Source L4         | Port: 1234    |               |     |
| Destination       | L4 Port: 5678 |               |     |
| Egress interface: | ECMP          | lag1 -> 1/1/2 |     |
Attemptingtoshowforwardinginformationbutwiththerequesttimedout:
| switch# show | forwarding-info | mac-ip ingress-interface | 1/1/1 |
| ------------ | --------------- | ------------------------ | ----- |
source-mac-address 00:00:00:00:01 destination-mac-address 00:00:00:00:00:02
Usingclassifier policiesfortrafficcaptureandanalysis|105

| source-ip-address | 10.10.10.10 | destination-ip-address |     | 200.0.0.1 |     |
| ----------------- | ----------- | ---------------------- | --- | --------- | --- |
transport-protocol 6 source-l4-port 1234 destination-l4-port 5678 vrf default
| Ingress interface: | 1/1/1                      |                   |     |     |     |
| ------------------ | -------------------------- | ----------------- | --- | --- | --- |
| Source MAC         | address: 00:00:00:00:00:01 |                   |     |     |     |
| Destination        | MAC address:               | 00:00:00:00:00:02 |     |     |     |
VLAN: 1
VRF: default
| Source IP:    | 10.10.10.10   |     |     |     |     |
| ------------- | ------------- | --- | --- | --- | --- |
| Destination   | IP: 200.0.0.1 |     |     |     |     |
| Protocol:     | TCP(6)        |     |     |     |     |
| Source L4     | Port: 1234    |     |     |     |     |
| Destination   | L4 Port: 5678 |     |     |     |     |
| Request timed | out           |     |     |     |     |
Showingforwardinginformationona6300orSwitchseriesthatincludestheinnerdestinationand
innersourceMACaddresses:
| switch# show | forwarding-info | mac-ip ingress-interface |     | 1/1/26 |     |
| ------------ | --------------- | ------------------------ | --- | ------ | --- |
source-mac-address 00:11:22:33:44:55 destination-mac-address 00:50:56:96:13:b6
source-ip-address 10.1.30.11 destination-ip-address 10.1.50.21 vlan 10
vrf test1
| Ingress-interface:  | 1/1/26            |                   |     |     |     |
| ------------------- | ----------------- | ----------------- | --- | --- | --- |
| Source mac-address: | 00:11:22:33:44:55 |                   |     |     |     |
| Destination         | mac-address:      | 00:50:56:96:13:b6 |     |     |     |
VLAN: 10
VRF: test1
| Source IP:        | 10.1.30.11             |                   |     |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- | --- |
| Destination       | IP: 10.1.50.21         |                   |     |     |     |
| Egress interface: | vxlan1                 |                   |     |     |     |
| Tunnel Egress     | Info:                  |                   |     |     |     |
| Inner Destination | MAC:                   | 00:00:12:12:12:12 |     |     |     |
| Inner Source      | MAC: 00:50:56:96:13:b6 |                   |     |     |     |
VNI: 1010
| VNI Type:          | l3_vni       |              |              |                   |     |
| ------------------ | ------------ | ------------ | ------------ | ----------------- | --- |
| Tunnel Source      | IP: 10.0.0.1 |              |              |                   |     |
| Tunnel Destination | IP:          | 10.0.0.2     |              |                   |     |
| UDP Source         | Port: 51432  |              |              |                   |     |
| UDP Dest           | Port: 4789   |              |              |                   |     |
| Tunnel Egress      | Path:        |              |              |                   |     |
| Nexthop            |              | L3 Interface | L2 Interface | Destination       | MAC |
| 192.168.11.10      |              | 1/1/35       | 1/1/35       | b8:d4:e7:dd:e2:00 |     |
Showingforwardinginformationona6300/6400or8360switchserieswithoutputthatincludesan
ethertypeandegressinterface:
| switch# show | forwarding-info | mac ingress-interface |     | 1/3/47 |     |
| ------------ | --------------- | --------------------- | --- | ------ | --- |
source-mac-address 00:00:00:00:01 destination-mac-address 00:00:00:00:00:02 vlan 1
| ethertype          | 0xffff                     |     |     |     |     |
| ------------------ | -------------------------- | --- | --- | --- | --- |
| Ingress interface: | 1/3/47                     |     |     |     |     |
| Source MAC         | address: 00:00:00:00:00:01 |     |     |     |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 106

| Destination | MAC address: | 00:00:00:00:00:02 |     |     |
| ----------- | ------------ | ----------------- | --- | --- |
VLAN: 1
| Ethertype:        | 0xffff |           |     |     |
| ----------------- | ------ | --------- | --- | --- |
| Egress interface: | lag1   | -> 1/3/48 |     |     |
SampleShowcommand-Bridgingv4
Showingcommandoutput-Bridgingv4
| Leaf2# show | forwarding-info | mac-ip ingress-interface | 1/1/11 |     |
| ----------- | --------------- | ------------------------ | ------ | --- |
source-mac-address 00:12:01:00:00:01 destination-mac-address 00:13:01:00:00:01
source-ip-address 20.1.1.21 destination-ip-address 20.1.1.31 ethertype 0x0800
| transport-protocol  | 61                | vlan 1001 vrf VRF_1 |     |     |
| ------------------- | ----------------- | ------------------- | --- | --- |
| Ingress-interface:  | 1/1/11            |                     |     |     |
| Source mac-address: | 00:12:01:00:00:01 |                     |     |     |
| Destination         | mac-address:      | 00:13:01:00:00:01   |     |     |
VLAN: 1001
VRF: VRF_1
| Source IP:        | 20.1.1.21              |                   |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- |
| Destination       | IP: 20.1.1.31          |                   |     |     |
| Protocol:         | 61                     |                   |     |     |
| Ethertype:        | 0x0800                 |                   |     |     |
| Egress interface: | vxlan1                 |                   |     |     |
| Tunnel Egress     | Info:                  |                   |     |     |
| Inner Destination | MAC:                   | 00:13:01:00:00:01 |     |     |
| Inner Source      | MAC: 00:12:01:00:00:01 |                   |     |     |
VNI: 1001
| VNI Type:          | 12_vni       |              |                 |     |
| ------------------ | ------------ | ------------ | --------------- | --- |
| Tunnel Source      | IP: 2.2.2.2  |              |                 |     |
| Tunnel Destination | IP:          | 3.3.3.3      |                 |     |
| UDP Source         | Port: 11820  |              |                 |     |
| UDP Dest           | Port: 4789   |              |                 |     |
| Tunnel Egress      | Path:        |              |                 |     |
| Nexthop            | L3 Interface | L2 Interface | Destination     | MAC |
| 72.1.1.1           | lag72        | lag72->1/1/3 | b8d4e7:de:f1:00 |     |
Leaf2#
|     |     |     | Usingclassifier | policiesfortrafficcaptureandanalysis|107 |
| --- | --- | --- | --------------- | ---------------------------------------- |

SampleShowcommand-Bridgingv6
Showingcommandoutput-Bridgingv6
| Leaf2# show | forwarding-info | mac-ip ingress-interface |     | 1/1/11 |     |
| ----------- | --------------- | ------------------------ | --- | ------ | --- |
source-mac-address 00:12:01:00:00:01 destination-mac-address 00:13:01:00:00:01
source-ipv6-address 20:1::21 destination-ipv6-address 20:1::31 ethertype 0x86dd
| vlan 1001           | vrf VRF_1    |                   |     |     |     |
| ------------------- | ------------ | ----------------- | --- | --- | --- |
| Ingress-interface:  | 1/1/11       |                   |     |     |     |
| Source mac-address: |              | 00:12:01:00:00:01 |     |     |     |
| Destination         | mac-address: | 00:13:01:00:00:01 |     |     |     |
VLAN: 1001
VRF: VRF_1
| Source IPv6:      | 20:1::21               |                   |     |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- | --- |
| Destination       | IPv6: 20:1::31         |                   |     |     |     |
| Ethertype:        | Ox86dd                 |                   |     |     |     |
| Egress interface: | vxlan1                 |                   |     |     |     |
| Tunnel Egress     | Info:                  |                   |     |     |     |
| Inner Destination | MAC:                   | 00:13:01:00:00:01 |     |     |     |
| Inner Source      | MAC: 00:12:01:00:00:01 |                   |     |     |     |
VNI: 1001
| VNI Type:          | 12_vni      |              |              |                   |     |
| ------------------ | ----------- | ------------ | ------------ | ----------------- | --- |
| Tunnel Source      | IP: 2.2.2.2 |              |              |                   |     |
| Tunnel Destination | IP:         | 3.3.3.3      |              |                   |     |
| UDP Source         | Port: 50828 |              |              |                   |     |
| UDP Dest           | Port: 4789  |              |              |                   |     |
| Tunnel Egress      | Path:       |              |              |                   |     |
| Nexthop            |             | L3 Interface | L2 Interface | Destination       | MAC |
| 62.1.1.1           |             | lag62        | lag62->1/1/1 | b8:d4:e7:dd:ba:00 |     |
Leaf2#
SampleShowcommand-Routingv4
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 108

Showingcommandoutput-Routingv4
| Leaf2# | show forwarding-info |     | mac-ip | ingress-interface | 1/1/11 |
| ------ | -------------------- | --- | ------ | ----------------- | ------ |
source-mac-address 00:15:01:00:00:01 destination-mac-address 00:00:00:32:32:32
source-ip-address 32.1.1.21 destination-ip-address 33.1.1.31 ethertype 0x0800
| transport-protocol |              | 61                | vlan 3201         | vrf VRF_1 |     |
| ------------------ | ------------ | ----------------- | ----------------- | --------- | --- |
| Ingress-interface: |              | 1/1/11            |                   |           |     |
| Source             | mac-address: | 00:15:01:00:00:01 |                   |           |     |
| Destination        | mac-address: |                   | 00:00:00:32:32:32 |           |     |
VLAN: 3201
VRF: VRF_1
| Source            | IP: 32.1.1.21 |                   |                   |     |     |
| ----------------- | ------------- | ----------------- | ----------------- | --- | --- |
| Destination       | IP:           | 33.1.1.31         |                   |     |     |
| Protocol:         | 61            |                   |                   |     |     |
| Ethertype:        | 0x0800        |                   |                   |     |     |
| Egress            | interface:    | vxlan1            |                   |     |     |
| Tunnel            | Egress Info:  |                   |                   |     |     |
| Inner Destination |               | MAC:              | 00:00:00:0c:0c:0c |     |     |
| Inner Source      | MAC:          | 8c:85:c1:49:00:00 |                   |     |     |
VNI: 9001
| VNI Type:  | 13_vni       |         |               |                |     |
| ---------- | ------------ | ------- | ------------- | -------------- | --- |
| Tunnel     | Source IP:   | 2.2.2.2 |               |                |     |
| Tunnel     | Destination  | IP:     | 3.3.3.3       |                |     |
| UDP Source | Port:        | 41081   |               |                |     |
| UDP Dest   | Port: 4789   |         |               |                |     |
| Tunnel     | Egress Path: |         |               |                |     |
| Nexthop    | L3 Interface |         | L2 Interface  | Destination    | MAC |
| 62.1.1.1   | lag62        |         | lag62->1/1/14 | b8d4e7dd:ba:00 |     |
SampleShowcommand-Routingv6
Usingclassifier policiesfortrafficcaptureandanalysis|109

Showingcommandoutput-Routingv6
| Leaf2# show | forwarding-info | mac-ip ingress-interface | 1/1/11 |     |
| ----------- | --------------- | ------------------------ | ------ | --- |
source-mac-address 00:15:01:00:00:01 destination-mac-address 00:00:00:32:32:32
source-ipv6-address 32:1::21 destination-ipv6-address 33:1::31 ethertype 0x86dd
| vlan 3201           | vrf VRF_1         |                   |     |     |
| ------------------- | ----------------- | ----------------- | --- | --- |
| Ingress-interface:  | 1/1/11            |                   |     |     |
| Source mac-address: | 00:15:01:00:00:01 |                   |     |     |
| Destination         | mac-address:      | 00:00:00:32:32:32 |     |     |
VLAN: 3201
VRF: VRF_1
| Source IPv6:      | 32:1::21               |                   |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- |
| Destination       | IPv6: 33:1::31         |                   |     |     |
| Ethertype:        | Ox86dd                 |                   |     |     |
| Egress interface: | vxlan1                 |                   |     |     |
| Tunnel Egress     | Info:                  |                   |     |     |
| Inner Destination | MAC:                   | 00:00:00:0c:0c:Oc |     |     |
| Inner Source      | MAC: 8c:85:c1:49:00:00 |                   |     |     |
VNI: 9001
| VNI Type:          | 13 vni       |              |                   |     |
| ------------------ | ------------ | ------------ | ----------------- | --- |
| Tunnel Source      | IP: 2.2.2.2  |              |                   |     |
| Tunnel Destination | IP:          | 3.3.3.3      |                   |     |
| UDP Source         | Port: 27596  |              |                   |     |
| UDP Dest           | Port: 4789   |              |                   |     |
| Tunnel Egress      | Path:        |              |                   |     |
| Nexthop            | L3 Interface | L2 Interface | Destination       | MAC |
| 72.1.1.1           | lag72        | lag72->1/1/2 | b8:d4:e7:de:f1:00 |     |
Leaf2#
SampleShowcommand-UDPBridgingv4
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 110

Showingcommandoutput-UDP Bridgingv4
| Leaf1# show | forwarding-info | mac-ip | ingress-interface | 1/1/1 |     |
| ----------- | --------------- | ------ | ----------------- | ----- | --- |
source-mac-address 00:11:01:00:00:01 destination-mac-address 00:12:01:00:00:01
source-ip-address 20.1.1.11 destination-ip-address 20.1.1.21 ethertype 0x0800 vlan
| 1001 vrf            | VRF_1 transport-protocol |                   | 17 source-14-port | 2222 |     |
| ------------------- | ------------------------ | ----------------- | ----------------- | ---- | --- |
| destination-14-port | 4444                     |                   |                   |      |     |
| Ingress-interface:  | 1/1/1                    |                   |                   |      |     |
| Source mac-address: | 00:11:01:00:00:01        |                   |                   |      |     |
| Destination         | mac-address:             | 00:12:01:00:00:01 |                   |      |     |
VLAN: 1001
VRF: VRF_1
| Source IP:        | 20.1.1.11              |                   |     |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- | --- |
| Destination       | IP: 20.1.1.21          |                   |     |     |     |
| Protocol:         | UDP(17)                |                   |     |     |     |
| Source L4         | Port: 2222             |                   |     |     |     |
| Destination       | L4 Port: 4444          |                   |     |     |     |
| Ethertype:        | 0x0800                 |                   |     |     |     |
| Egress interface: | vxlan1                 |                   |     |     |     |
| Tunnel Egress     | Info:                  |                   |     |     |     |
| Inner Destination | MAC:                   | 00:12:01:00:00:01 |     |     |     |
| Inner Source      | MAC: 00:11:01:00:00:01 |                   |     |     |     |
VNI: 1001
| VNI Type:          | 12_vni       |         |              |                   |     |
| ------------------ | ------------ | ------- | ------------ | ----------------- | --- |
| Tunnel Source      | IP: 1.1.1.1  |         |              |                   |     |
| Tunnel Destination | IP:          | 2.2.2.2 |              |                   |     |
| UDP Source         | Port: 30424  |         |              |                   |     |
| UDP Dest           | Port: 4789   |         |              |                   |     |
| Tunnel Egress      | Path:        |         |              |                   |     |
| Nexthop            | L3 Interface |         | L2 Interface | Destination       | MAC |
| 61.1.1.1           | lag61        |         | lag61->1/1/7 | b8:d4:e7:dd:ba:00 |     |
Leaf1#
|     |     |     |     | Usingclassifier | policiesfortrafficcaptureandanalysis|111 |
| --- | --- | --- | --- | --------------- | ---------------------------------------- |

Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
10.15.1000 Commandintroducedonthe6300and8360Switchseriesforthe
VXLANfeature.
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 112

Chapter 13
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
113
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

| switch# | show | accounting |     | log | last 5 |     |     |
| ------- | ---- | ---------- | --- | --- | ------ | --- | --- |
---------------------------------------------------
| Command | logs | from | current | boot |     |     |     |
| ------- | ---- | ---- | ------- | ---- | --- | --- | --- |
---------------------------------------------------
| No command |     | logs | has been | logged | in the system |     |     |
| ---------- | --- | ---- | -------- | ------ | ------------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command   | History     |         |     |         |                    |     |     |
| --------- | ----------- | ------- | --- | ------- | ------------------ | --- | --- |
| Release   |             |         |     |         | Modification       |     |     |
| 10.11     |             |         |     |         | Commandintroduced. |     |     |
| Command   | Information |         |     |         |                    |     |     |
| Platforms |             | Command |     | context | Authority          |     |     |
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
Remotesyslog|114

Parameter

Description

[udp [<PORT-NUM>] | tcp [<PORT-NUM> |

tls [<PORT-NUM>]]

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

the remote syslog server. Required.

Specifies the UDP port, TCP port, or TLS port of the
remote syslog server to receive the forwarded syslog
messages.

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

115

Parameter

Description

n info: Forwards syslog messages with the severity of

info (1) and above. Default.

n notice: Forwards syslog messages with the severity

of notice (2) and above.

n warning: Forwards syslog messages with the

severity of warning (3) and above.

Specifies the VRF used to connect to the syslog server.
Optional. Default: default

vrf <VRF-NAME>

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

switch(config)# logging 10.0.10.6 severity info filter filter_lldp_logs vrf mgmt

Applying log filtering and enabling the rate limit for syslog server forwarding over TCP port:

switch(config)# logging 10.0.10.2 tcp 3440 severity err vrf mgmt include-
auditable-events filter filter_lldp_logs rate-limit-burst 3 rate-limit-interval 35

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Remote syslog | 116

| Release             |         |         | Modification                    |
| ------------------- | ------- | ------- | ------------------------------- |
| 10.12.1000          |         |         | Thedisableparameterisintroduced |
| 10.07orearlier      |         |         | --                              |
| Command Information |         |         |                                 |
| Platforms           | Command | context | Authority                       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logging accounting-format-native |     |     |     |
| -------------------------------- | --- | --- | --- |
logging accounting-format-native
| [no] logging | accounting-format-native |     |     |
| ------------ | ------------------------ | --- | --- |
Description
ChangetheaccountinglogmessageformattonativeLinuxformat.(Default:AOS-CXformat)
The'no'formofthiscommandwillchangetheaccountinglogmessageformattoAOS-CXformat.
Usage
Thisoptionenablestheswitchtoshowalltypesofaccountingrecordstotheuser.Whenconfigured,the
sameformatwillbeusedwhilesendingmessagestosyslogservers.Whenupgradingtothisversionof
AOS-CXfromAOS-CX10.10orearlierversions,ifnativeaccountinglogsarepreferred,thenbest
practicesistoissuethiscommandasapartoftheupgrade.IftheswitchupgradesfromAOS-CX10.10
orearlierwithoutconfiguringthissetting,bydefault,theaccountinglogmessageformatwillbeAOS-CX
Format.
Example
ThisexamplechangestheaccountinglogmessageformattonativeLinuxformat.
| switch(config)# | logging | accounting-format-native |     |
| --------------- | ------- | ------------------------ | --- |
ThefollowingexamplereturnstheaccountinglogmessageformattothedefaultAOS-CXformat.
| switch(config)# | no  | logging accounting-format-native |     |
| --------------- | --- | -------------------------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |     |     |                    |
| ------------------- | --- | --- | ------------------ |
| Release             |     |     | Modification       |
| 10.11               |     |     | Commandintroduced. |
| Command Information |     |     |                    |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 117

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| logging        | filter        |     |     |
| -------------- | ------------- | --- | --- |
| logging filter | <FILTER-NAME> |     |     |
| [{enable       | | disable}]   |     |     |
[<SEQUENCE-ID>] {permit | deny} [event-id <EVENT-ID-RANGE>] [includes <REGEX>]
| [severity | <COMPARISON-OPERATOR> |     | <LEVEL>] |
| --------- | --------------------- | --- | -------- |
no <SEQUENCE-ID>
| resequence | <OLD-SEQUENCE-ID>    |     | <NEW-SEQUENCE-ID> |
| ---------- | -------------------- | --- | ----------------- |
| no logging | filter <FILTER-NAME> |     |                   |
Description
Createsafiltertorestrictwhateventordebuglogsarelogged.Afiltercanbeusedtoeitherpermitor
deny:
Theeventlogsfrombeinggeneratedontheswitch,or
n
n Theeventordebuglogsgeneratedontheswitchfrombeingforwardedtoasyslogserver.
Afilterisidentifiedbyafilternameandcanhaveupto20rulesorentries,eachwithadifferent
sequencenumber,matchingcriteria,andcorrespondingaction(denyorpermit).Whenafilterisapplied
onalog,thelogismatchedagainstthecriteriamentionedintherulesorentriesinascendingnumerical
orderoftheirsequencenumbersuntilamatchingentryisfound.Onceamatchingentryisfound,its
correspondingactionisappliedonthelog.Ifnomatchingruleisfound,thedefaultaction(permit)is
applied.
Thenoformofthiscommandremovesthefilter.
| Parameter     |     |     | Description                                |
| ------------- | --- | --- | ------------------------------------------ |
| <FILTER-NAME> |     |     | Specifiestheuniquenametoidentifythefilter. |
| enable        |     |     | Filtereventlogsgeneratedontheswitch.       |
<SEQUENCE-ID> Specifiesthefiltercriteriasequencenumber.Default:Increments
by10fromthelargestsequence-idcurrentlyusedinthisfilter.
| deny   |     |     | Preventsthematchinglogfrombeinglogged. |
| ------ | --- | --- | -------------------------------------- |
| permit |     |     | Allowsthematchinglog.                  |
<event-id> MatcheslogsbyeventID.SpecifyaneventIDorarangeofevent
IDs.Itsupportsamaximumof100eventIDs.
includes <REGEX> Matchesthelogmessageagainstaregularexpressionstring.
severity
Matchesthelogsbyseveritylevel.
Remotesyslog|118

Parameter

Description

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

Usage

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

119

Filtering event or debug logs when forwarding to a remote syslog server:Thefilternamemustbe
configuredintheloggingcommandthatisusedtoconfigureremotesyslogserver.Thelogswillbe
generatedontheswitchandthefilteronlydecideswhethertodenyorpermitthesyslogforwardingfor
| thematchinglog.Forexample:logging |     | 10.0.10.6 | filter filter_lldp_logs |     |
| --------------------------------- | --- | --------- | ----------------------- | --- |
Thefilteraffectsdebuglogsonlywhenthecommanddebugdestinationsyslogisconfiguredontheswitch.
Theseveritymentionedintheremotesyslogserverconfigurationusingloggingcommandunderconfiguration
contexthasmoreprecedencethantheseveritymentionedinafilterentry.Ifalogwithwarningseverityis
permittedbyafilter,buttheremotesyslogconfigurationhasseverityerrmentionedinit,thelogwillnotbe
forwardedtotheremotesyslogserver(sincewarning(3)islesserthanerr(4)).Ontheotherhand,ifalogwitherr
severityispermittedbyafilterandtheremotesyslogconfigurationhasseveritywarningmentionedinit,thelog
willbeforwardedtotheremotesyslogserver.
Examples
Configuringanewloggingfilter:
| switch(config)# | logging filter | example_filter |     |     |
| --------------- | -------------- | -------------- | --- | --- |
TodenylogshavingeventID1301andarangeofeventIDsfrom1305to1309:
| switch(config-logging-filter)# |     | 20 deny | event-id 1301,1305-1309 |     |
| ------------------------------ | --- | ------- | ----------------------- | --- |
TopermitlogshavingeventID1300:
| switch(config-logging-filter)# |     | 30 permit | event-id | 1300 |
| ------------------------------ | --- | --------- | -------- | ---- |
Topermitlogswithseveritygreaterthanorequaltoerr:
| switch(config-logging-filter)# |     | 30 permit | severity | ge err |
| ------------------------------ | --- | --------- | -------- | ------ |
Todenylogswithseveritygreaterthaninfo:
| switch(config-logging-filter)# |     | 30 deny | severity gt | info |
| ------------------------------ | --- | ------- | ----------- | ---- |
TodenylogswitheventID1024andamessagematchingtheregularexpressionLLDP:
switch(config-logging-filter)# 40 deny event-id 1024 includes LLDP
Denyingalllogs:
| switch(config-logging-filter)# |     | 40 deny |     |     |
| ------------------------------ | --- | ------- | --- | --- |
Remotesyslog|120

ChangingthesequenceIDofanexistingrule:
| switch(config-logging-filter)# |     |     | resequence | 20 70 |
| ------------------------------ | --- | --- | ---------- | ----- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms configandconfig- Administratorsorlocalusergroupmemberswithexecution
|                  | logging-filter |     | rightsforthiscommand. |     |
| ---------------- | -------------- | --- | --------------------- | --- |
| logging facility |                |     |                       |     |
logging facility {local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7}
| no logging facility |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Description
Setstheloggingfacilitytobeusedforremotesyslogmessages.Default:local7
Thenoformofthiscommanddisablestheloggingfacilitytobeusedforremotesyslogmessages.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{local0 | local1 | local2 | Selectstheloggingfacilitytobeusedforremotesyslogmessages.
| local3 | | local4 | local5 | |   | Required. |     |
| -------- | --------------- | --- | --------- | --- |
| local6 | | local7}         |     |           |     |
Specifiestheseverityofthesyslogmessages:
n local0
n local1
n local2
n local3
n local4
n local5
n local6
n local7
Examples
Setsthelocal5loggingfacilitytobeusedforremotesyslogmessages:
| switch(config)# | logging | facility | local5 |     |
| --------------- | ------- | -------- | ------ | --- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 121

Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
Remotesyslog|122

Examples
Enablingstorageoflogsinstoragewithseverityinfo:
switch(config)#logging
persistent-storage severity info
Logs will be written to storage and made available across reboot.
| Do you want | to continue | (y/n)? |     |
| ----------- | ----------- | ------ | --- |
Disablingstorageoflogsinstorage:
| switch(config)# | no  | logging persistent-storage |     |
| --------------- | --- | -------------------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 123

Chapter 14

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

For 6400 switches only:
diagnostic monitor {fabric <SLOT-ID>}
no diagnostic monitor {fabric <SLOT-ID>}

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

Usage

Specifies the slot ID of a module. Format: member/slot.

When no parameters are used in the command (diagnostic monitor or no diagnostic monitor), the
command applies to all modules. This command impacts the diagnostics that run periodically. It does
not affect on-demand diagnostics.

Example

Enabling runtime diagnostics for a specified module:

switch(config)# diagnostic monitor management-module 1/1

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

124

Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
config
| 6300 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 6400 |     |     | rightsforthiscommand.                              |
diag on-demand
diag on-demand {fan-tray | line-module | management-module} [<SLOT-ID>]
For6400switchesonly:
| diag on-demand | {fabric | <SLOT-ID>} |     |
| -------------- | ------- | ---------- | --- |
Description
Runsthediagnostictestsforallmodulesorforaspecifiedmodule.
Parameter Description
| [fan-tray | | line-module | | management-module] |     |
| --------- | ------------- | -------------------- | --- |
Selectstheoptionsforenablingordisablingrun-
timediagnosticsforaspecificmodule.
fan-tray Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID> Specifiesthemember/slotformanagement
modules(1/1or1/2),linemodules(1/3-1/7,1/8-
1/12),fantrays(1/1-1/3),andfabricmodules(1/1-
1/2)ona6400switch.
Specifiesthemember/slotformanagement
modules(1/1),linemodules(1/1),andfantrays
(1/1-1/2)ona6300switch.
Usage
Whennoparametersareusedinthecommand(diag on-demand),thecommandappliestoall
modules.
Examples
Runningdiagnostictestsforallmodulesona6300switch:
RuntimeDiagnostics|125

| switch#  | diag on-demand |                |     |         |
| -------- | -------------- | -------------- | --- | ------- |
| Fetching | Test results.  | Please wait    | ... |         |
| Module   |                | ID Diagnostics |     | Success |
Performed
| -------------------- |     | ----- ----------- |     | ------- |
| -------------------- | --- | ----------------- | --- | ------- |
| FanTray              |     | 1/2               | 1   | 100%    |
| FanTray              |     | 1/1               | 1   | 100%    |
| LineModule           |     | 1/1               | 13  | 100%    |
| ManagementModule     |     | 1/1               | 13  | 100%    |
Runningdiagnostictestsforaspecificmoduleona6300switch:
| switch#    | diag on-demand | management-module |      | 1/1     |
| ---------- | -------------- | ----------------- | ---- | ------- |
| Performing | diagnostic     | tests. Please     | wait | ...     |
| Fetching   | Test results.  | Please wait       | ...  |         |
| Module     |                | ID Diagnostics    |      | Success |
Performed
| -------------------- |     | ----- ----------- |     | ------- |
| -------------------- | --- | ----------------- | --- | ------- |
| ManagementModule     |     | 1/1               | 13  | 100%    |
Runningdiagnostictestsforallmodulesona6400switch:
| switch#  | diag on-demand |                |     |         |
| -------- | -------------- | -------------- | --- | ------- |
| Fetching | Test results.  | Please wait    | ... |         |
| Module   |                | ID Diagnostics |     | Success |
Performed
| -------------------- |     | ----- ----------- |     | ------- |
| -------------------- | --- | ----------------- | --- | ------- |
| FanTray              |     | 1/2               | 2   | 100%    |
| LineModule           |     | 1/3               | 24  | 100%    |
| ManagementModule     |     | 1/1               | 19  | 100%    |
| LineModule           |     | 1/7               | 12  | 100%    |
| Fabric               |     | 1/1               | 6   | 100%    |
| LineModule           |     | 1/5               | 24  | 100%    |
| LineModule           |     | 1/4               | 24  | 100%    |
| FanTray              |     | 1/1               | 2   | 100%    |
| LineModule           |     | 1/6               | 24  | 100%    |
Runningdiagnostictestsforaspecificmoduleona6400switch:
| switch#    | diag on-demand | management-module |      |         |
| ---------- | -------------- | ----------------- | ---- | ------- |
| Performing | diagnostic     | tests. Please     | wait | ...     |
| Fetching   | Test results.  | Please wait       | ...  |         |
| Module     |                | ID Diagnostics    |      | Success |
Performed
| -------------------- |     | ----- ----------- |     | ------- |
| -------------------- | --- | ----------------- | --- | ------- |
| ManagementModule     |     | 1/1               | 19  | 100%    |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command | History |     |     |     |
| ------- | ------- | --- | --- | --- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 126

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
show diagnostic
show diagnostic {fan-tray | line-module | management-module} [<SLOT-ID>] {brief |
detail} [vsx-peer]
Description
Displaysthediagnostictestresultsforallmodulesorforaspecifiedmodule.
Parameter Description
[fan-tray | line-module | management-module] Selectstheoptionsforenablingordisabling
runtimediagnosticsforaspecificmodule.
fan-tray Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module
Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID> Specifiesthemember/slotformanagement
modules(1/1),linemodules(1/1),andfantrays
(1/1-1/2)onthe6300switch.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Ifthe
switchesdonothavetheVSXconfigurationorthe
ISLisdown,theoutputfromtheVSXpeerswitch
isnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Whennoparametersareusedinthecommand(showdiagnostic),thecommandappliestoallmodules.
Example
Showingdiagnostictestresultsinbriefformatforallmodulesona6300switch:
| switch# show | diagnostic | brief          |         |
| ------------ | ---------- | -------------- | ------- |
| Module       |            | ID Diagnostics | Success |
Performed
| -------------------- |     | ----- ----------- | ------- |
| -------------------- | --- | ----------------- | ------- |
| ManagementModule     |     | 1/1               | 13 100% |
RuntimeDiagnostics|127

| LineModule |     | 1/1 |     | 13  | 100%   |     |     |
| ---------- | --- | --- | --- | --- | ------ | --- | --- |
| FanTray    |     | 1/1 |     |     | 1 100% |     |     |
| FanTray    |     | 1/2 |     |     | 1 100% |     |     |
Showingdiagnostictestresultsinbriefformatforaspecifiedmoduleona6300switch:
| switch# show | diagnostic |     | line-module |     | brief   |     |     |
| ------------ | ---------- | --- | ----------- | --- | ------- | --- | --- |
| Module       |            | ID  | Diagnostics |     | Success |     |     |
Performed
| -------------------- |     | ----- | ----------- |     | ------- |     |     |
| -------------------- | --- | ----- | ----------- | --- | ------- | --- | --- |
| LineModule           |     | 1/1   |             | 13  | 100%    |     |     |
Showingdiagnostictestresultsindetailformatforallmodulesona6300switch:
| switch# show              | diagnostic |     | detail |     |     |     |     |
| ------------------------- | ---------- | --- | ------ | --- | --- | --- | --- |
| Module : ManagementModule |            |     | 1/1    |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp |     | First Run | Timestamp |               |       |     |
| -------- | --------- | --- | --------- | --------- | ------------- | ----- | --- |
|          |           |     |           |           | Failure Count | Count |     |
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          |     | ------------------- |          |          |     |     |
| ---------------------- | -------- | --- | ------------------- | -------- | -------- | --- | --- |
| ddr_cecount            | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:38 |     | 2019-07-31          |          | 07:44:55 |     |     |
| emmc                   | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| fan_ctrlr              | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| fepld                  | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:38 |     | 2019-07-31          |          | 07:44:54 |     |     |
| fru_eeprom             | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:54 |          |     |     |
| fru_eeprom_ul          | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:54 |          |     |     |
| mm_lcb                 | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:37 |     | 2019-07-31          |          | 07:44:54 |     |     |
| pmc                    | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:37 |     | 2019-07-31          |          | 07:44:54 |     |     |
| rdimm_spd              | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| rdimm_tmp              | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| rtc                    | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| tmp1                   | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| tmp2                   | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| Module : LineModule    |          | 1/1 |                     |          |          |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp |     | First Run | Timestamp |               |       |     |
| -------- | --------- | --- | --------- | --------- | ------------- | ----- | --- |
|          |           |     |           |           | Failure Count | Count |     |
Iteration
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 128

-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- | --- |
| lc_asic                | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 108 2019-07-31         | 16:43:37 | 2019-07-31          | 07:46:03 |     |     |     |
| poe_ctrlr_1_q1         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:03 |     |     |     |
| poe_ctrlr_1_q2         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:04 |     |     |     |
| poe_ctrlr_1_q3         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:04 |     |     |     |
| poe_ctrlr_2_q1         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:05 |     |     |     |
| poe_ctrlr_2_q2         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:05 |     |     |     |
| poe_ctrlr_2_q3         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:05 |     |     |     |
| poe_ctrlr_3_q1         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:06 |     |     |     |
| poe_ctrlr_3_q2         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:06 |     |     |     |
| poe_ctrlr_3_q3         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:17 | 2019-07-31          | 07:46:06 |     |     |     |
| poe_ctrlr_4_q1         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:17 | 2019-07-31          | 07:46:07 |     |     |     |
| poe_ctrlr_4_q2         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:17 | 2019-07-31          | 07:46:07 |     |     |     |
| poe_ctrlr_4_q3         | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:17 | 2019-07-31          | 07:46:08 |     |     |     |
| Module : FanTray       | 1/1      |                     |          |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --- |
|          |           |           |           | Failure Count | Count |     |
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- | --- |
| ft1_eeprom             | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 4 2019-07-31           | 16:08:33 | 2019-07-31          | 07:44:54 |     |     |     |
| Module : FanTray       | 1/2      |                     |          |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --- |
|          |           |           |           | Failure Count | Count |     |
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          | ------------------- |          |     |     |     |
| ---------------------- | -------- | ------------------- | -------- | --- | --- | --- |
| ft2_eeprom             | Pass     | 0x0                 | 0x0      |     | 0   | 0   |
| 3 2019-07-31           | 16:07:50 | 2019-07-31          | 07:44:54 |     |     |     |
Showingdiagnostictestresultsindetailformatforaspecifiedmoduleona6300switch:
| switch# show              | diagnostic | management-module |     | detail |     |     |
| ------------------------- | ---------- | ----------------- | --- | ------ | --- | --- |
| Module : ManagementModule |            | 1/1               |     |        |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |     |     |     |
| -------- | --------- | --------- | --------- | --- | --- | --- |
RuntimeDiagnostics|129

|     |     |     |     |     | Failure Count | Count |     |
| --- | --- | --- | --- | --- | ------------- | ----- | --- |
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
| - -------------------- |          |     | ------------------- |          |          |     |     |
| ---------------------- | -------- | --- | ------------------- | -------- | -------- | --- | --- |
| ddr_cecount            | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:38 |     | 2019-07-31          |          | 07:44:55 |     |     |
| emmc                   | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| fan_ctrlr              | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| fepld                  | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:38 |     | 2019-07-31          |          | 07:44:54 |     |     |
| fru_eeprom             | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:54 |          |     |     |
| fru_eeprom_ul          | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:54 |          |     |     |
| mm_lcb                 | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:37 |     | 2019-07-31          |          | 07:44:54 |     |     |
| pmc                    | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 109 2019-07-31         | 16:43:37 |     | 2019-07-31          |          | 07:44:54 |     |     |
| rdimm_spd              | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| rdimm_tmp              | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| rtc                    | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| tmp1                   | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
| tmp2                   | Pass     | 0x0 |                     | 0x0      |          | 0   | 0   |
| 4 2019-07-31           | 16:08:04 |     | 2019-07-31          | 07:44:55 |          |     |     |
Showingdiagnostictestresultsinbriefformatforallmodulesona6400switch:
| switch# show | diagnostic |     | brief       |     |         |     |     |
| ------------ | ---------- | --- | ----------- | --- | ------- | --- | --- |
| Module       |            | ID  | Diagnostics |     | Success |     |     |
Performed
| -------------------- |     | ----- | ----------- |     | ------- |     |     |
| -------------------- | --- | ----- | ----------- | --- | ------- | --- | --- |
| ManagementModule     |     | 1/1   |             | 19  | 100%    |     |     |
| LineModule           |     | 1/3   |             | 24  | 100%    |     |     |
| LineModule           |     | 1/7   |             | 12  | 100%    |     |     |
| LineModule           |     | 1/5   |             | 24  | 100%    |     |     |
| LineModule           |     | 1/4   |             | 24  | 100%    |     |     |
| LineModule           |     | 1/6   |             | 24  | 100%    |     |     |
| Fabric               |     | 1/1   |             |     | 6 100%  |     |     |
| FanTray              |     | 1/2   |             |     | 2 100%  |     |     |
| FanTray              |     | 1/1   |             |     | 2 100%  |     |     |
Showingdiagnostictestresultsinbriefformatforaspecifiedmoduleona6400switch:
| switch# show | diagnostic |     | management-module |     | brief   |     |     |
| ------------ | ---------- | --- | ----------------- | --- | ------- | --- | --- |
| Module       |            | ID  | Diagnostics       |     | Success |     |     |
Performed
| -------------------- |     | ----- | ----------- |     | ------- |     |     |
| -------------------- | --- | ----- | ----------- | --- | ------- | --- | --- |
| ManagementModule     |     | 1/1   |             | 19  | 100%    |     |     |
Showingdiagnostictestresultsindetailformatforaspecifiedmoduleona6400switch:
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 130

| switch# show              | diagnostic | management-module | detail |     |     |
| ------------------------- | ---------- | ----------------- | ------ | --- | --- |
| Module : ManagementModule |            | 1/1               |        |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestp |     |               |       |     |
| -------- | ------- | --- | ------------- | ----- | --- |
|          |         |     | Failure Count | Count |     |
Iteration
-------------- ------ ---------- ------------ ------------- ------------- --------
- ----------------
| curr_sensor   | Pass  | 0x0 0x0 |     | 0   | 0   |
| ------------- | ----- | ------- | --- | --- | --- |
| 2 2019-10-14  | 00:25 |         |     |     |     |
| ddr_cecount   | Pass  | 0x0 0x0 |     | 0   | 0   |
| 34 2019-10-14 | 01:26 |         |     |     |     |
| eeprom        | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:25 |         |     |     |     |
| eeprom_ul     | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:25 |         |     |     |     |
| emmc          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:26 |         |     |     |     |
| icbbp         | Pass  | 0x0 0x0 |     | 0   | 0   |
| 34 2019-10-14 | 01:24 |         |     |     |     |
| icbx          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 34 2019-10-14 | 01:25 |         |     |     |     |
| ledpld        | Pass  | 0x0 0x0 |     | 0   | 0   |
| 34 2019-10-14 | 01:24 |         |     |     |     |
| mm_mcb        | Pass  | 0x0 0x0 |     | 0   | 0   |
| 34 2019-10-14 | 01:24 |         |     |     |     |
| psu1          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:27 |         |     |     |     |
| psu1_eeprom   | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:26 |         |     |     |     |
| psu2          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:27 |         |     |     |     |
| psu2_eeprom   | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:27 |         |     |     |     |
| rdimm_spd     | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:26 |         |     |     |     |
| rdimm_tmp     | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:26 |         |     |     |     |
| rtc           | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:26 |         |     |     |     |
| tmp1          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:25 |         |     |     |     |
| tmp2          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:25 |         |     |     |     |
| tmp3          | Pass  | 0x0 0x0 |     | 0   | 0   |
| 2 2019-10-14  | 00:25 |         |     |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Release Modification
10.07orearlier --
| Command Information |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
RuntimeDiagnostics|131

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400            |        |        | rightsforthiscommand. |
| --------------- | ------ | ------ | --------------------- |
| show diagnostic |        | events |                       |
| show diagnostic | events |        |                       |
Description
Displaysthediagnosticrelatedeventlogs.
Example
Showingdiagnosticrelatedeventlogs:
| switch# | show diagnostic | events |     |
| ------- | --------------- | ------ | --- |
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
Showingdiagnosticrelatedeventlogs(Outputfroma6400switch):
| switch# | show diagnostic | events |     |
| ------- | --------------- | ------ | --- |
---------------------------------------------------
| Event logs | from current | boot |     |
| ---------- | ------------ | ---- | --- |
---------------------------------------------------
2019-10-17T20:27:04.066486+00:00 6405 hhmd[9237]: Event|3002|LOG_
ERR|LC|1/6|Diagnostic brd_tmp1 failed with error code 0x1000000 on line card 4
2019-10-17T20:27:04.102968+00:00 6405 hhmd[9237]: Event|3002|LOG_
ERR|LC|1/3|Diagnostic brd_tmp1 failed with error code 0x1000000 on line card 1
2019-10-17T20:27:04.117467+00:00 6405 hhmd[9237]: Event|3002|LOG_
ERR|LC|1/5|Diagnostic brd_tmp1 failed with error code 0x1000000 on line card 3
2019-10-17T20:27:04.210276+00:00 6405 hhmd[9237]: Event|3002|LOG_
ERR|LC|1/4|Diagnostic brd_tmp1 failed with error code 0x1000000 on line card 2
2019-10-17T20:27:04.212133+00:00 6405 hhmd[9237]: Event|3002|LOG_
ERR|LC|1/7|Diagnostic brd_tmp1 failed with error code 0x1000000 on line card 5
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History |     |              |
| -------------- | ------- | --- | ------------ |
| Release        |         |     | Modification |
| 10.07orearlier |         |     | --           |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 132

Command Information

Platforms

Command context

Authority

6300
6400

Manager (#)

Administrators or local user group members with execution
rights for this command.

Runtime Diagnostics | 133

Chapter 15

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

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: admin
SVOS>
..........
..........

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: reboot
reboot: Restarting system

.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

134

|     | Looking | for | SVOS. |     |     |     |     |     |
| --- | ------- | --- | ----- | --- | --- | --- | --- | --- |
Primary SVOS: Checking...Loading...Finding...Verifying...Booting...
|     | ServiceOS |     | Information: |     |                        |          |     |     |
| --- | --------- | --- | ------------ | --- | ---------------------- | -------- | --- | --- |
|     | Version:  |     |              |     | FL.01.07.0002-internal |          |     |     |
|     | Build     |     | Date:        |     | 2020-09-03             | 10:38:03 | PDT |     |
Build ID: ServiceOS:FL.01.07.0002-internal:1a017598b673:202009031038
|     | SHA: |     |     |     | 1a017598b6738448ef679175712e022a966eca88 |     |     |     |
| --- | ---- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
..............
..............
To reboot without logging in, enter 'reboot' as the login user name.
|     | ServiceOS |     | login: | zeroize |     |     |     |     |
| --- | --------- | --- | ------ | ------- | --- | --- | --- | --- |
This will securely erase all customer data, including passwords, and
|     | reset    | the    | switch   | to factory | defaults. |          |        |                  |
| --- | -------- | ------ | -------- | ---------- | --------- | -------- | ------ | ---------------- |
|     | This     | action | requires | proof      | of        | physical | access | via a USB drive. |
|     | * Create |        | a FAT32  | formatted  | USB       | drive    |        |                  |
* Create a file in the root directory of the USB drive named zeroize.txt
* Type the following serial number into the zeroize.txt file: SG9ZKN7050
|     | * Insert  |        | the USB | drive     | into   | the target | module   |     |
| --- | --------- | ------ | ------- | --------- | ------ | ---------- | -------- | --- |
|     | * Confirm |        | the     | following | prompt | to         | continue |     |
|     | Continue  | (y/n)? |         | y         |        |            |          |     |
############################WARNING############################
This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the
|     | switch | unavailable |      | until   | the zeroization |     | is complete. |              |
| --- | ------ | ----------- | ---- | ------- | --------------- | --- | ------------ | ------------ |
|     | This   | should      | take | several | minutes         | to  | one hour     | to complete. |
############################WARNING############################
|         | Continue | (y/n)?     |      | y        |     |     |     |     |
| ------- | -------- | ---------- | ---- | -------- | --- | --- | --- | --- |
|         | reboot:  | Restarting |      | system   |     |     |     |     |
| Service |          | OS         | user | accounts |     |     |     |     |
ServiceOSprovidesasingleadminloginaccount.Bydefault,nopasswordisrequiredtologin.Service
OSwillrequireapasswordiftheServiceOSadminuseraccountpasswordfeatureisenabled.This
settingcanbeenabledordisabledinAOS-CX.
| Service |     | OS  | boot | menu |     |     |     |     |
| ------- | --- | --- | ---- | ---- | --- | --- | --- | --- |
Description
Onboot,theuserispresentedwithaServiceOSversionbannerwithversion,builddate,buildtime,
buildID,andSHAstrings.
Theuseristhenshownthebootimageprofiles.
n Enter0toboottheServiceOSloginCLI.
n Enter1toboottheprimaryfirmwareimage.
n Enter2tobootthesecondaryfirmwareimage.
ServiceOS|135

n Ifnoinputisgivenwithin5seconds,thedefaultbootprofileisselected.Alternatively,pressEnterto
selectthedefaultbootprofile.
Theimageselectedbytheuserduringbootisarun-timedecisiononlyandwillnotpersistacross
reboots.Thedefaultimagecanbeconfiguredusingtheboot set-defaultcommand.
Example
| ServiceOS | Information: |                        |              |
| --------- | ------------ | ---------------------- | ------------ |
| Version:  |              | FL.01.xx.xxxx-internal |              |
| Build     | Date:        | 2020-09-03             | 10:38:03 PDT |
Build ID: ServiceOS:FL.01.xx.xxxx-internal:1a017598b673:202009031038
| SHA: |     | 1a017598b6738448ef679175712e022a966eca88 |     |
| ---- | --- | ---------------------------------------- | --- |
Boot Profiles:
| 0. Service   | OS Console |       |                                  |
| ------------ | ---------- | ----- | -------------------------------- |
| 1. Primary   | Software   | Image | [FL.10.xx.xxxx]                  |
| 2. Secondary | Software   | Image | [FL.10.xx.xxxx-263-g4ac34862e3a] |
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
BuildID
n
n Builddate
ServiceOSwillthenpresentstatusandboottheimage.
Example
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 136

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
ServiceOS|137

ThesemountpointsallowtheusertocopyfilesontheSSD toaUSBstoragedeviceoruploadfiles
usingTFTP.CopyingfilesfromtheSSD isintendedtobeusedundertheguidanceofasupport
engineer(touploadlogsorcoredumpstoHPEsupport).
USBstoragedeviceaccessisprovidedthroughthemountat/mnt/usb.
Theremainingdirectoriesintherootfilesystembin,cli,andlibarenotintendedtobeusedbythe
customer.
| Service | OS  | mount |     | failure |     |     |     |     |     |     |
| ------- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
Description
IftheSSD isdetectedasmissingoranyofthepartitionscouldnotbemounted,ServiceOSwillforcethe
usertoboottotheServiceOSconsoleanddisplayanerrormessageindicatingthatrecoveryshouldbe
attemptedusingtheformatcommand.
Example
| (C) Copyright |     | 2017 | Hewlett |            | Packard | Enterprise |        | Development |     | LP  |
| ------------- | --- | ---- | ------- | ---------- | ------- | ---------- | ------ | ----------- | --- | --- |
|               |     |      |         | RESTRICTED |         | RIGHTS     | LEGEND |             |     |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. | Government |     | under | vendor's |     | standard | commercial |     | license. |     |
| ---- | ---------- | --- | ----- | -------- | --- | -------- | ---------- | --- | -------- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
| Error,    | Could   | not    | mount      | the        | primary | storage      |             | device.  |     |     |
| --------- | ------- | ------ | ---------- | ---------- | ------- | ------------ | ----------- | -------- | --- | --- |
| This      | may     | be due | to         | filesystem |         | or device    | corruption. |          |     |     |
| Please    | attempt |        | to recover |            | using   | the "format" |             | command. |     |     |
| ServiceOS |         | login: |            |            |         |              |             |          |     |     |
| Service   | OS      | CLI    | command    |            |         | list         |             |          |     |     |
Description
AfterlogintoServiceOSCLI,theusermayenterthecommandshelpor?togetafulllistofcommands
andatersedescriptionforeachcommand.Theusermayalsoenter<command>followedby--helpto
getmoredetailedhelpandusageforaspecificcommand.
Example
| SVOS>     | ?   |           |      |           |     |             |           |     |           |     |
| --------- | --- | --------- | ---- | --------- | --- | ----------- | --------- | --- | --------- | --- |
| Available |     | Commands: |      |           |     |             |           |     |           |     |
|           |     |           | ?    | - Display |     | help screen |           |     |           |     |
|           |     |           | cd   | - Change  | the | working     | directory |     |           |     |
|           |     |           | pwd  | - Print   | the | current     | working   |     | directory |     |
|           |     |           | help | - Display |     | help screen |           |     |           |     |
allow-unsafe-updates - Allow non-failsafe updates for a limited amount of time
|     |              |     | boot | - Boot   | a product |                | image |     |     |     |
| --- | ------------ | --- | ---- | -------- | --------- | -------------- | ----- | --- | --- | --- |
|     | config-clear |     |      | - Clears | the       | startup-config |       |     |     |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 138

|     |     |     | diag | - Run | diagnostic | commands |     |     |     |
| --- | --- | --- | ---- | ----- | ---------- | -------- | --- | --- | --- |
erase - Securely erase storage devices on the management module
|         |             | format   |          | - Formats  | and               | partitions      | the            | primary       | storage device   |
| ------- | ----------- | -------- | -------- | ---------- | ----------------- | --------------- | -------------- | ------------- | ---------------- |
|         |             | identify |          | - Prints   | hardware          |                 | identification |               | information      |
|         |             |          | ip       | - Sets     | the OOBM          | Port            | Network        | Configuration |                  |
|         |             |          | mount    | - Mount    | a storage         |                 | device         |               |                  |
|         |             | password |          | - Set      | the admin         | account         | password       |               |                  |
|         |             |          | ping     | - Send     | ICMP ECHO_REQUEST |                 | to             | network       | hosts (IPv4)     |
|         |             | reboot   |          | - Reboots  | the               | Management      | Module         |               |                  |
|         | secure-mode |          |          | - Set      | or retrieve       |                 | the secure     | mode          | setting          |
|         |             |          | sh       | - Launch   | support           | shell           |                |               |                  |
|         |             | umount   |          | - Unmounts | a                 | storage         | device         |               |                  |
|         |             | update   |          | - Update   | a product         |                 | image          |               |                  |
|         |             | version  |          | - Prints   | ServiceOS         |                 | release        | version       | information      |
|         |             |          | cat      | - Prints   | files             | to              | stdout         |               |                  |
|         |             |          | cp       | - Copy     | files             | and directories |                |               |                  |
|         |             |          | du       | - Estimate | file              | space           | usage          |               |                  |
|         |             |          | ls       | - List     | directory         | contents        |                |               |                  |
|         |             | md5sum   |          | - Compute  | and               | check           | md5 message    |               | digest           |
|         |             |          | mkdir    | - Make     | directories       |                 |                |               |                  |
|         |             |          | mv       | - Move     | (rename)          | files           |                |               |                  |
|         |             |          | rm       | - Remove   | files             | or              | directories    |               |                  |
|         |             |          | rmdir    | - Remove   | empty             | directories     |                |               |                  |
|         |             |          | tftp     | - Allows   | transfer          |                 | of files       | to/from       | a remote machine |
|         |             |          | exit     | - Logout   |                   |                 |                |               |                  |
| Enter   | '<command>  |          | --help'  |            | for more          | info            |                |               |                  |
| Service | OS          | CLI      | features |            | and               | limitations     |                |               |                  |
TheServiceOSCLIprovidesbasicshellfunctionalitythatallowsyoutoexecutecommandsandpass
argumentstothosecommandsonly.Thefollowingfeaturesarenotavailable:
n Input/outputredirection(<,>,>>)
n Jobcontrol(&,fg,bg)
n Processpiping(|)
n Fileglobbing(\*)
EventhoughtheServiceOSCLIdoesnotprovidefileglobbingcapabilities,somecommandsmayprovidethis
functionalityinternally.Anexampleisthelscommand.
Thefollowingcommonfeaturesareavailable:
Commandhistory(UpArrow)andsearch(Ctrl-R)
n
n Tabcompletionforfileandfoldernames(notCLIcommands)
n CommandabortusingCtrl-C
| Service | OS  | CLI | commands |     |     |     |     |     |     |
| ------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
boot
boot
Description
ServiceOS|139

Presentsyouwiththebootmenuprompt.Youcanthenspecifywhichbootprofile:primary,secondary,
orServiceOSconsole.
Example
Presentingthebootmenuprompt:
| SVOS>     | boot     |              |                        |     |              |
| --------- | -------- | ------------ | ---------------------- | --- | ------------ |
| ServiceOS |          | Information: |                        |     |              |
|           | Version: |              | FL.01.07.0002-internal |     |              |
|           | Build    | Date:        | 2020-09-03             |     | 10:38:03 PDT |
Build ID: ServiceOS:FL.01.07.0002-internal:1a017598b673:202009031038
|     | SHA: |     | 1a017598b6738448ef679175712e022a966eca88 |     |     |
| --- | ---- | --- | ---------------------------------------- | --- | --- |
Boot Profiles:
| 0.     | Service           | OS Console |       |                              |     |
| ------ | ----------------- | ---------- | ----- | ---------------------------- | --- |
| 1.     | Primary           | Software   | Image | [FL.10.06.0001]              |     |
| 2.     | Secondary         | Software   | Image | [FL.10.08.0000-308-gcfbc0e3] |     |
| Select | profile(primary): |            |       |                              |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        |     | History     |         |     |              |
| -------------- | --- | ----------- | ------- | --- | ------------ |
| Release        |     |             |         |     | Modification |
| 10.07orearlier |     |             |         |     | --           |
| Command        |     | Information |         |     |              |
| Platforms      |     | Command     | context |     | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
cat
cat <FILENAME/DIRECTORY-NAME>
Description
Printsthecontentsofafiletotheconsole.TheServiceOSdoesnotallowcommandoutputredirection,
sothiscommandisonlyusefulforreadingshorttextfiles.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<FILENAME/DIRECTORY-NAME> Showsthecontentsofthespecifiedfileordirectory.
Example
Showingthecontentsof/nos/hosts:
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 140

| SVOS> cat | /nos/hosts            |     |     |           |
| --------- | --------------------- | --- | --- | --------- |
| 127.0.0.1 | localhost.localdomain |     |     | localhost |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
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
cd
/
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
ServiceOS(SVOS>)
rightsforthiscommand.
ServiceOS|141

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
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 142

Parameter

[options]

-d,-P

-a

R,-r

-L

-H

-p

-f

-i

-l,-s

Description

Selects the options for the command.

Specifies the preservation of symlinks (default if -
R).

Same as -dpR.

Specifies recursiveness, all files, and subdirectories
are copied.

Specifies the following of all symlinks.

Specifies the following of symlinks on command
line.

Specifies the preservation of file attributes if
possible.

Specifies the overwriting of a file or directory.

Specifies the prompting before an overwrite.

Specifies the creation of (sym) links.

<SOURCE-FILENAME/SOURCE-DIRECTORY>

Specifies the name of the source file or directory.

<DESTINATION-FLENAME/DESTINATION-DIRECTORY>

Specifies the name of the destination file or
directory.

Example

Copying /home/customers directory to the /home/clients directory:

SVOS> cp /home/customers /home/clients

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

All platforms

ServiceOS (SVOS>)

Administrators or local user group members with execution
rights for this command.

du

Service OS | 143

du [options] <FILENAME/DIRECTORY-NAME>...

Description

Shows estimated disk space used for each file or directory or both.

Parameter

[options]

-a

-L

-H

-d, N

-c

-l

-s

-x

-h

-m

-k

Description

Selects the options for the command.

Show file sizes.

Shows all symlinks.

Shows symlinks on a command line.

Shows limited output to directories (and files with -a) of depth less
than N.

Shows the total disk space usage of all files or directories or both.

Shows the count sizes if hard linked.

Shows only a total for each argument.

Does not show directories on different file systems.

Show sizes in human readable format (1K, 243M, and 2G).

Show sizes in megabytes.

Show sizes in kilobytes (default).

<FILENAME/DIRECTORY-NAME>

Specifies the file or directory or both for displaying a size estimate.

Example

Estimating disk space for the /nos directory:

SVOS> du -ah /nos
196.4M
196.4M
SVOS>

/nos/primary.swi
/nos

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

144

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
erase zeroize
erase zeroize
Description
SecurelyerasesanyuserdatacontainedontheSSD orotherstoragedevicesonthemanagement
module.
Backupalldatabeforerunningthiscommandoralluser/configdatawillbelost.
Usage
Usethiscommandtosecurelyeraseallcustomerdataandrestorethesoftwareenvironmenttofactory
default.Whenyouissuethiscommand:
n SoftwareimagesarecopiedtoRAMtoberestoredoncompletion.
n Allbitsundergoa0>1>0transitiontocompletelyzeroizedata.Thisdataisnotrecoverable.
n Thisfeaturecanbeusedtoremoveallconfigurationsettingsorsystemalterationsfordebuggingor
troubleshooting.
n Thezeroizationprocesstakesapproximatelytwominutes.
Alllogsanddataarelostinthezeroizationprocess.Bestpracticesistocollectallapplicabledatabefore
performingzeroization.
Example
Erasinguserdata:
| SVOS> SVOS>  | erase   | --help  |         |        |            |         |
| ------------ | ------- | ------- | ------- | ------ | ---------- | ------- |
| Usage: erase | zeroize |         |         |        |            |         |
| Securely     | erases  | storage | devices | on the | management | module. |
SVOS>
```
```
| SVOS> erase | zeroize |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- |
############################WARNING############################
This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the
| switch unavailable |      | until   | the     | zeroization | is complete. |              |
| ------------------ | ---- | ------- | ------- | ----------- | ------------ | ------------ |
| This should        | take | several | minutes | to one      | hour         | to complete. |
############################WARNING############################
| Continue           | (y/n)?                 | y      |     |     |     |     |
| ------------------ | ---------------------- | ------ | --- | --- | --- | --- |
| reboot: Restarting |                        | system |     |     |     |     |
| ServiceOS          | Information:           |        |     |     |     |     |
| Version:           | FL.01.07.0002-internal |        |     |     |     |     |
ServiceOS|145

Build Date: 2020-09-02 11:53:34 PDT
Build ID: ServiceOS:FL.01.07.0002-internal:1a017598b673:202009031038
SHA: 1a017598b6738448ef679175712e022a966eca88

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

For more information on features that use this command, refer to the Diagnostics and Supportability Guide for

your switch model.

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

All platforms

ServiceOS (SVOS>)

Administrators or local user group members with execution
rights for this command.

exit (svos)
exit

Description

Logs the user out from the SVOS> prompt.

Example

Loging the user out from the SVOS> prompt:

SVOS> exit

(C) Copyright 2025 Hewlett Packard Enterprise Development LP

RESTRICTED RIGHTS LEGEND

Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
U.S. Government under vendor's standard commercial license.

To reboot without logging in, enter 'reboot' as the login user name.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

146

| ServiceOS | login: |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
ServiceOS(SVOS>)
rightsforthiscommand.
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
| Continue?      | (y/n): | y   |      |                  |     |     |
| -------------- | ------ | --- | ---- | ---------------- | --- | --- |
| Working...This |        | may | take | a few minutes... |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History |     |     |     |              |     |
| -------------- | ------- | --- | --- | --- | ------------ | --- |
| Release        |         |     |     |     | Modification |     |
| 10.07orearlier |         |     |     |     | --           |     |
ServiceOS|147

| Command   | Information |         |           |
| --------- | ----------- | ------- | --------- |
| Platforms | Command     | context | Authority |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
identify
identify
Description
Printstheversionandserialnumberinformationofhardwaredevicesonthemanagementmodule(for
example,FPGAS,PLDs).
Example
Outputfroma6400/6300switch:
| SVOS>               | identify |                 |     |
| ------------------- | -------- | --------------- | --- |
| mc svos_primary     |          | : FL.01.05.0001 |     |
| mc svos_secondary   |          | : FL.01.05.0001 |     |
| mc uboot_single     |          | : FL.01.0001    |     |
| mc uboot_capsule    |          | : FL.01.0001    |     |
| mc pmc_single       |          | : 0x4           |     |
| mc pmc_primary      |          | : 0x4           |     |
| mc pmc_secondary    |          | : 0x4           |     |
| mc mcb_single       |          | : 0x6           |     |
| mc mcb_primary      |          | : 0x6           |     |
| mc mcb_secondary    |          | : 0x6           |     |
| mc mcb_factory      |          | : 0x3           |     |
| mc ledpld_single    |          | : 0x4           |     |
| mc ledpld_primary   |          | : 0x4           |     |
| mc ledpld_secondary |          | : 0x4           |     |
| mc tpm              |          | : 0x102420E     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip
| ip {show | | dhcp | disable | | addr <ADDR-NETMASK-GATEWAY>} |     |
| -------- | ---------------- | ------------------------------ | --- |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 148

Description
ShowsorconfigurestheportwithastaticIPaddress(IPv4only)orenablestheDHCPclientontheport.
AnaddressissetonlyifaDHCPserverisavailabletoprovideone.
Parameter Description
{show | dhcp | disable | addr <ADDR-NETMASK-GATEWAY>} SelectstheoptionsfortheOOBM
port.
show ShowstheOOBMport.
dhcp ConfigurestheportwithaDHCP
address.
disable DisablestheOOBMport.
| addr <ADDR-NETMASK-GATEWAY> |     |     | ConfigurestheportwithastaticIP |
| --------------------------- | --- | --- | ------------------------------ |
address(IPv4only).Specifyaddress,
netmask,andgatewayasA.B.C.D.
Example
ConfiguringtheportwithaDHCPIPaddress:
| SVOS> ip     | dhcp          |     |     |
| ------------ | ------------- | --- | --- |
| SVOS> ip     | show          |     |     |
| Interface    | : Link Up     |     |     |
| IP Address   | : 10.0.26.17  |     |     |
| Subnet Mask: | 255.255.252.0 |     |     |
| Gateway      | : 10.0.24.1   |     |     |
| SVOS> ip     | disable       |     |     |
| SVOS> ip     | show          |     |     |
| Interface    | : Disabled    |     |     |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |                                                    |
| ------------------- | ------- | ------- | -------------------------------------------------- |
| Release             |         |         | Modification                                       |
| 10.07orearlier      |         |         | --                                                 |
| Command Information |         |         |                                                    |
| Platforms           | Command | context | Authority                                          |
| 6300                |         |         | Administratorsorlocalusergroupmemberswithexecution |
ServiceOS(SVOS>)
| 6400 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
ls
ServiceOS|149

ls [<OPTIONS>] [<FILE-NME>]

Description

This command lists directory contents.

Parameter

<OPTIONS>

-1

-a

-A

-C

-x

-d

-L

-H

-R

-p

-F

-l

-i

-n

-s

-e

-h

-r

-S

-X

-v

-c

-t

Description

Specifies options for the command.

Shows one-column output.

Shows entries which start with a period (.).

Shows output similar to -a, but excludes a period (.) and a
double period (..).

Shows output list by columns.

Shows output list by lines.

Shows listing of directory entries instead of contents

Follows symlinks.

Follows symlinks on the command line.

Recurse.

Appends a slash (/) to directory entries.

Appends an indicator to entries. An indicator can be as an
asterisk (*) or slash (/) or equal sign (=) or at sign (@) or pipe
(|).

Shows the output in a long listing format.

Shows the list inode numbers.

Shows a list of numeric UIDs and GIDs instead of names.

Shows a list of allocated blocks.

Shows in one column a list with the full date and time.

Shows list sizes in human readable format (1K, 243M, 2G)
with a one-column output.

Shows in one column a sort in reverse order.

Shows in one column a sort by size.

Shows in the output sort by extension.

Shows in one column a sort by version.

With -l, it shows a sort in one column by ctime.

With -l, it shows a sort by mtime.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

150

| Parameter |     |     |     |     |     | Description                                     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| -u        |     |     |     |     |     | With-l,sortbyatime.                             |     |     |     |
| -c        |     |     |     |     |     | With-l,itshowsasortinonecolumnbyctime           |     |     |     |
| -w <N>    |     |     |     |     |     | Assumesthattheterminalhasthenumberofcolumnswide |     |     |     |
asspecifiedby<N>.
| --color[={always |     |     | | never | | auto}] |     |     |     |     |     |
| ---------------- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- |
Controlscolorintheoutput.
| <FILE-NAME> |     |     |     |     |     | Specifiesthenameofthefiletolist. |     |     |     |
| ----------- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
Example
Listingdirectorycontents:
| SVOS>      | ls -la | /nos |     |     |           |       |     |          |             |
| ---------- | ------ | ---- | --- | --- | --------- | ----- | --- | -------- | ----------- |
| drwxr-xr-x |        | 3    | 0   | 0   |           | 4096  | Nov | 21 03:19 | .           |
| drwxr-xr-x |        | 11   | 0   | 0   |           | 220   | Nov | 21 03:21 | ..          |
| drwx------ |        | 2    | 0   | 0   |           | 16384 | Nov | 21 03:20 | lost+found  |
| -rwxr-xr-x |        | 1    | 0   | 0   | 205957424 |       | Nov | 21 03:19 | primary.swi |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |     |         |              |     |     |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- | --- | --- | --- |
| Release        |             |         |     |         | Modification |     |     |     |     |
| 10.07orearlier |             |         |     |         | --           |     |     |     |     |
| Command        | Information |         |     |         |              |     |     |     |     |
| Platforms      |             | Command |     | context | Authority    |     |     |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
md5sum
| md5sum [-c | |   | -s | -w] | [<FILE-NAME>] |     |     |     |     |     |     |
| ---------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
Description
ThiscommandcomputesandcheckstheMD5messagedigest.
| Parameter |          |     |     |     | Description |     |     |     |     |
| --------- | -------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
| [-c |     | -s | -w] |     |     |     |             |     |     |     |     |
Selectstheoptionsforthecommand.
ServiceOS|151

| Parameter   |     |     | Description                                           |
| ----------- | --- | --- | ----------------------------------------------------- |
| -c          |     |     | Specifiestocheckthesumsagainstthelistinfiles.         |
| -s          |     |     | Specifiesnotoutputanything,statuscodeshowssuccess.    |
| -w          |     |     | Specifiestowarnaboutimproperlyformattedchecksumlines. |
| <FILE-NAME> |     |     | Specifiesthefilenametorunthechecksumagainst.          |
Example
ComputingandcheckingtheMD5messagedigestfor/nos/primary.swi:
| SVOS> md5sum                     | /nos/primary.swi |     |                  |
| -------------------------------- | ---------------- | --- | ---------------- |
| 93ffc89e7ec357854704d8e450c4b7ab |                  |     | /nos/primary.swi |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
ServiceOS(SVOS>)
rightsforthiscommand.
mkdir
| mkdir [-m | | -p] [<DIRECTORY-NAME>] |     |     |
| ----------- | ---------------------- | --- | --- |
Description
Thiscommandmakesdirectories.
| Parameter |     |     | Description                                             |
| --------- | --- | --- | ------------------------------------------------------- |
| [-m | -p] |     |     | Specifiestheoptionsforthecommand.                       |
| -m        |     |     | Specifiesthemode.                                       |
| -p        |     |     | Specifiestomakeparentdirectoriesasneededwithnoerrorsfor |
pre-existingdirectories.
| <DIRECTORY-NAME> |     |     | Specifiesthedirectorytocreate. |
| ---------------- | --- | --- | ------------------------------ |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 152

Example
Makingthedirdirectory:
SVOS>
mkdir dir
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
ServiceOS(SVOS>)
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
| MountingalloftheSSD | partitions: |     |     |
| ------------------- | ----------- | --- | --- |
| SVOS> mount         | all         |     |     |
| SVOS> mount         | usb         |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
ServiceOS|153

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
-i
Specifiestopromptbeforeoverwriting.
| -n  |     |     | Specifiestonotoverwriteanexistingfile. |
| --- | --- | --- | -------------------------------------- |
Example
Movingthefilenamedmyfile:
| SVOS> mv | myfile |     |     |
| -------- | ------ | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| password | (svos) |     |     |
| -------- | ------ | --- | --- |
password
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 154

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
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ping (svos)
ping <HOST-IP-ADDRESS>
Description
Pingsnetworkhostsfordebugpurposes.
| Parameter         |     |     | Description                |     |
| ----------------- | --- | --- | -------------------------- | --- |
| <HOST-IP-ADDRESS> |     |     | SpecifiesthehostIPaddress. |     |
Example
Pinginganetworkhost:
| SVOS> ping     | 10.0.8.10       |       |                   |     |
| -------------- | --------------- | ----- | ----------------- | --- |
| PING 10.0.8.10 | (10.0.8.10):    | 56    | data bytes        |     |
| 64 bytes       | from 10.0.8.10: | seq=0 | ttl=63 time=3.496 | ms  |
| 64 bytes       | from 10.0.8.10: | seq=1 | ttl=63 time=0.367 | ms  |
ServiceOS|155

| 64 bytes | from 10.0.8.10: | seq=2 | ttl=63 | time=0.380 | ms  |
| -------- | --------------- | ----- | ------ | ---------- | --- |
| 64 bytes | from 10.0.8.10: | seq=3 | ttl=63 | time=0.282 | ms  |
| 64 bytes | from 10.0.8.10: | seq=4 | ttl=63 | time=0.669 | ms  |
^C
| --- 10.0.8.10 | ping         | statistics          | ---       |     |             |
| ------------- | ------------ | ------------------- | --------- | --- | ----------- |
| 5 packets     | transmitted, | 5 packets           | received, | 0%  | packet loss |
| round-trip    | min/avg/max  | = 0.282/1.038/3.496 |           | ms  |             |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
6300 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --------------------- | --- | --- |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |     |              |     |     |
| -------------- | ----------- | --- | ------------ | --- | --- |
| Release        |             |     | Modification |     |     |
| 10.07orearlier |             |     | --           |     |     |
| Command        | Information |     |              |     |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 156

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
reboot
reboot
Description
RebootstheManagementModule.
Example
Rebootingthemanagementmodule:
| SVOS>   | reboot     |        |     |
| ------- | ---------- | ------ | --- |
| reboot: | Restarting | system |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
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
-f
Neverpromptbeforeremovingfilesordirectories.
| -i   |     |     | Alwayspromptbeforeremovingfilesordirectories. |
| ---- | --- | --- | --------------------------------------------- |
| -R | | -r  |     |                                               |
Recursive.
ServiceOS|157

Example
Removingthefilenamedfoo:
SVOS>
rm foo
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
ServiceOS(SVOS>)
rightsforthiscommand.
rmdir
| rmdir [-p] <DIRECTORY-NAME> |     |     |     |
| --------------------------- | --- | --- | --- |
Description
Removesemptydirectories.
| Parameter |     |     | Description                         |
| --------- | --- | --- | ----------------------------------- |
| -p        |     |     | Specifiestoremoveparentdirectories. |
Example
Removingtheemptyfoodirectory:
| SVOS> rmdir | foo |     |     |
| ----------- | --- | --- | --- |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
| 10.07orearlier  |     |     | --           |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 158

| Command   | Information |         |     |         |           |     |     |     |
| --------- | ----------- | ------- | --- | ------- | --------- | --- | --- | --- |
| Platforms |             | Command |     | context | Authority |     |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| secure-mode |           | (Service |            | OS) |           |     |     |     |
| ----------- | --------- | -------- | ---------- | --- | --------- | --- | --- | --- |
| secure-mode | <enhanced |          | | standard |     | | status> |     |     |     |
Description
Setsthesecuremodetoenhancedorstandardsecuremode.Alsocandisplaythecurrentsecuremode.
Azeroizationisrequiredbeforeswitchingbetweenenhancedandstandardsecuremodes.
Thecommandalsodisplaysamessagenotifyingtheuserthattheyarealreadyinthetargetedsecure
mode.
Example
Settingthesecuremodetoenhancedorstandard:
| SVOS>  | secure-mode |     | --help    |     |            |           |     |     |
| ------ | ----------- | --- | --------- | --- | ---------- | --------- | --- | --- |
| Usage: | secure-mode |     | <enhanced |     | | standard | | status> |     |     |
Set or retrieve the secure mode setting. Requires a zeroization to change modes.
SVOS>
```
```
| SVOS> | secure-mode |     | enhanced |     |     |     |     |     |
| ----- | ----------- | --- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| This | will set | the | switch | into | enhanced | secure | mode. | Before |
| ---- | -------- | --- | ------ | ---- | -------- | ------ | ----- | ------ |
enhanced secure mode is enabled, the switch must securely erase
| all customer |                 | data | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | --------------- | ---- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This         | will initiate   |      | a reboot | and          | render | the switch |              | unavailable |
| until        | the zeroization |      |          | is complete. |        |            |              |             |
| This         | should          | take | several  | minutes      | to     | one hour   | to complete. |             |
############################WARNING############################
| Continue | (y/n)?     |     | y      |     |     |     |     |     |
| -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
| reboot:  | Restarting |     | system |     |     |     |     |     |
```
```
| SVOS> | secure-mode |     | standard |     |     |     |     |     |
| ----- | ----------- | --- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| This | will set | the | switch | into | standard | secure | mode. | Before |
| ---- | -------- | --- | ------ | ---- | -------- | ------ | ----- | ------ |
standard secure mode is enabled, the switch must securely erase
| all customer |                 | data | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | --------------- | ---- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This         | will initiate   |      | a reboot | and          | render | the switch |              | unavailable |
| until        | the zeroization |      |          | is complete. |        |            |              |             |
| This         | should          | take | several  | minutes      | to     | one hour   | to complete. |             |
############################WARNING############################
| Continue | (y/n)?     |     | y      |     |     |     |     |     |
| -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
| reboot:  | Restarting |     | system |     |     |     |     |     |
```
ServiceOS|159

```
| SVOS> secure-mode |     | standard |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- |
############################WARNING############################
| Secure | mode is already | set | to standard. |     | Setting | it again will |
| ------ | --------------- | --- | ------------ | --- | ------- | ------------- |
repeat the zeroization process. The switch must securely erase
| all customer | data         | and reset | the       | switch | to factory | defaults.    |
| ------------ | ------------ | --------- | --------- | ------ | ---------- | ------------ |
| This will    | initiate     | a reboot  | and       | render | the switch | unavailable  |
| until the    | zeroization  | is        | complete. |        |            |              |
| This should  | take several |           | minutes   | to     | one hour   | to complete. |
############################WARNING############################
| Continue | (y/n)? y   |        |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |
```
```
| SVOS> secure-mode |             | status  |     |     |     |     |
| ----------------- | ----------- | ------- | --- | --- | --- | --- |
| enhanced          | secure mode | is set. |     |     |     |     |
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |     |              |     |     |
| -------------- | ----------- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |     | Modification |     |     |
| 10.07orearlier |             |         |     | --           |     |     |
| Command        | Information |         |     |              |     |     |
| Platforms      | Command     | context |     | Authority    |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sh
sh
Description
Launchesabashshellforsupportpurposes.Toquitbash,enterexit.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Launchingabashshell:
SVOS>
sh
switch:/cli/fs/home#
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 160

Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
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
Example
EnabllingpasswordauthenticationforServiceOS
| switch(config)# |     |     | system serviceos | password-prompt |
| --------------- | --- | --- | ---------------- | --------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |     |     |              |
| -------------- | ----------- | --- | --- | ------------ |
| Release        |             |     |     | Modification |
| 10.07orearlier |             |     |     | --           |
| Command        | Information |     |     |              |
ServiceOS|161

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| SVOS> umount | all |     |     |
| ------------ | --- | --- | --- |
| SVOS> umount | usb |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
update
| update {primary | | secondary} | <IMAGE> |     |
| --------------- | ------------ | ------- | --- |
Description
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 162

Verifiesandinstallsaproductimage.Theusercanselecttheprimaryorsecondarybootprofileto
updateandthelocationofthefile.
| Parameter  |            | Description |     |
| ---------- | ---------- | ----------- | --- |
| {primary | | secondary} |             |     |
Selectseithertheprimaryorsecondaryimage.
| <IMAGE> |     | Specifiestheimagename. |     |
| ------- | --- | ---------------------- | --- |
Examples
UpdatingthesoftwareimageusingTFTP:
TheOOBMportisdisabledonfirstbootandmustbeenabledusingtheipcommand.
| SVOS> ip     | dhcp                    |              |            |
| ------------ | ----------------------- | ------------ | ---------- |
| SVOS> ip     | show                    |              |            |
| Interface    | : Link Up               |              |            |
| IP Address   | : 192.0.2.22            |              |            |
| Subnet Mask: | 255.255.200.20          |              |            |
| Gateway      | : 10.0.24.1             |              |            |
| SVOS> tftp   | -g -r XL.10.00.0001.swi | -l image.swi | 192.4.8.10 |
XL.10.00.0001.swi 100% |*******************************| 178M 0:00:00 ETA
SVOS> ls
image.swi
| SVOS> update | primary image.swi         |     |     |
| ------------ | ------------------------- | --- | --- |
| Updating     | primary software image... |     |     |
| Verifying    | image...                  |     |     |
Done
UpdatethesoftwareimageusingUSB:
ThisexampleassumesthattheuserhaspreloadedaUSBflashdrivewiththeimagetobeupdated.Theimage
nameontheflashdriveisnotimportant.
| SVOS> mount | usb      |     |     |
| ----------- | -------- | --- | --- |
| SVOS> ls    | /mnt/usb |     |     |
image.swi
| SVOS> update | primary /mnt/usb/image.swi |     |     |
| ------------ | -------------------------- | --- | --- |
| Updating     | primary software image...  |     |     |
| Verifying    | image...                   |     |     |
Done
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History |              |     |
| -------------- | ------- | ------------ | --- |
| Release        |         | Modification |     |
| 10.07orearlier |         | --           |     |
ServiceOS|163

| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
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
| -g  |     |     | Specifiestogetafile. |     |
| --- | --- | --- | -------------------- | --- |
-l
Specifiesalocalfile.
| -p  |     |     | Specifiestoputafileinremotelocation. |     |
| --- | --- | --- | ------------------------------------ | --- |
-r <REMOTE-FILE>
Specifiesaremotefile.
| <PORT> |     |     | Specifiestheportfortransfer.Ifnoportoptionis |     |
| ------ | --- | --- | -------------------------------------------- | --- |
specified,TFTPusesthestandardUDPport69bydefault.
Example
Transferringfiles:
| SVOS> tftp | -b 65464 | -g -r XL.10.00.0002.swi.swi |     | 192.0.2.1 |
| ---------- | -------- | --------------------------- | --- | --------- |
XL.10.00.0002 100% |*******************************| 178M 0:00:00 ETA
SVOS>
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 164

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6300 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
| 6400                |     |     | rightsforthiscommand. |
| ------------------- | --- | --- | --------------------- |
| version (ServiceOS) |     |     |                       |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ServiceOS|165

Chapter 16
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
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
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
166
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

Description
Displayswhetheranyprogrammabledevicesareinneedofanupdate.
Withoutthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetothecurrently
runningAOS-CXimage.
Withthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetoanAOS-CXimagefile
inthepersistentstorageoftheswitch,whichmightbedifferentfromthecurrentlyrunningimage.If
eithertheprimaryorsecondaryparameterisspecified,thiscommandqueriesthatspecificAOS-CX
imagefile.Otherwise,itqueriesthedefaultAOS-CXimagefileassetbythemostrecentboot systemor
boot set-defaultcommand.
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
In-SystemProgramming|167

Chapter 17

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

168

POSTrunsmemorybuilt-inselftest(BISTs)andfront-endportloopbacktests.MemoryBISTsverifythe
internalandexternalmemoryblockspresentinthemodule.Thememorytablesarecriticalforproper
functionalityofthesystemsoanyfailuresinthesetestsresultsinthecorrespondingsubsystemtobe
markedas"Failed"andthusthatsubsystemisnotavailableforuse.
Front-endportloopbacktestsverifythephysicalportfront-endinterface.Thesetestscheckifa
particularinterfacecanfunctionproperly.Atestfailuremeansthataparticularinterfacehasbeen
markedas"Failed"andisnowunavailableforuse.
On6300and6400switches,theline-moduleandfabric-moduleselftestisrunregardlessoffastboot
setting.Theinterfaceselftestisonlyrunwhenfastbootisdisabled.
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
Selftest|169

!
| vlan 1    |       |     |     |
| --------- | ----- | --- | --- |
| interface | 1/1/1 |     |     |
no shutdown
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 170

Displayingtheoutputwhenfastbootisdisabledonan8400ora6400switch:
| switch#         | show selftest       |               |            |                     |                     |          |
| --------------- | ------------------- | ------------- | ---------- | ------------------- | ------------------- | -------- |
| Name            | Id Status           |               | ErrorCode  |                     | LastRunTime         |          |
| ----------      | ---- -------------- |               | ---------- |                     | ------------------- |          |
| LineModule      | 1/1 passed          |               | 0x0        |                     | 2016-10-15          | 10:10:09 |
| LineModule      | 1/2 failed          |               | 0x09       |                     | 2016-10-15          | 10:10:56 |
| Fabric 1/1      | passed              |               | 0x0        |                     | 2016-10-15          | 10:10:09 |
| Fabric 1/2      | failed              |               | 0x1E       |                     | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | line-module   |            |                     |                     |          |
| Name            | Id Status           |               | ErrorCode  |                     | LastRunTime         |          |
| ----------      | ---- -------------- |               | ---------  |                     | ------------------- |          |
| LineModule      | 1/1 passed          |               | 0x0        |                     | 2016-10-15          | 10:10:09 |
| LineModule      | 1/2 failed          |               | 0x09       |                     | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | fabric-module |            |                     |                     |          |
| Name Id         | Status              |               | ErrorCode  |                     | LastRunTime         |          |
| ------ -------- | --------------      |               | ---------  |                     | ------------------- |          |
| Fabric 1/1      | passed              |               | 0x0        |                     | 2016-10-15          | 10:10:09 |
| Fabric 1/2      | failed              |               | 0x1E       |                     | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | fabric-module |            | 1/2                 |                     |          |
| Name Id         | Status              |               | ErrorCode  |                     | LastRunTime         |          |
| ------ -------- | --------------      |               | ---------  |                     | ------------------- |          |
| Fabric 1/2      | failed              |               | 0x11       |                     | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | line-module   |            | 1/10                |                     |          |
| Name            | Id Status           |               | ErrorCode  |                     | LastRunTime         |          |
| ----------      | ---- -------------- |               | ---------  |                     | ------------------- |          |
| LineModule      | 1/10 failed         |               | 0x1A       |                     | 2016-10-15          | 10:10:56 |
| switch#         | show selftest       | interface     | 1/2/2      |                     |                     |          |
| Name            | Status              | ErrorCode     |            | LastRunTime         |                     |          |
| -------         | --------------      | ---------     |            | ------------------- |                     |          |
| 1/2/2           | passed              | 0x0           |            | 2016-11-19          | 05:10:11            |          |
| switch#         | show selftest       | line-module   |            | 1/3 interface       |                     |          |
| Name            | Status              | ErrorCode     |            | LastRunTime         |                     |          |
| -------         | --------------      | ---------     |            | ------------------- |                     |          |
| 1/3/1           | passed              | 0x0           |            | 2016-11-19          | 05:10:11            |          |
| 1/3/2           | passed              | 0x0           |            | 2016-11-19          | 05:10:11            |          |
| 1/3/3           | passed              | 0x0           |            | 2016-11-19          | 05:10:11            |          |
| 1/3/31          | failed              | 0x20          |            | 2016-11-19          | 05:10:11            |          |
Displayingtheoutputwhenfastbootisdisabledona6300switch:
| switch# | show selftest | interface |           |     |             |     |
| ------- | ------------- | --------- | --------- | --- | ----------- | --- |
| Name    | Status        |           | ErrorCode |     | LastRunTime |     |
---------- ----------------- ---------------- -------------------
| 1/1/2 | skipped |     | 0x0 |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- |
Selftest|171

| 1/1/44  | skipped       |           | 0x0       |     |             |
| ------- | ------------- | --------- | --------- | --- | ----------- |
| 1/1/46  | skipped       |           | 0x0       |     |             |
| switch# | show selftest | interface | 1/1/1     |     |             |
| Name    | Status        |           | ErrorCode |     | LastRunTime |
---------- ----------------- ---------------- -------------------
| 1/1/1 | skipped |     | 0x0 |     |     |
| ----- | ------- | --- | --- | --- | --- |
Displayingtheoutputwhenfastbootisenabledona6400switch:
| switch#    | show selftest       |     |            |     |                     |
| ---------- | ------------------- | --- | ---------- | --- | ------------------- |
| Name       | Id Status           |     | ErrorCode  |     | LastRunTime         |
| ---------- | ---- -------------- |     | ---------- |     | ------------------- |
| LineModule | 1/1 passed          |     | 0x0        |     |                     |
| LineModule | 1/2 passed          |     | 0x0        |     |                     |
| Fabric     | 1/1 passed          |     | 0x0        |     |                     |
| Fabric     | 1/2 passed          |     | 0x0        |     |                     |
switch#
|                 | show selftest       | line-module   |            |     |                     |
| --------------- | ------------------- | ------------- | ---------- | --- | ------------------- |
| Name            | Id Status           |               | ErrorCode  |     | LastRunTime         |
| ----------      | ---- -------------- |               | ---------  |     | ------------------- |
| LineModule      | 1/1 passed          |               | 0x0        |     |                     |
| LineModule      | 1/2 passed          |               | 0x0        |     |                     |
| switch#         | show selftest       | fabric-module |            |     |                     |
| Name            | Id Status           |               | ErrorCode  |     | LastRunTime         |
| ----------      | ---- -------------- |               | ---------- |     | ------------------- |
| Fabric          | 1/1 passed          |               | 0x0        |     |                     |
| Fabric          | 1/2 passed          |               | 0x0        |     |                     |
| switch#         | show selftest       | fabric-module |            | 1/2 |                     |
| Name Id         | Status              |               | ErrorCode  |     | LastRunTime         |
| ------ -------- | --------------      |               | ---------  |     | ------------------- |
| Fabric 1/2      | passed              |               | 0x0        |     |                     |
| switch#         | show selftest       | line-module   |            | 1/1 |                     |
| Name            | Id Status           |               | ErrorCode  |     | LastRunTime         |
| ----------      | ---- -------------- |               | ---------  |     | ------------------- |
| LineModule      | 1/1 passed          |               | 0x0        |     |                     |
Displayingtheoutputwhenfastbootisenabled:
| switch# | show selftest  | interface   | 1/1/2 |                     |     |
| ------- | -------------- | ----------- | ----- | ------------------- | --- |
| Name    | Status         | ErrorCode   |       | LastRunTime         |     |
| ------- | -------------- | ---------   |       | ------------------- |     |
| 1/1/2   | skipped        | 0x0         |       |                     |     |
| switch# | show selftest  | line-module |       | 1/1 interface       |     |
| Name    | Status         | ErrorCode   |       | LastRunTime         |     |
| ------- | -------------- | ---------   |       | ------------------- |     |
| 1/1/1   | skipped        | 0x0         |       |                     |     |
| 1/1/2   | skipped        | 0x0         |       |                     |     |
| 1/1/3   | skipped        | 0x0         |       |                     |     |
| 1/1/31  | skipped        | 0x0         |       |                     |     |
Displayingtheoutputwhenfastbootisdisabled:
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 172

Testingtoregisterread/write:
Thistestisrunirrespectiveoffastbootbeingenabledordisabled.
| switch#    | show selftest       |     |                                |          |
| ---------- | ------------------- | --- | ------------------------------ | -------- |
| Name       | Id Status           |     | ErrorCode LastRunTime          |          |
| ---------- | ---- -------------- |     | ---------- ------------------- |          |
| LineModule | 1/1 passed          |     | 0x0 2018-02-16                 | 18:15:53 |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Selftest|173

Chapter 18

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

174

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

Zeroization | 175

Whenyouloginafterzeroization,yougetaprompttocreateapasswordfortheadministratoraccount.Youcan
setthepasswordasblank(tosetthepasswordasblank,hitenterattheprompt)ortype1to32printableASCII
characters,excludingspacesandquestionmarks(?).Formoreinformationonpasswordrequirements,see
PasswordrequirementsintheSecurityGuide.
| switch | login: | admin |     |     |
| ------ | ------ | ----- | --- | --- |
Password:
| Please    | configure     | the 'admin' | user account | password. |
| --------- | ------------- | ----------- | ------------ | --------- |
| Enter new | password:     | *****       |              |           |
| Confirm   | new password: | *****       |              |           |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command        | History     |         |                              |     |
| -------------- | ----------- | ------- | ---------------------------- | --- |
| Release        |             |         | Modification                 |     |
| 10.11.1010     |             |         | IntroducederaseallCLIcommand |     |
| 10.07orearlier |             |         | --                           |     |
| Command        | Information |         |                              |     |
| Platforms      | Command     | context | Authority                    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 176

Chapter 19
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
177
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringconsoleloggingintheconsolesession:
| switch(config)#  |     | logging | console |              |              |               |
| ---------------- | --- | ------- | ------- | ------------ | ------------ | ------------- |
| Terminal-monitor |     | is      | enabled | successfully |              |               |
| switch(config)#  |     | logging | console |              | notify all   |               |
| Terminal-monitor |     | is      | enabled | successfully |              |               |
| switch(config)#  |     | logging | console |              | notify event | severity info |
| Terminal-monitor |     | is      | enabled | successfully |              |               |
| switch(config)#  |     | logging | console |              | filter lldp  |               |
| Terminal-monitor |     | is      | enabled | successfully |              |               |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command   | History     |     |         |     |                    |     |
| --------- | ----------- | --- | ------- | --- | ------------------ | --- |
| Release   |             |     |         |     | Modification       |     |
| 10.08     |             |     |         |     | Featureintroduced. |     |
| Command   | Information |     |         |     |                    |     |
| Platforms | Command     |     | context |     | Authority          |     |
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
TerminalMonitor|178

| event | debug |     | lldp |     |
| ----- | ----- | --- | ---- | --- |
-------------------------------------
Displayingterminalmonitorwhendisabled:
| switch# show     | terminal-monitor |             |     |     |
| ---------------- | ---------------- | ----------- | --- | --- |
| Terminal-monitor |                  | is disabled |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| terminal-monitor |     | {notify | | severity | | filter} |
| ---------------- | --- | ------- | ---------- | --------- |
terminal-monitor {notify <event|debug|all> | severity <level> | filter <keyword>}
no terminal-monitor
Description
Enablesandsavestheterminalmonitorfeatureintheswitchconfiguration.Itdisplaysalldebuglogor
eventlogorbothdebugandeventlogmessages.Terminalmonitoringcanbefilteredwiththeseverity
optionsorwiththehelpofkeywords.Enablingterminalmonitorwithoutoptionsdisplaysbothdebug
andeventlogwithaseverityerror.
Thenoformofthiscommandremovestheterminalmonitorfeaturefromtheswitchconfigurationand
thecommandwillnotpersist.
| Parameter                |     |     | Description |     |
| ------------------------ | --- | --- | ----------- | --- |
| notify <event|debug|all> |     |     |             |     |
Specifiesthetypeoflognotification.
n Event:Displaystheeventlogmessages.(Default)
n Debug:Displaysthedebuglogmessages.
n All:Displaysbotheventanddebuglogmessages.
severity <level> Specifiestheseveritylevelforthelogs.Thedifferentseverity
levelsareemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries) 179

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
filter <keyword> Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingterminalmonitor:
| switch# terminal-monitor |     |         |              |                     |
| ------------------------ | --- | ------- | ------------ | ------------------- |
| Terminal-monitor         | is  | enabled | successfully |                     |
| switch# terminal-monitor |     |         | notify       | all                 |
| Terminal-monitor         | is  | enabled | successfully |                     |
| switch# terminal-monitor |     |         | notify       | event severity info |
| Terminal-monitor         | is  | enabled | successfully |                     |
| switch# terminal-monitor |     |         | filter       | lldp                |
| Terminal-monitor         | is  | enabled | successfully |                     |
Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor
yourswitchmodel.
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
TerminalMonitor|180

|                 |     |                 |               |        | Chapter  | 20  |
| --------------- | --- | --------------- | ------------- | ------ | -------- | --- |
|                 |     | Troubleshooting |               | Web UI | and REST | API |
| Troubleshooting | Web | UI and REST API | Access Issues |        |          |     |
Thefollowingsectiondescribessymptoms,causesandcorrectiveactionsfor401or404errors.
| HTTP 404 | error when | accessing | the | switch URL |     |     |
| -------- | ---------- | --------- | --- | ---------- | --- | --- |
Symptom
TheswitchisoperationalandyouareusingthecorrectURLfortheswitch,butattemptstoaccessthe
RESTAPIorWebUIresultinanHTTP404"Pagenotfound"error.
Cause
RESTAPIaccessisnotenabledontheVRFthatcorrespondstotheaccessportyouareusing.For
example,youareattemptingtoaccesstheRESTAPIorWebUIfromthemanagement(OOBM)port,and
accessisnotenabledonthemgmtVRF.Bydefault,https-serverisenabledonthemgmtVRFforthe6300
and6400switches.
Action
Usethehttps-server vrfcommandtoenableRESTAPIaccessonthespecifiedVRF.
Forexample:
| switch(config)# | https-server | vrf mgmt |         |                |     |     |
| --------------- | ------------ | -------- | ------- | -------------- | --- | --- |
| HTTP 401        | error "Login | failed:  | session | limit reached" |     |     |
Symptom
ARESTrequestorWebUIloginattemptreturnsresponsecode401andtheresponsebodycontainsthe
followingtextstring:
| Login failed: | session limit | reached |     |     |     |     |
| ------------- | ------------- | ------- | --- | --- | --- | --- |
Cause
AuserattemptedtologintotheRESTAPIortheWebUI,butthatuseralreadyhasthemaximum
numberofconcurrentsessionsrunning.
Action
1. Logoutfromoneoftheexistingsessions.
Browsersshareasinglesessioncookieacrossmultipletabsorevenwindows.However,scripts
thatPOSTtotheloginresourceandlaterdonotPOSTtothelogoutresourcecaneasilycreatethe
maximumnumberofconcurrentsessions.
2. Ifthesessioncookieislostanditisnotpossibletologoutofthesession,thenwaitforthesession
idletimelimittoexpire.
181
AOS-CX10.15.xxxxDiagnosticsandSupportabilityGuide|(6300,6400SwitchSeries)

When the session idle timeout expires, the session is terminated automatically.

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions, Web UI sessions, and real-time notification subscriptions.

Troubleshooting Web UI and REST API Access Issues | 182

Chapter 21

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

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

183

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
SupportandOtherResources|184

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.15.xxxx Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

185