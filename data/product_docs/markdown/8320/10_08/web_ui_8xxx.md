AOS-CX 10.08 Web UI Guide

8320, 8325, 8360, 8400 Switch Series

Published: August 2021
Edition: 1

Copyright Information

© Copyright 2021 Hewlett Packard Enterprise Development LP.

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
| Contents                            |                                                |               | 3   |
| ----------------------------------- | ---------------------------------------------- | ------------- | --- |
| About                               | this document                                  |               | 5   |
| Applicableproducts                  |                                                |               | 5   |
| Latestversionavailableonline        |                                                |               | 5   |
| Commandsyntaxnotationconventions    |                                                |               | 5   |
| Abouttheexamples                    |                                                |               | 6   |
| Identifyingswitchportsandinterfaces |                                                |               | 6   |
| Identifyingmodularswitchcomponents  |                                                |               | 7   |
| Accessing                           | the                                            | AOS-CX Web UI | 8   |
| TroubleshootingWebUIaccessissues    |                                                |               | 8   |
|                                     | HTTP404errorwhenaccessingtheswitchURL          |               | 8   |
|                                     | HTTP401error"Loginfailed:sessionlimitreached"  |               | 9   |
|                                     | "NotAuthorized"isdisplayedinsteadofpagecontent |               | 9   |
| AOS-CX                              | Web                                            | UI overview   | 11  |
| AOS-CXWebUIframework                |                                                |               | 11  |
| CustomizingtheWebUI                 |                                                |               | 12  |
|                                     | Customizingpagelayouts                         |               | 12  |
|                                     | AddingacustompaneltotheOverviewpage            |               | 13  |
|                                     | Customizingtables                              |               | 14  |
|                                     | UsingShow/Hidefiltersintables                  |               | 15  |
| AOS-CX                              | Web                                            | UI pages      | 17  |
| Navigationpane                      |                                                |               | 17  |
| Overviewpage                        |                                                |               | 18  |
| AnalyticsDashboard                  |                                                |               | 20  |
| Interfacespage                      |                                                |               | 21  |
|                                     | Editinganinterface                             |               | 22  |
| VLANspage                           |                                                |               | 23  |
|                                     | AddinganddeletingaVLAN                         |               | 23  |
|                                     | EditingaVLAN                                   |               | 24  |
| LAGspage                            |                                                |               | 25  |
|                                     | AddinganddeletingaLAG                          |               | 26  |
|                                     | EditingaLAG                                    |               | 26  |
| Userspage                           |                                                |               | 27  |
|                                     | Addinganddeletingauser                         |               | 27  |
|                                     | Changingthepasswordforauser                    |               | 28  |
| VSXpage                             |                                                |               | 29  |
| Environmentalpage                   |                                                |               | 30  |
| Logpage                             |                                                |               | 31  |
| NameServerpage                      |                                                |               | 32  |
| SNMPpage                            |                                                |               | 33  |
|                                     | AddinganddeletinganSNMPv3user                  |               | 34  |
|                                     | EditinganSNMPv3user                            |               | 34  |
|                                     | AddinganddeletinganSNMPcommunity               |               | 35  |
|                                     | AddinganddeletinganSNMPtrapreceiver            |               | 35  |
3
AOS-CX10.08WebUIGuide| (8xxxSwitchSeries)

|                                       | EditinganSNMPtrapreceiver              |         |           |          | 36  |
| ------------------------------------- | -------------------------------------- | ------- | --------- | -------- | --- |
| Sessionpage                           |                                        |         |           |          | 36  |
| ConfigMgmtpage                        |                                        |         |           |          | 38  |
| FirmwareUpdatepage                    |                                        |         |           |          | 39  |
| Pingpage                              |                                        |         |           |          | 40  |
| Traceroutepage                        |                                        |         |           |          | 41  |
| ShowTechpage                          |                                        |         |           |          | 42  |
| SpanningTreepage                      |                                        |         |           |          | 42  |
|                                       | Editingthespanningtreesettings         |         |           |          | 44  |
| ConnectedClientspage                  |                                        |         |           |          | 44  |
| PKIpage                               |                                        |         |           |          | 45  |
|                                       | AddinganddeletinganESTProfile          |         |           |          | 46  |
|                                       | ViewinganESTProfile                    |         |           |          | 46  |
|                                       | AddinganddeletingaTAProfile            |         |           |          | 47  |
|                                       | EditingaTAProfile                      |         |           |          | 48  |
|                                       | Addinganddeletingacertificate          |         |           |          | 48  |
|                                       | Uploadingacertificate                  |         |           |          | 49  |
|                                       | Viewinganddownloadingacertificate      |         |           |          | 50  |
|                                       | Editingassociatedapplicationdetails    |         |           |          | 50  |
| SupportFilepage                       |                                        |         |           |          | 51  |
|                                       | Creatinganddeletingsupportfiles        |         |           |          | 52  |
|                                       | Downloadingasupportfile                |         |           |          | 53  |
| Finding                               | alert details                          | using   | the Web   | UI       | 54  |
| Working                               | with the                               | network | analytics | features | 56  |
| ViewingagentinformationusingtheWebUI  |                                        |         |           |          | 56  |
| WorkingwithanAnalyticstimeseriesgraph |                                        |         |           |          | 59  |
|                                       | Customizingdatadisplayedonthegraph     |         |           |          | 60  |
|                                       | Zoominginonthegraph                    |         |           |          | 62  |
|                                       | Downloadingthegraphasanimageor.csvfile |         |           |          | 62  |
|                                       | Viewinganalertonthegraph               |         |           |          | 63  |
ArubaNetworkAnalyticsEnginescripts,agents,andtroubleshootinginformation 66
| Support               | and Other          | Resources |     |     | 67  |
| --------------------- | ------------------ | --------- | --- | --- | --- |
| AccessingArubaSupport |                    |           |     |     | 67  |
| AccessingUpdates      |                    |           |     |     | 67  |
|                       | ArubaSupportPortal |           |     |     | 67  |
|                       | MyNetworking       |           |     |     | 68  |
| WarrantyInformation   |                    |           |     |     | 68  |
| RegulatoryInformation |                    |           |     |     | 68  |
| DocumentationFeedback |                    |           |     |     | 68  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

n Aruba 8400 Switch Series (JL375A, JL376A)

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

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

5

Convention

Usage

{ }

[ ]

… or

...

Braces. Indicates that at least one of the enclosed items is required.

Brackets. Indicates that the enclosed item or items are optional.

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

On the 83xx Switch Series

About this document | 6

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

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

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

7

Accessing the AOS-CX Web UI

Chapter 2

Accessing the AOS-CX Web UI

When Aruba Central manages AOS-CX switches, it functions as the single source of truth and the Web UI operates

in read-only mode.

Prerequisites

n Use a supported browser to access the Web UI, such as Chrome, Firefox, Edge, or Safari. For details on

supported browser versions, see the Release Notes for the version of AOS-CX you are using.

n You must have a valid login user name and password.

n You must have configured the management interface on the switch and enabled REST access for the VRF

that people will access the UI on.

n To use the Web UI to make configuration changes—such as adding users—the following must be true:

o You must have a valid login user name and password.

o The user name you use to log in must have administrator rights.

o The REST API access mode must be set to read-write.

For information about configuring the management interface and REST API access, see the AOS-CX
Fundamentals Guide.

Procedure

1. Start a supported web browser and enter the IP address of the management port in the address bar.

Use HTTPS.

For example:
https://192.0.2.5

2. Optionally a pre- and post-login message may be displayed. The message can be customized or

disabled with the banner command.

3. At the login page, enter your user name and password credentials, then click Login.

4. After you log in, the main Web UI page is displayed.

Ensure that both the switch and the client where the Web UI is running are set to use NTP or to a

time zone based on UTC time. If the switch and the client time are not in sync, then a message is

displayed after you log in, indicating the time difference.

Troubleshooting Web UI access issues
View issue symptoms and causes, as well as actions to resolve common Web UI access issues.

HTTP 404 error when accessing the switch URL

Symptom

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

8

The switch is operational and you are using the correct URL for the switch, but attempts to access the REST
API or Web UI result in an HTTP 404 "Page not found" error.

Cause

REST API access is not enabled on the VRF that corresponds to the access port you are using. For example,
you are attempting to access the REST API or Web UI from the management (OOBM) port, and access is not
enabled on the mgmt VRF.

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

1. Log out from one of the existing sessions.

Browsers share a single session cookie across multiple tabs or even windows. However, scripts that
POST to the login resource and later do not POST to the logout resource can easily create the
maximum number of concurrent sessions.

2.

If the session cookie is lost and it is not possible to log out of the session, then wait for the session
idle time limit to expire.

When the session idle timeout expires, the session is terminated automatically.

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions, Web UI sessions, and real-time notification subscriptions.

"Not Authorized" is displayed instead of page content

Symptom

The message "Not Authorized" is displayed in the details pane of a Web UI page.

Cause

Accessing the AOS-CX Web UI | 9

You have logged in as a user that is not authorized to view this page.

Action

Use the navigation pane to select a page you are authorized to access.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

10

Chapter 3

AOS-CX Web UI overview

AOS-CX Web UI overview

The AOS-CX Web UI provides quick and easy visibility into what is happening on your switch. With the Web
UI, you get faster problem detection, diagnosis, and resolution.

You can use the Web UI to do the following:

n Monitor the status of a switch from a single pane that shows easy-to-read indicators for power,

temperature, fans, CPU use, memory use, log entries, system information, firmware, and various aspects
of the network configuration.

n Identify issues when indicators turn red, and quickly locate and diagnose the problem.

n View and configure Network Analytics Engine agents, scripts, and alerts.

n Modify some aspects of the switch configuration.

n Run diagnostics including the ping, traceroute, and show tech commands.

n Upgrade or downgrade the image build on the device.

n Reboot the switch.

AOS-CX Web UI framework
Descriptions for (numbered) common areas, buttons, menus, and controls in the Web UI are listed after the
image.

Figure 1 Overview page with callouts

1. The

Show/Hide button on the left in the top banner, allows you to hide the navigation pane

(slides the pane in and out).

2. The navigation pane. Expand or collapse the System or Diagnostics group to show or hide related
items. For a description of each menu item in the navigation pane, see the description of the
Navigation pane.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

11

3. Breadcrumbs in the top banner show the path to your navigation selection.

4. The top banner provides information and other menu items.

5. The details pane shows information based on your selection.

6. Panels in the details pane display status, alerts, and other information and allow you to drill down to

more information.

7. The IP address of the management (mgmt) interface through which the switch Web UI is opened and
the name of the switch are displayed at the center of the top banner. If a switch does not have a
mgmt interface or if the mgmt interface is not configured, then an IP address is not displayed.

8. The

Layout Management icon in the top banner allows you to unlock the details pane page

layout. You can then resize and move panels, or reset the details pane page layout to the default

layout. Changes are persistent in the local browser. The icon changes to
unlocked.

, when the layout is

9. The

User Management menu in the top banner includes a logout selection.

10. The

System menu in the top banner includes the following:

n Save Config: Save configuration changes

n Reboot: Reboot the switch to either primary or secondary image.

n API: Access v1 REST APIs that you can use to read and/or write to the switch.

n v10.04 API: Access v10.04 REST APIs that you can use to read and/or write to the switch.

11. The

Show/Hide button on the right side of the top banner displays the Log Summary pane

(slides the pane in and out). The Log Summary provides a summary of the most recent critical level
log entries in the last X seconds. It also shows counts of the number of critical, warning, and info log
entries arriving in the last X seconds.

Customizing the Web UI

n You can customize the Web UI to change the page layout, include additional information, or filter to

display selected information.

n The changes that you make to customize the Web UI are restricted to the browser session. For example,
if you add a custom panel for an interface, the panel will be available only in the current browser session.
That is, if you open a Web UI session in a different browser or device, the newly added panel will not be
available.

Customizing page layouts

Some of the pages in the Web UI provide a user customizable layout. Each customization is persistent in the
local browser. The customization is stored based on the switch URL (based on the management address of
the switch). For example, if you change the management address, you will lose any page layout
configuration that was tied to that URL.

Each page can be reset back to the default layout.

Prerequisites

You must be logged in to the Web UI. You must allow cookies to be stored.

Procedure

AOS-CX Web UI overview | 12

1.

In the top banner, click the
the layout. The panel borders change to a dotted line, indicating that you can resize and move the
panels in the details pane.

Layout Management icon, and select Unlock Page Layout to unlock

Figure 1 Unlock Page Layout menu

Some of the possible changes you can make to a panel are described in the following steps.

2. To resize a panel, drag the handle at the bottom-right corner of the panel, and change the width and

height.

3. To reposition a panel, move the panel to a new position. The other panels will automatically rearrange

to accommodate the position of the moved panel.

4. To lock the changes to the page layout, click the

Layout Management icon, and select Lock Page

Layout.

5. To reset the page layout to the default view, click the

Layout Management icon, and select Reset

Page Layout. The option to reset the page is available only when the page layout is unlocked.

Adding a custom panel to the Overview page

You can add a custom panel to the Overview page to display a custom indicator for an interface.

Prerequisites

You must be logged in to the Web UI.

Procedure

1. Select an empty panel in the Overview page and click the + plus button.

Figure 1 Empty panel with + (plus) button

2. The Set Indicator dialog box is displayed. Select the interface you want to set an indicator for. Use the

Show/Hide Column Filters button to show a specific interface in the list. Click Interface: <X/X/X>
to set an indicator or Cancel to exit.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

13

Figure 2 Set Indicator dialog with example content

3. A new panel showing an indicator for the interface you selected is added to the Overview page.

Figure 3 Panel showing a selected interface

4.

If you want to move the panel you added or customize the new panel, click the Layout Management
menu in the top banner and select Unlock Page Layout to change the layout.
a. Move the new panel to where you want it to appear on the Overview page.
b. Resize the new panel, if desired.

5. To remove a custom indicator panel from the Overview page, click the X in the custom panel.

Customizing tables

You can show or hide table columns and you can resize column widths. Column customization is persistent
in the local browser. For how to filter column data, see Using Show/Hide filters in tables.

Prerequisites

You must be logged in to the Web UI.

Procedure

1. To hide a table column or show a hidden column, click the

Column Settings button in the title bar

of the table.

AOS-CX Web UI overview | 14

n From the list of column headings displayed, click any of the headings in the list with a check mark

to hide the column.

n Click any of the headings in the list without a check mark to show the column.

n Click Reset Table Columns to reset to the default.

Figure 1 List of column headings with check marks

2. To resize a column drag the column separators to expand or narrow the column. Columns cannot be

reordered.

3. View additional pages of content in the table using the table scroll bar.

Using Show/Hide filters in tables

You can use filters to display a subset of data in the table. Filtering is not persistent, so when you leave the
page, the filtering is removed.

Prerequisites

You must be logged in to the Web UI.

Procedure

To filter the data displayed in a table column, click
filter row is displayed below the column headings.

Show/Hide Column Filters on the table title bar. The

1. For columns that have a drop-down list as a filter, click the down arrow to display the list and select an

item from the list. The data displayed in the column will be filtered to just the specified data.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

15

Figure 1 Filtering a column by selecting from a list

2. For columns without a drop-down list, type in a value to filter the data in the column. Any item that
matches that value is then displayed. For example, entering lag10 will display data for lag10, lag100,
lag109.

Figure 2 Filtering a column by typing text

3. Turn off filters by clicking

Show/Hide Column Filters a second time. The full set of data, without

filtering, will be displayed in the table.

AOS-CX Web UI overview | 16

Chapter 4

AOS-CX Web UI pages

AOS-CX Web UI pages

Descriptions of the AOS-CX Web UI pages, and workflows for using these pages.

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

Selection

Overview

Description

Shows important information and statistics about the switch. Each indicator

panel provides "roll-up" status (color and icon) of Analytics, Environmental,

System, and so on. Empty titles allow you to select and save specific
interfaces to monitor (packets, bytes, utilization).

Analytics Dashboard

Shows the Analytics Dashboard providing information related to Network

Analytics Engine agents, scripts, alerts, and actions generated by these

scripts.

Interfaces

Shows information for each interface and shows the status of the

interfaces. Allows you to edit the interfaces details.

VLANs

LAGs

Users

Shows information for each VLAN and the status of the VLANs. Allows you to

add, edit, and delete VLANs.

Shows the information and the up or down status of the LAGs. Allows you to

add, edit, and delete Lags.

Shows user roles and names. Also allows you to add or delete a user and

change user passwords.

Administrator rights are required to access this selection.

VSX

Shows the Aruba Virtual Switching Extension (VSX) configuration and status

information.

System - Environmental

Shows power supply failures and warnings, temperatures, and fan

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

17

Selection

Description

information.

System - Log

Shows event log entries, event log queries, and message details.

System - Name Server

Shows primary and secondary name servers, and allows you to configure

addresses for name servers.

System – SNMP

Shows the SNMPv3 users, SNMP communities, and trap receivers details.

Allows you to add and delete SNMPv3 users, SNMP community names,

informs, and trap receivers.

System - Config Mgmt

Enables you to upload/download configurations to/from the running or

startup configurations.

System - Firmware Update

Enables you to upload firmware files.

Diagnostics - Ping

Enables you to run the ping command with various options.

Diagnostics - Traceroute

Enables you to run the traceroute command with various options.

Diagnostics - Show Tech

Enables you to run the showtech command. Administrator rights are
required to run this command.

Traffic - Spanning Tree

Shows the details of the spanning tree configuration, assigned ports, and

inconsistent ports. Allows you to enable Spanning Tree with Multiple

Spanning Tree or Rapid Per-Vlan Spanning Tree mode.

Connected Device - Clients

Shows the details of the devices connected to the switch.

Security - PKI

Shows the details of the TA profile, EST profile, digital certificates, and

associated applications in the switch. Allows you to add, edit, and delete TA

profile; add, view, and delete EST profile; add, view, upload, and delete

certificates; and edit associated applications.

Overview page
The Overview page provides a quick view of the status of a switch. It shows easy-to-read indicators for:
Analytics agents, power supply, thermal, fans, CPU use, memory use, log entries, checkpoints, firmware,
management modules, and system information.

Custom indicator panels allow you to select specific interfaces to monitor and to add panels for those
interfaces to the Overview page.

Ensure that both the switch and the client where the Web UI is running are set to use NTP or to a time zone based

on UTC time. Otherwise, the NAE agent data might be incorrect or missing and the System Uptime will be

incorrect. For example, if the time on the switch is set to 2 hours ahead of the client manually, instead of changing

the time zone offset, the agent data is populated according to the new time on the switch. If the switch time is set

back to match client time later, the Time Series Database does not overwrite the old data. Therefore the client

Web UI shows inaccurate data.

AOS-CX Web UI pages | 18

Figure 1 WebUI Overview Dashboard

The following table describes each panel included out of the box in the Overview page.

Panel

Analytics

Firmware

Config

Description

Shows: Total number of agents in critical, major, or minor status; total
number of agents scripts, agents, and monitors (both enabled and disabled)
compared to the maximum number supported on the switch. For example,
7/25 indicates that there are a total of 7 out of a supported maximum of 25.
Clicking the link displays the Analytics Dashboard.

Shows: Current firmware version, Primary version, and Secondary version.
Clicking the link displays the Firmware Update page.

Shows: Most recent checkpoint and total number of checkpoints. Clicking the
link displays the Config Mgmt page.

Management Modules

Shows: Detected module name, Active, and Standby status information.

Log

CPU

Shows: New log entries over the last 15 seconds. Clicking the link displays
the Log page.

Shows: Current average CPU utilization per management module.

Memory

Shows: Percent memory usage per management module.

System Information

Shows: System Uptime, System Description, System Location, System
Contact, Serial number, Base MAC, BIOS Version, Total number of available
interfaces, and a pie chart for link status.

Power Supplies

Shows: Summary count of alerts. Clicking the link displays the Environmental
page.

Thermal

Fans

Shows: Summary count of alerts. Clicking the link displays the Environmental
page.

Shows: Summary count of alerts. Clicking the link displays the Environmental
page.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

19

Panel

VSX

Description

Shows: Aruba Virtual Switching Extension (VSX) information, including
interswitch link (ISL) state, configuration synchronization state, and the role
of this switch (primary or secondary). Clicking the link displays the VSX page.

Analytics Dashboard
The Analytics Dashboard shows information related to Network Analytics Engine agents, scripts, alerts, and
information generated by these scripts. You can use the Network Analytics Engine to automate data
collection so you can quickly troubleshoot problems on a switch.

To see the total number of agents scripts, agents, and monitors (both enabled and disabled) compared to
the maximum number supported on the switch, see the Analytics panel on the Overview page.

From the Analytics Dashboard, you can drill down to other Analytics detail pages.

For some basic steps to using Analytics to monitor a switch, see Viewing agent information using the Web
UI. For complete information about using the Network Analytics Engine, scripts, and agents, see the Network
Analytics Engine Guide.

Ensure that both the switch and the client where Web UI is running are set to use NTP or to a time zone based on

UTC time. Otherwise, NAE agent data might be incorrect or missing. For example, if the time on switch is set to 2

hours ahead of the client manually instead of by changing the time zone offset, the agent data is populated

according to the new time on switch. If the switch time is set back to match client time later, the Time Series

Database does not overwrite the old data. Therefore the client Web UI shows inaccurate data.

If the software detects that the switch time and browser time differs by more than one minute, the Web UI

displays the following:

n A yellow warning triangle in the top banner of the Analytics Dashboard:

n When a user logs into the Web UI, the Web UI displays a warning message with the following title:

Switch Time and Browser Time are not in Sync

Figure 1 Analytics dashboard

Agents panel

AOS-CX Web UI pages | 20

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
You can create your own scripts or use scripts from other sources such as ones hosted on the Aruba
Solutions Exchange (ASE).

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

Figure 1 Interfaces page

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

21

Links in the VLAN and LAG columns allows you to drill down to the respective VLANs or LAGs page, auto-
selecting the appropriate resource.

Selecting a row in the interfaces list, displays more information on the interface. Details include: duplex,
MAC, IPv4, IPv6 address, Rx and Tx stats, packets, and more.

A graphical panel shows interface modules currently installed. Clicking an interface, selects the
corresponding row in the table. Each interface displayed in the graph will dynamically change based on the
current interface status.

Use the Show/Hide Column Filters button or Column Settings button to customize the table display.

Editing an interface

Use this procedure to perform the following tasks:

n Add an interface description

n Set the interface speed

n Set admin status

n Set flow control status

n Split interface

Procedure

1.

In the navigation pane, select Interfaces.

The Interfaces page is displayed.

2.

In the Interfaces panel, select an interface and click

.

The Configure Interface dialog box is displayed for the selected interface. You can select a different
interface if required.

3. Enter a description for the interface. For example, Guest connection.

AOS-CX Web UI pages | 22

4. Youcanselectoneofthefollowingvaluesfortheinterfacespeed.
| n   | 10-full |     |
| --- | ------- | --- |
10-half
n
100-full
n
100-half
n
| n                            | auto |         |
| ---------------------------- | ---- | ------- |
| 5. SelectUporDownfortheAdmin |      | Status. |
6. SelectEnableorDisablefortheFlowControlStatus.
7. SelecttheSplitcheckboxtosplittheportintomultipleinterfaces.
Splittingaportdisablestheselectedport,clearsallportconfiguration,andsplitstheportinto
multipleinterfaces.Thesplitinterfacesarenotavailableuntilyoureboottheswitchorthe
module.Forexample,selectthe40Gb/sport,andselecttheSplitcheckboxtosplittheportinto
four10Gb/sinterfaces.
8. ClickUpdate.
| VLANs | page |     |
| ----- | ---- | --- |
TheVLANspagedisplaysalistofVLANs.DetailsoneachVLANinclude:ID,Name,Status,Reason(errors
suchasNomemberport),alistofinterfaces,andalistofLAGs.
LinksintheInterfacesandLAGscolumnsallowyoutodrilldowntotherespectiveInterfacesorLAGspages,
auto-selectingtheappropriateresource.
SelectingarowintheVLANslist,displaysmoreinformationontheVLANinthedetailspane.Detailsinclude:
VLANmode,AdminState,LinkState,andtheassociatedLAGname.
UsetheShow/HideColumnFiltersbuttonorColumnSettingsbuttontocustomizethetabledisplay.
| Adding | and deleting | a VLAN |
| ------ | ------------ | ------ |
Youcanaddfrom1to4094VLANs.
23
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |
| ---------------------- | ------------------ | --- |

To add a VLAN:

1.

In the navigation pane, select VLANs.

The VLANs page is displayed.

2.

In the VLANs panel, click Add.

The Add VLAN dialog box is displayed.

3. Configure the following parameters:

n Vlan ID: A unique number from 1 to 4094.

n Vlan Name: A unique string to represent the VLAN. A default name is added with the VLAN ID

that you enter. You can change the default name.

4. Click OK.

To delete a VLAN:

1.

In the VLANs panel, select the VLAN, and click Delete.

A confirmation message is displayed.

When you delete a VLAN, if the selected VLAN is used as an interface VLAN, then the VLAN interface is also

deleted.

2. Click Delete VLAN.

Editing a VLAN

Use this procedure to perform the following tasks:

n Edit the VLAN name

n Add and delete ports

n Configure IPv4 address

For the default VLAN, you cannot edit the name or delete ports.

Procedure

1. To edit a VLAN name:

In the navigation pane, select VLANs. The VLANs page is displayed.
In the VLANs panel, select the VLAN, and click Edit. The Edit VLAN dialog box is displayed.

a.
b.
c. Edit the name.
d. Click OK.

2. To add ports:

Before adding ports, you must disable routing on the interface using the CLI. For more

information about using the CLI, see the AOS-CX Command-Line Interface Guide.

In the Edit Vlan dialog box, select Add Ports.

a.
b. Select the Vlan Mode as Access or Trunk.

n If you select the Vlan Mode as Access, then you can add access ports. All access ports are

displayed in the Untagged column in the VLANs panel.

AOS-CX Web UI pages | 24

n If you select the Vlan Mode as Trunk, then you can select Allowed or Native under Vlan

Trunk. All trunk ports are displayed in the Tagged column in the VLANs panel.

n If you select the Vlan Trunk as Allowed, then you can select the Allow all Vlans checkbox
to associate the entered port with all configured VLANs. By default, the port is associated to
any new VLAN that you add.

n If you select the Vlan Trunk as Native, then you can select the Tag checkbox to add the port

as native-tagged. Not selecting the Tag checkbox, leaves the ports as native-untagged.

c. Enter the port number in the member/slot/port notation.

You can add multiple ports with comma separated port numbers. For example, 1/1/1,1/1/2,1/1/3.
You can also add a LAG by entering the LAG name. For example, lag1, lag2.

d. Click OK.

3. To delete ports:

In the Edit Vlan dialog box, select Delete Ports.

a.
b. Delete the port numbers that you want to retain. The ports that are displayed in the dialog box

are deleted for the selected VLAN. Ports are displayed in the dialog box based on the option that
you select for the Vlan Mode and Vlan Trunk.

c. Click OK.

4. To configure IP address:

In the Edit Vlan dialog box, select IP Configuration.

a.
b. Select Enable to create a VLAN interface (if not created earlier) for the selected VLAN, and

configure a static IPv4 address.

Selecting Disable, removes any previously configured static IPv4 address on the selected

interface. Only the default VLAN can have DHCP IP configuration. For the default VLAN,

configuring a static IP through the Web UI, overrides the DHCP IP address. If you disable
static IP configuration, the IP address changes to the DHCP IP.

c. Enter the IP Address with the subnet mask in the IPv4 format (x.x.x.x/x).
d. Click OK.

LAGs page
The LAGs page displays a list of LAGs. Details on each LAG include: Name of the LAG, whether the admin
status is up or down, LAG bond status, whether the LAG is a multi-chassis LAG, a list of down interfaces, a list
of up interfaces, a list of VLANs, whether trunk allowed or not allowed, and a list of IP addresses.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

25

Figure 1 LAGs page

Links in the Interfaces and VLANs columns allow you to drill down to the respective Interfaces or VLANs
pages, auto-selecting the appropriate resource. Selecting a row in the LAGs list displays more information on
the LAG. Details include Interfaces and LAG statistics.

You can add and delete static LAGs. You can edit a LAG and add or delete ports, and set the admin status.

Use the Show/Hide Column Filters button or Column Settings button to customize the table display.

Adding and deleting a LAG

To add a LAG:

1.

In the navigation pane, select LAGs.

The LAGs page is displayed.

2.

In the LAGs panel, click Add.

The Add Lag dialog box is displayed.

3. Enter a number between 1 to 256.

4. Click OK.

To delete a LAG:

1.

In the LAGs panel, select the LAG, and click Delete.

A confirmation message is displayed.

2. Click Delete Lag.

Editing a LAG

Use this procedure to perform the following tasks:

n Add and delete ports

n Set admin status

To add ports:

AOS-CX Web UI pages | 26

1.

In the navigation pane, select LAGs.

The LAGs page is displayed.

2.

In the LAGs panel, select a lag, and click Edit.

The Edit Lag dialog box is displayed.

3. Select Add Ports.

4. Enter the port number in the member/slot/port notation.

You can add multiple ports with comma separated port numbers. For example, 1/1/1,1/1/2,1/1/3.

5. Click Update.

To delete ports:

1.

In the Edit Lag dialog box, select Delete Ports.

2. Delete the port numbers that you want to retain. The ports that are displayed in the dialog box are

deleted for the selected LAG.

3. Click Update.

To set admin status:

1.

In the Edit Lag dialog box, select Set Admin Status.

2. Select Up or Down as the admin status.

3. Click Update.

Users page
The Users page displays user names and roles. You can also add or delete a user, or change a password for
the logged in user. A user with the administrator role can access this page.

Figure 1 Users page showing an administrator user entry

Adding and deleting a user

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

27

You can add users with the following roles:

n Administrators: An administrator can access all pages and perform all tasks in the Web UI. An

administrator user is added by default.

n Operators: An operator can access all pages except the Users page and perform all tasks except adding or

deleting users and changing password.

n Auditors: An auditor can access only the Log page, and generate and export log reports.

Prerequisites

You must have the administrator role to add or delete users.

Procedure

To add a user:

1.

In the navigation pane, select Users.

The Users page is displayed.

2.

In the Users panel, click Add.

The New User Info dialog box is displayed.

3. Select a role for the user: operators, administrators, or auditors.

4. Enter the user name.

The user name can contain a maximum of 32 characters with only lowercase alphanumeric, dot,
dash, and underscore characters.

5. Enter the new password and confirm the password.

The password can contain a maximum of 32 characters without a space.

6. Click Add User.

To delete a user:

1.

In the Users pane, select the user to delete, and click Delete. You cannot delete the default
administrator user.

A confirmation message is displayed.

2. Click Delete User.

Changing the password for a user

Prerequisites

You must have the administrator role to add or delete users.

Procedure

To change the password for a user:

1.

In the navigation pane, select Users.

The Users page is displayed.

2.

In the Users panel, select the user, and click Change Password.

The Changing Password dialog box is displayed.

3. Enter the new password and confirm the password.

AOS-CX Web UI pages | 28

The password can contain a maximum of 32 characters without a space.

4. Click Change Password.

VSX page
If Aruba Virtual Switching Extension (VSX) is configured, the VSX page shows configuration and status
information about the VSX:

n The switch configurations include VSX LAGs that span both switches.

n Each switch has a user-configured role: either primary or secondary. If configuration synchronization is
enabled, supported configuration changes performed on the primary switch are performed on the
secondary switch automatically.

n The switches synchronize their configuration and state information over a user-configured interswitch

link (ISL).

The ISL is used for both datapath traffic forwarding and control path VSX protocol exchange.

n A separate IP-based keepalive mechanism completes the control plane by providing an integrity check if

there is an ISL failure.

For more information about VSX, see the Virtual Technologies Guide.

Figure 1 VSX page

Summary panel

The Summary panel shows state information about the switch to which you are connected, including
whether the switch role is primary or secondary and state information about the connections to the peer
switch.

The IP address of the switch to which you are connected is shown in the top banner of the Web UI.

Info panel

The Info panel provides configuration information about the VSX switches, including the following:

n The system ID of this switch and of the peer switch.

n The ISL port of this switch and of the peer switch. If the ISL is a LAG, the name of the LAG is shown.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

29

n The host name and IP address of the peer switch.

n Whether configuration synchronization between switches is enabled.

n The names of the VSX LAGs.

Keep Alive Information panel

The Keep Alive Information panel shows information and status information about the keep alive
communications from the keep alive source IP address to the IP address of this switch (shown in the top
banner of the Web UI) and IP address of the peer switch (shown under Peer IP in the panel).

Control Traffic Statistics panel

The Control Traffic Statistics panel shows information about control plane traffic between the primary
and secondary VSX switches. The traffic shown in this panel is related to the coordination of information
between VSX switches when the switches are acting as a single routing device.

Management & Assurance Statistics panel

The Management & Assurance Statistics panel shows information about management traffic between
the primary and secondary VSX switches. Examples of management traffic between VSX switches include
the following:

n Traffic related to synchronizing switch configuration data from the primary switch to the secondary

switch.

n Traffic related to executing show commands that include the vsx-peer option to get data from the peer

switch.

n Traffic related to Network Analytics Engine monitors or REST API calls that query the peer switch.

Environmental page
From the Environmental page you can view:

n Power supply failures or warnings.

n Fans' details such as status, RPMs, speed, and direction.

n Thermals' details such as status, fan state, location, temperature, maximum, and minimum values.

AOS-CX Web UI pages | 30

Figure 1 Environmental page

Log page
From the Log page you can view a list of event log entries. Each log entry displayed includes the following:
Time, Severity (Critical, Warning, Info), ID, and Message. If you set filtering on the table the custom changes
apply only to the data on the current page.

The Log page shows event log messages only. Accounting log messages must be accessed through the REST
API or the CLI.

Figure 1 Log page

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

31

n You can select an entry from the list of log entries to view more information in the details pane.

n Click Export to download the current log query as a CSV file.

n To run a new server-side query, click Query. A Query dialog box is displayed. You can customize the

query by Range, Severity, and identifier. Click Run to run the new query.

Figure 2 Query page

The following table shows how Syslog RFC 3164 severity levels are mapped to Web UI severity levels.

Web UI severity

Syslog severity

Critical

Warning

Info

0 Emergency: system is unusable

1 Alert: action must be taken immediately

2 Critical: critical conditions

3 Error: error conditions

4 Warning: warning conditions

5 Notice: normal but significant condition

6 Informational: informational messages

7 Debug: debug-level messages

Name Server page
From the Name Server page, you can view the current primary and secondary name server addresses.

To configure the addresses, enter a Primary IP Address and Secondary IP Address, and click Apply.
Primary and Secondary Name Server addresses can only be set when there is a static IP address on the
management interface. If it has a DHCP address, the values passed from the DHCP server are used.

Click Reset to undo any change that are not applied.

Figure 1 Name Server page

AOS-CX Web UI pages | 32

SNMP page
The SNMP page displays the SNMP community and trap receiver details.

Figure 1 SNMP Page

SNMPv3 Users panel

The SNMPv3 Users panel lists the SNMPv3 users added to the switch. You can add, edit, and delete
SNMPv3 user details.

SNMP Communities panel

The SNMP Communities panel lists the communities added in the switch. You can add and delete SNMP
community names.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

33

Trap Receivers panel

The Trap Receivers panel shows the details of the trap receivers and SNMP informs added in the switch.
You can add and delete trap receivers and SNMP informs.

Adding and deleting an SNMPv3 user

You can add SNMPv3 users to provide secured access to SNMP management stations. You can optionally
associate an authentication protocol and a privacy protocol, with passwords, to each user.

The user names that you add can be used when adding SNMPv3 trap receivers.

Procedure

To add an SNMPv3 user:

1.

In the navigation pane, expand System, and select SNMP.

The SNMP page is displayed.

2.

In the SNMPv3 Users panel, click Add.

The New SNMPv3 User Info dialog box is displayed.

3. Enter a user name.

The user name can contain a maximum of 32 characters without a space and must begin and end
with an alphabet, a number, or an underscore. The user name cannot contain any special characters
other than the underscore.

4. You can configure the following optional parameters:

n Authentication Protocol: You can select either md5 (Message Digest) or sha (Secure Hash

Algorithm) as the standard cryptographic hash function, to provide secured access to the user.

n Authentication Password: You must enter a password if you select an authentication protocol.
The password must be 8 to 32 characters long, and can contain alphabets, numbers, and special
characters.

n Privacy Protocol: You can select either aes (Advanced Encryption Standard) or des (Data

Encryption Standard) as the standard encryption method, to provide secured access to the user.

n Privacy Password: You must enter a password if you select a privacy protocol. The password
must be 8 to 32 characters long, and can contain alphabets, numbers, and special characters.

n Context: You can enter an SNMPv3 context that exists in the switch. For more information about

viewing and adding SNMPv3 context, see the AOS-CX Command-Line Interface Guide.

5. Click Add.

To delete an SNMPv3 user:

1.

In the SNMPv3 Users panel, select the SNMPv3 user name that you want to delete, and click
Delete.

A confirmation message is displayed.

2. Click Delete.

Editing an SNMPv3 user

Use this procedure to edit each SNMPv3 user.

Procedure

AOS-CX Web UI pages | 34

1. Inthenavigationpane,expandSystem,andselectSNMP.
TheSNMPpageisdisplayed.
| 2. IntheSNMPv3 | Userspanel,selecttheuser,andclickEdit. |     |     |     |
| -------------- | -------------------------------------- | --- | --- | --- |
TheEditSNMPv3UserInfodialogboxisdisplayed.
3. Youcaneditthefollowing:
| n   | UserName                   |                           |          |          |
| --- | -------------------------- | ------------------------- | -------- | -------- |
| n   | Authentication             | ProtocolandAuthentication |          | Password |
| n   | Privacy ProtocolandPrivacy |                           | Password |          |
| n   | Context                    |                           |          |          |
IfyouhavesetuptheAuthentication ProtocolandPrivacy Protocolforauser,youmustre-
enterthepasswordwheneditinganyofthedetails.Youcanenteradifferentpasswordtochange
thepassword.
4. ClickUpdate.
| Adding | and deleting | an  | SNMP community |     |
| ------ | ------------ | --- | -------------- | --- |
YoucanaddSNMPcommunitiestorestrictaccesstotheswitchfromtheSNMPmanagementstations.You
mustaddcommunitynamesthatexistinthenetwork.
Thedefaultcommunitynameispublic.Thisdefaultcommunityisusedwhennocommunityisaddedinthe
switch.Afteryouaddanewcommunityname,thedefaultcommunitynamepublicisnotdisplayedinthe
SNMPCommunitiespane.
ToaddanSNMPcommunity:
1. Inthenavigationpane,expandSystem,andselectSNMP.
TheSNMPpageisdisplayed.
2. IntheSNMPCommunitiespanel,clickAdd.
TheAddSNMPCommunitydialogboxisdisplayed.
3. EnteravalidSNMPname.
Thenamecancontainamaximumof32characterswithoutaspaceandmustbeginandendwithan
alphabet,anumber,oranunderscore.
4. ClickAddCommunity.
TodeleteanSNMPcommunity:
1. IntheSNMPCommunitiespanel,selectthecommunitynamethatyouwanttodelete,andclick
Delete.
Aconfirmationmessageisdisplayed.
| 2. ClickDelete | Community.   |     |           |          |
| -------------- | ------------ | --- | --------- | -------- |
| Adding         | and deleting | an  | SNMP trap | receiver |
YoucanaddtrapreceiversthatcanreceiveSNMPv1,SNMPv2c,andSNMPv3trapsorSNMPv2cand
SNMPv3informmessages.
ToaddanSNMPtrapreceiver:
35
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |     |     |
| ---------------------- | ------------------ | --- | --- | --- |

1. Inthenavigationpane,expandSystem,andselectSNMP.
TheSNMPpageisdisplayed.
2. IntheTrapReceiverspanel,clickAdd.
TheAddTrapHostdialogboxisdisplayed.
3. Configurethefollowingparameters:
| n   | Host:AvalidIPv4orIPv6addressoftheSNMPhost. |     |
| --- | ------------------------------------------ | --- |
| n   | Type:ThetypeofSNMPmessage,traporinform.    |     |
| n   | Version:TheSNMPversion,v1,v2c,orv3.        |     |
n UserID:TheuserIDforauthentication.TheuserIDisrequiredonlyiftheSNMPversionisv3.
Community:Thecommunitynameavailableintheswitch.Thedefaultcommunitynameis
n
public.ThecommunitynameisnotrequiredwhentheSNMPversionisv3.
n Port:TheSNMPportonwhichthehostlistensforthetraprequests.Thedefaultportnumberis
162.
| n   | VRF:TheVRFavailableontheswitch. |     |
| --- | ------------------------------- | --- |
4. ClickAddHost.
TodeleteanSNMPtrapreceiver:
1. IntheTrapReceiverspanel,selectthetrapreceiverthatyouwanttodelete,andclickDelete.
Aconfirmationmessageisdisplayed.
| 2. ClickDelete | Host.   |               |
| -------------- | ------- | ------------- |
| Editing        | an SNMP | trap receiver |
UsethisproceduretoviewandedittheSNMPtrapreceiverdetails.Youcaneditonlythecommunitythatis
addedtothetrapreceiver.
Procedure
1. Inthenavigationpane,expandSystem,andselectSNMP.
TheSNMPpageisdisplayed.
2. IntheTrapReceiverspanel,selectthetrapreceiver,andclickEdit.
TheEditTrapHostdialogboxisdisplayed.
3. YoucanchangetheCommunity.
4. ClickUpdate.
| Session | page |     |
| ------- | ---- | --- |
TheSessionpageallowsawaytoconfigurevaluesfortheHTTPSserver.
AOS-CXWebUIpages|36

HTTPS Server Session panel

The HTTPS Sever Session panel allows the user to configure the max sessions per user and session idle
timeout for the HTTPS server.

The APPLY button is used to configure the values provided by the user. The LOAD DEFAULT button
configures default values for session parameters. The APPLY button is disabled on providing invalid values
for the session parameters. On successful configuration of session parameters values, the following
dialogue is displayed:

Max sessions

The functionality of maintaining the maximum number of sessions per user is handled by the REST module
in the switch. The Web UI only provides configuration support. On attempting to establish a session beyond
the configured max number of sessions, the following error dialogue is displayed:

Idle timer

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

37

Web UI sessions are maintained by REST module and these Web UI sessions inactivity is monitored by REST
deamon based on the RESTAPI request activity from each session. In Web UI implementation, many pages
use periodic data polling (like every 10 secs) using the REST API to provide dynamic update of data. This
causes the Web UI session to never timeout from the REST daemon perspective, because the REST API does
not distinguish between the active polling API and the user-triggered REST API. Therefore, the REST Daemon
will never timeout Web UI sessions even if the user is inactive. Because of this, the user activity idle timer is
must be maintained by the Web UI and once the activity timer times out, the Web UI will automatically log
out of the session.

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

A warning message is displayed when the idle session timer has one-minute before expiring.

The user can reset the timer and continue the session by clicking the RESET button. If not reset, the session
expires in one minute from the warning message display.

Config Mgmt page
From the Config Mgmt page you can:

n Upload or download configurations to or from the Running or Startup configuration.

n Create a configuration checkpoint.

n Download running, startup, and checkpoint configurations

AOS-CX Web UI pages | 38

Copyfromortovariousconfigurations:runningtostartup,runningtocheckpoint,checkpointtostartup,
n
checkpointtorunning,startuptorunning.
UploadsanddownloadsareperformedthroughtheRESTinterface.
| Figure1 ConfigMgmt(configurationmanagement)page |        |      |
| ----------------------------------------------- | ------ | ---- |
| Firmware                                        | Update | page |
FromtheFirmwareUpdatepage,youcanseethecurrent,primary,andsecondaryfirmwareversionsand
youcanuploadfirmwarefiles.
FirmwareUpdateshowingimageversions
Figure1
UploadsareperformedthroughtheRESTinterface.
39
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |
| ---------------------- | ------------------ | --- |

After the update starts, it cannot be canceled.

Prior to updating, a message is displayed: Are you sure you want to update the primary/secondary
image?

After the firmware upload is completed, a new dialog box is displayed that contains the message: New
firmware has been successfully uploaded. Verifying and writing system firmware...

You may need to press Reboot on the page or select the Reboot item in the top right System menu for the
image to take effect.

Selecting Reboot reboots the switch.

After you select Reboot, you cannot cancel the request.

After selecting Reboot, you will be prompted to verify that you want to reboot the switch and to choose an
image to use when rebooting.

Figure 2 Reboot confirmation dialog box

Ping page
From the Ping page, you can run the ping command to the specified target hostname and view the output.
Click Ping to run the command or Cancel.

Figure 1 Ping page

AOS-CX Web UI pages | 40

You can set the following parameters on the ping command:

n Repetition: Specify the number of pings sent (1-10,000).

n Interval: Specify the interval between successive ping requests (1-60).

n Timeout: Specify the Ping Timeout in seconds (1-60).

n Datagram-Size: Specify the size of ping datagram (100 - 65,399).

n Type of Service (TOS): Specify IP TOS to be used in ping request (0 - 255).

n Data Fill: Specify the ping packet data pattern in hexadecimal digits.

n IP-Option: Specify an IP option to be used in ping packet.

n Use Management Interface: Specify the use of the management interface (check box).

Click Reset to reset options to the default.

Traceroute page
From the Traceroute page, you can run the traceroute command to the specified target hostname and
view the output. Click Traceroute to run the command.

Figure 1 Traceroute page

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

41

You can set the following parameters on the traceroute command:

n Destination Port: Specify the destination port (1 - 34000).

n timeout: Specify the traceroute timeout in seconds (1-60).

n maxttl: Specify the maximum number of hops to reach the destination (1 - 255).

n minttl: Specify minimum number of hops to reach the destination (1 - 255).

n probes: Specify the number of probe packets per hop to send (1 - 5).

n Loose src Route: Specify routing information to be used by the gateways.

n Use Management Interface: Specify the use of the management interface (check box).

Click Reset to reset options to the default.

Show Tech page
From the Show Tech page, you can run the showtech command. Administrator rights are required.

Figure 1 Show Tech page

Click Generate, to start generating the report on the switch.

Click Export to download the showtech file locally. The exported file is in simple text format, the same as
with the CLI output.

Spanning Tree page
The Spanning Tree page displays the spanning tree configuration details of the switch. The Spanning Tree
Protocol (STP) eliminates Layer 2 loops in networks, by selectively blocking some ports and allowing other
ports to forward traffic.

AOS-CX Web UI pages | 42

Figure 1 Spanning Tree page

Status panel

The Status panel shows information about the spanning tree configuration—whether spanning tree is
enabled or disabled and the spanning tree mode that is selected.

You can enable spanning tree with Multiple Spanning Tree (MST) or Rapid Per-Vlan Spanning Tree (Rapid
PVST) mode.

In the Multiple Spanning Tree mode, the Spanning Tree page displays additional details like the assigned
ports, MSTP configuration details, the number of times the topology was changed, and the time since the
topology changed.

In the Rapid Per-Vlan Spanning Tree mode, the Spanning Tree page displays only the details of the assigned
ports. The Rapid Per-Vlan Spanning Tree mode enables a separate spanning tree in each VLAN, including the
default VLAN.

Assigned Ports panel

The Assigned Ports panel shows the details of the ports based on the ports added in the spanning tree
configuration. For example, if some ports are set as BPDU Filter or Guard Ports, then the port numbers are
displayed in the member/slot/port notation.

Inconsistent Ports panel

The Inconsistent Ports panel shows the details of the ports that are in an inconsistent STP state.
Inconsistent state occurs when the ports on both ends of a point-to-point link are untagged members of
different VLANs or when the ports have different configurations on both end. For example, if one end is
configured as trunk and the other end is configured as an access port.

MSTP Configuration Details panel

The MSTP Configuration Details panel shows the name of the region, the revision number, and a digest
of the MST VLANs-to-instance mapping from the switch configuration.

Topology panel

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

43

TheTopologypanelshowsthenumberoftimesthetopologychanged.
| TopologyChange | Time panel |     |
| -------------- | ---------- | --- |
TheTopology Change Timepanelshowsthetimesincethetopologychanged.
| Editing | the spanning | tree settings |
| ------- | ------------ | ------------- |
Toeditthespanningtreesettings:
1. Inthenavigationpane,expandTraffic,andselectSpanning Tree.
TheSpanningTreepageisdisplayed.
2. IntheStatuspanel,click.
TheEditSpanningTreedialogboxisdisplayed.
3. Configurethefollowingparameters:
| n   | Status:Optiontoenableordisablespanningtree. |     |
| --- | ------------------------------------------- | --- |
n Mode:OptiontoselecttheMultipleSpanningTreeorRapidPer-VlanSpanningTreemode.
n Config Name:AnamefortheMultipleSpanningTreeconfiguration.Thisfieldisdisplayedonlyif
theMultipleSpanningTreemodeisselected.
n Config Revision:ArevisionnumberoftheMultipleSpanningTreeconfiguration.Thisfieldis
displayedonlyiftheMultipleSpanningTreemodeisselected.
| n   | Priority:Apriorityforthespanningtreeconfiguration. |     |
| --- | -------------------------------------------------- | --- |
4. ClickOK.
| Connected | Clients | page |
| --------- | ------- | ---- |
TheConnectedClientspagedisplaysdetailsofthedevicesconnectedtotheswitch.
| Figure1 | ConnectedDevicespage |     |
| ------- | -------------------- | --- |
ConnectedClientspanel
AOS-CXWebUIpages|44

The Connected Clients panel displays the device ID, IP address, device name, local and remote ports,
capability, TTL time, parent device, and source details.

PKI page
Public Key Infrastructure (PKI) capability on the switch provides digital certificates to authenticate network
entities. This page enables you to configure and manage digital certificates on the switch. The switch uses
certificates to validate SSH clients when acting as an SSH server and when communicating with syslog
servers while TLS encryption is used.

Each entity in the PKI has their identity validated by a certificate authority (CA). The CA issues a digital
certificate as part of enrolling each entity into the PKI. This digital certificate is used by the replying parties
(for example, network connection peers) to set up secure communication. Based on the information
present in the certificate of the sender, the receiving entity can validate the authenticity of the sender and
subsequently establish a secure communication channel. For more information about PKI, see the AOS-CX
Security Guide.

Figure 1 WebUI Overview Dashboard

EST Profiles panel

The EST Profiles panel displays the details of the EST profiles added to the switch. Enrollment over Secure
Transport (EST) enhances the switch PKI infrastructure with a simpler, scalable, and more secure method of
certificate provisioning, re-enrollment, and renewal.

TA Profiles panel

The TA Profiles panel displays information and status of TA profiles added to the switch. A Trust Anchor
(TA) defines certificate-specific operations, such as enrollment and validations. Each TA profile stores the
certificate for a trusted CA.

Certificates panel

The Certificates panel displays details about the digital certificates that can be used for applications in the
switch. Certificates help secure digital transactions by enabling the end parties to validate each other's

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

45

identity. Digital certificates are issued by a CA and are composed of an encoded string of characters (usually
stored in a file).

Associated Application Details panel

The Associated Application Details panel displays the features (applications) on the switch to which you
can associate certificates. The panel also displays the associated certificate name and status. By default, all
features are associated with the default, self-signed certificate local-cert. This certificate is created by the
switch the first time it starts.

Adding and deleting an EST Profile

To add an EST profile:

1.

In the navigation pane, expand Security, and select PKI.

The PKI page is displayed.

2.

In the EST Profiles panel, click Add.

The New EST Profile Info dialog box is displayed.

3. Enter a profile name for the EST profile.

4. Configure the following optional parameters:

n Arbitrary Label: Enter an arbitrary label for the EST URI to distinguish it from the other EST

profiles running on the EST server. The arbitrary label can contain alphabets, numbers, and special
characters without a space. Only dot (.), underscore (_), tilde (~), colon (:), slash (/), and hyphen (-)
are allowed as special characters.

n Arbitrary Label Enrollment: Enter an arbitrary enrollment label for EST URI.

n Arbitrary Label Re-enrollment: Enter an arbitrary re-enrollment label for EST URI.

n Re-enrollment Lead Time: Enter the lead time to re-enroll a certificate before it expires. The

time should be from 0 to 30 days. The default value is 2 days.

n Retry Count: Enter the number of times to retry to enroll a certificate. The value should be from

0 to 32. The default value is 3 retries.

n Retry Interval: Enter the interval after which the switch can retry to enroll a certificate. The value

should be from 30 to 600 seconds. The default value is 30 seconds.

n URL: Enter the URL for the EST server.

n Username: Enter the username to access the EST server. The username can contain alphabets,

numbers, and special characters without a space.

n Password: Enter the password for the username in the plain-text format. The password can

contain alphabets, numbers, and special characters without a space.

n VRF: Select the VFR that the switch uses to communicate with the EST server. VRF mgmt is used

by default.

5. Click OK.

To delete an EST profile:

1.

In the EST Profiles panel, select the EST profile, and click Delete.

A confirmation message is displayed.

2. Click Delete.

Viewing an EST Profile

To view the details of an EST profile:

AOS-CX Web UI pages | 46

1.

In the navigation pane, expand Security, and select PKI.

The PKI page is displayed.

2.

In the EST Profiles panel, select the EST profile, and click View.

The details are displayed in a dialog box.

3. Click OK.

Adding and deleting a TA Profile

To add a TA profile:

1.

In the navigation pane, expand Security, and select PKI.

The PKI page is displayed.

2.

In the TA Profiles panel, click Add.

The Add TA Profile dialog box is displayed.

3. Click Browse and select a certificate to associate with the TA profile. The certificate file must be in
.pem format. The switch can import Privacy-Enhanced Mail (PEM) encoded ITU-T X.509 v3
certificates.

The certificate with PEM data must be delimited with the following lines:

-----BEGIN CERTIFICATE-----

-----END CERTIFICATE-----

For example:

-----BEGIN CERTIFICATE-----

MIIDsDCCApgCCQDJotuPPj9GCDANBgkqhkiG9w0BAQsAADCBqzELMAkGA
UEBhVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcBM1JvY2tsa
W4xDDAKBgBAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSokwAYD
...
MioDy0096DvSMPsnOaI+jnZ3AozN8y+nLgotXUsg36pO/Ncc51oQhyUdc
AbgA1rzSLgyTnpXZKumvlaoTk3pzrIf7m5V103GTbgHGSFCzgO6QWxVxu
9d7ju1o59SaOIT7JSsYI5LsLpVz9ZqS599rj/lLoH+rLNlRDVXpS+J51U

-----END CERTIFICATE-----

4. Enter a profile name for the TA profile. The profile name can have a maximum of 32 characters.

5. Configure the following optional parameters:

n Revocation-Check: Select the OCSP checkbox to determining the revocation status of the

certificate. Optionally, enter the primary and secondary OCSP responder URLs that the TA profile
should use to verify the revocation status.
Selecting the checkbox enables certificate revocation checking for the TA profile using the online
certificate status protocol (OCSP). If no OCSP responder URLs are defined for a TA profile (default
setting), then the OCSP responder URL in the peer certificate is used for revocation status
checking. (The OCSP responder URL is contained in a certificate's Authority Information Access
field, which is an X.509 v3 certificate extension.)

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

47

n OCSP Disable-Nounce: Select the Disable-Nounce checkbox to exclude nonce from OCSP

requests.
A nonce is a unique identifier that an OCSP client inserts in an OCSP request and expects the OCSP
responder to include it in the corresponding OCSP response. The nonce mechanism helps prevent
replay attacks in which a malicious player attempts to masquerade as the OCSP responder.
Although the nonce is included by default, it can be excluded. Some OCSP responders choose to
not support the use of the nonce due to performance considerations

n OCSP Enforcement Level: Select either Strict or Optional to enforce OCSP check on

certificates. Strict enforcement is enabled by default.

o Strict: The certificate is accepted only if all possible checking (including validation failures,

software system errors, configuration errors, transactional errors) is successful.

o Optional: The certificate is accepted unless one or more of the following validation errors
occur: Response signature is invalid, nonce in response mismatch, or certificate is revoked,
when revocation checking is possible. If revocation check is not possible, the certificate is still
accepted if there are no other validation errors.

n OCSP VRF: Select the VRF that the switch uses to communicate with OCSP responders for OCSP

checking. VRF mgmt is used by default.

6. Click OK.

To delete a TA profile:

1.

In the TA Profiles panel, select the TA profile, and click Delete.

A confirmation message is displayed.

2. Click Delete.

Editing a TA Profile

To edit a TA profile:

1.

In the navigation pane, expand Security, and select PKI.

The PKI page is displayed.

2.

In the TA Profiles panel, click Edit.

The Edit TA Profile dialog box is displayed.

3. Configure the following optional parameters:

n Revocation-Check: Select or clear the OCSP checkbox.

n OCSP Disable-Nounce: Select or clear the OCSP Disable-Nounce checkbox.

n OCSP Enforcement Level: Select either Strict or Optional to enforce OCSP check on

certificates.

n OCSP VRF: Select the VRF that the switch uses to communicate with OCSP responders for OCSP

checking.

4. Click OK.

Adding and deleting a certificate

To add a certificate:

1.

In the navigation pane, expand Security, and select PKI.

The PKI page is displayed.

AOS-CX Web UI pages | 48

2.

In the Certificates panel, click New Certificate.

The New Certificate Info dialog box is displayed.

3.

In the Certificate Name field, enter a name for the certificate.

The certificate name can contain lowercase alphanumeric, dot, hyphen, and underscore characters.
The device-identity and local-cert certificates are added by default.

4. Configure the following optional parameters:

n Certificate Type: Select either regular or self-signed from the drop-down. Regular certificates
are signed by a CA. Self-signed certificates are signed by the switch or the user who is using the
certificate and not signed by a CA.

n EST Profile: Select the EST profile to associate with the certificate. This field is displayed only for

the regular certificate type.

n Key Type: Select either RSA or ECDSA from the drop-down for the encryption key type. The

default type is RSA.

n Key Size: Select the key size from the drop-down for the key type selected.

RSA key type has longer key size with values: 2048, 3072, and 4096 bits. The default size for RSA is
2048. The ECDSA key type has shorter key size with values: 256, 381, and 521 bits. The default size
for ECDSA is 256.

5.

In the Common Name field, enter the IP address or domain name associated with the switch.

Your web browser might warn you if this field does not match the URL entered into the web browser
when accessing the switch.

6. Configure the following optional parameters:

n Org Unit: Enter the name of the sub-entity (for example, the department) where the switch is

used.

n Org Name: Enter the name of the entity (for example, the company) where the switch is used.

n State: Enter the name of the state where the switch is used.

n Locality: Enter the name of the city where the switch is used.

7.

In the Country field, enter the country where the switch is used.

You must enter only two letters in uppercase for the country name, for example, US for the
United States.

8. Click OK.

To delete a certificate:

1.

In the Certificates pane, select the certificate, and click Delete.

A confirmation message is displayed.

2. Click Delete.

You cannot delete the default device-identity and local-cert certificates.

Uploading a certificate

You can upload a certificate only for regular certificates that are in a csr_pending certificate status. You
must upload a certificate to send a certificate signing request (CSR) for the regular certificate that you add in
the switch. You cannot upload a certificate for the device-identity regular certificate and if the certificate
status is installed.

The signed certificate that you upload must contain PEM data in the following chain format:

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

49

| -----BEGIN | CERTIFICATE----- |     |     |
| ---------- | ---------------- | --- | --- |
| -----END   | CERTIFICATE----- |     |     |
| -----BEGIN | CERTIFICATE----- |     |     |
| -----END   | CERTIFICATE----- |     |     |
Forexample:
| -----BEGIN | CERTIFICATE----- |     |     |
| ---------- | ---------------- | --- | --- |
MIIDsDCCApgCCQDJotuPPj9GCDANBgkqhkiG9w0BAQsAADCBqzELMAkGA
UEBhVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcBM1JvY2tsa
W4xDDAKBgBAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSokwAYD
...
MioDy0096DvSMPsnOaI+jnZ3AozN8y+nLgotXUsg36pO/Ncc51oQhyUdc
AbgA1rzSLgyTnpXZKumvlaoTk3pzrIf7m5V103GTbgHGSFCzgO6QWxVxu
9d7ju1o59SaOIT7JSsYI5LsLpVz9ZqS599rj/lLoH+rLNlRDVXpS+J51U
| -----END   | CERTIFICATE----- |     |     |
| ---------- | ---------------- | --- | --- |
| -----BEGIN | CERTIFICATE----- |     |     |
MIIDsDCCApgCCQDJotuPPj9GCDANBgkqhkiG9w0BAQsAADCBqzELMAkGA
UEBhVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcBM1JvY2tsa
W4xDDAKBgBAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSokwAYD
...
MioDy0096DvSMPsnOaI+jnZ3AozN8y+nLgotXUsg36pO/Ncc51oQhyUdc
AbgA1rzSLgyTnpXZKumvlaoTk3pzrIf7m5V103GTbgHGSFCzgO6QWxVxu
9d7ju1o59SaOIT7JSsYI5LsLpVz9ZqS599rj/lLoH+rLNlRDVXpS+J51U
| -----END | CERTIFICATE----- |     |     |
| -------- | ---------------- | --- | --- |
Touploadacertificate:
1. Inthenavigationpane,expandSecurity,andselectPKI.
ThePKIpageisdisplayed.
2. IntheCertificatespanel,selectthecertificate,andclickUploadCertificate.
TheUploadSignedCertificatedialogboxisdisplayed.
3. ClickBrowseandselectthecertificateinPEMformat.
4. ClickOK.
| Viewing | and downloading |     | a certificate |
| ------- | --------------- | --- | ------------- |
YoucanviewthedetailsofthecertificateanddownloadthecertificateinPEMformat.
Toviewthedetailsofacertificate:
1. Inthenavigationpane,expandSecurity,andselectPKI.
ThePKIpageisdisplayed.
2. IntheCertificatespanel,selectthecertificate,andclickViewCertificate.
Thecertificatedetailsaredisplayedinadialogbox.
3. TodownloadacopyofthecertificateinPEMformat,clickDownloadCertificate.
4. ClickOK.
| Editing | associated | application | details |
| ------- | ---------- | ----------- | ------- |
Youcaneditanassociatedapplicationtochangethecertificateassociatedwiththeapplication.Bydefault,
thelocal-certcertificateisassociatedwithallapplicationsintheswitch.
Toeditanassociatedapplication:
AOS-CXWebUIpages|50

1.

In the navigation pane, expand Security, and select PKI.

The PKI page is displayed.

2.

In the Associated Application Details panel, click Edit.

The Adding following Certificate dialog box for the associated application is displayed.

3. Select the required certificate name from the drop-down.

4. Click OK.

Support File page
Supported only on the 8320, 8325, and 8360 Switch Series.

From the Support file page, you can create support files that can be used to troubleshoot issues in the
switch. The support files contain the following information:

n Running configuration

n Events

n Errors

n Confidential information, such as usernames and passwords (in encrypted format)

n Support logs

n Previous boot logs

n Hardware information

n Software build version details

n Debugging information

Figure 1 Support File Page

Support File panel

The Support File panel displays the details of the support files created on the switch. Administrator rights
are required.

The following information is displayed:

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

51

n Name: Name of the support file.

n Type: Type of the support file. By default, the value is All and no other type of support file can be

generated.

n Status: Status of the support file. The following options are supported:

o Requested: Appears immediately after a support file is created.

o In Progress: Appears when the support file is being generated.

o Generated: Appears when the support file is successfully generated.

You can download the support file only when the status displays Generated.

o Failed: Appears when the support file fails to generate with a specific error message.

n Progress(%): Progress of support file generation (in percentage). This field displays 100% when the

support file is successfully generated.

n Size(KBs): Size of the support file in kilobytes. The size is displayed only after the support file is

successfully generated.

n Error: Error message when the support file fails to be generated. The following error messages are

supported:

o Collection is aborted

o File is not available in local file system

o Collection process terminated

o Collection process exceeded max collection time

o Insufficient storage space available storing the collection

o Insufficient RAM memory available for collection

o Collection already in progress in another session

o Collection is failed due to unexpected error

Creating and deleting support files

You can create support files to capture data about the switch.

You can generate a maximum of one support file. If you want to generate another support file, you must first

download and delete the previously generated file, and then generate a new file.

Procedure

To create a support file:

1.

In the navigation pane, expand Supportability, and select Support File.

The Support File page is displayed.

2.

In the Support File panel, click Create.

The Support File Name dialog box is displayed.

3. Enter the file name.

The file name can contain 5 to 64 alphanumeric characters.

4. Click Create.

To delete a support file:

AOS-CX Web UI pages | 52

1. IntheSupport Filepanel,selectthesupportfilethatyouwanttodelete,andclickDelete.
Aconfirmationmessageisdisplayed.
2. ClickDelete.
| Downloading | a support | file |
| ----------- | --------- | ---- |
Todownloadalocalcopyofthesupportfile:
YoucandownloadasupportfileonlywhenthestatusisGeneratedandtheprogressdisplays100%.
1. Inthenavigationpane,expandSupportability,andselectSupport File.
TheSupportFilepageisdisplayed.
| 2. IntheSupport | Filepanel,selectthesupportfile,andclickDownload. |     |
| --------------- | ------------------------------------------------ | --- |
Aconfirmationmessageisdisplayed.
3. ClickClose.
53
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |
| ---------------------- | ------------------ | --- |

Chapter 5
|               |               | Finding | alert details | using the | Web UI |
| ------------- | ------------- | ------- | ------------- | --------- | ------ |
| Finding alert | details using | the Web | UI            |           |        |
YoucanviewdetailsonthealertsdisplayedintheWebUI.
Prerequisites
YoumustbeloggedintotheWebUI.
Procedure
1. SelectAnalyticsfromthenavigationpane.
2. IntheAnalyticsDashboard,theAlertspanelliststhealertsforallagents.
| Figure1 | AlertspanelonAnalyticsDashboard |     |     |     |     |
| ------- | ------------------------------- | --- | --- | --- | --- |
3. Toseethealertsforaspecificagent,intheAnalyticsDashboardAgentspanelorAlertspanel,selectan
agent.
4. IntheAgentDetailspage,theagentalertsarelistedintheAlertspanel.
| Figure2 | AgentDetailspage |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
54
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |     |     |     |
| ---------------------- | ------------------ | --- | --- | --- | --- |

5.

In the Alerts panel, select an alert and click Details to view the Alert Details dialog box. To close the
dialog box, click Close.

You can also access alert details directly from the Analytics Dashboard by selecting an alert in the
Alerts panel and clicking Details.

6. The Action Result(s) in Alert Details dialog box might include additional details about actions and

links to the action result output.

Figure 3 Alert Details dialog box

To view the Action Result Output dialog box for an action, click the Output link.

Figure 4 Action Result dialog box

Finding alert details using the Web UI | 55

Chapter 6
|     |     |     |     | Working | with the | network | analytics |
| --- | --- | --- | --- | ------- | -------- | ------- | --------- |
features
| Working | with the | network | analytics | features |     |     |     |
| ------- | -------- | ------- | --------- | -------- | --- | --- | --- |
ThissectiondescribesthestepstoviewagentinformationusingtheWebUI,andworkwithanAnalyticstime
seriesgraph.
| Viewing | agent | information |     | using | the Web | UI  |     |
| ------- | ----- | ----------- | --- | ----- | ------- | --- | --- |
YoucanviewAnalyticsagentinformationincluding:agentstatus,scriptinformation,agentparameters,one
ormoretimeseriesgraphs,andanyalertsgenerated.
Prerequisites
n YoumustbeloggedintotheWebUI.
n EnsurethattheswitchandtheclientwhereWebUIisrunningaresettouseNTPortoatimezonebased
onUTCtime.Otherwise,NAEagentdatamightbeincorrectormissing.
Forexample,ifthetimeonswitchissetto2hoursaheadoftheclientmanuallyinsteadofbychangingthe
timezoneoffset,theagentdataispopulatedaccordingtothenewtimeonswitch.Iftheswitchtimeisset
backtomatchclienttimelater,theTimeSeriesDatabasedoesnotoverwritetheolddata.Thereforetheclient
WebUIshowsinaccuratedata.
Procedure
1. FromtheOverviewpage,lookattheAnalyticspaneltoseethetotalnumberofagentsincritical,
major,andminorstatus.Ifthepanelisoutlinedinred,itindicatesagentstatusissues.
| Figure1 | AnalyticspanelonOverviewpage |     |     |     |     |     |     |
| ------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
2. TogototheAnalyticsDashboard,selecttheAnalyticslinkintheAnalyticspanelontheOverview
page.
56
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |     |     |     |     |     |
| ---------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

Figure 2 Analytics Dashboard

The following information appears on the Analytics Dashboard:

n Top banner: Shows the number of agents with each type of status.
n Agents panel: Lists the agents installed on the switch and indicates the status of each agent.

If there is an error in an agent, the Agents panel shows an error icon next to the agent status.

Optionally, you can add an Analytics agent time series graph to the Analytics Dashboard by clicking the
+ plus sign next to any agent listed in the Agents panel.

The time series graph shows data collected by the Analytics agent. If an agent has multiple time series
graphs, the graph displayed on the Analytics Dashboard is specified by the script. You cannot choose
which graph to display on the Analytics Dashboard, but you can see all the graphs in the Agent Details
page.

Click the Agents link to display the Agent Management page. On this page you can create, edit, delete,
enable, and disable an agent.

n Scripts panel: Lists available scripts.

Select a script from the list to display the Script Details page where you can view script details, create an
agent to run the script, and download the script.

Click the Scripts link to display the Script Management page. On this page you can upload, download
or delete a script, create an agent, and access the Aruba Solution Exchange to find more scripts.

n Alerts panel: Lists alerts generated by all agents.

Select an alert in the list and click Details to display the Alert Details dialog box.

Click the Alerts link to display a list of the alerts with information on the rule and actions for each alert.

n Time series graphs: If an agent time series graph has been added to the Analytics Dashboard,
the graph is outlined in the agent status color. Agents can have more than one time series graph,
but only one graph for the agent is displayed in the Analytics dashboard. Click the link in the graph
to display the Agent Details page.

3. From the Analytics Dashboard, Agents panel, select the link to a specific agent. The Agent Details page

is displayed.

Working with the network analytics features | 57

Figure 3 Agent Details panels example

View the following information from the Agent Details page:

n Agent Details panel: Shows information about the agent.

Select the

Edit button to enable or disable an agent and modify agent parameters.

Select the
information, create an agent to run the script, and download the script.

View Script button to display the Script Details page where you can view script

n Status panel: Shows the status of the agent and when the status was last updated. For some

agents, you may see additional information. For example:

n System Created: If the Status panel includes the statement System Created, the agent cannot

be deleted.

n Baseline Thresholds: If the Status panel includes Baseline Thresholds, the agent can learn about
the activity being measured and set low thresholds and high thresholds based on what it learns.
The Baseline Thresholds information shown in the Status panel includes the number of thresholds
in the following states:

o Active: When a baseline threshold is in the active state, the agent has learned and established
the high and low thresholds, and the agent executes actions and generates alerts based on
those low or high thresholds.

o Inactive: When agent is disabled, the baseline stops collecting data and updating thresholds.

After the agent is re-enabled, the baseline goes into the learning state again.

o Learning: While a baseline threshold is in the learning state:

l The agent gathers data related to that baseline until the initial learning period completes.

Low and high thresholds are determined using the learning algorithm defined in the script,
and are set only after learning state is completed.

l Default thresholds (if specified in the script) are used to determine whether to execute

actions or generate alerts.

Baseline thresholds remain in the learning state for a script-specified period of time after the
agent is enabled.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

58

Selecting Baseline Thresholds displays a dialog box that shows additional information about all the
baselines for the agent, including the name, the associated monitor, state, and the current learned low
and high thresholds.

Figure 4 Baseline Thresholds

If there is an agent error, an error indicator is shown and you can hover over it for more information.

Figure 5 Agent Status

.

n Parameters panel: Shows the parameters used by the agent. For example, a parameter can be a

threshold value that, when breached, causes the agent status to change and an alert to be
generated. Selecting a parameter displays the description in a dialog box.

n Time Series graph: Graphs the data collected by the agent over time. Agents might have more
than one time series graph. Alert indicators and configuration checkpoints are overlaid on the
graph.

Alert indicators can include: a red or yellow triangle for an alert, a green triangle for return to normal, a
blue triangle for an alert on several resources being monitored. An example of an alert on several
resources: when monitoring multiple interfaces (wildcard), if an interface goes down, a red alert is
generated. If another interface goes down, then a blue alert is generated. A green alert will not be
generated until all the interfaces are back up.

Configuration checkpoints are shown as purple diamonds on the graph.

Clicking an alert indicator on the graph displays the Alert Details dialog box.

n Alerts panel: Lists alerts.

Select the Alerts link to display a list of the alerts with information on the rule and actions for each
alert.

Select an alert and click Details to display the Alert Details dialog box.

Select an alert and click Navigate to change the time series graph to show the time period with this
alert.

Working with an Analytics time series graph

Working with the network analytics features | 59

Data collected by an Analytics agent is displayed in the Web UI in one or more time series graphs. An agent
has at least one graph. An agent can have multiple graphs as specified in the script, but only one graph
represents the agent on the Analytics dashboard. The graph that represents the agent on the Analytics
dashboard is specified in the script.

If the Analytics dashboard does not include a graph for an agent, you can add the graph that represents that
agent from Analytics dashboard. Graphs on the Analytics dashboard represent a live view only. The graph
customization toolbar is not available from the Analytics dashboard.

The Agent Details page displays all the graphs for an agent, with each graph displayed in a panel.

Configuration checkpoints and alert indicators are overlaid on the graph. Configuration checkpoints are
shown as purple diamonds. Alert indicators can include the following:

n A red or yellow triangle for an alert

n A green triangle for a return to normal

n A blue triangle for an alert on several resources being monitored.

The graph displays alerts for all metrics being monitored. However, time series graphical information can be
shown for a maximum of eight metrics. The metrics that are being shown on the graph are listed at the
bottom of the graph.

Figure 1 Agent Details panel including graph

Procedure

1. Customizing data displayed on the graph

2. Zooming in on the graph

3. Downloading the graph as an image or .csv file

4. Viewing an alert on the graph

Customizing data displayed on the graph

There are several ways you can customize the data displayed on a time series graph to show more or less
data.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

60

1. View a tooltip for each data point on the graph by hovering the cursor over the data point.

The tooltip displays the date, time range, and min-max range.

Figure 1 Graph with tooltip displayed

2. Hover over a specific item in the legend following the graph to show only that specific data line on the

graph. The other data will be less visible.

3. From the graph shown on the Agent Details page, click the

Configure Chart button to open the

Customize Chart dialog box.
n The default mode is Automatic Monitoring, where the most meaningful monitors and resources
are automatically selected to display on the agent graph. To customize what data (monitors and
resources) you want displayed on the agent time series graph, select Customize Monitoring.

n You can sort and filter the Show column. If a monitor is a wildcard type, then you see a different

icon from the check box, where you can click and select subresources under that monitor.

The graph displays alerts for all metrics being monitored. However, the graph can show graphed data
for a maximum of eight metrics at a time. The metrics that are being shown on the graph are listed at
the bottom of the graph. You can choose which metrics to show. To remove the metric from the graph,
clear the box in the Show column of the metric you want to remove. To show a metric in the graph,
select the box in the Show column of the metric you want to display.

n The Resources Selected column shows how many total resources are selected out of the total

available resources.

n If a monitor can have an aggregation function, that function is displayed in the Aggregation

column.

Working with the network analytics features | 61

| Figure2 | CustomizeChart |       |     |     |
| ------- | -------------- | ----- | --- | --- |
| Zooming | in on the      | graph |     |     |
Thereareseveraldifferentwaystozoominonaspecifictimeperiodonthetimeseriesgraph.
1. Zoominandoutonthegraphbyselectingazoomlevelfromtheoptionsdisplayedatthetopofthe
timeseriesgraph:1hour,1day,10days,30days,90days,180days,1year.Youcanalsoselect
Customtoenteraspecificdateandtimerange.
| Figure1 | Zoomoptionsportionofagraph |     |     |     |
| ------- | -------------------------- | --- | --- | --- |
2. Oryoucanhighlightacustomrangeofdataonthegraphasfollows:
a. Positionthecursoronthetimeaxisofthegraphuntilaverticallineappearsthroughthetime.
b. Dragtheverticallinetotheleftorrighttothebeginningorendofthetimeperiodyouwantto
view.
c. Theselectedtimeperiodishighlightedandthebeginandenddatesaredisplayednexttothe
Customzoomlevel.
d. Releasethemousebuttonandthegraphisredrawnforjustthetimeperiodselected.
3. ResetthegraphtothedefaultbyselectingtheLivezoomlevel.
| Downloading | the | graph as an image | or .csv | file |
| ----------- | --- | ----------------- | ------- | ---- |
Youcandownloadthegrapheitherasanimageorrepresentedasasetofcomma-separatedvaluesthatcan
beopenedinspreadsheetprograms.Thedownloadoptionsareaccessedfromthedownarrowinthetop
rightcornerofthetimeseriesgraph:
62
| AOS-CX10.08WebUIGuide| | (8xxxSwitchSeries) |     |     |     |
| ---------------------- | ------------------ | --- | --- | --- |

Figure 1 Graph with down arrow highlighted

n To download the graph as an image, click the down arrow and select Download Chart.

The graph is downloaded in a file in .png format.

n To download the graph as a set of comma-separated values, click the down arrow and select Export to

CSV.

The graph is downloaded in a file in .csv format.

Viewing an alert on the graph

The graph shown on the Agent Details page might not show the time period or resource associated with a
specific alert. Use this procedure to change the graph to show the alert and the associated metric.

1. From the alerts panel on the Agent Details page, select an alert and click Navigate.

Figure 1 Agent Details before navigating to an alert

The graph is changed to display the time period containing the alert. However, the alert might be for
a metric that is being monitored but that is not being shown in the graph.

The graph displays alerts for all metrics being monitored. However, the graph can show graphed data
for a maximum of eight metrics at a time. The metrics that are being shown on the graph are listed at
the bottom of the graph.

Working with the network analytics features | 63

Figure 2 Graph with alert but not metric for 1/1/3

2. To adjust the graph display to show the metrics for the alert, do the following:

a. Locate the alert on the graph and click the alert triangle flag. The Alert Details dialog box is

displayed.

Figure 3 Alert details box with View on Graph button displayed

b. Click View on Graph.

3.

If the graph is showing eight metrics and the metric you want to display is the ninth metric, you must
choose an existing metric to clear so that the graph can show the metric associated with the alert. For
example:

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

64

Figure 4 Dialog box prompting you to clear a metric

a. Clear the selection box for the metrics you no longer want to show. For example:

Figure 5 Dialog box with 1/1/9 removed

b. Click View on Graph.

The graph is changed to show the metric associated with the alert. For example:

Working with the network analytics features | 65

Figure 6 Graph showing alert and metric 1/1/3

4. You can reset the graph to the default by selecting the Live zoom level.

Aruba Network Analytics Engine scripts, agents, and
troubleshooting information
For detailed information about the Aruba Network Analytics Engine and the Analytics dashboard, see the
Network Analytics Engine Guide. This guide includes information about using the Web UI to do the following:

n Create, modify, and delete agents.

n Enable and disable agents.

n Create, edit, download, and install scripts.

n Access scripts on the Aruba Solutions Exchange.

n Troubleshoot problems with agents and scripts.

In addition, the guide provides information about using the REST API to perform script and agent tasks and
information about writing scripts.

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

66

Support and Other Resources

Chapter 7

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

AOS-CX 10.08 Web UI Guide | (8xxx Switch Series)

67

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

Support and Other Resources | 68