AOS-CX 10.11 Diagnostics and
Supportability Guide

6200 Switch Series

Published: May 2023
Edition: 3

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

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

| 2

Contents
Contents
| Contents                                          |                                                    | 3   |
| ------------------------------------------------- | -------------------------------------------------- | --- |
| About                                             | this document                                      | 7   |
| Applicableproducts                                |                                                    | 7   |
| Latestversionavailableonline                      |                                                    | 7   |
| Commandsyntaxnotationconventions                  |                                                    | 7   |
| Abouttheexamples                                  |                                                    | 8   |
| Identifyingswitchportsandinterfaces               |                                                    | 8   |
| Debug                                             | logging                                            | 10  |
| Debugloggingcommands                              |                                                    | 10  |
|                                                   | cleardebugbuffer                                   | 10  |
|                                                   | debug{all|<MODULE-NAME>}                           | 11  |
|                                                   | debugdb                                            | 12  |
|                                                   | debugdestination                                   | 15  |
|                                                   | showdebug                                          | 16  |
|                                                   | showdebugbuffer                                    | 17  |
|                                                   | showdebugbuffervsf                                 | 18  |
|                                                   | showdebugdestination                               | 19  |
| Log Rotation                                      |                                                    | 20  |
| Logfilepaths                                      |                                                    | 20  |
| Aboutrotatedlogfiles                              |                                                    | 20  |
| Changingthesizeofthelogrotationfile               |                                                    | 20  |
| Changingthetimefrequencyforlogrotation            |                                                    | 21  |
| Resettingthetimefrequencytodaily                  |                                                    | 21  |
| Identifyingaremotehostforreceivingrotatedlogfiles |                                                    | 21  |
| Remotetransferofrotatedlogfiles                   |                                                    | 22  |
| Resettingtheremotehostforreceivingrotatedlogfiles |                                                    | 22  |
| Resettingthesizeofthelogrotationfile              |                                                    | 23  |
| Verifyingthelogrotationparameters                 |                                                    | 23  |
| Logrotationtroubleshooting                        |                                                    | 24  |
|                                                   | Logfilesnottransferredremotely                     | 24  |
|                                                   | Logrotationnotoccurringimmediatelyaftermaxfilesize | 24  |
|                                                   | Logrotationnotoccurringregardlessofperiod          | 24  |
| Logrotationcommands                               |                                                    | 25  |
|                                                   | loggingthreshold                                   | 25  |
|                                                   | logrotatemaxsize                                   | 27  |
|                                                   | logrotateperiod                                    | 27  |
|                                                   | logrotatetarget                                    | 28  |
|                                                   | showlogrotate                                      | 30  |
| Reboot                                            | reasons                                            | 31  |
| Event                                             | Logs                                               | 33  |
| Showingandclearingevents                          |                                                    | 33  |
3
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Client                                 | Filter                           |           | 34  |
| -------------------------------------- | -------------------------------- | --------- | --- |
| Logmessages                            |                                  |           | 34  |
| Network                                | Configuration                    | Validator | 35  |
| Showingandclearingevents               |                                  |           | 35  |
| Networkconfigurationvalidationcommands |                                  |           | 35  |
|                                        | switchconfig-validator           |           | 35  |
| Cable                                  | Diagnostics                      |           | 37  |
| HowTDRworksonAOS-CXplatforms           |                                  |           | 37  |
| Cablediagnosticstests                  |                                  |           | 37  |
| Cablediagnosticcommands                |                                  |           | 38  |
|                                        | diagcable-diagnostic             |           | 38  |
| Supportability                         | Copy                             |           | 42  |
| Supportabilitycopycommands             |                                  |           | 42  |
|                                        | copycheckpoint                   |           | 42  |
|                                        | copycommand-output               |           | 43  |
|                                        | copycore-dumpvsfmemberdaemon     |           | 44  |
|                                        | copycore-dumpvsfmemberkernel     |           | 45  |
|                                        | copydiag-dumpfeature<FEATURE>    |           | 46  |
|                                        | copydiag-dumplocal-file          |           | 47  |
|                                        | copydiag-dumpvsfmemberlocal-file |           | 49  |
|                                        | copy<IMAGE>                      |           | 50  |
|                                        | copyrunning-config               |           | 51  |
|                                        | copyshow-techfeature             |           | 52  |
|                                        | copyshow-techlocal-file          |           | 53  |
|                                        | copyshow-techvsfmemberlocal-file |           | 54  |
|                                        | copystartup-config               |           | 55  |
|                                        | copysupport-files                |           | 56  |
|                                        | copysupport-fileslocal-file      |           | 58  |
|                                        | copysupport-filesvsfmember       |           | 59  |
|                                        | copysupport-log                  |           | 60  |
|                                        | copysupport-logvsfmember         |           | 62  |
| Traceroute                             |                                  |           | 64  |
| Traceroutecommands                     |                                  |           | 64  |
|                                        | traceroute                       |           | 64  |
|                                        | traceroute6                      |           | 66  |
| Ping                                   |                                  |           | 69  |
| Pingcommands                           |                                  |           | 69  |
|                                        | ping                             |           | 69  |
|                                        | ping6                            |           | 74  |
| Troubleshooting                        |                                  |           | 77  |
|                                        | Operationnotpermitted            |           | 77  |
|                                        | Networkisunreachable             |           | 77  |
|                                        | Destinationhostunreachable       |           | 78  |
| Remote                                 | syslog                           |           | 79  |
| Remotesyslogcommands                   |                                  |           | 79  |
|                                        | clearaccounting-logs             |           | 79  |
|                                        | logging                          |           | 80  |
|                                        | loggingaccounting-format-native  |           | 82  |
|                                        | loggingfilter                    |           | 83  |
Contents|4

|                                     | loggingfacility           | 86  |
| ----------------------------------- | ------------------------- | --- |
|                                     | loggingpersistent-storage | 87  |
| Runtime                             | Diagnostics               | 89  |
| Runtimediagnosticcommands           |                           | 89  |
|                                     | diagnosticmonitor         | 89  |
|                                     | diagon-demand             | 90  |
|                                     | showdiagnostic            | 91  |
|                                     | showdiagnosticevents      | 92  |
| Service                             | OS                        | 93  |
| ServiceOSCLIlogin                   |                           | 93  |
| ServiceOSuseraccounts               |                           | 94  |
| ServiceOSbootmenu                   |                           | 94  |
| Consoleconfiguration                |                           | 95  |
| AOS-CXboot                          |                           | 95  |
| Filesystemaccess                    |                           | 96  |
| ServiceOSmountfailure               |                           | 97  |
| ServiceOSCLIcommandlist             |                           | 97  |
| ServiceOSCLIfeaturesandlimitations  |                           | 98  |
| ServiceOSCLIcommands                |                           | 98  |
|                                     | boot                      | 98  |
|                                     | cat                       | 99  |
|                                     | cdpath                    | 100 |
|                                     | config-clear              | 100 |
|                                     | cp                        | 101 |
|                                     | du                        | 102 |
|                                     | erasezeroize              | 103 |
|                                     | exit                      | 104 |
|                                     | format                    | 105 |
|                                     | identify                  | 106 |
|                                     | ip                        | 106 |
|                                     | ls                        | 107 |
|                                     | md5sum                    | 109 |
|                                     | mkdir                     | 110 |
|                                     | mount                     | 111 |
|                                     | mv                        | 111 |
|                                     | password(svos)            | 112 |
|                                     | ping                      | 113 |
|                                     | pwd                       | 113 |
|                                     | reboot                    | 114 |
|                                     | rm                        | 114 |
|                                     | rmdir                     | 115 |
|                                     | secure-mode               | 116 |
|                                     | sh                        | 117 |
|                                     | umount                    | 118 |
|                                     | update                    | 119 |
|                                     | tftp                      | 120 |
|                                     | version                   | 121 |
| In-System                           | Programming               | 122 |
| ShowtechcommandlistfortheISPfeature |                           | 122 |
| In-SystemProgrammingcommands        |                           | 122 |
|                                     | clearupdate-log           | 122 |
|                                     | showneeded-updates        | 122 |
5
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Selftest                                      |                                          |           |             |            |        | 124 |
| --------------------------------------------- | ---------------------------------------- | --------- | ----------- | ---------- | ------ | --- |
| Selftestcommands                              |                                          |           |             |            |        | 124 |
|                                               | fastboot                                 |           |             |            |        | 124 |
|                                               | showselftest                             |           |             |            |        | 125 |
| Zeroization                                   |                                          |           |             |            |        | 128 |
| Zeroizationcommands                           |                                          |           |             |            |        | 128 |
|                                               | eraseallzeroize                          |           |             |            |        | 128 |
| Terminal                                      | Monitor                                  |           |             |            |        | 131 |
| Terminalmonitorcommands                       |                                          |           |             |            |        | 131 |
|                                               | loggingconsole{notify|severity|filter}   |           |             |            |        | 131 |
|                                               | showterminal-monitor                     |           |             |            |        | 132 |
|                                               | terminal-monitor{notify|severity|filter} |           |             |            |        | 133 |
| Troubleshooting                               |                                          | Web       | UI and REST | API Access | Issues | 135 |
| HTTP404errorwhenaccessingtheswitchURL         |                                          |           |             |            |        | 135 |
| HTTP401error"Loginfailed:sessionlimitreached" |                                          |           |             |            |        | 135 |
| Support                                       | and Other                                | Resources |             |            |        | 137 |
| AccessingArubaSupport                         |                                          |           |             |            |        | 137 |
| AccessingUpdates                              |                                          |           |             |            |        | 138 |
|                                               | ArubaSupportPortal                       |           |             |            |        | 138 |
|                                               | MyNetworking                             |           |             |            |        | 138 |
| WarrantyInformation                           |                                          |           |             |            |        | 138 |
| RegulatoryInformation                         |                                          |           |             |            |        | 138 |
| DocumentationFeedback                         |                                          |           |             |            |        | 139 |
Contents|6

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A,R8Q67A,R8Q68A,R8Q69A,R8Q70A,
R8Q71A,R8V08A,R8V09A,R8V10A,R8V11A,R8V12A,R8Q72A)
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Items
thatappearliketheexampletextinthepreviouscolumnaretobeentered
exactlyasshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
<example-text> substitutewithanactualvalueinacommandorincode:
n
n <example-text>
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ------------------------------------------------------------ | --- |
n example-text
areenclosedinanglebrackets(< >).Substitutethetext—including
n example-text
theenclosinganglebrackets—withanactualvalue.
|     |     | n Foroutputformatswhereitalictextcanbedisplayed,variables |     |
| --- | --- | --------------------------------------------------------- | --- |
mightormightnotbeenclosedinanglebrackets.Substitutethe
textincludingtheenclosinganglebrackets,ifany,withanactual
value.
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
7
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchor
environment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understanding | the CLI prompts |     |     |
| ------------- | --------------- | --- | --- |
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
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,whenin
theVLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6200 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|8

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

9

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
| poll | interval | changed | to 32 |
| ---- | -------- | ------- | ----- |
switch#
|         | clear | debug buffer |     |
| ------- | ----- | ------------ | --- |
| switch# | show  | debug buffer |     |
----------------------------------------------------------------------------------
----------------------------
10
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |
| --------------------------------------------- | --- | --- | ------------------ |

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
| Platforms      | Command     |         | context | Authority    |     |     |
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
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
all
Enablesdebugloggingforallmodules.
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
| crit |     |     |     | Specifiesstorageofdebuglogswithseveritylevelofcritical |     |     |
| ---- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
andabove.
Debuglogging|11

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
alert
Specifiesstorageofdebuglogswithseveritylevelofalertand
above.
| err |     |     | Specifiesstorageofdebuglogswithseverityleveloferrorand |
| --- | --- | --- | ------------------------------------------------------ |
above.
notice Specifiesstorageofdebuglogswithseveritylevelofnoticeand
above.
warning Specifiesstorageofdebuglogswithseveritylevelofwarningand
above.
| info |     |     | Specifiesstorageofdebuglogswithseveritylevelofinfoand |
| ---- | --- | --- | ----------------------------------------------------- |
above.
| debug |     |     | Specifiesstorageofdebuglogswithseveritylevelofdebug |
| ----- | --- | --- | --------------------------------------------------- |
(default).
| port |     |     | Displaysdebuglogsforthespecifiedport,forexample1/1/1. |
| ---- | --- | --- | ----------------------------------------------------- |
vlan <VLAN-ID>
DisplaysdebuglogsforthespecifiedVLAN.ProvideaVLANfrom1
to4094.
| ip <IP-ADDRESS> |     |     | DisplaysdebuglogsforthespecifiedIPAddress. |
| --------------- | --- | --- | ------------------------------------------ |
mac <MAC-ADDRESS> DisplaysdebuglogsforthespecifiedMACAddress,forexample
A:B:C:D:E:F.
vrf <VRF-NAME>
DisplaysdebuglogsforthespecifiedVRF.
instance <INSTANCE-ID> Displaysdebuglogsforthespecifiedinstance.Provideaninstance
IDfrom1to255.
Examples
| switch#             | debug all |         |              |
| ------------------- | --------- | ------- | ------------ |
| Command History     |           |         |              |
| Release             |           |         | Modification |
| 10.07orearlier      |           |         | --           |
| Command Information |           |         |              |
| Platforms           | Command   | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
debug db
12
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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

DBlog is a high performance, configuration, and state database server logging infrastructure where a
user can log the transactions which are sent or received by clients to the configuration and state
database server. It can be enabled through the CLI and REST, and also supports filters where a user can
filter out logs on the basis of table, column, or client. It is helpful for debugging when the user wants to
debug an issue with a particular client, table, or column combination. It is not enabled by default. A
combination of filters can also be applied to filter out messages based on table, column, and client.

Debug logging | 13

Therearethreesubmodulesforthe"db"module:
1. all:WhenAllisenabled,nofiltersareappliedtoanyofthedebuglogs,evenifothersubmodules
areconfiguredwithfilters.
2. tx:Ifenabled,onlytherepliesandnotificationssentoutfortheinitialandincrementalupdates
arelogged.
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
| switch# | debug db all | severity debug |     |
| ------- | ------------ | -------------- | --- |
Configuringthetxsubmodulewithtable Interfacefilterandseveritydebug:
| switch# | debug db tx | table Interface | severity debug |
| ------- | ----------- | --------------- | -------------- |
Configuringtherxsubmodulewithtable Interface column statisticsfilterandseveritydebug:
switch# debug db rx table Interface column statistics severity debug
Disablingtherxsubmodule:
| switch#                      | no debug db | rx                 |              |
| ---------------------------- | ----------- | ------------------ | ------------ |
| Disablingthetxsubmoduletable |             | Interface:         |              |
| switch#                      | no debug db | tx table Interface |              |
| Command                      | History     |                    |              |
| Release                      |             |                    | Modification |
| 10.07orearlier               |             |                    | --           |
| Command                      | Information |                    |              |
14
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
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
| syslog  |     |     | Specifiesthatthedebuglogsarestoredinthesyslog. |     |
| ------- | --- | --- | ---------------------------------------------- | --- |
| file    |     |     | Specifiesthatdebuglogsarestoredinfile.         |     |
| console |     |     | Specifiesthatdebuglogsarestoredinconsole.      |     |
buffer
Specifiesthatdebuglogsarestoredinbuffer(default).
severity (emer|crit|alert|err| Selectstheminimumseverityloglevelforthedestination.Ifa
notice|warning|info|debug)
severityisnotprovided,thedefaultloglevelisdebug.
Optional.
| emer |     |     | Specifiesstorageofdebuglogswithaseveritylevelof |     |
| ---- | --- | --- | ----------------------------------------------- | --- |
emergencyonly.
| crit |     |     | Specifiesstorageofdebuglogswithseveritylevelof |     |
| ---- | --- | --- | ---------------------------------------------- | --- |
criticalandabove.
| alert |     |     | Specifiesstorageofdebuglogswithseveritylevelofalert |     |
| ----- | --- | --- | --------------------------------------------------- | --- |
andabove.
| err |     |     | Specifiesstorageofdebuglogswithseverityleveloferror |     |
| --- | --- | --- | --------------------------------------------------- | --- |
andabove.
| notice |     |     | Specifiesstorageofdebuglogswithseveritylevelofnotice |     |
| ------ | --- | --- | ---------------------------------------------------- | --- |
andabove.
warning Specifiesstorageofdebuglogswithseveritylevelofwarning
andabove.
| info |     |     | Specifiesstorageofdebuglogswithseveritylevelofinfoand |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
above.
| debug |     |     | Specifiesstorageofdebuglogswithseveritylevelofdebug |     |
| ----- | --- | --- | --------------------------------------------------- | --- |
(default).
Usage
Debuglogging|15

Eventsthathaveaseverityequaltoorhigherthantheconfiguredseveritylevelarestoredinthe
designateddestination.Theproductdefaultstobufferfordestinationanddebugasaseveritylevel.
Examples
| switch#             | debug destination |         | syslog  | severity     | alert   |     |     |
| ------------------- | ----------------- | ------- | ------- | ------------ | ------- | --- | --- |
| switch#             | debug destination |         | console | severity     | info    |     |     |
| switch#             | debug destination |         | file    | severity     | warning |     |     |
| switch#             | debug destination |         | buffer  | severity     | err     |     |     |
| Command History     |                   |         |         |              |         |     |     |
| Release             |                   |         |         | Modification |         |     |     |
| 10.07orearlier      |                   |         |         | --           |         |     |     |
| Command Information |                   |         |         |              |         |     |     |
| Platforms           | Command           | context |         | Authority    |         |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show debug
show debug
Description
Displaystheenableddebugtypes.
Examples
| switch# | show debug |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
--
| module sub_module |     | severity | vlan | port | ip  | mac | instance vrf |
| ----------------- | --- | -------- | ---- | ---- | --- | --- | ------------ |
----------------------------------------------------------------------------------
--
| all | all | err | 1   | 1/1/1 | 10.0.0.1 | 1a:2b:3c:4d:5e:6f | 2   |
| --- | --- | --- | --- | ----- | -------- | ----------------- | --- |
default
| Command History     |     |     |     |              |     |     |     |
| ------------------- | --- | --- | --- | ------------ | --- | --- | --- |
| Release             |     |     |     | Modification |     |     |     |
| 10.07orearlier      |     |     |     | --           |     |     |     |
| Command Information |     |     |     |              |     |     |     |
16
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| interval       | changed to | 20  |              |
| -------------- | ---------- | --- | ------------ |
| Command        | History    |     |              |
| Release        |            |     | Modification |
| 10.07orearlier |            |     | --           |
Debuglogging|17

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show debug | buffer | vsf |     |     |
| ---------- | ------ | --- | --- | --- |
show debug buffer vsf [member <MEMBER-ID>] [{conductor | standby}]
Description
DisplaysVSFmemberdebuglogsstoredinthedebugbuffer,withanoptiontofilterbyVSFmemberand
role.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<MEMBER-ID> Displaysdebuglogsforthespecifiedmember-id.Optional.Range:
1-8.
| conductor |     |     |     | DisplaydebuglogsfortheVSFconductor. |
| --------- | --- | --- | --- | ----------------------------------- |
standby
DisplaydebuglogsfortheVSFstandby.
Examples
DisplayingVSFmemberdebuglogswithmember-id1:
| switch# | show debug | buffer | vsf member | 1   |
| ------- | ---------- | ------ | ---------- | --- |
------------------------------------------------------------------------------
| show debug | buffer |     |     |     |
| ---------- | ------ | --- | --- | --- |
------------------------------------------------------------------------------
2020-12-14:07:53:17.217919|hpe-ledarbd|LOG_DEBUG|MMBR|2|LED|LED|ledarbd_vsf_mbrs_
| check: Checking |     | VSF_Member | table |     |
| --------------- | --- | ---------- | ----- | --- |
DisplayingVSFmemberdebuglogsformemberstateconductor:
| switch# | show debug | buffer | vsf conductor |     |
| ------- | ---------- | ------ | ------------- | --- |
------------------------------------------------------------------------------
| show debug | buffer |     |     |     |
| ---------- | ------ | --- | --- | --- |
------------------------------------------------------------------------------
2020-12-14:07:54:20.469024|hpe-ledarbd|LOG_DEBUG|CDTR|1|LED|LED|ledarbd_pd_
| subsystems_check:   |     | Checking | Subsystem | table                                    |
| ------------------- | --- | -------- | --------- | ---------------------------------------- |
| Command History     |     |          |           |                                          |
| Release             |     |          |           | Modification                             |
| 10.09               |     |          |           | Updatedparameternameforinclusivelanguage |
| 10.07orearlier      |     |          |           | --                                       |
| Command Information |     |          |           |                                          |
18
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show debug             | destination |     |     |
| ---------------------- | ----------- | --- | --- |
| show debug destination |             |     |     |
Description
Displaystheconfigureddebugdestinationandseverity.
Examples
| switch# | show debug | destination |     |
| ------- | ---------- | ----------- | --- |
---------------------------------------------------------------------
|     | show | debug destination |     |
| --- | ---- | ----------------- | --- |
---------------------------------------------------------------------
CONSOLE:info
FILE:warning
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Debuglogging|19

Chapter 3
Log Rotation
Log Rotation
Logrotationprovidesyouwiththeabilitytosystematicallyrotateandarchiveanylogfilesproducedby
thesystem.Logrotationreduceslogspacerequiredontheswitch.Logrotationrotatesandcompresses
thelogfilesbasedonsizeand/orperiod.Rotatedlogfilesarestoredlocallyortransferredtoaremote
hostusingTFTP.
Optionally,notificationscanbetriggeredifalogbufferpercentfullthresholdisexceeded,givingyouthe
opportunitytosavethelogselsewherebeforethebuffersarerotatedwiththeoldestdatabeing
overwritten.
| Log file | paths |     |     |     |
| -------- | ----- | --- | --- | --- |
Logsstoredinthefollowingfilesarerotated:
| Auditlogsarestoredinfile |     | /var/log/audit/audit.log. |     |     |
| ------------------------ | --- | ------------------------- | --- | --- |
n
| n Authenticationlogsarestoredinfile |     |                        | /var/log/auth.log.  |     |
| ----------------------------------- | --- | ---------------------- | ------------------- | --- |
| n Eventlogsarestoredinfile          |     | /var/log/event.log.    |                     |     |
| n HTTPSserverlogsarestoredinfile    |     |                        | /var/log/nginx.log. |     |
| n Securitylogsarestoredinfile       |     | /var/log/security.log. |                     |     |
n NTPlogsarestoredinfile/var/log/ntp.log.
n Logsofbadloginattemptsarestoredin/var/log/btmp.
Logsofthelastloginsessionsarestoredin/var/log/wtmp.
n
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
20
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

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

Log Rotation | 21

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
22
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- |

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
LogRotation|23

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

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

24

Log rotation commands

logging threshold
logging threshold {audit-log | auth-log | commands-log |event-log | security-log | https-
server-log} <THRESHOLD%>
no logging threshold {audit-log | auth-log | commands-log | event-log |
https-server-log} [<THRESHOLD%>]

security-log |

Description

Selects the logging buffer notification threshold for the specified logging buffer. Whenever the logging
buffer space consumption exceeds the selected threshold (percent of buffer capacity), a LOG_BUFFER_
ALMOST_FULL event and SNMP RMON trap is triggered. This gives you the opportunity to save the logs
elsewhere before the buffers are rotated with the oldest data being overwritten.

Also, a LOG_BUFFER_WRAPPED event and SNMP RMON trap is triggered if the logging buffer capacity is
fully consumed and the log buffer is rotated with the oldest data being overwritten.

The no form of this command resets the logging buffer warning threshold to its default. All logs except
audit-log have a default of 90 (percent) and audit-log has a default of 50 (percent).

The largest REST payload that can be sent to RADIUS/TACACS servers is 1024 characters, and the maximum REST

payload that can be sent to syslog servers is 3500 characters. Once this limit is exceeded, the log will display

three dots ( …) to indicate the the message has exceeded the character limit and is incomplete. .

Parameter

audit-log

auth-log

commands-log

event-log

Description

Selects the audit log.

Selects the authentication log.

Configure the logging threshold for commands log buffer

Selects the event log.

https-server-log

Selects the HTTPS server log.

security-log

<THRESHOLD%>

Selects the security log.

Selects the notification threshold as a percent that the selected
logging buffer is full.
Available percent values for all logs except audit-log: 15 30 50
70 90 100
Available percent values for audit-log: 50 100

Examples

Setting the audit log threshold:

switch(config)# logging threshold audit-log 100

Setting the authentication log threshold:

Log Rotation | 25

| switch(config)# | logging | threshold | auth-log | 50  |
| --------------- | ------- | --------- | -------- | --- |
Settingtheeventlogthreshold:
| switch(config)# | logging | threshold | event-log | 70  |
| --------------- | ------- | --------- | --------- | --- |
Settingthesecuritylogthreshold:
| switch(config)# | logging | threshold | security-log | 70  |
| --------------- | ------- | --------- | ------------ | --- |
Resettingtheauditlogthresholdtoitsdefaultof50:
| switch(config)# | no  | logging threshold | audit-log |     |
| --------------- | --- | ----------------- | --------- | --- |
Resettingtheauthenticationlogthresholdtoitsdefaultof90:
| switch(config)# | no  | logging threshold | auth-log |     |
| --------------- | --- | ----------------- | -------- | --- |
Resettingtheeventlogthresholdtoitsdefaultof90:
| switch(config)# | no  | logging threshold | event-log |     |
| --------------- | --- | ----------------- | --------- | --- |
Resettingthesecuritylogthresholdtoitsdefaultof90:
| switch(config)#     | no      | logging threshold | security-log                        |     |
| ------------------- | ------- | ----------------- | ----------------------------------- | --- |
| Command History     |         |                   |                                     |     |
| Release             |         |                   | Modification                        |     |
| 10.11               |         |                   | Introducedthecommands-logparameter. |     |
| 10.09               |         |                   | Commandintroduced.                  |     |
| Command Information |         |                   |                                     |     |
| Platforms           | Command | context           | Authority                           |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
26
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

| logrotate    |         | maxsize    |     |     |     |     |
| ------------ | ------- | ---------- | --- | --- | --- | --- |
| logrotate    | maxsize | <MAX-SIZE> |     |     |     |     |
| no logrotate |         | maxsize    |     |     |     |     |
Description
Specifiesthemaximumallowedlogfilesize.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappens
first),triggersrotationofthelogfile.
Thenoformofthiscommandresetsthesizeofthelogfiletothedefault(100MB).
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MAX-SIZE> Specifiestheallowedsizethelogfilecanreachbeforeitis
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logrotate    |        | period |     |        |           |           |
| ------------ | ------ | ------ | --- | ------ | --------- | --------- |
| logrotate    | period | {daily | |   | hourly | | monthly | | weekly} |
| no logrotate |        | period |     |        |           |           |
Description
Setsthelogfilerotationtimeperiod.Defaultstodaily.
Alogfilethatexceedseitherthelogrotate maxsizeorthelogrotate period(whicheverhappens
first),triggersrotationofthelogfile.
Thenoformofthiscommandresetsthelogrotationperiodtothedefaultofdaily.
LogRotation|27

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
28
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- |

Parameter Description
tftp://{{<IPV4_ADDR>|IPV6_ADDR>}|HOST}
[/<DIRECTORY>]
<VRF_NAME>
SpecifiestheVRFname(Default:default).
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
switch(config)# logrotate target tftp://2001:db8:0:1::128 vrf default
Resettingthetargettolocal:
| switch(config)#     | no      | logrotate | target                       |     |
| ------------------- | ------- | --------- | ---------------------------- | --- |
| Command History     |         |           |                              |     |
| Release             |         |           | Modification                 |     |
| 10.09               |         |           | Updatedthesyntaxandexamples. |     |
| 10.07orearlier      |         |           | --                           |     |
| Command Information |         |           |                              |     |
| Platforms           | Command | context   | Authority                    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
LogRotation|29

show logrotate
show logrotate
Description
Showsthelogrotateconfiguration.
Examples
| switch#        | show logrotate |                            |              |          |
| -------------- | -------------- | -------------------------- | ------------ | -------- |
| Logrotate      | configurations | :                          |              |          |
| Period         |                | : weekly                   |              |          |
| Maxsize        |                | : 20MB                     |              |          |
| Target         |                | : tftp://2001:db8:0:1::128 |              | vrf mgmt |
| Command        | History        |                            |              |          |
| Release        |                |                            | Modification |          |
| 10.07orearlier |                |                            | --           |          |
| Command        | Information    |                            |              |          |
| Platforms      | Command        | context                    | Authority    |          |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
30
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

Chapter 4

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

VSF member renumbered

An user requested a renumber of a VSF member.

VSF switchover requested

An user requested a VSF switchover.

Chassis critical temperature

Chassis operating temperature exceeded.

Chassis insufficient fans

Insufficient fans to cool the chassis.

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

31

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

Reboot reasons | 32

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

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

33

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

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

34

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
| Showing | and clearing | events |     |     |     |
| ------- | ------------ | ------ | --- | --- | --- |
Theclear eventscommandisusedtocleartheeventlogofallevents.Theshow eventscommandis
usedtoshowalleventlogsgeneratedbytheswitchsincethelastreboot.SeetheSwitchsystemand
hardwarecommandschapterchapteroftheFundamentalsGuideforinformationonthesecommands.
ThetimestampforeventlogmessagesgeneratedfromtheServiceOSindicateswhentheeventlog
messagesweretransferredtotheeventlogafteraswitchbootandnotwhentheissueoccurred.
SeetheSecurityGuideforinformationaboutaccountinglogs.
| Network | configuration    | validation | commands |     |     |
| ------- | ---------------- | ---------- | -------- | --- | --- |
| switch  | config-validator |            |          |     |     |
switch config-validator [config <CONFIG-NAME>] [feature <feature>] [mode consistency]
| [format | {cli | json}] |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- |
Description
Runsconfigurationvalidationtodetectconfigurationanomalies.
| Parameter |     | Description                                    |     |     |     |
| --------- | --- | ---------------------------------------------- | --- | --- | --- |
| config    |     | Specifiesconfigurationtobevalidated.Thedefault |     |     |     |
configurationisrunning-config.
| feature<feature> |     | Specifiesthenameofthefeaturetobevalidated.        |     |     |     |
| ---------------- | --- | ------------------------------------------------- | --- | --- | --- |
| mode             |     | Specifiesconfigurationvalidationmode.Thedefaultis |     |     |     |
consistency.
consistency
Validatesfeatureconfigurationforconsistencycheck.
| format |     | Specifiestheresultsdisplayformat.Thedefaultiscli. |     |     |     |
| ------ | --- | ------------------------------------------------- | --- | --- | --- |
Examples
Runningconfigurationvalidationwithalldefaultvalues.
35
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- |

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
| Command   | History     |         |                    |     |
| --------- | ----------- | ------- | ------------------ | --- |
| Release   |             |         | Modification       |     |
| 10.10     |             |         | Commandintroduced. |     |
| Command   | Information |         |                    |     |
| Platforms | Command     | context | Authority          |     |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
NetworkConfigurationValidator|36

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
10G-
| Platforms | 1GbT | 5G-SmartRate |     |
| --------- | ---- | ------------ | --- |
SmartRate
| 6200 | Yes | Yes | -   |
| ---- | --- | --- | --- |
FromAOS-CX10.11,TDRorCableDiagnosticscanalsoberunfromCXAPI.
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
37
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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

Reasons

1GbT

5G-SmartRate

10G-SmartRate

When diagnostic status is not "good" or "failed", distance
to fault is reported within +/-10m.

When diagnostic status is not "good" or "failed", distance
to fault is reported within +/-5m.

When diagnostic status is not "good" or "failed", distance
to fault is reported within +/-5m.

Cable diagnostic commands

diag cable-diagnostic

Cable Diagnostics | 38

diag cable-diagnostic
test <IF-NAME>
show <IF-NAME>
clear <IF-NAME>
Description
Providesinformationaboutthecablehealthafterrunningadiagnostictestonaninterface.
Ifyourunanewcablediagnosticcommandwhenacablediagnosticisinprogressfortheinterface,the
newcablediagnosticcommandfailstoexecute.Insuchascenario,anerrormessageisdisplayed.
Onexecutingacablediagnostictestcommand,itautomaticallyclearstheoldtestresultsbeforethe
newteststarts.
| Parameter      |     | Description                            |     |     |     |
| -------------- | --- | -------------------------------------- | --- | --- | --- |
| <IF-NAME>      |     | Specifiesthenameoftheinterface.        |     |     |     |
| test <IF-NAME> |     | Runsacablediagnostictestonaninterface. |     |     |     |
show <IF-NAME> Displaysthediagnostictestresultforaninterface.
clear <IF-NAME> Clearsthecablediagnostictestresultsforaninterface.
Examples
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
switch#
| diag             | cable-diagnostic | test 1/3/1   |                  |     |     |
| ---------------- | ---------------- | ------------ | ---------------- | --- | --- |
| Cable diagnostic | is not           | supported on | interface 1/3/1. |     |     |
Thefollowingexamplesdisplaythecablediagnostictestresultfor1GbTinterface:
| switch# diag | cable-diagnostic | show 1/3/1 |           |           |      |
| ------------ | ---------------- | ---------- | --------- | --------- | ---- |
|              |                  | Cable      | Impedance | Distance* | MDI  |
| Interface    | Pinout           | Status     | (Ohms)    | (Meters)  | Mode |
--------------------------------------------------------------------
| 1/3/1 | 1-2 | good | 85-115 | 10 +/- 10 | mdi |
| ----- | --- | ---- | ------ | --------- | --- |
39
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| (1GbT) | 3-6 | good |     |     | 85-115 |     | 10 +/- 10 | mdi |
| ------ | --- | ---- | --- | --- | ------ | --- | --------- | --- |
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
| switch# diag | cable-diagnostic |        | show | 1/1/20 |           |           |     |      |
| ------------ | ---------------- | ------ | ---- | ------ | --------- | --------- | --- | ---- |
|              |                  | Cable  |      |        | Impedance | Distance* |     | MDI  |
| Interface    | Pinout           | Status |      |        | (Ohms)    | (Meters)  |     | Mode |
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
| switch# diag | cable-diagnostic |     | show | 1/3/1 |     |     |     |     |
| ------------ | ---------------- | --- | ---- | ----- | --- | --- | --- | --- |
Cable diagnostic test results for interface 1/3/1 are not available.
Thefollowingexampleclearsthecablediagnostictestresultsforthespecifiedinterface:
CableDiagnostics|40

| switch# | diag cable-diagnostic | clear | 1/3/1 |
| ------- | --------------------- | ----- | ----- |
Thefollowingexampledisplaystheerrormessagewhenyouexecuteacablediagnosticcommandwhile
thecurrentdiagnostictestisinprogress:
| switch# | diag cable-diagnostic | clear | 1/3/1 |
| ------- | --------------------- | ----- | ----- |
A cable diagnostic test for interface 1/3/1 is currently in progress.
Runningacablediagnostictestwillresultinabriefinterruptioninconnectivityonalltestedports.
IfagoodcableisusedontheSmartRateports,theDistancetoFault(Meters)valueis0.
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.11               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
41
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Chapter 9

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

Supportability copy commands

copy checkpoint
copy checkpoint <CHECKPOINT-NAME> {<STORAGE-URL> | <REMOTE-URL>}

Description

Copies the checkpoint using TFTP, SFTP, SCP, or USB.

Parameter

Description

<CHECKPOINT-NAME>

Specifies the checkpoint name.

{<STORAGE-URL> | <REMOTE-URL>}

Select either the storage URL or the remote URL for the
destination of the copied command output. Required.

<STORAGE-URL>

<REMOTE-URL>

Specifies the USB to copy command output.
Syntax:
{usb}:/<FILE>

Specifies the URL to copy the command output.
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]

[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP> | <HOST>}

[:<PORT>]/<FILE>

Examples

Copying checkpoint chpt to a remote URL:

switch# copy checkpoint chpt scp://root@10.0.1.1/config vrf mgmt

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

42

| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
copy command-output
copy command-output "<COMMAND>" {<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]}
Description
CopiesthespecifiedcommandoutputusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<COMMAND> Specifiesthecommandfromwhichyouwanttoobtainitsoutput.
Required.Userswithauditorrightscanspecifythesetwo
commandsonly:
show accounting log
show events
{<STORAGE-URL> | <REMOTE-URL> SelecteitherthestorageURLortheremoteURLforthe
[vrf <VRF-NAME>]} destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |
| ------------- | --- | --- | ----------------------------------- |
Syntax:
{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommandoutput. |
| ------------ | --- | --- | -------------------------------------- |
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://<USER>@}{<IP> | <HOST>}[:<PORT>]/<FILE>
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
| Copyingtheoutputfromtheshow |     | eventscommandtoaremoteURL: |     |
| --------------------------- | --- | -------------------------- | --- |
switch# copy command-output "show events" tftp://10.100.0.12/file
SupportabilityCopy|43

Copyingtheoutputfromtheshow techcommandtoaremoteURLwithaVRFnamedmgmt:
switch# copy command-output "show tech" scp://user@10.100.0.12/file vrf mgmt
Copyingtheoutputfromtheshow eventscommandtoafilenamedeventsonaUSBdrive:
| switch#             | copy command-output |         | "show | events"           | usb:/events |     |
| ------------------- | ------------------- | ------- | ----- | ----------------- | ----------- | --- |
| Command History     |                     |         |       |                   |             |     |
| Release             |                     |         |       | Modification      |             |     |
| 10.08               |                     |         |       | AddedSCP support. |             |     |
| 10.07orearlier      |                     |         |       | --                |             |     |
| Command Information |                     |         |       |                   |             |     |
| Platforms           | Command             | context |       | Authority         |             |     |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| copy core-dump |     | vsf member |     | daemon |     |     |
| -------------- | --- | ---------- | --- | ------ | --- | --- |
copy core-dump vsf member <MEMBER-ID> daemon [<DAEMON-NAME> | <DAEMON-NAME>:<INSTANCE-
ID>]
| <REMOTE-URL> | [vrf | <VRF-NAME>] |     |     |     |     |
| ------------ | ---- | ----------- | --- | --- | --- | --- |
copy core-dump vsf member <MEMBER-ID> daemon [<DAEMON-NAME> | <DAEMON-NAME>:<INSTANCE-
ID>]
<STORAGE-URL>
Description
Copiesthecore-dumpfromthespecifieddaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
vsf member <MEMBER-ID> Specifiesthemember-idoftheVSFmember.Required.
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
|     |     |     |     | {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | --- | --------- | ------------------- | --------- |
n
[:<PORT>]/<FILE>
44
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
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
| Platforms                        | Command        | context    | Authority            |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy core-dump |     | vsf member | kernel |
| -------------- | --- | ---------- | ------ |
copy core-dump vsf member <MEMBER-ID> kernel <REMOTE-URL> [vrf <VRF-NAME>]
| copy core-dump | vsf | member <MEMBER-ID> | kernel <STORAGE-URL> |
| -------------- | --- | ------------------ | -------------------- |
Description
Copiesthekernelcore-dumpusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MEMBER-ID>
Specifiesthemember-idoftheVSFmember.Required.
<REMOTE_URL> SpecifiestheremotedestinationURL.Required.Thesyntaxofthe
URListhefollowing:
Syntax:
n {tftp://}{<IP> | <HOST>}[:<PORT>]
SupportabilityCopy|45

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
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
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel sftp://abc@10.0.14.206/kernel.tar.gz
vrf mgmt
CopyingthekernelcoredumptotheURLwithaVRFnamedmgmt:
switch# copy core-dump vsf member 3 kernel scp://abc@10.0.14.206/kernel.tar.gz vrf
mgmt
| Command History     |         |         |                   |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- |
| Release             |         |         | Modification      |     |     |
| 10.08               |         |         | AddedSCP support. |     |     |
| 10.07orearlier      |         |         | --                |     |     |
| Command Information |         |         |                   |     |     |
| Platforms           | Command | context | Authority         |     |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy diag-dump | feature | <FEATURE> |     |     |     |
| -------------- | ------- | --------- | --- | --- | --- |
copy diag-dump feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesthespecifieddiagnosticinformationusingTFTP,SFTP,SCP,orUSB.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<FEATURE>
Thenameofafeature,forexampleaaa.
Required.
46
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- |

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
{<REMOTE-URL> [vrf <VRF-NAME> |<STORAGE-URL>]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopied
commandoutput.Required.
| <REMOTE-URL> |     |     |     | SpecifiestheremotedestinationURL. |     |     |
| ------------ | --- | --- | --- | --------------------------------- | --- | --- |
Required.ThesyntaxoftheURListhe
following:
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.IfnoVRFnameis |     |     |
| -------------- | --- | --- | --- | --------------------------------- | --- | --- |
provided,theVRFnameddefaultisused.
Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Required.
Syntax:{usb}:/<FILE>
Examples
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa tftp://10.100.0.12/diagdump.txt vrf mgmt
CopyingtheoutputfromtheaaafeaturetoaremoteURLwithaspecifiedVRF:
switch# copy diag-dump feature aaa scp://user@10.100.0.12/diagdump.txt vrf mgmt
| Command History     |         |         |                   |     |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- | --- |
| Release             |         |         | Modification      |     |     |     |
| 10.08               |         |         | AddedSCP support. |     |     |     |
| 10.07orearlier      |         |         | --                |     |     |     |
| Command Information |         |         |                   |     |     |     |
| Platforms           | Command | context | Authority         |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy diag-dump | local-file |     |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- | --- |
copy diag-dump local-file {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,orUSB.
SupportabilityCopy|47

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
{<REMOTE-URL> [vrf <VRF-NAME>] |<STORAGE-URL>} SelecteitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommand |     |     |
| ------------ | --- | --- | --- | ------------------------------- | --- | --- |
output.
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
Thecopy diag-dump local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump
local-filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# diag-dump | aaa | basic local-file |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | --- | --- |
switch# copy diag-dump local-file tftp://10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# diag-dump | aaa | basic local-file |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | --- | --- |
switch# copy diag-dump local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaUSBdrive:
| switch# diag-dump   | aaa       | basic local-file |                   |     |     |     |
| ------------------- | --------- | ---------------- | ----------------- | --- | --- | --- |
| switch# copy        | diag-dump | local-file       | usb:/diagdump.txt |     |     |     |
| Command History     |           |                  |                   |     |     |     |
| Release             |           |                  | Modification      |     |     |     |
| 10.08               |           |                  | AddedSCP support. |     |     |     |
| 10.07orearlier      |           |                  | --                |     |     |     |
| Command Information |           |                  |                   |     |     |     |
48
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| Platforms | Command | context | Authority |     |     |     |
| --------- | ------- | ------- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy diag-dump | vsf | member | local-file |     |     |     |
| -------------- | --- | ------ | ---------- | --- | --- | --- |
copy diag-dump vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] |
<STORAGE-URL>}
Description
CopiesthediagnosticinformationstoredinalocalfileusingTFTP,SFTP,SCP,orUSB.
| Parameter  |             |     |     | Description                          |     |     |
| ---------- | ----------- | --- | --- | ------------------------------------ | --- | --- |
| vsf member | <MEMBER-ID> |     |     | Specifiesthemember-idoftheVSFmember. |     |     |
Required.
| {<REMOTE-URL> | [vrf <VRF-NAME>] | |<STORAGE-URL>} |     |     |     |     |
| ------------- | ---------------- | --------------- | --- | --- | --- | --- |
SelecteitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommand |     |     |
| ------------ | --- | --- | --- | ------------------------------- | --- | --- |
output.
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
Thecopy local-filecommandcanbeusedonlyaftertheinformationiscaptured.Runthe
diag-dump
diag-dump <FEATURE-NAME> basic local-filecommandbeforeyouenterthecopy diag-dump
local-filecommandtocapturethediagnosticinformationforthespecifiedfeatureintothelocalfile.
Examples
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic local-file |     |     |     |     |
| ------- | --------- | -------------------- | --- | --- | --- | --- |
switch#
copy diag-dump vsf member 2 local-file scp://user@10.100.0.12/diagdump.txt
CopyingtheoutputfromthelocalfiletoaremoteURL:
| switch# | diag-dump | aaa basic local-file |     |     |     |     |
| ------- | --------- | -------------------- | --- | --- | --- | --- |
switch# copy diag-dump vsf member 2 local-file tftp://10.100.0.12/diagdump.txt
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
SupportabilityCopy|49

| Release             |         |         | Modification      |     |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- | --- |
| 10.08               |         |         | AddedSCP support. |     |     |     |
| 10.07orearlier      |         |         | --                |     |     |     |
| Command Information |         |         |                   |     |     |     |
| Platforms           | Command | context | Authority         |     |     |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy <IMAGE>
copy <IMAGE> {<STORAGE-URL> | <REMOTE-URL>} <FILE-NAME> [vrf <VRF-NAME>]
Description
CopiestheimageusingTFTP,SFTP,SCP,orUSB.
| Parameter      |                 |     | Description        |     |     |     |
| -------------- | --------------- | --- | ------------------ | --- | --- | --- |
| <IMAGE>        |                 |     | Specifiestheimage. |     |     |     |
| {<STORAGE-URL> | | <REMOTE-URL>} |     |                    |     |     |     |
SelecteitherthestorageURLortheremoteURLforthe
destinationofthecopiedcommandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- | --- |
Syntax:
{usb}:/<FILE>
<REMOTE-URL>
SpecifiestheURLtocopythecommandoutput.
Syntax:
|     |     |     | {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |     |
| --- | --- | --- | -------------- | ------------------ | --- | --- |
n
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> |     | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --- | --------- |
[:<PORT>]/<FILE>
| <FILE-NAME> |     |     | Specifiesthefilename. |     |     |     |
| ----------- | --- | --- | --------------------- | --- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingtheimagetoaremoteURL:
| switch# | copy scp://root@20.0.1.1/primary.swi |     |     | primary vrf | mgmt |     |
| ------- | ------------------------------------ | --- | --- | ----------- | ---- | --- |
CopyingthesecondaryimagetoaremoteURL:
switch# copy secondary scp://root@20.0.1.1/primary.swi vrf mgmt
| Command History |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
50
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Release             |         |         | Modification      |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- |
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
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --------- |
[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     | Specifiestherunningconfiguration. |     |     |
| -------------------- | --- | --- | --------------------------------- | --- | --- |
vrf <VRF-NAME>
SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingtherunningconfigurationtoaremoteURL:
switch# copy running-config scp://root@10.0.1.1/config cli vrf mgmt
| Command History |     |     |                   |     |     |
| --------------- | --- | --- | ----------------- | --- | --- |
| Release         |     |     | Modification      |     |     |
| 10.08           |     |     | AddedSCP support. |     |     |
| 10.07orearlier  |     |     | --                |     |     |
SupportabilityCopy|51

| Command Information |         |         |           |     |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- | --- |
| Platforms           | Command | context | Authority |     |     |     |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| copy show-tech | feature |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- |
copy show-tech feature <FEATURE> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesshowtechoutputusingTFTP,SFTP,SCP,andUSB.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
{<REMOTE-URL> [vrf <VRF-NAME> | <STORAGE-URL>]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopied
commandoutput.Required.
<REMOTE-URL>
SpecifiestheURLtocopythecommand
output.Required.
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
SpecifiestheVRFname.ThedefaultVRF
nameisdefault.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Required.
Syntax:{usb}:/<FILE>
Example
CopyingshowtechoutputoftheaaafeatureusingSCP:
switch# copy show-tech feature aaa scp://user@10.0.0.12/file.txt vrf mgmt
CopyingshowtechoutputoftheconfigfeatureusingSFTPonthemgmtVRF:
switch# copy show-tech feature config sftp://root@10.0.0.1/tech.txt vrf mgmt
| Command History |     |     |                   |     |     |     |
| --------------- | --- | --- | ----------------- | --- | --- | --- |
| Release         |     |     | Modification      |     |     |     |
| 10.08           |     |     | AddedSCP support. |     |     |     |
| 10.07orearlier  |     |     | --                |     |     |     |
52
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

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
n {tftp://}{<IP> | <HOST>}

[:<PORT>]
[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP>

| <HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF
name is default. Optional.

Specifies the USB to copy command
output.
Syntax: {usb}:/<FILE>

Before entering the copy show-tech local-file command, run the show tech command with the
local-file parameter for the specified feature.

Examples

Copying the output to a remote URL:

switch# copy show-tech local-file tftp://10.100.0.12/file.txt

Copying the output to a remote URL:

switch# copy show-tech local-file scp://user@10.100.0.12/file.txt

Copying the output to a remote URL with a VRF:

Supportability Copy | 53

switch# copy show-tech local-file tftp://10.100.0.12/file.txt vrf mgmt
CopyingtheoutputtoaUSB:
| switch#             | copy show-tech |     | local-file | usb:/file         |
| ------------------- | -------------- | --- | ---------- | ----------------- |
| Command History     |                |     |            |                   |
| Release             |                |     |            | Modification      |
| 10.08               |                |     |            | AddedSCP support. |
| 10.07orearlier      |                |     |            | --                |
| Command Information |                |     |            |                   |
| Platforms           | Command        |     | context    | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy show-tech |     | vsf | member | local-file |
| -------------- | --- | --- | ------ | ---------- |
copy show-tech vsf member <MEMBER-ID> local-file {<REMOTE-URL> [vrf <VRF-NAME>] |
<STORAGE-URL>}
Description
Copiesshowtechoutputstoredinalocalfile.
Parameter Description
| vsf member | <MEMBER-ID> |     |     |     |
| ---------- | ----------- | --- | --- | --- |
Specifiesthemember-idoftheVSF
member.Required.
{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]} SelecteithertheremoteURLorthe
storageURLforthedestinationofthe
copiedcommandoutput.Required.
<REMOTE-URL> SpecifiestheURLtocopythecommand
output.
Syntax:
n {tftp://}{<IP> | <HOST>}
[:<PORT>]
[;blocksize=<VAL>]/<FILE>
n {sftp://| scp://<USER>@}{<IP>
| <HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.ThedefaultVRF |
| -------------- | --- | --- | --- | --------------------------------- |
nameisdefault.Optional.
<STORAGE-URL> SpecifiestheUSBtocopycommand
output.
Syntax:{usb}:/<FILE>
54
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

Usage
Beforeenteringthecopy local-filecommand,runtheshow techcommandwiththe
show-tech
local-fileparameterforthespecifiedfeature.
Examples
CopyingtheoutputtoaremoteURLwithaVRF:
switch# copy show-tech vsf member 2 local-file tftp://10.100.0.12/showtech.txt vrf
mgmt
CopyingtheoutputtoaUSB:
| switch#             | copy show-tech | vsf member | 2 local-file      | usb:/file |     |
| ------------------- | -------------- | ---------- | ----------------- | --------- | --- |
| Command History     |                |            |                   |           |     |
| Release             |                |            | Modification      |           |     |
| 10.08               |                |            | AddedSCP support. |           |     |
| 10.07orearlier      |                |            | --                |           |     |
| Command Information |                |            |                   |           |     |
| Platforms           | Command        | context    | Authority         |           |     |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
copy startup-config
copy startup-config {<STORAGE-URL> | <REMOTE-URL>}/config <CONFIG-NAME> [vrf <VRF-NAME>]
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
|     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | | <HOST>} |
| --- | --- | --- | ----------- | ------------------- | --------- |
SupportabilityCopy|55

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
[:<PORT>]/<FILE>
| config <CONFIG-NAME> |     |     | Specifiesthestartupconfiguration. |
| -------------------- | --- | --- | --------------------------------- |
vrf <VRF-NAME> SpecifiestheVRFname.ThedefaultVRFnameisdefault.Optional.
Examples
CopyingthestartupconfigurationtoaremoteURL:
switch# copy startup-config scp://root@10.0.1.1/config json vrf mgmt
| Command        | History     |         |                   |
| -------------- | ----------- | ------- | ----------------- |
| Release        |             |         | Modification      |
| 10.08          |             |         | AddedSCP support. |
| 10.07orearlier |             |         | --                |
| Command        | Information |         |                   |
| Platforms      | Command     | context | Authority         |
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
| feature       | <FEATURE-NAME> | <STORAGE-URL> |                  |
| ------------- | -------------- | ------------- | ---------------- |
| previous-boot | <REMOTE-URL>   | [vrf          | <VRF-NAME>]      |
| previous-boot | <STORAGE-URL>  |               |                  |
| vsf member    | <MEMBER-ID>    | <REMOTE-URL>  | {vrf <VRF-NAME>} |
| vsf member    | <MEMBER-ID>    | <STORAGE-URL> |                  |
Description
Copiesasetofsupportfilestoacompressedfileintar.gzformatusingTFTP,SFTP,SCP,orUSBortoa
directoryoverSFTPorUSB.
Parameter Description
<FEATURE-NAME>
Thefeaturename,forexample,aaa.
{<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL> ]} SelecteithertheremoteURLorthe
storageURLforthedestinationofthe
56
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Parameter

Description

<REMOTE-URL>

vrf <VRF-NAME>

<STORAGE-URL>

<MEMBER-ID>

Usage

copied command output. Required.

Specifies the URL to copy the command
output.
Syntax:
n {tftp://}{<IP> | <HOST>}

[:<PORT>]
[;blocksize=<VAL>]/<FILE>

n {sftp:// | scp:// <USER>@}{<IP>

| <HOST>}[:<PORT>]/<FILE>

Specifies the VRF name. The default VRF
name is default. Optional.

Specifies the USB to copy command
output.
Syntax: {usb}:/<FILE>

The member ID in the VSF stack. Range 1-
10.

If feature name is not provided, the command collects generic system-specific support information. If a
feature name is provided, the command collects feature-specific support information.

In order to collect data from standby and member in a VSF stack, the command will prompt for the local user

password once.

Examples

Copying the support files to a remote URL:

switch# copy support-files tftp://10.100.0.12/file.tar.gz

Copying the support files of the lldp feature to a remote URL with a specified VRF:

switch# copy support-files feature lldp tftp://10.100.0.12/file.tar.gz vrf mgmt

Copying the support files from the previous boot to a remote URL with a specified VRF:

switch# copy support-files previous-boot scp://user@10.0.14.206/file.tar.gz vrf
mgmt

Copying the support files to a USB:

switch# copy support-files usb:/file.tar.gz

Copying all the support files to a remote URL:

Supportability Copy | 57

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy | support-files |     | local-file |     |     |
| ---- | ------------- | --- | ---------- | --- | --- |
copy support-files [feature <FEATURE-NAME> | previous-boot | all ] local-file {<REMOTE-
| URL> [vrf | <VRF-NAME>] |     | | <STORAGE-URL>} |     |     |
| --------- | ----------- | --- | ---------------- | --- | --- |
Description
Storesasetofsupportfilesasacompressedfileintheswitchlocallyandcopiesthepreservedsupport
filestoadirectoryusingTFTP,SFTP,SCP,orUSB.
Youcanstoreonlyonecopyofthesupportfilelocally.Whenyoustoreanewsupportfile,itoverwritesthe
existingsupportfile.
| Parameter      |     |     |     | Description                            |     |
| -------------- | --- | --- | --- | -------------------------------------- | --- |
| <FEATURE-NAME> |     |     |     | Specifiesthefeatureforthesupportfiles. |     |
<SLOT-ID> Specifiesthemoduleslotnumberidentifierforthesupportfiles.
Range:1/1-1/4,1/7-1/10
<MEMBER-ID> SpecifiestheVSFmemberidentifierforthesupportfiles.Range:1-
10
| <REMOTE-URL>  |     |     |     | SpecifiestheURLtocopythesupportfiles.           |     |
| ------------- | --- | --- | --- | ----------------------------------------------- | --- |
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopythesupportfiles.           |     |
| <VRF-NAME>    |     |     |     | SpecifiestheVRFname.ThedefaultVRFnameisdefault. |     |
Usage
58
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

Ifthecopyofthesupportfilestothedestinationfails,analternateoptionispromptedtostorethe
collecteddatainthelocalfile.Thishelpsustoretrythecopyprocessusingcopy support-files local-
file <REMOTE-URL/STORAGE-URL>withouttheneedofregeneratingthefile.
Examples
Copyingsupportfiletothelocalfile:
| switch# | copy support-files | local-file    |            |            |
| ------- | ------------------ | ------------- | ---------- | ---------- |
| switch# | copy support-files | feature       | lldp       | local-file |
| switch# | copy support-files | previous-boot |            | local-file |
| switch# | copy support-files | all           | local-file |            |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy support-files |     | vsf member |     |     |
| ------------------ | --- | ---------- | --- | --- |
copy support-files vsf member <MEMBER-ID> {<REMOTE-URL> [vrf <VRF-NAME>] | <STORAGE-URL>}
Description
CopiesasetofsupportfilesusingTFTP,SFTP,SCP,orUSB.
Parameter Description
<MEMBER-ID> Specifiedthemember-idoftheVSFmember.
Required.
{<REMOTE-URL> [vrf <VRF-NAME> | <STORAGE-URL>]} SelecteithertheremoteURLorthestorage
URLforthedestinationofthecopied
commandoutput.Required.
<REMOTE-URL> SpecifiestheURLtocopythecommand
output.
Syntax:
SupportabilityCopy|59

| Parameter |     |     |     | Description      |           |     |
| --------- | --- | --- | --- | ---------------- | --------- | --- |
|           |     |     |     | n {tftp://}{<IP> | | <HOST>} |     |
[:<PORT>]
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.ThedefaultVRF |     |     |
| -------------- | --- | --- | --- | --------------------------------- | --- | --- |
nameisdefault.Optional.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
Usage
Iffeaturenameisnotprovided,thecommandcollectsgenericsystem-specificsupportinformation.Ifa
featurenameisprovided,thecommandcollectsfeature-specificsupportinformation.
Examples
CopyingthesupportfilestoaUSB:
| switch# | copy support-files | vsf | member 2 usb:/file.tar.gz |     |     |     |
| ------- | ------------------ | --- | ------------------------- | --- | --- | --- |
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch# copy support-files vsf member 2 scp://user@10.100.0.12/file.tar.gz/ vrf
mgmt
CopyingallthesupportfilestoaremoteURLwithaspecifiedVRF:
switch# copy support-files vsf member 2 sftp://user@10.100.0.12/support_files_dir_
| path/ vrf           | mgmt    |         |                   |     |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- | --- |
| Command History     |         |         |                   |     |     |     |
| Release             |         |         | Modification      |     |     |     |
| 10.08               |         |         | AddedSCP support. |     |     |     |
| 10.07orearlier      |         |         | --                |     |     |     |
| Command Information |         |         |                   |     |     |     |
| Platforms           | Command | context | Authority         |     |     |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy support-log
60
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

Description
CopiesthespecifiedsupportlogforadaemonTFTP,SFTP,SCP,orUSB.
| Parameter      |                |                   | Description                           |     |     |
| -------------- | -------------- | ----------------- | ------------------------------------- | --- | --- |
| <DAEMON-NAME>  |                |                   | Specifiesthenameofthedaemon.Required. |     |     |
| {<STORAGE-URL> | | <REMOTE-URL> | [vrf <VRF-NAME>]} |                                       |     |     |
SelectseitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
| <STORAGE-URL> |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
| <REMOTE-URL> |     |     | SpecifiestheURLtocopythecommand |     |     |
| ------------ | --- | --- | ------------------------------- | --- | --- |
output.
Syntax:
|     |     |     | n {tftp://}{<IP> | | <HOST>} |     |
| --- | --- | --- | ---------------- | --------- | --- |
[:<PORT>]
[;blocksize=<VAL>]/<FILE>
|     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.IfnoVRFnameis |     |     |
| -------------- | --- | --- | --------------------------------- | --- | --- |
provided,theVRFnameddefaultisused.
Optional.
Usage
Fastlogisahighperformance,per-daemonbinarylogginginfrastructureusedtodebugdaemonlevel
issuesbypreciselycapturingtheperdaemon/module/functionalitiesdebugtracesinrealtime.Fastlog,
alsoreferredtoassupportlogs,helpsuserstounderstandthefeatureinternalsanditsspecific
happenings.Thefastlogsfromonedaemonarenotoverwrittenbyotherdaemonlogsbecausefast
logsarecapturedaspartofadaemoncoredump.Fastlogsareenabledbydefault.
Examples
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURL:
| switch# copy | support-log | hpe-fand tftp://10.100.0.12/file |     |     |     |
| ------------ | ----------- | -------------------------------- | --- | --- | --- |
CopyingthesupportlogfromthedaemonfandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log fand scp://user@10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log hpe-fand tftp://10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaUSB:
| switch# copy | support-log | hpe-fand usb:/support-log |     |     |     |
| ------------ | ----------- | ------------------------- | --- | --- | --- |
SupportabilityCopy|61

| Command History     |         |         |                   |     |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- | --- |
| Release             |         |         | Modification      |     |     |     |
| 10.08               |         |         | AddedSCP support. |     |     |     |
| 10.07orearlier      |         |         | --                |     |     |     |
| Command Information |         |         |                   |     |     |     |
| Platforms           | Command | context | Authority         |     |     |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy support-log |     | vsf member |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- |
copy support-log vsf member <MEMBER-ID> <DAEMON-NAME> {<STORAGE-URL> | <REMOTE-URL> [vrf
<VRF-NAME>]}
Description
CopiesthespecifiedsupportlogforadaemonusingTFTP,SFTP,SCP,orUSB.
| Parameter   |     |     |     | Description                          |     |     |
| ----------- | --- | --- | --- | ------------------------------------ | --- | --- |
| <MEMBER-ID> |     |     |     | Specifiesthemember-idoftheVSFmember. |     |     |
Required.
<DAEMON-NAME>
Specifiesthenameofthedaemon.Required.
{<STORAGE-URL> | <REMOTE-URL> [vrf <VRF-NAME>]} SelectseitherthestorageURLortheremote
URLforthedestinationofthecopied
commandoutput.Required.
| <STORAGE-URL> |     |     |     | SpecifiestheUSBtocopycommandoutput. |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
Syntax:{usb}:/<FILE>
| <REMOTE-URL> |     |     |     | SpecifiestheURLtocopythecommand |     |     |
| ------------ | --- | --- | --- | ------------------------------- | --- | --- |
output.
Syntax:
|     |     |     |     | n {tftp://}{<IP> | | <HOST>}[:<PORT>] |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- |
[;blocksize=<VAL>]/<FILE>
|     |     |     |     | n {sftp://| | scp://<USER>@}{<IP> | |   |
| --- | --- | --- | --- | ----------- | ------------------- | --- |
<HOST>}[:<PORT>]/<FILE>
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.IfnoVRFnameis |     |     |
| -------------- | --- | --- | --- | --------------------------------- | --- | --- |
provided,theVRFnameddefaultisused.
Optional.
Usage
Fastlogisahighperformance,per-daemonbinarylogginginfrastructureusedtodebugdaemonlevel
issuesbypreciselycapturingtheperdaemon/module/functionalitiesdebugtracesinrealtime.Fastlog,
alsoreferredtoassupportlogs,helpsuserstounderstandthefeatureinternalsanditsspecific
happenings.Thefastlogsfromonedaemonarenotoverwrittenbyotherdaemonlogsbecausefast
logsarecapturedaspartofadaemoncoredump.Fastlogsareenabledbydefault.
62
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

Examples
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch#
copy support-log vsf member 2 hpe-fand tftp://10.100.0.12/file vrf mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaremoteURLwithaVRFnamedmgmt:
switch# copy support-log vsf member 2 hpe-fand scp://user@10.100.0.12/file vrf
mgmt
Copyingthesupportlogfromthedaemonhpe-fandtoaUSB:
switch# copy support-log vsf member 2 hpe-fand usb:/support-log
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | AddedSCP support. |
| 10.07orearlier      |         |         | --                |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
SupportabilityCopy|63

Chapter 10
Traceroute
Traceroute
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
Protocol(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashop
limit,isusedindeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
| Traceroute | commands |     |
| ---------- | -------- | --- |
traceroute
traceroute {<IPV4-ADDR> | <HOSTNAME>} [ip-option loosesourceroute <IPV4-ADDR>] [dstport
<NUMBER> | maxttl <NUMBER> | minttl <NUMBER> | probes <NUMBER> | timeout <TIME>] [vrf
| <VRF-NAME>] | source {<IPV4-ADDR> | | <IFNAME>} |
| ----------- | ------------------- | ----------- |
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
dstport <NUMBER> Specifiesthedestinationport,<1-34000>.Default:33434
maxttl <NUMBER> Specifiesthemaximumnumberofhopstoreachthedestination,
<1-255>.Default:30
minttl <NUMBER> SpecifiestheMinimumnumberofhopstoreachthedestination,
<1-255>.Default:1
| probes | <NUMBER> |     |
| ------ | -------- | --- |
Specifiesthenumberofprobes,<1-5>.Default:3
timeout <TIME> Specifiesthetraceroutetimeoutinseconds,<1-60>.Default:3
seconds
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.
source {<IPV4-ADDR> | <IFNAME>} SpecifiesthesourceIPv4addressorinterfacename.
Usage
Tracerouteisacomputernetworkdiagnostictoolfordisplayingtheroute(path),andmeasuringtransit
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
64
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |
| --------------------------------------------- | --- | ------------------ |

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
Traceroute|65

switch# traceroute 10.0.10.1 maxttl 20 timeout 5 minttl 1 probes 3 dstport 33434
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1 10.0.40.2 |     | 0.002ms 0.002ms | 0.001ms |     |     |     |
| ----------- | --- | --------------- | ------- | --- | --- | --- |
| 2 10.0.30.1 |     | 0.002ms 0.001ms | 0.001ms |     |     |     |
| 3 10.0.10.1 |     | 0.001ms 0.002ms | 0.002ms |     |     |     |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 30 hops max, 3 sec. timeout, 3
probes
| 1 10.0.40.2 |     | 0.002ms 0.002ms | 0.001ms |     |     |     |
| ----------- | --- | --------------- | ------- | --- | --- | --- |
| 2 10.0.30.1 |     | 0.002ms 0.001ms | 0.001ms |     |     |     |
| 3 10.0.10.1 |     | 0.001ms 0.002ms | 0.002ms |     |     |     |
switch# traceroute 10.0.10.1 ip-option loosesourceroute 10.0.40.2 maxttl 20
| timeout | 5 minttl | 1 probes 3 dstport | 33434 |     |     |     |
| ------- | -------- | ------------------ | ----- | --- | --- | --- |
traceroute to 10.0.10.1 (10.0.10.1) , 1 hops min, 20 hops max, 5 sec. timeout, 3
probes
| 1 10.0.40.2 |             | 0.002ms 0.002ms | 0.001ms      |                     |           |      |
| ----------- | ----------- | --------------- | ------------ | ------------------- | --------- | ---- |
| 2 10.0.30.1 |             | 0.002ms 0.001ms | 0.001ms      |                     |           |      |
| 3 10.0.10.1 |             | 0.001ms 0.002ms | 0.002ms      |                     |           |      |
| switch#     | traceroute  | 10.0.0.2 source | 10.0.0.1     |                     |           |      |
| traceroute  | to 10.0.0.2 | (10.0.0.2),     | 30 hops      | max                 |           |      |
| 1 10.0.0.2  |             | 0.299ms 0.155ms | 0.115ms      |                     |           |      |
| switch#     | traceroute  | 10.0.0.2 source | 1/1/1        |                     |           |      |
| traceroute  | to 10.0.0.2 | (10.0.0.2),     | 30 hops      | max                 |           |      |
| 1 10.0.0.2  |             | 0.479ms 0.222ms | 0.171ms      |                     |           |      |
| Command     | History     |                 |              |                     |           |      |
| Release     |             |                 | Modification |                     |           |      |
| 10.08       |             |                 | Addedsource  | IP addressandsource | interface | name |
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
66
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Parameter    |             |     |     | Description                                  |     |
| ------------ | ----------- | --- | --- | -------------------------------------------- | --- |
| IPv6-address | <IPV6-ADDR> |     |     | SpecifiestheIPv6address.                     |     |
| hostname     |             |     |     | Specifiesthehostnameofthedevicetotraceroute. |     |
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
delaysofpacketsacrossanInternetProtocol(IP)network.ItsendsasequenceofUserDatagram
Protocol(UDP)packetsaddressedtoadestinationhost.Thetime-to-live(TTL)value,alsoknownashop
limit,isusedindeterminingtheintermediateroutersbeingtraversedtowardsthedestination.
Examples
| switch# | traceroute6 | 0:0::0:1 |     |     |     |
| ------- | ----------- | -------- | --- | --- | --- |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117     | ms 0.032 | ms 0.021 | ms  |
| ----------- | ----------- | --------- | -------- | -------- | --- |
| switch#     | traceroute6 | localhost |          |          |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.089    | ms 0.03 | ms 0.014 | ms  |
| ----------- | ----------- | -------- | ------- | -------- | --- |
| switch#     | traceroute6 | 0:0::0:1 | maxttl  | 30       |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms 0.032 | ms 0.021 | ms  |
| ----------- | ----------- | -------- | -------- | -------- | --- |
| switch#     | traceroute6 | 0:0::0:1 | dsrport  | 33434    |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms 0.032 | ms 0.021 | ms  |
| ----------- | ----------- | -------- | -------- | -------- | --- |
| switch#     | traceroute6 | 0:0::0:1 | probes   | 2        |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 2 probes, 24
byte packets
| 1 localhost | (::1)       | 0.117    | ms 0.032 | ms  |     |
| ----------- | ----------- | -------- | -------- | --- | --- |
| switch#     | traceroute6 | 0:0::0:1 | timeout  | 3   |     |
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost | (::1) | 0.117 | ms 0.032 | ms 0.021 | ms  |
| ----------- | ----- | ----- | -------- | -------- | --- |
Traceroute|67

switch#
|     | traceroute6 |     | localhost |     | vrf red |     |     |     |     |
| --- | ----------- | --- | --------- | --- | ------- | --- | --- | --- | --- |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost |             | (::1) | 0.077     | ms  | 0.051 | ms 0.054 | ms  |     |     |
| ----------- | ----------- | ----- | --------- | --- | ----- | -------- | --- | --- | --- |
| switch#     | traceroute6 |       | localhost |     | mgmt  |          |     |     |     |
traceroute to localhost (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost |     | (::1) | 0.089 | ms  | 0.03 ms | 0.014 | ms  |     |     |
| ----------- | --- | ----- | ----- | --- | ------- | ----- | --- | --- | --- |
switch#
traceroute6 0:0::0:1 maxttl 30 timeout 3 probes 3 dstport 33434
traceroute to 0:0::0:1 (::1) from ::1, 30 hops max, 3 sec. timeout, 3 probes, 24
byte packets
| 1 localhost |             | (::1) | 0.117   | ms     | 0.032   | ms 0.021 | ms  |     |     |
| ----------- | ----------- | ----- | ------- | ------ | ------- | -------- | --- | --- | --- |
| switch#     | traceroute6 |       | 2001::2 | source | 2001::1 |          |     |     |     |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3
| probes,   | 24  | byte packets |        |     |        |     |           |     |     |
| --------- | --- | ------------ | ------ | --- | ------ | --- | --------- | --- | --- |
| 1 2001::2 |     | (2001::2)    | 0.4331 | ms  | 0.3186 | ms  | 0.1874 ms |     |     |
switch#
|     | traceroute6 |     | 2001::2 | source | 1/1/1 |     |     |     |     |
| --- | ----------- | --- | ------- | ------ | ----- | --- | --- | --- | --- |
traceroute to 2001::2 (2001::2) from 2001::1, 30 hops max, 3 sec. timeout, 3
| probes,   | 24      | byte      | packets |     |              |     |                     |           |      |
| --------- | ------- | --------- | ------- | --- | ------------ | --- | ------------------- | --------- | ---- |
| 1 2001::2 |         | (2001::2) | 0.6145  | ms  | 0.4165       | ms  | 0.1620 ms           |           |      |
| Command   | History |           |         |     |              |     |                     |           |      |
| Release   |         |           |         |     | Modification |     |                     |           |      |
| 10.08     |         |           |         |     | Addedsource  |     | IP addressandsource | interface | name |
parameters.
| 10.07orearlier |             |         |         |     | --        |     |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | --------- | --- | --- | --- | --- |
| Command        | Information |         |         |     |           |     |     |     |     |
| Platforms      |             | Command | context |     | Authority |     |     |     |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
68
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

Chapter 11

Ping

Ping

The ping (Packet Internet Groper) command is a common method for troubleshooting the accessibility
of devices. It uses Internet Control Message Protocol (ICMP) echo requests and ICMP echo replies to
determine if another device is alive. It also measures the amount of time it takes to receive a reply from
the specified destination. The ping command is mostly used to verify IP connectivity between two
endpoints which could be switch to switch, host to host, or host to switch. The reply packet tells if the
host received the ping and the amount of time it took to return the packet.

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

Specifies the number of packets to send. Range: 1-10000
packets, default: Five packets.

Specifies the ping timeout in seconds. Range: 1-60 seconds,
default: 2 seconds.

Specifies the IP Type of Service to be used in Ping request.
Range: 0-255

Specifies an IP option (record-route or timestamp option).

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

69

| Parameter         |     |     |     |     | Description                              |     |     |     |
| ----------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
| include-timestamp |     |     |     |     | Specifiestheintermediateroutertimestamp. |     |     |     |
include-timestamp-and-address SpecifiestheintermediateroutertimestampandIPaddress.
| record-route |     |     |     |     | Specifiestheintermediaterouteraddresses. |     |     |     |
| ------------ | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.When
VRFoptionisnotgiven,thedefaultVRFisused.
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
| --- 10.0.0.0         |              | ping       | statistics                | ---        |        |        |            |             |
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
| --- localhost        |              | ping | statistics                | ---       |     |        |       |             |
| -------------------- | ------------ | ---- | ------------------------- | --------- | --- | ------ | ----- | ----------- |
| 5 packets            | transmitted, |      | 5                         | received, | 0%  | packet | loss, | time 3998ms |
| rtt min/avg/max/mdev |              |      | = 0.034/0.042/0.060/0.011 |           |     |        | ms    |             |
Pingingaserverwithadatapattern:
switch# ping 10.0.0.2 data-fill 1234123412341234acde123456789012
| PATTERN:      | 0x1234123412341234acde123456789012 |            |     |            |        |     |            |     |
| ------------- | ---------------------------------- | ---------- | --- | ---------- | ------ | --- | ---------- | --- |
| PING 10.0.0.2 |                                    | (10.0.0.2) |     | 100(128)   | bytes  | of  | data.      |     |
| 108 bytes     | from                               | 10.0.0.2:  |     | icmp_seq=1 | ttl=64 |     | time=0.207 | ms  |
| 108 bytes     | from                               | 10.0.0.2:  |     | icmp_seq=2 | ttl=64 |     | time=0.187 | ms  |
| 108 bytes     | from                               | 10.0.0.2:  |     | icmp_seq=3 | ttl=64 |     | time=0.225 | ms  |
| 108 bytes     | from                               | 10.0.0.2:  |     | icmp_seq=4 | ttl=64 |     | time=0.197 | ms  |
Ping|70

| 108 bytes            | from 10.0.0.2: |                           | icmp_seq=5 |     | ttl=64    | time=0.210 | ms          |
| -------------------- | -------------- | ------------------------- | ---------- | --- | --------- | ---------- | ----------- |
| --- 10.0.0.2         | ping           | statistics                | ---        |     |           |            |             |
| 5 packets            | transmitted,   | 5                         | received,  |     | 0% packet | loss,      | time 3999ms |
| rtt min/avg/max/mdev |                | = 0.187/0.205/0.225/0.015 |            |     |           | ms         |             |
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
10 packets transmitted, 10 received, 0% packet loss, time 8999ms
| rtt min/avg/max/mdev |     | = 0.184/0.197/0.213/0.008 |     |     |     | ms  |     |
| -------------------- | --- | ------------------------- | --- | --- | --- | --- | --- |
Pingingaserverwithaspecifiedtimeout:
71
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

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
Ping|72

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
73
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

| --- 9.0.0.2          |              | ping statistics |                           | ---       |     |        |            |        |
| -------------------- | ------------ | --------------- | ------------------------- | --------- | --- | ------ | ---------- | ------ |
| 5 packets            | transmitted, |                 | 5                         | received, | 0%  | packet | loss, time | 3999ms |
| rtt min/avg/max/mdev |              |                 | = 0.034/0.036/0.038/0.001 |           |     |        | ms         |        |
Pingingaserverwithdo-not-fragment:
| switch#              | ping         | 192.168.1.8   |                           | datagram-size |              | 2000   | do-not-fragment |        |
| -------------------- | ------------ | ------------- | ------------------------- | ------------- | ------------ | ------ | --------------- | ------ |
| PING 192.168.1.8     |              | (192.168.1.8) |                           |               | 2000(2028)   |        | bytes of data.  |        |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=1    |              | ttl=64 | time=0.721      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=2    |              | ttl=64 | time=0.792      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=3    |              | ttl=64 | time=0.857      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=4    |              | ttl=64 | time=0.833      | ms     |
| 2008 bytes           | from         | 192.168.1.8:  |                           | icmp_seq=5    |              | ttl=64 | time=0.836      | ms     |
| --- 192.168.1.8      |              | ping          | statistics                |               | ---          |        |                 |        |
| 5 packets            | transmitted, |               | 5                         | received,     | 0%           | packet | loss, time      | 4056ms |
| rtt min/avg/max/mdev |              |               | = 0.721/0.807/0.857/0.048 |               |              |        | ms              |        |
| Command              | History      |               |                           |               |              |        |                 |        |
| Release              |              |               |                           |               | Modification |        |                 |        |
| 10.07orearlier       |              |               |                           |               | --           |        |                 |        |
| Command              | Information  |               |                           |               |              |        |                 |        |
| Platforms            | Command      |               | context                   |               | Authority    |        |                 |        |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
ping6
ping6 {<IPv6-ADDR> | <HOSTNAME>} [data-fill <PATTERN> | datagram-size <SIZE> |
| interval       | <TIME> | |        | repetitions | <NUMBER> |     | | timeout   | <TIME> | |   |
| -------------- | ------ | -------- | ----------- | -------- | --- | ----------- | ------ | --- |
| vrf <VRF-NAME> |        | | source | <IPv6-ADDR> |          |     | | <IFNAME>] |        |     |
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
Ping|74

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
interval <TIME> Specifiestheintervalbetweensuccessivepingrequestsin
seconds.Range:1-60seconds,default:1second.
repetitions <NUMBER> Specifiesthenumberofpacketstosend.Range:1-10000packets,
default:Fivepackets.
timeout <TIME>
Specifiesthepingtimeoutinseconds.Range:1-60seconds,
default:2seconds.
vrf <VRF-NAME> Specifiesthevirtualroutingandforwarding(VRF)touse.When
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
| switch#               | ping6 2020::2 | data-fill |            | ab    |        |            |     |
| --------------------- | ------------- | --------- | ---------- | ----- | ------ | ---------- | --- |
| PATTERN:              | 0xab          |           |            |       |        |            |     |
| PING 2020::2(2020::2) |               | 100       | data       | bytes |        |            |     |
| 108 bytes             | from 2020::2: |           | icmp_seq=1 |       | ttl=64 | time=0.038 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=2 |       | ttl=64 | time=0.074 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=3 |       | ttl=64 | time=0.076 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=4 |       | ttl=64 | time=0.075 | ms  |
| 108 bytes             | from 2020::2: |           | icmp_seq=5 |       | ttl=64 | time=0.077 | ms  |
75
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

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
| switch#     | ping6            | 2020::2         | interval   |      | 5      |            |     |
| ----------- | ---------------- | --------------- | ---------- | ---- | ------ | ---------- | --- |
| PING        | 2020::2(2020::2) |                 | 100        | data | bytes  |            |     |
| 108 bytes   | from             | 2020::2:        | icmp_seq=1 |      | ttl=64 | time=0.043 | ms  |
| 108 bytes   | from             | 2020::2:        | icmp_seq=2 |      | ttl=64 | time=0.075 | ms  |
| 108 bytes   | from             | 2020::2:        | icmp_seq=3 |      | ttl=64 | time=0.074 | ms  |
| 108 bytes   | from             | 2020::2:        | icmp_seq=4 |      | ttl=64 | time=0.075 | ms  |
| 108 bytes   | from             | 2020::2:        | icmp_seq=5 |      | ttl=64 | time=0.075 | ms  |
| --- 2020::2 |                  | ping statistics |            | ---  |        |            |     |
5 packets transmitted, 5 received, 0% packet loss, time 19999ms
| rtt min/avg/max/mdev |     |     | = 0.043/0.068/0.075/0.014 |     |     | ms  |     |
| -------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
Pingingaserverwithaspecifiednumberofpacketstosend:
switch#
|                      | ping6            | 2020::2         | repetitions               |           | 6            |            |             |
| -------------------- | ---------------- | --------------- | ------------------------- | --------- | ------------ | ---------- | ----------- |
| PING                 | 2020::2(2020::2) |                 | 100                       | data      | bytes        |            |             |
| 108 bytes            | from             | 2020::2:        | icmp_seq=1                |           | ttl=64       | time=0.039 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=2                |           | ttl=64       | time=0.070 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=3                |           | ttl=64       | time=0.076 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=4                |           | ttl=64       | time=0.076 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=5                |           | ttl=64       | time=0.071 | ms          |
| 108 bytes            | from             | 2020::2:        | icmp_seq=6                |           | ttl=64       | time=0.078 | ms          |
| --- 2020::2          |                  | ping statistics |                           | ---       |              |            |             |
| 6 packets            | transmitted,     |                 | 6                         | received, | 0% packet    | loss,      | time 4999ms |
| rtt min/avg/max/mdev |                  |                 | = 0.039/0.068/0.078/0.015 |           |              | ms         |             |
| Command              | History          |                 |                           |           |              |            |             |
| Release              |                  |                 |                           |           | Modification |            |             |
| 10.07orearlier       |                  |                 |                           |           | --           |            |             |
| Command              | Information      |                 |                           |           |              |            |             |
Ping|76

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
Troubleshooting
| Operation | not permitted |     |     |     |
| --------- | ------------- | --- | --- | --- |
Symptom
Theswitchdisplaysanoperation not permittedmessagewhenauserattemptstosendaping
request.
Example:
| switch#         | ping 100.1.2.10 |            |                |         |
| --------------- | --------------- | ---------- | -------------- | ------- |
| PING 100.1.2.10 | (100.1.2.10)    |            | 100(128) bytes | of data |
| ping: sendmsg:  | Operation       | not        | permitted      |         |
| ping: sendmsg:  | Operation       | not        | permitted      |         |
| ping: sendmsg:  | Operation       | not        | permitted      |         |
| ping: sendmsg:  | Operation       | not        | permitted      |         |
| ping: sendmsg:  | Operation       | not        | permitted      |         |
| --- 100.1.2.10  | ping            | statistics | ---            |         |
5 packets transmitted, 0 received, 100% packet loss, time 4000ms
Cause
WhenanACLisappliedtotheControlPlane,sendingapingrequestmaybedenied.Ifthepingpacket
matchesadropentryintheACL,applyingaControlPlanemayblocktrafficsentfromtheswitchCLIping
command.
Whenthissituationoccurs,thefollowingerrormessageisdisplayed:ping: sendmsg: Operation not
permitted.ThemessageindicatesthattheICMPechorequestpackethasnotbeensentandisblocked
bytheControlPlaneACL.
Whenthismessageisnotdisplayed,thepingrequestpackethasbeensentcorrectly.Apingfailurein
thiscaserepresentsafailuretoreceivetheICMPechoreplypacket.
Action
1. ModifytheACLtoallowthepingtraffic.
2. UnapplytheACLfromegress(8400/8320/8325/9300switches)orControlPlane.
3. PingadestinationwhichisnotmatchedbytheACL.Forexample,iftheACLisblockingtraffic
basedondestinationIP.DependingontheACLcontent,thismightnotalwaysbepossiblelike
whentheACLblocksallICMPpackets.
| Network | is unreachable |     |     |     |
| ------- | -------------- | --- | --- | --- |
Symptom
Userreceivesa"networkisunreachable"messageonsendingapingrequest.
77
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

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
possible that Ingress ACLs on that switch are blocking ping packets. In such cases, the configuration
option on the destination switch should be examined.

Ping | 78

Chapter 12
Remote syslog
| Remote | syslog |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- |
Remotesyslogenablestheforwardingofsyslogmessagestotheremotesyslogserver.Thefeature
supportsamaximumoffourremotesyslogservers.Onlyoneconfigurationperremotesyslogserveris
allowed.TheremotesyslogserversupportsTCPandUDPtransportprotocolsandTLStoestablisha
connection.Inadditiontoforwardinglogstotheremoteserver,theycanalsobepreservedinlocal
storage.
Whentheclientcertificateassociatedwiththesyslogclientisupdated,thesyslogclientisrestartedand
anewTLSconnectionisestablishedusingtheupdatedclientcertificate.
| Remote | syslog | commands |     |     |     |
| ------ | ------ | -------- | --- | --- | --- |
clear accounting-logs
clear accounting-logs
Description
Usethiscommandtoclearaccountinglogs.Onceissued,onlylogsgeneratedafterthiscommandisrun
| willbedisplayedintheoutputoftheshow |     |     |     | accounting | logcommands. |
| ----------------------------------- | --- | --- | --- | ---------- | ------------ |
Thiscommandwillnotclearlogswhentheloggingaccounting-format-nativefeatureisconfigured.Toclear
accountinglogsonswitcheswiththisfeatureenabled,usersshouldfirstrevertthenativeaccountingformatback
tothedefaultAOS-CXformatbyexecutingthenologgingaccounting-format-nativecommand.
Example
| switch(config)# |     | clear | accounting-logs |     |     |
| --------------- | --- | ----- | --------------- | --- | --- |
Thefollowingexampleshowsthataccountinglogscannotbeclearedusingtheclearaccounting-logs
commandifthelogging accounting-native-formatcommandhasbeenenabled,andthatdisabling
thisoptionwiththeno logging accounting-format-nativecommandagainallowstheaccountinglogs
tobecleared.
| switch# | logging               | audit-format-native |     |     |     |
| ------- | --------------------- | ------------------- | --- | --- | --- |
| switch# | clear accounting-logs |                     |     |     |     |
Warning: Clear accounting-logs is not supported for 'audit-format-native'.
| switch# | no logging            | audit-format-native |          |     |     |
| ------- | --------------------- | ------------------- | -------- | --- | --- |
| switch# | clear accounting-logs |                     |          |     |     |
| switch# | show accounting       |                     | log last | 5   |     |
---------------------------------------------------
| Command | logs from | current | boot |     |     |
| ------- | --------- | ------- | ---- | --- | --- |
---------------------------------------------------
| No command | logs    | has been | logged | in the system |     |
| ---------- | ------- | -------- | ------ | ------------- | --- |
| Command    | History |          |        |               |     |
79
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

| Release   |             |         | Modification       |     |     |
| --------- | ----------- | ------- | ------------------ | --- | --- |
| 10.11     |             |         | Commandintroduced. |     |     |
| Command   | Information |         |                    |     |     |
| Platforms | Command     | context | Authority          |     |     |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |     |     |
| --- | --- | --- | --------------- | --- | --- |
logging
| logging | {<IPV4-ADDR> | | <IPV6-ADDR> | | <FQDN | | HOSTNAME>} |     |
| ------- | ------------ | ------------- | ------- | ------------ | --- |
[ {udp [<PORT-NUM>] }|{tcp [<PORT-NUM>} | {tls [<PORT-NUM> [auth-mode
{certificate|subject-name}] [legacy-tls-renegotiation]}] [severity <LEVEL>] [vrf <VRF-
NAME>] [include-auditable-events]
[filter <FILTER-NAME>] [ rate-limit-burst <BURST> [rate-limit-interval <INTERVAL>] ]
| no logging | {<IPV4-ADDR> | | <IPV6-ADDR> | | <FQDN | | HOSTNAME> | }   |
| ---------- | ------------ | ------------- | ------- | ----------- | --- |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
StartingwithAOS-CX10.11,payloadinformationispresentinaccountinglogs.
ThemaximumRESTpayloadthatcanbesenttoRADIUS/TACACSserveris1024characters,andthe
maximumofRESTpayloadthatcanbesenttosyslogserveris3500characters.Ifthislimitisisreached,
thelogwilldisplaythreedots(...)toindicatethattheloganexceededthecharacterlimitandis
incomplete.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
{<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>} SelectstheIPv4address,IPv6address,orhostname
oftheremotesyslogserver.Required.
[udp [<PORT-NUM>] | tcp [<PORT-NUM> | SpecifiestheUDPport,TCPport,orTLSportofthe
| tls | [<PORT-NUM>]] |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- |
remotesyslogservertoreceivetheforwardedsyslog
messages.
| udp [<PORT-NUM>] |     |     |     | Range:1to65535.Default:514 |     |
| ---------------- | --- | --- | --- | -------------------------- | --- |
tcp [<PORT-NUM>]
Range:1to65535.Default:1470
| tls [<PORT-NUM>] |     |     |     | Range:1to65535.Default:6514 |     |
| ---------------- | --- | --- | --- | --------------------------- | --- |
include-auditable-events
Specifiesthatauditablemessagesarealsologgedto
theremotesyslogserver.
| severity | <LEVEL> |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
Specifiestheseverityofthesyslogmessages:
alert:Forwardssyslogmessageswiththeseverity
n
|     |     |     |     | ofalert | (6)andemergency (7). |
| --- | --- | --- | --- | ------- | -------------------- |
n crit:Forwardssyslogmessageswiththeseverity
|     |     |     |     | ofcritical | (5)andabove. |
| --- | --- | --- | --- | ---------- | ------------ |
Remotesyslog|80

Parameter

Description

n debug: Forwards syslog messages with the severity

of debug (0) and above.

n emerg: Forwards syslog messages with the severity

of emergency (7) only.

n err: Forwards syslog messages with the severity of

err (4) and above

n info: Forwards syslog messages with the severity

of info (1) and above. Default.

n notice: Forwards syslog messages with the

severity of notice (2) and above.

n warning: Forwards syslog messages with the

severity of warning (3) and above.

Specifies the TLS authentication mode used to validate
the certificate.
n certificate: Validates the peer using trust

anchor certificate based authentication. Default.

n subject-name: Validates the peer using trust

anchor certificates as well as subject-name based

authentication.

Enables the TLS connection with a remote syslog
server supporting legacy renegotiation.

Specifies the name of the filter to be applied on the
syslog messages.

Specifies the rate limit for the messages sent to the
remote syslog server.

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

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

81

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
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logging accounting-format-native |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- |
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
switch(config)#
|     | logging | accounting-format-native |     |     |     |
| --- | ------- | ------------------------ | --- | --- | --- |
ThefollowingexamplereturnstheaccountinglogmessageformattothedefaultArubaOS-CXformat.
Remotesyslog|82

| switch(config)# |             | no  | logging | accounting-format-native |                    |
| --------------- | ----------- | --- | ------- | ------------------------ | ------------------ |
| Command         | History     |     |         |                          |                    |
| Release         |             |     |         |                          | Modification       |
| 10.11           |             |     |         |                          | Commandintroduced. |
| Command         | Information |     |         |                          |                    |
| Platforms       | Command     |     | context |                          | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logging        | filter        |     |     |     |     |
| -------------- | ------------- | --- | --- | --- | --- |
| logging filter | <FILTER-NAME> |     |     |     |     |
| [{enable       | | disable}]   |     |     |     |     |
[<SEQUENCE-ID>] {permit | deny} [event-id <EVENT-ID-RANGE>] [includes <REGEX>]
| [severity | <COMPARISON-OPERATOR> |     |     |     | <LEVEL>] |
| --------- | --------------------- | --- | --- | --- | -------- |
no <SEQUENCE-ID>
| resequence | <OLD-SEQUENCE-ID> |               |     | <NEW-SEQUENCE-ID> |     |
| ---------- | ----------------- | ------------- | --- | ----------------- | --- |
| no logging | filter            | <FILTER-NAME> |     |                   |     |
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
| Parameter     |     |     |     |     | Description                                |
| ------------- | --- | --- | --- | --- | ------------------------------------------ |
| <FILTER-NAME> |     |     |     |     | Specifiestheuniquenametoidentifythefilter. |
| enable        |     |     |     |     | Filtereventlogsgeneratedontheswitch.       |
83
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- |

Parameter

<SEQUENCE-ID>

deny

permit

<event-id>

Description

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

Remote syslog | 84

If a filter contains enable command, it is not recommended to configure this filter in the logging command
used for remote syslog server configuration. This is because, any event logs denied by the filter are already not

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

To deny logs having event ID 1301 and a range of event IDs from 1305 to 1309:

switch(config-logging-filter)# 20 deny event-id 1301,1305-1309

To permit logs having event ID 1300:

switch(config-logging-filter)# 30 permit event-id 1300

To permit logs with severity greater than or equal to err:

switch(config-logging-filter)# 30 permit severity ge err

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

85

Todenylogswithseveritygreaterthaninfo:
| switch(config-logging-filter)# |     |     | 30 deny | severity gt info |
| ------------------------------ | --- | --- | ------- | ---------------- |
TodenylogswitheventID1024andamessagematchingtheregularexpressionLLDP:
switch(config-logging-filter)# 40 deny event-id 1024 includes LLDP
Denyingalllogs:
switch(config-logging-filter)#
40 deny
ChangingthesequenceIDofanexistingrule:
| switch(config-logging-filter)# |         |         | resequence   | 20 70 |
| ------------------------------ | ------- | ------- | ------------ | ----- |
| Command History                |         |         |              |       |
| Release                        |         |         | Modification |       |
| 10.07orearlier                 |         |         | --           |       |
| Command Information            |         |         |              |       |
| Platforms                      | Command | context | Authority    |       |
Allplatforms configandconfig- Administratorsorlocalusergroupmemberswithexecutionrights
|                  | logging-filter |     | forthiscommand. |     |
| ---------------- | -------------- | --- | --------------- | --- |
| logging facility |                |     |                 |     |
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
local1
n
n local2
local3
n
n local4
Remotesyslog|86

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
local5
n
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| logging persistent-storage |     |     |     |
| -------------------------- | --- | --- | --- |
logging persistent-storage [severity {alert|crit|debug|emerg|err|info|notice|warning}]
| no logging persistent-storage |     |     |     |
| ----------------------------- | --- | --- | --- |
Description
Enablesordisablesstorageoflogsinstorage.Onlylogsofthespecifiedseverityandabovewillbe
preservedinthestorage.
Thenoformofthiscommanddisablesstorageoflogsinstorage.
| Parameter        |     |     | Description |
| ---------------- | --- | --- | ----------- |
| severity <LEVEL> |     |     |             |
Specifiestheseverityofthesyslogmessages:
n alert:Preservessyslogmessageswiththeseverityofalert
(6)andemergency (7)
crit:Preservessyslogmessageswiththeseverityof
n
critical (5)andabove.Default.
n debug:Preservessyslogmessageswiththeseverityofdebug
(0)andabove.
n emerg:Preservessyslogmessageswiththeseverityof
emergency (7)only.
n err:Preservessyslogmessageswiththeseverityoferr (4)
andabove.
info:Preservessyslogmessageswiththeseverityofinfo
n
(1)andabove.
87
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
n notice:Preservessyslogmessageswiththeseverityof
|     |     |     | notice | (2)andabove. |
| --- | --- | --- | ------ | ------------ |
n warning:Preservessyslogmessageswiththeseverityof
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
| switch(config)#     | no      | logging persistent-storage |              |     |
| ------------------- | ------- | -------------------------- | ------------ | --- |
| Command History     |         |                            |              |     |
| Release             |         |                            | Modification |     |
| 10.07orearlier      |         |                            | --           |     |
| Command Information |         |                            |              |     |
| Platforms           | Command | context                    | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Remotesyslog|88

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

Command History

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

89

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
diag on-demand
diag on-demand {fan-tray | line-module | management-module} [<SLOT-ID>]
Description
Runsthediagnostictestsforallmodulesorforaspecifiedmodule.
Parameter Description
| [fan-tray | | line-module | | management-module] |     |
| --------- | ------------- | -------------------- | --- |
Selectstheoptionsforenablingordisabling
runtimediagnosticsforaspecificmodule.
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
| -------------------- |             | ----- ----------- | -------      |
| -------------------- | ----------- | ----------------- | ------------ |
| LineModule           |             | 1/1               | 13 100%      |
| ManagementModule     |             | 1/1               | 13 100%      |
| Command              | History     |                   |              |
| Release              |             |                   | Modification |
| 10.07orearlier       |             |                   | --           |
| Command              | Information |                   |              |
RuntimeDiagnostics|90

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show diagnostic
show diagnostic {fan-tray | line-module | management-module} [<SLOT-ID>] {brief |
detail}
Description
Displaysthediagnostictestresultsforallmodulesorforaspecifiedmodule.
Parameter Description
[fan-tray | line-module | management-module] Selectstheoptionsforenablingordisabling
runtimediagnosticsforaspecificmodule.
fan-tray
Specifiestheenablingofdiagnosticmonitoring
specifictoafantray.
line-module Specifiestheenablingofdiagnosticmonitoring
specifictoalinemodule.
management-module Specifiestheenablingofdiagnosticmonitoring
specifictoamanagementmodule.
<SLOT-ID> Specifiesthemember/slotformanagement
modules(1/1),linemodules(1/1),andfantrays
(1/1-1/2).
Usage
Whennoparametersareusedinthecommand(show diagnostic),thecommandappliestoallmodules.
| switch# | show diagnostic | brief          |         |
| ------- | --------------- | -------------- | ------- |
| Module  |                 | ID Diagnostics | Success |
Performed
| -------------------- |         | ----- ----------- | -------      |
| -------------------- | ------- | ----------------- | ------------ |
| ManagementModule     |         | 1/1               | 13 100%      |
| LineModule           |         | 1/1               | 13 100%      |
| Command History      |         |                   |              |
| Release              |         |                   | Modification |
| 10.07orearlier       |         |                   | --           |
| Command Information  |         |                   |              |
| Platforms            | Command | context           | Authority    |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
91
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

| show diagnostic |        | events |     |
| --------------- | ------ | ------ | --- |
| show diagnostic | events |        |     |
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
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
RuntimeDiagnostics|92

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
---------------------
---------------------

To reboot without logging in, enter 'reboot' as the login user name.

ServiceOS login: reboot
reboot: Restarting system

.
Looking for SVOS.

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

93

Primary SVOS: Checking...Loading...Finding...Verifying...Booting...
|     | ServiceOS |     | Information: |     |                        |          |     |     |
| --- | --------- | --- | ------------ | --- | ---------------------- | -------- | --- | --- |
|     | Version:  |     |              |     | ML.01.07.0001-internal |          |     |     |
|     | Build     |     | Date:        |     | 2020-09-02             | 11:53:34 | PDT |     |
Build ID: ServiceOS:ML.01.07.0001-internal:64dfa8c99840:202009021153
|     | SHA: |     |     |     | 64dfa8c998408ec69d835a070f57aad610bc0383 |     |     |     |
| --- | ---- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
------------------------
------------------------
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
Enter0toboottheServiceOSloginCLI.
n
n Enter1toboottheprimaryfirmwareimage.
n Enter2tobootthesecondaryfirmwareimage.
ServiceOS|94

n Ifnoinputisgivenwithin5seconds,thedefaultbootprofileisselected.Alternatively,pressEnterto
selectthedefaultbootprofile.
Theimageselectedbytheuserduringbootisarun-timedecisiononlyandwillnotpersistacross
reboots.Thedefaultimagecanbeconfiguredusingtheboot set-defaultcommand.
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
Imageversion
n
n BuildID
n Builddate
ServiceOSwillthenpresentstatusandboottheimage.
Example
95
AOS-CX10.11DiagnosticsandSupportabilityGuide| (6200SwitchSeries)

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
ServiceOS|96

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
97
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

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
n Commandhistory(UpArrow)andsearch(Ctrl-R)
n Tabcompletionforfileandfoldernames(notCLIcommands)
n CommandabortusingCtrl-C
| Service | OS  | CLI | commands |     |     |     |     |     |     |
| ------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
boot
boot
Description
ServiceOS|98

Presentsyouwiththebootmenuprompt.Youcanthenspecifywhichbootprofile:primary,secondary,
orServiceOSconsole.
Example
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
| 0.             | Service           | OS Console  |         |                  |              |     |
| -------------- | ----------------- | ----------- | ------- | ---------------- | ------------ | --- |
| 1.             | Primary           | Software    | Image   | [ML.10.06.0001]  |              |     |
| 2.             | Secondary         | Software    | Image   | [ML.10.07.0001E] |              |     |
| Select         | profile(primary): |             |         |                  |              |     |
| Command        |                   | History     |         |                  |              |     |
| Release        |                   |             |         |                  | Modification |     |
| 10.07orearlier |                   |             |         |                  | --           |     |
| Command        |                   | Information |         |                  |              |     |
| Platforms      |                   | Command     | context |                  | Authority    |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
cat
cat <FILENAME/DIRECTORY-NAME>
Description
Printsthecontentsofafiletotheconsole.TheServiceOSdoesnotallowcommandoutputredirection,
sothiscommandisonlyusefulforreadingshorttextfiles.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<FILENAME/DIRECTORY-NAME>
Showsthecontentsofthespecifiedfileordirectory.
Example
Showingthecontentsof/nos/hosts:
| SVOS>     | cat | /nos/hosts            |     |     |     |           |
| --------- | --- | --------------------- | --- | --- | --- | --------- |
| 127.0.0.1 |     | localhost.localdomain |     |     |     | localhost |
99
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- |

SVOS>
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
cd path
cd path
Description
Changesthecurrentworkingdirectory.
Example
Changingthecurrentworkingdirectory:
cd /
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
config-clear
config-clear
Description
Configurestheswitchtosetallconfigurationsettingstofactorydefaultwhentheswitchisrestarted.
Thenexttimetheswitchstarts,thecurrentstartup-configisrenamedtostartup-config-fixme,and
anewstartup-configiscreatedwithfactorydefaultsettings.
ServiceOS|100

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
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
cp
cp [options] <SOURCE-FILENAME/SOURCE-DIRECTORY> <DESTINATION-FLENAME/DESTINATION-
DIRECTORY>
Description
Copiesfilesordirectories.
Parameter Description
[options] Selectstheoptionsforthecommand.
-d,-P Specifiesthepreservationofsymlinks(defaultif-
R).
-a Sameas-dpR.
R,-r Specifiesrecursiveness,allfiles,andsubdirectories
arecopied.
-L
Specifiesthefollowingofallsymlinks.
-H Specifiesthefollowingofsymlinksoncommand
101
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Parameter Description
line.
-p Specifiesthepreservationoffileattributesif
possible.
-f
Specifiestheoverwritingofafileordirectory.
-i Specifiesthepromptingbeforeanoverwrite.
-l,-s
Specifiesthecreationof(sym)links.
<SOURCE-FILENAME/SOURCE-DIRECTORY> Specifiesthenameofthesourcefileordirectory.
<DESTINATION-FLENAME/DESTINATION-DIRECTORY>
Specifiesthenameofthedestinationfileor
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
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
du
| du [options] | <FILENAME/DIRECTORY-NAME>... |     |     |
| ------------ | ---------------------------- | --- | --- |
Description
Showsestimateddiskspaceusedforeachfileordirectoryorboth.
| Parameter |     |     | Description                     |
| --------- | --- | --- | ------------------------------- |
| [options] |     |     | Selectstheoptionsforthecommand. |
| -a        |     |     | Showfilesizes.                  |
| -L        |     |     | Showsallsymlinks.               |
ServiceOS|102

| Parameter |     |     | Description                                            |
| --------- | --- | --- | ------------------------------------------------------ |
| -H        |     |     | Showssymlinksonacommandline.                           |
| -d, N     |     |     | Showslimitedoutputtodirectories(andfileswith-a)ofdepth |
lessthanN.
| -c  |     |     | Showsthetotaldiskspaceusageofallfilesordirectoriesorboth. |
| --- | --- | --- | --------------------------------------------------------- |
-l
Showsthecountsizesifhardlinked.
| -s  |     |     | Showsonlyatotalforeachargument. |
| --- | --- | --- | ------------------------------- |
-x
Doesnotshowdirectoriesondifferentfilesystems.
| -h  |     |     | Showsizesinhumanreadableformat(1K,243M,and2G). |
| --- | --- | --- | ---------------------------------------------- |
-m
Showsizesinmegabytes.
| -k  |     |     | Showsizesinkilobytes(default). |
| --- | --- | --- | ------------------------------ |
<FILENAME/DIRECTORY-NAME>
Specifiesthefileordirectoryorbothfordisplayingasize
estimate.
Example
Estimatingdiskspaceforthe/nosdirectory:
| SVOS> du | -ah /nos         |     |     |
| -------- | ---------------- | --- | --- |
| 196.4M   | /nos/primary.swi |     |     |
| 196.4M   | /nos             |     |     |
SVOS>
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
erase zeroize
erase zeroize
Description
SecurelyerasesanyuserdatacontainedontheSSD orotherstoragedevicesonthemanagement
module.
103
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Backupalldatabeforerunningthiscommandoralluser/configdatawillbelost.
Example
Erasinguserdata:
| SVOS>    | SVOS> | erase   | --help  |         |     |     |            |         |
| -------- | ----- | ------- | ------- | ------- | --- | --- | ---------- | ------- |
| Usage:   | erase | zeroize |         |         |     |     |            |         |
| Securely |       | erases  | storage | devices | on  | the | management | module. |
SVOS>
```
```
| SVOS> | erase | zeroize |     |     |     |     |     |     |
| ----- | ----- | ------- | --- | --- | --- | --- | --- | --- |
############################WARNING############################
This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the
| switch | unavailable |      | until   | the     | zeroization |     | is complete. |              |
| ------ | ----------- | ---- | ------- | ------- | ----------- | --- | ------------ | ------------ |
| This   | should      | take | several | minutes | to          | one | hour         | to complete. |
############################WARNING############################
| Continue |           | (y/n)?                 | y          |          |     |     |     |     |
| -------- | --------- | ---------------------- | ---------- | -------- | --- | --- | --- | --- |
| reboot:  |           | Restarting             | system     |          |     |     |     |     |
|          | ServiceOS | Information:           |            |          |     |     |     |     |
|          | Version:  | ML.01.07.0001-internal |            |          |     |     |     |     |
|          | Build     | Date:                  | 2020-09-02 | 11:53:34 |     | PDT |     |     |
Build ID: ServiceOS:ML.01.07.0001-internal:64dfa8c99840:202009021153
|                  | SHA:        | 64dfa8c998408ec69d835a070f57aad610bc0383 |           |             |                             |                         |                   |            |
| ---------------- | ----------- | ---------------------------------------- | --------- | ----------- | --------------------------- | ----------------------- | ----------------- | ---------- |
| ################ |             |                                          | Preparing | for         | zeroization                 |                         | ################# |            |
| ################ |             |                                          | Storage   | zeroization |                             | ####################### |                   |            |
| ################ |             |                                          | WARNING:  | DO          | NOT POWER                   |                         | OFF UNTIL         | ########## |
| ################ |             |                                          |           | ZEROIZATION |                             | IS                      | COMPLETE          | ########## |
| ################ |             |                                          | This      | should      | take                        | several                 | minutes           | ########## |
| ################ |             |                                          | to one    | hour        | to complete                 |                         |                   | ########## |
| ################ |             |                                          | Restoring | files       | ########################### |                         |                   |            |
| Command          | History     |                                          |           |             |                             |                         |                   |            |
| Release          |             |                                          |           |             |                             | Modification            |                   |            |
| 10.07orearlier   |             |                                          |           |             |                             | --                      |                   |            |
| Command          | Information |                                          |           |             |                             |                         |                   |            |
| Platforms        |             | Command                                  |           | context     |                             | Authority               |                   |            |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
exit
exit
ServiceOS|104

Description
LogstheuseroutfromtheSVOS>prompt.
Example
LogingtheuseroutfromtheSVOS>prompt:
| SVOS> exit    |     |      |            |         |            |        |             |     |
| ------------- | --- | ---- | ---------- | ------- | ---------- | ------ | ----------- | --- |
| (C) Copyright |     | 2023 | Hewlett    | Packard | Enterprise |        | Development | LP  |
|               |     |      | RESTRICTED |         | RIGHTS     | LEGEND |             |     |
Confidential computer software. Valid license from Hewlett Packard Enterprise
Development LP required for possession, use or copying. Consistent with FAR
12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the
| U.S. Government |     | under | vendor's |     | standard | commercial | license. |     |
| --------------- | --- | ----- | -------- | --- | -------- | ---------- | -------- | --- |
To reboot without logging in, enter 'reboot' as the login user name.
| ServiceOS      | login:      |     |         |     |              |     |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- |
| Command        | History     |     |         |     |              |     |     |     |
| Release        |             |     |         |     | Modification |     |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |     |
| Command        | Information |     |         |     |              |     |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
format
format
Description
Configurestheprimarystoragedevicewiththecorrectpartitionandfilesystemformatting.This
commandremovesallpre-existingdataontheprimarystoragedevice.
Example
Configuringtheprimarystoragedevicewiththecorrectpartitionandfilesystemformatting:
| SVOS> format |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
##################WARNING####################
| The following |         | action     | will    | cause           | all   | data on |     |     |
| ------------- | ------- | ---------- | ------- | --------------- | ----- | ------- | --- | --- |
| the primary   | storage |            | device  | to be           | lost. | After   |     |     |
| formatting    | has     | completed, |         | a reboot        | will  | be      |     |     |
| initiated     | to      | complete   | storage | initialization. |       |         |     |     |
##################WARNING####################
105
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- |

| Continue?      | (y/n):      | y       |                       |              |
| -------------- | ----------- | ------- | --------------------- | ------------ |
| Working...This |             | may     | take a few minutes... |              |
| Command        | History     |         |                       |              |
| Release        |             |         |                       | Modification |
| 10.07orearlier |             |         |                       | --           |
| Command        | Information |         |                       |              |
| Platforms      |             | Command | context               | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
identify
identify
Description
PrintstheversionoftheSVOSandoftheUEFIBIOS.
| Command        | History     |         |         |              |
| -------------- | ----------- | ------- | ------- | ------------ |
| Release        |             |         |         | Modification |
| 10.07orearlier |             |         |         | --           |
| Command        | Information |         |         |              |
| Platforms      |             | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip
| ip {show | | dhcp | | disable | | addr <ADDR-NETMASK-GATEWAY>} |     |
| -------- | ------ | --------- | ------------------------------ | --- |
Description
ShowsorconfigurestheportwithastaticIPaddress(IPv4only)orenablestheDHCPclientontheport.
AnaddressissetonlyifaDHCPserverisavailabletoprovideone.
Parameter Description
| {show | | dhcp | | disable | | addr <ADDR-NETMASK-GATEWAY>} |     |
| ----- | -------- | ------- | ------------------------------ | --- |
SelectstheoptionsfortheOOBM
port.
ServiceOS|106

Parameter Description
show ShowstheOOBMport.
dhcp ConfigurestheportwithaDHCP
address.
disable
DisablestheOOBMport.
| addr <ADDR-NETMASK-GATEWAY> |     |     | ConfigurestheportwithastaticIP |
| --------------------------- | --- | --- | ------------------------------ |
address(IPv4only).Specifyaddress,
netmask,andgatewayasA.B.C.D.
Example
ConfiguringtheportwithaDHCPIPaddress:
| SVOS> ip     | dhcp          |     |     |
| ------------ | ------------- | --- | --- |
| SVOS> ip     | show          |     |     |
| Interface    | : Link        | Up  |     |
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
6200 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ls
| ls [<OPTIONS>] | [<FILE-NME>] |     |     |
| -------------- | ------------ | --- | --- |
Description
Thiscommandlistsdirectorycontents.
| Parameter |     |     | Description                    |
| --------- | --- | --- | ------------------------------ |
| <OPTIONS> |     |     | Specifiesoptionsforthecommand. |
107
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

Parameter

Description

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

-w <N>

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

With -l, sort by atime.

With -l, it shows a sort in one column by ctime

Assumes that the terminal has the number of columns wide
as specified by <N>.

Service OS | 108

| Parameter        |     |     |         |          |     | Description                      |     |     |     |
| ---------------- | --- | --- | ------- | -------- | --- | -------------------------------- | --- | --- | --- |
| --color[={always |     |     | | never | | auto}] |     | Controlscolorintheoutput.        |     |     |     |
| <FILE-NAME>      |     |     |         |          |     | Specifiesthenameofthefiletolist. |     |     |     |
Example
Listingdirectorycontents:
| SVOS>      | ls -la | /nos |     |     |           |       |     |          |             |
| ---------- | ------ | ---- | --- | --- | --------- | ----- | --- | -------- | ----------- |
| drwxr-xr-x |        | 3    | 0   | 0   |           | 4096  | Nov | 21 03:19 | .           |
| drwxr-xr-x |        | 11   | 0   | 0   |           | 220   | Nov | 21 03:21 | ..          |
| drwx------ |        | 2    | 0   | 0   |           | 16384 | Nov | 21 03:20 | lost+found  |
| -rwxr-xr-x |        | 1    | 0   | 0   | 205957424 |       | Nov | 21 03:19 | primary.swi |
SVOS>
| Command        | History     |         |     |         |              |     |     |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- | --- | --- | --- |
| Release        |             |         |     |         | Modification |     |     |     |     |
| 10.07orearlier |             |         |     |         | --           |     |     |     |     |
| Command        | Information |         |     |         |              |     |     |     |     |
| Platforms      |             | Command |     | context | Authority    |     |     |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
md5sum
| md5sum [-c | |   | -s | -w] | [<FILE-NAME>] |     |     |     |     |     |     |
| ---------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
Description
ThiscommandcomputesandcheckstheMD5messagedigest.
| Parameter |          |     |     |     | Description |     |     |     |     |
| --------- | -------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
| [-c |     | -s | -w] |     |     |     |             |     |     |     |     |
Selectstheoptionsforthecommand.
| -c  |     |     |     |     | Specifiestocheckthesumsagainstthelistinfiles. |     |     |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
-s
Specifiesnotoutputanything,statuscodeshowssuccess.
| -w  |     |     |     |     | Specifiestowarnaboutimproperlyformattedchecksumlines. |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
<FILE-NAME>
Specifiesthefilenametorunthechecksumagainst.
Example
ComputingandcheckingtheMD5messagedigestfor/nos/primary.swi:
109
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

| SVOS> md5sum                     | /nos/primary.swi |     |                  |
| -------------------------------- | ---------------- | --- | ---------------- |
| 93ffc89e7ec357854704d8e450c4b7ab |                  |     | /nos/primary.swi |
SVOS>
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Example
Makingthedirdirectory:
| SVOS> mkdir         | dir |     |              |
| ------------------- | --- | --- | ------------ |
| Command History     |     |     |              |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
ServiceOS|110

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
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
| MountingalloftheSSD |         | partitions: |              |
| ------------------- | ------- | ----------- | ------------ |
| SVOS> mount         | all     |             |              |
| SVOS> mount         | usb     |             |              |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mv
| mv [-f | -i | | -n] <TARGET-DIRECTORY> |     |     |
| ----------- | ------------------------ | --- | --- |
Description
Thiscommandmoves(renames)files.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
-f
Specifiesnottopromptbeforeoverwriting.
111
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
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
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| password | (svos) |     |     |
| -------- | ------ | --- | --- |
password
Description
SetstheadminuseraccountpasswordforbothServiceOSandAOS-CXoncetheuserbootsintoAOS-CX
andsavestheconfiguration.Thiswilloverwritethepreviouspasswordifoneexists.Userinputis
maskedwithasterisks.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Settingtheadminaccountpassword:
| SVOS> password          |                   |     |     |
| ----------------------- | ----------------- | --- | --- |
| Enter password:******** |                   |     |     |
| Confirm                 | password:******** |     |     |
SVOS>
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
ServiceOS|112

| Platforms |     | Command | context |     | Authority |     |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
ServiceOS(SVOS>)
forthiscommand.
ping
ping <HOST-IP-ADDRESS>
Description
Pingsnetworkhostsfordebugpurposes.
| Parameter         |     |     |     |     | Description                |     |     |     |
| ----------------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
| <HOST-IP-ADDRESS> |     |     |     |     | SpecifiesthehostIPaddress. |     |     |     |
Example
Pinginganetworkhost:
| SVOS> ping     | 10.0.8.10 |              |     |       |        |            |     |     |
| -------------- | --------- | ------------ | --- | ----- | ------ | ---------- | --- | --- |
| PING 10.0.8.10 |           | (10.0.8.10): |     | 56    | data   | bytes      |     |     |
| 64 bytes       | from      | 10.0.8.10:   |     | seq=0 | ttl=63 | time=3.496 |     | ms  |
| 64 bytes       | from      | 10.0.8.10:   |     | seq=1 | ttl=63 | time=0.367 |     | ms  |
| 64 bytes       | from      | 10.0.8.10:   |     | seq=2 | ttl=63 | time=0.380 |     | ms  |
| 64 bytes       | from      | 10.0.8.10:   |     | seq=3 | ttl=63 | time=0.282 |     | ms  |
| 64 bytes       | from      | 10.0.8.10:   |     | seq=4 | ttl=63 | time=0.669 |     | ms  |
^C
| --- 10.0.8.10 |              | ping | statistics |                   | ---       |     |     |             |
| ------------- | ------------ | ---- | ---------- | ----------------- | --------- | --- | --- | ----------- |
| 5 packets     | transmitted, |      | 5          | packets           | received, |     | 0%  | packet loss |
| round-trip    | min/avg/max  |      | =          | 0.282/1.038/3.496 |           |     | ms  |             |
SVOS>
| Command        | History     |         |         |     |              |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- | --- |
| Release        |             |         |         |     | Modification |     |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |     |
| Command        | Information |         |         |     |              |     |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |     |
6200 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
pwd
pwd
Description
Displaysthecurrentworkingdirectory.
Example
113
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- |

Displayingthecurrentworkingdirectory:
| SVOS> | pwd |     |     |
| ----- | --- | --- | --- |
/home
SVOS>
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
reboot
reboot
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
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
rm
| rm [-f | | -i | -R | -r] | <FILE-NAME> |     |
| -------- | ------------- | ----------- | --- |
Description
Removesfilesordirectories.
ServiceOS|114

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
[-f | -i | -R | -r] Selectstheoptionsforremovingfilesordirectories.
| -f      |     |     | Neverpromptbeforeremovingfilesordirectories.  |
| ------- | --- | --- | --------------------------------------------- |
| -i      |     |     | Alwayspromptbeforeremovingfilesordirectories. |
| -R | -r |     |     | Recursive.                                    |
Example
Removingthefilenamedfoo:
| SVOS> rm            | foo     |         |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Command History |     |     |     |
| --------------- | --- | --- | --- |
115
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

| Release        |             |     |         | Modification |     |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier |             |     |         | --           |     |     |     |
| Command        | Information |     |         |              |     |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
secure-mode
| secure-mode | <enhanced | | standard |     | | status> |     |     |     |
| ----------- | --------- | ---------- | --- | --------- | --- | --- | --- |
Description
Setsthesecuremodetoenhancedorstandardsecuremode.Alsocandisplaythecurrentsecuremode.
Azeroizationisrequiredbeforeswitchingbetweenenhancedandstandardsecuremodes.
Thecommandalsodisplaysamessagenotifyingtheuserthattheyarealreadyinthetargetedsecure
mode.
Example
Settingthesecuremodetoenhancedorstandard:
| SVOS>  | secure-mode | --help    |     |            |           |     |     |
| ------ | ----------- | --------- | --- | ---------- | --------- | --- | --- |
| Usage: | secure-mode | <enhanced |     | | standard | | status> |     |     |
Set or retrieve the secure mode setting. Requires a zeroization to change modes.
SVOS>
```
```
| SVOS> | secure-mode | enhanced |     |     |     |     |     |
| ----- | ----------- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| This | will set the | switch | into | enhanced | secure | mode. | Before |
| ---- | ------------ | ------ | ---- | -------- | ------ | ----- | ------ |
enhanced secure mode is enabled, the switch must securely erase
| all customer | data            | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | --------------- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This         | will initiate   | a reboot | and          | render | the switch |              | unavailable |
| until        | the zeroization |          | is complete. |        |            |              |             |
| This         | should take     | several  | minutes      | to     | one hour   | to complete. |             |
############################WARNING############################
| Continue | (y/n)?     | y      |     |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |     |
```
```
| SVOS> | secure-mode | standard |     |     |     |     |     |
| ----- | ----------- | -------- | --- | --- | --- | --- | --- |
############################WARNING############################
| This | will set the | switch | into | standard | secure | mode. | Before |
| ---- | ------------ | ------ | ---- | -------- | ------ | ----- | ------ |
standard secure mode is enabled, the switch must securely erase
| all customer | data            | and      | reset the    | switch | to factory |              | defaults.   |
| ------------ | --------------- | -------- | ------------ | ------ | ---------- | ------------ | ----------- |
| This         | will initiate   | a reboot | and          | render | the switch |              | unavailable |
| until        | the zeroization |          | is complete. |        |            |              |             |
| This         | should take     | several  | minutes      | to     | one hour   | to complete. |             |
ServiceOS|116

############################WARNING############################
| Continue | (y/n)? y   |        |     |     |     |     |
| -------- | ---------- | ------ | --- | --- | --- | --- |
| reboot:  | Restarting | system |     |     |     |     |
```
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
| Command        | History     |         |     |              |     |     |
| -------------- | ----------- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |     | Modification |     |     |
| 10.07orearlier |             |         |     | --           |     |     |
| Command        | Information |         |     |              |     |     |
| Platforms      | Command     | context |     | Authority    |     |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sh
sh
Description
Launchesabashshellforsupportpurposes.Toquitbash,enterexit.
Thiscommandisnotavailableifenhancedsecuremodeisset.
Example
Launchingabashshell:
| SVOS> sh |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
switch:/cli/fs/home#
117
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- | --- |

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| SVOS> umount        | all     |         |              |
| ------------------- | ------- | ------- | ------------ |
| SVOS> umount        | usb     |         |              |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ServiceOS|118

update
| update {primary | | secondary} | <IMAGE> |     |     |
| --------------- | ------------ | ------- | --- | --- |
Description
Verifiesandinstallsaproductimage.Theusercanselecttheprimaryorsecondarybootprofileto
updateandthelocationofthefile.
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
| Command        | History |     |              |     |
| -------------- | ------- | --- | ------------ | --- |
| Release        |         |     | Modification |     |
| 10.07orearlier |         |     | --           |     |
119
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
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
blocksizeissetto1468,whichcanbeoverriddenwiththe
-boption.
| -g               |     |     | Specifiestogetafile.                         |     |
| ---------------- | --- | --- | -------------------------------------------- | --- |
| -l               |     |     | Specifiesalocalfile.                         |     |
| -p               |     |     | Specifiestoputafileinremotelocation.         |     |
| -r <REMOTE-FILE> |     |     | Specifiesaremotefile.                        |     |
| <PORT>           |     |     | Specifiestheportfortransfer.Ifnoportoptionis |     |
specified,TFTPusesthestandardUDPport69bydefault.
Example
Transferringfiles:
| SVOS> tftp | -b 65464 | -g -r XL.10.00.0002.swi.swi |     | 192.0.2.1 |
| ---------- | -------- | --------------------------- | --- | --------- |
XL.10.00.0002 100% |*******************************| 178M 0:00:00 ETA
SVOS>
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
6200 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ServiceOS|120

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
Allplatforms ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
121
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | ------------------ | --- |

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
Description
Displayswhetheranyprogrammabledevicesareinneedofanupdate.
122
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | ------------------ | --- | --- |

Withoutthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetothecurrently
runningAOS-CXimage.
Withthenext-bootparameter,thiscommanddisplaysneededupdatesrelativetoanAOS-CXimagefile
inthepersistentstorageoftheswitch,whichmightbedifferentfromthecurrentlyrunningimage.If
eithertheprimaryorsecondaryparameterisspecified,thiscommandqueriesthatspecificAOS-CX
imagefile.Otherwise,itqueriesthedefaultAOS-CXimagefileassetbythemostrecentboot systemor
boot set-defaultcommand.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
In-SystemProgramming|123

Chapter 16

Selftest

Selftest

Power On Self Test (POST) is the first task which verifies the hardware functionality of various modules
during boot-up. Based on the criticality of the test, the selftest module decides whether to go ahead with
the boot-up sequence of a particular subsystem or interface during a POST failure.

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

When fastboot is enabled, most tests under a Power On Self Test (POST) are skipped. By default,
fastboot is enabled.

After disabling fastboot, save switch configurations and then reboot for POST to run. POST verifies the
hardware functionality of various modules during boot-up. Based on the criticality of the test, the
selftest module decides whether to go ahead with the boot-up sequence of a particular subsystem or
interface during a POST failure.

POST runs memory built-in selftest (BISTs) and front-end port loopback tests. Memory BISTs verify the
internal and external memory blocks present in the module. The memory tables are critical for proper
functionality of the system so any failures in these tests results in the corresponding subsystem to be
marked as "Failed" and thus that subsystem is not available for use.

Front-end port loopback tests verify the physical port front-end interface. These tests check if a
particular interface can function properly. A test failure means that a particular interface has been
marked as "Failed" and is now unavailable for use.

Examples

Enabling fastboot:

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

124

| switch# | configure | terminal |     |
| ------- | --------- | -------- | --- |
switch(config)#
fastboot
| switch(config)# | end                 |     |     |
| --------------- | ------------------- | --- | --- |
| switch#         | show running-config |     |     |
| Current         | configuration:      |     |     |
!
| !Version   | AOS-CX ML.10.06.0001 |        |     |
| ---------- | -------------------- | ------ | --- |
| module 1/1 | product-number       | jl726a |     |
!
!
!
!
!
!
!
vlan 1
| interface   | 1/1/1 |     |     |
| ----------- | ----- | --- | --- |
| no shutdown |       |     |     |
Disablingfastboot:
| switch# | configure | terminal |     |
| ------- | --------- | -------- | --- |
switch(config)#
|                 | no    | fastboot |     |
| --------------- | ----- | -------- | --- |
| switch(config)# | end   |          |     |
| switch(config)# | write | mem      |     |
Configuration changes will take time to process, please be patient.
| switch# | show running-config |     |     |
| ------- | ------------------- | --- | --- |
| Current | configuration:      |     |     |
!
| !Version   | AOS-CX ML.10.06.0001 |        |     |
| ---------- | -------------------- | ------ | --- |
| module 1/1 | product-number       | jl726a |     |
!
!
!
no fastboot
!
!
!
!
vlan 1
| interface      | 1/1/1       |         |              |
| -------------- | ----------- | ------- | ------------ |
| no shutdown    |             |         |              |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show selftest
Selftest|125

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
126
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- |

| 1/1/2   | skipped        | 0x0         |                     |     |     |
| ------- | -------------- | ----------- | ------------------- | --- | --- |
| switch# | show selftest  | line-module | 1/1 interface       |     |     |
| Name    | Status         | ErrorCode   | LastRunTime         |     |     |
| ------- | -------------- | ---------   | ------------------- |     |     |
| 1/1/1   | skipped        | 0x0         |                     |     |     |
| 1/1/2   | skipped        | 0x0         |                     |     |     |
| 1/1/3   | skipped        | 0x0         |                     |     |     |
| 1/1/31  | skipped        | 0x0         |                     |     |     |
Displayingtheoutputwhenfastbootisdisabled:
switch#
show selftest
| Name           | Id Status           |         | ErrorCode    | LastRunTime         |          |
| -------------- | ------------------- | ------- | ------------ | ------------------- | -------- |
| ----------     | ---- -------------- |         | ----------   | ------------------- |          |
| LineModule     | 1/1 passed          |         | 0x0          | 2018-02-16          | 18:15:53 |
| Command        | History             |         |              |                     |          |
| Release        |                     |         | Modification |                     |          |
| 10.07orearlier |                     |         | --           |                     |          |
| Command        | Information         |         |              |                     |          |
| Platforms      | Command             | context | Authority    |                     |          |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Selftest|127

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
erase all zeroize

Description

Restores the switch to its factory default configuration. You will be prompted before the procedure
starts. Once complete, the switch will restart from the primary image with factory default settings.

Usage

The erase all command is always available in the CLI. On running the erase all command, the switch
is restored to a factory default settings, but retains the enhanced secure mode settings.

The erase all zeroize command is not available in the CLI when enhanced secure mode is enabled.

This command restore the switch to a factory default settings. On running the erase all zeroize
command in enhanced secure mode, displays a notification stating that the command is unavailable in
enhanced secure mode.

Back up all data before running this command as all configuration settings will be lost.

Example

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

128

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
disabled:

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

Please register your products now at: https://asp.arubanetworks.com

Zeroization | 129

Whenyouloginafterzeroization,yougetaprompttocreateapasswordfortheadministratoraccount.Youcan
setthepasswordasblank(tosetthepasswordasblank,hitenterattheprompt)ortype1to32printableASCII
characters,excludingspacesandquestionmarks(?).Formoreinformationonpasswordrequirements,see
PasswordrequirementsintheSecurityGuide.
| switch | login: | admin |     |     |
| ------ | ------ | ----- | --- | --- |
Password:
| Please         | configure     | the 'admin' | user account    | password.     |
| -------------- | ------------- | ----------- | --------------- | ------------- |
| Enter new      | password:     | *****       |                 |               |
| Confirm        | new password: | *****       |                 |               |
| Command        | History       |             |                 |               |
| Release        |               |             | Modification    |               |
| 10.11.1010     |               |             | Introducederase | allCLIcommand |
| 10.07orearlier |               |             | --              |               |
| Command        | Information   |             |                 |               |
| Platforms      | Command       | context     | Authority       |               |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
130
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

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
| Parameter |                   |     | Description                                   |     |
| --------- | ----------------- | --- | --------------------------------------------- | --- |
| notify    | <event|debug|all> |     | Specifiesthetypeoflognotification.            |     |
|           |                   |     | n Event:Displaystheeventlogmessages.(Default) |     |
|           |                   |     | n Debug:Displaysthedebuglogmessages.          |     |
|           |                   |     | n All:Displaysbotheventanddebuglogmessages.   |     |
| severity  | <level>           |     |                                               |     |
Specifiestheseveritylevelforthelogs.Thedifferentseveritylevels
areemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
filter <keyword> Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
131
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     |     | (6200SwitchSeries) |     |
| --------------------------------------------- | --- | --- | ------------------ | --- |

Examples
Configuringconsoleloggingintheconsolesession:
switch(config)#
|                  |             | logging | console |              |                    |               |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
TerminalMonitor|132

| switch#             | show terminal-monitor |          |              |     |
| ------------------- | --------------------- | -------- | ------------ | --- |
| Terminal-monitor    | is                    | disabled |              |     |
| Command History     |                       |          |              |     |
| Release             |                       |          | Modification |     |
| 10.07orearlier      |                       |          | --           |     |
| Command Information |                       |          |              |     |
| Platforms           | Command               | context  | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| severity <level> |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
Specifiestheseveritylevelforthelogs.Thedifferentseverity
levelsareemergency,critical,error,warning,notice,information
(default),alert,anddebug(showsallseverities).
filter <keyword> Specifiesthefilterbyapplyingkeywordforthelogs.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingterminalmonitor:
133
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- |

| switch#             | terminal-monitor |         |              |                     |
| ------------------- | ---------------- | ------- | ------------ | ------------------- |
| Terminal-monitor    | is               | enabled | successfully |                     |
| switch#             | terminal-monitor |         | notify       | all                 |
| Terminal-monitor    | is               | enabled | successfully |                     |
| switch#             | terminal-monitor |         | notify       | event severity info |
| Terminal-monitor    | is               | enabled | successfully |                     |
| switch#             | terminal-monitor |         | filter       | lldp                |
| Terminal-monitor    | is               | enabled | successfully |                     |
| Command History     |                  |         |              |                     |
| Release             |                  |         |              | Modification        |
| 10.07orearlier      |                  |         |              | --                  |
| Command Information |                  |         |              |                     |
| Platforms           | Command          | context |              | Authority           |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
TerminalMonitor|134

|                 |     |                 |               |        | Chapter       | 19  |
| --------------- | --- | --------------- | ------------- | ------ | ------------- | --- |
|                 |     | Troubleshooting |               | Web UI | and REST      | API |
|                 |     |                 |               |        | Access Issues |     |
| Troubleshooting | Web | UI and REST API | Access Issues |        |               |     |
Thefollowingsectiondescribessymptoms,causesandcorrectiveactionsfor401or404errors.
| HTTP 404 | error when | accessing | the | switch URL |     |     |
| -------- | ---------- | --------- | --- | ---------- | --- | --- |
Symptom
TheswitchisoperationalandyouareusingthecorrectURLfortheswitch,butattemptstoaccessthe
RESTAPIorWebUIresultinanHTTP404"Pagenotfound"error.
Cause
RESTAPIaccessisnotenabledontheVRFthatcorrespondstotheaccessportyouareusing.For
example,youareattemptingtoaccesstheRESTAPIorWebUIfromthemanagement(OOBM)port,and
accessisnotenabledonthemgmtVRF.
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
Whenthesessionidletimeoutexpires,thesessionisterminatedautomatically.
135
| AOS-CX10.11DiagnosticsandSupportabilityGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------------------------- | --- | ------------------ | --- | --- | --- | --- |

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions, Web UI sessions, and real-time notification subscriptions.

Troubleshooting Web UI and REST API Access Issues | 136

Support and Other Resources

Chapter 20

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

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

Airheads social
forums and
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

Aruba Hardware
Documentation
and Translations

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

137

Portal
| Arubasoftware | https://asp.arubanetworks.com/downloads |     |
| ------------- | --------------------------------------- | --- |
| Software      | https://lms.arubanetworks.com/          |     |
licensing
End-of-Life https://www.arubanetworks.com/support-services/end-of-life/
information
| ArubaDeveloper | https://developer.arubanetworks.com/ |     |
| -------------- | ------------------------------------ | --- |
Hub
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
| Aruba | Support | Portal |
| ----- | ------- | ------ |
https://asp.arubanetworks.com/downloads
IfyouareunabletofindyourproductintheArubaSupportPortal,youmayneedtosearchMy
Networking,whereoldernetworkingproductscanbefound:
My Networking
https://www.hpe.com/networking/support
Toviewandupdateyourentitlements,andtolinkyourcontractsandwarrantieswithyourprofile,goto
theHewlettPackardEnterpriseSupportCenterMore Information on Access to Support Materials
page:
https://support.hpe.com/portal/site/hpsc/aae/home/
AccesstosomeupdatesmightrequireproductentitlementwhenaccessedthroughtheHewlettPackard
EnterpriseSupportCenter.YoumusthaveanHPPassportsetupwithrelevantentitlements.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://asp.arubanetworks.com/notifications/subscriptions(requiresanactiveArubaSupportPortal
(ASP)accounttomanagesubscriptions).SecuritynoticesareviewablewithoutanASPaccount.
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
SupportandOtherResources|138

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs,
product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.11 Diagnostics and Supportability Guide | (6200 Switch Series)

139