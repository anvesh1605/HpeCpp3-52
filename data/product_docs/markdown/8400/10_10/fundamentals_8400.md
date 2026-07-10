AOS-CX 10.10 Fundamentals
Guide

8400 Switch Series

Published: January 2024

Version: 3

Copyright Information

© Copyright 2024 Hewlett Packard Enterprise Development LP.

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

| 2

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
For more information, see the KM Process Guide. ?>
Acknowledgments

Bluetooth is a trademark owned by its proprietor and used by Hewlett Packard Enterprise under license.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

3

Contents
| About this                                   | document                                       | 10  |
| -------------------------------------------- | ---------------------------------------------- | --- |
| Applicableproducts                           |                                                | 10  |
| Latestversionavailableonline                 |                                                | 10  |
| Commandsyntaxnotationconventions             |                                                | 10  |
| Abouttheexamples                             |                                                | 11  |
| Identifyingswitchportsandinterfaces          |                                                | 11  |
| Identifyingmodularswitchcomponents           |                                                | 12  |
| About AOS-CX                                 |                                                | 13  |
| AOS-CXsystemdatabases                        |                                                | 13  |
| ArubaNetworkAnalyticsEngineintroduction      |                                                | 14  |
| AOS-CXCLI                                    |                                                | 14  |
| ArubaCXmobileapp                             |                                                | 14  |
| ArubaNetEdit                                 |                                                | 14  |
| Ansiblemodules                               |                                                | 15  |
| AOS-CXWebUI                                  |                                                | 15  |
| AOS-CXRESTAPI                                |                                                | 15  |
| In-bandandout-of-bandmanagement              |                                                | 16  |
| SNMP-basedmanagementsupport                  |                                                | 16  |
| Useraccounts                                 |                                                | 16  |
| Initial Configuration                        |                                                | 17  |
| InitialconfigurationusingZTP                 |                                                | 17  |
| InitialconfigurationusingtheArubaCXmobileapp |                                                | 17  |
|                                              | TroubleshootingBluetoothconnections            | 19  |
|                                              | BluetoothconnectionIPaddresses                 | 19  |
|                                              | Bluetoothisconnectedbuttheswitchisnotreachable | 19  |
|                                              | Bluetoothisnotconnected                        | 20  |
| InitialconfigurationusingtheCLI              |                                                | 23  |
|                                              | Connectingtotheconsoleport                     | 23  |
|                                              | Connectingtothemanagementport                  | 24  |
|                                              | Loggingintotheswitchforthefirsttime            | 25  |
|                                              | SettingswitchtimeusingtheNTPclient             | 25  |
| Configuringbanners                           |                                                | 26  |
| Configuringin-bandmanagementonadataport      |                                                | 26  |
| UsingtheWebUI                                |                                                | 27  |
| Configuringthemanagementinterface            |                                                | 27  |
| Restoringtheswitchtofactorydefaultsettings   |                                                | 28  |
| Managementinterfacecommands                  |                                                | 30  |
|                                              | default-gateway                                | 30  |
|                                              | ipstatic                                       | 31  |
|                                              | nameserver                                     | 32  |
|                                              | showinterfacemgmt                              | 33  |
| NTPcommands                                  |                                                | 34  |
|                                              | ntpauthentication                              | 34  |
|                                              | ntpauthentication-key                          | 34  |
|                                              | ntpdisable                                     | 36  |
|                                              | ntpenable                                      | 36  |
|                                              | ntpconductor                                   | 37  |
4
AOS-CX10.10FundamentalsGuide| (8400SwitchSeries)

|                                   | ntpserver                                |           | 38  |
| --------------------------------- | ---------------------------------------- | --------- | --- |
|                                   | ntptrusted-key                           |           | 40  |
|                                   | ntpvrf                                   |           | 41  |
|                                   | showntpassociations                      |           | 41  |
|                                   | showntpauthentication-keys               |           | 43  |
|                                   | showntpservers                           |           | 43  |
|                                   | showntpstatistics                        |           | 44  |
|                                   | showntpstatus                            |           | 45  |
| Interface                         | configuration                            |           | 47  |
| Configuringalayer2interface       |                                          |           | 47  |
| Configuringalayer3interface       |                                          |           | 47  |
| SinglesourceIPaddress             |                                          |           | 48  |
| Priority-basedflowcontrol(PFC)    |                                          |           | 48  |
| Flowcontrolandlosslessbuffering   |                                          |           | 49  |
|                                   | Requirementsforproperlosslessbuffering   |           | 49  |
| Unsupportedtransceiversupport     |                                          |           | 49  |
| Configuringaninterfacepersona     |                                          |           | 50  |
|                                   | Modes                                    |           | 51  |
|                                   | Predefinedandcustompersonanames          |           | 51  |
|                                   | Creatingandconfiguringaninterfacepersona |           | 52  |
|                                   | Examples                                 |           | 52  |
| Interfacecommands                 |                                          |           | 52  |
|                                   | allow-unsupported-transceiver            |           | 53  |
|                                   | defaultinterface                         |           | 54  |
|                                   | description                              |           | 55  |
|                                   | flow-control                             |           | 56  |
|                                   | interface                                |           | 58  |
|                                   | interfaceloopback                        |           | 58  |
|                                   | interfacevlan                            |           | 59  |
|                                   | ipaddress                                |           | 60  |
|                                   | ipmtu                                    |           | 61  |
|                                   | ipsource-interface                       |           | 62  |
|                                   | ipv6address                              |           | 63  |
|                                   | ipv6source-interface                     |           | 64  |
|                                   | l3-counters                              |           | 66  |
|                                   | mtu                                      |           | 67  |
|                                   | persona                                  |           | 67  |
|                                   | routing                                  |           | 70  |
|                                   | showallow-unsupported-transceiver        |           | 70  |
|                                   | showinterface                            |           | 71  |
|                                   | showinterfacedom                         |           | 75  |
|                                   | showinterfaceflow-control                |           | 76  |
|                                   | showinterfacestatistics                  |           | 81  |
|                                   | showinterfacetransceiver                 |           | 82  |
|                                   | showinterfaceutilization                 |           | 86  |
|                                   | showipinterface                          |           | 87  |
|                                   | showipsource-interface                   |           | 88  |
|                                   | showipv6interface                        |           | 89  |
|                                   | showipv6source-interface                 |           | 90  |
|                                   | shutdown                                 |           | 91  |
|                                   | systeminterface-group                    |           | 91  |
| Source                            | interface                                | selection | 93  |
| Source-interfaceselectioncommands |                                          |           | 93  |
|                                   | ipsource-interface(protocol<ip-addr>)    |           | 93  |
|5

ip source-interface
ipv6 source-interface
ipv6 source-interface
show ip source-interface
show ipv6 source-interface
show running-config

VLANs

Configuration and firmware management

Upgrade and downgrade scenarios

Upgrades
Downgrades
Limitations

Checkpoints

Checkpoint types
Maximum number of checkpoints
User generated checkpoints
System generated checkpoints
Supported remote file formats
Rollback
Checkpoint auto mode
Testing a switch configuration in checkpoint auto mode

Checkpoint commands
checkpoint auto
checkpoint auto confirm
checkpoint diff
checkpoint post-configuration
checkpoint post-configuration timeout
checkpoint rename
checkpoint rollback
copy checkpoint <CHECKPOINT-NAME> <REMOTE-URL>
copy checkpoint <CHECKPOINT-NAME> {running-config | startup-config}
copy checkpoint <CHECKPOINT-NAME> <STORAGE-URL>
copy <REMOTE-URL> checkpoint <CHECKPOINT-NAME>
copy <REMOTE-URL> {running-config | startup-config}
copy running-config {startup-config | checkpoint <CHECKPOINT-NAME>}
copy {running-config | startup-config} <REMOTE-URL>
copy {running-config | startup-config} <STORAGE-URL>
copy startup-config running-config
copy <STORAGE-URL> running-config
erase
show checkpoint <CHECKPOINT-NAME>
show checkpoint <CHECKPOINT-NAME> hash
show checkpoint post-configuration
show checkpoint
show checkpoint date
show running-config hash
show startup-config hash
write memory

Boot commands

boot fabric-module
boot line-module
boot management-module
boot set-default
boot system

95
96
98
99
100
102

104

105
105
105
105
105
106
106
106
106
106
107
107
107
107
108
108
109
109
111
112
113
114
114
115
116
117
118
120
121
122
123
123
125
126
128
129
130
130
131
132
133
133
133
134
135
136
137

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

6

|                            | showboot-history                           |                   | 139 |
| -------------------------- | ------------------------------------------ | ----------------- | --- |
| Firmwaremanagementcommands |                                            |                   | 141 |
|                            | copy{primary|secondary}<REMOTE-URL>        |                   | 141 |
|                            | copy{primary|secondary}<FIRMWARE-FILENAME> |                   | 142 |
|                            | copyprimarysecondary                       |                   | 143 |
|                            | copy<REMOTE-URL>                           |                   | 143 |
|                            | copysecondaryprimary                       |                   | 145 |
|                            | copy<STORAGE-URL>                          |                   | 146 |
| SNMP                       |                                            |                   | 148 |
| ConfiguringSNMP            |                                            |                   | 148 |
| Port                       | filtering                                  |                   | 150 |
| Portfilteringcommands      |                                            |                   | 150 |
|                            | portfilter                                 |                   | 150 |
|                            | showportfilter                             |                   | 151 |
| DNS                        |                                            |                   | 154 |
| DNSclient                  |                                            |                   | 154 |
| ConfiguringtheDNSclient    |                                            |                   | 154 |
| DNSclientcommands          |                                            |                   | 155 |
|                            | ipdnsdomain-list                           |                   | 155 |
|                            | ipdnsdomain-name                           |                   | 156 |
|                            | ipdnshost                                  |                   | 157 |
|                            | ipdnsserveraddress                         |                   | 158 |
|                            | showipdns                                  |                   | 159 |
| Device                     | discovery                                  | and configuration | 162 |
| LLDP                       |                                            |                   | 162 |
|                            | LLDPagent                                  |                   | 162 |
|                            | LLDPMEDsupport                             |                   | 164 |
|                            | LLDPEEE                                    |                   | 165 |
|                            | ConfiguringtheLLDPagent                    |                   | 165 |
|                            | LLDPcommands                               |                   | 166 |
|                            | clearlldpneighbors                         |                   | 166 |
|                            | clearlldpstatistics                        |                   | 166 |
|                            | lldp                                       |                   | 167 |
|                            | lldpdot3                                   |                   | 167 |
|                            | lldpholdtime-multiplier                    |                   | 168 |
|                            | lldpmanagement-ipv4-address                |                   | 169 |
|                            | lldpmanagement-ipv6-address                |                   | 170 |
|                            | lldpmed                                    |                   | 171 |
|                            | lldpmed-location                           |                   | 172 |
|                            | lldpreceive                                |                   | 173 |
|                            | lldpreinit                                 |                   | 174 |
|                            | lldpselect-tlv                             |                   | 175 |
|                            | lldptimer                                  |                   | 176 |
|                            | lldptransmit                               |                   | 177 |
|                            | lldptxdelay                                |                   | 178 |
|                            | lldptrapenable                             |                   | 179 |
|                            | showlldpconfiguration                      |                   | 181 |
|                            | showlldpconfigurationmgmt                  |                   | 182 |
|                            | showlldplocal-device                       |                   | 183 |
|                            | showlldpneighbor-info                      |                   | 185 |
|                            | showlldpneighbor-infodetail                |                   | 188 |
|                            | showlldpneighbor-infomgmt                  |                   | 190 |
|7

|                                    | showlldpstatistics     |              |          | 192 |
| ---------------------------------- | ---------------------- | ------------ | -------- | --- |
|                                    | showlldpstatisticsmgmt |              |          | 193 |
|                                    | showlldptlv            |              |          | 194 |
| CiscoDiscoveryProtocol(CDP)        |                        |              |          | 194 |
|                                    | CDPsupport             |              |          | 195 |
|                                    | CDPcommands            |              |          | 195 |
|                                    | cdp                    |              |          | 195 |
|                                    | clearcdpcounters       |              |          | 196 |
|                                    | clearcdpneighbor-info  |              |          | 197 |
|                                    | showcdp                |              |          | 197 |
|                                    | showcdpneighbor-info   |              |          | 198 |
|                                    | showcdptraffic         |              |          | 199 |
| Zero                               | Touch Provisioning     |              |          | 200 |
| ZTPsupport                         |                        |              |          | 200 |
| SettingupZTPonatrustednetwork      |                        |              |          | 201 |
| ZTPprocessduringswitchboot         |                        |              |          | 202 |
| ZTPVSFswitchoversupport            |                        |              |          | 203 |
| ZTPcommands                        |                        |              |          | 203 |
|                                    | showztpinformation     |              |          | 203 |
|                                    | ztpforceprovision      |              |          | 207 |
| Switch                             | system                 | and hardware | commands | 209 |
| bluetoothdisable                   |                        |              |          | 209 |
| bluetoothenable                    |                        |              |          | 209 |
| clearevents                        |                        |              |          | 210 |
| cleariperrors                      |                        |              |          | 211 |
| consolebaud-rate                   |                        |              |          | 212 |
| domain-name                        |                        |              |          | 213 |
| fabricadmin-state                  |                        |              |          | 213 |
| hostname                           |                        |              |          | 214 |
| ledlocator                         |                        |              |          | 215 |
| moduleadmin-state                  |                        |              |          | 216 |
| moduleproduct-number               |                        |              |          | 217 |
| mtrace                             |                        |              |          | 219 |
| showbluetooth                      |                        |              |          | 220 |
| showboot-history                   |                        |              |          | 222 |
| showcapacities                     |                        |              |          | 224 |
| showcapacities-status              |                        |              |          | 225 |
| showconsole                        |                        |              |          | 226 |
| showcore-dump                      |                        |              |          | 227 |
| showdomain-name                    |                        |              |          | 229 |
| showenvironmentfan                 |                        |              |          | 229 |
| showenvironmentled                 |                        |              |          | 231 |
| showenvironmentpower-consumption   |                        |              |          | 232 |
| showenvironmentpower-supply        |                        |              |          | 234 |
| showenvironmentrear-display-module |                        |              |          | 235 |
| showenvironmenttemperature         |                        |              |          | 236 |
| showevents                         |                        |              |          | 237 |
| showfabric                         |                        |              |          | 240 |
| showhostname                       |                        |              |          | 241 |
| showimages                         |                        |              |          | 242 |
| showiperrors                       |                        |              |          | 243 |
| showmodule                         |                        |              |          | 245 |
| showrunning-config                 |                        |              |          | 247 |
| showrunning-configcurrent-context  |                        |              |          | 250 |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 8

| showstartup-config                       |                    |           | 252 |
| ---------------------------------------- | ------------------ | --------- | --- |
| showsystemerror-counter-monitor          |                    |           | 253 |
| showsystem                               |                    |           | 255 |
| showsystemresource-utilization           |                    |           | 256 |
| showtech                                 |                    |           | 257 |
| showusb                                  |                    |           | 259 |
| showusbfile-system                       |                    |           | 260 |
| showversion                              |                    |           | 261 |
| systemerror-counter-monitor              |                    |           | 262 |
| systemerror-counter-monitorpoll-interval |                    |           | 263 |
| systemresource-utilizationpoll-interval  |                    |           | 263 |
| topcpu                                   |                    |           | 264 |
| topmemory                                |                    |           | 265 |
| usb                                      |                    |           | 265 |
| usbmount|unmount                         |                    |           | 266 |
| Support                                  | and Other          | Resources | 268 |
| AccessingHPEArubaNetworkingSupport       |                    |           | 268 |
| AccessingUpdates                         |                    |           | 269 |
|                                          | ArubaSupportPortal |           | 269 |
|                                          | MyNetworking       |           | 269 |
| WarrantyInformation                      |                    |           | 269 |
| RegulatoryInformation                    |                    |           | 270 |
| DocumentationFeedback                    |                    |           | 270 |
|9

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 8400 Switch Series (JL375A, JL376A)

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

|

{ }

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

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

10

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
| On the 8400 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|11

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

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

12

Chapter 2

About AOS-CX

About AOS-CX

AOS-CX is a new, modern, fully programmable operating system built using a database-centric design
that ensures higher availability and dynamic software process changes for reduced downtime. In
addition to robust hardware reliability, the AOS-CX operating system includes additional software
elements not available with traditional systems, including:

n Automated visibility to help IT organizations scale: The Aruba Network Analytics Engine allows IT to
monitor and troubleshoot network, system, application, and security-related issues easily through
simple scripts. This engine comes with a built-in time series database that enables customers and
developers to create software modules that allow historical troubleshooting, as well as analysis of
historical trends to predict and avoid future problems due to scale, security, and performance
bottlenecks.

n Programmability simplified: A switch that is running the AOS-CX operating system is fully

programmable with a built-in Python interpreter as well as REST-based APIs, allowing easy integration
with other devices both on premise and in the cloud. This programmability accelerates IT
organization understanding of and response to network issues. The database holds all aspects of the
configuration, statistics, and status information in a highly structured and fully defined form.

n Faster resolution with network insights: With legacy switches, IT organizations must troubleshoot

problems after the fact, using traditional tools like CLI and SNMP, augmented by separate, expensive
monitoring, analytics, and troubleshooting solutions. These capabilities are built in to the AOS-CX
operating system and are extensible.

n High availability: For switches that support active and standby management modules, the AOS-CX

database can synchronize data between active and standby modules and maintain current
configuration and state information during a failover to the standby management module.

n Ease of roll-back to previous configurations: The built-in database acts as a network record, enabling
support for multiple configuration checkpoints and the ability to roll back to a previous configuration
checkpoint.

AOS-CX system databases

The AOS-CX operating system is a modular, database-centric operating system. Every aspect of the
switch configuration and state information is modeled in the AOS-CX switch configuration and state
database, including the following:

n Configuration information

n Status of all features

n Statistics

The AOS-CX operating system also includes a time series database, which acts as a built-in network
record. The time series database makes the data seamlessly available to Aruba Network Analytics Engine
agents that use rules that evaluate network conditions over time. Time-series data about the resources
monitored by agents are automatically collected and presented in graphs in the switch Web UI.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

13

Aruba Network Analytics Engine introduction

The Aruba Network Analytics Engine is a first-of-its-kind built-in framework for network assurance and
remediation. Combining the full automation and deep visibility capabilities of the AOS-CX operating
system, this unique framework enables monitoring, collecting network data, evaluating conditions, and
taking corrective actions through simple scripting agents.

This engine is integrated with the AOS-CX system configuration and time series databases, enabling you
to examine historical trends and predict future problems due to scale, security, and performance
bottlenecks. With that information, you can create software modules that automatically detect such
issues and take appropriate actions.

With the faster network insights and automation provided by the Aruba Network Analytics Engine, you
can reduce the time spent on manual tasks and address current and future demands driven by Mobility
and IoT.

AOS-CX CLI

The AOS-CX CLI is an industry standard text-based command-line interface with hierarchical structure
designed to reduce training time and increase productivity in multivendor installations.

The CLI gives you access to the full set of commands for the switch while providing the same password
protection that is used in the Web UI. You can use the CLI to configure, manage, and monitor devices
running the AOS-CX operating system.

Aruba CX mobile app

The Aruba CX mobile app enables you to use a mobile device to configure or access a supported AOS-CX
switch. You can connect to the switch through Bluetooth or Wi-Fi.

You can use this application to do the following:

n Connect to the switch for the first time and configure basic operational settings—all without

requiring you to connect a terminal emulator to the console port.

n View and change the configuration of individual switch features or settings.

n Manage the running configuration and startup configuration of the switch, including the following:

o Transferring files between the switch and your mobile device

o Sharing configuration files from your mobile device

o Copying the running configuration to the startup configuration

n Access the switch CLI.

For more information about the Aruba CX mobile app, see:

www.arubanetworks.com/products/networking/switches/cx-mobileapp.

Aruba NetEdit

Aruba NetEdit enables the automation of multidevice configuration change workflows without the
overhead of programming.

The key capabilities of NetEdit include the following:

n Intelligent configuration with validation for consistency and compliance

n Time savings by simultaneously viewing and editing multiple configurations

About AOS-CX | 14

n Customized validation tests for corporate compliance and network design

n Automated large-scale configuration deployment without programming

n Ability to track changes to hardware, software, and configurations (whether made through NetEdit or

directly on the switch) with automated versioning

For more information about Aruba NetEdit, search for NetEdit at the following website:

www.hpe.com/support/hpesc

Ansible modules

Ansible is an open-source IT automation platform.

Aruba publishes a set of Ansible configuration management modules designed for switches running
AOS-CX software. The modules are available from the following places:

n The arubanetworks.aoscx_role role in the Ansible Galaxy at:

https://galaxy.ansible.com/arubanetworks/aoscx_role

n The aoscx-ansible-role at the following GitHub repository: https://github.com/aruba/aoscx-ansible-

role

AOS-CX Web UI

The Web UI gives you quick and easy visibility into what is happening on your switch, providing faster
problem detection, diagnosis, and resolution. The Web UI provides dashboards and views to monitor
the status of the switch, including easy to read indicators for: power supply, temperature, fans, CPU use,
memory use, log entries, system information, firmware, interfaces, VLANs, and LAGs. In addition, you
use the Web UI to access the Network Analytics Engine, run certain diagnostics, and modify some
aspects of the switch configuration.

AOS-CX REST API

Switches running the AOS-CX software are fully programmable with a REST (REpresentational State
Transfer) API, allowing easy integration with other devices both on premises and in the cloud. This
programmability—combined with the Aruba Network Analytics Engine—accelerates network
administrator understanding of and response to network issues.

The AOS-CX REST API enables programmatic access to the AOS-CX configuration and state database at
the heart of the switch. By using a structured model, changes to the content and formatting of the CLI
output do not affect the programs you write. And because the configuration is stored in a structured
database instead of a text file, rolling back changes is easier than ever, thus dramatically reducing a risk
of downtime and performance issues.

The AOS-CX REST API is a web service that performs operations on switch resources using HTTPS POST,
GET, PUT, and DELETE methods.

A switch resource is indicated by its Uniform Resource Identifier (URI). A URI can be made up of several
components, including the host name or IP address, port number, the path, and an optional query
string. The AOS-CX operating system includes the AOS-CX REST API Reference, which is a web interface
based on the Swagger UI. The AOS-CX REST API Reference provides the reference documentation for the
REST API, including resources URIs, models, methods, and errors. The AOS-CX REST API Reference shows
most of the supported read and write methods for all switch resources.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

15

In-band and out-of-band management

Management communications with a managed switch can be either of the following:

In band

In-band management communications occur through ports on the line modules of the switch, using
common communications protocols such as SSH and SNMP.

When you use an in-band management connection, management traffic from that connection uses
the same network infrastructure as user data. User data uses the data plane, which is responsible
for moving data from source to destination. Management traffic that uses the data plane is more
likely to be affected by traffic congestion and other issues affecting the user network.

Out of band

OOBM (out-of-band management) communications occur through a dedicated serial or USB console
port or though a dedicated networked management port.

OOBM operates on a management plane that is separate from the data plane used by data traffic on
the switch and by in-band management traffic. That separation means that OOBM can continue to
function even during periods of traffic congestion, equipment malfunction, or attacks on the
network. In addition, it can provide improved switch security: a properly configured switch can limit
management access to the management port only, preventing malicious attempts to gain access
through the data ports.

Networked OOBM typically occurs on a management network that connects multiple switches. It has
the added advantage that it can be done from a central location and does not require an individual
physical cable from the management station to the console port of each switch.

SNMP-based management support

The AOS-CX operating system provides SNMP read access to the switch. SNMP support includes support
of industry-standard MIB (Management Information Base) plus private extensions, including SNMP
events, alarms, history, statistics groups, and a private alarm extension group. SNMP access is disabled
by default.

User accounts

To view or change configuration settings on the switch, users must log in with a valid account.
Authentication of user accounts can be performed locally on the switch, or by using the services of an
external TACACS+ or RADIUS server.

Two types of user accounts are supported:

n Operators: Operators can view configuration settings, but cannot change them. No operator

accounts are created by default.

n Administrators: Administrators can view and change configuration settings. A default locally stored

administrator account is created with username set to admin and no password. You set the
administrator account password as part of the initial configuration procedure for the switch.

About AOS-CX | 16

Chapter 3

Initial Configuration

Initial Configuration

Perform the initial configuration of a factory default switch using one of the following methods:

n Load a switch configuration using zero-touch provisioning (ZTP). When ZTP is used, the configuration
is loaded from a server automatically when the switch booted from the factory default configuration.

n Connect to the switch wirelessly with a mobile device through Bluetooth, and use the Aruba CX

Mobile App to deploy an initial configuration from a provided template. The template you choose
during the deployment process determines how the management interface is configured. Optionally,
as the final deployment step, you can select to import the switch into NetEdit through a WiFI
connection to the NetEdit server.

Alternatively, you can use the Aruba CX Mobile App to manually configure switch settings and features
for a subset of the features you can configure using the CLI. You can also access the CLI through the
mobile application.

n Connect the management port on the switch to your network, and then use SSH client software to

reach the switch from a computer connected to the same network. This requires that a DHCP server
is installed on the network. Configure switch settings and features by executing CLI commands.

n Connect a computer running terminal emulation software to the console port on the switch.

Configure switch settings and features by executing CLI commands.

Initial configuration using ZTP

Zero Touch Provisioning (ZTP) configures a switch automatically from a remote server.

Prerequisites

n The switch must be in the factory default configuration.

Do not change the configuration of the switch from its factory default configuration in any way, including
by setting the administrator password.

n Your network administrator or installation site coordinator must provide a Category 6 (Cat6) cable

connected to the network that provides access to the servers used for Zero Touch Provisioning (ZTP)
operations.

Procedure

1. Connect the network cable to the out-of-band management port on the switch.

See the Installation Guide for switch to determine the location of the switch ports.

2.

If the switch is powered on, power off the switch.

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image
is being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

Initial configuration using the Aruba CX mobile app

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

17

This procedure describes how to use your mobile device to connect to the Bluetooth interface of the
switch to connect to the switch for the first time so that you can configure basic operational settings
using the Aruba CX mobile app.

Prerequisites

n You have obtained the USB Bluetooth adapter that was shipped with the switch. Information about
the make and model of the supported adapter is included in the information about the Aruba CX
mobile app in the Apple Store or Google Play.

n The Aruba CX mobile app must be installed on your mobile device.

n Bluetooth must be enabled on your mobile device.

n Your mobile device must be within the communication range of the Bluetooth adapter.

n If you are planning to import the switch into NetEdit, your mobile device must be able to use a Wi-Fi

connection—not Bluetooth—to access the NetEdit server.

If your mobile device does not support simultaneous Bluetooth and Wi-Fi connections, you must use
the NetEdit interface to import the switch at a later time. You can use the Devices tab to display the IP
address of the switches you configured using your mobile device.

n The switch must be installed and powered on, with the network operating system boot sequence

complete.

For information about installing and powering on the switch, see the Installation Guide for the switch.

Because you are using this mobile application to configure the switch through the Bluetooth interface, it
is not necessary to connect a console to the switch.

n Bluetooth and USB must be enabled on the switch. On switches shipped from the factory, Bluetooth

and USB are enabled by default.

Procedure

1.

Install the USB Bluetooth adapter in the USB port of the switch.

For switches that have multiple management modules, you must install the USB Bluetooth
adapter in the USB port of the active management module. Typically, the active management
module is the module in slot 5.

Switches shipped from the factory have both USB and Bluetooth enabled by default.

For information about the location of the USB port on the switch, see the Installation Guide for the
switch.

2. Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile

device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following
format:
Switch_model - Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify
that it be used for Internet access.

3. Open the Aruba CX mobile app on your mobile device.

;" />

Initial Configuration | 18

The application attempts to connect to the switch using the switch Bluetooth IP address and
the default switch login credentials. The Home screen of the application shows the status of
the connection to the switch:

n If the login attempt was successful, the Bluetooth icon is displayed and the status message

shows the Bluetooth IP address of the switch. In addition, the connection graphic is green. You
can continue to the next step.

n If the login attempt was not successful, but a response was received, the Bluetooth icon is
displayed, but the status message is: Login Required. You can continue to the next step.
When you tap one of the tiles, you will be prompted for login credentials.

n If the login attempt did not receive a response, the Bluetooth icon is not displayed, and the

status message is: No Connection.

4. Create the initial switch configuration:

n You can deploy an initial configuration to the switch. Through this process, you supply the
information required by a configuration template that you choose from a list of templates
provided by the application. Then you deploy the configuration to the switch and, optionally,
import the switch into NetEdit.

When you deploy a switch configuration, it becomes the running configuration, replacing the

entire existing configuration of the switch. All changes previously made to the factory default

configuration are overwritten.

If you plan to both deploy a switch configuration and customize the configuration of switch

features, deploy the initial configuration first.

To deploy an initial switch configuration, tap: Initial Config and follow the instructions in the
application.

n Alternatively, you can complete the initial configuration of the switch by tapping Modify

Config and then selecting the features and settings to configure.

n You can also use the Modify Config feature to configure some switch features after the initial

configuration is complete. For more information about what you can configure using the
Aruba CX mobile app, see the online help for the application.

Troubleshooting Bluetooth connections

Bluetooth connection IP addresses

The Bluetooth connection uses IP addresses in the 192.168.99.0/24 subnet.

Switch

192.168.99.1

Mobile device

192.168.99.10

Bluetooth is connected but the switch is not reachable

Symptom

The mobile device settings indicate that the device is connected to the switch through Bluetooth.
However, the mobile application indicates that the switch is not reachable.

Solution 1

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

19

Cause

The mobile device is paired with a different nearby switch.

Action

1. Verify the model number and serial number of the switch to which you are attempting to

connect.

2. Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile

device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify that it
be used for Internet access.

Solution 2

Cause

The mobile device is connected to a different network—such as through a Wi-Fi connection—that
conflicts with the subnet used for the switch Bluetooth connection.

Action

Disconnect the mobile device from the network that is using the conflicting subnet.

For example, use the mobile device settings to turn off or disable Wi-Fi. If you choose to disable Wi-Fi on
the mobile device, and you are not able to access cellular service, you will not be able to connect to the
NetEdit server to import the switch, but you can still deploy a switch configuration.

Bluetooth is not connected

Symptom

Your mobile device cannot establish a Bluetooth connection to the switch.

Solution 1

Cause

Bluetooth is not enabled on your mobile device.

Action

n Use your mobile device settings application to enable Bluetooth.

n Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile

device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify that it
be used for Internet access.

Solution 2

Initial Configuration | 20

Cause

Your mobile device is not within the broadcast range of the Bluetooth adapter.

Action

Move closer to the switch.

Devices can communicate through Bluetooth when they are close, typically within a few feet of each
other.

Solution 3

Cause

Your mobile device is not paired with the switch.

Action

1. Use your mobile device settings application to enable Bluetooth.

2. Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile

device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following
format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

3. On some Android devices, you might need to change the settings of the paired device to specify

that it be used for Internet access.

Solution 4

Cause

Bluetooth is not enabled on the switch.

New switches are shipped from the factory with the USB port and Bluetooth enabled. However, an
installed switch might have been configured to disable Bluetooth or disable the USB port, which the USB
Bluetooth adapter uses.

Action

Use a different CLI connection to enable Bluetooth on the switch.

n Use the show bluetooth CLI command to show the Bluetooth configuration and the status of the

Bluetooth adapter.

n To enable the USB port, enter the CLI command: usb

n An inserted USB drive must be mounted each time the switch boots or fails over to a different

management module. To mount the drive, enter the CLI command: usb mount

n To enable Bluetooth, enter the CLI command: bluetooth enable

Solution 5

Cause

Another mobile device has already connected to the switch through Bluetooth. This cause is likely if
your device is repeatedly disconnected within 1-2 seconds of establishing a connection.

Action

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

21

1. Use a different CLI connection to see if there is another device connected:

Use the show bluetooth CLI command to show the Bluetooth configuration and the status of the
Bluetooth adapter.

2. Either disconnect the other device or use that device to communicate with the switch.

A switch can use Bluetooth to connect to one mobile device at a time.

Solution 6

Cause

The switch has been restarted since the mobile device was last paired with the switch, and the device is
having difficulty establishing the Bluetooth connection.

Action

1. Use the Bluetooth mobile device settings to forget the switch device.

2. Use your mobile device settings application to disable Bluetooth.
Use your mobile device settings application to enable Bluetooth.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following
format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify
that it be used for Internet access.

Solution 7

Cause

The USB Bluetooth adapter is not installed in the switch.

If the switch has multiple management modules, the USB Bluetooth adapter might be installed in the
management module that is not the active management module.

Action

Install the USB Bluetooth adapter in the USB port of the switch.

For switches that have multiple management modules, you must install the USB Bluetooth adapter in
the USB port of the active management module. Typically, for new switches, the active management
module is the module in slot 5 (Aruba 8400 switches) or slot 1 (Aruba 6400 switches).

For information about the location of the USB port on the switch, see the Installation Guide for the
switch.

Solution 8

Cause

A problem occurred with the Bluetooth feature on the switch. For example, the software daemon was
stopped and then restarted.

Action

Initial Configuration | 22

1. Use a different connection to the switch CLI to disable and then enable Bluetooth.

switch(config)# bluetooth disable
switch(config)# bluetooth enable

2. Use the Bluetooth mobile device settings to forget the switch device.

3. Use your mobile device settings application to disable Bluetooth.

4. Use your mobile device settings application to enable Bluetooth.

5. Use your mobile device settings application to enable Bluetooth.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following
format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify
that it be used for Internet access.

Solution 9

Cause

A switch that is member of a stack (but is not the conductor switch), has a USB Bluetooth adapter
installed, but mobile application has lost contact with that switch.

Action

Remove and then reinstall the USB Bluetooth adapter.

Do not remove the USB Bluetooth adapter from the conductor switch.

Initial configuration using the CLI

This procedure describes how to connect to the switch for the first time and configure basic operational
settings using the CLI. In this procedure, you use a computer to connect to the switch using the either
the console port or management port.

Procedure

1. Connect to the console port or the management port.

2. Log into the switch for the first time.

3. Configure switch time using the NTP client.

Connecting to the console port

Prerequisites

n A switch installed as described in its hardware installation guide.

n A computer with terminal emulation software.

n A JL448A Aruba X2 C2 RJ45 to DB9 console cable.

Procedure

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

23

1. Connecttheconsoleportontheswitchtotheserialportonthecomputerusingaconsolecable.
2. Starttheterminalemulationsoftwareonthecomputerandconfigureanewserialsessionwith
thefollowingsettings:
| n   | Speed:115200bps |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- |
| n   | Databits:8      |     |     |     |     |
| n   | Stopbits:1      |     |     |     |     |
| n   | Parity:None     |     |     |     |     |
Flowcontrol:None
n
3. Starttheterminalemulationsession.
4. PressEnteronce.Iftheconnectionissuccessful,youarepromptedtologin.
| Optional | console | port | speed setting |     |     |
| -------- | ------- | ---- | ------------- | --- | --- |
Ifdesired,theconsoleportspeedcanbesetwiththeconsole baud-ratecommand.Forexample,
settingtheconsoleportspeedto9600bps:
| switch(config)# |     |     | console baud-rate | 9600 |     |
| --------------- | --- | --- | ----------------- | ---- | --- |
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
| settings |     | are updated | to match the | baud rate | of the switch. |
| -------- | --- | ----------- | ------------ | --------- | -------------- |
| Continue |     | (y/n)?      | y            |           |                |
Showingtheconsoleportcurrentspeed:
| switch# | show  | console |     |     |     |
| ------- | ----- | ------- | --- | --- | --- |
| Baud    | Rate: | 9600    |     |     |     |
Fordetailsontheconsole baud-rateandshow consolecommands,seeSwitchsystemandhardware
commands.
| Connecting |     | to the | management | port |     |
| ---------- | --- | ------ | ---------- | ---- | --- |
Prerequisites
n TwoEthernetcables
n SSHclientsoftware
Procedure
1. Bydefault,themanagementinterfaceissettoautomaticallyobtainanIPaddressfromaDHCP
server,andSSHsupportisenabled.IfthereisnoDHCPserveronyournetwork,youmust
configureastaticaddressonthemanagementinterface:
|     | a. Connecttotheconsoleport          |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- |
|     | b. Configurethemanagementinterface. |     |     |     |     |
2. UseanEthernetcabletoconnectthemanagementporttoyournetwork.
3. UseanEthernetcabletoconnectyourcomputertothesamenetwork.
4. StartyourSSHclientsoftwareandconfigureanewsessionusingtheaddressassignedtothe
managementinterface.(IfthemanagementinterfaceissettooperateasaDHCPclient,retrieve
InitialConfiguration |24

theIPaddressassignedtothemanagementinterfacefromyourDHCPserver.)
5. Startthesession.Iftheconnectionissuccessful,youarepromptedtologin.
| Logging | into | the switch | for | the first | time |
| ------- | ---- | ---------- | --- | --------- | ---- |
Thefirsttimeyoulogintotheswitchyoumustusethedefaultadministratoraccount.Thisaccounthas
nopassword,soyouwillbepromptedonlogintodefineonetosafeguardtheswitch.
Procedure
1. Whenpromptedtologin,specifyadmin.Whenpromptedforthepassword,pressENTER.(By
default,nopasswordisdefined.)
Forexample:
|     | switch | login: admin |     |     |     |
| --- | ------ | ------------ | --- | --- | --- |
password:
2. Defineapasswordfortheadminaccount.Thepasswordcancontainupto32alphanumeric
charactersintherangeASCII32to127,whichincludesspecialcharacterssuchasasterisk(*),
ampersand(&),exclamationpoint(!),dash(-),underscore(_),andquestionmark(?).
Forexample:
|     | Please    | configure     | the 'admin' | user account | password. |
| --- | --------- | ------------- | ----------- | ------------ | --------- |
|     | Enter new | password:     | *******     |              |           |
|     | Confirm   | new password: | *******     |              |           |
switch#
3. Youareplacedintothemanagercommandcontext,whichisidentifiedbytheprompt:switch#,
whereswitchisthemodelnumberoftheswitch.Enterthecommandconfigtochangetothe
globalconfigurationcontextconfig.
Forexample:
|     | switch# | config |     |     |     |
| --- | ------- | ------ | --- | --- | --- |
switch(config)#
| Setting | switch | time | using the | NTP | client |
| ------- | ------ | ---- | --------- | --- | ------ |
Prerequisites
n TheIPaddressordomainnameofanNTPserver.
n IftheNTPserverusesauthentication,obtainthepasswordrequiredtocommunicatewiththeNTP
server.
Procedure
1. IftheNTPserverrequiresauthentication,definetheauthenticationkeyfortheNTPclientwiththe
|     | commandntp | authentication. |     |     |     |
| --- | ---------- | --------------- | --- | --- | --- |
2. ConfigureanNTPserverwiththecommandntp server.Whenconfiguringatimebackward
morethanfiveminutes,arebootisrecommendedtoavoidunusualswitchbehavior.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 25

3. Bydefault,NTPtrafficissentonthedefaultVRF.IfyouwanttosendNTPtrafficonthe
|     | managementVRF,usethecommandntp |     |     |     |     | vrf. |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
4. ReviewyourNTPconfigurationsettingswiththecommandsshow ntp serversandshow ntp
status.
5. Seethecurrentswitchtime,date,andtimezonewiththecommandshow clock.
Example
Thisexamplecreatesthefollowingconfiguration:
n Definestheauthenticationkey1withthepasswordmyPassword.
n DefinestheNTPservermy-ntp.mydomain.comandmakesitthepreferredserver.
n SetstheswitchtousethemanagementVRF(mgmt)forallNTPtraffic.
| switch(config)# |     |         | ntp authentication-key |                     |     | 1   | md5 myPassword |        |        |     |
| --------------- | --- | ------- | ---------------------- | ------------------- | --- | --- | -------------- | ------ | ------ | --- |
| switch(config)# |     |         | ntp server             | my-ntp.mydomain.com |     |     |                | key 10 | prefer |     |
| switch(config)# |     |         | ntp vrf                | mgmt                |     |     |                |        |        |     |
| Configuring     |     | banners |                        |                     |     |     |                |        |        |     |
1. Configurethebannerthatisdisplayedwhenauserconnectstoamanagementinterface.Usethe
|     | commandbanner   |     | motd.Forexample: |      |     |     |     |     |     |     |
| --- | --------------- | --- | ---------------- | ---- | --- | --- | --- | --- | --- | --- |
|     | switch(config)# |     | banner           | motd | ^   |     |     |     |     |     |
Enter a new banner. Terminate the banner with the delimiter you have chosen.
|     | >> This | is  | an example | of   | a banner     | text | which     | a   | connecting | user |
| --- | ------- | --- | ---------- | ---- | ------------ | ---- | --------- | --- | ---------- | ---- |
|     | >> will | see | before     | they | are prompted |      | for their |     | password.  |      |
>>
|     | >> As   | you can | see        | it may | span | multiple  | lines     | and | the input |     |
| --- | ------- | ------- | ---------- | ------ | ---- | --------- | --------- | --- | --------- | --- |
|     | >> will | be      | terminated | when   | the  | delimiter | character |     | is        |     |
>> encountered.^
|     | Banner | updated | successfully! |     |     |     |     |     |     |     |
| --- | ------ | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
2. Configurethebannerthatisdisplayedafterauserisauthenticated.Usethecommandbanner
exec.Forexample:
|     | switch(config)# |     | banner | exec | &   |     |     |     |     |     |
| --- | --------------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- |
Enter a new banner. Terminate the banner with the delimiter you have chosen.
|     | >> This | is     | an example | of   | a different |           | banner | text. | This     | time |
| --- | ------- | ------ | ---------- | ---- | ----------- | --------- | ------ | ----- | -------- | ---- |
|     | >> the  | banner | entered    | will | be          | displayed | after  | a     | user has |      |
>> authenticated.
>>
>> & This text will not be included because it comes after the '&'
|             | Banner | updated | successfully! |            |     |     |     |     |        |      |
| ----------- | ------ | ------- | ------------- | ---------- | --- | --- | --- | --- | ------ | ---- |
| Configuring |        | in-band |               | management |     |     |     | on  | a data | port |
Prerequisites
InitialConfiguration |26

n AconnectiontotheCLIviaeithertheconsoleportorthemanagementport
n Ethernetcable
Procedure
1. UseanEthernetcabletoconnectadataporttoyournetwork.
2. Configurealayer3interfaceonthedataport.
3. EnableSSHsupportontheinterface(onthedefaultVRF)withthecommandssh server vrf
default.
Forexample:
|     | switch# config  |     |            |             |     |
| --- | --------------- | --- | ---------- | ----------- | --- |
|     | switch(config)# |     | ssh server | vrf default |     |
4. EnabletheWebUIontheinterface(onthedefaultVRF)withthecommandhttps-server vrf
default.
Forexample:
|       | switch(config)# |     | https-server | vrf default |     |
| ----- | --------------- | --- | ------------ | ----------- | --- |
| Using | the             | Web | UI           |             |     |
TheWebUIisdisabledbydefault.Followthesestepstoenableitonthemanagementportandlogin.
TheWebUIisenabledbydefaultonthedefaultVRF.
Prerequisites
n AconnectiontotheswitchCLI.
Procedure
1. LogintotheCLI.
2. SwitchtoconfigcontextandenabletheWebUIonthemanagementportVRFwiththecommand
mgmt.
|     | https-server | vrf |     |     |     |
| --- | ------------ | --- | --- | --- | --- |
Forexample:
|     | switch#         | config |              |     |      |
| --- | --------------- | ------ | ------------ | --- | ---- |
|     | switch(config)# |        | https-server | vrf | mgmt |
3. StartyourwebbrowserandentertheIPaddressofthemanagementportintheaddressbar,
|     | Forexample: | https://192.168.1.1 |     |     |     |
| --- | ----------- | ------------------- | --- | --- | --- |
4. TheWebUIstartsandyouarepromptedtologin.
| Configuring |     | the | management |     | interface |
| ----------- | --- | --- | ---------- | --- | --------- |
Prerequisites
Aconnectiontotheconsoleport.
Procedure
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 27

1. Switchtothemanagementinterfacecontextwiththecommandinterface mgmt.
2. Bydefault,themanagementinterfaceonthemanagementportisenabled.Ifitwasdisabled,re-
| enableitwiththecommandno |     | shutdown. |     |     |     |
| ------------------------ | --- | --------- | --- | --- | --- |
3. Usethecommandip dhcptoconfigurethemanagementinterfacetoautomaticallyobtainan
addressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastaticIPv4or
IPv6address,defaultgateway,andDNSserverwiththecommandsip address,ipv6 address,ip
static,default-gateway,andnameserver.
4. SSHisenabledbydefaultonthemanagementVRF.Ifdisabled,enableSSHwiththecommand
| ssh server | vrf mgmt. |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
Examples
ThisexampleenablesthemanagementinterfacewithdynamicaddressingusingDHCP:
| switch(config)#         | interface | mgmt        |     |     |     |
| ----------------------- | --------- | ----------- | --- | --- | --- |
| switch(config-if-mgmt)# |           | no shutdown |     |     |     |
| switch(config-if-mgmt)# |           | ip dhcp     |     |     |     |
Thisexampleenablesthemanagementinterfacewithstaticaddressingcreatingthefollowing
configuration:
n SetsastaticIPv4addressof198.168.100.10withamaskof24bits.
n Setsthedefaultgatewayto198.168.100.200.
n SetstheDNSserverto198.168.100.201.
| switch(config)#         | interface | mgmt        |     |     |     |
| ----------------------- | --------- | ----------- | --- | --- | --- |
| switch(config-if-mgmt)# |           | no shutdown |     |     |     |
switch(config-if-mgmt)#
|                         |            | ip static       | 198.168.100.10/24 |                 |          |
| ----------------------- | ---------- | --------------- | ----------------- | --------------- | -------- |
| switch(config-if-mgmt)# |            | default-gateway |                   | 198.168.100.200 |          |
| switch(config-if-mgmt)# |            | nameserver      | 198.168.100.201   |                 |          |
| Restoring               | the switch | to              | factory           | default         | settings |
Prerequisites
YouareconnectedtotheswitchthroughitsConsoleport.
ThisprocedureerasesalluserinformationandconfigurationsettingsConsiderbackingupyourrunning
configurationfirst.
1. Optionally,backuptherunningconfigurationwitheithercopy running-config <REMOTE-URL>or
copy running-config <STORAGE-URL>.Thejsonstorageformatisrequiredforlater
configurationrestoration.
2. Switchtotheconfigurationcontextwiththecommandconfig.
3. Erasealluserinformationandconfiguration,restoringtheswitchtoitsfactorydefaultstatewith
thecommanderase all zeroize.EnterYwhenpromptedtocontinue.Theswitchautomatically
restarts.
InitialConfiguration |28

4. Optionallyrestoreyoursavedconfiguration(itmustbeinjsonformat)witheithercopy <REMOTE-
URL> running-configorcopy <STORAGE-URL> running-configfollowedbycopy running-
| config | startup-config. |     |     |     |     |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Example
Backinguptherunningconfigurationtoafileonaremoteserver(usingTFTP),resettingtheswitchtoits
factorydefaultstate,andthenrestoringthesavedconfiguration.
switch# copy running-config tftp://192.168.1.10/backup_cfg json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload |     | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ----------- | ---------- |
100 10340 0 0 100 10340 0 1329k --:--:-- --:--:-- --:--:-- 1329k
100 10340 0 0 100 10340 0 1313k --:--:-- --:--:-- --:--:-- 1313k
switch#
switch#
| switch# | erase | all zeroize |     |     |     |     |     |     |     |
| ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the
| switch unavailable |         |         | until  | the zeroization  |        |     | is complete. |              |     |
| ------------------ | ------- | ------- | ------ | ---------------- | ------ | --- | ------------ | ------------ | --- |
| This should        | take    | several |        | minutes          | to     | one | hour         | to complete. |     |
| Continue           | (y/n)?  | y       |        |                  |        |     |              |              |     |
| The system         | is      | going   | down   | for zeroization. |        |     |              |              |     |
| [  OK ]            | Stopped | PSPO    | Module | Daemon.          |        |     |              |              |     |
| [  OK ]            | Stopped | AOS-CX  |        | Switch           | Daemon | for | BCM.         |              |     |
...
| [  OK ]   | Stopped      | Remount |                                                   | Root      | and Kernel |     | File | Systems. |     |
| --------- | ------------ | ------- | ------------------------------------------------- | --------- | ---------- | --- | ---- | -------- | --- |
| [  OK ]   | Reached      | target  |                                                   | Shutdown. |            |     |      |          |     |
| reboot:   | Restarting   |         | system                                            |           |            |     |      |          |     |
| Press Esc | for          | boot    | options                                           |           |            |     |      |          |     |
| ServiceOS | Information: |         |                                                   |           |            |     |      |          |     |
| Version:  |              |         | GT.01.03.0006                                     |           |            |     |      |          |     |
| Build     | Date:        |         | 2018-10-30                                        |           | 14:20:44   |     | PDT  |          |     |
| Build     | ID:          |         | ServiceOS:GT.01.03.0006:8ee0faaa52da:201810301420 |           |            |     |      |          |     |
| SHA:      |              |         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx          |           |            |     |      |          |     |
...
| ################ |     | Preparing |        | for         | zeroization                 |                         | ################# |            |     |
| ---------------- | --- | --------- | ------ | ----------- | --------------------------- | ----------------------- | ----------------- | ---------- | --- |
| ################ |     | Storage   |        | zeroization |                             | ####################### |                   |            |     |
| ################ |     | WARNING:  |        | DO NOT      | POWER                       | OFF                     | UNTIL             | ########## |     |
| ################ |     |           |        | ZEROIZATION |                             | IS                      | COMPLETE          | ########## |     |
| ################ |     | This      | should | take        | several                     |                         | minutes           | ########## |     |
| ################ |     | to        | one    | hour to     | complete                    |                         |                   | ########## |     |
| ################ |     | Restoring |        | files       | ########################### |                         |                   |            |     |
Boot Profiles:
| 0. Service   | OS       | Console |       |                 |     |     |     |     |     |
| ------------ | -------- | ------- | ----- | --------------- | --- | --- | --- | --- | --- |
| 1. Primary   | Software |         | Image | [XL.10.02.0010] |     |     |     |     |     |
| 2. Secondary | Software |         | Image | [XL.10.02.0010] |     |     |     |     |     |
Select profile(primary):
| Booting   | primary  | software |     | image... |     |     |     |     |     |
| --------- | -------- | -------- | --- | -------- | --- | --- | --- | --- | --- |
| Verifying | Image... |          |     |          |     |     |     |     |     |
Image Info:
Name: AOS-CX
| Version: |     | XL.10.02.0010 |     |     |     |     |     |     |     |
| -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 29

Build Id: AOS-CX:XL.10.02.0010:feaf5b9b7f09:201901292014
| Build Date:      | 2019-01-29 | 12:43:50 | PST |     |     |
| ---------------- | ---------- | -------- | --- | --- | --- |
| Extracting       | Image...   |          |     |     |     |
| Loading Image... |            |          |     |     |     |
Done.
| kexec_core: | Starting new | kernel |     |     |     |
| ----------- | ------------ | ------ | --- | --- | --- |
| System is   | initializing |        |     |     |     |
fips_post_check[5473]: FIPS_POST: Cryptographic selftest started...SUCCESS
| [  OK ] | Started Login | banner | readiness check. |     |     |
| ------- | ------------- | ------ | ---------------- | --- | --- |
...
| 8400X login: | admin |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- |
Password:
switch#
switch#
switch# copy tftp://192.168.1.10/backup_cfg running-config json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     | Dload Upload | Total Spent | Left Speed |
| --- | --- | --- | ------------ | ----------- | ---------- |
100 10340 100 10340 0 0 2858k 0 --:--:-- --:--:-- --:--:-- 2858k
100 10340 100 10340 0 0 2804k 0 --:--:-- --:--:-- --:--:-- 2804k
Large configuration changes will take time to process, please be patient.
switch#
switch#
| switch# copy | running-config | startup-config |     |     |     |
| ------------ | -------------- | -------------- | --- | --- | --- |
Large configuration changes will take time to process, please be patient.
switch#
| Management | interface |     | commands |     |     |
| ---------- | --------- | --- | -------- | --- | --- |
default-gateway
| default-gateway    | <IP-ADDR> |     |     |     |     |
| ------------------ | --------- | --- | --- | --- | --- |
| no default-gateway | <IP-ADDR> |     |     |     |     |
Description
AssignsanIPv4orIPv6defaultgatewaytothemanagementinterface.AnIPv4defaultgatewaycanonly
beconfiguredifastaticIPv4addresswasassignedtothemanagementinterface.AnIPv6default
gatewaycanonlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.The
defaultgatewayshouldbeonthesamenetworksegment.
Thenoformofthiscommandremovesthedefaultgatewayfromthemanagementinterface.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
SettingadefaultgatewaywiththeIPv4addressof198.168.5.1:
InitialConfiguration |30

| switch(config)# | interface | mgmt |     |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-mgmt)#
|     |     | default-gateway |     | 198.168.5.1 |
| --- | --- | --------------- | --- | ----------- |
SettinganIPv6addressof2001:DB8::1:
| switch(config)#         | interface | mgmt            |              |             |
| ----------------------- | --------- | --------------- | ------------ | ----------- |
| switch(config-if-mgmt)# |           | default-gateway |              | 2001:DB8::1 |
| Command History         |           |                 |              |             |
| Release                 |           |                 | Modification |             |
| 10.07orearlier          |           |                 | --           |             |
| Command Information     |           |                 |              |             |
| Platforms               | Command   | context         | Authority    |             |
8400 config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip static
| ip static <IP-ADDR>/<MASK> |                  |     |     |     |
| -------------------------- | ---------------- | --- | --- | --- |
| no ip static               | <IP-ADDR>/<MASK> |     |     |     |
Description
AssignsanIPv4orIPv6addresstothemanagementinterface.
ThenoformofthiscommandremovestheIPaddressfromthemanagementinterfaceandsetsthe
interfacetooperateasaDHCPclient.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| <MASK> |     |     | SpecifiesthenumberofbitsinanIPv4orIPv6addressmaskin |     |
| ------ | --- | --- | --------------------------------------------------- | --- |
CIDRformat(x),wherexisadecimalnumberfrom0to32for
IPv4,and0to128forIPv6.
Examples
SettinganIPv4addressof198.51.100.1withamaskof24bits:
| switch(config)#         | interface | mgmt      |                 |     |
| ----------------------- | --------- | --------- | --------------- | --- |
| switch(config-if-mgmt)# |           | ip static | 198.51.100.1/24 |     |
SettinganIPv6addressof2001:DB8::1withamaskof32bits:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 31

| switch(config)# |     | interface |     | mgmt |     |     |
| --------------- | --- | --------- | --- | ---- | --- | --- |
switch(config-if-mgmt)#
|                |             |     | ip      | static | 2001:DB8::1/32 |     |
| -------------- | ----------- | --- | ------- | ------ | -------------- | --- |
| Command        | History     |     |         |        |                |     |
| Release        |             |     |         |        | Modification   |     |
| 10.07orearlier |             |     |         |        | --             |     |
| Command        | Information |     |         |        |                |     |
| Platforms      | Command     |     | context |        | Authority      |     |
8400 config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
nameserver
| nameserver    | <PRIMARY-IP-ADDR> |     |     | [ <SECONDARY-IP-ADDR> |     | ]   |
| ------------- | ----------------- | --- | --- | --------------------- | --- | --- |
| no nameserver | <PRIMARY-IP-ADDR> |     |     | [ <SECONDARY-IP-ADDR> |     | ]   |
Description
AssignsaprimaryorsecondaryIPv4orIPv6DNSservertothemanagementinterface.IPv4DNSservers
canonlybeconfiguredifastaticIPv4addresswasassignedtothemanagementinterface.IPv6DNS
serverscanonlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.The
defaultgatewayshouldbeonthesamenetworksegment.
ThenoformofthiscommandremovestheDNSserversfromthemanagementinterface.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<PRIMARY-IP-ADDR> SpecifiestheIPaddressoftheprimaryDNSserver.Specifythe
addressinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
<SECONDARY-IP-ADDR> SpecifiestheIPaddressofthesecondaryDNSserver.Specifythe
addressinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
SettingprimaryandsecondaryDNSserverswiththeIPv4addressesof198.168.5.1and198.168.5.2:
| switch(config)#         |     | interface |            | mgmt |             |             |
| ----------------------- | --- | --------- | ---------- | ---- | ----------- | ----------- |
| switch(config-if-mgmt)# |     |           | nameserver |      | 198.168.5.1 | 198.168.5.2 |
SettingprimaryandsecondaryDNSserverswiththeIPv6addressesof2001:DB8::1and2001:DB8::2:
InitialConfiguration |32

| switch(config)# |     | interface | mgmt |     |     |
| --------------- | --- | --------- | ---- | --- | --- |
switch(config-if-mgmt)#
|                     |         |     | nameserver | 2001:DB8::1  | 2001:DB8::2 |
| ------------------- | ------- | --- | ---------- | ------------ | ----------- |
| Command History     |         |     |            |              |             |
| Release             |         |     |            | Modification |             |
| 10.07orearlier      |         |     |            | --           |             |
| Command Information |         |     |            |              |             |
| Platforms           | Command |     | context    | Authority    |             |
8400 config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show interface |      | mgmt       |     |     |     |
| -------------- | ---- | ---------- | --- | --- | --- |
| show interface | mgmt | [vsx-peer] |     |     |     |
Description
Showsstatusandconfigurationinformationforthemanagementinterface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# show             | interface  |                 | mgmt |                              |     |
| ------------------------ | ---------- | --------------- | ---- | ---------------------------- | --- |
| Address                  | Mode       |                 |      | : static                     |     |
| Admin State              |            |                 |      | : up                         |     |
| Mac Address              |            |                 |      | : 02:42:ac:11:00:02          |     |
| IPv4 address/subnet-mask |            |                 |      | : 192.168.1.10/16            |     |
| Default                  | gateway    | IPv4            |      | : 192.168.1.1                |     |
| IPv6 address/prefix      |            |                 |      | : 2001:db8:0:1::129/64       |     |
| IPv6 link                | local      | address/prefix: |      | fe80::7272:cfff:fefd:e485/64 |     |
| Default                  | gateway    | IPv6            |      | : 2001:db8:0:1::1            |     |
| Primary                  | Nameserver |                 |      | : 2001::1                    |     |
| Secondary                | Nameserver |                 |      | : 2001::2                    |     |
| Command History          |            |                 |      |                              |     |
| Release                  |            |                 |      | Modification                 |     |
| 10.07orearlier           |            |                 |      | --                           |     |
| Command Information      |            |                 |      |                              |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 33

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
NTP commands
ntp authentication
ntp authentication
no ntp authentication
Description
EnablessupportforauthenticationwhencommunicatingwithanNTPserver.
Thenoformofthiscommanddisablesauthenticationsupport.
Examples
Enablingauthenticationsupport:
| switch(config)# |     | ntp authentication |     |     |     |
| --------------- | --- | ------------------ | --- | --- | --- |
Disablingauthenticationsupport:
| switch(config)#     |         | no ntp authentication |              |     |     |
| ------------------- | ------- | --------------------- | ------------ | --- | --- |
| Command History     |         |                       |              |     |     |
| Release             |         |                       | Modification |     |     |
| 10.07orearlier      |         |                       | --           |     |     |
| Command Information |         |                       |              |     |     |
| Platforms           | Command | context               | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp authentication-key
| ntp authentication-key    |     | <KEY-ID>  | {md5 | sha1} |                 |     |
| ------------------------- | --- | --------- | ------------ | --------------- | --- |
| [{ <PLAINTXT-KEY>         |     | [trusted] | | ciphertext | <ENCRYPTED-KEY> | }]  |
| no ntp authentication-key |     | <KEY-ID>  | {md5 |       | sha1}           |     |
| [{ <PLAINTXT-KEY>         |     | [trusted] | | ciphertext | <ENCRYPTED-KEY> | }]  |
Description
DefinesanauthenticationkeythatisusedtosecuretheexchangewithanNTPtimeserver.This
commandprovidesprotectionagainstaccidentallysynchronizingtoatimesourcethatisnottrusted.
Thenoformofthiscommandremovestheauthenticationkey.
InitialConfiguration |34

| Parameter |     |     | Description                                     |     |     |
| --------- | --- | --- | ----------------------------------------------- | --- | --- |
| <KEY-ID>  |     |     | SpecifiestheauthenticationkeyID.Range:1to65534. |     |     |
| md5       |     |     | SelectsMD5keyencryption.                        |     |     |
| sha1      |     |     | SpecifiesSHA1keyencryption.                     |     |     |
<PLAINTXT-KEY> Specifiestheplaintextauthenticationkey.Range:8to40
characters.ThekeymaycontainprintableASCIIcharacters
excluding"#"orbeenteredinhex.Keyslongerthan20characters
areassumedtobehex.TouseanASCIIkeylongerthan20
characters,convertittohex.
trusted Specifiesthatthisisatrustedkey.WhenNTPauthenticationis
enabled,theswitchonlysynchronizeswithtimeserversthat
transmitpacketscontainingatrustedkey.
ciphertext <ENCRYPTED-KEY> SpecifiestheciphertextauthenticationkeyinBase64format.This
isusedtorestoretheNTPauthenticationkeywhencopying
configurationfilesbetweenswitchesorwhenuploadinga
previouslysavedconfiguration.
NOTE:
Whenthekeyisnotprovidedonthecommandline,
plaintextkeypromptingoccursuponpressingEnter,
followedbypromptingastowhetherthekeyistobe
trusted.Theenteredkeycharactersaremaskedwith
asterisks.
Examples
Definingkey10withMD5encryptionandaprovidedplaintexttrustedkey:
| switch(config)# | ntp | authentication-key |     | 10 md5 F82#450b | trusted |
| --------------- | --- | ------------------ | --- | --------------- | ------- |
Definingkey5withSHA1encryptionandapromptedplaintexttrustedkey:
| switch(config)# | ntp                    | authentication-key |                | 5 sha1 |     |
| --------------- | ---------------------- | ------------------ | -------------- | ------ | --- |
| Enter the       | NTP authentication     |                    | key: ********* |        |     |
| Re-Enter        | the NTP authentication |                    | key: ********* |        |     |
| Configure       | the key                | as trusted         | (y/n)? y       |        |     |
Removingkey10:
| switch(config)# | no      | ntp authentication-key |              | 10  |     |
| --------------- | ------- | ---------------------- | ------------ | --- | --- |
| Command         | History |                        |              |     |     |
| Release         |         |                        | Modification |     |     |
| 10.07orearlier  |         |                        | --           |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 35

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp disable
ntp disable
Description
DisablestheNTPclientontheswitch.TheNTPclientisdisabledbydefault.
Examples
DisablingtheNTPclient.
switch(config)#
|                     | ntp     | disable |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp enable
ntp enable
no ntp enable
Description
EnablestheNTPclientontheswitchtoautomaticallyadjustthelocaltimeanddateontheswitch.The
NTPclientisdisabledbydefault.
ThenoformofthiscommanddisablestheNTPclient.
Examples
EnablingtheNTPclient.
| switch(config)# | ntp | enable |     |
| --------------- | --- | ------ | --- |
DisablingtheNTPclient.
InitialConfiguration |36

| switch(config)# |             | no  | ntp enable |     |              |     |
| --------------- | ----------- | --- | ---------- | --- | ------------ | --- |
| Command         | History     |     |            |     |              |     |
| Release         |             |     |            |     | Modification |     |
| 10.07orearlier  |             |     |            |     | --           |     |
| Command         | Information |     |            |     |              |     |
| Platforms       | Command     |     | context    |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp conductor
| ntp conductor    | vrf | <VRF-NAME>     |     | {stratum | <NUMBER>] |     |
| ---------------- | --- | -------------- | --- | -------- | --------- | --- |
| no ntp conductor |     | vrf <VRF-NAME> |     | {stratum | <NUMBER>] |     |
Description
SetstheswitchastheconductortimesourceforNTPclientsonthespecifiedVRF.Bydefault,theswitch
operatesatstratumlevel8.TheswitchcannotfunctionasbothNTPconductorandclientonthesame
VRF.
Thenoformofthiscommandstopstheswitchfromoperatingastheconductortimesourceonthe
specifiedVRF.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vrf <VRF-NAME> SpecifiestheVRFonwhichtoactasconductortimesource.
stratum <NUMBER> Specifiesthestratumlevelatwhichtheswitchoperates.Range:1-
15.Default:8.
Examples
SettingtheswitchtoactasconductortimesourceonVRFprimary-vrfwithastratumlevelof9.
| switch(config)# |     | ntp | conductor | vrf | primary-vry | statum 9 |
| --------------- | --- | --- | --------- | --- | ----------- | -------- |
StopstheswitchfromactingasconductortimesourceonVRFprimary-vrf.
| switch(config)# |         | no  | ntp conductor |     | vrf primary-vry    |     |
| --------------- | ------- | --- | ------------- | --- | ------------------ | --- |
| Command         | History |     |               |     |                    |     |
| Release         |         |     |               |     | Modification       |     |
| 10.08           |         |     |               |     | Inclusivelanguage. |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 37

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution
rights for this command.

ntp server
ntp server <IP-ADDR> [key <KEY-NUM>] [minpoll <MIN-NUM>] [maxpoll <MAX-NUM>][burst |
iburst][prefer] [version <VER-NUM>]
no ntp server <IP-ADDR> <IP-ADDR> [key <KEY-NUM>] [minpoll <MIN-NUM>] [maxpoll <MAX-NUM>]
[burst | iburst] [prefer] [version <VER-NUM>]

Description

Defines an NTP server to use for time synchronization, or updates the settings of an existing server with
new values. Up to eight servers can be defined.

The no form of this command removes a configured NTP server.

The default NTP version is 4; it is backwards compatible with version 3.

Parameter

Description

server <IP-ADDR>

key <KEY-NUM>

minpoll <MIN-NUM>

maxpoll <MAX-NUM>

Specifies the address of an NTP server as a DNS name, an IPv4
address (x.x.x.x), where x is a decimal number from 0 to 255, or
an IPv6 address
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.
When specifying an IPv4 address, you can remove leading zeros.
For example, the address 192.169.005.100 becomes
192.168.5.100.
When specifying an IPv6 address, you can use two colons (::) to
represent consecutive zeros (but only once), remove leading
zeros, and collapse a hextet of four zeros to a single 0. For
example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes
2222:0:3333::4444:55 .

Specifies the key to use when communicating with the server. A
trusted key must be defined with the command ntp
authentication-key and authentication must be enabled with
the command ntp authentication. Range: 1 to 65534.

Specifies the minimum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 6 (64 seconds).

Specifies the maximum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 10 (1024 seconds).

burst

Send a burst of packets instead of just one when connected to the

Initial Configuration | 38

Parameter

Description

iburst

prefer

server. Useful for reducing phase noise when the polling interval
is long.

Send a burst of six packets when not connected to the server.
Useful for reducing synchronization time at startup.

Make this the preferred server.

version <VER-NUM>

Specifies the version number to use for all outgoing NTP packets.
Range: 3 or 4. Default: 4.

NOTE: NTP is backwards compatible.

Usage

For features such as Activate and ZTP, a switch that has a factory default configuration will automatically
be configured with pool.ntp.org. NTP server configurations via DHCP options are supported. The DHCP
server can be configured with maximum of two NTP server addresses which will be supported on the
switch. Only IPV4 addresses are supported.

When configuring a time backward more than five minutes, a reboot is recommended to avoid unusual switch

behavior.

NTP uses a stratum to describe the distance between a network device and an authoritative time
source:

n A stratum 1 time server is directly attached to an authoritative time source (such as a radio or atomic

clock or a GPS time source).

n A stratum 2 NTP server receives its time through NTP from a stratum 1 time server.

When using multiple servers with same stratum setting, the best practice to configure a preferred
server, so NTP will attempt to use the preferred server as the primary NTP connection. If a preferred
server is not manually set when NTP is enabled, the configured server with the lowest stratum will
automatically be set as the preferred server. If there are servers with the same stratum, this auto prefer
status will prevent AOS-CX from toggling between different servers as the primary server. Auto prefer
selection of servers with same stratum (if not manually selected) may change after reconfiguring the
switch, or after executing the reboot command.

Examples

Defining the ntp server pool.ntp.org, using iburst, and NTP version 4.

switch(config)# ntp server pool.ntp.org iburst version 4

Removing the ntp server pool.ntp.org.

switch(config)# no ntp server pool.ntp.org

Defining the ntp server my-ntp.mydomain.com and makes it the preferred server.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

39

| switch(config)#     | ntp     | server my-ntp.mydomain.com |              | prefer |
| ------------------- | ------- | -------------------------- | ------------ | ------ |
| Command History     |         |                            |              |        |
| Release             |         |                            | Modification |        |
| 10.07orearlier      |         |                            | --           |        |
| Command Information |         |                            |              |        |
| Platforms           | Command | context                    | Authority    |        |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp trusted-key
| ntp trusted-key    | <KEY-ID> |     |     |     |
| ------------------ | -------- | --- | --- | --- |
| no ntp trusted-key | <KEY-ID> |     |     |     |
Description
Setsakeyastrusted.WhenNTPauthenticationisenabled,theswitchonlysynchronizeswithtime
serversthattransmitpacketscontainingatrustedkey.
Thenoformofthiscommandremovesthetrusteddesignationfromakey.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<KEY-ID> Specifiestheidentificationnumberofthekeytosetastrusted.
Range:1to65534.
Examples
Definingkey10asatrustedkey.
| switch(config)# | ntp | trusted-key | 10  |     |
| --------------- | --- | ----------- | --- | --- |
Removingtrusteddesignationfromkey10:
| switch(config)#     | no  | ntp trusted-key | 10           |     |
| ------------------- | --- | --------------- | ------------ | --- |
| Command History     |     |                 |              |     |
| Release             |     |                 | Modification |     |
| 10.07orearlier      |     |                 | --           |     |
| Command Information |     |                 |              |     |
InitialConfiguration |40

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp vrf
ntp vrf <VRF-NAME>
| no ntp vrf <VRF-NAME> |     |     |     |
| --------------------- | --- | --- | --- |
Description
SpecifiestheVRFonwhichtheNTPclientcommunicateswithanNTPserver.Theswitchcannotfunction
asbothNTPconductorandclientonthesameVRF.
ThenoformofthecommandreturnstodefaultVRF.
| Parameter  |     |     | Description             |
| ---------- | --- | --- | ----------------------- |
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |
Example
SettingtheswitchtousethedefaultVRFforNTPclienttraffic.
| switch(config)# | ntp | vrf default |     |
| --------------- | --- | ----------- | --- |
SettingtheswitchtousethedefaultmanagementVRFforNTPclienttraffic.
| switch(config)# | ntp | vrf mgmt |     |
| --------------- | --- | -------- | --- |
ReturningtheswitchtousethedefaultVRFforNTPclienttraffic.
| switch(config)#     | no      | ntp vrf |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ntp              | associations |            |     |
| --------------------- | ------------ | ---------- | --- |
| show ntp associations |              | [vsx-peer] |     |
Description
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 41

Shows the status of the connection to each NTP server. The following information is displayed for each
server:

n Tally code : The first character is the Tally code:

o (blank): No state information available (e.g. non-responding server)

o x : Out of tolerance (discarded by intersection algorithm)

o . : Discarded by table overflow (not used)

o - : Out of tolerance (discarded by the cluster algorithm)

o + : Good and a preferred remote peer or server (included by the combine algorithm)

o # : Good remote peer or server, but not utilized (ready as a backup source)

o * : Remote peer or server presently used as a primary reference

o o : PPS peer (when the prefer peer is valid)

n ID: Server number.

n NAME: NTP server FQDN/IP address (Only the first 24 characters of the name are displayed).

n REMOTE: Remote server IP address.

n REF_ID: Reference ID for the remote server (Can be an IP address).

n ST: (Stratum) Number of hops between the NTP client and the reference clock.

n LAST: Time since the last packet was received in seconds unless another unit is indicated.

n POLL: Interval (in seconds) between NTP poll packets. Maximum (1024) reached as server and client

sync.

n REACH: 8-bit octal number that displays status of the last eight NTP messages (377 = all messages

received).

Parameter

vsx-peer

Example

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

ID

switch# show ntp associations
----------------------------------------------------------------------
REF-ID ST LAST POLL REACH
----------------------------------------------------------------------
0
1
* 2
377
----------------------------------------------------------------------

192.0.1.1
time.apple.com

192.0.1.1
17.253.2.253

.INIT. 16
2
.GPSs.

64
70 128

REMOTE

NAME

-

Command History

Release

10.07 or earlier

Command Information

Modification

--

Initial Configuration | 42

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp                     | authentication-keys |            |     |
| ---------------------------- | ------------------- | ---------- | --- |
| show ntp authentication-keys |                     | [vsx-peer] |     |
Description
Showsthecurrentlydefinedauthenticationkeys.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# | show ntp | authentication-keys |     |
| ------- | -------- | ------------------- | --- |
--------------------------------
| Auth key | Trusted | MD5 password |     |
| -------- | ------- | ------------ | --- |
--------------------------------
| 10             | No          | ********** |              |
| -------------- | ----------- | ---------- | ------------ |
| 20             | Yes         | ********** |              |
| Command        | History     |            |              |
| Release        |             |            | Modification |
| 10.07orearlier |             |            | --           |
| Command        | Information |            |              |
| Platforms      | Command     | context    | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ntp | servers |     |     |
| -------- | ------- | --- | --- |
show ntp servers[vsx-peer]
Description
ShowsallconfiguredNTPservers,includinganyDHCPservers,defaultpoolserversoranyserverwith
| thestatusauto | prefer. |     |     |
| ------------- | ------- | --- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 43

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# | show | ntp servers |     |     |
| ------- | ---- | ----------- | --- | --- |
------------------------------------------------
|     | NTP SERVER | KEYID MINPOLL | MAXPOLL OPTION | VER |
| --- | ---------- | ------------- | -------------- | --- |
------------------------------------------------
|     | 192.0.1.18 | -   | 5 10 iburst | 3        |
| --- | ---------- | --- | ----------- | -------- |
|     | 192.0.1.19 | -   | 6 10 none   | 4        |
|     | 192.0.1.20 | -   | 6 8 burst   | 3 prefer |
------------------------------------------------
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | ntp statistics |            |     |     |
| ---- | -------------- | ---------- | --- | --- |
| show | ntp statistics | [vsx-peer] |     |     |
Description
ShowsglobalNTPstatistics.Thefollowinginformationisdisplayed:
Rx-pkts:TotalNTPpacketsreceived.
n
n CurrentVersionRx-pkts:NumberofNTPpacketsthatmatchthecurrentNTPversion.
n OldVersionRx-pkts:NumberofNTPpacketsthatmatchthepreviousNTPversion.
n Errorpkts:Packetsdroppedduetoallothererrorreasons.
n Auth-failedpkts:Packetsdroppedduetoauthenticationfailure.
n Declinedpkts:Packetsdeniedaccessforanyreason.
n Restrictedpkts:PacketsdroppedduetoNTPaccesscontrol.
n Rate-limitedpkts:Numberofpacketsdiscardedduetoratelimitation.
n KODpkts:NumberofKissofDeathpacketssent.
InitialConfiguration |44

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch(config)#     | show          | ntp statistics |              |
| ------------------- | ------------- | -------------- | ------------ |
|                     | Rx-pkts       | 100            |              |
| Current Version     | Rx-pkts       | 80             |              |
| Old Version         | Rx-pkts       | 20             |              |
|                     | Err-pkts      | 2              |              |
| Auth-failed-pkts    |               | 1              |              |
|                     | Declined-pkts | 0              |              |
| Restricted-pkts     |               | 0              |              |
| Rate-limited-pkts   |               | 0              |              |
|                     | KoD-pkts      | 0              |              |
| Command History     |               |                |              |
| Release             |               |                | Modification |
| 10.07orearlier      |               |                | --           |
| Command Information |               |                |              |
| Platforms           | Command       | context        | Authority    |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp        | status     |     |     |
| --------------- | ---------- | --- | --- |
| show ntp status | [vsx-peer] |     |     |
Description
ShowsthestatusofNTPontheswitch.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingthestatusinformationwhentheswitchisnotsyncedtoanNTPserver:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 45

| switch#            | show ntp    | status  |             |        |         |          |              |     |
| ------------------ | ----------- | ------- | ----------- | ------ | ------- | -------- | ------------ | --- |
| NTP is             | enabled.    |         |             |        |         |          |              |     |
| NTP authentication |             |         | is enabled. |        |         |          |              |     |
| NTP is             | using the   | default |             | VRF    | for NTP | server   | connections. |     |
| Wed Nov            | 23 23:29:10 |         | PDT         | 2016   |         |          |              |     |
| NTP uptime:        | 187         | days,   | 1           | hours, | 37      | minutes, | 48 seconds   |     |
| Not synchronized   |             | with    | an          | NTP    | server. |          |              |     |
DisplayingthestatusinformationwhentheswitchissyncedtoanNTPserver:
switch#
show ntp status
| NTP is             | enabled.    |           |             |              |             |              |              |     |
| ------------------ | ----------- | --------- | ----------- | ------------ | ----------- | ------------ | ------------ | --- |
| NTP authentication |             |           | is enabled. |              |             |              |              |     |
| NTP is             | using the   | default   |             | VRF          | for NTP     | server       | connections. |     |
| Wed Nov            | 23 23:29:10 |           | PDT         | 2016         |             |              |              |     |
| NTP uptime:        | 187         | days,     | 1           | hours,       | 37          | minutes,     | 48 seconds   |     |
| Synchronized       | to          | NTP       | Server      | 17.253.2.253 |             | at           | stratum      | 2.  |
| Poll interval      |             | = 1024    | seconds.    |              |             |              |              |     |
| Time accuracy      |             | is within |             | 0.994        | seconds     |              |              |     |
| Reference          | time:       | Thu       | Jan         | 28 2016      | 0:57:06.647 |              | (UTC)        |     |
| Command            | History     |           |             |              |             |              |              |     |
| Release            |             |           |             |              |             | Modification |              |     |
| 10.07orearlier     |             |           |             |              |             | --           |              |     |
| Command            | Information |           |             |              |             |              |              |     |
| Platforms          | Command     |           | context     |              |             | Authority    |              |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
InitialConfiguration |46

Chapter 4

Interface configuration

Interface configuration

Configuring a layer 2 interface

Procedure

1. Change to the interface configuration context for the interface with the command interface.

2. By default, interfaces are layer 3. To create a layer 2 interface, disable routing with the command

no routing.

3. Set the interface MTU (maximum transmission unit) with the command mtu.

4. Review interface configuration settings with the command show interface.

Configuring a layer 3 interface

Procedure

1. Change to the interface configuration context for the interface with the command interface.

2.

Interfaces are layer 3 by default. If you previously set the interface to layer 2, then enable routing
support with the command routing.

3. Assign an IPv4 address with the command ip address, or an IPv6 address with the command

ipv6 address.

4.

5.

If required, enable support for layer 3 counters with the command l3-counters.

If required, set the IP MTU with the command ip mtu.

6. Review interface configuration settings with the command show interface.

Examples

This example creates the following configuration:

n Configures interface 1/1/1 as a layer 3 interface.

n Defines an IPv4 address of 10.10.20.209 with a 24-bit mask.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ip address 10.10.20.209/24

This example creates the following configuration:

n Configures interface 1/1/2 as a layer 3 interface.

n Defines an IPv6 address of 2001:0db8:85a3::8a2e:0370:7334 with a 24-bit mask.

n Enables layer 3 transmit and receive counters.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

47

switch# config
switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
switch(config-if)# l3-counters tx
switch(config-if)# l3-counters rx

Single source IP address

Certain IP-based protocols used by the switch (such as RADIUS, sFlow, TACACS, and TFTP), use a client-
server model in which the client's source IP address uniquely identifies the client in packets sent to the
server. By default, the source IP address is defined as the IP address of the outgoing switch interface on
which the client is communicating with the server. Since the switch can have multiple routing interfaces,
outgoing packets can potentially be sent on different paths at different times. This can result in different
source IP addresses being used for a client, which can create a client identification problem on the
server. For example, it can be difficult to interpret system logs and accounting data on the server when
the same client is associated with multiple IP addresses.

To resolve this issue, you can use the commands ip source-interface and ipv6 source-interface to
define a single source IP address that applies to all supported protocols (RADIUS, sFlow, TACACS, and
TFTP), or an individual address for each protocol. This ensures that all traffic sent by a client to a server
uses the same IP address.

Priority-based flow control (PFC)

Priority-based flow control (PFC) is defined in the IEEE 802.1Qbb standard. It is used to eliminate packet
loss due to congestion on a network link.

For priority-based flow control, care must be taken when configuring quality of service.

1. Configure the global CoS map (qos cos-map command) and queue profile (qos queue-profile

command) before configuring PFC on any interface.

n Each code point in the CoS Map to be used for PFC must be assigned a unique local-priority

value.

n Each local-priority used for PFC must be the sole local-priority mapped to a queue in the

queue profile.

2. CoS map or queue profile changes for non-PFC priorities can be modified without any impact on

PFC functionality.

3. All interfaces with PFC enabled must also be configured with `qos trust cos` or `qos trust dscp.`

4. For PFC to function properly with VSX and MCLAG, PFC must be configured on the inter-switch-

link.

See also commands flow-control and show interface flow-control.

Refer to the Quality of Service Guide for more information about buffering and queuing for flow-
controlled traffic.

PFC is not supported on the 8400X 32x10G module (JL363A).

PFC is not supported on the 8400X 8x40G module (JL365A) split interfaces (for example, 10G).

While interfaces with PFC configured are enabled, any change to QoS cos-map or queue-profile affecting
the priority or queue used by PFC could cause the intended traffic to no longer be treated as lossless.

Interface configuration | 48

Before making CoS map or Queue Profile changes (see Quality of Service Guide), shut down all PFC
interfaces, make all cos-map or queue-profile changes, reboot any line-modules with PFC interfaces, and
then re-enable the PFC interfaces.

Flow control and lossless buffering

The switch supports IEEE 802.1Q Priority-based Flow Control (PFC). The PFC standard specifies
additional frames exchanged between the Ethernet Media Access Controllers (MACs) on both sides of a
link to pause and resume transmissions. The goal is to prevent packet loss despite congestion.

Prerequisites

1. A Priority Code Point (PCP) chosen for PFC must not share a local priority with any other PCP in the
Class of Service (CoS) map.

2. A local priority mapped to the PCP via the CoS map must be the only local priority assigned to a queue
in the queue profile.

Requirements for proper lossless buffering

The switch uses a virtual output queue (VOQ) architecture where most packet buffering for all
destination ports occurs on the ingress line module. Each line module has between 1.5 and 4 GB of
buffer memory with 256 MB used for traffic destined for multiple ports (Multidest) and the remainder
for traffic destined for one port (Unidest). By default, all unicast packets arriving on ports of the same
line module share the Unidest pool. Any packet can be dropped if the destination port VOQ has
exceeded its limit. The VOQ limit is either 1 MB for JL365 modules, or 1.7 MB for JL366 and JL687
modules. The TX Drops columns of show interface <IF-NAME> command will display the number of drops
that have occurred.

Priority-based Flow Control (PFC) reconfigures buffering. After the first interface is configured for PFC
the switch will move some Unidest buffers to a new Headroom pool. Unicast traffic arriving at PFC-
configured ports with the specified PCP will still use the Unidest pool with other traffic but will be
marked as lossless. Lossless-marked packets will never be dropped when a destination port VOQ has
exceeded its limit. All other unicast traffic arriving on non-PFC ports, or on PFC-configured ports with
different PCPs also shares the Unidest pool. However, such traffic is still subject to dropping when a
destination port VOQ has exceeded its limit.

Each PFC-configured-port priority is given a limit on the amount of lossless buffering it can store in the
Unidest pool. The limit is either 1 MB for JL365A modules, or 1.7 Mbytes for JL366A and JL687A modules.
Once the limit is exceeded, the switch will send a PFC pause frame from the port to stop further packets
from arriving. Due to link propagation time and processing time on the receiving switch, additional
packets in flight are allowed to be received and will be stored in the Headroom pool. The Headroom
pool size is sufficient to store all packets in flight arriving after the priority pause frame is sent. The
switch will periodically transmit priority pause frames until all the port’s lossless packets are gone from
the Headroom pool and its lossless packets in the Unidest pool go below half of the pool's capacity.

When the switch receives a PFC pause frame for the configured PCP, the port will cease transmitting
further packets from that queue until the timeout specified in the Quanta field has expired or a resume
frame is received.

Unsupported transceiver support

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

49

Transceiverproducts(optical,DAC,AOCs)thatarelistedassupportedbyaswitchmodelaredetailedin
theTransceiverGuide.Transceiverproductsthatarenotlisted,areconsideredunsupported;thiswould
includetransceiversthatare:
n Non-Arubabrandedproducts
n HPEbrandedproductsthatweredesignedfornon-AOS-CXswitchmodels(e.g.Comware)
n HPEbrandedproductsdesignatedforuseinHPEComputeServersorStorage
n TransceiversoriginallydesignatedforuseinArubaWLANcontrollersorformerMobilityAccess
Switch(MAS)products
n End-of-lifeArubaTransceivers
Theunsupportedtransceivermode(UT-mode)isdesignedtoallowthepossibleuseofthese
unsupportedproducts.Notallunsupportedproductscanberecognizedandenabled;theymaybe
unabletobeidentified(donotfollowtheproperMSAstandardsforidentification).Theseunsupported
transceiverproductsareenabledonlyonabest-effortbasisandtherearenoguaranteesimpliedfor
theircontinuedoperation.
Thisfeatureisenabledbydefault.Aperiodicsystemlogwillbegeneratedbydefaultatanintervalof24
hourslistingtheportsonwhichunsupportedtransceiversarepresent.Thelogintervalisconfigurable
andcanbedisabledbysettingthelog-intervaltonone.
| Configuring |     | an interface |     | persona |     |     |
| ----------- | --- | ------------ | --- | ------- | --- | --- |
Apersonaisatemplateinterface.Itisamechanismintendedtoeasestheprocessofconfiguringoneor
multipleinterfacesthatbehaveinthesamemanner.Forexample,apersonacouldbeanuplink
interfacewithawell-knowncollectionofVLANstowhichitbelongs.Insteadofmanuallyconfiguring
eachinterfaceone-by-one,thepersonacollectsthecommonconfigurationsettingsandallowsthemto
beappliedontheinterfaceoracollectionofinterfaces.
Personaconfigurationissimilartoconfiguringotherinterfaces.Mostofthecommandsintheinterface
contextareavailable.Becauseofthenatureofthecommands,severalofthemdonotapplytothe
persona(forexample,applyingthesameIPaddressconfigurationtoseveralports)andhavebeen
removedfromtheavailablelist.
Thefollowingcommandsarenotsupportedwithintheinterfacecontextwhenconfiguringapersona:
| aaa authentication   |     | port-access | dot1x      | authenticator |     | macsec |
| -------------------- | --- | ----------- | ---------- | ------------- | --- | ------ |
| arp ipv4 <IPV4_ADDR> |     | mac         | <MAC_ADDR> |               |     |        |
downshift-enable
energy-efficient-ethernet
| error-control              | { auto  | | none            | | base-r-fec      |              | | rs-fec     | }             |
| -------------------------- | ------- | ----------------- | ----------------- | ------------ | ------------ | ------------- |
| ip bootp-gateway           |         | <IPV4-ADDR>       |                   |              |              |               |
| ip forward-protocol        |         | udp               | <IPV4-ADDR>       | {<PORT-NUM>  |              | | <PROTOCOL>} |
| ip helper-address          |         | <IPV4-ADDR>       | [vrf              | <VRF-NAME>]  |              |               |
| ip igmp router-alert-check |         |                   | [enable           | | disable]   |              |               |
| ip igmp snooping           |         | [auto vlan        | <VLAN-LIST>]      |              |              |               |
| ip igmp snooping           |         | [blocked          | vlan <VLAN-LIST>] |              |              |               |
| ip igmp snooping           |         | [fastleave        | vlan              | <VLAN-LIST>] |              |               |
| ip igmp snooping           |         | [forced-fastleave |                   | vlan         | <VLAN-LIST>] |               |
| ip igmp snooping           |         | [forward          | vlan <VLAN-LIST>] |              |              |               |
| ip ospf <PROCESS-ID>       |         | area              | <AREA-ID>         |              |              |               |
| ip ospf passive            |         |                   |                   |              |              |               |
| ip rip <PROCESS-ID>        |         | {all-ip           | | ip-address}     |              |              |               |
| ip rip all-ip              | disable |                   |                   |              |              |               |
| ip rip all-ip              | enable  |                   |                   |              |              |               |
| ip rip all-ip              | receive | disable           |                   |              |              |               |
| ip rip all-ip              | send    | disable           |                   |              |              |               |
Interfaceconfiguration|50

ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
| ipv6 mld           | snooping     | [auto             | vlan | <VLAN-LIST>]   |              |              |
| ------------------ | ------------ | ----------------- | ---- | -------------- | ------------ | ------------ |
| ipv6 mld           | snooping     | [blocked          |      | vlan           | <VLAN-LIST>] |              |
| ipv6 mld           | snooping     | [fastleave        |      | vlan           | <VLAN-LIST>] |              |
| ipv6 mld           | snooping     | [forced-fastleave |      |                | vlan         | <VLAN-LIST>] |
| ipv6 mld           | snooping     | [forward          |      | vlan           | <VLAN-LIST>] |              |
| ipv6 neighbor      | <IPV6-ADDR>  |                   |      | mac <MAC-ADDR> |              |              |
| ipv6 ospfv3        | <PROCESS-ID> |                   | area | <AREA-ID>      |              |              |
| ipv6 ospfv3        | passive      |                   |      |                |              |              |
| ipv6 ripng         | <PROCESS-ID> |                   |      |                |              |              |
| lacp port-id       | <PORT-ID>    |                   |      |                |              |              |
| lacp port-priority |              | <PORT-PRIORITY>   |      |                |              |              |
lag <ID>
link-poe
| lldp dot3 | eee                     |     |     |     |     |     |
| --------- | ----------------------- | --- | --- | --- | --- | --- |
| lldp dot3 | poe                     |     |     |     |     |     |
| lldp med  | poe                     |     |     |     |     |     |
| lldp med  | poe [priority-override] |     |     |     |     |     |
persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
| port-access | device-profile |     |     | <DEVICE-PROFILE-NAME> |     |     |
| ----------- | -------------- | --- | --- | --------------------- | --- | --- |
power-over-ethernet
| power-over-ethernet |          | allocate-by       |               |                     | {usage                  | | class}    |
| ------------------- | -------- | ----------------- | ------------- | ------------------- | ----------------------- | ----------- |
| power-over-ethernet |          | assigned-class    |               |                     | {3 |                    | 4 | 6 | 8}  |
| power-over-ethernet |          | pd-class-override |               |                     |                         |             |
| power-over-ethernet |          | power-pairs       |               |                     | {alt-a|alt-a-and-alt-b} |             |
| power-over-ethernet |          | pre-std-detect    |               |                     |                         |             |
| power-over-ethernet |          | priority          |               | {critical|high|low} |                         |             |
| ptp lag-role        | {primary |                   | | secondary}  |                     |                         |             |
| spanning-tree       | cost     | <PORT-COST>       |               |                     |                         |             |
| spanning-tree       | instance |                   | <INSTANCE-ID> |                     | cost                    | <PORT-COST> |
spanning-tree instance <INSTANCE-ID> port-priority <PRIORITY-MULTIPLIER>
| spanning-tree | port-priority |            |     | <PRIORITY-MULTIPLIER> |               |        |
| ------------- | ------------- | ---------- | --- | --------------------- | ------------- | ------ |
| spanning-tree | vlan          | <A:1-4094> |     | cost                  | <0-200000000> |        |
| spanning-tree | vlan          | <A:1-4094> |     | port-priority         |               | <0-15> |
split [confirm]
| track by | <OBJECT-ID> |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
vsx-sync {access-lists | qos | rate-limits | vlans | policies | irdp}
Modes
Therearetwosupportedmodes:
1.Copy—Thecopymodeisaone-stepconfigurationthatcopiesthepersonaconfigurationtoan
interface.Furtherchangestothepersonawillnotbeappliedtotheinterfacesusingthatmode.
2.Attach—Unlikethecopymode,besidesapplyingtheconfigurationtotheinterfaceimmediately,the
attachmodealsofollowsthepersonaconfiguration.Itmeansthatthesubsequentchangestothe
personawillbeappliedtotheinterfacesattachedtoit.
| Predefined |     | and | custom | persona |     | names |
| ---------- | --- | --- | ------ | ------- | --- | ----- |
Therearetwopredefinedinterfacepersonanames:
n uplink
n access
Thesenameshavenopredefinedconfiguration.Tousethem,theymustbemanuallyconfiguredas
needed.Youcanalsocreatepersonaswithacustomname.Thesecustompersonascanbecreatedand
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 51

configuredinthesamemannerasthepredefinedones.Theonlydifferenceisthecommandusedto
applythemtotheinterface.Theprocedurebelowprovidesthedetails.
| Creating | and configuring |     | an interface | persona |
| -------- | --------------- | --- | ------------ | ------- |
Followthesestepstocreateandconfigureaninterfacepersona:
1. Createtheinterfacepersonawiththecommandinterface persona <PERSONA-NAME>.
2. Settheinterfaceconfigurationasanyotherphysicalinterface.
3. Reviewtheconfigurationwiththecommandshow running-configuration current-context.
4. Switchtoaninterfacecontextwiththecommandinterface <PORT>.
5. Applythepersonaconfigurationtotheinterfaceandsetthemodewiththecommandpersona
custom <PERSONA-NAME> <mode>.Notethat<custom>isanoptionalargument,requiredonlyif
thepersonaisnotoneofthepredefinednames(neitheruplinknoraccess).
Forinformationonthisfeature,seetherelatedvideoontheArubaAirHeadsBroadcastingChannel.
Examples
Tocopyapredefinedpersonanameconfigurationtoaninterface:
1.Configuretheinterfacepersona:
| switch(config)#    |     | interface   | persona uplink |     |
| ------------------ | --- | ----------- | -------------- | --- |
| switch(config-if)# |     | no shutdown |                |     |
| switch(config-if)# |     | no routing  |                |     |
| switch(config-if)# |     | vlan access | 100            |     |
| switch(config-if)# |     | exit        |                |     |
2.Applytheconfigurationwithcopymode:
| switch(config)#    |     | interface | 1/1/1            |      |
| ------------------ | --- | --------- | ---------------- | ---- |
| switch(config-if)# |     | persona   | custom mypersona | copy |
| switch(config-if)# |     | exit      |                  |      |
Toattachacustompersonanametoseveralinterfacessimultaneously:
1.Configuretheinterfacepersona:
| switch(config)#    |     | interface   | persona mytemplate |     |
| ------------------ | --- | ----------- | ------------------ | --- |
| switch(config-if)# |     | no shutdown |                    |     |
| switch(config-if)# |     | vrf attach  | upstream           |     |
| switch(config-if)# |     | exit        |                    |     |
2.Applytheconfigurationwithattachmode:
| switch(config)#    |          | interface | 1/1/1-1/1/24     |        |
| ------------------ | -------- | --------- | ---------------- | ------ |
| switch(config-if)# |          | persona   | custom mypersona | attach |
| switch(config-if)# |          | exit      |                  |        |
| Interface          | commands |           |                  |        |
Interfaceconfiguration|52

allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver

Description

Allows unsupported transceivers to be enabled or establish connections. Transceivers with speeds up to
100G are enabled by this command.

The 8400 Series Switches will enable unsupported transceivers for speeds up to 100G when running AOS-CX

10.10 or later.

The no form of this command disallows using unsupported transceivers.

Parameter

confirm

Description

Specifies that unsupported transceiver warnings are to be
automatically confirmed.

log-interval none

Disables unsupported transceiver logging.

log-interval <INTERVAL>

Sets the unsupported transceiver logging interval in minutes.
Default: 1440 minutes. Range: 1440 to 10080 minutes.

Usage

When none of the parameters are specified it will display a warning message to accept the warranty
terms. With confirm option the warning message is displayed but the user is not prompted to (y/n)
answering. Warranty terms must be agreed to as part of enablement and the support is on best effort
basis.

Examples

Allowing unsupported transceivers with follow-up confirmation:

switch(config)# allow-unsupported-transceiver
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.

Do you agree and do you want to continue (y/n)? y

Allowing unsupported transceivers with confirmation in command syntax:

switch(config)# allow-unsupported-transceiver confirm
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.

Configuring unsupported transceiver logging with an interval of every 48 hours:

switch(config)# allow-unsupported-transceiver log-interval 2880

Disabling unsupported transceiver logging:

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

53

switch(config)# allow-unsupported-transceiver log-interval none
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no  | allow-unsupported-transceiver |     |     |
| --------------- | --- | ----------------------------- | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
| Continue    | (y/n)? y    |               |           |       |
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
switch(config)#
|     | no  | allow-unsupported-transceiver |     | confirm |
| --- | --- | ----------------------------- | --- | ------- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
switch(config)#
| Command History |     |     |                                                     |     |
| --------------- | --- | --- | --------------------------------------------------- | --- |
| Release         |     |     | Modification                                        |     |
| 10.10           |     |     | Upto100G supportenabledforunsupportedtransceiverson |     |
8400(upto100G)seriesswitchesinUT mode.
| 10.07orearlier      |         |         | --        |     |
| ------------------- | ------- | ------- | --------- | --- |
| Command Information |         |         |           |     |
| Platforms           | Command | context | Authority |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| default interface |                |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
| default interface | <INTERFACE-ID> |     |     |     |
Description
Setsaninterface(orarangeofinterfaces)tofactorydefaultvalues.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID> SpecifiestheIDofasingleinterfaceorrangeofinterfaces.
Format:member/slot/portormember/slot/port-
member/slot/porttospecifyarange.
Examples
Resettinganinterface:
Interfaceconfiguration|54

| switch(config)# | default | default | interface | 1/1/1 |
| --------------- | ------- | ------- | --------- | ----- |
Resettinganrangeofinterfaces:
| switch(config)#     | default | default | interface    | 1/1/1-1/1/10 |
| ------------------- | ------- | ------- | ------------ | ------------ |
| Command History     |         |         |              |              |
| Release             |         |         | Modification |              |
| 10.07orearlier      |         |         | --           |              |
| Command Information |         |         |              |              |
| Platforms           | Command | context | Authority    |              |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
description
| description | <DESCRIPTION> |     |     |     |
| ----------- | ------------- | --- | --- | --- |
no description
Description
Associatesdescriptiveinformationwithaninterfacetohelpadministratorsandoperatorsidentifythe
purposeorroleofaninterface.
Thenoformofthiscommandremovesadescriptionfromaninterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DESCRIPTION> Specifyadescriptionfortheinterface.Range:1to64ASCII
characters(includingspace,excludingquestionmark).
Examples
| SettingthedescriptionforaninterfacetoDataLink |     |             |          | 01: |
| --------------------------------------------- | --- | ----------- | -------- | --- |
| switch(config-if)#                            |     | description | DataLink | 01  |
Removingthedescriptionforaninterface.
| switch(config-if)# |     | no description |              |     |
| ------------------ | --- | -------------- | ------------ | --- |
| Command History    |     |                |              |     |
| Release            |     |                | Modification |     |
| 10.07orearlier     |     |                | --           |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 55

| Command   | Information |         |     |           |
| --------- | ----------- | ------- | --- | --------- |
| Platforms | Command     | context |     | Authority |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
flow-control
| flow-control    | rx       |      |            |     |
| --------------- | -------- | ---- | ---------- | --- |
| no flow-control | rx       |      |            |     |
| flow-control    | priority | rxtx | <PRIORITY> |     |
| no flow-control | priority | rxtx | <PRIORITY> |     |
Description
Commandflow-controlenablesnegotiationofreceiveflowcontrolonthecurrentinterface.The
switchadvertisesRXsupporttothelinkpartner.Thefinalconfigurationisdeterminedbasedonthe
capabilitiesofbothpartners.
Commandflow-control priorityenablespriority-basedflowcontrol(PFC).Asinglepriorityis
supported..
Eachinvocationofthiscommandreplacesthepreviousconfiguration.
Thenoformofthesecommandsdisablesanyconfiguredflowcontrolontheselectedinterface.
| Parameter |     |     |     | Description                                       |
| --------- | --- | --- | --- | ------------------------------------------------- |
| rx        |     |     |     | Enablestheabilitytoceaseandresumetransmissionwhen |
receivingIEEE802.3xLLFCpauseframesonthisinterface.
<PRIORITY> SpecifiesthepacketpriorityforwhichPFCwilloperate.Range:0
to7.Oneprioritycanbespecified.
| Usage (flow | control) |     |     |     |
| ----------- | -------- | --- | --- | --- |
n Forinterfacesthatauto-negotiate,link-levelflowcontrolissubjecttonegotiation,plusspeedand
otherparameters.Bothendsofthelinkmustnegotiatethesameflowcontrolmodeforittobe
applied.
n Forinterfacesthatdonotauto-negotiate,theconfiguredlink-levelflowcontrolmodeisalways
appliedandtheuserisresponsibleforensuringthatbothendsofthelinkareconfiguredforthe
samemode.
n AllmembersofaLAGmusthavethesameflowcontrolconfiguration.
n Losslessflowcontrolisonlysupportedforsingledestinationunicasttraffic.Replicatedtraffic(for
example,broadcast,multicast,mirroring)cannotbeguaranteedtobelossless.
n LosslessbehaviorisnotsupportedwhenoperatinginaVSFstackconfiguration.
| Usage (priority-based |     | flow | control | (PFC)) |
| --------------------- | --- | ---- | ------- | ------ |
PFCwillonlyoperatecorrectlybetweeninterfaceswiththesamepriorityconfiguration.Trafficflow
n
willnotbelosslessbetweeninterfaceswithdifferentprioritiesorbetweeninterfaceswhereonehas
PFCenabledandtheotherdoesnot.
Interfaceconfiguration|56

n Anyqueueusedbyprotocolorcontroltrafficmustnotbeconfiguredforlosslessbehavior.Routing
protocolsandVSX-synchronizationmessagesuselocal-priority7,thereforetheCoSprioritymapped
tolocal-priority7shouldnotbeusedinanylosslessconfiguration.
Forexample,inadefaultconfiguration,theCoSmapassignslocal-priority7topacketsarrivingwith
VLANpriority7.Thismeansthatlosslesspoolsshouldnotbeconfiguredtousepriority7,andthat
anyflow-control prioritymodeshouldnotbeconfiguredonpriority7,sincethatVLANpriority
mapstolocal-priority7.
n PFCisenabledforthegivenPriorityCodePoint.OnlyoneprioritymaybeenabledforPFCper
interface.PFCisonlysupportedonJL365A8400X8-port40GbEQSFP+AdvancedModule,JL366A
Aruba8400X6-port40GbE/100GbEQSFP28AdvMod,andJL687A8400X-32Y32p1/10/25G
SFP/SFP+/SFP28Modulelinemodules.
n PFCwillonlyoperatecorrectlybetweeninterfaceswiththesamepriorityconfiguration.Trafficflow
willnotbelosslessbetweeninterfaceswithdifferentprioritiesorbetweeninterfaceswhereonehas
PFCenabledandtheotherdoesnot.
Examples
EnablingsupportforRXflowcontrol:
| switch(config)#    | interface    | 1/1/1 |     |     |
| ------------------ | ------------ | ----- | --- | --- |
| switch(config-if)# | flow-control |       | rx  |     |
DisablingsupportforRXflowcontrol:
| switch(config)#    | interface       | 1/1/1 |     |     |
| ------------------ | --------------- | ----- | --- | --- |
| switch(config-if)# | no flow-control |       | rx  |     |
EnablingsupportforpriorityRXTXflowcontrol:
| switch(config)#    | interface    | 1/1/1 |               |     |
| ------------------ | ------------ | ----- | ------------- | --- |
| switch(config-if)# | flow-control |       | priority rxtx | 2   |
DisablingsupportforpriorityRXTXflowcontrol:
| switch(config)#    | interface       | 1/1/1 |          |        |
| ------------------ | --------------- | ----- | -------- | ------ |
| switch(config-if)# | no flow-control |       | priority | rxtx 2 |
Command History
| Release        |     |     | Modification               |     |
| -------------- | --- | --- | -------------------------- | --- |
| 10.10          |     |     | Adjustedtheprioritysyntax. |     |
| 10.07orearlier |     |     | --                         |     |
Command Information
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 57

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
interface
| interface <PORT-NUM> |     |     |     |
| -------------------- | --- | --- | --- |
Description
Switchestotheconfig-ifcontextforaphysicalport.Thisiswhereyoudefinetheconfiguration
settingsforthelogicalinterfaceassociatedwiththephysicalport.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PORT-NUM> Specifiesaphysicalportnumber.Format:member/slot/port.
Examples
Configuringaninterface:
| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| interface          | loopback |      |     |
| ------------------ | -------- | ---- | --- |
| interface loopback | <ID>     |      |     |
| no interface       | loopback | <ID> |     |
Description
Createsaloopbackinterfaceandchangestotheconfig-loopback-ifcontext.Loopbackinterfacesare
layer3.
Thenoformofthiscommanddeletesaloopbackinterface.
| Parameter  |     |     | Description                                  |
| ---------- | --- | --- | -------------------------------------------- |
| <INSTANCE> |     |     | SpecifiestheloopbackinterfaceID.Range:1to256 |
Interfaceconfiguration|58

Examples
| switch# config  |           |          |     |
| --------------- | --------- | -------- | --- |
| switch(config)# | interface | loopback | 1   |
switch(config-loopback-if)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
| 8400 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| interface      | vlan           |     |     |
| -------------- | -------------- | --- | --- |
| interface vlan | <VLAN-ID>      |     |     |
| no interface   | vlan <VLAN-ID> |     |     |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-
if-vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
| Parameter |     |     | Description                                   |
| --------- | --- | --- | --------------------------------------------- |
| <VLAN-ID> |     |     | SpecifiestheloopbackinterfaceID.Range:1to4094 |
Examples
| switch# config          |           |      |     |
| ----------------------- | --------- | ---- | --- |
| switch(config)#         | vlan      | 10   |     |
| switch(config-vlan-10)# |           | exit |     |
| switch(config)#         | interface | vlan | 10  |
switch(config-if-vlan)#
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 59

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip address
| ip address    | <IPV4-ADDR>/<MASK> |     |     | [secondary] |             |     |
| ------------- | ------------------ | --- | --- | ----------- | ----------- | --- |
| no ip address | <IPV4-ADDR>/<MASK> |     |     |             | [secondary] |     |
Description
SetsanIPv4addressforthecurrentlayer3interface.
ThenoformofthiscommandremovestheIPv4addressfromtheinterface.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| <MASK> |     |     |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |     |
| ------ | --- | --- | --- | --- | ---------------------------------------------------- | --- |
(x),wherexisadecimalnumberfrom0to128.
| secondary |     |     |     |     | SpecifiesasecondaryIPaddress. |     |
| --------- | --- | --- | --- | --- | ----------------------------- | --- |
Examples
SettingtheIPaddressoninterface1/1/1to192.168.100.1withamaskof24bits:
| switch(config)#    |     | interface |            | 1/1/1 |                  |     |
| ------------------ | --- | --------- | ---------- | ----- | ---------------- | --- |
| switch(config-if)# |     |           | ip address |       | 192.168.100.1/24 |     |
RemovingtheIPaddress192.168.100.1withamaskof24bitsfrominterface1/1/1:
| switch(config)#    |     | interface |       | 1/1/1   |                  |     |
| ------------------ | --- | --------- | ----- | ------- | ---------------- | --- |
| switch(config-if)# |     |           | no ip | address | 192.168.100.1/24 |     |
AssigningtheIPaddress192.168.20.1withamaskof24bitstoloopbackinterface1:
| switch(config)#             |     | interface |     | loopback | 1       |                 |
| --------------------------- | --- | --------- | --- | -------- | ------- | --------------- |
| switch(config-loopback-if)# |     |           |     | ip       | address | 192.168.20.1/24 |
AssigningtheIPaddress192.168.199.1withamaskof24bitstointerfaceVLAN10:
| switch(config)#         |     | interface |     | vlan    | 10               |     |
| ----------------------- | --- | --------- | --- | ------- | ---------------- | --- |
| switch(config-if-vlan)# |     |           | ip  | address | 192.168.199.1/24 |     |
RemovingtheIPaddress192.168.199.1withamaskof24bitsfrominterfaceVLAN10:
Interfaceconfiguration|60

| switch(config)# | interface | vlan | 10  |
| --------------- | --------- | ---- | --- |
switch(config-if-vlan)#
|                     |         | no ip address | 192.168.199.1/24 |
| ------------------- | ------- | ------------- | ---------------- |
| Command History     |         |               |                  |
| Release             |         |               | Modification     |
| 10.07orearlier      |         |               | --               |
| Command Information |         |               |                  |
| Platforms           | Command | context       | Authority        |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-loopback-if |     | rightsforthiscommand. |
| --- | ------------------ | --- | --------------------- |
config-if-vlan
ip mtu
ip mtu <VALUE>
no ip mtu
Description
SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthatcan
besentorreceivedbytheinterface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE> SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
SettingtheIPMTUto576bytes:
| switch(config-if)# |     | ip mtu 576 |     |
| ------------------ | --- | ---------- | --- |
SettingtheIPMTUtothedefaultvalue:
| switch(config-if)# |     | no ip mtu |                           |
| ------------------ | --- | --------- | ------------------------- |
| Command History    |     |           |                           |
| Release            |     |           | Modification              |
| 10.08              |     |           | Subinterfacesupportadded. |
| 10.07orearlier     |     |           | --                        |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 61

Command Information

Platforms

Command context

Authority

All platforms

config-if
config-if-vlan

Administrators or local user group members with execution
rights for this command.

ip source-interface
ip source-interface {sflow |
simplivity | dns | all} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
no ip source-interface {sflow | tftp |
relay | simplivity | dns | all} [interface <IFNAME> | <IPV4-ADDR>] [vrf <VRF-NAME>]

radius | tacacs | ntp | syslog | ubt | dhcp-

radius | tacacs | ntp | syslog | ubt | dhcp-relay |

tftp |

Description

Sets a single source IP address for a feature on the switch. This ensures that all traffic sent the feature
has the same source IP address regardless of how it egresses the switch. You can define a single global
address that applies to all supported features, or an individual address for each feature.

This command provides two ways to set the source IP addresses: either by specifying a static IP address,
or by using the address assigned to a switch interface. If you define both options, then the static IP
address takes precedence.

The no form of this command deletes the single source IP address for all supported services, or a
specific service.

Parameter

Description

sflow | tftp | radius | tacacs |
ntp | syslog | ubt | dhcp-relay |
simplivity | dns | all

Sets a single source IP address for a specific service. The all
option sets a global address that applies to all protocols that do
not have an address set. For DHCP relay, the address is used as
both the source IP and GIADDR.

interface <IFNAME>

<IPV4-ADDR>

Specifies the name of the interface from which the specified
service obtains its source IP address. The interface must have a
valid IP address assigned to it. If the interface has both a primary
and secondary IP address, the primary IP address is used.

Specifies the source IP address to use for the specified service.
The IP address must be defined on the switch, and it must exist
on the specified VRF (which is the default VRF, if the vrf option
is not used). Specify the address in IPv4 format (x.x.x.x), where
x is a decimal number from 0 to 255.

vrf <VRF-NAME>

Specifies the name of a VRF.

Examples

Setting the IPv4 address 10.10.10.5 as the global single source address:

switch# config
switch(config)# ip source-interface all 10.10.10.5

Interface configuration | 62

SettingthesecondaryIPv4address10.10.10.5oninterface1/1/1astheglobalsinglesourceaddress:
| switch#            | config |           |                  |               |                |           |
| ------------------ | ------ | --------- | ---------------- | ------------- | -------------- | --------- |
| switch(config)#    |        | interface | 1/1/1            |               |                |           |
| switch(config-if)# |        |           | ip address       | 10.10.10.1/24 |                |           |
| switch(config-if)# |        |           | ip address       | 10.10.10.5/24 |                | secondary |
| switch(config)#    |        | exit      |                  |               |                |           |
| switch(config)#    |        | ip        | source-interface |               | all 10.10.10.5 |           |
Settingtheaddress10.10.10.25onVRFsflow-vrfoninterface1/1/2asthesinglesourceaddressfor
sFlow:
| switch(config)# |     | vrf | sflow-vrf |     |     |     |
| --------------- | --- | --- | --------- | --- | --- | --- |
switch(config-vrf)#
exit
| switch(config)#    |     | interface | 1/1/2       |                |     |     |
| ------------------ | --- | --------- | ----------- | -------------- | --- | --- |
| switch(config-if)# |     |           | no shutdown |                |     |     |
| switch(config-if)# |     |           | vrf attach  | sflow-vrf      |     |     |
| switch(config-if)# |     |           | ip address  | 10.10.10.25/24 |     |     |
| switch(config-if)# |     |           | exit        |                |     |     |
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)# |             | no  | ip source-interface |     | all          | 10.10.10.5 |
| --------------- | ----------- | --- | ------------------- | --- | ------------ | ---------- |
| Command         | History     |     |                     |     |              |            |
| Release         |             |     |                     |     | Modification |            |
| 10.07orearlier  |             |     |                     |     | --           |            |
| Command         | Information |     |                     |     |              |            |
| Platforms       | Command     |     | context             |     | Authority    |            |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK>{eui64 |                    |     |     | | [tag | <ID>]} |
| --------------- | ------------------------ | ------------------ | --- | --- | ------ | ------ |
| no ipv6 address |                          | <IPV6-ADDR>/<MASK> |     |     |        |        |
Description
SetsanIPv6addressontheinterface.
ThenoformofthiscommandremovestheIPv6addressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-
localaddressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6 address
link-localcommand.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 63

| Parameter   |     |     | Description                       |
| ----------- | --- | --- | --------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiestheIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
| eui64    |     |     | ConfiguretheIPv6addressintheEUI-64bitformat.  |
| -------- | --- | --- | --------------------------------------------- |
| tag <ID> |     |     | Configureroutetagforconnectedroutes.Range:0to |
4294967295.Default:0.
Examples
SettingtheIPv6address2001:0db8:85a3::8a2e:0370:7334withamaskof24bits:
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
RemovingtheIPaddress2001:0db8:85a3::8a2e:0370:7334withmaskof24bits:
switch(config-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 source-interface
ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay
| simplivity | dns | all} {interface <IFNAME> | <IPV6-ADDR>} [vrf <VRF-NAME>]
no ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-
relay | simplivity | dns | all} [interface <IFNAME> | <IPV6-ADDR>] [vrf <VRF-NAME>]
Description
SetsasinglesourceIPaddressforafeatureontheswitch.Thisensuresthatalltrafficsentthefeature
hasthesamesourceIPaddressregardlessofhowitegressestheswitch.Youcandefineasingleglobal
addressthatappliestoallsupportedfeatures,oranindividualaddressforeachfeature.
Interfaceconfiguration|64

ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,
orbyusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIP
addresstakesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforallsupportedprotocols,ora
specificprotocol.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | SetsasinglesourceIPaddressforaspecificprotocol.Theall
ntp | syslog | ubt | dhcp-relay | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
| simplivity | | dns | | all |     | nothaveanaddressset. |
| ---------- | ----- | ----- | --- | -------------------- |
interface <IFNAME> Specifiesthenameoftheinterfacefromwhichthespecified
protocolobtainsitssourceIPaddress.
<IPV6-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedprotocol.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionis
notused).SpecifytheIPaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
vrf <VRF-NAME> SpecifiesthenameoftheVRFfromwhichthespecifiedprotocol
setsitssourceIPaddress.
Examples
ConfiguringtheIPv6address2001:DB8::1astheglobalsinglesourceaddress:
| switch#         | config |                     |     |                    |
| --------------- | ------ | ------------------- | --- | ------------------ |
| switch(config)# |        | ip source-interface |     | all 2001:DB8::1/32 |
ConfiguringtheIPv6address2001:DB8::1onVRFsflow-vrfoninterface1/1/2asthesinglesource
addressforsFlow:
| switch(config)#     |     | vrf sflow-vrf |         |                |
| ------------------- | --- | ------------- | ------- | -------------- |
| switch(config-vrf)# |     | exit          |         |                |
| switch(config)#     |     | interface     | 1/1/2   |                |
| switch(config-if)#  |     | no shutdown   |         |                |
| switch(config-if)#  |     | vrf           | attach  | sflow-vrf      |
| switch(config-if)#  |     | ipv6          | address | 2001:DB8::1/32 |
| switch(config-if)#  |     | exit          |         |                |
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
StopthesourceIPaddressfromusingtheIPaddressoninterface1/1/1onVRFone.
switch(config)# no ip source-interface all interface 1/1/1 vrf one
ClearthesourceIPaddress2001:DB8::1.
| switch(config)# |         | no ip source-interface |     | all 2001:DB8::1 |
| --------------- | ------- | ---------------------- | --- | --------------- |
| Command         | History |                        |     |                 |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 65

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
l3-counters
| l3-counters    | [rx | tx] |       |     |     |
| -------------- | --------- | ----- | --- | --- |
| no l3-counters | [rx       | | tx] |     |     |
Description
Enablescountersonalayer3interface.Bydefault,allinterfacesarelayer3.Tochangealayer2
interfacetolayer3,usetheroutingcommand.
Thenoformofthiscommand,withnospecification,disablesbothtransmitandreceivecountersona
layer3interface.Todisabletransmit(tx)orreceive(rx)countersonly,specifythecountertypeyou
wanttodisable.
| Parameter |     |     |     | Description                |
| --------- | --- | --- | --- | -------------------------- |
| rx        |     |     |     | Specifiesreceivecounters.  |
| tx        |     |     |     | Specifiestransmitcounters. |
Examples
Enablinglayer3transmitcountersoninterface1/1/1:
switch(config)#
|                    |     | interface   | 1/1/1 |     |
| ------------------ | --- | ----------- | ----- | --- |
| switch(config-if)# |     | l3-counters |       | tx  |
Disablinglayer3transmitandreceivecountersoninterface1/1/2:
| switch(config)#     |     | interface      | 1/1/2 |                                          |
| ------------------- | --- | -------------- | ----- | ---------------------------------------- |
| switch(config-if)#  |     | no l3-counters |       |                                          |
| Command History     |     |                |       |                                          |
| Release             |     |                |       | Modification                             |
| 10.08               |     |                |       | Addedsupportfor13countersonsubinterfaces |
| 10.07orearlier      |     |                |       | --                                       |
| Command Information |     |                |       |                                          |
Interfaceconfiguration|66

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
mtu
mtu <VALUE>
no mtu
Description
SetstheMTU(maximumtransmissionunit)foraninterface.Thisdefinesthemaximumsizeofalayer2
(Ethernet)frame.FrameslargerthantheMTU(1500bytesbydefault)aredropped.
Tosupportjumboframes(frameslargerthan1522bytes),increasetheMTUasrequiredbyyour
network.Aframesizeofupto9198bytesissupported.
Thelargestpossiblelayer1framewillbe18byteslargerthantheMTUvaluetoallowforlinklayer
headersandtrailers.
ThenoformofthiscommandsetstheMTUtothedefaultvalue1500.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE>
SpecifiestheMTUinbytes.Range:46to9198.Default:1500.
Examples
SettingtheMTUoninterface1/1/1to1000bytes:
| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|                    |     | no routing |     |
| ------------------ | --- | ---------- | --- |
| switch(config-if)# |     | mtu 1000   |     |
SettingtheMTUoninterface1/1/1tothedefaultvalue:
| switch(config)#     | interface | 1/1/1      |              |
| ------------------- | --------- | ---------- | ------------ |
| switch(config-if)#  |           | no routing |              |
| switch(config-if)#  |           | no mtu     |              |
| Command History     |           |            |              |
| Release             |           |            | Modification |
| 10.07orearlier      |           |            | --           |
| Command Information |           |            |              |
| Platforms           | Command   | context    | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
persona
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 67

persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
no persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]

Description

Associates one of three persona types with an interface to classify the purpose or role of an interface.
On the 10000 Switch Series, “access” persona ports are typically connected to workloads / VMs, and the
“uplink” (fabric) persona ports are connected to the core / spine.

The no form of this command removes the interface persona.

Parameter

Description

access

uplink

Selects the access persona type.

Selects the uplink persona type.

custom <PERSONA-NAME>

Selects the custom persona type with a user-provided name.
Range: 1 to 64 printable ASCII characters including space.

copy

attach

Usage

Specifies the mode: copies settings from the persona interface of
the same name.

Specifies the mode: attaches the specified interface to the
persona interface of the same name.

n If the mode is specified, either copy or attach, the interface configuration is dependent on the

interface template whose name is "access", "uplink", or "<PERSONA-NAME>". On the other hand, if the
mode is not specified, then the persona is just a label in the interface, and its configuration is not
modified even if the interface persona exists. When configuring the mode, one of the following
options is possible:

o The copy option performs a one-time copy of the template interface. Subsequent changes to the
template are not copied and the 'persona' setting is just a label. If the mode is set to copy and the
interface persona does not exist, then the CLI command fails with the message "Interface persona
not found".

o The attach option performs a copy of the template interface, and subsequent changes to the

template interface configuration are immediately applied to all attached interfaces. The template
interface does not need to exist before attaching other interfaces to it. After attaching a template,
the copied settings can be modified for an individual interface. However, any change in the
attached template will overwrite the modified values with the new template values.

n When a mode is specified, it should match an interface created with the command interface persona
<PERSONA-NAME>. The only exception to this rule is when the mode is set to attach and the persona
does not already exist.

n The mode is only available to be configured for an interface that meets the following conditions:

o IS a physical interface

o IS NOT a LAG member

o IS NOT a persona interface

Examples

Configuring an access persona:

Interface configuration | 68

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|     | persona | access |     |
| --- | ------- | ------ | --- |
Configuringanuplinkpersona:
| switch(config)#    | interface | 1/1/1  |     |
| ------------------ | --------- | ------ | --- |
| switch(config-if)# | persona   | uplink |     |
Configuringacustompersonanamed"mypersona":
| switch(config)#    | interface | 1/1/1            |     |
| ------------------ | --------- | ---------------- | --- |
| switch(config-if)# | persona   | custom mypersona |     |
Removingthepersonasetting.
| switch(config-if)# | no persona |     |     |
| ------------------ | ---------- | --- | --- |
Copyingapredefinedpersonanameconfigurationtoaninterface:
1.Configuringtheinterfacepersona:
| switch(config)#    | interface   | persona uplink |     |
| ------------------ | ----------- | -------------- | --- |
| switch(config-if)# | no shutdown |                |     |
| switch(config-if)# | no routing  |                |     |
switch(config-if)#
|                    | vlan | access 100 |     |
| ------------------ | ---- | ---------- | --- |
| switch(config-if)# | exit |            |     |
2.Applyingtheconfigurationfromthepersonanamed"mypersona"withcopymode:
| switch(config)#    | interface | 1/1/1            |      |
| ------------------ | --------- | ---------------- | ---- |
| switch(config-if)# | persona   | custom mypersona | copy |
| switch(config-if)# | exit      |                  |      |
Attachingacustompersonanamenamed"mypersona"toseveralinterfacessimultaneously:
1.Configuringaninterfacepersonanamed"mypersona":
| switch(config)#    | interface   | persona mypersona |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | vrf         | attach upstream   |     |
| switch(config-if)# | exit        |                   |     |
2.Applyingthe"mypersona"configurationwithattachmode:
| switch(config)#    | interface | 1/1/1-1/1/24     |        |
| ------------------ | --------- | ---------------- | ------ |
| switch(config-if)# | persona   | custom mypersona | attach |
| switch(config-if)# | exit      |                  |        |
Command History
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 69

| Release             |         |         | Modification                         |
| ------------------- | ------- | ------- | ------------------------------------ |
| 10.10               |         |         | Addedoptionalparameters:attach,copy. |
| 10.09               |         |         | Commandintroduced.                   |
| Command Information |         |         |                                      |
| Platforms           | Command | context | Authority                            |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
routing
routing
no routing
Description
Enablesroutingsupportonaninterface,creatingaL3(layer3)interfaceonwhichtheswitchcanroute
IPv4/IPv6traffictootherdevices.
Bydefault,routingisenabledonallinterfaces.
Thenoformofthiscommanddisablesroutingsupportonaninterface,creatingaL2(layer2)interface.
Examples
Enablingroutingsupportonaninterface:
| switch(config-if)# |     | routing |     |
| ------------------ | --- | ------- | --- |
Disablingroutingsupportonaninterface:
| switch(config-if)#  |         | no routing |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show allow-unsupported-transceiver
show allow-unsupported-transceiver
Description
Interfaceconfiguration|70

Displaysconfigurationandstatusofunsupportedtransceivers.
Examples
Showingunallowedunsupportedtransceivers:
| switch(config)#   |          | show allow-unsupported-transceiver |     |     |              |
| ----------------- | -------- | ---------------------------------- | --- | --- | ------------ |
| Allow unsupported |          | transceivers                       |     | :   | no           |
| Logging           | interval |                                    |     | :   | 1440 minutes |
---------------------------------------------
| Port | Type |     | Status |     |     |
| ---- | ---- | --- | ------ | --- | --- |
---------------------------------------------
| 1/1/31 | SFP-SX     |     | unsupported |     |     |
| ------ | ---------- | --- | ----------- | --- | --- |
| 1/1/32 | SFP-1G-BXD |     | unsupported |     |     |
| 1/1/2  | SFP28DAC3  |     | unsupported |     |     |
Showingallowedunsupportedtransceivers:
| switch#           | show allow-unsupported-transceiver |              |     |     |              |
| ----------------- | ---------------------------------- | ------------ | --- | --- | ------------ |
| Allow unsupported |                                    | transceivers |     | :   | yes          |
| Logging           | interval                           |              |     | :   | 1440 minutes |
---------------------------------------------
| Port | Type |     | Status |     |     |
| ---- | ---- | --- | ------ | --- | --- |
---------------------------------------------
| 1/1/31         | SFP-SX      |         | unsupported-allowed |     |              |
| -------------- | ----------- | ------- | ------------------- | --- | ------------ |
| 1/1/32         | SFP-1G-BXD  |         | unsupported-allowed |     |              |
| 1/1/2          | SFP28DAC3   |         | unsupported         |     |              |
| Command        | History     |         |                     |     |              |
| Release        |             |         |                     |     | Modification |
| 10.07orearlier |             |         |                     |     | --           |
| Command        | Information |         |                     |     |              |
| Platforms      | Command     | context |                     |     | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show interface |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero] [human-
| readable] | | [human-readable]] |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]
| show interface | lag | [<LAG-ID>] | [extended |     | [non-zero]] |
| -------------- | --- | ---------- | --------- | --- | ----------- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 71

| Parameter |     |     | Description                                    |     |
| --------- | --- | --- | ---------------------------------------------- | --- |
| <IFNAME>  |     |     | Specifiesainterfacename.                       |     |
| <IFRANGE> |     |     | Specifiestheportidentifierrange.               |     |
| brief     |     |     | Showsbriefinfointabularformat.                 |     |
| physical  |     |     | Showsthephysicalconnectioninfointabularformat. |     |
| extended  |     |     | Showsadditionalstatistics.                     |     |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero |     |     | Showsonlynonzerostatistics. |     |
| -------- | --- | --- | --------------------------- | --- |
LAG
ShowsLAGinterfaceinformation.
| LOOPBACK |     |     | Showsloopbackinterfaceinformation. |     |
| -------- | --- | --- | ---------------------------------- | --- |
TUNNEL
Showstunnelinterfaceinformation.
| VLAN |     |     | ShowsVLANinterfaceinformation. |     |
| ---- | --- | --- | ------------------------------ | --- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255 |     |
| ------------- | --- | --- | -------------------------------------- | --- |
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
| <VLAN-ID> |     |     | SpecifiestheVLANID.Range:1-4094 |     |
| --------- | --- | --- | ------------------------------- | --- |
VXLAN
ShowstheVXLANinterfaceinformation.
| <VXLAN-ID> |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |
| ---------- | --- | --- | ---------------------------------------------- | --- |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch#           | show interface | 1/1/1         |                     |           |
| ----------------- | -------------- | ------------- | ------------------- | --------- |
| Interface         | 1/1/1 is       | up            |                     |           |
| Admin state       | is up          |               |                     |           |
| Link state:       | up for         | 2 days (since | Sun Jun 21 05:30:22 | UTC 2020) |
| Link transitions: |                | 1             |                     |           |
| Description:      | backup         | data center   | link                |           |
| Hardware:         | Ethernet,      | MAC Address:  | 70:72:cf:fd:e7:b4   |           |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |       |     |     |
| ---------------- | ---- | ----- | --- | --- |
| Speed 1000       | Mb/s |       |     |     |
| Auto-negotiation |      | is on |     |     |
| Flow-control:    | off  |       |     |     |
| Error-control:   | off  |       |     |     |
Interfaceconfiguration|72

| L3 Counters:    |     | Rx Enabled, | Tx  | Enabled |     |     |       |         |
| --------------- | --- | ----------- | --- | ------- | --- | --- | ----- | ------- |
| Rate collection |     | interval:   | 300 | seconds |     |     |       |         |
| Rates           |     |             |     | RX      |     | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization | %   |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistics  |     |     |     | RX   |     | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 0   |     | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     | 0   |     | 0   |     | 0   |
| Multicast    |     |     |     | 0   |     | 0   |     | 0   |
| Broadcast    |     |     |     | 0   |     | 0   |     | 0   |
| Bytes        |     |     |     | 0   |     | 0   |     | 0   |
| Jumbos       |     |     |     | 0   |     | 0   |     | 0   |
| Dropped      |     |     |     | 0   |     | 0   |     | 0   |
| Filtered     |     |     |     | 0   |     | 0   |     | 0   |
| Pause Frames |     |     |     | 0   |     | 0   |     | 0   |
| L3 Packets   |     |     |     | 0   |     | 0   |     | 0   |
| L3 Bytes     |     |     |     | 0   |     | 0   |     | 0   |
| Errors       |     |     |     | 0   |     | 0   |     | 0   |
| CRC/FCS      |     |     |     | 0   |     | n/a |     | 0   |
| Collision    |     |     |     | n/a |     | 0   |     | 0   |
| Runts        |     |     |     | 0   |     | n/a |     | 0   |
| Giants       |     |     |     | 0   |     | n/a |     | 0   |
| Other        |     |     |     | 0   |     | 0   |     | 0   |
Showinginformationwhentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |       |     |     |     |     |
...
| Auto-negotiation |     | is on | with | downshift | active |     |     |     |
| ---------------- | --- | ----- | ---- | --------- | ------ | --- | --- | --- |
ShowinginformationwhentheinterfaceisshutdownduringaVSX split:
switch(config-if)#
|                    |       | show     | interface | 1/1/1  |     |     |     |     |
| ------------------ | ----- | -------- | --------- | ------ | --- | --- | --- | --- |
| Interface          | 1/1/1 | is down  |           |        |     |     |     |     |
| Admin state        | is    | up       |           |        |     |     |     |     |
| State information: |       | Disabled |           | by VSX |     |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
| Link transitions: |     | 0   |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none |        |     |     |     |     |     |     |
| ---------------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
| Speed 0          | Mb/s |        |     |     |     |     |     |     |
| Auto-negotiation |      | is off |     |     |     |     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 73

| Flow-control:   | off             |             |     |     |       |         |
| --------------- | --------------- | ----------- | --- | --- | ----- | ------- |
| Error-control:  | off             |             |     |     |       |         |
| VLAN Mode:      | native-untagged |             |     |     |       |         |
| Native VLAN:    | 1               |             |     |     |       |         |
| Allowed VLAN    | List: 1502-1505 |             |     |     |       |         |
| Rate collection | interval:       | 300 seconds |     |     |       |         |
| Rate            |                 |             | RX  | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits / sec |     |     | 0.00 | 0.00 |     | 0.00  |
| ----------- | --- | --- | ---- | ---- | --- | ----- |
| KPkts / sec |     |     | 0.00 | 0.00 |     | 0.00  |
| Unicast     |     |     | 0.00 | 0.00 |     | 0.00  |
| Multicast   |     |     | 0.00 | 0.00 |     | 0.00  |
| Broadcast   |     |     | 0.00 | 0.00 |     | 0.00  |
| Utilization |     |     | 0.00 | 0.00 |     | 0.00  |
| Statistic   |     |     | RX   | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     | 0   | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     | 0   | 0   |     | 0   |
| Multicast    |     |     | 0   | 0   |     | 0   |
| Broadcast    |     |     | 0   | 0   |     | 0   |
| Bytes        |     |     | 0   | 0   |     | 0   |
| Jumbos       |     |     | 0   | 0   |     | 0   |
| Dropped      |     |     | 0   | 0   |     | 0   |
| Pause Frames |     |     | 0   | 0   |     | 0   |
| Errors       |     |     | 0   | 0   |     | 0   |
| CRC/FCS      |     |     | 0   | n/a |     | 0   |
| Collision    |     |     | n/a | 0   |     | 0   |
| Runts        |     |     | 0   | n/a |     | 0   |
| Giants       |     |     | 0   | n/a |     | 0   |
Showingtheoutputinhuman-readableformat:
Inthehuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsis
betweenzeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsand
theUtilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# | show        | interface | 1/1/1 human-readable |     |     |     |
| ------------------ | ----------- | --------- | -------------------- | --- | --- | --- |
| Interface          | 1/1/1 is up |           |                      |     |     |     |
...
| Rate |     |     | RX  | TX  | Total | (RX+TX) |
| ---- | --- | --- | --- | --- | ----- | ------- |
---------------- -------------------- -------------------- --------------------
| Bits / sec  |     |     | 3M  | 3M  |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | ----- |
| Pkts / sec  |     |     | 316 | 316 |     | 633   |
| Unicast     |     |     | 319 | 319 |     | 638   |
| Multicast   |     |     | 0   | 0   |     | 0     |
| Broadcast   |     |     | 0   | 0   |     | 0     |
| Utilization | %   |     | < 1 | < 1 |     | < 1   |
| Statistic   |     |     | RX  | TX  |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets   |     |     | 577K | 577K |     | 1M  |
| --------- | --- | --- | ---- | ---- | --- | --- |
| Unicast   |     |     | 577K | 577K |     | 1M  |
| Multicast |     |     | 0    | 51   |     | 51  |
Interfaceconfiguration|74

|     | Broadcast    |     |     |     | 0    |     | 15   | 15  |
| --- | ------------ | --- | --- | --- | ---- | --- | ---- | --- |
|     | Bytes        |     |     |     | 744M |     | 745M | 1G  |
|     | Jumbos       |     |     |     | 0    |     | 0    | 0   |
|     | Dropped      |     |     |     | 0    |     | 0    | 0   |
|     | Filtered     |     |     |     | 0    |     | 0    | 0   |
|     | Pause Frames |     |     |     | 0    |     | 0    | 0   |
|     | Errors       |     |     |     | 0    |     | 0    | 0   |
|     | CRC/FCS      |     |     |     | 0    |     | n/a  | 0   |
|     | Collision    |     |     |     | n/a  |     | 0    | 0   |
|     | Runts        |     |     |     | 0    |     | n/a  | 0   |
|     | Giants       |     |     |     | 0    |     | n/a  | 0   |
...
| Command | History |     |     |     |              |     |     |     |
| ------- | ------- | --- | --- | --- | ------------ | --- | --- | --- |
| Release |         |     |     |     | Modification |     |     |     |
10.10
Addedhuman-readableparameter.
| 10.07orearlier |             |         |         |     | --        |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | --------- | --- | --- | --- |
| Command        | Information |         |         |     |           |     |     |     |
| Platforms      |             | Command | context |     | Authority |     |     |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | interface | dom              |     |     |          |            |     |     |
| ---- | --------- | ---------------- | --- | --- | -------- | ---------- | --- | --- |
| show | interface | [<INTERFACE-ID>] |     | dom | [detail] | [vsx-peer] |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+,QSFP+).
ThisinformationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter      |     |     |     |     | Description                                   |     |     |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |     |
| detail         |     |     |     |     | Showdetailedinformation.                      |     |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
|     | switch# | show interface | dom |     |     |     |     |     |
| --- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 75

----------------------------------------------------------------------------------
Port Type Channel Temperature Voltage Tx Bias Rx Power Tx Power
|     |     | (Celsius) | (Volts) | (mA) | (mW/dBm) | (mW/dBm) |
| --- | --- | --------- | ------- | ---- | -------- | -------- |
----------------------------------------------------------------------------------
| 1/1/1               | SFP+SR     | 47.65   | 3.31         | 8.40 | 0.08, -10.96 | 0.63, -2.49 |
| ------------------- | ---------- | ------- | ------------ | ---- | ------------ | ----------- |
| 1/1/2               | SFP+SR     | n/a     | n/a          | n/a  | n/a          | n/a         |
| 1/1/3               | SFP+DA3    | 42.10   | 3.24         | n/a  | n/a          | n/a         |
| 1/1/4               | QSFP+SR4 1 | 44.46   | 3.30         | 6.12 | 0.08, -10.96 | 0.63, -1.95 |
|                     | 2          | 44.46   | 3.30         | 6.04 | 0.08, -10.96 | 0.63, -2.00 |
|                     | 3          | 44.46   | 3.30         | 6.51 | 0.08, -10.96 | 0.60, -2.16 |
|                     | 4          | 44.46   | 3.30         | 6.19 | 0.08, -10.96 | 0.63, -1.94 |
| Command History     |            |         |              |      |              |             |
| Release             |            |         | Modification |      |              |             |
| 10.07orearlier      |            |         | --           |      |              |             |
| Command Information |            |         |              |      |              |             |
| Platforms           | Command    | context | Authority    |      |              |             |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface | flow-control          |     |              |          |     |     |
| -------------- | --------------------- | --- | ------------ | -------- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | flow-control | [detail] |     |     |
Description
Showstheflowcontrolconfiguration,status,andstatisticsofthespecifiedinterfaceforinterfaceson
whichflowcontrolisenabled.
Ifdetailisnotspecified,thiscommandshowsasummaryofallflowcontrolledinterfaceswithoneinterfaceper
line.Ifdetailisspecified,thiscommandshowsflowcontroldetailedstatistics.
AsofAOS-CX10.10,theseparateshow flow-controlcommandhasbeenremoved,withitbeingeffectively
replacedbythiscommand.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IFNNAME>|<IFRANGE> Specifiestheinterface(port)nameorrange.Whennointerface
rangeisspecified,onlyinterfaceswithflowcontrolenabledinthe
configurationorstatusareshown.
| detail |     |     | Showsdetailedinformation. |     |     |     |
| ------ | --- | --- | ------------------------- | --- | --- | --- |
Examples
Showingsummaryflowcontrolinformation:
Interfaceconfiguration|76

| switch# show | interface                             | flow-control |     |     |
| ------------ | ------------------------------------- | ------------ | --- | --- |
| -----------  | ------------------------------------- |              |     |     |
| Port         | Flow                                  |              |     |     |
Control
| ----------- | ------------------------------------- |         |     |     |
| ----------- | ------------------------------------- | ------- | --- | --- |
| 1/1/1       | config:                               | llfc rx |     |     |
|             | status:                               | llfc rx |     |     |
| 1/1/2       | config:                               | llfc rx |     |     |
|             | status:                               | none    |     |     |
ShowingsummaryflowcontrolinformationwithPFC:
| switch# show | interface                             | flow-control |     |     |
| ------------ | ------------------------------------- | ------------ | --- | --- |
| -----------  | ------------------------------------- |              |     |     |
| Port         | Flow                                  |              |     |     |
Control
| ----------- | ------------------------------------- |              |     |     |
| ----------- | ------------------------------------- | ------------ | --- | --- |
| 1/1/1       | config:                               | pfc rxtx-1,2 |     |     |
|             | status:                               | pfc rxtx-1,2 |     |     |
| 1/1/2       | config:                               | pfc rxtx-5   |     |     |
|             | status:                               | none         |     |     |
ShowingsummaryflowcontrolinformationwithPFC:
| switch# show | interface | flow-control     |     |     |
| ------------ | --------- | ---------------- | --- | --- |
| Flow Control | Watchdog  | Settings         |     |     |
| Trigger      | Timeout:  | 100 milliseconds |     |     |
| Resume       | Time:     | 100 milliseconds |     |     |
----------- ------------------------------------- ------------- --------
| Port | Flow    |     | Watchdog | Watchdog |
| ---- | ------- | --- | -------- | -------- |
|      | Control |     | Status   | Timeouts |
----------- ------------------------------------- ------------- --------
| 1/1/1    | config: | llfc rx      |              |      |
| -------- | ------- | ------------ | ------------ | ---- |
|          | status: | llfc rx      |              |      |
| 1/1/2    | config: | llfc rx      | incompatible | 0    |
|          | status: | llfc rx      |              |      |
| 1/1/10   | config: | pfc rxtx-1,2 | enabled      | 1234 |
|          | status: | pfc rxtx-1,2 |              |      |
| 1/1/12   | config: | pfc rxtx-1,2 | error        | 0    |
|          | status: | pfc rxtx-1,2 |              |      |
| 1/1/32:4 | config: | pfc rxtx-5   |              |      |
|          | status: | pfc rxtx-5   |              |      |
Showingsummaryflowcontrolinformationwheretheconfigurationdoesnotmatchstatusduetoa
rebootrequiredtoapplyPFCconfigurationinhardware:
switch#
| show         | interface | flow-control |     |     |
| ------------ | --------- | ------------ | --- | --- |
| Flow Control | Watchdog  | Settings     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 77

| Trigger |     | Timeout: | 100 | milliseconds | (actual: not | applied) |     |     |
| ------- | --- | -------- | --- | ------------ | ------------ | -------- | --- | --- |
| Resume  |     | Time:    | 100 | milliseconds | (actual: not | applied) |     |     |
----------- ------------------------------------- ------------- --------
| Port |     | Flow    |     |     |     | Watchdog | Watchdog |     |
| ---- | --- | ------- | --- | --- | --- | -------- | -------- | --- |
|      |     | Control |     |     |     | Status   | Timeouts |     |
----------- ------------------------------------- ------------- --------
| 1/1/1    |     | config: | llfc | rx       |     |              |     |      |
| -------- | --- | ------- | ---- | -------- | --- | ------------ | --- | ---- |
|          |     | status: | llfc | rx       |     |              |     |      |
| 1/1/2    |     | config: | llfc | rx       |     | incompatible |     | 0    |
|          |     | status: | llfc | rx       |     |              |     |      |
| 1/1/10   |     | config: | pfc  | rxtx-1,2 |     | pending      |     | 1234 |
|          |     | status: | none |          |     |              |     |      |
| 1/1/12   |     | config: | pfc  | rxtx-1,2 |     | pending      |     | 0    |
|          |     | status: | none |          |     |              |     |      |
| 1/1/32:4 |     | config: | pfc  | rxtx-5   |     |              |     |      |
|          |     | status: | none |          |     |              |     |      |
ShowingdetailedflowcontrolinformationwithRXflowcontrolenabled:
| switch#   | show  | interface |     | 1/1/1 flow-control | detail |     |     |     |
| --------- | ----- | --------- | --- | ------------------ | ------ | --- | --- | --- |
| Interface |       | 1/1/1 is  | up  |                    |        |     |     |     |
| Admin     | state | is up     |     |                    |        |     |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        |       | llfc   | rx                   |     |     |     |     |     |
| -------------------- | ----- | ------ | -------------------- | --- | --- | --- | --- | --- |
| Statistics           |       |        |                      |     | RX  |     |     |     |
| -------------------- |       |        | -------------------- |     |     |     |     |     |
| Dot3                 | Pause | Frames |                      |     | 0   |     |     |     |
ShowingdetailedflowcontrolinformationwithRXflowcontrolenabled:
| switch#   | show  | interface |     | 1/1/1 flow-control | detail |     |     |     |
| --------- | ----- | --------- | --- | ------------------ | ------ | --- | --- | --- |
| Interface |       | 1/1/1 is  | up  |                    |        |     |     |     |
| Admin     | state | is up     |     |                    |        |     |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        |       | llfc      | rx                   |          |     |     |     |     |
| -------------------- | ----- | --------- | -------------------- | -------- | --- | --- | --- | --- |
| Flow-control         |       | watchdog: |                      | disabled |     |     |     |     |
| Statistics           |       |           |                      |          | RX  |     |     |     |
| -------------------- |       |           | -------------------- |          |     |     |     |     |
| Dot3                 | Pause | Frames    |                      |          | 0   |     |     |     |
ShowingdetailedflowcontrolinformationwithRXTXflowcontrolenabled:
switch#
|           | show  | interface |     | 1/1/1 flow-control | detail |     |     |     |
| --------- | ----- | --------- | --- | ------------------ | ------ | --- | --- | --- |
| Interface |       | 1/1/1 is  | up  |                    |        |     |     |     |
| Admin     | state | is up     |     |                    |        |     |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: |     | llfc | rxtx |     |     |     |     |     |
| ------------- | --- | ---- | ---- | --- | --- | --- | --- | --- |
| Statistics    |     |      |      |     | RX  |     | TX  |     |
Interfaceconfiguration|78

| -------------------- |        | -------------------- | -------------------- |     |
| -------------------- | ------ | -------------------- | -------------------- | --- |
| Dot3 Pause           | Frames |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabled:
| switch#   | show interface | 1/1/1 flow-control | detail |     |
| --------- | -------------- | ------------------ | ------ | --- |
| Interface | 1/1/1 is       | up                 |        |     |
| Admin     | state is up    |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | pfc          | rxtx-4,5             |                      |     |
| -------------------- | ------------ | -------------------- | -------------------- | --- |
| Statistics           |              |                      | RX                   | TX  |
| -------------------- |              | -------------------- | -------------------- |     |
| Priority             | 0 Pauses     |                      | 0                    | 0   |
| Priority             | 1 Pauses     |                      | 0                    | 0   |
| Priority             | 2 Pauses     |                      | 0                    | 0   |
| Priority             | 3 Pauses     |                      | 0                    | 0   |
| Priority             | 4 Pauses     |                      | 0                    | 0   |
| Priority             | 5 Pauses     |                      | 0                    | 0   |
| Priority             | 6 Pauses     |                      | 0                    | 0   |
| Priority             | 7 Pauses     |                      | 0                    | 0   |
| Total                | Pause Frames |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabledandflowcontrolwatchdogdisabled:
| switch#   | show interface | 1/1/1 flow-control | detail |     |
| --------- | -------------- | ------------------ | ------ | --- |
| Interface | 1/1/1 is       | up                 |        |     |
| Admin     | state is up    |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | pfc          | rxtx-4,5             |                      |     |
| -------------------- | ------------ | -------------------- | -------------------- | --- |
| Flow-control         | watchdog:    | disabled             |                      |     |
| Statistics           |              |                      | RX                   | TX  |
| -------------------- |              | -------------------- | -------------------- |     |
| Priority             | 0 Pauses     |                      | 0                    | 0   |
| Priority             | 1 Pauses     |                      | 0                    | 0   |
| Priority             | 2 Pauses     |                      | 0                    | 0   |
| Priority             | 3 Pauses     |                      | 0                    | 0   |
| Priority             | 4 Pauses     |                      | 0                    | 0   |
| Priority             | 5 Pauses     |                      | 0                    | 0   |
| Priority             | 6 Pauses     |                      | 0                    | 0   |
| Priority             | 7 Pauses     |                      | 0                    | 0   |
| Total                | Pause Frames |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithbothPFCandflowcontrolwatchdogenabled:
| switch#   | show interface | 1/1/1 flow-control | detail |     |
| --------- | -------------- | ------------------ | ------ | --- |
| Interface | 1/1/1 is       | up                 |        |     |
| Admin     | state is up    |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: | pfc       | rxtx-4,5 |     |     |
| ------------- | --------- | -------- | --- | --- |
| Flow-control  | watchdog: | enabled  |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 79

| Statistics           |                   |                      | RX                   | TX  |
| -------------------- | ----------------- | -------------------- | -------------------- | --- |
| -------------------- |                   | -------------------- | -------------------- |     |
| Priority             | 0 Pauses          |                      | 0                    | 0   |
| Priority             | 1 Pauses          |                      | 0                    | 0   |
| Priority             | 2 Pauses          |                      | 0                    | 0   |
| Priority             | 3 Pauses          |                      | 0                    | 0   |
| Priority             | 4 Pauses          |                      | 0                    | 0   |
| Priority             | 5 Pauses          |                      | 0                    | 0   |
| Priority             | 6 Pauses          |                      | 0                    | 0   |
| Priority             | 7 Pauses          |                      | 0                    | 0   |
| Total Pause          | Frames            |                      | 0                    | 0   |
| Queue                | Watchdog          | Timeouts             |                      |     |
| ------------         | ----------------- |                      |                      |     |
Queue 0 0
Queue 1 0
Queue 2 0
Queue 3 0
Queue 4 0
Queue 5 0
Queue 6 0
Queue 7 0
Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butitcouldnotbeappliedbecausetheconfiguredflowcontrolmodeisnotcompatiblewithwatchdog:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: | llfc      | rx           |     |     |
| ------------- | --------- | ------------ | --- | --- |
| Flow-control  | watchdog: | incompatible |     |     |
Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butcouldnotbeappliedbecauseacompatibleflowcontrolmodefirstrequiresareboot:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:       | off       |                                                 |     |     |
| ------------------- | --------- | ----------------------------------------------- | --- | --- |
| Flow-control        | watchdog: | pending                                         |     |     |
| Command History     |           |                                                 |     |     |
| Release             |           | Modification                                    |     |     |
| 10.10               |           | Examplesupdatedwithnewandchangedoutputelements. |     |     |
| 10.08               |           | Commandintroduced.                              |     |     |
| Command Information |           |                                                 |     |     |
Interfaceconfiguration|80

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show interface | statistics |     |     |
| -------------- | ---------- | --- | --- |
show interface [<IFNAME>|<IFRANGE>] statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics [non-zero] [human-readable]
show interface vxlan <VXLAN-ID> statistics [non-zero] [human-readable]
Description
Showsstatisticsforswitchinterfacessuchaspacketstransmittedandreceived,bytestransmittedand
received,broadcastandmulticastpackets.
| Parameter  |     |     | Description                                    |
| ---------- | --- | --- | ---------------------------------------------- |
| <IFNAME>   |     |     | Specifiesainterfacename.                       |
| <IFRANGE>  |     |     | Specifiestheportidentifierrange.               |
| LAG        |     |     | ShowsLAGinterfaceinformation.                  |
| <LAG-ID>   |     |     | SpecifiestheLAGnumber.Range:1-256              |
| VXLAN      |     |     | ShowstheVXLANinterfaceinformation.             |
| <VXLAN-ID> |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.
non-zero
Showsonlynonzerostatistics.
Examples
Showingstatisticsofallinterfaces:
Showingstatisticsofallinterfaceswithonlynon-zerostatistics:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 81

Showingstatisticsofallinterfacesinthehuman-readableformat:
Showingstatisticsofasingleinterfaces:
ShowingstatisticsofallmembersofaLAGinterface:
Showingerrorstatisticsofallinterfaces:
| Command History     |         |         |                               |
| ------------------- | ------- | ------- | ----------------------------- |
| Release             |         |         | Modification                  |
| 10.10               |         |         | Addedhuman-readableparameter. |
| 10.07orearlier      |         |         | --                            |
| Command Information |         |         |                               |
| Platforms           | Command | context | Authority                     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface | transceiver |     |     |
| -------------- | ----------- | --- | --- |
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations] [vsx-peer]
Description
Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfor
differenttransceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPE
andthird-partytransceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskinthe
output.
Interfaceconfiguration|82

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
| detail               |     |     | Showdetailedinformationfortheinterfaces. |     |     |
| -------------------- | --- | --- | ---------------------------------------- | --- | --- |
| threshold-violations |     |     | Showthresholdviolationsfortransceivers.  |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingsummarytransceiverinformationwithidentificationofunsupportedtransceivers:
| switch(config)# | show | interface | transceiver |     |     |
| --------------- | ---- | --------- | ----------- | --- | --- |
-------------------------------------------------------------------
| Port | Type | Product | Serial |     | Part   |
| ---- | ---- | ------- | ------ | --- | ------ |
|      |      | Number  | Number |     | Number |
-------------------------------------------------------------------
| 1/1/1         | SFP+SR      | J9150A     | MYxxxxxxxx |     | 1990-3657 |
| ------------- | ----------- | ---------- | ---------- | --- | --------- |
| 1/1/2         | SFP+ER*     | --         | --         |     | --        |
| 1/2/1         | QSFP+SR4    | JH233A     | MYxxxxxxxx |     | 2005-1234 |
| 1/2/2         | QSFP+ER4*   | --         | --         |     | --        |
| 1/3/1         | SFP28DAC3   | 844477-B21 | MYxxxxxxxx |     | 77fc-7ce7 |
| * unsupported | transceiver |            |            |     |           |
Showingdetailedtransceiverinformation:
| switch(config)# | show     | interface | transceiver | detail |     |
| --------------- | -------- | --------- | ----------- | ------ | --- |
| Transceiver     | in 1/1/1 |           |             |        |     |
| Interface       | Name     | : 1/1/1   |             |        |     |
| Type            |          | : SFP+SR  |             |        |     |
| Connector       | Type     | : LC      |             |        |     |
| Wavelength      |          | : 850nm   |             |        |     |
Transfer Distance : 0m (SMF), 30m (OM1), 80m (OM2), 300m (OM3)
| Diagnostic | Support | : DOM       |     |     |     |
| ---------- | ------- | ----------- | --- | --- | --- |
| Product    | Number  | : J9150A    |     |     |     |
| Serial     | Number  | : MYxxxxxxx |     |     |     |
| Part       | Number  | : 1990-3657 |     |     |     |
Status
| Temperature | : 47.65C          |           |     |     |     |
| ----------- | ----------------- | --------- | --- | --- | --- |
| Voltage     | : 3.31V           |           |     |     |     |
| Tx Bias     | : 8.40mA          |           |     |     |     |
| Rx Power    | : 0.08mW,         | -10.96dBm |     |     |     |
| Tx Power    | : 0.56mW,         | -2.49dBm  |     |     |     |
| Recent      | Alarms :          |           |     |     |     |
| Rx          | power low alarm   |           |     |     |     |
| Rx          | power low warning |           |     |     |     |
| Recent      | Errors :          |           |     |     |     |
| Rx          | loss of signal    |           |     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 83

| Transceiver | in 1/1/2 |             |           |           |            |
| ----------- | -------- | ----------- | --------- | --------- | ---------- |
| Interface   | Name     | : 1/1/2     |           |           |            |
| Type        |          | : unknown   |           |           |            |
| Connector   | Type     | : ??        |           |           |            |
| Wavelength  |          | : ??        |           |           |            |
| Transfer    | Distance | : ??        |           |           |            |
| Diagnostic  | Support  | : ??        |           |           |            |
| Product     | Number   | : ??        |           |           |            |
| Serial      | Number   | : ??        |           |           |            |
| Part Number |          | : ??        |           |           |            |
| Transceiver | in 1/2/1 |             |           |           |            |
| Interface   | Name     | : 1/2/1     |           |           |            |
| Type        |          | : QSFP+SR4  |           |           |            |
| Connector   | Type     | : MPO       |           |           |            |
| Wavelength  |          | : 850nm     |           |           |            |
| Transfer    | Distance | : 0m (SMF), | 0m (OM1), | 0m (OM2), | 100m (OM3) |
| Diagnostic  | Support  | : DOM       |           |           |            |
| Product     | Number   | : JH233A    |           |           |            |
| Serial      | Number   | : MYxxxxxxx |           |           |            |
| Part Number |          | : 2005-1234 |           |           |            |
Status
| Temperature | : 44.46C |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
| Voltage     | : 3.30V  |     |     |     |     |
----------------------------------------------
|          | Tx Bias | Rx Power | Tx Power |     |     |
| -------- | ------- | -------- | -------- | --- | --- |
| Channel# | (mA)    | (mW/dBm) | (mW/dBm) |     |     |
----------------------------------------------
| 1           | 6.12           | 0.00, -inf | 0.63, -1.95 |     |     |
| ----------- | -------------- | ---------- | ----------- | --- | --- |
| 2           | 6.04           | 0.00, -inf | 0.63, -2.00 |     |     |
| 3           | 6.51           | 0.00, -inf | 0.60, -2.16 |     |     |
| 4           | 6.19           | 0.00, -inf | 0.63, -1.94 |     |     |
| Recent      | Alarms :       |            |             |     |     |
| Channel     | 1 :            |            |             |     |     |
| Rx          | power low      | alarm      |             |     |     |
| Rx          | power low      | warning    |             |     |     |
| Channel     | 2 :            |            |             |     |     |
| Rx          | power low      | alarm      |             |     |     |
| Rx          | power low      | warning    |             |     |     |
| Channel     | 3 :            |            |             |     |     |
| Rx          | power low      | alarm      |             |     |     |
| Rx          | power low      | warning    |             |     |     |
| Channel     | 4 :            |            |             |     |     |
| Rx          | power low      | alarm      |             |     |     |
| Rx          | power low      | warning    |             |     |     |
| Recent      | Errors :       |            |             |     |     |
| Channel     | 1 :            |            |             |     |     |
| Rx          | Loss of Signal |            |             |     |     |
| Channel     | 2 :            |            |             |     |     |
| Rx          | Loss of Signal |            |             |     |     |
| Channel     | 3 :            |            |             |     |     |
| Rx          | Loss of Signal |            |             |     |     |
| Channel     | 4 :            |            |             |     |     |
| Rx          | Loss of Signal |            |             |     |     |
| Transceiver | in 1/2/2       |            |             |     |     |
| Interface   | Name           | : 1/2/2    |             |     |     |
| Type        |                | : unknown  |             |     |     |
Interfaceconfiguration|84

| Connector   | Type     | : ??        |         |     |     |     |
| ----------- | -------- | ----------- | ------- | --- | --- | --- |
| Wavelength  |          | : ??        |         |     |     |     |
| Transfer    | Distance | : ??        |         |     |     |     |
| Diagnostic  | Support  | : ??        |         |     |     |     |
| Product     | Number   | : ??        |         |     |     |     |
| Serial      | Number   | : ??        |         |     |     |     |
| Part        | Number   | : ??        |         |     |     |     |
| Transceiver | in 1/3/1 |             |         |     |     |     |
| Interface   | Name     | : 1/3/1     |         |     |     |     |
| Type        |          | : SFP28DAC3 |         |     |     |     |
| Connector   | Type     | : Copper    | Pigtail |     |     |     |
Transfer Distance : 0.00km (SMF), 0m (OM1), 0m (OM2), 0m (OM3)
| Diagnostic | Support | : None       |     |     |     |     |
| ---------- | ------- | ------------ | --- | --- | --- | --- |
| Product    | Number  | : 844477-B21 |     |     |     |     |
| Serial     | Number  | : MYxxxxxxx  |     |     |     |     |
| Part       | Number  | : 77fc-7ce7  |     |     |     |     |
Showingdetailedtransceiverinformationwithidentificationofunsupportedtransceivers:
| switch#     | show interface | transceiver    | detail        |        |           |          |
| ----------- | -------------- | -------------- | ------------- | ------ | --------- | -------- |
| Transceiver | in 1/1/2       |                |               |        |           |          |
| Interface   | Name           | : 1/1/2        |               |        |           |          |
| Type        |                | : SFP+ER       | (unsupported) |        |           |          |
| Connector   | Type           | : LC           |               |        |           |          |
| Wavelength  |                | : 3590nm       |               |        |           |          |
| Transfer    | Distance       | : 80m          | (SMF), 0m     | (OM1), | 0m (OM2), | 0m (OM3) |
| Diagnostic  | Support        | : DOM          |               |        |           |          |
| Vendor      | Name           | : INNOLIGHT    |               |        |           |          |
| Vendor      | Part Number    | : TR-PX15Z-NHP |               |        |           |          |
| Vendor      | Part Revision: | 1A             |               |        |           |          |
| Vendor      | Serial number: | MYxxxxxxx      |               |        |           |          |
Status
| Temperature | : 28.88C    |         |     |     |     |     |
| ----------- | ----------- | ------- | --- | --- | --- | --- |
| Voltage     | : 3.30V     |         |     |     |     |     |
| Tx Bias     | : 65.53mA   |         |     |     |     |     |
| Rx Power    | : 0.00mW,   | -inf    |     |     |     |     |
| Tx Power    | : 1.47mW,   | 1.67dBm |     |     |     |     |
| Recent      | Alarms:     |         |     |     |     |     |
| Rx Power    | low alarm   |         |     |     |     |     |
| Rx Power    | low warning |         |     |     |     |     |
| Recent      | Errors:     |         |     |     |     |     |
| Rx loss     | of signal   |         |     |     |     |     |
Showingtransceiverthreshold-violations:
switch(config)# show interface transceiver threshold-violations
-----------------------------------------------------
| Port | Type | Channel | Type(s)   | of           | Recent |     |
| ---- | ---- | ------- | --------- | ------------ | ------ | --- |
|      |      |         | Threshold | Violation(s) |        |     |
-----------------------------------------------------
| 1/1/1 | SFP+SR   |     | Tx bias  | high | warning     |     |
| ----- | -------- | --- | -------- | ---- | ----------- | --- |
|       |          |     | 50.52    | mA > | 40.00 mA    |     |
| 1/1/2 | SFP+ER*  |     | ??       |      |             |     |
| 1/2/1 | QSFP+SR4 | 1   | Tx power | low  | alarm       |     |
|       |          |     | -17.00   | dBm  | < -0.50 dBm |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 85

|                |             |             | 2       | Tx bias      | low       | warning |     |     |     |
| -------------- | ----------- | ----------- | ------- | ------------ | --------- | ------- | --- | --- | --- |
|                |             |             |         | 3.12         | mA < 4.00 | mA      |     |     |     |
| 1/2/2          | QSFP+ER4*   |             |         | ??           |           |         |     |     |     |
| 1/3/1          | SFP28DAC3   |             |         | n/a          |           |         |     |     |     |
| * unsupported  |             | transceiver |         |              |           |         |     |     |     |
| Command        | History     |             |         |              |           |         |     |     |     |
| Release        |             |             |         | Modification |           |         |     |     |     |
| 10.07orearlier |             |             |         | --           |           |         |     |     |     |
| Command        | Information |             |         |              |           |         |     |     |     |
| Platforms      | Command     |             | context | Authority    |           |         |     |     |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                       | utilization |     |             |     |            |     |     |     |
| -------------- | --------------------- | ----------- | --- | ----------- | --- | ---------- | --- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |             |     | utilization |     | [non-zero] |     |     |     |
Description
Displaysphysicalportthroughputandutilization.
| Parameter   |     |     |     | Description                      |     |     |     |     |     |
| ----------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| <IFNAME>    |     |     |     | Specifiesaninterfacename.        |     |     |     |     |     |
| <IFRANGE>   |     |     |     | Specifiestheportidentifierrange. |     |     |     |     |     |
| utilization |     |     |     | Displaysutilizationstatistics.   |     |     |     |     |     |
| non-zero    |     |     |     | Displaysnon-zerostatistics       |     |     |     |     |     |
Examples
Thefollowingexampleshowsportutilizationofallinterfaces:
| switch# | show | interface | utilization |     |     |     |     |     |     |
| ------- | ---- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|------
---------------------|----------------------
|               |     | Interval | |   |     | RX  |     | |   | TX  | |   |
| ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Total (RX+TX) |     |          | |   |     |     |     |     |     |     |
Interface seconds | Mbps KPkt/s Util % | Mbps KPkt/s Util % |
| Mbps | KPkt/s | Util | % | Description |     |     |     |     |     |     |
| ---- | ------ | ---- | --------------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|------
---------------------|----------------------
| 1/1/1   |        |     | 300 9578.02 | 788.70   |     | 95.78 | 25.70 | 45.89 | 0.26 |
| ------- | ------ | --- | ----------- | -------- | --- | ----- | ----- | ----- | ---- |
| 9603.72 | 834.59 |     | 96.04       | Aruba-AP |     |       |       |       |      |
Interfaceconfiguration|86

| 1/1/2          |             | 300     | 25.71                 | 45.90 0.26     | 9581.09 788.96 | 95.81 |
| -------------- | ----------- | ------- | --------------------- | -------------- | -------------- | ----- |
| 9606.80        | 834.86      | 96.07   | Aruba2530-AP-conce... |                |                |       |
| 1/1/3          | - lag123    | 300     | 0.00                  | 0.00 0.00      | 0.00 0.00      | 0.00  |
| 0.00           | 0.00        | 0.00    | ISL: SWRTS-0064-1     |                |                |       |
| 1/1/4          |             | 300     | 9261.79               | 804.52 92.62   | 9496.70 823.97 | 94.97 |
| 18758.50       | 1628.48     | 187.58  | Backup                | data center... |                |       |
| 1/1/5          |             | 300     | 9496.70               | 823.97 94.97   | 9261.79 804.52 | 92.62 |
| 18758.50       | 1628.48     | 187.58  | --                    |                |                |       |
| Command        | History     |         |                       |                |                |       |
| Release        |             |         |                       | Modification   |                |       |
| 10.07orearlier |             |         |                       | --             |                |       |
| Command        | Information |         |                       |                |                |       |
| Platforms      | Command     | context |                       | Authority      |                |       |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ip           | interface |                |            |     |     |     |
| ----------------- | --------- | -------------- | ---------- | --- | --- | --- |
| show ip interface |           | <INTERFACE-ID> | [vsx-peer] |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#      | show ip        | interface | 1/1/1    |                   |     |     |
| ------------ | -------------- | --------- | -------- | ----------------- | --- | --- |
| Interface    | 1/1/1          | is up     |          |                   |     |     |
| Admin        | state is       | up        |          |                   |     |     |
| Hardware:    | Ethernet,      | MAC       | Address: | 70:72:cf:fd:e7:b4 |     |     |
| IPv4 address | 192.168.1.1/24 |           |          |                   |     |     |
| MTU 1500     |                |           |          |                   |     |     |
RX
|     | 0 packets, | 0   | bytes |     |     |     |
| --- | ---------- | --- | ----- | --- | --- | --- |
TX
|         | 0 packets, | 0   | bytes |     |     |     |
| ------- | ---------- | --- | ----- | --- | --- | --- |
| Command | History    |     |       |     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 87

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip source-interface |     |     |     |
| ------------------------ | --- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
| vsx-peer |     |     | ShowstheoutputfromtheVSXpeerswitch.Iftheswitches |
| -------- | --- | --- | ------------------------------------------------ |
donothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.This
parameterisavailableonswitchesthatsupportVSX.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
switch#
| show             | ip  | source-interface | sflow       |
| ---------------- | --- | ---------------- | ----------- |
| Source-interface |     | Configuration    | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| sflow    |     | 10.10.10.1       |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch# show     | ip  | source-interface | all         |
| ---------------- | --- | ---------------- | ----------- |
| Source-interface |     | Configuration    | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| all      |     | 1/1/1            |     |
Interfaceconfiguration|88

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

Manager (#)

Administrators or local user group members with execution
rights for this command.

show ipv6 interface
show ipv6 interface <INTERFACE-ID> [vsx-peer]

Description

Shows status and configuration information for an IPv6 interface.

Parameter

<INTERFACE-ID>

vsx-peer

Examples

Description

Specifies an interface ID. Format: member/slot/port.

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

switch# show ipv6 interface 1/1/1

Interface 1/1/1 is up

Admin state is up
IPv6 address:

2001:0db8:85a3:0000:0000:8a2e:0370:7334/24 [VALID]

IPv6 link-local address: fe80::1e98:ecff:fee3:e800/64 (default)[VALID]
IPv6 virtual address configured: none
IPv6 multicast routing: disable
IPv6 Forwarding feature: enabled
IPv6 multicast groups locally joined:

ff02::ff70:7334
ff02::2

ff02::ffe3:e800

ff02::1

ff02::1:ff00:0

IPv6 multicast (S,G) entries joined: none
IPv6 MTU: 1524 (using link MTU)
IPv6 unicast reverse path forwarding: none
IPv6 load sharing: none
RX

TX

0 packets, 0 bytes

0 packets, 0 bytes

Command History

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

89

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ipv6 | source-interface |     |     |
| --------- | ---------------- | --- | --- |
show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.                          |
| -------------- | --- | --- | ------------------------------------------------ |
| vsx-peer       |     |     | ShowstheoutputfromtheVSXpeerswitch.Iftheswitches |
donothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.This
parameterisavailableonswitchesthatsupportVSX.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch# show     | ipv6 | source-interface | sflow       |
| ---------------- | ---- | ---------------- | ----------- |
| Source-interface |      | Configuration    | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| sflow    |     | 2001:DB8::1      |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch# show     | ipv6 | source-interface | all         |
| ---------------- | ---- | ---------------- | ----------- |
| Source-interface |      | Configuration    | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| all      |     | 1/1/1            |     |
Interfaceconfiguration|90

| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
shutdown
shutdown
no shutdown
Description
Disablesaninterface.Interfacesaredisabledbydefaultwhencreated.
Thenoformofthiscommandenablesaninterface.
Examples
Disablinganinterface:
| switch(config-if)# |     | shutdown |     |
| ------------------ | --- | -------- | --- |
Enablinganinterface:
| switch(config-if)# |             | no shutdown |              |
| ------------------ | ----------- | ----------- | ------------ |
| Command            | History     |             |              |
| Release            |             |             | Modification |
| 10.07orearlier     |             |             | --           |
| Command            | Information |             |              |
| Platforms          | Command     | context     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| system | interface-group |     |     |
| ------ | --------------- | --- | --- |
system interface-group <GROUP> line-module <SLOT-ID> speed <SPEED>
| no system | interface-group | <GROUP> | line-module <SLOT-ID> |
| --------- | --------------- | ------- | --------------------- |
Description
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 91

Configuresspeedforaninterfacegroup.Afterchanginggroupspeed,onlytransceiverscompatiblewith
thenewspeedwillbeenabled.
n Allspeed-mismatchedinterfacesinthegroupwillbedisabled.
n Thiscommandcaninterruptactivenetworklinks,userconfirmationisrequiredtoproceed.
Thenoformofthiscommandresetsthespecifiedinterfacegrouptoitsdefault.
| Parameter |     |     | Description                                    |
| --------- | --- | --- | ---------------------------------------------- |
| <GROUP>   |     |     | Specifiesinterfacegrouptoconfigure.            |
| <SPEED>   |     |     | Configurestransceiverspeed(10gor25g)foragroup. |
Defaultis25g(seetheTransceiverGuideforfurtherdetail).
On8400SwitchSeries:
10gallows1Gbpsor10Gbpstransceiversonly.
25gallows25Gbpstransceiversonly.
| <SLOT-ID> |     |     | SpecifiesslotID ofthelinemodule. |
| --------- | --- | --- | -------------------------------- |
Examples
Configuringinterfacegroup1online-module1/1toallow10Gbpsandslowertransceivers:
switch(config)# system interface-group 1 line-module 1/1 speed 10g
Changing the group speed will disable all member interfaces that do not match the
new speed.
| Continue            | (y/n)? y |         |                   |
| ------------------- | -------- | ------- | ----------------- |
| Command History     |          |         |                   |
| Release             |          |         | Modification      |
| 10.09.0002orlater   |          |         | Commandintroduced |
| Command Information |          |         |                   |
| Platforms           | Command  | context | Authority         |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
Interfaceconfiguration|92

Chapter 5
|                  |           |     |     | Source | interface | selection |
| ---------------- | --------- | --- | --- | ------ | --------- | --------- |
| Source interface | selection |     |     |        |           |           |
ThesourceIPaddressisdeterminedbythesystemandistypicallytheIPaddressoftheoutgoing
interfaceintheroutingtable.However,routingswitchesmayhavemultipleroutinginterfacesand
outgoingpacketscanpotentiallybesentbydifferentpathsatdifferenttimes.Thisresultsindifferent
sourceIPaddresses.
AOS-CXprovidesaconfigurationmodelthatallowstheselectionofanIPaddresstouseasthesource
addressforalloutgoingtraffic.Thisallowsuniqueidentificationofthesoftwareapplicationonthe
serversiteregardlessofwhichlocalinterfacehasbeenusedtoreachthedestinationserver.Thesource
interfaceselectionsupportsselectinganIPaddressorinterfacename.
IfthesourceinterfaceandsourceIPareconfigured,SourceIPwillhavepriority.
| Source-interface       | selection  |           | commands         |             |     |     |
| ---------------------- | ---------- | --------- | ---------------- | ----------- | --- | --- |
| ip source-interface    | (protocol  |           | <ip-addr>)       |             |     |     |
| ip source-interface    | <PROTOCOL> | <IP-ADDR> | [vrf <VRF-NAME>] |             |     |     |
| no ip source-interface | <PROTOCOL> | <IP-ADDR> | [vrf             | <VRF-NAME>] |     |     |
Description
Configuresthesource-interfaceIPv4addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.Ifnointerfaceoptionisgiven,thedevicefloodsthroughinterfacesandVRFsto
reachArubaCentral.WhicheverreachesArubaCentralwillbepickedautomatically.
Thenoformofthiscommandremovesallconfigurations.
| Parameter  |     |     | Description                      |     |     |     |
| ---------- | --- | --- | -------------------------------- | --- | --- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoconfigure. |     |     |     |
all
Selectsallprotocolsthatcanbeconfiguredbythis
command.
central
SelectsArubaCentral.
dhcp_relay
SelectsDHCPrelay.
dns
SelectsDNS.
ntp
SelectsNTP.
radius
Selectsradius.
sflow
93
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries)

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
SelectssFLow.
simplivity
Selectssimplivity.
syslog
Selectssyslog.
tacacs
SelectsTACACS.
tftp
SelectsTFTP.
| <IP-ADDR>      |     | SpecifiestheIPv4address. |     |
| -------------- | --- | ------------------------ | --- |
| vrf <VRF-NAME> |     | SpecifiestheVRF name.    |     |
Examples
Configuringsource-interfaceIPv410.1.1.1tousefortheTFTPprotocol:
| switch(config)# | ip source-interface | tftp 10.1.1.1 |     |
| --------------- | ------------------- | ------------- | --- |
Configuringsource-interfaceIPv410.1.1.2tousefortheTFTPprotocolonVRF green:
| switch(config)# | ip source-interface | tftp 10.1.1.2 | vrf green |
| --------------- | ------------------- | ------------- | --------- |
Removingsource-interfaceIPv410.1.1.1configurationfortheTFTPprotocol:
| switch(config)# | no ip source-interface | tftp 10.1.1.1 |     |
| --------------- | ---------------------- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationforTFTPprotocolonVRFgreen:
| switch(config)# | no ip source-interface | tftp 10.1.1.2 | vrf green |
| --------------- | ---------------------- | ------------- | --------- |
Configuringsource-interfaceIPv410.1.1.1tousefortheDNSprotocol:
| switch(config)# | ip source-interface | dns 10.1.1.1 |     |
| --------------- | ------------------- | ------------ | --- |
Configuringsource-interfaceIPv410.1.1.2tousefortheDNSprotoclonVRF green:
| switch(config)# | ip source-interface | dns 10.1.1.2 | vrf green |
| --------------- | ------------------- | ------------ | --------- |
Removingsource-interfaceIPv410.1.1.1configurationfortheDNSprotocol:
| switch(config)# | no ip source-interface | tftp 10.1.1.1 |     |
| --------------- | ---------------------- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationfortheDNSprotocolonVRFgreen:
Sourceinterfaceselection|94

| switch(config)#     | no      | ip source-interface | dns 10.1.1.2 | vrf green |
| ------------------- | ------- | ------------------- | ------------ | --------- |
| Command History     |         |                     |              |           |
| Release             |         |                     | Modification |           |
| 10.07orearlier      |         |                     | --           |           |
| Command Information |         |                     |              |           |
| Platforms           | Command | context             | Authority    |           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip source-interface
ip source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
no ip source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
Description
ConfigurestheIPv4source-interfaceinterfacetouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedconfiguration.
| Parameter  |     |     | Description                      |     |
| ---------- | --- | --- | -------------------------------- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoconfigure. |     |
all
Selectsallprotocolsthatcanbeconfiguredbythis
command.
central
SelectsArubaCentral.
dhcp_relay
SelectsDHCPrelay.
dns
SelectsDNS.
ntp
SelectsNTP.
radius
Selectsradius.
sflow
SelectssFLow.
syslog
Selectssyslog.
tacacs
SelectsTACACS.
tftp
SelectsTFTP.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 95

| Parameter      |     |     |     |     | Description                |     |     |
| -------------- | --- | --- | --- | --- | -------------------------- | --- | --- |
| vrf <VRF-NAME> |     |     |     |     | SpecifiestheVRF name.      |     |     |
| <IFNAME>       |     |     |     |     | Specifiestheinterfacename. |     |     |
Examples
ConfiguringIPv4source-interfaceinterface1/1/1tousefortheTFTP protocol:
| switch(config)# |     | ip  | source-interface |     |     | tftp interface | 1/1/1 |
| --------------- | --- | --- | ---------------- | --- | --- | -------------- | ----- |
ConfiguringIPv4source-interfaceinterface1/1/2tousefortheTFTP protocolonVRFgreen:
switch(config)# ip source-interface tftp interface 1/1/2 vrf green
RemovingIPv4source-interface1/1/1configurationfortheTFTP protocol:
| switch(config)# |     | no  | ip source-interface |     |     | tftp interface | 1/1/1 |
| --------------- | --- | --- | ------------------- | --- | --- | -------------- | ----- |
Removingsource-interfaceinterface1/1/2configurationforTFTP protocolonVRFgreen:
switch(config)# no ip source-interface tftp interface 1/1/2 vrf green
| Command History     |         |     |         |     |              |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| Release             |         |     |         |     | Modification |     |     |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 source-interface
| ipv6 source-interface |     |            | <PROTOCOL> | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |     |
| --------------------- | --- | ---------- | ---------- | ----------- | --- | ---------------- | --- |
| no source-interface   |     | <PROTOCOL> |            | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |     |
Description
Configuresthesource-interfaceIPv6addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedprotocolconfiguration.
Sourceinterfaceselection|96

| Parameter  |     |     | Description                      |     |
| ---------- | --- | --- | -------------------------------- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoconfigure. |     |
n all:Selectsallprotocolssupportedbythiscommand.
n central:SelectsArubaCentral.
n ntp:SelectsNTP.
n radius:Selectsradius.
n sflow:SelectssFLow.
n syslog:Selectssyslog.
n tacacs:SelectsTACACS.
n tftp:SelectsTFTP.
| <IPV6-ADDR> |     |     | SpecifiestheIPv6address. |     |
| ----------- | --- | --- | ------------------------ | --- |
vrf <VRF-NAME>
SpecifiestheVRF name.
Examples
Configuringsource-interfaceIPv61111:2222tousefortheTFTP protocol:
switch(config)#
|     | ipv6 | source-interface | tftp 1111:2222 |     |
| --- | ---- | ---------------- | -------------- | --- |
Configuringsource-interfaceIPv61111:3333touseforTFTPprotocolonVRF green:
| switch(config)# | ipv6 | source-interface | tftp 1111:3333 | vrf green |
| --------------- | ---- | ---------------- | -------------- | --------- |
Removingsource-interfaceIPv61111:2222configurationforTFTPprotocol:
| switch(config)# | no  | ipv6 source-interface | tftp 1111:2222 |     |
| --------------- | --- | --------------------- | -------------- | --- |
Removingsource-interfaceIPv61111:3333configurationforTFTPprotocolonVRFgreen:
switch(config)# no ipv6 source-interface tftp 1111:3333 vrf green
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 97

ipv6 source-interface
ipv6 source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
no ipv6 source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]

Description

Configures the IPv6 source-interface interface to use for the specified protocol. If a VRF is not given, the
default VRF applies.

The no form of this command removes all configurations.

Parameter

<PROTOCOL>

Description

Specifies the protocol to configure.

all
Selects all protocols supported by this command.
central
Selects Aruba Central.
ntp
Selects NTP.
radius
Selects radius.
sflow
Selects sFLow.
syslog
Selects syslog.
tacacs
Selects TACACS.
tftp
SelectsTFTP.

<IFNAME>

Specifies the interface name.

vrf <VRF-NAME>

Specifies the VRF name.

<IFNAME>
Specifies the interface name.
vrf <VRF-NAME>
Specifies the VRF name.

Examples

Configuring IPv6 source-interface interface 1/1/1 to use for the TFTP protocol :

switch(config)# ipv6 source-interface tftp interface 1/1/1

Configuring IPv6 source-interface interface 1/1/2 to use for the TFTP protocol on VRF green :

switch(config)# ipv6 source-interface tftp interface 1/1/2 vrf green

Removing IPv6 source-interface interface 1/1/1 configuration for the TFTP protocol:

switch(config)# no ipv6 source-interface tftp interface 1/1/1

Removing IPv6 source-interface interface 1/1/2 configuration for the TFTP protocol on VRF green:

Source interface selection | 98

switch(config)# no ipv6 source-interface tftp interface 1/1/2 vrf green

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

config

Administrators or local user group members with execution
rights for this command.

show ip source-interface
show ip source-interface <PROTOCOL> [vrf <VRF-NAME> | all-vrfs]

Description

Displays the source interface information for all VRFs or a specific VRF.

If a VRF is not specified, the default is displayed.

Parameter

<PROTOCOL>

Description

Specifies the protocol to show.
all

Shows the source interface configuration for all other
protocols.

central

Shows the source interface configuration for Aruba
Central.
dhcp relay

Shows the source interface configuration for DHCP
relay.

dns

Shows the source interface configuration for DNS.

ntp

Shows the source interface configuration for NTP.

radius

Shows the source interface configuration for radius.

sflow

Shows the source interface configuration for sFLow.

syslog

Shows the source interface configuration for syslog.

tacacs

Shows the source interface configuration for TACACS.

tftp

Shows the source interface configuration for TFTP.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

99

| Parameter      |     |     | Description                                     |     |
| -------------- | --- | --- | ----------------------------------------------- | --- |
| vrf <VRF-NAME> |     |     | SpecifiestheVRF name.                           |     |
| all-vrfs       |     |     | ShowsthesourceinterfaceconfigurationforallVRFs. |     |
Examples
Displayingallsource-interfaceprotocolconfigurationsforVRF red:
| switch# show     | ip source-interface |     | all vrf red |     |
| ---------------- | ------------------- | --- | ----------- | --- |
| Source-interface | Configuration       |     | Information |     |
---------------------------------------------------------------
| Protocol | Src-Interface |     | Src-IP | VRF |
| -------- | ------------- | --- | ------ | --- |
---------------------------------------------------------------
| all | 1/1/1 |     |     | red |
| --- | ----- | --- | --- | --- |
switch#
Displayingallsource-interfaceprotocolconfigurationsfordefaultVRF:
| switch# show     | ip source-interface |     | all         |     |
| ---------------- | ------------------- | --- | ----------- | --- |
| Source-interface | Configuration       |     | Information |     |
-------------------------------------------------------------------
| Protocol | Src-Interface |     | Src-IP | VRF |
| -------- | ------------- | --- | ------ | --- |
-------------------------------------------------------------------
| all |     |     | 1.1.1.1 | default |
| --- | --- | --- | ------- | ------- |
switch#
Displaying allsource-interfaceprotocolconfigurationsforallVRFs:
| switch# show     | ip source-interface |     | all all-vrfs |     |
| ---------------- | ------------------- | --- | ------------ | --- |
| Source-interface | Configuration       |     | Information  |     |
-------------------------------------------------------------------
| Protocol | Src-Interface |     | Src-IP | VRF |
| -------- | ------------- | --- | ------ | --- |
-------------------------------------------------------------------
| all |         |     | 2.2.2.2 | all-vrfs |
| --- | ------- | --- | ------- | -------- |
| all |         |     | 1.1.1.1 | default  |
| all | 1/1/1/1 |     |         | red      |
switch#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| show ipv6 | source-interface |     |     |     |
| --------- | ---------------- | --- | --- | --- |
Sourceinterfaceselection|100

show ipv6 source-interface <PROTOCOL> [detail] [vrf <VRF-NAME> | all-vrfs]
Description
DisplaystheIPV6sourceinterfaceinformationconfiguredintherouterforallVRFsoraspecificVRF.
IfaVRF isnotspecified,thedefaultisdisplayed.
| Parameter  |     | Description                 |     |
| ---------- | --- | --------------------------- | --- |
| <PROTOCOL> |     | Specifiestheprotocoltoshow. |     |
all
Showsthesourceinterfaceconfigurationforallother
protocols.
central
ShowsthesourceinterfaceconfigurationforAruba
Central.
ntp
ShowsthesourceinterfaceconfigurationforNTP.
radius
Showsthesourceinterfaceconfigurationforradius.
sflow
ShowsthesourceinterfaceconfigurationforsFLow.
syslog
Showsthesourceinterfaceconfigurationforsyslog.
tacacs
ShowsthesourceinterfaceconfigurationforTACACS.
tftp
ShowsthesourceinterfaceconfigurationforTFTP.
| vrf <VRF-NAME> |     | SpecifiestheVRF name.                          |     |
| -------------- | --- | ---------------------------------------------- | --- |
| all-vrfs       |     | ShowsthesourceinterfaceconfigurationforallVRF. |     |
Examples
DisplayingallIPv6source-interfaceprotocolconfigurationsfordefaultVRF:
| switch# show     | ipv6 source-interface | all         |     |
| ---------------- | --------------------- | ----------- | --- |
| Source-interface | Configuration         | Information |     |
------------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
------------------------------------------------------------------
| all |     | 1111:2222 | default |
| --- | --- | --------- | ------- |
switch#
DisplayingallIPv6source-interfaceprotocolconfigurationforVRFred:
| switch# show     | ipv6 source-interface | all vrf red |     |
| ---------------- | --------------------- | ----------- | --- |
| Source-interface | Configuration         | Information |     |
---------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
---------------------------------------------------------------
| all | 1/1/1 |     | red |
| --- | ----- | --- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 101

switch#
Displaying allIPv6source-interfaceprotocolconfigurationsforallVRFs:
| switch# show     | ipv6 | source-interface |     |             | all all-vrfs |     |     |
| ---------------- | ---- | ---------------- | --- | ----------- | ------------ | --- | --- |
| Source-interface |      | Configuration    |     | Information |              |     |     |
-------------------------------------------------------------------
| Protocol |     | Src-Interface |     |     | Src-IP |     | VRF |
| -------- | --- | ------------- | --- | --- | ------ | --- | --- |
-------------------------------------------------------------------
| all |     |       |     |     | 2.2.2.2:3.3.3.3 |     | all-vrfs |
| --- | --- | ----- | --- | --- | --------------- | --- | -------- |
| all |     |       |     |     | 1.1.1.1:2.2.2.2 |     | default  |
| all |     | 1/1/1 |     |     | 2::2            |     | red      |
switch#
| Command History     |         |     |         |     |              |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| Release             |         |     |         |     | Modification |     |     |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show running-config
show running-config
Description
Displaysthecurrentrunningconfiguration.
Examples
Displayingtherunningconfiguration(onlyitemsofinteresttosourceinterfaceselectionareshownin
thisexampleoutputcommand):
ArubaCentralisthepriorityagent.Ifnocommandisspecifiedforipsource-interface,Centralwillchoosethe
commandautomaticallyifitisreachableonanyoftheknownports.
| switch# show | running-config |     |     |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- | --- | --- |
vrf green
| ip source-interface   |     |     | tftp interface   |           | 1/1/2     | vrf green |     |
| --------------------- | --- | --- | ---------------- | --------- | --------- | --------- | --- |
| ip source-interface   |     |     | radius interface |           | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | ntp interface    |           | 1/1/2 vrf | green     |     |
| ip source-interface   |     |     | tacacs interface |           | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | dns interface    |           | 1/1/2 vrf | green     |     |
| ip source-interface   |     |     | central          | interface | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | all interface    |           | 1/1/2 vrf | green     |     |
| ipv6 source-interface |     |     | tftp 2222::3333  |           | vrf       | green     |     |
Sourceinterfaceselection|102

| ipv6 source-interface |                      | radius 2222::3333  | vrf green |
| --------------------- | -------------------- | ------------------ | --------- |
| ipv6 source-interface |                      | ntp 2222::3333     | vrf green |
| ipv6 source-interface |                      | tacacs 2222::3333  | vrf green |
| ipv6 source-interface |                      | central 2222::3333 | vrf green |
| ipv6 source-interface |                      | all 2222::3333     | vrf green |
| ip source-interface   |                      | tftp 10.20.3.1     |           |
| ip source-interface   |                      | radius 10.20.3.1   |           |
| ip source-interface   |                      | ntp 10.20.3.1      |           |
| ip source-interface   |                      | tacacs 10.20.3.1   |           |
| ip source-interface   |                      | dns 10.20.3.1      |           |
| ip source-interface   |                      | central 10.20.3.1  |           |
| ip source-interface   |                      | all 10.20.3.1      |           |
| interface             | 1/1/1                |                    |           |
| no                    | shutdown             |                    |           |
| ip                    | address 10.20.3.1/24 |                    |           |
| interface             | 1/1/2                |                    |           |
| vrf                   | attach green         |                    |           |
| ip                    | address 20.1.1.1/24  |                    |           |
| ipv6                  | address              | 2222::3333/64      |           |
| interface             | 1/1/45               |                    |           |
| no                    | shutdown             |                    |           |
| ip                    | address 100.1.0.1/24 |                    |           |
| ipv6                  | address              | 1111::2222/64      |           |
| ip route              | 100.2.0.0/24         | 10.20.3.2          |           |
switch#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 103

Chapter 6

VLANs

VLANs

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of
users by logical function instead of physical location. They make managing bandwidth usage within
networks possible by:

n Allowing grouping of high-bandwidth users on low-traffic segments

n Organizing users from different LAN segments according to their need for common resources and

individual protocols

n Improving traffic control at the edge of networks by separating traffic of different protocol types.

n Enhancing network security by creating subnets to control in-band access to specific network

resources

VLANs are generally assigned on an organizational basis rather than on a physical basis. For example, a
network administrator could assign all workstations and servers used by a particular workgroup to the
same VLAN, regardless of their physical locations.

Hosts in the same VLAN can directly communicate with one another. A router or a Layer 3 switch is
required for hosts in different VLANs to communicate with one another.

VLANs help reduce bandwidth waste, improve LAN security, and enable network administrators to
address issues such as scalability and network management.

Refer to the Layer 2 Bridging Guide for VLAN configuration and commands.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

104

Chapter 7
|               |               | Configuration | and firmware | management |
| ------------- | ------------- | ------------- | ------------ | ---------- |
| Configuration | and firmware  | management    |              |            |
| Upgrade       | and downgrade | scenarios     |              |            |
UpgradeanddowngradescenariosareprovidedbytheConfiguration MigrationFramework(CMF).
Upgrades
Allupgradescenariosaresupportedandconfigurationismigrated.
Downgrades
Thefollowingscenarioissupported:
Createacheckpointbeforeupgrading.
Upgrade.
Performconfigchanges.
Setthestartupconfigurationtothecheckpointcreatedinstep1.
Downgrade
Configurationchangesthatoccurafterthecheckpointinstep1willbelostduringthedowngrade.
Limitations
ThefollowingarethelimitationsofupgradeanddowngradescenariosprovidedbyCMF.
Table1:Configurationfromandtothesamebuild
| From/to    |     | Checkpoint | Running | Startup   |
| ---------- | --- | ---------- | ------- | --------- |
| Checkpoint |     | N/A        |         | Supported |
Supported
| Running                   |     | Supported | N/A       | Supported |
| ------------------------- | --- | --------- | --------- | --------- |
| Startup                   |     | Supported | Supported | N/A       |
| ConfigfromURLinCLIFormat  |     | Supported | Supported | Supported |
| ConfigfromURLinJSONFormat |     | Supported | Supported | Supported |
Table2:Configurationfromanolderbuildtoanewerbuild(upgrade)
| From/to |     | Checkpoint | Running | Startup |
| ------- | --- | ---------- | ------- | ------- |
ConfigfromURLinCLIFormat Notsupported Notsupported Notsupported
105
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries)

| From/to |     | Checkpoint | Running | Startup |
| ------- | --- | ---------- | ------- | ------- |
ConfigfromURLinJSONFormat Notsupported Notsupported Notsupported
| Startup |     | Notsupported | Supported | Supported |
| ------- | --- | ------------ | --------- | --------- |
Table3:Configurationfromanewerbuildtoanolderbuild(downgrade)
| From/to |     | Checkpoint | Running | Startup |
| ------- | --- | ---------- | ------- | ------- |
ConfigfromURLinCLIFormat Notsupported Notsupported Notsupported
ConfigfromURLinJSONFormat Notsupported Notsupported Notsupported
| Startup |     | Notsupported | Notsupported | Notsupported |
| ------- | --- | ------------ | ------------ | ------------ |
Checkpoints
Acheckpointisasnapshotoftherunningconfigurationofaswitchanditsrelevantmetadataduringthe
timeofcreation.Checkpointscanbeusedtoapplytheswitchconfigurationstoredwithinacheckpoint
wheneverneeded,suchastoreverttoaprevious,cleanconfiguration.Checkpointscanbeappliedto
otherswitchesofthesameplatform.Aswitchisabletostoremultiplecheckpoints.
| Checkpoint | types |     |     |     |
| ---------- | ----- | --- | --- | --- |
Theswitchsupportstwotypesofcheckpoints:
n System generated checkpoints:Theswitchautomaticallygeneratesasystemcheckpointwhenever
aconfigurationchangeoccurs.
n User generated checkpoints:Theadministratorcanmanuallygenerateacheckpointwhenever
required.
| Maximum | number | of checkpoints |     |     |
| ------- | ------ | -------------- | --- | --- |
n Maximumcheckpoints:64(includingthestartupconfiguration)
n Maximumusercheckpoints:32
n Maximumsystemcheckpoints:32
| User | generated | checkpoints |     |     |
| ---- | --------- | ----------- | --- | --- |
Usercheckpointscanbecreatedatanytime,aslongasoneconfigurationdifferenceexistssincethelast
checkpointwascreated.Checkpointscanbeappliedtoeithertherunningorstartupconfigurationson
theswitch.
Allusergeneratedcheckpointsincludeatimestamptoidentifywhenacheckpointwascreated.
Amaximumof32usergeneratedcheckpointscanbecreated.
| System | generated | checkpoints |     |     |
| ------ | --------- | ----------- | --- | --- |
Systemgeneratedcheckpointsareautomaticallycreatedbydefault.Wheneveraconfigurationchange
occurs,theswitchstartsatimeoutcounter(300secondsbydefault).Foreachadditionalconfiguration
Configurationandfirmwaremanagement |106

change, the timeout counter is restarted. If the timeout expires with no additional configuration
changes being made, the switch generates a new checkpoint.

System generated checkpoints are named with the prefix CPC followed by a time stamp in the format
<YYYYMMDDHHMMSS>. For example: CPC20170630073127.

System checkpoints can be applied using the checkpoint rollback feature or copy command.

A maximum of 32 system checkpoints can be created. Beyond this limit, the newest system checkpoint
replaces the oldest system checkpoint.

Supported remote file formats

You can restore a switch configuration by copying a switch configuration stored on a USB drive or a
remote network device through SFTP/TFTP. The remote file formats that the switch supports depends
on where you plan to restore the checkpoint.

Restoring a checkpoint to a...

File type supported

Running configuration

Startup configuration

n CLI
n JSON
n Checkpoint

n JSON
n Checkpoint

Specified checkpoint

Specified checkpoint

Rollback

The term rollback is used to refer to when a switch configuration is reverted to a pre-existing
checkpoint.

For example, the following command applies the configuration from checkpoint ckpt1. All previous
configurations are lost after the execution of this command: checkpoint rollback ckpt1

You can also specify the rollback of the running configuration or of the startup configuration with a
specified checkpoint, as shown with the following command: copy checkpoint <checkpoint-name>
{running-config | startup-config}

Checkpoint auto mode

Checkpoint auto mode configures the switch with failover support, causing it to automatically revert to a
previous configuration if it becomes inoperable or inaccessible due to configuration changes that are
being made.

After entering checkpoint auto mode, you have a set amount of time to add, remove, or modify the
existing switch configuration. To save your changes, you must execute the checkpoint auto confirm
command before the auto mode timer expires. If you do not execute the checkpoint auto confirm
command within the specified time, all configuration changes you made are discarded and the running
configuration reverts to the state it was before entering checkpoint auto mode.

Testing a switch configuration in checkpoint auto mode

Process overview:

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

107

1. Enablethecheckpointautomode.
2. Tosavetheconfiguration,enterthecheckpoint auto confirmcommandbeforethespecified
timesetinstep1.
| Checkpoint | commands                   |     |
| ---------- | -------------------------- | --- |
| checkpoint | auto                       |     |
| checkpoint | auto <TIME-LAPSE-INTERVAL> |     |
Description
Startsautocheckpointmode.Inautocheckpointmode,theswitchtemporarilysavestheruntime
configurationasacheckpointonlyforthespecifiedtimelapseinterval.Configurationchangesmustbe
savedbeforetheintervalexpires,otherwisetheruntimeconfigurationisrestoredfromthetemporary
checkpoint.
| Parameter |     | Description |
| --------- | --- | ----------- |
<TIME-LAPSE-INTERVAL> Specifiesthetimelapseintervalinminutes.Range:1to60.
Usage
Tosavetheruntimecheckpointpermanently,runthecheckpoint auto confirmcommandduringthe
timelapseinterval.ThefilenameforthesavedcheckpointisnamedAUTO<YYYYMMDDHHMMSS>.Ifthe
checkpoint auto confirmcommandisnotenteredduringthespecifiedtimelapseinterval,the
previousruntimeconfigurationisrestored.
Examples
Confirmingtheautocheckpoint:
| switch#         | checkpoint auto 20 |                 |
| --------------- | ------------------ | --------------- |
| Auto checkpoint | mode expires       | in 20 minute(s) |
switch# WARNING Please "checkpoint auto confirm" within 2 minutes
| switch#    | checkpoint auto confirm |         |
| ---------- | ----------------------- | ------- |
| checkpoint | AUTO20170801011154      | created |
Inthisexample,theruntimecheckpointwassavedbecausethecheckpoint auto confirmcommand
wasenteredwithinthevaluesetbythetime-lapse-intervalparameter,whichwas20minutes.
Notconfirmingtheautocheckpoint:
| switch#         | checkpoint auto 20 |                 |
| --------------- | ------------------ | --------------- |
| Auto checkpoint | mode expires       | in 20 minute(s) |
switch# WARNING Please "checkpoint auto confirm" within 2 minutes
WARNING: Restoring configuration. Do NOT add any new configuration.
| Restoration | successful |     |
| ----------- | ---------- | --- |
Inthisexample,theruntimecheckpointwasrevertedbecausethecheckpoint auto confirmcommand
wasnotenteredwithinthevaluesetbythetime-lapse-intervalparameter,whichwas20minutes.
| Command | History |     |
| ------- | ------- | --- |
Configurationandfirmwaremanagement |108

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint      | auto    | confirm |     |
| --------------- | ------- | ------- | --- |
| checkpoint auto | confirm |         |     |
Description
Signalstotheswitchtosavetherunningconfigurationusedduringtheautocheckpointmode.This
commandalsoendstheautocheckpointmode.
Usage
Tosavetheruntimecheckpointpermanently,runthecheckpoint confirmcommandduringthe
auto
timelapsevaluesetbythecheckpoint auto <TIME-LAPSE-INTERVAL>command.Thegenerated
checkpointnamewillbeintheformatAUTO<YYYYMMDDHHMMSS>.Ifthecheckpoint auto confirm
commandisnotenteredduringthespecifiedtimelapseinterval,thepreviousruntimeconfigurationis
restored.
Examples
Confirmingtheautocheckpoint:
| switch# checkpoint  |         | auto confirm |              |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint | diff |     |     |
| ---------- | ---- | --- | --- |
checkpoint diff {<CHECKPOINT-NAME1> | running-config | startup-config}
| {<CHECKPOINT-NAME2> |     | | running-config | | startup-config} |
| ------------------- | --- | ---------------- | ----------------- |
Description
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 109

Showsthedifferenceinconfigurationbetweentwoconfigurations.Comparecheckpoints,therunning
configuration,orthestartupconfiguration.
Parameter Description
| {<CHECKPOINT-NAME1> |     | | running-config |     | | startup-config} |
| ------------------- | --- | ---------------- | --- | ----------------- |
Selectseitheracheckpoint,the
runningconfiguration,orthestartup
configurationasthebaseline.
{<CHECKPOINT-NAME2> | running-config | startup-config} Selectseitheracheckpoint,the
runningconfiguration,orthestartup
configurationtocompare.
Usability
| Theoutputofthecheckpoint |     |     | diffcommandhasseveralsymbols: |     |
| ------------------------ | --- | --- | ----------------------------- | --- |
n Theplussign(+)atthebeginningofalineindicatesthatthelineexistsinthecomparisonbutnotin
thebaseline.
n Theminussign(-)atthebeginningofalineindicatesthatthelineexistsinthebaselinebutnotinthe
comparison.
Examples
Inthefollowingexample,theconfigurationsofcheckpointscp1andcp2aredisplayedbeforethe
checkpoint diffcommand,sothatyoucanseethecontextofthecheckpoint diffcommand.
| switch#    | show checkpoint |     | cp1 |     |
| ---------- | --------------- | --- | --- | --- |
| Checkpoint | configuration:  |     |     |     |
!
| !Version   | AOS-CX         | XL.10.00.0002 |        |     |
| ---------- | -------------- | ------------- | ------ | --- |
| !Schema    | version        | 0.1.8         |        |     |
| module 1/1 | product-number |               | jl363a |     |
!
!
!
!
!
!
!
vlan 1,200
| interface   | 1/1/1           |            |     |     |
| ----------- | --------------- | ---------- | --- | --- |
| no shutdown |                 |            |     |     |
| ip address  |                 | 1.0.0.1/24 |     |     |
| interface   | 1/1/2           |            |     |     |
| no shutdown |                 |            |     |     |
| ip address  |                 | 2.0.0.1/24 |     |     |
| switch#     | show checkpoint |            | cp2 |     |
| Checkpoint  | configuration:  |            |     |     |
!
| !Version   | AOS-CX         | XL.10.00.0002 |        |     |
| ---------- | -------------- | ------------- | ------ | --- |
| !Schema    | version        | 0.1.8         |        |     |
| module 1/1 | product-number |               | jl363a |     |
!
!
!
!
!
Configurationandfirmwaremanagement |110

!
!
vlan 1,200,300
| interface          | 1/1/1      |              |     |
| ------------------ | ---------- | ------------ | --- |
| no shutdown        |            |              |     |
| ip address         | 1.0.0.1/24 |              |     |
| interface          | 1/1/2      |              |     |
| no shutdown        |            |              |     |
| ip address         | 2.0.0.1/24 |              |     |
| switch# checkpoint |            | diff cp1 cp2 |     |
--- /tmp/chkpt11501550258421 2017-08-01 01:17:38.420514016 +0000
+++ /tmp/chkpt21501550258421 2017-08-01 01:17:38.420514016 +0000
| @@ -9,7 +9,7 | @@  |     |     |
| ------------ | --- | --- | --- |
!
!
!
| -vlan 1,200         |            |         |              |
| ------------------- | ---------- | ------- | ------------ |
| +vlan 1,200,300     |            |         |              |
| interface           | 1/1/1      |         |              |
| no shutdown         |            |         |              |
| ip address          | 1.0.0.1/24 |         |              |
| Command History     |            |         |              |
| Release             |            |         | Modification |
| 10.07orearlier      |            |         | --           |
| Command Information |            |         |              |
| Platforms           | Command    | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint                    | post-configuration |     |     |
| ----------------------------- | ------------------ | --- | --- |
| checkpoint post-configuration |                    |     |     |
| no checkpoint                 | post-configuration |     |     |
Description
Enablescreationofsystemgeneratedcheckpointswhenconfigurationchangesoccur.Thisfeatureis
enabledbydefault.
Thenoformofthiscommanddisablessystemgeneratedcheckpoints.
Usage
Systemgeneratedcheckpointsareautomaticallycreatedbydefault.Wheneveraconfigurationchange
occurs,theswitchstartsatimeoutcounter(300secondsbydefault).Foreachadditionalconfiguration
change,thetimeoutcounterisrestarted.Ifthetimeoutexpireswithnoadditionalconfiguration
changesbeingmade,theswitchgeneratesanewcheckpoint.
SystemgeneratedcheckpointsarenamedwiththeprefixCPCfollowedbyatimestampintheformat
<YYYYMMDDHHMMSS>.Forexample:CPC20170630073127.
Systemcheckpointscanbeappliedusingthecheckpointrollbackfeatureorcopycommand.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 111

Amaximumof32systemcheckpointscanbecreated.Beyondthislimit,thenewestsystemcheckpoint
replacestheoldestsystemcheckpoint.
Examples
Enablingsystemcheckpoints:
| switch(config)# |     | checkpoint |     | post-configuration |     |     |
| --------------- | --- | ---------- | --- | ------------------ | --- | --- |
Disablingsystemcheckpoints:
| switch(config)# |             | no  | checkpoint | post-configuration |              |     |
| --------------- | ----------- | --- | ---------- | ------------------ | ------------ | --- |
| Command         | History     |     |            |                    |              |     |
| Release         |             |     |            |                    | Modification |     |
| 10.07orearlier  |             |     |            |                    | --           |     |
| Command         | Information |     |            |                    |              |     |
| Platforms       | Command     |     | context    |                    | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint    | post-configuration |     |     |         | timeout   |     |
| ------------- | ------------------ | --- | --- | ------- | --------- | --- |
| checkpoint    | post-configuration |     |     | timeout | <TIMEOUT> |     |
| no checkpoint | post-configuration |     |     | timeout | <TIMEOUT> |     |
Description
Setsthetimeoutforthecreationofsystemcheckpoints.Thetimeoutspecifiestheamountoftimesince
thelatestconfigurationfortheswitchtocreateasystemcheckpoint.
Thenoformofthiscommandresetsthetimeoutto300seconds,regardlessofthevalueofthe
<TIMEOUT>parameter.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
timeout <TIMEOUT> Specifiesthetimeoutinseconds.Range:5to600.Default:300.
Examples
Settingthetimeoutforsystemcheckpointsto60seconds:
| switch(config)# |     | checkpoint |     | post-configuration |     | timeout 60 |
| --------------- | --- | ---------- | --- | ------------------ | --- | ---------- |
Resettingthetimeoutforsystemcheckpointsto300seconds:
Configurationandfirmwaremanagement |112

| switch(config)# |             | no  | checkpoint | post-configuration |              | timeout 1 |
| --------------- | ----------- | --- | ---------- | ------------------ | ------------ | --------- |
| Command         | History     |     |            |                    |              |           |
| Release         |             |     |            |                    | Modification |           |
| 10.07orearlier  |             |     |            |                    | --           |           |
| Command         | Information |     |            |                    |              |           |
| Platforms       | Command     |     | context    |                    | Authority    |           |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint | rename |                       |     |     |                       |     |
| ---------- | ------ | --------------------- | --- | --- | --------------------- | --- |
| checkpoint | rename | <OLD-CHECKPOINT-NAME> |     |     | <NEW-CHECKPOINT-NAME> |     |
Description
Renamesanexistingcheckpoint.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<OLD-CHECKPOINT-NAME> Specifiesthenameofanexistingcheckpointtoberenamed.
<NEW-CHECKPOINT-NAME> Specifiesthenewnameforthecheckpoint.Thecheckpointname
canbealphanumeric.Itcanalsocontainunderscores(_)and
dashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitis
usedforsystem-generatedcheckpoints.
Examples
Renamingcheckpointckpt1tocfg001:
| switch#        | checkpoint  |     | rename ckpt1 | cfg001 |              |     |
| -------------- | ----------- | --- | ------------ | ------ | ------------ | --- |
| Command        | History     |     |              |        |              |     |
| Release        |             |     |              |        | Modification |     |
| 10.07orearlier |             |     |              |        | --           |     |
| Command        | Information |     |              |        |              |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 113

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint | rollback |                    |                   |     |
| ---------- | -------- | ------------------ | ----------------- | --- |
| checkpoint | rollback | {<CHECKPOINT-NAME> | | startup-config} |     |
Description
Appliestheconfigurationfromapre-existingcheckpointorthestartupconfigurationtotherunning
configuration.
| Parameter         |     |     | Description                       |     |
| ----------------- | --- | --- | --------------------------------- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesacheckpointname.         |     |
| startup-config    |     |     | Specifiesthestartupconfiguration. |     |
Examples
Applyingacheckpointnamedckpt1totherunningconfiguration:
| switch# | checkpoint | rollback ckpt1 |     |     |
| ------- | ---------- | -------------- | --- | --- |
Success
Applyingastartupcheckpointtotherunningconfiguration:
| switch# | checkpoint | rollback startup-config |     |     |
| ------- | ---------- | ----------------------- | --- | --- |
Success
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy checkpoint |     | <CHECKPOINT-NAME> |     | <REMOTE-URL> |
| --------------- | --- | ----------------- | --- | ------------ |
copy checkpoint <CHECKPOINT-NAME> <REMOTE-URL> [vrf <VRF-NAME>]
Description
Copiesacheckpointconfigurationtoaremotelocationasafile.Theconfigurationisexportedin
checkpointformat,whichincludesswitchconfigurationandrelevantmetadata.
Configurationandfirmwaremanagement |114

| Parameter         |     |     | Description                    |     |     |     |
| ----------------- | --- | --- | ------------------------------ | --- | --- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint. |     |     |     |
<REMOTE-URL> Specifiestheremotedestinationandfilenameusingthesyntax:
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname. |     |     |     |
| -------------- | --- | --- | ------------------ | --- | --- | --- |
Examples
CopyingcheckpointconfigurationtoremotefilethroughTFTP:
switch# copy checkpoint ckpt1 tftp://192.168.1.10/ckptmeta vrf default
######################################################################### 100.0%
Success
CopyingcheckpointconfigurationtoremotefilethroughSFTP:
switch# copy checkpoint ckpt1 sftp://root@192.168.1.10/ckptmeta vrf default
The authenticity of host '192.168.1.10 (192.168.1.10)' can't be established.
ECDSA key fingerprint is SHA256:FtOm6Uxuxumil7VCwLnhz92H9LkjY+eURbdddOETy50.
| Are you             | sure you want | to continue       | connecting | (yes/no)? | yes |     |
| ------------------- | ------------- | ----------------- | ---------- | --------- | --- | --- |
| root@192.168.1.10's |               | password:         |            |           |     |     |
| sftp> put           | /tmp/ckptmeta | ckptmeta          |            |           |     |     |
| Uploading           | /tmp/ckptmeta | to /root/ckptmeta |            |           |     |     |
Warning: Permanently added '192.168.1.10' (ECDSA) to the list of known hosts.
| Connected | to 192.168.1.10. |     |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- | --- |
Success
| Command        | History     |         |              |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy checkpoint |     | <CHECKPOINT-NAME> |     | {running-config |     | | startup- |
| --------------- | --- | ----------------- | --- | --------------- | --- | ---------- |
config}
copy checkpoint <CHECKPOINT-NAME> {running-config | startup-config}
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 115

Description
Copiesanexistingcheckpointconfigurationtotherunningconfigurationortothestartupconfiguration.
| Parameter         |     |                 | Description                             |     |
| ----------------- | --- | --------------- | --------------------------------------- | --- |
| <CHECKPOINT-NAME> |     |                 | Specifiesthenameofanexistingcheckpoint. |     |
| {running-config   | |   | startup-config} |                                         |     |
Selectswhethertherunningconfigurationorthestartup
configurationreceivesthecopiedcheckpointconfiguration.If
thestartupconfigurationisalreadypresent,thecommand
overwritesthestartupconfiguration.
Examples
Copyingckpt1checkpointtotherunningconfiguration:
| switch# copy | checkpoint | ckpt1 | running-config |     |
| ------------ | ---------- | ----- | -------------- | --- |
Success
Copyingckpt1checkpointtothestartupconfiguration:
| switch# copy | checkpoint | ckpt1 | startup-config |     |
| ------------ | ---------- | ----- | -------------- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy checkpoint |                   | <CHECKPOINT-NAME> |               | <STORAGE-URL> |
| --------------- | ----------------- | ----------------- | ------------- | ------------- |
| copy checkpoint | <CHECKPOINT-NAME> |                   | <STORAGE-URL> |               |
Description
CopiesanexistingcheckpointconfigurationtoaUSBdrive.Thefileformatisdefinedwhenthe
checkpointwascreated.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<CHECKPOINT-NAME> Specifiesthenameofthecheckpointtocopy.Thecheckpoint
namecanbealphanumeric.Itcanalsocontainunderscores(_)
anddashes(-).
Configurationandfirmwaremanagement |116

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<STORAGE-URL>> SpecifiesthenameofthetargetfileontheUSBdriveusingthe
followingsyntax:usb:/<FILE>
TheUSBdrivemustbeformattedwiththeFATfilesystem.
Examples
CopyingthetestcheckpointtothetestCheckfileontheUSBdrive:
| switch# copy | checkpoint | test usb:/testCheck |     |
| ------------ | ---------- | ------------------- | --- |
Success
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy <REMOTE-URL> |     | checkpoint | <CHECKPOINT-NAME> |
| ----------------- | --- | ---------- | ----------------- |
copy <REMOTE-URL> checkpoint <CHECKPOINT-NAME> [vrf <VRF-NAME>]
Description
Copiesaremoteconfigurationfiletoacheckpoint.Theremoteconfigurationfilemustbeincheckpoint
format.
| Parameter    |     |     | Description                                  |
| ------------ | --- | --- | -------------------------------------------- |
| <REMOTE-URL> |     |     | Specifiesaremotefileusingthefollowingsyntax: |
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
<CHECKPOINT-NAME> Specifiesthenameofthetargetcheckpoint.Thecheckpointname
canbealphanumeric.Itcanalsocontainunderscores(_)and
dashes(-).Required.
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitis
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 117

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
usedforsystem-generatedcheckpoints.
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | ---------------------------------- | --- | --- |
Examples
Copyingacheckpointformatfiletocheckpointckpt5onthedefaultVRF:
| switch# copy | tftp://192.168.1.10/ckptmeta |     |     | checkpoint | ckpt5 |
| ------------ | ---------------------------- | --- | --- | ---------- | ----- |
######################################################################### 100.0%
100.0%
Success
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy <REMOTE-URL> |     | {running-config |     | | startup-config} |     |
| ----------------- | --- | --------------- | --- | ----------------- | --- |
copy <REMOTE-URL> {running-config | startup-config } [vrf <VRF-NAME>]
Description
Copiesaremotefilecontainingaswitchconfigurationtotherunningconfigurationortothestartup
configuration.
| Parameter    |     |     | Description                                 |     |     |
| ------------ | --- | --- | ------------------------------------------- | --- | --- |
| <REMOTE-URL> |     |     | Specifiesaremotefilewiththefollowingsyntax: |     |     |
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationreceivesthecopiedcheckpointconfiguration.If
thestartupconfigurationisalreadypresent,thecommand
overwritesthestartupconfiguration.
Configurationandfirmwaremanagement |118

| Parameter      |     | Description                             |     |
| -------------- | --- | --------------------------------------- | --- |
| vrf <VRF-NAME> |     | SpecifiesthenameofaVRF.Default:default. |     |
Usage
Theswitchcopiesonlycertainfiletypes.Theformatofthefileisautomaticallydetectedfromcontents
ofthefile.Thestartup-configoptiononlysupportstheJSONfileformatandcheckpoints,butthe
running-configoptionsupportstheJSONandCLIfileformatsandcheckpoints.
WhenafileoftheCLIformatiscopied,itoverwritestherunningconfiguration.TheCLIcommanddoes
notcleartherunningconfigurationbeforeapplyingtheCLIcommands.AlloftheCLIcommandsinthe
fileareappliedline-by-line.IfaparticularCLIcommandfails,theswitchlogsthefailureanditcontinues
tothenextlineintheCLIconfiguration.Theeventlog(show events -d hpe-config)provides
informationastowhichcommandfailed.
Examples
CopyingaJSONformatfiletotherunningconfiguration:
| switch# | copy tftp://192.168.1.10/runjson |     | running-config |
| ------- | -------------------------------- | --- | -------------- |
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Success
CopyingaCLIformatfiletotherunningconfigurationwithanerrorinthefile:
| switch# | copy tftp://192.168.1.10/runcli |     | running-config |
| ------- | ------------------------------- | --- | -------------- |
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Some of the configuration lines from the file were NOT applied. Use 'show
| events | -d hpe-config' | for more info. |     |
| ------ | -------------- | -------------- | --- |
CopyingaCLIformatfiletothestartupconfiguration:
| switch# | copy tftp://192.168.1.10/startjson |     | startup-config |
| ------- | ---------------------------------- | --- | -------------- |
######################################################################### 100.0%
100.0%
Success
Copyinganunsupportedfileformattothestartupconfiguration:
| switch# | copy tftp://192.168.1.10/startfile |     | startup-config |
| ------- | ---------------------------------- | --- | -------------- |
######################################################################### 100.0%
100.0%
| unsupported | file format |     |     |
| ----------- | ----------- | --- | --- |
| Command     | History     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 119

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy running-config {startup-config | checkpoint <CHECKPOINT-
NAME>}
copy running-config {startup-config | checkpoint <CHECKPOINT-NAME>}
Description
Copiestherunningconfigurationtothestartupconfigurationortoanewcheckpoint.Ifthestartup
configurationisalreadypresent,thecommandoverwritestheexistingstartupconfiguration.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
startup-config Specifiesthatthestartupconfigurationreceivesacopyofthe
runningconfiguration.
checkpoint <CHECKPOINT-NAME> Specifiesthenameofanewcheckpointtoreceiveacopyofthe
runningconfiguration.Thecheckpointnamecanbe
alphanumeric.Itcanalsocontainunderscores(_)anddashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitis
usedforsystem-generatedcheckpoints.
Examples
Copyingtherunningconfigurationtothestartupconfiguration:
| switch# copy | running-config | startup-config |     |
| ------------ | -------------- | -------------- | --- |
Success
Copyingtherunningconfigurationtoanewcheckpointnamedckpt1:
| switch# copy | running-config | checkpoint | ckpt1 |
| ------------ | -------------- | ---------- | ----- |
Success
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
Configurationandfirmwaremanagement |120

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy {running-config |     | | startup-config} |     | <REMOTE-URL> |     |
| -------------------- | --- | ----------------- | --- | ------------ | --- |
copy {running-config | startup-config} <REMOTE-URL> {cli | json} [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationorthestartupconfigurationtoaremotefileineitherCLIorJSON
format.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationiscopiedtoaremotefile.
| <REMOTE-URL> |     |     | Specifiestheremotefileusingthesyntax: |     |     |
| ------------ | --- | --- | ------------------------------------- | --- | --- |
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
| {cli | json}   |     |     | Selectstheremotefileformat:P:CLIorJSON. |     |     |
| -------------- | --- | --- | --------------------------------------- | --- | --- |
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |     |
Examples
CopyingarunningconfigurationtoaremotefileinCLIformat:
| switch# | copy running-config | tftp://192.168.1.10/runcli |     |     | cli |
| ------- | ------------------- | -------------------------- | --- | --- | --- |
######################################################################### 100.0%
Success
CopyingarunningconfigurationtoaremotefileinJSONformat:
| switch# | copy running-config | tftp://192.168.1.10/runjson |     |     | json |
| ------- | ------------------- | --------------------------- | --- | --- | ---- |
######################################################################### 100.0%
Success
CopyingastartupconfigurationtoaremotefileinCLIformat:
switch# copy startup-config sftp://root@192.168.1.10/startcli cli
| root@192.168.1.10's |                  | password:         |     |     |     |
| ------------------- | ---------------- | ----------------- | --- | --- | --- |
| sftp> put           | /tmp/startcli    | startcli          |     |     |     |
| Uploading           | /tmp/startcli    | to /root/startcli |     |     |     |
| Connected           | to 192.168.1.10. |                   |     |     |     |
Success
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 121

CopyingastartupconfigurationtoaremotefileinJSONformat:
switch# copy startup-config sftp://root@192.168.1.10/startjson json
| root@192.168.1.10's |                  | password:          |     |     |
| ------------------- | ---------------- | ------------------ | --- | --- |
| sftp> put           | /tmp/startjson   | startjson          |     |     |
| Uploading           | /tmp/startjson   | to /root/startjson |     |     |
| Connected           | to 192.168.1.10. |                    |     |     |
Success
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy {running-config |     | | startup-config} |     | <STORAGE-URL> |
| -------------------- | --- | ----------------- | --- | ------------- |
copy {running-config | startup-config} <STORAGE-URL> {cli | json}
Description
CopiestherunningconfigurationorastartupconfigurationtoaUSBdrive.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{running-config | startup-config} Selectstherunningconfigurationorthestartupconfiguration
tobecopiedtotheswitchUSBdrive.
<STORAGE-URL> Specifiesaremotefilewiththefollowingsyntax:usb:/<file>
| {cli | json} |     |     |     |     |
| ------------ | --- | --- | --- | --- |
Selectstheformatoftheremotefile:CLIorJSON.
Usage
TheswitchsupportsJSONandCLIfileformatswhencopyingtherunningorstartingconfigurationtothe
USBdrive.TheUSBdrivemustbeformattedwiththeFATfilesystem.
TheUSBdrivemustbeenabledandmountedwiththefollowingcommands:
switch(config)#
usb
| switch(config)# | end       |     |     |     |
| --------------- | --------- | --- | --- | --- |
| switch#         | usb mount |     |     |     |
Examples
CopyingarunningconfigurationtoafilenamedrunCLIontheUSBdrive:
Configurationandfirmwaremanagement |122

| switch# copy | running-config | usb:/runCLI |     | cli |
| ------------ | -------------- | ----------- | --- | --- |
Success
CopyingastartupconfigurationtoafilenamedstartCLIontheUSBdrive:
| switch# copy | startup-config | usb:/startCLI |     | cli |
| ------------ | -------------- | ------------- | --- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| copy startup-config |                | running-config |     |     |
| ------------------- | -------------- | -------------- | --- | --- |
| copy startup-config | running-config |                |     |     |
Description
Copiesthestartupconfigurationtotherunningconfiguration.
Examples
| switch# copy | startup-config | running-config |     |     |
| ------------ | -------------- | -------------- | --- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy <STORAGE-URL> |     | running-config |     |     |
| ------------------ | --- | -------------- | --- | --- |
copy <STORAGE-URL> {running-config | startup-config | checkpoint <CHECKPOINT-NAME>}
Description
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 123

This command copies a specified configuration from the USB drive to the running configuration, to a
startup configuration, or to a checkpoint.

Parameter

<STORAGE-URL>

running-config

startup-config

checkpoint <CHECKPOINT-NAME>

Description

Specifies the name of a configuration file on the USB drive with
the syntax: usb:/<FILE>

Specifies that the configuration file is copied to the running
configuration. The file must be in CLI, JSON, or checkpoint format
or the copy will fail. the copy will not work.

Specifies that the configuration file is copied to the startup
configuration. The switch stores this configuration between
reboots. The startup configuration is used as the operating
configuration following a reboot of the switch. The file must be in
JSON or checkpoint format or the copy will fail.

Specifies the name of a new checkpoint file to receive a copy of
the configuration. The configuration file on the USB drive must be
in checkpoint format.

NOTE:
Do not start the checkpoint name with CPC because it is
used for system-generated checkpoints.

Usage

This command requires that the USB drive is formatted with the FAT file system and that the file be in
the appropriate format as follows:

n running-config: This option requires the file on the USB drive be in CLI, JSON, or checkpoint format.

n startup-config: This option requires the file on the USB drive be in JSON or checkpoint format.

n checkpoint <checkpoint-name>: This option requires the file on the USB drive be in checkpoint

format.

Examples

Copying the file runCli from the USB drive to the running configuration:

switch# copy usb:/runCli running-config
Configuration may take several minutes to complete according to configuration
file size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Success

Copying the file startUp from the USB drive to the startup configuration:

switch# copy usb:/startUp startup-config
Success

Copying the file testCheck from the USB drive to the abc checkpoint:

Configuration and firmware management | 124

| switch# | copy usb:/testCheck |     | checkpoint | abc |
| ------- | ------------------- | --- | ---------- | --- |
Success
| Command        | History     |         |     |              |
| -------------- | ----------- | ------- | --- | ------------ |
| Release        |             |         |     | Modification |
| 10.07orearlier |             |         |     | --           |
| Command        | Information |         |     |              |
| Platforms      | Command     | context |     | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
erase
erase
| checkpoint | <checkpont-name>      |     |     |     |
| ---------- | --------------------- | --- | --- | --- |
| core-dump  | all|daemon|dsm|kernel |     |     |     |
startup-config
all
Description
Deletesanexistingcheckpoint,startupconfiguration,orcore-dump.
| Parameter  |                   |     |     | Description                                 |
| ---------- | ----------------- | --- | --- | ------------------------------------------- |
| checkpoint | <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint.              |
| core-dump  |                   |     |     | Eraseoneofthefollowingsetsofcore-dumpfiles: |
| all|daemon | <daemon-name>     |     |     |                                             |
|            |                   |     |     | n all:Eraseallcore-dumpfiles.               |
|kernel
|     |     |     |     | n daemon<daemon-name>:Erasedaemoncore-dumpfiles. |
| --- | --- | --- | --- | ------------------------------------------------ |
|     |     |     |     | n kerne:lErasethekernelcore-dump.                |
n
| startup-config |     |     |     | Specifiesthestartupconfiguration. |
| -------------- | --- | --- | --- | --------------------------------- |
| all            |     |     |     | Specifiesallcheckpoints.          |
Examples
Erasingcheckpointckpt1:
| switch# | erase checkpoint |     | ckpt1 |     |
| ------- | ---------------- | --- | ----- | --- |
Erasingthestartupconfiguration:
switch#
erase startup-config
Erasingallcheckpoints:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 125

| switch#        | erase checkpoint | all     |              |
| -------------- | ---------------- | ------- | ------------ |
| Command        | History          |         |              |
| Release        |                  |         | Modification |
| 10.07orearlier |                  |         | --           |
| Command        | Information      |         |              |
| Platforms      | Command          | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |                   | <CHECKPOINT-NAME> |        |
| --------------- | ----------------- | ----------------- | ------ |
| show checkpoint | <CHECKPOINT-NAME> |                   | [json] |
Description
Showstheconfigurationofacheckpoint.
| Parameter         |     |     | Description                                    |
| ----------------- | --- | --- | ---------------------------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint.                 |
| [json]            |     |     | SpecifiesthattheoutputisdisplayedinJSONformat. |
Examples
Showingtheconfigurationoftheckpt1checkpointinCLIformat:
| switch#    | show checkpoint | ckpt1 |     |
| ---------- | --------------- | ----- | --- |
| Checkpoint | configuration:  |       |     |
!
| !Version             | AOS-CX PL.10.07.0000K-75-g55e5193 |       |                     |
| -------------------- | --------------------------------- | ----- | ------------------- |
| !export-password:    | default                           |       |                     |
| lacp system-priority |                                   | 65535 |                     |
| user admin           | group administrators              |       | password ciphertext |
AQBapQjwipebv36io0jFfde7ZzrHckncal1D+3n8XFTZKQdmYgAAADEtYOeHSme93xzdD0uz6Vr9Kl+XBz
B+2GB0UBxSF7rvgN2x8KSgkqv7iqXVQ0Te6LkSMnH4BdNaT3Bf25qyvOqmr4YakO1V3rg8zAOADkPktQD8
joTHXflzwomoIzcmv/uX
cli-session
timeout 0
!
!
!
!
| ssh server | vrf default |     |     |
| ---------- | ----------- | --- | --- |
| vlan 1     |             |     |     |
spanning-tree
| interface | lag 1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
vlan access 1
Configurationandfirmwaremanagement |126

interface lag 128

no shutdown
vlan access 1
interface lag 129
shutdown
vlan access 1
lacp mode active

interface 1/1/1
no shutdown
lag 128
lacp port-id 65535

interface 1/1/2
no shutdown
vlan access 1

interface 1/1/3
no shutdown
vlan access 1

interface 1/1/4
no shutdown
vlan access 1

interface 1/1/5
no shutdown
vlan access 1

interface 1/1/6
no shutdown
vlan access 1

interface 1/1/7
no shutdown
vlan access 1

interface 1/1/8
no shutdown
vlan access 1

interface 1/1/9
no shutdown
vlan access 1

interface 1/1/10

no shutdown
vlan access 1

interface 1/1/11

no shutdown
vlan access 1

interface 1/1/12

no shutdown
vlan access 1

interface 1/1/13

no shutdown
vlan access 1

interface 1/1/14

no shutdown
vlan access 1

interface 1/1/15

no shutdown
vlan access 1

interface 1/1/16

no shutdown
vlan access 1

interface vlan 1
ip dhcp

snmp-server vrf default
!
!
!

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

127

!
!
| https-server | vrf | default |     |     |
| ------------ | --- | ------- | --- | --- |
Showingtheconfigurationoftheckpt1checkpointinJSONformat:
| switch# show | checkpoint     | ckpt1 | json |     |
| ------------ | -------------- | ----- | ---- | --- |
| Checkpoint   | configuration: |       |      |     |
{
"AAA_Server_Group": {
"local": {
|     | "group_name": | "local" |     |     |
| --- | ------------- | ------- | --- | --- |
},
"none": {
|     | "group_name": | "none" |     |     |
| --- | ------------- | ------ | --- | --- |
}
},
...
...
...
...
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |                   | <CHECKPOINT-NAME> |           | hash    |
| --------------- | ----------------- | ----------------- | --------- | ------- |
| show checkpoint | <CHECKPOINT-NAME> |                   | hash [cli | | json] |
Description
ShowsaconfigurationcheckpointhashcalculatedwiththeSHA-256algorithm.Whentheoutputformat
isnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<CHECKPOINT-NAME>
Specifiesanexistingcheckpointname.
| [cli | json] |     |     | SelectseithertheCLIorJSONformat. |     |
| ------------ | --- | --- | -------------------------------- | --- |
Examples
ShowingacheckpointSHA-256hashinJSONformat:
Configurationandfirmwaremanagement |128

| switch#     | show checkpoint | ckpt1     | hash json |
| ----------- | --------------- | --------- | --------- |
| Calculating | the hash:       | [Success] |           |
The SHA-256 hash of the checkpoint in JSON format, created in image XX.10.08.xxxx:
cc7a57a9bbb4e6600d3b4180296a35f6af9e797ce9c439955dfe5de58b06da9e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version, | etc.).      |         |                   |
| ----------- | ----------- | ------- | ----------------- |
| Command     | History     |         |                   |
| Release     |             |         | Modification      |
| 10.08       |             |         | Commandintroduced |
| Command     | Information |         |                   |
| Platforms   | Command     | context | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |                    | post-configuration |     |
| --------------- | ------------------ | ------------------ | --- |
| show checkpoint | post-configuration |                    |     |
Description
Showstheconfigurationsettingsforcreatingsystemcheckpoints.
Examples
| switch#    | show checkpoint    | post-configuration |         |
| ---------- | ------------------ | ------------------ | ------- |
| Checkpoint | Post-Configuration |                    | feature |
-------------------------------------
| Status         |             | : enabled |              |
| -------------- | ----------- | --------- | ------------ |
| Timeout        | (sec) : 300 |           |              |
| Command        | History     |           |              |
| Release        |             |           | Modification |
| 10.07orearlier |             |           | --           |
| Command        | Information |           |              |
| Platforms      | Command     | context   | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 129

show checkpoint
show checkpoint
Description
Showsadetailedlistofallsavedcheckpoints.
Examples
Showingadetailedlistofallsavedcheckpoints:
| switch# show    | checkpoint |     |                           |               |                        |
| --------------- | ---------- | --- | ------------------------- | ------------- | ---------------------- |
| NAME            | TYPE       |     | WRITER DATE(YYYY/MM/DD)   | IMAGE         | VERSION                |
| ckpt1           | checkpoint |     | User 2017-02-23T00:10:02Z | XX.01.01.000X |                        |
| ckpt2           | checkpoint |     | User 2017-03-08T18:10:01Z | XX.01.01.000X |                        |
| ckpt3           | checkpoint |     | User 2017-03-09T23:11:02Z | XX.01.01.000X |                        |
| ckpt4           | checkpoint |     | User 2017-03-11T00:00:03Z | XX.01.01.000X |                        |
| ckpt5           | latest     |     | User 2017-03-14T01:12:27Z | XX.01.01.000X |                        |
| Command History |            |     |                           |               |                        |
| Release         |            |     | Modification              |               |                        |
| 10.08           |            |     | Commandsyntaxshow         | checkpoint    | list allisreplacedwith |
show checkpoint.
| 10.07orearlier      |         |         | --        |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Command Information |         |         |           |     |     |
| Platforms           | Command | context | Authority |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |                   | date |            |     |     |
| --------------- | ----------------- | ---- | ---------- | --- | --- |
| show checkpoint | date <START-DATE> |      | <END-DATE> |     |     |
Description
Showsdetailedlistofallsavedcheckpointscreatedwithinthespecifieddaterange.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
<END-DATE> Specifiestheendingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Examples
Showingadetailedlistofsavedcheckpointsforaspecificdaterange:
Configurationandfirmwaremanagement |130

| switch# show    | checkpoint |            | date | 2017-03-08   | 2017-03-12           |     |               |         |     |
| --------------- | ---------- | ---------- | ---- | ------------ | -------------------- | --- | ------------- | ------- | --- |
| NAME            |            | TYPE       |      | WRITER       | DATE(YYYY/MM/DD)     |     | IMAGE         | VERSION |     |
| ckpt2           |            | checkpoint |      | User         | 2017-03-08T18:10:01Z |     | XX.01.01.000X |         |     |
| ckpt3           |            | checkpoint |      | User         | 2017-03-09T23:11:02Z |     | XX.01.01.000X |         |     |
| ckpt4           |            | checkpoint |      | User         | 2017-03-11T00:00:03Z |     | XX.01.01.000X |         |     |
| Command History |            |            |      |              |                      |     |               |         |     |
| Release         |            |            |      | Modification |                      |     |               |         |     |
10.08
|                     |         |         |     | Commandsyntaxshow |                              | checkpoint | list | date       | <START- |
| ------------------- | ------- | ------- | --- | ----------------- | ---------------------------- | ---------- | ---- | ---------- | ------- |
|                     |         |         |     | DATE>             | <END-DATE>isreplacedwithshow |            |      | checkpoint | date    |
|                     |         |         |     | <START-DATE>      | <END-DATE>                   |            |      |            |         |
| 10.07orearlier      |         |         |     | --                |                              |            |      |            |         |
| Command Information |         |         |     |                   |                              |            |      |            |         |
| Platforms           | Command | context |     | Authority         |                              |            |      |            |         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show running-config |     |           | hash |       |     |     |     |     |     |
| ------------------- | --- | --------- | ---- | ----- | --- | --- | --- | --- | --- |
| show running-config |     | hash [cli | |    | json] |     |     |     |     |     |
Description
Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutput
formatisnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description                      |     |     |     |     |     |
| ------------ | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| [cli | json] |     |     |     | SelectseithertheCLIorJSONformat. |     |     |     |     |     |
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
| switch# show | running-config |           | hash | cli         |     |     |     |     |     |
| ------------ | -------------- | --------- | ---- | ----------- | --- | --- | --- | --- | --- |
| Calculating  | the hash:      | [Success] |      |             |     |     |     |     |     |
| SHA-256 hash | of the         | config    | in   | CLI format: |     |     |     |     |     |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,     | etc.). |     |     |     |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Command History |        |     |     |     |     |     |     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 131

| Release             |         |         |     | Modification      |
| ------------------- | ------- | ------- | --- | ----------------- |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show startup-config |      | hash |         |     |
| ------------------- | ---- | ---- | ------- | --- |
| show startup-config | hash | [cli | | json] |     |
Description
Showsthestartup-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutput
formatisnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description |
| ------------ | --- | --- | --- | ----------- |
| [cli | json] |     |     |     |             |
SelectseithertheCLIorJSONformat.
Examples
Showingthestartup-configcheckpointSHA-256hashinCLIformat:
| switch# show | startup-config |           | hash   | cli     |
| ------------ | -------------- | --------- | ------ | ------- |
| Calculating  | the hash:      | [Success] |        |         |
| SHA-256 hash | of the         | config    | in CLI | format: |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,         | etc.).  |         |     |                   |
| ------------------- | ------- | ------- | --- | ----------------- |
| Command History     |         |         |     |                   |
| Release             |         |         |     | Modification      |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Configurationandfirmwaremanagement |132

write memory
write memory
Description
Savestherunningconfigurationtothestartupconfiguration.Itisanaliasofthecommand copy
running-config startup-config.Ifthestartupconfigurationisalreadypresent,thiscommand
overwritesthestartupconfiguration.
Examples
| switch# write | memory |     |     |
| ------------- | ------ | --- | --- |
Success
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Boot commands
boot fabric-module
| boot fabric-module | <SLOT-ID> |     |     |
| ------------------ | --------- | --- | --- |
Description
Rebootsthespecifiedfabricmodule.
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <SLOT-ID> |     |     | Specifiesthememberandslotofthemoduleintheformat |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Theboot fabric-modulecommandrebootsthespecifiedfabricmodule.Trafficperformanceisaffected
whilethemoduleisdown.
Ifthespecifiedmoduleistheonlyfabricmoduleinanupstate,rebootingthatmodulestopstraffic
switchingbetweenlinemodulesandthelinemodulespowerdown.Thelinemodulespowerupwhen
onefabricmodulereturnstoanupstate.
Thiscommandisvalidforfabricmodulesonly.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 133

Examples
Rebootingthefabricmoduleinslot1/3whenauto-confirmisnotenabled:
switch#
| boot | fabric-module | 1/3 |     |
| ---- | ------------- | --- | --- |
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
| stop traffic | switching   | between | line modules. |
| ------------ | ----------- | ------- | ------------- |
| Do you want  | to continue | (y/n)?  | y             |
switch#
Rebootingthefabricmoduleinslot1/1whenauto-confirmisenabled:
| switch# boot | fabric-module | 1/3 |     |
| ------------ | ------------- | --- | --- |
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
| stop traffic | switching   | between | line modules.  |
| ------------ | ----------- | ------- | -------------- |
| Do you want  | to continue | (y/n) y | (auto-confirm) |
switch#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
boot line-module
| boot line-module | <SLOT-ID> |     |     |
| ---------------- | --------- | --- | --- |
Description
Rebootsthespecifiedlinemodule.
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <SLOT-ID> |     |     | Specifiesthememberandslotofthemoduleintheformat |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Rebootsthespecifiedlinemodule.Anytrafficfortheswitchpassingthroughtheaffectedmodule(SSH,
TELNET,andSNMP)isinterrupted.Itcantakeupto2minutestorebootthemodule.Duringthattime,
youcanmonitorprogressbyviewingtheeventlog.
Thiscommandisvalidforlinemodulesonly.
Configurationandfirmwaremanagement |134

Examples
Reloadingthemoduleinslot1/1:
switch#
| boot | line-module |     |     | 1/1 |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- |
This command will reboot the specified line module and interfaces on this
module will not send or receive packets while the module is down. Any
traffic passing through the line module will be interrupted. Management
sessions connected through the line module will be affected. It might take
up to 2 minutes to complete rebooting the module. During that time, you can
| monitor progress |     | by       | viewing | the | event | log. |
| ---------------- | --- | -------- | ------- | --- | ----- | ---- |
| Do you want      | to  | continue | (y/n)?  |     | y     |      |
switch#
| Command History     |         |     |         |     |              |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| Release             |         |     |         |     | Modification |     |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
boot management-module
| boot management-module |     |     | {active | | standby |     | | <SLOT-ID>} |
| ---------------------- | --- | --- | ------- | --------- | --- | ------------ |
Description
Rebootsthespecifiedmanagementmodule.Choosethemanagementmoduletorebootbyrole(active
orstandby)orbyslotnumber.
| Parameter |     |     |     |     | Description                        |     |
| --------- | --- | --- | --- | --- | ---------------------------------- | --- |
| active    |     |     |     |     | Selectstheactivemanagementmodule.  |     |
| standby   |     |     |     |     | Selectsthestandbymanagementmodule. |     |
<SLOT-ID> Specifiesthememberandslotofthemanagementmoduleinthe
formatmember/slot.Forexample,tospecifythemodulein
member1slot5,enter1/5.
Usage
Thiscommandrebootsasinglemanagementmoduleinachassis.Choosethemanagementmoduleto
rebootbyrole(activeorstandby)orbyslotnumber.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisavailable,the
activemanagementmodulerebootsandthestandbymanagementmodulebecomestheactive
managementmodule.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 135

Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisnotavailable,
youarewarned,youarepromptedtosavetheconfiguration,andyouarepromptedtoconfirmthe
operation.
Ifyourebootthestandbymanagementmodule,thestandbymanagementmodulerebootsandremains
thestandbymanagementmodule.
Ifyouattempttorebootamanagementmodulethatisnotavailable,thebootcommandisaborted.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,thebootcommandisaborted.
HewlettPackardEnterpriserecommendsthatyouusetheboot management-modulecommandinsteadof
pressingthemoduleresetbuttontorebootamanagementmodulebecauseifyouarerebootingtheonly
availablemanagementmodule,theboot management-modulecommandenablesyoutosavethe
configuration,cancelthereboot,orboth.
Examples
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisavailable:
| switch# | boot | management-module |     | active |     |     |     |
| ------- | ---- | ----------------- | --- | ------ | --- | --- | --- |
The management-module in slot 1/5 is going down for reboot now.
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisnotavailable:
| switch#        | boot        | management-module |              | 1/5     |               |                |     |
| -------------- | ----------- | ----------------- | ------------ | ------- | ------------- | -------------- | --- |
| The management |             | module            | in slot      | 1/5     | is currently  | active and     | no  |
| standby        | management  |                   | module was   | found.  |               |                |     |
| This will      | reboot      | the               | entire       | switch. |               |                |     |
| Do you         | want        | to save           | the current  |         | configuration | (y/n)? n       |     |
| This will      | reboot      | the               | entire       | switch  | and render    | it unavailable |     |
| until the      | process     |                   | is complete. |         |               |                |     |
| Continue       | (y/n)?      | y                 |              |         |               |                |     |
| The system     | is          | going             | down for     | reboot. |               |                |     |
| Command        | History     |                   |              |         |               |                |     |
| Release        |             |                   |              |         | Modification  |                |     |
| 10.07orearlier |             |                   |              |         | --            |                |     |
| Command        | Information |                   |              |         |               |                |     |
| Platforms      |             | Command           | context      |         | Authority     |                |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
boot set-default
| boot set-default |     | {primary | | secondary} |     |     |     |     |
| ---------------- | --- | -------- | ------------ | --- | --- | --- | --- |
Configurationandfirmwaremanagement |136

Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     |     | Description                                     |
| --------- | --- | --- | --- | ----------------------------------------------- |
| primary   |     |     |     | Selectstheprimarynetworkoperatingsystemimage.   |
| secondary |     |     |     | Selectsthesecondarynetworkoperatingsystemimage. |
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch#        | boot set-default |     | primary     |              |
| -------------- | ---------------- | --- | ----------- | ------------ |
| Default        | boot image       | set | to primary. |              |
| Command        | History          |     |             |              |
| Release        |                  |     |             | Modification |
| 10.07orearlier |                  |     |             | --           |
| Command        | Information      |     |             |              |
| Platforms      | Command          |     | context     | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
boot system
| boot system | [primary | | secondary | |   | serviceos] |
| ----------- | -------- | ----------- | --- | ---------- |
Description
Rebootsallmodulesontheswitch.Bydefault,theconfigureddefaultoperatingsystemimageisused.
Optionalparametersenableyoutospecifywhichsystemimagetousefortherebootoperationandfor
futurerebootoperations.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
primary Selectstheprimaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetoprimary
forfuturereboots.
secondary Selectsthesecondaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetosecondary
forfuturereboots.
serviceos Selectstheserviceoperatingsystemforthisreboot.Doesnot
changetheconfigureddefaultoperatingsystemimage.The
serviceoperatingsystemactsasastandalonebootloaderand
recoveryOSforswitchesrunningtheAOS-CXoperatingsystem
andisusedinrarecaseswhentroubleshootingaswitch.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 137

Usage
Thiscommandrebootstheentiresystem.Ifyoudonotselectoneoftheoptionalparameters,the
systemrebootsfromtheconfigureddefaultbootimage.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Choosingoneoftheoptionalparametersaffectsthesettingforthedefaultbootimage:
n Ifyouselecttheprimaryorsecondaryoptionalparameter,thatimagebecomestheconfigured
defaultbootimageforfuturesystemreboots.Thecommandfailsiftheswitchisnotabletosetthe
operatingsystemimagetotheimageyouselected.
Youcanusetheboot set-defaultcommandtochangetheconfigureddefaultoperatingsystemimage.
n Ifyouselectserviceosastheoptionalparameter,theconfigureddefaultbootimageremainsthe
same,andthesystemrebootsallmanagementmoduleswiththeserviceoperatingsystem.
Iftheconfigurationoftheswitchhaschangedsincethelastreboot,whenyouexecutetheboot system
commandyouarepromptedtosavetheconfigurationandyouarepromptedtoconfirmthereboot
operation.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,theboot systemcommandisaborted.
Examples
Rebootingthesystemfromtheconfigureddefaultoperatingsystemimage:
| switch# | boot system  |             |               |          |
| ------- | ------------ | ----------- | ------------- | -------- |
| Do you  | want to save | the current | configuration | (y/n)? y |
The running configuration was saved to the startup configuration.
| This will  | reboot the | entire switch    | and render | it unavailable |
| ---------- | ---------- | ---------------- | ---------- | -------------- |
| until the  | process    | is complete.     |            |                |
| Continue   | (y/n)? y   |                  |            |                |
| The system | is going   | down for reboot. |            |                |
Rebootingthesystemfromthesecondaryoperatingsystemimage,settingthesecondaryoperating
systemimageastheconfigureddefaultbootimage:
| switch#    | boot system  | secondary         |               |                |
| ---------- | ------------ | ----------------- | ------------- | -------------- |
| Default    | boot image   | set to secondary. |               |                |
| Do you     | want to save | the current       | configuration | (y/n)? n       |
| This will  | reboot the   | entire switch     | and render    | it unavailable |
| until the  | process      | is complete.      |               |                |
| Continue   | (y/n)? y     |                   |               |                |
| The system | is going     | down for reboot.  |               |                |
Cancelingasystemreboot:
| switch#   | boot system  |               |               |                |
| --------- | ------------ | ------------- | ------------- | -------------- |
| Do you    | want to save | the current   | configuration | (y/n)? n       |
| This will | reboot the   | entire switch | and render    | it unavailable |
Configurationandfirmwaremanagement |138

| until the | process | is complete. |     |
| --------- | ------- | ------------ | --- |
| Continue  | (y/n)?  |              |     |
n
| Reboot | aborted. |     |     |
| ------ | -------- | --- | --- |
switch#
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show boot-history |       |     |     |
| ----------------- | ----- | --- | --- |
| show boot-history | [all] |     |     |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationabout
thebootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.When
theallparameterisspecified,showsthebootinformationfortheactivemanagementmoduleandall
availablelinemodules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandby
console.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| all       |     |     | Showsbootinformationfortheactivemanagementmoduleand |
allavailablelinemodules.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | up for | <SECONDS> seconds |     |
| ------------- | ------ | ----------------- | --- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
| Timestamp | boot reason |     |     |
| --------- | ----------- | --- | --- |
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperationoccurred
andthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |     |
| ------------- | ----- | --- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernel crash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
| Reboot requested | through | database |     |
| ---------------- | ------- | -------- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 139

TherebootoccurredbecauseofarequestmadethroughtheCLIorotherAPI.
| Uncontrolled | reboot |     |     |
| ------------ | ------ | --- | --- |
Thereasonfortherebootisnotknown.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index : | 3                                  |                    |                  |
| ------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |                    |                  |
| Current | Boot, up for                       | 22 hrs 12          | mins 22 secs     |
| Index : | 2                                  |                    |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot requested | through database |
| Index : | 1                                  |                    |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |                    |                  |
| 07 Aug  | 18 14:08:46                        | : Reboot requested | through database |
| Index : | 0                                  |                    |                  |
| Boot ID | : 23da2b0e26d048d7b3f4b6721b69c110 |                    |                  |
| 07 Aug  | 18 13:00:46                        | : Reboot requested | through database |
switch#
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
| switch#    | show boot-history | all |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index :     | 3                                  |                    |                  |
| ----------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |                    |                  |
| Current     | Boot, up for                       | 22 hrs 12          | mins 22 secs     |
| Index :     | 2                                  |                    |                  |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| 07 Aug      | 18 16:28:01                        | : Reboot requested | through database |
| Index :     | 1                                  |                    |                  |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |                    |                  |
| 07 Aug      | 18 14:08:46                        | : Reboot requested | through database |
| Index :     | 0                                  |                    |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |                    |                  |
| 07 Aug      | 18 13:00:46                        | : Reboot requested | through database |
| Line module | 1/1                                |                    |                  |
=================
| Index : | 3           |              |         |
| ------- | ----------- | ------------ | ------- |
| 10 Aug  | 17 12:45:46 | : dune_agent | crashed |
...
| Command | History |     |     |
| ------- | ------- | --- | --- |
Configurationandfirmwaremanagement |140

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| Firmware      | management   |              | commands         |
| ------------- | ------------ | ------------ | ---------------- |
| copy {primary | | secondary} |              | <REMOTE-URL>     |
| copy {primary | | secondary} | <REMOTE-URL> | [vrf <VRF-NAME>] |
Description
UploadsafirmwareimagetoaTFTPorSFTPserver.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{primary | secondary} Selectstheprimaryorsecondaryimageprofiletoupload.
Required
<REMOTE-URL> SpecifiestheURLtoreceivetheuploadedfirmwareusingSFTP,
TFTPorSCP.
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname.Default:default. |
| -------------- | --- | --- | ---------------------------------- |
Examples
TFTPupload:
| switch# | copy primary | tftp://192.0.2.0/00_10_00_0002.swi |     |
| ------- | ------------ | ---------------------------------- | --- |
######################################################################### 100.0%
| Verifying | and writing | system | firmware... |
| --------- | ----------- | ------ | ----------- |
SFTPupload:
| switch#            | copy primary  | sftp://swuser@192.0.2.0/00_10_00_0002.swi |     |
| ------------------ | ------------- | ----------------------------------------- | --- |
| swuser@192.0.2.0's |               | password:                                 |     |
| Connected          | to 192.0.2.0. |                                           |     |
| sftp> put          | primary.swi   | XL_10_00_0002.swi                         |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 141

| Uploading      | primary.swi | to /users/swuser/00_10_00_0002.swi |              |          |       |
| -------------- | ----------- | ---------------------------------- | ------------ | -------- | ----- |
| primary.swi    |             |                                    | 100% 179MB   | 35.8MB/s | 00:05 |
| Command        | History     |                                    |              |          |       |
| Release        |             |                                    | Modification |          |       |
| 10.07orearlier |             |                                    | --           |          |       |
| Command        | Information |                                    |              |          |       |
| Platforms      | Command     | context                            | Authority    |          |       |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy {primary | | secondary} |                     | <FIRMWARE-FILENAME> |     |     |
| ------------- | ------------ | ------------------- | ------------------- | --- | --- |
| copy {primary | | secondary} | <FIRMWARE-FILENAME> |                     |     |     |
Description
CopiesafirmwareimagetoUSBstorage.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{primary | secondary} Selectstheprimaryorsecondaryimagefromwhichtocopythe
firmware.Required
<FIRMWARE-FILENAME> SpecifiesthenameofthefirmwarefiletocreateontheUSB
storagedevice.Prefixthefilenamewithusb:/.Forexample:
usb:/firmware_v1.2.3.swi
Forinformationonhowtoformatthepathtoafirmwarefileona
USBdrive,seeUSBURL.
Examples
| switch#        | copy primary | usb:/11.10.00.0002.swi |              |     |     |
| -------------- | ------------ | ---------------------- | ------------ | --- | --- |
| Command        | History      |                        |              |     |     |
| Release        |              |                        | Modification |     |     |
| 10.07orearlier |              |                        | --           |     |     |
| Command        | Information  |                        |              |     |     |
| Platforms      | Command      | context                | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Configurationandfirmwaremanagement |142

| copy primary | secondary |     |     |
| ------------ | --------- | --- | --- |
| copy primary | secondary |     |     |
Description
Copiesthefirmwareimagefromtheprimarytothesecondarylocation.
Examples
| switch#        | copy primary | secondary          |              |
| -------------- | ------------ | ------------------ | ------------ |
| The secondary  | image        | will be deleted.   |              |
| Continue       | (y/n)? y     |                    |              |
| Verifying      | and writing  | system firmware... |              |
| Command        | History      |                    |              |
| Release        |              |                    | Modification |
| 10.07orearlier |              |                    | --           |
| Command        | Information  |                    |              |
| Platforms      | Command      | context            | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <REMOTE-URL>
copy <REMOTE-URL> {hot-patch|primary|secondary} [vrf <VRF-NAME>]
Description
DownloadsafirmwareimagefromaTFTPorSFTPserver.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<REMOTE-URL> SpecifiestheURLfromwhichtodownloadthefirmwareusing
SFTPorTFTP.
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
{hot-patch|primary|secondary}
Selectaprimaryorsecondaryimageprofileforreceivingthe
downloadedfirmware.Required.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |
| -------------- | --- | --- | --------------------------------------- |
TFTP usage
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 143

To specify a URL with:

n an IPv4 address: tftp://192.0.2.1/a.txt

n an IPv6 address: tftp://[2000::2]/a.txt

n a hostname: tftp://hpe.com/a.txt

To specify TFTP with:

n the port number of the server in the URL: tftp://192.0.2.1:12/a.txt

n the blocksize in the URL: tftp://192.0.2.1;blocksize=1462/a.txt

The valid blocksize range is 8 to 65464.

n the port number of the server and blocksize in the URL:

tftp://192.0.2.1:12;blocksize=1462/a.txt

To specify a file in a directory of URL: tftp://192.0.2.1/dir/a.txt

SFTP usage

To specify:

n A URL with an IPv4 address: sftp://user@192.0.2.1/a.txt

n A URL with an IPv6 address: sftp://user@[2000::2]/a.txt

n A URL with a hostname: sftp://user@hpe.com/a.txt

n SFTP port number of a server in the URL: sftp://user@192.0.2.1:12/a.txt

n A file in a directory of URL: sftp://user@192.0.2.1/dir/a.txt

n To specify a file with absolute path in the URL: sftp://user@192.0.2.1//home/user/a.txt

SCP Usage

To specify:

n A username with an IP address: scp://user@192.0.2.1:12/a.txt

n A username with a remote host:scp://user@hpe.com/a.txt

Examples

TFTP download for primary software image:

switch#
The primary image will be deleted.

copy tftp://192.10.12.0/ss.10.a0.0001.swi primary

Continue (y/n)? y
######################################################################### 100.0%
Verifying and writing system firmware...

SFTP download:

switch# copy sftp://swuser@192.10.12.0/ss.10.00.0002.swi primary
The primary image will be deleted.

Continue (y/n)? y
The authenticity of host '192.10.12.0 (192.10.12.0)' can't be established.
ECDSA key fingerprint is SHA256:L64khLwlyLgXlARKRMiwcAAK8oRaQ8C0oWP+PkGBXHY.
Are you sure you want to continue connecting (yes/no)? yes

Configuration and firmware management | 144

Warning: Permanently added '192.10.12.0' (ECDSA) to the list of known hosts.
| swuser@192.10.12.0's |                 | password: |     |     |     |     |     |
| -------------------- | --------------- | --------- | --- | --- | --- | --- | --- |
| Connected            | to 192.10.12.0. |           |     |     |     |     |     |
Fetching /users/swuser/ss.10.00.0002.swi to ss.10.00.0002.swi.dnld
| /users/swuser/ss.10.00.0002.swi |             |         |              | 100% | 179MB | 25.6MB/s | 00:07 |
| ------------------------------- | ----------- | ------- | ------------ | ---- | ----- | -------- | ----- |
| Verifying                       | and writing | system  | firmware...  |      |       |          |       |
| Command                         | History     |         |              |      |       |          |       |
| Release                         |             |         | Modification |      |       |          |       |
| 10.07orearlier                  |             |         | --           |      |       |          |       |
| Command                         | Information |         |              |      |       |          |       |
| Platforms                       | Command     | context | Authority    |      |       |          |       |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| copy secondary | primary |     |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- | --- |
| copy secondary | primary |     |     |     |     |     |     |
Description
Copiesthefirmwareimagefromthesecondarytotheprimarylocation.
Examples
| switch#     | copy secondary | primary     |             |     |     |     |     |
| ----------- | -------------- | ----------- | ----------- | --- | --- | --- | --- |
| The primary | image will     | be deleted. |             |     |     |     |     |
| Continue    | (y/n)? y       |             |             |     |     |     |     |
| Verifying   | and writing    | system      | firmware... |     |     |     |     |
switch# copy sftp://stor@192.22.1.0/im-switch.swi primary vrf mgmt
| The primary | image will | be deleted. |     |     |     |     |     |
| ----------- | ---------- | ----------- | --- | --- | --- | --- | --- |
| Continue    | (y/n)? y   |             |     |     |     |     |     |
The authenticity of host '192.22.1.0 (192.22.1.0)' can't be established.
ECDSA key fingerprint is SHA256:MyI1xbdKnehYut0NLfL69gDpNzCmZqBVvBaRR46m7o8.
| Are you | sure you want | to continue | connecting | (yes/no)? | yes |     |     |
| ------- | ------------- | ----------- | ---------- | --------- | --- | --- | --- |
Warning: Permanently added '192.22.1.0' (ECDSA) to the list of known hosts.
| stor@192.22.1.0's      | password:              |        |                              |                |     |       |     |
| ---------------------- | ---------------------- | ------ | ---------------------------- | -------------- | --- | ----- | --- |
| Connected              | to 192.22.1.0.         |        |                              |                |     |       |     |
| sftp> get              | c8d5b9f-topflite.swi   |        | c8d5b9f-topflite.swi.dnld    |                |     |       |     |
| Fetching               | /home/dr/im-switch.swi |        | to c8d5b9f-topflite.swi.dnld |                |     |       |     |
| /home/dr/im-switch.swi |                        |        | 100%                         | 226MB 56.6MB/s |     | 00:04 |     |
| Verifying              | and writing            | system | firmware...                  |                |     |       |     |
| Command                | History                |        |                              |                |     |       |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 145

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <STORAGE-URL>
| copy <STORAGE-URL> | {primary|secondary} |     |     |
| ------------------ | ------------------- | --- | --- |
Description
Copies,verifies,andinstallsafirmwareimagefromaUSBstoragedeviceconnectedtotheactive
managementmodule.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<STORAGE-URL> Specifiesthenameofthefirmwarefiletocopyfromthestorage
device.Required.
USBformat:
usb:/<FILENAME>
{primary|secondary} Selectaprimaryorsecondaryprofileforreceivingthecopied
firmware.
USB usage
Tospecifyafile:
InaUSBstoragedevice:usb:/a.txt
n
n InadirectoryofaUSBstoragedevice:usb:/dir/a.txt
Examples
| switch#        | copy usb:/11.10.00.0002.swi |                    | primary      |
| -------------- | --------------------------- | ------------------ | ------------ |
| The primary    | image will                  | be deleted.        |              |
| Continue       | (y/n)? y                    |                    |              |
| Verifying      | and writing                 | system firmware... |              |
| Command        | History                     |                    |              |
| Release        |                             |                    | Modification |
| 10.07orearlier |                             |                    | --           |
| Command        | Information                 |                    |              |
Configurationandfirmwaremanagement |146

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

147

Chapter 8

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing and modifying information
about managed devices on IP networks.

Configuring SNMP

(The SNMP agent provides read-only access.)

Procedure

1. Enable SNMP on a VRF using the command snmp-server vrf.

2. Set the system contact, location, and description for the switch with the following commands:

n snmp-server system-contact

n snmp-server system-location

n snmp-server system-description

3.

If required, change the default SNMP port on which the agent listens for requests with the
command snmp-server agent-port.

4. By default, the agent uses the community string public to protect access through SNMPv1/v2c.

Set a new community string with the command snmp-server community.

5. Configure the trap receivers to which the SNMP agent will send trap notifications with the

command snmp-server host.

6. Create an SNMPv3 context and associate it with any available SNMPv3 user to perform context

specific v3 MIB polling using the command snmpv3 user .

7. Create an SNMPv3 context and associate it with an available SNMPv1/v2c community string to

perform context specific v1/v2c MIB polling using the command snmpv3 context.

8. Review your SNMP configuration settings with the following commands:

n show snmp agent-port

n show snmp community

n show snmp system

n show snmpv3 context

n show snmp trap

n show snmp vrf

n show snmpv3 users

n show tech snmp

Example 1

This example creates the following configuration:

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

148

n EnablesSNMPontheout-of-bandmanagementinterface(VRFmgmt).
n Setsthecontact,location,anddescriptionfortheswitchto:JaniceM,Building2,LabSwitch.
SetsthecommunitystringtoLab8899X.
n
| switch(config)# | snmp-server | vrf mgmt           |          |           |
| --------------- | ----------- | ------------------ | -------- | --------- |
| switch(config)# | snmp-server | system-contact     | JaniceM  |           |
| switch(config)# | snmp-server | system-location    |          | Building2 |
| switch(config)# | snmp-server | system-description |          | LabSwitch |
| switch(config)# | snmp-server | community          | Lab8899X |           |
Example 2
Thisexamplecreatesthefollowingconfiguration:
n CreatesanSNMPv3usernamedAdminusingshaauthenticationwiththeplaintextpassword
mypasswordandusingdessecuritywiththeplaintextpasswordmyprivpass.
n AssociatestheSNMPv3userAdminwithacontextnamednewContext.
switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
| priv-pass       | plaintext | myprivpass         |            |     |
| --------------- | --------- | ------------------ | ---------- | --- |
| switch(config)# | snmpv3    | user Admin context | newContext |     |
RefertotheSNMP GuideforSNMP Commands.
SNMP|149

Chapter 9

Port filtering

Port filtering

Port filtering is a feature in which packets that are ingressed through a source port can be blocked for
egressing on a specific set of ports.

Figure 1 Port Filter Application

;" />

Port filtering commands

portfilter
portfilter <INTERFACE-LIST>
no portfilter [<INTERFACE-LIST>]

Description

Configures the specified ports so they do not egress any packets that were received on the source port
specified in interface context.

The no form of this command removes the port filter setting from one or more ingress ports/LAGs.

Parameter

Description

<INTERFACE-LIST>

Usage

Specifies a list of ports/LAGs to be blocked for egressing. Specify a
single interface or LAG, or a range as a comma-separated list, or
both. For example: 1/1/1, 1/1/3-1/1/6,lag2, lag1-lag4.

When a port filter configuration is applied on the same ingress physical port/LAG, the configuration is
updated with the new sets of egress ports/LAGs that are to be blocked for egressing and that are not a
part of its previous configuration. Duplicate updates on an existing port filter configuration are ignored.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

150

Whenegressports/LAGsareremovedfromtheexistingportfilterconfigurationofaningressport/LAG,
egressingisallowedagainonthoseegressports/LAGsforallpacketsoriginatingfromtheingress
port/LAG.
Theno portfilter [<IF-NAME-LIST>]commandremovesportfilterconfigurationsfromtheegress
ports/LAGslistedinthe<IF-NAME-LIST>parameteronly.Allotheregressports/LAGsintheportfilter
configurationoftheingressport/LAGremainintact.
IfnophysicalportsorLAGsareprovidedfortheno portfiltercommand,thecommandremovesthe
entireportfilterconfigurationfortheingressport/LAG.
Examples
Creatingafilterthatpreventspacketsreceivedonport1/1/1fromforwardingtoports1/1/3-1/1/6and
toLAGs1through4:
| switch(config)#    |     | interface  | 1/1/1 |                       |
| ------------------ | --- | ---------- | ----- | --------------------- |
| switch(config-if)# |     | portfilter |       | 1/1/3-1/1/6,lag1-lag4 |
CreatingafilterthatpreventspacketsreceivedonLAG1fromforwardingtoports1/1/6andLAGs2and
4:
| switch(config)#        |     | interface | lag        | 1               |
| ---------------------- | --- | --------- | ---------- | --------------- |
| switch(config-lag-if)# |     |           | portfilter | 1/1/6,lag2,lag4 |
Removingfiltersfromanexistingconfigurationthatallowsbackpacketsreceivedonport1/1/1to
forwardtoports1/1/6andLAGs3and4:
| switch(config)#    |     | interface     | 1/1/1 |                 |
| ------------------ | --- | ------------- | ----- | --------------- |
| switch(config-if)# |     | no portfilter |       | 1/1/6,lag3,lag4 |
RemovingallfiltersfromanexistingconfigurationthatallowsbackpacketsreceivedonLAG1to
forwardtoalltheportsandLAGs:
| switch(config)#        |         | interface | lag           | 1            |
| ---------------------- | ------- | --------- | ------------- | ------------ |
| switch(config-lag-if)# |         |           | no portfilter |              |
| Command History        |         |           |               |              |
| Release                |         |           |               | Modification |
| 10.07orearlier         |         |           |               | --           |
| Command Information    |         |           |               |              |
| Platforms              | Command | context   |               | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-lag-if |     |     | rightsforthiscommand. |
| --- | ------------- | --- | --- | --------------------- |
show portfilter
| show portfilter | [<IFNAME>][vsx-peer] |     |     |     |
| --------------- | -------------------- | --- | --- | --- |
Portfiltering|151

Description
Displaysfiltersettingsforallinterfacesoraspecificinterface.
Parameter Description
<IFNAME> Specifiestheingressinterfacename.
Specifiesoneofthesevalues:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
<IPV6>:anIPv6address.
n
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Displayingallportfiltersettingsontheswitch:
| switch# show | portfilter          |     |
| ------------ | ------------------- | --- |
| Incoming     | Blocked             |     |
| Interface    | Outgoing Interfaces |     |
-------------------------------------------------------------------------------
| 1/1/1 | 1/1/3-1/1/6,lag1-lag2 |     |
| ----- | --------------------- | --- |
1/1/3 1/1/1,1/1/5,1/1/7,1/1/9,1/1/11,1/1/13,1/1/15,1/1/17,1/1/19,1/1/21,
1/1/23,1/1/25,1/1/27,1/1/29,1/1/31,1/1/33,1/1/35
| lag2 | 1/1/1,1/1/3-1/1/6 |     |
| ---- | ----------------- | --- |
Displayingtheportfiltersettingsforport1/1/1:
| switch# show | portfilter          | 1/1/1 |
| ------------ | ------------------- | ----- |
| Incoming     | Blocked             |       |
| Interface    | Outgoing Interfaces |       |
-------------------------------------------------------------------------------
| 1/1/1 | 1/1/3-1/1/6,lag1-lag2 |     |
| ----- | --------------------- | --- |
DisplayingtheportfiltersettingsforLAG2:
| switch# show | portfilter          | lag2 |
| ------------ | ------------------- | ---- |
| Incoming     | Blocked             |      |
| Interface    | Outgoing Interfaces |      |
-------------------------------------------------------------------------------
| lag2            | 1/1/1,1/1/3-1/1/6 |     |
| --------------- | ----------------- | --- |
| Command History |                   |     |
Release Modification
10.07orearlier --
| Command Information |     |     |
| ------------------- | --- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 152

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

Port filtering | 153

Chapter 10

DNS

DNS

The Domain Name System (DNS) is the Internet protocol for mapping a hostname to its IP address. DNS
allows users to enter more readily memorable and intuitive hostnames, rather than IP addresses, to
identify devices connected to a network. It also allows a host to keep the same hostname even if it
changes its IP address.

Hostname resolution can be either static or dynamic.

n In static resolution, a local table is defined on the switch that associates hostnames with their IP
addresses. Static tables can be used to speed up the resolution of frequently queried hosts.

n Dynamic resolution requires that the switch query a DNS server located elsewhere on the network.

Dynamic name resolution takes more time than static name resolution, but requires far less
configuration and management.

DNS client

The DNS client resolves hostnames to IP addresses for protocols that are running on the switch. When
the DNS client receives a request to resolve a hostname, it can do so in one of two ways:

n Forward the request to a DNS name server for resolution.

n Reply to the request without using a DNS name server, by resolving the name using a statically

defined table of hostnames and their associated IP addresses.

Configuring the DNS client

Procedure

1. Configure one or more DNS name servers with the command ip dns server.

2. To resolve DNS requests by appending a domain name to the requests, either configure a single
domain name with the command ip dns domain-name, or configure a list of up to six domain
names with the command ip dns domain-list.

3. To use static name resolution for certain hosts, associate an IP address to a host with the

command ip dns host.

4. Review your DNS configuration settings with the command show ip dns.

Examples

This example creates the following configuration:

n Defines the domain switch.com to append to all requests.

n Defines a DNS server with IPv4 address of 1.1.1.1.

n Defines a static DNS host named myhost1 with an IPv4 address of 3.3.3.3.

n DNS client traffic is sent on the default VRF (named default).

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

154

| switch(config)# |     | ip dns domain-name |     | switch.com |     |
| --------------- | --- | ------------------ | --- | ---------- | --- |
switch(config)#
|                 |                 | ip dns server-address |         | 1.1.1.1 |         |
| --------------- | --------------- | --------------------- | ------- | ------- | ------- |
| switch(config)# |                 | ip dns host           | myhost1 | 3.3.3.3 |         |
| switch(config)# |                 | exit                  |         |         |         |
| switch#         | show            | ip dns                |         |         |         |
| VRF             | Name : vrf_mgmt |                       |         |         |         |
| Host            | Name            |                       |         |         | Address |
--------------------------------------------------------------------------------
| VRF    | Name : vrf_default |              |     |     |         |
| ------ | ------------------ | ------------ | --- | --- | ------- |
| Domain | Name               | : switch.com |     |     |         |
| DNS    | Domain list        | :            |     |     |         |
| Name   | Server(s)          | : 1.1.1.1    |     |     |         |
| Host   | Name               |              |     |     | Address |
--------------------------------------------------------------------------------
myhost1
Thisexamplecreatesthefollowingconfiguration:
n DefinesthreedomainstoappendtoDNSrequestsdomain1.com,domain2.com,domain3.com
withtrafficforwardingonVRFmainvrf.
n DefinesaDNSserverwithanIPv6addressofc::13.
n DefinesaDNShostnamedmyhostwithanIPv4addressof3.3.3.3.
| switch(config)# |     | ip dns domain-list |     | domain1.com | vrf mainvrf |
| --------------- | --- | ------------------ | --- | ----------- | ----------- |
switch(config)#
|                 |                | ip dns domain-list    |              | domain2.com | vrf mainvrf |
| --------------- | -------------- | --------------------- | ------------ | ----------- | ----------- |
| switch(config)# |                | ip dns domain-list    |              | domain3.com | vrf mainvrf |
| switch(config)# |                | ip dns server-address |              | c::13       |             |
| switch(config)# |                | ip dns host           | myhost       | 3.3.3.3     | vrf mainvrf |
| switch(config)# |                | quit                  |              |             |             |
| switch#         | show           | ip dns mainvrf        |              |             |             |
| VRF             | Name : mainvrf |                       |              |             |             |
| Domain          | Name           | :                     |              |             |             |
| DNS             | Domain list    | : domain1.com,        | domain2.com, |             | domain3.com |
| Name            | Server(s)      | : c::13               |              |             |             |
| Host            | Name           |                       |              |             | Address     |
--------------------------------------------------------------------------------
myhost 3.3.3.3
| DNS       | client      | commands      |      |                  |     |
| --------- | ----------- | ------------- | ---- | ---------------- | --- |
| ip dns    | domain-list |               |      |                  |     |
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | <VRF-NAME>]      |     |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf <VRF-NAME>] |     |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
DNS|155

Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     |     | ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ----------- | --- |
| switch(config)# |     |     | ip dns | domain-list |     | domain2.com |     |
Thisexampledefinesalistwithtwoentries,domain2.comanddomain5.com,withrequestsbeingsent
onmainvrf.
| switch(config)# |     |     | ip dns | domain-list |     | domain2.com | vrf mainvrf |
| --------------- | --- | --- | ------ | ----------- | --- | ----------- | ----------- |
| switch(config)# |     |     | ip dns | domain-list |     | domain5.com | vrf mainvrf |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |             |         | no ip dns | domain-list |              | domain1.com |     |
| --------------- | ----------- | ------- | --------- | ----------- | ------------ | ----------- | --- |
| Command         | History     |         |           |             |              |             |     |
| Release         |             |         |           |             | Modification |             |     |
| 10.07orearlier  |             |         |           |             | --           |             |     |
| Command         | Information |         |           |             |              |             |     |
| Platforms       |             | Command | context   |             | Authority    |             |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | domain-name |     |               |     |       |            |     |
| --------- | ----------- | --- | ------------- | --- | ----- | ---------- | --- |
| ip dns    | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.
Bydefault,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip
dns domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 156

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     | ip  | dns | domain-name | domain.com |     |
| --------------- | --- | --- | --- | ----------- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |             | no      | ip dns  | domain-name | domain.com   |     |
| --------------- | ----------- | ------- | ------- | ----------- | ------------ | --- |
| Command         | History     |         |         |             |              |     |
| Release         |             |         |         |             | Modification |     |
| 10.07orearlier  |             |         |         |             | --           |     |
| Command         | Information |         |         |             |              |     |
| Platforms       |             | Command | context |             | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | host |             |           |           |                  |     |
| --------- | ---- | ----------- | --------- | --------- | ---------------- | --- |
| ip dns    | host | <HOST-NAME> | <IP-ADDR> |           | [ vrf <VRF-NAME> | ]   |
| no ip dns | host | <HOST-NAME> |           | <IP-ADDR> | [ vrf <VRF-NAME> | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadof
queryingaDNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFis
defined,thedefaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
DNS|157

Examples
| ThisexampledefinesanIPv4addressof |     |     |     |     | 3.3.3.3forhost1. |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
switch(config)#
|                                       |             |         | ip dns    | host | host1 | 3.3.3.3           |     |       |
| ------------------------------------- | ----------- | ------- | --------- | ---- | ----- | ----------------- | --- | ----- |
| ThisexampledefinesanIPv6addressofb::5 |             |         |           |      |       | forhost           | 1.  |       |
| switch(config)#                       |             |         | ip dns    | host | host1 | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |             |         |           |      |       | host 1withaddress |     | b::5. |
| switch(config)#                       |             |         | no ip dns | host | host1 | b::5              |     |       |
| Command                               | History     |         |           |      |       |                   |     |       |
| Release                               |             |         |           |      |       | Modification      |     |       |
| 10.07orearlier                        |             |         |           |      |       | --                |     |       |
| Command                               | Information |         |           |      |       |                   |     |       |
| Platforms                             |             | Command | context   |      |       | Authority         |     |       |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | server         | address |           |     |       |            |     |     |
| --------- | -------------- | ------- | --------- | --- | ----- | ---------- | --- | --- |
| ip dns    | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
| no ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 158

| switch(config)# | ip  | dns server-address |     |     | 1.1.1.1 |     |
| --------------- | --- | ------------------ | --- | --- | ------- | --- |
Thisexampledefinesanameserverata::1.
| switch(config)# | ip  | dns server-address |     |     | a::1 |     |
| --------------- | --- | ------------------ | --- | --- | ---- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)#     | no      | ip dns  | server-address |              | a::1 |     |
| ------------------- | ------- | ------- | -------------- | ------------ | ---- | --- |
| Command History     |         |         |                |              |      |     |
| Release             |         |         |                | Modification |      |     |
| 10.07orearlier      |         |         |                | --           |      |     |
| Command Information |         |         |                |              |      |     |
| Platforms           | Command | context |                | Authority    |      |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip dns |                            |     |     |     |     |     |
| ----------- | -------------------------- | --- | --- | --- | --- | --- |
| show ip dns | [vrf <VRF-NAME>][vsx-peer] |     |     |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow ip dns
command.
switch(config)#
|                 | ip  | dns domain-name    |       | domain.com     |         |         |
| --------------- | --- | ------------------ | ----- | -------------- | ------- | ------- |
| switch(config)# | ip  | dns domain-list    |       | domain5.com    |         |         |
| switch(config)# | ip  | dns domain-list    |       | domain8.com    |         |         |
| switch(config)# | ip  | dns server-address |       |                | 4.4.4.4 |         |
| switch(config)# | ip  | dns server-address |       |                | 6.6.6.6 |         |
| switch(config)# | ip  | dns host           | host3 | 5.5.5.5        |         |         |
| switch(config)# | ip  | dns host           | host2 | 2.2.2.2        |         |         |
| switch(config)# | ip  | dns host           | host3 | c::12          |         |         |
| switch(config)# | ip  | dns domain-name    |       | reddomain.com  |         | vrf red |
| switch(config)# | ip  | dns domain-list    |       | reddomain5.com |         | vrf red |
switch(config)#
|     | ip  | dns domain-list |     | reddomain8.com |     | vrf red |
| --- | --- | --------------- | --- | -------------- | --- | ------- |
DNS|159

| switch(config)# |     | ip dns | server-address |     | 4.4.4.5 |     | vrf red |
| --------------- | --- | ------ | -------------- | --- | ------- | --- | ------- |
switch(config)#
|                 |           | ip dns         | server-address |             | 6.6.6.7 |     | vrf red |
| --------------- | --------- | -------------- | -------------- | ----------- | ------- | --- | ------- |
| switch(config)# |           | ip dns         | host           | host3       | 5.5.5.6 | vrf | red     |
| switch(config)# |           | ip dns         | host           | host2       | 2.2.2.3 | vrf | red     |
| switch(config)# |           | ip dns         | host           | host3       | c::13   | vrf | red     |
| switch#         | show      | ip dns         |                |             |         |     |         |
| VRF Name        | : default |                |                |             |         |     |         |
| Domain Name     | :         | domain.com     |                |             |         |     |         |
| DNS Domain      | list      | : domain5.com, |                | domain8.com |         |     |         |
| Name Server(s)  |           | : 4.4.4.4,     | 6.6.6.6        |             |         |     |         |
| Host Name       |           | Address        |                |             |         |     |         |
-------------------------------
| host2          |       | 2.2.2.2           |         |     |                |     |     |
| -------------- | ----- | ----------------- | ------- | --- | -------------- | --- | --- |
| host3          |       | 5.5.5.5           |         |     |                |     |     |
| host3          |       | c::12             |         |     |                |     |     |
| VRF Name       | : red |                   |         |     |                |     |     |
| Domain Name    | :     | reddomain.com     |         |     |                |     |     |
| DNS Domain     | list  | : reddomain5.com, |         |     | reddomain8.com |     |     |
| Name Server(s) |       | : 4.4.4.5,        | 6.6.6.7 |     |                |     |     |
| Host Name      |       | Address           |         |     |                |     |     |
-------------------------------
| host2           |     | 2.2.2.3 |                |     |             |     |         |
| --------------- | --- | ------- | -------------- | --- | ----------- | --- | ------- |
| host3           |     | 5.5.5.6 |                |     |             |     |         |
| host3           |     | c::13   |                |     |             |     |         |
| switch(config)# |     | ip dns  | domain-name    |     | domain.com  |     | vrf red |
| switch(config)# |     | ip dns  | domain-list    |     | domain5.com |     | vrf red |
| switch(config)# |     | ip dns  | domain-list    |     | domain8.com |     | vrf red |
| switch(config)# |     | ip dns  | server-address |     | 4.4.4.4     |     | vrf red |
| switch(config)# |     | ip dns  | server-address |     | 6.6.6.6     |     | vrf red |
switch(config)#
|                 |       | ip dns         | host     | host3       | 5.5.5.5 | vrf | red     |
| --------------- | ----- | -------------- | -------- | ----------- | ------- | --- | ------- |
| switch(config)# |       | no ip          | dns host | host2       | 2.2.2.2 |     | vrf red |
| switch(config)# |       | ip dns         | host     | host3       | c::12   | vrf | red     |
| switch#         | show  | ip dns vrf     | red      |             |         |     |         |
| VRF Name        | : red |                |          |             |         |     |         |
| Domain Name     | :     | domain.com     |          |             |         |     |         |
| DNS Domain      | list  | : domain5.com, |          | domain8.com |         |     |         |
| Name Server(s)  |       | : 4.4.4.4,     | 6.6.6.6  |             |         |     |         |
| Host Name       |       | Address        |          |             |         |     |         |
-------------------------------
| host3          |             | 5.5.5.5 |     |     |              |     |     |
| -------------- | ----------- | ------- | --- | --- | ------------ | --- | --- |
| host3          |             | c::12   |     |     |              |     |     |
| Command        | History     |         |     |     |              |     |     |
| Release        |             |         |     |     | Modification |     |     |
| 10.07orearlier |             |         |     |     | --           |     |     |
| Command        | Information |         |     |     |              |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 160

Platforms

Command context

Authority

All platforms

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

DNS | 161

Device discovery and configuration

Chapter 11

Device discovery and configuration

The switch provides support for LLDP and CDP to enable automatic discovery and configuration of other
devices on the network.

LLDP

The IEEE 802.1AB Link Layer Discovery Protocol (LLDP) provides a standards-based method for network
devices to discover each other and exchange information about their capabilities. An LLDP device
advertises itself to adjacent (neighbor) devices by transmitting LLDP data packets on all interfaces on
which outbound LLDP is enabled, and reading LLDP advertisements from neighbor devices on ports on
which inbound LLDP is enabled. Inbound packets from neighbor devices are stored in a special LLDP
MIB (management information base). This information can then be queried by other devices through
SNMP.

LLDP information is used by network management tools to create accurate physical network topologies
by determining which devices are neighbors and through which interfaces they connect. LLDP operates
at layer 2 and requires an LLDP agent to be active on each interface that sends and receives LLDP
advertisements. LLDP advertisements can contain a variable number of TLV (type, length, value)
information elements. Each TLV describes a single attribute of a device such as: system capabilities,
management IP address, device ID, port ID.

Packet boundaries

When multiple LLDP devices are directly connected, an outbound LLDP packet travels only to the next
LLDP device. An LLDP-capable device does not forward LLDP packets to any other devices, regardless of
whether they are LLDP-enabled.

An intervening hub or repeater forwards the LLDP packets it receives in the same manner as any other
multicast packets it receives. Therefore, two LLDP switches joined by a hub or repeater handle LLDP
traffic in the same way that they would if directly connected.

Any intervening 802.1D device or Layer-3 device that is either LLDP-unaware or has disabled LLDP
operation drops the packet.

LLDP-MED

LLDP-MED (ANSI/TIA-1057/D6) extends the LLDP (IEEE 802.1AB) industry standard to support advanced
features on the network edge for Voice Over IP (VoIP) endpoint devices with specialized capabilities and
LLDP-MED standards-based functionality. LLDP-MED in the switches uses the standard LLDP commands
described earlier in this section, with some extensions, and also introduces new commands unique to
LLDP-MED operation. The show commands described elsewhere in this section are applicable to both
LLDP and LLDP-MED operation. LLDP-MED enables:

n Configure Voice VLAN and advertise it to connected MED endpoint devices.

n Power over Ethernet (PoE) status and troubleshooting support via SNMP.

LLDP agent

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

162

When you enable LLDP on the switch, it is automatically enabled on all data plane interfaces. You can
customize this behavior by manually enabling/disabling support on each interface.

Supported standards

The LLDP agent supports the following standards: IEEE 802.1AB-2005, Station, and Media Access Control
Connectivity Discovery.

Supported interfaces

LLDP is supported on interfaces mapped to a physical port, and the Out-Of-Band Management (OOBM)
port. It is not supported on logical interfaces, such as loopback, tunnels, and SVIs.

Operating modes

When LLDP is enabled, the switch periodically transmits an LLDP advertisement (packet) out each active
port enabled for outbound LLDP transmissions and receives LLDP advertisements on each active port
enabled to receive LLDP traffic.

The LLDP agent can operate in one of the following modes:

n Transmit and receive (TxRx): This is the default setting on all ports. It enables a given port to both

transmit and receive LLDP packets and to store the data from received (inbound) LLDP packets in the
switch's MIB.

n Transmit only (Tx): Enables a port to transmit LLDP packets that can be read by LLDP neighbors.
However, the port drops inbound LLDP packets from LLDP neighbors without reading them. This
prevents the switch from learning about LLDP neighbors on that port.

n Receive only (Rx): Enables a port to receive and read LLDP packets from LLDP neighbors and to store
the packet data in the switch's MIB. However, the port does not transmit outbound LLDP packets.
This prevents LLDP neighbors from learning about the switch through that port.

n Disabled: Disables LLDP packet transmissions and reception on a port. In this state, the switch does

not use the port for either learning about LLDP neighbors or informing LLDP neighbors of its
presence.

An LLDP agent operating in TxRx mode or Tx mode sends LLDP frames to its directly connected devices
both periodically and when the local configuration changes.

Sending LLDP frames

Each time the LLDP operating mode of an LLDP agent changes, its LLDP protocol state machine
reinitializes. A configurable reinitialization delay prevents frequent initializations caused by frequent
changes to the operating mode. If you configure the reinitialization delay, an LLDP agent must wait the
specified amount of time to initialize LLDP after the LLDP operating mode changes.

Receiving LLDP frames

An LLDP agent operating in TxRx mode or Rx mode confirms the validity of TLVs carried in every
received LLDP frame. If the TLVs are valid, the LLDP agent saves the information and starts an aging
timer. The initial value of the aging timer is equal to the TTL value in the Time To Live TLV carried in the
LLDP frame. When the LLDP agent receives a new LLDP frame, the aging timer restarts. When the aging
timer decreases to zero, all saved information ages out.

TLV support

By default, the agent sends and receives the following mandatory TLVs on each interface:

Device discovery and configuration | 163

n Port ID

n Chassis ID

n TTL

By default, the following ANSI/TIA-1057 TLVs for LLDP Media Endpoint Discovery (MED) are enabled on
an agent. Sending them depends on the configuration and reception of any MED TLVs:

n MAC/PHY status. Includes the bit rate and auto negotiation status of the link.

n Power Via MDI: Includes Power Over Ethernet related information for supported interfaces.

n Port description

n System name

n System description

n Management address

n System capabilities

n Port VLAN ID

By default, the agent sends and receives the following ANSI/TIA-1057 TLVs for LLDP Media Endpoint
Discovery (MED):

n Capabilities: Indicates MED TLV capability.

n Power Via MDI: Includes Power Over Ethernet related information.

n Network Policy: Includes the VLAN configuration for voice application.

n Location: Location identification information.

n Extended Power Via MDI: Power Over Ethernet related information

TLV advertisements

The LLDP agent transmits the following:

n Chassis-ID: Base MAC address of the switch.

n Port-ID: Port number of the physical port.

n Time-to-Live (TTL): Length of time an LLDP neighbor retains advertised data before discarding it.

n System capabilities: Identifies the primary switch capabilities (bridge, router). Identifies the primary

switch functions that are enabled, such as routing.

n System description: Includes switch model name and running software version, and ROM version.

n System name: Name assigned to the switch.

n Management address: Default address selection method unless an optional address is configured.

n Port description: Physical port identifier.

n Port VLAN ID: On an L2 port, contains access or native VLAN ID. On an L3 port, contains a value of 0.
Trunk allowed VLANs information are not advertised as part of the Port VLAN ID TLV. (Not supported
on the OOBM interface)

LLDP MED support

LLDP-MED interoperates with directly connected IP telephony (endpoint) clients and provides the
following features:

n Advertisement of the voice VLAN configured on the interface which is used by connected IP

telephony (endpoint) clients.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

164

n Advertisement of the configured location on the switch that can be used by the connected endpoint.

n Support for the fast-start capability

LLDP-MED is intended for use with VoIP endpoints and is not designed to support links between network

infrastructure devices (such as switch-to-switch or switch-to-router links).

LLDP EEE

Energy Efficient Ethernet (EEE) is a mechanism defined by IEEE 802.3az, which is an extension of 802.3
IEEE standards. EEE defines support for the device to operate in the Low Power Idle (LPI) mode during
low link utilization. This allows both sides of a link to disable or turn off respective transmit/receive
circuitry to save power. EEE uses LLDP for exchanging optimal set of parameters for both devices.

Guidelines

n An LLDP must not contain more than one EEE TLV.

n LLDP may or may not be enabled on the interfaces supporting EEE. If LLDP is not enabled, it might

not be in the optimal operational mode.

n EEE TLV should not be exchanged until it negotiates from L1 and it detects peer EEE capabilities.

n EEE TLV is disabled by default and enabled only when EEE is active.

n EEE and EEE TLV exchange can be enabled or disabled at the interface level.

Configuring the LLDP agent

Procedure

1. By default, the LLDP agent is enabled on all active interfaces. If LLDP was disabled, enable it with

the command lldp.

2. By default, the LLDP agent transmits and receive on all interfaces. To customize LLDP behavior on

a specific interface, use the commands lldp transmit and lldp receive.

3. By default, the LLDP agent sets the management address in all TLVs in the following order:

a. LLDP management IP address.
b. Loopback interface IP.
c. ROP (L3 ports) or SVI (L2 ports).
d. OOBM (Management interface IP).
e. Base MAC.

On the OOBM port, the following order is used:

a. LLDP management IP address,

b.

c.

IP address of the management interface (OOBM port).

IP address of the loopback interface.

d. Base MAC address of the switch.

To specify a different address, use the commands lldp management-ipv4-address and lldp
management-ipv6-address

4. By default, all supported TLVs are sent and received. To customize the list, use the command

lldp select-tlv.

5. By default, support for the LLDP-MED TLV is enabled. To customize settings, use the commands

lldp med and lldp med-location.

Device discovery and configuration | 165

6. Ifrequired,adjustLLDPtimer,holdtime,reinitializationdelay,andtransmitdelayfromtheir
defaultvalueswiththecommandslldp timer,lldp holdtime,lldp reinit,andlldp txdelay.
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablesLLDPsupport.
n DisablesLLDPtransmissiononinterface1/1/1.
| switch(config)#      | lldp      |                  |     |
| -------------------- | --------- | ---------------- | --- |
| switch(config)#      | interface | 1/1/1            |     |
| switch(config-copp)# |           | no lldp transmit |     |
LLDP commands
| clear lldp neighbors |     |     |     |
| -------------------- | --- | --- | --- |
| clear lldp neighbors |     |     |     |
Description
ClearsallLLDPneighbordetails.
Examples
ClearingallLLDPneighbordetails:
| switch# clear       | lldp    | neighbors |              |
| ------------------- | ------- | --------- | ------------ |
| Command History     |         |           |              |
| Release             |         |           | Modification |
| 10.07orearlier      |         |           | --           |
| Command Information |         |           |              |
| Platforms           | Command | context   | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| clear lldp statistics |     |     |     |
| --------------------- | --- | --- | --- |
| clear lldp statistics |     |     |     |
Description
ClearsallLLDPneighborstatistics.
Examples
ClearingallLLDPneighborstatistics:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 166

| switch# clear       | lldp    | statistics |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
lldp
lldp
no lldp
Description
EnablesLLDPsupportgloballyonallactiveinterfaces.Bydefault,LLDPisenabled.
ThenoformofthiscommanddisablesLLDPsupportgloballyonallactiveinterfaces.Itdoesnotremove
anyLLDPconfigurationsettings.
Examples
EnablingLLDP:
| switch(config)# | lldp |     |     |
| --------------- | ---- | --- | --- |
DisablingLLDP:
| switch(config)#     | no      | lldp    |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp dot3
| lldp dot3 {poe | | macphy} |     |     |
| -------------- | --------- | --- | --- |
Devicediscoveryandconfiguration|167

| no lldp dot3 | {poe | | macphy} |     |
| ------------ | ------ | ------- | --- |
Description
Setsthe802.3TLVstobeadvertised.Bydefault,advertisementofbothPOEandMAC/PHYTLVsis
enabled.NotsupportedontheOOBMinterface.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     |     | Description                                       |
| --------- | --- | --- | ------------------------------------------------- |
| poe       |     |     | SpecifiesadvertisementofpoweroverEthernetdatalink |
classification.
macphy
Specifiesadvertisementofmediaaccesscontrolandphysicallayer
information.
Examples
EnablingadvertisementofthePOETLV:
| switch(config-if)# |     | lldp dot3 | poe |
| ------------------ | --- | --------- | --- |
DisablingadvertisementofthePOETLV:
| switch(config-if)#  |         | no lldp | dot3 poe     |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp holdtime-multiplier
| lldp holdtime-multiplier |     | <multiplier> |     |
| ------------------------ | --- | ------------ | --- |
no lldp holdtime-multiplier
Description
SetstheholdtimeTTLmultipliervaluethatisusedtocalculatetheLLDPTime-to-Livevalue.Time-to-Live
definesthelengthoftimethatneighborsconsiderLLDPinformationsentbythisagentasvalid.When
Time-to-Liveexpires,theinformationisdeletedbytheneighbor.Time-to-liveiscalculatedbymultiplying
| holdtimebythevalueoflldp |     | timer. |     |
| ------------------------ | --- | ------ | --- |
ThenoformofthiscommandsetstheholdtimeTTLmultipliertoitsdefaultvalueof4.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 168

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<multiplier> SpecifiestheTTLmultiplierintherangeof2to10.Default:4.
Formula
TTL=Holdtime-multiplierxlldptimer
where:
TTL=Time-to-Live
Holdtime-multiplier=Multiplyingholdtimevalue
lldptimer=Messagetransmissioninterval
Examples
Settingtheholdtimeto8timesofthevalueoflldptimer:
| switch(config)# | lldp | holdtime-multiplier | 8   |
| --------------- | ---- | ------------------- | --- |
Settingtheholdtimetothedefaultvalueof4timesofthevalueoflldptimer:
| switch(config)#     | no      | lldp holdtime-multiplier |              |
| ------------------- | ------- | ------------------------ | ------------ |
| Command History     |         |                          |              |
| Release             |         |                          | Modification |
| 10.07orearlier      |         |                          | --           |
| Command Information |         |                          |              |
| Platforms           | Command | context                  | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp management-ipv4-address
| lldp management-ipv4-address |     | <IPV4-ADDR> |     |
| ---------------------------- | --- | ----------- | --- |
no lldp management-ipv4-address
Description
DefinestheIPv4managementaddressoftheswitchwhichissentinthemanagementaddressTLV.One
IPv4andoneIPv6managementaddresscanbeconfigured.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
IPaddressoftheport
n
n IPaddressofthemanagementinterface
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv4managementaddressoftheswitch.
Devicediscoveryandconfiguration|169

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesthemanagementaddressoftheswitchasanIPv4format
(x.x.x.x),wherexisadecimalvaluefrom0to255.
Examples
Settingthemanagementaddressto10.10.10.2:
| switch(config)# | lldp | management-ipv4-address |     | 10.10.10.2 |
| --------------- | ---- | ----------------------- | --- | ---------- |
Removingthemanagementaddress:
switch(config)#
|                     | no      | lldp management-ipv4-address |              |     |
| ------------------- | ------- | ---------------------------- | ------------ | --- |
| Command History     |         |                              |              |     |
| Release             |         |                              | Modification |     |
| 10.07orearlier      |         |                              | --           |     |
| Command Information |         |                              |              |     |
| Platforms           | Command | context                      | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp management-ipv6-address
| lldp management-ipv6-address |     | <IPV6-ADDR> |     |     |
| ---------------------------- | --- | ----------- | --- | --- |
no lldp management-ipv6-address
Description
DefinestheIPv6managementaddressoftheswitch.Themanagementaddressisencapsulatedinthe
managementaddressTLV.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
n IPaddressoftheport
n IPaddressofthemanagementinterface
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv6managementaddressoftheswitch.
| Parameter   |     |     | Description                      |     |
| ----------- | --- | --- | -------------------------------- | --- |
| <IPV6-ADDR> |     |     | SpecifiesanIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 170

Settingthemanagementaddressto2001:db8:85a3::8a2e:370:7334:
switch(config)# lldp management-ipv6-address 2001:0db8:85a3::8a2e:0370:7334
Removingthemanagementaddress:
| switch(config)# | no          | lldp management-ipv6-address |              |     |     |
| --------------- | ----------- | ---------------------------- | ------------ | --- | --- |
| Command         | History     |                              |              |     |     |
| Release         |             |                              | Modification |     |     |
| 10.07orearlier  |             |                              | --           |     |     |
| Command         | Information |                              |              |     |     |
| Platforms       | Command     | context                      | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp med
lldp med [poe [priority-override] | capability | network-policy]
| no med [poe | [priority-override] | |   | capability | network-policy] |     |     |
| ----------- | ------------------- | --- | ---------------------------- | --- | --- |
Description
ConfiguressupportfortheLLDP-MEDTLV.LLDP-MED(mediaendpointdevices)isanextensiontoLLDP
developedbyTIAtosupportinteroperabilitybetweenVoIPendpointdevicesandothernetworkingend-
devices.TheswitchonlysendstheLLDPMEDTLVafterreceivingaMEDTLVfromandconnected
endpointdevice.
NotsupportedontheOOBMinterface.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
poe [priority-override] SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
|     |     |     | dot3 poeandlldp | med poeareenabled,thelldp | dot3 poe3 |
| --- | --- | --- | --------------- | ------------------------- | --------- |
settingtakesprecedence.Default:enabled.
| capability |     |     | SpecifiesadvertisementofsupportedLLDPMEDTLVs.The |     |     |
| ---------- | --- | --- | ------------------------------------------------ | --- | --- |
capabilityTLVisalwayssentwithotherMEDTLVs,thereforeit
cannotbedisabledwhenotherMEDTLVsareenabled.Default:
enabled.
network-policy
Networkpolicydiscoveryletsendpointsandnetworkdevices
advertisetheirVLANIDs,andIEEE802.1p(PCPandDSCP)values
forvoiceapplications.ThisTLVisonlysentwhenavoiceVLAN
policyispresent.Default:enabled.
Examples
Devicediscoveryandconfiguration|171

EnablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |     | lldp | med | network-policy |     |     |
| ------------------ | --- | ---- | --- | -------------- | --- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)#  |         | no  | lldp med | network-policy |              |     |
| ------------------- | ------- | --- | -------- | -------------- | ------------ | --- |
| Command History     |         |     |          |                |              |     |
| Release             |         |     |          |                | Modification |     |
| 10.07orearlier      |         |     |          |                | --           |     |
| Command Information |         |     |          |                |              |     |
| Platforms           | Command |     | context  |                | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp med-location
| lldp med-location | {civic-addr |     |             | | elin-addr | }   |     |
| ----------------- | ----------- | --- | ----------- | ----------- | --- | --- |
| no med-location   | {civic-addr |     | | elin-addr |             | }   |     |
Description
ConfiguressupportfortheLLDP-MEDTLV.Supportsonlycivicaddressandemergencylocation
informationnumber(ELIN).Coordinate-basedlocationisnotsupported.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter  |     |     |     |     | Description                           |     |
| ---------- | --- | --- | --- | --- | ------------------------------------- | --- |
| civic-addr |     |     |     |     | ConfigurestheLLDPMEDciviclocationTLV. |     |
elin-addr ConfiguressupportfortheLLDPMEDemergencylocationTLV.
Examples
EnablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | lldp | med-location |     | elin-addr | gher |
| ------------------ | --- | ---- | ------------ | --- | --------- | ---- |
DisablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | no  | lldp med-location |     | elin-addr | gher |
| ------------------ | --- | --- | ----------------- | --- | --------- | ---- |
EnablingsupportfortheLLDPMEDcivicaddressTLV:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 172

switch(config-if)# lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
DisablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# no lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp receive
lldp receive
no lldp receive
Description
EnablesreceptionofLLDPinformationonaninterface.Bydefault,LLDPreceptionisenabledonall
activeinterfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablesreceptionofLLDPinformationonaninterface.
Examples
EnablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1        |     |
| ------------------ | --------- | ------------ | --- |
| switch(config-if)# |           | lldp receive |     |
DisablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1           |     |
| ------------------ | --------- | --------------- | --- |
| switch(config-if)# |           | no lldp receive |     |
EnablingLLDPreceptionontheOOBMinterface:
| switch(config)#    | interface | mgmt         |     |
| ------------------ | --------- | ------------ | --- |
| switch(config-if)# |           | lldp receive |     |
DisablingLLDPreceptionontheOOBMinterface:
Devicediscoveryandconfiguration|173

| switch(config)# | interface |     | mgmt |     |
| --------------- | --------- | --- | ---- | --- |
switch(config-if)#
|                     |         | no lldp | receive |              |
| ------------------- | ------- | ------- | ------- | ------------ |
| Command History     |         |         |         |              |
| Release             |         |         |         | Modification |
| 10.07orearlier      |         |         |         | --           |
| Command Information |         |         |         |              |
| Platforms           | Command | context |         | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp reinit
| lldp reinit | <TIME> |     |     |     |
| ----------- | ------ | --- | --- | --- |
no lldp reinit
Description
Setstheamountoftime(inseconds)towaitbeforeperformingLLDPinitializationonaninterface.
Thenoformofthiscommandsetsthereinitializationtimetoitsdefaultvalueof2seconds.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<TIME> Specifiesthereinitializationtimeinseconds.Range:1to10.
Default:2seconds.
Examples
Settingthereinitializationtimeto5seconds:
| switch(config)# | lldp | reinit | 5   |     |
| --------------- | ---- | ------ | --- | --- |
Settingthereinitializationtimetothedefaultvalueof2seconds:
| switch(config)#     | no  | lldp reinit |     |              |
| ------------------- | --- | ----------- | --- | ------------ |
| Command History     |     |             |     |              |
| Release             |     |             |     | Modification |
| 10.07orearlier      |     |             |     | --           |
| Command Information |     |             |     |              |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 174

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

lldp select-tlv

lldp select-tlv <TLV-NAME>
no lldp select-tlv <TLV-NAME>

Description

Selects a TLV that the LLDP agent will send and receive. By default, all supported TLVs are sent and
received.

The no form of this command stops the LLDP agent from sending and receiving a specific TLV.

Parameter

Description

select-tlv <TLV-NAME>

Specifies the TLV name to send. The following TLV names are
supported:

n management-address: Selected as follows:

1.
2.

3.

IPv4 or IPV6 management address.
IP address of the lowest configured loopback

interface.
If layer 3, then the route-only port IP address. If

layer 2, the IP address of the SVI.

4. OOBM interface IP address.
5. Base MAC address of the switch.

n port-description: A description of the port.

n port-vlan-id: VLAN ID assigned to the port.

n system-capabilities: Identifies the primary switch

functions that are enabled, such as routing.

n system-description: Description of the system,
comprised of the following information: hardware
serial number, hardware revision number, and
firmware version.

n system-name: Host name assigned to the switch.

Examples

Stopping the LLDP agent from sending the port-description TLV:

switch(config)# no lldp select-tlv port-description

Enabling the LLDP agent to send the port-description TLV:

switch(config)# lldp select-tlv port-description

Command History

Device discovery and configuration | 175

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp timer
| lldp timer <TIME> |     |     |     |
| ----------------- | --- | --- | --- |
no lldp timer
Description
Setstheinterval(inseconds)atwhichlocalLLDPinformationisupdatedandTLVsaresentto
neighboringnetworkdevicesbytheLLDPagent.Theminimumsettingforthistimermustbefourtimes
| thevalueoflldp | txdelay. |     |     |
| -------------- | -------- | --- | --- |
Forexample,thisisavalidconfiguration:
n lldp timer=16
n lldp txdelay=4
And,thisisaninvalidconfiguration:
n lldp timer=5
n lldp txdelay=2
Whencopyingasavedconfigurationtotherunningconfiguration,thevalueforlldp timerisappliedbefore
thevalueoflldp txdelay.Thiscanresultinaconfigurationerrorifthesavedconfigurationhasavalueoflldp
timerthatisnotfourtimesthevalueoflldp txdelayintherunningconfiguration.
Forexample,ifthesavedconfigurationhasthesettings:
| n lldp timer=16 |     |     |     |
| --------------- | --- | --- | --- |
| lldp txdelay=4  |     |     |     |
n
Andtherunningconfigurationhasthesettings:
| n lldp timer=30  |     |     |     |
| ---------------- | --- | --- | --- |
| n lldp txdelay=7 |     |     |     |
Thenyouwillseeanerrorindicatingthatcertainconfigurationsettingscouldnotbeapplied,andyouwillhaveto
| manuallyadjustthevalueoflldp |     | txdelayintherunningconfiguration. |     |
| ---------------------------- | --- | --------------------------------- | --- |
Thenoformofthiscommandsetstheupdateintervaltoitsdefaultvalueof30seconds.
| Parameter |     |     | Description                                           |
| --------- | --- | --- | ----------------------------------------------------- |
| <TIME>    |     |     | Specifiestheupdateinterval(inseconds).Range:5to32768. |
Default:30.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 176

Examples
Settingtheupdateintervalto7seconds:
switch(config)#
|     | lldp | timer 7 |     |
| --- | ---- | ------- | --- |
Settingtheupdateintervaltothedefaultvalueof30seconds:
| switch(config)#     | no      | lldp timer |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp transmit
lldp transsmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionis
enabledonallactiveinterfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablestransmissionofLLDPinformationonaninterface.
Examples
EnablingLLDPtransmissiononinterface1/1/1:
| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|     |     | lldp transsmit |     |
| --- | --- | -------------- | --- |
DisablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1             |     |
| ------------------ | --------- | ----------------- | --- |
| switch(config-if)# |           | no lldp transsmit |     |
EnablingLLDPtransmissionontheOOBMinterface:
| switch(config)#    | interface | mgmt           |     |
| ------------------ | --------- | -------------- | --- |
| switch(config-if)# |           | lldp transsmit |     |
DisablingLLDPtransmissionontheOOBMinterface:
Devicediscoveryandconfiguration|177

| switch(config)# | interface |     | mgmt |
| --------------- | --------- | --- | ---- |
switch(config-if)#
|                     |         | no lldp | transsmit    |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp txdelay
| lldp txdelay | <TIME> |     |     |
| ------------ | ------ | --- | --- |
no lldp txdelay
Description
Setstheamountoftime(inseconds)towaitbeforesendingLLDPinformationfromanyinterface.The
maximumvaluefortxdelayis25%ofthevalueoflldp tx timer.
Thenoformofthiscommandsetsthedelaytimetoitsdefaultvalueof2seconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<TIME>
Specifiesthedelaytimeinseconds.Range:0to10.Default:2.
Examples
Settingthedelaytimeto8seconds:
| switch(config)# | lldp | txdelay | 8   |
| --------------- | ---- | ------- | --- |
Settingthedelaytimetothedefaultvalueof2seconds:
| switch(config)#     | no  | lldp txdelay |              |
| ------------------- | --- | ------------ | ------------ |
| Command History     |     |              |              |
| Release             |     |              | Modification |
| 10.07orearlier      |     |              | --           |
| Command Information |     |              |              |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 178

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp trap enable |        |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- |
| lldp trap        | enable |     |     |     |     |
| no lldp trap     | enable |     |     |     |     |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenot
requiredtobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | lldp | trap | enable |     |
| --------------- | --- | ---- | ---- | ------ | --- |
EnablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     |     | lldp trap | enable |     |
| ------------------ | --- | --- | --------- | ------ | --- |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no  | lldp trap | enable |     |
| --------------- | --- | --- | --------- | ------ | --- |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     |     | no lldp | trap | enable |
| ------------------ | --- | --- | ------- | ---- | ------ |
DisplayingLLDPglobalconfiguration:
| switch#     | show          | lldp configuration |     |     |     |
| ----------- | ------------- | ------------------ | --- | --- | --- |
| LLDP Global | Configuration |                    |     |     |     |
=========================
| LLDP Enabled  |         |            |          | :   | No  |
| ------------- | ------- | ---------- | -------- | --- | --- |
| LLDP Transmit |         | Interval   |          | :   | 30  |
| LLDP Hold     | Time    | Multiplier |          | :   | 4   |
| LLDP Transmit |         | Delay      | Interval | :   | 2   |
| LLDP Reinit   | Timer   | Interval   |          | :   | 2   |
| LLDP Trap     | Enabled |            |          | :   | No  |
Devicediscoveryandconfiguration|179

TLVs Advertised
===============
| Management | Address |     |     |
| ---------- | ------- | --- | --- |
Port Description
Port VLAN-ID
System Description
System Name
| LLDP Port | Configuration |     |     |
| --------- | ------------- | --- | --- |
=======================
| PORT | TX-ENABLED | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 | Yes | Yes | Yes |
| ----- | --- | --- | --- |
| 1/1/2 | Yes | Yes | Yes |
| 1/1/3 | Yes | Yes | Yes |
| 1/1/4 | Yes | Yes | Yes |
| 1/1/5 | Yes | Yes | Yes |
| 1/1/6 | Yes | Yes | Yes |
...........
...........
| mgmt | Yes | Yes | Yes |
| ---- | --- | --- | --- |
DisplayingLLDPConfigurationfortheinterface:
| switch#     | show lldp configuration | 1/1/1 |     |
| ----------- | ----------------------- | ----- | --- |
| LLDP Global | Configuration           |       |     |
=========================
| LLDP Enabled  |                 | : Yes |     |
| ------------- | --------------- | ----- | --- |
| LLDP Transmit | Interval        | : 30  |     |
| LLDP Hold     | Time Multiplier | : 4   |     |
| LLDP Transmit | Delay Interval  | : 2   |     |
| LLDP Reinit   | Timer Interval  | : 2   |     |
| LLDP Trap     | Enabled         | : No  |     |
| LLDP Port     | Configuration   |       |     |
=======================
| PORT | TX-ENABLED | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 | Yes | Yes | Yes |
| ----- | --- | --- | --- |
DisplayingLLDPConfigurationforthemanagementinterface:
| switch#     | show lldp configuration | mgmt |     |
| ----------- | ----------------------- | ---- | --- |
| LLDP Global | Configuration           |      |     |
=========================
| LLDP Enabled  |                 | : Yes |     |
| ------------- | --------------- | ----- | --- |
| LLDP Transmit | Interval        | : 30  |     |
| LLDP Hold     | Time Multiplier | : 4   |     |
| LLDP Transmit | Delay Interval  | : 2   |     |
| LLDP Reinit   | Timer Interval  | : 2   |     |
| LLDP Trap     | Enabled         | : Yes |     |
| LLDP Port     | Configuration   |       |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 180

=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt           |             | Yes     |         |     | Yes          | Yes |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Command        | History     |         |         |     |              |     |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show lldp | configuration |     |                            |     |     |     |
| --------- | ------------- | --- | -------------------------- | --- | --- | --- |
| show lldp | configuration |     | [<INTERFACE-ID>][vsx-peer] |     |     |     |
Description
ShowsLLDPconfigurationsettingsforallinterfacesoraspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingconfigurationsettingsforallinterfaces:
| switch# | show   | lldp          | configuration |     |     |     |
| ------- | ------ | ------------- | ------------- | --- | --- | --- |
| LLDP    | Global | Configuration |               |     |     |     |
=========================
| LLDP | Enabled    |                 |          | : No |     |     |
| ---- | ---------- | --------------- | -------- | ---- | --- | --- |
| LLDP | Transmit   | Interval        |          | : 30 |     |     |
| LLDP | Hold       | Time Multiplier |          | : 4  |     |     |
| LLDP | Transmit   | Delay           | Interval | : 2  |     |     |
| LLDP | Reinit     | Timer           | Interval | : 2  |     |     |
| LLDP | Trap       | Enabled         |          | : No |     |     |
| TLVs | Advertised |                 |          |      |     |     |
===============
| Management |             | Address |     |     |     |     |
| ---------- | ----------- | ------- | --- | --- | --- | --- |
| Port       | Description |         |     |     |     |     |
| Port       | VLAN-ID     |         |     |     |     |     |
Devicediscoveryandconfiguration|181

| System | Description |               |     |     |     |     |
| ------ | ----------- | ------------- | --- | --- | --- | --- |
| System | Name        |               |     |     |     |     |
| LLDP   | Port        | Configuration |     |     |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 |     | Yes |     |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     | Yes |     |     | Yes | Yes |
| 1/1/3 |     | Yes |     |     | Yes | Yes |
| 1/1/4 |     | Yes |     |     | Yes | Yes |
| 1/1/5 |     | Yes |     |     | Yes | Yes |
| 1/1/6 |     | Yes |     |     | Yes | Yes |
...........
...........
| mgmt |     | Yes |     |     | Yes | Yes |
| ---- | --- | --- | --- | --- | --- | --- |
Thisexampleshowsconfigurationsettingsforinterface1/1/1.
| switch# |        | show lldp     | configuration |     | 1/1/1 |     |
| ------- | ------ | ------------- | ------------- | --- | ----- | --- |
| LLDP    | Global | Configuration |               |     |       |     |
=========================
| LLDP | Enabled  |                 |          | :   | Yes |     |
| ---- | -------- | --------------- | -------- | --- | --- | --- |
| LLDP | Transmit | Interval        |          | :   | 30  |     |
| LLDP | Hold     | Time Multiplier |          | :   | 4   |     |
| LLDP | Transmit | Delay           | Interval | :   | 2   |     |
| LLDP | Reinit   | Timer           | Interval | :   | 2   |     |
| LLDP | Trap     | Enabled         |          | :   | No  |     |
| LLDP | Port     | Configuration   |          |     |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1          |             | Yes     |         |     | Yes          | Yes |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Command        | History     |         |         |     |              |     |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | configuration |     | mgmt |     |     |     |
| --------- | ------------- | --- | ---- | --- | --- | --- |
| show lldp | configuration |     | mgmt |     |     |     |
Description
ShowsLLDPconfigurationsettingsfortheOOBMinterface.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 182

Example
Showingconfigurationsettingsforallinterfaces:
switch#
|      | show   | lldp configuration |     |     | mgmt |     |
| ---- | ------ | ------------------ | --- | --- | ---- | --- |
| LLDP | Global | Configuration      |     |     |      |     |
=========================
| LLDP | Enabled            |                |          | :   | Yes |     |
| ---- | ------------------ | -------------- | -------- | --- | --- | --- |
| LLDP | Transmit           | Interval       |          | :   | 30  |     |
| LLDP | Hold Time          | Multiplier     |          | :   | 4   |     |
| LLDP | Transmit           | Delay          | Interval | :   | 2   |     |
| LLDP | Reinit             | Timer Interval |          | :   | 2   |     |
| LLDP | Trap Enabled       |                |          | :   | Yes |     |
| LLDP | Port Configuration |                |          |     |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt           |             | Yes     |         |     | Yes          | Yes |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Command        | History     |         |         |     |              |     |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | local-device           |     |     |     |     |     |
| --------- | ---------------------- | --- | --- | --- | --- | --- |
| show lldp | local-device[vsx-peer] |     |     |     |     |     |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsare
configuredonanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDson
accessinterfaces.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingglobalLLDPinformationonly(allportsincludingOOBMportareadministrativelydown):
Devicediscoveryandconfiguration|183

| switch# | show lldp | local-device |     |
| ------- | --------- | ------------ | --- |
Global Data
===========
| Chassis-ID   |             | : 1c:98:ec:e3:45:00 |                            |
| ------------ | ----------- | ------------------- | -------------------------- |
| System       | Name        | : switch            |                            |
| System       | Description | : Aruba             | JL375A 8400X XL.01.01.0001 |
| Management   | Address     | : 192.168.10.1      |                            |
| Capabilities | Available   | : Bridge,           | Router                     |
| Capabilities | Enabled     | : Bridge,           | Router                     |
| TTL          |             | : 120               |                            |
Showingallportsexcept1/1/11andOOBMasadministrativelydown:
| switch# | show lldp | local-device |     |
| ------- | --------- | ------------ | --- |
Global Data
===========
| Chassis-ID   |             | : 1c:98:ec:e3:45:00 |        |
| ------------ | ----------- | ------------------- | ------ |
| System       | Name        | : switch            |        |
| System       | Description | : Aruba             |        |
| Management   | Address     | : 192.168.10.1      |        |
| Capabilities | Available   | : Bridge,           | Router |
| Capabilities | Enabled     | : Bridge,           | Router |
| TTL          |             | : 120               |        |
| Port Based   | Data        |                     |        |
===============
| Port-ID           |     | : 1/1/11         |     |
| ----------------- | --- | ---------------- | --- |
| Port-Desc         |     | : "1/1/11"       |     |
| Port Mgmt-Address |     | : 164.254.21.220 |     |
| Port VLAN         | ID  | : 0              |     |
| Port-ID           |     | : mgmt           |     |
| Port-Desc         |     | : "mgmt"         |     |
| Port Mgmt-Address |     | : 164.254.21.220 |     |
Inthisexample,alltheportsexcept1/1/11areadministrativelydown,andVLANID100isconfiguredon
thisaccessinterface.
| switch# | show lldp | local-device |     |
| ------- | --------- | ------------ | --- |
Global Data
===========
| Chassis-ID   |             | : 1c:98:ec:e3:45:00 |        |
| ------------ | ----------- | ------------------- | ------ |
| System       | Name        | : switch            |        |
| System       | Description | : Aruba             |        |
| Management   | Address     | : 192.168.10.1      |        |
| Capabilities | Available   | : Bridge,           | Router |
| Capabilities | Enabled     | : Bridge,           | Router |
| TTL          |             | : 120               |        |
| Port Based   | Data        |                     |        |
===============
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 184

| Port-ID        |             |         | : 1/1/11    |              |     |     |
| -------------- | ----------- | ------- | ----------- | ------------ | --- | --- |
| Port-Desc      |             |         | : "1/1/11"  |              |     |     |
| Port           | VLAN        | ID      | : 100       |              |     |     |
| Parent         | Interface   |         | : interface | 1/1/11       |     |     |
| Command        | History     |         |             |              |     |     |
| Release        |             |         |             | Modification |     |     |
| 10.07orearlier |             |         |             | --           |     |     |
| Command        | Information |         |             |              |     |     |
| Platforms      |             | Command | context     | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     |                              |     |     |     |
| --------- | ------------- | --- | ---------------------------- | --- | --- | --- |
| show lldp | neighbor-info |     | [<INTERFACE-NAME>][vsx-peer] |     |     |     |
Description
Displaysinformationaboutneighboringdevicesforallinterfacesorforaspecificinterface.The
informationdisplayedvariesdependingonthetypeofneighborconnectedandthetypeofTLVssentby
theneighbor.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-NAME> Specifiestheinterfaceforwhichtoshowinformationfor
neighboringdevices.Usetheformatmember/slot/port(for
example,1/3/1).
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingLLDPinformationforallinterfaces:
| switch# |          | show lldp   | neighbor-info |     |     |     |
| ------- | -------- | ----------- | ------------- | --- | --- | --- |
| LLDP    | Neighbor | Information |               |     |     |     |
=========================
| Total      | Neighbor |            | Entries          | : 3     |           |              |
| ---------- | -------- | ---------- | ---------------- | ------- | --------- | ------------ |
| Total      | Neighbor |            | Entries Deleted  | : 0     |           |              |
| Total      | Neighbor |            | Entries Dropped  | : 0     |           |              |
| Total      | Neighbor |            | Entries Aged-Out | : 0     |           |              |
| LOCAL-PORT |          | CHASSIS-ID |                  | PORT-ID | PORT-DESC | TTL SYS-NAME |
Devicediscoveryandconfiguration|185

--------------------------------------------------------------------------------
| 1/1/1  | 70:72:cf:a4:7d:50 |     | 1/1/1  | 1/1/1  | 32 switch  |
| ------ | ----------------- | --- | ------ | ------ | ---------- |
| 1/1/2  | 48:0f:cf:af:73:80 |     | 1/1/2  | 1/1/2  | 120 switch |
| 1/1/46 | 48:0f:cf:af:73:80 |     | 1/1/46 | 1/1/46 | 120 switch |
| mgmt   | 48:0f:cf:af:73:80 |     | mgmt   | mgmt   | 120 switch |
Showinginformationforinterface1/3/1whenithasonlyoneswitchconnectedasaneighbor:
| switch#  | show lldp    | neighbor-info | 1/3/1                  |     |     |
| -------- | ------------ | ------------- | ---------------------- | --- | --- |
| Port     |              |               | : 1/1/1                |     |     |
| Neighbor | Entries      |               | : 1                    |     |     |
| Neighbor | Entries      | Deleted       | : 0                    |     |     |
| Neighbor | Entries      | Dropped       | : 0                    |     |     |
| Neighbor | Entries      | Aged-Out      | : 0                    |     |     |
| Neighbor | Chassis-Name |               | : HP-3800-24G-PoEP-2XG |     |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor | Chassis-ID         |           | : 10:60:4b:39:3e:80 |        |     |
| -------- | ------------------ | --------- | ------------------- | ------ | --- |
| Neighbor | Management-Address |           | : 192.168.1.1       |        |     |
| Chassis  | Capabilities       | Available | : Bridge,           | Router |     |
| Chassis  | Capabilities       | Enabled   | : Bridge            |        |     |
| Neighbor | Port-ID            |           | : 1/1/1             |        |     |
| Neighbor | Port-Desc          |           | : 1/1/1             |        |     |
| Neighbor | Port               | VLAN ID   | :                   |        |     |
| TTL      |                    |           | : 120               |        |     |
Showinginformationforinterface1/3/10whentheneighborsendsaDOT3powerTLV:
| switch#  | show lldp    | neighbor-info | 1/3/10              |     |     |
| -------- | ------------ | ------------- | ------------------- | --- | --- |
| Port     |              |               | : 1/3/10            |     |     |
| Neighbor | Entries      |               | : 1                 |     |     |
| Neighbor | Entries      | Deleted       | : 0                 |     |     |
| Neighbor | Entries      | Dropped       | : 0                 |     |     |
| Neighbor | Entries      | Aged-Out      | : 0                 |     |     |
| Neighbor | Chassis-Name |               | : 84:d4:7e:ce:5d:68 |     |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor      | Chassis-ID         |              | : 84:d4:7e:ce:5d:68 |      |     |
| ------------- | ------------------ | ------------ | ------------------- | ---- | --- |
| Neighbor      | Management-Address |              | : 169.254.41.250    |      |     |
| Chassis       | Capabilities       | Available    | : Bridge,           | WLAN |     |
| Chassis       | Capabilities       | Enabled      | : WLAN              |      |     |
| Neighbor      | Port-ID            |              | : 84:d4:7e:ce:5d:68 |      |     |
| Neighbor      | Port-Desc          |              | : eth0              |      |     |
| TTL           |                    |              | : 120               |      |     |
| Neighbor      | Port               | VLAN ID      | :                   |      |     |
| Neighbor      | PoE information    |              | : DOT3              |      |     |
| Neighbor      | Power              | Type         | : TYPE2             | PD   |     |
| Neighbor      | Power              | Priority     | : Unkown            |      |     |
| Neighbor      | Power              | Source       | : Primary           |      |     |
| PD Requested  | Power              | Value        | : 25.0              | W    |     |
| PSE Allocated |                    | Power Value: | 25.0 W              |      |     |
| Neighbor      | Power              | Supported    | : Yes               |      |     |
| Neighbor      | Power              | Enabled      | : Yes               |      |     |
| Neighbor      | Power              | Class        | : 5                 |      |     |
| Neighbor      | Power              | Paircontrol  | : No                |      |     |
| PSE Power     | Pairs              |              | : Signal            |      |     |
Showinginformationforinterface1/1/1whenithasmultipleneighbors(displaysamaximumoffour):
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 186

| switch# show | lldp             | neighbor-info | 1/1/1    |     |
| ------------ | ---------------- | ------------- | -------- | --- |
| Port         |                  |               | : 1/1/1  |     |
| Neighbor     | Entries          |               | : 4      |     |
| Neighbor     | Entries Deleted  |               | : 0      |     |
| Neighbor     | Entries Dropped  |               | : 0      |     |
| Neighbor     | Entries Aged-Out |               | : 0      |     |
| Neighbor     | Chassis-Name     |               | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor             | Chassis-ID         |           | : 1c:98:ec:fe:25:00 |        |
| -------------------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor             | Management-Address |           | : 10.1.1.2          |        |
| Chassis Capabilities |                    | Available | : Bridge,           | Router |
| Chassis Capabilities |                    | Enabled   | : Bridge,           | Router |
| Neighbor             | Port-ID            |           | : 1/1/1             |        |
| Neighbor             | Port-Desc          |           | : 1/1/1             |        |
| Neighbor             | Port VLAN          | ID        | :                   |        |
| TTL                  |                    |           | : 120               |        |
| Neighbor             | Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor             | Chassis-ID         |           | : 1c:98:ec:fe:25:01 |        |
| -------------------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor             | Management-Address |           | : 10.1.1.3          |        |
| Chassis Capabilities |                    | Available | : Bridge,           | Router |
| Chassis Capabilities |                    | Enabled   | : Bridge,           | Router |
| Neighbor             | Port-ID            |           | : 1/1/1             |        |
| Neighbor             | Port-Desc          |           | : 1/1/1             |        |
| Neighbor             | Port VLAN          | ID        | :                   |        |
| TTL                  |                    |           | : 120               |        |
| Neighbor             | Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor             | Chassis-ID         |           | : 1c:98:ec:fe:25:02 |        |
| -------------------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor             | Management-Address |           | : 10.1.1.4          |        |
| Chassis Capabilities |                    | Available | : Bridge,           | Router |
| Chassis Capabilities |                    | Enabled   | : Bridge,           | Router |
| Neighbor             | Port-ID            |           | : 1/1/1             |        |
| Neighbor             | Port-Desc          |           | : 1/1/1             |        |
| Neighbor             | Port VLAN          | ID        | : 50                |        |
| TTL                  |                    |           | : 120               |        |
| Neighbor             | Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor             | Chassis-ID         |           | : 1c:98:ec:fe:25:03 |        |
| -------------------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor             | Management-Address |           | : 10.1.1.5          |        |
| Chassis Capabilities |                    | Available | : Bridge,           | Router |
| Chassis Capabilities |                    | Enabled   | : Bridge,           | Router |
| Neighbor             | Port-ID            |           | : 1/1/1             |        |
| Neighbor             | Port-Desc          |           | : 1/1/1             |        |
| Neighbor             | Port VLAN          | ID        | : 100               |        |
| TTL                  |                    |           | : 120               |        |
| Command History      |                    |           |                     |        |
| Release              |                    |           | Modification        |        |
| 10.07orearlier       |                    |           | --                  |        |
| Command Information  |                    |           |                     |        |
| Platforms            | Command            | context   | Authority           |        |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Devicediscoveryandconfiguration|187

| show lldp | neighbor-info |     | detail |            |     |
| --------- | ------------- | --- | ------ | ---------- | --- |
| show lldp | neighbor-info |     | detail | [vsx-peer] |     |
Description
ShowsdetailedLLDPneighborinformationforallLLDPneighborconnectedinterfaces.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingdetailedLLDPinformationforallinterfaces:
| switch# | show     | lldp        | neighbor-info | detail |     |
| ------- | -------- | ----------- | ------------- | ------ | --- |
| LLDP    | Neighbor | Information |               |        |     |
=========================
| Total | Neighbor | Entries |          | : 6 |     |
| ----- | -------- | ------- | -------- | --- | --- |
| Total | Neighbor | Entries | Deleted  | : 2 |     |
| Total | Neighbor | Entries | Dropped  | : 0 |     |
| Total | Neighbor | Entries | Aged-Out | : 2 |     |
--------------------------------------------------------------------------------
| Port     |                     |      |           | : 1/1/1             |        |
| -------- | ------------------- | ---- | --------- | ------------------- | ------ |
| Neighbor | Entries             |      |           | : 1                 |        |
| Neighbor | Entries             |      | Deleted   | : 0                 |        |
| Neighbor | Entries             |      | Dropped   | : 0                 |        |
| Neighbor | Entries             |      | Aged-Out  | : 0                 |        |
| Neighbor | Chassis-Name        |      |           | : 6300              |        |
| Neighbor | Chassis-Description |      |           | : Aruba             | ...    |
| Neighbor | Chassis-ID          |      |           | : 38:11:17:1a:d5:00 |        |
| Neighbor | Management-Address  |      |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities        |      | Available | : Bridge,           | Router |
| Chassis  | Capabilities        |      | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID             |      |           | : 1/1/4             |        |
| Neighbor | Port-Desc           |      |           | : 1/1/4             |        |
| Neighbor | Port                | VLAN | ID        | : 1                 |        |
| TTL      |                     |      |           | : 120               |        |
| Neighbor | Mac-Phy             |      | details   |                     |        |
| Neighbor | Auto-neg            |      | Supported | : true              |        |
| Neighbor | Auto-Neg            |      | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor | MAU | type |     | : 1000 | BASETFD |
| -------- | --- | ---- | --- | ------ | ------- |
--------------------------------------------------------------------------------
| Port     |              |     |          | : 1/1/2 |     |
| -------- | ------------ | --- | -------- | ------- | --- |
| Neighbor | Entries      |     |          | : 1     |     |
| Neighbor | Entries      |     | Deleted  | : 0     |     |
| Neighbor | Entries      |     | Dropped  | : 0     |     |
| Neighbor | Entries      |     | Aged-Out | : 0     |     |
| Neighbor | Chassis-Name |     |          | : 6300  |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 188

| Neighbor Chassis-Description |           | : Aruba             | ...    |
| ---------------------------- | --------- | ------------------- | ------ |
| Neighbor Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis Capabilities         | Available | : Bridge,           | Router |
| Chassis Capabilities         | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID             |           | : 1/1/5             |        |
| Neighbor Port-Desc           |           | : 1/1/5             |        |
| Neighbor Port                | VLAN ID   | : 1                 |        |
| TTL                          |           | : 120               |        |
| Neighbor Mac-Phy             | details   |                     |        |
| Neighbor Auto-neg            | Supported | : true              |        |
| Neighbor Auto-Neg            | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor MAU | type | : 1000 | BASETFD |
| ------------ | ---- | ------ | ------- |
--------------------------------------------------------------------------------
| Port                         |           | : 1/1/3             |        |
| ---------------------------- | --------- | ------------------- | ------ |
| Neighbor Entries             |           | : 1                 |        |
| Neighbor Entries             | Deleted   | : 0                 |        |
| Neighbor Entries             | Dropped   | : 0                 |        |
| Neighbor Entries             | Aged-Out  | : 0                 |        |
| Neighbor Chassis-Name        |           | : 6300              |        |
| Neighbor Chassis-Description |           | : Aruba             | ...    |
| Neighbor Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis Capabilities         | Available | : Bridge,           | Router |
| Chassis Capabilities         | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID             |           | : 1/1/6             |        |
| Neighbor Port-Desc           |           | : 1/1/6             |        |
| Neighbor Port                | VLAN ID   | : 1                 |        |
| TTL                          |           | : 120               |        |
| Neighbor Mac-Phy             | details   |                     |        |
| Neighbor Auto-neg            | Supported | : true              |        |
| Neighbor Auto-Neg            | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor MAU | type | : 1000 | BASETFD |
| ------------ | ---- | ------ | ------- |
--------------------------------------------------------------------------------
| Port                         |           | : 1/1/46            |        |
| ---------------------------- | --------- | ------------------- | ------ |
| Neighbor Entries             |           | : 1                 |        |
| Neighbor Entries             | Deleted   | : 0                 |        |
| Neighbor Entries             | Dropped   | : 0                 |        |
| Neighbor Entries             | Aged-Out  | : 0                 |        |
| Neighbor Chassis-Name        |           | : 6300              |        |
| Neighbor Chassis-Description |           | : Aruba             | ...    |
| Neighbor Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis Capabilities         | Available | : Bridge,           | Router |
| Chassis Capabilities         | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID             |           | : 1/1/19            |        |
| Neighbor Port-Desc           |           | : 1/1/19            |        |
| Neighbor Port                | VLAN ID   | : 1                 |        |
| TTL                          |           | : 120               |        |
| Neighbor Mac-Phy             | details   |                     |        |
| Neighbor Auto-neg            | Supported | : true              |        |
| Neighbor Auto-Neg            | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
Devicediscoveryandconfiguration|189

| Neighbor |     | MAU type |     | : 1000 | BASETFD |
| -------- | --- | -------- | --- | ------ | ------- |
--------------------------------------------------------------------------------
| Port           |             |                     |          | : 1/1/47            |     |
| -------------- | ----------- | ------------------- | -------- | ------------------- | --- |
| Neighbor       |             | Entries             |          | : 1                 |     |
| Neighbor       |             | Entries             | Deleted  | : 0                 |     |
| Neighbor       |             | Entries             | Dropped  | : 0                 |     |
| Neighbor       |             | Entries             | Aged-Out | : 0                 |     |
| Neighbor       |             | Chassis-Name        |          | : 6300              |     |
| Neighbor       |             | Chassis-Description |          | : Aruba             | ... |
| Neighbor       |             | Chassis-ID          |          | : 38:11:17:1a:d5:00 |     |
| Neighbor       |             | Management-Address  |          | : 38:11:17:1a:d5:00 |     |
| Chassis        | Cap         |                     |          |                     |     |
| Command        | History     |                     |          |                     |     |
| Release        |             |                     |          | Modification        |     |
| 10.07orearlier |             |                     |          | --                  |     |
| Command        | Information |                     |          |                     |     |
| Platforms      |             | Command             | context  | Authority           |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     | mgmt |     |     |
| --------- | ------------- | --- | ---- | --- | --- |
| show lldp | neighbor-info |     | mgmt |     |     |
Description
DisplaysinformationaboutneighboringdevicesconnectedtotheOOBMinterface.
Examples
ShowingLLDPinformationfortheOOBMinterface:
| switch#  | show | lldp         | neighbor-info | mgmt                   |     |
| -------- | ---- | ------------ | ------------- | ---------------------- | --- |
| Port     |      |              |               | : mgmt                 |     |
| Neighbor |      | Entries      |               | : 1                    |     |
| Neighbor |      | Entries      | Deleted       | : 0                    |     |
| Neighbor |      | Entries      | Dropped       | : 0                    |     |
| Neighbor |      | Entries      | Aged-Out      | : 0                    |     |
| Neighbor |      | Chassis-Name |               | : HP-3800-24G-PoEP-2XG |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor |              | Chassis-ID         |           | : 10:60:4b:39:3e:80 |        |
| -------- | ------------ | ------------------ | --------- | ------------------- | ------ |
| Neighbor |              | Management-Address |           | : 192.168.1.1       |        |
| Chassis  | Capabilities |                    | Available | : Bridge,           | Router |
| Chassis  | Capabilities |                    | Enabled   | : Bridge            |        |
| Neighbor |              | Port-ID            |           | : mgmt              |        |
| Neighbor |              | Port-Desc          |           | : mgmt              |        |
| Neighbor |              | Port               | VLAN ID   | :                   |        |
| TTL      |              |                    |           | : 120               |        |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 190

ShowingLLDPinformationfortheOOBMinterfacewhentherearefourneighbors:
| switch# show          | lldp neighbor-info | mgmt     |     |
| --------------------- | ------------------ | -------- | --- |
| Port                  |                    | : mgmt   |     |
| Neighbor Entries      |                    | : 4      |     |
| Neighbor Entries      | Deleted            | : 0      |     |
| Neighbor Entries      | Dropped            | : 0      |     |
| Neighbor Entries      | Aged-Out           | : 0      |     |
| Neighbor Chassis-Name |                    | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:00 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.2          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| Neighbor Port               | VLAN ID   | :                   |        |
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:01 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.3          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| Neighbor Port               | VLAN ID   | :                   |        |
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:02 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.4          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| Neighbor Port               | VLAN ID   | :                   |        |
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:03 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.5          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| Neighbor Port               | VLAN ID   | :                   |        |
| TTL                         |           | : 120               |        |
| Command History             |           |                     |        |
| Release                     |           | Modification        |        |
| 10.07orearlier              |           | --                  |        |
| Command Information         |           |                     |        |
Devicediscoveryandconfiguration|191

| Platforms |     | Command | context |     | Authority |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | statistics |     |                            |     |     |     |     |
| --------- | ---------- | --- | -------------------------- | --- | --- | --- | --- |
| show lldp | statistics |     | [<INTERFACE-ID>][vsx-peer] |     |     |     |     |
Description
ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingglobalstatisticsforallinterfaces:
| switch# | show   | lldp       | statistics |     |     |     |     |
| ------- | ------ | ---------- | ---------- | --- | --- | --- | --- |
| LLDP    | Global | Statistics |            |     |     |     |     |
======================
| Total | Packets |              | Transmitted  |           | : 19 |     |     |
| ----- | ------- | ------------ | ------------ | --------- | ---- | --- | --- |
| Total | Packets |              | Received     |           | : 19 |     |     |
| Total | Packets |              | Received And | Discarded | : 0  |     |     |
| Total | TLVs    | Unrecognized |              |           | : 0  |     |     |
| LLDP  | Port    | Statistics   |              |           |      |     |     |
====================
| PORT-ID |     |     | TX-PACKETS | RX-PACKETS |     | RX-DISCARDED | TLVS-UNKNOWN |
| ------- | --- | --- | ---------- | ---------- | --- | ------------ | ------------ |
-------------------------------------------------------------------------
| 1/1/1 |     |     | 7   | 7   |     | 0   | 0   |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     |     | 7   | 7   |     | 0   | 0   |
| 1/1/3 |     |     | 0   | 0   |     | 0   | 0   |
| 1/1/4 |     |     | 0   | 0   |     | 0   | 0   |
| 1/1/5 |     |     | 0   | 0   |     | 0   | 0   |
...
| mgmt |     |     | 5   | 5   |     | 0   | 0   |
| ---- | --- | --- | --- | --- | --- | --- | --- |
```
Showingstatisticsforinterface1/1/1:
| switch# | show       | lldp | statistics | 1/1/1 |     |     |     |
| ------- | ---------- | ---- | ---------- | ----- | --- | --- | --- |
| LLDP    | Statistics |      |            |       |     |     |     |
===============
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 192

: 1/1/1
Port Name
: 159
Packets Transmitted
: 163
Packets Received
Packets Received And Discarded
: 0
Packets Received And Unrecognized : 0

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

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show lldp statistics mgmt

show lldp statistics mgmt

Description

Shows LLDP statistics for the OOBM interface.

Example

Showing LLDP statistics for the OOBM interface:

switch# show lldp statistics mgmt

LLDP Statistics
===============

Port Name
: mgmt
Packets Transmitted
: 20
Packets Received
: 23
: 0
Packets Received And Discarded
Packets Received And Unrecognized : 0

Command History

Release

10.07 or earlier

Command Information

Modification

--

Device discovery and configuration | 193

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp tlv           |     |     |     |
| ----------------------- | --- | --- | --- |
| show lldp tlv[vsx-peer] |     |     |     |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# show    | lldp tlv |     |     |
| --------------- | -------- | --- | --- |
| TLVs Advertised |          |     |     |
===============
| Management          | Address |         |              |
| ------------------- | ------- | ------- | ------------ |
| Port Description    |         |         |              |
| Port VLAN-ID        |         |         |              |
| System Capabilities |         |         |              |
| System Description  |         |         |              |
| System Name         |         |         |              |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| Cisco Discovery |     | Protocol | (CDP) |
| --------------- | --- | -------- | ----- |
CiscoDiscoveryProtocol(CDP)isaproprietarylayer2protocolsupportedbymostCiscodevices.Itis
usedtoexchangeinformation,suchassoftwareversion,devicecapabilities,andvoiceVLAN
information,betweendirectlyconnecteddevices,suchasaVoIPphoneandaswitch.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 194

CDP support

By default, CDP is enabled on each active switch port. This is a read-only capability, which means the
switch can receive and store information about adjacent CDP devices, but does not generate CDP
packets (except when communicating with Cisco IP phones.)

The switch supports CDPv2 only and does not support SNMP MIB traps.

When a CDP-enabled port receives a CDP packet from another CDP device, it enters data for that device
into the CDP Neighbors table, along with the port number on which the data was received. It does not
forward the packet. The switch also periodically purges the table of any entries that have expired. (The
holdtime for any data entry in the switch CDP Neighbors table is configured in the device transmitting
the CDP packet and cannot be controlled in the switch receiving the packet.) A switch reviews the list of
CDP neighbor entries every three seconds and purges any expired entries.

Support for legacy Cisco IP phones

Autoconfiguration of legacy Cisco IP phones for tagged voice VLAN support requires CDPv2.

On initial boot-up, and sometimes periodically, a Cisco phone queries the switch and advertises
information about itself using CDPv2. When the switch receives the VoIP VLAN Query TLV (type 0x0f)
from the phone, the switch immediately responds with the voice VLAN ID in a reply packet using the
VoIP VLAN Reply TLV (type 0x0e). This enables the Cisco phone to boot properly and send traffic on the
advertised voice VLAN ID.

The switch CDP packet includes these TLVs:

n CDP Version: 2

n CDP TTL: 180 seconds

n Checksum

n Capabilities (type 0x04): 0x0008 (is a switch)

n Native VLAN: The PVID of the port

n VoIP VLAN Reply (type 0xe): voice VLAN ID (same as advertised by LLDP-MED)

n Trust Bitmap (type 0x12): 0x00

n Untrusted port CoS (type 0x13): 0x00

CDP commands

cdp

cdp

Description

Configures CDP support globally on all active interfaces or on a specific interface. By default, CDP is
enabled on all active interfaces.

When CDP is enabled, the switch adds entries to its CDP Neighbors table for any CDP packets it receives
from neighboring CDP devices.

When CDP is disabled, the CDP Neighbors table is cleared and the switch drops all inbound CDP packets
without entering the data in the CDP Neighbors table.

The no form of this command disables CDP support globally on all active interfaces or on a specific
interface.

Examples

Enabling CDP globally:

Device discovery and configuration | 195

| switch(config)# | cdp |     |     |
| --------------- | --- | --- | --- |
DisablingCDPglobally:
| switch(config)# | no  | cdp |     |
| --------------- | --- | --- | --- |
EnablingCDPoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
| switch(config-if)# |           | cdp   |     |
DisablingCDPoninterface1/1/1:
| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|                     |         | no cdp  |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|                    | config-if |     | rightsforthiscommand. |
| ------------------ | --------- | --- | --------------------- |
| clear cdp counters |           |     |                       |
| clear cdp counters |           |     |                       |
Description
ClearsCDPcounters.
Examples
ClearingCDPcounters:
| switch(config)      | clear | cdp counters |              |
| ------------------- | ----- | ------------ | ------------ |
| Command History     |       |              |              |
| Release             |       |              | Modification |
| 10.07orearlier      |       |              | --           |
| Command Information |       |              |              |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 196

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear cdp neighbor-info |     |     |     |
| ----------------------- | --- | --- | --- |
| clear cdp neighbor-info |     |     |     |
Description
ClearsCDPneighborinformation.
Examples
ClearingCDPneighborinformation:
switch(config)
|                     | clear   | neighbor-info |              |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show cdp
show cdp
Description
ShowsCDPinformationforallinterfaces.
Examples
ShowingCDPinformation:
| switch(config)# | show        | cdp |     |
| --------------- | ----------- | --- | --- |
| CDP Global      | Information |     |     |
======================
| CDP      | : Enabled      |         |     |
| -------- | -------------- | ------- | --- |
| CDP Mode | : Rx           | only    |     |
| CDP Hold | Time : 180     | seconds |     |
| Port     | CDP            |         |     |
| -------- | -------------- |         |     |
| 1/1/1    | Enabled        |         |     |
| 1/1/2    | Enabled        |         |     |
| 1/1/3    | Enabled        |         |     |
| 1/1/4    | Enabled        |         |     |
Devicediscoveryandconfiguration|197

| 1/1/5          | Enabled     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| 1/1/6          | Enabled     |         |              |     |     |
| 1/1/7          | Enabled     |         |              |     |     |
| 1/1/8          | Enabled     |         |              |     |     |
| 1/1/9          | Enabled     |         |              |     |     |
| 1/1/10         | Enabled     |         |              |     |     |
| Command        | History     |         |              |     |     |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show cdp neighbor-info |     |                |     |     |     |
| ---------------------- | --- | -------------- | --- | --- | --- |
| show cdp neighbor-info |     | <INTERFACE-ID> |     |     |     |
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
Examples
ShowingallCDPneighborinformation:
| switch(config)# | show   | cdp neighbor-info |     |          |            |
| --------------- | ------ | ----------------- | --- | -------- | ---------- |
| Port            | Device | ID                |     | Platform | Capability |
-------------------------------------------------------------------------------
| 1/1/1 | myswitch |     |     | cisco WS-C2950-12 | SI  |
| ----- | -------- | --- | --- | ----------------- | --- |
ShowingCDPinformationforinterface1/1/1:
| switch(config)# | show    | cdp neighbor-info   |          | 1/1/1 |     |
| --------------- | ------- | ------------------- | -------- | ----- | --- |
| Local Port      | : 1/1/1 |                     |          |       |     |
| MAC             |         | : 3c:a8:2a:7b:6b:2b |          |       |     |
| Device ID       |         | : SEPd4adbd2a30d6   |          |       |     |
| Address         |         | : 2.71.0.230        |          |       |     |
| Platform        |         | : Cisco             | IP Phone | 3905  |     |
| Duplex          |         | : full              |          |       |     |
| Capability      |         | : host              |          |       |     |
| Voice VLAN      | Support | : Yes               |          |       |     |
| Neighbor        | Port-ID | : Port 1            |          |       |     |
| Command         | History |                     |          |       |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 198

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show cdp traffic |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
show cdp neighbor-info
Description
ShowsCDPstatisticsforeachinterface.
Examples
ShowingCDPtrafficstatistics:
| switch(config)# | show | cdp traffic |     |     |     |
| --------------- | ---- | ----------- | --- | --- | --- |
CDP Statistics
====================
| Port | Transmitted | Frames | Received Frames | Discarded | Frames |
| ---- | ----------- | ------ | --------------- | --------- | ------ |
--------------------------------------------------------------------------------
| 1/1/1               | 0       |         | 4            | 0   |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 1/1/2               | 0       |         | 0            | 0   |     |
| 1/1/3               | 0       |         | 2            | 0   |     |
| 1/1/4               | 0       |         | 0            | 0   |     |
| 1/1/5               | 0       |         | 0            | 0   |     |
| Command History     |         |         |              |     |     |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Devicediscoveryandconfiguration|199

Chapter 12

Zero Touch Provisioning

Zero Touch Provisioning

Zero Touch Provisioning (ZTP) enables the auto-configuration of factory default switches without a
network administrator onsite.

When a switch is booted from its factory default configuration, ZTP autoprovisions the switch by
automatically downloading and installing a firmware file, a configuration file, or both. With ZTP, even a
nontechnical user (for example: a store manager in a retail chain or a teacher in a school) can deploy
devices at a site.

ZTP support

The switch supports standards-based Zero Touch Provisioning (ZTP) operations as follows:

n The switch must be running the factory default configuration.

n The switch can connect to the DHCP server from the OOBM management port.

n ZTP operations are supported over IPv4 connections only. IPv6 connections are not supported for

ZTP operations.

n You must configure the DHCP server to provide a standards-based ZTP server solution. Options and
features that are specific to Network Management Solution (NMS) tools, such as AirWave, are not
supported.

o Aruba Central on-premise can manage AOS-CX switches on supported models through DHCP ZTP

using two approaches:

l On the DHCP server, configure DHCP option-60 as "ArubaInstantAP" 90 and provide the value
in option-43 in the format <group-details>, <aruba-central-on-prem-ip-or-fqdn>, <shared-token>.

l On the DHCP server, configure DHCP option-60 as HPE vendor VCI and provide the value in

option-43 in the tag-length-value (TLV) format. Next, enter the Aruba Central on-premise fully
qualified domain name (FQDN) or IPv4 address as the value for sub-option code 146 using the
format: <group-details>, <aruba-central-on-prem-ip-or-fqdn>, <shared-token>.

o Supported DHCP options are:

DHCP option

43

43 suboption 144

43 suboption 145

Description

Vendor Specific Information

Name of the configuration file

Name of the firmware image file

43 suboption 146

FQDN or IPv4 address of the Aruba Central on-premise server

43 suboption 148

FQDN or IPv4 address of the HTTP Proxy

60

Vendor Class Identifier (VCI)

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

200

DHCP option

Description

66

67

IPv4 address of the TFTP server (Specifying a host name instead
of an IP address is not supported.)

Name of the configuration file (Option 43 suboption 144 takes
precedence over this option.)

n The configuration file is a text file or JSON file that becomes the startup and running configuration on
the switch after the ZTP operation is complete. The configuration can be in CLI or in JSON format.

n When the switch is started using the factory default configuration, the ZTP operation is started

automatically and is active until any running configuration of the switch is modified. There is no CLI
command required to start the operation.

The switch supports the following standards:

n RFC 2131, Dynamic Host Configuration Protocol.

n RFC 2132, DHCP Options and BOOTP Vendor Extensions. Support is limited to the options listed in the

table "Supported DHCP options for ZTP on AOS-CX."

Hewlett Packard Enterprise recommends that you implement ZTP in a secure and private environment.
Any public access can compromise the security of the switch, as follows:

n ZTP is enabled only in the factory default configuration of the switch, DHCP snooping is not enabled.

The Rogue DHCP server must be manually managed.

n The DHCP offer is in plain data without encryption.

Setting up ZTP on a trusted network

The following procedure is an overview of setting up a Zero Touch Provisioning (ZTP) environment to
provision newly installed switches automatically. The procedure is intended for network administrators
who are familiar with automatically provisioning switches in a network, and does not provide detailed
information about configuring or managing switches.

Procedure

1. For each switch model to be provisioned using ZTP, do the following:

a. Obtain the switch firmware image file.
b. Prepare the switch configuration file. The configuration file becomes the running

configuration and the startup configuration on the switch.

2. Set up a TFTP server and record its IP address. The address is required when you set up the DHCP
server. The switch must be able to reach the TFTP server and DHCP server, either on the same
subnet, or on a remote subnet via DHCP relay.

For switches that do not support ZTP connections through a data port, use the management port
and management network.

3. Publish the configuration files and image files to the TFTP server. You need to know the locations
of the files and the IP address of the TFTP server when you set up the vendor class options on the
DHCP server.

4. On the DHCP server, set up vendor classes for each switch model you plan to provision. To do

this you need the following information:

Zero Touch Provisioning | 201

n The IP address of the TFTP server. Using a host name is not supported.

n The path to the switch configuration and firmware image files on the TFTP server.

n The vendor class identifier (VCI) for each switch model.

You can obtain the VCI by entering the show dhcp client vendor-class-identifier command
from a switch CLI command prompt in the manager context. The VCI is the text string in the
response that starts with Aruba.

For example:

switch# show dhcp client vendor-class-identifier
Vendor Class Identifier: Aruba xxxxx xxxx

Where x indicates the switch model number.

5. At the installation site, provide the switch installer with a Cat6 network cable connected to the

network that includes the DHCP and TFTP servers, and information about the switch port to use.
The switch installer plugs the cable into the data port you specify.

The ZTP operation begins when power is applied to the switch after the network cable is installed.

6. Assuming the downloaded configuration includes a way to access the CLI of the switch, you can
enter the following command to show the options offered by the DHCP server and the status of
the ZTP operation:
show ztp information

ZTP process during switch boot

1. The switch boots up with the factory default configuration.

If the ZTP operation detects that the switch configuration is different from the factory default
configuration, the ZTP operation ends. The switch must be configured at the installation site.

2. The switch sends out a DHCP discovery from the management port.

The switch waits to receive DHCP options indefinitely or until the running configuration is
modified. If a DHCP IP address is received but no DHCP options are received, the switch waits an
additional minute before ending the ZTP operation.

After the ZTP operation ends, there is no automatic retry. You can either attempt to boot the
switch with the factory default configuration again, configure the switch at the installation site, or
use the ZTP force-provision CLI to trigger the ZTP process, ignoring the present running
configuration of the switch.

n Once force-provision is enabled, new DHCP requests are sent from the switch. Disabling force-

provision does not stop the DHCP already in progress, but only changes the switch
configuration status of force-provision.

n If ZTP fails while force-provision is enabled, there is no automatic retry. To retry, ztp force-
provision should be disabled and re-enabled to clear the current ZTP state and send a new
DHCP request. When ztp force-provision is already enabled on the switch, re-enabling it
results in no operation.

n If the DHCP server is configured to provide both ZTP image and configuration options and
there is a non-default startup configuration present on the switch, clearing the non-default
startup configuration before triggering ztp force-provision is recommended. If an image is
downloaded via ZTP, the switch reboots once the image download is complete and ZTP force-

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

202

provision configuration is lost, causing ZTP to enter into a failed state. ZTP force-provision will
need to be enabled again to continue the process.

3. The DHCP server responds with an offer containing the following:

n The IPv4 address of the TFTP server

n One or both of the following:

o The name of the firmware image file

o The name of the configuration file

n Aruba Central Location (optional) including the shared token value for the on-premise server

n HTTP Proxy Location (optional)

4.

If a firmware image file is offered, the ZTP operation downloads the image file from the TFTP
server to the switch. If the current switch image and downloaded firmware image version do not
match, then the switch boots with the downloaded image:
n If the image upgrade fails, the switch retains its original firmware image and the ZTP operation

ends with a failed status.

n If the image upgrade succeeds, the ZTP operation is started again after the switch reboots.
Because the downloaded image file matches the image file installed on the switch, the ZTP
operation continues, and checks if a configuration file is offered.

5.

If a configuration file is offered, the ZTP operation downloads the configuration file copies the file
to the running-config and then to the startup-config of the switch:
n If the startup configuration update fails, the switch retains its factory-default running

configuration and the ZTP operation ends with a failed status.

o If the copy operation fails, the ZTP operation ends with a failed status.

o If the copy operation succeeds, the ZTP operation ends successfully.

ZTP VSF switchover support

ZTP status is not synced in the VSF stack. When the VSF stack is formed, configuration changes are
applied on the conductor switch, which is then synced to standby switch. When the switchover is
performed on the VSF stack, the standby becomes the new conductor switch.

As part of the switchover process, the ZTP daemon starts on the new conductor. The status of the ZTP is
failed because there are configuration changes present.

ZTP commands

show ztp information
show ztp information

Description

Shows information about Zero Touch Provisioning (ZTP) operations performed on the switch.

Usage

When a switch configured to use ZTP is booted from a factory default configuration, the switch contacts
a DHCP server, which offers options for obtaining files used to provision the switch:

Zero Touch Provisioning | 203

n TheIPaddressoftheTFTPserver
n Thenameoftheimagefile
Thenameoftheconfigurationfile
n
Theshow ztp informationcommandshowstheoptionsofferedbytheDHCPserverandthestatusof
theZTPoperation.
ThestatusoftheZTPoperationisoneofthefollowing:
Success
TheZTPoperationsucceeded.
Oneofthefollowingistrue:
n Boththerunningconfigurationandthestartupconfigurationwereupdated.
n TheIPaddressoftheTFTPserverwasreceived,buttheofferdidnotincludeaconfigurationfileora
firmwareimagefile.
n AnycombinationofvendorencapsulatedDHCPoptionsarereceivedasconfigured,alongwiththe
firmwareimageandswitchconfigurationfile.
n OnlyvendorencapsulatedDHCPoptionsareconfiguredandarereceivedaccordingly.
| Failed - Custom |     | startup | configuration |     | detected |     |     |     |
| --------------- | --- | ------- | ------------- | --- | -------- | --- | --- | --- |
Theswitchwasbootedfromaconfigurationthatisnotthefactorydefaultconfiguration.Forexample,
theadministratorpasswordhasbeenset.
| Failed - Timed | out | while | waiting | to  | receive ZTP | options |     |     |
| -------------- | --- | ----- | ------- | --- | ----------- | ------- | --- | --- |
EithertheswitchreceivedtheDHCPIPv4addressbutnoZTPoptionswerereceivedwithin1minuteor
ZTPforce-provisionistriggeredandnoZTPoptionsarereceivedwithin3minutes.
| Failed - Detected |     | change | in running |     | configuration |     |     |     |
| ----------------- | --- | ------ | ---------- | --- | ------------- | --- | --- | --- |
TherunningconfigurationwasmodifiedbyauserwhiletheZTPoperationwasinprogress.
| Failed - TFTP | server | unreachable |     |     |     |     |     |     |
| ------------- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
TheTFTPserverisnotreachableatthespecifiedIPaddress.
| Failed - TFTP | server | information |     | unavailable |     |     |     |     |
| ------------- | ------ | ----------- | --- | ----------- | --- | --- | --- | --- |
TheimagefilenameorconfigfilenameisprovidedwithouttheTFTPserverlocationtofetchthefiles
fromandZTPentersfailedstate.
| Failed - Invalid |     | configuration |     | file received |     |     |     |     |
| ---------------- | --- | ------------- | --- | ------------- | --- | --- | --- | --- |
Eitherthefiletransferoftheconfigurationfilefailed,ortheconfigurationfileisinvalid(anerror
occurredwhileattemptingtoapplytheconfiguration).
| Failed - Invalid |     | image | file received |     |     |     |     |     |
| ---------------- | --- | ----- | ------------- | --- | --- | --- | --- | --- |
Eitherthefiletransferofthefirmwareimagefilefailed,orthefirmwareimagefileisinvalid(anerror
occurredwhileverifyingtheimage).
Examples
ShowingswitchimagedownloadinprogressafterreceivingZTP options:
| switch#       | show    | ztp      | information |     |                            |     |                  |                  |
| ------------- | ------- | -------- | ----------- | --- | -------------------------- | --- | ---------------- | ---------------- |
| TFTP          | Server  |          |             |     | : 10.0.0.2                 |     |                  |                  |
| Image         | File    |          |             |     | : TL_10_02_0001.swi        |     |                  |                  |
| Configuration |         | File     |             |     | : config_file              |     |                  |                  |
| ZTP Status    |         |          |             |     | : In-progress              |     | - Image download | and verification |
| Aruba         | Central | Location |             |     | : secure.arubanetworks.com |     |                  |                  |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 204

| Aruba Central   | Shared Token | : aruba123                     |     |     |
| --------------- | ------------ | ------------------------------ | --- | --- |
| Force-Provision |              | : Disabled                     |     |     |
| HTTP Proxy      | Location     | : http.proxy.arubanetworks.com |     |     |
ShowingswitchimagedownloadfailureafterreceivingZTPoptions:
| switch#         | show ztp information |                                |          |                   |
| --------------- | -------------------- | ------------------------------ | -------- | ----------------- |
| TFTP Server     |                      | : 10.0.0.2                     |          |                   |
| Image File      |                      | : TL_10_02_0001.swi            |          |                   |
| Configuration   | File                 | : config_file                  |          |                   |
| ZTP Status      |                      | : Failed                       | - Unable | to download image |
| Aruba Central   | Location             | : secure.arubanetworks.com     |          |                   |
| Aruba Central   | Shared Token         | : aruba123                     |          |                   |
| Force-Provision |                      | : Disabled                     |          |                   |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |          |                   |
ShowingswitchconfigurationdownloadinprogressafterreceivingZTPoptions:
| switch#         | show ztp information |                                |                 |          |
| --------------- | -------------------- | ------------------------------ | --------------- | -------- |
| TFTP Server     |                      | : 10.0.0.2                     |                 |          |
| Image File      |                      | : TL_10_02_0001.swi            |                 |          |
| Configuration   | File                 | : config_file                  |                 |          |
| ZTP Status      |                      | : In-progress                  | - Configuration | download |
| Aruba Central   | Location             | : secure.arubanetworks.com     |                 |          |
| Aruba Central   | Shared Token         | : aruba123                     |                 |          |
| Force-Provision |                      | : Disabled                     |                 |          |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |                 |          |
ShowingswitchconfigurationdownloadfailureafterreceivingZTPoptions:
| switch#         | show ztp information |                                |          |                           |
| --------------- | -------------------- | ------------------------------ | -------- | ------------------------- |
| TFTP Server     |                      | : 10.0.0.2                     |          |                           |
| Image File      |                      | : TL_10_02_0001.swi            |          |                           |
| Configuration   | File                 | : config_file                  |          |                           |
| ZTP Status      |                      | : Failed                       | - Unable | to download configuration |
| Aruba Central   | Location             | : secure.arubanetworks.com     |          |                           |
| Aruba Central   | Shared Token         | : aruba123                     |          |                           |
| Force-Provision |                      | : Disabled                     |          |                           |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |          |                           |
Showingswitchfailuretoupdatestart-upconfrigurationafterdownloadingconfigurationreceivedfrom
ZTPoptions:
| switch#       | show ztp information |                     |     |     |
| ------------- | -------------------- | ------------------- | --- | --- |
| TFTP Server   |                      | : 10.0.0.2          |     |     |
| Image File    |                      | : TL_10_02_0001.swi |     |     |
| Configuration | File                 | : config_file       |     |     |
ZTP Status : Failed - Could not copy to start-up configuration
| Aruba Central   | Location     | : secure.arubanetworks.com     |     |     |
| --------------- | ------------ | ------------------------------ | --- | --- |
| Aruba Central   | Shared Token | : aruba123                     |     |     |
| Force-Provision |              | : Disabled                     |     |     |
| HTTP Proxy      | Location     | : http.proxy.arubanetworks.com |     |     |
ZeroTouchProvisioning|205

Inthefollowingexample,theZTPoperationsucceeded,andbothanimagefileandaconfigurationfile
wereprovided.
| VSF-10-Mbr#     | show ztp information |                                       |     |     |
| --------------- | -------------------- | ------------------------------------- | --- | --- |
| TFTP Server     |                      | : 10.1.84.160                         |     |     |
| Image File      |                      | : FL_10_06_0001CK.swi                 |     |     |
| Configuration   | File                 | : 102720-new-setup-config-updated.txt |     |     |
| Status          |                      | : Success                             |     |     |
| Aruba Central   | Location             | : NA                                  |     |     |
| Aruba Central   | Shared Token         | : aruba123                            |     |     |
| Force-Provision |                      | : Disabled                            |     |     |
| HTTP Proxy      | Location             | : NA                                  |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoptionsucceeded.Aconfigurationfilewasnotprovided,butanimage
filewasprovided.
VSF-10-Mbr#
show ztp information
| TFTP Server     |              | : 10.1.84.160       |     |     |
| --------------- | ------------ | ------------------- | --- | --- |
| Image File      |              | : TL_10_02_0001.swi |     |     |
| Configuration   | File         | : NA                |     |     |
| Status          |              | : Success           |     |     |
| Aruba Central   | Location     | : NA                |     |     |
| Aruba Central   | Shared Token | : aruba123          |     |     |
| Force-Provision |              | : Disabled          |     |     |
| HTTP Proxy      | Location     | : NA                |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationfailedbecausetheTFTPserverwasunreachable.
| VSF-10-Mbr#     | show ztp information |                                       |               |             |
| --------------- | -------------------- | ------------------------------------- | ------------- | ----------- |
| TFTP Server     |                      | : 10.1.84.160                         |               |             |
| Image File      |                      | : TL_10_02_0001.swi                   |               |             |
| Configuration   | File                 | : 102720-new-setup-config-updated.txt |               |             |
| Status          |                      | : Failed                              | - TFTP server | unreachable |
| Aruba Central   | Location             | : NA                                  |               |             |
| Aruba Central   | Shared Token         | : NA                                  |               |             |
| Force-Provision |                      | : Disabled                            |               |             |
| HTTP Proxy      | Location             | : NA                                  |               |             |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchdidnotreceiveanyoptions
fromtheDHCPserverforZTPwithin1minuteofreceivingtheIPaddressfromtheserver.
| VSF-10-Mbr##  | show ztp information |      |     |     |
| ------------- | -------------------- | ---- | --- | --- |
| TFTP Server   |                      | : NA |     |     |
| Image File    |                      | : NA |     |     |
| Configuration | File                 | : NA |     |     |
Status : Failed - Timed out while waiting to receive ZTP options
| Aruba Central   | Location     | : NA       |     |     |
| --------------- | ------------ | ---------- | --- | --- |
| Aruba Central   | Shared Token | : NA       |     |     |
| Force-Provision |              | : Disabled |     |     |
| HTTP Proxy      | Location     | : NA       |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchwasbootedfroma
configurationthatwasnotthefactorydefaultconfiguration.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 206

| switch#         | show ztp information |         |                           |               |          |
| --------------- | -------------------- | ------- | ------------------------- | ------------- | -------- |
| TFTP Server     |                      |         | : 10.0.0.2                |               |          |
| Image File      |                      |         | : TL_10_02_0001.swi       |               |          |
| Configuration   | File                 |         | : ztp.cfg                 |               |          |
| Status          |                      |         | : Failed - Custom startup | configuration | detected |
| Aruba Central   | Location             |         | : NA                      |               |          |
| Aruba Central   | Shared               | Token   | : NA                      |               |          |
| Force-Provision |                      |         | : Disabled                |               |          |
| HTTP Proxy      | Location             |         | : NA                      |               |          |
| Command         | History              |         |                           |               |          |
| Release         |                      |         | Modification              |               |          |
| 10.07orearlier  |                      |         | --                        |               |          |
| Command         | Information          |         |                           |               |          |
| Platforms       | Command              | context | Authority                 |               |          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| ztp force | provision |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
ztp force-provision
no ztp force-provision
Description
Startson-demandZTP.
Usage
DHCPoptionsreceivedareprocessedindependentofhecurrentstateofconfigurationontheswitch.
PreviousZTPTFTPServer,ImageFile,ConfigurationFile,ArubaCentralLocation,andHTTPProxy
locationoptionsareclearedandtheswitchsendsaDHCPrequest.
Examples
Inthefollowingexample,force-provisionisenabled.
| switch#         | configure terminal |                 |     |     |     |
| --------------- | ------------------ | --------------- | --- | --- | --- |
| switch(config)# | ztp                | force-provision |     |     |     |
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
| switch#       | show ztp information |       |                     |     |     |
| ------------- | -------------------- | ----- | ------------------- | --- | --- |
| TFTP Server   |                      |       | : 10.0.0.2          |     |     |
| Image File    |                      |       | : TL_10_02_0001.swi |     |     |
| Configuration | File                 |       | : ztp.cfg           |     |     |
| Status        |                      |       | : Success           |     |     |
| Aruba Central | Location             |       | : NA                |     |     |
| Aruba Central | Shared               | Token | : NA                |     |     |
ZeroTouchProvisioning|207

| Force-Provision |          |     | : Enabled |
| --------------- | -------- | --- | --------- |
| HTTP Proxy      | Location |     | : NA      |
Inthefollowingexample,force-provisionisdisabled.
| switch#         | configure terminal |                     |     |
| --------------- | ------------------ | ------------------- | --- |
| switch(config)# | no                 | ztp force-provision |     |
Inthefollowingexample,force-provisionstatusischeckedwhiledisabled.
| switch#         | show ztp information |         |                     |
| --------------- | -------------------- | ------- | ------------------- |
| TFTP Server     |                      |         | : 10.0.0.2          |
| Image File      |                      |         | : TL_10_02_0001.swi |
| Configuration   | File                 |         | : ztp.cfg           |
| Status          |                      |         | : Success           |
| Aruba Central   | Location             |         | : NA                |
| Aruba Central   | Shared               | Token   | : NA                |
| Force-Provision |                      |         | : Disabled          |
| HTTP Proxy      | Location             |         | : NA                |
| Command         | History              |         |                     |
| Release         |                      |         | Modification        |
| 10.07orearlier  |                      |         | --                  |
| Command         | Information          |         |                     |
| Platforms       | Command              | context | Authority           |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|     | (#) |     | rightsforthiscommand. |
| --- | --- | --- | --------------------- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 208

Chapter 13
|                   |              |     | Switch   | system | and hardware | commands |
| ----------------- | ------------ | --- | -------- | ------ | ------------ | -------- |
| Switch system     | and hardware |     | commands |        |              |          |
| bluetooth         | disable      |     |          |        |              |          |
| bluetooth disable |              |     |          |        |              |          |
| no bluetooth      | disable      |     |          |        |              |          |
Description
DisablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesbothBluetoothClassicand
BluetoothLowEnergy(BLE).Bluetoothisenabledbydefault.
ThenoformofthiscommandenablestheBluetoothfeatureontheswitch.
Example
DisablingBluetoothontheswitch.<XXXX>istheswitchplatformand<NNNNNNNNNN>isthedevice
identifier.
| switch(config)# | bluetooth |                       | disable |     |     |     |
| --------------- | --------- | --------------------- | ------- | --- | --- | --- |
| switch# show    | bluetooth |                       |         |     |     |     |
| Enabled         |           | : No                  |         |     |     |     |
| Device name     |           | : <XXXX>-<NNNNNNNNNN> |         |     |     |     |
| switch(config)# | show      | running-config        |         |     |     |     |
...
| bluetooth | disabled |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- |
...
| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
8400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| bluetooth        | enable |     |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- | --- |
| bluetooth enable |        |     |     |     |     |     |
| no bluetooth     | enable |     |     |     |     |     |
Description
209
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries)

ThiscommandenablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesboth
BluetoothClassicandBluetoothLowEnergy(BLE).
Default:Bluetoothisenabledbydefault.
ThenoformofthiscommanddisablestheBluetoothfeatureontheswitch.
Usage
ThedefaultconfigurationoftheBluetoothfeatureisenabled.Theoutputoftheshow running-config
commandincludesBluetoothinformationonlyiftheBluetoothfeatureisdisabled.
TheBluetoothfeatureincludesbothBluetoothClassicandBluetoothLowEnergy(BLE).
TheBluetoothfeaturerequirestheUSBfeaturetobeenabled.IftheUSBfeaturehasbeendisabled,you
mustenabletheUSBfeaturebeforeyoucanenabletheBluetoothfeature.
Examples
| switch(config)#     | bluetooth | enable  |              |
| ------------------- | --------- | ------- | ------------ |
| Command History     |           |         |              |
| Release             |           |         | Modification |
| 10.07orearlier      |           |         | --           |
| Command Information |           |         |              |
| Platforms           | Command   | context | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
clear events
clear events
Description
Clearsupeventlogs.Usingtheshow eventscommandwillonlydisplaythelogsgeneratedafterthe
clear eventscommand.
Examples
Clearingallgeneratedeventlogs:
| switch# show | events |     |     |
| ------------ | ------ | --- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 27 |
| ----------- | ------------- | ---------- | ----- |
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to
36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 49 |
| ----------- | ------------- | ---------- | ----- |
Switchsystemandhardwarecommands|210

switch#
clear events
| switch# | show events |     |     |
| ------- | ----------- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2018-10-14:07:03:05.637544|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization    | poll interval | is changed | to 34        |
| -------------- | ------------- | ---------- | ------------ |
| Command        | History       |            |              |
| Release        |               |            | Modification |
| 10.07orearlier |               |            | --           |
| Command        | Information   |            |              |
| Platforms      | Command       | context    | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear ip | errors |     |     |
| -------- | ------ | --- | --- |
clear ip errors
Description
ClearsallIPerrorstatistics.
Example
Clearingandshowingiperrors:
| switch# | clear ip errors |     |     |
| ------- | --------------- | --- | --- |
| switch# | show ip errors  |     |     |
----------------------------------
| Drop reason |     | Packets |     |
| ----------- | --- | ------- | --- |
----------------------------------
| Malformed  | packets |     | 0   |
| ---------- | ------- | --- | --- |
| IP address | errors  |     | 0   |
...
| Command        | History     |     |              |
| -------------- | ----------- | --- | ------------ |
| Release        |             |     | Modification |
| 10.07orearlier |             |     | --           |
| Command        | Information |     |              |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 211

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| console    | baud-rate |         |     |     |     |     |
| ---------- | --------- | ------- | --- | --- | --- | --- |
| console    | baud-rate | <SPEED> |     |     |     |     |
| no console | baud-rate | <SPEED> |     |     |     |     |
Description
Setstheconsoleserialportspeed.
Thenoformofthiscommandresetstheconsoleportspeedtoitsdefaultof115200bps.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<SPEED>
Selectstheconsoleportspeedinbps,either9600or115200.
Usage
Thespeedchangeoccursimmediatelyfortheactiveconsolesession.Theconsolewillbeinaccessible
untiltheclientterminalsettingsareupdatedtomatchtheconsoleportspeedthatyouset.Afterthe
commandisexecutedyouwillbepromptedtologinagain.
Examples
Settingtheconsoleportspeedto9600bps:
| switch(config)# |     | console |     | baud-rate | 9600 |     |
| --------------- | --- | ------- | --- | --------- | ---- | --- |
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
| settings | are    | updated | to  | match the | baud rate | of the switch. |
| -------- | ------ | ------- | --- | --------- | --------- | -------------- |
| Continue | (y/n)? | y       |     |           |           |                |
Resettingtheconsoleporttoitsdefaultspeed115200bps:
| switch(config)# |             | no      | console | baud-rate |                   |     |
| --------------- | ----------- | ------- | ------- | --------- | ----------------- | --- |
| Command         | History     |         |         |           |                   |     |
| Release         |             |         |         |           | Modification      |     |
| 10.08           |             |         |         |           | Commandintroduced |     |
| Command         | Information |         |         |           |                   |     |
| Platforms       |             | Command | context |           | Authority         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Switchsystemandhardwarecommands|212

domain-name
| domain-name    | <NAME>   |     |     |     |
| -------------- | -------- | --- | --- | --- |
| no domain-name | [<NAME>] |     |     |     |
Description
Specifiesthedomainnameoftheswitch.
Thenoformofthiscommandsetsthedomainnametothedefault,whichisnodomainname.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<NAME> Specifiesthedomainnametobeassignedtotheswitch.Thefirst
characterofthenamemustbealetteroranumber.Length:1to
32characters.
Examples
Settingandshowingthedomainname:
| switch# show    | domain-name |             |             |     |
| --------------- | ----------- | ----------- | ----------- | --- |
| switch# config  |             |             |             |     |
| switch(config)# | domain-name |             | example.com |     |
| switch(config)# | show        | domain-name |             |     |
example.com
switch(config)#
Settingthedomainnametothedefaultvalue:
| switch(config)# | no   | domain-name |     |     |
| --------------- | ---- | ----------- | --- | --- |
| switch(config)# | show | domain-name |     |     |
switch(config)#
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| fabric admin-state |             |     |             |              |
| ------------------ | ----------- | --- | ----------- | ------------ |
| fabric <SLOT-ID>   | admin-state |     | {diagnostic | | down | up} |
Description
Setstheadministrativestateofthespecifiedfabricmodule.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 213

| Parameter |     |     | Description                                      |
| --------- | --- | --- | ------------------------------------------------ |
| <SLOT-ID> |     |     | Specifiesthememberandslotofthemodule.Forexample, |
tospecifythemoduleinmember1,slot2,enterthe
following:
1/2
admin-state {diagnostic | down | up} Selectstheadministrativestateinwhichtoputthespecified
module:
diagnostic
Selectsthediagnosticadministrativestate.Network
trafficdoesnotpassthroughthemodule.
down
Selectsthedownadministrativestate.Networktrafficdoes
notpassthroughthemodule.
up
Selectstheupadministrativestate.Themoduleisfully
operational.Theupstateisthedefaultadministrativestate.
Usage
Thiscommandisvalidforfabricmodulesonly.
Examples
Settingtheadministrativestateofthefabricmodule2todown:
| switch(config)#     | fabric  | 1/2 admin-state | down         |
| ------------------- | ------- | --------------- | ------------ |
| Command History     |         |                 |              |
| Release             |         |                 | Modification |
| 10.07orearlier      |         |                 | --           |
| Command Information |         |                 |              |
| Platforms           | Command | context         | Authority    |
config
| 8400 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
hostname
hostname <HOSTNAME>
| no hostname | [<HOSTNAME>] |     |     |
| ----------- | ------------ | --- | --- |
Description
Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
Switchsystemandhardwarecommands|214

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<HOSTNAME> Specifiesthehostname.Thefirstcharacterofthehostname
mustbealetteroranumber.Length:1to32characters.Default:
switch
Examples
Settingandshowingthehostname:
| switch# show | hostname |     |     |
| ------------ | -------- | --- | --- |
switch
switch#
config
| switch(config)#   | hostname | myswitch |     |
| ----------------- | -------- | -------- | --- |
| myswitch(config)# | show     | hostname |     |
myswitch
Settingthehostnametothedefaultvalue:
| myswitch(config)# | no  | hostname |     |
| ----------------- | --- | -------- | --- |
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
led locator
led locator {on | off | flashing | slow_blink | fast_blink | half_bright}
no led locator {on | off | flashing |slow_blink | fast_blink | half_bright}
Description
SetsthestateofthelocatorLED.
| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
| on        |     |     | TurnsontheLED.                         |
| off       |     |     | TurnsofftheLED,whichisthedefaultvalue. |
| flashing  |     |     | SetstheLEDtoblinkonandoffrepeatedly.   |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 215

| Parameter   |     |     |     |     | Description                      |     |
| ----------- | --- | --- | --- | --- | -------------------------------- | --- |
| slow_blink  |     |     |     |     | SetstheLEDtoslowblinkonandoff.   |     |
| fast_blink  |     |     |     |     | SetstheLEDtofastblinkonandoff.   |     |
| half_bright |     |     |     |     | SetstheLEDintensitytohalfbright. |     |
Example
SettingthestateofthelocatorLED:
| switch#        | led         | locator |     | flashing |              |           |
| -------------- | ----------- | ------- | --- | -------- | ------------ | --------- |
| Command        | History     |         |     |          |              |           |
| Release        |             |         |     |          | Modification |           |
| 10.07orearlier |             |         |     |          | --           |           |
| Command        | Information |         |     |          |              |           |
| Platforms      |             | Command |     | context  |              | Authority |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| module    |           | admin-state |              |             |             |               |
| --------- | --------- | ----------- | ------------ | ----------- | ----------- | ------------- |
| module    | <SLOT-ID> |             | admin-state  | {diagnostic |             | | down | up}  |
| no module | <SLOT-ID> |             | [admin-state |             | [diagnostic | | down | up]] |
Description
Setstheadministrativestateofthespecifiedlinemodule.
Thenoformofthecommandconfiguresadministrativestatetothedefaultup.
| Parameter |     |     |     |     |     | Description                                      |
| --------- | --- | --- | --- | --- | --- | ------------------------------------------------ |
| <SLOT-ID> |     |     |     |     |     | Specifiesthememberandslotofthemodule.Forexample, |
tospecifythemoduleinmember1,slot3,enterthe
following:
1/3
| admin-state |     | {diagnostic |     | | down | | up} |     |
| ----------- | --- | ----------- | --- | ------ | ----- | --- |
Selectstheadministrativestateinwhichtoputthespecified
module:
| diagnostic |     |     |     |     |     | Selectsthediagnosticadministrativestate.Network |
| ---------- | --- | --- | --- | --- | --- | ----------------------------------------------- |
trafficdoesnotpassthroughthemodule.
| down |     |     |     |     |     | Selectsthedownadministrativestate.Networktrafficdoes |
| ---- | --- | --- | --- | --- | --- | ---------------------------------------------------- |
notpassthroughthemodule.
Switchsystemandhardwarecommands|216

| Parameter |     |     |     |     | Description                                          |
| --------- | --- | --- | --- | --- | ---------------------------------------------------- |
| up        |     |     |     |     | Selectstheupadministrativestate.Thelinemoduleisfully |
operational.Theupstateisthedefaultadministrativestate.
Example
Settingtheadministrativestateofthemoduleinslot1/3todown:
switch(config)#
|                |             | module  | 1/3     | admin-state | down         |
| -------------- | ----------- | ------- | ------- | ----------- | ------------ |
| Command        | History     |         |         |             |              |
| Release        |             |         |         |             | Modification |
| 10.07orearlier |             |         |         |             | --           |
| Command        | Information |         |         |             |              |
| Platforms      |             | Command | context |             | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| module    |           | product-number  |     |                 |                  |
| --------- | --------- | --------------- | --- | --------------- | ---------------- |
| module    | <SLOT-ID> | product-number  |     | [<PRODUCT-NUM>] |                  |
| no module | <SLOT-ID> | [product-number |     |                 | [<PRODUCT-NUM>]] |
Description
Changestheconfigurationoftheswitchtoindicatethatthespecifiedmemberandslotnumber
contains,orwillcontain,alinemodule.
Thenoformofthiscommandremovesthelinemoduleanditsinterfacesfromtheconfiguration.If
thereisalinemoduleinstalledintheslot,thelinemoduleispoweredoffandthenpoweredon.
| Parameter |     |     |     |     | Description                                       |
| --------- | --- | --- | --- | --- | ------------------------------------------------- |
| <SLOT-ID> |     |     |     |     | Specifiesthememberandslotintheformm/s,wheremisthe |
membernumber,andsistheslotnumber.
<PRODUCT-NUM> Specifiestheproductnumberofthelinemodule.Forexample:
JL363A
Ifthereisalinemoduleinstalledintheslotwhenyouexecutethis
command,<PRODUCT-NUM>isoptional.Theswitchreadsthe
productnumberinformationfromthemodulethatisinstalledin
theslot.
Ifthereisnolinemoduleinstalledintheslotwhenyouexecute
thiscommand,<PRODUCT-NUM>isrequired.
Usage
Thedefaultconfigurationassociatedwithalinemoduleslotis:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 217

n There is no module product number or interface configuration information associated with the slot.

The slot is available for the installation with any supported line module.

n The Admin State is Up (which is the default value for Admin State).

To add a line module to the configuration, you must use the module command either before or after you
install the physical module.

If you execute the module command after you install a line module in an empty slot, you can omit the
<PRODUCT-NUM> variable. The switch reads the product information from the installed module.

If the module is not installed in the slot when you execute the module command, you must specify a
value for the <PRODUCT-NUM> variable:

n The switch validates the product number of the module against the slot number you specify to

ensure that the right type of module is configured for the specified slot.

For example, the switch returns an error if you specify the product number of a line module for a slot
reserved for management modules.

n You can configure the line module interfaces before the line module is installed.

When you install the physical line module in a preconfigured slot, the following actions occur:

n If a product number was specified in the command and it matches the product number of the

installed module, the switch initializes the module.

n If a product number was specified in the command and the product number of the module does not

match what was specified, the module device initialization fails.

The no form of the command removes the line module and its interfaces from the configuration and
restores the line module slot to the default configuration.

If there is a line module installed in the slot when you execute the no form of the command, the
command also powers off and then powers on the module. Traffic passing through the line module is
stopped. Management sessions connected through the line module are also affected.

If the slot associated with the line module is in the default configuration, you can remove the module
from the chassis without disrupting the operation of the switch.

Examples

Configuring slot 1/1 for future installation of a line module:

switch(config)# module 1/1 product-number jl363a

Configuring a line module that is already installed in slot 1/1:

switch(config)# module 1/1 product-number

Attempting to configure slot 1/1 for the future installation of a line module without specifying the
product number (returned error shown):

switch(config)# module 1/1 product-number
Line module '1/4' is not physically available.
number to preconfigure the line module.

Please provide the product

Configuring a JL363A line module in a slot that has already been used to configure a different module:

Switch system and hardware commands | 218

| switch(config)# | no  | module | 1/4 |     |     |
| --------------- | --- | ------ | --- | --- | --- |
switch(config)#
|     | module | 1/4 | product-number |     | jl363a |
| --- | ------ | --- | -------------- | --- | ------ |
Removingamodulefromtheconfiguration:
| switch(config)# | no  | module | 1/1 |     |     |
| --------------- | --- | ------ | --- | --- | --- |
This command will power cycle the specified line module and restore its default
configuration. Any traffic passing through the line module will be interrupted.
Management sessions connected through the line module will be affected. It
| might take  | a few minutes |     | to complete | this | operation. |
| ----------- | ------------- | --- | ----------- | ---- | ---------- |
| Do you want | to continue   |     | (y/n)?      | y    |            |
switch(config)#
| Command        | History     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------------ | --- |
| Release        |             |         |     | Modification |     |
| 10.07orearlier |             |         |     | --           |     |
| Command        | Information |         |     |              |     |
| Platforms      | Command     | context |     | Authority    |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
mtrace
mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
[vrf <VRF-NAME>]
Description
TracesthespecifiedIPv4sourceandgroupaddresses.
| Parameter       |     |     |     | Description                           |     |
| --------------- | --- | --- | --- | ------------------------------------- | --- |
| IPV4-SRC-ADDR   |     |     |     | SpecifiesthesourceIPv4addresstotrace. |     |
| IPV4-GROUP-ADDR |     |     |     | SpecifiesthegroupIPv4addresstotrace.  |     |
lhr <IPV4-LHR-ADDR> Specifiesthelasthoprouteraddressfromwhichtostartthetrace.
ttl <HOPS> SpecifiestheTime-To-Livedurationinhops.Range:1to255hops.
Default:8hops.
vrf <VRF-NAME> SpecifiesthenameoftheVRF.Ifanameisnotspecifiedthe
defaultVRFwillbeused.
Examples
Tracingwithsource,group,andLHRaddressesandTTL:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 219

| (switch)#           | mtrace        | 20.0.0.1 | 239.1.1.1 |          | lhr | 10.1.1.1 | ttl 10          |
| ------------------- | ------------- | -------- | --------- | -------- | --- | -------- | --------------- |
| Type escape         | sequence      | to       | abort.    |          |     |          |                 |
| Mtrace              | from 10.0.0.1 | for      | Source    | 20.0.0.1 |     | via      | Group 239.1.1.1 |
| From destination(?) |               | to       | source    | (?)...   |     |          |                 |
| Querying            | ful reverse   | path...  |           |          |     |          |                 |
0 10.0.0.1
| -1 30.0.0.1 | PIM | 0 ms |     |     |     |     |     |
| ----------- | --- | ---- | --- | --- | --- | --- | --- |
| -2 40.0.0.1 | PIM | 2 ms |     |     |     |     |     |
| -3 50.0.0.1 | PIM | 100  | ms  |     |     |     |     |
| -4 60.0.0.1 | PIM | 156  | ms  |     |     |     |     |
| -5 20.0.0.1 | PIM | 123  | ms  |     |     |     |     |
Tracingwithsourceandgroupaddresses:
| (switch)#           | mtrace      | 200.0.0.1  |        | 239.1.1.1 |     |           |           |
| ------------------- | ----------- | ---------- | ------ | --------- | --- | --------- | --------- |
| Type escape         | sequence    | to         | abort. |           |     |           |           |
| Mtrace              | from self   | for Source |        | 200.0.0.1 |     | via Group | 239.1.1.1 |
| From destination(?) |             | to         | source | (?)...    |     |           |           |
| Querying            | ful reverse | path...    |        |           |     |           |           |
0 10.0.0.1
| -1 30.0.0.1    | PIM         | 0 ms |         |     |              |     |     |
| -------------- | ----------- | ---- | ------- | --- | ------------ | --- | --- |
| -2 40.0.0.1    | PIM         | 2 ms |         |     |              |     |     |
| -3 50.0.0.1    | PIM         | 100  | ms      |     |              |     |     |
| -4 60.0.0.1    | PIM         | 156  | ms      |     |              |     |     |
| -5 200.0.0.1   | PIM         | 123  | ms      |     |              |     |     |
| Command        | History     |      |         |     |              |     |     |
| Release        |             |      |         |     | Modification |     |     |
| 10.07orearlier |             |      |         |     | --           |     |     |
| Command        | Information |      |         |     |              |     |     |
| Platforms      | Command     |      | context |     | Authority    |     |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show bluetooth
show bluetooth
Description
ShowsgeneralstatusinformationabouttheBluetoothwirelessmanagementfeatureontheswitch.
Usage
Thiscommandshowsstatusinformationaboutthefollowing:
Switchsystemandhardwarecommands|220

n TheUSBBluetoothadapter
n ClientsconnectedusingBluetooth
TheswitchBluetoothfeature.
n
Theoutputoftheshow running-configcommandincludesBluetoothinformationonlyiftheBluetooth
featureisdisabled.
Thedevicenamegiventotheswitchincludestheswitchserialnumbertouniquelyidentifytheswitch
whilepairingwithamobiledevice.
ThemanagementIPaddressisaprivatenetworkaddresscreatedformanagingtheswitchthrougha
Bluetoothconnection.
Examples
ExampleoutputwhenBluetoothisenabledbutnoBluetoothadapterisconnected.<XXXX>istheswitch
platformand<NNNNNNNNNN>isthedeviceidentifier.
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : Yes                 |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
| Adapter     | State          | : Absent              |     |     |     |
ExampleoutputwhenBluetoothisenabledandthereisaBluetoothadapterconnected:
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : Yes                 |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
| Adapter     | State          | : Ready               |     |     |     |
| Adapter     | IP address     | : 192.168.99.1        |     |     |     |
| Adapter     | MAC address    | : 480fcf-af153a       |     |     |     |
| Connected   | Clients        |                       |     |     |     |
-----------------
| Name | MAC | Address | IP Address | Connected | Since |
| ---- | --- | ------- | ---------- | --------- | ----- |
-------------- -------------- ------------ ------------------------
Mark's iPhone 089734-b12000 192.168.99.10 2018-07-09 08:47:22 PDT
ExampleoutputwhenBluetoothisdisabled:
| switch#        | show bluetooth |                       |              |     |     |
| -------------- | -------------- | --------------------- | ------------ | --- | --- |
| Enabled        |                | : No                  |              |     |     |
| Device name    |                | : <XXXX>-<NNNNNNNNNN> |              |     |     |
| Command        | History        |                       |              |     |     |
| Release        |                |                       | Modification |     |     |
| 10.07orearlier |                |                       | --           |     |     |
| Command        | Information    |                       |              |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 221

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show boot-history |       |     |     |
| ----------------- | ----- | --- | --- |
| show boot-history | [all] |     |     |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationabout
thebootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.When
theallparameterisspecified,showsthebootinformationfortheactivemanagementmoduleandall
availablelinemodules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandby
console.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| all       |     |     | Showsbootinformationfortheactivemanagementmoduleand |
allavailablelinemodules.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | up for <SECONDS> | seconds |     |
| ------------- | ---------------- | ------- | --- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
| Timestamp boot | reason |     |     |
| -------------- | ------ | --- | --- |
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperationoccurred
andthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |     |
| ------------- | ----- | --- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernel crash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
| Reboot requested | through | database |     |
| ---------------- | ------- | -------- | --- |
TherebootoccurredbecauseofarequestmadethroughtheCLIorotherAPI.
| Uncontrolled | reboot |     |     |
| ------------ | ------ | --- | --- |
Thereasonfortherebootisnotknown.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
Switchsystemandhardwarecommands|222

| Index : | 3                                  |          |           |      |                  |
| ------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| Current | Boot, up for                       | 22       | hrs 12    | mins | 22 secs          |
| Index : | 2                                  |          |           |      |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |          |           |      |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot | requested |      | through database |
| Index : | 1                                  |          |           |      |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |          |           |      |                  |
| 07 Aug  | 18 14:08:46                        | : Reboot | requested |      | through database |
| Index : | 0                                  |          |           |      |                  |
| Boot ID | : 23da2b0e26d048d7b3f4b6721b69c110 |          |           |      |                  |
| 07 Aug  | 18 13:00:46                        | : Reboot | requested |      | through database |
switch#
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
| switch#    | show boot-history |     | all |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
| Management | module            |     |     |     |     |
=================
| Index :     | 3                                  |          |           |      |                  |
| ----------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| Current     | Boot, up for                       | 22       | hrs 12    | mins | 22 secs          |
| Index :     | 2                                  |          |           |      |                  |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |          |           |      |                  |
| 07 Aug      | 18 16:28:01                        | : Reboot | requested |      | through database |
| Index :     | 1                                  |          |           |      |                  |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |          |           |      |                  |
| 07 Aug      | 18 14:08:46                        | : Reboot | requested |      | through database |
| Index :     | 0                                  |          |           |      |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |          |           |      |                  |
| 07 Aug      | 18 13:00:46                        | : Reboot | requested |      | through database |
| Line module | 1/1                                |          |           |      |                  |
=================
| Index : | 3           |              |     |         |     |
| ------- | ----------- | ------------ | --- | ------- | --- |
| 10 Aug  | 17 12:45:46 | : dune_agent |     | crashed |     |
...
| Command        | History     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------------ | --- |
| Release        |             |         |     | Modification |     |
| 10.07orearlier |             |         |     | --           |     |
| Command        | Information |         |     |              |     |
| Platforms      | Command     | context |     | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 223

| show capacities |           |            |     |     |
| --------------- | --------- | ---------- | --- | --- |
| show capacities | <FEATURE> | [vsx-peer] |     |     |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<FEATURE>
Specifiesafeature.Forexample,aaaorvrrp.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
ShowingallavailablecapacitiesforBGP:
| switch#            | show capacities | bgp        |     |       |
| ------------------ | --------------- | ---------- | --- | ----- |
| System Capacities: |                 | Filter BGP |     |       |
| Capacities         | Name            |            |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of AS | numbers in as-path | attribute |     |
| ------- | ------------ | ------------------ | --------- | --- |
32
...
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring        |     |       |
| ------------------ | --------------- | ---------------- | --- | ----- |
| System Capacities: |                 | Filter Mirroring |     |       |
| Capacities         | Name            |                  |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of Mirror | Sessions configurable | in a system |     |
| ------- | ---------------- | --------------------- | ----------- | --- |
4
| Maximum | number of enabled | Mirror Sessions | in a system |     |
| ------- | ----------------- | --------------- | ----------- | --- |
4
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp        |     |       |
| ------------------ | --------------- | ----------- | --- | ----- |
| System Capacities: |                 | Filter MSTP |     |       |
| Capacities         | Name            |             |     | Value |
----------------------------------------------------------------------------------
-
Switchsystemandhardwarecommands|224

| Maximum | number of | mstp instances | configurable | in a system |     |     |
| ------- | --------- | -------------- | ------------ | ----------- | --- | --- |
64
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities | vlan-count |            |     |     |       |
| ------------------ | --------------- | ---------- | ---------- | --- | --- | ----- |
| System Capacities: |                 | Filter     | VLAN Count |     |     |       |
| Capacities         | Name            |            |            |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | VLANs supported | in the system |     |     |     |
| ------- | --------- | --------------- | ------------- | --- | --- | --- |
4094
| Command        | History     |         |              |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show capacities-status |     |           |            |     |     |     |
| ---------------------- | --- | --------- | ---------- | --- | --- | --- |
| show capacities-status |     | <FEATURE> | [vsx-peer] |     |     |     |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description                                       |     |     |     |
| --------- | --- | --- | ------------------------------------------------- | --- | --- | --- |
| <FEATURE> |     |     | Specifiesthefeature,forexampleaaaorvrrpforwhichto |     |     |     |
displaycapacities,values,andstatus.Required.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
| switch#           | show capacities-status |        |     |     |               |     |
| ----------------- | ---------------------- | ------ | --- | --- | ------------- | --- |
| System Capacities |                        | Status |     |     |               |     |
| Capacities        | Status                 | Name   |     |     | Value Maximum |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 225

------------------------------------------------------------------------------
| Number | of active          | gateway | mac        | addresses | in  | a system | 0 16 |
| ------ | ------------------ | ------- | ---------- | --------- | --- | -------- | ---- |
| Number | of aspath-lists    |         | configured |           |     |          | 0 64 |
| Number | of community-lists |         | configured |           |     |          | 0 64 |
...
ShowingthesystemcapacitiesstatusforBGP:
| switch#    | show capacities-status |         |        | bgp |     |     |               |
| ---------- | ---------------------- | ------- | ------ | --- | --- | --- | ------------- |
| System     | Capacities             | Status: | Filter | BGP |     |     |               |
| Capacities | Status                 | Name    |        |     |     |     | Value Maximum |
-------------------------------------------------------------------------------
| Number | of aspath-lists    |        | configured |        |     |      | 0 64     |
| ------ | ------------------ | ------ | ---------- | ------ | --- | ---- | -------- |
| Number | of community-lists |        | configured |        |     |      | 0 64     |
| Number | of neighbors       |        | configured | across | all | VRFs | 0 50     |
| Number | of peer            | groups | configured | across | all | VRFs | 0 25     |
| Number | of prefix-lists    |        | configured |        |     |      | 0 64     |
| Number | of route-maps      |        | configured |        |     |      | 0 64     |
| Number | of routes          | in     | BGP RIB    |        |     |      | 0 256000 |
Number of route reflector clients configured across all VRFs 0 16
| Command        | History     |     |         |              |     |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- | --- |
| Release        |             |     |         | Modification |     |     |     |
| 10.07orearlier |             |     |         | --           |     |     |     |
| Command        | Information |     |         |              |     |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
| switch#    | show console |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- |
| Baud Rate: | 9600         |     |     |     |     |     |     |
| Command    | History      |     |     |     |     |     |     |
Switchsystemandhardwarecommands|226

Release

10.08

Modification

Command introduced

Command Information

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show core-dump
show core-dump [all | <SLOT-ID>]

Description

Shows core dump information about the specified module. When no parameters are specified, shows
only the core dumps generated in the current boot of the management module. When the all
parameter is specified, shows all available core dumps.

Parameter

all

<SLOT-ID>

Usage

Description

Shows all available core dumps.

Shows the core dumps for the management module or
line module in <SLOT-ID>. <SLOT-ID> specifies a physical
location on the switch. Use the format
member/slot/port (for example, 1/3/1) for line
modules. Use the format member/slot for management
modules.

You must specify the slot ID for either the active
management module, or the line module.

When no parameters are specified, the show core-dump command shows only the core dumps
generated in the current boot of the management module. You can use this command to determine
when any crashes are occurring in the current boot.

If no core dumps have occurred, the following message is displayed: No core dumps are present

To show core dump information for the standby management module, you must use the standby
command to switch to the standby management module and then execute the show core-dump
command.

In the output, the meaning of the information is the following:
Daemon Name
Identifies name of the daemon for which there is dump information.
Instance ID
Identifies the specific instance of the daemon shown in the Daemon Name column.
Present
Indicates the status of the core dump:
Yes
The core dump has completed and available for copying.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

227

In Progress
Coredumpgenerationisinprogress.Donotattempttocopythiscoredump.
Timestamp
Indicatesthetimethedaemoncrashoccurred.Thetimeisthelocaltimeusingthetimezoneconfiguredonthe
switch.
Build ID
Identifiesadditionalinformationaboutthesoftwareimageassociatedwiththedaemon.
Examples
Showingcoredumpinformationforthecurrentbootoftheactivemanagementmoduleonly:
| switch# show | core-dump |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- |
==================================================================================
| Daemon Name |     | | Instance | ID | | Present | | Timestamp |     | | Build ID |
| ----------- | --- | ---------- | ---- | ------- | ----------- | --- | ---------- |
==================================================================================
| hpe-fand    |     | 1399 |     | Yes | 2017-08-04 | 19:05:34 | 1246d2a |
| ----------- | --- | ---- | --- | --- | ---------- | -------- | ------- |
| hpe-sysmond |     | 957  |     | Yes | 2017-08-04 | 19:05:29 | 1246d2a |
==================================================================================
| Total number | of  | core dumps | : 2 |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- |
==================================================================================
Showingallcoredumps:
| switch# show | core-dump | all |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- |
=============================================================================
| Management | Module | core-dumps |     |     |     |     |     |
| ---------- | ------ | ---------- | --- | --- | --- | --- | --- |
=============================================================================
| Daemon Name |     | | Instance | ID | | Present | | Timestamp |     | | Build ID |
| ----------- | --- | ---------- | ---- | ------- | ----------- | --- | ---------- |
=============================================================================
| hpe-sysmond |            | 513  |     | Yes | 2017-07-31 | 13:58:05 | e70f101 |
| ----------- | ---------- | ---- | --- | --- | ---------- | -------- | ------- |
| hpe-tempd   |            | 1048 |     | Yes | 2017-08-13 | 13:31:53 | e70f101 |
| hpe-tempd   |            | 1052 |     | Yes | 2017-08-13 | 13:41:44 | e70f101 |
| Line Module | core-dumps |      |     |     |            |          |         |
=============================================================================
| Line Module | : 1/1 |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- |
=============================================================================
| dune_agent_0 |     | 18958 |     | Yes | 2017-08-12 | 11:50:17 | e70f101 |
| ------------ | --- | ----- | --- | --- | ---------- | -------- | ------- |
| dune_agent_0 |     | 18842 |     | Yes | 2017-08-12 | 11:50:09 | e70f101 |
=============================================================================
| Total number | of  | core dumps | : 5 |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- |
=============================================================================
| Command History     |         |         |     |              |     |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- | --- |
| Release             |         |         |     | Modification |     |     |     |
| 10.07orearlier      |         |         |     | --           |     |     |     |
| Command Information |         |         |     |              |     |     |     |
| Platforms           | Command | context |     | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Switchsystemandhardwarecommands|228

show domain-name
| show domain-name | [vsx-peer] |     |     |
| ---------------- | ---------- | --- | --- |
Description
Showsthecurrentdomainname.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Ifthereisnodomainnameconfigured,theCLIdisplaysablankline.
Example
Settingandshowingthedomainname:
| switch# show    | domain-name |             |     |
| --------------- | ----------- | ----------- | --- |
| switch# config  |             |             |     |
| switch(config)# | domain-name | example.com |     |
| switch(config)# | show        | domain-name |     |
example.com
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show environment |                | fan |     |
| ---------------- | -------------- | --- | --- |
| show environment | fan [vsx-peer] |     |     |
Description
Showsthestatusinformationforallfansandfantrays(ifpresent)inthesystem.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 229

Parameter

vsx-peer

Usage

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

For fan trays, Status is one of the following values:
ready
The fan tray is operating normally.
fault
The fan tray is in a fault event. The status of the fan tray does not indicate the status of fans.
empty
The fan tray is not installed in the system.

For fans:
Speed

Indicates the relative speed of the fan based on the nominal speed range of the fan. Values are:
Slow

The fan is running at less than 25% of its maximum speed.

Normal

The fan is running at 25-49% of its maximum speed.

Medium

The fan is running at 50-74% of its maximum speed.

Fast

The fan is running at 75-99% of its maximum speed.

Max

The fan is running at 100% of its maximum speed.

N/A

The fan is not installed.

Direction
The direction of airflow through the fan. Values are:

front-to-back

Air flows from the front of the system to the back of the system.

N/A

The fan is not installed.

Status
Fan status. Values are:
uninitialized

The fan has not completed initialization.

ok

The fan is operating normally.

fault

The fan is in a fault state.

empty

The fan is not installed.

Examples

Showing output for systems with fan trays for 8400 switch series:

Switch system and hardware commands | 230

| switch#  | show environment | fan |     |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- | --- | --- |
| Fan tray | information      |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Mbr/Tray | Description |     |     |     | Status Serial | Number | Fans |
| -------- | ----------- | --- | --- | --- | ------------- | ------ | ---- |
------------------------------------------------------------------------------
| 1/1 | JL369A 8400 | Fan | tray |     | ready SGXXXXXXXXXX |     | 6   |
| --- | ----------- | --- | ---- | --- | ------------------ | --- | --- |
| 1/2 | JL369A 8400 | Fan | tray |     | ready SGXXXXXXXXXX |     | 6   |
| 1/3 | N/A         |     |      |     | empty N/A          |     | 0   |
Fan information
------------------------------------------------------------------------
| Mbr/Tray/Fan | Serial | Number | Speed Direction |     | Status | RPM |     |
| ------------ | ------ | ------ | --------------- | --- | ------ | --- | --- |
------------------------------------------------------------------------
| 1/1/1 | SGXXXXXXXXXX |     | slow front-to-back   |     | ok    | 6000  |     |
| ----- | ------------ | --- | -------------------- | --- | ----- | ----- | --- |
| 1/1/2 | SGXXXXXXXXXX |     | normal front-to-back |     | ok    | 8000  |     |
| 1/1/3 | SGXXXXXXXXXX |     | medium front-to-back |     | ok    | 11000 |     |
| 1/1/4 | SGXXXXXXXXXX |     | fast front-to-back   |     | ok    | 14000 |     |
| 1/1/5 | SGXXXXXXXXXX |     | max front-to-back    |     | fault | 16500 |     |
| 1/1/6 | N/A          |     | N/A N/A              |     | empty | 0     |     |
| 1/2/1 | SGXXXXXXXXX  |     | slow front-to-back   |     | ok    | 6000  |     |
...
Showingoutputforasystemwithoutafantray:
| switch# | show environment | fan |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- | --- |
Fan information
---------------------------------------------------------------
| Fan Serial | Number | Speed | Direction | Status | RPM |     |     |
| ---------- | ------ | ----- | --------- | ------ | --- | --- | --- |
---------------------------------------------------------------
| 1 SGXXXXXXXXXX |     | slow   | front-to-back | ok    | 6000  |     |     |
| -------------- | --- | ------ | ------------- | ----- | ----- | --- | --- |
| 2 SGXXXXXXXXXX |     | normal | front-to-back | ok    | 8000  |     |     |
| 3 SGXXXXXXXXXX |     | medium | front-to-back | ok    | 11000 |     |     |
| 4 SGXXXXXXXXXX |     | fast   | front-to-back | ok    | 14000 |     |     |
| 5 SGXXXXXXXXXX |     | max    | front-to-back | fault | 16500 |     |     |
| 6 N/A          |     | N/A    | N/A           | empty |       |     |     |
...
| Command        | History     |         |              |     |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |     |
| Command        | Information |         |              |     |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |     | led        |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- | --- |
| show environment | led | [vsx-peer] |     |     |     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 231

Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingstateandstatusforLED:
| switch# show | environment | led    |     |
| ------------ | ----------- | ------ | --- |
| Name         | State       | Status |     |
-----------------------------------
| locator             | flashing | ok      |              |
| ------------------- | -------- | ------- | ------------ |
| Command History     |          |         |              |
| Release             |          |         | Modification |
| 10.07orearlier      |          |         | --           |
| Command Information |          |         |              |
| Platforms           | Command  | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show environment |                   | power-consumption |            |
| ---------------- | ----------------- | ----------------- | ---------- |
| show environment | power-consumption |                   | [vsx-peer] |
Description
Showsthepowerbeingconsumedbyeachmanagementmodule,linecard,andfabriccardsubsystem,
andshowspowerconsumptionfortheentirechassis.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Thiscommandisonlyapplicabletosystemsthatsupportpowerconsumptionreadings.
Thepowerconsumptionvaluesareupdatedonceeveryminute.
Switchsystemandhardwarecommands|232

Theoutputofthiscommandincludesthefollowinginformation:
Name
Showsthemembernumberandslotnumberofthemanagementmodule,linemodule,orfabriccardmodule.
Type
ShowsthetypeofmoduleinstalledatthelocationspecifiedbyName.
Description
Showstheproductnameandbriefdescriptionofthemodule.
Usage
Showstheinstantaneouspowerconsumptionofthemodule.PowerconsumptionisshowninWatts.
| Module Total | Power Usage |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
Showsthetotalpowerconsumptionofallthemoduleslisted.PowerconsumptionisshowninWatts.
| Chassis Total | Power Usage |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- |
Showsthetotalinstantaneouspowerconsumedbytheentirechassis,includingmodulesandcomponentsthatdo
notsupportindividualpowerreporting.PowerconsumptionisshowninWatts.
| Chassis Total | Power Available |     |     |     |     |
| ------------- | --------------- | --- | --- | --- | --- |
Showsthetotalamountofpower,inWatts,thatcanbesuppliedtothechassis.
| Chassis Total | Power Allocated |     |     |     |     |
| ------------- | --------------- | --- | --- | --- | --- |
Showstotalpower,inWatts,thatisallocatedtopoweringthechassisanditsinstalledmodules.
| Chassis Total | Power Unallocated |     |     |     |     |
| ------------- | ----------------- | --- | --- | --- | --- |
Showsthetotalamountofpower,inWatts,thathasnotbeenallocatedtopoweringthechassisoritsinstalled
modules.Thispowercanbeusedforadditionalhardwareyouinstallinthechassis.
Example
ShowingpowerconsumptionusageforanAruba8400switch
| switch> show | environment | power-consumption |     |     |       |
| ------------ | ----------- | ----------------- | --- | --- | ----- |
| Name Type    |             | Description       |     |     | Usage |
------------------------------------------------------------------------------
| 1/5 management-module |     | JL368A 8400X | Mgmt Mod |     | 97 W |
| --------------------- | --- | ------------ | -------- | --- | ---- |
| 1/6 management-module |     | JL368A 8400X | Mgmt Mod |     | 49 W |
1/1 line-card-module JL363A 8400X 32P 10G SFP/SFP+ Msec Mod 139 W
| 1/2 line-card-module |     | JL365A 8400X | 8P 40G QSFP+ | Adv Mod | 158 W |
| -------------------- | --- | ------------ | ------------ | ------- | ----- |
1/3 line-card-module JL366A 8400X 6P 40G/100G QSFP28 Adv Mod 127 W
1/4 line-card-module JL363A 8400X 32P 10G SFP/SFP+ Msec Adv Mod 148 W
1/7 line-card-module JL363A 8400X 32P 10G SFP/SFP+ Msec Adv Mod 152 W
1/8 line-card-module JL363A 8400X 32P 10G SFP/SFP+ Msec Adv Mod 125 W
1/9 line-card-module JL363A 8400X 32P 10G SFP/SFP+ Msec Adv Mod 132 W
1/10 line-card-module JL363A 8400X 32P 10G SFP/SFP+ Msec Adv Mod 143 W
| 1/1 fabric-card-module |                 | JL367A 8400X | 7.2Tbps Fab | Mod | 107 W  |
| ---------------------- | --------------- | ------------ | ----------- | --- | ------ |
| 1/2 fabric-card-module |                 | JL367A 8400X | 7.2Tbps Fab | Mod | 93 W   |
| 1/3 fabric-card-module |                 | JL367A 8400X | 7.2Tbps Fab | Mod | 87 W   |
| Module Total           | Power Usage     |              |             |     | 1557 W |
| Chassis Total          | Power Usage     |              |             |     | 1807 W |
| Chassis Total          | Power Available |              |             |     | 9990 W |
Chassis Total Power Allocated (total of all max wattages) 4130 W
| Chassis Total       | Power Unallocated |              |     |     | 5860 W |
| ------------------- | ----------------- | ------------ | --- | --- | ------ |
| Command History     |                   |              |     |     |        |
| Release             |                   | Modification |     |     |        |
| 10.07orearlier      |                   | --           |     |     |        |
| Command Information |                   |              |     |     |        |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 233

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show environment |              | power-supply |     |
| ---------------- | ------------ | ------------ | --- |
| show environment | power-supply | [vsx-peer]   |     |
Description
Showsstatusinformationaboutallpowersuppliesintheswitch.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| vsf       |     |     | ShowsoutputfromtheVSFmember-idonswitchesthatsupport |
VSF.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Thefollowinginformationisprovidedforeachpowersupply:
Mbr/PSU
Showsthememberandslotnumberofthepowersupply.
| Product Number |     |     |     |
| -------------- | --- | --- | --- |
Showstheproductnumberofthepowersupply.
Serial Number
Showstheserialnumberofthepowersupply,whichuniquelyidentifiesthepowersupply.
PSU Status
Thestatusofthepowersupply.Valuesare:
OK
Powersupplyisoperatingnormally.
OK*
Powersupplyisoperatingnormally,butitistheonlypowersupplyinthechassis.Onepower
supplyisnotsufficienttosupplyfullpowertotheswitch.Whenthisvalueisshown,theoutputof
thecommandalsoshowsamessageattheendofthedisplayeddata.
Absent
Nopowersupplyisinstalledinthespecifiedslot.
| Input fault |     |     |     |
| ----------- | --- | --- | --- |
Thepowersupplyhasafaultconditiononitsinput.
| Output fault |     |     |     |
| ------------ | --- | --- | --- |
Thepowersupplyhasafaultconditiononitsoutput.
Warning
Thepowersupplyisnotoperatingnormally.
| Wattage Maximum |     |     |     |
| --------------- | --- | --- | --- |
Showsthemaximumamountofwattagethatthepowersupplycanprovide.
Example
Showingtheoutputwhenonlyonepowersupplyisactiveinthechassis:
Switchsystemandhardwarecommands|234

| switch# | show environment |        |     | power-supply |        |         |
| ------- | ---------------- | ------ | --- | ------------ | ------ | ------- |
|         | Product          | Serial |     |              | PSU    | Wattage |
| Mbr/PSU | Number           | Number |     |              | Status | Maximum |
---------------------------------------------------------
| 1/1 | JL372A | M031RM002JAFC |     |     | OK*          | 2700 |
| --- | ------ | ------------- | --- | --- | ------------ | ---- |
| 1/2 | N/A    | N/A           |     |     | Absent       | 0    |
| 1/3 | N/A    | N/A           |     |     | Input Fault  | 0    |
| 1/4 | JL372A | M031RM003JAFC |     |     | Output Fault | 0    |
* More than one active power supply required to supply full power to the switch
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show environment |                     |     |     | rear-display-module |            |     |
| ---------------- | ------------------- | --- | --- | ------------------- | ---------- | --- |
| show environment | rear-display-module |     |     |                     | [vsx-peer] |     |
Description
Showsinformationaboutthedisplaymoduleonthebackoftheswitch.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingthereardisplaymoduleinformationonthebackoftheswitch:
| switch>           | show environment |            |          | rear-display-module |        |     |
| ----------------- | ---------------- | ---------- | -------- | ------------------- | ------ | --- |
| Rear display      | module           |            | is ready |                     |        |     |
| Description:      | 8400             | Rear       | Display  |                     | Mod    |     |
| Full Description: |                  | 8400       | Rear     | Display             | Module |     |
| Serial            | number:          | SG00000000 |          |                     |        |     |
| Part number:      | 5300_0272        |            |          |                     |        |     |
| Command           | History          |            |          |                     |        |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 235

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show environment |             | temperature |            |
| ---------------- | ----------- | ----------- | ---------- |
| show environment | temperature | [detail]    | [vsx-peer] |
Description
Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
| Parameter |     |     | Description                                        |
| --------- | --- | --- | -------------------------------------------------- |
| detail    |     |     | Showsdetailedinformationfromeachtemperaturesensor. |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
TemperaturesareshowninCelsius.
Validvaluesforstatusarethefollowing:
normal
Sensoriswithinnominaltemperaturerange.
min
Lowesttemperaturefromthissensor.
max
Highesttemperaturefromthissensor.
low_critical
Lowestthresholdtemperatureforthissensor.
critical
Highestthresholdtemperatureforthissensor.
fault
Faulteventforthissensor.
emergency
Overtemperatureeventforthissensor.
Examples
Showingcurrenttemperatureinformationforan8400switch:
| switch# show | environment | temperature |     |
| ------------ | ----------- | ----------- | --- |
| Temperature  | information |             |     |
Switchsystemandhardwarecommands|236

------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     |     | Module Type | temperature | Status |
| --------------- | --- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-PCIE-Switch          |     |     | line-card-module | 95.82 C  | normal    |
| ------------------------ | --- | --- | ---------------- | -------- | --------- |
| 1/1-Processor            |     |     | line-card-module | 0.00 C   | fault     |
| 1/1-Switch-ASIC          |     |     | line-card-module | 116.36 C | emergency |
| 1/1-Switch-ASIC-Internal |     |     | line-card-module | 108.25 C | critical  |
| 1/2-PCIE-Switch          |     |     | line-card-module | 95.82 C  | normal    |
...
Showingdetailedtemperatureinformationforan8400switch:
| switch#  | show environment | temperature | detail |     |     |
| -------- | ---------------- | ----------- | ------ | --- | --- |
| Detailed | temperature      | information |        |     |     |
---------------------------------------------------
| Mbr/Slot-Sensor |             | : 1/1-PCIE-Switch  |                        |          |     |
| --------------- | ----------- | ------------------ | ---------------------- | -------- | --- |
| Module          | Type        | : line-card-module |                        |          |     |
| Module          | Description | : JL363A           | 8400X 32P 10G SFP/SFP+ | Msec Mod |     |
| Status          |             | : normal           |                        |          |     |
| Fan-state       |             | : normal           |                        |          |     |
| Current         | temperature | : 95.82            | C                      |          |     |
| Minimum         | temperature | : 93.52            | C                      |          |     |
| Maximum         | temperature | : 96.15            | C                      |          |     |
...
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show        | events          |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- |
| show events | [ -e <EVENT-ID> | |   |     |     |     |
-s {emergency | alert | critical | error | warning | notice | info | debug} |
-r |
-a |
| -n <COUNT>       | |          |                |     |     |     |
| ---------------- | ---------- | -------------- | --- | --- | --- |
| -i <MEMBER-SLOT> |            | |              |     |     |     |
| -m {active       | | standby} | |              |     |     |     |
| -c {lldp         | | ospf |   | ...} |         |     |     |     |
| -d {lldpd        | | bgpd     | | fand | ...}] |     |     |     |
Description
Showseventlogsgeneratedbytheswitchmodulessincethelastreboot.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 237

Parameter

-e <EVENT-ID>

Description

Shows the event logs for the specified event ID. Event ID
range: 101 through 99999.

-s {emergency | alert | critical |
error | warning | notice |
info | debug}

Shows the event logs for the specified severity. Select the
severity from the following list:
n emergency: Displays event logs with severity emergency

only.

n alert: Displays event logs with severity alert and above.
n critical: Displays event logs with severity critical and

above.

n error: Displays event logs with severity error and above.
n warning: Displays event logs with severity warning and

above.

n notice: Displays event logs with severity notice and above.
n info: Displays event logs with severity info and above.
n debug: Displays event logs with all severities.

Shows the most recent event logs first.

Shows all event logs, including those events from previous
boots.

-r

-a

-n <COUNT>

Displays the specified number of event logs.

-i <MEMBER-SLOT>

Shows the event logs for the specified slot ID.

-m {active | standby}

-c {lldp | ospf | ...}

-d {lldpd | bgpd | fand | ...}

Shows the event logs for the specified management card role.
Selecting active displays the event log for the AMM
management card role and standby displays event logs for
the SMM management card role.

Shows the event logs for the specified event category. Enter
show event -c for a full listing of supported categories with
descriptions.

Shows the event logs for the specified process. Enter show
event -d for a full listing of supported daemons with
descriptions.

Examples

Showing event logs:

switch# show events
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to

70:72:cf:51:50:7c

2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to

up for bridge_normal interface

2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1

in Hardware

Showing the most recent event logs first:

Switch system and hardware commands | 238

| switch# show | events | -r  |     |
| ------------ | ------ | --- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for | bridge_normal | interface |     |
| ------ | ------------- | --------- | --- |
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingalleventlogs:
| switch# show | events | -a  |     |
| ------------ | ------ | --- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for | bridge_normal | interface |     |
| ------ | ------------- | --------- | --- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
ShowingeventlogsrelatedtoLACP:
| switch# show | events | -c lacp |     |
| ------------ | ------ | ------- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingeventlogsasperthespecifiedmanagementcardrole:
| switch# show | events | -m active |     |
| ------------ | ------ | --------- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for | bridge_normal | interface |     |
| ------ | ------------- | --------- | --- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
Showingeventlogsasperthespecifiedmember/slotID:
| switch# show | events | -i 1/1 |     |
| ------------ | ------ | ------ | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2017-08-17:22:32:25.743991|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll | interval is changed | to 313 |
| ----------- | ---- | ------------------- | ------ |
2017-08-17:22:33:01.692860|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll | interval is changed | to 23 |
| ----------- | ---- | ------------------- | ----- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 239

2017-08-17:22:33:06.181436|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
|     | utilization |     | poll | interval | is changed | to 512 |
| --- | ----------- | --- | ---- | -------- | ---------- | ------ |
2017-08-17:22:33:06.181436|systemd-coredump|1201|LOG_CRIT|LC|1/1|hpe-sysmond
|     | crashed | due | to signal:11 |     |     |     |
| --- | ------- | --- | ------------ | --- | --- | --- |
Showingeventlogsasperthespecifiedprocess:
|     | switch# | show | events | -d lacpd |     |     |
| --- | ------- | ---- | ------ | -------- | --- | --- |
---------------------------------------------------
|     | show | event logs |     |     |     |     |
| --- | ---- | ---------- | --- | --- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Displayingthespecifiednumberofeventlogs:
|     | switch# | show | events | -n 5 |     |     |
| --- | ------- | ---- | ------ | ---- | --- | --- |
---------------------------------------------------
|     | show | event logs |     |     |     |     |
| --- | ---- | ---------- | --- | --- | --- | --- |
---------------------------------------------------
2018-03-21:06:12:15.500603|arpmgrd|6101|LOG_INFO|AMM|-|ARPMGRD daemon has started
2018-03-21:06:12:17.734405|lldpd|109|LOG_INFO|AMM|-|Configured LLDP tx-delay to 2
2018-03-21:06:12:17.740517|lacpd|1307|LOG_INFO|AMM|-|LACP system ID set to
70:72:cf:d4:34:42
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889
| Command        |     | History     |         |         |              |     |
| -------------- | --- | ----------- | ------- | ------- | ------------ | --- |
| Release        |     |             |         |         | Modification |     |
| 10.07orearlier |     |             |         |         | --           |     |
| Command        |     | Information |         |         |              |     |
| Platforms      |     |             | Command | context | Authority    |     |
Allplatforms AuditorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show |        | fabric      |     |            |     |     |
| ---- | ------ | ----------- | --- | ---------- | --- | --- |
| show | fabric | [<SLOT-ID>] |     | [vsx-peer] |     |     |
Description
Showsinformationabouttheinstalledfabrics.
Switchsystemandhardwarecommands|240

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<SLOT-ID> Specifiesthememberandslotofthefabrictoshow.Forexample,
toshowthemoduleinmember1,slot2,enterthefollowing:
1/2
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingallfabrics:
| switch# show   | fabric |     |     |     |     |     |
| -------------- | ------ | --- | --- | --- | --- | --- |
| Fabric Modules |        |     |     |     |     |     |
==============
| Product     |             |     |     |     | Serial |        |
| ----------- | ----------- | --- | --- | --- | ------ | ------ |
| Slot Number | Description |     |     |     | Number | Status |
---- ------- ---------------------------------- ---------- ------
| 1/1 JL367A | 8400X | 7.2Tbps | Fab | Mod | SG00000000 | Ready        |
| ---------- | ----- | ------- | --- | --- | ---------- | ------------ |
| 1/2 JL367A | 8400X | 7.2Tbps | Fab | Mod | SG00000000 | Initializing |
| 1/3 JL367A | 8400X | 7.2Tbps | Fab | Mod | SG00000000 | Initializing |
Showingasinglefabric:
| switch# show        | fabric  | 1/1        |               |              |        |     |
| ------------------- | ------- | ---------- | ------------- | ------------ | ------ | --- |
| Fabric module       | 1/1     | is ready   |               |              |        |     |
| Admin state:        | Up      |            |               |              |        |     |
| Description:        | 8400X   | 7.2Tbps    | Fab           | Mod          |        |     |
| Full Description:   |         | Aruba      | 8400X 7.2Tbps | Fabric       | Module |     |
| Serial number:      |         | SG00000000 |               |              |        |     |
| Product number:     |         | JL367A     |               |              |        |     |
| Command History     |         |            |               |              |        |     |
| Release             |         |            |               | Modification |        |     |
| 10.07orearlier      |         |            |               | --           |        |     |
| Command Information |         |            |               |              |        |     |
| Platforms           | Command | context    |               | Authority    |        |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
show hostname
| show hostname | [vsx-peer] |     |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- | --- |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 241

Description
Showsthecurrenthostname.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Settingandshowingthehostname:
| switch# show | hostname |     |     |
| ------------ | -------- | --- | --- |
switch
| switch# config    |          |          |     |
| ----------------- | -------- | -------- | --- |
| switch(config)#   | hostname | myswitch |     |
| myswitch(config)# | show     | hostname |     |
myswitch
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show images
| show images | [vsx-peer] |     |     |
| ----------- | ---------- | --- | --- |
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingtheprimaryandsecondaryimages:
Switchsystemandhardwarecommands|242

| switch# | show images |     |     |
| ------- | ----------- | --- | --- |
----------------------------------------------------------------------------
| AOS-CX | Primary Image |     |     |
| ------ | ------------- | --- | --- |
----------------------------------------------------------------------------
| Version | : XL.xx.xx.xxxx |          |     |
| ------- | --------------- | -------- | --- |
| Size    | : 141 MB        |          |     |
| Date    | : 2017-06-30    | 14:02:34 | PDT |
SHA-256 : 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
----------------------------------------------------------------------------
| AOS-CX | Secondary Image |     |     |
| ------ | --------------- | --- | --- |
----------------------------------------------------------------------------
| Version | : XL.xx.xx.xxxx |          |     |
| ------- | --------------- | -------- | --- |
| Size    | : 143 MB        |          |     |
| Date    | : 2017-06-30    | 14:02:34 | PDT |
SHA-256 : 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
| Default | Image : secondary |     |     |
| ------- | ----------------- | --- | --- |
------------------------------------------------------
| Management | Module | 1/5 (Active) |     |
| ---------- | ------ | ------------ | --- |
------------------------------------------------------
| Active       | Image      | : primary       |     |
| ------------ | ---------- | --------------- | --- |
| Service      | OS Version | : GT.01.01.0001 |     |
| BIOS Version |            | : GT-01-0013    |     |
------------------------------------------------------
| Management | Module | 1/6 (Standby) |     |
| ---------- | ------ | ------------- | --- |
------------------------------------------------------
| Active         | Image       | : secondary     |              |
| -------------- | ----------- | --------------- | ------------ |
| Service        | OS Version  | : GT.01.01.0001 |              |
| BIOS Version   |             | : GT-01-0013    |              |
| Command        | History     |                 |              |
| Release        |             |                 | Modification |
| 10.07orearlier |             |                 | --           |
| Command        | Information |                 |              |
| Platforms      | Command     | context         | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show ip        | errors     |     |     |
| -------------- | ---------- | --- | --- |
| show ip errors | [vsx-peer] |     |     |
Description
ShowsIPerrorstatisticsforpacketsreceivedbytheswitchsincetheswitchwaslastbooted.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 243

| Parameter |     | Description |
| --------- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
IPerrorinfoaboutreceivedpacketsiscollectedfromeachactivelinecardontheswitchandis
preservedduringfailoverevents.Errorcountsareclearedwhentheswitchisrebooted.
Dropreasonsarethefollowing:
| n Malformed | packet |     |
| ----------- | ------ | --- |
ThepacketdoesnotconformtoTCP/IPprotocolstandardssuchaspacketlengthorinternetheaderlength.
Alargenumberofmalformedpacketscanindicatethattherearehardwaremalfunctionssuchasloosecables,
networkcardmalfunctions,orthataDOS(denialofservice)attackisoccurring.
| n IP address | error |     |
| ------------ | ----- | --- |
ThepackethasanerrorinthedestinationorsourceIPaddress.ExamplesofIPaddresserrorsincludethe
following:
o ThesourceIPaddressanddestinationIPaddressarethesame.
o
ThereisnodestinationIPaddress.
o ThesourceIPaddressisamulticastIPaddress.
o TheforwardingheaderofanIPv6addressisempty.
o ThereisnosourceIPaddressforanIPv6packet.
n Invalid TTLs
TheTTL(timetolive)valueofthepacketreachedzero.Thepacketwasdiscardedbecauseittraversedthe
maximumnumberofhopspermittedbytheTTLvalue.
TTLsareusedtopreventpacketsfrombeingcirculatedonthenetworkendlessly.
Example
Showingiperrorstatisticsforpacketsreceivedbytheswitch:
| switch# | show ip errors |     |
| ------- | -------------- | --- |
----------------------------------
| Drop reason | Packets |     |
| ----------- | ------- | --- |
----------------------------------
| Malformed  | packets | 1   |
| ---------- | ------- | --- |
| IP address | errors  | 10  |
...
| Command        | History     |              |
| -------------- | ----------- | ------------ |
| Release        |             | Modification |
| 10.07orearlier |             | --           |
| Command        | Information |              |
Switchsystemandhardwarecommands|244

Platforms

Command context

Authority

8400

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show module
show module [<SLOT-ID>] [vsx-peer]

Description

Shows information about installed line modules and management modules.

Parameter

<SLOT-ID>

vsx-peer

Usage

Description

Specifies the member and slot numbers in format
member/slot. For example, to show the module in
member 1, slot 3, enter 1/3.

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

Identifies and shows status information about the line modules and management modules that are
installed in the switch.

If you use the <SLOT-ID> parameter to specify a slot that does not have a line module installed, a
message similar to the following example is displayed:

Module 1/4 is not physically present.

To show the configuration information—if any—associated with that line module slot, use the show
running-configuration command.

Status is one of the following values:
Active
This module is the active management module.
Standby

This module is the standby management module.

Deinitializing
The module is being deinitialized.
Diagnostic
The module is in a state used for troubleshooting.
Down
The module is physically present but is powered down.
Empty

The module hardware is not installed in the chassis.

Failed
The module has experienced an error and failed.
Failover

This module is a fabric module or a line module, and it is in the process of connecting to the new
active management module during a management module failover event.

Initializing
The module is being initialized.

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

245

Present
Themodulehardwareisinstalledinthechassis.
Ready
Themoduleisavailableforuse.
Updating
Afirmwareupdateisbeingappliedtothemodule.
Examples
Showingallinstalledmodules:
| switch#    | show module |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
| Management | Modules     |     |     |     |     |     |
==================
| Product     |             |     |     |     | Serial |        |
| ----------- | ----------- | --- | --- | --- | ------ | ------ |
| Slot Number | Description |     |     |     | Number | Status |
---- ------- ---------------------------------- ---------- ------
| 1/5 JL368A | 8400 | Mgmt | Mod |     | SG00000000 | Active  |
| ---------- | ---- | ---- | --- | --- | ---------- | ------- |
| 1/6 JL368A | 8400 | Mgmt | Mod |     | SG00000000 | Standby |
Line Modules
=================
| Product     |             |     |     |     | Serial |        |
| ----------- | ----------- | --- | --- | --- | ------ | ------ |
| Slot Number | Description |     |     |     | Number | Status |
---- ------- ---------------------------------- ---------- ------
| 1/1 JL363A | 8400X | 32P    | 10G SFP/SFP+ | Msec Mod | SG00000000 | Down  |
| ---------- | ----- | ------ | ------------ | -------- | ---------- | ----- |
| 1/3 JL365A | 8400X | 8P 40G | QSFP+        | Adv Mod  | SG00000000 | Ready |
1/4 JL366A 8400X 6P 40G/100G QSFP28 Adv Mod SG00000000 Initializing
| 1/8 JL365A  | 8400X | 8P 40G | QSFP+ | Adv Mod | SG00000000 | Ready |
| ----------- | ----- | ------ | ----- | ------- | ---------- | ----- |
| 1/10 JL365A | 8400X | 8P 40G | QSFP+ | Adv Mod | SG00000000 | Ready |
...
Showingamanagementmodule:
| switch#           | show module | 1/5        |            |        |     |     |
| ----------------- | ----------- | ---------- | ---------- | ------ | --- | --- |
| Management        | module      | 1/5 is     | active     |        |     |     |
| Admin state:      | Up          |            |            |        |     |     |
| Description:      | 8400        | Mgmt       | Mod        |        |     |     |
| Full Description: |             | 8400       | Management | Module |     |     |
| Serial number:    |             | SG00000000 |            |        |     |     |
| Product           | number:     | JL368A     |            |        |     |     |
Showingaslotthatdoesnotcontainalinemodule:
| switch(config)# |        | show module | 1/3     |     |     |     |
| --------------- | ------ | ----------- | ------- | --- | --- | --- |
| Module 1/3      | is not | physically  | present |     |     |     |
Showingalinemoduleafterremovingitfromtheconfigurationwithno modulecommand,butthe
hardwareremainsinstalledintheslot:
| switch(config)# |     | show module | 1/1 |     |     |     |
| --------------- | --- | ----------- | --- | --- | --- | --- |
| Line module     | 1/1 | is ready    |     |     |     |     |
Switchsystemandhardwarecommands|246

| Admin state: |     | Up    |         |          |          |
| ------------ | --- | ----- | ------- | -------- | -------- |
| Description: |     | 8400X | 32P 10G | SFP/SFP+ | Msec Mod |
Full Description: 8400X 32-port 10GbE SFP/SFP+ with MACsec Advanced Module
| Serial number:      |         | SG00000000 |         |     |              |
| ------------------- | ------- | ---------- | ------- | --- | ------------ |
| Product number:     |         | JL363A     |         |     |              |
| Command History     |         |            |         |     |              |
| Release             |         |            |         |     | Modification |
| 10.07orearlier      |         |            |         |     | --           |
| Command Information |         |            |         |     |              |
| Platforms           | Command |            | context |     | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show running-config |     |             |     |       |            |
| ------------------- | --- | ----------- | --- | ----- | ---------- |
| show running-config |     | [<FEATURE>] |     | [all] | [vsx-peer] |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<FEATURE>
Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).Whenthejsonparameteris
used,thevsx-peerparameterisnotapplicable.
| all |     |     |     |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |
| --- | --- | --- | --- | --- | ------------------------------------------------------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthecurrentrunningconfiguration:
| switch> show           |     | running-config |     |     |     |
| ---------------------- | --- | -------------- | --- | --- | --- |
| Current configuration: |     |                |     |     |     |
!
| !Version | AOS-CX | 10.0X.XXXX |     |     |     |
| -------- | ------ | ---------- | --- | --- | --- |
!
| lldp enable     |     |     |             |     |        |
| --------------- | --- | --- | ----------- | --- | ------ |
| linecard-module |     | LC1 | part-number |     | JL363A |
vrf green
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 247

!
!
!
!
!
!
| aaa authentication |     | login    | default | local |
| ------------------ | --- | -------- | ------- | ----- |
| aaa authorization  |     | commands | default | none  |
!
!
!
!
vlan 1
no shutdown
vlan 20
no shutdown
vlan 30
no shutdown
| interface | 1/1/1 |     |     |     |
| --------- | ----- | --- | --- | --- |
no shutdown
no routing
| vlan access |        | 30  |     |     |
| ----------- | ------ | --- | --- | --- |
| interface   | 1/1/32 |     |     |     |
no shutdown
no routing
| vlan access |                 | 20  |     |     |
| ----------- | --------------- | --- | --- | --- |
| interface   | bridge_normal-1 |     |     |     |
no shutdown
| interface | bridge_normal-2 |     |     |     |
| --------- | --------------- | --- | --- | --- |
no shutdown
| interface | vlan20 |     |     |     |
| --------- | ------ | --- | --- | --- |
no shutdown
| vrf attach    | green        |         |     |     |
| ------------- | ------------ | ------- | --- | --- |
| ip address    | 20.0.0.44/24 |         |     |     |
| ip ospf       | 1 area       | 0.0.0.0 |     |     |
| ip pim-sparse |              | enable  |     |     |
| interface     | vlan30       |         |     |     |
no shutdown
| vrf attach    | green        |                |     |     |
| ------------- | ------------ | -------------- | --- | --- |
| ip address    | 30.0.0.44/24 |                |     |     |
| ip ospf       | 1 area       | 0.0.0.0        |     |     |
| ip pim-sparse |              | enable         |     |     |
| ip pim-sparse |              | hello-interval |     | 100 |
Showingthecurrentrunningconfigurationinjsonformat:
| switch> show          | running-config |     | json  |     |
| --------------------- | -------------- | --- | ----- | --- |
| Running-configuration |                | in  | JSON: |     |
{
| "Monitoring_Policy_Script": |     |     |     | {   |
| --------------------------- | --- | --- | --- | --- |
"system_resource_monitor_mm1.1.0": {
|     | "Monitoring_Policy_Instance": |     |     | {   |
| --- | ----------------------------- | --- | --- | --- |
"system_resource_monitor_mm1.1.0/system_resource_monitor_
| mm1.1.0.default": |     | {                    |                                            |     |
| ----------------- | --- | -------------------- | ------------------------------------------ | --- |
|                   |     | "name":              | "system_resource_monitor_mm1.1.0.default", |     |
|                   |     | "origin":            | "system",                                  |     |
|                   |     | "parameters_values": |                                            | {   |
"long_term_high_threshold": "70",
"long_term_normal_threshold": "60",
Switchsystemandhardwarecommands|248

"long_term_time_period": "480",
"medium_term_high_threshold": "80",
"medium_term_normal_threshold": "60",
"medium_term_time_period": "120",
"short_term_high_threshold": "90",
"short_term_normal_threshold": "80",
"short_term_time_period": "5"

}

}

},

...
...
...
...

Show the current running configuration without default values:

switch(config)# show running-config
Current configuration:
!
!Version AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!
!
!
!
!
!
!
!
vlan 1
switch(config)# show running-config all
Current configuration:
!
!Version AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!
!
!
!
!
!
!
!
vlan 1
switch(config)#

Show the current running configuration with default values:

switch(config)# snmp-server vrf mgmt
switch(config)# show running-config
Current configuration:
!
!Version AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

249

!
!
| snmp-server | vrf mgmt |     |     |
| ----------- | -------- | --- | --- |
!
!
!
!
!
vlan 1
switch(config)#
switch(config)#
| switch(config)#        | show | running-config | all |
| ---------------------- | ---- | -------------- | --- |
| Current configuration: |      |                |     |
!
| !Version    | AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| led locator | on                                            |     |     |
!
!
!
!
| snmp-server | vrf mgmt   |        |     |
| ----------- | ---------- | ------ | --- |
| snmp-server | agent-port | 161    |     |
| snmp-server | community  | public |     |
!
!
!
!
!
vlan 1
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show running-config |                 | current-context |     |
| ------------------- | --------------- | --------------- | --- |
| show running-config | current-context |                 |     |
Description
Showsthecurrentnon-defaultconfigurationrunningontheswitchinthecurrentcommandcontext.
Usage
Youcanenterthiscommandfromthefollowingconfigurationcontexts:
n Anychildoftheglobalconfiguration(config)context.Ifthechildcontexthasinstances—suchas
interfaces—youcanenterthecommandinthecontextofaspecificinstance.Supportforthis
Switchsystemandhardwarecommands|250

commandisprovidedforonelevelbelowtheconfigcontext.Forexample,enteringthiscommand
forachildofachildoftheconfigcontextnotsupported.Ifyouenterthecommandonachildofthe
configcontext,thecurrentconfigurationofthatcontextandthechildrenofthatcontextare
displayed.
Theglobalconfiguration(config)context.Ifyouenterthiscommandintheglobalconfiguration
n
(config)context,itshowstherunningconfigurationoftheentireswitch.Usetheshow running-
configurationcommandinstead.
Examples
Showingtherunningconfigurationforthecurrentinterface:
| switch(config-if)# | show running-config | current-context |
| ------------------ | ------------------- | --------------- |
interface 1/1/1
| vsx-sync qos vlans |     |     |
| ------------------ | --- | --- |
no shutdown
| description | Example interface |     |
| ----------- | ----------------- | --- |
no routing
| vlan access 1 |     |     |
| ------------- | --- | --- |
exit
Showingthecurrentrunningconfigurationforthemanagementinterface:
| switch(config-if-mgmt)# | show running-config | current-context |
| ----------------------- | ------------------- | --------------- |
interface mgmt
no shutdown
| ip static 10.0.0.1/24 |          |     |
| --------------------- | -------- | --- |
| default-gateway       | 10.0.0.8 |     |
| nameserver 10.0.0.1   |          |     |
Showingtherunningconfigurationfortheexternalstoragesharenamednasfiles:
switch(config-external-storage-nasfiles)#
show running-config current-context
| external-storage | nasfiles |     |
| ---------------- | -------- | --- |
address 192.168.0.1
vrf default
| username nasuser    |     |     |
| ------------------- | --- | --- |
| password ciphertext |     |     |
AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
type scp
| directory /home/nas |     |     |
| ------------------- | --- | --- |
enable
switch(config-external-storage-nasfiles)#
Showingtherunningconfigurationforacontextthatdoesnothaveinstances:
| switch(config-vsx)# | show run current-context |     |
| ------------------- | ------------------------ | --- |
vsx
| inter-switch-link | 1/1/1 |     |
| ----------------- | ----- | --- |
role secondary
| vsx-sync sflow | time |     |
| -------------- | ---- | --- |
Command History
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 251

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms configorachildof Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
config.SeeUsage.
show startup-config
| show startup-config | [json] |     |     |
| ------------------- | ------ | --- | --- |
Description
Showsthecontentsofthestartupconfiguration.
Switchesinthefactory-defaultconfigurationdonothaveastartupconfigurationtodisplay.
| Parameter |     |     | Description                |
| --------- | --- | --- | -------------------------- |
| json      |     |     | DisplayoutputinJSONformat. |
Examples
Showingthestartup-configurationinnon-JSONformat:
| switch# | show startup-config |     |     |
| ------- | ------------------- | --- | --- |
| Startup | configuration:      |     |     |
!
| !Version          | AOS-CX XL.xx.xx.xxxx |     |     |
| ----------------- | -------------------- | --- | --- |
| !export-password: | default              |     |     |
| hostname          | BLDG03-F1            |     |     |
user admin group administrators password ciphertext AQBapfYzQNiCPJ/
JNSu7YNfaCzlWEnWFlwLfkARd8OG6yPpcYgAAABXRe9joTRtF1S1b4b09teMfMN3POKdQk+
br6SjSXGG40BB3ilZ8ym9qqSRkr84FEdq6w5uR2IGciVC5tBnZMrWCim0KR20XcQ5rFj/TMBvTkHq8bJpS
YG8nMh
| module 1/3 | product-number | jl365a |     |
| ---------- | -------------- | ------ | --- |
| module 1/1 | product-number | jl363a |     |
| module 1/2 | product-number | jl363a |     |
cli-session
| timeout | 0   |     |     |
| ------- | --- | --- | --- |
!
!
!
| ssh server | vrf mgmt |     |     |
| ---------- | -------- | --- | --- |
ssh certified-algorithms-only
!
!
!
!
!
Switchsystemandhardwarecommands|252

vlan 1,195,197-200,4000
| interface       | mgmt             |            |            |
| --------------- | ---------------- | ---------- | ---------- |
| no shutdown     |                  |            |            |
| ip static       | 10.6.9.24/24     |            |            |
| default-gateway |                  | 10.6.9.1   |            |
| interface       | 1/1/1            |            |            |
| no shutdown     |                  |            |            |
| no routing      |                  |            |            |
| vlan            | trunk native     | 1          |            |
| vlan            | trunk allowed    | 1,197-200  |            |
| interface       | vlan200          |            |            |
| ip address      | 10.3.200.3/24    |            |            |
| ip route        | 0.0.0.0/0        | 10.3.200.1 |            |
| https-server    | rest access-mode |            | read-write |
| https-server    | vrf mgmt         |            |            |
Showingthestartup-configurationinJSONformat:
| switch# show           | startup-config |     | json |
| ---------------------- | -------------- | --- | ---- |
| Startup configuration: |                |     |      |
{
| "AAA_Server_Group": |     | {   |     |
| ------------------- | --- | --- | --- |
"local": {
|     | "group_name": | "local" |     |
| --- | ------------- | ------- | --- |
},
"none": {
|     | "group_name": | "none" |     |
| --- | ------------- | ------ | --- |
}
},
...
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show system | error-counter-monitor |     |     |
| ----------- | --------------------- | --- | --- |
show system error-counter-monitor {basic <PORT-NUM> | extended} [vsx-peer]
Description
Showserrorcounterstatistics.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 253

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
basic <PORT-NUM> Specifiesaphysicalportontheswitch.Usetheformat
member/slot/port(forexample,1/3/1).
| extended |     |     | Showsstatisticsforallinterfaces. |
| -------- | --- | --- | -------------------------------- |
Examples
Showingerrorcounterstatisticsforinterface1/1/1:
| switch#       | show system error-counter-monitor |            | basic 1/1/1 |
| ------------- | --------------------------------- | ---------- | ----------- |
| Interface     | error counter                     | statistics | for 1/1/1   |
| Error Counter |                                   |            | Value       |
-----------------------------------------
| EtherStatsOversizePkts       |     |     | 983  |
| ---------------------------- | --- | --- | ---- |
| EtherStatsUndersizePkts      |     |     | 1024 |
| EtherStatsJabbers            |     |     | 10   |
| Dot3StatsAlignmentErrors     |     |     | 462  |
| Dot3StatsFCSErrors           |     |     | 321  |
| Dot3StatsLateCollisions      |     |     | 2024 |
| EtherStatsFragments          |     |     | 121  |
| Dot3StatsExcessiveCollisions |     |     | 1025 |
| IfInBroadcastPkts            |     |     | 2001 |
Showingerrorcounterstatisticsforallinterfaces:
| switch#       | show system error-counter-monitor |            | extended  |
| ------------- | --------------------------------- | ---------- | --------- |
| Interface     | error counter                     | statistics | for 1/1/1 |
| Error Counter |                                   |            | Value     |
-----------------------------------------
| EtherStatsOversizePkts       |     |     | 983  |
| ---------------------------- | --- | --- | ---- |
| EtherStatsUndersizePkts      |     |     | 1024 |
| EtherStatsJabbers            |     |     | 10   |
| Dot3StatsAlignmentErrors     |     |     | 462  |
| Dot3StatsFCSErrors           |     |     | 321  |
| Dot3StatsLateCollisions      |     |     | 2024 |
| EtherStatsFragments          |     |     | 121  |
| Dot3StatsExcessiveCollisions |     |     | 1025 |
| IfInBroadcastPkts            |     |     | 2001 |
...
...
| Interface     | error counter | statistics | for 1/8/32 |
| ------------- | ------------- | ---------- | ---------- |
| Error Counter |               |            | Value      |
-----------------------------------------
| EtherStatsOversizePkts |     |     | 0   |
| ---------------------- | --- | --- | --- |
...
| Command | History |     |     |
| ------- | ------- | --- | --- |
Switchsystemandhardwarecommands|254

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show system
| show system | [vsx-peer] |     |     |     |
| ----------- | ---------- | --- | --- | --- |
Description
Showsgeneralstatusinformationaboutthesystem.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemContact,SystemLocation,andSystemDescriptioncanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformation:
| switch# show       | system          |                       |          |              |
| ------------------ | --------------- | --------------------- | -------- | ------------ |
| Hostname           |                 | : switch              |          |              |
| System Description |                 | : My switch           |          |              |
| System Contact     |                 | : John Doe            |          |              |
| System Location    |                 | : ROS-R3-UPR-R10      |          |              |
| Vendor             |                 | : Aruba               |          |              |
| Product            | Name            | : 8400 Base           | Cbl Mgr  | X462 Bndl    |
| Chassis            | Serial Nbr      | : SGYMK2G001          |          |              |
| Base MAC           | Address         | : 00:00:5E:00:53:05   |          |              |
| AOS-CX Version     | : XL.10.xx.xxxx |                       |          |              |
| Time Zone          |                 | : America/Los_Angeles |          | (PDT, -0700) |
| Up Time            |                 | : up 1 week,          | 5 hours, | 28 minutes   |
| CPU Util           | (%)             | : 5                   |          |              |
| Memory Usage       | (%)             | : 35                  |          |              |
| Command History    |                 |                       |          |              |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 255

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show system | resource-utilization |     |     |
| ----------- | -------------------- | --- | --- |
show system resource-utilization [daemon <DAEMON-NAME> | module <SLOT-ID> | standby]
[vsx-peer]
Description
ShowsinformationabouttheusageofsystemresourcessuchasCPU,memory,andopenfile
descriptors.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
daemon <DAEMON-NAME> Showsthefilteredresourceutilizationdatafortheprocess
specifiedby<DAEMON-NAME> only.
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
NOTE:
Foralistofdaemonsthatlogevents,entershow events -d
?fromaswitchpromptinthemanager(#)context.
module <SLOT-ID> Showsthefilteredresourceutilizationdataforthelinemodule
specifiedby<SLOT-ID>only.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingallsystemresourceutilizationdata:
| switch# show      | system | resource-utilization |     |
| ----------------- | ------ | -------------------- | --- |
| System Resources: |        |                      |     |
| Processes:        | 70     |                      |     |
| CPU usage(%):     | 20     |                      |     |
| Memory usage(%):  | 25     |                      |     |
| Open FD's:        | 1024   |                      |     |
Switchsystemandhardwarecommands|256

| Process |     |     | CPU | Usage(%) |     | Memory |     | Usage(%) | Open FD's |
| ------- | --- | --- | --- | -------- | --- | ------ | --- | -------- | --------- |
-----------------------------------------------------------------------
| pmd         |     |     |     | 2   |     |     | 1   |     | 14  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hpe-sysmond |     |     |     | 1   |     |     | 2   |     | 11  |
| hpe-mgmdd   |     |     |     | 0   |     |     | 1   |     | 5   |
...
Showingtheresourceutilizationdataforthepmdprocess:
| switch# | show | system | resource-utilization |       |     | daemon |       | pmd  |      |
| ------- | ---- | ------ | -------------------- | ----- | --- | ------ | ----- | ---- | ---- |
| Process |      |        | CPU                  | Usage |     | Memory | Usage | Open | FD's |
-----------------------------------------------------------------------
| pmd |     |     |     | 2   |     | 1   |     | 14  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# | show     | system      | resource-utilization |      |      |              |     |          |     |
| ------- | -------- | ----------- | -------------------- | ---- | ---- | ------------ | --- | -------- | --- |
| System  | resource | utilization |                      | data | poll | is currently |     | disabled |     |
Showingresourceutilizationdataforalinemodule:
| switch#        | show        | system      | resource-utilization |     |              | module  |     | 1/1 |     |
| -------------- | ----------- | ----------- | -------------------- | --- | ------------ | ------- | --- | --- | --- |
| System         | Resource    | utilization |                      | for | line card    | module: |     | 1/1 |     |
| CPU            | usage(%):   | 0           |                      |     |              |         |     |     |     |
| Memory         | usage(%):   |             | 35                   |     |              |         |     |     |     |
| Open           | FD's:       | 512         |                      |     |              |         |     |     |     |
| Command        | History     |             |                      |     |              |         |     |     |     |
| Release        |             |             |                      |     | Modification |         |     |     |     |
| 10.07orearlier |             |             |                      |     | --           |         |     |     |     |
| Command        | Information |             |                      |     |              |         |     |     |     |
| Platforms      |             | Command     | context              |     | Authority    |         |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | tech   |              |     |              |     |     |     |     |     |
| --------- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- |
| show tech | [basic | | <FEATURE>] |     | [local-file] |     |     |     |     |     |
Description
Showsdetailedinformationaboutswitchfeaturesbyautomaticallyrunningtheshowcommands
associatedwiththefeature.Ifnoparametersarespecified,theshow techcommandshowsinformation
aboutallswitchfeatures.Technicalsupportpersonnelusetheoutputfromthiscommandfor
troubleshooting.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 257

| Parameter |     |     | Description                             |
| --------- | --- | --- | --------------------------------------- |
| basic     |     |     | Specifiesshowingabasicsetofinformation. |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow techcommand,followedbyaspace,followedbya
questionmark(?).
local-file
Showstheoutputoftheshow techcommandtoalocaltextfile.
Usage
| Toterminatetheoutputoftheshow |     | techcommand,enterCtrl+C. |     |
| ----------------------------- | --- | ------------------------ | --- |
IfthecommandwasnotterminatedwithCtrl+C,attheendoftheoutput,theshow techcommand
showsthefollowing:
n Thetimeconsumedtoexecutethecommand.
n Thelistoffailedshowcommands,ifany.
Togetacopyofthelocaltextfilecontentcreatedwiththeshowtechcommandthatisusedwiththe
| local-fileparameter,usethecopy |     |     | local-filecommand. |
| ------------------------------ | --- | --- | ------------------ |
show-tech
Example
Showingthebasicsetofsysteminformation:
| switch# | show tech basic |     |     |
| ------- | --------------- | --- | --- |
=============================================================
| Show Tech | executed | on Wed Sep | 6 16:50:37 2017 |
| --------- | -------- | ---------- | --------------- |
=============================================================
=============================================================
| [Begin] | Feature basic |     |     |
| ------- | ------------- | --- | --- |
=============================================================
*******************************
| Command | : show core-dump | all |     |
| ------- | ---------------- | --- | --- |
*******************************
| no core | dumps are present |     |     |
| ------- | ----------------- | --- | --- |
...
=============================================================
| [End] Feature | basic |     |     |
| ------------- | ----- | --- | --- |
=============================================================
=============================================================
| 1 show | tech command | failed |     |
| ------ | ------------ | ------ | --- |
=============================================================
Failed command:
| 1. show | boot-history |     |     |
| ------- | ------------ | --- | --- |
=============================================================
| Show tech | took 3.000000 | seconds | for execution |
| --------- | ------------- | ------- | ------------- |
Directingtheoutputoftheshow tech basiccommandtothelocaltextfile:
| switch# | show tech basic | local-file |     |
| ------- | --------------- | ---------- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
| to copy-out | this file. |     |     |
| ----------- | ---------- | --- | --- |
Switchsystemandhardwarecommands|258

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show usb
show usb [vsx-peer]
Description
ShowstheUSBportconfigurationandmountsettings.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
IfUSBhasnotbeenenabled:
| switch> show | usb |     |     |
| ------------ | --- | --- | --- |
| Enabled:     | No  |     |     |
| Mounted:     | No  |     |     |
IfUSBhasbeenenabled,butnodevicehasbeenmounted:
| switch> show | usb |     |     |
| ------------ | --- | --- | --- |
| Enabled:     | Yes |     |     |
| Mounted:     | No  |     |     |
IfUSBhasbeenenabledandadevicemounted:
| switch> show    | usb |     |     |
| --------------- | --- | --- | --- |
| Enabled:        | Yes |     |     |
| Mounted:        | Yes |     |     |
| Command History |     |     |     |
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 259

| Release        |             |         | Modification |     |
| -------------- | ----------- | ------- | ------------ | --- |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show usb             | file-system |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| show usb file-system | [<PATH>]    |     |     |     |
Description
ShowsdirectorylistingsforamountedUSBdevice.Whenenteredwithoutthe<PATH>parameterthe
topleveldirectorytreeisshown.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PATH> Specifiesthefilepathtoshow.Aleading"/"inthepathisoptional.
Usage
Addingaleading"/"asthefirstcharacterofthe<PATH>parameterisoptional.
Attemptingtoenter'..'asanypartofthe<PATH>willgenerateaninvalidpathargumenterror.Only
fully-qualifiedpathnamesaresupported.
Examples
Showingthetopleveldirectorytree:
| switch# | show usb file-system |     |     |     |
| ------- | -------------------- | --- | --- | --- |
/mnt/usb:
| 'System           | Volume Information' |                | dir1' |     |
| ----------------- | ------------------- | -------------- | ----- | --- |
| /mnt/usb/System   | Volume              | Information':  |       |     |
| IndexerVolumeGuid |                     | WPSettings.dat |       |     |
/mnt/usb/dir1:
| dir2 test1 |     |     |     |     |
| ---------- | --- | --- | --- | --- |
/mnt/usb/dir1/dir2:
test2
Showingavailablepathoptionsfromthetoplevel:
| switch#    | show usb file-system |        | /             |                     |
| ---------- | -------------------- | ------ | ------------- | ------------------- |
| total 64   |                      |        |               |                     |
| drwxrwxrwx | 2 32768              | Jan 22 | 16:27 'System | Volume Information' |
| drwxrwxrwx | 3 32768              | Mar 5  | 15:26 dir1    |                     |
Switchsystemandhardwarecommands|260

Showingthecontentsofaspecificfolder:
| switch#    | show usb file-system |         | /dir1       |
| ---------- | -------------------- | ------- | ----------- |
| total 32   |                      |         |             |
| drwxrwxrwx | 2 32768              | Mar 5   | 15:26 dir2  |
| -rwxrwxrwx | 1 0                  | Feb 5   | 18:08 test1 |
| switch#    | show usb file-system |         | dir1/dir2   |
| total 0    |                      |         |             |
| -rwxrwxrwx | 1 0 Feb              | 6 05:35 | test2       |
Attemptingtoenteraninvalidcharacterinthepath:
| switch#        | show usb file-system |         | dir1/../..   |
| -------------- | -------------------- | ------- | ------------ |
| Invalid        | path argument        |         |              |
| Command        | History              |         |              |
| Release        |                      |         | Modification |
| 10.07orearlier |                      |         | --           |
| Command        | Information          |         |              |
| Platforms      | Command              | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show version
| show version | [vsx-peer] |     |     |
| ------------ | ---------- | --- | --- |
Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingversioninformation:
| switch> | show version |     |     |
| ------- | ------------ | --- | --- |
-----------------------------------------------------------------------------
AOS-CX
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 261

| (c) Copyright | 2022 | Hewlett Packard | Enterprise | Development | LP  |
| ------------- | ---- | --------------- | ---------- | ----------- | --- |
-----------------------------------------------------------------------------
| Version        | : XL.xx.xx.xxxx                                  |                 |              |     |     |
| -------------- | ------------------------------------------------ | --------------- | ------------ | --- | --- |
| Build Date     | : 2022-05-27                                     | 17:00:46        | PDT          |     |     |
| Build ID       | : AOS-CX:XL.xx.xx.xxxx:2b4032a4282b:201707241803 |                 |              |     |     |
| Build SHA      | : 2b4032a4282b47ab94ea92a1436e1194f34bb5ba       |                 |              |     |     |
| Active Image   | : secondary                                      |                 |              |     |     |
| Service        | OS Version                                       | : GT.01.01.0010 |              |     |     |
| BIOS Version   |                                                  | : GT-01-0020    |              |     |     |
| Command        | History                                          |                 |              |     |     |
| Release        |                                                  |                 | Modification |     |     |
| 10.07orearlier |                                                  |                 | --           |     |     |
| Command        | Information                                      |                 |              |     |     |
| Platforms      | Command                                          | context         | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| system | error-counter-monitor |     |     |     |     |
| ------ | --------------------- | --- | --- | --- | --- |
system error-counter-monitor
| no system error-counter-monitor |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- |
Description
Enablesthesystemerrorcountermonitoringfeature,whichrecordserrorcounterdataevery10
seconds.Default:Disabled.
Thenoformofthecommanddisableserrorcountermonitoringandstopstherecordingoferror
counterdata.
Example
Enablingthesystemerrorcountermonitor:
| switch(config)# | system      | error-counter-monitor |              |     |     |
| --------------- | ----------- | --------------------- | ------------ | --- | --- |
| Command         | History     |                       |              |     |     |
| Release         |             |                       | Modification |     |     |
| 10.07orearlier  |             |                       | --           |     |     |
| Command         | Information |                       |              |     |     |
Switchsystemandhardwarecommands|262

| Platforms | Command |     | context | Authority |     |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- | --- |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| system                       | error-counter-monitor |     |               |     |            | poll-interval |     |
| ---------------------------- | --------------------- | --- | ------------- | --- | ---------- | ------------- | --- |
| system error-counter-monitor |                       |     | poll-interval |     | <INTERVAL> |               |     |
Description
Setsthepollingintervalusedforthecollectionandrecordingoferrorcounterdata.
| Parameter  |     |     |     | Description                                       |     |     |     |
| ---------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
| <INTERVAL> |     |     |     | Specifiesthepollintervalinseconds.Range:10to3600. |     |     |     |
Default:10.
Example
Settingthesystemerrorcountermonitorpollinterval:
| switch(config)# |             | system | error-counter-monitor |              |     | poll-interval | 20  |
| --------------- | ----------- | ------ | --------------------- | ------------ | --- | ------------- | --- |
| Command         | History     |        |                       |              |     |               |     |
| Release         |             |        |                       | Modification |     |               |     |
| 10.07orearlier  |             |        |                       | --           |     |               |     |
| Command         | Information |        |                       |              |     |               |     |
| Platforms       | Command     |        | context               | Authority    |     |               |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| system                      | resource-utilization |     |               |     | poll-interval |     |     |
| --------------------------- | -------------------- | --- | ------------- | --- | ------------- | --- | --- |
| system resource-utilization |                      |     | poll-interval |     | <SECONDS>     |     |     |
Description
ConfiguresthepollingintervalforsystemresourceinformationcollectionandrecordingsuchasCPU
andmemoryusage.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<SECONDS> Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Example
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 263

Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |             | system | resource-utilization |     |              |     | poll-interval |     | 20  |     |
| --------------- | ----------- | ------ | -------------------- | --- | ------------ | --- | ------------- | --- | --- | --- |
| Command         | History     |        |                      |     |              |     |               |     |     |     |
| Release         |             |        |                      |     | Modification |     |               |     |     |     |
| 10.07orearlier  |             |        |                      |     | --           |     |               |     |     |     |
| Command         | Information |        |                      |     |              |     |               |     |     |     |
| Platforms       | Command     |        | context              |     | Authority    |     |               |     |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
top cpu
top cpu
Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch# | top cpu |     |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
| Tasks: | 76 total, | 2   | running, | 74  | sleeping, |     | 0 stopped, |     | 0 zombie |     |
| ------ | --------- | --- | -------- | --- | --------- | --- | ---------- | --- | -------- | --- |
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used, 661948 buff/cache
| KiB Swap: |     | 0 total, |         |     | 0 free, |     | 0      | used, | 2859196 | avail Mem     |
| --------- | --- | -------- | ------- | --- | ------- | --- | ------ | ----- | ------- | ------------- |
| PID USER  |     | PRI      | NI VIRT |     | RES     | SHR | S %CPU | %MEM  |         | TIME+ COMMAND |
...
| Command        | History     |     |         |     |              |     |     |     |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
| Release        |             |     |         |     | Modification |     |     |     |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |     |     |     |
| Command        | Information |     |         |     |              |     |     |     |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Switchsystemandhardwarecommands|264

top memory
top memory
Description
Showsmemoryutilizationinformation.
Example
Showingtopmemory:
| switch> | top memory |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
| Tasks: | 76 total, | 2   | running, | 74  | sleeping, |     | 0 stopped, | 0 zombie |     |
| ------ | --------- | --- | -------- | --- | --------- | --- | ---------- | -------- | --- |
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used, 661948 buff/cache
| KiB Swap: |     | 0 total, |         |     | 0 free, |     | 0      | used, 2859196 | avail Mem     |
| --------- | --- | -------- | ------- | --- | ------- | --- | ------ | ------------- | ------------- |
| PID USER  |     | PRI      | NI VIRT |     | RES     | SHR | S %CPU | %MEM          | TIME+ COMMAND |
...
| Command        | History     |     |         |     |              |     |     |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- |
| Release        |             |     |         |     | Modification |     |     |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |     |     |
| Command        | Information |     |         |     |              |     |     |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
usb
usb
no usb
Description
EnablestheUSBportsontheswitch.Thissettingispersistentacrossswitchrebootsandmanagement
modulefailovers.Bothactiveandstandbymanagementmodulesareaffectedbythissetting.
ThenoformofthiscommanddisablestheUSBports.
Example
EnablingUSBports:
| switch(config)# |     | usb |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DisablingUSBportswhenaUSBdriveismounted:
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 265

| switch(config)#     | no      | usb     |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| usb mount    | | unmount |     |     |
| ------------ | --------- | --- | --- |
| usb {mount | | unmount}  |     |     |
Description
EnablesordisablestheinsertedUSBdrive.
| Parameter |     |     | Description                 |
| --------- | --- | --- | --------------------------- |
| mount     |     |     | EnablestheinsertedUSBdrive. |
unmount
DisablestheinsertedUSBdriveinpreparationforremoval.
Usage
IfUSBhasbeenenabledintheconfiguration,theUSBportontheactivemanagementmoduleis
availableformountingaUSBdrive.TheUSBportonthestandbymanagementmoduleisnotavailable.
AninsertedUSBdrivemustbemountedeachtimetheswitchbootsorfailsovertoadifferent
managementmodule.
AUSBdrivemustbeunmountedbeforeremoval.
ThesupportedUSBfilesystemsareFAT16andFAT32.
Examples
MountingaUSBdriveintheUSBport:
| switch# usb | mount |     |     |
| ----------- | ----- | --- | --- |
UnmountingaUSBdrive:
| switch# usb     | unmount |     |     |
| --------------- | ------- | --- | --- |
| Command History |         |     |     |
Switchsystemandhardwarecommands|266

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10FundamentalsGuide|(8400SwitchSeries) 267

Chapter 14

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

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

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

AOS-CX Software

Videos on new features introduced in this release:

Technical Update

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

268

channel on

YouTube.

HPE Aruba
Networking
Hardware
Documentation
and Translations
Portal

HPE Aruba
Networking
software

Software
licensing and
Feature Packs

End-of-Life
information

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

https://networkingsupport.hpe.com/downloads

https://licensemanagement.hpe.com/

https://www.arubanetworks.com/support-services/end-of-life/

Accessing Updates

You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My
Networking, where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to
the Hewlett Packard Enterprise Support Center More Information on Access to Support Materials
page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal
(ASP) account to manage subscriptions). Security notices are viewable without an ASP account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Support and Other Resources | 269

Regulatory Information

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

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

AOS-CX 10.10 Fundamentals Guide | (8400 Switch Series)

270