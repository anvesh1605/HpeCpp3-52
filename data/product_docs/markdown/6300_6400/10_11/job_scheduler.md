AOS-CX 10.11 Job Scheduler
Guide

All Switch Series

Published: February 2023
Edition: 2

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General
Public License, and/or certain other open source licenses. A complete machine-readable copy of the
source code corresponding to such code is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, send a check or
money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

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
| Contents                            |                                  |           | 3   |
| ----------------------------------- | -------------------------------- | --------- | --- |
| About                               | this document                    |           | 4   |
| Applicableproducts                  |                                  |           | 4   |
| Latestversionavailableonline        |                                  |           | 4   |
| Commandsyntaxnotationconventions    |                                  |           | 4   |
| Abouttheexamples                    |                                  |           | 5   |
| Identifyingswitchportsandinterfaces |                                  |           | 6   |
| Identifyingmodularswitchcomponents  |                                  |           | 7   |
| Job Scheduler                       |                                  |           | 8   |
| WorkingwithJobScheduler             |                                  |           | 8   |
|                                     | Porttoggleexample                |           | 8   |
|                                     | Switchrebootexample              |           | 10  |
| JobSchedulercommands                |                                  |           | 11  |
|                                     | job                              |           | 11  |
|                                     | schedule                         |           | 13  |
|                                     | showcapacities(job,schedule)     |           | 16  |
|                                     | showjob                          |           | 17  |
|                                     | showrunning-config(job,schedule) |           | 19  |
|                                     | showschedule                     |           | 21  |
| Support                             | and Other                        | Resources | 23  |
| AccessingArubaSupport               |                                  |           | 23  |
| AccessingUpdates                    |                                  |           | 24  |
|                                     | ArubaSupportPortal               |           | 24  |
|                                     | MyNetworking                     |           | 24  |
| WarrantyInformation                 |                                  |           | 24  |
| RegulatoryInformation               |                                  |           | 24  |
| DocumentationFeedback               |                                  |           | 25  |
3
AOS-CX10.11JobSchedulerGuide| (4100i,6xxx,8xxx,9300,10000SwitchSeries)

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A, R8Q69A, R8Q70A,

R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C, JL704C, JL705C,
JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n Aruba 8400 Switch Series (JL366A, JL363A, JL687A)

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items
that appear like the example text in the previous column are to be entered
exactly as shown and are required unless enclosed in brackets ([ ]).

AOS-CX 10.11 Job Scheduler Guide | (4100i, 6xxx, 8xxx, 9300, 10000 Switch Series)

4

Convention

Usage

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

Indicates the configuration context for a feature. For example:

switch(config-if)#

Identifies the interface context.

About this document | 5

| Variable information |     | in CLI prompts |     |
| -------------------- | --- | -------------- | --- |
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
| On the 4100i | Switch | Series |     |
| ------------ | ------ | ------ | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6000 | and 6100 | Switch Series |     |
| ----------- | -------- | ------------- | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6200 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to8.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1on
member1.
| On the 6300 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4onmember1.
| On the 6400 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
6
| AOS-CX10.11JobSchedulerGuide| |     | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ---------------------------------------- | --- |

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx, 9300, and 10000 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

On the 8400 Switch Series

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

About this document | 7

Chapter 2
Job Scheduler
Job Scheduler
TheJobSchedulerenablesyoutoexecutebatchesofCLIcommandsonauser-configuredscheduleor
n
interval.JobSchedulercanbeused,forexample,toscheduleactivitiessuchasporttoggles,switch
reboots,QoSpolicychanges,systemhealthstatuschecks,statisticsclearing,clean-up,andsavingthe
runningconfiguration.
n Schedulescantriggerjobsbasedoncalendardateandtimeoratperiodicintervals.
n Jobscanbescheduledtoexecuteasfrequentlyasonceeverythirtyminutes.
n Whenexecuted,commandswithsimple(y/n)prompts(suchasboot system)willbeautomatically
confirmedwith"y."Othercommandsrequiringmorecomplexuserinput(suchaspasswordchange)
cannotbeused.
| Working | with Job | Scheduler |     |
| ------- | -------- | --------- | --- |
TohelpunderstandhowtoworkwiththeJobScheduler,severalbasicexamplesarepresented,followed
bydetaileddescriptionsofthecommandsinvolvedunderJobSchedulercommands.
| Port toggle | example |     |     |
| ----------- | ------- | --- | --- |
ThisexamplecreatesaporttogglejobandthenschedulesthejobforexecutiononMondayandFriday
nightat11:45PM.
CreatingaporttogglejobnamedPTog1:
| switch(config)#           | job | PTog1            |                    |
| ------------------------- | --- | ---------------- | ------------------ |
| switch(config-job-PTog1)# |     | desc Toggle      | port 1/1/1         |
| switch(config-job-PTog1)# |     | 10 cli config    |                    |
| switch(config-job-PTog1)# |     | 20 cli interface | 1/1/1              |
| switch(config-job-PTog1)# |     | 30 cli shutdown  |                    |
| switch(config-job-PTog1)# |     | 40 delay         | 10 cli no shutdown |
| switch(config-job-PTog1)# |     | 50 cli end       |                    |
| switch(config-job-PTog1)# |     | exit             |                    |
CreatingaschedulenamedPT2xWthatrunstheporttogglejobPTog1onMondaysandFridaysat11:45
PM,startingonAugust22021,withaone-yearduration:
| switch(config)# | schedule | PT2xW |     |
| --------------- | -------- | ----- | --- |
switch(config-schedule-PT2xW)# desc Monday & Friday 11:45 PM port toggles
| switch(config-schedule-PT2xW)# |     | 10 job | PTog1 |
| ------------------------------ | --- | ------ | ----- |
switch(config-schedule-PT2xW)# trigger on 23:45 weekly 2,6 count 104 start 2021-
08-02
| switch(config-schedule-PT2xW)# |     | exit |     |
| ------------------------------ | --- | ---- | --- |
Showingtheporttogglejobinformationafterfirstexecution:
8
| AOS-CX10.11JobSchedulerGuide| | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ---------------------------------------- | --- | --- |

| switch#     | show      | job PTog1 |       |           |      |       |     |
| ----------- | --------- | --------- | ----- | --------- | ---- | ----- | --- |
| Job Name    | : PTog1   |           |       |           |      |       |     |
| Enabled     |           |           |       | : Yes     |      |       |     |
| Description |           |           |       | : Toggle  | port | 1/1/1 |     |
| Status      |           |           |       | : waiting |      |       |     |
| Number      | of        | commands  |       | : 5       |      |       |     |
| Total       | execution |           | count | : 1       |      |       |     |
| Failed      | execution |           | count | : 0       |      |       |     |
| Job         | execution | history   |       |           |      |       |     |
---------------------
| Instance  |              | number   |      | : 1       |     |            |      |
| --------- | ------------ | -------- | ---- | --------- | --- | ---------- | ---- |
| Execution |              | status   |      | : success |     |            |      |
| Execution |              | start    | time | : Mon     | Aug | 2 23:45:00 | 2021 |
| Execution |              | duration |      | : 10s     |     |            |      |
| Job       | CLI commands |          |      |           |     |            |      |
----------------
| 10  | cli config    |        |             |     |     |     |     |
| --- | ------------- | ------ | ----------- | --- | --- | --- | --- |
| 20  | cli interface |        | 1/1/1       |     |     |     |     |
| 30  | cli shutdown  |        |             |     |     |     |     |
| 40  | delay         | 10 cli | no shutdown |     |     |     |     |
| 50  | cli end       |        |             |     |     |     |     |
Showingtheporttogglejobscheduleinformationafterfirstexecution:
| switch#  | show  | schedule | PT2xW |     |     |     |     |
| -------- | ----- | -------- | ----- | --- | --- | --- | --- |
| Schedule | Name: | PT2xW    |       |     |     |     |     |
| Schedule |       | config   |       |     |     |     |     |
---------------
| Description |         |        | : Monday     |     | & Friday | 11:45 | PM port toggles |
| ----------- | ------- | ------ | ------------ | --- | -------- | ----- | --------------- |
| Enabled     |         |        | : Yes        |     |          |       |                 |
| Trigger     | type    |        | : calendar   |     |          |       |                 |
| Transient   |         |        | : No         |     |          |       |                 |
| Max         | trigger | count  | : 104        |     |          |       |                 |
| Trigger     | start   | date   | : 2021-08-02 |     |          | 23:45 |                 |
| Schedule    |         | Status |              |     |          |       |                 |
---------------
| Trigger   | status  |       | : active |     |     |          |      |
| --------- | ------- | ----- | -------- | --- | --- | -------- | ---- |
| Next      | trigger | time  | : Fri    | Aug | 6   | 23:45:00 | 2021 |
| Triggered |         | count | : 1      |     |     |          |      |
| Scheduled |         | Jobs  |          |     |     |          |      |
--------------
| 10  | : PTog1 |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
Showingtheporttogglejobmostrecentexecutionoutput:
| switch# | show | job PTog1 | execution-output |     |     | 1   |     |
| ------- | ---- | --------- | ---------------- | --- | --- | --- | --- |
=================================================================================
| Command:  | config |            |      |     |     |     |     |
| --------- | ------ | ---------- | ---- | --- | --- | --- | --- |
| time: Mon | Aug    | 2 23:45:00 | 2021 |     |     |     |     |
=================================================================================
JobScheduler|9

=================================================================================
| Command: |     | interface      | 1/1/1 |     |     |     |     |
| -------- | --- | -------------- | ----- | --- | --- | --- | --- |
| time:    | Mon | Aug 2 23:45:00 | 2021  |     |     |     |     |
=================================================================================
=================================================================================
| Command: |     | shutdown       |      |     |     |     |     |
| -------- | --- | -------------- | ---- | --- | --- | --- | --- |
| time:    | Mon | Aug 2 23:45:00 | 2021 |     |     |     |     |
=================================================================================
=================================================================================
| Command: |     | cli no shutdown |      |     |     |     |     |
| -------- | --- | --------------- | ---- | --- | --- | --- | --- |
| time:    | Mon | Aug 2 23:45:10  | 2021 |     |     |     |     |
=================================================================================
=================================================================================
| Command: |     | end            |      |     |     |     |     |
| -------- | --- | -------------- | ---- | --- | --- | --- | --- |
| time:    | Mon | Aug 2 23:45:10 | 2021 |     |     |     |     |
=================================================================================
| Switch | reboot | example |     |     |     |     |     |
| ------ | ------ | ------- | --- | --- | --- | --- | --- |
Thisexamplecreatesaswitchrebootjobandthenschedulesthejobforexecutiononthelastdayof
everymonthat3:00AM.
CreatingajobnamedReboot_sw1thatsavestherunningconfigurationandthenrebootstheswitch:
| switch(config)# |     | job | Reboot_sw1 |     |     |     |     |
| --------------- | --- | --- | ---------- | --- | --- | --- | --- |
switch(config-job-Reboot_sw1)# desc Save config then reboot switch
| switch(config-job-Reboot_sw1)# |     |     |     | 10 cli | config |        |     |
| ------------------------------ | --- | --- | --- | ------ | ------ | ------ | --- |
| switch(config-job-Reboot_sw1)# |     |     |     | 20 cli | write  | mem    |     |
| switch(config-job-Reboot_sw1)# |     |     |     | 30 cli | boot   | system |     |
| switch(config-job-Reboot_sw1)# |     |     |     | exit   |        |        |     |
switch(config)#
CreatingaschedulenamedRB_LDMthatrunstheswitchrebootjobReboot_sw1onthelastdayofthe
monthat3:00AM,startingonJanuary312022,withatwo-yearduration:
| switch(config)#                 |     | schedule | RB_LDM |      |         |        |         |
| ------------------------------- | --- | -------- | ------ | ---- | ------- | ------ | ------- |
| switch(config-schedule-RB_LDM)# |     |          |        | desc | Monthly | reboot | 3:00 AM |
switch(config-schedule-RB_LDM)#
|     |     |     |     | 10 job | Reboot_sw1 |     |     |
| --- | --- | --- | --- | ------ | ---------- | --- | --- |
switch(config-schedule-RB_LDM)# trigger on 3:00 monthly 31 count 24 start 2022-01-
31
| switch(config-schedule-RB_LDM)# |     |     |     | exit |     |     |     |
| ------------------------------- | --- | --- | --- | ---- | --- | --- | --- |
switch(config)#
AftertheRB_LDMscheduletriggerstherebootjobReboot_sw1,theshow eventscommandisavailable
toshowscheduletriggering(<MODEL>representstheswitchmodelnumber):
| switch# |     | show events | -a -d schedulerd |     |     |     |     |
| ------- | --- | ----------- | ---------------- | --- | --- | --- | --- |
---------------------------------------------------
| Event | logs | from previous | boots |     |     |     |     |
| ----- | ---- | ------------- | ----- | --- | --- | --- | --- |
---------------------------------------------------
...
2022-01-31T03:00:14.405135+00:00 <MODEL> schedulerd[2054]: Event|12202|LOG_
| INFO|AMM|1/1|Schedule |     |     | RB_LDM | triggered, | trigger_count: |     | 1   |
| --------------------- | --- | --- | ------ | ---------- | -------------- | --- | --- |
10
| AOS-CX10.11JobSchedulerGuide| |     | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |

---------------------------------------------------
| Event | logs from current | boot |     |
| ----- | ----------------- | ---- | --- |
---------------------------------------------------
switch#
| Job Scheduler | commands |     |     |
| ------------- | -------- | --- | --- |
job
Intheconfigcontext:
job <JOB-NAME>
no job [<JOB-NAME>]
SubcommandsavailableInthejobconfigcontext(config-job):
[no] enable
| [no] desc        | <DESCRIPTION>   |                        |     |
| ---------------- | --------------- | ---------------------- | --- |
| [no] [<SEQ-NUM>] | [delay          | <DELAY>] cli <COMMAND> |     |
| resequence       | <START-SEQ-NUM> | <INCREMENT>            |     |
Description
If<JOB-NAME>doesnotexist,thiscommandcreatesajobandthenentersitscontext.
Thenoformofthiscommanddeletesthespecifiedjob.Ifnojobisspecified,alljobsaredeleted.
Deletingajobalsoremovesitfromanyschedulethatusesthejob,preventingfurtherattemptstoexecutethe
job.
If<JOB-NAME>exists,thiscommandenterstheconfig-job-<NAME>contextforthespecifiedjob.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<JOB-NAME> Specifiesthejobname.Range1to64characters(alphanumeric
and"_"(underscore)
Subcommands
Thesesubcommandsareavailablewithintheconfig-job-<NAME>contextforconfiguringthejob:
enable
| Enablesthejob(thedefault).no |               | enabledisablesthejob. |     |
| ---------------------------- | ------------- | --------------------- | --- |
| [no] desc                    | <DESCRIPTION> |                       |     |
Specifiesauser-definedjobdescription.no descremovesthedescription.Range:1to128
characters.Forexample:
| switch(config-job-PTog1)# |        | desc Toggle            | port 1/1/1 |
| ------------------------- | ------ | ---------------------- | ---------- |
| [no] [<SEQ-NUM>]          | [delay | <DELAY>] cli <COMMAND> |            |
AddsaCLIcommandtothejob.Thenoformremovesthecommandfromthejob.Whenexecuted,
commandswithsimple(y/n)prompts(suchasboot system)willbeautomaticallyconfirmedwith"y."
Othercommandsrequiringmorecomplexuserinput(suchaspasswordchange)cannotbeused.
<SEQ-NUM>specifiesthejobCLIcommandsequencenumbertofacilitateorderingofcommands
withinajob.Whenomitted,asequencenumberthatis10greaterthehighestexistingsequence
JobScheduler|11

numberisauto-assigned.Thefirstauto-assignedsequencenumberis10.Range:1to
4294967295.
<DELAY>]specifiesthedelayinsecondsbeforethisCLIcommandisexecuted.The
[delay
cumulativedelayforallcommandsinajobmustbenomorethan300seconds.Range1to300.
cli <COMMAND>specifiestheCLIcommandtobeexecuted.Range1to4096characters.
Thesecommandsmustnotbeusedinajob:copy,repeat,show boot-history,show core-dump,
| show | events,show job,show | tech,sleep,terminal-monitor. |     |     |
| ---- | -------------------- | ---------------------------- | --- | --- |
Forexample,addingacommandasline18toajob:
| switch(config-job-PTog1)# |                 | 18          | cli interface | 1/1/1 |
| ------------------------- | --------------- | ----------- | ------------- | ----- |
| resequence                | <START-SEQ-NUM> | <INCREMENT> |               |       |
ResequencestheCLIcommandlinesequencenumbers.Both<START-SEQ-NUM>and<INCREMENT>
defaultto10.Forexample,resequencingtheCLIcommandlisttostartat10withanincrementof5.
| switch(config-job-PTog1)# |     | resequence |     | 10 5 |
| ------------------------- | --- | ---------- | --- | ---- |
switch(config-job-PTog1)#
|     |              | show | job | PTog1 |
| --- | ------------ | ---- | --- | ----- |
| Job | Name : PTog1 |      |     |       |
...
Job CLI commands
----------------
10 cli config
|     | 15 cli interface | 1/1/1 |     |     |
| --- | ---------------- | ----- | --- | --- |
20 cli shutdown
...
Usage
Amaximumof20commandscanbeusedinajob.
n
n Toseethemaximumnumberofjobsandjobexecutionoutputpreservedinstancesforyour
| particularswitch,usecommandshow |     |     | capacities | job. |
| ------------------------------- | --- | --- | ---------- | ---- |
Jobsmustcompleteexecutioninunderfiveminutesandareforce-stoppedafterfiveminutesifthey
n
donot.
Examples
CreatingaporttogglejobnamedPTog1:
| switch(config)#           | job | PTog1 |               |                    |
| ------------------------- | --- | ----- | ------------- | ------------------ |
| switch(config-job-PTog1)# |     | desc  | Toggle        | port 1/1/1         |
| switch(config-job-PTog1)# |     | 10    | cli config    |                    |
| switch(config-job-PTog1)# |     | 20    | cli interface | 1/1/1              |
| switch(config-job-PTog1)# |     | 30    | cli shutdown  |                    |
| switch(config-job-PTog1)# |     | 40    | delay         | 10 cli no shutdown |
| switch(config-job-PTog1)# |     | 50    | cli end       |                    |
| switch(config-job-PTog1)# |     | exit  |               |                    |
switch(config)#
CreatingajobnamedReboot_sw1thatsavestherunningconfigurationandthenrebootstheswitch:
12
| AOS-CX10.11JobSchedulerGuide| | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ---------------------------------------- | --- | --- | --- |

|     | switch(config)# |     | job | Reboot_Sw1 |     |     |     |
| --- | --------------- | --- | --- | ---------- | --- | --- | --- |
switch(config-job-Reboot_sw1)#
|     |                                |     |     |     | desc Save | config      | then reboot switch |
| --- | ------------------------------ | --- | --- | --- | --------- | ----------- | ------------------ |
|     | switch(config-job-Reboot_Sw1)# |     |     |     | 10 cli    | config      |                    |
|     | switch(config-job-Reboot_Sw1)# |     |     |     | 20 cli    | write mem   |                    |
|     | switch(config-job-Reboot_Sw1)# |     |     |     | 30 cli    | boot system |                    |
|     | switch(config-job-Reboot_Sw1)# |     |     |     | exit      |             |                    |
switch(config)#
Formoreinformationonfeaturesthatusethiscommand,refertotheJobSchedulerGuideforyourswitch
model.
| Command |           | History     |     |         |                    |     |     |
| ------- | --------- | ----------- | --- | ------- | ------------------ | --- | --- |
|         | Release   |             |     |         | Modification       |     |     |
|         | 10.08     |             |     |         | Commandintroduced. |     |     |
| Command |           | Information |     |         |                    |     |     |
|         | Platforms | Command     |     | context | Authority          |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     |     | config-job-<NAME> |     |     | forthiscommand. |     |     |
| --- | --- | ----------------- | --- | --- | --------------- | --- | --- |
schedule
Intheconfigcontext:
| schedule |          | <SCHEDULE-NAME>   |     | [transient] |     |     |     |
| -------- | -------- | ----------------- | --- | ----------- | --- | --- | --- |
| no       | schedule | [<SCHEDULE-NAME>] |     |             |     |     |     |
SubcommandsavailableInthescheduleconfigcontext(config-schedule):
[no] enable
| [no]       | desc        | <DESCRIPTION>   |            |             |              |           |         |
| ---------- | ----------- | --------------- | ---------- | ----------- | ------------ | --------- | ------- |
| [no]       | [<SEQ-NUM>] | job             | <JOB-NAME> |             |              |           |         |
| resequence |             | <START-SEQ-NUM> |            | <INCREMENT> |              |           |         |
| [no]       | trigger     | on HH:MM        | {daily     | |           | weekly <1-7> | | monthly | <1-31>} |
|            | [count      | <1-1000>]       | [start     | YYYY-MM-DD] |              |           |         |
[no] trigger every {days <1-365> | hours <1-8760> | minutes <30-525600>}
|      | [count  | <1-1000> | ] [start     | HH:MM | [YYYY-MM-DD]] |     |     |
| ---- | ------- | -------- | ------------ | ----- | ------------- | --- | --- |
| [no] | trigger | at HH:MM | [YYYY-MM-DD] |       |               |     |     |
Description
If<SCHEDULE-NAME>doesnotexist,thiscommandcreatesajobscheduleandthenentersitscontext.
Thenoformofthiscommanddeletesthespecifiedschedule.Ifnoscheduleisspecified,allschedules
aredeleted.
If<SCHEDULE-NAME>exists,thiscommandenterstheconfig-schedule-<NAME>contextforthespecified
jobschedule.
JobScheduler|13

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<SCHEDULE-NAME> Specifiestheschedulename.Range1to64characters
(alphanumericand"_"(underscore)).
[transient] Causesthescheduletobecleareduponswitchreboot.Bydefault,
schedulesaremaintainedafterswitchreboots.
Subcommands
Thesesubcommandsareavailablewithintheconfig-schedule-<NAME>contextforschedulingjobsand
controllingtheorderinwhichthejobsareexecuted:
enable
| Enablestheschedule(thedefault).no |               |     | enabledisablestheschedule. |     |     |
| --------------------------------- | ------------- | --- | -------------------------- | --- | --- |
| [no] desc                         | <DESCRIPTION> |     |                            |     |     |
Specifiesauser-definedscheduledescription.no descremovesthedescription.Range:1to128
characters.Forexample:
| switch(config-schedule-Monthly)# |                |     | desc | Monthly schedule |     |
| -------------------------------- | -------------- | --- | ---- | ---------------- | --- |
| [no] [<SEQ-NUM>]                 | job <JOB-NAME> |     |      |                  |     |
Associatesanexistingjobwiththisschedule.Thenoformremovesthejobfromtheschedule.
<JOB-NAME>specifiesanexistingjobname.Range:1to64characters(alphanumericand"_"
(underscore)).
<SEQ-NUM>specifiesthejobnamesequencenumbertofacilitateorderingofjobswithina
schedule.Whenomitted,asequencenumberthatis10greaterthehighestexistingsequence
numberisauto-assigned.Thefirstauto-assignedsequencenumberis10.
Forexample,associatingtwojobswiththeselectedschedule:
| switch(config-schedule-Monthly)# |                 |             | 10 job | PTog1 |     |
| -------------------------------- | --------------- | ----------- | ------ | ----- | --- |
| switch(config-schedule-Monthly)# |                 |             | 20 job | PTog2 |     |
| resequence                       | <START-SEQ-NUM> | <INCREMENT> |        |       |     |
Resequencesthejobnamesequencenumbersintheschedule.Both<START-SEQ-NUM>and
<INCREMENT>defaultto10.Forexample,resequencingthejoblisttostartat5withanincrementof
10.
| switch(config-schedule-Monthly)# |               |     | resequence | 5 10     |         |
| -------------------------------- | ------------- | --- | ---------- | -------- | ------- |
| switch(config-schedule-Monthly)# |               |     | show       | schedule | Monthly |
| Schedule                         | Name: Monthly |     |            |          |         |
...
Scheduled Jobs
--------------
5 : PTog1
15 : PTog2
| [no] trigger | on HH:MM {daily  | | weekly    | <1-7> | | monthly | <1-31>} |
| ------------ | ---------------- | ----------- | ----- | --------- | ------- |
| [count       | <1-1000>] [start | YYYY-MM-DD] |       |           |         |
Setsthejobtotriggerataspecifictime.Thenoformremovesthetrigger.
HH:MMselectsthetimeusinga24-hourclock(switchlocaltime).Range:00:00to23:59.
dailyselectsdaily.
14
| AOS-CX10.11JobSchedulerGuide| | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ---------------------------------------- | --- | --- | --- | --- |

weekly <1-7> selects specific days of week or days-of-week ranges (with comma or hyphen
separators) using numeric day-of-week numbers with Sunday equal 1. For example: 1,3,5-7 for
Sunday, Tuesday, Thursday, Friday, Saturday.

monthly <1-31> selects specific days of month or days of month ranges (with comma or hyphen
separators) using numeric day-of-month numbers. For example: 5,14-21,25,31. For months with
fewer days than the specified day number, the last day of the month is selected.

count <1-1000> selects the number of times the job will be executed. When omitted, job
execution triggering is indefinite.

start YYYY-MM-DD selects the schedule first trigger date. When omitted, today's date is used for
times at least 5 minutes into the future, otherwise tomorrow is selected as the first trigger date.

For example, setting the schedule to trigger monthly on the 15th, at 11:45 PM, starting on August 15,
with an execution limit of 200:

switch(config-schedule-M)# trigger on 23:45 monthly 15 count 200 start 2021-08-15

[no] trigger every {days <1-365> | hours <1-8760> | minutes <30-525600>}

[count <1-1000>] [start HH:MM [YYYY-MM-DD]]

Sets the job trigger to a specific periodic interval. The no form removes the trigger. By default, the
schedule is activated within 5 minutes from the configuration time. If the start time is specified, then
the job is executed beginning at the specified start time and thereafter at the specified interval.

days <1-365> selects the interval in days. Range: 1 to 365.

hours <1-8760> selects the interval in minutes. Range: 1 to 8760.

minutes <30-525600> selects the interval in seconds. Range: 30 to 525600.

count <1-1000> selects the number of times the job will be executed. When omitted, job
execution triggering is indefinite.

start HH:MM [YYYY-MM-DD] selects the schedule first trigger time and date.

For example, setting the schedule to trigger once every 14 days, starting on January 1, with an
execution limit of 500:

switch(config-schedule-Ev14D)# trigger every days 14 count 500 start 2022-01-01

[no] trigger at HH:MM [YYYY-MM-DD]

Sets the job to trigger one time only on a specific date and time. When the date is omitted, today's
date is used for times at least 5 minutes into the future, otherwise tomorrow is selected. The no form
removes the trigger.

For example, setting the schedule to trigger once only on August 26 at midnight:

switch(config-schedule-Aug26)# trigger at 00:00 2021-08-26

Usage

n A job can be used only once per schedule.

n To see the maximum number of schedules and jobs per schedule for your particular switch, use

command show capacities schedule.

n Configure the jobs to be executed (using the job command) before configuring a schedule.

n Jobs must complete execution in under five minutes and are force-stopped after five minutes if they

do not.

Job Scheduler | 15

n Ajobmustbescheduledtoexecuteatleastfiveminutesafteritspreviousexecution.Ifthesamejob
isscheduledtobeexecutedagainwithinlessthanfiveminutes,theexecutionisskipped.
Examples
CreatingaschedulenamedPT2xWthatrunstheporttogglejobPTog1onMondaysandFridaysat11:45
PM,startingonAugust22021,withaone-yearduration:
| switch(config)# | schedule | PT2xW |     |     |     |
| --------------- | -------- | ----- | --- | --- | --- |
switch(config-schedule-PT2xW)# desc Monday & Friday 11:45 PM port toggles
| switch(config-schedule-PT2xW)# |     |     | 10 job PTog1 |     |     |
| ------------------------------ | --- | --- | ------------ | --- | --- |
switch(config-schedule-PT2xW)# trigger on 23:45 weekly 2,6 count 104 start 2021-
08-02
| switch(config-schedule-PT2xW)# |     |     | exit |     |     |
| ------------------------------ | --- | --- | ---- | --- | --- |
switch(config)#
CreatingaschedulenamedRB_LDMthatrunstheswitchrebootjobonthelastdayofthemonthat3:00
AM,startingonJanuary312022,withatwo-yearduration:
| switch(config)#                 | schedule | RB_LDM |                   |             |     |
| ------------------------------- | -------- | ------ | ----------------- | ----------- | --- |
| switch(config-schedule-RB_LDM)# |          |        | desc Monthly      | reboot 3:00 | AM  |
| switch(config-schedule-RB_LDM)# |          |        | 10 job Reboot_sw1 |             |     |
switch(config-schedule-RB_LDM)# trigger on 3:00 monthly 31 count 24 start 2022-01-
31
| switch(config-schedule-RB_LDM)# |     |     | exit |     |     |
| ------------------------------- | --- | --- | ---- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheJobSchedulerGuideforyourswitch
model.
| Command History     |         |         |                    |     |     |
| ------------------- | ------- | ------- | ------------------ | --- | --- |
| Release             |         |         | Modification       |     |     |
| 10.08               |         |         | Commandintroduced. |     |     |
| Command Information |         |         |                    |     |     |
| Platforms           | Command | context | Authority          |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|                 | config-schedule-<NAME> |           | rightsforthiscommand. |     |     |
| --------------- | ---------------------- | --------- | --------------------- | --- | --- |
| show capacities | (job,                  | schedule) |                       |     |     |
| show capacities | {job |                 | schedule} |                       |     |     |
Description
Showseitherjoborschedulecapacitiesinformationforyourswitchmodel.
Examples
Showingjobcapacitiesinformation(8320exampleshown):
16
| AOS-CX10.11JobSchedulerGuide| | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ---------------------------------------- | --- | --- | --- | --- |

| switch#            | show capacities |        | job |     |     |     |       |
| ------------------ | --------------- | ------ | --- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter | Job |     |     |     |       |
| Capacities         | Name            |        |     |     |     |     | Value |
----------------------------------------------------------------------------------
| Maximum | number | of job  | execution    | output | preserved | per job | 10  |
| ------- | ------ | ------- | ------------ | ------ | --------- | ------- | --- |
| Maximum | number | of jobs | configurable | in     | a system  |         | 32  |
Showingschedulecapacitiesinformation(8320exampleshown):
| switch#            | show capacities |        | Schedule |     |     |     |       |
| ------------------ | --------------- | ------ | -------- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter | Schedule |     |     |     |       |
| Capacities         | Name            |        |          |     |     |     | Value |
----------------------------------------------------------------------------------
| Maximum | number | of jobs      | configurable | in  | a schedule |        | 10  |
| ------- | ------ | ------------ | ------------ | --- | ---------- | ------ | --- |
| Maximum | number | of schedules | configurable |     | in a       | system | 32  |
Formoreinformationonfeaturesthatusethiscommand,refertotheJobSchedulerGuideforyourswitch
model.
| Command   | History     |     |         |                    |     |     |     |
| --------- | ----------- | --- | ------- | ------------------ | --- | --- | --- |
| Release   |             |     |         | Modification       |     |     |     |
| 10.08     |             |     |         | Commandintroduced. |     |     |     |
| Command   | Information |     |         |                    |     |     |     |
| Platforms | Command     |     | context | Authority          |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show job              |     |                   |     |                |     |     |     |
| --------------------- | --- | ----------------- | --- | -------------- | --- | --- | --- |
| show job [<JOB-NAME>] |     | [execution-output |     | <INSTANCE-ID>] |     |     |     |
Description
Showsinformationaboutaspecificjoboreveryjob.Optionallyshowsthejobexecutionoutputlog.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<JOB-NAME>
Specifiesanexistingjobname.Whenomitted,informationis
shownforeveryjob.Range:1to64characters(alphanumericand
"_"(underscore)).
<INSTANCE-ID> Selectsthejobexecutionoutputinstancewith1selectingthe
mostrecent.Toseethemaximumnumberofjobexecution
outputinstancesforyourparticularswitch,usecommandshow
|     |     |     |     | capacities | job. |     |     |
| --- | --- | --- | --- | ---------- | ---- | --- | --- |
JobScheduler|17

Usage
Jobexecutionstatisticssuchasexecutioncountsareresettozerouponswitchreboot.
Examples
Showingporttogglejobinformationbeforeexecutionhasoccurred:
| switch# show | job PTog1 |     |     |     |
| ------------ | --------- | --- | --- | --- |
Job Name : PTog1
| Enabled         |                 | : Yes     |            |     |
| --------------- | --------------- | --------- | ---------- | --- |
| Description     |                 | : Toggle  | port 1/1/1 |     |
| Status          |                 | : waiting |            |     |
| Number          | of commands     | : 5       |            |     |
| Total execution | count           | : 0       |            |     |
| Failed          | execution count | : 0       |            |     |
| Job CLI         | commands        |           |            |     |
----------------
10 cli config
| 20 cli | interface 1/1/1 |     |     |     |
| ------ | --------------- | --- | --- | --- |
30 cli shutdown
| 40 delay | 10 cli no shutdown |     |     |     |
| -------- | ------------------ | --- | --- | --- |
50 cli end
Showingporttogglejobinformationafterexecutionhasoccurred:
| switch# show | job PTog1 |     |     |     |
| ------------ | --------- | --- | --- | --- |
Job Name : PTog1
| Enabled         |                 | : Yes     |            |     |
| --------------- | --------------- | --------- | ---------- | --- |
| Description     |                 | : Toggle  | port 1/1/1 |     |
| Status          |                 | : waiting |            |     |
| Number          | of commands     | : 5       |            |     |
| Total execution | count           | : 1       |            |     |
| Failed          | execution count | : 0       |            |     |
| Job execution   | history         |           |            |     |
---------------------
| Instance  | number     | : 1       |            |      |
| --------- | ---------- | --------- | ---------- | ---- |
| Execution | status     | : success |            |      |
| Execution | start time | : Mon Aug | 2 23:45:00 | 2021 |
| Execution | duration   | : 10s     |            |      |
| Job CLI   | commands   |           |            |      |
----------------
10 cli config
| 20 cli | interface 1/1/1 |     |     |     |
| ------ | --------------- | --- | --- | --- |
30 cli shutdown
| 40 delay | 10 cli no shutdown |     |     |     |
| -------- | ------------------ | --- | --- | --- |
50 cli end
Showingporttogglejobmostrecentexecutionoutput:
18
AOS-CX10.11JobSchedulerGuide| (4100i,6xxx,8xxx,9300,10000SwitchSeries)

| switch# | show job PTog1 | execution-output | 1   |
| ------- | -------------- | ---------------- | --- |
=================================================================================
| Command:  | config         |      |     |
| --------- | -------------- | ---- | --- |
| time: Mon | Aug 2 23:45:00 | 2021 |     |
=================================================================================
=================================================================================
| Command:  | interface      | 1/1/1 |     |
| --------- | -------------- | ----- | --- |
| time: Mon | Aug 2 23:45:00 | 2021  |     |
=================================================================================
=================================================================================
| Command:  | shutdown       |      |     |
| --------- | -------------- | ---- | --- |
| time: Mon | Aug 2 23:45:00 | 2021 |     |
=================================================================================
=================================================================================
| Command:  | cli no shutdown |      |     |
| --------- | --------------- | ---- | --- |
| time: Mon | Aug 2 23:45:10  | 2021 |     |
=================================================================================
=================================================================================
| Command:  | end            |      |     |
| --------- | -------------- | ---- | --- |
| time: Mon | Aug 2 23:45:10 | 2021 |     |
=================================================================================
Formoreinformationonfeaturesthatusethiscommand,refertotheJobSchedulerGuideforyourswitch
model.
| Command   | History     |         |                    |
| --------- | ----------- | ------- | ------------------ |
| Release   |             |         | Modification       |
| 10.08     |             |         | Commandintroduced. |
| Command   | Information |         |                    |
| Platforms | Command     | context | Authority          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show running-config |                   | (job, | schedule) |
| ------------------- | ----------------- | ----- | --------- |
| show running-config | [current-context] |       |           |
Description
Showstheentirerunningconfigurationfortheswitch,includingconfigurationdetailsfortheJob
Schedulerjobandscheduleconfiguration.
JobScheduler|19

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
current-context WhenincludedfromwithintheJobSchedulerjoborschedule
context,showsonlythejoborscheduleconfigurationinformation
fortheselectedjoborschedule.
Examples
Showingtherunningconfigurationinformationforalljobsandscheduleswithunrelatedconfiguration
informationomittedforclarity(omittedportionsrepresentedbyellipses("..."):
| switch# show           | running-config |     |     |     |
| ---------------------- | -------------- | --- | --- | --- |
| Current configuration: |                |     |     |     |
...
!
job PTog1
| desc Toggle | port 1/1/1      |          |     |     |
| ----------- | --------------- | -------- | --- | --- |
| 10 cli      | config          |          |     |     |
| 20 cli      | interface 1/1/1 |          |     |     |
| 30 cli      | shutdown        |          |     |     |
| 40 delay    | 10 cli no       | shutdown |     |     |
| 50 cli      | end             |          |     |     |
job Reboot_sw1
| desc Save       | config then     | reboot switch |           |            |
| --------------- | --------------- | ------------- | --------- | ---------- |
| 10 cli          | config          |               |           |            |
| 20 cli          | write mem       |               |           |            |
| 30 cli          | boot system     |               |           |            |
| schedule PT2xW  |                 |               |           |            |
| desc Monday     | & Friday        | 11:45 PM port | toggles   |            |
| trigger         | on 23:45 weekly | 2,6 count     | 104 start | 2021-08-02 |
| 10 job          | PTog1           |               |           |            |
| schedule RB_LDM |                 |               |           |            |
| desc Monthly    | reboot          | 3:00 AM       |           |            |
| trigger         | on 3:00 monthly | 31 count      | 24 start  | 2022-01-31 |
| 10 job          | Reboot_sw1      |               |           |            |
...
FromwithinthejobPTog1context,showingtherunningconfigurationinformationforthejob:
| switch(config-job-PTog1)# |     | show running-config |     | current-context |
| ------------------------- | --- | ------------------- | --- | --------------- |
| Current configuration:    |     |                     |     |                 |
job PTog1
| desc Toggle | port 1/1/1      |          |     |     |
| ----------- | --------------- | -------- | --- | --- |
| 10 cli      | config          |          |     |     |
| 20 cli      | interface 1/1/1 |          |     |     |
| 30 cli      | shutdown        |          |     |     |
| 40 delay    | 10 cli no       | shutdown |     |     |
| 50 cli      | end             |          |     |     |
FromwithintheschedulePT2xWcontext,showingtherunningconfigurationinformationforthe
schedule:
switch(config-schedule-PT2xW)# show running-config current-context
| Current configuration: |     |     |     |     |
| ---------------------- | --- | --- | --- | --- |
20
AOS-CX10.11JobSchedulerGuide| (4100i,6xxx,8xxx,9300,10000SwitchSeries)

| schedule |         | PT2xW    |        |          |                 |            |
| -------- | ------- | -------- | ------ | -------- | --------------- | ---------- |
|          | desc    | Monday & | Friday | 11:45 PM | port toggles    |            |
|          | trigger | on 23:45 | weekly | 2,6      | count 104 start | 2021-08-02 |
|          | 10 job  | PTog1    |        |          |                 |            |
Formoreinformationonfeaturesthatusethiscommand,refertotheJobSchedulerGuideforyourswitch
model.
| Command   | History     |         |         |     |                    |     |
| --------- | ----------- | ------- | ------- | --- | ------------------ | --- |
| Release   |             |         |         |     | Modification       |     |
| 10.08     |             |         |         |     | Commandintroduced. |     |
| Command   | Information |         |         |     |                    |     |
| Platforms |             | Command | context |     | Authority          |     |
Allplatforms Operator(>)orManager(#) OperatorsorAdministratorsorlocalusergroupmembers
config-job-<NAME> withexecutionrightsforthiscommand.Operatorscan
config-schedule-<NAME> executethiscommandfromtheoperatorcontext(>)only.
show schedule
| show | schedule | [<SCHEDULE-NAME>] |     |     |     |     |
| ---- | -------- | ----------------- | --- | --- | --- | --- |
Description
Showsinformationaboutaspecificscheduleoreveryschedule.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<SCHEDULE-NAME> Specifiesanexistingjobschedulename.Whenomitted,
informationisshownforeveryschedule.Range:1to64
characters(alphanumericand"_"(underscore)).
Usage
SchedulestatisticssuchasTriggered countareresettozerouponswitchreboot.
Examples
Showingporttogglejobscheduleinformationbeforeexecutionhasoccurred:
| switch#  |          | show schedule | PT2xW |     |     |     |
| -------- | -------- | ------------- | ----- | --- | --- | --- |
| Schedule |          | Name: PT2xW   |       |     |     |     |
|          | Schedule | config        |       |     |     |     |
---------------
|     | Description |      | :   | Monday   | & Friday 11:45 | PM port toggles |
| --- | ----------- | ---- | --- | -------- | -------------- | --------------- |
|     | Enabled     |      | :   | Yes      |                |                 |
|     | Trigger     | type | :   | calendar |                |                 |
JobScheduler|21

|     | Transient |         |       | : No         |     |       |     |
| --- | --------- | ------- | ----- | ------------ | --- | ----- | --- |
|     | Max       | trigger | count | : 104        |     |       |     |
|     | Trigger   | start   | date  | : 2021-08-02 |     | 23:45 |     |
|     | Schedule  | Status  |       |              |     |       |     |
---------------
|     | Trigger   | status  |      | : active |     |            |      |
| --- | --------- | ------- | ---- | -------- | --- | ---------- | ---- |
|     | Next      | trigger | time | : Mon    | Aug | 2 23:45:00 | 2021 |
|     | Scheduled |         | Jobs |          |     |            |      |
--------------
|     | 10  | : PTog1 |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- |
Showingporttogglejobscheduleinformationafterexecutionhasoccurred:
| switch#  |          | show schedule |       | PT2xW |     |     |     |
| -------- | -------- | ------------- | ----- | ----- | --- | --- | --- |
| Schedule |          | Name:         | PT2xW |       |     |     |     |
|          | Schedule | config        |       |       |     |     |     |
---------------
|     | Description |         |       | : Monday     |     | & Friday 11:45 | PM port toggles |
| --- | ----------- | ------- | ----- | ------------ | --- | -------------- | --------------- |
|     | Enabled     |         |       | : Yes        |     |                |                 |
|     | Trigger     | type    |       | : calendar   |     |                |                 |
|     | Transient   |         |       | : No         |     |                |                 |
|     | Max         | trigger | count | : 104        |     |                |                 |
|     | Trigger     | start   | date  | : 2021-08-02 |     | 23:45          |                 |
|     | Schedule    | Status  |       |              |     |                |                 |
---------------
|     | Trigger   | status  |       | : active |     |            |      |
| --- | --------- | ------- | ----- | -------- | --- | ---------- | ---- |
|     | Next      | trigger | time  | : Fri    | Aug | 6 23:45:00 | 2021 |
|     | Triggered |         | count | : 1      |     |            |      |
|     | Scheduled |         | Jobs  |          |     |            |      |
--------------
|     | 10  | : PTog1 |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheJobSchedulerGuideforyourswitch
model.
| Command   | History     |         |     |         |     |                    |     |
| --------- | ----------- | ------- | --- | ------- | --- | ------------------ | --- |
| Release   |             |         |     |         |     | Modification       |     |
| 10.08     |             |         |     |         |     | Commandintroduced. |     |
| Command   | Information |         |     |         |     |                    |     |
| Platforms |             | Command |     | context |     | Authority          |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
22
| AOS-CX10.11JobSchedulerGuide| |     |     | (4100i,6xxx,8xxx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |

Support and Other Resources

Chapter 3

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

AOS-CX 10.11 Job Scheduler Guide | (4100i, 6xxx, 8xxx, 9300, 10000 Switch Series)

23

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
SupportandOtherResources|24

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

AOS-CX 10.11 Job Scheduler Guide | (4100i, 6xxx, 8xxx, 9300, 10000 Switch Series)

25