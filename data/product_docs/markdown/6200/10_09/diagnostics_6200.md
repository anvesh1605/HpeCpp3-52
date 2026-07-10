AOS-CX 10.09 Diagnostics and
Supportability Guide

6200 Switch Series

Published: February 2022
Edition: 2

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
| Contents                            |                                                    |              |          | 3   |
| ----------------------------------- | -------------------------------------------------- | ------------ | -------- | --- |
| About                               | this document                                      |              |          | 7   |
| Applicableproducts                  |                                                    |              |          | 7   |
| Latestversionavailableonline        |                                                    |              |          | 7   |
| Commandsyntaxnotationconventions    |                                                    |              |          | 7   |
| Abouttheexamples                    |                                                    |              |          | 8   |
| Identifyingswitchportsandinterfaces |                                                    |              |          | 8   |
| Debug                               | logging                                            |              |          | 10  |
| Debugloggingcommands                |                                                    |              |          | 10  |
|                                     | cleardebugbuffer                                   |              |          | 10  |
|                                     | debug{all|<MODULE-NAME>}                           |              |          | 11  |
|                                     | debugdb                                            |              |          | 12  |
|                                     | debugdestination                                   |              |          | 14  |
|                                     | showdebug                                          |              |          | 16  |
|                                     | showdebugbuffer                                    |              |          | 16  |
|                                     | showdebugbuffervsf                                 |              |          | 18  |
|                                     | showdebugdestination                               |              |          | 18  |
| Log Rotation                        |                                                    |              |          | 20  |
| Logfilepaths                        |                                                    |              |          | 20  |
| Aboutrotatedlogfiles                |                                                    |              |          | 20  |
| Logrotationtroubleshooting          |                                                    |              |          | 20  |
|                                     | Logfilesnottransferredremotely                     |              |          | 20  |
|                                     | Logrotationnotoccurringimmediatelyaftermaxfilesize |              |          | 21  |
|                                     | Logrotationnotoccurringregardlessofperiod          |              |          | 21  |
| Logrotationcommands                 |                                                    |              |          | 21  |
|                                     | loggingthreshold                                   |              |          | 21  |
|                                     | logrotatemaxsize                                   |              |          | 23  |
|                                     | logrotateperiod                                    |              |          | 24  |
|                                     | logrotatetarget                                    |              |          | 24  |
|                                     | showlogrotate                                      |              |          | 26  |
| Switch                              | system                                             | and hardware | commands | 27  |
| Reboot                              | reasons                                            |              |          | 28  |
| Event                               | Logs                                               |              |          | 30  |
| Showingandclearingevents            |                                                    |              |          | 30  |
| Cable                               | Diagnostics                                        |              |          | 31  |
| HowTDRworksonAOS-CXplatforms        |                                                    |              |          | 31  |
| Cablediagnosticstests               |                                                    |              |          | 31  |
| Cablediagnosticcommands             |                                                    |              |          | 32  |
|                                     | diagcable-diagnostic                               |              |          | 32  |
3
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Supportability             |                                    | Copy | 34  |
| -------------------------- | ---------------------------------- | ---- | --- |
| Supportabilitycopycommands |                                    |      | 34  |
|                            | copycheckpoint                     |      | 34  |
|                            | copycommand-output                 |      | 35  |
|                            | copycore-dump[<MEMBER/SLOT>]daemon |      | 36  |
|                            | copycore-dump[<MEMBER/SLOT>]kernel |      | 37  |
|                            | copycore-dumpvsfmemberdaemon       |      | 38  |
|                            | copycore-dumpvsfmemberkernel       |      | 40  |
|                            | copydiag-dumpfeature<FEATURE>      |      | 41  |
|                            | copydiag-dumplocal-file            |      | 42  |
|                            | copydiag-dumpvsfmemberlocal-file   |      | 43  |
|                            | copy<IMAGE>                        |      | 44  |
|                            | copyrunning-config                 |      | 45  |
|                            | copyshow-techfeature               |      | 46  |
|                            | copyshow-techlocal-file            |      | 47  |
|                            | copyshow-techvsfmemberlocal-file   |      | 48  |
|                            | copystartup-config                 |      | 50  |
|                            | copysupport-files                  |      | 51  |
|                            | copysupport-fileslocal-file        |      | 52  |
|                            | copysupport-filesvsfmember         |      | 53  |
|                            | copysupport-log                    |      | 55  |
|                            | copysupport-logvsfmember           |      | 56  |
| Traceroute                 |                                    |      | 58  |
| Traceroutecommands         |                                    |      | 58  |
|                            | traceroute                         |      | 58  |
|                            | traceroute6                        |      | 60  |
| Ping                       |                                    |      | 63  |
| Pingcommands               |                                    |      | 63  |
|                            | ping                               |      | 63  |
|                            | ping6                              |      | 68  |
| Troubleshooting            |                                    |      | 71  |
|                            | Operationnotpermitted              |      | 71  |
|                            | Networkisunreachable               |      | 71  |
|                            | Destinationhostunreachable         |      | 72  |
| Remote                     | syslog                             |      | 73  |
| Remotesyslogcommands       |                                    |      | 73  |
|                            | logging                            |      | 73  |
|                            | loggingfilter                      |      | 75  |
|                            | loggingfacility                    |      | 78  |
|                            | loggingpersistent-storage          |      | 79  |
| Runtime                    | Diagnostics                        |      | 81  |
| Runtimediagnosticcommands  |                                    |      | 81  |
|                            | diagnosticmonitor                  |      | 81  |
|                            | diagon-demand                      |      | 82  |
|                            | showdiagnostic                     |      | 83  |
|                            | showdiagnosticevents               |      | 83  |
| Service                    | OS                                 |      | 85  |
| ServiceOSCLIlogin          |                                    |      | 85  |
| ServiceOSuseraccounts      |                                    |      | 86  |
| ServiceOSbootmenu          |                                    |      | 86  |
Contents|4

| Consoleconfiguration                |                                          | 87  |
| ----------------------------------- | ---------------------------------------- | --- |
| AOS-CXboot                          |                                          | 87  |
| Filesystemaccess                    |                                          | 88  |
| ServiceOSmountfailure               |                                          | 89  |
| ServiceOSCLIcommandlist             |                                          | 89  |
| ServiceOSCLIfeaturesandlimitations  |                                          | 90  |
| ServiceOSCLIcommands                |                                          | 90  |
|                                     | boot                                     | 90  |
|                                     | cat                                      | 91  |
|                                     | cdpath                                   | 92  |
|                                     | config-clear                             | 92  |
|                                     | cp                                       | 93  |
|                                     | du                                       | 94  |
|                                     | erasezeroize                             | 95  |
|                                     | exit(svos)                               | 96  |
|                                     | format                                   | 97  |
|                                     | identify                                 | 98  |
|                                     | ip                                       | 98  |
|                                     | ls                                       | 99  |
|                                     | md5sum                                   | 101 |
|                                     | mkdir                                    | 101 |
|                                     | mount                                    | 102 |
|                                     | mv                                       | 103 |
|                                     | password(svos)                           | 104 |
|                                     | ping(svos)                               | 104 |
|                                     | pwd                                      | 105 |
|                                     | reboot                                   | 105 |
|                                     | rm                                       | 106 |
|                                     | rmdir                                    | 107 |
|                                     | secure-mode                              | 107 |
|                                     | sh                                       | 109 |
|                                     | umount                                   | 109 |
|                                     | update                                   | 110 |
|                                     | tftp                                     | 111 |
|                                     | version(ServiceOS)                       | 112 |
| In-System                           | Programming                              | 114 |
| ShowtechcommandlistfortheISPfeature |                                          | 114 |
| In-SystemProgrammingcommands        |                                          | 114 |
|                                     | clearupdate-log                          | 114 |
|                                     | showneeded-updates                       | 114 |
| Selftest                            |                                          | 116 |
| Selftestcommands                    |                                          | 116 |
|                                     | fastboot                                 | 116 |
|                                     | showselftest                             | 117 |
| Zeroization                         |                                          | 120 |
| Zeroizationcommands                 |                                          | 120 |
|                                     | eraseallzeroize                          | 120 |
| Terminal                            | Monitor                                  | 122 |
| Terminalmonitorcommands             |                                          | 122 |
|                                     | loggingconsole{notify|severity|filter}   | 122 |
|                                     | showterminal-monitor                     | 123 |
|                                     | terminal-monitor{notify|severity|filter} | 124 |
5
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Troubleshooting                               |                    | Web       | UI and REST | API Access | Issues | 126 |
| --------------------------------------------- | ------------------ | --------- | ----------- | ---------- | ------ | --- |
| HTTP404errorwhenaccessingtheswitchURL         |                    |           |             |            |        | 126 |
| HTTP401error"Loginfailed:sessionlimitreached" |                    |           |             |            |        | 126 |
| Support                                       | and Other          | Resources |             |            |        | 128 |
| AccessingArubaSupport                         |                    |           |             |            |        | 128 |
| AccessingUpdates                              |                    |           |             |            |        | 129 |
|                                               | ArubaSupportPortal |           |             |            |        | 129 |
|                                               | MyNetworking       |           |             |            |        | 129 |
| WarrantyInformation                           |                    |           |             |            |        | 129 |
| RegulatoryInformation                         |                    |           |             |            |        | 129 |
| DocumentationFeedback                         |                    |           |             |            |        | 130 |
Contents|6

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedforadministrators
responsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A)
n
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Itemsthat
appearliketheexampletextinthepreviouscolumnaretobeenteredexactly
asshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
n <example-text> substitutewithanactualvalueinacommandorincode:
<example-text>
n
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variablesare |     |
| --- | --- | --------------------------------------------------------------- | --- |
n example-text
enclosedinanglebrackets(< >).Substitutethetext—includingthe
n example-text
enclosinganglebrackets—withanactualvalue.
Foroutputformatswhereitalictextcanbedisplayed,variablesmight
n
ormightnotbeenclosedinanglebrackets.Substitutethetext
includingtheenclosinganglebrackets,ifany,withanactualvalue.
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
7
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
format:
member/slot/port

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

About this document | 8

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

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
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

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
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

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
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |
| --------------------------------------------- | --- | --- | ------------------ |

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

| switch# | debug destination |     | syslog  | severity | alert   |     |     |
| ------- | ----------------- | --- | ------- | -------- | ------- | --- | --- |
| switch# | debug destination |     | console | severity | info    |     |     |
| switch# | debug destination |     | file    | severity | warning |     |     |
| switch# | debug destination |     | buffer  | severity | err     |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show debug
show debug
Description
Displaystheenableddebugtypes.
Examples
| switch# | show debug |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------------
| module sub_module |     | severity | vlan | port | ip  | mac | instance vrf |
| ----------------- | --- | -------- | ---- | ---- | --- | --- | ------------ |
------------------------------------------------------------------------------------
| all | all | err | 1   | 1/1/1 | 10.0.0.1 | 1a:2b:3c:4d:5e:6f | 2 default |
| --- | --- | --- | --- | ----- | -------- | ----------------- | --------- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show debug | buffer |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- |
16
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

| show debug | buffer [module | <MODULE-NAME> | | severity |
| ---------- | -------------- | ------------- | ---------- |
(emer|crit|alert|err|notice|warning|info|debug)]
Description
Displaysdebuglogsstoredinthespecifieddebugbufferwithoptionalfilteringbymoduleorseverity.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MODULE-NAME> Filtersdebuglogsdisplayedbythespecifiedmodulename.
severity (emer|crit|alert|err| Displaysdebuglogswithaspecifiedseveritylevel.Defaults
| notice|warning|info|debug) |     |     | todebug.Optional.                                   |
| -------------------------- | --- | --- | --------------------------------------------------- |
| emer                       |     |     | Displaysdebuglogswithaseveritylevelofemergencyonly. |
crit
Displaysdebuglogswithaseveritylevelofcriticalandabove.
alert
Displaysdebuglogswithaseveritylevelofalertandabove.
| err |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |
| --- | --- | --- | ------------------------------------------------------ |
above.
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning Displaysdebuglogswithaseveritylevelofwarningandabove.
| info |     |     | Displaysdebuglogswithaseveritylevelofinfoandabove. |
| ---- | --- | --- | -------------------------------------------------- |
debug
Displaysdebuglogswithaseveritylevelofdebug(default).
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
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
Debuglogging|17

| show debug | buffer | vsf |     |
| ---------- | ------ | --- | --- |
show debug buffer vsf [member <MEMBER-ID>] [{conductor | standby}]
Description
DisplaysVSFmemberdebuglogsstoredinthedebugbuffer,withanoptiontofilterbyVSFmemberand
role.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MEMBER-ID> Displaysdebuglogsforthespecifiedmember-id.Optional.Range:
1-8.
| conductor |     |     | DisplaydebuglogsfortheVSFconductor. |
| --------- | --- | --- | ----------------------------------- |
| standby   |     |     | DisplaydebuglogsfortheVSFstandby.   |
Examples
DisplayingVSFmemberdebuglogswithmember-id1:
| switch# | show debug buffer | vsf member | 1   |
| ------- | ----------------- | ---------- | --- |
------------------------------------------------------------------------------
| show debug | buffer |     |     |
| ---------- | ------ | --- | --- |
------------------------------------------------------------------------------
2020-12-14:07:53:17.217919|hpe-ledarbd|LOG_DEBUG|MMBR|2|LED|LED|ledarbd_vsf_mbrs_
| check: Checking | VSF_Member | table |     |
| --------------- | ---------- | ----- | --- |
DisplayingVSFmemberdebuglogsformemberstateconductor:
| switch# | show debug buffer | vsf conductor |     |
| ------- | ----------------- | ------------- | --- |
------------------------------------------------------------------------------
| show debug | buffer |     |     |
| ---------- | ------ | --- | --- |
------------------------------------------------------------------------------
2020-12-14:07:54:20.469024|hpe-ledarbd|LOG_DEBUG|CDTR|1|LED|LED|ledarbd_pd_
| subsystems_check: | Checking | Subsystem | table |
| ----------------- | -------- | --------- | ----- |
CommandHistory
| Release        |     |     | Modification                             |
| -------------- | --- | --- | ---------------------------------------- |
| 10.09          |     |     | Updatedparameternameforinclusivelanguage |
| 10.07orearlier |     |     | --                                       |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show debug             | destination |     |     |
| ---------------------- | ----------- | --- | --- |
| show debug destination |             |     |     |
18
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Description
Displaystheconfigureddebugdestinationandseverity.
Examples
| switch# | show debug destination |     |
| ------- | ---------------------- | --- |
---------------------------------------------------------------------
|     | show debug destination |     |
| --- | ---------------------- | --- |
---------------------------------------------------------------------
CONSOLE:info
FILE:warning
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
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

Log file paths
Only logs stored in the following files are rotated:

n Audit logs stored in the /var/log/audit/audit.log file

n Authentication logs stored in the /var/log/auth.log file.

n Event logs stored in the /var/log/event.log file.

n Security logs stored in the /var/log/security.log file.

n Logs of bad login attempts are stored in /var/log/btmp.

n Logs of the last login sessions are stored in /var/log/wtmp.

n NTP logs are stored in /var/log/ntp.log.

About rotated log files
Rotated log files are compressed and stored locally in /var/log/, regardless of the remote host
configuration. Rotated log files are stored with respective time extension to the granularity of hour in the
format file1–YYYYMMDDHH.gz (for example, messages-2015080715.gz). Rotated log files are replaced when
the number of old rotated log files exceeds three. The newly rotated log file replaces the oldest rotated log
file.

TFTP, SFTP, or SCP are used to transfer rotated log files to a remote host. Only newly rotated log files are
transferred to the remote host during the log rotation. Previously rotated log files are not re-transferred.
After a log file is successfully transferred, it is removed from the switch.

Log rotation troubleshooting
Some common log file rotation troubleshooting items are as follows.

Log files not transferred remotely

Symptom

Rotated log files are not transferred to a remote host.

Cause

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

20

n The remote host might not be reachable.

n The TFTP server on the remote host might not have sufficient privileges for file creation.

Action

1. Verify that the remote host is reachable.

2. Ensure that the TFTP server is configured with the required file creation permissions.

3. For example, on the TFTPD-HPA server, change the configuration file in /etc/default/tftpd-hpa to

include -c in TFTP_OPTIONS. (for example, TFTP_OPTIONS="--secure -c.).

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

Log rotation is not happening regardless of the period value.

Cause

Log files are not rotated when they are empty files (the log file size is zero).

Action

Log rotation occurs when the log file size is greater than zero.

Log rotation commands

logging threshold
logging threshold {audit-log | auth-log | event-log | security-log} <THRESHOLD%>
no logging threshold {audit-log | auth-log | event-log | security-log} [<THRESHOLD%>]

Description

Selects the logging buffer notification threshold for the specified logging buffer. Whenever the logging
buffer space consumption exceeds the selected threshold (percent of buffer capacity), a LOG_BUFFER_
ALMOST_FULL event and SNMP RMON trap is triggered. This gives you the opportunity to save the logs
elsewhere before the buffers are rotated with the oldest data being overwritten.

Also, a LOG_BUFFER_WRAPPED event and SNMP RMON trap is triggered if the logging buffer capacity is
fully consumed and the log buffer is rotated with the oldest data being overwritten.

The no form of this command resets the logging buffer warning threshold to its default of 90 (percent).

Log Rotation | 21

| Parameter    |     |     | Description                  |     |
| ------------ | --- | --- | ---------------------------- | --- |
| audit-log    |     |     | Selectstheauditlog.          |     |
| auth-log     |     |     | Selectstheauthenticationlog. |     |
| event-log    |     |     | Selectstheeventlog.          |     |
| security-log |     |     | Selectsthesecuritylog.       |     |
<THRESHOLD%> Selectsthenotificationthresholdasapercentthattheselected
loggingbufferisfull.
Availablepercentvaluesforauth-log,event-log,security
|     |     |     | log:15 30 | 50 70 90 100 |
| --- | --- | --- | --------- | ------------ |
Availablepercentvaluesforaudit-log:50 100
Examples
Settingtheauditlogthreshold:
| switch(config)# | logging | threshold | audit-log | 100 |
| --------------- | ------- | --------- | --------- | --- |
Settingtheauthenticationlogthreshold:
| switch(config)# | logging | threshold | auth-log 50 |     |
| --------------- | ------- | --------- | ----------- | --- |
Settingtheeventlogthreshold:
| switch(config)# | logging | threshold | event-log | 70  |
| --------------- | ------- | --------- | --------- | --- |
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
Resettingthesecuritylogthresholdtoitsdefaultof90:
22
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| switch(config)# | no logging | threshold | security-log |
| --------------- | ---------- | --------- | ------------ |
CommandHistory
| Release |     |     | Modification       |
| ------- | --- | --- | ------------------ |
| 10.09   |     |     | Commandintroduced. |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logrotate         | maxsize    |     |     |
| ----------------- | ---------- | --- | --- |
| logrotate maxsize | <MAX-SIZE> |     |     |
| no logrotate      | maxsize    |     |     |
Description
Specifiesthemaximumallowedlogfilesize.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappensfirst),
triggersrotationofthelogfile.
Thenoformofthiscommandresetsthesizeofthelogfiletothedefault(100MB).
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MAX-SIZE> Specifiestheallowedsizethelogfilecanreachbeforeitis
compressedandstoredlocallyortransferredtoaremotehost.
Range:10to200MB.Default:100MB.
Examples
Settingthemaximumlogfilesize:
| switch(config)# | logrotate | maxsize | 24  |
| --------------- | --------- | ------- | --- |
Resettingthemaximumlogfilesizetoitsdefaultof100MB:
| switch(config)# | no logrotate | maxsize |     |
| --------------- | ------------ | ------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
LogRotation|23

| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logrotate    | period |          |          |         |           |
| ------------ | ------ | -------- | -------- | ------- | --------- |
| logrotate    | period | {daily | | hourly | | monthly | | weekly} |
| no logrotate | period |          |          |         |           |
Description
Setsthelogfilerotationtimeperiod.Defaultstodaily.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappensfirst),
triggersrotationofthelogfile.
Thenoformofthiscommandresetsthelogrotationperiodtothedefaultofdaily.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
daily
Rotateslogfilesonadailybasis(default)at0:01.
| hourly |     |     |     | Rotateslogfileseveryhouratthefirstsecondofthehour. |     |
| ------ | --- | --- | --- | -------------------------------------------------- | --- |
monthly
Rotateslogfilesmonthlyonthefirstdayofthemonthat00:01.
| weekly |     |     |     | RotateslogfilesonceaweekonSundayat00:01. |     |
| ------ | --- | --- | --- | ---------------------------------------- | --- |
Examples
Settingaweeklyperiod:
| switch(config)# |     | logrotate | period | weekly |     |
| --------------- | --- | --------- | ------ | ------ | --- |
Resettingtheperiodtoitsdefaultofdaily:
| switch(config)# |     | no logrotate | period |     |     |
| --------------- | --- | ------------ | ------ | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logrotate | target |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
24
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

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

<VRF_NAME>

Usage

Description

Specifies the URI of the remote host. The default directory is
local.
tftp://{{<IPV4_ADDR>|IPV6_ADDR>}|HOST}
[/<DIRECTORY>]

Specifies the VRF name (Default: default).

n Rotated log files are compressed and stored locally in the path /var/log/ regardless of the remote host

configuration.

n Log storage locations on the switch included in the log rotate are as follows:

o Authentication logs are stored in /var/log/auth.log.

o Event logs are stored in /var/log/audit/audit.log.

o Audit logs are stored in /var/log/event.log.

o Security logs are stored in /var/log/security.log.

o Logs of bad login attempts are stored in /var/log/btmp.

o Logs of the last login sessions are stored in /var/log/wtmp.

o NTP logs are stored in /var/log/ntp.log.

Examples

Setting an IPv4 target:

switch(config)# logrotate target tftp://192.168.1.132

Setting an IPv4 target with a directory:

switch(config)# logrotate target tftp://192.168.1.132/logrotate/

Setting an IPv4 target with the default VRF:

switch(config)# logrotate target tftp://192.168.1.132 vrf mgmt

Setting an IPv6 target with the default VRF:

Log Rotation | 25

switch(config)# logrotate target tftp://2001:db8:0:1::128 vrf default
Resettingthetargettolocal:
| switch(config)# |     | no logrotate | target |     |
| --------------- | --- | ------------ | ------ | --- |
CommandHistory
| Release        |     |     | Modification                 |     |
| -------------- | --- | --- | ---------------------------- | --- |
| 10.09          |     |     | Updatedthesyntaxandexamples. |     |
| 10.07orearlier |     |     | --                           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show logrotate
show logrotate
Description
Showsthelogrotateconfiguration.
Examples
| switch#   | show logrotate |                            |     |          |
| --------- | -------------- | -------------------------- | --- | -------- |
| Logrotate | configurations | :                          |     |          |
| Period    |                | : weekly                   |     |          |
| Maxsize   |                | : 20MB                     |     |          |
| Target    |                | : tftp://2001:db8:0:1::128 |     | vrf mgmt |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
26
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

Chapter 4
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettingson
theswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
27
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- |

Chapter 5

Reboot reasons

Reboot reasons

The show boot-history command displays the following reboot reasons for the management module:

Reboot reasons for management module

Reboots handled through database

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

Redundant Management communication timeout

The standby management module has taken over from an

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

VSF member renumbered

An user requested a renumber of a VSF member.

VSF switchover requested

An user requested a VSF switchover.

Chassis critical temperature

Chassis operating temperature exceeded.

Chassis insufficient fans

Insufficient fans to cool the chassis.

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

28

Parameter

Description

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

Reboot reasons | 29

Chapter 6

Event Logs

Event Logs

Event logging logs events generated by daemons, processes, and plug-ins running within the switch
software. The event logging framework captures the event logs in a system journal by updating the journal
fields and meta data.

Showing and clearing events
The clear events command is used to clear the event log of all events. The show events command is used
to show all event logs generated by the switch since the last reboot. See the Switch system and hardware
commands chapter chapter of the Fundamentals Guide for information on these commands.

The time stamp for event log messages generated from the Service OS indicates when the event log
messages were transferred to the event log after a switch boot and not when the issue occurred.

See the Security Guide for information about accounting logs.

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

30

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
31
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

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
Runningacablediagnostictestoninterfaces:
CableDiagnostics|32

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
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
33
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
34
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

CommandHistory
| Release        |     | Modification      |
| -------------- | --- | ----------------- |
| 10.08          |     | AddedSCP support. |
| 10.07orearlier |     | --                |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy command-output
copy command-output "<COMMAND>" {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}
Description
CopiesthespecifiedcommandoutputusingTFTP,SFTP,SCP,orUSB.
| Parameter |     | Description |
| --------- | --- | ----------- |
<COMMAND> Specifiesthecommandfromwhichyouwanttoobtainitsoutput.
Required.Userswithauditorrightscanspecifythesetwo
commandsonly:
show accounting log
show events
{<STORAGE-URL> | <REMOTE-URL> SelecteitherthestorageURLortheremoteURLforthe
[vrf <VRF-NAME>]} destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     | SpecifiestheUSBtocopycommandoutput. |
| ------------- | --- | ----------------------------------- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | -------------------------------------- |
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://<USER>@}{<IP> | <HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
Copyingtheoutputfromtheshow eventscommandtoaremoteURL:
switch# copy command-output "show events" tftp://10.100.0.12/file
SupportabilityCopy|35

Copyingtheoutputfromtheshow techcommandtoaremoteURLwithaVRFnamedmgmt:
switch# copy command-output "show tech" scp://user@10.100.0.12/file vrf mgmt
Copyingtheoutputfromtheshow eventscommandtoafilenamedeventsonaUSBdrive:
| switch# | copy command-output | "show events" | usb:/events |
| ------- | ------------------- | ------------- | ----------- |
CommandHistory
| Release        |     | Modification      |     |
| -------------- | --- | ----------------- | --- |
| 10.08          |     | AddedSCP support. |     |
| 10.07orearlier |     | --                |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| copy core-dump | [<MEMBER/SLOT>] |     | daemon |
| -------------- | --------------- | --- | ------ |
copy core-dump [<MEMBER/SLOT>] daemon <DAEMON-NAME>[:<INSTANCE-ID>] <REMOTE-URL> [vrf <VRF-
NAME>]
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<MEMBER/SLOT> SpecifiestheslotIDonan8400or6400switch.Required.
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
| <DAEMON-NAME> |     | Specifiesthenameofthedaemon.Required. |     |
| ------------- | --- | ------------------------------------- | --- |
[:<INSTANCE-ID>] Specifiestheinstanceofthedaemoncoredump.Optional.
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
{tftp://}{<IP> | <HOST>}[:<PORT>]
n
[;blocksize=<VAL>]/<FILE>
{sftp://<USER>@}{<IP> | <HOST>}[:<PORT>]/<FILE>
n
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRFnamed
defaultisused.Optional.
Examples
36
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Copyingthecoredumpfromdaemonops-vlandtoaremoteURLwithaVRFnamedmgmt:
switch# copy core-dump daemon ops-vland sftp://abc@10.0.14.211/vland_coredump.xz vrf
mgmt
Copyingthecoredumpfromdaemonops-vlandtoaremoteURLwithaVRFnamedmgmt:
switch# copy core-dump daemon ops-vland scp://abc@10.0.14.211/vland_coredump.xz vrf
mgmt
Copyingthecoredumpfromdaemonops-switchdtoaUSBdrive:
| switch# | copy core-dump | daemon ops-switchd |     | usb:/switchd |
| ------- | -------------- | ------------------ | --- | ------------ |
CopyingthecoredumpwithslotID1/1fromdaemonhpe-sysmondtoaremoteURL:
switch# copy core-dump 1/1 daemon hpe-sysmond sftp://abc@10.0.14.206/core.hpe-
| sysmond.xz | vrf mgmt |     |     |     |
| ---------- | -------- | --- | --- | --- |
Copyingthecoredumpfromthehpe-configprocesstoaUSBdrive:
| switch# | copy core-dump | daemon hpe-config |     | usb:/config_core |
| ------- | -------------- | ----------------- | --- | ---------------- |
CommandHistory
| Release        |     |     | Modification      |     |
| -------------- | --- | --- | ----------------- | --- |
| 10.08          |     |     | AddedSCP support. |     |
| 10.07orearlier |     |     | --                |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy core-dump |     | [<MEMBER/SLOT>] |     | kernel |
| -------------- | --- | --------------- | --- | ------ |
copy core-dump [<MEMBER/SLOT>] kernel <REMOTE-URL> [vrf <VRF-NAME>]
Description
CopiesakernelcoredumpusingTFTP,SFTP,orSCP.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<MEMBER/SLOT> SpecifiestheslotIDonan8400or6400switch.Required.
SupportabilityCopy|37

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
Syntax:Slotnumberforline(1/1-1/4,1/7-1/10)MM(1/5or1/6)
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput.Required. |
| ------------ | --- | --- | ----------------------------------------------- |
Syntax:
{tftp://}{<IP> | <HOST>}[:<PORT>]
n
[;blocksize=<VAL>]/<FILE>
{sftp://<USER>@}{<IP> | <HOST>}[:<PORT>]/<FILE>
n
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthekernelcoredumptotheURL:
switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz
CopyingthekernelcoredumptotheURLwiththeVRFnamedmgmt:
switch# copy core-dump kernel tftp://10.100.0.12/kernel_dump.tar.gz vrf mgmt
CopyingthekernelcoredumpfromslotID1/1totheURLwiththeVRFnamedmgmt:
switch# copy core-dump 1/1 kernel sftp://abc@10.0.14.206/kernel_dump.tar.gz vrf mgmt
CopyingthekernelcoredumpfromslotID1/1totheURLwiththeVRFnamedmgmt:
switch# copy core-dump 1/1 kernel scp://abc@10.0.14.206/kernel_dump.tar.gz vrf mgmt
CommandHistory
| Release        |     |     | Modification      |
| -------------- | --- | --- | ----------------- |
| 10.08          |     |     | AddedSCP support. |
| 10.07orearlier |     |     | --                |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy core-dump |                  | vsf member                     | daemon |
| -------------- | ---------------- | ------------------------------ | ------ |
| copy core-dump | vsf member       | <MEMBER-ID>                    |        |
| daemon         | [<DAEMON-NAME>   | | <DAEMON-NAME>:<INSTANCE-ID>] |        |
| <REMOTE-URL>   | [vrf <VRF-NAME>] |                                |        |
| copy core-dump | vsf member       | <MEMBER-ID>                    |        |
38
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

| daemon [<DAEMON-NAME> |     | | <DAEMON-NAME>:<INSTANCE-ID>] |     |     |     |
| --------------------- | --- | ------------------------------ | --- | --- | --- |
<STORAGE-URL>
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter              |     |     | Description |     |     |
| ---------------------- | --- | --- | ----------- | --- | --- |
| vsf member <MEMBER-ID> |     |     |             |     |     |
Specifiesthemember-idoftheVSFmember.Required.
| <DAEMON-NAME> |     |     | Specifiesthenameofthedaemon.Required. |     |     |
| ------------- | --- | --- | ------------------------------------- | --- | --- |
[:<INSTANCE-ID>]
Specifiestheinstanceofthedaemoncoredump.Optional.
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
|     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --------- |
[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.IfnoVRFnameisprovided,theVRF
nameddefaultisused.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput.Required. |     |     |
| ------------- | --- | --- | -------------------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Examples
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch# copy                     | core-dump | vsf member | 1 daemon hpe-sysmond |     |     |
| -------------------------------- | --------- | ---------- | -------------------- | --- | --- |
| sftp://abc@10.0.14.206/sysmon.xz |           |            | vrf mgmt             |     |     |
Copyingthecoredumpfromdaemonhpe-sysmondtoaremoteURLwithaVRFnamedmgmt:
| switch# copy                     | core-dump | vsf member | 2 daemon hpe-sysmond |     |     |
| -------------------------------- | --------- | ---------- | -------------------- | --- | --- |
| scp://user@10.0.14.206/sysmon.xz |           |            | vrf mgmt             |     |     |
CommandHistory
| Release        |     |     | Modification      |     |     |
| -------------- | --- | --- | ----------------- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |
| 10.07orearlier |     |     | --                |     |     |
CommandInformation
SupportabilityCopy|39

| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy core-dump |     | vsf member | kernel |     |     |
| -------------- | --- | ---------- | ------ | --- | --- |
copy core-dump vsf member <MEMBER-ID> kernel <REMOTE-URL> [vrf <VRF-NAME>]
| copy core-dump | vsf member | <MEMBER-ID> | kernel <STORAGE-URL> |     |     |
| -------------- | ---------- | ----------- | -------------------- | --- | --- |
Description
Copiesthekernelcore-dumpusingTFTP,SFTP,SCP,orUSB.
| Parameter   |     |     | Description                                   |     |     |
| ----------- | --- | --- | --------------------------------------------- | --- | --- |
| <MEMBER-ID> |     |     | Specifiesthemember-idoftheVSFmember.Required. |     |     |
<REMOTE_URL>
SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
|     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | --------- | ------------------- | --------- |
n
[:<PORT>]/<FILE>
vrf <VRF-NAME>
SpecifiestheVRFname.IfnoVRFnameisprovided,theVRFnamed
defaultisused.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput.Required. |     |     |
| ------------- | --- | --- | -------------------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Examples
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel sftp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel scp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
CommandHistory
| Release        |     |     | Modification      |     |     |
| -------------- | --- | --- | ----------------- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |
| 10.07orearlier |     |     | --                |     |     |
CommandInformation
40
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- |

| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy diag-dump | feature | <FEATURE> |     |     |     |
| -------------- | ------- | --------- | --- | --- | --- |
copy diag-dump feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesthespecifieddiagnosticinformationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description                               |     |     |
| --------- | --- | --- | ----------------------------------------- | --- | --- |
| <FEATURE> |     |     | Thenameofafeature,forexampleaaa.Required. |     |     |
{<REMOTE-URL> [vrf <VRF-NAME> |<STORAGE-URL>]} SelecteithertheremoteURLorthestorageURLfor
thedestinationofthecopiedcommandoutput.
Required.
| <REMOTE-URL> |     |     | SpecifiestheremotedestinationURL.Required. |     |     |
| ------------ | --- | --- | ------------------------------------------ | --- | --- |
ThesyntaxoftheURListhefollowing:
Syntax:
|     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
SpecifiestheVRFname.IfnoVRFnameisprovided,
theVRFnameddefaultisused.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Required.
Syntax:{usb}:/<FILE>
Examples
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa tftp://10.100.0.12/diagdump.txt vrf mgmt
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa scp://user@10.100.0.12/diagdump.txt vrf mgmt
CommandHistory
| Release        |     | Modification      |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- |
| 10.08          |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     | --                |     |     |     |
SupportabilityCopy|41

CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
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
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
| vrf | <VRF-NAME> |     |     | SpecifiestheVRFname.ThedefaultVRFnameis |     |     |
| --- | ---------- | --- | --- | --------------------------------------- | --- | --- |
default.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Thecopy local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump local-
filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic | local-file |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | --- |
switch#
|     | copy diag-dump | local-file | tftp://10.100.0.12/diagdump.txt |     |     |     |
| --- | -------------- | ---------- | ------------------------------- | --- | --- | --- |
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic | local-file |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | --- |
switch# copy diag-dump local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaUSBdrive:
42
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- |

| switch# | diag-dump | aaa basic | local-file |     |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | --- | --- |
switch#
|     | copy diag-dump | local-file |     | usb:/diagdump.txt |     |     |     |
| --- | -------------- | ---------- | --- | ----------------- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification      |     |     |     |
| -------------- | --- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy diag-dump |     | vsf member |     | local-file |     |     |     |
| -------------- | --- | ---------- | --- | ---------- | --- | --- | --- |
copy diag-dump vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-
URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,orUSB.
| Parameter  |             |     |     |     | Description                          |     |     |
| ---------- | ----------- | --- | --- | --- | ------------------------------------ | --- | --- |
| vsf member | <MEMBER-ID> |     |     |     | Specifiesthemember-idoftheVSFmember. |     |     |
Required.
{<REMOTE-URL> [vrf <VRF-NAME>] |<STORAGE-URL>} SelecteitherthestorageURLortheremoteURLfor
thedestinationofthecopiedcommandoutput.
Required.
<REMOTE-URL>
SpecifiestheURLtocopythecommandoutput.
Syntax:
|     |     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
| vrf | <VRF-NAME> |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- |
SpecifiestheVRFname.ThedefaultVRFnameis
default.Optional.
| <STORAGE-URL> |     |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Thecopy diag-dump local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump local-
filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
SupportabilityCopy|43

Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
switch#
|     | diag-dump | aaa basic | local-file |     |     |
| --- | --------- | --------- | ---------- | --- | --- |
switch# copy diag-dump vsf member 2 local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic | local-file |     |     |
| ------- | --------- | --------- | ---------- | --- | --- |
switch# copy diag-dump vsf member 2 local-file tftp://10.100.0.12/diagdump.txt
CommandHistory
| Release        |     |     | Modification      |     |     |
| -------------- | --- | --- | ----------------- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |
| 10.07orearlier |     |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy <IMAGE>
copy <IMAGE> {<STORAGE-URL> | <REMOTE-URL>} <FILE-NAME> [vrf <VRF-NAME>]
Description
CopiestheimageusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description        |     |     |
| --------- | --- | --- | ------------------ | --- | --- |
| <IMAGE>   |     |     | Specifiestheimage. |     |     |
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
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --------- |
[:<PORT>]/<FILE>
44
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

| Parameter   |     |     | Description           |     |     |
| ----------- | --- | --- | --------------------- | --- | --- |
| <FILE-NAME> |     |     | Specifiesthefilename. |     |     |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingtheimagetoaremoteURL:
| switch# | copy scp://root@20.0.1.1/primary.swi |     |     | primary | vrf mgmt |
| ------- | ------------------------------------ | --- | --- | ------- | -------- |
CopyingthesecondaryimagetoaremoteURL:
| switch# | copy secondary | scp://root@20.0.1.1/primary.swi |     |     | vrf mgmt |
| ------- | -------------- | ------------------------------- | --- | --- | -------- |
CommandHistory
| Release        |     |     | Modification      |     |     |
| -------------- | --- | --- | ----------------- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |
| 10.07orearlier |     |     | --                |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |     |     |
| ------------ | --- | --- | -------------------------------------- | --- | --- |
Syntax:
|     |     |     | n {tftp://}{<IP> |     | | <HOST>}[:<PORT>] |
| --- | --- | --- | ---------------- | --- | ------------------ |
SupportabilityCopy|45

| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
[;blocksize=<VAL>]/<FILE>
|     |     | {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |     |
| --- | --- | --------- | ------------------- | --------- | --- |
n
[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     | Specifiestherunningconfiguration. |     |     |     |
| -------------------- | --- | --------------------------------- | --- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
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
|     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
46
| AOS-CX10.09DiagnosticsandSupportabilityGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | ------------------ | --- | --- | --- | --- |

| Parameter      |     |     | Description                             |
| -------------- | --- | --- | --------------------------------------- |
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.ThedefaultVRFnameis |
default.Optional.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |
| ------------- | --- | --- | ----------------------------------- |
Required.
Syntax:{usb}:/<FILE>
Example
CopyingshowtechoutputoftheaaafeatureusingSCP:
switch# copy show-tech feature aaa scp://user@10.0.0.12/file.txt vrf mgmt
CopyingshowtechoutputoftheconfigfeatureusingSFTPonthemgmtVRF:
switch# copy show-tech feature config sftp://root@10.0.0.1/tech.txt vrf mgmt
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
| copy show-tech | local-file |     |     |
| -------------- | ---------- | --- | --- |
copy show-tech local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
Copiesshowtechoutputstoredinalocalfile.
| Parameter     |                  |                 | Description |
| ------------- | ---------------- | --------------- | ----------- |
| {<REMOTE-URL> | [vrf <VRF-NAME>] | | <STORAGE-URL> | ]}          |
SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopiedcommand
output.Required.
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | --- | -------------------------------------- |
Syntax:
{tftp://}{<IP> | <HOST>}[:<PORT>]
n
[;blocksize=<VAL>]/<FILE>
SupportabilityCopy|47

| Parameter |     |     |     | Description |                     |     |
| --------- | --- | --- | --- | ----------- | ------------------- | --- |
|           |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
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
CopyingtheoutputtoaremoteURL:
| switch# | copy show-tech | local-file | tftp://10.100.0.12/file.txt |     |     |     |
| ------- | -------------- | ---------- | --------------------------- | --- | --- | --- |
CopyingtheoutputtoaremoteURL:
switch# copy show-tech local-file scp://user@10.100.0.12/file.txt
CopyingtheoutputtoaremoteURLwithaVRF:
switch# copy show-tech local-file tftp://10.100.0.12/file.txt vrf mgmt
CopyingtheoutputtoaUSB:
| switch# | copy show-tech | local-file | usb:/file |     |     |     |
| ------- | -------------- | ---------- | --------- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification      |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy show-tech | vsf | member | local-file |     |     |     |
| -------------- | --- | ------ | ---------- | --- | --- | --- |
48
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- |

copy show-tech vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-
URL>}
Description
Copiesshowtechoutputstoredinalocalfile.
| Parameter  |             |     |     | Description                          |     |     |
| ---------- | ----------- | --- | --- | ------------------------------------ | --- | --- |
| vsf member | <MEMBER-ID> |     |     | Specifiesthemember-idoftheVSFmember. |     |     |
Required.
{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopiedcommand
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
SupportabilityCopy|49

| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
copy startup-config
copy startup-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
{<STORAGE-URL> | <REMOTE-URL>} SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
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
| config <CONFIG-NAME> |     | Specifiesthestartupconfiguration. |     |     |
| -------------------- | --- | --------------------------------- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthestartupconfigurationtoaremoteURL:
switch# copy startup-config scp://root@10.0.1.1/config json vrf mgmt
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
50
| AOS-CX10.09DiagnosticsandSupportabilityGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | ------------------ | --- | --- | --- |

copy support-files
| copy support-files | previous-boot     | <REMOTE-URL>     | [vrf <VRF-NAME>] |     |     |     |
| ------------------ | ----------------- | ---------------- | ---------------- | --- | --- | --- |
| copy support-files | all <REMOTE-URL>  | [vrf             | <VRF-NAME>]      |     |     |     |
| copy support-files | <REMOTE-URL>      | [vrf <VRF-NAME>] |                  |     |     |     |
| copy support-files | feature           | <FEATURE-NAME>   | <STORAGE-URL>    |     |     |     |
| copy support-files | previous-boot     | <STORAGE-URL>    |                  |     |     |     |
| copy support-files | all <STORAGE-URL> |                  |                  |     |     |     |
| copy support-files | <STORAGE-URL>     |                  |                  |     |     |     |
copy support-files vsf member <MEMBER-ID> <REMOTE-URL> {vrf <VRF-NAME>}
| copy support-files | vsf member | <MEMBER-ID> | <STORAGE-URL> |     |     |     |
| ------------------ | ---------- | ----------- | ------------- | --- | --- | --- |
Description
Copiesasetofsupportfilestoacompressedfileintar.gzformatusingTFTP,SFTP,SCP,orUSBortoa
directoryoverSFTPorUSB.
| Parameter      |     |     |     | Description                    |     |     |
| -------------- | --- | --- | --- | ------------------------------ | --- | --- |
| <FEATURE-NAME> |     |     |     | Thefeaturename,forexample,aaa. |     |     |
{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopiedcommand
output.Required.
<REMOTE-URL>
SpecifiestheURLtocopythecommandoutput.
Syntax:
|     |     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | -------------- | ------------------ | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | --------- | ------------------- | --- |
n
<HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME>
SpecifiestheVRFname.ThedefaultVRFname
isdefault.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
| <MEMBER-ID> |     |     |     | ThememberIDintheVSFstack.Range1-10. |     |     |
| ----------- | --- | --- | --- | ----------------------------------- | --- | --- |
Usage
Iffeaturenameisnotprovided,thecommandcollectsgenericsystem-specificsupportinformation.Ifa
featurenameisprovided,thecommandcollectsfeature-specificsupportinformation.
InordertocollectdatafromstandbyandmemberinaVSFstack,thecommandwillpromptforthelocaluser
passwordonce.
Examples
CopyingthesupportfilestoaremoteURL:
| switch# copy | support-files | tftp://10.100.0.12/file.tar.gz |     |     |     |     |
| ------------ | ------------- | ------------------------------ | --- | --- | --- | --- |
CopyingthesupportfilesofthelldpfeaturetoaremoteURLwithaspecifiedVRF:
SupportabilityCopy|51

switch# copy support-files feature lldp tftp://10.100.0.12/file.tar.gz vrf mgmt
CopyingthesupportfilesfromthepreviousboottoaremoteURLwithaspecifiedVRF:
switch# copy support-files previous-boot scp://user@10.0.14.206/file.tar.gz vrf mgmt
CopyingthesupportfilestoaUSB:
| switch# | copy support-files | usb:/file.tar.gz |     |
| ------- | ------------------ | ---------------- | --- |
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
copy support-files [feature <FEATURE-NAME> | previous-boot | all ] local-file {<REMOTE-URL>
| [vrf <VRF-NAME>] | | <STORAGE-URL>} |     |     |
| ---------------- | ---------------- | --- | --- |
Description
Storesasetofsupportfilesasacompressedfileintheswitchlocallyandcopiesthepreservedsupportfiles
toadirectoryusingTFTP,SFTP,SCP,orUSB.
Youcanstoreonlyonecopyofthesupportfilelocally.Whenyoustoreanewsupportfile,itoverwritestheexisting
supportfile.
52
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
| switch# | copy support-files | local-file    |                 |
| ------- | ------------------ | ------------- | --------------- |
| switch# | copy support-files | feature       | lldp local-file |
| switch# | copy support-files | previous-boot | local-file      |
switch#
|     | copy support-files | all | local-file |
| --- | ------------------ | --- | ---------- |
The operation to copy all support files could take a while to complete.
| Do you want | to continue | (y/n)? |     |
| ----------- | ----------- | ------ | --- |
CopyinglocalsupportfiletoaremoteURLandstorageURL:
switch# copy support-files local-file usb:/support_files_dir_path/
switch# copy support-files local-file scp://root@10.0.14.206//support_files_dir_
| path/abc.tar.gz | vrf mgmt |     |     |
| --------------- | -------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy support-files |     | vsf member |     |
| ------------------ | --- | ---------- | --- |
SupportabilityCopy|53

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
Iffeaturenameisnotprovided,thecommandcollectsgenericsystem-specificsupportinformation.Ifa
featurenameisprovided,thecommandcollectsfeature-specificsupportinformation.
Examples
CopyingthesupportfilestoaUSB:
| switch# copy | support-files | vsf member | 2 usb:/file.tar.gz |     |     |     |
| ------------ | ------------- | ---------- | ------------------ | --- | --- | --- |
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch# copy support-files vsf member 2 scp://user@10.100.0.12/file.tar.gz/ vrf mgmt
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch#
copy support-files vsf member 2 sftp://user@10.100.0.12/support_files_dir_
| path/ vrf | mgmt |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
CommandHistory
| Release |     |     | Modification      |     |     |     |
| ------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08   |     |     | AddedSCP support. |     |     |     |
54
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

6200

Manager (#)

Administrators or local user group members with execution rights
for this command.

copy support-log

Description

Copies the specified support log for a daemon TFTP, SFTP, SCP, or USB.

Parameter

<DAEMON-NAME>

{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}

<STORAGE-URL>

<REMOTE-URL>

vrf <VRF-NAME>

Usage

Description

Specifies the name of the daemon. Required.

Selects either the storage URL or the remote URL
for the destination of the copied command output.
Required.

Specifies the USB to copy command output.
Syntax: {usb}:/<FILE>

Specifies the URL to copy the command output.
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> |

<HOST>}[:<PORT>]/<FILE>

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

Supportability Copy | 55

switch# copy support-log fand scp://user@10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log hpe-fand tftp://10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaUSB:
| switch# | copy support-log | hpe-fand | usb:/support-log |
| ------- | ---------------- | -------- | ---------------- |
CommandHistory
| Release        |     |     | Modification      |
| -------------- | --- | --- | ----------------- |
| 10.08          |     |     | AddedSCP support. |
| 10.07orearlier |     |     | --                |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy support-log | vsf | member |     |
| ---------------- | --- | ------ | --- |
copy support-log vsf member <MEMBER-ID> <DAEMON-NAME> {<STORAGE-URL> | <REMOTE-URL> [vrf
<VRF-NAME>]}
Description
CopiesthespecifiedsupportlogforadaemonusingTFTP,SFTP,SCP,orUSB.
Parameter Description
<MEMBER-ID> Specifiesthemember-idoftheVSFmember.
Required.
<DAEMON-NAME> Specifiesthenameofthedaemon.Required.
{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]} SelectseitherthestorageURLortheremoteURL
forthedestinationofthecopiedcommandoutput.
Required.
<STORAGE-URL>
SpecifiestheUSBtocopycommandoutput.
Syntax:{usb}:/<FILE>
<REMOTE-URL> SpecifiestheURLtocopythecommandoutput.
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
56
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

| Parameter |     |     |     | Description |                     |     |
| --------- | --- | --- | --- | ----------- | ------------------- | --- |
|           |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
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
| switch# | copy support-log | vsf member | 2 hpe-fand | usb:/support-log |     |     |
| ------- | ---------------- | ---------- | ---------- | ---------------- | --- | --- |
CommandHistory
| Release        |     |     | Modification      |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- |
| 10.08          |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier |     |     | --                |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
SupportabilityCopy|57

Chapter 9
Traceroute
Traceroute
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagramProtocol
(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashoplimit,isused
indeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
| Traceroute | commands |     |     |
| ---------- | -------- | --- | --- |
traceroute
traceroute {<IPV4-ADDR> | <HOSTNAME>} [ip-option loosesourceroute <IPV4-ADDR>] [dstport
<NUMBER> | maxttl <NUMBER> | minttl <NUMBER> | probes <NUMBER> | timeout <TIME>] [vrf <VRF-
| NAME>] source | {<IPV4-ADDR> | | <IFNAME>} |     |
| ------------- | ------------ | ----------- | --- |
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
maxttl <NUMBER> Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
minttl <NUMBER> SpecifiestheMinimumnumberofhopstoreachthedestination,
<1-255>.Default:1
| probes <NUMBER> |     |     |     |
| --------------- | --- | --- | --- |
Specifiesthenumberofprobes,<1-5>.Default:3
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.
source {<IPV4-ADDR> | <IFNAME>} SpecifiesthesourceIPv4addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagramProtocol
58
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
probes
| 1 10.0.40.2        | 0.002ms   | 0.002ms 0.001ms |
| ------------------ | --------- | --------------- |
| 2 10.0.30.1        | 0.002ms   | 0.001ms 0.001ms |
| 3 10.0.10.1        | 0.001ms   | 0.002ms 0.002ms |
| switch# traceroute | localhost | vrf red         |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 127.0.0.1        | 0.003ms   | 0.002ms 0.001ms |
| ------------------ | --------- | --------------- |
| switch# traceroute | localhost | mgmt            |
traceroute to localhost (127.0.0.1), 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 127.0.0.1 | 0.018ms | 0.006ms 0.003ms |
| ----------- | ------- | --------------- |
Traceroute|59

switch# traceroute 10.0.10.1 maxttl 20 timeout 5 minttl 1 probes 3 dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1 10.0.40.2 | 0.002ms | 0.002ms | 0.001ms |     |     |     |
| ----------- | ------- | ------- | ------- | --- | --- | --- |
| 2 10.0.30.1 | 0.002ms | 0.001ms | 0.001ms |     |     |     |
| 3 10.0.10.1 | 0.001ms | 0.002ms | 0.002ms |     |     |     |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 10.0.40.2 | 0.002ms | 0.002ms | 0.001ms |     |     |     |
| ----------- | ------- | ------- | ------- | --- | --- | --- |
| 2 10.0.30.1 | 0.002ms | 0.001ms | 0.001ms |     |     |     |
| 3 10.0.10.1 | 0.001ms | 0.002ms | 0.002ms |     |     |     |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2 maxttl 20 timeout
| 5 minttl | 1 probes 3 | dstport 33434 |     |     |     |     |
| -------- | ---------- | ------------- | --- | --- | --- | --- |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1 10.0.40.2 | 0.002ms             | 0.002ms     | 0.001ms     |     |     |     |
| ----------- | ------------------- | ----------- | ----------- | --- | --- | --- |
| 2 10.0.30.1 | 0.002ms             | 0.001ms     | 0.001ms     |     |     |     |
| 3 10.0.10.1 | 0.001ms             | 0.002ms     | 0.002ms     |     |     |     |
| switch#     | traceroute 10.0.0.2 | source      | 10.0.0.1    |     |     |     |
| traceroute  | to 10.0.0.2         | (10.0.0.2), | 30 hops max |     |     |     |
| 1 10.0.0.2  | 0.299ms             | 0.155ms     | 0.115ms     |     |     |     |
| switch#     | traceroute 10.0.0.2 | source      | 1/1/1       |     |     |     |
| traceroute  | to 10.0.0.2         | (10.0.0.2), | 30 hops max |     |     |     |
| 1 10.0.0.2  | 0.479ms             | 0.222ms     | 0.171ms     |     |     |     |
CommandHistory
| Release |     |     | Modification |                     |           |      |
| ------- | --- | --- | ------------ | ------------------- | --------- | ---- |
| 10.08   |     |     | Addedsource  | IP addressandsource | interface | name |
parameters.
| 10.07orearlier |     |     | --  |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
traceroute6
traceroute6 {<IPV6-ADDR> | <HOSTNAME>} [dstport <NUMBER> | maxttl <NUMBER> | probes <NUMBER>
| timeout <TIME>] [vrf <VRF-NAME>] source {<IPV6-ADDR> | <IFNAME>}
Description
UsestracerouteforthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.
60
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- |

| Parameter    |             |     | Description                                  |     |
| ------------ | ----------- | --- | -------------------------------------------- | --- |
| IPv6-address | <IPV6-ADDR> |     | SpecifiestheIPv6address.                     |     |
| hostname     |             |     | Specifiesthehostnameofthedevicetotraceroute. |     |
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
maxttl <NUMBER> Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
probes <NUMBER>
Specifiesthenumberofprobes,<1-5>.Default:3
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME>
Specifiesthevirtualroutingandforwarding(VRF)touse,<VRF-
NAME>.
source {<IPV6-ADDR> | <IFNAME>} SpecifiesthesourceIPv6addressorinterfacename.
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
byte packets
| 1 localhost | (::1)       | 0.117 ms         | 0.032 ms 0.021 | ms  |
| ----------- | ----------- | ---------------- | -------------- | --- |
| switch#     | traceroute6 | 0:0::0:1 dsrport | 33434          |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117 ms        | 0.032 ms 0.021 | ms  |
| ----------- | ----------- | --------------- | -------------- | --- |
| switch#     | traceroute6 | 0:0::0:1 probes | 2              |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 2 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117 ms         | 0.032 ms |     |
| ----------- | ----------- | ---------------- | -------- | --- |
| switch#     | traceroute6 | 0:0::0:1 timeout | 3        |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1) | 0.117 ms | 0.032 ms 0.021 | ms  |
| ----------- | ----- | -------- | -------------- | --- |
Traceroute|61

switch#
|     | traceroute6 |     | localhost |     | vrf red |     |     |     |     |     |
| --- | ----------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost |             | (::1) | 0.077     | ms  | 0.051 | ms 0.054 | ms  |     |     |     |
| ----------- | ----------- | ----- | --------- | --- | ----- | -------- | --- | --- | --- | --- |
| switch#     | traceroute6 |       | localhost |     | mgmt  |          |     |     |     |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost |     | (::1) | 0.089 | ms  | 0.03 ms | 0.014 | ms  |     |     |     |
| ----------- | --- | ----- | ----- | --- | ------- | ----- | --- | --- | --- | --- |
switch#
|     | traceroute6 |     | 0:0::0:1 | maxttl | 30  | timeout | 3 probes | 3 dstport | 33434 |     |
| --- | ----------- | --- | -------- | ------ | --- | ------- | -------- | --------- | ----- | --- |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost |             | (::1) | 0.117   | ms     | 0.032   | ms 0.021 | ms  |     |     |     |
| ----------- | ----------- | ----- | ------- | ------ | ------- | -------- | --- | --- | --- | --- |
| switch#     | traceroute6 |       | 2001::2 | source | 2001::1 |          |     |     |     |     |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3 probes,
| 24 byte   | packets |           |        |     |        |     |           |     |     |     |
| --------- | ------- | --------- | ------ | --- | ------ | --- | --------- | --- | --- | --- |
| 1 2001::2 |         | (2001::2) | 0.4331 | ms  | 0.3186 | ms  | 0.1874 ms |     |     |     |
switch#
|     | traceroute6 |     | 2001::2 | source | 1/1/1 |     |     |     |     |     |
| --- | ----------- | --- | ------- | ------ | ----- | --- | --- | --- | --- | --- |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3 probes,
| 24 byte   | packets |           |        |     |        |     |           |     |     |     |
| --------- | ------- | --------- | ------ | --- | ------ | --- | --------- | --- | --- | --- |
| 1 2001::2 |         | (2001::2) | 0.6145 | ms  | 0.4165 | ms  | 0.1620 ms |     |     |     |
CommandHistory
| Release |     |     |     |     | Modification |     |                     |     |           |      |
| ------- | --- | --- | --- | --- | ------------ | --- | ------------------- | --- | --------- | ---- |
| 10.08   |     |     |     |     | Addedsource  |     | IP addressandsource |     | interface | name |
parameters.
| 10.07orearlier |     |     |     |     | --  |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
62
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     |     |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

Chapter 10

Ping

Ping

The ping (Packet Internet Groper) command is a common method for troubleshooting the accessibility of
devices. It uses Internet Control Message Protocol (ICMP) echo requests and ICMP echo replies to determine
if another device is alive. It also measures the amount of time it takes to receive a reply from the specified
destination. The ping command is mostly used to verify IP connectivity between two endpoints which could
be switch to switch, host to host, or host to switch. The reply packet tells if the host received the ping and
the amount of time it took to return the packet.

Ping commands

ping
ping <IPv4-ADDR> | <hostname> [data-fill <pattern> | datagram-size <size> |
interval <time> | repetitions <number> | timeout <time> | tos <number> |
ip-option {include-timestamp | include-timestamp-and-address | record-route} |
vrf <vrfname> | do-not-fragment][source {IPv4-ADDR | IFNAME}]

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

timeout <TIME>

tos <NUMBER>

ip-option {include-timestamp |

include-timestamp-and-address |
record-route}

Specifies the interval between successive ping requests in
seconds. Range: 1-60 seconds, default: 1 second.

Specifies the number of packets to send. Range: 1-10000 packets,
default: Five packets.

Specifies the ping timeout in seconds. Range: 1-60 seconds,
default: 2 seconds.

Specifies the IP Type of Service to be used in Ping request. Range:
0-255

Specifies an IP option (record-route or timestamp option).

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

63

| Parameter         |     |     |     |     | Description                              |     |     |     |
| ----------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
| include-timestamp |     |     |     |     | Specifiestheintermediateroutertimestamp. |     |     |     |
include-timestamp-and-address SpecifiestheintermediateroutertimestampandIPaddress.
| record-route |     |     |     |     | Specifiestheintermediaterouteraddresses. |     |     |     |
| ------------ | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.WhenVRF
optionisnotgiven,thedefaultVRFisused.
| source {IPv4-ADDR |     | |   | IFNAME} |     |     |     |     |     |
| ----------------- | --- | --- | ------- | --- | --- | --- | --- | --- |
SpecifiesthesourceIPv4addressorinterfacetouse.
do-not-fragment Specifiesthedo-not-fragment(DF)bitinIPheaderofthePing
packet.Thisoptiondoesnotallowthepackettobefragmented
whenithastogothroughasegmentwithasmallermaximum
transmissionunit(MTU).
Examples
PinginganIPv4address:
| switch#              | ping         | 10.0.0.0   |                           |            |        |        |            |             |
| -------------------- | ------------ | ---------- | ------------------------- | ---------- | ------ | ------ | ---------- | ----------- |
| PING 10.0.0.0        |              | (10.0.0.0) |                           | 100(128)   | bytes  | of     | data.      |             |
| 108 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=1 | ttl=64 |        | time=0.035 | ms          |
| 108 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=2 | ttl=64 |        | time=0.034 | ms          |
| 108 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=3 | ttl=64 |        | time=0.034 | ms          |
| 108 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=4 | ttl=64 |        | time=0.034 | ms          |
| 108 bytes            | from         | 10.0.0.0:  |                           | icmp_seq=5 | ttl=64 |        | time=0.033 | ms          |
| --- 10.0.0.0         |              | ping       | statistics                |            | ---    |        |            |             |
| 5 packets            | transmitted, |            | 5                         | received,  | 0%     | packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |              |            | = 0.033/0.034/0.035/0.000 |            |        |        | ms         |             |
Pingingthelocalhost:
| switch#        | ping | localhost   |     |          |       |     |          |     |
| -------------- | ---- | ----------- | --- | -------- | ----- | --- | -------- | --- |
| PING localhost |      | (127.0.0.1) |     | 100(128) | bytes |     | of data. |     |
108 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.060 ms
108 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.035 ms
108 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.043 ms
108 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.041 ms
108 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.034 ms
| --- localhost        |              | ping | statistics                |           | --- |        |       |             |
| -------------------- | ------------ | ---- | ------------------------- | --------- | --- | ------ | ----- | ----------- |
| 5 packets            | transmitted, |      | 5                         | received, | 0%  | packet | loss, | time 3998ms |
| rtt min/avg/max/mdev |              |      | = 0.034/0.042/0.060/0.011 |           |     |        | ms    |             |
Pingingaserverwithadatapattern:
| switch#       | ping                               | 10.0.0.2   | data-fill |            | 1234123412341234acde123456789012 |     |            |     |
| ------------- | ---------------------------------- | ---------- | --------- | ---------- | -------------------------------- | --- | ---------- | --- |
| PATTERN:      | 0x1234123412341234acde123456789012 |            |           |            |                                  |     |            |     |
| PING 10.0.0.2 |                                    | (10.0.0.2) |           | 100(128)   | bytes                            | of  | data.      |     |
| 108 bytes     | from                               | 10.0.0.2:  |           | icmp_seq=1 | ttl=64                           |     | time=0.207 | ms  |
| 108 bytes     | from                               | 10.0.0.2:  |           | icmp_seq=2 | ttl=64                           |     | time=0.187 | ms  |
| 108 bytes     | from                               | 10.0.0.2:  |           | icmp_seq=3 | ttl=64                           |     | time=0.225 | ms  |
| 108 bytes     | from                               | 10.0.0.2:  |           | icmp_seq=4 | ttl=64                           |     | time=0.197 | ms  |
Ping|64

| 108 bytes            | from 10.0.0.2: |                           | icmp_seq=5 |     | ttl=64    | time=0.210 | ms   |        |
| -------------------- | -------------- | ------------------------- | ---------- | --- | --------- | ---------- | ---- | ------ |
| --- 10.0.0.2         | ping           | statistics                | ---        |     |           |            |      |        |
| 5 packets            | transmitted,   | 5                         | received,  |     | 0% packet | loss,      | time | 3999ms |
| rtt min/avg/max/mdev |                | = 0.187/0.205/0.225/0.015 |            |     |           | ms         |      |        |
Pingingaserverwithadatagramsize:
| switch#              | ping 10.0.0.0  | datagram-size             |            |       | 200       |            |      |        |
| -------------------- | -------------- | ------------------------- | ---------- | ----- | --------- | ---------- | ---- | ------ |
| PING 10.0.0.0        | (10.0.0.0)     |                           | 200(228)   | bytes | of        | data.      |      |        |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=1 |       | ttl=64    | time=0.202 | ms   |        |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=2 |       | ttl=64    | time=0.194 | ms   |        |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=3 |       | ttl=64    | time=0.201 | ms   |        |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=4 |       | ttl=64    | time=0.200 | ms   |        |
| 208 bytes            | from 10.0.0.0: |                           | icmp_seq=5 |       | ttl=64    | time=0.186 | ms   |        |
| --- 10.0.0.0         | ping           | statistics                | ---        |       |           |            |      |        |
| 5 packets            | transmitted,   | 5                         | received,  |       | 0% packet | loss,      | time | 4000ms |
| rtt min/avg/max/mdev |                | = 0.186/0.196/0.202/0.016 |            |       |           | ms         |      |        |
Pingingaserverwithanintervalspecified:
| switch#              | ping 9.0.0.2    | interval                  |           | 2     |           |            |      |        |
| -------------------- | --------------- | ------------------------- | --------- | ----- | --------- | ---------- | ---- | ------ |
| PING 9.0.0.2         | (9.0.0.2)       | 100(128)                  |           | bytes | of data.  |            |      |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=1                |           |       | ttl=64    | time=0.199 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=2                |           |       | ttl=64    | time=0.192 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=3                |           |       | ttl=64    | time=0.208 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=4                |           |       | ttl=64    | time=0.182 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=5                |           |       | ttl=64    | time=0.194 | ms   |        |
| --- 9.0.0.2          | ping statistics |                           | ---       |       |           |            |      |        |
| 5 packets            | transmitted,    | 5                         | received, |       | 0% packet | loss,      | time | 7999ms |
| rtt min/avg/max/mdev |                 | = 0.182/0.195/0.208/0.008 |           |       |           | ms         |      |        |
Pingingaserverwithaspecifiednumberofpacketstosend:
| switch#              | ping 9.0.0.2    | repetitions               |           | 10    |           |            |      |        |
| -------------------- | --------------- | ------------------------- | --------- | ----- | --------- | ---------- | ---- | ------ |
| PING 9.0.0.2         | (9.0.0.2)       | 100(128)                  |           | bytes | of data.  |            |      |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=1                |           |       | ttl=64    | time=0.213 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=2                |           |       | ttl=64    | time=0.204 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=3                |           |       | ttl=64    | time=0.201 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=4                |           |       | ttl=64    | time=0.184 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=5                |           |       | ttl=64    | time=0.202 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=6                |           |       | ttl=64    | time=0.184 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=7                |           |       | ttl=64    | time=0.193 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=8                |           |       | ttl=64    | time=0.196 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=9                |           |       | ttl=64    | time=0.193 | ms   |        |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=10               |           |       | ttl=64    | time=0.200 | ms   |        |
| --- 9.0.0.2          | ping statistics |                           | ---       |       |           |            |      |        |
| 10 packets           | transmitted,    | 10                        | received, |       | 0% packet | loss,      | time | 8999ms |
| rtt min/avg/max/mdev |                 | = 0.184/0.197/0.213/0.008 |           |       |           | ms         |      |        |
Pingingaserverwithaspecifiedtimeout:
65
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| switch#              | ping 9.0.0.2    | timeout                   | 3         |                |            |             |
| -------------------- | --------------- | ------------------------- | --------- | -------------- | ---------- | ----------- |
| PING 9.0.0.2         | (9.0.0.2)       | 100(128)                  |           | bytes of data. |            |             |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=1                |           | ttl=64         | time=0.175 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=2                |           | ttl=64         | time=0.192 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=3                |           | ttl=64         | time=0.190 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=4                |           | ttl=64         | time=0.181 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=5                |           | ttl=64         | time=0.197 | ms          |
| --- 9.0.0.2          | ping statistics |                           | ---       |                |            |             |
| 5 packets            | transmitted,    | 5                         | received, | 0% packet      | loss,      | time 4000ms |
| rtt min/avg/max/mdev |                 | = 0.175/0.187/0.197/0.007 |           |                | ms         |             |
PingingaserverwiththespecifiedIPTypeofService:
| switch#              | ping 9.0.0.2    | tos                       | 2         |                |            |             |
| -------------------- | --------------- | ------------------------- | --------- | -------------- | ---------- | ----------- |
| PING 9.0.0.2         | (9.0.0.2)       | 100(128)                  |           | bytes of data. |            |             |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=1                |           | ttl=64         | time=0.033 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=2                |           | ttl=64         | time=0.034 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=3                |           | ttl=64         | time=0.031 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=4                |           | ttl=64         | time=0.034 | ms          |
| 108 bytes            | from 9.0.0.2:   | icmp_seq=5                |           | ttl=64         | time=0.031 | ms          |
| --- 9.0.0.2          | ping statistics |                           | ---       |                |            |             |
| 5 packets            | transmitted,    | 5                         | received, | 0% packet      | loss,      | time 3999ms |
| rtt min/avg/max/mdev |                 | = 0.031/0.032/0.034/0.006 |           |                | ms         |             |
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
Ping|66

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
67
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| --- 9.0.0.2          |              | ping statistics |                           | ---       |     |        |            |        |
| -------------------- | ------------ | --------------- | ------------------------- | --------- | --- | ------ | ---------- | ------ |
| 5 packets            | transmitted, |                 | 5                         | received, | 0%  | packet | loss, time | 3999ms |
| rtt min/avg/max/mdev |              |                 | = 0.034/0.036/0.038/0.001 |           |     |        | ms         |        |
Pingingaserverwithdo-not-fragment:
| switch#              | ping         | 192.168.1.8   |                           | datagram-size |            | 2000   | do-not-fragment |        |
| -------------------- | ------------ | ------------- | ------------------------- | ------------- | ---------- | ------ | --------------- | ------ |
| PING 192.168.1.8     |              | (192.168.1.8) |                           |               | 2000(2028) |        | bytes of data.  |        |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=1    |            | ttl=64 | time=0.721      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=2    |            | ttl=64 | time=0.792      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=3    |            | ttl=64 | time=0.857      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=4    |            | ttl=64 | time=0.833      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=5    |            | ttl=64 | time=0.836      | ms     |
| --- 192.168.1.8      |              | ping          | statistics                |               | ---        |        |                 |        |
| 5 packets            | transmitted, |               | 5                         | received,     | 0%         | packet | loss, time      | 4056ms |
| rtt min/avg/max/mdev |              |               | = 0.721/0.807/0.857/0.048 |               |            |        | ms              |        |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
ping6
ping6 {<IPv6-ADDR> | <HOSTNAME>} [data-fill <PATTERN> | datagram-size <SIZE> |
| interval       | <TIME> | |        | repetitions | <NUMBER> |     | | timeout | <TIME> | |   |
| -------------- | ------ | -------- | ----------- | -------- | --- | --------- | ------ | --- |
| vrf <VRF-NAME> |        | | source | <IPv6-ADDR> |          | |   | <IFNAME>] |        |     |
Description
PingsthespecifiedIPv6addressorhostnamewithorwithoutoptionalparameters.
| Parameter |     |     |     |     | Description                                    |     |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| IPv6-ADDR |     |     |     |     | SelectstheIPv6addresstoping.                   |     |     |     |
| HOSTNAME  |     |     |     |     | Selectsthehostnametoping.Range:1-256characters |     |     |     |
data-fill <PATTERN> Specifiesthedatapatterninhexadecimaldigitstosend.A
maximumof16"pad"bytescanbespecifiedtofillouttheICMP
packet.Default:AB
datagram-size <SIZE> Specifiesthepingdatagramsize.Range:0-65399,default:100.
Ping|68

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
interval <TIME> Specifiestheintervalbetweensuccessivepingrequestsin
seconds.Range:1-60seconds,default:1second.
repetitions <NUMBER> Specifiesthenumberofpacketstosend.Range:1-10000packets,
default:Fivepackets.
timeout <TIME>
Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.Whenthis
optionisnotprovided,thedefaultVRFisused.
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
| switch#               | ping6 2020::2 | data-fill |            | ab    |        |            |     |
| --------------------- | ------------- | --------- | ---------- | ----- | ------ | ---------- | --- |
| PATTERN:              | 0xab          |           |            |       |        |            |     |
| PING 2020::2(2020::2) |               | 100       | data       | bytes |        |            |     |
| 108 bytes             | from 2020::2: |           | icmp_seq=1 |       | ttl=64 | time=0.038 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=2 |       | ttl=64 | time=0.074 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=3 |       | ttl=64 | time=0.076 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=4 |       | ttl=64 | time=0.075 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=5 |       | ttl=64 | time=0.077 | ms  |
69
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| --- 2020::2          |              | ping statistics |                           | ---       |           |       |             |
| -------------------- | ------------ | --------------- | ------------------------- | --------- | --------- | ----- | ----------- |
| 5 packets            | transmitted, |                 | 5                         | received, | 0% packet | loss, | time 3999ms |
| rtt min/avg/max/mdev |              |                 | = 0.038/0.068/0.077/0.015 |           |           | ms    |             |
Pingingaserverwithadatagramsize:
| switch#              | ping6            | 2020::2         | datagram-size             |           | 200       |            |             |
| -------------------- | ---------------- | --------------- | ------------------------- | --------- | --------- | ---------- | ----------- |
| PING                 | 2020::2(2020::2) |                 | 200                       | data      | bytes     |            |             |
| 208 bytes            | from             | 2020::2:        | icmp_seq=1                |           | ttl=64    | time=0.037 | ms          |
| 208 bytes            | from             | 2020::2:        | icmp_seq=2                |           | ttl=64    | time=0.076 | ms          |
| 208 bytes            | from             | 2020::2:        | icmp_seq=3                |           | ttl=64    | time=0.076 | ms          |
| 208 bytes            | from             | 2020::2:        | icmp_seq=4                |           | ttl=64    | time=0.077 | ms          |
| 208 bytes            | from             | 2020::2:        | icmp_seq=5                |           | ttl=64    | time=0.066 | ms          |
| --- 2020::2          |                  | ping statistics |                           | ---       |           |            |             |
| 5 packets            | transmitted,     |                 | 5                         | received, | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |                  |                 | = 0.037/0.066/0.077/0.016 |           |           | ms         |             |
Pingingaserverwithanintervalspecified:
| switch#              | ping6            | 2020::2         | interval                  |           | 5         |            |              |
| -------------------- | ---------------- | --------------- | ------------------------- | --------- | --------- | ---------- | ------------ |
| PING                 | 2020::2(2020::2) |                 | 100                       | data      | bytes     |            |              |
| 108 bytes            | from             | 2020::2:        | icmp_seq=1                |           | ttl=64    | time=0.043 | ms           |
| 108 bytes            | from             | 2020::2:        | icmp_seq=2                |           | ttl=64    | time=0.075 | ms           |
| 108 bytes            | from             | 2020::2:        | icmp_seq=3                |           | ttl=64    | time=0.074 | ms           |
| 108 bytes            | from             | 2020::2:        | icmp_seq=4                |           | ttl=64    | time=0.075 | ms           |
| 108 bytes            | from             | 2020::2:        | icmp_seq=5                |           | ttl=64    | time=0.075 | ms           |
| --- 2020::2          |                  | ping statistics |                           | ---       |           |            |              |
| 5 packets            | transmitted,     |                 | 5                         | received, | 0% packet | loss,      | time 19999ms |
| rtt min/avg/max/mdev |                  |                 | = 0.043/0.068/0.075/0.014 |           |           | ms         |              |
Pingingaserverwithaspecifiednumberofpacketstosend:
switch#
|                      | ping6            | 2020::2         | repetitions               |           | 6         |            |             |
| -------------------- | ---------------- | --------------- | ------------------------- | --------- | --------- | ---------- | ----------- |
| PING                 | 2020::2(2020::2) |                 | 100                       | data      | bytes     |            |             |
| 108 bytes            | from             | 2020::2:        | icmp_seq=1                |           | ttl=64    | time=0.039 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=2                |           | ttl=64    | time=0.070 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=3                |           | ttl=64    | time=0.076 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=4                |           | ttl=64    | time=0.076 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=5                |           | ttl=64    | time=0.071 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=6                |           | ttl=64    | time=0.078 | ms          |
| --- 2020::2          |                  | ping statistics |                           | ---       |           |            |             |
| 6 packets            | transmitted,     |                 | 6                         | received, | 0% packet | loss,      | time 4999ms |
| rtt min/avg/max/mdev |                  |                 | = 0.039/0.068/0.078/0.015 |           |           | ms         |             |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
Ping|70

| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
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
| Network | is unreachable |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
Symptom
Userreceivesa"networkisunreachable"messageonsendingapingrequest.
Cause
71
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

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

Ping | 72

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
logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} [ {udp [<PORT-NUM>] }|{tcp [<PORT-
NUM>} | {tls [<PORT-NUM> [auth-mode {certificate|subject-name}] [legacy-tls-renegotiation]}]
| [severity | <LEVEL>] [vrf | <VRF-NAME>] | [include-auditable-events] |     |     |
| --------- | ------------- | ----------- | -------------------------- | --- | --- |
[filter <FILTER-NAME>] [ rate-limit-burst <BURST> [rate-limit-interval <INTERVAL>] ]
| no logging | {<IPV4-ADDR> | | <IPV6-ADDR> | | <FQDN | | HOSTNAME> | }   |
| ---------- | ------------ | ------------- | ------- | ----------- | --- |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>} SelectstheIPv4address,IPv6address,orhostnameofthe
remotesyslogserver.Required.
[udp [<PORT-NUM>] | tcp [<PORT-NUM> | SpecifiestheUDPport,TCPport,orTLSportoftheremote
tls [<PORT-NUM>]]
syslogservertoreceivetheforwardedsyslogmessages.
| udp [<PORT-NUM>] |     |     | Range:1to65535.Default:514 |     |     |
| ---------------- | --- | --- | -------------------------- | --- | --- |
tcp [<PORT-NUM>]
Range:1to65535.Default:1470
| tls [<PORT-NUM>] |     |     | Range:1to65535.Default:6514 |     |     |
| ---------------- | --- | --- | --------------------------- | --- | --- |
include-auditable-events
Specifiesthatauditablemessagesarealsologgedtothe
remotesyslogserver.
| severity | <LEVEL> |     | Specifiestheseverityofthesyslogmessages: |     |     |
| -------- | ------- | --- | ---------------------------------------- | --- | --- |
alert:Forwardssyslogmessageswiththeseverityof
n
alert (6)andemergency (7).
n crit:Forwardssyslogmessageswiththeseverityof
critical (5)andabove.
n debug:Forwardssyslogmessageswiththeseverityof
73
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

Parameter

Description

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

switch(config)# no logging

Enabling syslog forwarding over TLS to a remote syslog server using subject-name authentication mode:

Remote syslog | 74

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
Theeventlogsfrombeinggeneratedontheswitch,or
n
n Theeventordebuglogsgeneratedontheswitchfrombeingforwardedtoasyslogserver.
Afilterisidentifiedbyafilternameandcanhaveupto20rulesorentries,eachwithadifferentsequence
number,matchingcriteria,andcorrespondingaction(denyorpermit).Whenafilterisappliedonalog,the
logismatchedagainstthecriteriamentionedintherulesorentriesinascendingnumericalorderoftheir
sequencenumbersuntilamatchingentryisfound.Onceamatchingentryisfound,itscorrespondingaction
isappliedonthelog.Ifnomatchingruleisfound,thedefaultaction(permit)isapplied.
Thenoformofthiscommandremovesthefilter.
75
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

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

enable

10 deny severity lt info

This configuration denies the event logs which have a severity less than info.

Remote syslog | 76

Ifafiltercontainsenablecommand,itisnotrecommendedtoconfigurethisfilterintheloggingcommandused
forremotesyslogserverconfiguration.Thisisbecause,anyeventlogsdeniedbythefilterarealreadynot
availableforforwardingtoaremoteserver.
Afilterwithenablecommandwillnotaffectdebuglogs.Considertheconfigurationinthefollowingexample
ofafilterwithenablecommandandtworulesapplied10 infoand20 deny.This
|     |     |     | permit | severity ge |
| --- | --- | --- | ------ | ----------- |
impliespermitonlythoseeventlogswhichhaveseveritygreaterthanorequaltoinfo.
Example:
| logging | filter low_severity_logs |     |     |     |
| ------- | ------------------------ | --- | --- | --- |
enable
| 10 permit | severity | ge info |     |     |
| --------- | -------- | ------- | --- | --- |
20 deny
Filtering event ordebug logs when forwarding toaremote syslog server:Thefilternamemustbe
configuredintheloggingcommandthatisusedtoconfigureremotesyslogserver.Thelogswillbe
generatedontheswitchandthefilteronlydecideswhethertodenyorpermitthesyslogforwardingforthe
matchinglog.Forexample:logging 10.0.10.6 filter filter_lldp_logs
Thefilteraffectsdebuglogsonlywhenthecommanddebug destination syslogisconfiguredontheswitch.
Theseveritymentionedintheremotesyslogserverconfigurationusingloggingcommandunderconfiguration
contexthasmoreprecedencethantheseveritymentionedinafilterentry.Ifalogwithwarningseverityis
permittedbyafilter,buttheremotesyslogconfigurationhasseverityerrmentionedinit,thelogwillnotbe
forwardedtotheremotesyslogserver(sincewarning(3)islesserthanerr(4)).Ontheotherhand,ifalogwitherr
severityispermittedbyafilterandtheremotesyslogconfigurationhasseveritywarningmentionedinit,thelog
willbeforwardedtotheremotesyslogserver.
Examples
Configuringanewloggingfilter:
| switch(config)# | logging | filter example_filter |     |     |
| --------------- | ------- | --------------------- | --- | --- |
TodenylogshavingeventID1301andarangeofeventIDsfrom1305to1309:
| switch(config-logging-filter)# |     | 20 deny | event-id 1301,1305-1309 |     |
| ------------------------------ | --- | ------- | ----------------------- | --- |
TopermitlogshavingeventID1300:
| switch(config-logging-filter)# |     | 30 permit | event-id | 1300 |
| ------------------------------ | --- | --------- | -------- | ---- |
Topermitlogswithseveritygreaterthanorequaltoerr:
| switch(config-logging-filter)# |     | 30 permit | severity | ge err |
| ------------------------------ | --- | --------- | -------- | ------ |
77
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

Todenylogswithseveritygreaterthaninfo:
| switch(config-logging-filter)# |     | 30 deny | severity gt info |
| ------------------------------ | --- | ------- | ---------------- |
TodenylogswitheventID1024andamessagematchingtheregularexpressionLLDP:
switch(config-logging-filter)# 40 deny event-id 1024 includes LLDP
Denyingalllogs:
switch(config-logging-filter)#
40 deny
ChangingthesequenceIDofanexistingrule:
| switch(config-logging-filter)# |     | resequence | 20 70 |
| ------------------------------ | --- | ---------- | ----- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms configandconfig- Administratorsorlocalusergroupmemberswithexecutionrights
|                  | logging-filter | forthiscommand. |     |
| ---------------- | -------------- | --------------- | --- |
| logging facility |                |                 |     |
logging facility {local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7}
| no logging facility |     |     |     |
| ------------------- | --- | --- | --- |
Description
Setstheloggingfacilitytobeusedforremotesyslogmessages.Default:local7
Thenoformofthiscommanddisablestheloggingfacilitytobeusedforremotesyslogmessages.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
{local0 | local1 | local2 | Selectstheloggingfacilitytobeusedforremotesyslogmessages.
| local3 | | local4 | local5 | | Required. |     |
| -------- | ----------------- | --------- | --- |
| local6 | | local7}           |           |     |
Specifiestheseverityofthesyslogmessages:
n local0
local1
n
n local2
local3
n
n local4
Remotesyslog|78

| Parameter |     | Description |
| --------- | --- | ----------- |
local5
n
n local6
n local7
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
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
| Parameter        |     | Description |
| ---------------- | --- | ----------- |
| severity <LEVEL> |     |             |
Specifiestheseverityofthesyslogmessages:
alert:Preservessyslogmessageswiththeseverityofalert
n
(6)andemergency (7)
crit:Preservessyslogmessageswiththeseverityof
n
critical (5)andabove.Default.
n debug:Preservessyslogmessageswiththeseverityofdebug
(0)andabove.
n emerg:Preservessyslogmessageswiththeseverityof
emergency (7)only.
err:Preservessyslogmessageswiththeseverityoferr (4)
n
andabove.
info:Preservessyslogmessageswiththeseverityofinfo
n
(1)andabove.
79
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |
| --------------------------------------------- | --- | ------------------ |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
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
Remotesyslog|80

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

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

81

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
diag on-demand
diag on-demand {fan-tray | line-module | management-module} [<SLOT-ID>]
Description
Runsthediagnostictestsforallmodulesorforaspecifiedmodule.
Parameter Description
| [fan-tray | | line-module | | management-module] |     |
| --------- | ------------- | -------------------- | --- |
Selectstheoptionsforenablingordisablingruntime
diagnosticsforaspecificmodule.
fan-tray Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID>
Usage
Whennoparametersareusedinthecommand(diag on-demand),thecommandappliestoallmodules.
| switch#  | diag on-demand |                |          |
| -------- | -------------- | -------------- | -------- |
| Fetching | Test results.  | Please         | wait ... |
| Module   |                | ID Diagnostics | Success  |
Performed
| -------------------- |     | ----- ----------- | ------- |
| -------------------- | --- | ----------------- | ------- |
| LineModule           |     | 1/1               | 13 100% |
| ManagementModule     |     | 1/1               | 13 100% |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
RuntimeDiagnostics|82

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show diagnostic
show diagnostic {fan-tray | line-module | management-module} [<SLOT-ID>] {brief | detail}
Description
Displaysthediagnostictestresultsforallmodulesorforaspecifiedmodule.
Parameter Description
[fan-tray | line-module | management-module] Selectstheoptionsforenablingordisablingruntime
diagnosticsforaspecificmodule.
fan-tray
Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID> Specifiesthemember/slotformanagementmodules
(1/1),linemodules(1/1),andfantrays(1/1-1/2).
Usage
Whennoparametersareusedinthecommand(show diagnostic),thecommandappliestoallmodules.
| switch# | show diagnostic | brief          |         |
| ------- | --------------- | -------------- | ------- |
| Module  |                 | ID Diagnostics | Success |
Performed
| -------------------- |     | ----- ----------- | ------- |
| -------------------- | --- | ----------------- | ------- |
| ManagementModule     |     | 1/1               | 13 100% |
| LineModule           |     | 1/1               | 13 100% |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show diagnostic |     | events |     |
| --------------- | --- | ------ | --- |
83
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

show diagnostic events

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

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6200

Manager (#)

Administrators or local user group members with execution rights
for this command.

Runtime Diagnostics | 84

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
---------------------
---------------------

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: reboot
reboot: Restarting system

.
Looking for SVOS.

Primary SVOS: Checking...Loading...Finding...Verifying...Booting...

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

85

ServiceOS Information:

Version:
Build Date:
Build ID:
SHA:

ML.01.07.0001-internal
2020-09-02 11:53:34 PDT
ServiceOS:ML.01.07.0001-internal:64dfa8c99840:202009021153
64dfa8c998408ec69d835a070f57aad610bc0383

------------------------
------------------------

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

Service OS | 86

Theimageselectedbytheuserduringbootisarun-timedecisiononlyandwillnotpersistacrossreboots.
Thedefaultimagecanbeconfiguredusingtheboot set-defaultcommand.
Example
| ServiceOS | Information: |                        |              |
| --------- | ------------ | ---------------------- | ------------ |
| Version:  |              | ML.01.xx.xxxx-internal |              |
| Build     | Date:        | 2020-09-02             | 11:53:34 PDT |
Build ID: ServiceOS:ML.01.xx.xxxx-internal:64dfa8c99840:202009021153
| SHA: |     | 64dfa8c998408ec69d835a070f57aad610bc0383 |     |
| ---- | --- | ---------------------------------------- | --- |
Boot Profiles:
| 0. Service   | OS Console |       |                 |
| ------------ | ---------- | ----- | --------------- |
| 1. Primary   | Software   | Image | [ML.10.xx.xxxx] |
| 2. Secondary | Software   | Image | [ML.10.xx.xxxx] |
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
87
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Booting   | primary software |     | image... |     |     |     |
| --------- | ---------------- | --- | -------- | --- | --- | --- |
| Verifying | Image...         |     |          |     |     |     |
Image Info:
Name: AOS-CX
| Version:   | XL.01.01.0001                                      |     |              |     |     |     |
| ---------- | -------------------------------------------------- | --- | ------------ | --- | --- | --- |
| Build      | Id: AOS-CX:XL.01.01.0001:1a36111da4e0:201707171452 |     |              |     |     |     |
| Build      | Date: 2017-07-17                                   |     | 14:52:27 PDT |     |     |     |
| Extracting | Image...                                           |     |              |     |     |     |
| Loading    | Image...                                           |     |              |     |     |     |
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
ServiceOS|88

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
89
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     |     |     |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

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
ServiceOS|90

Presentingthebootmenuprompt:
| SVOS>     | boot     |              |                        |     |              |     |
| --------- | -------- | ------------ | ---------------------- | --- | ------------ | --- |
| ServiceOS |          | Information: |                        |     |              |     |
|           | Version: |              | ML.01.07.0001-internal |     |              |     |
|           | Build    | Date:        | 2020-09-02             |     | 11:53:34 PDT |     |
Build ID: ServiceOS:ML.01.07.0001-internal:64dfa8c99840:202009021153
|     | SHA: |     | 64dfa8c998408ec69d835a070f57aad610bc0383 |     |     |     |
| --- | ---- | --- | ---------------------------------------- | --- | --- | --- |
Boot Profiles:
| 0.     | Service           | OS Console |       |                  |     |     |
| ------ | ----------------- | ---------- | ----- | ---------------- | --- | --- |
| 1.     | Primary           | Software   | Image | [ML.10.06.0001]  |     |     |
| 2.     | Secondary         | Software   | Image | [ML.10.07.0001E] |     |     |
| Select | profile(primary): |            |       |                  |     |     |
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
91
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- |

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

Service OS | 92

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
93
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

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
ServiceOS|94

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
95
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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

Version: ML.01.07.0001-internal
Build Date: 2020-09-02 11:53:34 PDT
Build ID: ServiceOS:ML.01.07.0001-internal:64dfa8c99840:202009021153
SHA: 64dfa8c998408ec69d835a070f57aad610bc0383

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

exit (svos)
exit

Description

Logs the user out from the SVOS> prompt.

Example

Loging the user out from the SVOS> prompt:

SVOS> exit

(C) Copyright 2022 Hewlett Packard Enterprise Development LP

Service OS | 96

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
97
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- |

Command Information

Platforms

Command context

Authority

All platforms

ServiceOS (SVOS>)

Administrators or local user group members with execution rights
for this command.

identify
identify

Description

Prints the version of the SVOS and of the UEFI BIOS.

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

ip
ip {show | dhcp | disable | addr <ADDR-NETMASK-GATEWAY>}

Description

Shows or configures the port with a static IP address (IPv4 only) or enables the DHCP client on the port. An
address is set only if a DHCP server is available to provide one.

Parameter

Description

{show | dhcp | disable | addr <ADDR-NETMASK-GATEWAY>}

Selects the options for the OOBM port.

show

dhcp

disable

addr <ADDR-NETMASK-GATEWAY>

Example

Configuring the port with a DHCP IP address:

Shows the OOBM port.

Configures the port with a DHCP address.

Disables the OOBM port.

Configures the port with a static IP address
(IPv4 only). Specify address, netmask, and
gateway as A.B.C.D.

Service OS | 98

| SVOS> ip | dhcp |     |
| -------- | ---- | --- |
SVOS>
ip show
| Interface    | : Link Up     |     |
| ------------ | ------------- | --- |
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
6200 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ls
| ls [<OPTIONS>] | [<FILE-NME>] |     |
| -------------- | ------------ | --- |
Description
Thiscommandlistsdirectorycontents.
| Parameter |     | Description |
| --------- | --- | ----------- |
<OPTIONS>
Specifiesoptionsforthecommand.
| -1  |     | Showsone-columnoutput. |
| --- | --- | ---------------------- |
-a
Showsentrieswhichstartwithaperiod(.).
| -A  |     | Showsoutputsimilarto-a,butexcludesaperiod(.)anda |
| --- | --- | ------------------------------------------------ |
doubleperiod(..).
| -C  |     | Showsoutputlistbycolumns. |
| --- | --- | ------------------------- |
-x
Showsoutputlistbylines.
| -d  |     | Showslistingofdirectoryentriesinsteadofcontents |
| --- | --- | ----------------------------------------------- |
-L
Followssymlinks.
| -H  |     | Followssymlinksonthecommandline. |
| --- | --- | -------------------------------- |
-R
Recurse.
99
| AOS-CX10.09DiagnosticsandSupportabilityGuide| | (6200SwitchSeries) |     |
| --------------------------------------------- | ------------------ | --- |

| Parameter |     |     | Description                                      |     |     |
| --------- | --- | --- | ------------------------------------------------ | --- | --- |
| -p        |     |     | Appendsaslash(/)todirectoryentries.              |     |     |
| -F        |     |     | Appendsanindicatortoentries.Anindicatorcanbeasan |     |     |
asterisk(*)orslash(/)orequalsign(=)oratsign(@)orpipe(|).
-l
Showstheoutputinalonglistingformat.
| -i  |     |     | Showsthelistinodenumbers. |     |     |
| --- | --- | --- | ------------------------- | --- | --- |
-n
ShowsalistofnumericUIDsandGIDsinsteadofnames.
| -s  |     |     | Showsalistofallocatedblocks. |     |     |
| --- | --- | --- | ---------------------------- | --- | --- |
-e
Showsinonecolumnalistwiththefulldateandtime.
| -h  |     |     | Showslistsizesinhumanreadableformat(1K,243M,2G)witha |     |     |
| --- | --- | --- | ---------------------------------------------------- | --- | --- |
one-columnoutput.
-r
Showsinonecolumnasortinreverseorder.
| -S  |     |     | Showsinonecolumnasortbysize. |     |     |
| --- | --- | --- | ---------------------------- | --- | --- |
-X
Showsintheoutputsortbyextension.
| -v  |     |     | Showsinonecolumnasortbyversion. |     |     |
| --- | --- | --- | ------------------------------- | --- | --- |
-c
With-l,itshowsasortinonecolumnbyctime.
-t
With-l,itshowsasortbymtime.
| -u     |     |     | With-l,sortbyatime.                               |     |     |
| ------ | --- | --- | ------------------------------------------------- | --- | --- |
| -c     |     |     | With-l,itshowsasortinonecolumnbyctime             |     |     |
| -w <N> |     |     | Assumesthattheterminalhasthenumberofcolumnswideas |     |     |
specifiedby<N>.
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
CommandHistory
ServiceOS|100

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
md5sum
| md5sum [-c | | -s | -w] | [<FILE-NAME>] |     |
| ---------- | ---------- | ------------- | --- |
Description
ThiscommandcomputesandcheckstheMD5messagedigest.
| Parameter |          |     | Description |
| --------- | -------- | --- | ----------- |
| [-c |     | -s | -w] |     |             |
Selectstheoptionsforthecommand.
| -c  |     |     | Specifiestocheckthesumsagainstthelistinfiles. |
| --- | --- | --- | --------------------------------------------- |
-s
Specifiesnotoutputanything,statuscodeshowssuccess.
| -w  |     |     | Specifiestowarnaboutimproperlyformattedchecksumlines. |
| --- | --- | --- | ----------------------------------------------------- |
<FILE-NAME>
Specifiesthefilenametorunthechecksumagainst.
Example
ComputingandcheckingtheMD5messagedigestfor/nos/primary.swi:
SVOS>
md5sum /nos/primary.swi
| 93ffc89e7ec357854704d8e450c4b7ab |     |     | /nos/primary.swi |
| -------------------------------- | --- | --- | ---------------- |
SVOS>
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
mkdir
101
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
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
ServiceOS|102

| SVOS> mount | all |     |
| ----------- | --- | --- |
SVOS>
mount usb
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
| Parameter |     | Description                            |
| --------- | --- | -------------------------------------- |
| -f        |     | Specifiesnottopromptbeforeoverwriting. |
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
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
103
| AOS-CX10.09DiagnosticsandSupportabilityGuide| | (6200SwitchSeries) |     |
| --------------------------------------------- | ------------------ | --- |

| password | (svos) |     |     |     |
| -------- | ------ | --- | --- | --- |
password
Description
SetstheadminuseraccountpasswordforbothServiceOSandAOS-CXoncetheuserbootsintoAOS-CX
andsavestheconfiguration.Thiswilloverwritethepreviouspasswordifoneexists.Userinputismasked
withasterisks.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Settingtheadminaccountpassword:
| SVOS> password          |                   |     |     |     |
| ----------------------- | ----------------- | --- | --- | --- |
| Enter password:******** |                   |     |     |     |
| Confirm                 | password:******** |     |     |     |
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
ping (svos)
ping <HOST-IP-ADDRESS>
Description
Pingsnetworkhostsfordebugpurposes.
| Parameter         |     |     | Description                |     |
| ----------------- | --- | --- | -------------------------- | --- |
| <HOST-IP-ADDRESS> |     |     | SpecifiesthehostIPaddress. |     |
Example
Pinginganetworkhost:
| SVOS> ping     | 10.0.8.10       |              |            |     |
| -------------- | --------------- | ------------ | ---------- | --- |
| PING 10.0.8.10 | (10.0.8.10):    | 56 data      | bytes      |     |
| 64 bytes       | from 10.0.8.10: | seq=0 ttl=63 | time=3.496 | ms  |
| 64 bytes       | from 10.0.8.10: | seq=1 ttl=63 | time=0.367 | ms  |
| 64 bytes       | from 10.0.8.10: | seq=2 ttl=63 | time=0.380 | ms  |
ServiceOS|104

| 64 bytes | from 10.0.8.10: | seq=3 | ttl=63 | time=0.282 | ms  |
| -------- | --------------- | ----- | ------ | ---------- | --- |
| 64 bytes | from 10.0.8.10: | seq=4 | ttl=63 | time=0.669 | ms  |
^C
| --- 10.0.8.10 | ping statistics |                     | ---       |     |             |
| ------------- | --------------- | ------------------- | --------- | --- | ----------- |
| 5 packets     | transmitted,    | 5 packets           | received, | 0%  | packet loss |
| round-trip    | min/avg/max     | = 0.282/1.038/3.496 |           | ms  |             |
SVOS>
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
reboot
reboot
105
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
[-f | -i | -R | -r] Selectstheoptionsforremovingfilesordirectories.
| -f   |     |     | Neverpromptbeforeremovingfilesordirectories.  |
| ---- | --- | --- | --------------------------------------------- |
| -i   |     |     | Alwayspromptbeforeremovingfilesordirectories. |
| -R | | -r  |     | Recursive.                                    |
Example
Removingthefilenamedfoo:
| SVOS> | rm foo |     |     |
| ----- | ------ | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
ServiceOS|106

CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
secure-mode
| secure-mode | <enhanced | | standard | | status> |
| ----------- | --------- | ---------- | --------- |
Description
Setsthesecuremodetoenhancedorstandardsecuremode.Alsocandisplaythecurrentsecuremode.A
zeroizationisrequiredbeforeswitchingbetweenenhancedandstandardsecuremodes.
Thecommandalsodisplaysamessagenotifyingtheuserthattheyarealreadyinthetargetedsecuremode.
Example
Settingthesecuremodetoenhancedorstandard:
107
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |
| --------------------------------------------- | --- | --- | ------------------ |

| SVOS> secure-mode |             |     | --help    |     |          |     |         |     |     |
| ----------------- | ----------- | --- | --------- | --- | -------- | --- | ------- | --- | --- |
| Usage:            | secure-mode |     | <enhanced | |   | standard | |   | status> |     |     |
Set or retrieve the secure mode setting. Requires a zeroization to change modes.
SVOS>
```
```
| SVOS> secure-mode |     |     | enhanced |     |     |     |     |     |     |
| ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
| This will    | set         | the     | switch      | into      | enhanced | secure   | mode.   | Before      |       |
| ------------ | ----------- | ------- | ----------- | --------- | -------- | -------- | ------- | ----------- | ----- |
| enhanced     | secure      | mode    | is enabled, |           | the      | switch   | must    | securely    | erase |
| all customer |             | data    | and reset   | the       | switch   | to       | factory | defaults.   |       |
| This will    | initiate    |         | a reboot    | and       | render   | the      | switch  | unavailable |       |
| until the    | zeroization |         | is          | complete. |          |          |         |             |       |
| This should  | take        | several |             | minutes   | to       | one hour | to      | complete.   |       |
############################WARNING############################
| Continue | (y/n)?     | y   |        |     |     |     |     |     |     |
| -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
| reboot:  | Restarting |     | system |     |     |     |     |     |     |
```
```
| SVOS> secure-mode |     |     | standard |     |     |     |     |     |     |
| ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
| This will    | set         | the     | switch      | into      | standard | secure   | mode.   | Before      |       |
| ------------ | ----------- | ------- | ----------- | --------- | -------- | -------- | ------- | ----------- | ----- |
| standard     | secure      | mode    | is enabled, |           | the      | switch   | must    | securely    | erase |
| all customer |             | data    | and reset   | the       | switch   | to       | factory | defaults.   |       |
| This will    | initiate    |         | a reboot    | and       | render   | the      | switch  | unavailable |       |
| until the    | zeroization |         | is          | complete. |          |          |         |             |       |
| This should  | take        | several |             | minutes   | to       | one hour | to      | complete.   |       |
############################WARNING############################
| Continue | (y/n)?     | y   |        |     |     |     |     |     |     |
| -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
| reboot:  | Restarting |     | system |     |     |     |     |     |     |
```
```
| SVOS> secure-mode |     |     | standard |     |     |     |     |     |     |
| ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
| Secure       | mode is         | already | set       | to        | standard. |          | Setting | it again    | will  |
| ------------ | --------------- | ------- | --------- | --------- | --------- | -------- | ------- | ----------- | ----- |
| repeat       | the zeroization |         | process.  |           | The       | switch   | must    | securely    | erase |
| all customer |                 | data    | and reset | the       | switch    | to       | factory | defaults.   |       |
| This will    | initiate        |         | a reboot  | and       | render    | the      | switch  | unavailable |       |
| until the    | zeroization     |         | is        | complete. |           |          |         |             |       |
| This should  | take            | several |           | minutes   | to        | one hour | to      | complete.   |       |
############################WARNING############################
| Continue | (y/n)?     | y   |        |     |     |     |     |     |     |
| -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
| reboot:  | Restarting |     | system |     |     |     |     |     |     |
```
```
| SVOS> secure-mode |        |      | status  |     |     |     |     |     |     |
| ----------------- | ------ | ---- | ------- | --- | --- | --- | --- | --- | --- |
| enhanced          | secure | mode | is set. |     |     |     |     |     |     |
SVOS>
CommandHistory
ServiceOS|108

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sh
sh
Description
Launchesabashshellforsupportpurposes.Toquitbash,enterexit.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Launchingabashshell:
| SVOS> sh |     |     |
| -------- | --- | --- |
switch:/cli/fs/home#
CommandHistory
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
109
| AOS-CX10.09DiagnosticsandSupportabilityGuide| | (6200SwitchSeries) |     |
| --------------------------------------------- | ------------------ | --- |

Examples
Unmountingalldevices:
SVOS>
umount all
| SVOS> umount | usb |     |
| ------------ | --- | --- |
UnmountingaUSBdevice:
| SVOS> umount | all |     |
| ------------ | --- | --- |
| SVOS> umount | usb |     |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
update
| update {primary | | secondary} | <IMAGE> |
| --------------- | ------------ | ------- |
Description
Verifiesandinstallsaproductimage.Theusercanselecttheprimaryorsecondarybootprofiletoupdate
andthelocationofthefile.
Parameter Description
{primary | secondary} Selectseithertheprimaryorsecondaryimage.
<IMAGE> Specifiestheimagename.
Examples
UpdatingthesoftwareimageusingTFTP:
TheOOBMportisdisabledonfirstbootandmustbeenabledusingtheipcommand.
| SVOS> ip     | dhcp           |     |
| ------------ | -------------- | --- |
| SVOS> ip     | show           |     |
| Interface    | : Link Up      |     |
| IP Address   | : 192.0.2.22   |     |
| Subnet Mask: | 255.255.200.20 |     |
| Gateway      | : 10.0.24.1    |     |
ServiceOS|110

| SVOS> tftp | -g -r XL.10.00.0001.swi | -l image.swi | 192.4.8.10 |
| ---------- | ----------------------- | ------------ | ---------- |
XL.10.00.0001.swi 100% |*******************************| 178M 0:00:00 ETA
| SVOS> ls |     |     |     |
| -------- | --- | --- | --- |
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
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
tftp
tftp {-b | -g | -l <LOCAL-FILE> | -p | -r <REMOTE-FILE>} host [<PORT>]
Description
Transfersfilestoandfromaremotemachine(TFTPafile).
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
{-b | -g | -l | -p | -r <REMOTE-FILE>} Selectstheoptionsfortransferringafile.
| -b  |     | Specifiesthetransferblocksofsizeoctets.Thedefault |     |
| --- | --- | ------------------------------------------------- | --- |
blocksizeissetto1468,whichcanbeoverriddenwiththe-b
option.
-g
Specifiestogetafile.
111
| AOS-CX10.09DiagnosticsandSupportabilityGuide| | (6200SwitchSeries) |     |     |
| --------------------------------------------- | ------------------ | --- | --- |

| Parameter        |     |     | Description                          |     |
| ---------------- | --- | --- | ------------------------------------ | --- |
| -l               |     |     | Specifiesalocalfile.                 |     |
| -p               |     |     | Specifiestoputafileinremotelocation. |     |
| -r <REMOTE-FILE> |     |     | Specifiesaremotefile.                |     |
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
6200 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| version (ServiceOS) |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
version
Description
Displaysthefollowingbuildstrings:
Version.
n
n Builddate.
n Buildtime.
n BuildID.
n SHA.
Example
Displayingversionbuildstrings:
| SVOS> version |              |               |     |     |
| ------------- | ------------ | ------------- | --- | --- |
| ServiceOS     | Information: |               |     |     |
| Version:      |              | GT.01.01.0001 |     |     |
ServiceOS|112

| Build | Date: | 2017-07-19                                        | 14:52:31 PDT |
| ----- | ----- | ------------------------------------------------- | ------------ |
| Build | ID:   | ServiceOS:GT.01.01.0001:461519208911:201707191452 |              |
| SHA:  |       | 46151920891195cdb2267ea6889a3c6cbc3d4193          |              |
SVOS>
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
113
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |
| --------------------------------------------- | --- | --- | ------------------ |

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
114
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

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
In-SystemProgramming|115

Chapter 15

Selftest

Selftest

Power On Self Test (POST) is the first task which verifies the hardware functionality of various modules
during boot-up. Based on the criticality of the test, the selftest module decides whether to go ahead with the
boot-up sequence of a particular subsystem or interface during a POST failure.

POST comprises of the following:

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

POST runs memory built-in selftest (BISTs) and front-end port loopback tests. Memory BISTs verify the
internal and external memory blocks present in the module. The memory tables are critical for proper
functionality of the system so any failures in these tests results in the corresponding subsystem to be
marked as "Failed" and thus that subsystem is not available for use.

Front-end port loopback tests verify the physical port front-end interface. These tests check if a particular
interface can function properly. A test failure means that a particular interface has been marked as "Failed"
and is now unavailable for use.

Examples

Enabling fastboot:

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

116

| switch# | configure terminal |     |
| ------- | ------------------ | --- |
switch(config)#
fastboot
| switch(config)# | end                 |     |
| --------------- | ------------------- | --- |
| switch#         | show running-config |     |
| Current         | configuration:      |     |
!
| !Version   | AOS-CX ML.10.06.0001 |        |
| ---------- | -------------------- | ------ |
| module 1/1 | product-number       | jl726a |
!
!
!
!
!
!
!
vlan 1
| interface   | 1/1/1 |     |
| ----------- | ----- | --- |
| no shutdown |       |     |
Disablingfastboot:
| switch# | configure terminal |     |
| ------- | ------------------ | --- |
switch(config)#
|                 | no fastboot |     |
| --------------- | ----------- | --- |
| switch(config)# | end         |     |
| switch(config)# | write mem   |     |
Configuration changes will take time to process, please be patient.
| switch# | show running-config |     |
| ------- | ------------------- | --- |
| Current | configuration:      |     |
!
| !Version   | AOS-CX ML.10.06.0001 |        |
| ---------- | -------------------- | ------ |
| module 1/1 | product-number       | jl726a |
!
!
!
no fastboot
!
!
!
!
vlan 1
| interface   | 1/1/1 |     |
| ----------- | ----- | --- |
| no shutdown |       |     |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show selftest
Selftest|117

| show selftest | [brief]     |     |              |     |           |         |
| ------------- | ----------- | --- | ------------ | --- | --------- | ------- |
| show selftest | line-module |     | <SLOT-ID>    |     |           |         |
| show selftest | line-module |     | <SLOT-ID>    |     | interface | [brief] |
| show selftest | interface   |     | [<PORT-NUM>] |     |           |         |
Description
Displaysselftestresults.
| Parameter |     |     |     |     | Description                                         |     |
| --------- | --- | --- | --- | --- | --------------------------------------------------- | --- |
| [brief]   |     |     |     |     | Showstheselftestresultsasabriefdescription.Default. |     |
line-module
Showstheselftestresultsforalinemodule.
<SLOT-ID> ShowstheselftestresultsfortheslotIDofthelineorfabric
module.
| <PORT-NUM> |     |     |     |     | Showstheselftestresultsfortheportnumber. |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------- | --- |
Examples
Displayingtheoutputwhenfastbootisenabled:
| switch#    | show     | selftest       |               |            |     |                     |
| ---------- | -------- | -------------- | ------------- | ---------- | --- | ------------------- |
| Name       | Id       | Status         |               | ErrorCode  |     | LastRunTime         |
| ---------- | ----     | -------------- |               | ---------- |     | ------------------- |
| LineModule | 1/1      | passed         |               | 0x0        |     |                     |
| LineModule | 1/2      | passed         |               | 0x0        |     |                     |
| Fabric     | 1/1      | passed         |               | 0x0        |     |                     |
| Fabric     | 1/2      | passed         |               | 0x0        |     |                     |
| switch#    | show     | selftest       | line-module   |            |     |                     |
| Name       | Id       | Status         |               | ErrorCode  |     | LastRunTime         |
| ---------- | ----     | -------------- |               | ---------  |     | ------------------- |
| LineModule | 1/1      | passed         |               | 0x0        |     |                     |
| LineModule | 1/2      | passed         |               | 0x0        |     |                     |
| switch#    | show     | selftest       | fabric-module |            |     |                     |
| Name       | Id       | Status         |               | ErrorCode  |     | LastRunTime         |
| ---------- | ----     | -------------- |               | ---------- |     | ------------------- |
| Fabric     | 1/1      | passed         |               | 0x0        |     |                     |
| Fabric     | 1/2      | passed         |               | 0x0        |     |                     |
| switch#    | show     | selftest       | fabric-module |            | 1/2 |                     |
| Name       | Id       | Status         |               | ErrorCode  |     | LastRunTime         |
| ------     | -------- | -------------- |               | ---------  |     | ------------------- |
| Fabric     | 1/2      | passed         |               | 0x0        |     |                     |
| switch#    | show     | selftest       | line-module   |            | 1/1 |                     |
| Name       | Id       | Status         |               | ErrorCode  |     | LastRunTime         |
| ---------- | ----     | -------------- |               | ---------  |     | ------------------- |
| LineModule | 1/1      | passed         |               | 0x0        |     |                     |
Displayingtheoutputwhenfastbootisenabled:
| switch# | show           | selftest | interface | 1/1/2 |                     |     |
| ------- | -------------- | -------- | --------- | ----- | ------------------- | --- |
| Name    | Status         |          | ErrorCode |       | LastRunTime         |     |
| ------- | -------------- |          | --------- |       | ------------------- |     |
118
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- |

| 1/1/2   | skipped        | 0x0         |                     |     |
| ------- | -------------- | ----------- | ------------------- | --- |
| switch# | show selftest  | line-module | 1/1 interface       |     |
| Name    | Status         | ErrorCode   | LastRunTime         |     |
| ------- | -------------- | ---------   | ------------------- |     |
| 1/1/1   | skipped        | 0x0         |                     |     |
| 1/1/2   | skipped        | 0x0         |                     |     |
| 1/1/3   | skipped        | 0x0         |                     |     |
| 1/1/31  | skipped        | 0x0         |                     |     |
Displayingtheoutputwhenfastbootisdisabled:
switch#
show selftest
| Name       | Id Status           |     | ErrorCode LastRunTime          |          |
| ---------- | ------------------- | --- | ------------------------------ | -------- |
| ---------- | ---- -------------- |     | ---------- ------------------- |          |
| LineModule | 1/1 passed          |     | 0x0 2018-02-16                 | 18:15:53 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Selftest|119

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
120
AOS-CX10.09DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

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
Zeroization|121

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
122
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

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
TerminalMonitor|123

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
124
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
TerminalMonitor|125

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
enabledonthemgmtVRF.
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
Whenthesessionidletimeoutexpires,thesessionisterminatedautomatically.
126
| AOS-CX10.09DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions, Web UI sessions, and real-time notification subscriptions.

Troubleshooting Web UI and REST API Access Issues | 127

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

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.htm

Airheads social
forums and
Knowledge
Base

AOS-CX Switch
Software
Documentation
Portal

Aruba
Hardware
Documentation
and
Translations

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

128

Portal

Aruba software

https://asp.arubanetworks.com/downloads

Software
licensing

End-of-Life
information

Aruba
Developer Hub

https://lms.arubanetworks.com/

https://www.arubanetworks.com/support-services/end-of-life/

https://developer.arubanetworks.com/

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

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

Support and Other Resources | 129

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

AOS-CX 10.09 Diagnostics and Supportability Guide | (6200 Switch Series)

130