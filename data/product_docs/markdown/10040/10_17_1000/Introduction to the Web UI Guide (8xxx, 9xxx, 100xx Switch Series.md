AOS-CX 10.17.xxxx Introduction to the Web UI Guide (8xxx, 9xxx,
100xx Switch Series)

Published: February 2026

AOS-CX 10.17.xxxx Introduction to the Web UI Guide (8xxx, 9xxx,
100xx Switch Series)

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

AOS-CX 10.17.xxxx Introduction to the Web UI Guide...

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

I
n
t
r
o
d
u
c
t
i
o
n

t
o

t
h
e

W
e
b

U
I

G
u
i
d
e
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.17.xxxx Introduction to the Web UI Guide...

Table of contents

About this document..................................................................................................................................................................................6

Applicable products........................................................................................................................................................................6

Latest version available online.................................................................................................................................................7

Command syntax notation conventions.............................................................................................................................7

About the examples....................................................................................................................................................................... 8

Identifying switch ports and interfaces...............................................................................................................................9

Identifying modular switch components............................................................................................................................9

Accessing the AOS-CX Web UI.......................................................................................................................................................... 10

AOS-CX Web UI overview..................................................................................................................................................................... 13

AOS-CX Web UI framework.................................................................................................................................................... 13

Customizing the Web UI........................................................................................................................................................... 16

Customizing page layouts...........................................................................................................................................16

Adding a custom panel to the Overview page................................................................................................17

Customizing tables..........................................................................................................................................................19

Using Show/Hide filters in tables........................................................................................................................... 20

AOS-CX Web UI pages............................................................................................................................................................................21

Navigation pane.............................................................................................................................................................................22

Overview page................................................................................................................................................................................24

Analytics Dashboard...................................................................................................................................................................26

Interfaces page...............................................................................................................................................................................29

Editing an interface.........................................................................................................................................................30

VLANs page.....................................................................................................................................................................................31

LAGs page.........................................................................................................................................................................................32

Users page........................................................................................................................................................................................ 33

VSX page........................................................................................................................................................................................... 34

Environmental page.................................................................................................................................................................... 36

Log page............................................................................................................................................................................................ 37

Name Server page........................................................................................................................................................................40

SNMP page.......................................................................................................................................................................................40

Session page....................................................................................................................................................................................41

Config Mgmt page........................................................................................................................................................................44

Firmware Update page.............................................................................................................................................................. 46

Firmware Mgmt page................................................................................................................................................................. 50

Ping page...........................................................................................................................................................................................52

Public

Table of contents 4

Traceroute page.............................................................................................................................................................................53

Show Tech page.............................................................................................................................................................................54

Spanning Tree page.................................................................................................................................................................... 54

Connected Clients page............................................................................................................................................................ 55

PKI page............................................................................................................................................................................................. 56

Support File page..........................................................................................................................................................................58

Finding alert details using the Web UI.......................................................................................................................................... 60

Working with the network analytics features............................................................................................................................63

Support and Other Resources............................................................................................................................................................63

Accessing HPE Aruba Networking Support..................................................................................................................64

Accessing Updates.......................................................................................................................................................................65

Warranty Information................................................................................................................................................................. 65

Regulatory Information............................................................................................................................................................. 66

Documentation Feedback........................................................................................................................................................66

Public

Table of contents 5

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

•  HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

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

•  HPE Aruba Networking 10040 Switch Series (S4R58A, S4R59A)

Public

About this document 6

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

example‐text

Any of the following:

•  <example‐text>
•  <example‐text>
•  example‐text
•  example‐text

|

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

Public

Latest version available online 7

Convention

Usage

{ }

[ ]

…  or

...

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

Public

About the examples 8

switch(config-vlan-100)#
When referring to this context, this document uses the syntax:

switch(config-vlan-<VLAN-ID>)#
Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 8xxx, 93xx, and 10xxx Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

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

Public

Identifying switch ports and interfaces 9

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

Accessing the AOS-CX Web UI

NOTE

When HPE Aruba Networking Central manages AOS-CX switches, it functions as
the single source of truth and the Web UI operates in read-only mode.

NOTE

The Web UI can be opened and accessed using both IPv4 and IPv6.

NOTE
After upgrading or downgrading the AOS-CX software on the switch, you must
clear the browser cache to ensure proper functionality of the Web UI pages for
the switch.

Prerequisites

•  Use a supported browser to access the Web UI, such as Chrome, Firefox, Edge, or Safari. For details on

supported browser versions, see the Release Notes for the version of AOS-CX you are using.

•  You must have a valid login user name and password or a valid certificate.

Public

Accessing the AOS-CX Web UI 10

•  You must have configured the management interface on the switch and enabled REST access for the

VRF that people will access the UI on.

•  To use the Web UI to make configuration changes—such as adding users—the following must be true:

◦  You must have a valid login user name and password, or a valid certificate.

◦  The user name you use to log in must have administrator rights.

◦  The REST API access mode must be set to  read-write .

For information about configuring the management interface and REST API access, see the AOS-CX
Fundamentals Guide .

For information about configuring and managing the certificates, see the AOS-CX Security Guide.

Procedure

1.  Start a supported web browser and enter the IP address of the management port in the address bar. Use

HTTPS.
For example:

https://192.0.2.5 or https://[1001::2]

2.  Optionally a pre- and post-login message may be displayed. The message can be customized or disabled

with the  banner  command.

3.  For the password-based authentication, at the login page, enter your user name and password

credentials, then click Login. For the certificate-based authentication, at the login page, click LOGIN
WITH CERTIFICATE, select your certificate and click Accept.

4.  After you log in, the main Web UI page is displayed.

NOTE

Ensure that both the switch and the client where the Web UI is running are set
to use NTP or to a time zone based on UTC time. If the switch and the client
time are not in sync, then a message is displayed after you log in, indicating
the time difference.

Troubleshooting Web UI access issues

View issue symptoms and causes, as well as actions to resolve common Web UI access issues.

HTTP 404 error when accessing the switch URL

Symptom

The switch is operational and you are using the correct URL for the switch, but attempts to access the REST
API or Web UI result in an HTTP 404 "Page not found" error.

Public

Accessing the AOS-CX Web UI 11

Cause

REST API access is not enabled on the VRF that corresponds to the access port you are using. For example,
you are attempting to access the REST API or Web UI from the management (OOBM) port, and access is not
enabled on the  mgmt  VRF.

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

A user attempted to log into the REST API or the Web UI, but that user already has the maximum number of
concurrent sessions running.

Action

1.  Log out from one of the existing sessions.

Browsers share a single session cookie across multiple tabs or even windows. However, scripts that
POST to the login resource and later do not POST to the logout resource can easily create the maximum
number of concurrent sessions.

2.

3.

If the session cookie is lost and it is not possible to log out of the session, then wait for the session idle
time limit to expire.
When the session idle timeout expires, the session is terminated automatically.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time limit
to expire, you can stop all HTTPS sessions using the https-server session close all command.
This command stops and starts the hpe-restd service, so using this command affects all existing REST
sessions, Web UI sessions, and real-time notification subscriptions.

"Not Authorized" is displayed instead of page content

Symptom

The message "Not Authorized" is displayed in the details pane of a Web UI page.

Cause

You have logged in as a user that is not authorized to view this page.

Public

Accessing the AOS-CX Web UI 12

Action

Use the navigation pane to select a page you are authorized to access.

AOS-CX Web UI overview

The AOS-CX Web UI provides quick and easy visibility into what is happening on your switch. With the Web
UI, you get faster problem detection, diagnosis, and resolution.

You can use the Web UI to do the following:

•  Monitor the status of a switch from a single pane that shows easy-to-read indicators for power,

temperature, fans, CPU use, memory use, log entries, system information, firmware, and various aspects
of the network configuration.

•

Identify issues when indicators turn red, and quickly locate and diagnose the problem.

•  View and configure Network Analytics Engine agents, scripts, and alerts.

•  Modify some aspects of the switch configuration.

•  Run diagnostics including the  ping ,  traceroute , and  show tech  commands.

•  Upgrade or downgrade the image build on the device.

•  Reboot the switch.

Subtopics

AOS-CX Web UI framework
Customizing the Web UI

AOS-CX Web UI framework

About this task

Descriptions for (numbered) common areas, buttons, menus, and controls in the Web UI are listed after the
image.

Figure 1. Overview page with callouts

Public

AOS-CX Web UI overview 13

Figure 2. Overview page with callouts

Procedure

1.  The Show/Hide button on the left in the top banner, allows you to hide the navigation pane (slides the

pane in and out).

Public

AOS-CX Web UI framework 14

2.  The navigation pane. Expand or collapse the System or Diagnostics group to show or hide related items.
For a description of each menu item in the navigation pane, see the description of the Navigation pane.

3.  Breadcrumbs in the top banner show the path to your navigation selection.

4.  The top banner provides information and other menu items.

5.  The details pane shows information based on your selection.

6.  Panels in the details pane display status, alerts, and other information and allow you to drill down to

more information.

7.  The IP address of the management (mgmt) interface through which the switch Web UI is opened and
the name of the switch are displayed at the center of the top banner. If a switch does not have a mgmt
interface or if the mgmt interface is not configured, then an IP address is not displayed.

8.  The Layout Management icon in the top banner allows you to unlock the details pane page layout. You

can then resize and move panels, or reset the details pane page layout to the default layout. Changes are
persistent in the local browser. The icon changes to , when the layout is unlocked.

9.  The User Management menu in the top banner includes a logout selection.

10.  The System menu in the top banner includes the following:

•  Save Config: Save configuration changes

•  Reboot: Reboot the switch to either primary or secondary image.

•  v10.04 API: Access v10.04 REST APIs that you can use to read and/or write to the switch.

11.  The Help icon provides a link to AOS-CXuser documentation.

12.  The Show/Hide button on the right side of the top banner displays the Log Summary pane (slides the
pane in and out). The Log Summary provides a summary of the most recent critical level log entries in
the last X seconds. It also shows counts of the number of critical, warning, and info log entries arriving in
the last X seconds.

Public

AOS-CX Web UI framework 15

Customizing the Web UI

•  You can customize the Web UI to change the page layout, include additional information, or filter to

display selected information.

•  The changes that you make to customize the Web UI are restricted to the browser session. For example,
if you add a custom panel for an interface, the panel will be available only in the current browser session.
That is, if you open a Web UI session in a different browser or device, the newly added panel will not be
available.

Subtopics

Customizing page layouts
Adding a custom panel to the Overview page
Customizing tables
Using Show/Hide filters in tables

Customizing page layouts

Some of the pages in the Web UI provide a user customizable layout. Each customization is persistent in the
local browser. The customization is stored based on the switch URL (based on the management address of
the switch). For example, if you change the management address, you will lose any page layout configuration
that was tied to that URL.

Each page can be reset back to the default layout.

Prerequisites

You must be logged in to the Web UI. You must allow cookies to be stored.

Procedure

1.

In the top banner, click the
Layout Management icon, and select Unlock Page Layout to unlock the
layout. The panel borders change to a dotted line, indicating that you can resize and move the panels in
the details pane.

Figure 1. Unlock Page Layout menu

Public

Customizing the Web UI 16

Some of the possible changes you can make to a panel are described in the following steps.

2.  To resize a panel, drag the handle at the bottom-right corner of the panel, and change the width and

height.

3.  To reposition a panel, move the panel to a new position. The other panels will automatically rearrange to

accommodate the position of the moved panel.

4.  To lock the changes to the page layout, click the

 Layout Management icon, and select Lock

Page Layout.

5.  To reset the page layout to the default view, click the

 Layout Management icon, and select

Reset Page Layout. The option to reset the page is available only when the page layout is unlocked.

Adding a custom panel to the Overview page

You can add a custom panel to the Overview page to display a custom indicator for an interface.

Prerequisites

You must be logged in to the Web UI.

Procedure

1.  Select an empty panel in the Overview page and click the + plus button.

Figure 1. Empty panel with + (plus) button

Public

Adding a custom panel to the Overview page 17

2.  The Set Indicator dialog box is displayed. Select the interface you want to set an indicator for. Use the

Show/Hide Column Filters button to show a specific interface in the list. Click Interface: <X/X/X> to set
an indicator or Cancel to exit.

Figure 2. Set Indicator dialog with example content

Public

Adding a custom panel to the Overview page 18

3.  A new panel showing an indicator for the interface you selected is added to the Overview page.

Figure 3. Panel showing a selected interface

4.

If you want to move the panel you added or customize the new panel, click the Layout Management
menu in the top banner and select Unlock Page Layout to change the layout.

a.  Move the new panel to where you want it to appear on the Overview page.

b.  Resize the new panel, if desired.

5.  To remove a custom indicator panel from the Overview page, click the X in the custom panel.

Customizing tables

You can show or hide table columns and you can resize column widths. Column customization is persistent in
the local browser. For how to filter column data, see Using Show/Hide filters in tables.

Prerequisites

You must be logged in to the Web UI.

Procedure

1.  To hide a table column or show a hidden column, click the

Column Settings button in the title bar of

the table.

•  From the list of column headings displayed, click any of the headings in the list with a check mark to

hide the column.

•  Click any of the headings in the list without a check mark to show the column.

•  Click Reset Table Columns to reset to the default.

Public

Customizing tables 19

Figure 1. List of column headings with check marks

2.  To resize a column drag the column separators to expand or narrow the column. Columns cannot be

reordered.

3.  View additional pages of content in the table using the table scroll bar.

Using Show/Hide filters in tables

You can use filters to display a subset of data in the table. Filtering is not persistent, so when you leave the
page, the filtering is removed.

Prerequisites

You must be logged in to the Web UI.

Public

Using Show/Hide filters in tables 20

Procedure

To filter the data displayed in a table column, click
filter row is displayed below the column headings.

Show/Hide Column Filters on the table title bar. The

1.  For columns that have a drop-down list as a filter, click the down arrow to display the list and select an

item from the list. The data displayed in the column will be filtered to just the specified data.

Figure 1. Filtering a column by selecting from a list

2.  For columns without a drop-down list, type in a value to filter the data in the column. Any item that

matches that value is then displayed. For example, entering lag10 will display data for lag10, lag100,
lag109.

Figure 2. Filtering a column by typing text

3.  Turn off filters by clicking

 Show/Hide Column Filters a second time. The full set of data, without

filtering, will be displayed in the table.

AOS-CX Web UI pages

Public

AOS-CX Web UI pages 21

Descriptions of the AOS-CX Web UI pages, and workflows for using these pages.

Subtopics

Navigation pane
Overview page
Analytics Dashboard
Interfaces page
VLANs page
LAGs page
Users page
VSX page
Environmental page
Log page
Name Server page
SNMP page
Session page
Config Mgmt page
Firmware Update page
Firmware Mgmt page
Ping page
Traceroute page
Show Tech page
Spanning Tree page
Connected Clients page
PKI page
Support File page

Navigation pane

Navigate the Web UI by selecting an item in the navigation pane. Information for the selected item is
displayed in a series of panels in the details pane.

From the details pane, you can select links to drill down to more detailed pages.

Use the

Show/Hide button to show or hide the navigation pane.

The user role of the login user (operators or administrators) determines which items in the navigation pane
you can access.

Expand and collapse the System or Diagnostics group to show or hide related items.

The navigation pane includes the following possible selections. Click the links for more information.

Public

Navigation pane 22

Selection

Overview

Analytics Dashboard

Interfaces

VLANs

LAGs

Users

VSX

System ‐ Environmental

System ‐ Log

System ‐ Name Server

System – SNMP

System ‐ Config Mgmt

Description

Shows important information and statistics about t
he switch. Each indicator panel provides "roll‐up"
status (color and icon) of Analytics, Environmental,
System, and so on. Empty titles allow you to select a
nd save specific interfaces to monitor (packets, bytes
, utilization).

Shows the Analytics Dashboard providing informatio
n related to Network Analytics Engine agents, scripts
, alerts, and actions generated by these scripts.

Shows information for each interface and shows the
status of the interfaces. Allows you to edit the interfa
ces details.

Shows information for each VLAN and the status of t
he VLANs. Allows you to add, edit, and delete VLAN
s.

Shows the information and the up or down status of
the LAGs. Allows you to add, edit, and delete Lags.

Shows user roles and names. Also allows you to add
or delete a user and change user passwords.

Administrator rights are required to access this sele
ction.

Shows the Virtual Switching Extension (VSX) config
uration and status information.

Shows power supply failures and warnings, temperat
ures, and fan information.

Shows event log entries, event log queries, and mess
age details.

Shows primary and secondary name servers, and allo
ws you to configure addresses for name servers.

Shows the SNMPv3 users, SNMP communities, and t
rap receivers details. Allows you to add and delete S
NMPv3 users, SNMP community names, informs, and
trap receivers.

Enables you to upload/download configurations to/f
rom the running or startup configurations.

Public

Navigation pane 23

Selection

Description

System ‐ Firmware Update

Enables you to upload firmware files.

System ‐ Firmware Mgmt

Diagnostics ‐ Ping

Diagnostics ‐ Traceroute

Diagnostics ‐ Show Tech

Traffic ‐ Spanning Tree

Connected Device ‐ Clients

Security ‐ PKI

Enables you to configure the switch to distribute fir
mware to other switches.

Enables you to run the  ping  command with variou
s options.

Enables you to run the  traceroute  command w
ith various options.

Enables you to run the  showtech  command. Ad
ministrator rights are required to run this command.

Shows the details of the spanning tree configuration,
assigned ports, and inconsistent ports. Allows you to
enable Spanning Tree with Multiple Spanning Tree or
Rapid Per‐Vlan Spanning Tree mode.

Shows the details of the devices connected to the sw
itch.

Shows the details of the TA profile, EST profile, digi
tal certificates, and associated applications in the swi
tch. Allows you to add, edit, and delete TA profile; ad
d, view, and delete EST profile; add, view, upload, and
delete certificates; and edit associated applications.

Overview page

The Overview page provides a quick view of the status of a switch. It shows easy-to-read indicators for:
Analytics agents, power supply, thermal, fans, CPU use, memory use, log entries, checkpoints, firmware,
management modules, and system information.

Public

Overview page 24

Custom indicator panels allow you to select specific interfaces to monitor and to add panels for those
interfaces to the Overview page.

NOTE

Ensure that both the switch and the client where the Web UI is running are set
to use NTP or to a time zone based on UTC time. Otherwise, the NAE agent
data might be incorrect or missing and the System Uptime will be incorrect. For
example, if the time on the switch is set to 2 hours ahead of the client manually,
instead of changing the time zone offset, the agent data is populated according
to the new time on the switch. If the switch time is set back to match client time
later, the Time Series Database does not overwrite the old data. Therefore the
client Web UI shows inaccurate data.

Figure 1. WebUI Overview Dashboard

The following table describes each panel included out of the box in the Overview page.

Panel

Analytics

Description

Shows: Total number of agents in critical, major, or m
inor status; total number of agents scripts, agents, an
d monitors (both enabled and disabled) compared to
the maximum number supported on the switch. For
example, 7/25 indicates that there are a total of 7 ou
t of a supported maximum of 25. Clicking the link dis
plays the Analytics Dashboard.

Public

Overview page 25

Description

Shows: Current firmware version, Primary version, an
d Secondary version. Clicking the link displays the Fi
rmware Update page.

Shows: Most recent checkpoint and total number of
checkpoints. Clicking the link displays the Config Mg
mt page.

Shows: Detected module name, Active, and Standby
status information.

Shows: New log entries over the last 15 seconds. Clic
king the link displays the Log page.

Shows: Current average CPU utilization per manage
ment module.

Shows: Percent memory usage per management m
odule.

Shows: System Uptime, System Description, System
Location, System Contact, Serial number, Base MAC,
BIOS Version, Total number of available interfaces, a
nd a pie chart for link status.

Shows: Summary count of alerts. Clicking the link dis
plays the Environmental page.

Shows: Summary count of alerts. Clicking the link dis
plays the Environmental page.

Shows: Summary count of alerts. Clicking the link dis
plays the Environmental page.

Shows: Virtual Switching Extension (VSX) informatio
n, including interswitch link (ISL) state, configuratio
n synchronization state, and the role of this switch (
primary or secondary). Clicking the link displays the
VSX page.

Panel

Firmware

Config

Management Modules

Log

CPU

Memory

System Information

Power Supplies

Thermal

Fans

VSX

Analytics Dashboard

Public

Analytics Dashboard 26

The Analytics Dashboard shows information related to Network Analytics Engine agents, scripts, alerts,
and information generated by these scripts. You can use the Network Analytics Engine to automate data
collection so you can quickly troubleshoot problems on a switch.

To see the total number of agents scripts, agents, and monitors (both enabled and disabled) compared to
the maximum number supported on the switch, see the Analytics panel on the Overview page.

From the Analytics Dashboard, you can drill down to other Analytics detail pages.

For some basic steps to using Analytics to monitor a switch, see Viewing agent information using the Web
UI. For complete information about using the Network Analytics Engine, scripts, and agents, see the Network
Analytics Engine Guide .

NOTE

Ensure that both the switch and the client where Web UI is running are set to use
NTP or to a time zone based on UTC time. Otherwise, NAE agent data might be
incorrect or missing. For example, if the time on switch is set to 2 hours ahead of
the client manually instead of by changing the time zone offset, the agent data is
populated according to the new time on switch. If the switch time is set back to
match client time later, the Time Series Database does not overwrite the old data.
Therefore the client Web UI shows inaccurate data.

If the software detects that the switch time and browser time differs by more
than one minute, the Web UI displays the following:

•  A yellow warning triangle in the top banner of the Analytics Dashboard:

•  When a user logs into the Web UI, the Web UI displays a warning message

with the following title:  Switch Time and Browser Time are n
ot in Sync

Figure 1. Analytics dashboard

Public

Analytics Dashboard 27

Figure 2. Analytics dashboard

Agents panel

The Agents panel displays a list of agents and agent status (Normal, Minor, Major, Critical and Disabled).

Agents monitor what is specified in the script. You can view agent details like alerts, time series graph of
alerts and changes, and parameter information. Agent status (reflecting any alerts or errors) is rolled up to
display in the Analytics panel on the Overview page.

Click the Agents link to drill down to the Agents Management page. Click the link to an individual agent in
the list to drill down to the Agent Details page.

Scripts panel

The Scripts panel displays a list of scripts.

Scripts specify what the Network Analytics Engine monitors. The script also specifies various conditions and
corresponding actions when these conditions are met. Some read-only scripts are provided with the switch.

Public

Analytics Dashboard 28

You can create your own scripts or use scripts from other sources such as ones hosted on the HPE Aruba
Neworking Solution Exchange.

Click the Scripts link to drill down to the Scripts Management page. Click the link to an individual script in
the list to drill down to the Scripts Details page.

Alerts panel

The Alerts panel displays a list of alerts generated by the agents running on the switch. When a condition is
met, an alert is generated.

Select an alert and click the Details button to display a dialog box with more information on the alert. Click
the Alerts link to display the Alert History page. Click an agent name to drill down to the Agents Details
page.

Analytics time series graph

Optionally, you can add an Analytics agent time series graph to the Analytics Dashboard by clicking the +
plus sign next to any agent listed in the Agents panel. If an agent has multiple time series graphs, the graph
displayed on the Analytics Dashboard is specified by the script. You cannot choose which graph to display
on the Analytics Dashboard, but you can see all the graphs in the Agent Details page. The time series graph
shows data collected by the Analytics agent.

Graphs added to the Analytics Dashboard are persistent only in the local browser. If you use a different
system or browser, then you would need to customize to add the graphs for that browser instance.

You can remove a graph by clicking X in the panel with the agent time series graph.

Click the link in the graph to drill down to the Agent Details page.

Interfaces page

The Interfaces page displays a list of interfaces. Details on the interface include: Name, Admin State, Type,
Link Status, Reason for status, Speed, VLAN Mode, a list of VLANs, Trunk Allowed, and a list of LAGs.

Figure 1. Interfaces page

Public

Interfaces page 29

Links in the VLAN and LAG columns allows you to drill down to the respective VLANs or LAGs page,
auto-selecting the appropriate resource.

Selecting a row in the interfaces list, displays more information on the interface. Details include: duplex, MAC,
IPv4, IPv6 address, Rx and Tx stats, packets, and more.

A graphical panel shows interface modules currently installed. Clicking an interface, selects the
corresponding row in the table. Each interface displayed in the graph will dynamically change based on
the current interface status.

Use the Show/Hide Column Filters button or Column Settings button to customize the table display.

Subtopics

Editing an interface

Editing an interface

Use this procedure to perform the following tasks:

•  Add an interface description

•  Set the interface speed

•  Set admin status

•  Set flow control status

Public

Editing an interface 30

•  Split interface

Procedure

1.

In the navigation pane, select Interfaces.
The Interfaces page is displayed.

2.

In the Interfaces panel, select an interface and click
The Configure Interface dialog box is displayed for the selected interface. You can select a different
interface if required.

.

3.  Enter a description for the interface. For example, Guest connection.

4.  You can select one of the following values for the interface speed.

•  10-full

•  10-half

•  100-full

•  100-half

•  auto

5.  Select Up or Down for the Admin Status.

6.  Select Enable or Disable for the Flow Control Status.

7.  Select the Split checkbox to split the port into multiple interfaces.

NOTE

Splitting a port disables the selected port, clears all port configuration, and
splits the port into multiple interfaces. The split interfaces are not available
until you reboot the switch or the module. For example, select the 40 Gb/
s port, and select the Split checkbox to split the port into four 10 Gb/s
interfaces.

8.  Click Update.

VLANs page

Public

VLANs page 31

LAGs page

The LAGs page displays a list of LAGs. Details on each LAG include: Name of the LAG, whether the admin
status is up or down, LAG bond status, whether the LAG is a multi-chassis LAG, a list of down interfaces, a
list of up interfaces, a list of VLANs, whether trunk allowed or not allowed, and a list of IP addresses.

Figure 1. LAGs page

Figure 2. LAGs Page

Public

LAGs page 32

Links in the Interfaces and VLANs columns allow you to drill down to the respective Interfaces or VLANs
pages, auto-selecting the appropriate resource. Selecting a row in the LAGs list displays more information on
the LAG. Details include Interfaces and LAG statistics.

You can add and delete static LAGs. You can edit a LAG and add or delete ports, and set the admin status.

Use the Show/Hide Column Filters button or Column Settings button to customize the table display.

Users page

The Users page displays user names and roles. You can also add or delete a user, or change a password for
the logged in user. A user with the administrator role can access this page.

Figure 1. Users page showing an administrator user entry

Public

Users page 33

Figure 2. Users page showing an administrator user entry

VSX page

If Virtual Switching Extension (VSX) is configured, the VSX page shows configuration and status information
about the VSX:

Public

VSX page 34

•  The switch configurations include VSX LAGs that span both switches.

•  Each switch has a user-configured role: either  primary  or  secondary . If configuration

synchronization is enabled, supported configuration changes performed on the primary switch are
performed on the secondary switch automatically.

•  The switches synchronize their configuration and state information over a user-configured interswitch

link (ISL).
The ISL is used for both datapath traffic forwarding and control path VSX protocol exchange.

•  A separate IP-based keepalive mechanism completes the control plane by providing an integrity check if

there is an ISL failure.

For more information about VSX, see the Virtual Technologies Guide.

Figure 1. VSX page

Summary panel

The Summary panel shows state information about the switch to which you are connected, including
whether the switch role is primary or secondary and state information about the connections to the peer
switch.

The IP address of the switch to which you are connected is shown in the top banner of the Web UI.

Info panel

The Info panel provides configuration information about the VSX switches, including the following:

•  The system ID of this switch and of the peer switch.

•  The ISL port of this switch and of the peer switch. If the ISL is a LAG, the name of the LAG is shown.

Public

VSX page 35

•  The host name and IP address of the peer switch.

•  Whether configuration synchronization between switches is enabled.

•  The names of the VSX LAGs.

Keep Alive Information panel

The Keep Alive Information panel shows information and status information about the keep alive
communications from the keep alive source IP address to the IP address of this switch (shown in the
top banner of the Web UI) and IP address of the peer switch (shown under Peer IP in the panel).

Control Traffic Statistics panel

The Control Traffic Statistics panel shows information about control plane traffic between the primary
and secondary VSX switches. The traffic shown in this panel is related to the coordination of information
between VSX switches when the switches are acting as a single routing device.

Management & Assurance Statistics panel

The Management & Assurance Statistics panel shows information about management traffic between the
primary and secondary VSX switches. Examples of management traffic between VSX switches include the
following:

•  Traffic related to synchronizing switch configuration data from the primary switch to the secondary

switch.

•  Traffic related to executing  show  commands that include the  vsx-peer  option to get data from

the peer switch.

•  Traffic related to Network Analytics Engine monitors or REST API calls that query the peer switch.

Environmental page

From the Environmental page you can view:

•  Power supply failures or warnings.

•  Fans' details such as status, RPMs, speed, and direction.

•  Thermals' details such as status, fan state, location, temperature, maximum, and minimum values.

Figure 1. Environmental page

Public

Environmental page 36

Figure 2. Environmental page

Log page

Public

Log page 37

From the Log page you can view a list of event log entries. Each log entry displayed includes the following:
Time, Severity (Critical, Warning, Info), ID, and Message. If you set filtering on the table the custom changes
apply only to the data on the current page.

NOTE

The WebUI reflects only those logging filters configured through the WebUI.
Filters configured via the command-line interface will not be applied to WebUI
logs.

The Log page shows event log messages only. Accounting log messages must be accessed through the
REST API or the CLI.

Figure 1. Log page

•  You can select an entry from the list of log entries to view more information in the details pane.

•  Click Export to download the current log query as a CSV file.

•  To run a new server-side query, click Query. A Query dialog box is displayed. You can customize the

query by Range, Severity, and identifier. Click Run to run the new query.

Figure 2. Query page

Public

Log page 38

The following table shows how Syslog RFC 3164 severity levels are mapped to Web UI severity levels.

Web UI severity

Critical

Warning

Info

Syslog severity

0 Emergency: system is unusable

1 Alert: action must be taken immediately

2 Critical: critical conditions

3 Error: error conditions

4 Warning: warning conditions

5 Notice: normal but significant condition

6 Informational: informational messages

Public

Log page 39

Web UI severity

Syslog severity
7 Debug: debug‐level messages

Name Server page

From the Name Server page, you can view the current primary and secondary name server addresses.

To configure the addresses, enter a Primary IP Address and Secondary IP Address, and click Apply.
Primary and Secondary Name Server addresses can only be set when there is a static IP address on the
management interface. If it has a DHCP address, the values passed from the DHCP server are used.

Click Reset to undo any change that are not applied.

Figure 1. Name Server page

SNMP page

The SNMP page displays the SNMP community and trap receiver details.

Figure 1. SNMP Page

Public

Name Server page 40

SNMPv3 Users panel

The SNMPv3 Users panel lists the SNMPv3 users added to the switch. You can add, edit, and delete
SNMPv3 user details.

SNMP Communities panel

The SNMP Communities panel lists the communities added in the switch. You can add and delete SNMP
community names.

Trap Receivers panel

The Trap Receivers panel shows the details of the trap receivers and SNMP informs added in the switch.
You can add and delete trap receivers and SNMP informs.

Session page

The Session page allows a way to configure values for the HTTPS server.

Public

Session page 41

HTTPS Server Session panel

The HTTPS Sever Session panel allows the user to configure the max sessions per user and session idle
timeout for the HTTPS server.

The APPLY button is used to configure the values provided by the user. The LOAD DEFAULT button
configures default values for session parameters. The APPLY button is disabled on providing invalid values
for the session parameters. On successful configuration of session parameters values, the following dialogue
is displayed:

Max sessions

The functionality of maintaining the maximum number of sessions per user is handled by the REST module
in the switch. The Web UI only provides configuration support. On attempting to establish a session beyond
the configured max number of sessions, the following error dialogue is displayed:

Public

Session page 42

Idle timer

Web UI sessions are maintained by REST module and these Web UI sessions inactivity is monitored by REST
deamon based on the RESTAPI request activity from each session. In Web UI implementation, many pages
use periodic data polling (like every 10 secs) using the REST API to provide dynamic update of data. This
causes the Web UI session to never timeout from the REST daemon perspective, because the REST API
does not distinguish between the active polling API and the user-triggered REST API. Therefore, the REST
Daemon will never timeout Web UI sessions even if the user is inactive. Because of this, the user activity
idle timer is must be maintained by the Web UI and once the activity timer times out, the Web UI will
automatically log out of the session.

A 10 second periodic timer is started on launching the Web UI. On timeout of this timer, a global
currSessTmr counter is incremented. This counter is checked against the configured idle timer session
timeout value. When the currSessTmr reaches the idle timeout timer value, a logout event is triggered, and
the current session is terminated.

The idle timeout counter currSessTmr is reset on any user activity which is detected using the
addEventListener function.

The configurable value for idle Timer is 0 to 480 (in minutes), where 0 disables the timer. On configuration
of a value of zero, the 10 second timer is stopped and on any non-zero value, the timer is restarted.

When there is no user activity in the Web UI for the configured session idle timeout, the session is logged off
and the following dialogue is displayed. The user needs to login again to access Web UI.

Public

Session page 43

A warning message is displayed when the idle session timer has one-minute before expiring.

The user can reset the timer and continue the session by clicking the RESET button. If not reset, the session
expires in one minute from the warning message display.

Config Mgmt page

From the Config Mgmt page you can:

•  Upload or download configurations to or from the Running or Startup configuration.

•  Create a configuration checkpoint.

•  Download running, startup, and checkpoint configurations

•  Copy from or to various configurations: running to startup, running to checkpoint, checkpoint to startup,

checkpoint to running, startup to running.

Uploads and downloads are performed through the REST interface.

Figure 1. Config Mgmt (configuration management) page

Public

Config Mgmt page 44

Figure 2. Config Mgmt (configuration management) page

Public

Config Mgmt page 45

Firmware Update page

From the Firmware Update page, you can see the current, primary, and secondary firmware versions and you
can upload firmware files.

Figure 1. Firmware update showing image versions

Uploads are performed through the REST interface.

NOTE

After the update starts it cannot be cancelled, however users can access other
functionalities by opening a new browser tab for the same session.

Prior to updating, a message is displayed: Are you sure you want to update the primary/secondary
image?

After the firmware upload is completed, a new dialog box is displayed that contains the message: New
firmware has been successfully uploaded. Verifying and writing system firmware...

You may need to press Reboot on the page or select the Reboot item in the top right System menu for the
image to take effect.

Selecting Reboot reboots the switch.

NOTE
After you select Reboot, you cannot cancel the request.

After selecting Reboot, you will be prompted to verify that you want to reboot the switch and to choose an
image to use when rebooting.

Figure 2. Reboot confirmation dialog box

Public

Firmware Update page 46

Firmware site distribution

Firmware site distribution is a feature in which a switch can upgrade its firmware by downloading image from
another switch in the network. It enables switches to download firmware from switch or remote server rather
than all switches requesting multiple downloads from a remote location. This reduces the traffic to external
networks, reduces network overhead, and speeds up the upgrade process.

The WebUI provides support for this feature through the Firmware Update page under the System group
in the Navigation pane. Switches may download their firmware from a remote switch or from any HTTP
server.

Selecting the Download from Firmware Distribution Server reveals additional options:

•  Remote Switch

•  Remote Server

Figure 3. Enabling the Firmware Distribution Server feature

Public

Firmware Update page 47

In the event that downloading firmware fails, the WebUI will display an error message sent by the REST
module.

NOTE

Only two switch clients can simultaneously install firmware from a remote switch.
If the remote switch receives a request from a third client while currently serving
two others, then firmware installation will fail for the 3rd client.

Figure 4. Firmware download error message

Downloading firmware from a remote switch

The following values are required to download firmware from a remote switch:

Value

Switch IP/host name

Image location

VRF

Description

IP address or hostname of the switch which has the f
irmware to be downloaded in its image bank.

Image bank in the remote switch. Firmware from eith
er the primary or secondary bank can be downloade
d.

Mgmt, Default, or any user‐created VRF to reach th
e remote switch.

Figure 5. Example of downloading an image from a remote switch

Public

Firmware Update page 48

In the example shown above the firmware is downloaded from primary bank of switch 20.0.0.1 using default
VRF.

When trying to download firmware from another switch, the WebUI provides a warning message to user to
ensure the configuration is done on the remote switch.

Figure 6. WebUI warning before downloading firmware from a remote switch

Downloading firmware from a remote HTTP server

The following values are required to download firmware from a remote HTTP server:

Value

Image location

Description

The complete URL of the image location in the re
mote HTTP server, for example, http://www.examp
le.com/images/FL_10_06_0100AM.swi?merchantId=
ACTIVATE_DROPBOX

VRF

VRF to reach the HTTP server.

Public

Firmware Update page 49

Figure 7. Example of downloading an image from a remote server

NOTE

To upgrade using firmware from another switch, the Firmware Site Distribution
feature must be enabled in the remote switch. Please refer to the Firmware Mgmt
page section for additional information.

Firmware Mgmt page

The Firmware Mgmt page contains the mechanism to enable the Firmware Site Distribution feature. This
feature must enabled on a remote switch in order to allow it to share its firmware image(s) with other
switches in your network and can be enable either via CLI or WebUI.

Enabling firmware site distribution using the CLI

Firmware site distribution can be enabled and verifies in the CLI using the following commands:

switch(config)# show https-server rest firmware-site-distribution

Firmware Site Distribution Configuration

----------------------------

 Status        : disabled

switch(config)# https-server rest firmware-site-distribution

switch(config)# show https-server rest firmware-site-distribution

Firmware Site Distribution Configuration

----------------------------

 Status        : enabled

Public

Firmware Mgmt page 50

Enabling firmware site distribution using the WebUI

The Firmware Mgmt page also allows you to enable or disable the firmware site distribution feature and can
be accessed through the following path: Navigation pane > System > Firmware Mgmt.

Figure 1. Enabling firmware site distribution using the WebUI

When the image has been successfully downloaded the system will display a confirmation message.

Figure 2. WebUI firmware system update confirmation message

Public

Firmware Mgmt page 51

Ping page

From the Ping page, you can run the ping command to the specified target hostname and view the output.
Click Ping to run the command or Cancel.

Figure 1. Ping page

You can set the following parameters on the ping command:

•  Repetition: Specify the number of pings sent (1-10,000).

•

Interval: Specify the interval between successive ping requests (1-60).

•  Timeout: Specify the Ping Timeout in seconds (1-60).

•  Datagram-Size: Specify the size of ping datagram (100 - 65,399).

•  Type of Service (TOS): Specify IP TOS to be used in ping request (0 - 255).

•  Data Fill: Specify the ping packet data pattern in hexadecimal digits.

•

IP-Option: Specify an IP option to be used in ping packet.

•  Use Management Interface: Specify the use of the management interface (check box).

Click Reset to reset options to the default.

Public

Ping page 52

Traceroute page

From the Traceroute page, you can run the traceroute command to the specified target hostname and view
the output. Click Traceroute to run the command.

Figure 1. Traceroute page

You can set the following parameters on the  traceroute  command:

•  Destination Port: Specify the destination port (1 - 34000).

•  timeout: Specify the traceroute timeout in seconds (1-60).

•  maxttl: Specify the maximum number of hops to reach the destination (1 - 255).

•  minttl: Specify minimum number of hops to reach the destination (1 - 255).

•  probes: Specify the number of probe packets per hop to send (1 - 5).

•  Loose src Route: Specify routing information to be used by the gateways.

•  Use Management Interface: Specify the use of the management interface (check box).

Click Reset to reset options to the default.

Public

Traceroute page 53

Show Tech page

From the Show Tech page, you can run the showtech command. Administrator rights are required.

Figure 1. Show Tech page

Click Generate, to start generating the report on the switch.

Click Export to download the  showtech  file locally. The exported file is in simple text format, the same
as with the CLI output.

Spanning Tree page

The Spanning Tree page displays the spanning tree configuration details of the switch. The Spanning Tree
Protocol (STP) eliminates Layer 2 loops in networks, by selectively blocking some ports and allowing other
ports to forward traffic.

Figure 1. Spanning Tree page

Public

Show Tech page 54

Status panel

The Status panel shows information about the spanning tree configuration—whether spanning tree is
enabled or disabled and the spanning tree mode that is selected.

You can enable spanning tree with Multiple Spanning Tree (MST) or Rapid Per-Vlan Spanning Tree (Rapid
PVST) mode.

In the Multiple Spanning Tree mode, the Spanning Tree page displays additional details like the assigned
ports, MSTP configuration details, the number of times the topology was changed, and the time since the
topology changed.

In the Rapid Per-Vlan Spanning Tree mode, the Spanning Tree page displays only the details of the assigned
ports. The Rapid Per-Vlan Spanning Tree mode enables a separate spanning tree in each VLAN, including
the default VLAN.

Assigned Ports panel

The Assigned Ports panel shows the details of the ports based on the ports added in the spanning tree
configuration. For example, if some ports are set as BPDU Filter or Guard Ports, then the port numbers are
displayed in the member/slot/port notation.

Inconsistent Ports panel

The Inconsistent Ports panel shows the details of the ports that are in an inconsistent STP state.
Inconsistent state occurs when the ports on both ends of a point-to-point link are untagged members
of different VLANs or when the ports have different configurations on both end. For example, if one end is
configured as trunk and the other end is configured as an access port.

MSTP Configuration Details panel

The MSTP Configuration Details panel shows the name of the region, the revision number, and a digest of
the MST VLANs-to-instance mapping from the switch configuration.

Topology panel

The Topology panel shows the number of times the topology changed.

Topology Change Time panel

The Topology Change Time panel shows the time since the topology changed.

Connected Clients page

The Connected Clients page displays details of the devices connected to the switch.

Figure 1. Connected Devices page

Public

Connected Clients page 55

Connected Clients panel

The Connected Clients panel displays the device ID, IP address, device name, local and remote ports,
capability, TTL time, parent device, and source details.

PKI page

Public Key Infrastructure (PKI) capability on the switch provides digital certificates to authenticate network
entities. This page enables you to configure and manage digital certificates on the switch. The switch uses
certificates to validate SSH clients when acting as an SSH server and when communicating with syslog
servers while TLS encryption is used.

Each entity in the PKI has their identity validated by a certificate authority (CA). The CA issues a digital
certificate as part of enrolling each entity into the PKI. This digital certificate is used by the replying
parties (for example, network connection peers) to set up secure communication. Based on the information
present in the certificate of the sender, the receiving entity can validate the authenticity of the sender and
subsequently establish a secure communication channel. For more information about PKI, see the AOS-CX
Security Guide.

Figure 1. WebUI Overview Dashboard

Public

PKI page 56

EST Profiles panel

The EST Profiles panel displays the details of the EST profiles added to the switch. Enrollment over Secure
Transport (EST) enhances the switch PKI infrastructure with a simpler, scalable, and more secure method of
certificate provisioning, re-enrollment, and renewal.

TA Profiles panel

The TA Profiles panel displays information and status of TA profiles added to the switch. A Trust Anchor
(TA) defines certificate-specific operations, such as enrollment and validations. Each TA profile stores the
certificate for a trusted CA.

Certificates panel

The Certificates panel displays details about the digital certificates that can be used for applications in
the switch. Certificates help secure digital transactions by enabling the end parties to validate each other's
identity. Digital certificates are issued by a CA and are composed of an encoded string of characters (usually
stored in a file).

Associated Application Details panel

The Associated Application Details panel displays the features (applications) on the switch to which you
can associate certificates. The panel also displays the associated certificate name and status. By default, all
features are associated with the default, self-signed certificate local-cert. This certificate is created by the
switch the first time it starts.

Public

PKI page 57

Support File page

Supported only on the 8100, 8320, 8325/8325H/8325P, 8360, 9300/9300S, 10000 and 10040 Switch
Series.

From the Support file page, you can create support files that can be used to troubleshoot issues in the
switch. The support files contain the following information:

•  Running configuration

•  Events

•  Errors

•  Confidential information, such as usernames and passwords (in encrypted format)

•  Support logs

•  Previous boot logs

•  Hardware information

•  Software build version details

•  Debugging information

Figure 1. Support File Page

Support File panel

The Support File panel displays the details of the support files created on the switch. Administrator rights
are required.

The following information is displayed:

Public

Support File page 58

•  Name: Name of the support file.

•  Type: Type of the support file. By default, the value is All and no other type of support file can be

generated.

•  Status: Status of the support file. The following options are supported:

◦  Requested: Appears immediately after a support file is created.

◦

In Progress: Appears when the support file is being generated.

◦  Generated: Appears when the support file is successfully generated.

You can download the support file only when the status displays Generated.

◦  Failed: Appears when the support file fails to generate with a specific error message.

•  Progress(%): Progress of support file generation (in percentage). This field displays 100% when the

support file is successfully generated.

•  Size(KBs): Size of the support file in kilobytes. The size is displayed only after the support file is

successfully generated.

•  Error: Error message when the support file fails to be generated. The following error messages are

supported:

◦  Collection is aborted

◦  File is not available in local file system

◦  Collection process terminated

◦  Collection process exceeded max collection time

◦

◦

Insufficient storage space available storing the collection

Insufficient RAM memory available for collection

◦  Collection already in progress in another session

◦  Collection is failed due to unexpected error

NOTE
Support files created before a switch reboot or upgrade will not be accessible to
users via HPE Aruba Networking Central.

Public

Support File page 59

Finding alert details using the Web UI

You can view details on the alerts displayed in the Web UI.

Prerequisites

You must be logged in to the Web UI.

Procedure

1.  Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, the Alerts panel lists the alerts for all agents.

Figure 1. Alerts panel on Analytics Dashboard

3.  To see the alerts for a specific agent, in the Analytics Dashboard Agents panel or Alerts panel, select an

agent.

4.

In the Agent Details page, the agent alerts are listed in the Alerts panel.

Figure 2. Agent Details page

Public

Finding alert details using the Web UI 60

5.

In the Alerts panel, select an alert and click Details to view the Alert Details dialog box. To close the
dialog box, click Close.
You can also access alert details directly from the Analytics Dashboard by selecting an alert in the Alerts
panel and clicking Details.

6.  The Action Result(s) in Alert Details dialog box might include additional details about actions and links

to the action result output.

Figure 3. Alert Details dialog box

Public

Finding alert details using the Web UI 61

To view the Action Result Output dialog box for an action, click the Output link.

Figure 4. Action Result dialog box

Public

Finding alert details using the Web UI 62

Working with the network analytics features

This section describes the steps to view agent information using the Web UI, and work with an Analytics
time series graph.

NOTE

For more information on the Network Analytics Engine, including agents and
scripts, see the Network Analytics Engine Guide.

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Subtopics

Accessing HPE Aruba Networking Support
Accessing Updates
Warranty Information

Public

Working with the network analytics features 63

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

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

•  Third-party products or components

Other useful sites

Other websites that can be used to find information:

Public

Accessing HPE Aruba Networking Support 64

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

https://networkingsupport.hpe./notifications/subscriptions (requires an active HPE Aruba Networking
Support Portal account to manage subscriptions). Security notices are viewable without an HPE Aruba
Networking Support Portal account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-services/
product-warranties/.

Public

Accessing Updates 65

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

Regulatory Information 66

