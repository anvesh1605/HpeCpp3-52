AOS-CX 10.17.xxxx Introduction to the Web UI Guide (4100i, 5xxx,
6xxx Switch Series)

Published: February 2026

AOS-CX 10.17.xxxx Introduction to the Web UI Guide (4100i, 5xxx,
6xxx Switch Series)

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

Identifying modular switch components.........................................................................................................................10

Accessing the AOS-CX Web UI.......................................................................................................................................................... 10

AOS-CX Web UI overview..................................................................................................................................................................... 14

AOS-CX Web UI framework.................................................................................................................................................... 14

Customizing the Web UI........................................................................................................................................................... 17

Customizing page layouts...........................................................................................................................................17

Adding a custom panel to the Overview page................................................................................................18

Customizing tables..........................................................................................................................................................21

Using Show/Hide filters in tables........................................................................................................................... 22

AOS-CX Web UI pages............................................................................................................................................................................23

Navigation pane.............................................................................................................................................................................24

Overview page................................................................................................................................................................................27

Analytics Dashboard...................................................................................................................................................................31

Interfaces page...............................................................................................................................................................................33

Editing an interface.........................................................................................................................................................36

VLANs page.....................................................................................................................................................................................37

LAGs page.........................................................................................................................................................................................38

Users page........................................................................................................................................................................................ 39

PoE page............................................................................................................................................................................................40

VSF page............................................................................................................................................................................................42

VSX page........................................................................................................................................................................................... 43

Environmental page.................................................................................................................................................................... 45

Log page............................................................................................................................................................................................ 46

Name Server page........................................................................................................................................................................49

SNMP page.......................................................................................................................................................................................49

Session page....................................................................................................................................................................................50

Config Mgmt page........................................................................................................................................................................53

Firmware Update page.............................................................................................................................................................. 55

Public

Table of contents 4

Firmware Mgmt page................................................................................................................................................................. 59

Ping page...........................................................................................................................................................................................61

Traceroute page.............................................................................................................................................................................62

Show Tech page.............................................................................................................................................................................63

Spanning Tree page.................................................................................................................................................................... 63

Connected Clients page............................................................................................................................................................ 64

Connected Devices Configuration page.......................................................................................................................... 65

PKI page............................................................................................................................................................................................. 66

Port Security page........................................................................................................................................................................68

Support File page..........................................................................................................................................................................68

Finding alert details using the Web UI.......................................................................................................................................... 70

Working with the network analytics features............................................................................................................................74

Support and Other Resources............................................................................................................................................................74

Accessing HPE Aruba Networking Support..................................................................................................................75

Accessing Updates.......................................................................................................................................................................76

Warranty Information................................................................................................................................................................. 76

Regulatory Information............................................................................................................................................................. 77

Documentation Feedback........................................................................................................................................................77

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

•  HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

•  HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A,

S4R20A, S4R21A, S4R22A, S4R23A, S4R24A, S4R25A, S4R26A, S4R27A, S4R28, S4R29A)

•  HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A,
S0U61A, S0U62A, S0U66A, S0U68A)

•  HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

•  HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A,
R8Q68A, R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A,
JL724B, JL725B, JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,
S0M87A, S0M88A, S0M89A, S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

•  HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A,

JL664A, JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A,
S0X44A, S3L75A, S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A, S4P47A,
S4P48A)

•  HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,

R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

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

On the HPE Aruba Networking 4100i Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

•  member: Always 1. VSF is not supported on this switch.

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

Public

Identifying switch ports and interfaces 9

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/1 and 1/2.

◦  Line modules are on the front of the switch starting in slot 1/3.

•  port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

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

Accessing the AOS-CX Web UI

Public

Identifying modular switch components 10

By default, the 5420, 6200, 6300, and 6400 switches have the HTTPS server enabled on the mgmt and  d
efault  VRF. The 4100i, 6000, and 6100 switches have the HTTPS server enabled on the default VRF.
On all switches, the REST API access mode is set to read-write. You must configure a static IP or use the
IP address on the management port (5420, 6200, 6300, 6400 switches only; the 4100i, 6000, and 6100
switches do not have a management port) to access the Web UI.

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

NOTE
The 5420 and 6200 switches support two VRFs. One mgmt VRF and one default
VRF.

NOTE
The 4100i switch only include the default VRF; there is no mgmt VRF.

NOTE

•  Certificate-based authentication is not supported on 6000 and 6100 Switch

Series.

•  The 6000 and 6100 switches only include the default VRF; there is no

mgmt VRF.

To use the Web UI to make configuration changes—such as adding users—the following must be true:

•  The system that you are using to access the Web UI must be on the same network and the subnet as the

switch.

Public

Accessing the AOS-CX Web UI 11

•  Proxy must be disabled on browsers through which you are accessing the Web UI.

•  You must have a valid login user name and password or a valid certificate.

•  The user name you use to log in must have administrator rights.

For information about configuring the management interface and REST API access, see the AOS-CX
Fundamentals Guide .

For information about configuring and managing the certificates, see the AOS-CX Security Guide.

Procedure

1.  Start a supported web browser and enter the IP address of the management port in the address bar. Use

HTTPS.
For example:

https://192.0.2.5 or https://[1001::2]

You must use a supported browser, such as Chrome, Firefox, Edge, or Safari. For details on supported
browser versions, see the Release Notes for the version of AOS-CX you are using.

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

Accessing the AOS-CX Web UI 12

Cause

REST API access is not enabled on the VRF that corresponds to the access port you are using. For example,
you are attempting to access the REST API or Web UI from the management (OOBM) port, and access is not
enabled on the  mgmt  VRF. By default, https-server is enabled on the  mgmt  VRF for the 6300 and 6400
switches. The 4100i, 6000, and 6100 switches do not have a  mgmt  VRF, so https-server is enabled on the
default  VRF.

Action

Use the https-server vrf command to enable REST API access on the specified VRF.

For example:

switch(config)# https-server vrf mgmt

Or, on the 4100i, 6000, or 6100 switch:

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

3.

If the session cookie is lost and it is not possible to log out of the session, then wait for the session idle
time limit to expire.
When the session idle timeout expires, the session is terminated automatically.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time limit
to expire, you can stop all HTTPS sessions using the https-server session close all command.
This command stops and starts the hpe-restd service, so using this command affects all existing REST
sessions, Web UI sessions, and real-time notification subscriptions.

Public

Accessing the AOS-CX Web UI 13

"Not Authorized" is displayed instead of page content

Symptom

The message "Not Authorized" is displayed in the details pane of a Web UI page.

Cause

You have logged in as a user that is not authorized to view this page.

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

•  View and configure Network Analytics Engine agents, scripts, and alerts. Not applicable to the 4100i,

6000, or 6100 switches, which do not support the Network Analytics Engine.

•  Modify some aspects of the switch configuration.

•  Run diagnostics including the  ping ,  traceroute , and  show tech  commands.

•  Upgrade or downgrade the image build on the device.

•  Reboot the switch.

Subtopics

AOS-CX Web UI framework
Customizing the Web UI

AOS-CX Web UI framework

Public

AOS-CX Web UI overview 14

About this task

Descriptions for (numbered) common areas, buttons, menus, and controls in the Web UI are listed after the
image.

Figure 1. Overview page with callouts

Figure 2. Overview page with callouts

Public

AOS-CX Web UI framework 15

Procedure

1.  The Show/Hide button on the left in the top banner, allows you to hide the navigation pane (slides the

pane in and out).

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

10.  The Toggle Locator LED menu in the top banner allows you to turn the switch locator LED on or off. In

the case of a stack, this menu lists all the member switches in the stack. You can turn the locator LED on
or off for each member in the stack. The icon changes to , when the switch locator LED is turned off for
all switches.

11.  The System menu in the top banner includes the following:

Public

AOS-CX Web UI framework 16

•  Save Config: Save configuration changes

•  Reboot: Reboot the switch to either primary or secondary image.

•  v10.04 API: Access v10.04 REST APIs that you can use to read and/or write to the switch.

12.  The Help icon provides a link to AOS-CXuser documentation.

13.  The Show/Hide button on the right side of the top banner displays the Log Summary pane (slides the
pane in and out). The Log Summary provides a summary of the most recent critical level log entries in
the last X seconds. It also shows counts of the number of critical, warning, and info log entries arriving in
the last X seconds.

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

Public

Customizing the Web UI 17

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

Public

Adding a custom panel to the Overview page 18

Prerequisites

You must be logged in to the Web UI.

Procedure

1.  Select an empty panel in the Overview page and click the + plus button.

Figure 1. Empty panel with + (plus) button

2.  The Set Indicator dialog box is displayed. Select the interface you want to set an indicator for. Use the

Show/Hide Column Filters button to show a specific interface in the list. Click Interface: <X/X/X> to set
an indicator or Cancel to exit.

Figure 2. Set Indicator dialog with example content

Public

Adding a custom panel to the Overview page 19

3.  A new panel showing an indicator for the interface you selected is added to the Overview page.

Figure 3. Panel showing a selected interface

Public

Adding a custom panel to the Overview page 20

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

Figure 1. List of column headings with check marks

Public

Customizing tables 21

2.  To resize a column drag the column separators to expand or narrow the column. Columns cannot be

reordered.

3.  View additional pages of content in the table using the table scroll bar.

Using Show/Hide filters in tables

You can use filters to display a subset of data in the table. Filtering is not persistent, so when you leave the
page, the filtering is removed.

Prerequisites

You must be logged in to the Web UI.

Public

Using Show/Hide filters in tables 22

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

AOS-CX Web UI pages 23

Descriptions of the AOS-CX Web UI pages, and workflows for using these pages.

Subtopics

Navigation pane
Overview page
Analytics Dashboard
Interfaces page
VLANs page
LAGs page
Users page
PoE page
VSF page
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
Connected Devices Configuration page
PKI page
Port Security page
Support File page

Navigation pane

Navigate the Web UI by selecting an item in the navigation pane. Information for the selected item is
displayed in a series of panels in the details pane. From the details pane, you can select links to drill down to
more detailed pages.

Use the

 Show/Hide button to show or hide the navigation pane.

In the navigation pane, expand and collapse the System, Diagnostics, or Traffic group to show or hide related
items.

Public

Navigation pane 24

The user role (operators, administrators, or auditor) determines which items in the navigation pane you can
access.

The navigation pane includes the following links to different feature pages. Click the links for more
information.

Link

Overview

Analytics Dashboard

Interfaces

VLANs

LAGs

Users

PoE

VSF

VSX

Description

Shows important information and statistics about t
he switch. Each indicator panel provides "roll‐up"
status (color and icon) of Analytics, Environmental,
System, and so on. Empty titles allow you to select a
nd save specific interfaces to monitor (packets, bytes
, utilization).

Shows the Analytics Dashboard providing informatio
n related to Network Analytics Engine agents, scripts
, alerts, and actions generated by these scripts. Not a
pplicable to the 4100i, 6000, or 6100 Switch Series.

Shows information and status for each interface. Allo
ws you to edit the interface details.

Shows information for each VLAN and the status of t
he VLANs. Allows you to add, edit, and delete VLAN
s.

Shows the information and the up or down status of
the LAGs. Allows you to add, edit, and delete Lags.

Shows user roles and names. Also allows you to add
or delete a user and change user passwords.

Administrator rights are required to access this sele
ction.

Shows information for PoE ports in the switch. Allow
s you to configure PoE for the ports.

Shows the Virtual Switching Framework (VSF) config
uration and status information. This link is displayed
for the 5420, 6200 and 6300 switches that support
VSF. Not applicable to the 4100i, 6000, or 6100 Swi
tch Series.

Shows the Virtual Switching Extension (VSX) config
uration and status information. This link is displayed
only for the 6400 switches that support VSX.

Public

Navigation pane 25

Link

System ‐ Environmental

System ‐ Log

System ‐ Name Server

System ‐ SNMP

System ‐ Config Mgmt

Description

Shows power supply failures and warnings, temperat
ures, and fan information.

Shows event log entries, event log queries, and mess
age details.

Shows primary and secondary name servers, and allo
ws you to configure addresses for name servers.

Shows the details of SNMPv3 users, SNMP communi
ties, and trap receivers. Allows you to add and delete
SNMPv3 users, SNMP community names, informs, an
d trap receivers.

Enables you to upload/download configurations to or
from the running or startup configurations.

System ‐ Firmware Update

Enables you to upload firmware files.

System ‐ Firmware Mgmt

Diagnostics ‐ Ping

Diagnostics ‐ Traceroute

Diagnostics ‐ Show Tech

Traffic ‐ Spanning Tree

Connected Device ‐ Clients

Connected Devices ‐ Configuration

Security ‐ PKI

Enables you to configure the switch to distribute fir
mware to other switches.

Enables you to run the  ping  command with variou
s options.

Enables you to run the  traceroute  command w
ith various options.

Enables you to run the  showtech  command. Ad
ministrator rights are required to run this command.

Shows the details of the Spanning Tree configuratio
n, assigned ports, and inconsistent ports. Allows you
to enable Spanning Tree with Multiple Spanning Tree
or Rapid Per‐Vlan Spanning Tree mode.

Shows the details of the devices connected to the sw
itch.

Shows the CDP, LLDP, and client tracking details of t
he devices connected to the switch. Allows you to co
nfigure the CDP, LLDP, and client tracking details at t
he switch and interface levels.

Shows the details of the TA profile, EST profile, digi
tal certificates, and associated applications in the swi
tch. Allows you to add, edit, and delete TA profile; ad

Public

Navigation pane 26

Link

Description

d, view, and delete EST profile; add, view, upload, and
delete certificates; and edit associated applications.

Shows the access port security, authorized MACs, an
d authorized client limit details. Allows you to edit th
e port security violation action for the ports.

Security ‐ Port Security

Overview page

The Overview page provides a quick view of the status of a switch. It shows easy-to-read indicators for:
Analytics agents, power supply, thermal, fans, CPU use, memory use, log entries, checkpoints, firmware,
management modules, and system information.

Custom indicator panels allow you to select specific interfaces to monitor and to add panels for those
interfaces to the Overview page.

NOTE

Ensure that both the switch and the client where the Web UI is running are set
to use NTP or to a time zone based on UTC time. Otherwise, the NAE agent
data might be incorrect or missing and the System Uptime will be incorrect. For
example, if the time on the switch is set to 2 hours ahead of the client manually,
instead of changing the time zone offset, the agent data is populated according
to the new time on the switch. If the switch time is set back to match the client
time later, the Time Series Database does not overwrite the old data. Therefore
the client Web UI shows inaccurate data.

The following image shows the Overview page of the 6100 switch series.

Public

Overview page 27

The following image shows the Overview page of the 6200 switch series.

The following image shows the Overview page of the 6300 switch series.

Figure 1. WebUI Overview Dashboard

Public

Overview page 28

The following image shows the Overview page of the 6400 switch series.

Figure 2. WebUI Overview Dashboard 6400

The following table describes the different panels displayed on the Overview page.

Panel

Analytics

Description

Shows: Total number of agents in critical, major, or m
inor status; total number of agents scripts, agents, an

Public

Overview page 29

Panel

Description

Firmware

Config

Management Modules

Log

CPU

Memory

System Info

Power Supplies

Thermal

Fans

VSF

VSX

d monitors (both enabled and disabled) compared to
the maximum number supported on the switch. For
example, 7/25 indicates that there are a total of 7 ou
t of a supported maximum of 25. Clicking the link dis
plays the Analytics Dashboard. Not applicable to the
6000 or 6100 Switch Series.

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

Shows: VSF information, including split status, topol
ogy, and health. This panel is displayed for the switc
hes that support VSF. Clicking the link displays the
VSF page.

Shows: VSX information, including inter‐switch link
(ISL) state, configuration synchronization state, and t
he role of this switch (primary or secondary). This p

Public

Overview page 30

Panel

Description

anel is displayed for the 6400 switches that support
VSX. Clicking the link displays the VSX page.

Analytics Dashboard

NOTE

The 6000 and 6100 Switch Series do not support he Network Analytics Engine,
so the there is no Analytics Dashboard in the Web UI for those switches.

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

Public

Analytics Dashboard 31

Figure 1. Analytics dashboard

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

Public

Analytics Dashboard 32

Scripts specify what the Network Analytics Engine monitors. The script also specifies various conditions and
corresponding actions when these conditions are met. Some read-only scripts are provided with the switch.
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

The following image shows the Interfaces page with the faceplate for the 6100 switch.

Public

Interfaces page 33

The following image shows the Interfaces page with the faceplate for the 6200 switch.

The following image shows the Interfaces page with the faceplate for the 6300 switch.

Public

Interfaces page 34

The following image shows the Interfaces page with the faceplate for the 6400 switch.

Links in the VLAN and LAG columns allow you to drill down to the respective VLANs or LAGs page,
auto-selecting the appropriate resource. Selecting a row in the interfaces list, displays more information on
the interface. Details include: duplex, MAC, IPv4, IPv6 address, Rx and Tx stats, packets, and more.

A graphical panel shows interface modules currently installed. Clicking an interface, selects the
corresponding row in the table. Each interface displayed in the graph will dynamically change based on
the current interface status.

Public

Interfaces page 35

Use the Show/Hide Column Filters button or Column Settings button to customize the table display. You
can edit an interface and update the interface details.

NOTE

The WebUI does not accurately display admin status or attributes for a LAG
subinterface. Use the show interface <IFNAME> . <ID> command in the
command-line interface to view details for a LAG subinterface.

Subtopics

Editing an interface

Editing an interface

Use this procedure to perform the following tasks:

•  Add an interface description

•  Set the interface speed

•  Set admin status

•  Set flow control status

•  Split interface

Procedure

1.

In the navigation pane, select Interfaces.
The Interfaces page is displayed.

2.

In the Interfaces panel, select an interface, and click
The Configure Interface dialog box is displayed for the selected interface. You can select a different
interface if required.

 .

3.  Enter a description for the interface. For example, Guest connection.

4.  You can select one of the following values for the interface speed.

•  10-full

•  10-half

•  100-full

Public

Editing an interface 36

•  100-half

•  auto

5.  Select Up or Down for the Admin Status.

6.  Select Enable or Disable for the Flow Control Status.

NOTE

Only the Web UI for 6400 (SKU: ROX45A LC) switch has an additional setting
called Split for the 40 Gb/s ports. Splitting a port disables the selected port,
clears all port configuration, and splits the port into multiple interfaces. The
split interfaces are not available until you reboot the switch or the module. For
example, select the 40 Gb/s port, and select the Split checkbox to split the
port into four 10 Gb/s interfaces.

7.  Click Update.

VLANs page

The VLANs page displays a list of VLANs configured in the switch.

Public

VLANs page 37

VLANs panel

The VLANs panel shows the details of each VLAN including the ID, Name, Status, Reason (errors such as
No member port), a list of interfaces, LAGs, tagged and untagged ports, and IP address. The IP address
column displays only an IPv4 address. IP address is blank if a VLAN interface is not created, and displays not
assigned if the VLAN interface is created, but an IPv4 address is not configured.

Links in the Interfaces and LAGs columns allow you to drill down to the respective Interfaces or LAGs pages,
auto-selecting the appropriate resource.

Interfaces panel

The Interfaces panel shows more information on the VLAN interfaces including Members, Mode, Admin
State, Link State, and the associated LAG name.

LAGs page

The LAGs page displays a list of LAGs. Details on each LAG include: Name of the LAG, whether the admin
status is up or down, LAG bond status, whether the LAG is a multi-chassis LAG, a list of down interfaces, a
list of up interfaces, a list of VLANs, whether trunk allowed or not allowed, and a list of IP addresses.

Figure 1. LAGs page

Figure 2. LAGs Page

Public

LAGs page 38

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

Users page 39

Figure 2. Users page showing an administrator user entry

PoE page

The PoE page displays the details of the PoE enabled ports in the switch. This page is displayed for all
switches that can be stacked and for switches that have PoE ports.

Public

PoE page 40

Figure 1. PoE page

PoE Status panel

The PoE Status panel displays the details by the PoE Status, Port Priority, and Power Class of the switch
ports. The PoE details are displayed only for the ports that support PoE.

The PoE Status view displays the following status of the ports in the graphical representation of the switch:

•  PoE Port: Indicates that the port is PoE enabled.

•  Up: Indicates that the interface is up.

•  Disabled: Indicates that the port is power enabled.

•  Down: Indicates that the interface is down.

Public

PoE page 41

•  Fault: Indicates that the port is faulty.

•  Power Denied: Indicates that the power is denied to the interface.

The Port Priority view displays the priority as Low, High, and Critical in the ports in the graphical
representation of the switch.

The Power Class view displays the color code for the power class in the ports in the graphical representation
of the switch.

In the case of a stack, the graphical representation displays details for all the switches in the stack.

Interfaces panel

The Interfaces panel shows the details of all PoE ports. You can edit the PoE settings and enable or disable
PoE on a port.

Interface panel

The Interface panel shows the details of the port selected in the Interfaces pane.

VSF page

The VSF page displays the topology, link, and member details of the switches in a stack. This page is
displayed only for all 6200 and 6300 switches that are VSF stacking capable.

Figure 1. VSF page

Public

VSF page 42

Summary panel

The Summary panel shows the topology, split status, split detection method, and health status of the switch
in the stack.

Member Info panel

The Member Info panel shows the MAC address, product code, model, status (Conductor or member), serial
number, and VSF link details of the switch.

Topology panel

The Topology panel lists the member switches and the Conductor switch with the MAC address, product
code, and status (Conductor or member).

Links panel

The Links panel shows the link state, peer member, peer link, and interfaces details of the switch selected in
the Topology pane.

VSX page

If Virtual Switching Extension (VSX) is configured, the VSX page (displayed only for the 5420 and 6400
switches) shows configuration and status information about the VSX:

•  The switch configurations include VSX LAGs that span both switches.

•  Each switch has a user-configured role: either  primary  or  secondary . If configuration

synchronization is enabled, supported configuration changes performed on the primary switch are
performed on the secondary switch automatically.

•  The switches synchronize their configuration and state information over a user-configured inter-switch

link (ISL).
The ISL is used for both datapath traffic forwarding and control path VSX protocol exchange.

•  A separate IP-based keepalive mechanism completes the control plane by providing an integrity check if

there is an ISL failure.

For more information about VSX, see the Virtual Technologies Guide.

Figure 1. VSX page

Public

VSX page 43

Summary panel

The Summary panel shows state information about the switch to which you are connected, including
whether the switch role is primary or secondary and state information about the connections to the peer
switch.

The IP address of the switch to which you are connected is shown in the top banner of the Web UI.

Info panel

The Info panel provides configuration information about the VSX switches, including the following:

•  The system ID of this switch and of the peer switch.

•  The ISL port of this switch and of the peer switch. If the ISL is a LAG, the name of the LAG is shown.

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

Public

VSX page 44

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

Figure 2. Environmental page

Public

Environmental page 45

Log page

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

Public

Log page 46

•  You can select an entry from the list of log entries to view more information in the details pane.

•  Click Export to download the current log query as a CSV file.

•  To run a new server-side query, click Query. A Query dialog box is displayed. You can customize the

query by Range, Severity, and identifier. Click Run to run the new query.

Figure 2. Query page

Public

Log page 47

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

Log page 48

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

Name Server page 49

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

Session page 50

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

Session page 51

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

Session page 52

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

Config Mgmt page 53

Figure 2. Config Mgmt (configuration management) page

Public

Config Mgmt page 54

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

Firmware Update page 55

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

Firmware Update page 56

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

Firmware Update page 57

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

Firmware Update page 58

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

Firmware Mgmt page 59

Enabling firmware site distribution using the WebUI

The Firmware Mgmt page also allows you to enable or disable the firmware site distribution feature and can
be accessed through the following path: Navigation pane > System > Firmware Mgmt.

Figure 1. Enabling firmware site distribution using the WebUI

When the image has been successfully downloaded the system will display a confirmation message.

Figure 2. WebUI firmware system update confirmation message

Public

Firmware Mgmt page 60

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

Ping page 61

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

Traceroute page 62

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

Show Tech page 63

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

Connected Clients page 64

Connected Clients panel

The Connected Clients panel displays the device ID, IP address, device name, local and remote ports,
capability, TTL time, parent device, and source details.

Connected Devices Configuration page

The Connected Devices Configuration page shows whether Cisco Discovery Protocol (CDP), Link Layer
Discovery Protocol (LLDP), and client tracking are enabled or disabled at the switch and interface level. You
can configure these settings to discover and share information about the connected network devices at the
switch and interface level.

Figure 1. Connected Devices page

Public

Connected Devices Configuration page 65

Status panel

The Status panel displays the status of CDP, LLDP, client tracking, and client tracking probe at the switch
level. You can edit and change the configuration.

Interfaces panel

The Interfaces panel displays the port name, CDP status, LLDP type, client tracking status, client tracking
interval, and client tracking limit details for each active interface. You can edit and change the configuration.

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

PKI page 66

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

PKI page 67

Port Security page

The Port Security page displays the access port security details, authorized MACs, and authorized client limit
details. The page also allows you to edit the port security violation action for the ports.

Figure 1. WebUI Overview Dashboard

Access Ports panel

The Access Ports panel lists the ports with the port security details. The port security checkbox is selected
for the ports that have port security enabled.

Authorized MACs panel

The Authorized MACs panel displays the static and dynamic MAC addresses authorized on the switch for
the selected port. If you configure static MAC addresses on a port, the number of static MAC addresses
configured is displayed in the Static MAC column in the Access Ports panel.

Authorized Client Limit panel

The Authorized Client Limit panel displays the maximum number of authenticated client sessions allowed
on the selected port.

Support File page

Supported only on the 4100i, 6000, and 6100 Switch Series.

Public

Port Security page 68

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

•  Name: Name of the support file.

•  Type: Type of the support file. By default, the value is All and no other type of support file can be

generated.

•  Status: Status of the support file. The following options are supported:

Public

Support File page 69

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

Finding alert details using the Web UI

NOTE
This chapter is not applicable to the 6000 or 6100 Switch Series, which do not
support the Network Analytics Engine.

Public

Finding alert details using the Web UI 70

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

Finding alert details using the Web UI 71

5.

In the Alerts panel, select an alert and click Details to view the Alert Details dialog box. To close the
dialog box, click Close.
You can also access alert details directly from the Analytics Dashboard by selecting an alert in the Alerts
panel and clicking Details.

6.  The Action Result(s) in Alert Details dialog box might include additional details about actions and links

to the action result output.

Figure 3. Alert Details dialog box

Public

Finding alert details using the Web UI 72

To view the Action Result Output dialog box for an action, click the Output link.

Figure 4. Action Result dialog box

Public

Finding alert details using the Web UI 73

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

Working with the network analytics features 74

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

Accessing HPE Aruba Networking Support 75

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

Accessing Updates 76

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

Regulatory Information 77

