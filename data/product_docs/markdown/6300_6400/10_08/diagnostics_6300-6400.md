AOS-CX 10.08 Diagnostics and
Supportability Guide

6300, 6400 Switch Series

Published: June 2022
Edition: 3

Copyright Information

© Copyright 2022 Hewlett Packard Enterprise Development LP.

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
| Contents                                                 |                          |              |          | 3   |
| -------------------------------------------------------- | ------------------------ | ------------ | -------- | --- |
| About                                                    | this document            |              |          | 7   |
| Applicableproducts                                       |                          |              |          | 7   |
| Latestversionavailableonline                             |                          |              |          | 7   |
| Commandsyntaxnotationconventions                         |                          |              |          | 7   |
| Abouttheexamples                                         |                          |              |          | 8   |
| Identifyingswitchportsandinterfaces                      |                          |              |          | 8   |
| Identifyingmodularswitchcomponents                       |                          |              |          | 9   |
| Debug                                                    | logging                  |              |          | 10  |
| Debugloggingcommands                                     |                          |              |          | 10  |
|                                                          | cleardebugbuffer         |              |          | 10  |
|                                                          | debug{all|<MODULE-NAME>} |              |          | 11  |
|                                                          | debugdb                  |              |          | 12  |
|                                                          | debugdestination         |              |          | 14  |
|                                                          | showdebug                |              |          | 16  |
|                                                          | showdebugbuffer          |              |          | 17  |
|                                                          | showdebugbuffervsf       |              |          | 18  |
|                                                          | showdebugdestination     |              |          | 19  |
| Log Rotation                                             |                          |              |          | 20  |
| Changingthesizeofthelogrotationfile                      |                          |              |          | 20  |
| Changingthetimefrequencyforlogrotation                   |                          |              |          | 20  |
| Identifyingaremotehostforreceivingrotatedlogfiles        |                          |              |          | 21  |
| Logrotationpaths                                         |                          |              |          | 21  |
| Managementofrotatedlogfiles                              |                          |              |          | 21  |
| Remotetransferofrotatedlogfiles                          |                          |              |          | 21  |
| Verifyingthelogrotationparameters                        |                          |              |          | 21  |
| Resettingthesizeofthelogrotationfile                     |                          |              |          | 22  |
| Resettingthetimefrequencytodaily                         |                          |              |          | 22  |
| Resettingtheremotehostforreceivingrotatedlogfiles        |                          |              |          | 22  |
| Logrotationnotoccurringimmediatelyafterreachingthreshold |                          |              |          | 23  |
| Logfilesnottransferredremotely                           |                          |              |          | 23  |
| Logrotationnotoccurringregardlessofperiodvalue           |                          |              |          | 23  |
| Logrotationcommands                                      |                          |              |          | 24  |
|                                                          | logrotatemaxsize         |              |          | 24  |
|                                                          | logrotateperiod          |              |          | 25  |
|                                                          | logrotatetarget          |              |          | 25  |
|                                                          | showlogrotate            |              |          | 27  |
| Switch                                                   | system                   | and hardware | commands | 28  |
| Reboot                                                   | reasons                  |              |          | 29  |
| Event                                                    | Logs                     |              |          | 31  |
| Showingandclearingevents                                 |                          |              |          | 31  |
3
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Cable                        | Diagnostics                                     | 32  |
| ---------------------------- | ----------------------------------------------- | --- |
| HowTDRworksonAOS-CXplatforms |                                                 | 32  |
| Cablediagnosticstests        |                                                 | 32  |
| Cablediagnosticcommands      |                                                 | 33  |
|                              | diagcable-diagnostic                            | 33  |
| Supportability               | Copy                                            | 35  |
| Supportabilitycopycommands   |                                                 | 35  |
|                              | copycheckpoint                                  | 35  |
|                              | copycommand-output                              | 36  |
|                              | copycore-dump[<MEMBER/SLOT>]daemon              | 37  |
|                              | copycore-dump[<MEMBER/SLOT>]kernel              | 38  |
|                              | copycore-dump[<MEMBER/SLOT>]kernel<STORAGE-URL> | 40  |
|                              | copycore-dumpvsfmemberdaemon                    | 40  |
|                              | copycore-dumpvsfmemberkernel                    | 41  |
|                              | copydiag-dumpfeature<FEATURE>                   | 42  |
|                              | copydiag-dumplocal-file                         | 44  |
|                              | copydiag-dumpvsfmemberlocal-file                | 45  |
|                              | copy<IMAGE>                                     | 46  |
|                              | copyrunning-config                              | 47  |
|                              | copyshow-techfeature                            | 48  |
|                              | copyshow-techlocal-file                         | 49  |
|                              | copyshow-techvsfmemberlocal-file                | 50  |
|                              | copystartup-config                              | 51  |
|                              | copysupport-files                               | 52  |
|                              | copysupport-fileslocal-file                     | 54  |
|                              | copysupport-filesvsfmember                      | 56  |
|                              | copysupport-log                                 | 57  |
|                              | copysupport-logvsfmember                        | 58  |
| Traceroute                   |                                                 | 61  |
| Traceroutecommands           |                                                 | 61  |
|                              | traceroute                                      | 61  |
|                              | traceroute6                                     | 64  |
| Ping                         |                                                 | 66  |
| Pingcommands                 |                                                 | 66  |
|                              | ping                                            | 66  |
|                              | ping6                                           | 72  |
| Troubleshooting              |                                                 | 75  |
|                              | Operationnotpermitted                           | 75  |
|                              | Networkisunreachable                            | 76  |
|                              | Destinationhostunreachable                      | 76  |
| Remote                       | syslog                                          | 77  |
| Remotesyslogcommands         |                                                 | 77  |
|                              | logging                                         | 77  |
|                              | loggingfilter                                   | 79  |
|                              | loggingfacility                                 | 82  |
|                              | loggingpersistent-storage                       | 83  |
| Runtime                      | Diagnostics                                     | 85  |
| Runtimediagnosticcommands    |                                                 | 85  |
|                              | diagnosticmonitor                               | 85  |
|                              | diagon-demand                                   | 86  |
Contents|4

|                                     | showdiagnostic       | 88  |
| ----------------------------------- | -------------------- | --- |
|                                     | showdiagnosticevents | 92  |
| Service                             | OS                   | 94  |
| ServiceOSCLIlogin                   |                      | 94  |
| ServiceOSuseraccounts               |                      | 95  |
| ServiceOSbootmenu                   |                      | 95  |
| Consoleconfiguration                |                      | 96  |
| AOS-CXboot                          |                      | 96  |
| Filesystemaccess                    |                      | 97  |
| ServiceOSmountfailure               |                      | 98  |
| ServiceOSCLIcommandlist             |                      | 98  |
| ServiceOSCLIfeaturesandlimitations  |                      | 99  |
| ServiceOSCLIcommands                |                      | 99  |
|                                     | boot                 | 99  |
|                                     | cat                  | 100 |
|                                     | cdpath               | 101 |
|                                     | config-clear         | 101 |
|                                     | cp                   | 102 |
|                                     | du                   | 103 |
|                                     | erasezeroize         | 104 |
|                                     | exit                 | 105 |
|                                     | format               | 106 |
|                                     | identify             | 107 |
|                                     | ip                   | 107 |
|                                     | ls                   | 108 |
|                                     | md5sum               | 110 |
|                                     | mkdir                | 111 |
|                                     | mount                | 112 |
|                                     | mv                   | 112 |
|                                     | password             | 113 |
|                                     | ping                 | 114 |
|                                     | pwd                  | 114 |
|                                     | reboot               | 115 |
|                                     | rm                   | 115 |
|                                     | rmdir                | 116 |
|                                     | secure-mode          | 117 |
|                                     | sh                   | 118 |
|                                     | umount               | 119 |
|                                     | update               | 119 |
|                                     | tftp                 | 121 |
|                                     | version              | 121 |
| In-System                           | Programming          | 123 |
| ShowtechcommandlistfortheISPfeature |                      | 123 |
| In-SystemProgrammingcommands        |                      | 123 |
|                                     | clearupdate-log      | 123 |
|                                     | showneeded-updates   | 123 |
| Selftest                            |                      | 125 |
| Selftestcommands                    |                      | 125 |
|                                     | fastboot             | 125 |
|                                     | showselftest         | 127 |
| Zeroization                         |                      | 131 |
| Zeroizationcommands                 |                      | 131 |
5
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

|                                               | eraseallzeroize                          |           |             |            |        | 131 |
| --------------------------------------------- | ---------------------------------------- | --------- | ----------- | ---------- | ------ | --- |
| Terminal                                      | Monitor                                  |           |             |            |        | 133 |
| Terminalmonitorcommands                       |                                          |           |             |            |        | 133 |
|                                               | loggingconsole{notify|severity|filter}   |           |             |            |        | 133 |
|                                               | showterminal-monitor                     |           |             |            |        | 134 |
|                                               | terminal-monitor{notify|severity|filter} |           |             |            |        | 135 |
| Troubleshooting                               |                                          | Web       | UI and REST | API Access | Issues | 137 |
| HTTP404errorwhenaccessingtheswitchURL         |                                          |           |             |            |        | 137 |
| HTTP401error"Loginfailed:sessionlimitreached" |                                          |           |             |            |        | 137 |
| Support                                       | and Other                                | Resources |             |            |        | 139 |
| AccessingArubaSupport                         |                                          |           |             |            |        | 139 |
| AccessingUpdates                              |                                          |           |             |            |        | 139 |
|                                               | ArubaSupportPortal                       |           |             |            |        | 139 |
|                                               | MyNetworking                             |           |             |            |        | 140 |
| WarrantyInformation                           |                                          |           |             |            |        | 140 |
| RegulatoryInformation                         |                                          |           |             |            |        | 140 |
| DocumentationFeedback                         |                                          |           |             |            |        | 140 |
Contents|6

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

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

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

7

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
| On the 6300Switch | Series |     |     |
| ----------------- | ------ | --- | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
Aboutthisdocument|8

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

Identifying modular switch components

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

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

9

Chapter 2
Debug logging
| Debug | logging |     |
| ----- | ------- | --- |
Thedebugloggingframeworkprovidesanimproved,customizable,andconditionalloggingframeworkwith
featureandentitybasedfilteringoptions.Debugloggingisaverbose,on-demandloggingmechanismwhich
customersandsupportcanenableinordertoobtainmoreinformationthatwillassistwithtroubleshooting.
EachdebugloggingeventhasbothaSeverityandaModule.Customers/supportarerequiredtoenablea
givenModuleinordertohavethoseeventslogged.ThelogoperationisnotrunwhenaModuleisnot
enabled.AlldebuglogeventsclassifiedwithaSeverityofErrorandabovewillalwaysbelogged.Thisensures
thatbothsupportandcustomerswillbeabletoseetheseimportanteventsevenwhentheirrespective
debuglogModuleisn’tenabled.
Debugloggingisdisabledbydefault.
| Debug       | logging      | commands |
| ----------- | ------------ | -------- |
| clear       | debug buffer |          |
| clear debug | buffer       |          |
Description
Clearsalldebuglogs.Usingtheshow debug buffercommandwillonlydisplaythelogsgeneratedafterthe
| clear debug | buffercommand. |     |
| ----------- | -------------- | --- |
Examples
Clearingallgenerateddebuglogs:
| switch# | show debug | buffer |
| ------- | ---------- | ------ |
-------------------------------------------------------------------------------------
-------------------------
| show | debug buffer |     |
| ---- | ------------ | --- |
-------------------------------------------------------------------------------------
-------------------------
2018-10-14:09:10:58.558710|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_CONFIG|No Port cfg changes
2018-10-14:09:10:58.558737|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_EVENT|lldpd_stats_run
| entered | at time | 8257199 |
| ------- | ------- | ------- |
2018-10-14:09:10:58.569317|lldpd|LOG_DEBUG|MSTR||LLDP|LLDP_CONFIG|No Port cfg changes
2018-10-14:09:11:21.881907|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|Sysmon
| poll    | interval changed | to 32  |
| ------- | ---------------- | ------ |
| switch# | clear debug      | buffer |
| switch# | show debug       | buffer |
-------------------------------------------------------------------------------------
-------------------------
| show | debug buffer |     |
| ---- | ------------ | --- |
-------------------------------------------------------------------------------------
-------------------------
10
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

2018-10-14:09:13:24.481407|hpe-sysmond|LOG_INFO|MSTR||SYSMON|SYSMON_CONFIG|Sysmon
| poll | interval | changed | to 51 |     |     |     |
| ---- | -------- | ------- | ----- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
<MODULE-NAME> Enablesdebugloggingforaspecificmodule.Foralistof
supportedmodules,enterthedebugcommandfollowedbya
spaceandaquestionmark(?).
<SUBMODULE-NAME> Enablesdebugloggingforaspecificsubmodule.Foralistof
supportedsubmodules,enterthedebug <MODULE-NAME>
commandfollowedbyaspaceandaquestionmark(?).
severity (emer|crit|alert|err| Selectstheminimumseverityloglevelforthedestination.Ifa
notice|warning|info|debug) severityisnotprovided,thedefaultloglevelisdebug.Optional.
emer Specifiesstorageofdebuglogswithaseveritylevelofemergency
only.
crit
Specifiesstorageofdebuglogswithseveritylevelofcritical
andabove.
alert
Specifiesstorageofdebuglogswithseveritylevelofalertand
above.
Debuglogging|11

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
err
Specifiesstorageofdebuglogswithseverityleveloferrorand
above.
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning Specifiesstorageofdebuglogswithseveritylevelofwarningand
above.
| info |     |     | Specifiesstorageofdebuglogswithseveritylevelofinfoand |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
above.
| debug |     |     | Specifiesstorageofdebuglogswithseveritylevelofdebug |     |
| ----- | --- | --- | --------------------------------------------------- | --- |
(default).
| port |     |     | Displaysdebuglogsforthespecifiedport,forexample1/1/1. |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
vlan <VLAN-ID> DisplaysdebuglogsforthespecifiedVLAN.ProvideaVLANfrom1
to4094.
| ip <IP-ADDRESS> |     |     | DisplaysdebuglogsforthespecifiedIPAddress. |     |
| --------------- | --- | --- | ------------------------------------------ | --- |
mac <MAC-ADDRESS> DisplaysdebuglogsforthespecifiedMACAddress,forexample
A:B:C:D:E:F.
| vrf <VRF-NAME> |     |     | DisplaysdebuglogsforthespecifiedVRF. |     |
| -------------- | --- | --- | ------------------------------------ | --- |
instance <INSTANCE-ID> Displaysdebuglogsforthespecifiedinstance.Provideaninstance
IDfrom1to255.
Examples
switch#
debug all
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| debug db      |               |        |                     |          |
| ------------- | ------------- | ------ | ------------------- | -------- |
| debug db {all | | sub-module} | [level | <MINIMUM-SEVERITY>] | [filter] |
no debug db {all | sub-module} [level <MINIMUM-SEVERITY>] [filter]
12
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- |

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

Specifies storage of debug logs with severity level of critical
and above.

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

DBlog is a high performance, configuration, and state database server logging infrastructure where a user
can log the transactions which are sent or received by clients to the configuration and state database server.
It can be enabled through the CLI and REST, and also supports filters where a user can filter out logs on the
basis of table, column, or client. It is helpful for debugging when the user wants to debug an issue with a
particular client, table, or column combination. It is not enabled by default. A combination of filters can also
be applied to filter out messages based on table, column, and client.

There are three submodules for the "db" module:

1. all: When All is enabled, no filters are applied to any of the debug logs, even if other submodules are

configured with filters.

Debug logging | 13

2. tx:Ifenabled,onlytherepliesandnotificationssentoutfortheinitialandincrementalupdatesare
logged.
3. rx:Ifenabled,onlythetransactionssenttotheconfigurationandstatedatabaseserverarelogged.
Thekeywordallmaybeusedtoenableordisabledebugloggingforallsub-modules.Alsoacombinationof
filterscanbeusedtofilterthemessagetypes.
Ifthetableorclientfilterisapplied,thenthemessagesbelongingtothisspecifictableorclientwillbelogged.
Thecolumnfiltercanalsobeappliedtofurtherfiltermessagesonatable,providingamechanismtofilter
messagesonacolumn.Thetableandclientfiltercanbeusedincombinationorseparately,butcolumncan
onlybeusedinconjunctionwithtable.
Examples
Configuringallsubmoduleswithseveritydebug:
| switch# | debug db | all severity | debug |
| ------- | -------- | ------------ | ----- |
Configuringthetxsubmodulewithtable Interfacefilterandseveritydebug:
switch#
|     | debug db | tx table Interface | severity debug |
| --- | -------- | ------------------ | -------------- |
Configuringtherxsubmodulewithtable Interface column statisticsfilterandseveritydebug:
switch# debug db rx table Interface column statistics severity debug
Disablingtherxsubmodule:
| switch#                      | no debug | db rx       |            |
| ---------------------------- | -------- | ----------- | ---------- |
| Disablingthetxsubmoduletable |          |             | Interface: |
| switch#                      | no debug | db tx table | Interface  |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
debug destination
14
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |
| --------------------------------------------- | --- | --- | ----------------------- |

debug destination {syslog | file | console | buffer} [severity
(emer|crit|alert|err|notice|warning|info|debug)]
no debug destination {syslog | file | console}

Description

Sets the destination for debug logs and the minimum severity level for each destination

The no form of this command unsets the destination for debug logs.

Parameter

Description

{syslog | file | console | buffer}

Selects the destination to store debug logs. Required.

syslog

file

console

buffer

Specifies that the debug logs are stored in the syslog.

Specifies that debug logs are stored in file.

Specifies that debug logs are stored in console.

Specifies that debug logs are stored in buffer (default).

severity (emer|crit|alert|err|
notice|warning|info|debug)

Selects the minimum severity log level for the destination. If a
severity is not provided, the default log level isdebug. Optional.

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

Specifies storage of debug logs with severity level of critical
and above.

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

Events that have a severity equal to or higher than the configured severity level are stored in the designated
destination. The product defaults to buffer for destination and debug as a severity level.

Examples

Debug logging | 15

| switch# | debug destination |     | syslog  | severity | alert   |     |     |     |
| ------- | ----------------- | --- | ------- | -------- | ------- | --- | --- | --- |
| switch# | debug destination |     | console | severity | info    |     |     |     |
| switch# | debug destination |     | file    | severity | warning |     |     |     |
| switch# | debug destination |     | buffer  | severity | err     |     |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show debug
| show debug [vsx-peer] |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Description
Displaystheenableddebugtypes.
| Parameter |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# | show debug |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
-----------------------------------------------------------------------------------
| module sub_module |     | severity | vlan | port | ip  | mac | instance | vrf |
| ----------------- | --- | -------- | ---- | ---- | --- | --- | -------- | --- |
-----------------------------------------------------------------------------------
| all | all | err | 1   | 1/1/1 | 10.0.0.1 | 1a:2b:3c:4d:5e:6f | 2   | abcd |
| --- | --- | --- | --- | ----- | -------- | ----------------- | --- | ---- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
16
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show       | debug buffer   |               |            |
| ---------- | -------------- | ------------- | ---------- |
| show debug | buffer [module | <MODULE-NAME> | | severity |
(emer|crit|alert|err|notice|warning|info|debug)]
Description
Displaysdebuglogsstoredinthespecifieddebugbufferwithoptionalfilteringbymoduleorseverity.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MODULE-NAME> Filtersdebuglogsdisplayedbythespecifiedmodulename.
| severity | (emer|crit|alert|err| |     |     |
| -------- | --------------------- | --- | --- |
Displaysdebuglogswithaspecifiedseveritylevel.Defaults
notice|warning|info|debug)
todebug.Optional.
emer
Displaysdebuglogswithaseveritylevelofemergencyonly.
| crit  |     |     | Displaysdebuglogswithaseveritylevelofcriticalandabove. |
| ----- | --- | --- | ------------------------------------------------------ |
| alert |     |     | Displaysdebuglogswithaseveritylevelofalertandabove.    |
| err   |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |
above.
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning
Displaysdebuglogswithaseveritylevelofwarningandabove.
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
| interval | changed to | 20  |     |
| -------- | ---------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
Debuglogging|17

CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | debug | buffer |     | vsf |     |     |
| ---- | ----- | ------ | --- | --- | --- | --- |
Applicablefor6300switchesonly.
| show debug | buffer | vsf | [member | <MEMBER-ID>] | [{master | | standby}] |
| ---------- | ------ | --- | ------- | ------------ | -------- | ----------- |
Description
DisplaysVSFmemberdebuglogsstoredinthedebugbuffer,withanoptiontofilterbyVSFmemberand
role.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MEMBER-ID>
Displaysdebuglogsforthespecifiedmember-id.Optional.Range:
1-10.
| master |     |     |     |     | DisplaydebuglogsfortheVSFmaster. |     |
| ------ | --- | --- | --- | --- | -------------------------------- | --- |
standby
DisplaydebuglogsfortheVSFstandby.
Examples
DisplayingVSFmemberdebuglogswithmember-id1:
switch#
|     | show | debug | buffer | vsf member | 1   |     |
| --- | ---- | ----- | ------ | ---------- | --- | --- |
------------------------------------------------------------------------------
| show | debug | buffer |     |     |     |     |
| ---- | ----- | ------ | --- | --- | --- | --- |
------------------------------------------------------------------------------
2018-11-21:06:16:38.214838|vsf-madd|LOG_ERR|MSTR|1|VSFMAD|VSFMAD_EVENT|VSF Member
| state | is master |     |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- | --- |
DisplayingVSFmemberdebuglogsformemberstatemaster:
| switch# | show | debug | buffer | vsf master |     |     |
| ------- | ---- | ----- | ------ | ---------- | --- | --- |
------------------------------------------------------------------------------
| show | debug | buffer |     |     |     |     |
| ---- | ----- | ------ | --- | --- | --- | --- |
------------------------------------------------------------------------------
2018-11-21:06:16:38.214838|vsf-madd|LOG_ERR|MSTR|1|VSFMAD|VSFMAD_EVENT|VSF Member
| state | is master |     |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
18
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- |

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
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
|     |     | show debug destination |     |
| --- | --- | ---------------------- | --- |
---------------------------------------------------------------------
CONSOLE:info
FILE:warning
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Debuglogging|19

Chapter 3

Log Rotation

Log Rotation

Log rotation provides you with the ability to systematically rotate and archive any log files produced by the
system. Log rotation reduces log space required on the switch. Log rotation rotates and compresses the log
files based on size and/or period. Rotated log files are stored locally or transferred to a remote host using
TFTP.

Optionally, notifications can be triggered if a log buffer percent full threshold is exceeded, giving you the
opportunity to save the logs elsewhere before the buffers are rotated with the oldest data being
overwritten.

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

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

20

Identifying a remote host for receiving rotated log files
You can send the rotated log files to a specified remote host Universal Resource Identifier (URI) by using the
TFTP protocol. If no URI is specified, the rotated and compressed log files are stored locally in /var/log/.
Only the TFTP protocol is supported for remote transfer, and the log rotation file cannot be more than 32
MB. Use the Linux TFTP command to transfer the file. Rotated log files are removed from the local path
/var/log/ when it is moved to TFTP server.

Prerequisites

You must be in the configuration context:
switch(config)#

Procedure

Provide the target IP address (IPv4 or IPv6) at the configuration context in the CLI:
switch(config)# logrotate target {tftp://A.B.C.D | tftp://X:X::X:X}

IPv4 Example

switch(config)# logrotate target tftp://192.168.1.132

IPv6 Example

switch(config)# logrotate target tftp://2001:db8:0:1::128

Log rotation paths
Only logs stored in the following files are rotated:

n Event logs stored in the /var/log/event.log file.

n Authentication logs stored in the /var/log/auth.log file.

n Audit logs stored in the /var/log/audit/audit.log file

Management of rotated log files
Rotated log files are compressed and stored locally in /var/log/, regardless of the remote host
configuration. Rotated log files are stored with respective time extension to the granularity of hour in the
format file1–YYYYMMDDHH.gz (for example, messages-2015080715.gz). Rotated log files are replaced when
the number of old rotated log files exceeds three. The newly rotated log file replaces the oldest rotated log
file.

Remote transfer of rotated log files
Only the TFTP protocol is supported for remote transfer, and both IPv4 and IPv6 addresses are supported.

Only newly rotated log files are transferred to the remote host during the log rotation. Previously rotated
log files are not transferred. After a file is successfully transferred, it is removed from the switch local path.

Packet level failures with TFTP are handled in the protocol itself. With each TFTP session failure, TFTP retries
the file transfer three times. Retries have a timeout of five seconds.

Verifying the log rotation parameters

Log Rotation | 21

Atthecommandprompt,enter:
| switch# show | logrotate |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
Exampleoutput
| switch#   | show logrotate |     |     |     |     |
| --------- | -------------- | --- | --- | --- | --- |
| Logrotate | configurations | :   |     |     |     |
| Period    | : daily        |     |     |     |     |
| Maxsize   | : 10MB         |     |     |     |     |
switch#
| Resetting | the size | of the | log rotation | file |     |
| --------- | -------- | ------ | ------------ | ---- | --- |
Prerequisites
Youmustbeintheconfigurationcontext:
switch(config)#
Procedure
Atconfigurationcontext,enterthenoformofthelogrotate maxsizecommand:
| switch(config)# | no logrotate | maxsize   |          |     |     |
| --------------- | ------------ | --------- | -------- | --- | --- |
| Resetting       | the time     | frequency | to daily |     |     |
Prerequisites
Youmustbeintheconfigurationcontext:
switch(config)#
Procedure
Atconfigurationcontext,enterthenoformofthelogrotate periodcommand:
| switch(config)# | no logrotate | period |               |         |           |
| --------------- | ------------ | ------ | ------------- | ------- | --------- |
| Resetting       | the remote   | host   | for receiving | rotated | log files |
Prerequisites
Youmustbeintheconfigurationcontext:
switch(config)#
Procedure
Atconfigurationcontext,enterthenoformofthelogrotate targetcommand:
| switch(config)# | no logrotate | target |     |     |     |
| --------------- | ------------ | ------ | --- | --- | --- |
22
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- |

Example:
| switch(config)# | logrotate        | target    | tftp://1.1.1.1 |     |     |
| --------------- | ---------------- | --------- | -------------- | --- | --- |
| switch(config)# | do show          | logrotate |                |     |     |
| Logrotate       | configurations   | :         |                |     |     |
| Period          | : daily          |           |                |     |     |
| Maxsize         | : 10MB           |           |                |     |     |
| Target          | : tftp://1.1.1.1 |           |                |     |     |
| switch(config)# | no logrotate     | target    |                |     |     |
| switch(config)# | do show          | logrotate |                |     |     |
| Logrotate       | configurations   | :         |                |     |     |
| Period          | : daily          |           |                |     |     |
| Maxsize         | : 10MB           |           |                |     |     |
switch(config)#
| Log rotation | not | occurring | immediately | after | reaching |
| ------------ | --- | --------- | ----------- | ----- | -------- |
threshold
Symptom
Logrotationdoesnotoccurimmediatelyafterthemaximumfilesizeforthelogfileisreached.
Cause
Thelogrotationchecksthesizeofthefileonthefirstminuteofeveryhour.Ifthemaximumfilesizeis
reachedinthemeantime,thelogrotationdoesnotoccuruntilthenexthourlycheckofthefilesize.
Action
Logrotationisworkingasdesigned.Thelogrotationfeatureisdesignedtocheckthefilesizeonanhourly
basis.
| Log files | not transferred |     | remotely |     |     |
| --------- | --------------- | --- | -------- | --- | --- |
Symptom
Rotatedlogfilesarenottransferredtoaremotehost.
Cause
Theremotehostmightnotbereachable.
n
TheTFTPserverontheremotehostmightnothavesufficientprivilegesforfilecreation.
n
Action
1. Verifythattheremotehostisreachable.
2. EnsurethattheTFTPserverisconfiguredwiththerequiredfilecreationpermissions.
3. Forexample,ontheTFTPD-HPAserver,changetheconfigurationfilein/etc/default/tftpd-hpato
| include-cinTFTP_OPTIONS.(forexample,TFTP_OPTIONS="--secure |     |           |            | -c.). |       |
| ---------------------------------------------------------- | --- | --------- | ---------- | ----- | ----- |
| Log rotation                                               | not | occurring | regardless | of    | value |
period
Symptom
LogRotation|23

Log rotation is not happening regardless of the period value.

Cause

Log files are not rotated when they are empty files (the log file size is zero).

Action

Log rotation occurs when the log file size is greater than zero.

Log rotation commands

logrotate maxsize
logrotate maxsize <MAX-SIZE>

no logrotate maxsize

Description

Specifies the maximum allowed log file size.

The no form of this command resets the size of the log file to the default (100 MB).

Parameter

<MAX-SIZE>

Usage

Description

Specifies the allowed size the log file can reach before it is
compressed and stored locally or transferred to a remote host.
The size is a value in the range of 10- 200 MB, and it cannot
exceed 32 MB for transferred files.

A log file that exceeds either the configured <MAX-SIZE> value or the logrotate period , triggers rotation
for that log file. Log rotation occurs during the next hourly maintenance cycle.

Logs are stored locally (event logs in the /var/log/event.log file, and authentication logs in the
/var/log/auth.log file) or transferred to the configured remote destination target using TFTP.

Examples

switch(config)# logrotate maxsize 32

switch(config)# no logrotate maxsize

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

24

| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logrotate    | period |          |          |         |           |
| ------------ | ------ | -------- | -------- | ------- | --------- |
| logrotate    | period | {daily | | hourly | | monthly | | weekly} |
| no logrotate | period |          |          |         |           |
Description
Setstherotateperiodfortheeventlogs,storedinthe/var/log/event.logfile,andauthenticationlogs,
storedinthe/var/log/auth.logfile.Defaultstodaily.
Alogfilethatexceedseitherthelogrotate <MAX-SIZE>valueorthelogrotate period(whichever
happensfirst),triggersrotationforthatlogfile.
Thenoformofthiscommandresetsthelogrotationperiodtothedefault.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
daily Rotateslogfilesonadailybasis(default)at1:00amlocaltime.
| hourly  |     |     |     | Rotateslogfileseveryhouratthefirstsecondofthehour. |     |
| ------- | --- | --- | --- | -------------------------------------------------- | --- |
| monthly |     |     |     | Rotateslogfilesmonthlyonthefirstdayofthemonth.     |     |
| weekly  |     |     |     | RotateslogfilesonceaweekonSunday.                  |     |
Examples
| switch(config)# |     | logrotate | period | weekly |     |
| --------------- | --- | --------- | ------ | ------ | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logrotate    | target |                     |     |                       |     |
| ------------ | ------ | ------------------- | --- | --------------------- | --- |
| logrotate    | target | {tftp://<IPV4_ADDR> |     | | tftp://<IPV6_ADDR>} |     |
| no logrotate | target |                     |     |                       |     |
Description
LogRotation|25

SpecifiesthetargetremotehostUniversalResourceIdentifier(URI)usingTFTPprotocoltoallowtransferof
rotatedandcompressedfilestoaremotetarget.Rotatedlogfilesarestoredlocally(eventlogsinthe
/var/log/event.logfile,andauthenticationlogsinthe/var/log/auth.logfile)ortransferredtothe
configuredremotedestinationtarget.
Thenoformofthiscommandresetsthetargettothedefault,whichstorestherotatedandcompressedlog
fileslocallyin/var/log/.
Commandcontext
Parameter Description
<IPV4_ADDR> SpecifiesanIPv4IPAddresslocationforlogfilestorage.
<IPV6_ADDR> SpecifiesanIPv6IPAddresslocationforlogfilestorage.
Usage
Totransferrotatedlogfilesremotely,usetheTFTPprotocolonly,andmakesurethattherotatedlogfileis
lessthan32MBinsize.UsetheLinuxTFTPcommandtotransferthefile.Therotatedlogfileisremoved
fromthelocalpath/var/log/whenthelogfileismovedtoaTFTPserver.
Examples
SettinganIPv4target:
| switch(config)# | logrotate | target tftp://192.168.1.132 |
| --------------- | --------- | --------------------------- |
SettinganIPv6target:
| switch(config)# | logrotate | target tftp://2001:db8:0:1::128 |
| --------------- | --------- | ------------------------------- |
Removingalogrotatetarget:
| switch(config)# | logrotate        | target tftp://1.1.1.1 |
| --------------- | ---------------- | --------------------- |
| switch(config)# | do show          | logrotate             |
| Logrotate       | configurations   | :                     |
| Period          | : daily          |                       |
| Maxsize         | : 10MB           |                       |
| Target          | : tftp://1.1.1.1 |                       |
| switch(config)# | no logrotate     | target                |
| switch(config)# | do show          | logrotate             |
| Logrotate       | configurations   | :                     |
| Period          | : daily          |                       |
| Maxsize         | : 10MB           |                       |
switch(config)#
CommandHistory
Release Modification
10.07orearlier --
26
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show logrotate
| show logrotate | [vsx-peer] |     |
| -------------- | ---------- | --- |
Description
Displayslogrotateconfigurationdetails.
Parameter Description
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#   | show logrotate |     |
| --------- | -------------- | --- |
| Logrotate | configurations | :   |
| Period    | : daily        |     |
| Maxsize   | : 100MB        |     |
| Target    | : local        |     |
switch#
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
LogRotation|27

Chapter 4
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettingson
theswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
28
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- |

Chapter 5

Reboot reasons

Reboot reasons

The show boot-history command displays the following reboot reasons for the management module and
line module:

Reboot reasons for management module

Reboots handled through database

Parameter

Description

Reboot requested by user

Reset button pressed
Backplane fault
Configuration change
Console error
Fabric fault
All line modules faulted
Redundacy switchover requested
Redundant Management communication
timeout

Redundant Management election timeout

Critical service fault (error)

VSF autojoin renumber

A user requested a switch reboot through the CLI or web
UI.
The switch detected a short-press of the reset button.
A backplane fault occured.
A configuration change resulted in a reboot.
Console failed to start.
A fabric fault occurred.
A zero line card condition occurred.
A user requested a redundancy switchover.
The standby management module has taken over from an
unresponsive active management module.
A failure to elect a standby management module in the
alloted time.
A daemon critical to switch operation has stopped
functioning. An extra error string may be present to
describe the error in detail.

NOTE: VSF is not applicable for 6400 Switch series.

Reset triggered by VSF autojoin.

VSF member renumbered
VSF switchover requested
VSX software update

An user requested a renumber of a VSF member.
An user requested a VSF switchover.

NOTE: Not applicable for 6300 Switch series.

Reset triggered by a VSX software update.

Chassis critical temperature
Chassis insufficient fans
Chassis unsupported PSUs/fans
Management module critical temperature

Chassis operating temperature exceeded.
Insufficient fans to cool the chassis.
Unsupported or misconfigured PSUs or system fans.
Management module operating temperature exceeded.

Uncontrolled reboots

n ops-switchd crashed

n ovsdb-server crashed

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

29

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

Reboot reasons | 30

Chapter 6

Event Logs

Event Logs

Event logging logs events generated by daemons, processes, and plug-ins running within the switch
software. The event logging framework captures the event logs in a system journal by updating the journal
fields and meta data.

Showing and clearing events
The clear events command is used to clear the event log of all events. The show events command is used
to show all event logs generated by the switch since the last reboot. See the Switch system and hardware
commands chapter of the Fundamentals Guide for information on these commands.

The time stamp for event log messages generated from the Service OS indicates when the event log
messages were transferred to the event log after a switch boot and not when the issue occurred.

See the Security Guide for information about accounting logs.

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

31

Chapter 7
Cable Diagnostics
Cable Diagnostics
TheTime-DomainReflectometer(TDR)featurehelpscharacterizeandlocatecablefaultsinthetwistedwire
pairs.TDRinvolvesshowingareflectionatanyimpedancechangewithinthecablewhenalowvoltagepulse
issentintothecable.TDRmeasuresthetimebetweenreleaseandreturnofthelowvoltagepulsefromany
reflections.Thedistancetothereflectioncanbecalculatedbymeasuringthetimeandthetransmission
velocityofthepulse.
TDRorCableDiagnosticsisaportfeaturesupportedonsomeswitchesrunningAOS-CXsoftware.TDRis
usedtodetectcablefaultson1GbT,2.5G-SmartRate,5G-SmartRate,and10G-SmartRate(onlyapplicable
for6400switch)ports.
| How | TDR works | on AOS-CX | platforms |
| --- | --------- | --------- | --------- |
TheimplementationofTDRinAOS-CXplatformsisdependentonthephysicallayerchips(PHYs)thatare
partofthefront-endnetworkportshardware.AOS-CXswitchesactivateTDRonthePHYwhenauserenters
thediag cable-diagnosticcommand.TheswitchwaitsforthereportaboutTDRmeasurementsfromthe
PHY.Theswitchthenreadstheresultsandreportsthevaluestotheuser.
| Cable | diagnostics | tests |     |
| ----- | ----------- | ----- | --- |
Thecablediagnosticstestwillbringdownthelink,whichwilltakemoretimetocompletethetest.
TheTDRcablediagnostictestallowsanoperatortotesttwistedpaircablesforfaultswithoutphysically
disconnectingthecablesfromtheswitch.Ithelpsintroubleshootingconnectivityormonitoring
performanceononeormoreswitchports.
Thediag cable-diagnosticcommandcanbeusedtoruncablediagnostictestsanddisplaythetestresults.
Thefollowingtableprovidesthecablestatusmessagesandtheirdescriptions.
| Status |     | Meaning                                          |     |
| ------ | --- | ------------------------------------------------ | --- |
| good   |     | TheMDIpairisgood.                                |     |
| open   |     | TheMDIpairisnotterminatedwithalinkpartnerorhasan |     |
opencircuit.
| short          |     | TheMDIpairisshortedwithinitself(intra-short).    |     |
| -------------- | --- | ------------------------------------------------ | --- |
| inter_short    |     | TheMDIpairisshortedwithanotherpair(inter-short). |     |
| high_impedance |     | TheMDIpairhashigh-impedancemismatchandisnot      |     |
guaranteedtolinkup.
| low_impedance |     | TheMDIpairhaslow-impedancemismatchandisnot |     |
| ------------- | --- | ------------------------------------------ | --- |
guaranteedtolinkup.
| failed |     | TheMDIpairhasfailedthecablediagnostictest. |     |
| ------ | --- | ------------------------------------------ | --- |
32
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

Thefollowingtableprovidesthepossiblecablediagnosticfailurereasonsforporttypes.
| Port | Type Reasons                                         |     |
| ---- | ---------------------------------------------------- | --- |
| 1GbT | Interfaceisbusy,orlinkpartnerisnotconfiguredforauto- |     |
negotiation,orlinkpartnerisbusyestablishingthelink.
| 2.5G-SmartRate | Interfaceisbusy. |     |
| -------------- | ---------------- | --- |
| 5G-SmartRate   | Interfaceisbusy. |     |
Thefollowingtableprovidesthecablelengthaccuracyforporttypes.
| Port | Type | Reasons                                    |
| ---- | ---- | ------------------------------------------ |
| 1GbT |      | Whendiagnosticstatusis"good",cablelengthis |
reportedwithin+/-10m.
| 2.5G-SmartRate |     | Whendiagnosticstatusis"good",cablelengthis |
| -------------- | --- | ------------------------------------------ |
notreported(0m).
| 5G-SmartRate |     | Whendiagnosticstatusis"good",cablelengthis |
| ------------ | --- | ------------------------------------------ |
notreported(0m).
Thefollowingtableprovidesthedistancetofaultaccuracyforporttypes.
| Port | Type | Reasons                                            |
| ---- | ---- | -------------------------------------------------- |
| 1GbT |      | Whendiagnosticstatusisnot"good"or"failed",distance |
tofaultisreportedwithin+/-5m.
2.5G-SmartRate Whendiagnosticstatusisnot"good"or"failed",distance
tofaultisreportedwithin+/-5m.
5G-SmartRate Whendiagnosticstatusisnot"good"or"failed",distance
tofaultisreportedwithin+/-5m.
| Cable | diagnostic | commands |
| ----- | ---------- | -------- |
diag cable-diagnostic
| diag cable-diagnostic | <IF-NAME> |     |
| --------------------- | --------- | --- |
Description
Runsacablediagnostictestonaninterface.
Parameter Description
<IF-NAME> Specifiesthenameoftheinterface.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Runningacablediagnostictestoninterfaces:
CableDiagnostics|33

| switch# | diag cable-diagnostic | 1/1/1 |     |
| ------- | --------------------- | ----- | --- |
This command will cause a loss of link on the port under test and will take
| several   | seconds to complete. |          |      |
| --------- | -------------------- | -------- | ---- |
| Continue  | (y/n)? y             |          |      |
|           | MDI Cable            | Distance | MDI  |
| Interface | Pair Status          | to Fault | Mode |
(Meters)
----------------------------------------------
| 1/1/1   | 1-2 good              | 5     | mdi |
| ------- | --------------------- | ----- | --- |
|         | 3-6 good              | 5     | mdi |
|         | 4-5 good              | 5     | mdi |
|         | 7-8 open              | 3     |     |
| switch# | diag cable-diagnostic | 1/1/2 |     |
This command will cause a loss of link on the port under test and will take
| several   | seconds to complete. |          |      |
| --------- | -------------------- | -------- | ---- |
| Continue  | (y/n)? y             |          |      |
|           | MDI Cable            | Distance | MDI  |
| Interface | Pair Status          | to Fault | Mode |
(Meters)
----------------------------------------------
| 1/1/2 | 1-2 good  | 5   | mdix |
| ----- | --------- | --- | ---- |
|       | 3-6 good  | 5   | mdix |
|       | 4-5 short | 1   |      |
|       | 7-8 good  | 5   | mdix |
Runningacablediagnostictestwillresultinabriefinterruptioninconnectivityonalltestedports.
IfagoodcableisusedontheSmartRateports,theDistancetoFault(Meters)valueis0.
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
34
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | ----------------------- | --- |

Chapter 8
Supportability Copy
| Supportability | Copy |     |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- | --- |
Toeffectivelydiagnosevariousissuesarisingattheswitch,differenttypesofdataarecopiedoutusingcopy
commandsforfurtheranalysis.
| Usethecopy | core-dumpcommandtocopythecore-dumpofadaemoncrash. |     |     |     |     |     |
| ---------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
| Usethecopy | show-techcommandtocapturethestatusofthefeature.   |     |     |     |     |     |
Ifthereisfeaturemisbehavior,usethecopy support-files featurecommandtocopyallfeaturerelated
informationforfurtheranalysis.Additionallyusecopy support-logandcopy diag-dumptocopy
informationthathelpstoanalyzetheinternalbehaviorofafeature/daemon.
Usecopy command-outputtocopyanyshowcommand'soutputtoremotedestinationsorUSBstorage.
Thesefilescanbecopiedtoaremotedestinationusingsftp/tftp,additionallytheycanalsobestoredinthe
USBstorage.
| Supportability | copy | commands |     |     |     |     |
| -------------- | ---- | -------- | --- | --- | --- | --- |
copy checkpoint
| copy checkpoint | <CHECKPOINT-NAME> | {<STORAGE-URL> |     | | <REMOTE-URL>} |     |     |
| --------------- | ----------------- | -------------- | --- | --------------- | --- | --- |
Description
CopiesthecheckpointusingTFTP,SFTP,SCP,orUSB.
| Parameter         |     |     | Description                 |     |     |     |
| ----------------- | --- | --- | --------------------------- | --- | --- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesthecheckpointname. |     |     |     |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- | --- |
Syntax:
|     |     |     | n {tftp://}{<IP> |     | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | --- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> |     | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --- | --------- |
[:<PORT>]/<FILE>
Examples
CopyingcheckpointchpttoaremoteURL:
switch#
|     | copy checkpoint | chpt scp://root@10.0.1.1/config |     |     | vrf mgmt |     |
| --- | --------------- | ------------------------------- | --- | --- | -------- | --- |
35
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- |

CommandHistory
| Release        |     | Modification      |     |     |
| -------------- | --- | ----------------- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |
| 10.07orearlier |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy command-output
copy command-output "<COMMAND>" {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}
Description
CopiesthespecifiedcommandoutputusingTFTP,SFTP,SCP,orUSB.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<COMMAND> Specifiesthecommandfromwhichyouwanttoobtainitsoutput.
Required.Userswithauditorrightscanspecifythesetwo
commandsonly:
|     |     | show accounting | log |     |
| --- | --- | --------------- | --- | --- |
show events
{<STORAGE-URL> | <REMOTE-URL> SelecteitherthestorageURLortheremoteURLforthe
[vrf <VRF-NAME>]} destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | ----------------------------------- | --- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | ----------- | ------------------- | --------- |
[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     |     |
| -------------- | --- | --- | --- | --- |
SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
Copyingtheoutputfromtheshow eventscommandtoaremoteURL:
switch# copy command-output "show events" tftp://10.100.0.12/file
SupportabilityCopy|36

Copyingtheoutputfromtheshow techcommandtoaremoteURLwithaVRFnamedmgmt:
switch# copy command-output "show tech" scp://user@10.100.0.12/file vrf mgmt
Copyingtheoutputfromtheshow techcommandtoaremoteURLwithaVRFnamedmgmt:
switch# copy command-output "show tech" tftp://10.100.0.12/file vrf mgmt
Copyingtheoutputfromtheshow eventscommandtoafilenamedeventsonaUSBdrive:
switch#
|     | copy command-output |     | "show events" | usb:/events |
| --- | ------------------- | --- | ------------- | ----------- |
CommandHistory
| Release        |     |     | Modification      |     |
| -------------- | --- | --- | ----------------- | --- |
| 10.08          |     |     | AddedSCP support. |     |
| 10.07orearlier |     |     | --                |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| copy core-dump |     | [<MEMBER/SLOT>] |     | daemon |
| -------------- | --- | --------------- | --- | ------ |
copy core-dump [<MEMBER/SLOT>] daemon <DAEMON-NAME>[:<INSTANCE-ID>] <REMOTE-URL> [vrf <VRF-
NAME>]
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<MEMBER/SLOT> SpecifiestheslotIDonan8400or6400switch.Required.
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
<DAEMON-NAME>
Specifiesthenameofthedaemon.Required.
[:<INSTANCE-ID>] Specifiestheinstanceofthedaemoncoredump.Optional.
<REMOTE_URL>
SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
{tftp://}{<IP> | <HOST>}[:<PORT>]
n
[;blocksize=<VAL>]/<FILE>
37
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ----------------------- | --- |

| Parameter |     |     | Description |     |                     |           |
| --------- | --- | --- | ----------- | --- | ------------------- | --------- |
|           |     |     | n {sftp://| |     | scp://<USER>@}{<IP> | | <HOST>} |
[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRFnamed
defaultisused.Optional.
Examples
Copyingthecoredumpfromdaemonops-vlandtoaremoteURLwithaVRFnamedmgmt:
switch# copy core-dump daemon ops-vland sftp://abc@10.0.14.211/vland_coredump.xz vrf
mgmt
Copyingthecoredumpfromdaemonops-vlandtoaremoteURLwithaVRFnamedmgmt:
switch# copy core-dump daemon ops-vland scp://abc@10.0.14.211/vland_coredump.xz vrf
mgmt
Copyingthecoredumpfromdaemonops-switchdtoaUSBdrive:
| switch# | copy core-dump | daemon ops-switchd |     | usb:/switchd |     |     |
| ------- | -------------- | ------------------ | --- | ------------ | --- | --- |
CopyingthecoredumpwithslotID1/1fromdaemonhpe-sysmondtoaremoteURL:
switch# copy core-dump 1/1 daemon hpe-sysmond sftp://abc@10.0.14.206/core.hpe-
| sysmond.xz | vrf mgmt |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
Copyingthecoredumpfromthehpe-configprocesstoaUSBdrive:
| switch# | copy core-dump | daemon hpe-config |     | usb:/config_core |     |     |
| ------- | -------------- | ----------------- | --- | ---------------- | --- | --- |
CommandHistory
| Release        |     |     | Modification      |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400           |     |                 | forthiscommand. |     |        |     |
| -------------- | --- | --------------- | --------------- | --- | ------ | --- |
| copy core-dump |     | [<MEMBER/SLOT>] |                 |     | kernel |     |
SupportabilityCopy|38

copy core-dump [<MEMBER/SLOT>] kernel <REMOTE-URL> [vrf <VRF-NAME>]

Description

Copies a kernel core dump using TFTP, SFTP, or SCP.

Parameter

<MEMBER/SLOT>

<REMOTE-URL>

Description

Specifies the slot ID on an 8400 or 6400 switch. Required.
Syntax: Slot number for line (1/1-1/4, 1/7-1/10) MM(1/5 or 1/6)

Specifies the URL to copy the command output. Required.
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}

[:<PORT>]/<FILE>

vrf <VRF-NAME>

Specifies the VRF name. The default VRF name is default. Optional.

Examples

Copying the kernel core dump to the URL:

switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz

Copying the kernel core dump to the URL with the VRF named mgmt:

switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz vrf mgmt

Copying the kernel core dump from slot ID 1/1 to the URL with the VRF named mgmt:

switch# copy core-dump 1/1 kernel sftp://abc@10.0.14.206/kernel_dump.tar.gz vrf mgmt

Copying the kernel core dump from slot ID 1/1 to the URL with the VRF named mgmt:

switch# copy core-dump 1/1 kernel scp://abc@10.0.14.206/kernel_dump.tar.gz vrf mgmt

Command History

Release

10.08

Modification

Added SCP support.

10.07 or earlier

--

Command Information

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

39

| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400           |                 |                 |        | forthiscommand. |                      |
| -------------- | --------------- | --------------- | ------ | --------------- | -------------------- |
| copy core-dump |                 | [<MEMBER/SLOT>] |        |                 | kernel <STORAGE-URL> |
| copy core-dump | [<MEMBER/SLOT>] |                 | kernel | <STORAGE-URL>   |                      |
Description
CopiesthekernelcoredumptoaUSBdrive.
| Parameter     |     |     |     | Description                  |     |
| ------------- | --- | --- | --- | ---------------------------- | --- |
| <MEMBER/SLOT> |     |     |     | SpecifiestheslotID.Required. |     |
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput.Required. |     |
| ------------- | --- | --- | --- | -------------------------------------------- | --- |
Syntax:{usb]:/<FILE>
Examples
CopyingthekernelcoredumptoaUSBdrive:
| switch# | copy core-dump | kernel | usb:/kernel.tar.gz |     |     |
| ------- | -------------- | ------ | ------------------ | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
| copy core-dump |     | vsf | member | daemon |     |
| -------------- | --- | --- | ------ | ------ | --- |
Applicablefor6300switchesonly.
| copy core-dump | vsf              | member <MEMBER-ID> |                              |     |     |
| -------------- | ---------------- | ------------------ | ---------------------------- | --- | --- |
| daemon         | [<DAEMON-NAME>   | |                  | <DAEMON-NAME>:<INSTANCE-ID>] |     |     |
| <REMOTE-URL>   | [vrf <VRF-NAME>] |                    |                              |     |     |
| copy core-dump | vsf              | member <MEMBER-ID> |                              |     |     |
| daemon         | [<DAEMON-NAME>   | |                  | <DAEMON-NAME>:<INSTANCE-ID>] |     |     |
<STORAGE-URL>
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
SupportabilityCopy|40

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsf member <MEMBER-ID> Specifiesthemember-idoftheVSFmember.Required.
| <DAEMON-NAME> |     |     | Specifiesthenameofthedaemon.Required. |     |     |
| ------------- | --- | --- | ------------------------------------- | --- | --- |
[:<INSTANCE-ID>] Specifiestheinstanceofthedaemoncoredump.Optional.
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
|     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --------- |
[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRFnamed
defaultisused.Optional.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.Required.
Syntax:{usb}:/<FILE>
Examples
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch#                          | copy core-dump | vsf member | 1 daemon hpe-sysmond |     |     |
| -------------------------------- | -------------- | ---------- | -------------------- | --- | --- |
| sftp://abc@10.0.14.206/sysmon.xz |                |            | vrf mgmt             |     |     |
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch#                          | copy core-dump | vsf member | 2 daemon hpe-sysmond |     |     |
| -------------------------------- | -------------- | ---------- | -------------------- | --- | --- |
| scp://user@10.0.14.206/sysmon.xz |                |            | vrf mgmt             |     |     |
CommandHistory
| Release        |     |     | Modification      |     |     |
| -------------- | --- | --- | ----------------- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |
| 10.07orearlier |     |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy core-dump |     | vsf member | kernel |     |     |
| -------------- | --- | ---------- | ------ | --- | --- |
Applicablefor6300switchesonly.
copy core-dump vsf member <MEMBER-ID> kernel <REMOTE-URL> [vrf <VRF-NAME>]
| copy core-dump | vsf member | <MEMBER-ID> | kernel <STORAGE-URL> |     |     |
| -------------- | ---------- | ----------- | -------------------- | --- | --- |
41
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ----------------------- | --- | --- |

Description
Copiesthekernelcore-dumpusingTFTP,SFTP,SCP,orUSB.
| Parameter   |     | Description                                   |     |     |
| ----------- | --- | --------------------------------------------- | --- | --- |
| <MEMBER-ID> |     | Specifiesthemember-idoftheVSFmember.Required. |     |     |
<REMOTE_URL>
SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
{tftp://}{<IP> | <HOST>}[:<PORT>]
n
[;blocksize=<VAL>]/<FILE>
|     |     | {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --------- | ------------------- | --------- |
n
[:<PORT>]/<FILE>
vrf <VRF-NAME>
SpecifiestheVRFname.IfnoVRFnameisprovided,theVRF
nameddefaultisused.Optional.
| <STORAGE-URL> |     | SpecifiestheUSBtocopycommandoutput.Required. |     |     |
| ------------- | --- | -------------------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Examples
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel sftp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel scp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
CommandHistory
| Release        |     | Modification      |     |     |
| -------------- | --- | ----------------- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |
| 10.07orearlier |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy diag-dump | feature | <FEATURE> |     |     |
| -------------- | ------- | --------- | --- | --- |
copy diag-dump feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
SupportabilityCopy|42

CopiesthespecifieddiagnosticinformationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<FEATURE>
Thenameofafeature,forexampleaaaorvrrp.
Required.
{<REMOTE-URL> [vrf <VRF-NAME> |<STORAGE-URL>]} SelecteithertheremoteURLorthestorageURLfor
thedestinationofthecopiedcommandoutput.
Required.
| <REMOTE-URL> |     |     |     | SpecifiestheremotedestinationURL.Required.The |     |     |
| ------------ | --- | --- | --- | --------------------------------------------- | --- | --- |
syntaxoftheURListhefollowing:
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.IfnoVRFnameisprovided, |     |     |
| -------------- | --- | --- | --- | ------------------------------------------ | --- | --- |
theVRFnameddefaultisused.Optional.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Required.
Syntax:{usb}:/<FILE>
Examples
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa tftp://10.100.0.12/diagdump.txt vrf mgmt
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch#
copy diag-dump feature aaa scp://user@10.100.0.12/diagdump.txt vrf mgmt
CopyingtheoutputfromthevrrpfeaturetoaUSBdrive:
| switch# copy | diag-dump | feature vrrp | usb:/diagdump.txt |     |     |     |
| ------------ | --------- | ------------ | ----------------- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification      |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     | --                |     |     |     |
CommandInformation
43
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy diag-dump |     | local-file |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- |
copy diag-dump local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
{<REMOTE-URL> [vrf <VRF-NAME>] |<STORAGE-URL>} SelecteitherthestorageURLortheremoteURLfor
thedestinationofthecopiedcommandoutput.
Required.
<REMOTE-URL>
SpecifiestheURLtocopythecommandoutput.
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME>
SpecifiestheVRFname.ThedefaultVRFnameis
default.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Thecopy diag-dump local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump local-
filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic | local-file |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | --- |
switch# copy diag-dump local-file tftp://10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic | local-file |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | --- |
switch# copy diag-dump local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaUSBdrive:
| switch# | diag-dump | aaa basic | local-file |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | --- |
switch#
|     | copy diag-dump | local-file | usb:/diagdump.txt |     |     |     |
| --- | -------------- | ---------- | ----------------- | --- | --- | --- |
SupportabilityCopy|44

CommandHistory
| Release        |     | Modification      |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy diag-dump | vsf member | local-file |     |     |     |
| -------------- | ---------- | ---------- | --- | --- | --- |
Applicablefor6300switchesonly.
copy diag-dump vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-
URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,orUSB.
| Parameter  |             |     | Description                          |     |     |
| ---------- | ----------- | --- | ------------------------------------ | --- | --- |
| vsf member | <MEMBER-ID> |     | Specifiesthemember-idoftheVSFmember. |     |     |
Required.
{<REMOTE-URL> [vrf <VRF-NAME>] |<STORAGE-URL>} SelecteitherthestorageURLortheremoteURLfor
thedestinationofthecopiedcommandoutput.
Required.
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.ThedefaultVRFnameis |     |     |
| -------------- | --- | --- | --------------------------------------- | --- | --- |
default.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Thecopy diag-dump local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump local-
filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
45
| AOS-CX10.08DiagnosticsandSupportabilityGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | ----------------------- | --- | --- | --- | --- |

| switch# | diag-dump aaa basic | local-file |     |     |
| ------- | ------------------- | ---------- | --- | --- |
switch#
copy diag-dump vsf member 2 local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump aaa basic | local-file |     |     |
| ------- | ------------------- | ---------- | --- | --- |
switch# copy diag-dump vsf member 2 local-file tftp://10.100.0.12/diagdump.txt
CommandHistory
| Release        |     | Modification      |     |     |
| -------------- | --- | ----------------- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |
| 10.07orearlier |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy <IMAGE>
copy <IMAGE> {<STORAGE-URL> | <REMOTE-URL>} <FILE-NAME> [vrf <VRF-NAME>]
Description
CopiestheimageusingTFTP,SFTP,SCP,orUSB.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<IMAGE>
Specifiestheimage.
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | ----------------------------------- | --- | --- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | ----------- | ------------------- | --------- |
[:<PORT>]/<FILE>
| <FILE-NAME> |     | Specifiesthefilename. |     |     |
| ----------- | --- | --------------------- | --- | --- |
vrf <VRF-NAME>
SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
SupportabilityCopy|46

CopyingtheimagetoaremoteURL:
| switch# | copy scp://root@20.0.1.1/primary.swi |     |     | primary | vrf mgmt |     |
| ------- | ------------------------------------ | --- | --- | ------- | -------- | --- |
CopyingthesecondaryimagetoaremoteURL:
| switch# | copy secondary | scp://root@20.0.1.1/primary.swi |     |     | vrf mgmt |     |
| ------- | -------------- | ------------------------------- | --- | --- | -------- | --- |
CommandHistory
| Release        |     |     | Modification      |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy running-config
copy running-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- | --- |
Syntax:
|     |     |     | n {tftp://}{<IP> |     | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | --- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> |     | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --- | --------- |
[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     | Specifiestherunningconfiguration. |     |     |     |
| -------------------- | --- | --- | --------------------------------- | --- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
47
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- |

CopyingtherunningconfigurationtoaremoteURL:
switch# copy running-config scp://root@10.0.1.1/config cli vrf mgmt
CommandHistory
| Release        |     | Modification      |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| copy show-tech | feature |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- |
copy show-tech feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesshowtechoutputusingTFTP,SFTP,SCP,andUSB.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{<REMOTE-URL> [vrf <VRF-NAME> | <STORAGE-URL>]} SelecteithertheremoteURLorthestorageURL
forthedestinationofthecopiedcommandoutput.
Required.
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- |
Required.
Syntax:
|     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.ThedefaultVRFnameis |     |     |
| -------------- | --- | --- | --------------------------------------- | --- | --- |
default.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Required.
Syntax:{usb}:/<FILE>
Example
CopyingshowtechoutputoftheaaafeatureusingSCP:
switch# copy show-tech feature aaa scp://user@10.0.0.12/file.txt vrf mgmt
SupportabilityCopy|48

CopyingshowtechoutputoftheconfigfeatureusingSFTPonthemgmtVRF:
switch# copy show-tech feature config sftp://root@10.0.0.1/tech.txt vrf mgmt
CommandHistory
| Release        |     | Modification      |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy show-tech | local-file |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- |
copy show-tech local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
Copiesshowtechoutputstoredinalocalfile.
| Parameter     |                  |                 | Description |     |     |
| ------------- | ---------------- | --------------- | ----------- | --- | --- |
| {<REMOTE-URL> | [vrf <VRF-NAME>] | | <STORAGE-URL> | ]}          |     |     |
SelecteithertheremoteURLorthestorageURL
forthedestinationofthecopiedcommand
output.Required.
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.ThedefaultVRFname |     |     |
| -------------- | --- | --- | ------------------------------------- | --- | --- |
isdefault.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Beforeenteringthecopy show-tech local-filecommand,runtheshow techcommandwiththelocal-
fileparameterforthespecifiedfeature.
Examples
CopyingtheoutputtoaremoteURL:
49
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- |

| switch# | copy show-tech | local-file |     | tftp://10.100.0.12/file.txt |     |
| ------- | -------------- | ---------- | --- | --------------------------- | --- |
CopyingtheoutputtoaremoteURL:
switch# copy show-tech local-file scp://user@10.100.0.12/file.txt
CopyingtheoutputtoaremoteURLwithaVRF:
switch# copy show-tech local-file tftp://10.100.0.12/file.txt vrf mgmt
CopyingtheoutputtoaUSB:
| switch# | copy show-tech | local-file |     | usb:/file |     |
| ------- | -------------- | ---------- | --- | --------- | --- |
CommandHistory
| Release        |     |     |     | Modification      |     |
| -------------- | --- | --- | --- | ----------------- | --- |
| 10.08          |     |     |     | AddedSCP support. |     |
| 10.07orearlier |     |     |     | --                |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy show-tech |     | vsf member |     | local-file |     |
| -------------- | --- | ---------- | --- | ---------- | --- |
Applicablefor6300switchesonly.
copy show-tech vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-
URL>}
Description
Copiesshowtechoutputstoredinalocalfile.
| Parameter  |             |     |     |     | Description                          |
| ---------- | ----------- | --- | --- | --- | ------------------------------------ |
| vsf member | <MEMBER-ID> |     |     |     | Specifiesthemember-idoftheVSFmember. |
Required.
| {<REMOTE-URL> | [vrf | <VRF-NAME>] | |   | <STORAGE-URL> | ]}  |
| ------------- | ---- | ----------- | --- | ------------- | --- |
SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopiedcommand
output.Required.
| <REMOTE-URL> |     |     |     |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | --- | --- | --- | -------------------------------------- |
Syntax:
SupportabilityCopy|50

| Parameter |     |     |     | Description      |                    |     |
| --------- | --- | --- | --- | ---------------- | ------------------ | --- |
|           |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.ThedefaultVRFname |     |     |
| -------------- | --- | --- | --- | ------------------------------------- | --- | --- |
isdefault.Optional.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Syntax:{usb}:/<FILE>
Usage
Beforeenteringthecopy show-tech local-filecommand,runtheshow techcommandwiththelocal-
fileparameterforthespecifiedfeature.
Examples
CopyingtheoutputtoaremoteURLwithaVRF:
switch# copy show-tech vsf member 2 local-file tftp://10.100.0.12/showtech.txt vrf
mgmt
CopyingtheoutputtoaUSB:
| switch# | copy show-tech | vsf member | 2 local-file | usb:/file |     |     |
| ------- | -------------- | ---------- | ------------ | --------- | --- | --- |
CommandHistory
| Release        |     |     | Modification      |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy startup-config
copy startup-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationusingTFTP,SFTP,SCP,orUSB.
51
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | ----------------------- | --- | --- | --- |

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
{tftp://}{<IP> | <HOST>}[:<PORT>]
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | --------- | ------------------- | --------- |
n
[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     | Specifiesthestartupconfiguration. |     |     |
| -------------------- | --- | --- | --------------------------------- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthestartupconfigurationtoaremoteURL:
switch# copy startup-config scp://root@10.0.1.1/config json vrf mgmt
CommandHistory
| Release        |     |     | Modification      |     |     |
| -------------- | --- | --- | ----------------- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |
| 10.07orearlier |     |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy support-files
| copy support-files | previous-boot          | <REMOTE-URL>  |                  | [vrf <VRF-NAME>] |     |
| ------------------ | ---------------------- | ------------- | ---------------- | ---------------- | --- |
| copy support-files | all <REMOTE-URL>       |               | [vrf <VRF-NAME>] |                  |     |
| copy support-files | <REMOTE-URL>           | [vrf          | <VRF-NAME>]      |                  |     |
| copy support-files | feature <FEATURE-NAME> |               | <STORAGE-URL>    |                  |     |
| copy support-files | previous-boot          | <STORAGE-URL> |                  |                  |     |
| copy support-files | all <STORAGE-URL>      |               |                  |                  |     |
| copy support-files | <STORAGE-URL>          |               |                  |                  |     |
Forthe6400switchonly:
copy support-files module <SLOT-ID> <REMOTE-URL> [vrf <VRF-NAME>]
| copy support-files | standby <REMOTE-URL> |     | [vrf          | <VRF-NAME>] |     |
| ------------------ | -------------------- | --- | ------------- | ----------- | --- |
| copy support-files | module <SLOT-ID>     |     | <STORAGE-URL> |             |     |
SupportabilityCopy|52

Forthe6300switchonly:
copy support-files vsf member <MEMBER-ID> <REMOTE-URL> {vrf <VRF-NAME>}
| copy support-files | vsf member | <MEMBER-ID> | <STORAGE-URL> |     |     |     |
| ------------------ | ---------- | ----------- | ------------- | --- | --- | --- |
Description
Copiesasetofsupportfilestoacompressedfileintar.gzformatusingTFTP,SFTP,SCP,orUSBortoa
directoryoverSFTPorUSB.
ThiscommanddoesnotsupportTFTPtransferon6300switches.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<FEATURE-NAME>
Thefeaturename,forexample,aaa.
{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]} SelecteithertheremoteURLorthestorageURL
forthedestinationofthecopiedcommand
output.Required.
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.ThedefaultVRFname |     |     |
| -------------- | --- | --- | --- | ------------------------------------- | --- | --- |
isdefault.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
| <MEMBER-ID> |     |     |     | ThememberIDintheVSFstack.Range1-10.        |     |     |
| ----------- | --- | --- | --- | ------------------------------------------ | --- | --- |
| <SLOT-ID>   |     |     |     | SpecifiestheslotIDon6400switches.Optional. |     |     |
Syntax:Slotnumberforline(1/1-1/4,1/7-
1/10)MM(1/5or1/6)
Usage
Iffeaturenameisnotprovided,thecommandcollectsgenericsystem-specificsupportinformation.Ifa
featurenameisprovided,thecommandcollectsfeature-specificsupportinformation.
InordertocollectdatafromstandbyandmemberinaVSFstack,thecommandwillpromptforthelocaluser
passwordonce.
Inordertocollectdatafromthestandby6400swtich,thecommandwillpromptforthelocaluserpasswordonce.
Examples
CopyingthesupportfilestoaremoteURL:
| switch# copy | support-files | tftp://10.100.0.12/file.tar.gz |     |     |     |     |
| ------------ | ------------- | ------------------------------ | --- | --- | --- | --- |
53
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- |

CopyingthesupportfilesofthelldpfeaturetoaremoteURLwithaspecifiedVRF:
switch# copy support-files feature lldp tftp://10.100.0.12/file.tar.gz vrf mgmt
CopyingthesupportfilesfromthepreviousboottoaremoteURLwithaspecifiedVRF:
switch# copy support-files previous-boot scp://user@10.0.14.206/file.tar.gz vrf mgmt
CopyingthesupportfilestoaUSB:
switch#
|     | copy support-files | usb:/file.tar.gz |     |
| --- | ------------------ | ---------------- | --- |
CopyingthefilesfromamoduletoaremoteURLwithaspecifiedVRFonan8400or6400switch:
switch# copy support-files module 1/1 tftp://10.100.0.12/file.tar.gz vrf mgmt
CopyingthefilesfromastandbymoduletoaremoteURLwithaspecifiedVRFonan8400or6400switch:
switch# copy support-files standby sftp://root@10.0.14.216/file.tar.gz vrf mgmt
CopyingallthesupportfilestoaremoteURL:
switch# copy support-files all sftp://root@10.0.14.216/file.tar.gz vrf mgmt
CopyingthesupportfilesoftheconfigfeaturetoaUSB:
| switch# | copy support-files | feature config | usb:/file.tar.gz |
| ------- | ------------------ | -------------- | ---------------- |
CommandHistory
| Release        |     | Modification      |     |
| -------------- | --- | ----------------- | --- |
| 10.08          |     | AddedSCP support. |     |
| 10.07orearlier |     | --                |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy support-files | local-file |     |     |
| ------------------ | ---------- | --- | --- |
copy support-files [feature <FEATURE-NAME> | previous-boot | all | module <SLOT-ID> |
standby | vsf member <MEMBER-ID>] local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
SupportabilityCopy|54

Themoduleandstandbyaresupportedonlyon6400switch.Thevsf memberissupportedonlyon6300switch.
Description
Storesasetofsupportfilesasacompressedfileintheswitchlocallyandcopiesthepreservedsupportfiles
toadirectoryusingTFTP,SFTP,SCP,orUSB.
Youcanstoreonlyonecopyofthesupportfilelocally.Whenyoustoreanewsupportfile,itoverwritestheexisting
supportfile.
| Parameter      |     |     | Description                            |
| -------------- | --- | --- | -------------------------------------- |
| <FEATURE-NAME> |     |     | Specifiesthefeatureforthesupportfiles. |
<SLOT-ID> Specifiesthemoduleslotnumberidentifierforthesupportfiles.
Range:1/1-1/4,1/7-1/10
<MEMBER-ID> SpecifiestheVSFmemberidentifierforthesupportfiles.Range:1-
10
| <REMOTE-URL>  |     |     | SpecifiestheURLtocopythesupportfiles.           |
| ------------- | --- | --- | ----------------------------------------------- |
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopythesupportfiles.           |
| <VRF-NAME>    |     |     | SpecifiestheVRFname.ThedefaultVRFnameisdefault. |
Usage
Ifthecopyofthesupportfilestothedestinationfails,analternateoptionispromptedtostorethecollected
datainthelocalfile.Thishelpsustoretrythecopyprocessusingcopy support-files local-file
<REMOTE-URL/STORAGE-URL>withouttheneedofregeneratingthefile.
Examples
Copyingsupportfiletothelocalfile:
| switch# copy | support-files | local-file     |                 |
| ------------ | ------------- | -------------- | --------------- |
| switch# copy | support-files | feature        | lldp local-file |
| switch# copy | support-files | previous-boot  | local-file      |
| switch# copy | support-files | all local-file |                 |
The operation to copy all support files could take a while to complete.
| Do you want  | to continue   | (y/n)?     |            |
| ------------ | ------------- | ---------- | ---------- |
| switch# copy | support-files | module 1/1 | local-file |
switch#
| copy         | support-files | standby    | local-file   |
| ------------ | ------------- | ---------- | ------------ |
| switch# copy | support-files | vsf member | 7 local-file |
CopyinglocalsupportfiletoaremoteURLandstorageURL:
switch# copy support-files local-file usb:/support_files_dir_path/
switch# copy support-files local-file scp://root@10.0.14.206//support_files_dir_
| path/abc.tar.gz | vrf mgmt |     |     |
| --------------- | -------- | --- | --- |
CommandHistory
55
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Release        |     |     | Modification |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy support-files | vsf | member |     |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- | --- |
Applicablefor6300switchesonly.
copy support-files vsf member <MEMBER-ID> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesasetofsupportfilesusingTFTP,SFTP,SCP,orUSB.
| Parameter   |     |     |     | Description                          |     |     |
| ----------- | --- | --- | --- | ------------------------------------ | --- | --- |
| <MEMBER-ID> |     |     |     | Specifiedthemember-idoftheVSFmember. |     |     |
Required.
{<REMOTE-URL> [vrf <VRF-NAME> | <STORAGE-URL>]} SelecteithertheremoteURLorthestorageURL
forthedestinationofthecopiedcommandoutput.
Required.
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.ThedefaultVRFnameis |     |     |
| -------------- | --- | --- | --- | --------------------------------------- | --- | --- |
default.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Iffeaturenameisnotprovided,thecommandcollectsgenericsystem-specificsupportinformation.Ifa
featurenameisprovided,thecommandcollectsfeature-specificsupportinformation.
Examples
CopyingthesupportfilestoaUSB:
| switch# | copy support-files | vsf member | 2 usb:/file.tar.gz |     |     |     |
| ------- | ------------------ | ---------- | ------------------ | --- | --- | --- |
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
SupportabilityCopy|56

switch# copy support-files vsf member 2 scp://user@10.100.0.12/file.tar.gz/ vrf mgmt
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch# copy support-files vsf member 2 sftp://user@10.100.0.12/support_files_dir_
| path/ vrf | mgmt |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
CommandHistory
| Release        |     | Modification      |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy support-log
copy support-log <DAEMON-NAME> [<MEMBER/SLOT>] {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-
NAME>]}
Description
CopiesthespecifiedsupportlogforadaemonTFTP,SFTP,SCP,orUSB.
| Parameter     |     |     | Description                             |     |     |
| ------------- | --- | --- | --------------------------------------- | --- | --- |
| <MEMBER/SLOT> |     |     | SpecifiestheslotIDonan8400or6400switch. |     |     |
Optional.
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)
MM(1/5or1/6)
| <DAEMON-NAME> |     |     | Specifiesthenameofthedaemon.Required. |     |     |
| ------------- | --- | --- | ------------------------------------- | --- | --- |
{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]} SelectseitherthestorageURLortheremoteURL
forthedestinationofthecopiedcommandoutput.
Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
57
| AOS-CX10.08DiagnosticsandSupportabilityGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | ----------------------- | --- | --- | --- | --- |

Parameter

vrf <VRF-NAME>

Usage

Description

Specifies the VRF name. If no VRF name is
provided, the VRF named default is used. Optional.

Fast log is a high performance, per-daemon binary logging infrastructure used to debug daemon level issues
by precisely capturing the per daemon/module/functionalities debug traces in real time. Fast log, also
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

Administrators or local user group members with execution rights
for this command.

copy support-log vsf member

Applicable for 6300 switches only.
copy support-log vsf member <MEMBER-ID> <DAEMON-NAME> {<STORAGE-URL> | <REMOTE-URL> [vrf
<VRF-NAME>]}

Supportability Copy | 58

Description
CopiesthespecifiedsupportlogforadaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter   |     |     |     | Description                          |     |     |
| ----------- | --- | --- | --- | ------------------------------------ | --- | --- |
| <MEMBER-ID> |     |     |     | Specifiesthemember-idoftheVSFmember. |     |     |
Required.
<DAEMON-NAME>
Specifiesthenameofthedaemon.Required.
{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]} SelectseitherthestorageURLortheremoteURL
forthedestinationofthecopiedcommandoutput.
Required.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.IfnoVRFnameis |     |     |
| -------------- | --- | --- | --- | --------------------------------- | --- | --- |
provided,theVRFnameddefaultisused.Optional.
Usage
Fastlogisahighperformance,per-daemonbinarylogginginfrastructureusedtodebugdaemonlevelissues
bypreciselycapturingtheperdaemon/module/functionalitiesdebugtracesinrealtime.Fastlog,also
referredtoassupportlogs,helpsuserstounderstandthefeatureinternalsanditsspecifichappenings.The
fastlogsfromonedaemonarenotoverwrittenbyotherdaemonlogsbecausefastlogsarecapturedaspart
ofadaemoncoredump.Fastlogsareenabledbydefault.
Examples
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log vsf member 2 hpe-fand tftp://10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log vsf member 2 hpe-fand scp://user@10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaUSB:
| switch# copy | support-log | vsf member | 2 hpe-fand | usb:/support-log |     |     |
| ------------ | ----------- | ---------- | ---------- | ---------------- | --- | --- |
CommandHistory
59
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Release        |     | Modification      |
| -------------- | --- | ----------------- |
| 10.08          |     | AddedSCP support. |
| 10.07orearlier |     | --                |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
SupportabilityCopy|60

Chapter 9
Traceroute
Traceroute
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagramProtocol
(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashoplimit,isused
indeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
| Traceroute | over VXLAN |     |     |
| ---------- | ---------- | --- | --- |
Tracerouteandtraceroute6aresupportedoverVXLANfromVTEPtoVTEP,VTEPtohost,andhosttoVTEP
overL2VNI/L3VNI.AuniqueIPonVTEPshouldbeusedasthetraceroutesourceanddestination.Both
sourceanddestinationVTEPsrequireAOS-CX10.8orlaterforthisfeaturetowork.Tracerouteand
traceroute6overVXLANcannotbeusedtotracktheunderlayhopsbetweenVTEPs.
| Traceroute | commands |     |     |
| ---------- | -------- | --- | --- |
traceroute
traceroute {<IPV4-ADDR> | <HOSTNAME>} [ip-option loosesourceroute <IPV4-ADDR>] [dstport
<NUMBER> | maxttl <NUMBER> | minttl <NUMBER> | probes <NUMBER> | timeout <TIME>] [vrf <VRF-
| NAME>] source | {<IPV4-ADDR> | | <IFNAME>} |     |
| ------------- | ------------ | ----------- | --- |
TracerouteoverVXLANwithip-option loosesourcerouteonL3VNIisnotsupported.
Description
UsestracerouteforthespecifiedIPv4addressorhostnamewithorwithoutoptionalparameters.
| Parameter    |             |     | Description                                  |
| ------------ | ----------- | --- | -------------------------------------------- |
| IPv4-address | <IPV4-ADDR> |     | SpecifiestheIPv4address.                     |
| hostname     |             |     | Specifiesthehostnameofthedevicetotraceroute. |
| ip-option    |             |     | SpecifiestheIPoption.                        |
loosesourceroute <IPV4-ADDR> Specifiestherouteforloosesourcerecordroute.Enteroneor
moreintermediaterouterIPaddressesseparatedby','forloose
sourcerouting.
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
| maxttl <NUMBER> |     |     |     |
| --------------- | --- | --- | --- |
Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
minttl <NUMBER> SpecifiestheMinimumnumberofhopstoreachthedestination,
<1-255>.Default:1
| probes <NUMBER> |     |     | Specifiesthenumberofprobes,<1-5>.Default:3 |
| --------------- | --- | --- | ------------------------------------------ |
61
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | ----------------------- | --- |

| Parameter |     | Description |
| --------- | --- | ----------- |
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.
| source {<IPV4-ADDR> | | <IFNAME>} |     |
| ------------------- | ----------- | --- |
SpecifiesthesourceIPv4addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagramProtocol
(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashoplimit,isused
indeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
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
| 1 10.0.40.2        | 0.002ms   | 0.002ms 0.001ms |
| ------------------ | --------- | --------------- |
| 2 10.0.30.1        | 0.002ms   | 0.001ms 0.001ms |
| 3 10.0.10.1        | 0.001ms   | 0.002ms 0.002ms |
| switch# traceroute | 10.0.10.1 | probes 2        |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 2
probes
| 1 10.0.40.2        | 0.002ms   | 0.002ms   |
| ------------------ | --------- | --------- |
| 2 10.0.30.1        | 0.002ms   | 0.001ms   |
| 3 10.0.10.1        | 0.001ms   | 0.002ms   |
| switch# traceroute | 10.0.10.1 | timeout 5 |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 5 sec. timeout, 3
Traceroute|62

probes
| 1       | 10.0.40.2  | 0.002ms   |     | 0.002ms | 0.001ms |     |     |     |
| ------- | ---------- | --------- | --- | ------- | ------- | --- | --- | --- |
| 2       | 10.0.30.1  | 0.002ms   |     | 0.001ms | 0.001ms |     |     |     |
| 3       | 10.0.10.1  | 0.001ms   |     | 0.002ms | 0.002ms |     |     |     |
| switch# | traceroute | localhost |     | vrf     | red     |     |     |     |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1       | 127.0.0.1  | 0.003ms   |     | 0.002ms | 0.001ms |     |     |     |
| ------- | ---------- | --------- | --- | ------- | ------- | --- | --- | --- |
| switch# | traceroute | localhost |     | mgmt    |         |     |     |     |
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
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2 maxttl 20 timeout
| 5 minttl | 1 probes | 3   | dstport | 33434 |     |     |     |     |
| -------- | -------- | --- | ------- | ----- | --- | --- | --- | --- |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1          | 10.0.40.2  | 0.002ms  |             | 0.002ms | 0.001ms     |     |     |     |
| ---------- | ---------- | -------- | ----------- | ------- | ----------- | --- | --- | --- |
| 2          | 10.0.30.1  | 0.002ms  |             | 0.001ms | 0.001ms     |     |     |     |
| 3          | 10.0.10.1  | 0.001ms  |             | 0.002ms | 0.002ms     |     |     |     |
| switch#    | traceroute | 10.0.0.2 |             | source  | 10.0.0.1    |     |     |     |
| traceroute | to         | 10.0.0.2 | (10.0.0.2), |         | 30 hops max |     |     |     |
| 1          | 10.0.0.2   | 0.299ms  | 0.155ms     |         | 0.115ms     |     |     |     |
switch#
|            | traceroute | 10.0.0.2 |             | source | 1/1/1       |     |     |     |
| ---------- | ---------- | -------- | ----------- | ------ | ----------- | --- | --- | --- |
| traceroute | to         | 10.0.0.2 | (10.0.0.2), |        | 30 hops max |     |     |     |
| 1          | 10.0.0.2   | 0.479ms  | 0.222ms     |        | 0.171ms     |     |     |     |
CommandHistory
| Release |     |     |     |     | Modification |                     |           |      |
| ------- | --- | --- | --- | --- | ------------ | ------------------- | --------- | ---- |
| 10.08   |     |     |     |     | Addedsource  | IP addressandsource | interface | name |
parameters.
| 10.07orearlier |     |     |     |     | --  |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
CommandInformation
63
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
traceroute6
traceroute6 {<IPV6-ADDR> | <HOSTNAME>} [dstport <NUMBER> | maxttl <NUMBER> | probes <NUMBER>
| timeout <TIME>] [vrf <VRF-NAME>] source {<IPV6-ADDR> | <IFNAME>}
Description
UsestracerouteforthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.
| Parameter    |             |     | Description              |     |
| ------------ | ----------- | --- | ------------------------ | --- |
| IPv6-address | <IPV6-ADDR> |     | SpecifiestheIPv6address. |     |
hostname
Specifiesthehostnameofthedevicetotraceroute.
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
maxttl <NUMBER>
Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
| probes <NUMBER> |     |     | Specifiesthenumberofprobes,<1-5>.Default:3 |     |
| --------------- | --- | --- | ------------------------------------------ | --- |
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse,<VRF-
NAME>.
| source {<IPV6-ADDR> |     | | <IFNAME>} |     |     |
| ------------------- | --- | ----------- | --- | --- |
SpecifiesthesourceIPv6addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagramProtocol
(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashoplimit,isused
indeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
Examples
| switch# | traceroute6 | 0:0::0:1 |     |     |
| ------- | ----------- | -------- | --- | --- |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117 ms  | 0.032 ms 0.021 | ms  |
| ----------- | ----------- | --------- | -------------- | --- |
| switch#     | traceroute6 | localhost |                |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.089 ms        | 0.03 ms 0.014 | ms  |
| ----------- | ----------- | --------------- | ------------- | --- |
| switch#     | traceroute6 | 0:0::0:1 maxttl | 30            |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
Traceroute|64

byte packets
| 1 localhost | (::1)       | 0.117    | ms      | 0.032 | ms 0.021 | ms  |     |     |
| ----------- | ----------- | -------- | ------- | ----- | -------- | --- | --- | --- |
| switch#     | traceroute6 | 0:0::0:1 | dsrport |       | 33434    |     |     |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms     | 0.032 | ms 0.021 | ms  |     |     |
| ----------- | ----------- | -------- | ------ | ----- | -------- | --- | --- | --- |
| switch#     | traceroute6 | 0:0::0:1 | probes | 2     |          |     |     |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 2 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms      | 0.032 | ms  |     |     |     |
| ----------- | ----------- | -------- | ------- | ----- | --- | --- | --- | --- |
| switch#     | traceroute6 | 0:0::0:1 | timeout |       | 3   |     |     |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117     | ms  | 0.032   | ms 0.021 | ms  |     |     |
| ----------- | ----------- | --------- | --- | ------- | -------- | --- | --- | --- |
| switch#     | traceroute6 | localhost |     | vrf red |          |     |     |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.077     | ms  | 0.051 | ms 0.054 | ms  |     |     |
| ----------- | ----------- | --------- | --- | ----- | -------- | --- | --- | --- |
| switch#     | traceroute6 | localhost |     | mgmt  |          |     |     |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1) | 0.089 | ms  | 0.03 ms | 0.014 | ms  |     |     |
| ----------- | ----- | ----- | --- | ------- | ----- | --- | --- | --- |
switch# traceroute6 0:0::0:1 maxttl 30 timeout 3 probes 3 dstport 33434
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117   | ms     | 0.032   | ms 0.021 | ms  |     |     |
| ----------- | ----------- | ------- | ------ | ------- | -------- | --- | --- | --- |
| switch#     | traceroute6 | 2001::2 | source | 2001::1 |          |     |     |     |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3 probes,
| 24 byte   | packets     |         |        |        |     |           |     |     |
| --------- | ----------- | ------- | ------ | ------ | --- | --------- | --- | --- |
| 1 2001::2 | (2001::2)   | 0.4331  | ms     | 0.3186 | ms  | 0.1874 ms |     |     |
| switch#   | traceroute6 | 2001::2 | source | 1/1/1  |     |           |     |     |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3 probes,
| 24 byte   | packets   |        |     |        |     |           |     |     |
| --------- | --------- | ------ | --- | ------ | --- | --------- | --- | --- |
| 1 2001::2 | (2001::2) | 0.6145 | ms  | 0.4165 | ms  | 0.1620 ms |     |     |
CommandHistory
| Release |     |     |     | Modification |     |                     |           |      |
| ------- | --- | --- | --- | ------------ | --- | ------------------- | --------- | ---- |
| 10.08   |     |     |     | Addedsource  |     | IP addressandsource | interface | name |
parameters.
| 10.07orearlier |     |     |     | --  |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
65
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |

Chapter 10

Ping

Ping

The ping (Packet Internet Groper) command is a common method for troubleshooting the accessibility of
devices. It uses Internet Control Message Protocol (ICMP) echo requests and ICMP echo replies to determine
if another device is alive. It also measures the amount of time it takes to receive a reply from the specified
destination. The ping command is mostly used to verify IP connectivity between two endpoints which could
be switch to switch, host to host, or host to switch. The reply packet tells if the host received the ping and
the amount of time it took to return the packet.

Ping over VXLAN

Ping and ping6 are supported over VXLAN from VTEP to VTEP, VTEP to host, and host to VTEP over L2
VNI/L3 VNI. A unique IP on VTEP should be used as the source and destination. Both source and destination
VTEPs require AOS-CX 10.8 or later for this feature to work.

Ping commands

ping
ping <IPv4-ADDR> | <hostname> [data-fill <pattern> | datagram-size <size> |
interval <time> | repetitions <number> | timeout <time> | tos <number> |
ip-option {include-timestamp | include-timestamp-and-address | record-route} |
vrf <vrfname> | do-not-fragment][source {IPv4-ADDR | IFNAME}]

Ping on VXLAN with ip-option such as include-timestamp-and-address, include-timestamp and record-
route is not supported.

Description

Pings the specified IPv4 address or hostname with or without optional parameters.

Parameter

Description

ping <IPv4-ADDR>

Selects the IPv4 address to ping.

<HOSTNAME>

Selects the hostname to ping. Range: 1-256 characters

data-fill <PATTERN>

Specifies the data pattern in hexadecimal digits to send. A
maximum of 16 "pad" bytes can be specified to fill out the ICMP
packet. Default: AB

datagram-size <SIZE>

Specifies the ping datagram size. Range: 0-65399, default: 100.

interval <TIME>

repetitions <NUMBER>

Specifies the interval between successive ping requests in
seconds. Range: 1-60 seconds, default: 1 second.

Specifies the number of packets to send. Range: 1-10000 packets,
default: Five packets.

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

66

| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
timeout <TIME> Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
tos <NUMBER> SpecifiestheIPTypeofServicetobeusedinPingrequest.Range:
0-255
| ip-option | {include-timestamp |     |     | |   |     |     |     |     |
| --------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
SpecifiesanIPoption(record-routeortimestampoption).
| include-timestamp-and-address |     |     |     | |   |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
record-route}
| include-timestamp |     |     |     |     | Specifiestheintermediateroutertimestamp. |     |     |     |
| ----------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
include-timestamp-and-address SpecifiestheintermediateroutertimestampandIPaddress.
| record-route |     |     |     |     | Specifiestheintermediaterouteraddresses. |     |     |     |
| ------------ | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.WhenVRF
optionisnotgiven,thedefaultVRFisused.
source {IPv4-ADDR | IFNAME} SpecifiesthesourceIPv4addressorinterfacetouse.
do-not-fragment Specifiesthedo-not-fragment(DF)bitinIPheaderofthePing
packet.Thisoptiondoesnotallowthepackettobefragmented
whenithastogothroughasegmentwithasmallermaximum
transmissionunit(MTU).
Examples
PinginganIPv4address:
| switch#              | ping     | 10.0.0.0       |                           |            |        |        |            |             |
| -------------------- | -------- | -------------- | ------------------------- | ---------- | ------ | ------ | ---------- | ----------- |
| PING                 | 10.0.0.0 | (10.0.0.0)     |                           | 100(128)   | bytes  | of     | data.      |             |
| 108 bytes            |          | from 10.0.0.0: |                           | icmp_seq=1 | ttl=64 |        | time=0.035 | ms          |
| 108 bytes            |          | from 10.0.0.0: |                           | icmp_seq=2 | ttl=64 |        | time=0.034 | ms          |
| 108 bytes            |          | from 10.0.0.0: |                           | icmp_seq=3 | ttl=64 |        | time=0.034 | ms          |
| 108 bytes            |          | from 10.0.0.0: |                           | icmp_seq=4 | ttl=64 |        | time=0.034 | ms          |
| 108 bytes            |          | from 10.0.0.0: |                           | icmp_seq=5 | ttl=64 |        | time=0.033 | ms          |
| --- 10.0.0.0         |          | ping           | statistics                | ---        |        |        |            |             |
| 5 packets            |          | transmitted,   | 5                         | received,  | 0%     | packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |          |                | = 0.033/0.034/0.035/0.000 |            |        |        | ms         |             |
Pingingthelocalhost:
| switch# | ping      | localhost   |     |          |       |     |          |     |
| ------- | --------- | ----------- | --- | -------- | ----- | --- | -------- | --- |
| PING    | localhost | (127.0.0.1) |     | 100(128) | bytes |     | of data. |     |
108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.060 ms
108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.035 ms
108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.043 ms
108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.041 ms
108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.034 ms
| --- localhost        |     | ping         | statistics                | ---       |     |        |       |             |
| -------------------- | --- | ------------ | ------------------------- | --------- | --- | ------ | ----- | ----------- |
| 5 packets            |     | transmitted, | 5                         | received, | 0%  | packet | loss, | time 3998ms |
| rtt min/avg/max/mdev |     |              | = 0.034/0.042/0.060/0.011 |           |     |        | ms    |             |
Pingingaserverwithadatapattern:
Ping|67

| switch#              | ping 10.0.0.2                      | data-fill                 |            | 1234123412341234acde123456789012 |           |            |             |
| -------------------- | ---------------------------------- | ------------------------- | ---------- | -------------------------------- | --------- | ---------- | ----------- |
| PATTERN:             | 0x1234123412341234acde123456789012 |                           |            |                                  |           |            |             |
| PING 10.0.0.2        | (10.0.0.2)                         |                           | 100(128)   | bytes                            | of        | data.      |             |
| 108 bytes            | from 10.0.0.2:                     |                           | icmp_seq=1 |                                  | ttl=64    | time=0.207 | ms          |
| 108 bytes            | from 10.0.0.2:                     |                           | icmp_seq=2 |                                  | ttl=64    | time=0.187 | ms          |
| 108 bytes            | from 10.0.0.2:                     |                           | icmp_seq=3 |                                  | ttl=64    | time=0.225 | ms          |
| 108 bytes            | from 10.0.0.2:                     |                           | icmp_seq=4 |                                  | ttl=64    | time=0.197 | ms          |
| 108 bytes            | from 10.0.0.2:                     |                           | icmp_seq=5 |                                  | ttl=64    | time=0.210 | ms          |
| --- 10.0.0.2         | ping                               | statistics                | ---        |                                  |           |            |             |
| 5 packets            | transmitted,                       | 5                         | received,  |                                  | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |                                    | = 0.187/0.205/0.225/0.015 |            |                                  |           | ms         |             |
Pingingaserverwithadatagramsize:
| switch#              | ping 10.0.0.0  | datagram-size             |            |       | 200       |            |             |
| -------------------- | -------------- | ------------------------- | ---------- | ----- | --------- | ---------- | ----------- |
| PING 10.0.0.0        | (10.0.0.0)     |                           | 200(228)   | bytes | of        | data.      |             |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=1 |       | ttl=64    | time=0.202 | ms          |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=2 |       | ttl=64    | time=0.194 | ms          |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=3 |       | ttl=64    | time=0.201 | ms          |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=4 |       | ttl=64    | time=0.200 | ms          |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=5 |       | ttl=64    | time=0.186 | ms          |
| --- 10.0.0.0         | ping           | statistics                | ---        |       |           |            |             |
| 5 packets            | transmitted,   | 5                         | received,  |       | 0% packet | loss,      | time 4000ms |
| rtt min/avg/max/mdev |                | = 0.186/0.196/0.202/0.016 |            |       |           | ms         |             |
Pingingaserverwithanintervalspecified:
| switch#              | ping 9.0.0.2    | interval                  |           | 2     |           |            |             |
| -------------------- | --------------- | ------------------------- | --------- | ----- | --------- | ---------- | ----------- |
| PING 9.0.0.2         | (9.0.0.2)       | 100(128)                  |           | bytes | of data.  |            |             |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=1                |           |       | ttl=64    | time=0.199 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=2                |           |       | ttl=64    | time=0.192 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=3                |           |       | ttl=64    | time=0.208 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=4                |           |       | ttl=64    | time=0.182 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=5                |           |       | ttl=64    | time=0.194 | ms          |
| --- 9.0.0.2          | ping statistics |                           | ---       |       |           |            |             |
| 5 packets            | transmitted,    | 5                         | received, |       | 0% packet | loss,      | time 7999ms |
| rtt min/avg/max/mdev |                 | = 0.182/0.195/0.208/0.008 |           |       |           | ms         |             |
Pingingaserverwithaspecifiednumberofpacketstosend:
| switch#      | ping 9.0.0.2    | repetitions |     | 10    |          |            |     |
| ------------ | --------------- | ----------- | --- | ----- | -------- | ---------- | --- |
| PING 9.0.0.2 | (9.0.0.2)       | 100(128)    |     | bytes | of data. |            |     |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=1  |     |       | ttl=64   | time=0.213 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=2  |     |       | ttl=64   | time=0.204 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=3  |     |       | ttl=64   | time=0.201 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=4  |     |       | ttl=64   | time=0.184 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=5  |     |       | ttl=64   | time=0.202 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=6  |     |       | ttl=64   | time=0.184 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=7  |     |       | ttl=64   | time=0.193 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=8  |     |       | ttl=64   | time=0.196 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=9  |     |       | ttl=64   | time=0.193 | ms  |
| 108 bytes    | from 9.0.0.2:   | icmp_seq=10 |     |       | ttl=64   | time=0.200 | ms  |
| --- 9.0.0.2  | ping statistics |             | --- |       |          |            |     |
68
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| 10 packets           | transmitted, |     |                           | 10 received, | 0%  | packet | loss, | time | 8999ms |
| -------------------- | ------------ | --- | ------------------------- | ------------ | --- | ------ | ----- | ---- | ------ |
| rtt min/avg/max/mdev |              |     | = 0.184/0.197/0.213/0.008 |              |     |        | ms    |      |        |
Pingingaserverwithaspecifiedtimeout:
| switch#              | ping         | 9.0.0.2         | timeout                   | 3          |           |            |       |      |        |
| -------------------- | ------------ | --------------- | ------------------------- | ---------- | --------- | ---------- | ----- | ---- | ------ |
| PING 9.0.0.2         |              | (9.0.0.2)       | 100(128)                  |            | bytes of  | data.      |       |      |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=1 | ttl=64    | time=0.175 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=2 | ttl=64    | time=0.192 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=3 | ttl=64    | time=0.190 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=4 | ttl=64    | time=0.181 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=5 | ttl=64    | time=0.197 |       | ms   |        |
| --- 9.0.0.2          |              | ping statistics |                           | ---        |           |            |       |      |        |
| 5 packets            | transmitted, |                 | 5                         | received,  | 0% packet |            | loss, | time | 4000ms |
| rtt min/avg/max/mdev |              |                 | = 0.175/0.187/0.197/0.007 |            |           |            | ms    |      |        |
PingingaserverwiththespecifiedIPTypeofService:
| switch#              | ping         | 9.0.0.2         | tos                       | 2          |           |            |       |      |        |
| -------------------- | ------------ | --------------- | ------------------------- | ---------- | --------- | ---------- | ----- | ---- | ------ |
| PING 9.0.0.2         |              | (9.0.0.2)       | 100(128)                  |            | bytes of  | data.      |       |      |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=1 | ttl=64    | time=0.033 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=2 | ttl=64    | time=0.034 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=3 | ttl=64    | time=0.031 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=4 | ttl=64    | time=0.034 |       | ms   |        |
| 108 bytes            | from         | 9.0.0.2:        |                           | icmp_seq=5 | ttl=64    | time=0.031 |       | ms   |        |
| --- 9.0.0.2          |              | ping statistics |                           | ---        |           |            |       |      |        |
| 5 packets            | transmitted, |                 | 5                         | received,  | 0% packet |            | loss, | time | 3999ms |
| rtt min/avg/max/mdev |              |                 | = 0.031/0.032/0.034/0.006 |            |           |            | ms    |      |        |
PingingalocalhostwiththespecifiedVRF.
| switch#        | ping | localhost   | vrf | red      |       |     |       |     |     |
| -------------- | ---- | ----------- | --- | -------- | ----- | --- | ----- | --- | --- |
| PING localhost |      | (127.0.0.1) |     | 100(128) | bytes | of  | data. |     |     |
108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.048 ms
108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.052 ms
108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.044 ms
108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.036 ms
108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.055 ms
| --- localhost        |              | ping | statistics                | ---       |           |     |       |      |        |
| -------------------- | ------------ | ---- | ------------------------- | --------- | --------- | --- | ----- | ---- | ------ |
| 5 packets            | transmitted, |      | 5                         | received, | 0% packet |     | loss, | time | 4005ms |
| rtt min/avg/max/mdev |              |      | = 0.036/0.047/0.055/0.006 |           |           |     | ms    |      |        |
PingingthelocalhostwiththedefaultVRF:
| switch#        | ping | localhost   | vrf | mgmt     |       |     |       |     |     |
| -------------- | ---- | ----------- | --- | -------- | ----- | --- | ----- | --- | --- |
| PING localhost |      | (127.0.0.1) |     | 100(128) | bytes | of  | data. |     |     |
108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.085 ms
108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.057 ms
108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.047 ms
108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.038 ms
108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.059 ms
| --- localhost |     | ping | statistics | --- |     |     |     |     |     |
| ------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
Ping|69

| 5 packets            | transmitted, | 5                         | received, | 0% packet | loss, | time 3999ms |
| -------------------- | ------------ | ------------------------- | --------- | --------- | ----- | ----------- |
| rtt min/avg/max/mdev |              | = 0.038/0.057/0.085/0.016 |           |           | ms    |             |
Pingingaserverwiththeintermediateroutertimestamp:
| switch#      | ping 9.0.0.2      | ip-option  | include-timestamp |                |            |     |
| ------------ | ----------------- | ---------- | ----------------- | -------------- | ---------- | --- |
| PING 9.0.0.2 | (9.0.0.2)         | 100(168)   |                   | bytes of data. |            |     |
| 108 bytes    | from 9.0.0.2:     | icmp_seq=1 |                   | ttl=64         | time=0.031 | ms  |
| TS:          | 59909005 absolute |            |                   |                |            |     |
0
0
0
| 108 bytes | from 9.0.0.2:     | icmp_seq=2 |     | ttl=64 | time=0.034 | ms  |
| --------- | ----------------- | ---------- | --- | ------ | ---------- | --- |
| TS:       | 59910005 absolute |            |     |        |            |     |
0
0
0
| 108 bytes | from 9.0.0.2:     | icmp_seq=3 |     | ttl=64 | time=0.038 | ms  |
| --------- | ----------------- | ---------- | --- | ------ | ---------- | --- |
| TS:       | 59911005 absolute |            |     |        |            |     |
0
0
0
| 108 bytes | from 9.0.0.2:     | icmp_seq=4 |     | ttl=64 | time=0.035 | ms  |
| --------- | ----------------- | ---------- | --- | ------ | ---------- | --- |
| TS:       | 59912005 absolute |            |     |        |            |     |
0
0
0
| 108 bytes | from 9.0.0.2:     | icmp_seq=5 |     | ttl=64 | time=0.037 | ms  |
| --------- | ----------------- | ---------- | --- | ------ | ---------- | --- |
| TS:       | 59913005 absolute |            |     |        |            |     |
0
0
0
| --- 9.0.0.2          | ping statistics |                           | ---       |           |       |             |
| -------------------- | --------------- | ------------------------- | --------- | --------- | ----- | ----------- |
| 5 packets            | transmitted,    | 5                         | received, | 0% packet | loss, | time 3999ms |
| rtt min/avg/max/mdev |                 | = 0.031/0.035/0.038/0.002 |           |           | ms    |             |
Pingingaserverwiththeintermediateroutertimestampandaddress:
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
| 108 bytes | from 9.0.0.2: | icmp_seq=3 |     | ttl=64 | time=0.037 | ms  |
| --------- | ------------- | ---------- | --- | ------ | ---------- | --- |
70
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| TS:                  | 9.0.0.2 | 60009355        |                           | absolute  |        |        |            |      |        |
| -------------------- | ------- | --------------- | ------------------------- | --------- | ------ | ------ | ---------- | ---- | ------ |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
| 108 bytes            |         | from 9.0.0.2:   | icmp_seq=4                |           | ttl=64 |        | time=0.038 | ms   |        |
| TS:                  | 9.0.0.2 | 60010355        |                           | absolute  |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
| 108 bytes            |         | from 9.0.0.2:   | icmp_seq=5                |           | ttl=64 |        | time=0.039 | ms   |        |
| TS:                  | 9.0.0.2 | 60011355        |                           | absolute  |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
|                      | 9.0.0.2 | 0               |                           |           |        |        |            |      |        |
| --- 9.0.0.2          |         | ping statistics |                           | ---       |        |        |            |      |        |
| 5 packets            |         | transmitted,    | 5                         | received, | 0%     | packet | loss,      | time | 3999ms |
| rtt min/avg/max/mdev |         |                 | = 0.030/0.036/0.039/0.005 |           |        |        | ms         |      |        |
Pingingaserverwiththeintermediaterouteraddress:
| switch#   | ping    | 9.0.0.2       | ip-option  | record-route |        |          |            |     |     |
| --------- | ------- | ------------- | ---------- | ------------ | ------ | -------- | ---------- | --- | --- |
| PING      | 9.0.0.2 | (9.0.0.2)     | 100(168)   |              | bytes  | of data. |            |     |     |
| 108 bytes |         | from 9.0.0.2: | icmp_seq=1 |              | ttl=64 |          | time=0.034 | ms  |     |
| RR:       | 9.0.0.2 |               |            |              |        |          |            |     |     |
9.0.0.2
9.0.0.2
9.0.0.2
108 bytes from 9.0.0.2: icmp_seq=2 ttl=64 time=0.038 ms (same route)
108 bytes from 9.0.0.2: icmp_seq=3 ttl=64 time=0.036 ms (same route)
108 bytes from 9.0.0.2: icmp_seq=4 ttl=64 time=0.037 ms (same route)
108 bytes from 9.0.0.2: icmp_seq=5 ttl=64 time=0.035 ms (same route)
| --- 9.0.0.2          |     | ping statistics |                           | ---       |     |        |       |      |        |
| -------------------- | --- | --------------- | ------------------------- | --------- | --- | ------ | ----- | ---- | ------ |
| 5 packets            |     | transmitted,    | 5                         | received, | 0%  | packet | loss, | time | 3999ms |
| rtt min/avg/max/mdev |     |                 | = 0.034/0.036/0.038/0.001 |           |     |        | ms    |      |        |
Pingingaserverwithdo-not-fragment:
switch#
|                      | ping        | 192.168.1.8       |                           | datagram-size |     | 2000   | do-not-fragment |       |        |
| -------------------- | ----------- | ----------------- | ------------------------- | ------------- | --- | ------ | --------------- | ----- | ------ |
| PING                 | 192.168.1.8 | (192.168.1.8)     |                           | 2000(2028)    |     |        | bytes of        | data. |        |
| 2008                 | bytes       | from 192.168.1.8: |                           | icmp_seq=1    |     | ttl=64 | time=0.721      |       | ms     |
| 2008                 | bytes       | from 192.168.1.8: |                           | icmp_seq=2    |     | ttl=64 | time=0.792      |       | ms     |
| 2008                 | bytes       | from 192.168.1.8: |                           | icmp_seq=3    |     | ttl=64 | time=0.857      |       | ms     |
| 2008                 | bytes       | from 192.168.1.8: |                           | icmp_seq=4    |     | ttl=64 | time=0.833      |       | ms     |
| 2008                 | bytes       | from 192.168.1.8: |                           | icmp_seq=5    |     | ttl=64 | time=0.836      |       | ms     |
| --- 192.168.1.8      |             | ping              | statistics                |               | --- |        |                 |       |        |
| 5 packets            |             | transmitted,      | 5                         | received,     | 0%  | packet | loss,           | time  | 4056ms |
| rtt min/avg/max/mdev |             |                   | = 0.721/0.807/0.857/0.048 |               |     |        | ms              |       |        |
CommandHistory
Ping|71

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
ping6
ping6 {<IPv6-ADDR> | <HOSTNAME>} [data-fill <PATTERN> | datagram-size <SIZE> |
interval <TIME> | repetitions <NUMBER> | timeout <TIME> | vrrp <VRID> |
| vrf <VRF-NAME> | | source <IPv6-ADDR> | | <IFNAME>] |
| -------------- | -------------------- | ----------- |
Description
PingsthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.TheVRRPoptionis
providedtoself-pingtheconfiguredlink-localaddressontheVRRPgroup.
| Parameter |     | Description                                    |
| --------- | --- | ---------------------------------------------- |
| IPv6-ADDR |     | SelectstheIPv6addresstoping.                   |
| HOSTNAME  |     | Selectsthehostnametoping.Range:1-256characters |
data-fill <PATTERN> Specifiesthedatapatterninhexadecimaldigitstosend.A
maximumof16"pad"bytescanbespecifiedtofillouttheICMP
packet.Default:AB
datagram-size <SIZE> Specifiesthepingdatagramsize.Range:0-65399,default:100.
interval <TIME> Specifiestheintervalbetweensuccessivepingrequestsin
seconds.Range:1-60seconds,default:1second.
| repetitions | <NUMBER> |     |
| ----------- | -------- | --- |
Specifiesthenumberofpacketstosend.Range:1-10000packets,
default:Fivepackets.
timeout <TIME> Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
| vrrp <VRID> |     | SpecifiestheVRRPgroupID. |
| ----------- | --- | ------------------------ |
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.Whenthis
optionisnotprovided,thedefaultVRFisused.
source <IPv6-ADDR> | <IFNAME> SpecifiesthesourceIPv6addressorinterfacetouse.
Examples
PinginganIPv6address:
72
| AOS-CX10.08DiagnosticsandSupportabilityGuide| | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | ----------------------- | --- |

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
| switch#               | ping6 2020::2   | data-fill |                         | ab    |           |            |             |
| --------------------- | --------------- | --------- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PATTERN:              | 0xab            |           |                         |       |           |            |             |
| PING 2020::2(2020::2) |                 | 100       | data                    | bytes |           |            |             |
| 108 bytes             | from 2020::2:   |           | icmp_seq=1              |       | ttl=64    | time=0.038 | ms          |
| 108 bytes             | from 2020::2:   |           | icmp_seq=2              |       | ttl=64    | time=0.074 | ms          |
| 108 bytes             | from 2020::2:   |           | icmp_seq=3              |       | ttl=64    | time=0.076 | ms          |
| 108 bytes             | from 2020::2:   |           | icmp_seq=4              |       | ttl=64    | time=0.075 | ms          |
| 108 bytes             | from 2020::2:   |           | icmp_seq=5              |       | ttl=64    | time=0.077 | ms          |
| --- 2020::2           | ping statistics |           | ---                     |       |           |            |             |
| 5 packets             | transmitted,    |           | 5 received,             |       | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev  |                 | =         | 0.038/0.068/0.077/0.015 |       |           | ms         |             |
Pingingaserverwithadatagramsize:
| switch#               | ping6 2020::2   | datagram-size |                         |       | 200       |            |             |
| --------------------- | --------------- | ------------- | ----------------------- | ----- | --------- | ---------- | ----------- |
| PING 2020::2(2020::2) |                 | 200           | data                    | bytes |           |            |             |
| 208 bytes             | from 2020::2:   |               | icmp_seq=1              |       | ttl=64    | time=0.037 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=2              |       | ttl=64    | time=0.076 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=3              |       | ttl=64    | time=0.076 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=4              |       | ttl=64    | time=0.077 | ms          |
| 208 bytes             | from 2020::2:   |               | icmp_seq=5              |       | ttl=64    | time=0.066 | ms          |
| --- 2020::2           | ping statistics |               | ---                     |       |           |            |             |
| 5 packets             | transmitted,    |               | 5 received,             |       | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev  |                 | =             | 0.037/0.066/0.077/0.016 |       |           | ms         |             |
Pingingaserverwithanintervalspecified:
Ping|73

| switch#               | ping6 2020::2   | interval |                         | 5     |           |            |              |
| --------------------- | --------------- | -------- | ----------------------- | ----- | --------- | ---------- | ------------ |
| PING 2020::2(2020::2) |                 | 100      | data                    | bytes |           |            |              |
| 108 bytes             | from 2020::2:   |          | icmp_seq=1              |       | ttl=64    | time=0.043 | ms           |
| 108 bytes             | from 2020::2:   |          | icmp_seq=2              |       | ttl=64    | time=0.075 | ms           |
| 108 bytes             | from 2020::2:   |          | icmp_seq=3              |       | ttl=64    | time=0.074 | ms           |
| 108 bytes             | from 2020::2:   |          | icmp_seq=4              |       | ttl=64    | time=0.075 | ms           |
| 108 bytes             | from 2020::2:   |          | icmp_seq=5              |       | ttl=64    | time=0.075 | ms           |
| --- 2020::2           | ping statistics |          |                         | ---   |           |            |              |
| 5 packets             | transmitted,    |          | 5 received,             |       | 0% packet | loss,      | time 19999ms |
| rtt min/avg/max/mdev  |                 | =        | 0.043/0.068/0.075/0.014 |       |           | ms         |              |
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
PingingthelocalhostwiththedefaultVRF:
| switch#                   | ping6 localhost |            | vrf                     | mgmt |           |            |             |
| ------------------------- | --------------- | ---------- | ----------------------- | ---- | --------- | ---------- | ----------- |
| PING localhost(localhost) |                 |            | 100                     | data | bytes     |            |             |
| 108 bytes                 | from localhost: |            | icmp_seq=1              |      | ttl=64    | time=0.032 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=2              |      | ttl=64    | time=0.022 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=3              |      | ttl=64    | time=0.040 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=4              |      | ttl=64    | time=0.022 | ms          |
| 108 bytes                 | from localhost: |            | icmp_seq=5              |      | ttl=64    | time=0.046 | ms          |
| --- localhost             | ping            | statistics |                         | ---  |           |            |             |
| 5 packets                 | transmitted,    |            | 5 received,             |      | 0% packet | loss,      | time 3998ms |
| rtt min/avg/max/mdev      |                 | =          | 0.022/0.032/0.046/0.010 |      |           | ms         |             |
CommandHistory
74
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
Troubleshooting
| Operation | not permitted |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- |
Symptom
Theswitchdisplaysanoperation not permittedmessagewhenauserattemptstosendapingrequest.
Example:
| switch#         | ping 100.1.2.10 |             |                |            |        |
| --------------- | --------------- | ----------- | -------------- | ---------- | ------ |
| PING 100.1.2.10 | (100.1.2.10)    |             | 100(128) bytes | of data    |        |
| ping: sendmsg:  | Operation       | not         | permitted      |            |        |
| ping: sendmsg:  | Operation       | not         | permitted      |            |        |
| ping: sendmsg:  | Operation       | not         | permitted      |            |        |
| ping: sendmsg:  | Operation       | not         | permitted      |            |        |
| ping: sendmsg:  | Operation       | not         | permitted      |            |        |
| --- 100.1.2.10  | ping            | statistics  | ---            |            |        |
| 5 packets       | transmitted,    | 0 received, | 100% packet    | loss, time | 4000ms |
Cause
WhenanACLisappliedtotheControlPlane,sendingapingrequestmaybedenied.Ifthepingpacket
matchesadropentryintheACL,applyingaControlPlanemayblocktrafficsentfromtheswitchCLIping
command.
Whenthissituationoccurs,thefollowingerrormessageisdisplayed:ping: sendmsg: Operation not
permitted.ThemessageindicatesthattheICMPechorequestpackethasnotbeensentandisblockedby
theControlPlaneACL.
Whenthismessageisnotdisplayed,thepingrequestpackethasbeensentcorrectly.Apingfailureinthis
caserepresentsafailuretoreceivetheICMPechoreplypacket.
Action
1. ModifytheACLtoallowthepingtraffic.
2. UnapplytheACLfromegress(8400/8320/8325switches)orControlPlane.
3. PingadestinationwhichisnotmatchedbytheACL.Forexample,iftheACLisblockingtrafficbased
ondestinationIP.DependingontheACLcontent,thismightnotalwaysbepossiblelikewhentheACL
blocksallICMPpackets.
Ping|75

Network is unreachable

Symptom

User receives a "network is unreachable" message on sending a ping request.

Cause

The ping packet did not get sent, because the switch cannot find an interface with a route that leads to the
destination for one of the following reasons:

n A configuration error, such as an interface having an incorrect IP address or subnet defined.

n DHCP having failed to assign an address at all.

n The user meant to ping out the management vrf, but forgot to add vrf mgmt to the ping command.

Action

Adjust the switch configuration to ensure that a route to the destination network exists.

Destination host unreachable

Symptom

User receives a Destination host unreachable message on sending a ping request.

Cause

This issue typically indicates that the host is down or otherwise not returning ICMP echo requests. It is also
possible that an intermediate network hop is dropping the packets.

Action

Investigate whether an intermediate hop is not returning pings by using the traceroute command. Check
the intermediate hop, and then the endpoint. If the destination is another Aruba switch, it is possible that
Ingress ACLs on that switch are blocking ping packets. In such cases, the configuration option on the
destination switch should be examined.

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

76

Chapter 11
Remote syslog
| Remote | syslog |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- |
Remotesyslogenablestheforwardingofsyslogmessagestotheremotesyslogserver.Thefeaturesupports
amaximumoffourremotesyslogservers.Onlyoneconfigurationperremotesyslogserverisallowed.The
remotesyslogserversupportsTCPandUDPtransportprotocolsandTLStoestablishaconnection.In
additiontoforwardinglogstotheremoteserver,theycanalsobepreservedinlocalstorage.
Whentheclientcertificateassociatedwiththesyslogclientisupdated,thesyslogclientisrestartedanda
newTLSconnectionisestablishedusingtheupdatedclientcertificate.
| Remote | syslog | commands |     |     |     |
| ------ | ------ | -------- | --- | --- | --- |
logging
logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} [ udp [<PORT-NUM>] | tcp [<PORT-
NUM>] ] [severity <LEVEL>] [vrf <VRF-NAME>] [include-auditable-events]
[filter <FILTER-NAME>] [ rate-limit-burst <BURST> [rate-limit-interval <INTERVAL>] ]
logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} [tls [<PORT-NUM>]] [auth-mode
{certificate|subject-name}] [legacy-tls-renegotiation] [severity <LEVEL>] [vrf <VRF-NAME>]
[include-auditable-events] [filter <FILTER-NAME>] [ rate-limit-burst <BURST> [rate-limit-
| interval   | <INTERVAL>]] |               |         |             |     |
| ---------- | ------------ | ------------- | ------- | ----------- | --- |
| no logging | {<IPV4-ADDR> | | <IPV6-ADDR> | | <FQDN | | HOSTNAME> | }   |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
| Parameter    |               |               | Description |     |     |
| ------------ | ------------- | ------------- | ----------- | --- | --- |
| {<IPV4-ADDR> | | <IPV6-ADDR> | | <HOSTNAME>} |             |     |     |
SelectstheIPv4address,IPv6address,orhostnameofthe
remotesyslogserver.Required.
[udp [<PORT-NUM>] | tcp [<PORT-NUM> | SpecifiestheUDPport,TCPport,orTLSportoftheremote
tls [<PORT-NUM>]] syslogservertoreceivetheforwardedsyslogmessages.
| udp [<PORT-NUM>] |     |     | Range:1to65535.Default:514  |     |     |
| ---------------- | --- | --- | --------------------------- | --- | --- |
| tcp [<PORT-NUM>] |     |     | Range:1to65535.Default:1470 |     |     |
| tls [<PORT-NUM>] |     |     | Range:1to65535.Default:6514 |     |     |
include-auditable-events Specifiesthatauditablemessagesarealsologgedtothe
remotesyslogserver.
| severity | <LEVEL> |     | Specifiestheseverityofthesyslogmessages: |                                                 |     |
| -------- | ------- | --- | ---------------------------------------- | ----------------------------------------------- | --- |
|          |         |     |                                          | n alert:Forwardssyslogmessageswiththeseverityof |     |
alert (6)andemergency (7).
77
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- |

Parameter

Description

n crit: Forwards syslog messages with the severity of

critical (5) and above.

n debug: Forwards syslog messages with the severity of

debug (0) and above.

n emerg: Forwards syslog messages with the severity of

emergency (7) only.

n err: Forwards syslog messages with the severity of err

(4) and above

n info: Forwards syslog messages with the severity of

info (1) and above. Default.

n notice: Forwards syslog messages with the severity of

notice (2) and above.

n warning: Forwards syslog messages with the severity of

warning (3) and above.

Specifies the TLS authentication mode used to validate the
certificate.
n certificate: Validates the peer using trust anchor

certificate based authentication. Default.

n subject-name: Validates the peer using trust anchor

certificates as well as subject-name based

authentication.

Enables the TLS connection with a remote syslog server
supporting legacy renegotiation.

Specifies the name of the filter to be applied on the syslog
messages.

Specifies the rate limit for the messages sent to the remote
syslog server.

Specifies the rate limit interval in seconds. Default: 30
Seconds

Specifies the VRF used to connect to the syslog server.
Optional. Default: default

auth-mode

legacy-tls-renegotiation

filter <FILTER-NAME>

rate-limit-burst <BURST>

rate-limit-interval <INTERVAL>

vrf <VRF-NAME>

Examples

Enabling the syslog forwarding to remote syslog server 10.0.10.2:

switch(config)# logging 10.0.10.2

Enabling the syslog forwarding of messages with a severity of err (4) and above to TCP port 4242 on
remote syslog server 10.0.10.9 with VRF lab_vrf:

switch(config)# logging 10.0.10.9 tcp 4242 severity err vrf lab_vrf

Disabling syslog forwarding to a remote syslog server:

Remote syslog | 78

| switch(config)# | no logging |     |     |     |
| --------------- | ---------- | --- | --- | --- |
EnablingsyslogforwardingoverTLStoaremotesyslogserverusingsubject-nameauthenticationmode:
| switch(config)#logging |     | example.com | tls auth-mode | subject-name |
| ---------------------- | --- | ----------- | ------------- | ------------ |
Applyinglogfilteringforsyslogserverforwarding:
switch(config)# logging 10.0.10.6 severity info filter filter_lldp_logs vrf mgmt
ApplyinglogfilteringandenablingtheratelimitforsyslogserverforwardingoverTCPport:
switch(config)# logging 10.0.10.2 tcp 3440 severity err vrf mgmt include-auditable-
events filter filter_lldp_logs rate-limit-burst 3 rate-limit-interval 35
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logging        | filter        |     |     |     |
| -------------- | ------------- | --- | --- | --- |
| logging filter | <FILTER-NAME> |     |     |     |
| [{enable       | | disable}]   |     |     |     |
[<SEQUENCE-ID>] {permit | deny} [event-id <EVENT-ID-RANGE>] [includes <REGEX>] [severity
| <COMPARISON-OPERATOR> |     | <LEVEL>] |     |     |
| --------------------- | --- | -------- | --- | --- |
no <SEQUENCE-ID>
| resequence | <OLD-SEQUENCE-ID>    | <NEW-SEQUENCE-ID> |     |     |
| ---------- | -------------------- | ----------------- | --- | --- |
| no logging | filter <FILTER-NAME> |                   |     |     |
Description
Createsafiltertorestrictwhateventordebuglogsarelogged.Afiltercanbeusedtoeitherpermitordeny:
n Theeventlogsfrombeinggeneratedontheswitch,or
n Theeventordebuglogsgeneratedontheswitchfrombeingforwardedtoasyslogserver.
Afilterisidentifiedbyafilternameandcanhaveupto20rulesorentries,eachwithadifferentsequence
number,matchingcriteria,andcorrespondingaction(denyorpermit).Whenafilterisappliedonalog,the
79
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- |

log is matched against the criteria mentioned in the rules or entries in ascending numerical order of their
sequence numbers until a matching entry is found. Once a matching entry is found, its corresponding action
is applied on the log. If no matching rule is found, the default action (permit) is applied.

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

Usage

Filtering event logs on the switch: To permit or deny event logs from being generated on the switch. In
this case, the matching event logs are filtered at generation. The denied event logs are neither logged to the
switch events nor forwarded to any remote syslog servers. Multiple filters can be configured, but only one
filter can be applied to filter the events on the switch. Such a filter can be chosen by adding the enable
command under its configuration. Configuring the enable command under a new filter automatically
removes it from the filter where it was previously used.

For example:

logging filter low_severity_logs

Remote syslog | 80

enable

10 deny severity lt info

This configuration denies the event logs which have a severity less than info.

If a filter contains enable command, it is not recommended to configure this filter in the logging command used
for remote syslog server configuration. This is because, any event logs denied by the filter are already not

available for forwarding to a remote server.

A filter with enable command will not affect debug logs. Consider the configuration in the following example
of a filter with enable command and two rules applied 10 permit severity ge info and 20 deny. This
implies permit only those event logs which have severity greater than or equal to info.
Example:

logging filter low_severity_logs
enable
10 permit severity ge info
20 deny

Filtering event or debug logs when forwarding to a remote syslog server: The filter name must be
configured in the logging command that is used to configure remote syslog server. The logs will be
generated on the switch and the filter only decides whether to deny or permit the syslog forwarding for the
matching log. For example: logging 10.0.10.6 filter filter_lldp_logs

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

To deny logs having event ID 1301 and a range of event IDs from 1305 to 1309:

switch(config-logging-filter)# 20 deny event-id 1301,1305-1309

To permit logs having event ID 1300:

switch(config-logging-filter)# 30 permit event-id 1300

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

81

Topermitlogswithseveritygreaterthanorequaltoerr:
| switch(config-logging-filter)# |     |     | 30 permit | severity | ge err |     |
| ------------------------------ | --- | --- | --------- | -------- | ------ | --- |
Todenylogswithseveritygreaterthaninfo:
| switch(config-logging-filter)# |     |     | 30 deny | severity gt | info |     |
| ------------------------------ | --- | --- | ------- | ----------- | ---- | --- |
TodenylogswitheventID1024andamessagematchingtheregularexpressionLLDP:
switch(config-logging-filter)#
|     |     |     | 40 deny | event-id 1024 | includes | LLDP |
| --- | --- | --- | ------- | ------------- | -------- | ---- |
Denyingalllogs:
| switch(config-logging-filter)# |     |     | 40 deny |     |     |     |
| ------------------------------ | --- | --- | ------- | --- | --- | --- |
ChangingthesequenceIDofanexistingrule:
| switch(config-logging-filter)# |     |     | resequence | 20 70 |     |     |
| ------------------------------ | --- | --- | ---------- | ----- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms configandconfig- Administratorsorlocalusergroupmemberswithexecutionrights
|         | logging-filter |     | forthiscommand. |     |     |     |
| ------- | -------------- | --- | --------------- | --- | --- | --- |
| logging | facility       |     |                 |     |     |     |
logging facility {local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7}
| no logging | facility |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
Description
Setstheloggingfacilitytobeusedforremotesyslogmessages.Default:local7
Thenoformofthiscommanddisablestheloggingfacilitytobeusedforremotesyslogmessages.
| Parameter |                   |     | Description |     |     |     |
| --------- | ----------------- | --- | ----------- | --- | --- | --- |
| {local0   | | local1 | local2 | |   |             |     |     |     |
Selectstheloggingfacilitytobeusedforremotesyslogmessages.
| local3 | | local4 | local5 | |   |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- | --- |
Required.
| local6 | | local7} |     | Specifiestheseverityofthesyslogmessages: |     |     |     |
| ------ | --------- | --- | ---------------------------------------- | --- | --- | --- |
Remotesyslog|82

| Parameter |     | Description |
| --------- | --- | ----------- |
local0
n
n local1
n local2
n local3
n local4
local5
n
n local6
local7
n
Examples
Setsthelocal5loggingfacilitytobeusedforremotesyslogmessages:
| switch(config)# | logging facility | local5 |
| --------------- | ---------------- | ------ |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logging persistent-storage |     |     |
| -------------------------- | --- | --- |
logging persistent-storage [severity {alert|crit|debug|emerg|err|info|notice|warning}]
| no logging persistent-storage |     |     |
| ----------------------------- | --- | --- |
Description
Enablesordisablesstorageoflogsinstorage.Onlylogsofthespecifiedseverityandabovewillbepreserved
inthestorage.
Thenoformofthiscommanddisablesstorageoflogsinstorage.
| Parameter        |     | Description                              |
| ---------------- | --- | ---------------------------------------- |
| severity <LEVEL> |     | Specifiestheseverityofthesyslogmessages: |
n alert:Preservessyslogmessageswiththeseverityofalert
(6)andemergency (7)
crit:Preservessyslogmessageswiththeseverityof
n
critical (5)andabove.Default.
debug:Preservessyslogmessageswiththeseverityofdebug
n
(0)andabove.
n emerg:Preservessyslogmessageswiththeseverityof
83
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |
| --------------------------------------------- | --- | ----------------------- |

| Parameter |     |     | Description |          |
| --------- | --- | --- | ----------- | -------- |
|           |     |     | emergency   | (7)only. |
err:Preservessyslogmessageswiththeseverityoferr (4)
n
andabove.
n info:Preservessyslogmessageswiththeseverityofinfo
(1)andabove.
n notice:Preservessyslogmessageswiththeseverityof
|     |     |     | notice | (2)andabove. |
| --- | --- | --- | ------ | ------------ |
warning:Preservessyslogmessageswiththeseverityof
n
|     |     |     | warning | (3)andabove. |
| --- | --- | --- | ------- | ------------ |
Usage
Theselogscanbecopiedoutbyusingthecopy support-files allorcopy support-files previous-
boot.
Examples
Enablingstorageoflogsinstoragewithseverityinfo:
| switch(config)#logging |     | persistent-storage |     | severity info |
| ---------------------- | --- | ------------------ | --- | ------------- |
Logs will be written to storage and made available across reboot.
| Do you want | to continue | (y/n)? |     |     |
| ----------- | ----------- | ------ | --- | --- |
Disablingstorageoflogsinstorage:
| switch(config)# | no logging | persistent-storage |     |     |
| --------------- | ---------- | ------------------ | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Remotesyslog|84

Chapter 12

Runtime Diagnostics

Runtime Diagnostics

Run Time diagnostics framework is intended to monitor and validate the health of different hardware
components present in the system. It uses a set of safe hardware diagnostics test cases to validate the
health of different hardware components. These diagnostics test cases are run periodically at every
predetermined interval. Additionally, these hardware diagnostics test cases can be run on demand.

Runtime diagnostic commands

diagnostic monitor
diagnostic monitor {fan-tray | line-module | management-module} [<SLOT-ID>]
no diagnostic monitor {fan-tray | line-module | management-module} [<SLOT-ID>]

For 6400 switches only:
diagnostic monitor {fabric <SLOT-ID>}
no diagnostic monitor {fabric <SLOT-ID>}

Description

Enables runtime diagnostics for all modules or for a specified module. This feature is enabled by default for
all modules.

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
command applies to all modules. This command impacts the diagnostics that run periodically. It does not
affect on-demand diagnostics.

Example

Enabling runtime diagnostics for a specified module:

switch(config)# diagnostic monitor management-module 1/1

Command History

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

85

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
diag on-demand
diag on-demand {fan-tray | line-module | management-module} [<SLOT-ID>]
For6400switchesonly:
| diag on-demand | {fabric | <SLOT-ID>} |     |
| -------------- | ------- | ---------- | --- |
Description
Runsthediagnostictestsforallmodulesorforaspecifiedmodule.
Parameter Description
[fan-tray | line-module | management-module] Selectstheoptionsforenablingordisablingruntime
diagnosticsforaspecificmodule.
fan-tray Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module
Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID> Specifiesthemember/slotformanagementmodules
(1/1or1/2),linemodules(1/3-1/7,1/8-1/12),fantrays
(1/1-1/3),andfabricmodules(1/1-1/2)ona6400
switch.
Specifiesthemember/slotformanagementmodules
(1/1),linemodules(1/1),andfantrays(1/1-1/2)ona
6300switch.
Usage
Whennoparametersareusedinthecommand(diag on-demand),thecommandappliestoallmodules.
Examples
Runningdiagnostictestsforallmodulesona6300switch:
| switch#  | diag on-demand |                |          |
| -------- | -------------- | -------------- | -------- |
| Fetching | Test results.  | Please         | wait ... |
| Module   |                | ID Diagnostics | Success  |
Performed
RuntimeDiagnostics|86

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
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
87
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
show diagnostic
show diagnostic {fan-tray | line-module | management-module} [<SLOT-ID>] {brief | detail}
[vsx-peer]
Description
Displaysthediagnostictestresultsforallmodulesorforaspecifiedmodule.
Parameter Description
[fan-tray | line-module | management-module] Selectstheoptionsforenablingordisablingruntime
diagnosticsforaspecificmodule.
fan-tray Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID> Specifiesthemember/slotformanagementmodules
(1/1),linemodules(1/1),andfantrays(1/1-1/2)onthe
6300switch.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Ifthe
switchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnot
displayed.Thisparameterisavailableonswitches
thatsupportVSX.
Usage
Whennoparametersareusedinthecommand(show diagnostic),thecommandappliestoallmodules.
Example
Showingdiagnostictestresultsinbriefformatforallmodulesona6300switch:
| switch# | show diagnostic | brief          |         |
| ------- | --------------- | -------------- | ------- |
| Module  |                 | ID Diagnostics | Success |
Performed
| -------------------- |     | ----- ----------- | ------- |
| -------------------- | --- | ----------------- | ------- |
| ManagementModule     |     | 1/1               | 13 100% |
| LineModule           |     | 1/1               | 13 100% |
| FanTray              |     | 1/1               | 1 100%  |
| FanTray              |     | 1/2               | 1 100%  |
Showingdiagnostictestresultsinbriefformatforaspecifiedmoduleona6300switch:
RuntimeDiagnostics|88

| switch# | show diagnostic | line-module    |     | brief   |     |     |     |
| ------- | --------------- | -------------- | --- | ------- | --- | --- | --- |
| Module  |                 | ID Diagnostics |     | Success |     |     |     |
Performed
| -------------------- |     | ----- ----------- |     | ------- |     |     |     |
| -------------------- | --- | ----------------- | --- | ------- | --- | --- | --- |
| LineModule           |     | 1/1               | 13  | 100%    |     |     |     |
Showingdiagnostictestresultsindetailformatforallmodulesona6300switch:
| switch#  | show diagnostic  | detail |     |     |     |     |     |
| -------- | ---------------- | ------ | --- | --- | --- | --- | --- |
| Module : | ManagementModule | 1/1    |     |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |           |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --------- | --- |
|          |           |           |           | Failure Count | Count | Iteration |     |
-------------- ------ ---------- ------------ ------------- ------------- ---------
| -------------------- |            | ------------------- |          |     |     |     |     |
| -------------------- | ---------- | ------------------- | -------- | --- | --- | --- | --- |
| ddr_cecount          | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 109 |
| 2019-07-31           | 16:43:38   | 2019-07-31          | 07:44:55 |     |     |     |     |
| emmc                 | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| fan_ctrlr            | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| fepld                | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 109 |
| 2019-07-31           | 16:43:38   | 2019-07-31          | 07:44:54 |     |     |     |     |
| fru_eeprom           | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:54 |     |     |     |     |
| fru_eeprom_ul        | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:54 |     |     |     |     |
| mm_lcb               | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 109 |
| 2019-07-31           | 16:43:37   | 2019-07-31          | 07:44:54 |     |     |     |     |
| pmc                  | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 109 |
| 2019-07-31           | 16:43:37   | 2019-07-31          | 07:44:54 |     |     |     |     |
| rdimm_spd            | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| rdimm_tmp            | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| rtc                  | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| tmp1                 | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| tmp2                 | Pass       | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04   | 2019-07-31          | 07:44:55 |     |     |     |     |
| Module :             | LineModule | 1/1                 |          |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |           |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --------- | --- |
|          |           |           |           | Failure Count | Count | Iteration |     |
-------------- ------ ---------- ------------ ------------- ------------- ---------
| -------------------- |          | ------------------- |          |     |     |     |     |
| -------------------- | -------- | ------------------- | -------- | --- | --- | --- | --- |
| lc_asic              | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 108 |
| 2019-07-31           | 16:43:37 | 2019-07-31          | 07:46:03 |     |     |     |     |
| poe_ctrlr_1_q1       | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:03 |     |     |     |     |
| poe_ctrlr_1_q2       | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:04 |     |     |     |     |
| poe_ctrlr_1_q3       | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:16 | 2019-07-31          | 07:46:04 |     |     |     |     |
89
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| poe_ctrlr_2_q1 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| -------------- | ----------- | ---------- | -------- | --- | --- | --- | --- |
| 2019-07-31     | 16:08:16    | 2019-07-31 | 07:46:05 |     |     |     |     |
| poe_ctrlr_2_q2 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:16    | 2019-07-31 | 07:46:05 |     |     |     |     |
| poe_ctrlr_2_q3 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:16    | 2019-07-31 | 07:46:05 |     |     |     |     |
| poe_ctrlr_3_q1 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:16    | 2019-07-31 | 07:46:06 |     |     |     |     |
| poe_ctrlr_3_q2 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:16    | 2019-07-31 | 07:46:06 |     |     |     |     |
| poe_ctrlr_3_q3 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:17    | 2019-07-31 | 07:46:06 |     |     |     |     |
| poe_ctrlr_4_q1 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:17    | 2019-07-31 | 07:46:07 |     |     |     |     |
| poe_ctrlr_4_q2 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:17    | 2019-07-31 | 07:46:07 |     |     |     |     |
| poe_ctrlr_4_q3 | Pass        | 0x0        | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31     | 16:08:17    | 2019-07-31 | 07:46:08 |     |     |     |     |
| Module :       | FanTray 1/1 |            |          |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |           |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --------- | --- |
|          |           |           |           | Failure Count | Count | Iteration |     |
-------------- ------ ---------- ------------ ------------- ------------- ---------
| -------------------- |             | ------------------- |          |     |     |     |     |
| -------------------- | ----------- | ------------------- | -------- | --- | --- | --- | --- |
| ft1_eeprom           | Pass        | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:33    | 2019-07-31          | 07:44:54 |     |     |     |     |
| Module :             | FanTray 1/2 |                     |          |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |           |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --------- | --- |
|          |           |           |           | Failure Count | Count | Iteration |     |
-------------- ------ ---------- ------------ ------------- ------------- ---------
| -------------------- |          | ------------------- |          |     |     |     |     |
| -------------------- | -------- | ------------------- | -------- | --- | --- | --- | --- |
| ft2_eeprom           | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 3   |
| 2019-07-31           | 16:07:50 | 2019-07-31          | 07:44:54 |     |     |     |     |
Showingdiagnostictestresultsindetailformatforaspecifiedmoduleona6300switch:
| switch#  | show diagnostic  | management-module |     | detail |     |     |     |
| -------- | ---------------- | ----------------- | --- | ------ | --- | --- | --- |
| Module : | ManagementModule | 1/1               |     |        |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestamp | First Run | Timestamp |               |       |           |     |
| -------- | --------- | --------- | --------- | ------------- | ----- | --------- | --- |
|          |           |           |           | Failure Count | Count | Iteration |     |
-------------- ------ ---------- ------------ ------------- ------------- ---------
| -------------------- |          | ------------------- |          |     |     |     |     |
| -------------------- | -------- | ------------------- | -------- | --- | --- | --- | --- |
| ddr_cecount          | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 109 |
| 2019-07-31           | 16:43:38 | 2019-07-31          | 07:44:55 |     |     |     |     |
| emmc                 | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04 | 2019-07-31          | 07:44:55 |     |     |     |     |
| fan_ctrlr            | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 4   |
| 2019-07-31           | 16:08:04 | 2019-07-31          | 07:44:55 |     |     |     |     |
| fepld                | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 109 |
| 2019-07-31           | 16:43:38 | 2019-07-31          | 07:44:54 |     |     |     |     |
| fru_eeprom           | Pass     | 0x0                 | 0x0      |     | 0   | 0   | 4   |
RuntimeDiagnostics|90

| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:54 |     |     |     |     |     |
| ------------- | -------- | ---------- | -------- | --- | --- | --- | --- | --- |
| fru_eeprom_ul | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 4   |
| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:54 |     |     |     |     |     |
| mm_lcb        | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 109 |
| 2019-07-31    | 16:43:37 | 2019-07-31 | 07:44:54 |     |     |     |     |     |
| pmc           | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 109 |
| 2019-07-31    | 16:43:37 | 2019-07-31 | 07:44:54 |     |     |     |     |     |
| rdimm_spd     | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 4   |
| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:55 |     |     |     |     |     |
| rdimm_tmp     | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 4   |
| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:55 |     |     |     |     |     |
| rtc           | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 4   |
| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:55 |     |     |     |     |     |
| tmp1          | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 4   |
| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:55 |     |     |     |     |     |
| tmp2          | Pass     | 0x0        | 0x0      |     |     | 0   | 0   | 4   |
| 2019-07-31    | 16:08:04 | 2019-07-31 | 07:44:55 |     |     |     |     |     |
Showingdiagnostictestresultsinbriefformatforallmodulesona6400switch:
| switch# | show diagnostic | brief          |     |         |     |     |     |     |
| ------- | --------------- | -------------- | --- | ------- | --- | --- | --- | --- |
| Module  |                 | ID Diagnostics |     | Success |     |     |     |     |
Performed
| -------------------- |     | ----- ----------- |     | ------- |     |     |     |     |
| -------------------- | --- | ----------------- | --- | ------- | --- | --- | --- | --- |
| ManagementModule     |     | 1/1               | 19  | 100%    |     |     |     |     |
| LineModule           |     | 1/3               | 24  | 100%    |     |     |     |     |
| LineModule           |     | 1/7               | 12  | 100%    |     |     |     |     |
| LineModule           |     | 1/5               | 24  | 100%    |     |     |     |     |
| LineModule           |     | 1/4               | 24  | 100%    |     |     |     |     |
| LineModule           |     | 1/6               | 24  | 100%    |     |     |     |     |
| Fabric               |     | 1/1               |     | 6 100%  |     |     |     |     |
| FanTray              |     | 1/2               |     | 2 100%  |     |     |     |     |
| FanTray              |     | 1/1               |     | 2 100%  |     |     |     |     |
Showingdiagnostictestresultsinbriefformatforaspecifiedmoduleona6400switch:
| switch# | show diagnostic | management-module |     | brief   |     |     |     |     |
| ------- | --------------- | ----------------- | --- | ------- | --- | --- | --- | --- |
| Module  |                 | ID Diagnostics    |     | Success |     |     |     |     |
Performed
| -------------------- |     | ----- ----------- |     | ------- |     |     |     |     |
| -------------------- | --- | ----------------- | --- | ------- | --- | --- | --- | --- |
| ManagementModule     |     | 1/1               | 19  | 100%    |     |     |     |     |
Showingdiagnostictestresultsindetailformatforaspecifiedmoduleona6400switch:
| switch#  | show diagnostic  | management-module |     | detail |     |     |     |     |
| -------- | ---------------- | ----------------- | --- | ------ | --- | --- | --- | --- |
| Module : | ManagementModule | 1/1               |     |        |     |     |     |     |
Diagnostic Status Error Code History Code Successive Total Failure Total
| Last Run | Timestp |     |     |     |               |       |           |     |
| -------- | ------- | --- | --- | --- | ------------- | ----- | --------- | --- |
|          |         |     |     |     | Failure Count | Count | Iteration |     |
-------------- ------ ---------- ------------ ------------- ------------- ---------
----------------
| curr_sensor | Pass  | 0x0 | 0x0 |     |     | 0   | 0   | 2   |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| 2019-10-14  | 00:25 |     |     |     |     |     |     |     |
91
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| ddr_cecount | Pass 0x0 | 0x0 | 0   | 0   | 34  |
| ----------- | -------- | --- | --- | --- | --- |
| 2019-10-14  | 01:26    |     |     |     |     |
| eeprom      | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:25    |     |     |     |     |
| eeprom_ul   | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:25    |     |     |     |     |
| emmc        | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:26    |     |     |     |     |
| icbbp       | Pass 0x0 | 0x0 | 0   | 0   | 34  |
| 2019-10-14  | 01:24    |     |     |     |     |
| icbx        | Pass 0x0 | 0x0 | 0   | 0   | 34  |
| 2019-10-14  | 01:25    |     |     |     |     |
| ledpld      | Pass 0x0 | 0x0 | 0   | 0   | 34  |
| 2019-10-14  | 01:24    |     |     |     |     |
| mm_mcb      | Pass 0x0 | 0x0 | 0   | 0   | 34  |
| 2019-10-14  | 01:24    |     |     |     |     |
| psu1        | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:27    |     |     |     |     |
| psu1_eeprom | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:26    |     |     |     |     |
| psu2        | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:27    |     |     |     |     |
| psu2_eeprom | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:27    |     |     |     |     |
| rdimm_spd   | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:26    |     |     |     |     |
| rdimm_tmp   | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:26    |     |     |     |     |
| rtc         | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:26    |     |     |     |     |
| tmp1        | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:25    |     |     |     |     |
| tmp2        | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:25    |     |     |     |     |
| tmp3        | Pass 0x0 | 0x0 | 0   | 0   | 2   |
| 2019-10-14  | 00:25    |     |     |     |     |
CommandHistory
| Release        |     | Modification |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400            |        | forthiscommand. |     |     |     |
| --------------- | ------ | --------------- | --- | --- | --- |
| show diagnostic | events |                 |     |     |     |
| show diagnostic | events |                 |     |     |     |
Description
Displaysthediagnosticrelatedeventlogs.
Example
RuntimeDiagnostics|92

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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
93
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | ----------------------- | --- |

Chapter 13

Service OS

Service OS

Service OS is an operating system that the customer only uses to fix filesystem corruption, download and
update firmware, and other support related issues. HPE Service OS is a Linux distribution that acts as a
standalone bootloader and recovery OS for AOS-CX-based switches. It is only accessible if the user is
consoled into the switch. The main high level features provided include:

n Access to file system partitions for retrieval of logs, coredumps, and configuration for supportability

purposes.

n Filesystem utilities to format and partition a corrupted storage disk.

n Management interface networking with TFTP to download and update a product image.

n Ability to boot primary and secondary firmware images (.SWI file) on the storage disk.

n Support for clearing the AOS-CX startup-config.

n Ability to not only clear the admin password for AOS-CX, but also change it in SVOS.

n Ability to set the secure mode to enhanced or standard.

This document covers the customer CLI commands available in Service OS, as well as a few non-CLI features.

Service OS CLI login

Description

If the user enters 0 at the boot menu prompt, they will be presented with a Service OS CLI login prompt. The
user must enter the login account "admin" to log in. By default, Service OS does not require a password.

To reboot without logging in, enter reboot as the login user name.

There are two additional login accounts that execute a command without requiring a password: reboot and
zeroize. Enter the login account reboot to reboot the management module and zeroize to initiate a
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
Looking for SVOS.

Primary SVOS: Checking...Loading...Finding...Verifying...Booting...

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

94

ServiceOS Information:

Version:
Build Date:
Build ID:
SHA:

FL.01.07.0002-internal
2020-09-03 10:38:03 PDT
ServiceOS:FL.01.07.0002-internal:1a017598b673:202009031038
1a017598b6738448ef679175712e022a966eca88

..............
..............
To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: zeroize
This will securely erase all customer data, including passwords, and
reset the switch to factory defaults.
This action requires proof of physical access via a USB drive.

* Create a FAT32 formatted USB drive
* Create a file in the root directory of the USB drive named zeroize.txt
* Type the following serial number into the zeroize.txt file: SG9ZKN7050
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
Service OS provides a single admin login account. By default, no password is required to log in. Service OS
will require a password if the Service OS admin user account password feature is enabled. This setting can be
enabled or disabled in AOS-CX.

Service OS boot menu

Description

On boot, the user is presented with a Service OS version banner with version, build date, build time, build ID,
and SHA strings.

The user is then shown the boot image profiles.

n Enter 0 to boot the Service OS login CLI.

n Enter 1 to boot the primary firmware image.

n Enter 2 to boot the secondary firmware image.

n If no input is given within 5 seconds, the default boot profile is selected. Alternatively, press Enter to

select the default boot profile.

Service OS | 95

Theimageselectedbytheuserduringbootisarun-timedecisiononlyandwillnotpersistacrossreboots.
Thedefaultimagecanbeconfiguredusingtheboot set-defaultcommand.
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
The(primary)stringinthebootmenudisplaysthedefaultbootprofilethatwillbebootedafterthetimeoutperiod.
Thisstringwillchangeto(secondary)or(ServiceOS)dependingonthecurrentdefaultbootoption.
| Console | configuration |     |     |
| ------- | ------------- | --- | --- |
Duringboot,ServiceOScommunicateswiththeRJ45serialconsolewithabaudrateof115200.Thereisno
optiontochangethebaudrateduringboot.
Additionally,ifaUSBconsoleisconnectedtothemanagementmoduleconsoleport,inputwillautomatically
beswitchedovertousetheUSBconsole.AutomaticswitchingtoUSBisconsistentwiththeAOS-CXUSB
consolebehavior.
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
Builddate
n
ServiceOSwillthenpresentstatusandboottheimage.
Example
96
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| Booting   | primary software |     | image... |     |     |     |
| --------- | ---------------- | --- | -------- | --- | --- | --- |
| Verifying | Image...         |     |          |     |     |     |
Image Info:
Name: ArubaOS-CX
| Version:   | XL.01.01.0001                                          |     |              |     |     |     |
| ---------- | ------------------------------------------------------ | --- | ------------ | --- | --- | --- |
| Build      | Id: ArubaOS-CX:XL.01.01.0001:1a36111da4e0:201707171452 |     |              |     |     |     |
| Build      | Date: 2017-07-17                                       |     | 14:52:27 PDT |     |     |     |
| Extracting | Image...                                               |     |              |     |     |     |
| Loading    | Image...                                               |     |              |     |     |     |
Done.
| kexec:      | Starting new | kernel |     |     |     |     |
| ----------- | ------------ | ------ | --- | --- | --- | --- |
| File system | access       |        |     |     |     |     |
Description
WhentheuserlogsintotheServiceOSCLI,theyarepresentedwithalimitedfilesystem.Theusercanuse
standardfilesystemcommandsofcd,ls,andpwdtoviewandmovethroughthefilesystem.
Onlogin,theuserisfirstplacedinthe/homedirectory:
| (C) Copyright | 2017 | Hewlett    | Packard Enterprise | Development |     | LP  |
| ------------- | ---- | ---------- | ------------------ | ----------- | --- | --- |
|               |      | RESTRICTED | RIGHTS             | LEGEND      |     |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. Government | under | vendor's | standard | commercial | license. |     |
| --------------- | ----- | -------- | -------- | ---------- | -------- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
| ServiceOS | login: | admin |     |     |     |     |
| --------- | ------ | ----- | --- | --- | --- | --- |
SVOS> pwd
/home
SVOS>
ThehomedirectoryandtheUSBdevice(/mnt/usbandanysubdirectory)aretheonlywritabledirectories
available.ThesedirectoriescanbeusedasastaginglocationfordownloadingproductimagesusingTFTP.
/homecanalsobeusedastemporarystoragebeforecopyingfilesfromthemanagementmodulethrough
TFTPorUSB.Anychangesmadeto/homewillnotpersistacrossrebootsorafterbootinganAOS-CXimage.
Theroot/directorydisplaysviewabledirectories:
| SVOS> ls | /        |      |     |          |     |     |
| -------- | -------- | ---- | --- | -------- | --- | --- |
| bin      | coredump | lib  | mnt | selftest |     |     |
| cli      | home     | logs | nos |          |     |     |
SVOS>
Thedirectoriescoredump,selftest,nos,andlogseachprovidetheuseraccesstoanSSD partitionmount.
Theusermayread,butnotwriteanyfileonthesepartitions.
ThesemountpointsallowtheusertocopyfilesontheSSD toaUSBstoragedeviceoruploadfilesusing
TFTP.CopyingfilesfromtheSSD isintendedtobeusedundertheguidanceofasupportengineer(to
uploadlogsorcoredumpstoHPEsupport).
ServiceOS|97

USBstoragedeviceaccessisprovidedthroughthemountat/mnt/usb.
Theremainingdirectoriesintherootfilesystembin,cli,andlibarenotintendedtobeusedbythecustomer.
| Service | OS  | mount |     |     | failure |     |     |     |     |     |     |
| ------- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Description
IftheSSD isdetectedasmissingoranyofthepartitionscouldnotbemounted,ServiceOSwillforcethe
usertoboottotheServiceOSconsoleanddisplayanerrormessageindicatingthatrecoveryshouldbe
attemptedusingtheformatcommand.
Example
| (C) Copyright |     | 2017 | Hewlett |            | Packard | Enterprise |        | Development |     | LP  |     |
| ------------- | --- | ---- | ------- | ---------- | ------- | ---------- | ------ | ----------- | --- | --- | --- |
|               |     |      |         | RESTRICTED |         | RIGHTS     | LEGEND |             |     |     |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. | Government |     | under | vendor's |     | standard | commercial |     | license. |     |     |
| ---- | ---------- | --- | ----- | -------- | --- | -------- | ---------- | --- | -------- | --- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
| Error,    | Could   | not    | mount      | the        | primary |           | storage     | device.  |     |     |     |
| --------- | ------- | ------ | ---------- | ---------- | ------- | --------- | ----------- | -------- | --- | --- | --- |
| This      | may     | be due | to         | filesystem |         | or device | corruption. |          |     |     |     |
| Please    | attempt |        | to recover |            | using   | the       | "format"    | command. |     |     |     |
| ServiceOS |         | login: |            |            |         |           |             |          |     |     |     |
| Service   | OS      | CLI    |            | command    |         |           | list        |          |     |     |     |
Description
AfterlogintoServiceOSCLI,theusermayenterthecommandshelpor?togetafulllistofcommandsanda
tersedescriptionforeachcommand.Theusermayalsoenter<command>followedby--helptogetmore
detailedhelpandusageforaspecificcommand.
Example
| SVOS>     | ?   |           |      |           |     |         |           |     |           |     |     |
| --------- | --- | --------- | ---- | --------- | --- | ------- | --------- | --- | --------- | --- | --- |
| Available |     | Commands: |      |           |     |         |           |     |           |     |     |
|           |     |           | ?    | - Display |     | help    | screen    |     |           |     |     |
|           |     |           | cd   | - Change  | the | working | directory |     |           |     |     |
|           |     |           | pwd  | - Print   | the | current | working   |     | directory |     |     |
|           |     |           | help | - Display |     | help    | screen    |     |           |     |     |
allow-unsafe-updates - Allow non-failsafe updates for a limited amount of time
|     |              |          | boot  | - Boot     | a product  |                | image          |         |               |                   |        |
| --- | ------------ | -------- | ----- | ---------- | ---------- | -------------- | -------------- | ------- | ------------- | ----------------- | ------ |
|     | config-clear |          |       | - Clears   | the        | startup-config |                |         |               |                   |        |
|     |              |          | diag  | - Run      | diagnostic |                | commands       |         |               |                   |        |
|     |              |          | erase | - Securely |            | erase          | storage        | devices |               | on the management | module |
|     |              | format   |       | - Formats  |            | and partitions |                | the     | primary       | storage device    |        |
|     |              | identify |       | - Prints   | hardware   |                | identification |         |               | information       |        |
|     |              |          | ip    | - Sets     | the        | OOBM           | Port Network   |         | Configuration |                   |        |
98
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |

|         |             | mount    | - Mount       | a           | storage        | device         |            |                  |
| ------- | ----------- | -------- | ------------- | ----------- | -------------- | -------------- | ---------- | ---------------- |
|         |             | password | - Set         | the         | admin          | account        | password   |                  |
|         |             |          | ping - Send   | ICMP        | ECHO_REQUEST   |                | to network | hosts (IPv4)     |
|         |             | reboot   | - Reboots     |             | the Management |                | Module     |                  |
|         | secure-mode |          | - Set         | or          | retrieve       | the            | secure     | mode setting     |
|         |             |          | sh - Launch   |             | support        | shell          |            |                  |
|         |             | umount   | - Unmounts    |             | a storage      | device         |            |                  |
|         |             | update   | - Update      |             | a product      | image          |            |                  |
|         |             | version  | - Prints      |             | ServiceOS      | release        | version    | information      |
|         |             |          | cat - Prints  |             | files          | to stdout      |            |                  |
|         |             |          | cp - Copy     | files       | and            | directories    |            |                  |
|         |             |          | du - Estimate |             | file           | space          | usage      |                  |
|         |             |          | ls - List     | directory   |                | contents       |            |                  |
|         |             | md5sum   | - Compute     |             | and check      | md5            | message    | digest           |
|         |             | mkdir    | - Make        | directories |                |                |            |                  |
|         |             |          | mv - Move     | (rename)    |                | files          |            |                  |
|         |             |          | rm - Remove   |             | files          | or directories |            |                  |
|         |             | rmdir    | - Remove      |             | empty          | directories    |            |                  |
|         |             |          | tftp - Allows |             | transfer       | of files       | to/from    | a remote machine |
|         |             |          | exit - Logout |             |                |                |            |                  |
| Enter   | '<command>  |          | --help'       | for more    | info           |                |            |                  |
| Service | OS          | CLI      | features      |             | and            | limitations    |            |                  |
TheServiceOSCLIprovidesbasicshellfunctionalitythatallowsyoutoexecutecommandsandpass
argumentstothosecommandsonly.Thefollowingfeaturesarenotavailable:
n Input/outputredirection(<,>,>>)
n Jobcontrol(&,fg,bg)
Processpiping(|)
n
Fileglobbing(\*)
n
EventhoughtheServiceOSCLIdoesnotprovidefileglobbingcapabilities,somecommandsmayprovidethis
functionalityinternally.Anexampleisthelscommand.
Thefollowingcommonfeaturesareavailable:
n Commandhistory(UpArrow)andsearch(Ctrl-R)
n Tabcompletionforfileandfoldernames(notCLIcommands)
n CommandabortusingCtrl-C
| Service | OS  | CLI | commands |     |     |     |     |     |
| ------- | --- | --- | -------- | --- | --- | --- | --- | --- |
boot
boot
Description
Presentsyouwiththebootmenuprompt.Youcanthenspecifywhichbootprofile:primary,secondary,or
ServiceOSconsole.
Example
ServiceOS|99

Presentingthebootmenuprompt:
| SVOS>     | boot     |              |                        |     |              |     |
| --------- | -------- | ------------ | ---------------------- | --- | ------------ | --- |
| ServiceOS |          | Information: |                        |     |              |     |
|           | Version: |              | FL.01.07.0002-internal |     |              |     |
|           | Build    | Date:        | 2020-09-03             |     | 10:38:03 PDT |     |
Build ID: ServiceOS:FL.01.07.0002-internal:1a017598b673:202009031038
|     | SHA: |     | 1a017598b6738448ef679175712e022a966eca88 |     |     |     |
| --- | ---- | --- | ---------------------------------------- | --- | --- | --- |
Boot Profiles:
| 0.     | Service           | OS Console |       |                              |     |     |
| ------ | ----------------- | ---------- | ----- | ---------------------------- | --- | --- |
| 1.     | Primary           | Software   | Image | [FL.10.06.0001]              |     |     |
| 2.     | Secondary         | Software   | Image | [FL.10.08.0000-308-gcfbc0e3] |     |     |
| Select | profile(primary): |            |       |                              |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
cat
cat <FILENAME/DIRECTORY-NAME>
Description
Printsthecontentsofafiletotheconsole.TheServiceOSdoesnotallowcommandoutputredirection,so
thiscommandisonlyusefulforreadingshorttextfiles.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<FILENAME/DIRECTORY-NAME> Showsthecontentsofthespecifiedfileordirectory.
Example
Showingthecontentsof/nos/hosts:
| SVOS>     | cat | /nos/hosts            |     |     |     |           |
| --------- | --- | --------------------- | --- | --- | --- | --------- |
| 127.0.0.1 |     | localhost.localdomain |     |     |     | localhost |
SVOS>
CommandHistory
100
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- |

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS (SVOS>)

Administrators or local user group members with execution rights
for this command.

cd path
cd path

Description

Changes the current working directory.

Example

Changing the current working directory:

cd /

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

Administrators or local user group members with execution rights
for this command.

config-clear
config-clear

Description

Configures the switch to set all configuration settings to factory default when the switch is restarted. The
next time the switch starts, the current startup-config is renamed to startup-config-fixme, and a new
startup-config is created with factory default settings.

Using this command is not the same as performing zeroization, which securely erases the entire primary storage

and other devices, and not just the configuration.

Example

Service OS | 101

Configuringthesystemtocleartheswitchconfiguration:
| SVOS> config-clear |               |         |          |     |
| ------------------ | ------------- | ------- | -------- | --- |
| The switch         | configuration | will be | cleared. |     |
| Continue           | (y/n)? y      |         |          |     |
The system has been configured to clear the startup-config on the next
| boot. Please | execute the | 'boot' | command to complete | this action. |
| ------------ | ----------- | ------ | ------------------- | ------------ |
SVOS>
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
cp
cp [options] <SOURCE-FILENAME/SOURCE-DIRECTORY> <DESTINATION-FLENAME/DESTINATION-DIRECTORY>
Description
Copiesfilesordirectories.
Parameter Description
[options] Selectstheoptionsforthecommand.
-d,-P Specifiesthepreservationofsymlinks(defaultif-R).
-a Sameas-dpR.
R,-r Specifiesrecursiveness,allfiles,andsubdirectoriesare
copied.
-L
Specifiesthefollowingofallsymlinks.
-H Specifiesthefollowingofsymlinksoncommandline.
-p
Specifiesthepreservationoffileattributesifpossible.
-f Specifiestheoverwritingofafileordirectory.
-i
Specifiesthepromptingbeforeanoverwrite.
-l,-s Specifiesthecreationof(sym)links.
102
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- |

Parameter Description
<SOURCE-FILENAME/SOURCE-DIRECTORY> Specifiesthenameofthesourcefileordirectory.
<DESTINATION-FLENAME/DESTINATION-DIRECTORY> Specifiesthenameofthedestinationfileordirectory.
Example
Copying/home/customersdirectorytothe/home/clientsdirectory:
| SVOS> cp | /home/customers /home/clients |     |
| -------- | ----------------------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
du
| du [options] | <FILENAME/DIRECTORY-NAME>... |     |
| ------------ | ---------------------------- | --- |
Description
Showsestimateddiskspaceusedforeachfileordirectoryorboth.
| Parameter |     | Description                     |
| --------- | --- | ------------------------------- |
| [options] |     | Selectstheoptionsforthecommand. |
-a
Showfilesizes.
| -L  |     | Showsallsymlinks. |
| --- | --- | ----------------- |
-H
Showssymlinksonacommandline.
-d, N Showslimitedoutputtodirectories(andfileswith-a)ofdepthless
thanN.
| -c  |     | Showsthetotaldiskspaceusageofallfilesordirectoriesorboth. |
| --- | --- | --------------------------------------------------------- |
| -l  |     | Showsthecountsizesifhardlinked.                           |
| -s  |     | Showsonlyatotalforeachargument.                           |
| -x  |     | Doesnotshowdirectoriesondifferentfilesystems.             |
ServiceOS|103

| Parameter |     | Description                                    |     |
| --------- | --- | ---------------------------------------------- | --- |
| -h        |     | Showsizesinhumanreadableformat(1K,243M,and2G). |     |
| -m        |     | Showsizesinmegabytes.                          |     |
| -k        |     | Showsizesinkilobytes(default).                 |     |
<FILENAME/DIRECTORY-NAME> Specifiesthefileordirectoryorbothfordisplayingasize
estimate.
Example
Estimatingdiskspaceforthe/nosdirectory:
| SVOS> du | -ah /nos         |     |     |
| -------- | ---------------- | --- | --- |
| 196.4M   | /nos/primary.swi |     |     |
| 196.4M   | /nos             |     |     |
SVOS>
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
erase zeroize
erase zeroize
Description
SecurelyerasesanyuserdatacontainedontheSSD orotherstoragedevicesonthemanagementmodule.
Backupalldatabeforerunningthiscommandoralluser/configdatawillbelost.
Example
Erasinguserdata:
| SVOS> SVOS>  | erase --help           |                   |         |
| ------------ | ---------------------- | ----------------- | ------- |
| Usage: erase | zeroize                |                   |         |
| Securely     | erases storage devices | on the management | module. |
SVOS>
```
104
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | ----------------------- | --- |

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

Version: FL.01.07.0002-internal
Build Date: 2020-09-02 11:53:34 PDT
Build ID: ServiceOS:FL.01.07.0002-internal:1a017598b673:202009031038
SHA: 1a017598b6738448ef679175712e022a966eca88

################ Preparing for zeroization #################

################ Storage zeroization #######################
################ WARNING: DO NOT POWER OFF UNTIL ##########
ZEROIZATION IS COMPLETE ##########
################
################ This should take several minutes ##########
##########
################ to one hour to complete

################ Restoring files ###########################

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

Administrators or local user group members with execution rights
for this command.

exit
exit

Description

Logs the user out from the SVOS> prompt.

Example

Loging the user out from the SVOS> prompt:

SVOS> exit

(C) Copyright 2022 Hewlett Packard Enterprise Development LP

Service OS | 105

|     |     |     | RESTRICTED |     | RIGHTS | LEGEND |     |
| --- | --- | --- | ---------- | --- | ------ | ------ | --- |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. Government |     | under | vendor's |     | standard | commercial | license. |
| --------------- | --- | ----- | -------- | --- | -------- | ---------- | -------- |
To reboot without logging in, enter 'reboot' as the login user name.
| ServiceOS | login: |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
format
format
Description
Configurestheprimarystoragedevicewiththecorrectpartitionandfilesystemformatting.Thiscommand
removesallpre-existingdataontheprimarystoragedevice.
Example
Configuringtheprimarystoragedevicewiththecorrectpartitionandfilesystemformatting:
| SVOS> format |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
##################WARNING####################
| The following |     | action     | will    | cause           | all data | on    |     |
| ------------- | --- | ---------- | ------- | --------------- | -------- | ----- | --- |
| the primary   |     | storage    | device  | to be           | lost.    | After |     |
| formatting    | has | completed, |         | a reboot        | will     | be    |     |
| initiated     | to  | complete   | storage | initialization. |          |       |     |
##################WARNING####################
| Continue?      | (y/n): | y   |      |                  |     |     |     |
| -------------- | ------ | --- | ---- | ---------------- | --- | --- | --- |
| Working...This |        | may | take | a few minutes... |     |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
106
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |

CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip
| ip {show | | dhcp | disable | | addr <ADDR-NETMASK-GATEWAY>} |     |
| -------- | ---------------- | ------------------------------ | --- |
Description
ServiceOS|107

ShowsorconfigurestheportwithastaticIPaddress(IPv4only)orenablestheDHCPclientontheport.An
addressissetonlyifaDHCPserverisavailabletoprovideone.
Parameter Description
{show | dhcp | disable | addr <ADDR-NETMASK-GATEWAY>} SelectstheoptionsfortheOOBMport.
show
ShowstheOOBMport.
dhcp ConfigurestheportwithaDHCPaddress.
disable
DisablestheOOBMport.
addr <ADDR-NETMASK-GATEWAY> ConfigurestheportwithastaticIPaddress
(IPv4only).Specifyaddress,netmask,and
gatewayasA.B.C.D.
Example
ConfiguringtheportwithaDHCPIPaddress:
| SVOS> ip     | dhcp          |     |
| ------------ | ------------- | --- |
| SVOS> ip     | show          |     |
| Interface    | : Link Up     |     |
| IP Address   | : 10.0.26.17  |     |
| Subnet Mask: | 255.255.252.0 |     |
| Gateway      | : 10.0.24.1   |     |
| SVOS> ip     | disable       |     |
| SVOS> ip     | show          |     |
| Interface    | : Disabled    |     |
SVOS>
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |
| ---- | --- | --------------- |
ls
| ls [<OPTIONS>] | [<FILE-NME>] |     |
| -------------- | ------------ | --- |
Description
Thiscommandlistsdirectorycontents.
108
| AOS-CX10.08DiagnosticsandSupportabilityGuide| | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | ----------------------- | --- |

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

-u

-c

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
asterisk (*) or slash (/) or equal sign (=) or at sign (@) or pipe (|).

Shows the output in a long listing format.

Shows the list inode numbers.

Shows a list of numeric UIDs and GIDs instead of names.

Shows a list of allocated blocks.

Shows in one column a list with the full date and time.

Shows list sizes in human readable format (1K, 243M, 2G) with a
one-column output.

Shows in one column a sort in reverse order.

Shows in one column a sort by size.

Shows in the output sort by extension.

Shows in one column a sort by version.

With -l, it shows a sort in one column by ctime.

With -l, it shows a sort by mtime.

With -l, sort by atime.

With -l, it shows a sort in one column by ctime

Service OS | 109

| Parameter |     |     |     |     | Description                                       |     |     |     |
| --------- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
| -w        | <N> |     |     |     | Assumesthattheterminalhasthenumberofcolumnswideas |     |     |     |
specifiedby<N>.
| --color[={always |     |     | | never | | auto}] | Controlscolorintheoutput. |     |     |     |
| ---------------- | --- | --- | ------- | -------- | ------------------------- | --- | --- | --- |
<FILE-NAME>
Specifiesthenameofthefiletolist.
Example
Listingdirectorycontents:
| SVOS>      | ls -la | /nos |     |     |           |           |          |             |
| ---------- | ------ | ---- | --- | --- | --------- | --------- | -------- | ----------- |
| drwxr-xr-x |        | 3    | 0   | 0   |           | 4096 Nov  | 21 03:19 | .           |
| drwxr-xr-x |        | 11   | 0   | 0   |           | 220 Nov   | 21 03:21 | ..          |
| drwx------ |        | 2    | 0   | 0   |           | 16384 Nov | 21 03:20 | lost+found  |
| -rwxr-xr-x |        | 1    | 0   | 0   | 205957424 | Nov       | 21 03:19 | primary.swi |
SVOS>
CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
md5sum
| md5sum [-c | |   | -s | -w] | [<FILE-NAME>] |     |     |     |     |     |
| ---------- | --- | -------- | ------------- | --- | --- | --- | --- | --- |
Description
ThiscommandcomputesandcheckstheMD5messagedigest.
| Parameter   |          |     |     |     | Description                                           |     |     |     |
| ----------- | -------- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
| [-c |       | -s | -w] |     |     |     | Selectstheoptionsforthecommand.                       |     |     |     |
| -c          |          |     |     |     | Specifiestocheckthesumsagainstthelistinfiles.         |     |     |     |
| -s          |          |     |     |     | Specifiesnotoutputanything,statuscodeshowssuccess.    |     |     |     |
| -w          |          |     |     |     | Specifiestowarnaboutimproperlyformattedchecksumlines. |     |     |     |
| <FILE-NAME> |          |     |     |     | Specifiesthefilenametorunthechecksumagainst.          |     |     |     |
Example
ComputingandcheckingtheMD5messagedigestfor/nos/primary.swi:
110
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |

| SVOS> md5sum                     | /nos/primary.swi |                  |
| -------------------------------- | ---------------- | ---------------- |
| 93ffc89e7ec357854704d8e450c4b7ab |                  | /nos/primary.swi |
SVOS>
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mkdir
| mkdir [-m | | -p] [<DIRECTORY-NAME>] |     |
| ----------- | ---------------------- | --- |
Description
Thiscommandmakesdirectories.
| Parameter |     | Description                                             |
| --------- | --- | ------------------------------------------------------- |
| [-m | -p] |     | Specifiestheoptionsforthecommand.                       |
| -m        |     | Specifiesthemode.                                       |
| -p        |     | Specifiestomakeparentdirectoriesasneededwithnoerrorsfor |
pre-existingdirectories.
| <DIRECTORY-NAME> |     | Specifiesthedirectorytocreate. |
| ---------------- | --- | ------------------------------ |
Example
Makingthedirdirectory:
| SVOS> mkdir | dir |     |
| ----------- | --- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
ServiceOS|111

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
mount
mount <DEVICE>
Description
ThiscommandmountstheSSD partitionstothefollowinglocations:/coredump,/logs,/nos,/selftest,
andmountstheUSBdeviceto/mnt/usb.
UserscanmountUSBflashdrivesformattedaseitherFAT16orFAT32withasinglepartition.
| Parameter |     | Description |
| --------- | --- | ----------- |
<DEVICE> Specifiesthedevicetobemounted.Supporteddeviceoptions
includeallandusb.
Examples
| MountingalloftheSSD | partitions: |     |
| ------------------- | ----------- | --- |
| SVOS> mount         | all         |     |
| SVOS> mount         | usb         |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mv
| mv [-f | -i | | -n] <TARGET-DIRECTORY> |     |
| ----------- | ------------------------ | --- |
Description
Thiscommandmoves(renames)files.
| Parameter |     | Description |
| --------- | --- | ----------- |
-f
Specifiesnottopromptbeforeoverwriting.
112
| AOS-CX10.08DiagnosticsandSupportabilityGuide| | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | ----------------------- | --- |

| Parameter |     | Description                            |
| --------- | --- | -------------------------------------- |
| -i        |     | Specifiestopromptbeforeoverwriting.    |
| -n        |     | Specifiestonotoverwriteanexistingfile. |
Example
Movingthefilenamedmyfile:
| SVOS> mv | myfile |     |
| -------- | ------ | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
password
password
Description
SetstheadminuseraccountpasswordforbothServiceOSandAOS-CXoncetheuserbootsintoAOS-CX
andsavestheconfiguration.Thiswilloverwritethepreviouspasswordifoneexists.Userinputismasked
withasterisks.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Settingtheadminaccountpassword:
| SVOS> password          |                   |     |
| ----------------------- | ----------------- | --- |
| Enter password:******** |                   |     |
| Confirm                 | password:******** |     |
SVOS>
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
ServiceOS|113

Platforms

Command context

Authority

All platforms

ServiceOS (SVOS>)

Administrators or local user group members with execution rights
for this command.

ping
ping <HOST-IP-ADDRESS>

Description

Pings network hosts for debug purposes.

Parameter

Description

<HOST-IP-ADDRESS>

Specifies the host IP address.

Example

Pinging a network host:

SVOS> ping 10.0.8.10
PING 10.0.8.10 (10.0.8.10): 56 data bytes
64 bytes from 10.0.8.10: seq=0 ttl=63 time=3.496 ms
64 bytes from 10.0.8.10: seq=1 ttl=63 time=0.367 ms
64 bytes from 10.0.8.10: seq=2 ttl=63 time=0.380 ms
64 bytes from 10.0.8.10: seq=3 ttl=63 time=0.282 ms
64 bytes from 10.0.8.10: seq=4 ttl=63 time=0.669 ms
^C
--- 10.0.8.10 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.282/1.038/3.496 ms
SVOS>

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

ServiceOS (SVOS>)

Administrators or local user group members with execution rights
for this command.

6300
6400

pwd
pwd

Description

Displays the current working directory.

Example

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

114

Displayingthecurrentworkingdirectory:
| SVOS> | pwd |     |     |
| ----- | --- | --- | --- |
/home
SVOS>
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
reboot
reboot
Description
RebootstheManagementModule.
Example
Rebootingthemanagementmodule:
| SVOS>   | reboot     |        |     |
| ------- | ---------- | ------ | --- |
| reboot: | Restarting | system |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
rm
| rm [-f | | -i | -R | -r] | <FILE-NAME> |     |
| -------- | ------------- | ----------- | --- |
Description
Removesfilesordirectories.
ServiceOS|115

| Parameter |     | Description |
| --------- | --- | ----------- |
[-f | -i | -R | -r] Selectstheoptionsforremovingfilesordirectories.
| -f      |     | Neverpromptbeforeremovingfilesordirectories.  |
| ------- | --- | --------------------------------------------- |
| -i      |     | Alwayspromptbeforeremovingfilesordirectories. |
| -R | -r |     | Recursive.                                    |
Example
Removingthefilenamedfoo:
| SVOS> rm | foo |     |
| -------- | --- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
rmdir
| rmdir [-p] <DIRECTORY-NAME> |     |     |
| --------------------------- | --- | --- |
Description
Removesemptydirectories.
| Parameter |     | Description                         |
| --------- | --- | ----------------------------------- |
| -p        |     | Specifiestoremoveparentdirectories. |
Example
Removingtheemptyfoodirectory:
| SVOS> rmdir | foo |     |
| ----------- | --- | --- |
SVOS>
CommandHistory
116
| AOS-CX10.08DiagnosticsandSupportabilityGuide| | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | ----------------------- | --- |

| Release        |     |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
secure-mode
| secure-mode | <enhanced |     | | standard |     | | status> |     |     |     |     |
| ----------- | --------- | --- | ---------- | --- | --------- | --- | --- | --- | --- |
Description
Setsthesecuremodetoenhancedorstandardsecuremode.Alsocandisplaythecurrentsecuremode.A
zeroizationisrequiredbeforeswitchingbetweenenhancedandstandardsecuremodes.
Thecommandalsodisplaysamessagenotifyingtheuserthattheyarealreadyinthetargetedsecuremode.
Example
Settingthesecuremodetoenhancedorstandard:
| SVOS>  | secure-mode |     | --help    |     |          |     |         |     |     |
| ------ | ----------- | --- | --------- | --- | -------- | --- | ------- | --- | --- |
| Usage: | secure-mode |     | <enhanced | |   | standard | |   | status> |     |     |
Set or retrieve the secure mode setting. Requires a zeroization to change modes.
SVOS>
```
```
| SVOS> | secure-mode |     | enhanced |     |     |     |     |     |     |
| ----- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
| This         | will set        | the     | switch      | into      | enhanced | secure   | mode.   | Before      |       |
| ------------ | --------------- | ------- | ----------- | --------- | -------- | -------- | ------- | ----------- | ----- |
| enhanced     | secure          | mode    | is enabled, |           | the      | switch   | must    | securely    | erase |
| all customer |                 | data    | and reset   | the       | switch   | to       | factory | defaults.   |       |
| This         | will initiate   |         | a reboot    | and       | render   | the      | switch  | unavailable |       |
| until        | the zeroization |         | is          | complete. |          |          |         |             |       |
| This         | should take     | several |             | minutes   | to       | one hour | to      | complete.   |       |
############################WARNING############################
| Continue | (y/n)?     | y   |        |     |     |     |     |     |     |
| -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
| reboot:  | Restarting |     | system |     |     |     |     |     |     |
```
```
| SVOS> | secure-mode |     | standard |     |     |     |     |     |     |
| ----- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
| This         | will set        | the     | switch      | into      | standard | secure   | mode.   | Before      |       |
| ------------ | --------------- | ------- | ----------- | --------- | -------- | -------- | ------- | ----------- | ----- |
| standard     | secure          | mode    | is enabled, |           | the      | switch   | must    | securely    | erase |
| all customer |                 | data    | and reset   | the       | switch   | to       | factory | defaults.   |       |
| This         | will initiate   |         | a reboot    | and       | render   | the      | switch  | unavailable |       |
| until        | the zeroization |         | is          | complete. |          |          |         |             |       |
| This         | should take     | several |             | minutes   | to       | one hour | to      | complete.   |       |
############################WARNING############################
ServiceOS|117

| Continue | (y/n)? y   |        |     |     |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |     |     |
```
```
| SVOS> secure-mode |     | standard |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
| Secure       | mode is already | set       | to        | standard. |          | Setting | it again    | will  |
| ------------ | --------------- | --------- | --------- | --------- | -------- | ------- | ----------- | ----- |
| repeat       | the zeroization | process.  |           | The       | switch   | must    | securely    | erase |
| all customer | data            | and reset | the       | switch    | to       | factory | defaults.   |       |
| This will    | initiate        | a reboot  | and       | render    | the      | switch  | unavailable |       |
| until the    | zeroization     | is        | complete. |           |          |         |             |       |
| This should  | take several    |           | minutes   | to        | one hour | to      | complete.   |       |
############################WARNING############################
| Continue | (y/n)? y   |        |     |     |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |     |     |
```
```
| SVOS> secure-mode |             | status  |     |     |     |     |     |     |
| ----------------- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
| enhanced          | secure mode | is set. |     |     |     |     |     |     |
SVOS>
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
CommandHistory
118
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
umount
umount <DEVICE>
Description
UnmountstheSSD partitionsmountedtothefollowinglocations:/coredump,/logs,/nos,/selftest,and
unmountstheUSBdevicemountedto/mnt/usb.
| Parameter |     | Description |
| --------- | --- | ----------- |
<DEVICE> Specifiesthedevicetobeunmounted.Supporteddeviceoptions
includeallandusb.
Examples
Unmountingalldevices:
| SVOS> umount | all |     |
| ------------ | --- | --- |
| SVOS> umount | usb |     |
UnmountingaUSBdevice:
| SVOS> umount | all |     |
| ------------ | --- | --- |
| SVOS> umount | usb |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
update
ServiceOS|119

| update {primary | | secondary} | <IMAGE> |     |     |
| --------------- | ------------ | ------- | --- | --- |
Description
Verifiesandinstallsaproductimage.Theusercanselecttheprimaryorsecondarybootprofiletoupdate
andthelocationofthefile.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{primary | secondary} Selectseithertheprimaryorsecondaryimage.
<IMAGE>
Specifiestheimagename.
Examples
UpdatingthesoftwareimageusingTFTP:
TheOOBMportisdisabledonfirstbootandmustbeenabledusingtheipcommand.
| SVOS> ip     | dhcp                    |     |              |            |
| ------------ | ----------------------- | --- | ------------ | ---------- |
| SVOS> ip     | show                    |     |              |            |
| Interface    | : Link Up               |     |              |            |
| IP Address   | : 192.0.2.22            |     |              |            |
| Subnet Mask: | 255.255.200.20          |     |              |            |
| Gateway      | : 10.0.24.1             |     |              |            |
| SVOS> tftp   | -g -r XL.10.00.0001.swi |     | -l image.swi | 192.4.8.10 |
XL.10.00.0001.swi 100% |*******************************| 178M 0:00:00 ETA
| SVOS> ls |     |     |     |     |
| -------- | --- | --- | --- | --- |
image.swi
| SVOS> update | primary image.swi |          |     |     |
| ------------ | ----------------- | -------- | --- | --- |
| Updating     | primary software  | image... |     |     |
| Verifying    | image...          |          |     |     |
Done
UpdatethesoftwareimageusingUSB:
ThisexampleassumesthattheuserhaspreloadedaUSBflashdrivewiththeimagetobeupdated.Theimage
nameontheflashdriveisnotimportant.
| SVOS> mount | usb      |     |     |     |
| ----------- | -------- | --- | --- | --- |
| SVOS> ls    | /mnt/usb |     |     |     |
image.swi
| SVOS> update | primary /mnt/usb/image.swi |          |     |     |
| ------------ | -------------------------- | -------- | --- | --- |
| Updating     | primary software           | image... |     |     |
| Verifying    | image...                   |          |     |     |
Done
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
120
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
tftp
tftp {-b | -g | -l <LOCAL-FILE> | -p | -r <REMOTE-FILE>} host [<PORT>]
Description
Transfersfilestoandfromaremotemachine(TFTPafile).
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{-b | -g | -l | -p | -r <REMOTE-FILE>} Selectstheoptionsfortransferringafile.
| -b  |     |     | Specifiesthetransferblocksofsizeoctets.Thedefault |     |
| --- | --- | --- | ------------------------------------------------- | --- |
blocksizeissetto1468,whichcanbeoverriddenwiththe-b
option.
| -g  |     |     | Specifiestogetafile. |     |
| --- | --- | --- | -------------------- | --- |
-l
Specifiesalocalfile.
| -p  |     |     | Specifiestoputafileinremotelocation. |     |
| --- | --- | --- | ------------------------------------ | --- |
-r <REMOTE-FILE>
Specifiesaremotefile.
<PORT> Specifiestheportfortransfer.Ifnoportoptionisspecified,
TFTPusesthestandardUDPport69bydefault.
Example
Transferringfiles:
| SVOS> tftp | -b 65464 | -g -r XL.10.00.0002.swi.swi |     | 192.0.2.1 |
| ---------- | -------- | --------------------------- | --- | --------- |
XL.10.00.0002 100% |*******************************| 178M 0:00:00 ETA
SVOS>
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
version
ServiceOS|121

version
Description
Displaysthefollowingbuildstrings:
Version.
n
Builddate.
n
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
122
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |
| --------------------------------------------- | --- | --- | ----------------------- |

Chapter 14
In-System Programming
| In-System | Programming |     |     |     |
| --------- | ----------- | --- | --- | --- |
TheISP(In-SystemProgramming)featureprovidesanautomatedwaytorolloutupdatestovarious
programmabledevicesinanAOS-CXnetworkswitch,aftertheproducthasshipped.ISPisintendedtorun
automaticallyeitheratboottimeorasnewmodulesareinsertedintothechassisatruntime.
| Show tech | command | list for | the ISP | feature |
| --------- | ------- | -------- | ------- | ------- |
| Task      |         |          |         | Command |
show tech isp
Displayingversionsofallpresentprogrammabledevices.
show tech update-log
DisplayingstoredlogfilesfromanyISPupdatesonthesystem.
SeetheCommand-LineInterfaceGuideforadditionalinformationabouttheshow techcommands.
| In-System | Programming | commands |     |     |
| --------- | ----------- | -------- | --- | --- |
clear update-log
clear update-log
Description
ClearsstoredlogfilesofanyIn-SystemProgrammingupdatesonthesystem.
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show needed-updates |            |                      |     |     |
| ------------------- | ---------- | -------------------- | --- | --- |
| show needed-updates | [next-boot | [primary|secondary]] |     |     |
Description
Displayswhetheranyprogrammabledevicesareinneedofanupdate.
123
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- |

Withoutthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetothecurrentlyrunning
AOS-CXimage.
Withthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetoanAOS-CXimagefilein
thepersistentstorageoftheswitch,whichmightbedifferentfromthecurrentlyrunningimage.Ifeitherthe
primaryorsecondaryparameterisspecified,thiscommandqueriesthatspecificAOS-CXimagefile.
Otherwise,itqueriesthedefaultAOS-CXimagefileassetbythemostrecentboot systemorboot set-
defaultcommand.
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
In-SystemProgramming|124

Chapter 15

Selftest

Selftest

Diagnostics involve four important sub-categories.

n Boot-up Diagnostics (Power On Selftest aka POST)

n Run-time Diagnostics (Hardware Health Monitoring)

n Online Diagnostics

n Offline Diagnostics

Power On Self Test (POST) is the first task which verifies the hardware functionality of various modules
during boot-up. Based on the criticality of the test, the selftest module decides whether to go ahead with the
boot-up sequence of a particular subsystem or interface during a POST failure.

POST comprises of the following:

n Memory BISTs (Built-in Self Test)

This is to verify the memory block(s) present in the module and involves both internal and external
memories.

The memory tables are critical for proper functionality of the system, so any failures in these tests will
result in the corresponding subsystem to be marked as "Failed" and thus that subsystem will not be
available for use.

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

When fastboot is enabled, most tests under a Power On Self Test (POST) are skipped. By default, fastboot is
enabled.

After disabling fastboot, save switch configurations and then reboot for POST to run. POST verifies the
hardware functionality of various modules during boot-up. Based on the criticality of the test, the selftest
module decides whether to go ahead with the boot-up sequence of a particular subsystem or interface
during a POST failure.

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

125

POSTrunsmemorybuilt-inselftest(BISTs)andfront-endportloopbacktests.MemoryBISTsverifythe
internalandexternalmemoryblockspresentinthemodule.Thememorytablesarecriticalforproper
functionalityofthesystemsoanyfailuresinthesetestsresultsinthecorrespondingsubsystemtobe
markedas"Failed"andthusthatsubsystemisnotavailableforuse.
Front-endportloopbacktestsverifythephysicalportfront-endinterface.Thesetestscheckifaparticular
interfacecanfunctionproperly.Atestfailuremeansthataparticularinterfacehasbeenmarkedas"Failed"
andisnowunavailableforuse.
On6300and6400switches,theline-moduleandfabric-moduleselftestisrunregardlessoffastboot
setting.Theinterfaceselftestisonlyrunwhenfastbootisdisabled.
Examples
Enablingfastboot:
| switch#         | configure terminal  |     |
| --------------- | ------------------- | --- |
| switch(config)# | fastboot            |     |
| switch(config)# | end                 |     |
| switch#         | show running-config |     |
| Current         | configuration:      |     |
!
| !Version   | ArubaOS-CX FL.10.06.0001 |        |
| ---------- | ------------------------ | ------ |
| module 1/1 | product-number           | jl661a |
!
!
!
!
!
!
!
vlan 1
| interface | 1/1/1 |     |
| --------- | ----- | --- |
no shutdown
Disablingfastboot:
| switch#         | configure terminal |     |
| --------------- | ------------------ | --- |
| switch(config)# | no fastboot        |     |
| switch(config)# | end                |     |
| switch(config)# | write mem          |     |
Configuration changes will take time to process, please be patient.
| switch# | show running-config |     |
| ------- | ------------------- | --- |
| Current | configuration:      |     |
!
| !Version   | ArubaOS-CX FL.10.06.0001 |        |
| ---------- | ------------------------ | ------ |
| module 1/1 | product-number           | jl661a |
!
!
!
no fastboot
!
!
!
!
vlan 1
| interface | 1/1/1 |     |
| --------- | ----- | --- |
no shutdown
CommandHistory
Selftest|126

| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show selftest |             |              |            |         |            |
| ------------- | ----------- | ------------ | ---------- | ------- | ---------- |
| show selftest | [brief]     | [vsx-peer]   |            |         |            |
| show selftest | line-module | <SLOT-ID>    |            |         |            |
| show selftest | line-module | <SLOT-ID>    | interface  | [brief] | [vsx-peer] |
| show selftest | interface   | [<PORT-NUM>] | [vsx-peer] |         |            |
For8400and6400switchesonly:
show selftest {line-module | fabric-module} [<SLOT-ID>] [brief] [vsx-peer]
Description
Displaysselftestresults.
| Parameter   |     |     | Description                                         |     |     |
| ----------- | --- | --- | --------------------------------------------------- | --- | --- |
| [brief]     |     |     | Showstheselftestresultsasabriefdescription.Default. |     |     |
| line-module |     |     | Showstheselftestresultsforalinemodule.              |     |     |
fabric-module Showstheselftestresultsforafabricmodule.Applicableonlyfor
8400and6400switches.
<SLOT-ID>
ShowstheselftestresultsfortheslotIDofthelineorfabric
module.
| <PORT-NUM> |     |     | Showstheselftestresultsfortheportnumber. |     |     |
| ---------- | --- | --- | ---------------------------------------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Displayingtheoutputwhenfastbootisdisabledonan8400ora6400switch:
| switch#    | show selftest       |             |            |                     |          |
| ---------- | ------------------- | ----------- | ---------- | ------------------- | -------- |
| Name       | Id Status           |             | ErrorCode  | LastRunTime         |          |
| ---------- | ---- -------------- |             | ---------- | ------------------- |          |
| LineModule | 1/1 passed          |             | 0x0        | 2016-10-15          | 10:10:09 |
| LineModule | 1/2 failed          |             | 0x09       | 2016-10-15          | 10:10:56 |
| Fabric     | 1/1 passed          |             | 0x0        | 2016-10-15          | 10:10:09 |
| Fabric     | 1/2 failed          |             | 0x1E       | 2016-10-15          | 10:10:56 |
| switch#    | show selftest       | line-module |            |                     |          |
127
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ----------------------- | --- | --- |

| Name       | Id       | Status         |               | ErrorCode |     | LastRunTime         |          |
| ---------- | -------- | -------------- | ------------- | --------- | --- | ------------------- | -------- |
| ---------- | ----     | -------------- |               | --------- |     | ------------------- |          |
| LineModule | 1/1      | passed         |               | 0x0       |     | 2016-10-15          | 10:10:09 |
| LineModule | 1/2      | failed         |               | 0x09      |     | 2016-10-15          | 10:10:56 |
| switch#    | show     | selftest       | fabric-module |           |     |                     |          |
| Name       | Id       | Status         |               | ErrorCode |     | LastRunTime         |          |
| ------     | -------- | -------------- |               | --------- |     | ------------------- |          |
| Fabric     | 1/1      | passed         |               | 0x0       |     | 2016-10-15          | 10:10:09 |
| Fabric     | 1/2      | failed         |               | 0x1E      |     | 2016-10-15          | 10:10:56 |
switch#
|            | show     | selftest       | fabric-module |           | 1/2  |                     |          |
| ---------- | -------- | -------------- | ------------- | --------- | ---- | ------------------- | -------- |
| Name       | Id       | Status         |               | ErrorCode |      | LastRunTime         |          |
| ------     | -------- | -------------- |               | --------- |      | ------------------- |          |
| Fabric     | 1/2      | failed         |               | 0x11      |      | 2016-10-15          | 10:10:56 |
| switch#    | show     | selftest       | line-module   |           | 1/10 |                     |          |
| Name       | Id       | Status         |               | ErrorCode |      | LastRunTime         |          |
| ---------- | ----     | -------------- |               | --------- |      | ------------------- |          |
| LineModule | 1/10     | failed         |               | 0x1A      |      | 2016-10-15          | 10:10:56 |
switch#
|         | show           | selftest | interface   | 1/2/2 |                     |          |     |
| ------- | -------------- | -------- | ----------- | ----- | ------------------- | -------- | --- |
| Name    | Status         |          | ErrorCode   |       | LastRunTime         |          |     |
| ------- | -------------- |          | ---------   |       | ------------------- |          |     |
| 1/2/2   | passed         |          | 0x0         |       | 2016-11-19          | 05:10:11 |     |
| switch# | show           | selftest | line-module |       | 1/3 interface       |          |     |
| Name    | Status         |          | ErrorCode   |       | LastRunTime         |          |     |
| ------- | -------------- |          | ---------   |       | ------------------- |          |     |
| 1/3/1   | passed         |          | 0x0         |       | 2016-11-19          | 05:10:11 |     |
| 1/3/2   | passed         |          | 0x0         |       | 2016-11-19          | 05:10:11 |     |
| 1/3/3   | passed         |          | 0x0         |       | 2016-11-19          | 05:10:11 |     |
| 1/3/31  | failed         |          | 0x20        |       | 2016-11-19          | 05:10:11 |     |
Displayingtheoutputwhenfastbootisdisabledona6300switch:
| switch# | show   | selftest | interface |           |     |             |     |
| ------- | ------ | -------- | --------- | --------- | --- | ----------- | --- |
| Name    | Status |          |           | ErrorCode |     | LastRunTime |     |
---------- ----------------- ---------------- -------------------
| 1/1/2   | skipped |          |           | 0x0       |     |             |     |
| ------- | ------- | -------- | --------- | --------- | --- | ----------- | --- |
| 1/1/44  | skipped |          |           | 0x0       |     |             |     |
| 1/1/46  | skipped |          |           | 0x0       |     |             |     |
| switch# | show    | selftest | interface | 1/1/1     |     |             |     |
| Name    | Status  |          |           | ErrorCode |     | LastRunTime |     |
---------- ----------------- ---------------- -------------------
| 1/1/1 | skipped |     |     | 0x0 |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- | --- |
Selftest|128

Displayingtheoutputwhenfastbootisenabledona6400switch:
| switch#    | show     | selftest       |               |            |                     |     |
| ---------- | -------- | -------------- | ------------- | ---------- | ------------------- | --- |
| Name       | Id       | Status         |               | ErrorCode  | LastRunTime         |     |
| ---------- | ----     | -------------- |               | ---------- | ------------------- |     |
| LineModule | 1/1      | passed         |               | 0x0        |                     |     |
| LineModule | 1/2      | passed         |               | 0x0        |                     |     |
| Fabric     | 1/1      | passed         |               | 0x0        |                     |     |
| Fabric     | 1/2      | passed         |               | 0x0        |                     |     |
| switch#    | show     | selftest       | line-module   |            |                     |     |
| Name       | Id       | Status         |               | ErrorCode  | LastRunTime         |     |
| ---------- | ----     | -------------- |               | ---------  | ------------------- |     |
| LineModule | 1/1      | passed         |               | 0x0        |                     |     |
| LineModule | 1/2      | passed         |               | 0x0        |                     |     |
| switch#    | show     | selftest       | fabric-module |            |                     |     |
| Name       | Id       | Status         |               | ErrorCode  | LastRunTime         |     |
| ---------- | ----     | -------------- |               | ---------- | ------------------- |     |
| Fabric     | 1/1      | passed         |               | 0x0        |                     |     |
| Fabric     | 1/2      | passed         |               | 0x0        |                     |     |
| switch#    | show     | selftest       | fabric-module | 1/2        |                     |     |
| Name       | Id       | Status         |               | ErrorCode  | LastRunTime         |     |
| ------     | -------- | -------------- |               | ---------  | ------------------- |     |
| Fabric     | 1/2      | passed         |               | 0x0        |                     |     |
| switch#    | show     | selftest       | line-module   | 1/1        |                     |     |
| Name       | Id       | Status         |               | ErrorCode  | LastRunTime         |     |
| ---------- | ----     | -------------- |               | ---------  | ------------------- |     |
| LineModule | 1/1      | passed         |               | 0x0        |                     |     |
Displayingtheoutputwhenfastbootisenabled:
| switch# | show           | selftest | interface | 1/1/2               |     |     |
| ------- | -------------- | -------- | --------- | ------------------- | --- | --- |
| Name    | Status         |          | ErrorCode | LastRunTime         |     |     |
| ------- | -------------- |          | --------- | ------------------- |     |     |
| 1/1/2   | skipped        |          | 0x0       |                     |     |     |
switch#
|         | show           | selftest | line-module | 1/1                 | interface |     |
| ------- | -------------- | -------- | ----------- | ------------------- | --------- | --- |
| Name    | Status         |          | ErrorCode   | LastRunTime         |           |     |
| ------- | -------------- |          | ---------   | ------------------- |           |     |
| 1/1/1   | skipped        |          | 0x0         |                     |           |     |
| 1/1/2   | skipped        |          | 0x0         |                     |           |     |
| 1/1/3   | skipped        |          | 0x0         |                     |           |     |
| 1/1/31  | skipped        |          | 0x0         |                     |           |     |
Displayingtheoutputwhenfastbootisdisabled:
Testingtoregisterread/write:
Thistestisrunirrespectiveoffastbootbeingenabledordisabled.
| switch#    | show | selftest       |     |            |                     |          |
| ---------- | ---- | -------------- | --- | ---------- | ------------------- | -------- |
| Name       | Id   | Status         |     | ErrorCode  | LastRunTime         |          |
| ---------- | ---- | -------------- |     | ---------- | ------------------- |          |
| LineModule | 1/1  | passed         |     | 0x0        | 2018-02-16          | 18:15:53 |
129
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Selftest|130

Chapter 16
Zeroization
Zeroization
Devicezeroizationletsyouremovealluserfilesfromflashstorage,includingsolid-statedrives(SSDs).User
filescannotberetrievedafterthezeroizationiscomplete.
ZeroizationcanoccurinbothAOS-CXandServiceOS.ThissectioncoverszeroizationandAOS-CX.Forinformation
aboutzeroizationandSupportOS,seeerasezeroize.
ZeroizationpreservestheprimaryandsecondarysoftwareimagesontheSSD.Zeroizationalsopreserves
manufacturinginformation.
Thesensitiveuserfilesstoredonan SSDorSPIflash/EEPROMstorageorbothinclude:
Switchconfigurations.
n
n Systemgeneratedprivatekeys.
n Userinstalledprivatekeys.
n Admin/operatorpasswordfiles.
Formoreinformationonpasswordrequirements,seePasswordrequirementsintheSecurityGuide.
| Zeroization | commands |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- |
| erase all   | zeroize  |     |     |     |     |     |
erase all zeroize
Description
Restorestheswitchtoitsfactorydefaultconfiguration.Youwillbepromptedbeforetheprocedurestarts.
Oncecomplete,theswitchwillrestartfromtheprimaryimagewithfactorydefaultsettings.
Backupalldatabeforerunningthiscommandasallconfigurationsettingswillbelost.
Example
Restoringtheswitchtofactorydefaultconfiguration:
| switch#     | erase all   | zeroize |         |              |              |                  |
| ----------- | ----------- | ------- | ------- | ------------ | ------------ | ---------------- |
| This will   | securely    | erase   | all     | customer     | data and     | reset the switch |
| to factory  | defaults.   | This    | will    | initiate     | a reboot     | and render the   |
| switch      | unavailable | until   | the     | zeroization  | is complete. |                  |
| This should | take        | several | minutes | to           | one hour     | to complete.     |
| Continue    | (y/n)?      | y       |         |              |              |                  |
| The system  | is going    | down    | for     | zeroization. |              |                  |
...
131
AOS-CX10.08DiagnosticsandSupportabilityGuide| (6300,6400SwitchSeries)

| ################ |     | Preparing |        | for         | zeroization                 |                         | ################# |            |
| ---------------- | --- | --------- | ------ | ----------- | --------------------------- | ----------------------- | ----------------- | ---------- |
| ################ |     | Storage   |        | zeroization |                             | ####################### |                   |            |
| ################ |     | WARNING:  |        | DO NOT      | POWER                       | OFF                     | UNTIL             | ########## |
| ################ |     |           |        | ZEROIZATION |                             | IS                      | COMPLETE          | ########## |
| ################ |     | This      | should | take        | several                     |                         | minutes           | ########## |
| ################ |     | to        | one    | hour to     | complete                    |                         |                   | ########## |
| ################ |     | Restoring |        | files       | ########################### |                         |                   |            |
...
| We'd like  | to keep | you           | up      | to date | about: |     |     |     |
| ---------- | ------- | ------------- | ------- | ------- | ------ | --- | --- | --- |
| * Software | feature |               | updates |         |        |     |     |     |
| * New      | product | announcements |         |         |        |     |     |     |
| * Special  | events  |               |         |         |        |     |     |     |
Please register your products now at: https://asp.arubanetworks.com
| switch | login: | admin |     |     |     |     |     |     |
| ------ | ------ | ----- | --- | --- | --- | --- | --- | --- |
Password:
| Please    | configure     | the | 'admin' | user | account |     | password. |     |
| --------- | ------------- | --- | ------- | ---- | ------- | --- | --------- | --- |
| Enter new | password:     |     | *****   |      |         |     |           |     |
| Confirm   | new password: |     | *****   |      |         |     |           |     |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Zeroization|132

Chapter 17
Terminal Monitor
| Terminal | Monitor |     |     |     |
| -------- | ------- | --- | --- | --- |
TheterminalmonitorisusedtodisplayselectivelogsdynamicallyontheVTYSHsession.Whentheterminal
monitorfeatureisenabledontheswitch,itdisplaysonlytheliveoractivelogs.Theselogsaredisplayedon
theSSHsessionorconsolesession.Ifrequired,youcanenabletheterminalmonitoringonmultiplesessions.
Itisimportanttomonitorthelogsdynamicallywhiledebugging,sothatyoucanco-relatetheissues.The
logscanbefilteredbytype(eventordebug),severity,orkeyword.Theterminalmonitorrunsin
synchronousmode,wheretheuserentersanycommand,thelogdisplaypausesuntilthecommand
executioniscomplete.ThisensuresthatthelogswillnotappearinbetweenotherCLIoutputsorwhilethe
useristyping.
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
Enablestheloggingconsolefeatureintheconsolesession.Itdisplayalldebuglogoreventlogorbothdebug
andeventlogmessages.Monitoringcanbefilteredwiththeseverityoptionsorwiththehelpofkeywords.
Enablingterminalmonitorwithoutoptionsdisplaysbothdebugandeventlogwithaseverityerror.This
commandispersistentacrossreboot.
Thenoformofthiscommanddisablestheterminalmonitorconfiguration.
| Parameter |                   |     | Description                        |     |
| --------- | ----------------- | --- | ---------------------------------- | --- |
| notify    | <event|debug|all> |     | Specifiesthetypeoflognotification. |     |
Event:Displaystheeventlogmessages.(Default)
n
|     |     |     | n Debug:Displaysthedebuglogmessages. |     |
| --- | --- | --- | ------------------------------------ | --- |
All:Displaysbotheventanddebuglogmessages.
n
severity <level> Specifiestheseveritylevelforthelogs.Thedifferentseverity
levelsareemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
| filter | <keyword> |     |     |     |
| ------ | --------- | --- | --- | --- |
Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
133
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ----------------------- | --- |

Examples
Configuringconsoleloggingintheconsolesession:
switch(config)#
|                  |     | logging    | console      |              |               |
| ---------------- | --- | ---------- | ------------ | ------------ | ------------- |
| Terminal-monitor |     | is enabled | successfully |              |               |
| switch(config)#  |     | logging    | console      | notify all   |               |
| Terminal-monitor |     | is enabled | successfully |              |               |
| switch(config)#  |     | logging    | console      | notify event | severity info |
| Terminal-monitor |     | is enabled | successfully |              |               |
| switch(config)#  |     | logging    | console      | filter lldp  |               |
| Terminal-monitor |     | is enabled | successfully |              |               |
CommandHistory
| Release |     |     |     | Modification       |     |
| ------- | --- | --- | --- | ------------------ | --- |
| 10.08   |     |     |     | Featureintroduced. |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show terminal-monitor
show terminal-monitor
Description
Showswhethertheterminalmonitoringisenabledordisabled.
Thiscommandwillnotshowanyinformationaboutconsolelogging.
Examples
Displayingterminalmonitorwhenenabled:
| switch#          | show | terminal-monitor |     |     |     |
| ---------------- | ---- | ---------------- | --- | --- | --- |
| Terminal-monitor |      | is enabled       |     |     |     |
-------------------------------------
| Notify | |   | Severity | | Filter |     |     |
| ------ | --- | -------- | -------- | --- | --- |
-------------------------------------
| event |     | debug | lldp |     |     |
| ----- | --- | ----- | ---- | --- | --- |
-------------------------------------
Displayingterminalmonitorwhendisabled:
TerminalMonitor|134

| switch#          | show terminal-monitor |     |     |
| ---------------- | --------------------- | --- | --- |
| Terminal-monitor | is disabled           |     |     |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| terminal-monitor | {notify | | severity | | filter} |
| ---------------- | ------- | ---------- | --------- |
terminal-monitor {notify <event|debug|all> | severity <level> | filter <keyword>}
no terminal-monitor
Description
Enablesandsavestheterminalmonitorfeatureintheswitchconfiguration.Itdisplaysalldebuglogorevent
logorbothdebugandeventlogmessages.Terminalmonitoringcanbefilteredwiththeseverityoptionsor
withthehelpofkeywords.Enablingterminalmonitorwithoutoptionsdisplaysbothdebugandeventlog
withaseverityerror.
Thenoformofthiscommandremovestheterminalmonitorfeaturefromtheswitchconfigurationandthe
commandwillnotpersist.
| Parameter                |     | Description                        |     |
| ------------------------ | --- | ---------------------------------- | --- |
| notify <event|debug|all> |     | Specifiesthetypeoflognotification. |     |
n Event:Displaystheeventlogmessages.(Default)
Debug:Displaysthedebuglogmessages.
n
n All:Displaysbotheventanddebuglogmessages.
| severity <level> |     |     |     |
| ---------------- | --- | --- | --- |
Specifiestheseveritylevelforthelogs.Thedifferentseverity
levelsareemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
filter <keyword> Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingterminalmonitor:
135
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |
| --------------------------------------------- | --- | ----------------------- | --- |

| switch#          | terminal-monitor |              |                     |
| ---------------- | ---------------- | ------------ | ------------------- |
| Terminal-monitor | is enabled       | successfully |                     |
| switch#          | terminal-monitor | notify       | all                 |
| Terminal-monitor | is enabled       | successfully |                     |
| switch#          | terminal-monitor | notify       | event severity info |
| Terminal-monitor | is enabled       | successfully |                     |
| switch#          | terminal-monitor | filter       | lldp                |
| Terminal-monitor | is enabled       | successfully |                     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
TerminalMonitor|136

Chapter 18
|                 |     | Troubleshooting |               | Web | UI and REST   | API |
| --------------- | --- | --------------- | ------------- | --- | ------------- | --- |
|                 |     |                 |               |     | Access Issues |     |
| Troubleshooting | Web | UI and REST API | Access Issues |     |               |     |
Thefollowingsectiondescribessymptoms,causesandcorrectiveactionsfor401or404errors.
| HTTP 404 | error when | accessing | the | switch | URL |     |
| -------- | ---------- | --------- | --- | ------ | --- | --- |
Symptom
TheswitchisoperationalandyouareusingthecorrectURLfortheswitch,butattemptstoaccesstheREST
APIorWebUIresultinanHTTP404"Pagenotfound"error.
Cause
RESTAPIaccessisnotenabledontheVRFthatcorrespondstotheaccessportyouareusing.Forexample,
youareattemptingtoaccesstheRESTAPIorWebUIfromthemanagement(OOBM)port,andaccessisnot
enabledonthemgmtVRF.Bydefault,https-serverisenabledonthemgmtVRFforthe6300and6400
switches.
Action
Usethehttps-server vrfcommandtoenableRESTAPIaccessonthespecifiedVRF.
Forexample:
| switch(config)# | https-server | vrf mgmt |         |       |          |     |
| --------------- | ------------ | -------- | ------- | ----- | -------- | --- |
| HTTP 401        | error "Login | failed:  | session | limit | reached" |     |
Symptom
ARESTrequestorWebUIloginattemptreturnsresponsecode401andtheresponsebodycontainsthe
followingtextstring:
| Login failed: | session limit | reached |     |     |     |     |
| ------------- | ------------- | ------- | --- | --- | --- | --- |
Cause
AuserattemptedtologintotheRESTAPIortheWebUI,butthatuseralreadyhasthemaximumnumberof
concurrentsessionsrunning.
Action
1. Logoutfromoneoftheexistingsessions.
Browsersshareasinglesessioncookieacrossmultipletabsorevenwindows.However,scriptsthat
POSTtotheloginresourceandlaterdonotPOSTtothelogoutresourcecaneasilycreatethe
maximumnumberofconcurrentsessions.
2. Ifthesessioncookieislostanditisnotpossibletologoutofthesession,thenwaitforthesessionidle
timelimittoexpire.
137
| AOS-CX10.08DiagnosticsandSupportabilityGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- |

When the session idle timeout expires, the session is terminated automatically.

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions, Web UI sessions, and real-time notification subscriptions.

Troubleshooting Web UI and REST API Access Issues | 138

Support and Other Resources

Chapter 19

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

AOS-CX 10.08 Diagnostics and Supportability Guide | (6300, 6400 Switch Series)

139

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

Support and Other Resources | 140