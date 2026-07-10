| AOS-CX |     | 10.09 | Job | Scheduler |     |     |
| ------ | --- | ----- | --- | --------- | --- | --- |
Guide
| 4100i, | 6000, | 6100, | 6200, | 6300,  | 6400,  | 8320, |
| ------ | ----- | ----- | ----- | ------ | ------ | ----- |
|        | 8325, | 8360, | 8400  | Switch | Series |       |
Published:September2022
Edition:3

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

3
3

4
4
4
6

Contents

Identifying modular switch components

Job Scheduler

Working with Job Scheduler
Port toggle example
Switch reboot example

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

AOS-CX 10.09 Job Scheduler Guide | (4100i, 6xxx, 8xxx Switch Series)

3

Chapter 3
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
TohelpunderstandhowtoworkwiththeJobScheduler,severalbasicexamplesarepresented,followedby
detaileddescriptionsofthecommandsinvolvedunderJobschedulercommands.
| Port toggle | example |     |     |
| ----------- | ------- | --- | --- |
ThisexamplecreatesaporttogglejobandthenschedulesthejobforexecutiononMondayandFridaynight
at11:45PM.
CreatingaporttogglejobnamedPTog1:
| switch(config)#           | job PTog1 |                  |                    |
| ------------------------- | --------- | ---------------- | ------------------ |
| switch(config-job-PTog1)# |           | desc Toggle      | port 1/1/1         |
| switch(config-job-PTog1)# |           | 10 cli config    |                    |
| switch(config-job-PTog1)# |           | 20 cli interface | 1/1/1              |
| switch(config-job-PTog1)# |           | 30 cli shutdown  |                    |
| switch(config-job-PTog1)# |           | 40 delay         | 10 cli no shutdown |
| switch(config-job-PTog1)# |           | 50 cli end       |                    |
| switch(config-job-PTog1)# |           | exit             |                    |
CreatingaschedulenamedPT2xWthatrunstheporttogglejobPTog1onMondaysandFridaysat11:45
PM,startingonAugust22021,withaone-yearduration:
| switch(config)# | schedule | PT2xW |     |
| --------------- | -------- | ----- | --- |
switch(config-schedule-PT2xW)# desc Monday & Friday 11:45 PM port toggles
| switch(config-schedule-PT2xW)# |     | 10 job | PTog1 |
| ------------------------------ | --- | ------ | ----- |
switch(config-schedule-PT2xW)# trigger on 23:45 weekly 2,6 count 104 start 2021-08-02
| switch(config-schedule-PT2xW)# |     | exit |     |
| ------------------------------ | --- | ---- | --- |
Showingtheporttogglejobinformationafterfirstexecution:
| switch# | show job PTog1 |     |     |
| ------- | -------------- | --- | --- |
4
| AOS-CX10.09JobSchedulerGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Job Name    | : PTog1   |          |       |           |      |       |     |
| ----------- | --------- | -------- | ----- | --------- | ---- | ----- | --- |
| Enabled     |           |          |       | : Yes     |      |       |     |
| Description |           |          |       | : Toggle  | port | 1/1/1 |     |
| Status      |           |          |       | : waiting |      |       |     |
| Number      | of        | commands |       | : 5       |      |       |     |
| Total       | execution |          | count | : 1       |      |       |     |
| Failed      | execution |          | count | : 0       |      |       |     |
| Job         | execution | history  |       |           |      |       |     |
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
=================================================================================
JobScheduler|5

| Command: |     | interface |            | 1/1/1 |     |     |     |     |
| -------- | --- | --------- | ---------- | ----- | --- | --- | --- | --- |
| time:    | Mon | Aug       | 2 23:45:00 | 2021  |     |     |     |     |
=================================================================================
=================================================================================
| Command: |     | shutdown |            |      |     |     |     |     |
| -------- | --- | -------- | ---------- | ---- | --- | --- | --- | --- |
| time:    | Mon | Aug      | 2 23:45:00 | 2021 |     |     |     |     |
=================================================================================
=================================================================================
| Command: |     | cli | no shutdown |      |     |     |     |     |
| -------- | --- | --- | ----------- | ---- | --- | --- | --- | --- |
| time:    | Mon | Aug | 2 23:45:10  | 2021 |     |     |     |     |
=================================================================================
=================================================================================
| Command: |     | end |            |      |     |     |     |     |
| -------- | --- | --- | ---------- | ---- | --- | --- | --- | --- |
| time:    | Mon | Aug | 2 23:45:10 | 2021 |     |     |     |     |
=================================================================================
| Switch | reboot |     | example |     |     |     |     |     |
| ------ | ------ | --- | ------- | --- | --- | --- | --- | --- |
Thisexamplecreatesaswitchrebootjobandthenschedulesthejobforexecutiononthelastdayofevery
monthat3:00AM.
CreatingajobnamedReboot_sw1thatsavestherunningconfigurationandthenrebootstheswitch:
switch(config)#
|     |     |     | job | Reboot_sw1 |     |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
switch(config-job-Reboot_sw1)# desc Save config then reboot switch
| switch(config-job-Reboot_sw1)# |     |     |     |     | 10 cli | config |        |     |
| ------------------------------ | --- | --- | --- | --- | ------ | ------ | ------ | --- |
| switch(config-job-Reboot_sw1)# |     |     |     |     | 20 cli | write  | mem    |     |
| switch(config-job-Reboot_sw1)# |     |     |     |     | 30 cli | boot   | system |     |
| switch(config-job-Reboot_sw1)# |     |     |     |     | exit   |        |        |     |
switch(config)#
CreatingaschedulenamedRB_LDMthatrunstheswitchrebootjobReboot_sw1onthelastdayofthe
monthat3:00AM,startingonJanuary312022,withatwo-yearduration:
| switch(config)#                 |     |     | schedule | RB_LDM |        |            |        |         |
| ------------------------------- | --- | --- | -------- | ------ | ------ | ---------- | ------ | ------- |
| switch(config-schedule-RB_LDM)# |     |     |          |        | desc   | Monthly    | reboot | 3:00 AM |
| switch(config-schedule-RB_LDM)# |     |     |          |        | 10 job | Reboot_sw1 |        |         |
switch(config-schedule-RB_LDM)# trigger on 3:00 monthly 31 count 24 start 2022-01-31
switch(config-schedule-RB_LDM)#
exit
switch(config)#
AftertheRB_LDMscheduletriggerstherebootjobReboot_sw1,theshow eventscommandisavailableto
showscheduletriggering(<MODEL>representstheswitchmodelnumber):
| switch# |     | show | events | -a -d schedulerd |     |     |     |     |
| ------- | --- | ---- | ------ | ---------------- | --- | --- | --- | --- |
---------------------------------------------------
| Event | logs | from | previous | boots |     |     |     |     |
| ----- | ---- | ---- | -------- | ----- | --- | --- | --- | --- |
---------------------------------------------------
...
2022-01-31T03:00:14.405135+00:00 <MODEL> schedulerd[2054]: Event|12202|LOG_
| INFO|AMM|1/1|Schedule |     |     |     | RB_LDM | triggered, | trigger_count: |     | 1   |
| --------------------- | --- | --- | --- | ------ | ---------- | -------------- | --- | --- |
---------------------------------------------------
| Event | logs | from | current | boot |     |     |     |     |
| ----- | ---- | ---- | ------- | ---- | --- | --- | --- | --- |
6
| AOS-CX10.09JobSchedulerGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

---------------------------------------------------
switch#

Job Scheduler | 7