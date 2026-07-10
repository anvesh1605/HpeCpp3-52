AOS-CX Job Scheduler Guide (All Switch Series)

Published: February 2026

AOS-CX Job Scheduler Guide (All Switch Series)

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

AOS-CX Job Scheduler Guide (All Switch Series)

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX Job Scheduler Guide (All Switch Series)

Table of contents

About this document..................................................................................................................................................................................5

Applicable products........................................................................................................................................................................5

Latest version available online.................................................................................................................................................6

Command syntax notation conventions.............................................................................................................................6

About the examples....................................................................................................................................................................... 7

Identifying switch ports and interfaces...............................................................................................................................8

Identifying modular switch components.........................................................................................................................10

Job Scheduler...............................................................................................................................................................................................11

Working with Job Scheduler...................................................................................................................................................11

Job Scheduler commands........................................................................................................................................................ 14

job ............................................................................................................................................................................................ 15

reload .....................................................................................................................................................................................18

schedule ............................................................................................................................................................................... 22

show job ............................................................................................................................................................................... 26

show capacities (job, schedule) ..............................................................................................................................29

show reload ........................................................................................................................................................................ 30

show running-config (job, schedule) ...................................................................................................................32

show schedule .................................................................................................................................................................. 34

Support and Other Resources............................................................................................................................................................36

Accessing HPE Aruba Networking Support..................................................................................................................36

Accessing Updates.......................................................................................................................................................................38

Warranty Information................................................................................................................................................................. 38

Regulatory Information............................................................................................................................................................. 38

Documentation Feedback........................................................................................................................................................39

Public

Table of contents 4

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Applicable products
Latest version available online
Command syntax notation conventions
About the examples
Identifying switch ports and interfaces
Identifying modular switch components

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

•  HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

•  HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

•  HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A,
S0U61A, S0U62A, S0U66A, S0U68A)

•  HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A,
R8Q68A, R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A,
JL724B, JL725B, JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,
S0M87A, S0M88A, S0M89A, S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

•  HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A,

JL664A, JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A,
S0X44A, S3L75A, S3L76A, S3L77A)

•  HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,

R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

•  HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

Public

About this document 5

•  HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

•  HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

•  HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

•  HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

•  HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A,
JL708A, JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C,
JL709C, JL710C, JL711C, JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

•  HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

•  HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

•  HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

•  HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

example‐text

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

In code and screen examples, indicates text entered
by a user.

Public

Latest version available online 6

Convention

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

About the examples

Examples in this document are representative and might not match your particular switch or environment.

The slot and port numbers in this document are for illustration only and might be unavailable on your switch.

Public

About the examples 7

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

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

•  member: Always 1. VSF is not supported on this switch.

Public

Identifying switch ports and interfaces 8

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6200 Switch Series

•  member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the HPE Aruba Networking 6300 Switch Series

•  member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/1 and 1/2.

◦  Line modules are on the front of the switch starting in slot 1/3.

•  port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

On the HPE Aruba Networking 8xxx, 9300/9300S, and 10000 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

Public

Identifying switch ports and interfaces 9

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

NOTE

If using breakout cables, the port designation changes to x:y, where x is the
physical port and y is the lane when split. For example, the logical interface
1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on
member 1.

On the HPE Aruba Networking 8400 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/5 and 1/6.

◦  Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

•  port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Identifying modular switch components

•  Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

◦  member: 1.

◦  power supply: 1 to 4.

•  Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

◦  member: 1.

◦  tray: 1 to 4.

◦  fan: 1 to 4.

•  Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

◦  member: 1.

◦  member: 1 or 2.

•  The display module on the rear of the switch is not labeled with a member or slot number.

Public

Identifying modular switch components 10

Job Scheduler

•  The Job Scheduler enables you to execute batches of CLI commands on a user-configured schedule

or interval. Job Scheduler can be used, for example, to schedule activities such as port toggles, switch
reboots, QoS policy changes, system health status checks, statistics clearing, clean-up, and saving the
running configuration.

•  Schedules can trigger jobs based on calendar date and time or at periodic intervals.

•  Jobs can be scheduled to execute as frequently as once every thirty minutes.

•  When executed, commands with simple (y/n) prompts (such as  boot system ) will be automatically
confirmed with "y." Other commands requiring more complex user input (such as password change)
cannot be used.

Subtopics

Working with Job Scheduler
Job Scheduler commands

Working with Job Scheduler

To help understand how to work with the Job Scheduler, several basic examples are presented, followed by
detailed descriptions of the commands involved under Job scheduler commands.

Port toggle example

This example creates a port toggle job and then schedules the job for execution on Monday and Friday night
at 11:45 PM.

Creating a port toggle job named PTog1:

switch(config)# job PTog1

switch(config-job-PTog1)# desc Toggle port 1/1/1

switch(config-job-PTog1)# 10 cli config

switch(config-job-PTog1)# 20 cli interface 1/1/1

switch(config-job-PTog1)# 30 cli shutdown

switch(config-job-PTog1)# 40 delay 10 cli no shutdown
switch(config-job-PTog1)# 50 cli end

switch(config-job-PTog1)# exit

Public

Job Scheduler 11

Creating a schedule named PT2xW that runs the port toggle job PTog1 on Mondays and Fridays at 11:45
PM, starting on August 2 2021, with a one-year duration:

switch(config)# schedule PT2xW

switch(config-schedule-PT2xW)# desc Monday & Friday 11:45 PM port toggles

switch(config-schedule-PT2xW)# 10 job PTog1

switch(config-schedule-PT2xW)# trigger on 23:45 weekly 2,6 count 104 start

2021-08-02

switch(config-schedule-PT2xW)# exit

Showing the port toggle job information after first execution:

switch# show job PTog1

Job Name : PTog1

    Enabled                : Yes

    Description            : Toggle port 1/1/1

    Status                 : waiting

    Number of commands     : 5

    Total execution count  : 1

    Failed execution count : 0

    Job execution history

    ---------------------

    Instance number        : 1

    Execution status       : success

    Execution start time   : Mon Aug 2 23:45:00 2021

    Execution duration     : 10s

    Job CLI commands

    ----------------

    10 cli config

    20 cli interface 1/1/1

    30 cli shutdown

    40 delay 10 cli no shutdown

    50 cli end
Showing the port toggle job schedule information after first execution:

switch# show schedule PT2xW

Schedule Name: PT2xW

    Schedule config

    ---------------

    Description         : Monday & Friday 11:45 PM port toggles
    Enabled             : Yes
    Trigger type        : calendar

    Transient           : No

    Max trigger count   : 104

Public

Working with Job Scheduler 12

    Trigger start date  : 2021-08-02 23:45

    Schedule Status

    ---------------

    Trigger status      : active

    Next trigger time   : Fri Aug  6 23:45:00 2021

    Triggered count     : 1

    Scheduled Jobs

    --------------

    10  : PTog1
Showing the port toggle job most recent execution output:

switch# show job PTog1 execution-output 1

============================================================================

=====

Command: config

time: Mon Aug  2 23:45:00 2021

============================================================================

=====

============================================================================

=====

Command: interface 1/1/1

time: Mon Aug  2 23:45:00 2021

============================================================================

=====

============================================================================

=====

Command: shutdown

time: Mon Aug  2 23:45:00 2021

============================================================================

=====

============================================================================

=====

Command: cli no shutdown

time: Mon Aug  2 23:45:10 2021

============================================================================

=====

============================================================================

=====

Command: end

time: Mon Aug  2 23:45:10 2021

============================================================================

=====

Public

Working with Job Scheduler 13

Switch reboot example

This example creates a switch reboot job and then schedules the job for execution on the last day of every
month at 3:00 AM.

Creating a job named Reboot_sw1 that saves the running configuration and then reboots the switch:

switch(config)# job Reboot_sw1

switch(config-job-Reboot_sw1)# desc Save config then reboot switch

switch(config-job-Reboot_sw1)# 10 cli config

switch(config-job-Reboot_sw1)# 20 cli write mem

switch(config-job-Reboot_sw1)# 30 cli boot system

switch(config-job-Reboot_sw1)# exit

switch(config)#
Creating a schedule named RB_LDM that runs the switch reboot job Reboot_sw1 on the last day of the
month at 3:00 AM, starting on January 31 2022, with a two-year duration:

switch(config)# schedule RB_LDM

switch(config-schedule-RB_LDM)# desc Monthly reboot 3:00 AM

switch(config-schedule-RB_LDM)# 10 job Reboot_sw1

switch(config-schedule-RB_LDM)# trigger on 3:00 monthly 31 count 24 start

2022-01-31

switch(config-schedule-RB_LDM)# exit

switch(config)#
After the RB_LDM schedule triggers the reboot job Reboot_sw1, the  show events  command is
available to show schedule triggering ( <MODEL>  represents the switch model number):

switch# show events -a -d schedulerd

---------------------------------------------------

Event logs from previous boots

---------------------------------------------------

...

2022-01-31T03:00:14.405135+00:00 <MODEL> schedulerd[2054]: Event|12202|

LOG_INFO|AMM|1/1|Schedule RB_LDM triggered, trigger_count: 1

---------------------------------------------------

Event logs from current boot

---------------------------------------------------

switch#

Job Scheduler commands

Select a command from the list in the left navigation menu.

Subtopics

Public

Job Scheduler commands 14

job
reload
schedule
show job
show capacities (job, schedule)
show reload
show running-config (job, schedule)
show schedule

job

Syntax

In the config context:

job <JOB-NAME>

no job [<JOB-NAME>]
Subcommands available In the job config context ( config-job ):

[no] enable

[no] desc <DESCRIPTION>

[no] [<SEQ-NUM>] [delay <DELAY>] cli <COMMAND>

resequence <START-SEQ-NUM>

            <INCREMENT>

Description

If <JOB-NAME> does not exist, this command creates a job and then enters its context.

The no form of this command deletes the specified job. If no job is specified, all jobs are deleted.

NOTE

Deleting a job also removes it from any schedule that uses the job, preventing
further attempts to execute the job.

If <JOB-NAME> exists, this command enters the config-job- <NAME> context for the specified job.

Parameter

Description

Specifies the job name. Range 1 to 64 characters (alphanumeric
and "_" (underscore)

Public

job 15

Description

Parameter

<JOB‐NAME>

Subcommands

These subcommands are available within the config-job- <NAME> context for configuring the job:

            enable

Enables the job (the default). no enable disables the job.

[no] desc <DESCRIPTION>

Specifies a user-defined job description. no desc removes the description. Range: 1 to 128 characters. For
example:

switch(config-job-PTog1)# desc Toggle port 1/1/1

            [no] [

            <SEQ-NUM>

            ] [delay

            <DELAY>

            ] cli

            <COMMAND>

Adds a CLI command to the job. The no form removes the command from the job. When executed,
commands with simple (y/n) prompts (such as boot system) will be automatically confirmed with "y." Other
commands requiring more complex user input (such as password change) cannot be used.

<SEQ-NUM> specifies the job CLI command sequence number to facilitate ordering of commands within
a job. When omitted, a sequence number that is 10 greater the highest existing sequence number is
auto-assigned. The first auto-assigned sequence number is 10. Range: 1 to 4294967295.

[delay <DELAY>] specifies the delay in seconds before this CLI command is executed. The cumulative delay
for all commands in a job must be no more than 300 seconds. Range 1 to 300.

cli <COMMAND> specifies the CLI command to be executed. Range 1 to 4096 characters.

These commands must not be used in a job: copy, repeat, show boot-history, show core-dump, show
events, show job, show tech, sleep, terminal-monitor.

For example, adding a command as line 18 to a job:

switch(config-job-PTog1)# 18 cli interface 1/1/1
resequence <START-SEQ-NUM>
            <INCREMENT>

Public

job 16

Resequences the CLI command line sequence numbers. Both <START-SEQ-NUM> and <INCREMENT>
default to 10. For example, resequencing the CLI command list to start at 10 with an increment of 5.

switch(config-job-PTog1)# resequence 10 5

switch(config-job-PTog1)# show job PTog1

Job Name : PTog1

...

    Job CLI commands

    ----------------

    10 cli config

    15 cli interface 1/1/1

    20 cli shutdown

...

Usage

•  A maximum of 20 commands can be used in a job.

•  To see the maximum number of jobs and job execution output preserved instances for your particular

switch, use command show capacities job.

•  Jobs must complete execution in under five minutes and are force-stopped after five minutes if they do

not.

Examples

Creating a port toggle job named PTog1:

switch(config)# job PTog1

switch(config-job-PTog1)# desc Toggle port 1/1/1

switch(config-job-PTog1)# 10 cli config

switch(config-job-PTog1)# 20 cli interface 1/1/1

switch(config-job-PTog1)# 30 cli shutdown

switch(config-job-PTog1)# 40 delay 10 cli no shutdown

switch(config-job-PTog1)# 50 cli end
switch(config-job-PTog1)# exit

switch(config)#
Creating a job named Reboot_sw1 that saves the running configuration and then reboots the switch:

switch(config)# job Reboot_Sw1

switch(config-job-Reboot_sw1)# desc Save config then reboot switch

switch(config-job-Reboot_Sw1)# 10 cli config

switch(config-job-Reboot_Sw1)# 20 cli write mem
switch(config-job-Reboot_Sw1)# 30 cli boot system

switch(config-job-Reboot_Sw1)# exit

switch(config)#

Public

job 17

Command History

Release

10.08

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config
config‐job‐
<NAME>

Administrators or local user group members with execution righ
ts for this command.

reload

Syntax

reload

   <1-10> {at YYYY-MM-DD HH:MM:SS}|{after DD:HH:MM}

   active|standby {at YYYY-MM-DD HH:MM:SS}|{after DD:HH:MM}

   at YYYY-MM-DD HH:MM:SS

   after DD:HH:MM

   cancel

Description

Reboot the switch, stack, or chassis at a specific date and time up to 99 days in the future, or after
a specified time period has elapsed. Reload information is not persistent after the reboot. The reload
commands trigger a reload of the default image, which is defined using the boot set-default command. The
reload cancel command cancels a scheduled reload operation.

NOTE
The reload command cannot be issued if an In-Service Software Update (ISSU) is
in progress.

Public

reload 18

Parameter

Description

                        <1‐
10>

On 6200, and 6300M/F Switch series, specify a VSF member ID
to reload that VSF member.

   at YYYY‐MM‐DD HH:MM:SS

On 6200, and 6300M/F Switch series, specify the timestamp fo
r the scheduled VSF member reload, where:

•  YYYY represents the year.
•  MM represents the month, from 01 (January) to 12 (Decem

ber).

•  DD represents the day (01 to 31).
•  HH represents the hour, in 24‐hour clock format, 00‐23.
•  MM represents the minute, 00‐59.
•  SS represents the seconds, 00‐59.

On 6200, and 6300M/F Switch series, specify how much time s
hould elapse before the scheduled VSF member reload, where:

•  DD represents the number of days before the reload
•  HH represents the number of hours before the reload
•  MM represents the number of minutes before the reload.

On 6400 and 8400 Switch series, use the active and standby o
ptions to reload the active or standby management module.

   after DD:HH:MM

(active | standby)

   at YYYY‐MM‐DD HH:MM:SS

On 6400 and 8400 Switch series, specify the timestamp for the
scheduled management module reload, where:

   after DD:HH:MM

•  YYYY represents the year.
•  MM represents the month, from 01 (January) to 12 (Decem

ber).

•  DD represents the day (01 to 31).
•  HH represents the hour, in 24‐hour clock format, 00‐23.
•  MM represents the minute, 00‐59.
•  SS represents the seconds, 00‐59.

On 6400 and 8400 Switch series, specify how much time shoul
d elapse before the scheduled management module reload, whe
re:

•  DD represents the number of days before the reload
•  HH represents the number of hours before the reload
•  MM represents the number of minutes before the reload.

Public

reload 19

Parameter

Description

at YYYY‐MM‐DD HH:MM:SS

   after DD:HH:MM

cancel

Usage

On 4100i, 5420, 6000, 6100, 6300M/F, 6300L, 6400, 8100, 8
320, 8325/8325H/8325P, 8360, 9300/9300S and 10000 swi
tch series, specify the timestamp for the scheduled reload, whe
re

•  YYYY represents the year.
•  MM represents the month, from 01 (January) to 12 (Decem

ber).

•  DD represents the day (01 to 31).
•  HH represents the hour, in 24‐hour clock format, 00‐23.
•  MM represents the minute, 00‐59.
•  SS represents the seconds, 00‐59.

On 4100i, 5420, 6000, 6100, 6300, 6400, 8100, 8320, 8325/8
325H/8325P, 8360, 9300/9300S and 10000 switch series, spe
cify how much time should elapse before the scheduled manag
ement module reload, where:

•  DD represents the number of days before the reload
•  HH represents the number of hours before the reload
•  MM represents the number of minutes before the reload.

Cancel any scheduled reload operations.

Configuring the reload feature will use one job scheduler space and reduce the number of available job
scheduler configurations.

Examples

Scheduling a system reload on 4100i, 5420, 6000, 6100, 6300, 6400, 8100, 8320, 8325/8325H/8325P,
8360, 9300/9300S or 10000 switch series at a specific date and time:

switch# reload at 2025-08-12 12:01:00

Reload scheduled at 12:01:00 08/12/2025 (in 10 days, 15 hours, 17 minutes,

12 seconds)

The system will be rebooted at the scheduled time from the secondary image.

Continue (y/n)? y

Warning! Any change in configuration may be lost during the scheduled

reboot.

Please remember to save the changes before the scheduled reboot happens.

Configuring reload feature will reduce one job configuration.
Scheduling a system reload on 4100i, 5420, 6000, 6100, 6300, 6400, 8100, 8320, 8325/8325H/8325P,
8360, 9300/9300S or 10000 switch series in one day and one hour from the current time:

Public

reload 20

switch# reload after 01:01:00

Reload scheduled in 1 days, 1 hours, 0 minutes

The system will be rebooted at the scheduled time from the secondary image.

Continue (y/n)? y

Warning! Any change in configuration may be lost during the scheduled

reboot.

Please remember to save the changes before the scheduled reboot happens.

Configuring reload feature will reduce one job configuration.
Scheduling a reload of an active management module on a 6400 or 8400 Switch series at a specified date
and time:

switch# reload active at 2025-08-12 12:01:00

Reload scheduled at 12:01:00 08/12/2025 (in 10 days, 15 hours, 17 minutes,

12 seconds)

The system will be rebooted at the scheduled time from the primary image.

Continue (y/n)? y

Warning! Any change in configuration may be lost during the scheduled

reboot.

Please remember to save the changes before the scheduled reboot happens.

Configuring reload feature will reduce one job configuration.
Scheduling a reload of an active management module on a 6400 or 8400 Switch series in one hour and one
day from the current time:

switch# reload standby after 01:01:00

Reload scheduled in 1 days, 1 hours, 0 minutes

The system will be rebooted at the scheduled time from the secondary image.

Continue (y/n)? y

Warning! Any change in configuration may be lost during the scheduled

reboot.

Please remember to save the changes before the scheduled reboot happens.

Configuring reload feature will reduce one job configuration.
Scheduling a reload of VSF member 4 on a 6300M/F or 6200 Switch series at a specified date and time.

Switch# reload 4 at 2025-08-12 12:01:00
Reload scheduled at 12:01:00 08/12/2025 (in 10 days, 15 hours, 17 minutes,

12 seconds)

The system will be rebooted at the scheduled time from the primary image.

Continue (y/n)? y

Warning! Any change in configuration may be lost during the scheduled

reboot.

Please remember to save the changes before the scheduled reboot happens.

Configuring reload feature will reduce one job configuration.
Scheduling a reload of VSF member 4 on a 6300M/F or 6200 Switch series, one day and one hour after the
current time.

Public

reload 21

switch# reload 4 after 01:01:00

Reload scheduled in 1 days, 1 hours, 0 minutes

The system will be rebooted at the scheduled time from the secondary image.

Continue (y/n)? y

Warning! Any change in configuration may be lost during the scheduled

reboot.

Please remember to save the changes before the scheduled reboot happens.

Configuring reload feature will reduce one job configuration.

Command History

Release

Modification

10.16.1000

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config
config‐job‐
<NAME>

Administrators or local user group members with execution righ
ts for this command.

schedule

Syntax

In the config context:

schedule <SCHEDULE-NAME> [transient]

no schedule [<SCHEDULE-NAME>]
Subcommands available In the schedule config context ( config-schedule ):

[no] enable

[no] desc <DESCRIPTION>
[no] [<SEQ-NUM>] job <JOB-NAME>

resequence <START-SEQ-NUM>

            <INCREMENT>

[no] trigger on HH:MM {daily | weekly <1-7> | monthly <1-31>}

Public

schedule 22

     [count <1-1000>] [start YYYY-MM-DD]

[no] trigger every {days <1-365> | hours <1-8760> | minutes <30-525600>}

     [count <1-1000> ] [start HH:MM [YYYY-MM-DD]]

[no] trigger at HH:MM [YYYY-MM-DD]

Description

If <SCHEDULE-NAME> does not exist, this command creates a job schedule and then enters its context.

The no form of this command deletes the specified schedule. If no schedule is specified, all schedules are
deleted.

If <SCHEDULE-NAME> exists, this command enters the config-schedule- <NAME> context for the specified
job schedule.

Parameter

Description

<SCHEDULE‐NAME>

[transient]

Subcommands

Specifies the schedule name. Range 1 to 64 characters (alphan
umeric and "_" (underscore)).

Causes the schedule to be cleared upon switch reboot. By defau
lt, schedules are maintained after switch reboots.

These subcommands are available within the  config-schedule-<NAME>   context for scheduling
jobs and controlling the order in which the jobs are executed:

            enable

Enables the schedule (the default).  no enable  disables the schedule.

[no] desc <DESCRIPTION>

Specifies a user-defined schedule description.  no desc  removes the description. Range: 1 to 128
characters. For example:

switch(config-schedule-Monthly)# desc Monthly schedule

            [no] [

            <SEQ-NUM>

            ] job

            <JOB-NAME>

Associates an existing job with this schedule. The no form removes the job from the schedule.

<JOB-NAME>  specifies an existing job name. Range: 1 to 64 characters (alphanumeric and "_"
(underscore)).

Public

schedule 23

<SEQ-NUM>  specifies the job name sequence number to facilitate ordering of jobs within a schedule.
When omitted, a sequence number that is 10 greater the highest existing sequence number is auto-
assigned. The first auto-assigned sequence number is 10.

For example, associating two jobs with the selected schedule:

switch(config-schedule-Monthly)# 10 job PTog1

switch(config-schedule-Monthly)# 20 job PTog2

resequence <START-SEQ-NUM>

            <INCREMENT>

Resequences the job name sequence numbers in the schedule. Both  <START-SEQ-NUM>  and  <INCRE
MENT>  default to 10. For example, resequencing the job list to start at 5 with an increment of 10.

switch(config-schedule-Monthly)# resequence 5 10

switch(config-schedule-Monthly)# show schedule Monthly

Schedule Name: Monthly

...

    Scheduled Jobs

    --------------

    5   : PTog1

    15  : PTog2

[no] trigger on HH:MM {daily | weekly <1-7> | monthly <1-31>}

                 [count <1-1000>] [start YYYY-MM-DD]

Sets the job to trigger at a specific time. The no form removes the trigger.

HH:MM  selects the time using a 24-hour clock (switch local time). Range: 00:00 to 23:59.

daily  selects daily.

weekly <1-7>   selects specific days of week or days-of-week ranges (with comma or hyphen
separators) using numeric day-of-week numbers with Sunday equal 1. For example:  1,3,5-7  for Sunday,
Tuesday, Thursday, Friday, Saturday.

monthly <1-31>  selects specific days of month or days of month ranges (with comma or hyphen
separators) using numeric day-of-month numbers. For example:  5,14-21,25,31 . For months with
fewer days than the specified day number, the last day of the month is selected.

count <1-1000>  selects the number of times the job will be executed. When omitted, job execution
triggering is indefinite.

start YYYY-MM-DD  selects the schedule first trigger date. When omitted, today's date is used for
times at least 5 minutes into the future, otherwise tomorrow is selected as the first trigger date.

For example, setting the schedule to trigger monthly on the 15th, at 11:45 PM, starting on August 15, with
an execution limit of 200:

switch(config-schedule-M)# trigger on 23:45 monthly 15 count 200 start

2021-08-15

Public

schedule 24

            [no] trigger every {days <1-365> | hours <1-8760> | minutes

<30-525600>}

                 [count <1-1000>] [start HH:MM [YYYY-MM-DD]]

Sets the job trigger to a specific periodic interval. The no form removes the trigger. By default, the schedule
is activated within 5 minutes from the configuration time. If the start time is specified, then the job is
executed beginning at the specified start time and thereafter at the specified interval.

days <1-365>  selects the interval in days. Range: 1 to 365.

hours <1-8760>  selects the interval in minutes. Range: 1 to 8760.

minutes <30-525600>  selects the interval in seconds. Range: 30 to 525600.

count <1-1000>  selects the number of times the job will be executed. When omitted, job execution
triggering is indefinite.

start HH:MM [YYYY-MM-DD]  selects the schedule first trigger time and date.

For example, setting the schedule to trigger once every 14 days, starting on January 1, with an execution
limit of 500:

switch(config-schedule-Ev14D)# trigger every days 14 count 500 start

2022-01-01

            [no] trigger at HH:MM [YYYY-MM-DD]

Sets the job to trigger one time only on a specific date and time. When the date is omitted, today's date is
used for times at least 5 minutes into the future, otherwise tomorrow is selected. The no form removes the
trigger.

For example, setting the schedule to trigger once only on August 26 at midnight:

switch(config-schedule-Aug26)# trigger at 00:00 2021-08-26

Usage

•  A job can be used only once per schedule.

•  To see the maximum number of schedules and jobs per schedule for your particular switch, use

command show capacities schedule.

•  Configure the jobs to be executed (using the job command) before configuring a schedule.

•  Jobs must complete execution in under five minutes and are force-stopped after five minutes if they do

not.

•  A job must be scheduled to execute at least five minutes after its previous execution. If the same job is

scheduled to be executed again within less than five minutes, the execution is skipped.

Public

schedule 25

Examples

Creating a schedule named PT2xW that runs the port toggle job PTog1 on Mondays and Fridays at 11:45
PM, starting on August 2 2021, with a one-year duration:

switch(config)# schedule PT2xW

switch(config-schedule-PT2xW)# desc Monday & Friday 11:45 PM port toggles

switch(config-schedule-PT2xW)# 10 job PTog1

switch(config-schedule-PT2xW)# trigger on 23:45 weekly 2,6 count 104 start

2021-08-02

switch(config-schedule-PT2xW)# exit

switch(config)#
Creating a schedule named RB_LDM that runs the switch reboot job on the last day of the month at 3:00
AM, starting on January 31 2022, with a two-year duration:

switch(config)# schedule RB_LDM

switch(config-schedule-RB_LDM)# desc Monthly reboot 3:00 AM

switch(config-schedule-RB_LDM)# 10 job Reboot_sw1

switch(config-schedule-RB_LDM)# trigger on 3:00 monthly 31 count 24 start

2022-01-31

switch(config-schedule-RB_LDM)# exit

Command History

Release

10.08

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config
config‐
schedule‐<NAME>

Administrators or local user group members with execution righ
ts for this command.

show job

Public

show job 26

Syntax

show job [<JOB-NAME>] [execution-output <INSTANCE-ID>]

Description

Shows information about a specific job or every job. Optionally shows the job execution output log.

Parameter

Description

Specifies an existing job name. When omitted, information is sh
own for every job. Range: 1 to 64 characters (alphanumeric and
"_" (underscore)).

Selects the job execution output instance with 1 selecting the
most recent. To see the maximum number of job execution out
put instances for your particular switch, use command show ca
pacities job.

<JOB‐NAME>

<INSTANCE‐ID>

Usage

Job execution statistics such as execution counts are reset to zero upon switch reboot.

Examples

Showing port toggle job information before execution has occurred:

switch# show job PTog1

Job Name : PTog1

    Enabled                : Yes

    Description            : Toggle port 1/1/1

    Status                 : waiting

    Number of commands     : 5
    Total execution count  : 0

    Failed execution count : 0

    Job CLI commands

    ----------------

    10 cli config

    20 cli interface 1/1/1

    30 cli shutdown

    40 delay 10 cli no shutdown

    50 cli end
Showing port toggle job information after execution has occurred:

Public

show job 27

switch# show job PTog1

Job Name : PTog1

    Enabled                : Yes

    Description            : Toggle port 1/1/1

    Status                 : waiting

    Number of commands     : 5

    Total execution count  : 1

    Failed execution count : 0

    Job execution history

    ---------------------

    Instance number        : 1

    Execution status       : success

    Execution start time   : Mon Aug 2 23:45:00 2021

    Execution duration     : 10s

    Job CLI commands

    ----------------

    10 cli config

    20 cli interface 1/1/1

    30 cli shutdown

    40 delay 10 cli no shutdown

    50 cli end
Showing port toggle job most recent execution output:

switch# show job PTog1 execution-output 1

============================================================================

=====

Command: config

time: Mon Aug  2 23:45:00 2021

============================================================================

=====

============================================================================

=====

Command: interface 1/1/1

time: Mon Aug  2 23:45:00 2021

============================================================================

=====

============================================================================

=====

Command: shutdown

time: Mon Aug  2 23:45:00 2021

============================================================================

=====

============================================================================

Public

show job 28

=====

Command: cli no shutdown

time: Mon Aug  2 23:45:10 2021

============================================================================

=====

============================================================================

=====

Command: end

time: Mon Aug  2 23:45:10 2021

============================================================================

=====

Command History

Release

10.08

Modification

Command introduced.

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

show capacities (job, schedule)

Syntax

show capacities {job | schedule}

Description

Shows either job or schedule capacities information for your switch model.

Examples

Showing job capacities information (8320 example shown):

switch# show capacities job

System Capacities: Filter Job

Public

show capacities (job, schedule) 29

Capacities

Name                                                              Value

----------------------------------------------------------------------------

------

Maximum number of job execution output preserved per

job                        10

Maximum number of jobs configurable in a

system                                 32
Showing schedule capacities information (8320 example shown):

switch# show capacities Schedule

System Capacities: Filter Schedule

Capacities

Name                                                              Value

----------------------------------------------------------------------------

------

Maximum number of jobs configurable in a

schedule                               10

Maximum number of schedules configurable in a

system                            32

Command History

Release

10.08

Modification

Command introduced.

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

show reload

Syntax

show reload

Public

show reload 30

Description

Display the configuration defined using the reload command.

Examples

Displaying the reload configuration on a 4100i, 5420, 6000, 6100, 6300, 6400, 8100, 8320, 8325/8325H/
8325P, 8360, 9300/9300S or 10000 switch series:

switch# show reload

----------------------------------------------------

Reload Configuration

----------------------------------------------------

Module                :  Chassis

Reboot after          :  2 days, 8 hours, 10 minutes

----------------------------------------------------
Displaying the reload configuration on an active management module on a 6400 or 8400 Switch series:

switch# show reload

----------------------------------------------------

Reload Configuration

----------------------------------------------------

Module                :  AMM

Reboot after          :  2 days, 8 hours, 08 minutes

----------------------------------------------------
Displaying the reload configuration on a standby management module on a 6400 or 8400 Switch series:

switch# show reload

----------------------------------------------------

Reload Configuration

----------------------------------------------------

Module                :  SMM

Reboot after          :  2 days, 8 hours, 10 minutes
Displaying the reload configuration on a 6300M/F or 6200 Switch series.

switch# show reload

----------------------------------------------------

Reload Configuration

----------------------------------------------------

Module                :  Stack

VSF member            :  2

Reboot at             :  2025-04-12 12:01:00

----------------------------------------------------

Public

show reload 31

Command History

Release

Modification

10.16.1000

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config
config‐job‐
<NAME>

Administrators or local user group members with execution righ
ts for this command.

show running-config (job, schedule)

Syntax

show running-config [current-context]

Description

Shows the entire running configuration for the switch, including configuration details for the Job Scheduler
job and schedule configuration.

Parameter

Description

current‐context

When included from within the Job Scheduler job or schedule c
ontext, shows only the job or schedule configuration informatio
n for the selected job or schedule.

Examples

Showing the running configuration information for all jobs and schedules with unrelated configuration
information omitted for clarity (omitted portions represented by ellipses("..."):

switch# show running-config

Current configuration:

...

Public

show running-config (job, schedule) 32

!

job PTog1

    desc Toggle port 1/1/1

    10 cli config

    20 cli interface 1/1/1

    30 cli shutdown

    40 delay 10 cli no shutdown

    50 cli end

job Reboot_sw1

    desc Save config then reboot switch

    10 cli config

    20 cli write mem

    30 cli boot system

schedule PT2xW

    desc Monday & Friday 11:45 PM port toggles

    trigger on 23:45 weekly 2,6 count 104 start 2021-08-02

    10 job PTog1

schedule RB_LDM

    desc Monthly reboot 3:00 AM

    trigger on 3:00 monthly 31 count 24 start 2022-01-31

    10 job Reboot_sw1

...
From within the job PTog1 context, showing the running configuration information for the job:

switch(config-job-PTog1)# show running-config current-context

Current configuration:

job PTog1

    desc Toggle port 1/1/1

    10 cli config

    20 cli interface 1/1/1

    30 cli shutdown

    40 delay 10 cli no shutdown

    50 cli end
From within the schedule PT2xW context, showing the running configuration information for the schedule:

switch(config-schedule-PT2xW)# show running-config current-context

Current configuration:

schedule PT2xW

    desc Monday & Friday 11:45 PM port toggles

    trigger on 23:45 weekly 2,6 count 104 start 2021-08-02
    10 job PTog1

Public

show running-config (job, schedule) 33

Command History

Release

10.08

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

config‐job‐
<NAME>
config‐
schedule‐<NAME>

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show schedule

Syntax

show schedule [<SCHEDULE-NAME>]

Description

Shows information about a specific schedule or every schedule.

Parameter

Description

Specifies an existing job schedule name. When omitted, inform
ation is shown for every schedule. Range: 1 to 64 characters (al
phanumeric and "_" (underscore)).

<SCHEDULE‐NAME>

Usage

Schedule statistics such as Triggered count are reset to zero upon switch reboot.

Public

show schedule 34

Examples

Showing port toggle job schedule information before execution has occurred:

switch# show schedule PT2xW

Schedule Name: PT2xW

    Schedule config

    ---------------

    Description         : Monday & Friday 11:45 PM port toggles

    Enabled             : Yes

    Trigger type        : calendar

    Transient           : No

    Max trigger count   : 104

    Trigger start date  : 2021-08-02 23:45

    Schedule Status

    ---------------

    Trigger status      : active

    Next trigger time   : Mon Aug  2 23:45:00 2021

    Scheduled Jobs

    --------------

    10  : PTog1
Showing port toggle job schedule information after execution has occurred:

switch# show schedule PT2xW

Schedule Name: PT2xW

    Schedule config

    ---------------

    Description         : Monday & Friday 11:45 PM port toggles

    Enabled             : Yes

    Trigger type        : calendar

    Transient           : No

    Max trigger count   : 104

    Trigger start date  : 2021-08-02 23:45

    Schedule Status

    ---------------

    Trigger status      : active

    Next trigger time   : Fri Aug  6 23:45:00 2021

    Triggered count     : 1

    Scheduled Jobs

    --------------

    10  : PTog1

Public

show schedule 35

Command History

Release

10.08

Modification

Command introduced.

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

Public

Support and Other Resources 36

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

Public

Accessing HPE Aruba Networking Support 37

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

Public

Accessing Updates 38

Documentation Feedback

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us improve
the documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition, and
publication date located on the front cover of the document. For online help content, include the product
name, product version, help edition, and publication date located on the legal notices page.

Public

Documentation Feedback 39

