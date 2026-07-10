AOS-CX 10.14.xxxx
Fundamentals Guide

8400 Switch Series

Published: January 2024

Version: 3

Copyright Information

© Copyright 2025 Hewlett Packard Enterprise Development LP.

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

3

Contents
| About this                                   | document                                       | 11  |
| -------------------------------------------- | ---------------------------------------------- | --- |
| Applicableproducts                           |                                                | 11  |
| Latestversionavailableonline                 |                                                | 11  |
| Commandsyntaxnotationconventions             |                                                | 11  |
| Abouttheexamples                             |                                                | 12  |
| Identifyingswitchportsandinterfaces          |                                                | 12  |
| Identifyingmodularswitchcomponents           |                                                | 13  |
| About AOS-CX                                 |                                                | 14  |
| AOS-CXsystemdatabases                        |                                                | 14  |
| ArubaNetworkAnalyticsEngineintroduction      |                                                | 15  |
| AOS-CXCLI                                    |                                                | 15  |
| ArubaCXmobileapp                             |                                                | 15  |
| ArubaNetEdit                                 |                                                | 15  |
| Ansiblemodules                               |                                                | 16  |
| AOS-CXWebUI                                  |                                                | 16  |
| AOS-CXRESTAPI                                |                                                | 16  |
| In-bandandout-of-bandmanagement              |                                                | 17  |
| SNMP-basedmanagementsupport                  |                                                | 17  |
| Useraccounts                                 |                                                | 17  |
| Initial Configuration                        |                                                | 18  |
| InitialconfigurationusingZTP                 |                                                | 18  |
| InitialconfigurationusingtheArubaCXmobileapp |                                                | 19  |
|                                              | TroubleshootingBluetoothconnections            | 20  |
|                                              | BluetoothconnectionIPaddresses                 | 20  |
|                                              | Bluetoothisconnectedbuttheswitchisnotreachable | 21  |
|                                              | Bluetoothisnotconnected                        | 21  |
| InitialconfigurationusingtheCLI              |                                                | 24  |
|                                              | Connectingtotheconsoleport                     | 24  |
|                                              | Connectingtothemanagementport                  | 25  |
|                                              | Loggingintotheswitchforthefirsttime            | 26  |
|                                              | SettingswitchtimeusingtheNTPclient             | 26  |
| Configuringbanners                           |                                                | 27  |
| Configuringin-bandmanagementonadataport      |                                                | 28  |
| UsingtheWebUI                                |                                                | 28  |
| Configuringthemanagementinterface            |                                                | 28  |
| Restoringtheswitchtofactorydefaultsettings   |                                                | 29  |
| Managementinterfacecommands                  |                                                | 31  |
|                                              | default-gateway                                | 31  |
|                                              | ipstatic                                       | 32  |
|                                              | nameserver                                     | 33  |
|                                              | showinterfacemgmt                              | 34  |
| NTPcommands                                  |                                                | 35  |
|                                              | ntpauthentication                              | 35  |
|                                              | ntpauthentication-key                          | 35  |
|                                              | ntpdisable                                     | 37  |
|                                              | ntpenable                                      | 37  |
|                                              | ntpconductor                                   | 38  |
4
AOS-CX10.14.xxxxFundamentalsGuide| (8400SwitchSeries)

|                                 | ntpserver                                | 39  |
| ------------------------------- | ---------------------------------------- | --- |
|                                 | ntptrusted-key                           | 41  |
|                                 | ntpvrf                                   | 41  |
|                                 | showntpassociations                      | 42  |
|                                 | showntpauthentication-keys               | 44  |
|                                 | showntpservers                           | 44  |
|                                 | showntpstatistics                        | 45  |
|                                 | showntpstatus                            | 46  |
| Telnet                          | access                                   | 48  |
| Telnetcommands                  |                                          | 48  |
|                                 | showtelnetserver                         | 48  |
|                                 | showtelnetserversessions                 | 49  |
|                                 | telnetserver                             | 50  |
| Interface                       | configuration                            | 51  |
| Configuringalayer2interface     |                                          | 51  |
| Configuringalayer3interface     |                                          | 51  |
| SinglesourceIPaddress           |                                          | 52  |
| Priority-basedflowcontrol(PFC)  |                                          | 52  |
| Flowcontrolandlosslessbuffering |                                          | 53  |
|                                 | Requirementsforproperlosslessbuffering   | 53  |
| Forwarderrorcorrection          |                                          | 53  |
| Unsupportedtransceiversupport   |                                          | 54  |
| Configuringaninterfacepersona   |                                          | 54  |
|                                 | Modes                                    | 55  |
|                                 | Predefinedandcustompersonanames          | 55  |
|                                 | Creatingandconfiguringaninterfacepersona | 56  |
|                                 | Examples                                 | 56  |
| Monitormode                     |                                          | 57  |
| Interfacecommands               |                                          | 57  |
|                                 | allow-unsupported-transceiver            | 57  |
|                                 | defaultinterface                         | 59  |
|                                 | description                              | 59  |
|                                 | error-control                            | 60  |
|                                 | flow-control                             | 61  |
|                                 | interface                                | 63  |
|                                 | interfaceloopback                        | 63  |
|                                 | interfacevlan                            | 64  |
|                                 | ipaddress                                | 65  |
|                                 | ipmtu                                    | 66  |
|                                 | ipsource-interface                       | 67  |
|                                 | iptcpmss                                 | 68  |
|                                 | ipunnumbered                             | 69  |
|                                 | ipv6address                              | 71  |
|                                 | ipv6source-interface                     | 72  |
|                                 | ipv6tcpmss                               | 74  |
|                                 | l3-counters                              | 75  |
|                                 | mtu                                      | 76  |
|                                 | persona                                  | 77  |
|                                 | rate-interval                            | 79  |
|                                 | routing                                  | 80  |
|                                 | showallow-unsupported-transceiver        | 81  |
|                                 | showinterface                            | 82  |
|                                 | showinterfacedom                         | 87  |
|                                 | showinterfaceflow-control                | 88  |
|5

| showinterfacelink-diagnostics                   |              |            | 93  |
| ----------------------------------------------- | ------------ | ---------- | --- |
| showinterfacestatistics                         |              |            | 96  |
| showinterfacetransceiver                        |              |            | 98  |
| showinterfaceutilization                        |              |            | 102 |
| showipinterface                                 |              |            | 103 |
| showipsource-interface                          |              |            | 104 |
| showipv6interface                               |              |            | 105 |
| showipv6source-interface                        |              |            | 107 |
| shutdown                                        |              |            | 108 |
| systeminterface-group                           |              |            | 109 |
| Source interface                                | selection    |            | 111 |
| Source-interfaceselectioncommands               |              |            | 111 |
| ipsource-interface(protocol<ip-addr>)           |              |            | 111 |
| ipsource-interface                              |              |            | 113 |
| ipv6source-interface                            |              |            | 115 |
| ipv6source-interfacedns                         |              |            | 117 |
| ipv6source-interface                            |              |            | 119 |
| showipsource-interface                          |              |            | 121 |
| showipv6source-interface                        |              |            | 122 |
| showrunning-config                              |              |            | 124 |
| VLANs                                           |              |            | 127 |
| Configuration                                   | and firmware | management | 128 |
| Upgradeanddowngradescenarios                    |              |            | 128 |
| Upgrades                                        |              |            | 128 |
| Downgrades                                      |              |            | 128 |
| Limitations                                     |              |            | 128 |
| Hot-patchsoftware                               |              |            | 129 |
| Checkpoints                                     |              |            | 131 |
| Checkpointtypes                                 |              |            | 131 |
| Maximumnumberofcheckpoints                      |              |            | 131 |
| Usergeneratedcheckpoints                        |              |            | 131 |
| Systemgeneratedcheckpoints                      |              |            | 131 |
| Supportedremotefileformats                      |              |            | 131 |
| Rollback                                        |              |            | 132 |
| Checkpointautomode                              |              |            | 132 |
| Testingaswitchconfigurationincheckpointautomode |              |            | 132 |
| Checkpointcommands                              |              |            | 132 |
| checkpointauto                                  |              |            | 132 |
| checkpointautoconfirm                           |              |            | 133 |
| checkpointdiff                                  |              |            | 134 |
| checkpointpost-configuration                    |              |            | 136 |
| checkpointpost-configurationtimeout             |              |            | 137 |
| checkpointrename                                |              |            | 138 |
| checkpointrollback                              |              |            | 139 |
| copycheckpoint<CHECKPOINT-NAME><REMOTE-URL>     |              |            | 139 |
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config} 140
| copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>    |     |     | 141 |
| ----------------------------------------------- | --- | --- | --- |
| copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>     |     |     | 142 |
| copy<REMOTE-URL>{running-config|startup-config} |     |     | 143 |
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>} 145
| copy{running-config|startup-config}<REMOTE-URL>  |     |     | 146 |
| ------------------------------------------------ | --- | --- | --- |
| copy{running-config|startup-config}<STORAGE-URL> |     |     | 147 |
| copystartup-configrunning-config                 |     |     | 148 |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 6

copy<STORAGE-URL>running-config 149
erase 150
showcheckpoint<CHECKPOINT-NAME> 151
showcheckpoint<CHECKPOINT-NAME>hash 153
showcheckpointpost-configuration 154
showcheckpoint 155
showcheckpointdate 155
showrunning-confighash 156
showstartup-confighash 157
writememory 158
| Bootcommands |     | 158 |
| ------------ | --- | --- |
bootfabric-module 158
bootline-module 159
bootmanagement-module 160
bootmanagement-module(recoveryconsole) 162
bootset-default 163
bootsystem 164
showboot-history 166
| Firmwaremanagementcommands |     | 168 |
| -------------------------- | --- | --- |
copy{primary|secondary}<REMOTE-URL> 168
copy{primary|secondary}<FIRMWARE-FILENAME> 169
copyprimarysecondary 170
copy<REMOTE-URL> 171
copysecondaryprimary 173
copy<STORAGE-URL> 174
copyhot-patch 175
hot-patch 176
showhot-patch 177
| SNMP                 |     | 179 |
| -------------------- | --- | --- |
| ConfiguringSNMP      |     | 179 |
| OneTouchProvisioning |     | 180 |
location-override-alternative 182
| DNS                     |     | 184 |
| ----------------------- | --- | --- |
| Configuration           |     | 184 |
| DNSclient               |     | 184 |
| ConfiguringtheDNSclient |     | 184 |
| DNSclientcommands       |     | 186 |
ipdnsdomain-list 186
ipdnsdomain-name 187
ipdnshost 187
ipdnsserveraddress 188
showipdns 189
| Device discovery | and configuration | 192 |
| ---------------- | ----------------- | --- |
| LLDP             |                   | 192 |
LLDPagent 192
LLDPMEDsupport 194
LLDPEEE 195
ConfiguringtheLLDPagent 195
LLDPcommands 196
| clearlldpneighbors  |     | 196 |
| ------------------- | --- | --- |
| clearlldpstatistics |     | 196 |
| lldp                |     | 197 |
| lldpdot3            |     | 198 |
|7

|                               | lldpdot3mfs                 | 198 |
| ----------------------------- | --------------------------- | --- |
|                               | lldpholdtime-multiplier     | 199 |
|                               | lldpmanagement-addressvlan  | 200 |
|                               | lldpmanagement-ip-address   | 201 |
|                               | lldpmanagement-ipv6-address | 202 |
|                               | lldpmed                     | 203 |
|                               | lldpmedlocation             | 204 |
|                               | lldpreceive                 | 206 |
|                               | lldpreinit                  | 207 |
|                               | lldpselect-tlv              | 207 |
|                               | lldptimer                   | 209 |
|                               | lldptlv-enable              | 210 |
|                               | lldptransmit                | 211 |
|                               | lldptxdelay                 | 212 |
|                               | lldptrapenable              | 212 |
|                               | showlldpconfiguration       | 215 |
|                               | showlldpconfigurationmgmt   | 216 |
|                               | showlldplocal-device        | 217 |
|                               | showlldpneighbor-info       | 219 |
|                               | showlldpneighbor-infodetail | 222 |
|                               | showlldpneighbor-infomgmt   | 224 |
|                               | showlldpstatistics          | 226 |
|                               | showlldpstatisticsmgmt      | 227 |
|                               | showlldptlv                 | 228 |
| CiscoDiscoveryProtocol(CDP)   |                             | 229 |
|                               | CDPsupport                  | 229 |
|                               | CDPcommands                 | 229 |
|                               | cdp                         | 230 |
|                               | clearcdpcounters            | 230 |
|                               | clearcdpneighbor-info       | 231 |
|                               | showcdp                     | 231 |
|                               | showcdpneighbor-info        | 232 |
|                               | showcdptraffic              | 233 |
|                               | showcdpvoice-vlanmode       | 234 |
| Zero Touch                    | Provisioning                | 235 |
| ZTPsupport                    |                             | 235 |
| SettingupZTPonatrustednetwork |                             | 236 |
| ZTPprocessduringswitchboot    |                             | 237 |
| ZTPVSFswitchoversupport       |                             | 238 |
| ZTPcommands                   |                             | 238 |
|                               | showztpinformation          | 238 |
|                               | ztpforceprovision           | 243 |
| vSphere                       | agent                       | 245 |
| InstallationofvSphereagent    |                             | 245 |
| Showcommands                  |                             | 246 |
| Supportedswitches             |                             | 248 |
| Troubleshooting               |                             | 248 |
| Containermanagementcommands   |                             | 251 |
|                               | container                   | 251 |
|                               | env                         | 252 |
|                               | containerexec               | 253 |
|                               | image-download-vrf          | 254 |
|                               | image-location              | 254 |
|                               | restrictcpu                 | 256 |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 8

| restrictmemory                             |              |          | 256 |
| ------------------------------------------ | ------------ | -------- | --- |
| restrictstorage                            |              |          | 257 |
| showcontainer                              |              |          | 258 |
| showcapacitiescontainers                   |              |          | 259 |
| showcapacities-statuscontainers            |              |          | 260 |
| showrunning-configcontainer                |              |          | 260 |
| vrf                                        |              |          | 261 |
| Switch system                              | and hardware | commands | 263 |
| bluetoothdisable                           |              |          | 263 |
| bluetoothenable                            |              |          | 263 |
| clearevents                                |              |          | 264 |
| cleariperrors                              |              |          | 265 |
| consolebaud-rate                           |              |          | 266 |
| domain-name                                |              |          | 267 |
| fabricadmin-state                          |              |          | 267 |
| hostname                                   |              |          | 268 |
| ledlocator                                 |              |          | 269 |
| moduleadmin-state                          |              |          | 270 |
| moduleproduct-number                       |              |          | 271 |
| mtrace                                     |              |          | 273 |
| powerconsumption-average-period            |              |          | 274 |
| showbluetooth                              |              |          | 275 |
| showboot-history                           |              |          | 276 |
| showcapacities                             |              |          | 279 |
| showcapacities-status                      |              |          | 281 |
| showconsole                                |              |          | 282 |
| showcore-dump                              |              |          | 282 |
| showdeprecatedcommands                     |              |          | 284 |
| showdomain-name                            |              |          | 285 |
| showenvironmentfan                         |              |          | 286 |
| showenvironmentled                         |              |          | 288 |
| showenvironmentpower-consumption           |              |          | 289 |
| showenvironmentpower-consumption[vsx-peer] |              |          | 292 |
| showenvironmentpower-supply                |              |          | 294 |
| showenvironmentrear-display-module         |              |          | 295 |
| showenvironmenttemperature                 |              |          | 296 |
| showevents                                 |              |          | 298 |
| showfabric                                 |              |          | 301 |
| showhostname                               |              |          | 302 |
| showimages                                 |              |          | 302 |
| showiperrors                               |              |          | 304 |
| showmodule                                 |              |          | 306 |
| showrunning-config                         |              |          | 309 |
| showrunning-configcurrent-context          |              |          | 312 |
| showstartup-config                         |              |          | 314 |
| showsystemerror-counter-monitor            |              |          | 315 |
| showsystem                                 |              |          | 316 |
| showsystemresource-utilization             |              |          | 319 |
| showtech                                   |              |          | 323 |
| showusb                                    |              |          | 324 |
| showusbfile-system                         |              |          | 325 |
| showversion                                |              |          | 327 |
| systemerror-counter-monitor                |              |          | 328 |
| systemerror-counter-monitorpoll-interval   |              |          | 328 |
| systemresource-utilizationpoll-interval    |              |          | 329 |
|9

| topcpu                             |           |           | 329 |
| ---------------------------------- | --------- | --------- | --- |
| topmemory                          |           |           | 330 |
| usb                                |           |           | 331 |
| usbmount|unmount                   |           |           | 331 |
| Support                            | and Other | Resources | 333 |
| AccessingHPEArubaNetworkingSupport |           |           | 333 |
| AccessingUpdates                   |           |           | 334 |
| WarrantyInformation                |           |           | 334 |
| RegulatoryInformation              |           |           | 334 |
| DocumentationFeedback              |           |           | 334 |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 10

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

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

[ ]

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

11

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

Variable information in CLI prompts

In certain configuration contexts, the prompt may include variable information. For example, when in
the VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the Aruba 8400 Switch Series

About this document | 12

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

13

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

14

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

About AOS-CX | 15

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

16

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

About AOS-CX | 17

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

Reserved ports or ports used by other applications/services with in the system are not recommended to be used
for other services. When two services use the same port there is chance of unexpected behaviors from these

services. Best practices is to use unique port for each service across system.

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

18

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image
is being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

Initial configuration using the Aruba CX mobile app

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

Initial Configuration | 19

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify
that it be used for Internet access.

3. Open the Aruba CX mobile app on your mobile device.

;" />

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

20

Bluetooth is connected but the switch is not reachable

Symptom

The mobile device settings indicate that the device is connected to the switch through Bluetooth.
However, the mobile application indicates that the switch is not reachable.

Solution 1

Cause

The mobile device is paired with a different nearby switch.

Action

1. Verify the model number and serial number of the switch to which you are attempting to

connect.

2. Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile

device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following
format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify
that it be used for Internet access.

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

Initial Configuration | 21

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify that it
be used for Internet access.

Solution 2

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

22

n An inserted USB drive must be mounted each time the switch boots or fails over to a different

management module. To mount the drive, enter the CLI command: usb mount

n To enable Bluetooth, enter the CLI command: bluetooth enable

Solution 5

Cause

Another mobile device has already connected to the switch through Bluetooth. This cause is likely if
your device is repeatedly disconnected within 1-2 seconds of establishing a connection.

Action

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

Initial Configuration | 23

Solution 8

Cause

A problem occurred with the Bluetooth feature on the switch. For example, the software daemon was
stopped and then restarted.

Action

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

24

n Aswitchinstalledasdescribedinitshardwareinstallationguide.
n Acomputerwithterminalemulationsoftware.
AJL448AArubaX2C2RJ45toDB9consolecable.
n
Procedure
1. Connecttheconsoleportontheswitchtotheserialportonthecomputerusingaconsolecable.
2. Starttheterminalemulationsoftwareonthecomputerandconfigureanewserialsessionwith
thefollowingsettings:
| n   | Speed:115200bps  |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- |
| n   | Databits:8       |     |     |     |     |
| n   | Stopbits:1       |     |     |     |     |
| n   | Parity:None      |     |     |     |     |
| n   | Flowcontrol:None |     |     |     |     |
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
switch#
show console
| Baud | Rate: | 9600 |     |     |     |
| ---- | ----- | ---- | --- | --- | --- |
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
InitialConfiguration |25

|     | a. Connecttotheconsoleport          |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- |
|     | b. Configurethemanagementinterface. |     |     |     |     |
2. UseanEthernetcabletoconnectthemanagementporttoyournetwork.
3. UseanEthernetcabletoconnectyourcomputertothesamenetwork.
4. StartyourSSHclientsoftwareandconfigureanewsessionusingtheaddressassignedtothe
managementinterface.(IfthemanagementinterfaceissettooperateasaDHCPclient,retrieve
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 26

Procedure
1. IftheNTPserverrequiresauthentication,definetheauthenticationkeyfortheNTPclientwiththe
|     | commandntp | authentication. |     |     |     |     |     |     |     |     |
| --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2. ConfigureanNTPserverwiththecommandntp server.Whenconfiguringatimebackward
morethanfiveminutes,arebootisrecommendedtoavoidunusualswitchbehavior.
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
| switch(config)# |     | ntp     | authentication-key |                     |     | 1   | md5 myPassword |        |        |     |
| --------------- | --- | ------- | ------------------ | ------------------- | --- | --- | -------------- | ------ | ------ | --- |
| switch(config)# |     | ntp     | server             | my-ntp.mydomain.com |     |     |                | key 10 | prefer |     |
| switch(config)# |     | ntp     | vrf                | mgmt                |     |     |                |        |        |     |
| Configuring     |     | banners |                    |                     |     |     |                |        |        |     |
1. Configurethebannerthatisdisplayedwhenauserconnectstoamanagementinterface.Usethe
|     | commandbanner   |     | motd.Forexample: |      |     |     |     |     |     |     |
| --- | --------------- | --- | ---------------- | ---- | --- | --- | --- | --- | --- | --- |
|     | switch(config)# |     | banner           | motd | ^   |     |     |     |     |     |
Enter a new banner. Terminate the banner with the delimiter you have chosen.
|     | >> This | is an      | example | of   | a banner     | text | which     | a   | connecting | user |
| --- | ------- | ---------- | ------- | ---- | ------------ | ---- | --------- | --- | ---------- | ---- |
|     | >> will | see before |         | they | are prompted |      | for their |     | password.  |      |
>>
|     | >> As you        | can           | see           | it may | span | multiple  | lines     | and | the input |     |
| --- | ---------------- | ------------- | ------------- | ------ | ---- | --------- | --------- | --- | --------- | --- |
|     | >> will          | be terminated |               | when   | the  | delimiter | character |     | is        |     |
|     | >> encountered.^ |               |               |        |      |           |           |     |           |     |
|     | Banner           | updated       | successfully! |        |      |           |           |     |           |     |
2. Configurethebannerthatisdisplayedafterauserisauthenticated.Usethecommandbanner
exec.Forexample:
|     | switch(config)# |     | banner | exec | &   |     |     |     |     |     |
| --- | --------------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- |
Enter a new banner. Terminate the banner with the delimiter you have chosen.
|     | >> This           | is an  | example | of   | a different |           | banner | text. | This     | time |
| --- | ----------------- | ------ | ------- | ---- | ----------- | --------- | ------ | ----- | -------- | ---- |
|     | >> the            | banner | entered | will | be          | displayed | after  | a     | user has |      |
|     | >> authenticated. |        |         |      |             |           |        |       |          |      |
>>
>> & This text will not be included because it comes after the '&'
|     | Banner | updated | successfully! |     |     |     |     |     |     |     |
| --- | ------ | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
InitialConfiguration |27

| Configuring |     | in-band |     | management | on a data | port |
| ----------- | --- | ------- | --- | ---------- | --------- | ---- |
Prerequisites
n AconnectiontotheCLIviaeithertheconsoleportorthemanagementport
n Ethernetcable
Procedure
1. UseanEthernetcabletoconnectadataporttoyournetwork.
2. Configurealayer3interfaceonthedataport.
3. EnableSSHsupportontheinterface(onthedefaultVRF)withthecommandssh server vrf
default.
Forexample:
|     | switch# config  |     |            |             |     |     |
| --- | --------------- | --- | ---------- | ----------- | --- | --- |
|     | switch(config)# |     | ssh server | vrf default |     |     |
4. EnabletheWebUIontheinterface(onthedefaultVRF)withthecommandhttps-server vrf
default.
Forexample:
|       | switch(config)# |     | https-server | vrf default |     |     |
| ----- | --------------- | --- | ------------ | ----------- | --- | --- |
| Using | the             | Web | UI           |             |     |     |
TheWebUIisdisabledbydefault.Followthesestepstoenableitonthemanagementportandlogin.
TheWebUIisenabledbydefaultonthedefaultVRF.
Prerequisites
n AconnectiontotheswitchCLI.
Procedure
1. LogintotheCLI.
2. SwitchtoconfigcontextandenabletheWebUIonthemanagementportVRFwiththecommand
|     | https-server | vrf | mgmt. |     |     |     |
| --- | ------------ | --- | ----- | --- | --- | --- |
Forexample:
|     | switch#         | config |              |     |      |     |
| --- | --------------- | ------ | ------------ | --- | ---- | --- |
|     | switch(config)# |        | https-server | vrf | mgmt |     |
3. StartyourwebbrowserandentertheIPaddressofthemanagementportintheaddressbar,
|     | Forexample: | https://192.168.1.1 |     |     |     |     |
| --- | ----------- | ------------------- | --- | --- | --- | --- |
4. TheWebUIstartsandyouarepromptedtologin.
| Configuring |     | the | management |     | interface |     |
| ----------- | --- | --- | ---------- | --- | --------- | --- |
Prerequisites
Aconnectiontotheconsoleport.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 28

Procedure
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
| switch(config)#         | interface  | mgmt            |                   |                 |          |
| ----------------------- | ---------- | --------------- | ----------------- | --------------- | -------- |
| switch(config-if-mgmt)# |            | no shutdown     |                   |                 |          |
| switch(config-if-mgmt)# |            | ip static       | 198.168.100.10/24 |                 |          |
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
InitialConfiguration |29

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 30

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
InitialConfiguration |31

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 32

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
InitialConfiguration |33

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 34

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
InitialConfiguration |35

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 36

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
InitialConfiguration |37

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 38

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

burst

Specifies the address of an NTP server as a DNS name, an IPv4
address (x.x.x.x), where x is a decimal number from 0 to 255, or
an IPv6 address (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
where x is a hexadecimal number from 0 to F.
When specifying an IPv4 address, you can remove leading zeros.
For example, the address 192.169.005.100 becomes
192.168.5.100.
When specifying an IPv6 address, you can use two colons (::) to
represent consecutive zeros (but only once), remove leading
zeros, and collapse a hextet of four zeros to a single 0. For
example, this address 2222:0000:3333:0000:0000:0000:4444:0055
becomes 2222:0:3333::4444:55 .

Specifies the key to use when communicating with the server. A
trusted key must be defined with the command ntp
authentication-key and authentication must be enabled with the
command ntp authentication. Range: 1 to 65534.

Specifies the minimum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 6 (64 seconds).

Specifies the maximum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 10 (1024 seconds).

Send a burst of packets instead of just one when connected to the
server. Useful for reducing phase noise when the polling interval
is long.

Initial Configuration | 39

Parameter

Description

iburst

prefer

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

switch(config)# ntp server my-ntp.mydomain.com prefer

Command History

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

40

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp trusted-key
| ntp trusted-key    | <KEY-ID> |     |     |
| ------------------ | -------- | --- | --- |
| no ntp trusted-key | <KEY-ID> |     |     |
Description
Setsakeyastrusted.WhenNTPauthenticationisenabled,theswitchonlysynchronizeswithtime
serversthattransmitpacketscontainingatrustedkey.
Thenoformofthiscommandremovesthetrusteddesignationfromakey.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<KEY-ID> Specifiestheidentificationnumberofthekeytosetastrusted.
Range:1to65534.
Examples
Definingkey10asatrustedkey.
| switch(config)# | ntp | trusted-key | 10  |
| --------------- | --- | ----------- | --- |
Removingtrusteddesignationfromkey10:
| switch(config)#     | no      | ntp trusted-key | 10           |
| ------------------- | ------- | --------------- | ------------ |
| Command History     |         |                 |              |
| Release             |         |                 | Modification |
| 10.07orearlier      |         |                 | --           |
| Command Information |         |                 |              |
| Platforms           | Command | context         | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp vrf
InitialConfiguration |41

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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ntp              | associations |            |     |
| --------------------- | ------------ | ---------- | --- |
| show ntp associations |              | [vsx-peer] |     |
Description
ShowsthestatusoftheconnectiontoeachNTPserver.Thefollowinginformationisdisplayedforeach
server:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 42

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
377
* 2
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

Initial Configuration | 43

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 44

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
InitialConfiguration |45

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 46

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
InitialConfiguration |47

Chapter 4
Telnet access
Telnet access
TelnetserverenablesswitchestoacceptTelnetconnectionsfromclientstomanagetheswitch.Theuser
authenticationispasswordbasedauthentication(RADIUS,TACACS+orlocallystoredpassword).The
TelnetservercanbeenabledonadesiredVRFusingthetelnet servercommand.Themaximum
numberofTelnetsessionsperVRF isfive.
Inthedefaultconfiguration,Telnetaccessisdisabled.
| Telnet | commands |        |     |     |     |
| ------ | -------- | ------ | --- | --- | --- |
| show   | telnet   | server |     |     |     |
| show   | telnet   | server |     |     |     |
Description
ShowstheTelnetserverconfiguration.
Examples
ShowingtheTelnetserverconfiguration:
| switch(config)# |            | show           | telnet     | server |             |
| --------------- | ---------- | -------------- | ---------- | ------ | ----------- |
| TELNET          | Server     | Configuration: |            |        |             |
|                 | IP Version |                | : IPv4     |        |             |
|                 | TCP Port   |                | : 23       |        |             |
|                 | Enabled    | VRFs           | : default, |        | vrf1, vrf2, |
red, green
| Command   | History     |         |         |     |                                       |
| --------- | ----------- | ------- | ------- | --- | ------------------------------------- |
| Release   |             |         |         |     | Modification                          |
| 10.11     |             |         |         |     | Commandintroducedonallotherplatforms. |
| Command   | Information |         |         |     |                                       |
| Platforms |             | Command | context |     | Authority                             |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
48
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries)

| show telnet | server          | sessions        |             |
| ----------- | --------------- | --------------- | ----------- |
| show telnet | server sessions | [vrf <VRF-NAME> | | all-vrfs] |
Description
ShowsallactiveTelnetsessionsforthespecifiedVRForallVRFs.IfnoVRFisprovided,theTelnet
sessionsonthedefaultVRFareshown.
| Parameter      |     | Description                                |     |
| -------------- | --- | ------------------------------------------ | --- |
| vrf <VRF-NAME> |     | SpecifiestheTelnetsessionsforaspecificVRF. |     |
| all-vrfs       |     | SpecifiestheTelnetsessionsforallVRFs       |     |
Examples
ShowingtheTelnetsessiononthedefaultVRF:
| switch(config)# | show            | telnet server sessions |     |
| --------------- | --------------- | ---------------------- | --- |
| TELNET          | sessions on VRF | default:               |     |
IPv4 TELNET Sessions:
|     | Server IP   | : 10.1.1.1 |     |
| --- | ----------- | ---------- | --- |
|     | Client IP   | : 10.1.1.2 |     |
|     | Client Port | : 58835    |     |
ShowingtheTelnetsessionsonallVRFs:
| switch(config)# | show            | telnet server sessions | all-vrfs |
| --------------- | --------------- | ---------------------- | -------- |
| TELNET          | sessions on VRF | mgmt:                  |          |
IPv4 TELNET Sessions:
|        | Server IP       | : 10.1.1.1 |     |
| ------ | --------------- | ---------- | --- |
|        | Client IP       | : 10.1.1.2 |     |
|        | Client Port     | : 58835    |     |
| TELNET | sessions on VRF | default:   |     |
IPv4 TELNET Sessions:
|         | Server IP   | : 20.1.1.1                            |     |
| ------- | ----------- | ------------------------------------- | --- |
|         | Client IP   | : 20.1.1.2                            |     |
|         | Client Port | : 58837                               |     |
| Command | History     |                                       |     |
| Release |             | Modification                          |     |
| 10.11   |             | Commandintroducedonallotherplatforms. |     |
Telnetaccess|49

| Command   | Information |     |         |           |
| --------- | ----------- | --- | ------- | --------- |
| Platforms | Command     |     | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| telnet    | server     |                |     |     |
| --------- | ---------- | -------------- | --- | --- |
| telnet    | server vrf | <VRF-NAME>     |     |     |
| no telnet | server     | vrf <VRF-NAME> |     |     |
Description
EnablestheTelnetserveronthedesiredVRF.Telnetserverisdisabledbydefault.
ThenoformofthiscommanddisablestheTelnetserver.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFonwhichtheTelnetserverwillbeenabledor
disabled.
Examples
ConfiguringtheTelnetserveronthemgmtVRF:
| switch(config)# |             | telnet | server  | vrf mgmt                              |
| --------------- | ----------- | ------ | ------- | ------------------------------------- |
| Command         | History     |        |         |                                       |
| Release         |             |        |         | Modification                          |
| 10.11           |             |        |         | Commandintroducedonallotherplatforms. |
| Command         | Information |        |         |                                       |
| Platforms       | Command     |        | context | Authority                             |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 50

Chapter 5

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

51

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

Reboot is required to split or unsplit a port that has had link up with PFC or RXTX enabled. Until reboot,
the interface will remain down with a status of Split in progress or Unsplit in progress.

PFC is not supported on the 8400X 32x10G module (JL363A).

PFC is not supported on the 8400X 8x40G module (JL365A) split interfaces (for example, 10G).

While interfaces with PFC configured are enabled, any change to QoS cos-map or queue-profile affecting
the priority or queue used by PFC could cause the intended traffic to no longer be treated as lossless.

Interface configuration | 52

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

Forward error correction

Forward error correction (FEC) is used to control errors in transmissions where the source sends
redundant data and the destination only recognizes the data portion that contains no apparent errors.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

53

FECdoesnotrequireahandshakebetweenthesourceanddestinationatthecostofahigherforward
channelbandwidth.Itisthereforebestusedinscenarioswherere-transmissionsarecostlyor
impossible,suchasusingmulticastone-waycommunication.
| Unsupported |     | transceiver |     |     | support |     |
| ----------- | --- | ----------- | --- | --- | ------- | --- |
Transceiverproducts(optical,DAC,AOCs)thatarelistedassupportedbyaswitchmodelaredetailedin
theTransceiverGuide.Transceiverproductsthatarenotlisted,areconsideredunsupported;thiswould
includetransceiversthatare:
n Non-Arubabrandedproducts
n HPEbrandedproductsthatweredesignedfornon-AOS-CXswitchmodels(e.g.Comware)
n HPEbrandedproductsdesignatedforuseinHPEComputeServersorStorage
TransceiversoriginallydesignatedforuseinArubaWLANcontrollersorformerMobilityAccess
n
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
| error-control              | { auto | | none            | | base-r-fec      |              | | rs-fec     | }             |
| -------------------------- | ------ | ----------------- | ----------------- | ------------ | ------------ | ------------- |
| ip bootp-gateway           |        | <IPV4-ADDR>       |                   |              |              |               |
| ip forward-protocol        |        | udp               | <IPV4-ADDR>       | {<PORT-NUM>  |              | | <PROTOCOL>} |
| ip helper-address          |        | <IPV4-ADDR>       | [vrf              | <VRF-NAME>]  |              |               |
| ip igmp router-alert-check |        |                   | [enable           | | disable]   |              |               |
| ip igmp snooping           |        | [auto vlan        | <VLAN-LIST>]      |              |              |               |
| ip igmp snooping           |        | [blocked          | vlan <VLAN-LIST>] |              |              |               |
| ip igmp snooping           |        | [fastleave        | vlan              | <VLAN-LIST>] |              |               |
| ip igmp snooping           |        | [forced-fastleave |                   | vlan         | <VLAN-LIST>] |               |
| ip igmp snooping           |        | [forward          | vlan <VLAN-LIST>] |              |              |               |
Interfaceconfiguration|54

| ip ospf <PROCESS-ID> |         |         | area    | <AREA-ID>     |     |     |
| -------------------- | ------- | ------- | ------- | ------------- | --- | --- |
| ip ospf passive      |         |         |         |               |     |     |
| ip rip <PROCESS-ID>  |         | {all-ip |         | | ip-address} |     |     |
| ip rip all-ip        | disable |         |         |               |     |     |
| ip rip all-ip        | enable  |         |         |               |     |     |
| ip rip all-ip        | receive |         | disable |               |     |     |
| ip rip all-ip        | send    | disable |         |               |     |     |
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 55

n uplink
n access
Thesenameshavenopredefinedconfiguration.Tousethem,theymustbemanuallyconfiguredas
needed.Youcanalsocreatepersonaswithacustomname.Thesecustompersonascanbecreatedand
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
| switch(config)#    |     | interface | 1/1/1-1/1/24     |        |
| ------------------ | --- | --------- | ---------------- | ------ |
| switch(config-if)# |     | persona   | custom mypersona | attach |
Interfaceconfiguration|56

switch(config-if)# exit

Monitor mode

Monitor mode displays interface statistics in real time, updating frequently. The update interval varies
by product, number of visible ports, and display options in use. View the current update interval in the
help menu.

Formatting options can be supplied either at command launch or while monitor mode is active. Press ?
to see the available formatting options available in the current command context. Exit the help menu
with q.

Monitor mode detects terminal size to adjust the number of interfaces and statistics viewable on
screen. Additional interfaces or statistics columns can be viewed with the navigation keys: Arrow keys,
PageUp, PageDown, Home, and End. Serial console does not automatically detect terminal setting
changes, resulting in unexpected output. Recommended recovery steps are to exit and restart.

Monitor mode refreshes data automatically until exited with q.

Interface commands

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

57

Allowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | allow-unsupported-transceiver |     |     |     |
| --------------- | ----------------------------- | --- | --- | --- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
| Do you agree | and do you | want to continue | (y/n)? | y   |
| ------------ | ---------- | ---------------- | ------ | --- |
Allowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | allow-unsupported-transceiver |     |     | confirm |
| --------------- | ----------------------------- | --- | --- | ------- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
Configuringunsupportedtransceiverloggingwithanintervalofevery48hours:
switch(config)# allow-unsupported-transceiver log-interval 2880
Disablingunsupportedtransceiverlogging:
switch(config)# allow-unsupported-transceiver log-interval none
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no allow-unsupported-transceivers |     |     |     |
| --------------- | --------------------------------- | --- | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
| Ccontinue   | (y/n)? y    |               |           |       |
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | no allow-unsupported-transceiver |     |     | confirm |
| --------------- | -------------------------------- | --- | --- | ------- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
switch(config)#
| Command History |     |                                                     |     |     |
| --------------- | --- | --------------------------------------------------- | --- | --- |
| Release         |     | Modification                                        |     |     |
| 10.10           |     | Upto100G supportenabledforunsupportedtransceiverson |     |     |
8400(upto100G)seriesswitchesinUT mode.
| 10.07orearlier |     | --  |     |     |
| -------------- | --- | --- | --- | --- |
Interfaceconfiguration|58

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
config
| 8400 |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| default interface |                |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
| default interface | <INTERFACE-ID> |     |     |     |
Description
Setsaninterface(orarangeofinterfaces)tofactorydefaultvalues.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID> SpecifiestheIDofasingleinterfaceorrangeofinterfaces.Format:
member/slot/portormember/slot/port-member/slot/portto
specifyarange.
Examples
Resettinganinterface:
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 59

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<DESCRIPTION> Specifyadescriptionfortheinterface.Range:1to64ASCII
characters(includingspace,excludingquestionmark).
Examples
| SettingthedescriptionforaninterfacetoDataLink |     |             |     |          | 01: |
| --------------------------------------------- | --- | ----------- | --- | -------- | --- |
| switch(config-if)#                            |     | description |     | DataLink | 01  |
Removingthedescriptionforaninterface.
| switch(config-if)# |             | no description |     |              |     |
| ------------------ | ----------- | -------------- | --- | ------------ | --- |
| Command            | History     |                |     |              |     |
| Release            |             |                |     | Modification |     |
| 10.07orearlier     |             |                |     | --           |     |
| Command            | Information |                |     |              |     |
| Platforms          | Command     | context        |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
error-control
| error-control    | {auto | | none | | base-r-fec |     | | rs-fec} |
| ---------------- | ----- | ------ | ------------ | --- | --------- |
| no error-control | {auto | | none | | base-r-fec |     | | rs-fec} |
Description
Configurestheforwarderrorcorrection(FEC)modetouseforaninterface.Whennotconfigured,the
systemwillautomaticallyselecttheFECmodebasedontheinstalledtransceiver.Inmostcases,the
standardFECmodewillworkbest,butcertainlinkpartnersmayrequireanon-standardmode.
ThenoandautoformsofthiscommandconfiguretheinterfacetoautomaticallyusethestandardFEC
modeofthecurrentlyinstalledtransceiver.
FECconfigurationonlyappliestotransceivers,DACs,orAOCsrunningat25Gor100G.100GDACsareaspecial
case.TheycanonlysetFECtononewhenauto-negotiationisdisabledthroughthespeedoverridecommand.
Thedefaultfortheinstalledtransceiverisusedinallothercases.
TransceiversforwhichFECisauto-negotiatedwillrequestthemodeconfiguredbythiscommand,butmay
resolvetoadifferentmode.TheappliedFEC modeisdisplayedasacommentedlineintheconfigurationshown
withtheshowruncommand.Itisalsodisplayedwithshowinterfacecommand.
Interfaceconfiguration|60

| Parameter  |             |         | Description                              |
| ---------- | ----------- | ------- | ---------------------------------------- |
| auto       |             |         | Usethetransceiverdefault.                |
| none       |             |         | DonotuseanyFEC.                          |
| base-r-fec |             |         | UseIEEEBASE-R(Firecode)FEC.              |
| rs-fec     |             |         | UseIEEERS(Reed-Solomon)FEC.              |
| Command    | History     |         |                                          |
| Release    |             |         | Modification                             |
| 10.11      |             |         | Commandenabledon6400and8400SwitchSeries. |
| 10.08.1021 |             |         | Commandintroduced.                       |
| Command    | Information |         |                                          |
| Platforms  | Command     | context | Authority                                |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
flow-control
| flow-control    | rx       |                 |     |
| --------------- | -------- | --------------- | --- |
| no flow-control | rx       |                 |     |
| flow-control    | priority | rxtx <PRIORITY> |     |
| no flow-control | priority | rxtx <PRIORITY> |     |
Description
Commandflow-controlenablesnegotiationofreceiveflowcontrolonthecurrentinterface.Theswitch
advertisesRXsupporttothelinkpartner.Thefinalconfigurationisdeterminedbasedonthecapabilities
ofbothpartners.
Commandflow-control priorityenablespriority-basedflowcontrol(PFC).Asinglepriorityis
supported..
Eachinvocationofthiscommandreplacesthepreviousconfiguration.
Thenoformofthesecommandsdisablesanyconfiguredflowcontrolontheselectedinterface.
| Parameter |     |     | Description                                       |
| --------- | --- | --- | ------------------------------------------------- |
| rx        |     |     | Enablestheabilitytoceaseandresumetransmissionwhen |
receivingIEEE802.3xLLFCpauseframesonthisinterface.
<PRIORITY> SpecifiesthepacketpriorityforwhichPFCwilloperate.Range:0to
7.Oneprioritycanbespecified.
| Usage (flow | control) |     |     |
| ----------- | -------- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 61

n For interfaces that auto-negotiate, link-level flow control is subject to negotiation, plus speed and
other parameters. Both ends of the link must negotiate the same flow control mode for it to be
applied.

n For interfaces that do not auto-negotiate, the configured link-level flow control mode is always

applied and the user is responsible for ensuring that both ends of the link are configured for the
same mode.

n All members of a LAG must have the same flow control configuration.

n Lossless flow control is only supported for single destination unicast traffic. Replicated traffic (for

example, broadcast, multicast, mirroring) cannot be guaranteed to be lossless.

n Lossless behavior is not supported when operating in a VSF stack configuration.

Usage (priority-based flow control (PFC))

n PFC will only operate correctly between interfaces with the same priority configuration. Traffic flow

will not be lossless between interfaces with different priorities or between interfaces where one has
PFC enabled and the other does not.

n Any queue used by protocol or control traffic must not be configured for lossless behavior. Routing
protocols and VSX-synchronization messages use local-priority 7, therefore the CoS priority mapped
to local-priority 7 should not be used in any lossless configuration.

For example, in a default configuration, the CoS map assigns local-priority 7 to packets arriving with
VLAN priority 7. This means that lossless pools should not be configured to use priority 7, and that
any flow-control priority mode should not be configured on priority 7, since that VLAN priority
maps to local-priority 7.

n PFC is enabled for the given Priority Code Point. Only one priority may be enabled for PFC per

interface. PFC is only supported on JL365A 8400X 8-port 40GbE QSFP+ Advanced Module, JL366A
Aruba 8400X 6-port 40GbE/100GbE QSFP28 Adv Mod, and JL687A 8400X-32Y 32p 1/10/25G
SFP/SFP+/SFP28 Module line modules.

n PFC will only operate correctly between interfaces with the same priority configuration. Traffic flow

will not be lossless between interfaces with different priorities or between interfaces where one has
PFC enabled and the other does not.

Examples

Enabling support for RX flow control:

switch(config)# interface 1/1/1
switch(config-if)# flow-control rx

Disabling support for RX flow control:

switch(config)# interface 1/1/1
switch(config-if)# no flow-control rx

Enabling support for priority RXTX flow control:

switch(config)# interface 1/1/1
switch(config-if)# flow-control priority rxtx 2

Disabling support for priority RXTX flow control:

Interface configuration | 62

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
| Command History     |         |         |                            |
| ------------------- | ------- | ------- | -------------------------- |
| Release             |         |         | Modification               |
| 10.10               |         |         | Adjustedtheprioritysyntax. |
| 10.07orearlier      |         |         | --                         |
| Command Information |         |         |                            |
| Platforms           | Command | context | Authority                  |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
interface
| interface <PORT-NUM> |     |     |     |
| -------------------- | --- | --- | --- |
Description
Switchestotheconfig-ifcontextforaphysicalport.Thisiswhereyoudefinetheconfigurationsettings
forthelogicalinterfaceassociatedwiththephysicalport.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PORT-NUM>
Specifiesaphysicalportnumber.Format:member/slot/port.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| interface | loopback |     |     |
| --------- | -------- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 63

| interface loopback | <ID>     |      |     |
| ------------------ | -------- | ---- | --- |
| no interface       | loopback | <ID> |     |
Description
Createsaloopbackinterfaceandchangestotheconfig-loopback-ifcontext.Loopbackinterfacesare
layer3.
Thenoformofthiscommanddeletesaloopbackinterface.
| Parameter  |     |     | Description                                  |
| ---------- | --- | --- | -------------------------------------------- |
| <INSTANCE> |     |     | SpecifiestheloopbackinterfaceID.Range:1to256 |
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
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| interface      | vlan           |     |     |
| -------------- | -------------- | --- | --- |
| interface vlan | <VLAN-ID>      |     |     |
| no interface   | vlan <VLAN-ID> |     |     |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-if-
vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-ID>
SpecifiestheloopbackinterfaceID.
| none |     |     | DonotreserveanyinternalVLANs. |
| ---- | --- | --- | ----------------------------- |
Examples
Interfaceconfiguration|64

| switch# | config |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- |
switch(config)#
vlan 10
| switch(config-vlan-10)# |     |           |     | exit |     |
| ----------------------- | --- | --------- | --- | ---- | --- |
| switch(config)#         |     | interface |     | vlan | 10  |
switch(config-if-vlan)#
| Command        | History     |     |         |     |              |
| -------------- | ----------- | --- | ------- | --- | ------------ |
| Release        |             |     |         |     | Modification |
| 10.07orearlier |             |     |         |     | --           |
| Command        | Information |     |         |     |              |
| Platforms      | Command     |     | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip address
| ip address    | <IP-ADDR>/<MASK> |     |     | [secondary] |     |
| ------------- | ---------------- | --- | --- | ----------- | --- |
| no ip address | <IP-ADDR>/<MASK> |     |     | [secondary] |     |
Description
SetsanIPv4addressforthecurrentlayer3interface.
ThenoformofthiscommandremovestheIPv4addressfromtheinterface.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes192.168.5.100.
| <MASK> |     |     |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
secondary SpecifiesasecondaryIPaddress.(Supportedon6300,exceptfor
S3L75A,S3L76A,S3L77A.)
Examples
SettingtheIPaddressoninterface1/1/1to192.168.100.1withamaskof24bits:
| switch(config)#    |     | interface |            | 1/1/1 |                  |
| ------------------ | --- | --------- | ---------- | ----- | ---------------- |
| switch(config-if)# |     |           | ip address |       | 192.168.100.1/24 |
RemovingtheIPaddress192.168.100.1withamaskof24bitsfrominterface1/1/1:
| switch(config)#    |     | interface |       | 1/1/1   |                  |
| ------------------ | --- | --------- | ----- | ------- | ---------------- |
| switch(config-if)# |     |           | No ip | address | 192.168.100.1/24 |
AssigningtheIPaddress192.168.20.1withamaskof24bitstoloopbackinterface1:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 65

| switch(config)# | interface | loopback | 1   |
| --------------- | --------- | -------- | --- |
switch(config-loopback-if)#
|     |     | ip  | address 192.168.20.1/24 |
| --- | --- | --- | ----------------------- |
AssigningtheIPaddress192.168.199.1withamaskof24bitstointerfaceVLAN10:
| switch(config)#         | interface | vlan       | 10               |
| ----------------------- | --------- | ---------- | ---------------- |
| switch(config-if-vlan)# |           | ip address | 192.168.199.1/24 |
RemovingtheIPaddress192.168.199.1withamaskof24bitsfrominterfaceVLAN10:
| switch(config)#         | interface | vlan          | 10               |
| ----------------------- | --------- | ------------- | ---------------- |
| switch(config-if-vlan)# |           | no ip address | 192.168.199.1/24 |
| Command History         |           |               |                  |
| Release                 |           |               | Modification     |
| 10.07orearlier          |           |               | --               |
| Command Information     |           |               |                  |
| Platforms               | Command   | context       | Authority        |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-loopback-if |     | rightsforthiscommand. |
| --- | ------------------ | --- | --------------------- |
config-if-vlan
ip mtu
ip mtu <VALUE>
no ip mtu
Description
SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthat
canbesentorreceivedbytheinterface.ThisvalueshouldbelessthanorequaltotheoverallMTUfor
theinterface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE>
SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
SettingtheIPMTUto576bytes:
| switch(config-if)# |     | ip mtu 576 |     |
| ------------------ | --- | ---------- | --- |
SettingtheIPMTUtothedefaultvalue:
Interfaceconfiguration|66

| switch(config-if)#  |         | no ip mtu |                           |
| ------------------- | ------- | --------- | ------------------------- |
| Command History     |         |           |                           |
| Release             |         |           | Modification              |
| 10.08               |         |           | Subinterfacesupportadded. |
| 10.07orearlier      |         |           | --                        |
| Command Information |         |           |                           |
| Platforms           | Command | context   | Authority                 |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     | rightsforthiscommand. |
| --- | -------------- | --- | --------------------- |
ip source-interface
ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay |
simplivity | dns | all} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
no ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-
relay | simplivity | dns | all} [interface <IFNAME> | <IPV4-ADDR>] [vrf <VRF-NAME>]
Description
SetsasinglesourceIPaddressforafeatureontheswitch.Thisensuresthatalltrafficsentthefeature
hasthesamesourceIPaddressregardlessofhowitegressestheswitch.Youcandefineasingleglobal
addressthatappliestoallsupportedfeatures,oranindividualaddressforeachfeature.
ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,
orbyusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIP
addresstakesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforallsupportedservices,ora
specificservice.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | SetsasinglesourceIPaddressforaspecificservice.Theall
ntp | syslog | ubt | dhcp-relay | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
simplivity | dns | all nothaveanaddressset.ForDHCPrelay,theaddressisusedas
boththesourceIPandGIADDR.
interface <IFNAME> Specifiesthenameoftheinterfacefromwhichthespecified
serviceobtainsitssourceIPaddress.Theinterfacemusthavea
validIPaddressassignedtoit.Iftheinterfacehasbothaprimary
andsecondaryIPaddress,theprimaryIPaddressisused.
<IPV4-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedservice.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionis
notused).SpecifytheaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |
| -------------- | --- | --- | ----------------------- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 67

Examples
SettingtheIPv4address10.10.10.5astheglobalsinglesourceaddress:
switch#
config
| switch(config)# |     | ip source-interface |     |     | all 10.10.10.5 |     |
| --------------- | --- | ------------------- | --- | --- | -------------- | --- |
SettingthesecondaryIPv4address10.10.10.5oninterface1/1/1astheglobalsinglesourceaddress:
| switch# config     |     |                     |               |     |                |           |
| ------------------ | --- | ------------------- | ------------- | --- | -------------- | --------- |
| switch(config)#    |     | interface           | 1/1/1         |     |                |           |
| switch(config-if)# |     | ip address          | 10.10.10.1/24 |     |                |           |
| switch(config-if)# |     | ip address          | 10.10.10.5/24 |     |                | secondary |
| switch(config)#    |     | exit                |               |     |                |           |
| switch(config)#    |     | ip source-interface |               |     | all 10.10.10.5 |           |
Settingtheaddress10.10.10.25onVRFsflow-vrfoninterface1/1/2asthesinglesourceaddressfor
sFlow:
| switch(config)# |     | vrf sflow-vrf |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- | --- |
switch(config-vrf)#
exit
| switch(config)#    |     | interface   | 1/1/2            |     |     |     |
| ------------------ | --- | ----------- | ---------------- | --- | --- | --- |
| switch(config-if)# |     | no shutdown |                  |     |     |     |
| switch(config-if)# |     | vrf         | attach sflow-vrf |     |     |     |
| switch(config-if)# |     | ip address  | 10.10.10.25/24   |     |     |     |
| switch(config-if)# |     | exit        |                  |     |     |     |
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)#     |         | no ip source-interface |     |              | all | 10.10.10.5 |
| ------------------- | ------- | ---------------------- | --- | ------------ | --- | ---------- |
| Command History     |         |                        |     |              |     |            |
| Release             |         |                        |     | Modification |     |            |
| 10.07orearlier      |         |                        |     | --           |     |            |
| Command Information |         |                        |     |              |     |            |
| Platforms           | Command | context                |     | Authority    |     |            |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip tcp mss
| ip tcp mss <VALUE> |         |     |     |     |     |     |
| ------------------ | ------- | --- | --- | --- | --- | --- |
| no ip tcp mss      | <VALUE> |     |     |     |     |     |
Description
SetstheTCP(TransmissionControlProtocol)MSS(MaximumSegmentSize)foraninterface.When
configured,theMSS optionintheTCPheaderissetintheTCP handshakefornegotiationduring
Interfaceconfiguration|68

connectionestablishment.OncetheTCPsessionisestablished,changingtheTCP MSSvalueonthe
interfacewillnotaffecttheexistingsession.
ThenoformofthiscommandremovestheTCP MSS configurationfromtheinterface.
TCPMSSissupportedonROP,SVI,subinterface,andL3GREtunnelinterface.
| Parameter |     |     |     | Description                                    |
| --------- | --- | --- | --- | ---------------------------------------------- |
| <VALUE>   |     |     |     | SpecifiestheIPv4TCPMSSinbytes.Range:68to65495. |
Examples
ConfiguringtheIPv4TCPMSSfortheinterface:
| switch(config)#    |     | interface | 1/1/1    |     |
| ------------------ | --- | --------- | -------- | --- |
| switch(config-if)# |     | ip tcp    | mss 1460 |     |
RemovingtheIPv4TCPMSSconfigurationfromtheinterface:
| switch(config)#     |         | interface | 1/1/1   |                    |
| ------------------- | ------- | --------- | ------- | ------------------ |
| switch(config-if)#  |         | no ip     | tcp mss | 1460               |
| Command History     |         |           |         |                    |
| Release             |         |           |         | Modification       |
| 10.14.1000          |         |           |         | Commandintroduced. |
| Command Information |         |           |         |                    |
| Platforms           | Command | context   |         | Authority          |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     |     | rightsforthiscommand. |
| --- | -------------- | --- | --- | --------------------- |
config-gre-if
ip unnumbered
| ip unnumbered    | <ifname> |     |     |     |
| ---------------- | -------- | --- | --- | --- |
| no ip unnumbered | <ifname> |     |     |     |
Description
TheIPunnumberedfeatureallowstheswitchtoprocessIPpacketswithoutconfiguringauniqueIPaddresson
aninterfacebytellingtheroutertousetheIPaddressofanotherselectedinterfaceastheaddressforthat
link.Onceset,thisportwillborrowtheuser-configuredprimaryIPv4addressfromanlenderinterfaceanduse
thatIP addressinitsL3controlplaneexchange.
ThenoversionofthiscommandremovesIPunnumberedsupportforthisport.Onceunset,thisportwill
removeborrowedIPv4address.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 69

| Parameter |     |     | Description        |     |
| --------- | --- | --- | ------------------ | --- |
| <Ifname > |     |     | Nameoftheinterface |     |
Usage
TheportwhereIPunnumberedisconfiguredisknownastheborrowerinterface.Onlyroute-onlyportscan
borrowanaddress.
Theporttheaddressisborrowedfromisknownasthelenderinterface.Onlyaloopbackinterfacecanbeused
asalenderinterface.TheunnumberedinterfaceandlenderinterfacemustbelongtothesameVRF.
Additionally,thelenderinterfaceforanIPunnumberedinterfacecannotitselfconfiguredasunnumbered.
Thefollowingcaveatsapplytothisfeature:
n OnlytheprimaryIPv4addresscanbeborrowedonanIPunnumberedinterface.Youcannotconfigurea
secondaryIPaddressforaninterfacethatisalreadyconfiguredasanIPunnumberedinterface.
n IfanIPaddressisconfiguredonaninterfacethatisalreadyconfiguredasanIPunnumberedinterface,it
willfunctionasanormalIPinterface.
n AnIPv6unnumberedconfigurationontheinterfaceisnotsupported.Ifipunnumberedisenabledonthe
interface,onlytheIPv4addressisborrowed.However,AnyIPv6configurationscanco-existwithanip
unnumberedinterface.
n AnIPunnumberedinterfacecannothavemultiplelenderinterfacesforthesameaddressfamily.
n Theipunnumberedcommandrequiresthattheinterfaceborrowingtheaddressisaroutedport.TheIP
unnumberedfeatureisonlysupportedondevicesconnectedwithpoint-to-pointinterfaces.
n AnunnumberedIPaddresscannotbeusedastunnelsource.
n TheunnumberedinterfaceandlenderinterfacemustbelongtothesameVRF.
n DeletingalenderinterfaceremovesalltheassociatedIPunnumberedreferences.
Examples
ConfiguringIPunnumberedforaroute-onlyport:
| switch(config)#    | interface     | 1/1/1 |           |     |
| ------------------ | ------------- | ----- | --------- | --- |
| switch(config-if)# | ip unnumbered |       | loopback1 |     |
ThefollowingexamplesremovesIPunnumberedsupportforthisport.Onceunset,thisportwillremovethe
borrowedIPv4address.
| switch(config)#    | interface | 1/1/1      |           |     |
| ------------------ | --------- | ---------- | --------- | --- |
| switch(config-if)# | no ip     | unnumbered | loopback1 |     |
IfanIPaddressisconfiguredonaninterfacethatisalreadyconfiguredasanIPunnumberedinterface
(orviceversa),bothconfigurationscancoexistontheinterface.Theswitch'sarbitrationlogicensures
thatstaticIPconfigurationisgivenpriorityoverunnumbered.
| switch(config)#    | interface     | 1/1/1 |                |            |
| ------------------ | ------------- | ----- | -------------- | ---------- |
| switch(config-if)# | ip unnumbered |       | interface      | loopback 1 |
| switch(config-if)# | ip address    |       | 10.16.1.1/24   |            |
| switch(config-if)# | ip address    |       | 192.168.1.2/24 | secondary  |
Interfaceconfiguration|70

or

switch(config)# interface 1/1/1
switch(config-if)# ip address 10.16.1.1/24
switch(config-if)# ip unnumbered interface loopback 1
switch(config-if)# ip address 192.168.1.2/24 secondary

switch(config)# sh running-config interface
switch(config-if)# do sh running-config interface 1/1/1
interface 1/1/1

no shutdown
ip address 10.16.1.1/24
ip address 192.168.1.2/24 secondary
ip unnumbered interface loopback 1

! ip unnumbered is ignored when static ip is configured

If loopback lender interface does not exist during IP unnumbered configuration, a prompt will be
displayed in CLI to allow the user to create that interface.

switch(config)# interface 1/1/1
switch(config-if)# ip unnumbered interface loopback 1
Lender port not found.
Do you want to create (y/n)? y
switch(config-if)#

Failure case:
switch(config)# ip unnumbered interface loopback 1
Lender port not found.
Do you want to create (y/n)? y
Lender port: loopback1 creation failed
switch(config-if)

Command History

Release

10.14.1000

Command Information

Modification

Command introduced

Platforms

Command context

Authority

8400

config-if

Administrators or local user group members with execution
rights for this command.

ipv6 address
ipv6 address <IPV6-ADDR>/<MASK>{eui64 | [tag <ID>]}
no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets an IPv6 address on the interface.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

71

ThenoformofthiscommandremovestheIPv6addressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6addresslink-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-local
addressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6addresslink-
localcommand.
| Parameter   |     |     | Description                       |
| ----------- | --- | --- | --------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiestheIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress2222:0000:3333:0000:0000:0000:4444:0055
becomes2222:0:3333::4444:55.
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
Interfaceconfiguration|72

no ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-
relay | simplivity | dns | all} [interface <IFNAME> | <IPV6-ADDR>] [vrf <VRF-NAME>]
Description
SetsasinglesourceIPaddressforafeatureontheswitch.Thisensuresthatalltrafficsentthefeature
hasthesamesourceIPaddressregardlessofhowitegressestheswitch.Youcandefineasingleglobal
addressthatappliestoallsupportedfeatures,oranindividualaddressforeachfeature.
ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,
orbyusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIP
addresstakesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforallsupportedprotocols,ora
specificprotocol.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | SetsasinglesourceIPaddressforaspecificprotocol.Theall
ntp | syslog | ubt | dhcp-relay | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
| simplivity | | dns    | | all |     | nothaveanaddressset. |
| ---------- | -------- | ----- | --- | -------------------- |
| interface  | <IFNAME> |       |     |                      |
Specifiesthenameoftheinterfacefromwhichthespecified
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
switch(config-if)#
exit
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
StopthesourceIPaddressfromusingtheIPaddressoninterface1/1/1onVRFone.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 73

switch(config)# no ip source-interface all interface 1/1/1 vrf one
ClearthesourceIPaddress2001:DB8::1.
| switch(config)#     |         | no ip source-interface |     |              | all 2001:DB8::1 |
| ------------------- | ------- | ---------------------- | --- | ------------ | --------------- |
| Command History     |         |                        |     |              |                 |
| Release             |         |                        |     | Modification |                 |
| 10.07orearlier      |         |                        |     | --           |                 |
| Command Information |         |                        |     |              |                 |
| Platforms           | Command | context                |     | Authority    |                 |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 tcp mss |             |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
| ipv6 tcp mss | <VALUE>     |     |     |     |     |
| no ipv6 tcp  | mss <VALUE> |     |     |     |     |
Description
SetstheTCP(TransmissionControlProtocol)MSS(MaximumSegmentSize)foraninterface.When
configured,theMSS optionintheTCPheaderissetintheTCP handshakefornegotiationduring
connectionestablishment.OncetheTCPsessionisestablished,changingtheTCP MSSvalueonthe
interfacewillnotaffecttheexistingsession.
ThenoformofthiscommandremovestheTCP MSS configurationfromtheinterface.
TCPMSSissupportedonROP,SVI,subinterface,andL3GREtunnelinterface.
| Parameter |     |     |     | Description                                    |     |
| --------- | --- | --- | --- | ---------------------------------------------- | --- |
| <VALUE>   |     |     |     | SpecifiestheIPv6TCPMSSinbytes.Range:68to65495. |     |
Examples
ConfiguringtheIPv6TCPMSSfortheinterface:
| switch(config)#    |     | interface | 1/1/1   |      |     |
| ------------------ | --- | --------- | ------- | ---- | --- |
| switch(config-if)# |     | ipv6      | tcp mss | 1440 |     |
RemovingtheIPv6TCPMSSconfigurationfromtheinterface:
| switch(config)#    |     | interface | 1/1/1 |          |     |
| ------------------ | --- | --------- | ----- | -------- | --- |
| switch(config-if)# |     | no ipv6   | tcp   | mss 1440 |     |
Interfaceconfiguration|74

| Command History     |         |         |     |                    |
| ------------------- | ------- | ------- | --- | ------------------ |
| Release             |         |         |     | Modification       |
| 10.14.1000          |         |         |     | Commandintroduced. |
| Command Information |         |         |     |                    |
| Platforms           | Command | context |     | Authority          |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     |     | rightsforthiscommand. |
| --- | -------------- | --- | --- | --------------------- |
config-gre-if
l3-counters
| l3-counters    | [rx | tx] |       |     |     |
| -------------- | --------- | ----- | --- | --- |
| no l3-counters | [rx       | | tx] |     |     |
Description
Enablescountersonalayer3interface.Bydefault,allinterfacesarelayer3.Tochangealayer2
interfacetolayer3,usetheroutingcommand.
Thenoformofthiscommand,withnospecification,disablesbothtransmitandreceivecountersona
layer3interface.Todisabletransmit(tx)orreceive(rx)countersonly,specifythecountertypeyouwant
todisable.
| Parameter |     |     |     | Description               |
| --------- | --- | --- | --- | ------------------------- |
| rx        |     |     |     | Specifiesreceivecounters. |
tx
Specifiestransmitcounters.
Examples
Enablinglayer3transmitcountersoninterface1/1/1:
| switch(config)#    |     | interface   | 1/1/1 |     |
| ------------------ | --- | ----------- | ----- | --- |
| switch(config-if)# |     | l3-counters |       | tx  |
Disablinglayer3transmitandreceivecountersoninterface1/1/2:
| switch(config)#    |     | interface      | 1/1/2 |                                          |
| ------------------ | --- | -------------- | ----- | ---------------------------------------- |
| switch(config-if)# |     | no l3-counters |       |                                          |
| Command History    |     |                |       |                                          |
| Release            |     |                |       | Modification                             |
| 10.08              |     |                |       | Addedsupportfor13countersonsubinterfaces |
| 10.07orearlier     |     |                |       | --                                       |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 75

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-if
| 8400 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
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
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| <VALUE>   |     |     | SpecifiestheMTUinbytes.Range:46to9198.Default:1500. |
Examples
SettingtheMTUoninterface1/1/1to1000bytes:
| switch(config)#    | interface | 1/1/1      |     |
| ------------------ | --------- | ---------- | --- |
| switch(config-if)# |           | no routing |     |
| switch(config-if)# |           | mtu 1000   |     |
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
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Interfaceconfiguration|76

persona
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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

77

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
| switch(config)#           | interface | 1/1/1            |     |
| ------------------------- | --------- | ---------------- | --- |
| switch(config-if)#persona |           | custom mypersona |     |
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
Interfaceconfiguration|78

| Release             |         |         |     | Modification                         |
| ------------------- | ------- | ------- | --- | ------------------------------------ |
| 10.10               |         |         |     | Addedoptionalparameters:attach,copy. |
| 10.09               |         |         |     | Commandintroduced.                   |
| Command Information |         |         |     |                                      |
| Platforms           | Command | context |     | Authority                            |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
rate-interval
| rate-interval | <VALUE> |     |     |     |
| ------------- | ------- | --- | --- | --- |
no rate-interval
Description
Thiscommandsetsthetimeintervaltocalculateinterfacerates.Lowerintervalsaremoreusefulfor
detectingtrafficbursts,butmayincreasecomputationloadtotheoverallsystem.Intervalsmustbea
multipleoffiveseconds.Thecommand-lineinterfacewillnotacceptarateintervalvaluethatisnota
multipleoffive.
Thenoformofthiscommandsetstheratecollectionintervaltothedefaultvalueof300seconds.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VALUE> Thestatisticsratecollectionintervalinseconds.Thesupported
rangeis5-300seconds,wherethenumberofsecondsisa
multipleoffive.
NOTE:ThesupportedrangeforAruba6400and8400Switch
seriesis30-300seconds.
Examples
Settingtheratecollectionintervalto50seconds
switch(config)#
|                    |     | interface     | 1/1/1 |     |
| ------------------ | --- | ------------- | ----- | --- |
| switch(config-if)# |     | rate-interval |       | 50  |
Settingtheratecollectionintervaltothedefaultvalue:
| switch(config-if)# |     | no rate-interval |     |     |
| ------------------ | --- | ---------------- | --- | --- |
Thefollowingexampleshowsthecommand-lineinterfacewarningthatappearswhileconfiguringan
invalidrate-interval.
| switch(config)#    |     | interface | 1/1/1    |     |
| ------------------ | --- | --------- | -------- | --- |
| switch(config-if)# |     | rate      | interval | 6   |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 79

| The interval | must be | a multiple | of 5. |
| ------------ | ------- | ---------- | ----- |
Usage
Theratecollectionintervalmustbeconfiguredinthemultiplesof5.Anyothervaluewillberejectedand
theCLIwilldisplaytheerrormessage,The interval must be a multiple of 5.
| Command History     |         |         |                                             |
| ------------------- | ------- | ------- | ------------------------------------------- |
| Release             |         |         | Modification                                |
| 10.12.1000          |         |         | Commandsupportedonallplatforms.             |
| 10.12               |         |         | CommandIntroducedon6300and8360Switchseries. |
| Command Information |         |         |                                             |
| Platforms           | Command | context | Authority                                   |
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
Ifyouenablethisconfiguration,collectionofflowtrackingstatisticsisdisabled.
Examples
Enablingroutingsupportonaninterface:
| switch(config-if)# |     | routing |     |
| ------------------ | --- | ------- | --- |
Disablingroutingsupportonaninterface:
| switch(config-if)# |     | no routing |     |
| ------------------ | --- | ---------- | --- |
| Command History    |     |            |     |
Interfaceconfiguration|80

| Release        |             |         |     | Modification |
| -------------- | ----------- | ------- | --- | ------------ |
| 10.07orearlier |             |         |     | --           |
| Command        | Information |         |     |              |
| Platforms      | Command     | context |     | Authority    |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show allow-unsupported-transceiver
show allow-unsupported-transceiver
Description
Displaysconfigurationandstatusofunsupportedtransceivers.
Examples
Showingunallowedunsupportedtransceivers:
| switch(config)#   |          | show allow-unsupported-transceiver |     |                |
| ----------------- | -------- | ---------------------------------- | --- | -------------- |
| Allow unsupported |          | transceivers                       |     | : no           |
| Logging           | interval |                                    |     | : 1440 minutes |
---------------------------------------------
| Port | Type |     | Status |     |
| ---- | ---- | --- | ------ | --- |
---------------------------------------------
| 1/1/31 | SFP-SX     |     | unsupported |     |
| ------ | ---------- | --- | ----------- | --- |
| 1/1/32 | SFP-1G-BXD |     | unsupported |     |
| 1/1/2  | SFP28DAC3  |     | unsupported |     |
Showingallowedunsupportedtransceivers:
| switch#           | show allow-unsupported-transceiver |              |     |                |
| ----------------- | ---------------------------------- | ------------ | --- | -------------- |
| Allow unsupported |                                    | transceivers |     | : yes          |
| Logging           | interval                           |              |     | : 1440 minutes |
---------------------------------------------
| Port | Type |     | Status |     |
| ---- | ---- | --- | ------ | --- |
---------------------------------------------
| 1/1/31         | SFP-SX      |     | unsupported-allowed |              |
| -------------- | ----------- | --- | ------------------- | ------------ |
| 1/1/32         | SFP-1G-BXD  |     | unsupported-allowed |              |
| 1/1/2          | SFP28DAC3   |     | unsupported         |              |
| Command        | History     |     |                     |              |
| Release        |             |     |                     | Modification |
| 10.07orearlier |             |     |                     | --           |
| Command        | Information |     |                     |              |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 81

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show interface |                       |     |                    |
| -------------- | --------------------- | --- | ------------------ |
| show interface | [<IFNNAME>|<IFRANGE>] |     | [brief | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] | monitor | [human-readable] |
| -------------- | ----------- | ------- | ---------------- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief]
show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]
| show interface | lag [<LAG-ID>] | monitor | [human-readable] |
| -------------- | -------------- | ------- | ---------------- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     | Description                                    |
| --------- | --- | --- | ---------------------------------------------- |
| <IFNAME>  |     |     | Specifiesainterfacename.                       |
| <IFRANGE> |     |     | Specifiestheportidentifierrange.               |
| brief     |     |     | Showsbriefinfointabularformat.                 |
| physical  |     |     | Showsthephysicalconnectioninfointabularformat. |
extended Showsadditionalstatistics,includingthetxfilteredandrx
filteredcounters.
n Rxfilterpacketsareprotocolpacketsreceivedwhenthe
protocolisdisabledontheswitchandthereisonlyoneportin
theVLAN.ProtocolsincludeOSPF,PIM,RIP,LACP,andLLDP.
n AnexampleofaTxfilteredpacketwouldbeamulticastpacket
beingfilteredfromgoingoutoftheingressport.
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero |     |     | Showsonlynonzerostatistics. |
| -------- | --- | --- | --------------------------- |
LAG
ShowsLAGinterfaceinformation.
| monitor |     |     | Continuouslymonitorinterfacestatistics. |
| ------- | --- | --- | --------------------------------------- |
LOOPBACK
Showsloopbackinterfaceinformation.
| TUNNEL |     |     | Showstunnelinterfaceinformation. |
| ------ | --- | --- | -------------------------------- |
VLAN
ShowsVLANinterfaceinformation.
| <LAG-ID> |     |     | SpecifiestheLAGnumber.Range:1-256 |
| -------- | --- | --- | --------------------------------- |
<LOOPBACK-ID>
SpecifiestheLOOPBACKnumber.Range:0-255
| <TUNNEL-ID> |     |     | SpecifiesthetunnelID.Range:1-255 |
| ----------- | --- | --- | -------------------------------- |
Interfaceconfiguration|82

| Parameter  |     |     |     |     | Description                                    |     |     |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| <VLAN-ID>  |     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |     |     |
| VXLAN      |     |     |     |     | ShowstheVXLANinterfaceinformation.             |     |     |     |
| <VXLAN-ID> |     |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |     |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch#           | show      | interface | 1/1/1        |                   |                 |           |     |     |
| ----------------- | --------- | --------- | ------------ | ----------------- | --------------- | --------- | --- | --- |
| Interface         | 1/1/1     | is up     |              |                   |                 |           |     |     |
| Admin state       | is        | up        |              |                   |                 |           |     |     |
| Link state:       | up        | for 2     | days (since  | Sun               | Jun 21 05:30:22 | UTC 2020) |     |     |
| Link transitions: |           | 1         |              |                   |                 |           |     |     |
| Description:      |           | backup    | data center  | link              |                 |           |     |     |
| Hardware:         | Ethernet, |           | MAC Address: | 70:72:cf:fd:e7:b4 |                 |           |     |     |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |         |     |     |       |         |
| ---------------- | ---- | ----------- | --- | ------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |         |     |     |       |         |
| Auto-negotiation |      | is          | on  |         |     |     |       |         |
| Flow-control:    |      | off         |     |         |     |     |       |         |
| Error-control:   |      | off         |     |         |     |     |       |         |
| L3 Counters:     |      | Rx Enabled, | Tx  | Enabled |     |     |       |         |
| Rate collection  |      | interval:   | 300 | seconds |     |     |       |         |
| Rates            |      |             |     | RX      |     | TX  | Total | (RX+TX) |
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 83

| switch(config-if)# |       | show  | interface |     | 1/1/1 |     |     |     |
| ------------------ | ----- | ----- | --------- | --- | ----- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |     |       |     |     |     |
...
| Auto-negotiation |     | is on | with | downshift | active |     |     |     |
| ---------------- | --- | ----- | ---- | --------- | ------ | --- | --- | --- |
ShowinginformationwhentheinterfaceisshutdownduringaVSX split:
| switch(config-if)# |       | show     | interface |        | 1/1/1 |     |     |     |
| ------------------ | ----- | -------- | --------- | ------ | ----- | --- | --- | --- |
| Interface          | 1/1/1 | is down  |           |        |       |     |     |     |
| Admin state        | is    | up       |           |        |       |     |     |     |
| State information: |       | Disabled |           | by VSX |       |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
| Link transitions: |     | 0   |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, | MAC | Address: |     | 04:09:73:62:90:e7 |     |     |     |
| --------- | --------- | --- | -------- | --- | ----------------- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |                 |     |         |     |     |       |         |
| ---------------- | --------------- | --------------- | --- | ------- | --- | --- | ----- | ------- |
| Speed 0          | Mb/s            |                 |     |         |     |     |       |         |
| Auto-negotiation |                 | is off          |     |         |     |     |       |         |
| Flow-control:    |                 | off             |     |         |     |     |       |         |
| Error-control:   |                 | off             |     |         |     |     |       |         |
| VLAN Mode:       | native-untagged |                 |     |         |     |     |       |         |
| Native           | VLAN:           | 1               |     |         |     |     |       |         |
| Allowed          | VLAN            | List: 1502-1505 |     |         |     |     |       |         |
| Rate collection  |                 | interval:       | 300 | seconds |     |     |       |         |
| Rate             |                 |                 |     |         | RX  | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     | 0.00 | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | --- | ---- | ---- | --- | ----- |
| KPkts /     | sec |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Unicast     |     |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Multicast   |     |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Broadcast   |     |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Utilization |     |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Statistic   |     |     |     |     | RX   | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     |     | 0   | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     |     | 0   | 0   |     | 0   |
| Multicast    |     |     |     |     | 0   | 0   |     | 0   |
| Broadcast    |     |     |     |     | 0   | 0   |     | 0   |
| Bytes        |     |     |     |     | 0   | 0   |     | 0   |
| Jumbos       |     |     |     |     | 0   | 0   |     | 0   |
| Dropped      |     |     |     |     | 0   | 0   |     | 0   |
| Pause Frames |     |     |     |     | 0   | 0   |     | 0   |
| Errors       |     |     |     |     | 0   | 0   |     | 0   |
| CRC/FCS      |     |     |     |     | 0   | n/a |     | 0   |
| Collision    |     |     |     |     | n/a | 0   |     | 0   |
| Runts        |     |     |     |     | 0   | n/a |     | 0   |
| Giants       |     |     |     |     | 0   | n/a |     | 0   |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
Interfaceconfiguration|84

| Interface | 1/1/1 | is up |     |     |     |     |       |         |     |
| --------- | ----- | ----- | --- | --- | --- | --- | ----- | ------- | --- |
| Rate      |       |       |     | RX  |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| MBits /     | sec |     |     | 30196.43 |     | 30196.43 |       | 60392.85  |        |
| ----------- | --- | --- | --- | -------- | --- | -------- | ----- | --------- | ------ |
| MPkts /     | sec |     |     | 58977.39 |     | 58977.40 |       | 117954.79 |        |
| Unicast     |     |     |     | 0.00     |     | 0.00     |       |           | 0.00   |
| Multicast   |     |     |     | 58977.39 |     | 58977.40 |       | 117954.79 |        |
| Broadcast   |     |     |     | 0.00     |     | 0.00     |       |           | 0.00   |
| Utilization | %   |     |     | 75.49    |     | 75.49    |       |           | 150.98 |
| Statistic   |     |     |     | RX       |     | TX       | Total | (RX+TX)   |        |
---------------- -------------------- -------------------- --------------------
| Packets      |                |            | 4756527649   |     | 4756527865   |     |              | 9513055514  |     |
| ------------ | -------------- | ---------- | ------------ | --- | ------------ | --- | ------------ | ----------- | --- |
| Unicast      |                |            |              | 0   |              | 0   |              |             | 0   |
| Multicast    |                |            | 4756527649   |     | 4756527865   |     |              | 9513055514  |     |
| Broadcast    |                |            |              | 2   |              | 0   |              |             | 2   |
| Bytes        |                |            | 304417778668 |     | 304417795428 |     | 608835574096 |             |     |
| Jumbos       |                |            |              | 0   |              | 0   |              |             | 0   |
| Dropped      |                |            |              | 0   | 19028847730  |     |              | 19028847730 |     |
| Pause Frames |                |            |              | 0   |              | 0   |              |             | 0   |
| Errors       |                |            |              | 0   |              | 0   |              |             | 0   |
| CRC/FCS      |                |            |              | 0   |              | n/a |              |             | 0   |
| help: ?,     | quit: q        |            |              |     |              |     |              |             |     |
| Help for     | Interface      | Monitor    |              |     |              |     |              |             |     |
| h Toggle     | human-readable |            | mode         |     |              |     |              |             |     |
| c Clear      | interface      | statistics |              |     |              |     |              |             |     |
| Does not     | apply to       | rates      |              |     |              |     |              |             |     |
| Arrows,      | PgUp, PgDn,    | Home,      | End          |     |              |     |              |             |     |
| Navigate     | interface      | statistics |              |     |              |     |              |             |     |
Delay: 2
| help: ?, | quit: q |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the<1symbolforUtilizationindicatesthattheamountofpacketsisbetweenzero
andone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |       |         |     |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | ----- | ------- | --- |
| Interface          | 1/1/1 | is up |           |                      |     |     |       |         |     |
| Rate               |       |       |           | RX                   |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| Bits /      | sec |     |     | 3M  |     | 3M  |     |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts /      | sec |     |     | 316 |     | 316 |     |     | 633   |
| Unicast     |     |     |     | 319 |     | 319 |     |     | 638   |
| Multicast   |     |     |     | 0   |     | 0   |     |     | 0     |
| Broadcast   |     |     |     | 0   |     | 0   |     |     | 0     |
| Utilization | %   |     |     | < 1 |     | < 1 |     |     | < 1   |
| Statistic   |     |     |     | RX  |     | TX  |     |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets   |     |     |     | 577K |     | 577K |     |     | 1M  |
| --------- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
| Unicast   |     |     |     | 577K |     | 577K |     |     | 1M  |
| Multicast |     |     |     | 0    |     | 51   |     |     | 51  |
| Broadcast |     |     |     | 0    |     | 15   |     |     | 15  |
| Bytes     |     |     |     | 744M |     | 745M |     |     | 1G  |
| Jumbos    |     |     |     | 0    |     | 0    |     |     | 0   |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 85

| Dropped      |     |     |     |     | 0   |     | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filtered     |     |     |     |     | 0   |     | 0   |     | 0   |
| Pause Frames |     |     |     |     | 0   |     | 0   |     | 0   |
| Errors       |     |     |     |     | 0   |     | 0   |     | 0   |
| CRC/FCS      |     |     |     |     | 0   |     | n/a |     | 0   |
| Collision    |     |     |     |     | n/a |     | 0   |     | 0   |
| Runts        |     |     |     |     | 0   |     | n/a |     | 0   |
| Giants       |     |     |     |     | 0   |     | n/a |     | 0   |
Showinginformationaboutextendedcounters:
Theoutputoftheshow interface extendedcommandvariesdependingontheswitchmodeland
configuration.
| switch(config-if)# |     | show | interface |     | 1/1/17 | extended |     |     |     |
| ------------------ | --- | ---- | --------- | --- | ------ | -------- | --- | --- | --- |
-------------------------------------------------------------------
| Interface | 1/1/17 |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Statistics |     |     |     |     |     | Value |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Tp | Port In         | Frames |         |     |     | 547   |     |     |     |
| -------- | --------------- | ------ | ------- | --- | --- | ----- | --- | --- | --- |
| Dot1d Tp | Port Out        | Frames |         |     |     | 608   |     |     |     |
| Dot3 In  | Pause Frames    |        |         |     |     | 0     |     |     |     |
| Dot3 Out | Pause Frames    |        |         |     |     | 0     |     |     |     |
| Ethernet | Stats Broadcast |        | Packets |     |     | 19    |     |     |     |
| Ethernet | Stats Bytes     |        |         |     |     | 40162 |     |     |     |
| Ethernet | Stats Packets   |        |         |     |     | 342   |     |     |     |
...
-------------------------------------------------------------------
| Error-Statistics |     |     |     |     |     | Value |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Base   | Port        | MTU Exceeded |          | Discards |        | 0   |     |     |     |
| ------------ | ----------- | ------------ | -------- | -------- | ------ | --- | --- | --- | --- |
| Dot3 Control | In          | Unknown      | Opcodes  |          |        | 0   |     |     |     |
| Dot3 Stats   | Alignment   | Errors       |          |          |        | 0   |     |     |     |
| Dot3 Stats   | FCS Errors  |              |          |          |        | 0   |     |     |     |
| Dot3 Stats   | Frame       | Too Longs    |          |          |        | 0   |     |     |     |
| Dot3 Stats   | Internal    | Mac          | Transmit |          | Errors | 0   |     |     |     |
| Ethernet     | RX Oversize | Packets      |          |          |        | 0   |     |     |     |
...
Showinginterfacelink-status:
| switch# | show interface |     | link-status |     |     |     |     |     |     |
| ------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------
| Port | Type |     |     | Physical |       | Link        | Last   |     |     |
| ---- | ---- | --- | --- | -------- | ----- | ----------- | ------ | --- | --- |
|      |      |     |     | Link     | State | Transitions | Change |     |     |
-------------------------------------------------------------
| 1/1/1    | 1G-BT     |     |     | down |     | 0   | --           |          |     |
| -------- | --------- | --- | --- | ---- | --- | --- | ------------ | -------- | --- |
| 1/1/2    | 1G-BT     |     |     | up   |     | 1   | 1 minute ago | (Fri Mar | 09  |
| 12:36:56 | UTC 2018) |     |     |      |     |     |              |          |     |
| 1/1/3    | 1G-BT     |     |     | up   |     | 1   | 1 minute ago | (Fri Mar | 09  |
| 12:36:56 | UTC 2018) |     |     |      |     |     |              |          |     |
| 1/1/4    | --        |     |     | down |     | 0   | --           |          |     |
| 1/1/5    | --        |     |     | down |     | 0   | --           |          |     |
Showinginterfaceloopback1link-status:
Interfaceconfiguration|86

-------------------------------------------------------------
|      |      |     | Physical |       | Link        | Last   |     |
| ---- | ---- | --- | -------- | ----- | ----------- | ------ | --- |
| Port | Type |     | Link     | State | Transitions | Change |     |
-------------------------------------------------------------
| loopback1 | --  |     | up  |     | --  | --  |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Showinginterface1/1/2-1/1/3link-status:
-------------------------------------------------------------
|      |      |     | Physical |       | Link        | Last   |     |
| ---- | ---- | --- | -------- | ----- | ----------- | ------ | --- |
| Port | Type |     | Link     | State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/2    | 1G-BT     |     | up  |     | 1   | 1 minute | ago (Fri Mar 09 |
| -------- | --------- | --- | --- | --- | --- | -------- | --------------- |
| 12:36:56 | UTC 2018) |     |     |     |     |          |                 |
| 1/1/3    | 1G-BT     |     | up  |     | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |     |     |     |          |                 |
Showinginterfacelink-status:
| switch# | show interface | link-status |     |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Port | Type |     |     | Physical   | Link        | Link Flaps | Last   |
| ---- | ---- | --- | --- | ---------- | ----------- | ---------- | ------ |
|      |      |     |     | Link State | Transitions | Ignored    | Change |
-------------------------------------------------------------------------
| 1/1/1           | 1G-BT       |     |       | down                   | 0   | 0   | --           |
| --------------- | ----------- | --- | ----- | ---------------------- | --- | --- | ------------ |
| 1/1/2           | 1G-BT       |     |       | up                     | 1   | 0   | 1 minute ago |
| (Fri Mar        | 09 12:36:56 | UTC | 2018) |                        |     |     |              |
| 1/1/3           | 1G-BT       |     |       | up                     | 1   | 0   | 1 minute ago |
| (Fri Mar        | 09 12:36:56 | UTC | 2018) |                        |     |     |              |
| 1/1/4           | --          |     |       | down                   | 0   | 0   | --           |
| 1/1/5           | --          |     |       | down                   | 0   | 0   | --           |
| Command History |             |     |       |                        |     |     |              |
| Release         |             |     |       | Modification           |     |     |              |
| 10.11           |             |     |       | Addedmonitorparameter. |     |     |              |
10.10
Addedhuman-readableparameter.
| 10.07orearlier      |         |         |     | --        |     |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- | --- |
| Command Information |         |         |     |           |     |     |     |
| Platforms           | Command | context |     | Authority |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show interface | dom              |     |     |          |            |     |     |
| -------------- | ---------------- | --- | --- | -------- | ---------- | --- | --- |
| show interface | [<INTERFACE-ID>] |     | dom | [detail] | [vsx-peer] |     |     |
Description
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 87

Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+,QSFP+).
ThisinformationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter      |     |     | Description                                   |     |     |     |
| -------------- | --- | --- | --------------------------------------------- | --- | --- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |     |
| detail         |     |     | Showdetailedinformation.                      |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# | show interface | dom |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- |
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
| 2                   |            | 44.46   | 3.30         | 6.04 | 0.08, -10.96 | 0.63, -2.00 |
| 3                   |            | 44.46   | 3.30         | 6.51 | 0.08, -10.96 | 0.60, -2.16 |
| 4                   |            | 44.46   | 3.30         | 6.19 | 0.08, -10.96 | 0.63, -1.94 |
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
Interfaceconfiguration|88

AsofAOS-CX10.10,theseparateshowflow-controlcommandhasbeenremoved,withitbeingeffectively
replacedbythiscommand.
Parameter Description
<IFNNAME>|<IFRANGE> Specifiestheinterface(port)nameorrange.Whennointerface
rangeisspecified,onlyinterfaceswithflowcontrolenabledinthe
configurationorstatusareshown.
detail Showsdetailedinformation.
Examples
Showingsummaryflowcontrolinformation:
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
| 1/1/1  | config: | llfc rx      |              |      |
| ------ | ------- | ------------ | ------------ | ---- |
|        | status: | llfc rx      |              |      |
| 1/1/2  | config: | llfc rx      | incompatible | 0    |
|        | status: | llfc rx      |              |      |
| 1/1/10 | config: | pfc rxtx-1,2 | enabled      | 1234 |
|        | status: | pfc rxtx-1,2 |              |      |
| 1/1/12 | config: | pfc rxtx-1,2 | error        | 0    |
|        | status: | pfc rxtx-1,2 |              |      |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 89

| 1/1/32:4 | config: | pfc | rxtx-5 |     |     |     |     |
| -------- | ------- | --- | ------ | --- | --- | --- | --- |
|          | status: | pfc | rxtx-5 |     |     |     |     |
Showingsummaryflowcontrolinformationwheretheconfigurationdoesnotmatchstatusduetoa
rebootrequiredtoapplyPFCconfigurationinhardware:
| switch# show | interface |     | flow-control |              |          |     |     |
| ------------ | --------- | --- | ------------ | ------------ | -------- | --- | --- |
| Flow Control | Watchdog  |     | Settings     |              |          |     |     |
| Trigger      | Timeout:  | 100 | milliseconds | (actual: not | applied) |     |     |
| Resume       | Time:     | 100 | milliseconds | (actual: not | applied) |     |     |
----------- ------------------------------------- ------------- --------
| Port | Flow    |     |     |     | Watchdog | Watchdog |     |
| ---- | ------- | --- | --- | --- | -------- | -------- | --- |
|      | Control |     |     |     | Status   | Timeouts |     |
----------- ------------------------------------- ------------- --------
| 1/1/1    | config: | llfc | rx       |     |              |     |      |
| -------- | ------- | ---- | -------- | --- | ------------ | --- | ---- |
|          | status: | llfc | rx       |     |              |     |      |
| 1/1/2    | config: | llfc | rx       |     | incompatible |     | 0    |
|          | status: | llfc | rx       |     |              |     |      |
| 1/1/10   | config: | pfc  | rxtx-1,2 |     | pending      |     | 1234 |
|          | status: | none |          |     |              |     |      |
| 1/1/12   | config: | pfc  | rxtx-1,2 |     | pending      |     | 0    |
|          | status: | none |          |     |              |     |      |
| 1/1/32:4 | config: | pfc  | rxtx-5   |     |              |     |      |
|          | status: | none |          |     |              |     |      |
ShowingdetailedflowcontrolinformationwithRXflowcontrolenabled:
| switch# show | interface |     | 1/1/1 flow-control | detail |     |     |     |
| ------------ | --------- | --- | ------------------ | ------ | --- | --- | --- |
| Interface    | 1/1/1 is  | up  |                    |        |     |     |     |
| Admin state  | is up     |     |                    |        |     |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | llfc   | rx                   |     |     |     |     |     |
| -------------------- | ------ | -------------------- | --- | --- | --- | --- | --- |
| Statistics           |        |                      |     | RX  |     |     |     |
| -------------------- |        | -------------------- |     |     |     |     |     |
| Dot3 Pause           | Frames |                      |     | 0   |     |     |     |
ShowingdetailedflowcontrolinformationwithRXflowcontrolenabled:
| switch# show | interface |     | 1/1/1 flow-control | detail |     |     |     |
| ------------ | --------- | --- | ------------------ | ------ | --- | --- | --- |
| Interface    | 1/1/1 is  | up  |                    |        |     |     |     |
| Admin state  | is up     |     |                    |        |     |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | llfc      | rx                   |          |     |     |     |     |
| -------------------- | --------- | -------------------- | -------- | --- | --- | --- | --- |
| Flow-control         | watchdog: |                      | disabled |     |     |     |     |
| Statistics           |           |                      |          | RX  |     |     |     |
| -------------------- |           | -------------------- |          |     |     |     |     |
| Dot3 Pause           | Frames    |                      |          | 0   |     |     |     |
Interfaceconfiguration|90

ShowingdetailedflowcontrolinformationwithRXTXflowcontrolenabled:
| switch#   | show  | interface | 1/1/1 flow-control | detail |     |
| --------- | ----- | --------- | ------------------ | ------ | --- |
| Interface |       | 1/1/1 is  | up                 |        |     |
| Admin     | state | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        |       | llfc   | rxtx                 |                      |     |
| -------------------- | ----- | ------ | -------------------- | -------------------- | --- |
| Statistics           |       |        |                      | RX                   | TX  |
| -------------------- |       |        | -------------------- | -------------------- |     |
| Dot3                 | Pause | Frames |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabled:
| switch#   | show  | interface | 1/1/1 flow-control | detail |     |
| --------- | ----- | --------- | ------------------ | ------ | --- |
| Interface |       | 1/1/1 is  | up                 |        |     |
| Admin     | state | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        |       | pfc      | rxtx-4,5             |                      |     |
| -------------------- | ----- | -------- | -------------------- | -------------------- | --- |
| Statistics           |       |          |                      | RX                   | TX  |
| -------------------- |       |          | -------------------- | -------------------- |     |
| Priority             |       | 0 Pauses |                      | 0                    | 0   |
| Priority             |       | 1 Pauses |                      | 0                    | 0   |
| Priority             |       | 2 Pauses |                      | 0                    | 0   |
| Priority             |       | 3 Pauses |                      | 0                    | 0   |
| Priority             |       | 4 Pauses |                      | 0                    | 0   |
| Priority             |       | 5 Pauses |                      | 0                    | 0   |
| Priority             |       | 6 Pauses |                      | 0                    | 0   |
| Priority             |       | 7 Pauses |                      | 0                    | 0   |
| Total                | Pause | Frames   |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabledandflowcontrolwatchdogdisabled:
switch#
|           | show  | interface | 1/1/1 flow-control | detail |     |
| --------- | ----- | --------- | ------------------ | ------ | --- |
| Interface |       | 1/1/1 is  | up                 |        |     |
| Admin     | state | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        |       | pfc       | rxtx-4,5             |                      |     |
| -------------------- | ----- | --------- | -------------------- | -------------------- | --- |
| Flow-control         |       | watchdog: | disabled             |                      |     |
| Statistics           |       |           |                      | RX                   | TX  |
| -------------------- |       |           | -------------------- | -------------------- |     |
| Priority             |       | 0 Pauses  |                      | 0                    | 0   |
| Priority             |       | 1 Pauses  |                      | 0                    | 0   |
| Priority             |       | 2 Pauses  |                      | 0                    | 0   |
| Priority             |       | 3 Pauses  |                      | 0                    | 0   |
| Priority             |       | 4 Pauses  |                      | 0                    | 0   |
| Priority             |       | 5 Pauses  |                      | 0                    | 0   |
| Priority             |       | 6 Pauses  |                      | 0                    | 0   |
| Priority             |       | 7 Pauses  |                      | 0                    | 0   |
| Total                | Pause | Frames    |                      | 0                    | 0   |
| Interface            |       | 1/1/1 is  | up                   |                      |     |
| Admin                | state | is up     |                      |                      |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: |     | pfc | rxtx-4,5 |     |     |
| ------------- | --- | --- | -------- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 91

| Flow-control         | watchdog: | disabled             |                      |     |
| -------------------- | --------- | -------------------- | -------------------- | --- |
| Statistics           |           |                      | RX                   | TX  |
| -------------------- |           | -------------------- | -------------------- |     |
| Priority             | 0 Pauses  |                      | 0                    | 0   |
| Priority             | 1 Pauses  |                      | 0                    | 0   |
| Priority             | 2 Pauses  |                      | 0                    | 0   |
| Priority             | 3 Pauses  |                      | 0                    | 0   |
| Priority             | 4 Pauses  |                      | 0                    | 0   |
| Priority             | 5 Pauses  |                      | 0                    | 0   |
| Priority             | 6 Pauses  |                      | 0                    | 0   |
| Priority             | 7 Pauses  |                      | 0                    | 0   |
| Total Pause          | Frames    |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithbothPFCandflowcontrolwatchdogenabled:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | pfc               | rxtx-4,5             |                      |     |
| -------------------- | ----------------- | -------------------- | -------------------- | --- |
| Flow-control         | watchdog:         | enabled              |                      |     |
| Statistics           |                   |                      | RX                   | TX  |
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
Interfaceconfiguration|92

Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butcouldnotbeappliedbecauseacompatibleflowcontrolmodefirstrequiresareboot:
| switch#   | show interface | 1/1/1 | flow-control |     | detail |     |     |
| --------- | -------------- | ----- | ------------ | --- | ------ | --- | --- |
| Interface | 1/1/1 is       | up    |              |     |        |     |     |
| Admin     | state is up    |       |              |     |        |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: | off         |         |         |                                                 |     |     |     |
| ------------- | ----------- | ------- | ------- | ----------------------------------------------- | --- | --- | --- |
| Flow-control  | watchdog:   |         | pending |                                                 |     |     |     |
| Command       | History     |         |         |                                                 |     |     |     |
| Release       |             |         |         | Modification                                    |     |     |     |
| 10.10         |             |         |         | Examplesupdatedwithnewandchangedoutputelements. |     |     |     |
| 10.08         |             |         |         | Commandintroduced.                              |     |     |     |
| Command       | Information |         |         |                                                 |     |     |     |
| Platforms     | Command     | context |         | Authority                                       |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface | link-diagnostics      |     |     |                  |     |     |     |
| -------------- | --------------------- | --- | --- | ---------------- | --- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |     |     | link-diagnostics |     |     |     |
Description
Showsinformationaboutselectlinkdiagnostics,includingMAC,PHY,andTransceiverdiagnostics.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE>        |     |     |     | Specifiestheportidentifierrange. |     |     |     |
| ---------------- | --- | --- | --- | -------------------------------- | --- | --- | --- |
| link-diagnostics |     |     |     | Showslinkdiagnosticsinformation. |     |     |     |
Examples
Showinginterfaceinformationfor1/1/12linkdiagnostics:
| switch# | show interface | 1/1/12 |     | link-diagnostics |     |     |     |
| ------- | -------------- | ------ | --- | ---------------- | --- | --- | --- |
----------------------------------------------------------------------------------
| Interface | 1/1/12 |     | Current | State |     | Changes | Last Change |
| --------- | ------ | --- | ------- | ----- | --- | ------- | ----------- |
----------------------------------------------------------------------------------
| Port Status |        |     | Waiting | for   | link |     |     |
| ----------- | ------ | --- | ------- | ----- | ---- | --- | --- |
| Link Down   | Reason |     | Local   | fault |      |     |     |
Transceiver
| No transceiver |     |     | --  |     |     | 0   | --  |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 93

| TX Fault    |                | --                      |     | 0   | --         |     |
| ----------- | -------------- | ----------------------- | --- | --- | ---------- | --- |
| Transceiver | error          | --                      |     | 0   | --         |     |
| System      | error          | --                      |     | 0   | --         |     |
| DOM error   |                | --                      |     | 0   | --         |     |
| Configuring | transceiver    | --                      |     | 0   | --         |     |
| Transceiver | disabled       | --                      |     | 0   | --         |     |
| Transceiver | unsupported    | --                      |     | 0   | --         |     |
| MAC and     | PHY            |                         |     |     |            |     |
| TX Disabled |                | --                      |     | 0   | --         |     |
| Autoneg     | Incomplete     | --                      |     | 0   | --         |     |
| No Signal   | Detected       | --                      |     | 0   | --         |     |
| No RX Lock  |                | True                    |     | 1   | 22 seconds | ago |
| (Tue Nov    | 14 14:30:48    | UTC 2023)               |     |     |            |     |
| Remote      | Fault          | --                      |     | 0   | --         |     |
| Local Fault |                | True                    |     | 1   | 22 seconds | ago |
| (Tue Nov    | 14 14:30:48    | UTC 2023)               |     |     |            |     |
| Link State  |                | Down                    |     | 1   | 16 seconds | ago |
| (Tue Nov    | 14 14:30:54    | UTC 2023)               |     |     |            |     |
| switch#     | show interface | 1/1/12 link-diagnostics |     |     |            |     |
----------------------------------------------------------------------------------
| Interface | 1/1/12 | Current | State | Changes | Last Change |     |
| --------- | ------ | ------- | ----- | ------- | ----------- | --- |
----------------------------------------------------------------------------------
| Port Status |        | Link | up  |     |     |     |
| ----------- | ------ | ---- | --- | --- | --- | --- |
| Link Down   | Reason | --   |     |     |     |     |
Transceiver
| No transceiver |                 | --        |     | 0   | --         |     |
| -------------- | --------------- | --------- | --- | --- | ---------- | --- |
| TX Fault       |                 | --        |     | 0   | --         |     |
| Transceiver    | error           | --        |     | 0   | --         |     |
| System         | error           | --        |     | 0   | --         |     |
| DOM error      |                 | --        |     | 0   | --         |     |
| Configuring    | transceiver     | --        |     | 0   | --         |     |
| Transceiver    | disabled        | --        |     | 0   | --         |     |
| Transceiver    | unsupported     | --        |     | 0   | --         |     |
| MAC and        | PHY             |           |     |     |            |     |
| TX Disabled    |                 | --        |     | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Autoneg        | Incomplete      | --        |     | 0   | --         |     |
| No Signal      | Detected        | --        |     | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| No RX Lock     |                 | --        |     | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Remote         | Fault           | --        |     | 2   | 21 seconds |     |
| ago (Tue       | Nov 14 14:30:49 | UTC 2023) |     |     |            |     |
| Local Fault    |                 | --        |     | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Link           | State           | Up        |     | 1   | 16 seconds |     |
| ago (Tue       | Nov 14 14:30:54 | UTC 2023) |     |     |            |     |
Showinginterfaceinformationfor1/1/7-1/1/8link-diagnostics:
| switch# | show interface | 1/1/7-1/1/8 | link-diagnostics |     |     |     |
| ------- | -------------- | ----------- | ---------------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Interface | 1/1/7 | Current | State | Changes | Last Change |     |
| --------- | ----- | ------- | ----- | ------- | ----------- | --- |
-------------------------------------------------------------------------------
| Port Status |        | Link | up  |     |     |     |
| ----------- | ------ | ---- | --- | --- | --- | --- |
| Link Down   | Reason | --   |     |     |     |     |
Transceiver
| No transceiver |     | --  |     | 0   | --  |     |
| -------------- | --- | --- | --- | --- | --- | --- |
| TX Fault       |     | --  |     | 0   | --  |     |
Interfaceconfiguration|94

| Transceiver | error           | --        | 0   | --         |     |
| ----------- | --------------- | --------- | --- | ---------- | --- |
| System      | error           | --        | 0   | --         |     |
| DOM error   |                 | --        | 0   | --         |     |
| Configuring | transceiver     | --        | 0   | --         |     |
| Transceiver | disabled        | --        | 0   | --         |     |
| Transceiver | unsupported     | --        | 0   | --         |     |
| MAC and     | PHY             |           |     |            |     |
| TX Disabled |                 | --        | 2   | 22 seconds |     |
| ago (Tue    | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| Autoneg     | Incomplete      | --        | 0   | --         |     |
| No Signal   | Detected        | --        | 2   | 22 seconds |     |
| ago (Tue    | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| No RX       | Lock            | --        | 2   | 22 seconds |     |
| ago (Tue    | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| Remote      | Fault           | --        | 2   | 21 seconds |     |
| ago (Tue    | Nov 14 14:30:49 | UTC 2023) |     |            |     |
| Local       | Fault           | --        | 2   | 22 seconds |     |
| ago (Tue    | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| Link State  |                 | Up        | 1   | 16 seconds |     |
| ago (Tue    | Nov 14 14:30:54 | UTC 2023) |     |            |     |
--------------------------------------------------------------------------------
| Interface | 1/1/8 | Current State | Changes | Last Change |     |
| --------- | ----- | ------------- | ------- | ----------- | --- |
--------------------------------------------------------------------------------
| Port Status |        | Link up |     |     |     |
| ----------- | ------ | ------- | --- | --- | --- |
| Link Down   | Reason | --      |     |     |     |
Transceiver
| No transceiver |                 | --    | 0   | --         |     |
| -------------- | --------------- | ----- | --- | ---------- | --- |
| TX Fault       |                 | --    | 0   | --         |     |
| Transceiver    | error           | --    | 0   | --         |     |
| System         | error           | --    | 0   | --         |     |
| DOM error      |                 | --    | 0   | --         |     |
| Configuring    | transceiver     | --    | 0   | --         |     |
| Transceiver    | disabled        | --    | 0   | --         |     |
| Transceiver    | unsupported     | --    | 0   | --         |     |
| MAC and        | PHY             |       |     |            |     |
| TX Disabled    |                 | --    | 2   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48 UTC | 2023) |     |            |     |
| Autoneg        | Incomplete      | --    | 0   | --         |     |
| No Signal      | Detected        | --    | 2   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48 UTC | 2023) |     |            |     |
| No RX Lock     |                 | --    | 2   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48 UTC | 2023) |     |            |     |
| Remote         | Fault           | --    | 2   | 21 seconds | ago |
| (Tue Nov       | 14 14:30:49 UTC | 2023) |     |            |     |
| Local Fault    |                 | --    | 2   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48 UTC | 2023) |     |            |     |
| Link State     |                 | Up    | 1   | 16 seconds | ago |
| (Tue Nov       | 14 14:30:54 UTC | 2023) |     |            |     |
| Command        | History         |       |     |            |     |
Release Modification
10.14 Commandintroduced.
| Command | Information |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 95

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
9300P Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show interface | statistics |     |     |
| -------------- | ---------- | --- | --- |
show interface [<IFNAME>|<IFRANGE>] statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] statistics monitor [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics monitor [non-zero] [human-readable]
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
| monitor    |     |     | Continuouslymonitorinterfacestatistics.        |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.
| non-zero |     |     | Showsonlynonzerostatistics. |
| -------- | --- | --- | --------------------------- |
Examples
Showingstatisticsofallinterfaces:
Showingstatisticsofallinterfaceswithonlynon-zerostatistics:
Interfaceconfiguration|96

Showing statistics of all interfaces in the human-readable format:

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

Showing monitor statistics:

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

97

Showingmonitorerrorstatisticsinhuman-readableformat:
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
10.11
Addedmoitorparameter.
| 10.10               |         |         | Addedhuman-readableparameter. |
| ------------------- | ------- | ------- | ----------------------------- |
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
Interfaceconfiguration|98

Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfor
differenttransceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPE
andthird-partytransceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskinthe
output.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
detail
Showdetailedinformationfortheinterfaces.
| threshold-violations |     |     | Showthresholdviolationsfortransceivers. |     |     |
| -------------------- | --- | --- | --------------------------------------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingsummarytransceiverinformationwithidentificationofunsupportedtransceivers:
| switch(config)# | show | interface | transceiver |     |     |
| --------------- | ---- | --------- | ----------- | --- | --- |
-------------------------------------------------------------------
| Port   | Type   | Product |        | Serial | Part |
| ------ | ------ | ------- | ------ | ------ | ---- |
| Number | Number |         | Number |        |      |
-------------------------------------------------------------------
| 1/1/1         | SFP+SR      | J9150A     |     | MYxxxxxxxx | 1990-3657 |
| ------------- | ----------- | ---------- | --- | ---------- | --------- |
| 1/1/2         | SFP+ER*     | --         |     | --         | --        |
| 1/2/1         | QSFP+SR4    | JH233A     |     | MYxxxxxxxx | 2005-1234 |
| 1/2/2         | QSFP+ER4*   | --         |     | --         | --        |
| 1/3/1         | SFP28DAC3   | 844477-B21 |     | MYxxxxxxxx | 77fc-7ce7 |
| * unsupported | transceiver |            |     |            |           |
Showingdetailedtransceiverinformation:
| switch(conf#) | show interface |          | transceiver | detailing |     |
| ------------- | -------------- | -------- | ----------- | --------- | --- |
| Transceiver   | in 1/1/1       |          |             |           |     |
| Interface     | Name           | : 1/1/1  |             |           |     |
| Type          |                | : SFP+SR |             |           |     |
| Connector     | Type           | : LC     |             |           |     |
| Wavelength    |                | : 850nm  |             |           |     |
Transfer Distance : 0m (SMF), 30m (OM1), 80m (OM2), 300m (OM3)
| Diagnostic | Support | : DOM       |     |     |     |
| ---------- | ------- | ----------- | --- | --- | --- |
| Product    | Number  | : J9150A    |     |     |     |
| Serial     | Number  | : MYxxxxxxx |     |     |     |
| Part       | Number  | : 1990-3657 |     |     |     |
Status
| Temperature | : 47.65C  |           |     |     |     |
| ----------- | --------- | --------- | --- | --- | --- |
| Voltage     | : 3.31V   |           |     |     |     |
| Tx Bias     | : 8.40mA  |           |     |     |     |
| Rx Power    | : 0.08mW, | -10.96dBm |     |     |     |
| Tx Power    | : 0.56mW, | -2.49dBm  |     |     |     |
| Recent      | Alarms :  |           |     |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 99

| Rx power    | low alarm   |             |           |           |            |
| ----------- | ----------- | ----------- | --------- | --------- | ---------- |
| Rx power    | low warning |             |           |           |            |
| Recent      | Errors :    |             |           |           |            |
| Rx loss     | of signal   |             |           |           |            |
| Transceiver | in 1/1/2    |             |           |           |            |
| Interface   | Name        | : 1/1/2     |           |           |            |
| Type        |             | : unknown   |           |           |            |
| Connector   | Type        | : ??        |           |           |            |
| Wavelength  |             | : ??        |           |           |            |
| Transfer    | Distance    | : ??        |           |           |            |
| Diagnostic  | Support     | : ??        |           |           |            |
| Product     | Number      | : ??        |           |           |            |
|    Serial   | Number      | : ??        |           |           |            |
| Part        | Number      | : ??        |           |           |            |
| Transceiver | in 1/2/1    |             |           |           |            |
| Interface   | Name        | : 1/2/1     |           |           |            |
| Type        |             | : QSFP+SR4  |           |           |            |
| Connector   | Type        | : MPO       |           |           |            |
| Wavelength  |             | : 850nm     |           |           |            |
| Transfer    | Distance    | : 0m (SMF), | 0m (OM1), | 0m (OM2), | 100m (OM3) |
| Diagnostic  | Support     | : DOM       |           |           |            |
| Product     | Number      | : JH233A    |           |           |            |
| Serial      | Number      | : MYxxxxxxx |           |           |            |
| Part        | Number      | : 2005-1234 |           |           |            |
Status
| Temperature | : 44.46C |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
| Voltage     | : 3.30V  |     |     |     |     |
----------------------------------------------
|          | Tx Bias | Rx Power | Tx Power |     |     |
| -------- | ------- | -------- | -------- | --- | --- |
| Channel# | (mA)    | (mW/dBm) | (mW/dBm) |     |     |
----------------------------------------------
| 1        | 6.12        | 0.00, -inf | 0.63, -1.95 |     |     |
| -------- | ----------- | ---------- | ----------- | --- | --- |
| 2        | 6.04        | 0.00, -inf | 0.63, -2.00 |     |     |
| 3        | 6.51        | 0.00, -inf | 0.60, -2.16 |     |     |
| 4        | 6.19        | 0.00, -inf | 0.63, -1.94 |     |     |
| Recent   | Alarms :    |            |             |     |     |
| Channel  | 1 :         |            |             |     |     |
| Rx power | low alarm   |            |             |     |     |
| Rx power | low warning |            |             |     |     |
| Channel  | 2 :         |            |             |     |     |
| Rx power | low alarm   |            |             |     |     |
| Rx power | low warning |            |             |     |     |
| Channel  | 3 :         |            |             |     |     |
| Rx power | low alarm   |            |             |     |     |
| Rx power | low warning |            |             |     |     |
| Channel  | 4 :         |            |             |     |     |
| Rx power | low alarm   |            |             |     |     |
| Rx power | low warning |            |             |     |     |
| Recent   | Errors :    |            |             |     |     |
| Channel  | 1 :         |            |             |     |     |
| Rx Loss  | of Signal   |            |             |     |     |
| Channel  | 2 :         |            |             |     |     |
| Rx Loss  | of Signal   |            |             |     |     |
| Channel  | 3 :         |            |             |     |     |
| Rx Loss  | of Signal   |            |             |     |     |
| Channel  | 4 :         |            |             |     |     |
Interfaceconfiguration|100

| Rx Loss     | of Signal |             |         |     |     |     |
| ----------- | --------- | ----------- | ------- | --- | --- | --- |
| Transceiver | in 1/2/2  |             |         |     |     |     |
| Interface   | Name      | : 1/2/2     |         |     |     |     |
| Type        |           | : unknown   |         |     |     |     |
| Connector   | Type      | : ??        |         |     |     |     |
| Wavelength  |           | : ??        |         |     |     |     |
| Transfer    | Distance  | : ??        |         |     |     |     |
| Diagnostic  | Support   | : ??        |         |     |     |     |
| Product     | Number    | : ??        |         |     |     |     |
| Serial      | Number    | : ??        |         |     |     |     |
| Part        | Number    | : ??        |         |     |     |     |
| Transceiver | in 1/3/1  |             |         |     |     |     |
| Interface   | Name      | : 1/3/1     |         |     |     |     |
| Type        |           | : SFP28DAC3 |         |     |     |     |
| Connector   | Type      | : Copper    | Pigtail |     |     |     |
Transfer Distance : 0.00km (SMF), 0m (OM1), 0m (OM2), 0m (OM3)
| Diagnostic | Support | : None       |     |     |     |     |
| ---------- | ------- | ------------ | --- | --- | --- | --- |
| Product    | Number  | : 844477-B21 |     |     |     |     |
| Serial     | Number  | : MYxxxxxxx  |     |     |     |     |
| Part       | Number  | : 77fc-7ce7  |     |     |     |     |
Showingdetailedtransceiverinformationwithidentificationofunsupportedtransceivers:
| Transceiver | in 1/1/2       |                |               |        |           |          |
| ----------- | -------------- | -------------- | ------------- | ------ | --------- | -------- |
| Interface   | Name           | : 1/1/2        |               |        |           |          |
| Type        |                | : SFP+ER       | (unsupported) |        |           |          |
| Connector   | Type           | : LC           |               |        |           |          |
| Wavelength  |                | : 3590nm       |               |        |           |          |
| Transfer    | Distance       | : 80m (SMF),   | 0m            | (OM1), | 0m (OM2), | 0m (OM3) |
| Diagnostic  | Support        | : DOM          |               |        |           |          |
| Vendor      | Name           | : INNOLIGHT    |               |        |           |          |
| Vendor      | Part Number    | : TR-PX15Z-NHP |               |        |           |          |
| Vendor      | Part Revision: | 1A             |               |        |           |          |
| Vendor      | Serial number: | MYxxxxxxx      |               |        |           |          |
Status
| Temperature | : 28.88C  |         |     |     |     |     |
| ----------- | --------- | ------- | --- | --- | --- | --- |
| Voltage     | : 3.30V   |         |     |     |     |     |
| Tx Bias     | : 65.53mA |         |     |     |     |     |
| Rx Power    | : 0.00mW, | -inf    |     |     |     |     |
| Tx Power    | : 1.47mW, | 1.67dBm |     |     |     |     |
Recent Alarms:
| Rx Power | low alarm   |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
| Rx Power | low warning |     |     |     |     |     |
| Recent   | Errors:     |     |     |     |     |     |
Showingtransceiverthreshold-violations:
switch(config)# show interface transceiver threshold-violations
-----------------------------------------------------
| Port | Type | Channel | Type(s)   | of           | Recent |     |
| ---- | ---- | ------- | --------- | ------------ | ------ | --- |
|      |      |         | Threshold | Violation(s) |        |     |
-----------------------------------------------------
| 1/1/1 | SFP+SR |     | Tx bias | high | warning  |     |
| ----- | ------ | --- | ------- | ---- | -------- | --- |
|       |        |     | 50.52   | mA > | 40.00 mA |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 101

| 1/1/2          | SFP+ER*     |         | ??           |             |     |     |     |
| -------------- | ----------- | ------- | ------------ | ----------- | --- | --- | --- |
| 1/2/1          | QSFP+SR4    | 1       | Tx power     | low alarm   |     |     |     |
|                |             |         | -17.00       | dBm < -0.50 | dBm |     |     |
|                |             | 2       | Tx bias      | low warning |     |     |     |
|                |             |         | 3.12 mA      | < 4.00 mA   |     |     |     |
| 1/2/2          | QSFP+ER4*   |         | ??           |             |     |     |     |
| 1/3/1          | SFP28DAC3   |         | n/a          |             |     |     |     |
| * unsupported  | transceiver |         |              |             |     |     |     |
| Command        | History     |         |              |             |     |     |     |
| Release        |             |         | Modification |             |     |     |     |
| 10.07orearlier |             |         | --           |             |     |     |     |
| Command        | Information |         |              |             |     |     |     |
| Platforms      | Command     | context | Authority    |             |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface | utilization           |     |             |            |     |     |     |
| -------------- | --------------------- | --- | ----------- | ---------- | --- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | utilization | [non-zero] |     |     |     |
Description
Displaysphysicalportthroughputandutilization.
| Parameter   |     |     | Description                      |     |     |     |     |
| ----------- | --- | --- | -------------------------------- | --- | --- | --- | --- |
| <IFNAME>    |     |     | Specifiesaninterfacename.        |     |     |     |     |
| <IFRANGE>   |     |     | Specifiestheportidentifierrange. |     |     |     |     |
| utilization |     |     | Displaysutilizationstatistics.   |     |     |     |     |
| non-zero    |     |     | Displaysnon-zerostatistics       |     |     |     |     |
Examples
Thefollowingexampleshowsportutilizationofallinterfaces:
| switch# | show interface | utilization |     |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|----------------
-----------|----------------------
| Interval | |   | RX  | |   | TX  | | Total | (RX+TX) | |   |
| -------- | --- | --- | --- | --- | ------- | ------- | --- |
Interface seconds | Mbps KPkt/s Util % | Mbps KPkt/s Util % | Mbps
| KPkt/s | Util % | Description |     |     |     |     |     |     |
| ------ | -------------------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|----------------
-----------|----------------------
Interfaceconfiguration|102

| 1/1/1          |             |                       | 300 9578.02  |           | 788.70 95.78 | 25.70 45.89    | 0.26 9603.72   |
| -------------- | ----------- | --------------------- | ------------ | --------- | ------------ | -------------- | -------------- |
| 834.59         | 96.04       | Aruba-AP              |              |           |              |                |                |
| 1/1/2          |             |                       | 300          | 25.71     | 45.90 0.26   | 9581.09 788.96 | 95.81 9606.80  |
| 834.86         | 96.07       | Aruba2530-AP-conce... |              |           |              |                |                |
| 1/1/3 -        | lag123      |                       | 300          | 0.00      | 0.00 0.00    | 0.00 0.00      | 0.00 0.00      |
| 0.00           | 0.00        | ISL:                  | SWRTS-0064-1 |           |              |                |                |
| 1/1/4          |             |                       | 300 9261.79  |           | 804.52 92.62 | 9496.70 823.97 | 94.97 18758.50 |
| 1628.48        | 187.58      | Backup                | data         | center... |              |                |                |
| 1/1/5          |             |                       | 300 9496.70  |           | 823.97 94.97 | 9261.79 804.52 | 92.62 18758.50 |
| 1628.48        | 187.58      | --                    |              |           |              |                |                |
| Command        | History     |                       |              |           |              |                |                |
| Release        |             |                       |              |           | Modification |                |                |
| 10.07orearlier |             |                       |              |           | --           |                |                |
| Command        | Information |                       |              |           |              |                |                |
| Platforms      | Command     |                       | context      |           | Authority    |                |                |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ip | interface |     |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- | --- |
show ip interface <INTERFACE-ID>|{lag|loopback|vlan|tunnel <ID>}
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
| lag <ID> |     |     |     |     | ShowLAGinterfaceinformation,where<ID>is1-256. |     |     |
| -------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- |
loopback <ID> Showloopbackinterfaceinformation,where<ID>is0-255.
| tunnel <ID> |     |     |     |     | Showtunnelinterfaceinformation,where<ID>is1-255. |     |     |
| ----------- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| vlan <ID>   |     |     |     |     | ShowVLANinterfaceinformation,where<ID>is1-4094.  |     |     |
Example
| switch#      | show ip        | interface |     | 1/1/1    |                   |     |     |
| ------------ | -------------- | --------- | --- | -------- | ----------------- | --- | --- |
| Interface    | 1/1/1          | is        | up  |          |                   |     |     |
| Admin state  | is             | up        |     |          |                   |     |     |
| Hardware:    | Ethernet,      |           | MAC | Address: | 70:72:cf:fd:e7:b4 |     |     |
| IP MTU       | 1500           |           |     |          |                   |     |     |
| IP TCP       | MSS 1460       |           |     |          |                   |     |     |
| IPv4 address | 192.168.1.1/24 |           |     |          |                   |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 103

| L3 Counters: | Rx Enabled, |     | Tx Enabled |     |     |       |
| ------------ | ----------- | --- | ---------- | --- | --- | ----- |
| Statistic    |             |     |            | RX  | TX  | Total |
---------------- -------------------- -------------------- --------------------
| L3 Packets   |                   |     |             | 0                 | 0   | 0   |
| ------------ | ----------------- | --- | ----------- | ----------------- | --- | --- |
| L3 Bytes     |                   |     |             | 0                 | 0   | 0   |
| switch#      | show ip interface |     | 1/1/1       |                   |     |     |
| Interface    | 1/1/1 is          | up  |             |                   |     |     |
| Admin state  | is up             |     |             |                   |     |     |
| Hardware:    | Ethernet,         | MAC | Address:    | 70:72:cf:fd:e7:b4 |     |     |
| IP MTU       | 1500              |     |             |                   |     |     |
| IP TCP       | MSS 1460          |     |             |                   |     |     |
| IP Directed  | Broadcast         |     | is Disabled |                   |     |     |
| IPv4 address | 2.2.2.2/32        |     | [unnumbered | to loopback1]     |     |     |
| L3 Counters: | Rx Disabled,      |     | Tx Disabled |                   |     |     |
| switch#      | show ip interface |     | loopback    | 1                 |     |     |
| Interface    | loopback1         | is  | up          |                   |     |     |
| Admin state  | is up             |     |             |                   |     |     |
| Hardware:    | Loopback          |     |             |                   |     |     |
| IP Directed  | Broadcast         |     | is Disabled |                   |     |     |
| IPv4 address | 192.168.1.1/24    |     |             |                   |     |     |
| Command      | History           |     |             |                   |     |     |
| Release      |                   |     |             | Modification      |     |     |
10.14.1000 CommandoutputcandisplayinformationforanIPunnumbered
interfaceandIPTCPMSSconfiguration.
| 10.07orearlier |             |     |         | --        |     |     |
| -------------- | ----------- | --- | ------- | --------- | --- | --- |
| Command        | Information |     |         |           |     |     |
| Platforms      | Command     |     | context | Authority |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip | source-interface |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
Interfaceconfiguration|104

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitches
donothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.This
parameterisavailableonswitchesthatsupportVSX.
Examples
Showing single source IP address configuration settings for sFlow:
| switch#          | show | ip source-interface |     | sflow       |
| ---------------- | ---- | ------------------- | --- | ----------- |
| Source-interface |      | Configuration       |     | Information |
----------------------------------------
| Protocol |     | Source           | Interface |     |
| -------- | --- | ---------------- | --------- | --- |
| -------- |     | ---------------- |           |     |
| sflow    |     | 10.10.10.1       |           |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show | ip source-interface |     | all         |
| ---------------- | ---- | ------------------- | --- | ----------- |
| Source-interface |      | Configuration       |     | Information |
----------------------------------------
| Protocol       |             | Source           | Interface |              |
| -------------- | ----------- | ---------------- | --------- | ------------ |
| --------       |             | ---------------- |           |              |
| all            |             | 1/1/1            |           |              |
| Command        | History     |                  |           |              |
| Release        |             |                  |           | Modification |
| 10.07orearlier |             |                  |           | --           |
| Command        | Information |                  |           |              |
| Platforms      |             | Command          | context   | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | ipv6      | interface      |     |            |
| --------- | --------- | -------------- | --- | ---------- |
| show ipv6 | interface | <INTERFACE-ID> |     | [vsx-peer] |
Description
ShowsstatusandconfigurationinformationforanIPv6interface.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 105

| Parameter |     |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<INTERFACE-ID> SpecifiesaninterfaceID.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#   | show  | ipv6  | interface |     | 1/1/1 |     |     |     |     |
| --------- | ----- | ----- | --------- | --- | ----- | --- | --- | --- | --- |
| Interface |       | 1/1/1 | is        | up  |       |     |     |     |     |
| Admin     | state |       | is up     |     |       |     |     |     |     |
IPv6 address:
|     | 2001:0db8:85a3:0000:0000:8a2e:0370:7334/24 |     |     |     |     |     |     | [VALID] |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- |
IPv6 link-local address: fe80::1e98:ecff:fee3:e800/64 (default)[VALID]
| IPv6 | virtual         |     | address  | configured:     |         |         | none    |                |     |
| ---- | --------------- | --- | -------- | --------------- | ------- | ------- | ------- | -------------- | --- |
| IPv6 | multicast       |     | routing: |                 | disable |         |         |                |     |
| IPv6 | Forwarding      |     | feature: |                 | enabled |         |         |                |     |
| IPv6 | multicast       |     | groups   | locally         |         | joined: |         |                |     |
|      | ff02::ff70:7334 |     |          | ff02::ffe3:e800 |         |         | ff02::1 | ff02::1:ff00:0 |     |
ff02::2
| IPv6 | multicast |          | (S,G)   | entries |             | joined: | none |     |     |
| ---- | --------- | -------- | ------- | ------- | ----------- | ------- | ---- | --- | --- |
| IPv6 | MTU:      | 1524     | (using  | link    | MTU)        |         |      |     |     |
| IPv6 | TCP       | MSS      | 1440    |         |             |         |      |     |     |
| IPv6 | unicast   |          | reverse | path    | forwarding: |         | none |     |     |
| IPv6 | load      | sharing: |         | none    |             |         |      |     |     |
RX
|     |     | 0 packets, |     | 0 bytes |     |     |     |     |     |
| --- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- |
TX
|           |          | 0 packets, |                   | 0 bytes  |                             |                |      |                |         |
| --------- | -------- | ---------- | ----------------- | -------- | --------------------------- | -------------- | ---- | -------------- | ------- |
| switch#   | show     | ipv6       | interface         |          | 1/1/14.1                    |                |      |                |         |
| Interface |          | 1/1/14.1   |                   | is up    |                             |                |      |                |         |
| Admin     | state    |            | is up             |          |                             |                |      |                |         |
|           | IPv6     | address:   |                   |          |                             |                |      |                |         |
|           | 30::1/64 |            | [VALID]           |          |                             |                |      |                |         |
|           | IPv6     | link-local |                   | address: | fe80::b86a:97c0:122:2f42/64 |                |      |                | [VALID] |
|           | IPv6     | virtual    | address           |          | configured:                 |                | none |                |         |
|           | IPv6     | multicast  |                   | routing: | disable                     |                |      |                |         |
|           | IPv6     | Forwarding |                   | feature: | enabled                     |                |      |                |         |
|           | IPv6     | multicast  |                   | groups   | locally                     | joined:        |      |                |         |
|           | ff02::1  |            | ff02::1:ff22:2f42 |          |                             | ff02::1:ff00:1 |      | ff02::1:ff00:0 |         |
ff02::2
|               | IPv6     | multicast |           | (S,G)  | entries | joined:     | none |     |     |
| ------------- | -------- | --------- | --------- | ------ | ------- | ----------- | ---- | --- | --- |
|               | IPv6     | MTU 1500  |           |        |         |             |      |     |     |
|               | IPv6     | TCP MSS   | 1440      |        |         |             |      |     |     |
|               | IPv6     | unicast   | reverse   |        | path    | forwarding: | none |     |     |
|               | IPv6     | load      | sharing:  | none   |         |             |      |     |     |
| Encapsulation |          |           | dot1q     | ID: 20 |         |             |      |     |     |
| switch#       | show     | ipv6      | interface |        | lag2.1  |             |      |     |     |
| Interface     |          | lag2.1    | is        | up     |         |             |      |     |     |
| Admin         | state    |           | is up     |        |         |             |      |     |     |
|               | IPv6     | address:  |           |        |         |             |      |     |     |
|               | 40::1/64 |           | [VALID]   |        |         |             |      |     |     |
Interfaceconfiguration|106

|     | IPv6    | link-local |                   | address:       | fe80::b86a:97c0:122:2f42/64 |                |     |                | [VALID] |
| --- | ------- | ---------- | ----------------- | -------------- | --------------------------- | -------------- | --- | -------------- | ------- |
|     | IPv6    | virtual    | address           | configured:    |                             | none           |     |                |         |
|     | IPv6    | multicast  |                   | routing:       | disable                     |                |     |                |         |
|     | IPv6    | Forwarding |                   | feature:       | enabled                     |                |     |                |         |
|     | IPv6    | multicast  |                   | groups locally |                             | joined:        |     |                |         |
|     | ff02::1 |            | ff02::1:ff22:2f42 |                |                             | ff02::1:ff00:1 |     | ff02::1:ff00:0 |         |
ff02::2
|         | IPv6          | multicast |          | (S,G) entries | joined:     |              | none |     |     |
| ------- | ------------- | --------- | -------- | ------------- | ----------- | ------------ | ---- | --- | --- |
|         | IPv6          | MTU 1500  |          |               |             |              |      |     |     |
|         | IPv6          | TCP MSS   | 1440     |               |             |              |      |     |     |
|         | IPv6          | unicast   | reverse  | path          | forwarding: |              | none |     |     |
|         | IPv6          | load      | sharing: | none          |             |              |      |     |     |
|         | Encapsulation |           | dot1q    | ID: 30        |             |              |      |     |     |
| Command | History       |           |          |               |             |              |      |     |     |
| Release |               |           |          |               |             | Modification |      |     |     |
10.14.1000 CommandoutputcandisplayinformationforanIPunnumbered
interfaceandIPv6TCPMSSconfiguration.
| 10.07orearlier |             |         |     |         |     | --        |     |     |     |
| -------------- | ----------- | ------- | --- | ------- | --- | --------- | --- | --- | --- |
| Command        | Information |         |     |         |     |           |     |     |     |
| Platforms      |             | Command |     | context |     | Authority |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | ipv6 | source-interface |     |     |     |     |     |     |     |
| ---- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
| vrf | <VRF-NAME> |     |     |     |     |     | SpecifiesthenameofaVRF. |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitches
donothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.This
parameterisavailableonswitchesthatsupportVSX.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 107

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
| Protocol            |         | Source Interface |              |
| ------------------- | ------- | ---------------- | ------------ |
| --------            |         | ---------------- |              |
| all                 |         | 1/1/1            |              |
| Command History     |         |                  |              |
| Release             |         |                  | Modification |
| 10.07orearlier      |         |                  | --           |
| Command Information |         |                  |              |
| Platforms           | Command | context          | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
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
| switch(config-if)# |     | no shutdown |     |
| ------------------ | --- | ----------- | --- |
| Command History    |     |             |     |
Interfaceconfiguration|108

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| system interface-group |     |     |     |
| ---------------------- | --- | --- | --- |
system interface-group <GROUP> line-module <SLOT-ID> speed <SPEED>
no system interface-group <GROUP> line-module <SLOT-ID> speed <SPEED>
Description
Configuresthespeedforaninterfacegroup.Afterchanginggroupspeed,onlytransceiverscompatible
withthenewspeedwillbeenabled.
n Allspeed-mismatchedinterfacesinthegroupwillbedisabled.
n Thiscommandcaninterruptactivenetworklinks,userconfirmationisrequiredtoproceed.
Thenoformofthiscommandresetsthespecifiedinterfacegrouptoitsdefault.
| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
| <GROUP>   |     |     | Specifiestheinterfacegrouptoconfigure. |
<SPEED>
Configurestransceiverspeed(10gor25g)foragroup.
Defaultis25g(seetheTransceiverGuideforfurtherdetail).
OnAruba8400SwitchSeries:
n 10gallows1Gbpsor10Gbpstransceiversonly.
25gallows25Gbpstransceiversonly.
n
| <SLOT-ID> |     |     | SpecifiestheslotID ofthelinemodule. |
| --------- | --- | --- | ----------------------------------- |
Examples
Configuringinterfacegroup1online-module1/1toallow10Gbpsandslowertransceivers:
switch(config)# system interface-group 1 line-module 1/1 speed 10g
Changing the group speed will disable all member interfaces that do not match the
new speed.
| Continue        | (y/n)? y |     |     |
| --------------- | -------- | --- | --- |
| Command History |          |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 109

| Release             |         |         | Modification                                |
| ------------------- | ------- | ------- | ------------------------------------------- |
| 10.09.0002          |         |         | Commandintroducedon6400and8400Switchseries. |
| Command Information |         |         |                                             |
| Platforms           | Command | context | Authority                                   |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|     | (#) |     | rightsforthiscommand. |
| --- | --- | --- | --------------------- |
Interfaceconfiguration|110

Chapter 6
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
111
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries)

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
Sourceinterfaceselection|112

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
ip source-interface <PROTOCOL> {<IP-ADDR>|interface <IFNAME>} [vrf <VRF-NAME>]
no ip source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
Description
ConfigurestheIPv4source-interfaceinterfacetouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedconfiguration.
| Parameter  |     |     | Description                      |     |
| ---------- | --- | --- | -------------------------------- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoconfigure. |     |
all
Selectsthesourceforallprotocolscoveredbythis
command.
central
SelectsArubaCentral.
dhcp_relay
SelectsDHCPrelay.Whenyouconfigureadhcp_relay
sourceinterface,youmustalsoenableDHCPrelay
Option82usingthedhcp-relay option 82source-
interfacecommand.
dns
SelectsDNS.
http
SelectsHTTP.
ntp
SelectsNTP.
radius
SelectsRADIUS.
sflow
SelectssFLow.
sftp-scp
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 113

Parameter

Description

Selects SFTP and SCP.

ssh-client

Selects SSH Client.

syslog

Selects the source for syslog packets.

tacacs

Selects the source for TACACS packets.

tftp

Selects TFTP.

Specifies the VRF name.

Specifies the interface name.

Specifies the IPv4 address.

<IFNAME>

<IP-ADDR>

vrf <VRF-NAME>

Specifies the VRF name.

Examples

Configuring IPv4 source-interface interface 1/1/1 to use for the TFTP protocol:

switch(config)# ip source-interface tftp interface 1/1/1

Configuring IPv4 source-interface interface 1/1/2 to use for the TFTP protocol on VRF green :

switch(config)# ip source-interface tftp interface 1/1/2 vrf green

Removing IPv4 source-interface 1/1/1configuration for the TFTP protocol:

switch(config)# no ip source-interface tftp interface 1/1/1

Removing source-interface interface 1/1/2 configuration for TFTP protocol on VRF green:

switch(config)# no ip source-interface tftp interface 1/1/2 vrf green

Configuring source-interface IPv4 10.1.1.1 to use for the TFTP protocol:

switch(config)# ip source-interface tftp 10.1.1.1

Configuring source-interface IPv4 10.1.1.2 to use for the TFTP protocol on VRF green :

switch(config)# ip source-interface tftp 10.1.1.2 vrf green

Removing source-interface IPv4 10.1.1.1 configuration for the TFTP protocol:

Source interface selection | 114

| switch(config)# |     | no  | ip source-interface |     |     | tftp 10.1.1.1 |     |
| --------------- | --- | --- | ------------------- | --- | --- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationforTFTPprotocolonVRFgreen:
| switch(config)# |     | no  | ip source-interface |     |     | tftp 10.1.1.2 | vrf green |
| --------------- | --- | --- | ------------------- | --- | --- | ------------- | --------- |
Configuringsource-interfaceIPv410.1.1.1tousefortheDNSprotocol:
| switch(config)# |     | ip  | source-interface |     |     | dns 10.1.1.1 |     |
| --------------- | --- | --- | ---------------- | --- | --- | ------------ | --- |
Configuringsource-interfaceIPv410.1.1.2tousefortheDNSprotoclonVRF green:
| switch(config)# |     | ip  | source-interface |     |     | dns 10.1.1.2 | vrf green |
| --------------- | --- | --- | ---------------- | --- | --- | ------------ | --------- |
Removingsource-interfaceIPv410.1.1.1configurationfortheDNSprotocol:
| switch(config)# |     | no  | ip source-interface |     |     | tftp 10.1.1.1 |     |
| --------------- | --- | --- | ------------------- | --- | --- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationfortheDNSprotocolonVRFgreen:
| switch(config)# |     | no  | ip source-interface |     |              | dns 10.1.1.2 | vrf green |
| --------------- | --- | --- | ------------------- | --- | ------------ | ------------ | --------- |
| Command History |     |     |                     |     |              |              |           |
| Release         |     |     |                     |     | Modification |              |           |
10.12.1000
|                     |         |     |         |     | Added     | cental, | sftp-scp,andssh-clientparameters. |
| ------------------- | ------- | --- | ------- | --- | --------- | ------- | --------------------------------- |
| 10.07orearlier      |         |     |         |     | --        |         |                                   |
| Command Information |         |     |         |     |           |         |                                   |
| Platforms           | Command |     | context |     | Authority |         |                                   |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 source-interface
| ipv6 source-interface |     |            | <PROTOCOL> | <IPV6-ADDR> |     | [vrf             | <VRF-NAME>] |
| --------------------- | --- | ---------- | ---------- | ----------- | --- | ---------------- | ----------- |
| no source-interface   |     | <PROTOCOL> |            | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |             |
Description
Configuresthesource-interfaceIPv6addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedprotocolconfiguration.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 115

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
Sourceinterfaceselection|116

ipv6 source-interface dns
ipv6 source-interface {dns | all} {interface | X:X::X:X} [vrf <VRF-NAME>]
[no] ipv6 source-interface {dns | all} {interface | X:X::X:X} [vrf <VRF-NAME>]

Description

Configures the IPv6 source-interface or source IP for IPv6 DNS clients.

The no form of this command removes all configurations.

Parameter

<PROTOCOL>

Description

Specifies the protocol to configure.
all

Selects all protocols supported by this command.

central

Selects Aruba Central.

dhcp_relay

Selects DHCP relay.

dns

Selects DNS packet source.

http

Selects HTTP.

ntp

Selects NTP.

radius

Selects radius.

sftp-scp

Selects SFTP and SCP.

sflow

Selects sFLow.

ssh-client

Selects SSH Client.

syslog

Selects syslog.

tacacs

Selects TACACS.

tftp

SelectsTFTP.

ubt

SelectsUBT.

Specifies the IPv6 address.

Specifies the VRF name.

<IPV6-ADDR>

vrf <VRF-NAME>

Examples

Configuring IPv6 source-interface dns :

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

117

| switch(config)# |            | ipv6 | source-interface |               |     |     |
| --------------- | ---------- | ---- | ---------------- | ------------- | --- | --- |
|                 | all        |      | All protocols    |               |     |     |
|                 | central    |      | Aruba Central    | protocol      |     |     |
|                 | dhcp_relay |      | DHCP_RELAY       | protocol      |     |     |
|                 | dns        |      | DNS protocol     |               |     |     |
|                 | http       |      | HTTP protocol    |               |     |     |
|                 | ntp        |      | NTP protocol     |               |     |     |
|                 | radius     |      | RADIUS protocol  |               |     |     |
|                 | sflow      |      | sFlow protocol   |               |     |     |
|                 | sftp-scp   |      | SFTP and         | SCP protocols |     |     |
|                 | ssh-client |      | SSH Client       | protocol      |     |     |
|                 | syslog     |      | syslog protocol  |               |     |     |
|                 | tacacs     |      | TACACS protocol  |               |     |     |
|                 | tftp       |      | TFTP protocol    |               |     |     |
ConfiguringIPv6source-interfacedns:
| switch(config)# |           | ipv6 | source-interface |     | dns |     |
| --------------- | --------- | ---- | ---------------- | --- | --- | --- |
| X:X::X:X        | Specify   |      | an IPv6 address  |     |     |     |
| interface       | Interface |      | information      |     |     |     |
ConfiguringIPv6source-interfacednson1::1:
switch(config)#
|     |                   | ipv6 | source-interface |     | dns 1::1 |     |
| --- | ----------------- | ---- | ---------------- | --- | -------- | --- |
| vrf | VRF Configuration |      |                  |     |          |     |
<cr>
ConfiguringIPv6source-interfacednson1::1:vrf:
| switch(config)# |     | ipv6 | source-interface |     | dns 1::1 | vrf |
| --------------- | --- | ---- | ---------------- | --- | -------- | --- |
| VRF_NAME        | VRF | name |                  |     |          |     |
ConfiguringIPv6source-interfacednson1::1vrfBLUE
| switch(config)# |     | ipv6 | source-interface |     | dns 1::1 vrf | BLUE |
| --------------- | --- | ---- | ---------------- | --- | ------------ | ---- |
switch(config)#
|     |                   | ipv6 | source-interface |     | dns interface | vlan10 |
| --- | ----------------- | ---- | ---------------- | --- | ------------- | ------ |
| vrf | VRF Configuration |      |                  |     |               |        |
<cr>
ConfiguringIPv6source-interfacednsonvlan10vrfBLUE:
switch(config)# ipv6 source-interface dns interface vlan10 vrf BLUE
| Command | History     |     |     |                    |     |     |
| ------- | ----------- | --- | --- | ------------------ | --- | --- |
| Release |             |     |     | Modification       |     |     |
| 10.13   |             |     |     | Commandintroduced. |     |     |
| Command | Information |     |     |                    |     |     |
Sourceinterfaceselection|118

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

ipv6 source-interface
ipv6 source-interface <PROTOCOL> {<IPV6-ADDR>|interface <IFNAME>} [vrf <VRF-NAME>]
no ipv6 source-interface <PROTOCOL> {<IPV6-ADDR>|interface <IFNAME>} [vrf <VRF-NAME>]

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

dhcp_relay

Selects DHCP relay.

dns

Selects DNS packets

http

Selects HTTP.

ntp

Selects NTP.

radius

Selects radius.

sftp-scp

Selects SFTP and SCP.

sflow

Selects sFLow.

ssh-client

Selects SSH Client.

syslog

Selects syslog.

tacacs

Selects TACACS.

tftp

SelectsTFTP.

Specifies the IPv6 address.

Specifies the interface name.

<IPV6-ADDR>

<IFNAME>

vrf <VRF-NAME>

Specifies the VRF name.

Examples

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

119

ConfiguringIPv6source-interfaceinterface1/1/1tousefortheTFTP protocol:
| switch(config)# | ipv6 source-interface | tftp interface | 1/1/1 |
| --------------- | --------------------- | -------------- | ----- |
ConfiguringIPv6source-interfaceinterface1/1/2tousefortheTFTP protocolonVRFgreen:
switch(config)# ipv6 source-interface tftp interface 1/1/2 vrf green
RemovingIPv6source-interfaceinterface1/1/1configurationfortheTFTP protocol:
switch(config)#
|     | no ipv6 source-interface | tftp interface | 1/1/1 |
| --- | ------------------------ | -------------- | ----- |
RemovingIPv6source-interfaceinterface1/1/2configurationfortheTFTP protocolonVRFgreen:
switch(config)# no ipv6 source-interface tftp interface 1/1/2 vrf green
Configuringsource-interfaceIPv61111:2222tousefortheTFTP protocol:
| switch(config)# | ipv6 source-interface | tftp 1111:2222 |     |
| --------------- | --------------------- | -------------- | --- |
Configuringsource-interfaceIPv61111:3333touseforTFTPprotocolonVRF green:
| switch(config)# | ipv6 source-interface | tftp 1111:3333 | vrf green |
| --------------- | --------------------- | -------------- | --------- |
Removingsource-interfaceIPv61111:2222configurationforTFTPprotocol:
| switch(config)# | no ipv6 source-interface | tftp 1111:2222 |     |
| --------------- | ------------------------ | -------------- | --- |
Removingsource-interfaceIPv61111:3333configurationforTFTPprotocolonVRFgreen:
switch(config)# no ipv6 source-interface tftp 1111:3333 vrf green
Command History
| Release    | Modification                  |     |     |
| ---------- | ----------------------------- | --- | --- |
| 10.13.0001 | Addedthednsprotocolparameter. |     |     |
10.12.1000 Addedcentral,sftp-scp,dhcp_relayandssh-clientparameters.
| 10.07orearlier | --  |     |     |
| -------------- | --- | --- | --- |
Command Information
Sourceinterfaceselection|120

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

http

Shows the source interface configuration for HTTP.

ntp

Shows the source interface configuration for NTP.

radius

Shows the source interface configuration for radius.

sflow

Shows the source interface configuration for sFLow.

sftp-scp

Shows source interface configuration for SFTP and SCP.

ssh-client

Shows source interface configuration for SSH Client.

syslog

Shows the source interface configuration for syslog.

tacacs

Shows the source interface configuration for TACACS.

tftp

Shows the source interface configuration for TFTP.

vrf <VRF-NAME>

Specifies the VRF name.

all-vrfs

Examples

Shows the source interface configuration for all VRFs.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

121

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
| Command History |     |     |              |     |
| --------------- | --- | --- | ------------ | --- |
| Release         |     |     | Modification |     |
10.12.1000
Added central, sftp-scp,andssh-clientparameters.
| 10.07orearlier      |         |         | --        |     |
| ------------------- | ------- | ------- | --------- | --- |
| Command Information |         |         |           |     |
| Platforms           | Command | context | Authority |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| show ipv6 | source-interface |     |     |     |
| --------- | ---------------- | --- | --- | --- |
show ipv6 source-interface <PROTOCOL> [detail] [vrf <VRF-NAME> | all-vrfs]
Description
DisplaystheIPV6sourceinterfaceinformationconfiguredintherouterforallVRFsoraspecificVRF.
IfaVRF isnotspecified,thedefaultisdisplayed.
Sourceinterfaceselection|122

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
dhcp_relay

Shows the source interface configuration for DHCP
realy.

dns

Shows the source interface configuration for DNS.

http

Shows the source interface configuration for HTTP.

ntp

Shows the source interface configuration for NTP.

radius

Shows the source interface configuration for radius.

sflow

Shows the source interface configuration for sFLow.

sftp-scp

Shows source interface configuration for SFTP and SCP.

ssh-client

Shows source interface configuration for SSH Client.

syslog

Shows the source interface configuration for syslog.

tacacs

Shows the source interface configuration for TACACS.

tftp

Shows the source interface configuration for TFTP.

vrf <VRF-NAME>

Specifies the VRF name.

all-vrfs

Examples

Shows the source interface configuration for all VRF.

Displaying all IPv6 source-interface protocol configurations for default VRF:

switch# show ipv6 source-interface all
Source-interface Configuration Information
------------------------------------------------------------------
Protocol
------------------------------------------------------------------
all
switch#

Src-Interface

1111::2222

Src-IP

VRF

default

Displaying all IPv6 source-interface protocol configuration for VRF red:

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

123

| switch# show     | ipv6 | source-interface |             | all vrf red |     |     |
| ---------------- | ---- | ---------------- | ----------- | ----------- | --- | --- |
| Source-interface |      | Configuration    | Information |             |     |     |
---------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP | VRF |     |
| -------- | --- | ------------- | --- | ------ | --- | --- |
---------------------------------------------------------------
| all |     | 1/1/1 |     | 2005::2 |     | red |
| --- | --- | ----- | --- | ------- | --- | --- |
switch#
Displaying allIPv6source-interfaceprotocolconfigurationsforallVRFs:
| switch# show     | ipv6 | source-interface |             | all all-vrfs |     |     |
| ---------------- | ---- | ---------------- | ----------- | ------------ | --- | --- |
| Source-interface |      | Configuration    | Information |              |     |     |
-------------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP | VRF |     |
| -------- | --- | ------------- | --- | ------ | --- | --- |
-------------------------------------------------------------------
| all |     |       |     | 2222::3333 | all-vrfs |     |
| --- | --- | ----- | --- | ---------- | -------- | --- |
| all |     |       |     | 1111::2222 | default  |     |
| all |     | 1/1/1 |     | 2::2       | red      |     |
DisplayingallIPv6source-interfaceprotocolconfirgurationsfordnsallVRFs:
| switch# show     | ipv6 | source-interface |             | dns all-vrfs |     |     |
| ---------------- | ---- | ---------------- | ----------- | ------------ | --- | --- |
| Source-interface |      | Configuration    | Information |              |     |     |
----------------------------------------------------------------------------------
--
| Protocol |     | Src-Interface |     | Src-IP | VRF |     |
| -------- | --- | ------------- | --- | ------ | --- | --- |
----------------------------------------------------------------------------------
--
| dns                 |         |         |     | 1::3                                            | blue    |     |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- | ------- | --- |
| dns                 |         |         |     | 1::4                                            | default |     |
| dns                 |         |         |     | 1::2                                            | red     |     |
| Command History     |         |         |     |                                                 |         |     |
| Release             |         |         |     | Modification                                    |         |     |
| 10.13               |         |         |     | Addeddnsparameters.                             |         |     |
| 10.12.1000          |         |         |     | Added central,sftp-scp,andssh-clientparameters. |         |     |
| 10.07orearlier      |         |         |     | --                                              |         |     |
| Command Information |         |         |     |                                                 |         |     |
| Platforms           | Command | context |     | Authority                                       |         |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show running-config
show running-config
Description
Displaysthecurrentrunningconfiguration.
Sourceinterfaceselection|124

Examples
Displayingtherunningconfiguration(onlyitemsofinteresttosourceinterfaceselectionareshownin
thisexampleoutputcommand):
ArubaCentralisthepriorityagent.Ifnocommandisspecifiedforipsource-interface,Centralwillchoosethe
commandautomaticallyifitisreachableonanyoftheknownports.
| switch# show running-config |     |     |     |     |
| --------------------------- | --- | --- | --- | --- |
vrf green
| ip source-interface   | tftp interface     | 1/1/2 | vrf       | green     |
| --------------------- | ------------------ | ----- | --------- | --------- |
| ip source-interface   | radius interface   |       | 1/1/2     | vrf green |
| ip source-interface   | ntp interface      | 1/1/2 | vrf       | green     |
| ip source-interface   | tacacs interface   |       | 1/1/2     | vrf green |
| ip source-interface   | dns interface      | 1/1/2 | vrf       | green     |
| ip source-interface   | central interface  |       | 1/1/2     | vrf green |
| ip source-interface   | all interface      | 1/1/2 | vrf       | green     |
| ipv6 source-interface | tftp 2222::3333    |       | vrf       | green     |
| ipv6 source-interface | radius 2222::3333  |       | vrf       | green     |
| ipv6 source-interface | ntp 2222::3333     |       | vrf green |           |
| ipv6 source-interface | tacacs 2222::3333  |       | vrf       | green     |
| ipv6 source-interface | central 2222::3333 |       | vrf       | green     |
| ipv6 source-interface | all 2222::3333     |       | vrf green |           |
| ip source-interface   | tftp 10.20.3.1     |       |           |           |
| ip source-interface   | radius 10.20.3.1   |       |           |           |
| ip source-interface   | ntp 10.20.3.1      |       |           |           |
| ip source-interface   | tacacs 10.20.3.1   |       |           |           |
| ip source-interface   | dns 10.20.3.1      |       |           |           |
| ip source-interface   | central 10.20.3.1  |       |           |           |
| ip source-interface   | all 10.20.3.1      |       |           |           |
interface 1/1/1
no shutdown
| ip address 10.20.3.1/24 |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
interface 1/1/2
| vrf attach green       |               |     |     |     |
| ---------------------- | ------------- | --- | --- | --- |
| ip address 20.1.1.1/24 |               |     |     |     |
| ipv6 address           | 2222::3333/64 |     |     |     |
interface 1/1/45
no shutdown
| ip address 100.1.0.1/24 |               |     |     |     |
| ----------------------- | ------------- | --- | --- | --- |
| ipv6 address            | 1111::2222/64 |     |     |     |
| ip route 100.2.0.0/24   | 10.20.3.2     |     |     |     |
switch#
Command History
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
Command Information
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 125

Platforms

Command context

Authority

All platforms

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

Source interface selection | 126

Chapter 7

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

127

Chapter 8
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
| Table 1: Configurationfromandtothesamebuild |     |            |         |           |
| ------------------------------------------- | --- | ---------- | ------- | --------- |
| From/to                                     |     | Checkpoint | Running | Startup   |
| Checkpoint                                  |     | N/A        |         | Supported |
Supported
| Running                                                      |     | Supported  | N/A       | Supported |
| ------------------------------------------------------------ | --- | ---------- | --------- | --------- |
| Startup                                                      |     | Supported  | Supported | N/A       |
| ConfigfromURLinCLIFormat                                     |     | Supported  | Supported | Supported |
| ConfigfromURLinJSONFormat                                    |     | Supported  | Supported | Supported |
| Table 2: Configurationfromanolderbuildtoanewerbuild(upgrade) |     |            |           |           |
| From/to                                                      |     | Checkpoint | Running   | Startup   |
ConfigfromURLinCLIFormat Notsupported Notsupported Notsupported
128
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries)

From/to

Checkpoint

Running

Startup

Config from URL in JSON Format

Not supported

Not supported

Not supported

Startup

Not supported

Supported

Supported

Table 3: Configuration from a newer build to an older build (downgrade)

From/to

Checkpoint

Running

Startup

Config from URL in CLI Format

Not supported

Not supported

Not supported

Config from URL in JSON Format

Not supported

Not supported

Not supported

Startup

Not supported

Not supported

Not supported

Hot-patch software

Overview

Hot-patching provides users of AOS-CX with a way to update running software without rebooting their
system. Hot-patches are distributed as signed .patch files and are applied on top of an official AOS-CX
image.

A hot-patch can be downloaded from a remote server onto an AOS-CX switch then applied without
rebooting the switch. By default, the software patch remains on the switch after it is applied, and is
automatically reapplied when the switch reboots. In order to revert an applied hot-patch update, the
patch must be disabled. When the hot-patch is disabled, rebooting the box is not necessary, though the
hot-patch will still remain on the system. The hot-patch can be removed from the system after disabling
the hot-patch.

Once a downloaded hot-patch is removed, it must be downloaded again before it can be reapplied.

Hot-patches are cumulative, meaning that each subsequent patch is a superset of the previous patch(es) for a

given software image. When multiple hot-patches are required, the first should be removed after the second has

been applied.

Prerequisites

n AOS-CX hot-patch software can be obtained from Aruba customer support, and is identified with a

.patch extension. The name of the patch indicates the version of AOS-CX to which it can be applied.
For example, the patch FL.10.12.XXXX-YYYY.patch indicates that the patch can be applied on top of
switch image FL.10.12.XXXX.swi and brings software up to date with the FL.10.12.YYYY release.

n Hot-patch software can be applied only after it has been downloaded to the switch.

Caveats and limitations

n Hot-patch files cannot be managed when the switch is loaded with a .swi image that does not

support the hot-patch feature.

n Only restartable daemons can be updated with a hot-patch file.

Configuration and firmware management | 129

n Eachhot-patchappliestoonlyonereleaseimageandeachsubsequenthot-patchforthatrelease
imageiscumulative.Thismeansthatapplyingthemostrecenthot-patchprovidesallthesamefixes
includedinprevioushot-patches.Assuch,onlyonehot-patchcanbeappliedatatime.
n incompatibleandun-appliedhot-patchesareallowedtoremainonthesystemandintheconfigto
supportrollbacktothepreviousversionofthesoftware,andtoautomaticallyapplyanyhot-patches
thathavebeenpreviouslyapplied.
n Amaximumoftenhot-patchesareallowedtobepresentorpreconfiguredonthesystematatime.
Adaemon/servicemayrestartifithasaharddependencyonanotherservicethatgetsrestartedby
n
beinghot-patched.Uponrebooting,hot-patchesarereappliedafterdaemonshavestarted.
n Thedpsedandhpe-cardddaemoncannothaveahot-patchappliedwhileaswitchoverorfailoveris
inprogress.
| To apply | a hot-patch |     | update |     |     |
| -------- | ----------- | --- | ------ | --- | --- |
1. Requestahot-patchfromArubacustomersupport,thenplacethehot-patchonanFTP-SFTP
server.
2. Usethecopycommandtocopythehot-patchfromtheremoteservertothestandaloneswitchor
VSF.
| 3. Usethehot-patch |     |           | applycommandtoapplythepatch. |     |     |
| ------------------ | --- | --------- | ---------------------------- | --- | --- |
| To unapply         |     | hot-patch | update                       |     |     |
Thisoptiononlyunappliesthepatch,butdoesnotremovethepatchfromthedevice.Thepatchcanbe
reappliedagainsinceitisstillonthedevice.Ifanunappliedpatchneedstoberemoved/deletedfrom
theswitch,itcanberemovedwiththecommandhot-patch remove <patch>.patch.
| switch(config)#          |     |     | show      | hot-patch                      |     |
| ------------------------ | --- | --- | --------- | ------------------------------ | --- |
| Name                     |     |     |           | Status                         |     |
| ------------------------ |     |     |           | ------                         |     |
| FL_10_12_0001-0002.patch |     |     |           | Not applied                    |     |
| switch(config)#          |     |     | hot-patch | apply FL_10_12_0001-0002.patch |     |
switch(config)#
| switch(config)#          |     |     | show         | hot-patch                      |     |
| ------------------------ | --- | --- | ------------ | ------------------------------ | --- |
| Name                     |     |     |              | Status                         |     |
| ------------------------ |     |     |              | ------                         |     |
| FL_10_12_0001-0002.patch |     |     |              | Applied                        |     |
| switch(config)#          |     |     | no hot-patch | apply FL_10_12_0001-0002.patch |     |
| switch(config)#          |     |     | show         | hot-patch                      |     |
| Name                     |     |     |              | Status                         |     |
| ------------------------ |     |     |              | ------                         |     |
| FL_10_12_0001-0002.patch |     |     |              | Not applied                    |     |
switch(config)#
| switch(config)# |          |     | hot-patch | remove FL_10_12_0001-0002.patch |          |
| --------------- | -------- | --- | --------- | ------------------------------- | -------- |
| Do              | you want | to  | save the  | current configuration           | (y/n)? y |
The running configuration was saved to the startup configuration.
switch(config)#
| switch(config)# |           |       | show | hot-patch  |     |
| --------------- | --------- | ----- | ---- | ---------- | --- |
| No              | hot-patch | found | or   | configured |     |
switch(config)#
| To remove/delete |     |     | a patch: |     |     |
| ---------------- | --- | --- | -------- | --- | --- |
Anappliedhot-patchcanbebothunappliedandremovedfromthedevicewiththecommandhot-
patch remove <patch-name>.patch.Thepatchcannotbereappliedunlessitisdownloadedagain.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 130

Checkpoints

A checkpoint is a snapshot of the running configuration of a switch and its relevant metadata during the
time of creation. Checkpoints can be used to apply the switch configuration stored within a checkpoint
whenever needed, such as to revert to a previous, clean configuration. Checkpoints can be applied to
other switches of the same platform. A switch is able to store multiple checkpoints.

Checkpoint types

The switch supports two types of checkpoints:

n System generated checkpoints: The switch automatically generates a system checkpoint whenever

a configuration change occurs.

n User generated checkpoints: The administrator can manually generate a checkpoint whenever

required.

Maximum number of checkpoints

n Maximum checkpoints: 64 (including the startup configuration)

n Maximum user checkpoints: 32

n Maximum system checkpoints: 32

User generated checkpoints

User checkpoints can be created at any time, as long as one configuration difference exists since the last
checkpoint was created. Checkpoints can be applied to either the running or startup configurations on
the switch.

All user generated checkpoints include a time stamp to identify when a checkpoint was created.

A maximum of 32 user generated checkpoints can be created.

System generated checkpoints

System generated checkpoints are automatically created by default. Whenever a configuration change
occurs, the switch starts a timeout counter (300 seconds by default). For each additional configuration
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

Configuration and firmware management | 131

| Restoring            | a checkpoint | to a... | File type supported |     |
| -------------------- | ------------ | ------- | ------------------- | --- |
| Runningconfiguration |              |         | n CLI               |     |
n JSON
n Checkpoint
Startupconfiguration
n JSON
n Checkpoint
| Specifiedcheckpoint |     |     | Specifiedcheckpoint |     |
| ------------------- | --- | --- | ------------------- | --- |
Rollback
Thetermrollbackisusedtorefertowhenaswitchconfigurationisrevertedtoapre-existing
checkpoint.
Forexample,thefollowingcommandappliestheconfigurationfromcheckpointckpt1.Allprevious
configurationsarelostaftertheexecutionofthiscommand:checkpoint rollback ckpt1
Youcanalsospecifytherollbackoftherunningconfigurationorofthestartupconfigurationwitha
specifiedcheckpoint,asshownwiththefollowingcommand:copy checkpoint <checkpoint-name>
| {running-config | | startup-config} |      |     |     |
| --------------- | ----------------- | ---- | --- | --- |
| Checkpoint      | auto              | mode |     |     |
Checkpointautomodeconfigurestheswitchwithfailoversupport,causingittoautomaticallyreverttoa
previousconfigurationifitbecomesinoperableorinaccessibleduetoconfigurationchangesthatare
beingmade.
Afterenteringcheckpointautomode,youhaveasetamountoftimetoadd,remove,ormodifythe
existingswitchconfiguration.Tosaveyourchanges,youmustexecutethecheckpoint auto confirm
commandbeforetheautomodetimerexpires.Ifyoudonotexecutethecheckpoint auto confirm
commandwithinthespecifiedtime,allconfigurationchangesyoumadearediscardedandtherunning
configurationrevertstothestateitwasbeforeenteringcheckpointautomode.
| Testing | a switch | configuration | in checkpoint | auto mode |
| ------- | -------- | ------------- | ------------- | --------- |
Processoverview:
1. Enablethecheckpointautomode.
2. Tosavetheconfiguration,enterthecheckpoint auto confirmcommandbeforethespecified
timesetinstep1.
| Checkpoint | commands                   |     |     |     |
| ---------- | -------------------------- | --- | --- | --- |
| checkpoint | auto                       |     |     |     |
| checkpoint | auto <TIME-LAPSE-INTERVAL> |     |     |     |
Description
Startsautocheckpointmode.Inautocheckpointmode,theswitchtemporarilysavestheruntime
configurationasacheckpointonlyforthespecifiedtimelapseinterval.Configurationchangesmustbe
savedbeforetheintervalexpires,otherwisetheruntimeconfigurationisrestoredfromthetemporary
checkpoint.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 132

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<TIME-LAPSE-INTERVAL> Specifiesthetimelapseintervalinminutes.Range:1to60.
Usage
Tosavetheruntimecheckpointpermanently,runthecheckpoint auto confirmcommandduringthe
timelapseinterval.ThefilenameforthesavedcheckpointisnamedAUTO<YYYYMMDDHHSS>.Ifthe
checkpoint auto confirmcommandisnotenteredduringthespecifiedtimelapseinterval,the
previousruntimeconfigurationisrestored.
Examples
Confirmingtheautocheckpoint:
| switch#         | checkpoint | auto 20 |                 |
| --------------- | ---------- | ------- | --------------- |
| Auto checkpoint | mode       | expires | in 20 minute(s) |
switch# WARNING Please "checkpoint auto confirm" within 2 minutes
| switch#    | checkpoint         | auto confirm |         |
| ---------- | ------------------ | ------------ | ------- |
| checkpoint | AUTO20170801011154 |              | created |
Inthisexample,theruntimecheckpointwassavedbecausethecheckpoint auto confirmcommand
wasenteredwithinthevaluesetbythetime-lapse-intervalparameter,whichwas20minutes.
Notconfirmingtheautocheckpoint:
| switch#         | checkpoint | auto 20 |                 |
| --------------- | ---------- | ------- | --------------- |
| Auto checkpoint | mode       | expires | in 20 minute(s) |
switch# WARNING Please "checkpoint auto confirm" within 2 minutes
WARNING: Restoring configuration. Do NOT add any new configuration.
| Restoration | successful |     |     |
| ----------- | ---------- | --- | --- |
Inthisexample,theruntimecheckpointwasrevertedbecausethecheckpoint auto confirmcommand
wasnotenteredwithinthevaluesetbythetime-lapse-intervalparameter,whichwas20minutes.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| checkpoint | auto         | confirm |     |
| ---------- | ------------ | ------- | --- |
| checkpoint | auto confirm |         |     |
Description
Configurationandfirmwaremanagement |133

Signalstotheswitchtosavetherunningconfigurationusedduringtheautocheckpointmode.This
commandalsoendstheautocheckpointmode.
Usage
Tosavetheruntimecheckpointpermanently,runthecheckpoint auto confirmcommandduringthe
timelapsevaluesetbythecheckpoint auto TIME-LAPSE-INTERVALcommand.Thegenerated
checkpointnamewillbeintheformatAUTO<YYYYMMDDHHSS>.Ifthecheckpoint auto confirm
commandisnotenteredduringthespecifiedtimelapseinterval,thepreviousruntimeconfigurationis
restored.
Examples
Confirmingtheautocheckpoint:
switch#
| checkpoint          |         | auto confirm |              |
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
Showsthedifferenceinconfigurationbetweentwoconfigurations.Comparecheckpoints,therunning
configuration,orthestartupconfiguration.
Parameter Description
{<CHECKPOINT-NAME1> | running-config | startup-config} Selectseitheracheckpoint,the
runningconfiguration,orthestartup
configurationasthebaseline.
{<CHECKPOINT-NAME2> | running-config | startup-config} Selectseitheracheckpoint,the
runningconfiguration,orthestartup
configurationtocompare.
Usability
| Theoutputofthecheckpoint |     | diffcommandhasseveralsymbols: |     |
| ------------------------ | --- | ----------------------------- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 134

n Theplussign(+)atthebeginningofalineindicatesthatthelineexistsinthecomparisonbutnotin
thebaseline.
n Theminussign(-)atthebeginningofalineindicatesthatthelineexistsinthebaselinebutnotinthe
comparison.
Examples
Inthefollowingexample,theconfigurationsofcheckpointscp1andcp2aredisplayedbeforethe
checkpoint diffcommand,sothatyoucanseethecontextofthecheckpoint diffcommand.
| switch#    | show checkpoint | cp1 |
| ---------- | --------------- | --- |
| Checkpoint | configuration:  |     |
!
| !Version   | AOS-CX XL.10.00.0002 |        |
| ---------- | -------------------- | ------ |
| !Schema    | version 0.1.8        |        |
| module 1/1 | product-number       | jl363a |
!
!
!
!
!
!
!
vlan 1,200
| interface | 1/1/1 |     |
| --------- | ----- | --- |
no shutdown
| ip address | 1.0.0.1/24 |     |
| ---------- | ---------- | --- |
| interface  | 1/1/2      |     |
no shutdown
| ip address | 2.0.0.1/24      |     |
| ---------- | --------------- | --- |
| switch#    | show checkpoint | cp2 |
| Checkpoint | configuration:  |     |
!
| !Version   | AOS-CX XL.10.00.0002 |        |
| ---------- | -------------------- | ------ |
| !Schema    | version 0.1.8        |        |
| module 1/1 | product-number       | jl363a |
!
!
!
!
!
!
!
vlan 1,200,300
| interface | 1/1/1 |     |
| --------- | ----- | --- |
no shutdown
| ip address | 1.0.0.1/24 |     |
| ---------- | ---------- | --- |
| interface  | 1/1/2      |     |
no shutdown
| ip address | 2.0.0.1/24 |     |
| ---------- | ---------- | --- |
switch#
|     | checkpoint diff | cp1 cp2 |
| --- | --------------- | ------- |
--- /tmp/chkpt11501550258421 2017-08-01 01:17:38.420514016 +0000
+++ /tmp/chkpt21501550258421 2017-08-01 01:17:38.420514016 +0000
| @@ -9,7 | +9,7 @@ |     |
| ------- | ------- | --- |
!
!
!
-vlan 1,200
+vlan 1,200,300
Configurationandfirmwaremanagement |135

| interface          | 1/1/1 |              |         |
| ------------------ | ----- | ------------ | ------- |
| no shutdown        |       |              |         |
| ip address         |       | 1.0.0.1/24   |         |
| switch# checkpoint |       | diff chkpt01 | chkpt02 |
--- /tmp/chkpt011607564301327
+++ /tmp/chkpt021607564301353
| @@ -1,7 +1,7 | @@  |     |     |
| ------------ | --- | --- | --- |
!
| !Version          | AOS-CX  | PL.10.06.0100V |                     |
| ----------------- | ------- | -------------- | ------------------- |
| !export-password: |         | default        |                     |
| -hostname         | Switch  |                |                     |
| +hostname         | Switch1 |                |                     |
| user admin        | group   | administrators | password ciphertext |
AQBapTyg9tpaiAaTfSVV5eNdFzOORRvZ6CMpglh1P+LQUHQLYgAAAGAhmRqFbkNvrgy2SBVk7H8C5hvg/I
ib8rWYFZLEaSCrobNP9EwMu+hLNM0xmsh45yG8dncP7WkxjwrW4p4Qra6dVfr0EW8xh/lpQf8F/2Wki20L
c9JLXiYge7ti0H6cVn+G
| radius-server | tracking | interval | 60  |
| ------------- | -------- | -------- | --- |
no usb
switch#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 136

Systemcheckpointscanbeappliedusingthecheckpointrollbackfeatureorcopycommand.
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
Configurationandfirmwaremanagement |137

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 138

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
Configurationandfirmwaremanagement |139

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 140

Description
Copiesanexistingcheckpointconfigurationtotherunningconfigurationortothestartupconfiguration.
| Parameter         |     |     | Description                             |     |
| ----------------- | --- | --- | --------------------------------------- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofanexistingcheckpoint. |     |
{running-config | startup-con- Selectswhethertherunningconfigurationorthestartup
configurationreceivesthecopiedcheckpointconfiguration.Ifthe
fig}
startupconfigurationisalreadypresent,thecommandoverwrites
thestartupconfiguration.
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
Configurationandfirmwaremanagement |141

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<CHECKPOINT-NAME> Specifiesthenameofthecheckpointtocopy.Thecheckpoint
namecanbealphanumeric.Itcanalsocontainunderscores(_)
anddashes(-).
<STORAGE-URL>>
SpecifiesthenameofthetargetfileontheUSBdriveusingthe
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 142

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
NOTE:DonotstartthecheckpointnamewithCPCbecauseitis
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
Configurationandfirmwaremanagement |143

Parameter

Description

{running-config | startup-config}

Selects whether the running configuration or the startup
configuration receives the copied checkpoint configuration. If
the startup configuration is already present, the command
overwrites the startup configuration.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

Usage

The switch copies only certain file types. The format of the file is automatically detected from contents
of the file. The startup-config option only supports the JSON file format and checkpoints, but the
running-config option supports the JSON and CLI file formats and checkpoints.

When a file of the CLI format is copied, it overwrites the running configuration. The CLI command does
not clear the running configuration before applying the CLI commands. All of the CLI commands in the
file are applied line-by-line. If a particular CLI command fails, the switch logs the failure and it continues
to the next line in the CLI configuration. The event log (show events -d hpe-config) provides
information as to which command failed.

Examples

Copying a JSON format file to the running configuration:

switch# copy tftp://192.168.1.10/runjson running-config
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size

--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--

Success

Copying a CLI format file to the running configuration with an error in the file:

switch# copy tftp://192.168.1.10/runcli running-config
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size

--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--

Some of the configuration lines from the file were NOT applied. Use 'show
events -d hpe-config' for more info.
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size

--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--

Some of the configuration lines from the file were NOT applied. Use 'show
events -d hpe-config' for more info.

Copying a CLI format file to the startup configuration:

switch# copy tftp://192.168.1.10/startjson startup-config
######################################################################### 100.0%
100.0%
Success

Copying an unsupported file format to the startup configuration:

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

144

| switch# copy | tftp://192.168.1.10/startfile |     |     | startup-config |
| ------------ | ----------------------------- | --- | --- | -------------- |
######################################################################### 100.0%
100.0%
| unsupported         | file format |         |              |     |
| ------------------- | ----------- | ------- | ------------ | --- |
| Command History     |             |         |              |     |
| Release             |             |         | Modification |     |
| 10.07orearlier      |             |         | --           |     |
| Command Information |             |         |              |     |
| Platforms           | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy running-config {startup-config | checkpoint <CHECKPOINT-
NAME>}
copy running-config {startup-config | checkpoint <CHECKPOINT-NAME>}
Description
Copiestherunningconfigurationtothestartupconfigurationortoanewcheckpoint.Ifthestartup
configurationisalreadypresent,thecommandoverwritestheexistingstartupconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
startup-config
Specifiesthatthestartupconfigurationreceivesacopyofthe
runningconfiguration.
checkpoint <CHECKPOINT-NAME> Specifiesthenameofanewcheckpointtoreceiveacopyofthe
runningconfiguration.Thecheckpointnamecanbecomprisedof
alphanumericcharacter,underscores(_)anddashes(-),andmust
be32charactersorfewer.
NOTE:DonotstartthecheckpointnamewithCPCbecauseitis
usedforsystem-generatedcheckpoints.
Examples
Copyingtherunningconfigurationtothestartupconfiguration:
| switch# copy | running-config | startup-config |     |     |
| ------------ | -------------- | -------------- | --- | --- |
Success
Copyingtherunningconfigurationtoanewcheckpointnamedckpt1:
| switch# copy | running-config | checkpoint | ckpt1 |     |
| ------------ | -------------- | ---------- | ----- | --- |
Success
Configurationandfirmwaremanagement |145

| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy {running-config |     | | startup-config} |     | <REMOTE-URL> |     |
| -------------------- | --- | ----------------- | --- | ------------ | --- |
copy {running-config | startup-config} <REMOTE-URL> {cli | json} [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationorthestartupconfigurationtoaremotefileineitherCLIorJSON
format.
| Parameter       |                   |     | Description |     |     |
| --------------- | ----------------- | --- | ----------- | --- | --- |
| {running-config | | startup-config} |     |             |     |     |
Selectswhethertherunningconfigurationorthestartup
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
| {cli | | json} |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
Selectstheremotefileformat:P:CLIorJSON.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |     |
| -------------- | --- | --- | --------------------------------------- | --- | --- |
Examples
CopyingarunningconfigurationtoaremotefileinCLIformat:
| switch# | copy running-config | tftp://192.168.1.10/runcli |     |     | cli |
| ------- | ------------------- | -------------------------- | --- | --- | --- |
######################################################################### 100.0%
Success
CopyingarunningconfigurationtoaremotefileinJSONformat:
switch#
|     | copy running-config | tftp://192.168.1.10/runjson |     |     | json |
| --- | ------------------- | --------------------------- | --- | --- | ---- |
######################################################################### 100.0%
Success
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 146

CopyingastartupconfigurationtoaremotefileinCLIformat:
switch# copy startup-config sftp://root@192.168.1.10/startcli cli
| root@192.168.1.10's |                  | password:         |     |     |
| ------------------- | ---------------- | ----------------- | --- | --- |
| sftp> put           | /tmp/startcli    | startcli          |     |     |
| Uploading           | /tmp/startcli    | to /root/startcli |     |     |
| Connected           | to 192.168.1.10. |                   |     |     |
Success
CopyingastartupconfigurationtoaremotefileinJSONformat:
switch# copy startup-config sftp://root@192.168.1.10/startjson json
| root@192.168.1.10's |     | password: |     |     |
| ------------------- | --- | --------- | --- | --- |
sftp>
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
| {cli | json} |     |     | Selectstheformatoftheremotefile:CLIorJSON. |     |
| ------------ | --- | --- | ------------------------------------------ | --- |
Usage
TheswitchsupportsJSONandCLIfileformatswhencopyingtherunningorstartingconfigurationtothe
USBdrive.TheUSBdrivemustbeformattedwiththeFATfilesystem.
TheUSBdrivemustbeenabledandmountedwiththefollowingcommands:
Configurationandfirmwaremanagement |147

| switch(config)# | usb |     |     |     |
| --------------- | --- | --- | --- | --- |
switch(config)#
end
| switch# usb | mount |     |     |     |
| ----------- | ----- | --- | --- | --- |
Examples
CopyingarunningconfigurationtoafilenamedrunCLIontheUSBdrive:
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
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
| Command History     |     |     |              |     |
| ------------------- | --- | --- | ------------ | --- |
| Release             |     |     | Modification |     |
| 10.07orearlier      |     |     | --           |     |
| Command Information |     |     |              |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 148

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

copy <STORAGE-URL> running-config
copy <STORAGE-URL> {running-config | startup-config | checkpoint <CHECKPOINT-NAME>}

Description

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

Configuration and firmware management | 149

Success
CopyingthefilestartUpfromtheUSBdrivetothestartupconfiguration:
| switch# | copy usb:/startUp |     | startup-config |     |
| ------- | ----------------- | --- | -------------- | --- |
Success
CopyingthefiletestCheckfromtheUSBdrivetotheabccheckpoint:
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
| Parameter  |                   |     |     | Description                    |
| ---------- | ----------------- | --- | --- | ------------------------------ |
| checkpoint | <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint. |
core-dump
Eraseoneofthefollowingsetsofcore-dumpfiles:
| all|daemon | <daemon-name> |     |     | n all:Eraseallcore-dumpfiles. |
| ---------- | ------------- | --- | --- | ----------------------------- |
|kernel
|     |     |     |     | n daemon<daemon-name>:Erasedaemoncore-dumpfiles. |
| --- | --- | --- | --- | ------------------------------------------------ |
kerne:lErasethekernelcore-dump.
n
n
startup-config
Specifiesthestartupconfiguration.
| all |     |     |     | Specifiesallcheckpoints. |
| --- | --- | --- | --- | ------------------------ |
Examples
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 150

Erasingcheckpointckpt1:
| switch# | erase checkpoint | ckpt1 |     |
| ------- | ---------------- | ----- | --- |
Erasingthestartupconfiguration:
| switch# | erase startup-config |     |     |
| ------- | -------------------- | --- | --- |
Erasingallcheckpoints:
switch#
|                | erase checkpoint | all     |              |
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
Configurationandfirmwaremanagement |151

B+2GB0UBxSF7rvgN2x8KSgkqv7iqXVQ0Te6LkSMnH4BdNaT3Bf25qyvOqmr4YakO1V3rg8zAOADkPktQD8
joTHXflzwomoIzcmv/uX
cli-session

timeout 0

!
!
!
!
ssh server vrf default
vlan 1
spanning-tree
interface lag 1
no shutdown
vlan access 1
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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

152

no shutdown
vlan access 1
| interface | 1/1/15 |     |     |     |
| --------- | ------ | --- | --- | --- |
no shutdown
vlan access 1
| interface | 1/1/16 |     |     |     |
| --------- | ------ | --- | --- | --- |
no shutdown
vlan access 1
| interface | vlan 1 |     |     |     |
| --------- | ------ | --- | --- | --- |
ip dhcp
| snmp-server | vrf | default |     |     |
| ----------- | --- | ------- | --- | --- |
!
!
!
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
Configurationandfirmwaremanagement |153

| Parameter         |     |     | Description                        |
| ----------------- | --- | --- | ---------------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesanexistingcheckpointname. |
| [cli | json]      |     |     | SelectseithertheCLIorJSONformat.   |
Examples
ShowingacheckpointSHA-256hashinJSONformat:
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
| Status  |             | : enabled |     |
| ------- | ----------- | --------- | --- |
| Timeout | (sec) : 300 |           |     |
| Command | History     |           |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 154

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Configurationandfirmwaremanagement |155

| Parameter |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
<END-DATE>
Specifiestheendingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Examples
Showingadetailedlistofsavedcheckpointsforaspecificdaterange:
switch#
|                | show        | checkpoint | date    | 2017-03-08        | 2017-03-12                   |            |               |         |
| -------------- | ----------- | ---------- | ------- | ----------------- | ---------------------------- | ---------- | ------------- | ------- |
| NAME           |             | TYPE       |         | WRITER            | DATE(YYYY/MM/DD)             |            | IMAGE VERSION |         |
| ckpt2          |             | checkpoint |         | User              | 2017-03-08T18:10:01Z         |            | XX.01.01.000X |         |
| ckpt3          |             | checkpoint |         | User              | 2017-03-09T23:11:02Z         |            | XX.01.01.000X |         |
| ckpt4          |             | checkpoint |         | User              | 2017-03-11T00:00:03Z         |            | XX.01.01.000X |         |
| Command        | History     |            |         |                   |                              |            |               |         |
| Release        |             |            |         | Modification      |                              |            |               |         |
| 10.08          |             |            |         | Commandsyntaxshow |                              | checkpoint | list date     | <START- |
|                |             |            |         | DATE>             | <END-DATE>isreplacedwithshow |            | checkpoint    | date    |
|                |             |            |         | <START-DATE>      | <END-DATE>                   |            |               |         |
| 10.07orearlier |             |            |         | --                |                              |            |               |         |
| Command        | Information |            |         |                   |                              |            |               |         |
| Platforms      | Command     |            | context | Authority         |                              |            |               |         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show running-config |     |      | hash   |       |     |     |     |     |
| ------------------- | --- | ---- | ------ | ----- | --- | --- | --- | --- |
| show running-config |     | hash | [cli | | json] |     |     |     |     |
Description
Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutput
formatisnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter |       |     |     | Description                      |     |     |     |     |
| --------- | ----- | --- | --- | -------------------------------- | --- | --- | --- | --- |
| [cli |    | json] |     |     | SelectseithertheCLIorJSONformat. |     |     |     |     |
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 156

| switch# show | running-config |           | hash   | cli     |
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
switch#
| show         | startup-config |           | hash   | cli     |
| ------------ | -------------- | --------- | ------ | ------- |
| Calculating  | the hash:      | [Success] |        |         |
| SHA-256 hash | of the         | config    | in CLI | format: |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,     | etc.). |     |     |     |
| --------------- | ------ | --- | --- | --- |
| Command History |        |     |     |     |
Configurationandfirmwaremanagement |157

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
write memory
write memory
Description
Savestherunningconfigurationtothestartupconfiguration.Itisanaliasofthecommandcopy
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 158

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
Examples
Rebootingthefabricmoduleinslot1/3whenauto-confirmisnotenabled:
| switch# boot | fabric-module | 1/3 |     |
| ------------ | ------------- | --- | --- |
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
Configurationandfirmwaremanagement |159

Description
Rebootsthespecifiedlinemodule.
| Parameter |     |     |     |     | Description                                     |     |
| --------- | --- | --- | --- | --- | ----------------------------------------------- | --- |
| <SLOT-ID> |     |     |     |     | Specifiesthememberandslotofthemoduleintheformat |     |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Rebootsthespecifiedlinemodule.Anytrafficfortheswitchpassingthroughtheaffectedmodule(SSH,
TELNET,andSNMP)isinterrupted.Itcantakeupto2minutestorebootthemodule.Duringthattime,
youcanmonitorprogressbyviewingtheeventlog.
Thiscommandisvalidforlinemodulesonly.
Examples
Reloadingthemoduleinslot1/1:
| switch# boot | line-module |     |     | 1/1 |     |     |
| ------------ | ----------- | --- | --- | --- | --- | --- |
This command will reboot the specified line module and interfaces on this
module will not send or receive packets while the module is down. Any
traffic passing through the line module will be interrupted. Management
sessions connected through the line module will be affected. It might take
up to 2 minutes to complete rebooting the module. During that time, you can
| monitor progress |     | by       | viewing | the | event | log. |
| ---------------- | --- | -------- | ------- | --- | ----- | ---- |
| Do you want      | to  | continue | (y/n)?  |     |       |      |
y
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 160

| Parameter |     |     |     |     | Description                        |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
| active    |     |     |     |     | Selectstheactivemanagementmodule.  |     |     |
| standby   |     |     |     |     | Selectsthestandbymanagementmodule. |     |     |
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
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisnotavailable,
youarewarned,youarepromptedtosavetheconfiguration,andyouarepromptedtoconfirmthe
operation.
Ifyourebootthestandbymanagementmodule,thestandbymanagementmodulerebootsandremains
thestandbymanagementmodule.
Ifyouattempttorebootamanagementmodulethatisnotavailable,thebootcommandisaborted.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,thebootcommandisaborted.
HewlettPackardEnterpriserecommendsthatyouusethebootmanagement-modulecommandinsteadof
pressingthemoduleresetbuttontorebootamanagementmodulebecauseifyouarerebootingtheonly
availablemanagementmodule,thebootmanagement-modulecommandenablesyoutosavethe
configuration,cancelthereboot,orboth.
Examples
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisavailable:
| switch# | boot | management-module |     | active |     |     |     |
| ------- | ---- | ----------------- | --- | ------ | --- | --- | --- |
The management-module in slot 1/5 is going down for reboot now.
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisnotavailable:
| switch#        | boot       | management-module |              | 1/5     |               |                |     |
| -------------- | ---------- | ----------------- | ------------ | ------- | ------------- | -------------- | --- |
| The management |            | module            | in slot      | 1/5     | is currently  | active and     | no  |
| standby        | management |                   | module was   | found.  |               |                |     |
| This will      | reboot     | the               | entire       | switch. |               |                |     |
| Do you         | want       | to save           | the current  |         | configuration | (y/n)? n       |     |
| This will      | reboot     | the               | entire       | switch  | and render    | it unavailable |     |
| until the      | process    |                   | is complete. |         |               |                |     |
Configurationandfirmwaremanagement |161

| Continue       | (y/n)? y    |          |              |     |
| -------------- | ----------- | -------- | ------------ | --- |
| The system     | is going    | down for | reboot.      |     |
| Command        | History     |          |              |     |
| Release        |             |          | Modification |     |
| 10.07orearlier |             |          | --           |     |
| Command        | Information |          |              |     |
| Platforms      | Command     | context  | Authority    |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| boot management-module |     |                | (recovery | console) |
| ---------------------- | --- | -------------- | --------- | -------- |
| boot management-module |     | {local|remote} |           |          |
Description
Rebootsthespecifiedmanagementmodulebyspecifiedlocation(localorremote).
| Parameter |     |     | Description                       |     |
| --------- | --- | --- | --------------------------------- | --- |
| <local>   |     |     | Rebootsthelocalmanagementmodule.  |     |
| <remote>  |     |     | Rebootstheremotemanagementmodule. |     |
Usage
Thiscommandrebootsasinglemanagementmoduleinachassis.Choosethemanagementmoduleto
rebootbyrole(activeorstandby)orbyslotnumber.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisavailable,the
activemanagementmodulerebootsandthestandbymanagementmodulebecomestheactive
managementmodule.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisnotavailable,
youarewarned,youarepromptedtosavetheconfiguration,andyouarepromptedtoconfirmthe
operation.
Ifyourebootthestandbymanagementmodule,thestandbymanagementmodulerebootsandremains
thestandbymanagementmodule.
Ifyouattempttorebootamanagementmodulethatisnotavailable,thebootcommandisaborted.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,thebootcommandisaborted.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 162

HewlettPackardEnterpriserecommendsthatyouusethebootmanagement-modulecommandinsteadof
pressingthemoduleresetbuttontorebootamanagementmodulebecauseifyouarerebootingtheonly
availablemanagementmodule,thebootmanagement-modulecommandenablesyoutosavethe
configuration,cancelthereboot,orboth.
Examples
Bootingaremotemanagementmodule:
| switch# boot | management-module   |     |        | remote     |
| ------------ | ------------------- | --- | ------ | ---------- |
| There is     | no other management |     | module | installed. |
Aborting.
switch#
| Command History     |         |         |     |                    |
| ------------------- | ------- | ------- | --- | ------------------ |
| Release             |         |         |     | Modification       |
| 10.12               |         |         |     | Commandintroduced. |
| Command Information |         |         |     |                    |
| Platforms           | Command | context |     | Authority          |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
boot set-default
| boot set-default | {primary | | secondary} |     |     |
| ---------------- | -------- | ------------ | --- | --- |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     |     | Description                                     |
| --------- | --- | --- | --- | ----------------------------------------------- |
| primary   |     |     |     | Selectstheprimarynetworkoperatingsystemimage.   |
| secondary |     |     |     | Selectsthesecondarynetworkoperatingsystemimage. |
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch# boot    | set-default | primary |          |     |
| --------------- | ----------- | ------- | -------- | --- |
| Default boot    | image       | set to  | primary. |     |
| Command History |             |         |          |     |
Configurationandfirmwaremanagement |163

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

boot system
boot system [primary | secondary | serviceos]

Description

Reboots all modules on the switch. By default, the configured default operating system image is used.
Optional parameters enable you to specify which system image to use for the reboot operation and for
future reboot operations.

Parameter

primary

secondary

serviceos

Usage

Description

Selects the primary operating system image for this reboot and
sets the configured default operating system image to primary
for future reboots.

Selects the secondary operating system image for this reboot and
sets the configured default operating system image to secondary
for future reboots.

Selects the service operating system for this reboot. Does not
change the configured default operating system image. The
service operating system acts as a standalone bootloader and
recovery OS for switches running the AOS-CX operating system
and is used in rare cases when troubleshooting a switch.

This command reboots the entire system. If you do not select one of the optional parameters, the
system reboots from the configured default boot image.

You can use the show images command to show information about the primary and secondary system
images.

Choosing one of the optional parameters affects the setting for the default boot image:

n If you select the primary or secondary optional parameter, that image becomes the configured

default boot image for future system reboots. The command fails if the switch is not able to set the
operating system image to the image you selected.

You can use the boot set-default command to change the configured default operating system
image.

n If you select serviceos as the optional parameter, the configured default boot image remains the

same, and the system reboots all management modules with the service operating system.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

164

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
| until the | process      | is complete.  |               |                |
| Continue  | (y/n)? n     |               |               |                |
Reboot aborted.
switch#
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
Configurationandfirmwaremanagement |165

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

show boot-history
show boot-history [all|{vsf member <1-10>}]

Description

Shows boot history information. When no parameters are specified, shows the most recent information
about the current boot operation, and the three previous boot operations for the switch. When the all
parameter is specified, the output of this command shows the boot information for the active
management module.

For switches that support line modules (such as 8400 switch series) including the all parameter displays
information for the active management module and all available line modules.

To view boot-history on a standby, the command must be sent on the conductor console.

Parameter

all

Description

Optional. Shows boot information for the active management
module. For switches that support line modules, including this
parameter displays information for and all available line modules.

vsf member <1-10>

Optional. Display boot history for the specified VSF member

Usage

This command displays the boot-index, boot-ID, and up time in seconds for the current boot. If there is
a previous boot, it displays boot-index, boot-ID, reboot time (based on the time zone configured in the
system) and reboot reasons. Previous boot information is displayed in reverse chronological order.

The output of this command includes the following information:

Parameter

Index

Boot ID

Current Boot, up for <time>

<Timestamp>: boot reason

Description

The position of the boot in the history file. Range: 0
to 3.

A unique ID for the boot . A system-generated 128-
bit string.

For the current boot, the show boot-history
command shows the number of seconds the
module has been running on the current software.

For previous boot operations, the show boot-
history command shows the time at which the
operation occurred and the reason for the boot.
The reason for the boot is one of the following
values:

n <DAEMON-NAME> crash: The daemon identified

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

166

Parameter Description
by<DAEMON-NAME>causedthemoduletoboot.
n Kernelcrash:Theoperatingsystemsoftware
associatedwiththemodulecausedthemodule
toboot.
n Uncontrolledreboot:Thereasonforthereboot
isnotknown.
n Rebootrequestedthroughdatabase:The
rebootoccurredbecauseofarequestmade
throughtheCLIorotherAPI.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |     |
| ---------- | ----------------- | --- | --- | --- |
| Management | module            |     |     |     |
=================
| Index : | 2                                  |        |     |                     |
| ------- | ---------------------------------- | ------ | --- | ------------------- |
| Boot ID | : c34a2c2499004a02bbeeff4992e1fdbd |        |     |                     |
| Current | Boot, up for                       | 1 days | 13  | hrs 13 mins 27 secs |
| Index : | 1                                  |        |     |                     |
| Boot ID | : bfba9bc486304e57904ac717a0ccbdcd |        |     |                     |
02 Sep 23 02:55:33 : CPU request reset with 0x20201, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:55:33                        | : Switch | boot | count is 2 |
| ------- | ---------------------------------- | -------- | ---- | ---------- |
| Index : | 0                                  |          |      |            |
| Boot ID | : a88a71b7ca9a4574af7e3b811ddfdc7e |          |      |            |
02 Sep 23 02:49:26 : Reboot requested by user, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:50:02                        | : Switch | boot | count is 1 |
| ------- | ---------------------------------- | -------- | ---- | ---------- |
| Index : | 3                                  |          |      |            |
| Boot ID | : f00ba10c8c44457f83fee303d014a89a |          |      |            |
25 Aug 23 10:27:42 : Power on reset with 0x1, Version: FL.10.14.0000-1465-
g9df95249d06b0~dirty
| 25 Aug | 23 10:28:18 | : Switch | boot | count is 3 |
| ------ | ----------- | -------- | ---- | ---------- |
25 Aug 23 10:29:02 : Primary overtemperature fault detected with 0x2 in PSU 1/1
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
switch#
| Management | module |     |     |     |
| ---------- | ------ | --- | --- | --- |
=================
| Index : | 3                                  |          |           |                  |
| ------- | ---------------------------------- | -------- | --------- | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |          |           |                  |
| Current | Boot, up for                       | 22 hrs   | 12        | mins 22 secs     |
| Index : | 2                                  |          |           |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |          |           |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot | requested | through database |
Configurationandfirmwaremanagement |167

| Index :     | 1                                  |     |                    |     |                  |
| ----------- | ---------------------------------- | --- | ------------------ | --- | ---------------- |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |     |                    |     |                  |
| 07 Aug      | 18 14:08:46                        |     | : Reboot requested |     | through database |
| Index :     | 0                                  |     |                    |     |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |     |                    |     |                  |
| 07 Aug      | 18 13:00:46                        |     | : Reboot requested |     | through database |
| Line module |                                    | 1/1 |                    |     |                  |
=================
| Index : | 3           |     |              |         |     |
| ------- | ----------- | --- | ------------ | ------- | --- |
| 10 Aug  | 17 12:45:46 |     | : dune_agent | crashed |     |
...
| Management | module |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
=================
| Index :     | 3                                  |        |                    |      |                  |
| ----------- | ---------------------------------- | ------ | ------------------ | ---- | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |        |                    |      |                  |
| Current     | Boot,                              | up for | 22 hrs 12          | mins | 22 secs          |
| Index :     | 2                                  |        |                    |      |                  |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |        |                    |      |                  |
| 07 Aug      | 18 16:28:01                        |        | : Reboot requested |      | through database |
| Index :     | 1                                  |        |                    |      |                  |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |        |                    |      |                  |
| 07 Aug      | 18 14:08:46                        |        | : Reboot requested |      | through database |
| Index :     | 0                                  |        |                    |      |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |        |                    |      |                  |
| 07 Aug      | 18 13:00:46                        |        | : Reboot requested |      | through database |
| Line module |                                    | 1/1    |                    |      |                  |
=================
| Index : | 3           |     |              |         |     |
| ------- | ----------- | --- | ------------ | ------- | --- |
| 10 Aug  | 17 12:45:46 |     | : dune_agent | crashed |     |
...
| Command        | History     |         |         |              |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- |
| Release        |             |         |         | Modification |     |
| 10.07orearlier |             |         |         | --           |     |
| Command        | Information |         |         |              |     |
| Platforms      |             | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| Firmware      | management |            |              | commands     |                  |
| ------------- | ---------- | ---------- | ------------ | ------------ | ---------------- |
| copy {primary |            | |          | secondary}   | <REMOTE-URL> |                  |
| copy {primary | |          | secondary} | <REMOTE-URL> |              | [vrf <VRF-NAME>] |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 168

Description
UploadsafirmwareimagetoaTFTPorSFTPserver.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
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
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
TFTPupload:
| switch# | copy primary | tftp://192.0.2.0/00_10_00_0002.swi |     |     |     |
| ------- | ------------ | ---------------------------------- | --- | --- | --- |
######################################################################### 100.0%
| Verifying | and writing | system firmware... |     |     |     |
| --------- | ----------- | ------------------ | --- | --- | --- |
SFTPupload:
| switch#            | copy primary  | sftp://swuser@192.0.2.0/00_10_00_0002.swi |              |          |       |
| ------------------ | ------------- | ----------------------------------------- | ------------ | -------- | ----- |
| swuser@192.0.2.0's |               | password:                                 |              |          |       |
| Connected          | to 192.0.2.0. |                                           |              |          |       |
| sftp> put          | primary.swi   | XL_10_00_0002.swi                         |              |          |       |
| Uploading          | primary.swi   | to /users/swuser/00_10_00_0002.swi        |              |          |       |
| primary.swi        |               |                                           | 100% 179MB   | 35.8MB/s | 00:05 |
| Command            | History       |                                           |              |          |       |
| Release            |               |                                           | Modification |          |       |
| 10.07orearlier     |               |                                           | --           |          |       |
| Command            | Information   |                                           |              |          |       |
| Platforms          | Command       | context                                   | Authority    |          |       |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy {primary | | secondary} |                     | <FIRMWARE-FILENAME> |     |     |
| ------------- | ------------ | ------------------- | ------------------- | --- | --- |
| copy {primary | | secondary} | <FIRMWARE-FILENAME> |                     |     |     |
Configurationandfirmwaremanagement |169

Description
CopiesafirmwareimagetoUSBstorage.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{primary | secondary} Selectstheprimaryorsecondaryimagefromwhichtocopythe
firmware.Required
<FIRMWARE-FILENAME> SpecifiesthenameofthefirmwarefiletocreateontheUSB
storagedevice.Prefixthefilenamewithusb:/.Forexample:
usb:/firmware_v1.2.3.swi
Forinformationonhowtoformatthepathtoafirmwarefileona
USBdrive,seeUSBURL.
Examples
| switch#        | copy primary | usb:/11.10.00.0002.swi |              |
| -------------- | ------------ | ---------------------- | ------------ |
| Command        | History      |                        |              |
| Release        |              |                        | Modification |
| 10.07orearlier |              |                        | --           |
| Command        | Information  |                        |              |
| Platforms      | Command      | context                | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 170

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

copy <REMOTE-URL>
copy <REMOTE-URL> {hot-patch|primary|secondary} [vrf <VRF-NAME>]

Description

Downloads a hot-patch or firmware image from a TFTP or SFTP server.

Parameter

<REMOTE-URL>

Description

Specifies the URL from which to download the firmware using
SFTP or TFTP.
TFTP format:

tftp://<IP-ADDR>[:<PORT-NUM>]

[;blocksize=<Value>]/<FILENAME>

SFTP format:

sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>

SCP format:

scp://USER@{IP|HOST}[:PORT]/FILE

{hot-patch|primary|secondary}

Select a hot-patch or a primary or secondary image profile for
receiving the downloaded firmware. Required.

NOTE: For more information about hot-patch, see hot-patch.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

TFTP usage

To specify a URL with:

n an IPv4 address: tftp://192.0.2.1/a.txt

n an IPv6 address: tftp://[2000::2]/a.txt

n a hostname: tftp://hpe.com/a.txt

To specify TFTP with:

n the port number of the server in the URL: tftp://192.0.2.1:12/a.txt

n the blocksize in the URL: tftp://192.0.2.1;blocksize=1462/a.txt

The valid blocksize range is 8 to 65464.

n the port number of the server and blocksize in the URL: tftp://192.0.2.1:12;blocksize=1462/a.txt

To specify a file in a directory of URL: tftp://192.0.2.1/dir/a.txt

SFTP usage

To specify:

Configuration and firmware management | 171

n AURLwithanIPv4address:sftp://user@192.0.2.1/a.txt
n AURLwithanIPv6address:sftp://user@[2000::2]/a.txt
AURLwithahostname:sftp://user@hpe.com/a.txt
n
n SFTPportnumberofaserverintheURL:sftp://user@192.0.2.1:12/a.txt
n AfileinadirectoryofURL:sftp://user@192.0.2.1/dir/a.txt
n TospecifyafilewithabsolutepathintheURL:sftp://user@192.0.2.1//home/user/a.txt
SCP Usage
Tospecify:
n AusernamewithanIP address:scp://user@192.0.2.1:12/a.txt
Ausernamewitharemotehost: scp://user@hpe.com/a.txt
n
Examples
TFTPdownloadforahot-patch:
switch# copy tftp://192.168.1.1/FL.10.12.0001-0002.patch hot-patch vrf vrf1
Fetching /users/swuser/FL.10.10.0001-0002.patch to hotpatch.dnld.uE2YT1
| FL.10.12.0001-0002.patch |             |              | 100% | 62KB | 12.4MB/s | 00:00 |     |
| ------------------------ | ----------- | ------------ | ---- | ---- | -------- | ----- | --- |
| Verifying                | and writing | hot-patch... |      |      |          |       |     |
TFTPdownloadforprimarysoftwareimage:
| switch#     | copy tftp://192.10.12.0/FL_10_12_0001.swi |             |     | primary |     |     |     |
| ----------- | ----------------------------------------- | ----------- | --- | ------- | --- | --- | --- |
| The primary | image will                                | be deleted. |     |         |     |     |     |
| Continue    | (y/n)? y                                  |             |     |         |     |     |     |
######################################################################### 100.0%
| Verifying | and writing | system firmware... |     |     |     |     |     |
| --------- | ----------- | ------------------ | --- | --- | --- | --- | --- |
SFTPdownload:
switch# copy sftp://swuser@192.10.12.0/FL_10_12_0001.swi primary
| The primary | image will | be deleted. |     |     |     |     |     |
| ----------- | ---------- | ----------- | --- | --- | --- | --- | --- |
| Continue    | (y/n)? y   |             |     |     |     |     |     |
The authenticity of host '192.10.12.0 (192.10.12.0)' can't be established.
ECDSA key fingerprint is SHA256:L64khLwlyLgXlARKRMiwcAAK8oRaQ8C0oWP+PkGBXHY.
| Are you | sure you want | to continue connecting | (yes/no)? |     |     |     |     |
| ------- | ------------- | ---------------------- | --------- | --- | --- | --- | --- |
yes
Warning: Permanently added '192.10.12.0' (ECDSA) to the list of known hosts.
| swuser@192.10.12.0's |                 | password: |     |     |     |     |     |
| -------------------- | --------------- | --------- | --- | --- | --- | --- | --- |
| Connected            | to 192.10.12.0. |           |     |     |     |     |     |
Fetching /users/swuser/ss.10.00.0002.swi to ss.10.00.0002.swi.dnld
| /users/swuser/ss.10.00.0002.swi |             |                    |     | 100% | 179MB 25.6MB/s |     | 00:07 |
| ------------------------------- | ----------- | ------------------ | --- | ---- | -------------- | --- | ----- |
| Verifying                       | and writing | system firmware... |     |      |                |     |       |
| Command                         | History     |                    |     |      |                |     |       |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 172

| Release        |             |         | Modification                                    |     |     |     |     |
| -------------- | ----------- | ------- | ----------------------------------------------- | --- | --- | --- | --- |
| 10.12          |             |         | Thehot-patchparameterissupportedonallplatforms. |     |     |     |     |
| 10.07orearlier |             |         | --                                              |     |     |     |     |
| Command        | Information |         |                                                 |     |     |     |     |
| Platforms      | Command     | context | Authority                                       |     |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
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
| Are you | sure you want | to continue | connecting |     | (yes/no)? | yes |     |
| ------- | ------------- | ----------- | ---------- | --- | --------- | --- | --- |
Warning: Permanently added '192.22.1.0' (ECDSA) to the list of known hosts.
| stor@192.22.1.0's      | password:              |        |                           |                           |                |     |       |
| ---------------------- | ---------------------- | ------ | ------------------------- | ------------------------- | -------------- | --- | ----- |
| Connected              | to 192.22.1.0.         |        |                           |                           |                |     |       |
| sftp> get              | c8d5b9f-topflite.swi   |        | c8d5b9f-topflite.swi.dnld |                           |                |     |       |
| Fetching               | /home/dr/im-switch.swi |        | to                        | c8d5b9f-topflite.swi.dnld |                |     |       |
| /home/dr/im-switch.swi |                        |        |                           | 100%                      | 226MB 56.6MB/s |     | 00:04 |
| Verifying              | and writing            | system | firmware...               |                           |                |     |       |
| Command                | History                |        |                           |                           |                |     |       |
| Release                |                        |        | Modification              |                           |                |     |       |
| 10.07orearlier         |                        |        | --                        |                           |                |     |       |
| Command                | Information            |        |                           |                           |                |     |       |
Configurationandfirmwaremanagement |173

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <STORAGE-URL>
| copy <STORAGE-URL> | {hot-patch|primary|secondary} |     |     |
| ------------------ | ----------------------------- | --- | --- |
Description
Copies,verifies,andinstallsahot-patchorfirmwareimagefromaUSBstoragedeviceconnectedtothe
activemanagementmodule.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<STORAGE-URL> Specifiesthenameofthefirmwarefiletocopyfromthestorage
device.Required.
USBformat:
usb:/<FILENAME>
{hot-patch|primary|secondary} Selectahot-patchimageoraprimaryorsecondaryprofilefor
receivingthecopiedfirmware.
NOTE:Formoreinformationabouthot-patch,seehot-patch.
USB usage
Tospecifyafile:
n InaUSBstoragedevice:usb:/a.txt
n InadirectoryofaUSBstoragedevice:usb:/dir/a.txt
Examples
switch#
copy usb:/FL.10.12.0001-0002.patch
| switch#        | copy usb:/FL.10.12.0001.swi |                    | primary                                         |
| -------------- | --------------------------- | ------------------ | ----------------------------------------------- |
| The primary    | image will                  | be deleted.        |                                                 |
| Continue       | (y/n)? y                    |                    |                                                 |
| Verifying      | and writing                 | system firmware... |                                                 |
| Command        | History                     |                    |                                                 |
| Release        |                             |                    | Modification                                    |
| 10.12          |                             |                    | Thehot-patchparameterissupportedonallplatforms. |
| 10.07orearlier |                             |                    | --                                              |
| Command        | Information                 |                    |                                                 |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 174

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy hot-patch
copy hot-patch <Word> {<REMOTE-URL>|<Storage-URL>} [vrf <VRF-NAME>]
Description
Copiesahot-patchfromaswitchtothespecifiedremoteURL orstorageURL.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
Nameofthehot-patchsoftwaretoupload.
<Word>
<REMOTE-URL> SpecifiestheURLtoreceivetheuploadedpatchusingSFTPor
TFTP.ForinformationonhowtoformattheremoteURL,seeURL
formattingforcopycommands.
[Optional]specifytheVRFinstancetouseforupload.
vrf <VRF-NAME>
<STORAGE-URL> SpecifiesthenameofthepatchfiletocreateontheUSBstorage
device.Prefixthefilenamewithusb:/,forexample,
usb:/firmware_FL_10_12_0001-0002.patch.
Examples
switch# copy hot-patch FL_10_12_0001-0002.patch tftp:172.21.18.170/FL_10_12_0001-
| 0002.patch | vrf vrf1 |     |     |
| ---------- | -------- | --- | --- |
Related Commands
| Command |     |     | Description |
| ------- | --- | --- | ----------- |
copy<REMOTE-URL> Downloadsahot-patchimagefromaTFTPorSFTPserver.
Applyahot-patchimageorremoveitfromtheswitch.
hot-patch
| Command History     |     |     |                                        |
| ------------------- | --- | --- | -------------------------------------- |
| Release             |     |     | Modification                           |
| 10.12               |     |     | Hot-patchisnowsupportedonallplatforms. |
| 10.10               |     |     | Commandintroduced                      |
| Command Information |     |     |                                        |
Configurationandfirmwaremanagement |175

| Platforms | Command |     | context | Authority |
| --------- | ------- | --- | ------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
hot-patch
| hot-patch    | apply|remove |              | <name.patch> |     |
| ------------ | ------------ | ------------ | ------------ | --- |
| no hot-patch | apply        | <name.patch> |              |     |
Description
Applyhot-patchsoftwareorremoveitfromtheswitch.Thenoformofthehot-patch applycommand
disablesthehot-patchimage,butdoesnotremoveitfromtheswitch.Rebootingthesystemafter
disablingorremovingthepatchisnotrequired.
| Profile | names |     |     | Description |
| ------- | ----- | --- | --- | ----------- |
apply <name.patch> Applythespecifiedhot-patchimagetoastandaloneswitchorVSF
stack.AOS-CXhot-patchsoftwareimagescanbeobtainedfrom
Arubacustomersupport,andareidentifiedwitha.patch
extension.
| remove | <name.patch> |     |     |     |
| ------ | ------------ | --- | --- | --- |
Disablesthehot-patchimageandremovesthepatchfromthe
switch.Thisremovalwillalsodisablethepatch.Onceremoved,a
hot-patchmustbedownloadedagaininordertobeapplied.
Usage
Ahot-patchcanbedownloadedfromaremoteserverontoaswitchthenappliedwithoutrebootingthe
switch.Whenthehot-patchisdisabled,thehot-patchwillstillremainonthesystem.Thedisabledhot-
patchcanberemovedfromthesystemwithouttheneedforarebootofthesystem.
Ifacheckpointconfigurationthatdoesnotcontainahot-patchisrestoredtoarunningconfiguration
thatdoeshaveahot-patch,thepatchisnotdeleted,itremainsasnotappliedbutispresentinthe
devicememory.
Examples
| switch(config)# |          | hot-patch | apply | FL_10_12_0001-0002.patch |
| --------------- | -------- | --------- | ----- | ------------------------ |
| Related         | Commands |           |       |                          |
| Command         |          |           |       | Description              |
copy<REMOTE-URL> Downloadsandinstallsahot-patchimagefromaTFTPorSFTP
server.
copyhot-patch Copiesahot-patchsoftwareimagefromaswitchtoaspecified
remoteURL orstorageURL.
| Command | History |     |     |     |
| ------- | ------- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 176

| Release   |             |         | Modification                                       |
| --------- | ----------- | ------- | -------------------------------------------------- |
| 10.12     |             |         | Hot-patchisnowsupportedonallplatforms.             |
| 10.10     |             |         | Commandintroduced.                                 |
| Command   | Information |         |                                                    |
| Platforms | Command     | context | Authority                                          |
|           | config      |         | Administratorsorlocalusergroupmemberswithexecution |
Allplatforms
rightsforthiscommand.
show hot-patch
| show hot-patch | [detail] |     |                                                       |
| -------------- | -------- | --- | ----------------------------------------------------- |
| Parameter      |          |     | Description                                           |
| detail         |          |     | Displaysthedetailedstatusofallhot-patchespresentonthe |
system.
Description
theshow hot-patchcommanddisplaysthestatusofallhot-patchespresentonthesystem.Theshow
hot-patch detailcommanddisplaysdetailedinformationforallhotpatchespresentonthesystem.
Examples
| switch#                  | show hot-patch |                            |              |
| ------------------------ | -------------- | -------------------------- | ------------ |
| Name                     |                |                            | Status       |
| -----------------------  |                |                            | -------      |
| FL_10_12_0001-0002.patch |                |                            | Applied      |
| switch#                  | show hot-patch | detail                     |              |
| Name                     |                | : FL_10_12_0001-0002.patch |              |
| Status                   |                | : Applied                  |              |
| Version                  |                | : FL_10_12_0001-0002.patch |              |
| Compatible               | Version        | : FL.10.12.0001            |              |
| Issues Fixed             |                | : CR1234,                  | CR2345       |
| Patch Date               |                | : 2022-03-29               | 20:46:15 UTC |
Patch ID : AOS-CX:FL.10.12.0001-sp1-256-gd457e88d39:20220442009
| Patch SHA |     | : a4038d06a2e5fe7e0d457e868d39e526185b |     |
| --------- | --- | -------------------------------------- | --- |
Related Commands
| Command |     |     | Description |
| ------- | --- | --- | ----------- |
copy<REMOTE-URL> Downloadsahot-patchimagefromaTFTPorSFTPserver.
| hot-patch |         |     | Applyahot-patchimageorremoveitfromtheswitch. |
| --------- | ------- | --- | -------------------------------------------- |
| Command   | History |     |                                              |
Configurationandfirmwaremanagement |177

| Release             |         |         | Modification                         |
| ------------------- | ------- | ------- | ------------------------------------ |
| 10.12               |         |         | Commandsupportedonallplatforms.      |
| 10.10               |         |         | Commandintroducedon6300Switchseries. |
| Command Information |         |         |                                      |
| Platforms           | Command | context | Authority                            |
Administratorsorlocalusergroupmemberswithexecution
| Allplatforms | Manager(#) |     |     |
| ------------ | ---------- | --- | --- |
rightsforthiscommand.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 178

Chapter 9

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

179

n EnablesSNMPontheout-of-bandmanagementinterface(VRFmgmt).
n Setsthecontact,location,anddescriptionfortheswitchto:JaniceM,Building2,LabSwitch.
SetsthecommunitystringtoLab8899X.
n
| switch(config)# |     | snmp-server |     | vrf mgmt           |          |           |
| --------------- | --- | ----------- | --- | ------------------ | -------- | --------- |
| switch(config)# |     | snmp-server |     | system-contact     |          | JaniceM   |
| switch(config)# |     | snmp-server |     | system-location    |          | Building2 |
| switch(config)# |     | snmp-server |     | system-description |          | LabSwitch |
| switch(config)# |     | snmp-server |     | community          | Lab8899X |           |
| Example         | 2   |             |     |                    |          |           |
Thisexamplecreatesthefollowingconfiguration:
n CreatesanSNMPv3usernamedAdminusingshaauthenticationwiththeplaintextpassword
mypasswordandusingdessecuritywiththeplaintextpasswordmyprivpass.
n AssociatestheSNMPv3userAdminwithacontextnamednewContext.
switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
|                 | priv-pass | plaintext |      | myprivpass    |     |            |
| --------------- | --------- | --------- | ---- | ------------- | --- | ---------- |
| switch(config)# |           | snmpv3    | user | Admin context |     | newContext |
RefertotheSNMP GuideforSNMP Commands.
| One | Touch | Provisioning |     |     |     |     |
| --- | ----- | ------------ | --- | --- | --- | --- |
OneTouchProvisioning(OTP)allowsaswitchtobeprovisionedonArubaCentralwiththeminimum
userconfiguration.
| Configuring | One | Touch | Provisioning |     |     |     |
| ----------- | --- | ----- | ------------ | --- | --- | --- |
ToprovisionaswitchtoArubaCentralbyusinganOTPscenario,youcanconfigure:
n TheArubaCentralLocation
Followingconfigurationscanbedoneoptionally:
n TheDomainNameSystem(DNS)serveraddress.
n TheHTTPproxylocation.
| Configuring | Aruba | Central | location |     |     |     |
| ----------- | ----- | ------- | -------- | --- | --- | --- |
1. CreatetheAruba-Centralcontext.
|     | switch(config)# |     | aruba-central |     |     |     |
| --- | --------------- | --- | ------------- | --- | --- | --- |
2. ConfiguretheArubaCentralserverlocation
SNMP|180

switch(config-aruba-central)# location-override <LOCATION> vrf <VRF>
IPv4orIPv6addresscanbeused.
3. ValidatetheconnectivitystatustoArubaCentral
|             | switch# show | aruba-central |     |     |     |
| ----------- | ------------ | ------------- | --- | --- | --- |
| Configuring | DNS server   | address       |     |     |     |
1. ConfiguretheDNSserveraddress.
|     | switch(config)# | ip dns server-address |     | <ADDRESS> | vrf <VRF> |
| --- | --------------- | --------------------- | --- | --------- | --------- |
|     | IPv4orIPv6a     | ddresscanbeused.      |     |           |           |
2. ValidatetheDNSserverstatus
|             | switch# show | ip dns   |     |     |     |
| ----------- | ------------ | -------- | --- | --- | --- |
| Configuring | HTTP proxy   | location |     |     |     |
1. ConfiguretheHTTPProxylocation
|     | switch(config)# | http-proxy | <LOCATION> | vrf <VRF> |     |
| --- | --------------- | ---------- | ---------- | --------- | --- |
LOCATIONcanbeeitheraFQDN,IPv4addressorIPv6address
| Limitations | for Zero | Touch Provisioning |     |     |     |
| ----------- | -------- | ------------------ | --- | --- | --- |
ThefollowingarethelimitationsforOTPwhenprovisioningaswitchbyusingIPv6:
n SupportforobtaningtheArubaCentrallocationviaActivate.
n SupportforobtaningtheArubaCentrallocationviaDHCP.
n SupportforconnectivitytoanArubaCentralon-premiseinstance.
Supportability
Debugloggingcanbeenabledwiththefollowingcommand:
ThecentraldebuglogsarehelpfultodetermineconnectivityissueswithArubaCentral.
| switch# | debug central | all |     |     |     |
| ------- | ------------- | --- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 181

location-override-alternative
location-override-alternative <LOCATION> [vrf <VRF>]
no location-override-alternative <LOCATION> [vrf <VRF>]

Description

Configures information about Aruba connection when the alternative location is used.

The no form of this command removes the location-override-alternative configuration.

Parameter

<LOCATION>

vrf <VRF>

Usage

Description

Specifies the Aruba location.

Specifies the VRF used to connect to Aruba.

When the main and alternative Aruba server locations are specified, the switch attempts to connect to
the main Aruba server. If there is connectivity failure with the main Aruba server location, it attempts to
establish a connection with the alternative server location.

If the alternative location is configured without a main location, the user is prompted for confirmation.
In this case, there is no redundancy and the switch attempts to connect to the alternative location.

Location can take one of the following values:

n A fully qualified domain name (FQDN) along with an optional port number.

n An IPv4 address with an optional port number.

n An IPv6 address with an optional port number.

If the port number is not specified, then port 443 is used by default. If the command is executed without
the VRF parameter, the switch uses

the 'default' VRF.

An Aruba server location can only be a fully qualified domain name (FQDN) or a valid IP address. If the
command is entered without the VRF parameter, the switch uses the default VRF.

Examples

Example of configuring with the aruba-central.com location and VRF red:

switch(config-aruba-central)# location-override-alternative aruba-central.com vrf
red
switch(config-aruba-central)#

Example of a configuration with location only:

switch(config-aruba-central)# location-override-alternative aruba-central.com
switch(config-aruba-central)#

Example of removing the override configuration:

switch(config-aruba-central)# no location-override-alternative
switch(config-aruba-central)# location-override-alternative 10.0.0.1 vrf red

SNMP | 182

switch(config-aruba-central)# location-override-alternative 10.0.0.1:443 vrf red
switch(config-aruba-central)#
location-override-alternative
| 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |                               | vrf red |
| --------------------------------------- | --- | ----------------------------- | ------- |
| switch(config-aruba-central)#           |     | location-override-alternative |         |
[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443 vrf red
| Command History     |         |         |                                     |
| ------------------- | ------- | ------- | ----------------------------------- |
| Release             |         |         | Modification                        |
| 10.13.1000          |         |         | CommandupdatedtoreflectOTPscenario. |
| 10.12.1000          |         |         | Commandintroduced.                  |
| Command Information |         |         |                                     |
| Platforms           | Command | context | Authority                           |
Allplatforms config-aruba-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 183

Chapter 10

DNS

DNS

The Domain Name System (DNS) is the Internet protocol for mapping domain names or hostnames into
addresses. DNS allows users to enter more readily memorable and intuitive hostnames, rather than IP
addresses, to identify devices connected to a network. It also allows a host to keep the same hostname
even if it changes its IP address.

Hostname resolution can be either static or dynamic.

n In static resolution, a local table is defined on the switch that associates hostnames with their IP
addresses. Static tables can be used to speed up the resolution of frequently queried hosts.

n Dynamic resolution requires that the switch query a DNS server located elsewhere on the network.

Dynamic name resolution takes more time than static name resolution, but requires far less
configuration and management.

Configuration

VxLAN IPv4 and IPv6 underlay support the DNS client. To ensure configuration, make sure the following
are set up:

n VxLAN overlay

o Must be configured to establish the VxLAN tunnel.

n VxLAN tunnel

o Ensure the tunnel is established between the VTEPS via either static or EVPN using the following

command: show interface VxLAN VTEPS.

For more information, refer to the AOS-CX VxLAN EVPN Guide.

DNS client

The DNS client resolves hostnames to IP addresses for protocols that are running on the switch. When
the DNS client receives a request to resolve a hostname, it can do so in one of two ways:

n Forward the request to a DNS name server for resolution.

n Reply to the request without using a DNS name server, by resolving the name using a statically

defined table of hostnames and their associated IP addresses.

Configuring the DNS client

Procedure

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

184

1. ConfigureoneormoreDNSnameserverswiththecommandip dns server.
2. ToresolveDNSrequestsbyappendingadomainnametotherequests,eitherconfigureasingle
domainnamewiththecommandip dns domain-name,orconfigurealistofuptosixdomain
| nameswiththecommandip |     | dns domain-list. |     |
| --------------------- | --- | ---------------- | --- |
3. Tousestaticnameresolutionforcertainhosts,associateanIPaddresstoahostwiththe
| commandip | dns host. |     |     |
| --------- | --------- | --- | --- |
4. ReviewyourDNSconfigurationsettingswiththecommandshow ip dns.
Examples
Thisexamplecreatesthefollowingconfiguration:
n Definesthedomainswitch.comtoappendtoallrequests.
n DefinesaDNSserverwithIPv4addressof1.1.1.1.
n DefinesastaticDNShostnamedmyhost1withanIPv4addressof3.3.3.3.
n DNSclienttrafficissentonthedefaultVRF(nameddefault).
| switch(config)#     | ip dns domain-name    |         | switch.com |
| ------------------- | --------------------- | ------- | ---------- |
| switch(config)#     | ip dns server-address |         | 1.1.1.1    |
| switch(config)#     | ip dns host           | myhost1 | 3.3.3.3    |
| switch(config)#     | exit                  |         |            |
| switch# show        | ip dns                |         |            |
| VRF Name : vrf_mgmt |                       |         |            |
Host Name Address
--------------------------------------------------------------------------------
| VRF Name : vrf_default |            |     |     |
| ---------------------- | ---------- | --- | --- |
| Domain Name :          | switch.com |     |     |
| DNS Domain list        | :          |     |     |
| Name Server(s)         | : 1.1.1.1  |     |     |
Host Name Address
--------------------------------------------------------------------------------
myhost1
Thisexamplecreatesthefollowingconfiguration:
n DefinesthreedomainstoappendtoDNSrequestsdomain1.com,domain2.com,domain3.com
withtrafficforwardingonVRFmainvrf.
n DefinesaDNSserverwithanIPv6addressofc::13.
n DefinesaDNShostnamedmyhostwithanIPv4addressof3.3.3.3.
| switch(config)#    | ip dns domain-list    |        | domain1.com vrf mainvrf |
| ------------------ | --------------------- | ------ | ----------------------- |
| switch(config)#    | ip dns domain-list    |        | domain2.com vrf mainvrf |
| switch(config)#    | ip dns domain-list    |        | domain3.com vrf mainvrf |
| switch(config)#    | ip dns server-address |        | c::13                   |
| switch(config)#    | ip dns host           | myhost | 3.3.3.3 vrf mainvrf     |
| switch(config)#    | quit                  |        |                         |
| switch# show       | ip dns mainvrf        |        |                         |
| VRF Name : mainvrf |                       |        |                         |
| Domain Name :      |                       |        |                         |
DNS|185

| DNS  | Domain list | : domain1.com, |     | domain2.com, |     | domain3.com |
| ---- | ----------- | -------------- | --- | ------------ | --- | ----------- |
| Name | Server(s)   | : c::13        |     |              |     |             |
| Host | Name        |                |     |              |     | Address     |
--------------------------------------------------------------------------------
myhost 3.3.3.3
| DNS       | client      | commands      |     |      |             |     |
| --------- | ----------- | ------------- | --- | ---- | ----------- | --- |
| ip dns    | domain-list |               |     |      |             |     |
| ip dns    | domain-list | <DOMAIN-NAME> |     | [vrf | <VRF-NAME>] |     |
| no ip dns | domain-list | <DOMAIN-NAME> |     | [vrf | <VRF-NAME>] |     |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
list <DOMAIN-NAME>
Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     | ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | ------ | ----------- | --- | ----------- | --- |
| switch(config)# |     | ip dns | domain-list |     | domain2.com |     |
Thisexampledefinesalistwithtwoentries,domain2.comanddomain5.com,withrequestsbeingsent
onmainvrf.
| switch(config)# |     | ip dns | domain-list |     | domain2.com | vrf mainvrf |
| --------------- | --- | ------ | ----------- | --- | ----------- | ----------- |
| switch(config)# |     | ip dns | domain-list |     | domain5.com | vrf mainvrf |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |             | no ip dns | domain-list |              | domain1.com |     |
| --------------- | ----------- | --------- | ----------- | ------------ | ----------- | --- |
| Command         | History     |           |             |              |             |     |
| Release         |             |           |             | Modification |             |     |
| 10.07orearlier  |             |           |             | --           |             |     |
| Command         | Information |           |             |              |             |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 186

| Platforms |     | Command |     | context |     | Authority |     |
| --------- | --- | ------- | --- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | domain-name |     |               |     |       |                  |     |
| --------- | ----------- | --- | ------------- | --- | ----- | ---------------- | --- |
| ip dns    | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME>       | ]   |
| no ip dns | domain-name |     | <DOMAIN-NAME> |     |       | [ vrf <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.
Bydefault,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip
dns domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     |     | ip dns | domain-name |     | domain.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |             |         | no ip | dns     | domain-name | domain.com   |     |
| --------------- | ----------- | ------- | ----- | ------- | ----------- | ------------ | --- |
| Command         | History     |         |       |         |             |              |     |
| Release         |             |         |       |         |             | Modification |     |
| 10.07orearlier  |             |         |       |         |             | --           |     |
| Command         | Information |         |       |         |             |              |     |
| Platforms       |             | Command |       | context |             | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | host |             |     |           |       |                  |     |
| --------- | ---- | ----------- | --- | --------- | ----- | ---------------- | --- |
| ip dns    | host | <HOST-NAME> |     | <IP-ADDR> | [ vrf | <VRF-NAME>       | ]   |
| no ip dns | host | <HOST-NAME> |     | <IP-ADDR> |       | [ vrf <VRF-NAME> | ]   |
Description
DNS|187

AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadof
queryingaDNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFis
defined,thedefaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
host <HOST-NAME>
Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
| ThisexampledefinesanIPv4addressof     |             |         |           |      | 3.3.3.3forhost1. |                   |     |       |
| ------------------------------------- | ----------- | ------- | --------- | ---- | ---------------- | ----------------- | --- | ----- |
| switch(config)#                       |             |         | ip dns    | host | host1            | 3.3.3.3           |     |       |
| ThisexampledefinesanIPv6addressofb::5 |             |         |           |      |                  | forhost           | 1.  |       |
| switch(config)#                       |             |         | ip dns    | host | host1            | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |             |         |           |      |                  | host 1withaddress |     | b::5. |
| switch(config)#                       |             |         | no ip dns | host | host1            | b::5              |     |       |
| Command                               | History     |         |           |      |                  |                   |     |       |
| Release                               |             |         |           |      |                  | Modification      |     |       |
| 10.07orearlier                        |             |         |           |      |                  | --                |     |       |
| Command                               | Information |         |           |      |                  |                   |     |       |
| Platforms                             |             | Command | context   |      |                  | Authority         |     |       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | server         | address |           |     |       |            |     |     |
| --------- | -------------- | ------- | --------- | --- | ----- | ---------- | --- | --- |
| ip dns    | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
| no ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
Description
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 188

ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
Thisexampledefinesanameserverat1.1.1.1.
| switch(config)# | ip  | dns server-address |     | 1.1.1.1 |
| --------------- | --- | ------------------ | --- | ------- |
Thisexampledefinesanameserverata::1.
| switch(config)# | ip  | dns server-address |     | a::1 |
| --------------- | --- | ------------------ | --- | ---- |
Thisexampleremovesanameserverata::1.
| switch(config)#     | no      | ip dns server-address |              | a::1 |
| ------------------- | ------- | --------------------- | ------------ | ---- |
| Command History     |         |                       |              |      |
| Release             |         |                       | Modification |      |
| 10.07orearlier      |         |                       | --           |      |
| Command Information |         |                       |              |      |
| Platforms           | Command | context               | Authority    |      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip dns |                            |     |     |     |
| ----------- | -------------------------- | --- | --- | --- |
| show ip dns | [vrf <VRF-NAME>][vsx-peer] |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
DNS|189

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow ip dns
command.
| switch(config)# |     | ip dns | domain-name    |       | domain.com    |     |         |
| --------------- | --- | ------ | -------------- | ----- | ------------- | --- | ------- |
| switch(config)# |     | ip dns | domain-list    |       | domain5.com   |     |         |
| switch(config)# |     | ip dns | domain-list    |       | domain8.com   |     |         |
| switch(config)# |     | ip dns | server-address |       | 4.4.4.4       |     |         |
| switch(config)# |     | ip dns | server-address |       | 6.6.6.6       |     |         |
| switch(config)# |     | ip dns | host           | host3 | 5.5.5.5       |     |         |
| switch(config)# |     | ip dns | host           | host2 | 2.2.2.2       |     |         |
| switch(config)# |     | ip dns | host           | host3 | c::12         |     |         |
| switch(config)# |     | ip dns | domain-name    |       | reddomain.com |     | vrf red |
switch(config)#
|                 |           | ip dns         | domain-list    |             | reddomain5.com |     | vrf red |
| --------------- | --------- | -------------- | -------------- | ----------- | -------------- | --- | ------- |
| switch(config)# |           | ip dns         | domain-list    |             | reddomain8.com |     | vrf red |
| switch(config)# |           | ip dns         | server-address |             | 4.4.4.5        |     | vrf red |
| switch(config)# |           | ip dns         | server-address |             | 6.6.6.7        |     | vrf red |
| switch(config)# |           | ip dns         | host           | host3       | 5.5.5.6        | vrf | red     |
| switch(config)# |           | ip dns         | host           | host2       | 2.2.2.3        | vrf | red     |
| switch(config)# |           | ip dns         | host           | host3       | c::13          | vrf | red     |
| switch#         | show      | ip dns         |                |             |                |     |         |
| VRF Name        | : default |                |                |             |                |     |         |
| Domain Name     | :         | domain.com     |                |             |                |     |         |
| DNS Domain      | list      | : domain5.com, |                | domain8.com |                |     |         |
| Name Server(s)  |           | : 4.4.4.4,     | 6.6.6.6        |             |                |     |         |
| Host Name       |           | Address        |                |             |                |     |         |
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
| host2           |     | 2.2.2.3 |             |     |             |     |         |
| --------------- | --- | ------- | ----------- | --- | ----------- | --- | ------- |
| host3           |     | 5.5.5.6 |             |     |             |     |         |
| host3           |     | c::13   |             |     |             |     |         |
| switch(config)# |     | ip dns  | domain-name |     | domain.com  |     | vrf red |
| switch(config)# |     | ip dns  | domain-list |     | domain5.com |     | vrf red |
switch(config)#
|                 |     | ip dns    | domain-list    |       | domain8.com |     | vrf red |
| --------------- | --- | --------- | -------------- | ----- | ----------- | --- | ------- |
| switch(config)# |     | ip dns    | server-address |       | 4.4.4.4     |     | vrf red |
| switch(config)# |     | ip dns    | server-address |       | 6.6.6.6     |     | vrf red |
| switch(config)# |     | ip dns    | host           | host3 | 5.5.5.5     | vrf | red     |
| switch(config)# |     | no ip dns | host           | host2 | 2.2.2.2     |     | vrf red |
| switch(config)# |     | ip dns    | host           | host3 | c::12       | vrf | red     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 190

switch#
|                | show ip dns         | vrf red |             |
| -------------- | ------------------- | ------- | ----------- |
| VRF Name       | : red               |         |             |
| Domain Name    | : domain.com        |         |             |
| DNS Domain     | list : domain5.com, |         | domain8.com |
| Name Server(s) | : 4.4.4.4,          | 6.6.6.6 |             |
| Host Name      | Address             |         |             |
-------------------------------
| host3 | 5.5.5.5 |     |     |
| ----- | ------- | --- | --- |
| host3 | c::12   |     |     |
DNSclientarbitrationontheMGMTinterfaceonaMGMTVRFcanbeupdatedviathreedifferentmethods.
1. Usingthedomain-name<name>ornameservers<servers>commandsinthecommand-lineinterface.
2. Usingthe ipdnsdomain-name<DOMAIN-NAME>vrfMGMToripdnsserver-address<SERVER>vrf
MGMTcommandsinthecommand-lineinterface.
3. Usingtheipdhcpcommandinthecommand-lineinterface(dynamicenties).
AOS-CXgivesthefollowingprioritylevelstothethesethreeupdatemothods.
n Priority1-standaloneCLIconfiguration
n Priority2-staticipdnsconfiguration
n Priority3-Dynamicconfig
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|191

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

192

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

Device discovery and configuration | 193

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

n Port VLAN Name: Access or native VLAN name. Enabled by default.

n Port MFS: Maximum Frame Size. Enabled by default.

LLDP MED support

LLDP-MED interoperates with directly connected IP telephony (endpoint) clients and provides the
following features:

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

194

n Advertisement of the voice VLAN configured on the interface which is used by connected IP

telephony (endpoint) clients.

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

Device discovery and configuration | 195

5. Bydefault,supportfortheLLDP-MEDTLVisenabled.Tocustomizesettings,usethecommands
| lldp medandlldp |     | med-location. |     |
| --------------- | --- | ------------- | --- |
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
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| clear lldp statistics |     |     |     |
| --------------------- | --- | --- | --- |
| clear lldp statistics |     |     |     |
Description
ClearsallLLDPneighborstatistics.
Examples
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 196

ClearingallLLDPneighborstatistics:
| switch# clear       | lldp    | statistics |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
Devicediscoveryandconfiguration|197

lldp dot3
| lldp dot3 {poe | | macphy} |         |     |
| -------------- | --------- | ------- | --- |
| no lldp dot3   | {poe |    | macphy} |     |
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
| lldp dot3 mfs |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 mfs |     |     |     |
| no lldp dot3  | mfs |     |     |
Description
Enablesthe802.3TLVlistinLLDP toadvertiseformaximumframesize(MFS).Enabledbydefault.
ThenoformofthiscommanddisablestheadvertisementofmaximumframesizeTLVs.
Examples
EnablingadvertisementofmaximumframesizeTLVs:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 198

switch(config)#
|                    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | lldp      | dot3  | mfs |
DisablingadvertisementofmaximumframesizeTLVs:
| switch(config)#     |         | interface | 1/1/1 |                   |
| ------------------- | ------- | --------- | ----- | ----------------- |
| switch(config-if)#  |         | no lldp   | dot3  | mfs               |
| Command History     |         |           |       |                   |
| Release             |         |           |       | Modification      |
| 10.11               |         |           |       | Commandintroduced |
| Command Information |         |           |       |                   |
| Platforms           | Command | context   |       | Authority         |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp holdtime-multiplier
| lldp holdtime-multiplier |     | <multiplier> |     |     |
| ------------------------ | --- | ------------ | --- | --- |
no lldp holdtime-multiplier
Description
SetstheholdtimeTTLmultipliervaluethatisusedtocalculatetheLLDPTime-to-Livevalue.Time-to-Live
definesthelengthoftimethatneighborsconsiderLLDPinformationsentbythisagentasvalid.When
Time-to-Liveexpires,theinformationisdeletedbytheneighbor.Time-to-liveiscalculatedbymultiplying
| holdtimebythevalueoflldp |     | timer. |     |     |
| ------------------------ | --- | ------ | --- | --- |
ThenoformofthiscommandsetstheholdtimeTTLmultipliertoitsdefaultvalueof4.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<multiplier> SpecifiestheTTLmultiplierintherangeof2to10.Default:4.
Formula
TTL=Holdtime-multiplierxlldptimer
where:
TTL=Time-to-Live
Holdtime-multiplier=Multiplyingholdtimevalue
lldptimer=Messagetransmissioninterval
Examples
Devicediscoveryandconfiguration|199

Settingtheholdtimeto8timesofthevalueoflldptimer:
| switch(config)# | lldp | holdtime-multiplier |     | 8   |
| --------------- | ---- | ------------------- | --- | --- |
Settingtheholdtimetothedefaultvalueof4timesofthevalueoflldptimer:
| switch(config)#     | no      | lldp holdtime-multiplier |              |     |
| ------------------- | ------- | ------------------------ | ------------ | --- |
| Command History     |         |                          |              |     |
| Release             |         |                          | Modification |     |
| 10.07orearlier      |         |                          | --           |     |
| Command Information |         |                          |              |     |
| Platforms           | Command | context                  | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp management-address    |     | vlan           |     |     |
| -------------------------- | --- | -------------- | --- | --- |
| lldp management-address    |     | vlan <VLAN-ID> |     |     |
| no lldp management-address |     | vlan <VLAN-ID> |     |     |
Description
SetstheVLANwhoseIPv4orIPv6addressisadvertisedastheLLDPmanagementauthority.
ThenoformofthiscommandremovestheVLANwhoseIPv4orIPv6addressisadvertisedastheLLDP
managementauthority.
ThefollowingistheprecedenceforthemanagementIPaddressTLVintheLLDPpacket(inorder):
n LLDPmanagement-IP-addressandmanagement-ipv6-address,ifconfigured.
n LLDPmanagementVLAN'sIPv4andIPv6address,ifconfigured.
n LoopbackIPaddressfromthesmallestconfiguredloopbackinterfaceidentifier.
n Route-only-portIP address(Layer-3interface)orIPaddressoftheSVI(Layer-2interface).
OOBMIPaddress.
n
n BaseMACaddressoftheswitch.
| Parameter |     |     | Description                     |     |
| --------- | --- | --- | ------------------------------- | --- |
| <VLAN-ID> |     |     | SpecifiestheVLANID.Range1-4094. |     |
Examples
SettingthemanagementauthorityforVLAN10:
| switch(config)# | lldp | management-address |     | vlan 10 |
| --------------- | ---- | ------------------ | --- | ------- |
RemovingthemanagementauthorityforVLAN10:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 200

| switch(config)#     | no      | lldp management-address | vlan 10            |
| ------------------- | ------- | ----------------------- | ------------------ |
| Command History     |         |                         |                    |
| Release             |         |                         | Modification       |
| 10.12               |         |                         | Commandintroduced. |
| Command Information |         |                         |                    |
| Platforms           | Command | context                 | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp management-ip-address
| lldp management-ip-address |     | <IPV-ADDR> |     |
| -------------------------- | --- | ---------- | --- |
no lldp management-ip-address
Description
DefinestheIPmanagementaddressoftheswitchwhichissentinthemanagementaddressTLV.One
IPv4andoneIPv6managementaddresscanbeconfigured.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
n IPaddressoftheport
n IPaddressofthemanagementinterface
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv4managementaddressoftheswitch.
| Parameter   |     |     | Description                                      |
| ----------- | --- | --- | ------------------------------------------------ |
| <IPV4-ADDR> |     |     | SpecifiesthemanagementaddressoftheswitchasanIPv4 |
format(x.x.x.x),wherexisadecimalvaluefrom0to255.
Examples
Settingthemanagementaddressto10.10.10.2:
| switch(config)# | lldp | management-ip-address | 10.10.10.2 |
| --------------- | ---- | --------------------- | ---------- |
Removingthemanagementaddress:
| switch(config)# | no  | lldp management-ip-address |     |
| --------------- | --- | -------------------------- | --- |
| Command History |     |                            |     |
Devicediscoveryandconfiguration|201

| Release |     |     | Modification                                     |
| ------- | --- | --- | ------------------------------------------------ |
| 10.14   |     |     | Themanagement-ipv4-addresskeywordisdeprecatedand |
replacedwithmanagement-ip-address.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp management-ipv6-address
| lldp management-ipv6-address |     | <IPV6-ADDR> |     |
| ---------------------------- | --- | ----------- | --- |
no lldp management-ipv6-address
Description
DefinestheIPv6managementaddressoftheswitch.Themanagementaddressisencapsulatedinthe
managementaddressTLV.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
IPaddressoftheport
n
n IPaddressofthemanagementinterface
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv6managementaddressoftheswitch.
| Parameter   |     |     | Description                      |
| ----------- | --- | --- | -------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiesanIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
Settingthemanagementaddressto2001:db8:85a3::8a2e:370:7334:
switch(config)# lldp management-ipv6-address 2001:0db8:85a3::8a2e:0370:7334
Removingthemanagementaddress:
| switch(config)# | no  | lldp management-ipv6-address |              |
| --------------- | --- | ---------------------------- | ------------ |
| Command History |     |                              |              |
| Release         |     |                              | Modification |
| 10.07orearlier  |     |                              | --           |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 202

| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp med
lldp med [poe [priority-override] | capability | network-policy]
| no med [poe | [priority-override] |     | | capability | | network-policy] |
| ----------- | ------------------- | --- | ------------ | ----------------- |
Description
ConfiguressupportfortheLLDP-MEDTLV.LLDP-MED(mediaendpointdevices)isanextensiontoLLDP
developedbyTIAtosupportinteroperabilitybetweenVoIPendpointdevicesandothernetworkingend-
devices.TheswitchonlysendstheLLDPMEDTLVafterreceivingaMEDTLVfromandconnected
endpointdevice.
NotsupportedontheOOBMinterface.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
poe [priority-override] SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
dot3poeandlldpmedpoeareenabled,thelldpdot3poe3
settingtakesprecedence.Default:enabled.
| capability |     |     | SpecifiesadvertisementofsupportedLLDPMEDTLVs.The |     |
| ---------- | --- | --- | ------------------------------------------------ | --- |
capabilityTLVisalwayssentwithotherMEDTLVs,thereforeit
cannotbedisabledwhenotherMEDTLVsareenabled.Default:
enabled.
network-policy
Networkpolicydiscoveryletsendpointsandnetworkdevices
advertisetheirVLANIDs,andIEEE802.1p(PCPandDSCP)values
forvoiceapplications.ThisTLVisonlysentwhenavoiceVLAN
policyispresent.Default:enabled.
Examples
EnablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |     | lldp med | network-policy |     |
| ------------------ | --- | -------- | -------------- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |         | no lldp | med network-policy |     |
| ------------------ | ------- | ------- | ------------------ | --- |
| Command            | History |         |                    |     |
| Release            |         |         | Modification       |     |
| 10.07orearlier     |         |         | --                 |     |
Devicediscoveryandconfiguration|203

Command Information

Platforms

Command context

Authority

All platforms

config-if

Administrators or local user group members with execution
rights for this command.

lldp med location

lldp med location {civic-addr
no med location {civic-addr elin-addr }

elin-addr }

Description

Configures support for the LLDP-MED TLV. Supports only civic address and emergency location
information number (ELIN). Coordinate-based location is not supported.

The no form of this command disables support for the LLDP MED TLV.

Parameter

civic-addr

elin-addr

Description

Configures the LLDP MED civic location TLV.

Configures support for the LLDP MED emergency location
TLV. This feature is intended for use in ECS applications to support
class 3 LLDP-MED VoIP telephones connected to a switch in an
MLTS infrastructure. An ELIN is a valid NANP format telephone
number assigned to MLTS operators in North America by the
appropriate authority. The ELIN is used to route emergency (E911)
calls to a PSAP.
(Range: 1-15 numeric characters)

The lldp med location civic-addr command requires a minimum of one type/value pair, but typically
includes multiple type/value pairs as needed to configure a complete set of data describing a given
location.

n CA-TYPE: This is the first entry in a type/value pair and is a number defining the type of data
contained in the second entry in the type/value pair (CA-VALUE.) Some examples of CA-TYPE
specifiers include: 3=city 6=street (name) 25=building name (Range: 0 - 255)

n CA-VALUE: This is the second entry in a type/value pair and is an alphanumeric string containing the

location information corresponding to the immediately preceding CA-TYPE entry. Strings are
delimited by either blank spaces, single quotes (' … '), or double quotes ("… ".) Each string should
represent a specific data type in a set of unique type/value pairs comprising the description of a
location, and each string must be preceded by a CA-TYPE number identifying the type of data in the
string.

The following LLDP-MED TLV values are supported. For details on these value types, refer to RFC 4776

n 1: national subdivisions (state, canton, region, province, prefecture)

n 2: county, parish, gun (JP), district (IN)

n 3: city, township, shi (JP)

n 4: city division, borough, city district, ward, chou (JP)

n 5: neighborhood, block

n 6: group of streets below the neighborhood level

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

204

n 16: leading street direction N

n 17: trailing street suffix SW

n 18: street suffix or type

n 19: house number

n 20: house number suffix

n 21: landmark or vanity

n 22: location

n 23: name

n 24: postal/zip code

n 25: building (structure)

n 26: unit (apartment, suite)

n 27: floor

n 28: room

n 29: type of place

n 30: postal community name

n 31: post office box

n 32: additional code 13203000003

n 33: seat (desk, cubicle workstation)

n 34: primary road name 35 road section

n 36: branch road name

n 37: sub-branch road name

n 38: street name pre-modifier

n 39: street name post-modifier

Examples

Enabling support for the LLDP MED emergency location TLV:

switch(config-if)# lldp med location elin-addr 408-555-1212

Disabling support for the LLDP MED emergency location TLV:

switch(config-if)# no lldp med location elin-addr 408-555-1212

Enabling support for the LLDP MED civic address TLV:

switch(config-if)# lldp med location civic-addr US 1 19 123 6 Fake 18 Street

Disabling support for the LLDP MED civic address TLV:

switch(config-if)# no lldp med location civic-addr US 1 19 123 6 Fake 18 Street

Command History

Device discovery and configuration | 205

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
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
| switch(config)#     | interface | mgmt            |              |
| ------------------- | --------- | --------------- | ------------ |
| switch(config-if)#  |           | no lldp receive |              |
| Command History     |           |                 |              |
| Release             |           |                 | Modification |
| 10.07orearlier      |           |                 | --           |
| Command Information |           |                 |              |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 206

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp reinit
| lldp reinit | <TIME> |     |     |
| ----------- | ------ | --- | --- |
no lldp reinit
Description
Setstheamountoftime(inseconds)towaitbeforeperformingLLDPinitializationonaninterface.
Thenoformofthiscommandsetsthereinitializationtimetoitsdefaultvalueof2seconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<TIME>
Specifiesthereinitializationtimeinseconds.Range:1to10.
Default:2seconds.
Examples
Settingthereinitializationtimeto5seconds:
| switch(config)# | lldp | reinit 5 |     |
| --------------- | ---- | -------- | --- |
Settingthereinitializationtimetothedefaultvalueof2seconds:
| switch(config)#     | no      | lldp reinit |              |
| ------------------- | ------- | ----------- | ------------ |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp select-tlv
| lldp select-tlv    | <TLV-NAME> |     |     |
| ------------------ | ---------- | --- | --- |
| no lldp select-tlv | <TLV-NAME> |     |     |
Description
SelectsaTLVthattheLLDPagentwillsendandreceive.Bydefault,allsupportedTLVsaresentand
received.
ThenoformofthiscommandstopstheLLDPagentfromsendingandreceivingaspecificTLV.
Devicediscoveryandconfiguration|207

LLDP supports Organization Unique Identifiers (OUIs) with the following Organization-specific TLVs:

n IEEE 802.1 (DOT1) (oui:0x00, 0x80, 0xc2)

n IEEE 802.3 (DOT3) (oui:0x00, 0x12, 0x0f)

n Aruba, a Hewlett Packard Enterprise Company (oui:0x88, 0x3a, 0x30)

Parameter

Description

select-tlv <TLV-NAME>

Specifies the TLV name to send. The following TLV names are
supported:

n management-address: Selection is based on priority
in the following list (for example if first TLV name isn't
selected, the next will be, progressing through this list
until a selection is made):

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

n port-description: Select port-description TLV.

n port-vlan-id: Select port-vlan-id TLV.

n port-vlan-name: Select port-vlan-name TLV.

n system-capabilities: Select system-capabilities TLV.

n system-description: Select system-description TLV.

n system-name: Select system-name TLV.

Examples

Stopping the LLDP agent from sending the port-description TLV:

switch(config)# no lldp select-tlv port-description

Enabling the LLDP agent to send the port-description TLV:

switch(config)# lldp select-tlv oui

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

208

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

lldp timer

lldp timer <TIME>
no lldp timer

Description

Sets the interval (in seconds) at which local LLDP information is updated and TLVs are sent to
neighboring network devices by the LLDP agent. The minimum setting for this timer must be four times
the value of lldp txdelay.

For example, this is a valid configuration:

n lldp timer = 16

n lldp txdelay = 4

And, this is an invalid configuration:

n lldp timer = 5

n lldp txdelay = 2

When copying a saved configuration to the running configuration, the value for lldp timer is applied before the

value of lldp txdelay. This can result in a configuration error if the saved configuration has a value of lldp timer

that is not four times the value of lldp txdelay in the running configuration.

For example, if the saved configuration has the settings:

n lldp timer = 16

n lldp txdelay = 4

And the running configuration has the settings:

n lldp timer = 30

n lldp txdelay = 7

Then you will see an error indicating that certain configuration settings could not be applied, and you will have to

manually adjust the value of lldp txdelay in the running configuration.

The no form of this command sets the update interval to its default value of 30 seconds.

Parameter

<TIME>

Examples

Setting the update interval to 7 seconds:

Description

Specifies the update interval (in seconds). Range: 5 to 32768.
Default: 30.

Device discovery and configuration | 209

| switch(config)# | lldp | timer 7 |     |
| --------------- | ---- | ------- | --- |
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
lldp tlv-enable
lldp tlv-enable basic-tlv management-address-tlv {ip <X.X.X.X>}|{ipv6 <X:X::X:X>}
| no lldp select-tlv | <TLV-NAME> |     |     |
| ------------------ | ---------- | --- | --- |
Description
ATLVisaninformationelementthatcontainsthetype,length,andvaluefields.Thiscommand
configurestheIPv4/IPv6addresstobeadvertisedinthemanagementaddressTLV.Thisconfigured
valuewilltakethehighestprecedenceintheselectionlogictheswitchusestoidentifytheIPaddressto
beadvertisedinthemanagementaddressTLV.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
ip <X.X.X.X>
SpecifyanIPaddressinIPv4format(X.X.X.X),whereXisa
decimalnumberfrom0to255.
ipv6 <X:X::X:X> SpecifyanIPaddressinIPv6format(X:X::X:X),whereXisa
hexadecimalnumberfrom0toF.
Examples
ConfiguringanIPaddressinIPv4format:
| switch(config)# | interface | 1/3/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)# lldp tlv-enable basic-tlv management-address-tlv ip 10.0.0.1
ConfiguringanIPaddressinIPv6format:
| switch(config)# | interface | 1/3/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)# lldp tlv-enable basic-tlv management-address-tlv ipv6
2001:db8:85a3::8a2e:370:7334
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 210

| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.14.1000          |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp transmit
lldp transmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionis
enabledonallactiveinterfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablestransmissionofLLDPinformationonaninterface.
Examples
EnablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1         |     |
| ------------------ | --------- | ------------- | --- |
| switch(config-if)# |           | lldp transmit |     |
DisablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1            |     |
| ------------------ | --------- | ---------------- | --- |
| switch(config-if)# |           | no lldp transmit |     |
EnablingLLDPtransmissionontheOOBMinterface:
| switch(config)#    | interface | mgmt          |     |
| ------------------ | --------- | ------------- | --- |
| switch(config-if)# |           | lldp transmit |     |
DisablingLLDPtransmissionontheOOBMinterface:
| switch(config)#    | interface | mgmt             |              |
| ------------------ | --------- | ---------------- | ------------ |
| switch(config-if)# |           | no lldp transmit |              |
| Command History    |           |                  |              |
| Release            |           |                  | Modification |
| 10.07orearlier     |           |                  | --           |
Devicediscoveryandconfiguration|211

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp txdelay
| lldp txdelay | <TIME> |     |     |
| ------------ | ------ | --- | --- |
no lldp txdelay
Description
Setstheamountoftime(inseconds)towaitbeforesendingLLDPinformationfromanyinterface.The
maximumvaluefortxdelayis25%ofthevalueoflldp tx timer.
Thenoformofthiscommandsetsthedelaytimetoitsdefaultvalueof2seconds.
| Parameter |     |     | Description                                           |
| --------- | --- | --- | ----------------------------------------------------- |
| <TIME>    |     |     | Specifiesthedelaytimeinseconds.Range:0to10.Default:2. |
Examples
Settingthedelaytimeto8seconds:
| switch(config)# | lldp | txdelay 8 |     |
| --------------- | ---- | --------- | --- |
Settingthedelaytimetothedefaultvalueof2seconds:
| switch(config)#     | no      | lldp txdelay |              |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp trap enable |        |     |     |
| ---------------- | ------ | --- | --- |
| lldp trap enable |        |     |     |
| no lldp trap     | enable |     |     |
Description
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 212

EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenot
requiredtobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | lldp trap | enable |     |     |
| --------------- | --- | --------- | ------ | --- | --- |
EnablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | lldp | trap | enable |     |
| ------------------ | --- | ---- | ---- | ------ | --- |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp | trap | enable |     |
| --------------- | --- | ------- | ---- | ------ | --- |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | no lldp | trap | enable |     |
| ------------------ | --- | ------- | ---- | ------ | --- |
DisplayingLLDPglobalconfiguration:
| switch#     | show | lldp configuration |     |     |     |
| ----------- | ---- | ------------------ | --- | --- | --- |
| LLDP Global |      | Configuration      |     |     |     |
=========================
| LLDP Enabled  |         |                |     | : No |     |
| ------------- | ------- | -------------- | --- | ---- | --- |
| LLDP Transmit |         | Interval       |     | : 30 |     |
| LLDP Hold     | Time    | Multiplier     |     | : 4  |     |
| LLDP Transmit |         | Delay Interval |     | : 2  |     |
| LLDP Reinit   |         | Timer Interval |     | : 2  |     |
| LLDP Trap     | Enabled |                |     | : No |     |
TLVs Advertised
===============
| Management | Address |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
Port Description
Port VLAN-ID
System Description
System Name
| LLDP Port | Configuration |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- |
=======================
| PORT |     | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | ---------- | ----------------- |
Devicediscoveryandconfiguration|213

--------------------------------------------------------------------------
| 1/1/1 |     |     | Yes |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     |     | Yes |     | Yes | Yes |
| 1/1/3 |     |     | Yes |     | Yes | Yes |
| 1/1/4 |     |     | Yes |     | Yes | Yes |
| 1/1/5 |     |     | Yes |     | Yes | Yes |
| 1/1/6 |     |     | Yes |     | Yes | Yes |
...........
...........
| mgmt |     |     | Yes |     | Yes | Yes |
| ---- | --- | --- | --- | --- | --- | --- |
DisplayingLLDPConfigurationfortheinterface:
| switch# | show   | lldp          | configuration |     | 1/1/1 |     |
| ------- | ------ | ------------- | ------------- | --- | ----- | --- |
| LLDP    | Global | Configuration |               |     |       |     |
=========================
| LLDP | Enabled  |               |            | : Yes |     |     |
| ---- | -------- | ------------- | ---------- | ----- | --- | --- |
| LLDP | Transmit | Interval      |            | : 30  |     |     |
| LLDP | Hold     | Time          | Multiplier | : 4   |     |     |
| LLDP | Transmit | Delay         | Interval   | : 2   |     |     |
| LLDP | Reinit   | Timer         | Interval   | : 2   |     |     |
| LLDP | Trap     | Enabled       |            | : No  |     |     |
| LLDP | Port     | Configuration |            |       |     |     |
=======================
| PORT |     |     | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | --- | ---------- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 |     |     | Yes |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- | --- |
DisplayingLLDPConfigurationforthemanagementinterface:
switch#
|      | show   | lldp          | configuration |     | mgmt |     |
| ---- | ------ | ------------- | ------------- | --- | ---- | --- |
| LLDP | Global | Configuration |               |     |      |     |
=========================
| LLDP | Enabled  |               |            | : Yes |     |     |
| ---- | -------- | ------------- | ---------- | ----- | --- | --- |
| LLDP | Transmit | Interval      |            | : 30  |     |     |
| LLDP | Hold     | Time          | Multiplier | : 4   |     |     |
| LLDP | Transmit | Delay         | Interval   | : 2   |     |     |
| LLDP | Reinit   | Timer         | Interval   | : 2   |     |     |
| LLDP | Trap     | Enabled       |            | : Yes |     |     |
| LLDP | Port     | Configuration |            |       |     |     |
=======================
| PORT |     |     | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | --- | ---------- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt           |             |     | Yes |     | Yes          | Yes |
| -------------- | ----------- | --- | --- | --- | ------------ | --- |
| Command        | History     |     |     |     |              |     |
| Release        |             |     |     |     | Modification |     |
| 10.07orearlier |             |     |     |     | --           |     |
| Command        | Information |     |     |     |              |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 214

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
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
| Management |             | Address       |     |     |     |     |
| ---------- | ----------- | ------------- | --- | --- | --- | --- |
| Port       | Description |               |     |     |     |     |
| Port       | VLAN-ID     |               |     |     |     |     |
| System     | Description |               |     |     |     |     |
| System     | Name        |               |     |     |     |     |
| LLDP       | Port        | Configuration |     |     |     |     |
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
Devicediscoveryandconfiguration|215

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
| Auto       | Flush | On Link      | Down | :   | Yes         |                   |
| ---------- | ----- | ------------ | ---- | --- | ----------- | ----------------- |
| Management |       | IPv4 Address |      | :   | 10.1.1.1    |                   |
| Management |       | IPv6 Address |      | :   | 3001:1::1:1 |                   |
| PORT       |       | TX-ENABLED   |      |     | RX-ENABLED  | INTF-TRAP-ENABLED |
--------------------------------------------------------------------------
| 1/1/1   |         | Yes |     |     | Yes          | Yes |
| ------- | ------- | --- | --- | --- | ------------ | --- |
| Command | History |     |     |     |              |     |
| Release |         |     |     |     | Modification |     |
10.14.1000 WhendisplayingtheLLDP configurationforaspecificinterface,
theoutputofthiscommanddisplaysanyconfiguredmanagement
IPaddresses.
| 10.07orearlier |             |         |         |     | --        |     |
| -------------- | ----------- | ------- | ------- | --- | --------- | --- |
| Command        | Information |         |         |     |           |     |
| Platforms      |             | Command | context |     | Authority |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | configuration |     | mgmt |     |     |     |
| --------- | ------------- | --- | ---- | --- | --- | --- |
| show lldp | configuration |     | mgmt |     |     |     |
Description
ShowsLLDPconfigurationsettingsfortheOOBMinterface.
Example
Showingconfigurationsettingsforallinterfaces:
| switch# |        | show lldp     | configuration |     | mgmt |     |
| ------- | ------ | ------------- | ------------- | --- | ---- | --- |
| LLDP    | Global | Configuration |               |     |      |     |
=========================
| LLDP | Enabled  |          |     | :   | Yes |     |
| ---- | -------- | -------- | --- | --- | --- | --- |
| LLDP | Transmit | Interval |     | :   | 30  |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 216

| LLDP Hold     | Time Multiplier |          | : 4   |     |     |
| ------------- | --------------- | -------- | ----- | --- | --- |
| LLDP Transmit | Delay           | Interval | : 2   |     |     |
| LLDP Reinit   | Timer Interval  |          | : 2   |     |     |
| LLDP Trap     | Enabled         |          | : Yes |     |     |
| LLDP Port     | Configuration   |          |       |     |     |
=======================
| PORT | TX-ENABLED |     | RX-ENABLED |     | INTF-TRAP-ENABLED |
| ---- | ---------- | --- | ---------- | --- | ----------------- |
--------------------------------------------------------------------------
| mgmt           | Yes         |         | Yes          |     | Yes |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Command        | History     |         |              |     |     |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | local-device           |     |     |     |     |
| --------- | ---------------------- | --- | --- | --- | --- |
| show lldp | local-device[vsx-peer] |     |     |     |     |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsare
configuredonanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDson
accessinterfaces.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingglobalLLDPinformationonly(allportsincludingOOBMportareadministrativelydown):
| switch# | show lldp local-device |     |     |     |     |
| ------- | ---------------------- | --- | --- | --- | --- |
| Global  | Data                   |     |     |     |     |
===========
| Chassis-ID |             | : 1c:98:ec:e3:45:00 |                  |               |     |
| ---------- | ----------- | ------------------- | ---------------- | ------------- | --- |
| System     | Name        | : switch            |                  |               |     |
| System     | Description | : HPE               | ANW JL375A 8400X | XL.01.01.0001 |     |
| Management | Address     | : 192.168.10.1      |                  |               |     |
Devicediscoveryandconfiguration|217

| Capabilities | Available |     | : Bridge, | Router |
| ------------ | --------- | --- | --------- | ------ |
| Capabilities | Enabled   |     | : Bridge, | Router |
| TTL          |           |     | : 120     |        |
Showingallportsexcept1/1/11andOOBMasadministrativelydown:
| switch# | show lldp | local-device |     |     |
| ------- | --------- | ------------ | --- | --- |
Global Data
===========
| Chassis-ID   |             |     | : 1c:98:ec:e3:45:00 |        |
| ------------ | ----------- | --- | ------------------- | ------ |
| System       | Name        |     | : switch            |        |
| System       | Description |     | : Aruba             |        |
| Management   | Address     |     | : 192.168.10.1      |        |
| Capabilities | Available   |     | : Bridge,           | Router |
| Capabilities | Enabled     |     | : Bridge,           | Router |
| TTL          |             |     | : 120               |        |
| Port Based   | Data        |     |                     |        |
===============
| Port-ID           |     | :   | 1/1/11         |     |
| ----------------- | --- | --- | -------------- | --- |
| Port-Desc         |     | :   | "1/1/11"       |     |
| Port Mgmt-Address |     | :   | 164.254.21.220 |     |
| Port VLAN         | ID  | :   | 1              |     |
| Port-ID           |     | :   | mgmt           |     |
| Port-Desc         |     | :   | "mgmt"         |     |
| Port Mgmt-Address |     | :   | 164.254.21.220 |     |
Inthisexample,alltheportsexcept1/1/11areadministrativelydown,andVLANID100isconfiguredon
thisaccessinterface.
| switch# | show lldp | local-device |     |     |
| ------- | --------- | ------------ | --- | --- |
Global Data
===========
| Chassis-ID   |             |     | : 1c:98:ec:e3:45:00 |        |
| ------------ | ----------- | --- | ------------------- | ------ |
| System       | Name        |     | : switch            |        |
| System       | Description |     | : Aruba             |        |
| Management   | Address     |     | : 192.168.10.1      |        |
| Capabilities | Available   |     | : Bridge,           | Router |
| Capabilities | Enabled     |     | : Bridge,           | Router |
| TTL          |             |     | : 120               |        |
| Port Based   | Data        |     |                     |        |
===============
| Port-ID   |           | :   | 1/1/11    |        |
| --------- | --------- | --- | --------- | ------ |
| Port-Desc |           | :   | "1/1/11"  |        |
| Port VLAN | ID        | :   | 100       |        |
| Parent    | Interface | :   | interface | 1/1/11 |
| Command   | History   |     |           |        |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 218

| Release        |             |         |         | Modification |     |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |         |         | --           |     |     |
| Command        | Information |         |         |              |     |     |
| Platforms      |             | Command | context | Authority    |     |     |
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
| switch# | show     | lldp        | neighbor-info |     |     |     |
| ------- | -------- | ----------- | ------------- | --- | --- | --- |
| LLDP    | Neighbor | Information |               |     |     |     |
=========================
| Total      | Neighbor | Entries    |          | : 3     |           |              |
| ---------- | -------- | ---------- | -------- | ------- | --------- | ------------ |
| Total      | Neighbor | Entries    | Deleted  | : 0     |           |              |
| Total      | Neighbor | Entries    | Dropped  | : 0     |           |              |
| Total      | Neighbor | Entries    | Aged-Out | : 0     |           |              |
| LOCAL-PORT |          | CHASSIS-ID |          | PORT-ID | PORT-DESC | TTL SYS-NAME |
--------------------------------------------------------------------------------
| 1/1/1  |     | 70:72:cf:a4:7d:50 |     | 1/1/1  | 1/1/1  | 32 switch  |
| ------ | --- | ----------------- | --- | ------ | ------ | ---------- |
| 1/1/2  |     | 48:0f:cf:af:73:80 |     | 1/1/2  | 1/1/2  | 120 switch |
| 1/1/46 |     | 48:0f:cf:af:73:80 |     | 1/1/46 | 1/1/46 | 120 switch |
| mgmt   |     | 48:0f:cf:af:73:80 |     | mgmt   | mgmt   | 120 switch |
Showinginformationforinterface1/3/1whenithasonlyoneswitchconnectedasaneighbor:
Devicediscoveryandconfiguration|219

switch#
|          | show         | lldp | neighbor-info |     | 1/3/1                  |     |
| -------- | ------------ | ---- | ------------- | --- | ---------------------- | --- |
| Port     |              |      |               |     | : 1/1/1                |     |
| Neighbor | Entries      |      |               |     | : 1                    |     |
| Neighbor | Entries      |      | Deleted       |     | : 0                    |     |
| Neighbor | Entries      |      | Dropped       |     | : 0                    |     |
| Neighbor | Entries      |      | Aged-Out      |     | : 0                    |     |
| Neighbor | Chassis-Name |      |               |     | : HP-3800-24G-PoEP-2XG |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor | Chassis-ID         |      |           |     | : 10:60:4b:39:3e:80 |        |
| -------- | ------------------ | ---- | --------- | --- | ------------------- | ------ |
| Neighbor | Management-Address |      |           |     | : 192.168.1.1       |        |
| Chassis  | Capabilities       |      | Available |     | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   |     | : Bridge            |        |
| Neighbor | Port-ID            |      |           |     | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           |     | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        |     | : 1                 |        |
| Neighbor | Port               | VLAN | Name      |     | : DEFAULT_VLAN_1    |        |
| Neighbor | Port               | MFS  |           |     | : 1500              |        |
| TTL      |                    |      |           |     | : 120               |        |
Showinginformationforinterface1/3/10whentheneighborsendsaDOT3powerTLV:
| switch#  | show         | lldp | neighbor-info |     | 1/3/10              |     |
| -------- | ------------ | ---- | ------------- | --- | ------------------- | --- |
| Port     |              |      |               |     | : 1/3/10            |     |
| Neighbor | Entries      |      |               |     | : 1                 |     |
| Neighbor | Entries      |      | Deleted       |     | : 0                 |     |
| Neighbor | Entries      |      | Dropped       |     | : 0                 |     |
| Neighbor | Entries      |      | Aged-Out      |     | : 0                 |     |
| Neighbor | Chassis-Name |      |               |     | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor      | Chassis-ID         |             |             |      | : 84:d4:7e:ce:5d:68 |      |
| ------------- | ------------------ | ----------- | ----------- | ---- | ------------------- | ---- |
| Neighbor      | Management-Address |             |             |      | : 169.254.41.250    |      |
| Chassis       | Capabilities       |             | Available   |      | : Bridge,           | WLAN |
| Chassis       | Capabilities       |             | Enabled     |      | : WLAN              |      |
| Neighbor      | Port-ID            |             |             |      | : 84:d4:7e:ce:5d:68 |      |
| Neighbor      | Port-Desc          |             |             |      | : eth0              |      |
| TTL           |                    |             |             |      | : 120               |      |
| Neighbor      | Port               | VLAN        | ID          |      | : 1                 |      |
| Neighbor      | Port               | VLAN        | Name        |      | : DEFAULT_VLAN_1    |      |
| Neighbor      | Port               | MFS         |             |      | : 1500              |      |
| Neighbor      | PoE                | information |             |      | : DOT3              |      |
| Neighbor      | Power              |             | Type        |      | : TYPE2             | PD   |
| Neighbor      | Power              |             | Priority    |      | : Unkown            |      |
| Neighbor      | Power              |             | Source      |      | : Primary           |      |
| PD Requested  |                    | Power       | Value       |      | : 25.0              | W    |
| PSE Allocated |                    | Power       | Value:      | 25.0 | W                   |      |
| Neighbor      | Power              |             | Supported   |      | : Yes               |      |
| Neighbor      | Power              |             | Enabled     |      | : Yes               |      |
| Neighbor      | Power              |             | Class       |      | : 5                 |      |
| Neighbor      | Power              |             | Paircontrol |      | : No                |      |
| PSE Power     |                    | Pairs       |             |      | : Signal            |      |
Showinginformationforinterface1/1/1whenithasmultipleneighbors(displaysamaximumoffour):
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 220

switch#
| show                  | lldp neighbor-info | 1/1/1    |     |
| --------------------- | ------------------ | -------- | --- |
| Port                  |                    | : 1/1/1  |     |
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
| Neighbor Port               | VLAN ID   | : 1                 |        |
| Neighbor Port               | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor Port               | MFS       | : 1500              |        |
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
| Neighbor Port               | VLAN ID   | : 1                 |        |
| Neighbor Port               | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor Port               | MFS       | : 1500              |        |
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
| Neighbor Port               | VLAN ID   | : 50                |        |
| Neighbor Port               | VLAN Name | : VLAN_50           |        |
| Neighbor Port               | MFS       | : 1500              |        |
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
| Neighbor Port               | VLAN ID   | : 100               |        |
| Neighbor Port               | VLAN Name | : VLAN_100          |        |
| Neighbor Port               | MFS       | : 1500              |        |
| TTL                         |           | : 120               |        |
| Command History             |           |                     |        |
Devicediscoveryandconfiguration|221

| Release        |             |         |         | Modification |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- |
| 10.07orearlier |             |         |         | --           |     |
| Command        | Information |         |         |              |     |
| Platforms      |             | Command | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     | detail |            |     |
| --------- | ------------- | --- | ------ | ---------- | --- |
| show lldp | neighbor-info |     | detail | [vsx-peer] |     |
Description
ShowsdetailedLLDPneighborinformationforallLLDPneighborconnectedinterfaces.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingdetailedLLDPinformationforallinterfaces:
| switch# | show     | lldp | neighbor-info | detail |     |
| ------- | -------- | ---- | ------------- | ------ | --- |
| LLDP    | Neighbor |      | Information   |        |     |
=========================
| Total | Neighbor |     | Entries          | : 6 |     |
| ----- | -------- | --- | ---------------- | --- | --- |
| Total | Neighbor |     | Entries Deleted  | : 2 |     |
| Total | Neighbor |     | Entries Dropped  | : 0 |     |
| Total | Neighbor |     | Entries Aged-Out | : 2 |     |
--------------------------------------------------------------------------------
| Port     |              |                     |           | : 1/1/1             |        |
| -------- | ------------ | ------------------- | --------- | ------------------- | ------ |
| Neighbor |              | Entries             |           | : 1                 |        |
| Neighbor |              | Entries             | Deleted   | : 0                 |        |
| Neighbor |              | Entries             | Dropped   | : 0                 |        |
| Neighbor |              | Entries             | Aged-Out  | : 0                 |        |
| Neighbor |              | Chassis-Name        |           | : 6300              |        |
| Neighbor |              | Chassis-Description |           | : Aruba             | ...    |
| Neighbor |              | Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor |              | Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities |                     | Available | : Bridge,           | Router |
| Chassis  | Capabilities |                     | Enabled   | : Bridge,           | Router |
| Neighbor |              | Port-ID             |           | : 1/1/4             |        |
| Neighbor |              | Port-Desc           |           | : 1/1/4             |        |
| Neighbor |              | Port                | VLAN ID   | : 1                 |        |
| Neighbor |              | Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 222

| Neighbor Port     | MFS       | : 1500 |     |
| ----------------- | --------- | ------ | --- |
| TTL               |           | : 120  |     |
| Neighbor Mac-Phy  | details   |        |     |
| Neighbor Auto-neg | Supported | : true |     |
| Neighbor Auto-Neg | Enabled   | : true |     |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor MAU | type | : 1000 | BASETFD |
| ------------ | ---- | ------ | ------- |
--------------------------------------------------------------------------------
| Port                         |           | : 1/1/2             |        |
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
| Neighbor Port-ID             |           | : 1/1/5             |        |
| Neighbor Port-Desc           |           | : 1/1/5             |        |
| Neighbor Port                | VLAN ID   | : 1                 |        |
| Neighbor Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor Port                | MFS       | : 1500              |        |
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
| Neighbor Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor Port                | MFS       | : 1500              |        |
| TTL                          |           | : 120               |        |
| Neighbor Mac-Phy             | details   |                     |        |
| Neighbor Auto-neg            | Supported | : true              |        |
| Neighbor Auto-Neg            | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor MAU | type | : 1000 | BASETFD |
| ------------ | ---- | ------ | ------- |
--------------------------------------------------------------------------------
Devicediscoveryandconfiguration|223

| Port     |              |                     |           | : 1/1/46            |        |
| -------- | ------------ | ------------------- | --------- | ------------------- | ------ |
| Neighbor |              | Entries             |           | : 1                 |        |
| Neighbor |              | Entries             | Deleted   | : 0                 |        |
| Neighbor |              | Entries             | Dropped   | : 0                 |        |
| Neighbor |              | Entries             | Aged-Out  | : 0                 |        |
| Neighbor |              | Chassis-Name        |           | : 6300              |        |
| Neighbor |              | Chassis-Description |           | : Aruba             | ...    |
| Neighbor |              | Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor |              | Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities |                     | Available | : Bridge,           | Router |
| Chassis  | Capabilities |                     | Enabled   | : Bridge,           | Router |
| Neighbor |              | Port-ID             |           | : 1/1/19            |        |
| Neighbor |              | Port-Desc           |           | : 1/1/19            |        |
| Neighbor |              | Port                | VLAN ID   | : 1                 |        |
| Neighbor |              | Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor |              | Port                | MFS       | : 1500              |        |
| TTL      |              |                     |           | : 120               |        |
| Neighbor |              | Mac-Phy             | details   |                     |        |
| Neighbor |              | Auto-neg            | Supported | : true              |        |
| Neighbor |              | Auto-Neg            | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 224

Examples
ShowingLLDPinformationfortheOOBMinterface:
switch#
| show                  | lldp neighbor-info | mgmt                   |     |
| --------------------- | ------------------ | ---------------------- | --- |
| Port                  |                    | : mgmt                 |     |
| Neighbor Entries      |                    | : 1                    |     |
| Neighbor Entries      | Deleted            | : 0                    |     |
| Neighbor Entries      | Dropped            | : 0                    |     |
| Neighbor Entries      | Aged-Out           | : 0                    |     |
| Neighbor Chassis-Name |                    | : HP-3800-24G-PoEP-2XG |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor Chassis-ID         |           | : 10:60:4b:39:3e:80 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 192.168.1.1       |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge            |        |
| Neighbor Port-ID            |           | : mgmt              |        |
| Neighbor Port-Desc          |           | : mgmt              |        |
| TTL                         |           | : 120               |        |
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
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Devicediscoveryandconfiguration|225

Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor       |              | Chassis-ID         |           |     | : 1c:98:ec:fe:25:03 |        |
| -------------- | ------------ | ------------------ | --------- | --- | ------------------- | ------ |
| Neighbor       |              | Management-Address |           |     | : 10.1.1.5          |        |
| Chassis        | Capabilities |                    | Available |     | : Bridge,           | Router |
| Chassis        | Capabilities |                    | Enabled   |     | : Bridge,           | Router |
| Neighbor       |              | Port-ID            |           |     | : 1/1/1             |        |
| Neighbor       |              | Port-Desc          |           |     | : 1/1/1             |        |
| TTL            |              |                    |           |     | : 120               |        |
| Command        | History      |                    |           |     |                     |        |
| Release        |              |                    |           |     | Modification        |        |
| 10.07orearlier |              |                    |           |     | --                  |        |
| Command        | Information  |                    |           |     |                     |        |
| Platforms      |              | Command            | context   |     | Authority           |        |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | statistics |     |                            |     |     |     |
| --------- | ---------- | --- | -------------------------- | --- | --- | --- |
| show lldp | statistics |     | [<INTERFACE-ID>][vsx-peer] |     |     |     |
Description
ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingglobalstatisticsforallinterfaces:
| switch# | show   | lldp       | statistics |     |     |     |
| ------- | ------ | ---------- | ---------- | --- | --- | --- |
| LLDP    | Global | Statistics |            |     |     |     |
======================
| Total | Packets |              | Transmitted  |           | :   | 19  |
| ----- | ------- | ------------ | ------------ | --------- | --- | --- |
| Total | Packets |              | Received     |           | :   | 19  |
| Total | Packets |              | Received And | Discarded | :   | 0   |
| Total | TLVs    | Unrecognized |              |           | :   | 0   |
| LLDP  | Port    | Statistics   |              |           |     |     |
====================
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 226

| PORT-ID |     | TX-PACKETS |     | RX-PACKETS | RX-DISCARDED | TLVS-UNKNOWN |
| ------- | --- | ---------- | --- | ---------- | ------------ | ------------ |
-------------------------------------------------------------------------
| 1/1/1 |     | 7   |     | 7   | 0   | 0   |
| ----- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     | 7   |     | 7   | 0   | 0   |
| 1/1/3 |     | 0   |     | 0   | 0   | 0   |
| 1/1/4 |     | 0   |     | 0   | 0   | 0   |
| 1/1/5 |     | 0   |     | 0   | 0   | 0   |
...
| mgmt |     | 5   |     | 5   | 0   | 0   |
| ---- | --- | --- | --- | --- | --- | --- |
```
Showingstatisticsforinterface1/1/1:
| switch# | show       | lldp | statistics | 1/1/1 |     |     |
| ------- | ---------- | ---- | ---------- | ----- | --- | --- |
| LLDP    | Statistics |      |            |       |     |     |
===============
| Port           | Name        |         |              | : 1/1/1      |     |     |
| -------------- | ----------- | ------- | ------------ | ------------ | --- | --- |
| Packets        | Transmitted |         |              | : 159        |     |     |
| Packets        | Received    |         |              | : 163        |     |     |
| Packets        | Received    | And     | Discarded    | : 0          |     |     |
| Packets        | Received    | And     | Unrecognized | : 0          |     |     |
| Command        | History     |         |              |              |     |     |
| Release        |             |         |              | Modification |     |     |
| 10.07orearlier |             |         |              | --           |     |     |
| Command        | Information |         |              |              |     |     |
| Platforms      |             | Command | context      | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | statistics | mgmt |     |     |     |     |
| --------- | ---------- | ---- | --- | --- | --- | --- |
| show lldp | statistics | mgmt |     |     |     |     |
Description
ShowsLLDPstatisticsfortheOOBMinterface.
Example
ShowingLLDPstatisticsfortheOOBMinterface:
| switch# | show       | lldp | statistics | mgmt |     |     |
| ------- | ---------- | ---- | ---------- | ---- | --- | --- |
| LLDP    | Statistics |      |            |      |     |     |
===============
Devicediscoveryandconfiguration|227

| Port Name           |         |              | : mgmt                                               |
| ------------------- | ------- | ------------ | ---------------------------------------------------- |
| Packets Transmitted |         |              | : 20                                                 |
| Packets Received    |         |              | : 23                                                 |
| Packets Received    | And     | Discarded    | : 0                                                  |
| Packets Received    | And     | Unrecognized | : 0                                                  |
| Command History     |         |              |                                                      |
| Release             |         |              | Modification                                         |
| 10.07orearlier      |         |              | --                                                   |
| Command Information |         |              |                                                      |
| Platforms           | Command | context      | Authority                                            |
| 8400                |         |              | OperatorsorAdministratorsorlocalusergroupmemberswith |
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp tlv           |     |     |     |
| ----------------------- | --- | --- | --- |
| show lldp tlv[vsx-peer] |     |     |     |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# show | lldp tlv |     |     |
| ------------ | -------- | --- | --- |
TLVs Advertised
===============
| Management | Address |     |     |
| ---------- | ------- | --- | --- |
Port Description
Port VLAN-ID
| System Capabilities |     |     |     |
| ------------------- | --- | --- | --- |
| System Description  |     |     |     |
| System Name         |     |     |     |
VLAN Name
MFS
OUI
| Command History |     |     |     |
| --------------- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 228

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

Cisco Discovery Protocol (CDP)

Cisco Discovery Protocol (CDP) is a proprietary layer 2 protocol supported by most Cisco devices. It is
used to exchange information, such as software version, device capabilities, and voice VLAN
information, between directly connected devices, such as a VoIP phone and a switch.

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

Device discovery and configuration | 229

cdp
cdp
Description
ConfiguresCDPsupportgloballyonallactiveinterfacesoronaspecificinterface.Bydefault,CDPis
enabledonallactiveinterfaces.
WhenCDPisenabled,theswitchaddsentriestoitsCDPNeighborstableforanyCDPpacketsitreceives
fromneighboringCDPdevices.
WhenCDPisdisabled,theCDPNeighborstableisclearedandtheswitchdropsallinboundCDPpackets
withoutenteringthedataintheCDPNeighborstable.
ThenoformofthiscommanddisablesCDPsupportgloballyonallactiveinterfacesoronaspecific
interface.
Examples
EnablingCDPglobally:
| switch(config)# | cdp |     |     |
| --------------- | --- | --- | --- |
DisablingCDPglobally:
| switch(config)# | no  | cdp |     |
| --------------- | --- | --- | --- |
EnablingCDPoninterface1/1/1:
| switch(config)#    | interface | 1/1/1s |     |
| ------------------ | --------- | ------ | --- |
| switch(config-if)# |           | cdp    |     |
DisablingCDPoninterface1/1/1:
| switch(config)#     | interface | 1/1/1   |              |
| ------------------- | --------- | ------- | ------------ |
| switch(config-if)#  |           | no cdp  |              |
| Command History     |           |         |              |
| Release             |           |         | Modification |
| 10.07orearlier      |           |         | --           |
| Command Information |           |         |              |
| Platforms           | Command   | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
|                    | config-if |     | rightsforthiscommand. |
| ------------------ | --------- | --- | --------------------- |
| clear cdp counters |           |     |                       |
| clear cdp counters |           |     |                       |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 230

Description
ClearsCDPcounters.
Examples
ClearingCDPcounters:
| switch(config)      | clear   | cdp counters |              |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear cdp neighbor-info |     |     |     |
| ----------------------- | --- | --- | --- |
| clear cdp neighbor-info |     |     |     |
Description
ClearsCDPneighborinformation.
Examples
ClearingCDPneighborinformation:
| switch(config)      | clear   | neighbor-info |              |
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
Devicediscoveryandconfiguration|231

ShowsCDPinformationforallinterfaces.
Examples
ShowingCDPinformation:
| switch(config)# | show        | cdp |     |
| --------------- | ----------- | --- | --- |
| CDP Global      | Information |     |     |
======================
| CDP                 | : Enabled      |         |              |
| ------------------- | -------------- | ------- | ------------ |
| CDP Mode            | : Rx           | only    |              |
| CDP Hold            | Time : 180     | seconds |              |
| Port                | CDP            |         |              |
| --------            | -------------- |         |              |
| 1/1/1               | Enabled        |         |              |
| 1/1/2               | Enabled        |         |              |
| 1/1/3               | Enabled        |         |              |
| 1/1/4               | Enabled        |         |              |
| 1/1/5               | Enabled        |         |              |
| 1/1/6               | Enabled        |         |              |
| 1/1/7               | Enabled        |         |              |
| 1/1/8               | Enabled        |         |              |
| 1/1/9               | Enabled        |         |              |
| 1/1/10              | Enabled        |         |              |
| Command History     |                |         |              |
| Release             |                |         | Modification |
| 10.07orearlier      |                |         | --           |
| Command Information |                |         |              |
| Platforms           | Command        | context | Authority    |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp neighbor-info |     |                |     |
| ---------------------- | --- | -------------- | --- |
| show cdp neighbor-info |     | <INTERFACE-ID> |     |
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
| Parameter      |     |     | Description                                   |
| -------------- | --- | --- | --------------------------------------------- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |
Examples
ShowingallCDPneighborinformation:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 232

| switch(config)# |        | show    | cdp | neighbor-info |     |          |     |            |     |
| --------------- | ------ | ------- | --- | ------------- | --- | -------- | --- | ---------- | --- |
| Total Neighbor  |        | Entries |     | : 1           |     |          |     |            |     |
| Port            | Device |         | ID  |               |     | Platform |     | Capability |     |
---------------------------------------------------------------------------
| 1/1/1 | HPE-ANW-3810M-24G-1-slot... |     |     |     |     | Aruba | Sw  |     | S   |
| ----- | --------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- |
ShowingCDPinformationforinterface1/1/1:
| switch(config)# |             | show | cdp                                       | neighbor-info  |              | 1/1/1 |                  |     |     |
| --------------- | ----------- | ---- | ----------------------------------------- | -------------- | ------------ | ----- | ---------------- | --- | --- |
| Local Port      |             |      | : 1/1/1                                   |                |              |       |                  |     |     |
| MAC             |             |      | : 70:10:6f:86:78:7f                       |                |              |       |                  |     |     |
| Device ID       |             |      | : HPE-ANW-3810M-24G-1-slot(70106f-867800) |                |              |       |                  |     |     |
| Address         |             |      | : 127.0.0.1                               |                |              |       |                  |     |     |
| Platform        |             |      | : HPE ANW                                 | Sw             |              |       |                  |     |     |
| Duplex          |             |      | : half                                    |                |              |       |                  |     |     |
| Version         |             |      | : Revision                                | KB.16.07.0002, |              |       | ROM KB.16.01.... |     |     |
| Capability      |             |      | : switch                                  |                |              |       |                  |     |     |
| Native VLAN     |             |      | : 1                                       |                |              |       |                  |     |     |
| Voice VLAN      | Support     |      | : No                                      |                |              |       |                  |     |     |
| Neighbor        | Port-ID     |      | : 1                                       |                |              |       |                  |     |     |
| Command         | History     |      |                                           |                |              |       |                  |     |     |
| Release         |             |      |                                           |                | Modification |       |                  |     |     |
| 10.07orearlier  |             |      |                                           |                | --           |       |                  |     |     |
| Command         | Information |      |                                           |                |              |       |                  |     |     |
| Platforms       | Command     |      | context                                   |                | Authority    |       |                  |     |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp traffic |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
show cdp traffic
Description
ShowsCDPstatisticsforeachinterface.
Examples
ShowingCDPtrafficstatistics:
switch(config)#
|     |     | show | cdp | traffic |     |     |     |     |     |
| --- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- |
CDP Statistics
====================
| Port | Transmitted |     |     | Frames |     | Received | Frames | Discarded | Frames |
| ---- | ----------- | --- | --- | ------ | --- | -------- | ------ | --------- | ------ |
--------------------------------------------------------------------------------
| 1/1/1 |     | 0   |     |     |     | 4   |     | 0   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     | 0   |     |     |     | 0   |     | 0   |     |
| 1/1/3 |     | 0   |     |     |     | 2   |     | 0   |     |
| 1/1/4 |     | 0   |     |     |     | 0   |     | 0   |     |
Devicediscoveryandconfiguration|233

| 1/1/5          |             |         | 0       |     | 0            | 0   |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Command        | History     |         |         |     |              |     |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp | voice-vlan |     | mode |     |     |     |
| -------- | ---------- | --- | ---- | --- | --- | --- |
| show cdp | voice-vlan |     | mode |     |     |     |
Description
ShowsCDPvoice-vlanandmode.
Examples
ShowingCDPvoice-vlanandmode:
| switch(config)# |       |      | show cdp voice-vlan |     | mode |     |
| --------------- | ----- | ---- | ------------------- | --- | ---- | --- |
| CDP             | voice | VLAN | mode                |     |      |     |
====================
| Port           |             | Voice       | VLAN    | Mode       |              |     |
| -------------- | ----------- | ----------- | ------- | ---------- | ------------ | --- |
| --------       |             | ----------- |         | ---------- |              |     |
| 1/1/1          |             | N/A         |         | Rx         | only         |     |
| 1/1/2          |             | N/A         |         | Rx         | only         |     |
| 1/1/3          |             | N/A         |         | Rx         | only         |     |
| 1/1/4          |             | N/A         |         | Rx         | only         |     |
| 1/1/5          |             | N/A         |         | Rx         | only         |     |
| 1/1/6          |             | N/A         |         | Rx         | only         |     |
| 1/1/7          |             | N/A         |         | Rx         | only         |     |
| 1/1/8          |             | N/A         |         | Rx         | only         |     |
| 1/1/9          |             | N/A         |         | Rx         | only         |     |
| Command        | History     |             |         |            |              |     |
| Release        |             |             |         |            | Modification |     |
| 10.07orearlier |             |             |         |            | --           |     |
| Command        | Information |             |         |            |              |     |
| Platforms      |             | Command     | context |            | Authority    |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 234

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

235

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

Zero Touch Provisioning | 236

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

237

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

Zero Touch Provisioning | 238

n The IP address of the TFTP server

n The name of the image file

n The name of the configuration file

n The Aruba FDQN or IPv4 address

n The HTTP proxy FDQN or IPv4 address

The show ztp information command shows the options offered by the DHCP server and the status of
the ZTP operation.

The status of the ZTP operation is one of the following:

Success

The ZTP operation succeeded.

One of the following is true:

n Both the running configuration and the startup configuration were updated.

n The IP address of the TFTP server was received, but the offer did not include a configuration file or a

firmware image file.

n Any combination of vendor encapsulated DHCP options are received as configured, along with the

firmware image and switch configuration file.

n Only vendor encapsulated DHCP options are configured and are received accordingly.

Failed - Custom startup configuration detected

The switch was booted from a configuration that is not the factory default configuration. For example,
the administrator password has been set.

Failed - Timed out while waiting to receive ZTP options

Either the switch received the DHCP IPv4 address but no ZTP options were received within 1 minute or
ZTP force-provision is triggered and no ZTP options are received within 3 minutes.

Failed - Detected change in running configuration

The running configuration was modified by a user while the ZTP operation was in progress.

Failed - TFTP server unreachable

The TFTP server is not reachable at the specified IP address.

Failed - TFTP server information unavailable

The image file name or config file name is provided without the TFTP server location to fetch the files
from and ZTP enters failed state.

Failed - Invalid configuration file received

Either the file transfer of the configuration file failed, or the configuration file is invalid (an error
occurred while attempting to apply the configuration).

Failed - Invalid image file received

Either the file transfer of the firmware image file failed, or the firmware image file is invalid (an error
occurred while verifying the image).

In the case of reconnection, connect with a main or alternative location to the COP instance as a user. The current

connection is shown in the Central location field.

Scenario 1: If the location the device is currently connected on is updated, the system reconnects in order to

connect with the new location.

Scenario 2: If the location in which the device is not currently connected on is updated, the DUT does not go

through the reconnection process.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

239

Examples
ShowingswitchimagedownloadinprogressafterreceivingZTP options:
switch#
show ztp information
| TFTP Server     |                 |                            | : 10.0.0.2                     |         |          |                  |
| --------------- | --------------- | -------------------------- | ------------------------------ | ------- | -------- | ---------------- |
| Image File      |                 |                            | : TL_10_02_0001.swi            |         |          |                  |
| Configuration   | File            |                            | : config_file                  |         |          |                  |
| ZTP Status      |                 |                            | : In-progress                  | - Image | download | and verification |
| Aruba Location  |                 | : secure.arubanetworks.com |                                |         |          |                  |
| Alternative     | Aruba Location: | NA                         |                                |         |          |                  |
| Aruba Shared    | Token           | : aruba123                 |                                |         |          |                  |
| Force-Provision |                 |                            | : Disabled                     |         |          |                  |
| HTTP Proxy      | Location        |                            | : http.proxy.arubanetworks.com |         |          |                  |
ShowingswitchimagedownloadfailureafterreceivingZTPoptions:
| switch#        | show ztp information |                            |                     |          |             |       |
| -------------- | -------------------- | -------------------------- | ------------------- | -------- | ----------- | ----- |
| TFTP Server    |                      |                            | : 10.0.0.2          |          |             |       |
| Image File     |                      |                            | : TL_10_02_0001.swi |          |             |       |
| Configuration  | File                 |                            | : config_file       |          |             |       |
| ZTP Status     |                      |                            | : Failed            | - Unable | to download | image |
| Aruba Location |                      | : secure.arubanetworks.com |                     |          |             |       |
| Alternative    | Aruba Location:      | NA                         |                     |          |             |       |
| Shared         | Token                | : aruba123                 |                     |          |             |       |
Aruba
| Force-Provision |          |     | : Disabled                     |     |     |     |
| --------------- | -------- | --- | ------------------------------ | --- | --- | --- |
| HTTP Proxy      | Location |     | : http.proxy.arubanetworks.com |     |     |     |
ShowingswitchconfigurationdownloadinprogressafterreceivingZTPoptions:
| switch#       | show ztp information |                            |                     |                 |     |          |
| ------------- | -------------------- | -------------------------- | ------------------- | --------------- | --- | -------- |
| TFTP Server   |                      |                            | : 10.0.0.2          |                 |     |          |
| Image File    |                      |                            | : TL_10_02_0001.swi |                 |     |          |
| Configuration | File                 |                            | : config_file       |                 |     |          |
| ZTP Status    |                      |                            | : In-progress       | - Configuration |     | download |
| Location      |                      | : secure.arubanetworks.com |                     |                 |     |          |
Aruba
| Alternative     | Aruba Location | : NA       |                                |     |     |     |
| --------------- | -------------- | ---------- | ------------------------------ | --- | --- | --- |
| Aruba Shared    | Token          | : aruba123 |                                |     |     |     |
| Force-Provision |                |            | : Disabled                     |     |     |     |
| HTTP Proxy      | Location       |            | : http.proxy.arubanetworks.com |     |     |     |
ShowingswitchconfigurationdownloadfailureafterreceivingZTPoptions:
| switch#         | show ztp information |                            |                                |          |             |               |
| --------------- | -------------------- | -------------------------- | ------------------------------ | -------- | ----------- | ------------- |
| TFTP Server     |                      |                            | : 10.0.0.2                     |          |             |               |
| Image File      |                      |                            | : TL_10_02_0001.swi            |          |             |               |
| Configuration   | File                 |                            | : config_file                  |          |             |               |
| ZTP Status      |                      |                            | : Failed                       | - Unable | to download | configuration |
| Aruba Location  |                      | : secure.arubanetworks.com |                                |          |             |               |
| Alternative     | Aruba Location       | : NA                       |                                |          |             |               |
| Aruba Shared    | Token                | : aruba123                 |                                |          |             |               |
| Force-Provision |                      |                            | : Disabled                     |          |             |               |
| HTTP Proxy      | Location             |                            | : http.proxy.arubanetworks.com |          |             |               |
Showingswitchfailuretoupdatestart-upconfigurationafterdownloadingconfigurationreceivedfrom
ZTPoptions:
ZeroTouchProvisioning|240

| switch#       | show ztp information |     |                     |     |     |
| ------------- | -------------------- | --- | ------------------- | --- | --- |
| TFTP Server   |                      |     | : 10.0.0.2          |     |     |
| Image File    |                      |     | : TL_10_02_0001.swi |     |     |
| Configuration | File                 |     | : config_file       |     |     |
ZTP Status : Failed - Could not copy to start-up configuration
| Aruba Location  |                 | : secure.arubanetworks.com |                                |     |     |
| --------------- | --------------- | -------------------------- | ------------------------------ | --- | --- |
| Alternative     | Aruba Location: | NA                         |                                |     |     |
| Aruba Shared    | Token           | : aruba123                 |                                |     |     |
| Force-Provision |                 |                            | : Disabled                     |     |     |
| HTTP Proxy      | Location        |                            | : http.proxy.arubanetworks.com |     |     |
Inthefollowingexample,theZTPoperationsucceeded,andbothanimagefileandaconfigurationfile
wereprovided.
| VSF-10-Mbr#     | show ztp       | information |                                       |     |     |
| --------------- | -------------- | ----------- | ------------------------------------- | --- | --- |
| TFTP Server     |                |             | : 10.1.84.160                         |     |     |
| Image File      |                |             | : FL_10_06_0001CK.swi                 |     |     |
| Configuration   | File           |             | : 102720-new-setup-config-updated.txt |     |     |
| Status          |                |             | : Success                             |     |     |
| Aruba Location  | :              | NA          |                                       |     |     |
| Alternative     | Aruba Location | : NA        |                                       |     |     |
| Aruba Shared    | Token          | : aruba123  |                                       |     |     |
| Force-Provision |                |             | : Disabled                            |     |     |
| HTTP Proxy      | Location       |             | : NA                                  |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoptionsucceeded.Aconfigurationfilewasnotprovided,butanimage
filewasprovided.
| VSF-10-Mbr#     | show ztp        | information |                     |     |     |
| --------------- | --------------- | ----------- | ------------------- | --- | --- |
| TFTP Server     |                 |             | : 10.1.84.160       |     |     |
| Image File      |                 |             | : TL_10_02_0001.swi |     |     |
| Configuration   | File            |             | : NA                |     |     |
| Status          |                 |             | : Success           |     |     |
| Aruba Location  | : NA            |             |                     |     |     |
| Alternative     | Aruba Location: | NA          |                     |     |     |
| Aruba Shared    | Token           | : aruba123  |                     |     |     |
| Force-Provision |                 |             | : Disabled          |     |     |
| HTTP Proxy      | Location        |             | : NA                |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationfailedbecausetheTFTPserverwasunreachable.
| VSF-10-Mbr#   | show ztp | information |                                       |               |             |
| ------------- | -------- | ----------- | ------------------------------------- | ------------- | ----------- |
| TFTP Server   |          |             | : 10.1.84.160                         |               |             |
| Image File    |          |             | : TL_10_02_0001.swi                   |               |             |
| Configuration | File     |             | : 102720-new-setup-config-updated.txt |               |             |
| Status        |          |             | : Failed                              | - TFTP server | unreachable |
| Location      | :        | NA          |                                       |               |             |
Aruba
| Alternative     | Aruba Location: | NA   |            |     |     |
| --------------- | --------------- | ---- | ---------- | --- | --- |
| Aruba Shared    | Token           | : NA |            |     |     |
| Force-Provision |                 |      | : Disabled |     |     |
| HTTP Proxy      | Location        |      | : NA       |     |     |
VSF-10-Mbr#
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 241

Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchdidnotreceiveanyoptions
fromtheDHCPserverforZTPwithin1minuteofreceivingtheIPaddressfromtheserver.
| VSF-10-Mbr## | show ztp information |     |     |     |     |     |
| ------------ | -------------------- | --- | --- | --- | --- | --- |
TFTP Server : NA
Image File : NA
| Configuration | File | : NA     |             |               |            |     |
| ------------- | ---- | -------- | ----------- | ------------- | ---------- | --- |
| Status        |      | : Failed | - Timed out | while waiting | to receive | ZTP |
options
| Aruba Location | : NA            |      |     |     |     |     |
| -------------- | --------------- | ---- | --- | --- | --- | --- |
| Alternative    | Aruba Location: | NA   |     |     |     |     |
| Shared         | Token           | : NA |     |     |     |     |
Aruba
Force-Provision : Disabled
| HTTP Proxy | Location | : NA |     |     |     |     |
| ---------- | -------- | ---- | --- | --- | --- | --- |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchwasbootedfroma
configurationthatwasnotthefactorydefaultconfiguration.
| switch# | show ztp information |     |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- | --- |
TFTP Server : 10.0.0.2
Image File : TL_10_02_0001.swi
| Configuration  | File            | : ztp.cfg |          |                       |          |     |
| -------------- | --------------- | --------- | -------- | --------------------- | -------- | --- |
| Status         |                 | : Failed  | - Custom | startup configuration | detected |     |
| Aruba Location | : NA            |           |          |                       |          |     |
| Alternative    | Aruba Location: | NA        |          |                       |          |     |
| Shared         | Token           | : NA      |          |                       |          |     |
Aruba
Force-Provision : Disabled
| HTTP Proxy | Location | : NA |     |     |     |     |
| ---------- | -------- | ---- | --- | --- | --- | --- |
Inthefollowingexample,theswitchreceivedtheimagefileandtheTFTP-severandconfigfilefromthe
DHCPserverforZTPwassuccessful:
| switch# | show ztp information |     |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- | --- |
TFTP Server : 10.0.0.2
Image File : TL_10_02_0001.swi
| Configuration | File | : ztp.cfg |     |     |     |     |
| ------------- | ---- | --------- | --- | --- | --- | --- |
ZTP Status : Success
| Aruba Location |                 | : NA |     |     |     |     |
| -------------- | --------------- | ---- | --- | --- | --- | --- |
| Alternative    | Aruba Location: | NA   |     |     |     |     |
| Aruba Shared   | Token           | : NA |     |     |     |     |
Force-Provision : Disabled
| HTTP Proxy | Location | : NA |     |     |     |     |
| ---------- | -------- | ---- | --- | --- | --- | --- |
Inthefollowingexample,theswitchreceivedtheimagefileandtheTFTP-severandconfigfilefromthe
DHCPserverenteredthefailedstateastehTFTPserverwasnotreachable:
switch#
show ztp information
TFTP Server : 10.0.0.2
Image File : TL_10_02_0001.swi
| Configuration  | File            | : ztp.cfg |               |             |     |     |
| -------------- | --------------- | --------- | ------------- | ----------- | --- | --- |
| ZTP Status     |                 | : Failed  | - TFTP server | unreachable |     |     |
| Aruba Location |                 | : NA      |               |             |     |     |
| Alternative    | Aruba Location: | NA        |               |             |     |     |
| Aruba Shared   | Token           | : NA      |               |             |     |     |
Force-Provision : Disabled
ZeroTouchProvisioning|242

| HTTP Proxy     | Location    |         | : NA         |
| -------------- | ----------- | ------- | ------------ |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| ztp force | provision |     |     |
| --------- | --------- | --- | --- |
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
| switch# | configure terminal |     |     |
| ------- | ------------------ | --- | --- |
switch(config)#
|     | ztp | force-provision |     |
| --- | --- | --------------- | --- |
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
| switch#         | show ztp information |       |                     |
| --------------- | -------------------- | ----- | ------------------- |
| TFTP Server     |                      |       | : 10.0.0.2          |
| Image File      |                      |       | : TL_10_02_0001.swi |
| Configuration   | File                 |       | : ztp.cfg           |
| Status          |                      |       | : Success           |
| Aruba Central   | Location             |       | : NA                |
| Aruba Central   | Shared               | Token | : NA                |
| Force-Provision |                      |       | : Enabled           |
| HTTP Proxy      | Location             |       | : NA                |
Inthefollowingexample,force-provisionisdisabled.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 243

| switch# | configure terminal |     |     |
| ------- | ------------------ | --- | --- |
switch(config)#
|     | no  | ztp force-provision |     |
| --- | --- | ------------------- | --- |
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
rightsforthiscommand.
(#)
ZeroTouchProvisioning|244

Chapter 13

vSphere agent

vSphere agent

The HPE Aruba Networking CX vSphere agent allows administrators to trace how Virtual Machines are
connected to the physical switches. The ability to visualize how a Virtual Machine connects to a CX port
helps to resolve connectivity issues. This functionality helps operators in several troubleshooting
scenarios, such as diagnosing a connectivity issue, or ensuring adequate distribution of VMs across the
physical infrastructure.

You can install the vSphere agent on one or many of the switches in the fabric. You can perform the
following tasks, from any switch where the agent is installed:

1. Run the show VMs command to list all the VMs managed by the vCenter Appliance integrated with
the agent. This functionality also helps to view VMs connections to the ports on other switches on
the fabric.

2. Search for a specific VM by name. To find the connection between the VM and a switch port,

attach the switch to at least one host managed by the integrated vCenter.

For more information about cloud capabilities of vSphere agent, refer to vSphere Integration.

The show neighbors command examines the LLDP data that is advertised from any switch to a distributed virtual

switch and provides connection details for third-party switches.

Installation of vSphere agent

To install a container, perform the following steps:

1. Download the vSphere agent from ASP and select the arm vs. x86_64 architecture for the switch
platform. Refer to the list of supported switches mentioned earlier to select the corresponding
architecture.

2. Host the agent on a local network that can be accessed using the HTTP protocol. Usage of the

https protocol is a limitation of the container framework. The directory where the images of the
agents are placed will be set in step 3.d. The HTTP server must be reachable on the mgmt vrf - or
otherwise configured vrf. Any simple HTTP server helps to accomplish this step.

Configure the CLI using the following commands:

1. To enter the config mode, run the container vsphere command.

2. To set the management vrf as the communication path for the container, run the vrf mgmt

command. The vrf is mgmt by default, or you can specify any other non-default vrf configured by
the user. mgmt is the only supported vrf currently.

3. To limit memory usage of the container, run the restrict memory command. Set 1GB for vSphere

instance.

4. To set the installation path to the path accessible by the HTTP protocol noted in Step 2, run the

image location command.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

245

5. TopassattributestobeconfiguredforthecontainerfromCXCLI,runtheenvcommand.Usethe
followingformattopasstheattributestoestablishtheconfigurationinstance:
a. VSPHERE_VCENTER_N,whereNtakesvalueintherange1–4.
b. TheencryptedplaintextcommandwithargumentsintheformofvSpherecredentials,for
example:user@<domain>:password@<fqdnofvcenter>
Thefollowingexampledisplaysavalidrunningconfig:
|     | container |     | vsphere |     |     |     |
| --- | --------- | --- | ------- | --- | --- | --- |
image-location http://X.X.X.X:8000//vsphere-agent.img vrf mgmt restrict
cpu 20
|     | restrict | memory            |     | 512 vrf mgmt |     |           |
| --- | -------- | ----------------- | --- | ------------ | --- | --------- |
|     | env      | VSPHERE_VCENTER_1 |     | encrypted    |     | plaintext |
USER@vsphere.local:PASSWORD@X.X.X.X
Show commands
Therearefourtop-levelshowcommands.
vms-showsvirtualmachineconnectioninformation.
n
n connection-status-showsinformationaboutconfiguredvSpherevCenters.
n neighbors-showslearnedneighborinformation(Note:ThisinformationislearnedfromLLDPon
vCenterdistributedvswitches,nottheswitch).
n help-showsagentversion,description,andconfigurableenvironmentvariables.
show vms
ThefollowingshowcommanddescribesthestatusoftheconnectiontovSphere,andshowtheVMsthat
areattachedtoswitches:
Atleastonecommandparametermustbeusediftheparametersareavailable.
Forexample,withtheshowvmscommand,weforceuseofthebriefoptionsotheuserisawareofall
availableoptions.
Ifnotspecified,allcommandsdefaulttobrief.
igor-sw-02# container vsphere exec show vms brief Hypervisor VM Name Physical
| Switch | Connections |     | Interface |     |     |     |
| ------ | ----------- | --- | --------- | --- | --- | --- |
laser-02-esxi.lab.plexxi.com vm4 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3 vm2 laser-
| sw-02 | (b8:d4:e7:da:40:00) |     |     | 1/1/4 |     |     |
| ----- | ------------------- | --- | --- | ----- | --- | --- |
laser-sw-02 (b8:d4:e7:da:40:00) 1/1/3 vm5 laser-sw-02 (b8:d4:e7:da:40:00) 1/1/4
laser-sw-02 (b8:d4:e7:da:40:00) 1/1/3 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3
laser-01-esxi.lab.plexxi.com vm1 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/1 vm3 laser-
| sw-01       | (b8:d4:e7:d9:af:00) |     |     | 1/1/2 |     |     |
| ----------- | ------------------- | --- | --- | ----- | --- | --- |
| laser-sw-02 | (b8:d4:e7:da:40:00) |     |     | 1/1/1 |     |     |
igor-sw-02# container vsphere exec show vms vm-name vm4 Hypervisor VM Name
| Physical | Switch | Connections |     | Interface |     |     |
| -------- | ------ | ----------- | --- | --------- | --- | --- |
laser-02-esxi.lab.plexxi.com vm4 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3 igor-sw-02#
container vsphere exec show vms vm-name vm4 detailed VM Name : vm4
| Hypervisor  | :     | laser-02-esxi.lab.plexxi.com |         |          |           | Vendor : vmware |
| ----------- | ----- | ---------------------------- | ------- | -------- | --------- | --------------- |
| Hostname    | : vm4 |                              |         |          |           |                 |
| OS : CentOS | 4/5   | or                           | later   | (64-bit) | VM status | : on            |
| Virtual     | NIC : | Network                      | adapter | 2 IP     | Address   | : 172.20.12.204 |
vSphereagent|246

| MAC Address | :      | 00:50:56:89:3c:bf |      |     | Virtual   |      | Switch :      | dvs4 |
| ----------- | ------ | ----------------- | ---- | --- | --------- | ---- | ------------- | ---- |
| Port Group  | :      | dpg4              | Vlan | : 0 |           |      |               |      |
| Physical    | Switch | Connections       |      |     | Interface | :    | 1/1/3         |      |
| Chassis     | ID :   | b8:d4:e7:d9:af:00 |      |     | Switch    | Name | : laser-sw-01 |      |
Switch Description : Aruba JL635A GL.10.12.0001G Management Address :
172.20.11.253
Container exec commands are top-level, and can be run in any CLI context.
igor-sw-02# container vsphere exec show connection-status brief Hypervisor Last
| Sync Connection |     | State |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
laser-vcsa.lab.plexxi.com 2023-03-17 23:30:03 connected igor-sw-02# config
igor-sw-02(config)# container vsphere exec show connection-status brief Hypervisor
| Last Sync | Connection |     | State |     |     |     |     |     |
| --------- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
laser-vcsa.lab.plexxi.com 2023-03-17 23:30:07 connected igor-sw-02(config)#
| interface | 1/1/1 |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
igor-sw-02(config-if)# container vsphere exec show connection-status brief
| Hypervisor                | Last | Sync | Connection |            | State |          |           |     |
| ------------------------- | ---- | ---- | ---------- | ---------- | ----- | -------- | --------- | --- |
| laser-vcsa.lab.plexxi.com |      |      |            | 2023-03-17 |       | 23:30:15 | connected |     |
show vms
ThiscommanddisplaystheconnectivitystatusforthevSphereagent.
TheconnectiontimestampisupdatedwheneverasuccessfulconnectionismadewiththevSphere
agent.Thesynctimestampisupdatedwheneverafullsync,eventpoll,oreventprocessoccurs.
igor-sw-02(config-container-vsphere)# container vsphere exec show connection-
| status                    | brief | Hypervisor |     | Last       | Sync | Connection | State     |     |
| ------------------------- | ----- | ---------- | --- | ---------- | ---- | ---------- | --------- | --- |
| laser-vcsa.lab.plexxi.com |       |            |     | 2023-03-18 |      | 02:36:06   | connected |     |
igor-sw-02(config-container-vsphere)# container vsphere exec show connection-
| status          | detailed | Hypervisor |            | :   | laser-vcsa.lab.plexxi.com |        |            |          |
| --------------- | -------- | ---------- | ---------- | --- | ------------------------- | ------ | ---------- | -------- |
| Connection      | State    | :          | connected  |     | Last                      | Sync : | 2023-03-18 | 02:35:08 |
| Last Connection |          | :          | 2023-03-18 |     | 02:35:09                  |        |            |          |
igor-sw-02(config-container-vsphere)# container vsphere exec show connection-
| status | detailed | Hypervisor |     | :   | laser-vcsa.lab.plexxi.com |     |     |     |
| ------ | -------- | ---------- | --- | --- | ------------------------- | --- | --- | --- |
Connection State : disconnected Last Sync : 2023-03-18 02:04:05
| Last Connection |         | :   | 2023-03-18 |     | 02:09:30 |             |          |     |
| --------------- | ------- | --- | ---------- | --- | -------- | ----------- | -------- | --- |
| Connection      | Failure |     | Reason     | :   | Could    | Not Resolve | Hostname |     |
show neighbors
showneighborscommanddisplaysthevirtualnetworkadapterneighborinformation.
NeighborsarepulledfromdistributedvirtualswitchesofthevSphereandcachedlocally.Neighborsare
usedtomapVMstophysicalswitchports.
Ifyoudonotseeaneighborontheport,youwillnotseeanyVMconnectivityonthatporteither.
detailedandbriefoptionsareavailable.Filteringcanbedoneonswitch-nameand/orinterface.
igor-sw-02(config-container-vsphere)# container vsphere exec show neighbors brief
| Chassis           | ID Switch |     | Name        | Interface |       |       |     |     |
| ----------------- | --------- | --- | ----------- | --------- | ----- | ----- | --- | --- |
| b8:d4:e7:da:40:00 |           |     | laser-sw-02 |           | 1/1/1 | 1/1/2 |     |     |
| b8:d4:e7:d9:af:00 |           |     | laser-sw-01 |           | 1/1/1 | 1/1/2 |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 247

igor-sw-02(config-container-vsphere)# container vsphere exec show neighbors
detailed Chassis ID : b8:d4:e7:da:40:00
Switch Name : laser-sw-02
Switch Description : Aruba JL635A GL.10.10.1000 Management Address : 192.168.200.1
Interface : 1/1/1 Advertisement Type : lldp TTL : 102
Interface : 1/1/2 Advertisement Type : lldp TTL : 102
Chassis ID : b8:d4:e7:d9:af:00 Switch Name : laser-sw-01
Switch Description : Aruba JL635A GL.10.10.1000 Management Address : 192.168.200.0
Interface : 1/1/1 Advertisement Type : lldp TTL : 102
Interface : 1/1/2 Advertisement Type : lldp TTL : 102

Supported switches

The following switch platforms are validated for data center. The agent itself has no context about the
switch that it is installed on, except that the chipset architecture must be either x86_64 or arm:

n 8100 (x86_64)

n 8320 (x86_64)

n 8325 (x86_64)

n 8360 (arm)

n 9300 (x86_64)

n 10000 (x86_64)

The HPE Aruba Networking CX vSphere agent is a containerized agent developed for data center applications.

The plugin consumes memory and CPU that would otherwise be allocated to the switch. Thus, the targeted

platforms have higher system resources. Those resources are capped to prevent its interference with

performance of the switch.

The solution was tested and qualified on the platforms listed here. Other platforms may work at low scale, but

they are not recommended outside of the labor test environments due to the resource requirements for

vSphere.

Troubleshooting

Overview

In data center networking, the most advanced step in troubleshooting often involves directly accessing
the closest physical device related to the issue at hand. This trouble shooting mechanism allows the
diagnosis of problems with connected endpoints. While administrators can use management tools to
avoid accessing the physical device, there are scenarios where the tools are not utilized. The lack of
utilization is either due to their absence, do not have of familiarity, or some of the administrators prefer
device interaction. To address this, it is important to embrace these variations and aim for better
integration between device-based approaches and management tools, rather than viewing them as
conflicting options.

The complexity of troubleshooting the devices is multiplied by the dynamically varying endpoints within
the data center. To troubleshoot, admins might extensively research endpoint metadata before
beginning the process. Customers use different methods to store inventory data about their endpoints.
This method can result in searching for incorrect or outdated information, causing confusion.

vSphere agent | 248

Additionally,adminsmaystruggletoidentifythecorrectnetworkdevicetostartwithormakemistakes
intheprocess.
Understandingthereasonsbehindenteringthe"Troubleshootingoflastresort"scenarioisessentialfor
developingmoreeffectivesolutions.Often,thisscenarioariseseitherduetoreportedconnectivity
problemsorwhenadminsattempttoestablishconnectivityforanewdeviceorservice.Interestingly,
thefirststepinthisscenarioistoresorttothelastoptionisaskingaseriesofquestionsaboutMAC
addresses,IPaddresses,switches,ports,andmore.Usersfrequentlydonothavethisinformationand
mustlookitupfromspreadsheets,paperrecords,oroutdatedinventorysystems.
| Troubleshooting | Tools |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
AdminscanuseMACtables,ARPtables,andpingandtracetoolstotroubleshoottheissues.Youcan
runtheshowmac-address-tablecommandtotroubleshoot:
cedar-sw-01# show mac-address-table MAC age-time : 300 seconds Number of
| MAC addresses     | : 15 |      |         |        |     |
| ----------------- | ---- | ---- | ------- | ------ | --- |
| MAC Address       | VLAN | Type | Port    |        |     |
| f4:03:43:d3:be:b8 |      | 1    | dynamic | 1/1/4  |     |
| f4:03:43:c0:e1:38 |      | 1    | dynamic | lag256 |     |
| f4:03:43:c0:e1:30 |      | 1    | dynamic | lag2   |     |
| 00:50:56:5e:7a:69 |      | 1    | dynamic | lag1   |     |
| 00:50:56:5b:a0:40 |      | 1    | dynamic | lag1   |     |
| 04:90:81:00:08:a2 |      | 10   | dynamic | lag256 |     |
TheMACaddresstablehelpsyoutocheckifyouhaveseentheMACaddressoftheendpointinthelast
5minutes.IftheuserdoesnotreportaproblemorsharetheMACaddress,findouttheMACaddress
usedbytheendpoint.However,ifthedevicehasmanyvirtualnetworkpartssuchasswitches,itcanbe
unclearwhichMACitisusing.
Youcanalsoruntheshowarpcommandtotroubleshoottheissue.
show arp
| cedar-sw-01# | show arp          | all-vrfs |               |                  |         |
| ------------ | ----------------- | -------- | ------------- | ---------------- | ------- |
| IPv4 Address | MAC               | Port     | Physical Port | State VRF        |         |
| 10.10.3.23   | 00:50:56:ac:3d:c6 |          | vlan30        | lag1 reachable   | default |
| 1.1.1.12     | 04:90:81:00:08:a2 |          | vlan99        | lag256 reachable | default |
| 1.1.1.1      | 04:90:81:00:08:a2 |          | 1/1/48        | 1/1/48 reachable | default |
ForthefollowingMACaddress04:90:81:00:08:a2,theoutputshowsthattherewasanARPrequestfor
thisMACaddress.ThedevicewithIPV4address1.1.1.1istheVSXkeepaliveinterfaceonthepeerswitch.
Endpoint metadata
Solvingtheissueinvolvesgettingthemetadatarightdowntotheswitch.Whenusersusespecific
commands,wecanaddextradetailstotheresponsesusingmetadata.Forinstance,ifweknowthatthe
IPaddress1.1.1.1correspondstoauserVMnamed"Simon,"wemustincludethatinformationinthe
output.
| show arp (decoration) |          |          |     |     |     |
| --------------------- | -------- | -------- | --- | --- | --- |
| cedar-sw-01#          | show arp | all-vrfs |     |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 249

IPv4 Address

MAC

Port

Physical Port

State

VRF

10.10.3.23
1.1.1.12
1.1.1.1 (simons-vm)

00:50:56:ac:3d:c6 vlan30
04:90:81:00:08:a2 vlan99

lag1
reachable default
lag256 reachable default

04:90:81:00:08:a2 1/1/48

1/1/48

reachable default

The previous example is generic, to show the value of extra meta-data on standard switch screens, but
in the vSphere context we have to research further to get more useful results.

VMware Use Cases

If you focus only on physical devices, you must figure out the specific switch to which your endpoint is
connected. Other switches in the network might not have complete data about the endpoint, so they
might not provide any information. In this scenario, more advanced data and perspectives become
valuable for our administrators. By using VMware vSphere data as a foundation for your metadata, you
gain a broader range of information beyond individual switches. You acquire a comprehensive set of
data about topology of the fabric and endpoints. Operators use this information without requiring them
to know the precise location of the endpoints.

Following queries that users might perform to gather more information about the endpoint:

Where can I find this endpoint (whether it is a virtual machine, VMkernel, or host)?

You might have a differing set of data on the endpoint, depending on their situation, and they want to
know where it resides based on the limited information they have.

Create this query with a flexible set of data:

n VMs name, DNS name (can be different from VM name), VMs IP (more than one IP is possible), VMs

NIC name (VMs version, not ESXi), VMs MAC

VMkernel looks like a VM in some ways, just a virtual interface used for some important VMware
control functions such as vMotion

n ESXi name, DNS name (often the same as ESXi name), IP, vmnic, vmnic MAC

What does the user want in response to their query?

n Switch, LAG , or Interface endpoint last seen

n When it was last seen

n Previous location (can be useful for detecting loops), will move if vMotion or depending on vmware

load balancing

What additional data is available for this endpoint?

There is additional metadata for vSphere on the endpoint that can be useful for the customer. For a
complete integration and for full visualization and automation, this data is used and is applied to Switch
CLI.

For VMs

n The basic inventory data on this VM

o VMs name, DNS name (often different from VM name), VMs IP (they can have more than one),

VMs NIC name (VMs version, not ESXi), VMs MAC

oo The VMs association with the Virtual network in ESXi/vsphere

n Portgroup (VLAN, VLAN type), vSwitch, ESXi Host, ESXi Host NIC (name, IP, and MAC)

vSphere agent | 250

n ForVMkernel
o BasicinventorydataonthisVMkernel
| l Name,IP,MAC |     |     |     |     |
| ------------- | --- | --- | --- | --- |
o TheVMKsassociationwiththeVirtualnetworkinESXiorvsphere
Portgroup(VLAN,VLANtype),vSwitch,ESXiHost,ESXiHostNIC(name,IP,andMAC)
l
n ForESXi
o Thebasicinventorydataonthis
| l ESXiname,DNSname,ESXiIP,ESXiNics,andMACs |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- |
ForeachESXiNIC,theassociationwithvSwitch
l
| What devices | are | connected | to this | port? |
| ------------ | --- | --------- | ------- | ----- |
Youcanrunshowmac-table-addressinterfacex/t/zcommand,todisplayactiveMACs.
TheadvantageofusingVMmetadataisthatyoucanfindoutthelocationoftheVMwithoutactive
MACs.YoucanfindouttheportgrouporvSwitchlocationthroughLLDPfromthehost,andfromtheVM
associationyoucanfindoutthelocationoftheswitchport.
Tothisend,theshowVMsinterfacex/t/zcouldrespondwithamixofactiveandinactiveVMs.
| Container | management |     |     | commands |
| --------- | ---------- | --- | --- | -------- |
container
| container    | <CONTAINER-NAME> |     |     |     |
| ------------ | ---------------- | --- | --- | --- |
| no container | <CONTAINER-NAME> |     |     |     |
Description
Entersintothecontainerconfigurationcontext.
Thenoformofthiscommandremovestheexistingconfigurationsofthespecifiedcontainer.
Example
Configuresanewcontainer:
| switch(config)# |     | container | app |     |
| --------------- | --- | --------- | --- | --- |
The feature being used requires a AOS-CX Advanced Software Feature Pack.
For more information,refer to the AOS-CX Feature Pack Deployment Guide.
AOS-CXdoesnotenforcetherequirementtoownafeaturepackpriortousingcontainerfeatures.This
warningmessageisdisplayedonlyduringcreation,subsequentcallstothecontainercontextwillnot
displaythemessage.
AOS-CX10.14ReleaseUpdate:ContainerUpdates
| Command | History     |     |     |                   |
| ------- | ----------- | --- | --- | ----------------- |
| Release |             |     |     | Modification      |
| 10.12   |             |     |     | Commandintroduced |
| Command | Information |     |     |                   |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 251

| Platforms | Command | context |     | Authority                             |
| --------- | ------- | ------- | --- | ------------------------------------- |
| 8400      | config  |         |     | Administratorsorlocalusergroupmembers |
config-container-<CONTAINER-NAME> withexecutionrightsforthiscommand.
env
env <NAME> {value <VALUE>}|{encrypted [plaintext <VALUE>|ciphertext <VALUE>]}
no env <NAME> {value <VALUE>}|{encrypted {plaintext|ciphertext}<VALUE>}
Description
Configuresanenvironmentvariableforacontainerthatiscomposedofakeyandavaluepair.Thekey-
valuepairdefinesthebehavioroftheenvironmentinacontainerandisusedbythecontainer
processes.Thevalueoftheenvironmentvariablecanbestoredinthehostsystemasanencrypted
value.Thecontainermanagerinfrastructureprovidesthedecryptedvaluetothecontainer.
Thenoformofthiscommandremovestheconfiguredenvironmentvariablefromacontainer.
Configuringtheenvvariableforanalreadyoperationalcontainercausesthecontainertorestart.
| Parameter     |     |     | Description                                         |     |
| ------------- | --- | --- | --------------------------------------------------- | --- |
| <NAME>        |     |     | Specifiesthenameofthecontainerenvironmentvariables. |     |
| value <VALUE> |     |     |                                                     |     |
Specifiesthevariablevalue.
encrypted
Encryptstheenvironmentvariablevalue.Ifyoupress
<enter>aftertheencryptedparameter,youwillentera
variableconfigurationmodethatallowsyoutosecurely
enterahiddenvalue.Thisistherecommendedmethodfor
enteringanencryptedvariable
| plaintext | <VALUE> |     |     |     |
| --------- | ------- | --- | --- | --- |
Optional.Specifiesthevariablevalueinplaintext.Not
recommendedforencryptedvariables.
| ciphertext | <VALUE> |     |     |     |
| ---------- | ------- | --- | --- | --- |
Optional.Specifiesthevariablevalueaspreviously
encryptedtext.Recommendedforencryptedvariables;specify
theencryptedvariablevalueaspreviouslyencryptedtext.
Example
Securelyenteringanencryptedvariable:
| 6300(config-container-test)# |          | env    | TEST encrypted |     |
| ---------------------------- | -------- | ------ | -------------- | --- |
| Enter environment            | variable | value: | ********       |     |
| 6300(config-container-test)# |          | end    |                |     |
| Command History              |          |        |                |     |
vSphereagent|252

Release

10.13.1000

Modification

The plaintext and ciphertext options for the encrypted
parameter are now optional. Starting with this release, you can
use the encrypted option to encrypt the environment variable
and specify the value in plaintext hidden from the CLI.

10.12

Command introduced

Command Information

Platforms

Command context

Authority

8400

config-container-<CONTAINER-NAME>

Administrators or local user group members
with execution rights for this command.

container exec
container <NAME> exec <PARAMS>

Description

Allows the execution of an endpoint script in the container. The location of this endpoint is provided to
the container manager infrastructure through a manifest file in the image file system of the container.
This manifest file provides metadata related to the container application. When the exec command
runs, the manifest information is used to determine the endpoint to execute and the user parameters
are passed directly to the endpoint. The output of such execution is provided directly to the user
through the CLI. In case the manifest information or the endpoint file are missing an error is presented
to the user. User can interrupt the execution by using Ctrl+C.

If the container is not operational when the command is executed, the following error message is returned:

Failed to execute endpoint - The container is not operational.

Parameter

Description

<NAME>

exec

<PARAMS>

Command History

Release

10.12

Command Information

Specifies a container name up to 64 characters long.

Runs a container application command.

Specifies container command parameters.

Modification

Command introduced

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

253

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8400 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.
image-download-vrf
| image-download-vrf    | <VRF-NAME> |            |     |
| --------------------- | ---------- | ---------- | --- |
| no image-download-vrf |            | <VRF-NAME> |     |
Description
Reservedforfutureuse.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.12 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8400 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.
image-location
| image-location    | <URL> [vrf | <VRF-NAME>][allow-unsigned]  |     |
| ----------------- | ---------- | ---------------------------- | --- |
| no image-location | <URL>      | [<VRF-NAME>][allow-unsigned] |     |
Description
Configurestheimagelocationforacontainer.Modifyingimagelocationpromptsanimageupgrade.
Thenoformofthiscommandremovestheconfiguredlocationofacontainer.
n IftheusersetsalocationvaluewhichdoesnotfollowthestandardURLformat,thefollowingerrormessage
isreturned:Failuretoconfigureimagelocation:InvalidURL
n IftheusertriestouseaVRFvaluethatdoesn'texistontheswitch,thefollowingerrormessageisreturned:
Failuretoconfigureimagelocation:InvalidVRF
n Iftheimageofthecontainerexceeds500mbthecontainerwon´tbedeployed.
Bydefault,onlycontainerimageswithavalidHPEsignatureareallowed.Tobypassthissignaturecheck
andallowunsignedcontainerimages,includetheallow-unsignedparameterwhenyoudefinethe
imagelocation.Theallow-unsignedparametercannotbeusedifyouhaveissuedthesecure-mode
enhancedcommandtosettheswitchtoenhancedsecuremode.
vSphereagent|254

Parameter

image-location

URL

vrf <VRF-NAME>

allow-unsigned

Examples

Description

Configures the URL of the container application.

Specifies the URL of the container application. URL supports HTTP
protocol. The image-location URL can either be IPv4 or IPv6
address. The IPv6 address must be provided within square
brackets.

(Optional) Specifies the VRF of the image URL.

(Optional) Allow download and deployment of an unsigned
container image.

Configures the image location for the IPv4 setting:

switch(config)# image-location http://10.0.0.1/container.img vrf mgmt

Appends the port to the address if the image server is running on a port other than HTTP for an IPv4
setting:

switch(config)# image-location http://10.0.0.1:9050/container.img vrf mgmt

Configures image location for IPv6 setting by wrapping IP address between square brackets:

switch(config)# image-location http://[2001::2]/container.img vrf mgmt

Specifies port number by appending it with the IPv6 address:

switch(config)# image-location http://[2001::2]:9050/container.img vrf mgmt

When you include the allow-unsigned parameter on a switch in standard secure mode, the following
message will be displayed to inform this can be a potential security issue.

switch(config)# image-location http://10.0.0.1/container.img vrf mgmt allow-
unsigned
Allowing unsigned container images poses a potential security risk
that can impact both the current device and the entire network. By
allowing installation of unsigned applications you are acknowledging
and accepting these risks. HPE shall not be responsible for the
consequences of your actions and disclaims any and all liability.

Continue (y/n)? y

When you attempt to include the allow-unsigned parameter on a switch in enhanced ecure mode, the
following message will appear to indicate that this parameter is not supported.

switch(config)# image-location http://10.0.0.1/container.img vrf mgmt allow-
unsigned

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

255

Unsigned images are not permitted in the current secure mode, using the
| allow-unsigned      | parameter | will have | no effect.                              |           |
| ------------------- | --------- | --------- | --------------------------------------- | --------- |
| Release             |           |           | Modification                            |           |
| 10.14               |           |           | Theallow-unsignedparameterisintroduced. |           |
| 10.12               |           |           | Commandintroduced.                      |           |
| Command Information |           |           |                                         |           |
| Platforms           | Command   | context   |                                         | Authority |
8400 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.
| restrict cpu |              |     |     |     |
| ------------ | ------------ | --- | --- | --- |
| restrict cpu | <PERCENTAGE> |     |     |     |
| no restrict  | cpu          |     |     |     |
Description
ConfigureslimitationsforthecontainerCPUusage.TheCPUconstraintissetasapercentageofthe
totalswitchCPUs.Acontainercanuseupto20%ofthetotalCPUcapacityofthedevice.
ConfiguringtheCPUconstraintforanalreadyoperationalcontainerwillcausethecontainertorestart.
ThenoformofthiscommandremovesrestrictionsontheCPU usage.
| Parameter    |     |     | Description                                    |     |
| ------------ | --- | --- | ---------------------------------------------- | --- |
| <PERCENTAGE> |     |     | SpecifiespercentageforthecontainerCPUusage,The |     |
defaultvalueis10%.
| Command History     |         |         |                   |           |
| ------------------- | ------- | ------- | ----------------- | --------- |
| Release             |         |         | Modification      |           |
| 10.12               |         |         | Commandintroduced |           |
| Command Information |         |         |                   |           |
| Platforms           | Command | context |                   | Authority |
8400 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.
| restrict memory |        |     |     |     |
| --------------- | ------ | --- | --- | --- |
| restrict memory | <MB>   |     |     |     |
| no restrict     | memory |     |     |     |
vSphereagent|256

Description
Configureslimitationsformemoryusageofthecontainer.ThememoryconstraintissetinMB,andthe
maximum20%ofthecapacityofthedevicecanbeconfigured.Configuringthememoryconstraintfor
analreadyoperationalcontainerrestartsthecontainer.
Thenoformofthiscommandremovesrestrictionsonthememoryusage.
Parameter Description
<MB> SpecifiesthemaximummemoryusageinMB.Thedefault
valueis256MB.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.12 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-container-<CONTAINER-NAME>
| 8400 |     |     | Administratorsorlocalusergroupmembers |
| ---- | --- | --- | ------------------------------------- |
withexecutionrightsforthiscommand.
| restrict storage |         |     |     |
| ---------------- | ------- | --- | --- |
| restrict storage | <MB>    |     |     |
| no restrict      | storage |     |     |
Description
ConfigureslimitationsofcontainerstorageusagespecifiedinMB.Therangeis1MB-4096MB.Default
valueis512MB.
Thenoformofthiscommandremovesrestrictionsontheusageofstorage.
Parameter Description
<MB> ConfiguresthemaximumstorageusageinMB.Thedefault
valueis512MB.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.12 Commandintroduced
| Command Information |     |     |     |
| ------------------- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 257

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
8400 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.
show container
| show container | [<CONTAINER-NAME>] |     |     |     |
| -------------- | ------------------ | --- | --- | --- |
Description
Showstheconfigurationandstatusinformationofthecontainersrunninginthesystem.Ifthecontainer
nameisnotspecified,displaysinformationofallthecontainers.Whenacontainernameisspecified,
displaysinformationspecifictothecontainer.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<CONTAINER-NAME>
Specifiesthenameofthecontainerforwhichinformation
needtobespecified.
Examples
Thefollowingexampleshowsconfiguredcontainerinformation:
| switch#     | show container |                                          |     |     |
| ----------- | -------------- | ---------------------------------------- | --- | --- |
| Container   |                | : app                                    |     |     |
| Container   | status         | : operational                            |     |     |
| Manifest    | status         | : success                                |     |     |
| Image       | status         | : verified                               |     |     |
| Image       | version        | : 1.0.0                                  |     |     |
| Image       | location       | VRF : mgmt                               |     |     |
| Image       | location       | URL : http://30.0.0.2:8000/container.img |     |     |
| CPU limit   |                | : 10%                                    |     |     |
| Memory      | limit          | : 512                                    | MB  |     |
| VRFs        |                | : mgmt                                   |     |     |
| Environment | variables:     |                                          |     |     |
PYP=/usr/bin/python3
| Encrypted | environment | variables: |     |     |
| --------- | ----------- | ---------- | --- | --- |
encryptedVar1
encryptedVar2
Thefollowingexampleshowsadditionalerrormessages:
switch#
show container
| Container |        | : app           |        |     |
| --------- | ------ | --------------- | ------ | --- |
| Container | status | : configuration | failed |     |
Config failure reason : Multiple definitions of environment variable PYP
| Manifest       | status        | : error                              |                |              |
| -------------- | ------------- | ------------------------------------ | -------------- | ------------ |
| Manifest       | status reason | : 'exec'                             | file not found | in container |
| Image status   |               | : verified                           |                |              |
| Image version  |               | : 1.0.0                              |                |              |
| Image location | VRF           | : mgmt                               |                |              |
| Image location | URL           | : http://30.0.0.2:8000/container.img |                |              |
| CPU limit      |               | : 10%                                |                |              |
| Memory         | limit         | : 512                                | MB             |              |
| VRFs           |               | : mgmt                               |                |              |
vSphereagent|258

| Environment | variables | :   |     |
| ----------- | --------- | --- | --- |
PYP=/usr/bin/python3
| Encrypted | environment | variables: |     |
| --------- | ----------- | ---------- | --- |
PYP
encryptedVar2
Thefollowingexampleshowsaconfiguredcontainerwithoutsignaturevalidation:
| switch# show   | container  | app1                                 |                   |
| -------------- | ---------- | ------------------------------------ | ----------------- |
| Container      |            | : app1                               |                   |
| Container      | status     | : operational                        |                   |
| Manifest       | status     | : success                            |                   |
| Image status   |            | : allowed                            | without signature |
| Image version  |            | : 1.0.0                              |                   |
| Image location | VRF        | : mgmt                               |                   |
| Image location | URL        | : http://30.0.0.2:8000/container.img |                   |
| CPU limit      |            | : 10%                                |                   |
| Memory         | limit      | : 512 MB                             |                   |
| Environment    | variables: |                                      |                   |
PYP=/usr/bin/python3
| Encrypted | environment | variables: |     |
| --------- | ----------- | ---------- | --- |
encryptedVar1
encryptedVar2
Network:
| VRF name  | : mgmt    |     |     |
| --------- | --------- | --- | --- |
| Preferred | : no      |     |     |
| Port      | map : n/a |     |     |
| VRF name  | : default |     |     |
| Preferred | : yes     |     |     |
| Port      | map :     |     |     |
8080:80/tcp
8080:8080/udp
Thefollowingexampleshowsthecommandoutwhentherearenoconfiguredcontainers:
| switch# show        | container  |         |                                                      |
| ------------------- | ---------- | ------- | ---------------------------------------------------- |
| No containers       | configured |         |                                                      |
| Command History     |            |         |                                                      |
| Release             |            |         | Modification                                         |
| 10.12               |            |         | Commandintroduced                                    |
| Command Information |            |         |                                                      |
| Platforms           | Command    | context | Authority                                            |
| 8400                |            |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show capacities | containers |     |     |
| --------------- | ---------- | --- | --- |
| show capacities | containers |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 259

Description
Showsthemaximumnumberofcontainerizedapplicationsthatcanbeconfiguredinthesystem.
Examples
Showsmaximumnumberofcontainerizedapplicationsthatcanbeconfigured:
| switch#            | show capacities | containers        |     |       |
| ------------------ | --------------- | ----------------- | --- | ----- |
| System Capacities: |                 | Filter CONTAINERS |     |       |
| Capacities         | Name            |                   |     | Value |
----------------------------------------------------------------------------------
----
Maximum number of containerized applications configurable in the system 2
2
| Command   | History     |         |                   |     |
| --------- | ----------- | ------- | ----------------- | --- |
| Release   |             |         | Modification      |     |
| 10.12     |             |         | Commandintroduced |     |
| Command   | Information |         |                   |     |
| Platforms | Command     | context | Authority         |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show capacities-status |     | containers |     |     |
| ---------------------- | --- | ---------- | --- | --- |
| show capacities-status |     | containers |     |     |
Description
Reservedforfutureuse.
| Command   | History     |         |                   |     |
| --------- | ----------- | ------- | ----------------- | --- |
| Release   |             |         | Modification      |     |
| 10.12     |             |         | Commandintroduced |     |
| Command   | Information |         |                   |     |
| Platforms | Command     | context | Authority         |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show running-config |           | container |     |     |
| ------------------- | --------- | --------- | --- | --- |
| show running-config | container |           |     |     |
vSphereagent|260

Description
Showstherunningconfigurationofallthecontainers.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
container
Specifiesthatcontainerrunningconfigurationmustbe
displayed.
Examples
Showstherunningconfigurationforthecontainer:
| container         | app1                   |                                    |            |          |
| ----------------- | ---------------------- | ---------------------------------- | ---------- | -------- |
| image-location    |                        | http://30.0.0.2:8000/container.img |            | vrf mgmt |
| restrict          | cpu 10                 |                                    |            |          |
| restrict          | memory                 | 512                                |            |          |
| vrf attach        | mgmt                   |                                    |            |          |
| env PYP           | value /usr/bin/python3 |                                    |            |          |
| env encryptedVar1 |                        | encrypted                          | ciphertext |          |
AQBapcmUTCVdagTGkLA3m6NsslLgNOdxqUP0j+CCaCxVdz7oEwAAAOmmBmgPHGavS+6GkgmtwE4NU1Y=
| container | app2 |     |     |     |
| --------- | ---- | --- | --- | --- |
image-location http://[2001::2]:8000/changeValidation_x86_t.img vrf mgmt
| restrict          | cpu 5                  |           |            |     |
| ----------------- | ---------------------- | --------- | ---------- | --- |
| restrict          | memory                 | 256       |            |     |
| vrf attach        | mgmt                   |           |            |     |
| env PYP           | value /usr/bin/python3 |           |            |     |
| env encryptedVar1 |                        | encrypted | ciphertext |     |
AQBapcmUTCVdagTGkLA3m6NsslLgNOdxqUP0j+CCaCxVdz7oEwAAAOmmBmgPHGavS+6GkgmtwE4NU1Y=
| env encryptedVar2 |     | encrypted | ciphertext |     |
| ----------------- | --- | --------- | ---------- | --- |
AQBapY4V4v9UtDaazZaaJMeROhUizlVYVrTKKpa1N1bABTYICQAAACiXj/d3ZtBSYg==
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.12               |         |         | Commandintroduced |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
vrf
vrf <VRF-NAME>
Description
AllowscontainerL3connectivityusingthegivenVRF.Thecontainernetworknamespaceisconnectedto
theVRFusingthesourceNAT.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 261

Parameter Description
<VRF-NAME> SpecifiestheVRF-NAMEusedbythecontainerapplication.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.12 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8400 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.
vSphereagent|262

Chapter 14
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
263
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries)

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
Switchsystemandhardwarecommands|264

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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 265

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
Switchsystemandhardwarecommands|266

domain-name
| domain-name    | <NAME>   |     |     |
| -------------- | -------- | --- | --- |
| no domain-name | [<NAME>] |     |     |
Description
Specifiesthedomainnameoftheswitch.
Thenoformofthiscommandsetsthedomainnametothedefault,whichisnodomainname.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<NAME> Specifiesthedomainnametobeassignedtotheswitch.Thefirst
characterofthenamemustbealetteroranumber.Length:1to
32characters.
Examples
Settingandshowingthedomainname:
| switch# show    | domain-name |             |     |
| --------------- | ----------- | ----------- | --- |
| switch# config  |             |             |     |
| switch(config)# | domain-name | example.com |     |
| switch(config)# | show        | domain-name |     |
example.com
switch(config)#
Settingthedomainnametothedefaultvalue:
| switch(config)# | no   | domain-name |     |
| --------------- | ---- | ----------- | --- |
| switch(config)# | show | domain-name |     |
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| fabric admin-state |             |     |     |
| ------------------ | ----------- | --- | --- |
| fabric <SLOT-ID>   | admin-state |     |     |
diagnostic
down
up
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 267

Description
Setstheadministrativestateofthespecifiedfabricmodule.
| Parameter |     |     | Description                                        |
| --------- | --- | --- | -------------------------------------------------- |
| <SLOT-ID> |     |     | Specifiesthememberandslotofthemodule.Forexample,to |
specifythemoduleinmember1,slot2,enterthefollowing:
1/2
diagnostic
Selectsthediagnosticadministrativestate.Networktrafficdoes
notpassthroughthemodule.
| down |     |     | Selectsthedownadministrativestate.Networktrafficdoesnot |
| ---- | --- | --- | ------------------------------------------------------- |
passthroughthemodule.
| up  |     |     | Selectstheupadministrativestate.Themoduleisfully |
| --- | --- | --- | ------------------------------------------------ |
operational.Theupstateisthedefaultadministrativestate.
Usage
Thiscommandisvalidforfabricmodulesonly.
Examples
Settingtheadministrativestateofthefabricmodule2todown:
switch(config)#
|                     | fabric  | 1/2 admin-state | down         |
| ------------------- | ------- | --------------- | ------------ |
| Command History     |         |                 |              |
| Release             |         |                 | Modification |
| 10.07orearlier      |         |                 | --           |
| Command Information |         |                 |              |
| Platforms           | Command | context         | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
hostname
hostname <HOSTNAME>
| no hostname | [<HOSTNAME>] |     |     |
| ----------- | ------------ | --- | --- |
Description
Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
Switchsystemandhardwarecommands|268

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
led locator
on
off
flashing
slow_blink
fast_blink
half_bright
no...
Description
SetsthestateofthelocatorLED.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 269

| Parameter   |     |     |     |     | Description                            |     |
| ----------- | --- | --- | --- | --- | -------------------------------------- | --- |
| on          |     |     |     |     | TurnsontheLED.                         |     |
| off         |     |     |     |     | TurnsofftheLED,whichisthedefaultvalue. |     |
| flashing    |     |     |     |     | SetstheLEDtoblinkonandoffrepeatedly.   |     |
| slow_blink  |     |     |     |     | SetstheLEDtoslowblinkonandoff.         |     |
| fast_blink  |     |     |     |     | SetstheLEDtofastblinkonandoff.         |     |
| half_bright |     |     |     |     | SetstheLEDintensitytohalfbright.       |     |
| no          |     |     |     |     | Negatesanyconfiguredparameter          |     |
Example
SettingthestateofthelocatorLED:
| switch# | led     | locator |     | flashing |                                                      |     |
| ------- | ------- | ------- | --- | -------- | ---------------------------------------------------- | --- |
| Command | History |         |     |          |                                                      |     |
| Release |         |         |     |          | Modification                                         |     |
| 10.13   |         |         |     |          | StartingwithAOS-CX10.13,thiscommandwillnottakeeffect |     |
whenitissenttotheswitchfromHPEArubaNetworkingCentral.
| 10.07orearlier |             |         |     |         | --  |           |
| -------------- | ----------- | ------- | --- | ------- | --- | --------- |
| Command        | Information |         |     |         |     |           |
| Platforms      |             | Command |     | context |     | Authority |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| module    |           | admin-state |              |             |             |               |
| --------- | --------- | ----------- | ------------ | ----------- | ----------- | ------------- |
| module    | <SLOT-ID> |             | admin-state  | {diagnostic |             | | down | up}  |
| no module | <SLOT-ID> |             | [admin-state |             | [diagnostic | | down | up]] |
Description
Setstheadministrativestateofthespecifiedlinemodule.
Thenoformofthecommandconfiguresadministrativestatetothedefaultup.
| Parameter |     |     |     |     | Description                                        |     |
| --------- | --- | --- | --- | --- | -------------------------------------------------- | --- |
| <SLOT-ID> |     |     |     |     | Specifiesthememberandslotofthemodule.Forexample,to |     |
specifythemoduleinmember1,slot3,enterthefollowing:
1/3
Switchsystemandhardwarecommands|270

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
diagnostic Selectsthediagnosticadministrativestate.Networktrafficdoes
notpassthroughthemodule.
down
Selectsthedownadministrativestate.Networktrafficdoesnot
passthroughthemodule.
| up  |     |     |     |     | Selectstheupadministrativestate.Thelinemoduleisfully |
| --- | --- | --- | --- | --- | ---------------------------------------------------- |
operational.Theupstateisthedefaultadministrativestate.
Example
Settingtheadministrativestateofthemoduleinslot1/3todown:
| switch(config)# |             | module  | 1/3     | admin-state | down         |
| --------------- | ----------- | ------- | ------- | ----------- | ------------ |
| Command         | History     |         |         |             |              |
| Release         |             |         |         |             | Modification |
| 10.07orearlier  |             |         |         |             | --           |
| Command         | Information |         |         |             |              |
| Platforms       |             | Command | context |             | Authority    |
config
| 8400 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | --- | --- | -------------------------------------------------- |
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 271

Parameter

Description

If there is no line module installed in the slot when you execute
this command, <PRODUCT-NUM> is required.

Usage

The default configuration associated with a line module slot is:

n There is no module product number or interface configuration information associated with the slot.

The slot is available for the installation with any supported line module.

n The Admin State is Up (which is the default value for Admin State).

To add a line module to the configuration, you must use the module command either before or after
you install the physical module.

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

Switch system and hardware commands | 272

Attemptingtoconfigureslot1/1forthefutureinstallationofalinemodulewithoutspecifyingthe
productnumber(returnederrorshown):
| switch(config)# |     | module | 1/1 | product-number |     |     |
| --------------- | --- | ------ | --- | -------------- | --- | --- |
Line module '1/4' is not physically available. Please provide the product
| number | to preconfigure |     | the | line | module. |     |
| ------ | --------------- | --- | --- | ---- | ------- | --- |
ConfiguringaJL363Alinemoduleinaslotthathasalreadybeenusedtoconfigureadifferentmodule:
| switch(config)# |     | no     | module | 1/4            |     |        |
| --------------- | --- | ------ | ------ | -------------- | --- | ------ |
| switch(config)# |     | module | 1/4    | product-number |     | jl363a |
Removingamodulefromtheconfiguration:
switch(config)#
|     |     | no  | module | 1/1 |     |     |
| --- | --- | --- | ------ | --- | --- | --- |
This command will power cycle the specified line module and restore its default
configuration. Any traffic passing through the line module will be interrupted.
Management sessions connected through the line module will be affected. It
| might take | a       | few minutes |     | to complete | this | operation. |
| ---------- | ------- | ----------- | --- | ----------- | ---- | ---------- |
| Do you     | want to | continue    |     | (y/n)?      | y    |            |
switch(config)#
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
mtrace
mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
[vrf <VRF-NAME>]
Description
TracesthespecifiedIPv4sourceandgroupaddresses.
| Parameter     |     |     |     |     | Description                           |     |
| ------------- | --- | --- | --- | --- | ------------------------------------- | --- |
| IPV4-SRC-ADDR |     |     |     |     | SpecifiesthesourceIPv4addresstotrace. |     |
IPV4-GROUP-ADDR
SpecifiesthegroupIPv4addresstotrace.
lhr <IPV4-LHR-ADDR> Specifiesthelasthoprouteraddressfromwhichtostartthetrace.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 273

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
ttl <HOPS> SpecifiestheTime-To-Livedurationinhops.Range:1to255hops.
Default:8hops.
vrf <VRF-NAME>
SpecifiesthenameoftheVRF.Ifanameisnotspecifiedthe
defaultVRFwillbeused.
Examples
Tracingwithsource,group,andLHRaddressesandTTL:
(switch)#
|                     | mtrace        | 20.0.0.1 | 239.1.1.1 |          | lhr | 10.1.1.1 | ttl 10          |
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
| power | consumption-average-period |     |     |     |     |     |     |
| ----- | -------------------------- | --- | --- | --- | --- | --- | --- |
Switchsystemandhardwarecommands|274

| power consumption-average-period |     | <PERIOD-IN-SECONDS> |     |     |
| -------------------------------- | --- | ------------------- | --- | --- |
Description
Configuresatimeperiodforaveragepowerconsumptioninseconds.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PERIOD-IN-SECONDS> Specifiestheperiodinsecondsforaveragepowerconsumed.
Range:60-3600.Default:600
Example
Configuringatimeperiodof60secondsforaveragepowerconsumption:
| switch(config)#     | power   | consumption-average-period |                    | 60  |
| ------------------- | ------- | -------------------------- | ------------------ | --- |
| Command History     |         |                            |                    |     |
| Release             |         |                            | Modification       |     |
| 10.13               |         |                            | Commandintroduced. |     |
| Command Information |         |                            |                    |     |
| Platforms           | Command | context                    | Authority          |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show bluetooth
show bluetooth
Description
ShowsgeneralstatusinformationabouttheBluetoothwirelessmanagementfeatureontheswitch.
Usage
Thiscommandshowsstatusinformationaboutthefollowing:
n TheUSBBluetoothadapter
n ClientsconnectedusingBluetooth
n TheswitchBluetoothfeature.
Theoutputoftheshow running-configcommandincludesBluetoothinformationonlyiftheBluetooth
featureisdisabled.
Thedevicenamegiventotheswitchincludestheswitchserialnumbertouniquelyidentifytheswitch
whilepairingwithamobiledevice.
ThemanagementIPaddressisaprivatenetworkaddresscreatedformanagingtheswitchthrougha
Bluetoothconnection.
Examples
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 275

ExampleoutputwhenBluetoothisenabledbutnoBluetoothadapterisconnected.<XXXX>istheswitch
platformand<NNNNNNNNNN>isthedeviceidentifier.
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : Yes                 |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
| Adapter     | State          | : Absent              |     |     |     |
ExampleoutputwhenBluetoothisenabledandthereisaBluetoothadapterconnected:
| switch#     | show bluetooth |                 |     |     |     |
| ----------- | -------------- | --------------- | --- | --- | --- |
| Enabled     |                | : Yes           |     |     |     |
| Device name |                | : <XXXX>-       |     |     |     |
| Adapter     | State          | : Ready         |     |     |     |
| Adapter     | IP address     | : 192.168.99.1  |     |     |     |
| Adapter     | MAC address    | : 480fcf-af153a |     |     |     |
| Connected   | Clients        |                 |     |     |     |
-----------------
| Name | MAC | Address | IP Address | Connected | Since |
| ---- | --- | ------- | ---------- | --------- | ----- |
-------------- -------------- ------------ ------------------------
Mark's iPhone 089734-b12000 192.168.99.10 2018-07-09 08:47:22 PDT
ExampleoutputwhenBluetoothisdisabled:
| switch#        | show bluetooth |                       |                                                      |     |     |
| -------------- | -------------- | --------------------- | ---------------------------------------------------- | --- | --- |
| Enabled        |                | : No                  |                                                      |     |     |
| Device name    |                | : <XXXX>-<NNNNNNNNNN> |                                                      |     |     |
| Command        | History        |                       |                                                      |     |     |
| Release        |                |                       | Modification                                         |     |     |
| 10.07orearlier |                |                       | --                                                   |     |     |
| Command        | Information    |                       |                                                      |     |     |
| Platforms      | Command        | context               | Authority                                            |     |     |
| 8400           |                |                       | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show boot-history |           |        |          |     |     |
| ----------------- | --------- | ------ | -------- | --- | --- |
| show boot-history | [all|{vsf | member | <1-10>}] |     |     |
Description
Showsboothistoryinformation.Whennoparametersarespecified,showsthemostrecentinformation
aboutthecurrentbootoperation,andthethreepreviousbootoperationsfortheswitch.Whentheall
parameterisspecified,theoutputofthiscommandshowsthebootinformationfortheactive
managementmodule.
Switchsystemandhardwarecommands|276

For switches that support line modules (such as 8400 switch series) including the all parameter displays
information for the active management module and all available line modules.

To view boot-history on a standby, the command must be sent on the conductor console.

Parameter

all

Description

Optional. Shows boot information for the active management
module. For switches that support line modules, including this
parameter displays information for and all available line modules.

vsf member <1-10>

Optional. Display boot history for the specified VSF member

Usage

This command displays the boot-index, boot-ID, and up time in seconds for the current boot. If there is
a previous boot, it displays boot-index, boot-ID, reboot time (based on the time zone configured in the
system) and reboot reasons. Previous boot information is displayed in reverse chronological order.

The output of this command includes the following information:

Parameter

Index

Boot ID

Current Boot, up for <time>

<Timestamp>: boot reason

Description

The position of the boot in the history file. Range: 0
to 3.

A unique ID for the boot . A system-generated 128-
bit string.

For the current boot, the show boot-history
command shows the number of seconds the
module has been running on the current software.

For previous boot operations, the show boot-
history command shows the time at which the
operation occurred and the reason for the boot.
The reason for the boot is one of the following
values:

n <DAEMON-NAME> crash: The daemon identified

by <DAEMON-NAME> caused the module to boot.

n Kernel crash: The operating system software

associated with the module caused the module

to boot.

n Uncontrolled reboot: The reason for the reboot

is not known.

n Reboot requested through database: The

reboot occurred because of a request made

through the CLI or other API.

Examples

Showing the boot history of the active management module:

switch# show boot-history

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

277

| Management | module |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
=================
| Index : | 2                                  |        |     |     |                 |
| ------- | ---------------------------------- | ------ | --- | --- | --------------- |
| Boot ID | : c34a2c2499004a02bbeeff4992e1fdbd |        |     |     |                 |
| Current | Boot, up for                       | 1 days | 13  | hrs | 13 mins 27 secs |
| Index : | 1                                  |        |     |     |                 |
| Boot ID | : bfba9bc486304e57904ac717a0ccbdcd |        |     |     |                 |
02 Sep 23 02:55:33 : CPU request reset with 0x20201, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:55:33                        | : Switch | boot | count | is 2 |
| ------- | ---------------------------------- | -------- | ---- | ----- | ---- |
| Index : | 0                                  |          |      |       |      |
| Boot ID | : a88a71b7ca9a4574af7e3b811ddfdc7e |          |      |       |      |
02 Sep 23 02:49:26 : Reboot requested by user, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:50:02                        | : Switch | boot | count | is 1 |
| ------- | ---------------------------------- | -------- | ---- | ----- | ---- |
| Index : | 3                                  |          |      |       |      |
| Boot ID | : f00ba10c8c44457f83fee303d014a89a |          |      |       |      |
25 Aug 23 10:27:42 : Power on reset with 0x1, Version: FL.10.14.0000-1465-
g9df95249d06b0~dirty
| 25 Aug | 23 10:28:18 | : Switch | boot | count | is 3 |
| ------ | ----------- | -------- | ---- | ----- | ---- |
25 Aug 23 10:29:02 : Primary overtemperature fault detected with 0x2 in PSU 1/1
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
switch#
| Management | module |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
=================
| Index :     | 3                                  |          |           |      |                  |
| ----------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| Current     | Boot, up for                       | 22 hrs   | 12        | mins | 22 secs          |
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
| Management | module |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
=================
| Index : | 3                                  |        |     |      |         |
| ------- | ---------------------------------- | ------ | --- | ---- | ------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |        |     |      |         |
| Current | Boot, up for                       | 22 hrs | 12  | mins | 22 secs |
Switchsystemandhardwarecommands|278

| Index :     | 2                                  |                    |                  |
| ----------- | ---------------------------------- | ------------------ | ---------------- |
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
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show capacities |           |            |     |
| --------------- | --------- | ---------- | --- |
| show capacities | <FEATURE> | [vsx-peer] |     |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description                             |
| --------- | --- | --- | --------------------------------------- |
| <FEATURE> |     |     | Specifiesafeature.Forexample,aaaorvrrp. |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
ShowingallavailablecapacitiesforBGP:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 279

| switch#            | show capacities |        | bgp |     |     |     |     |       |
| ------------------ | --------------- | ------ | --- | --- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter |     | BGP |     |     |     |       |
| Capacities         | Name            |        |     |     |     |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | AS  | numbers | in  | as-path | attribute |     |     |
| ------- | --------- | --- | ------- | --- | ------- | --------- | --- | --- |
32
...
Showingallavailablecapacitiesformirroring:
switch#
|                    | show capacities |        | mirroring |           |     |     |     |       |
| ------------------ | --------------- | ------ | --------- | --------- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter |           | Mirroring |     |     |     |       |
| Capacities         | Name            |        |           |           |     |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | Mirror | Sessions |     | configurable |     | in a system |     |
| ------- | --------- | ------ | -------- | --- | ------------ | --- | ----------- | --- |
4
| Maximum | number of | enabled |     | Mirror | Sessions | in  | a system |     |
| ------- | --------- | ------- | --- | ------ | -------- | --- | -------- | --- |
4
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities |        | mstp |      |     |     |     |       |
| ------------------ | --------------- | ------ | ---- | ---- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter |      | MSTP |     |     |     |       |
| Capacities         | Name            |        |      |      |     |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | mstp | instances |     | configurable |     | in a system |     |
| ------- | --------- | ---- | --------- | --- | ------------ | --- | ----------- | --- |
64
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities |        | vlan-count |      |       |     |     |       |
| ------------------ | --------------- | ------ | ---------- | ---- | ----- | --- | --- | ----- |
| System Capacities: |                 | Filter |            | VLAN | Count |     |     |       |
| Capacities         | Name            |        |            |      |       |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | VLANs | supported |     | in  | the system |     |     |
| ------- | --------- | ----- | --------- | --- | --- | ---------- | --- | --- |
4094
| Command        | History     |     |     |     |              |     |     |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- | --- | --- |
| Release        |             |     |     |     | Modification |     |     |     |
| 10.07orearlier |             |     |     |     | --           |     |     |     |
| Command        | Information |     |     |     |              |     |     |     |
Switchsystemandhardwarecommands|280

| Platforms | Command |     | context | Authority |     |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show capacities-status |     |     |           |            |     |     |     |
| ---------------------- | --- | --- | --------- | ---------- | --- | --- | --- |
| show capacities-status |     |     | <FEATURE> | [vsx-peer] |     |     |     |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<FEATURE> Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplay
capacities,values,andstatus.Required.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
| switch#    | show capacities-status |        |     |     |     |     |               |
| ---------- | ---------------------- | ------ | --- | --- | --- | --- | ------------- |
| System     | Capacities             | Status |     |     |     |     |               |
| Capacities | Status                 | Name   |     |     |     |     | Value Maximum |
------------------------------------------------------------------------------
| Number | of active          | gateway | mac        | addresses  | in  | a system | 0 16 |
| ------ | ------------------ | ------- | ---------- | ---------- | --- | -------- | ---- |
| Number | of aspath-lists    |         | configured |            |     |          | 0 64 |
| Number | of community-lists |         |            | configured |     |          | 0 64 |
...
ShowingthesystemcapacitiesstatusforBGP:
| switch#    | show capacities-status |         |     | bgp        |     |     |               |
| ---------- | ---------------------- | ------- | --- | ---------- | --- | --- | ------------- |
| System     | Capacities             | Status: |     | Filter BGP |     |     |               |
| Capacities | Status                 | Name    |     |            |     |     | Value Maximum |
-------------------------------------------------------------------------------
| Number | of aspath-lists    |        | configured |            |     |      | 0 64     |
| ------ | ------------------ | ------ | ---------- | ---------- | --- | ---- | -------- |
| Number | of community-lists |        |            | configured |     |      | 0 64     |
| Number | of neighbors       |        | configured | across     | all | VRFs | 0 50     |
| Number | of peer            | groups | configured | across     | all | VRFs | 0 25     |
| Number | of prefix-lists    |        | configured |            |     |      | 0 64     |
| Number | of route-maps      |        | configured |            |     |      | 0 64     |
| Number | of routes          | in     | BGP RIB    |            |     |      | 0 256000 |
Number of route reflector clients configured across all VRFs 0 16
| Command | History |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 281

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
| switch# show        | console |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Baud Rate:          | 9600    |         |                   |
| Command History     |         |         |                   |
| Release             |         |         | Modification      |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show core-dump
| show core-dump | [all | | <SLOT-ID>] |     |
| -------------- | ------ | ---------- | --- |
Description
Showscoredumpinformationaboutthespecifiedmodule.Whennoparametersarespecified,shows
onlythecoredumpsgeneratedinthecurrentbootofthemanagementmodule.Whentheall
parameterisspecified,showsallavailablecoredumps.
Switchsystemandhardwarecommands|282

Parameter

all

<SLOT-ID>

Usage

Description

Shows all available core dumps.

Shows the core dumps for the management module or
line module in <SLOT-ID>. <SLOT-ID> specifies a
physical location on the switch. Use the format
member/slot/port (for example, 1/3/1) for line
modules. Use the format member/slot for
management modules.

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
In Progress
Core dump generation is in progress. Do not attempt to copy this core dump.
Timestamp
Indicates the time the daemon crash occurred. The time is the local time using the time zone configured on the
switch.
Build ID
Identifies additional information about the software image associated with the daemon.

Examples

Showing core dump information for the current boot of the active management module only:

| Instance ID | Present

switch# show core-dump
==================================================================================
Daemon Name
==================================================================================
hpe-fand
hpe-sysmond
==================================================================================
Total number of core dumps : 2
==================================================================================

2017-08-04 19:05:34
2017-08-04 19:05:29

1246d2a
1246d2a

| Timestamp

| Build ID

1399
957

Yes
Yes

==================================================================================
Daemon Name

| Instance ID | Present

| Timestamp

| Build ID

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

283

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
| show deprecated          |     | commands    |     |     |     |     |     |
| ------------------------ | --- | ----------- | --- | --- | --- | --- | --- |
| show deprecated-commands |     | [<feature>] |     |     |     |     |     |
Description
ShowsthelistofCLIcommandsthatwillbedeprecatedinafuturereleasealongwiththenewformof
thesamecommandwhichisrecommendedforuse.
Boththecommandoptionswillbesupporteduntilacertainrelease,afterwhichonlythenewer
replacementcommandwillbesupported.
Switchsystemandhardwarecommands|284

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
| feature   |     |     |     | Optional.   |     |     |
Specifyfeaturename.
Thelistoffeaturesforwhichyoucanviewdeprecatedcommands
are:
Examples
CheckthedeprecatedCLIcommandsforaspecificfeature:
| switch# show | deprecated-commands |     |     |     |     |     |
| ------------ | ------------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
-----------
The following commands with ipv4 keyword will be replaced with ip
----------------------------------------------------------------------------------
-----------
| Deprecated:  | vrrp <1-255> |      | address-family |     | (ipv4 | | ipv6) |
| ------------ | ------------ | ---- | -------------- | --- | ----- | ------- |
| Replacement: | vrrp <1-255> |      | address-family |     | (ip   | | ipv6) |
| Deprecated:  | show bgp     | ipv4 | unicast        |     |       |         |
| Replacement: | show bgp     | ip   | unicast        |     |       |         |
...
| switch# show | deprecated-commands |     |     | vrrp |     |     |
| ------------ | ------------------- | --- | --- | ---- | --- | --- |
----------------------------------------------------------------------------------
-----------
The following commands with ipv4 keyword will be replaced with ip
----------------------------------------------------------------------------------
-----------
| Deprecated:  | vrrp <1-255> |       | address-family |         | (ipv4 | | ipv6)            |
| ------------ | ------------ | ----- | -------------- | ------- | ----- | ------------------ |
| Replacement: | vrrp <1-255> |       | address-family |         | (ip   | | ipv6)            |
| Deprecated:  | show vrrp    | (ipv4 | |              | ipv6 |  | brief | | detail)(<1-255>) |
| Replacement: | show vrrp    | (ip   | | ipv6         | | brief | |     | detail)(<1-255>)   |
...
| switch# show        | deprecated-commands |            |     | vsf                |     |     |
| ------------------- | ------------------- | ---------- | --- | ------------------ | --- | --- |
| Feature vsf         | has no              | deprecated |     | commands.          |     |     |
| Command History     |                     |            |     |                    |     |     |
| Release             |                     |            |     | Modification       |     |     |
| 10.14               |                     |            |     | Commandintroduced. |     |     |
| Command Information |                     |            |     |                    |     |     |
| Platforms           | Command             | context    |     | Authority          |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
show domain-name
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 285

| show domain-name | [vsx-peer] |     |     |
| ---------------- | ---------- | --- | --- |
Description
Showsthecurrentdomainname.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
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
Switchsystemandhardwarecommands|286

| Parameter |     |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Forfantrays,Statusisoneofthefollowingvalues:
n ready:Thefantrayisoperatingnormally.
n fault:Thefantrayisinafaultevent.Thestatusofthefantraydoesnotindicatethestatusoffans.
n empty:Thefantrayisnotinstalledinthesystem.
Forfans:
Speed :Indicates the relative speed of the fan based on the nominal speed range of the
| fan. Values | are: |            |            |           |        |             |         |                |     |     |
| ----------- | ---- | ---------- | ---------- | --------- | ------ | ----------- | ------- | -------------- | --- | --- |
| Slow:The    | fan  | is running |            | at less   | than   | 25% of      | its     | maximum speed. |     |     |
| Normal:The  | fan  | is         | running    | at 25-49% | of     | its         | maximum | speed.         |     |     |
| Medium:The  | fan  | is         | running    | at 50-74% | of     | its         | maximum | speed.         |     |     |
| Fast:The    | fan  | is running |            | at 75-99% | of     | its maximum |         | speed.         |     |     |
| Max:The     | fan  | is running |            | at 100%   | of its | maximum     | speed.  |                |     |     |
| N/A:The     | fan  | is not     | installed. |           |        |             |         |                |     |     |
Direction: The direction of airflow through the fan. Values are:
front-to-back:Air flows from the front of the system to the back of the system.
| N/A:The           | fan     | is not       | installed.     |               |     |                 |     |     |     |     |
| ----------------- | ------- | ------------ | -------------- | ------------- | --- | --------------- | --- | --- | --- | --- |
| Status: Fan       | status. |              | Values         | are:          |     |                 |     |     |     |     |
| uninitialized:The |         |              | fan has        | not completed |     | initialization. |     |     |     |     |
| ok: The           | fan     | is operating |                | normally.     |     |                 |     |     |     |     |
| fault:            | The fan | is           | in a           | fault state.  |     |                 |     |     |     |     |
| empty:            | The fan | is           | not installed. |               |     |                 |     |     |     |     |
Examples
ShowingoutputforsystemswithfantraysforAruba8400Switchseries:
| switch#  | show        | environment |     | fan |     |     |     |     |     |     |
| -------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fan tray | information |             |     |     |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Mbr/Tray | Description |     |     |     |     |     |     | Status Serial | Number | Fans |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---- |
------------------------------------------------------------------------------
| 1/1             | JL369A |     | 8400 | Fan tray |     |     |     | ready SGXXXXXXXXXX |     | 6   |
| --------------- | ------ | --- | ---- | -------- | --- | --- | --- | ------------------ | --- | --- |
| 1/2             | JL369A |     | 8400 | Fan tray |     |     |     | ready SGXXXXXXXXXX |     | 6   |
| 1/3             | N/A    |     |      |          |     |     |     | empty N/A          |     | 0   |
| Fan information |        |     |      |          |     |     |     |                    |     |     |
------------------------------------------------------------------------
| Mbr/Tray/Fan |     | Serial | Number | Speed |     | Direction |     | Status | RPM |     |
| ------------ | --- | ------ | ------ | ----- | --- | --------- | --- | ------ | --- | --- |
------------------------------------------------------------------------
| 1/1/1 |     | SGXXXXXXXXXX |     | slow   |     | front-to-back |     | ok    | 6000  |     |
| ----- | --- | ------------ | --- | ------ | --- | ------------- | --- | ----- | ----- | --- |
| 1/1/2 |     | SGXXXXXXXXXX |     | normal |     | front-to-back |     | ok    | 8000  |     |
| 1/1/3 |     | SGXXXXXXXXXX |     | medium |     | front-to-back |     | ok    | 11000 |     |
| 1/1/4 |     | SGXXXXXXXXXX |     | fast   |     | front-to-back |     | ok    | 14000 |     |
| 1/1/5 |     | SGXXXXXXXXXX |     | max    |     | front-to-back |     | fault | 16500 |     |
| 1/1/6 |     | N/A          |     | N/A    |     | N/A           |     | empty | 0     |     |
| 1/2/1 |     | SGXXXXXXXXX  |     | slow   |     | front-to-back |     | ok    | 6000  |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 287

...
| Fan tray | information |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- |
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
Switchsystemandhardwarecommands|288

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
| show environment |                   | power-consumption |          |
| ---------------- | ----------------- | ----------------- | -------- |
| show environment | power-consumption |                   | <DETAIL> |
Description
Displayspowerconsumptioninformation.
| Parameter   |     |     | Description                                   |
| ----------- | --- | --- | --------------------------------------------- |
| <DETAIL>    |     |     | Displaysdetailedpowerconsumptioninformation.  |
| <MEMBER-ID> |     |     | ForVSFsupportedplatformsonly.Displaysthepower |
consumptioninformationforthespecifiedVSF member. Range:1-
10.
Usage
Powerconsumedvaluesareupdatedevery5seconds.Thetotalpowerconsumedisthetotalpower
usedinachassis.Thepowerconsumedaverageiscalculatedfromthetotalpowerconsumedasa
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 289

runningaverageoveraperiodoftime.Theaverageperiodhasadefaultof10minutes.Theperiodcan
beconfiguredusingpower-consumption-average-period.
Onchassiswherepowerinputisnotsupported,powerconsumedisdisplayedasPowerUsageandPSU
OutputPowerisdisplayedasN/A.
Thefollowinginformationisprovidedforasummaryofpowerconsumption:
n linemodule:powerusedbylinemodule
n managementmodule:powerusedbymanagementmodule
n fabricmodule:powerusedbyfabricmodule
n chassismodule:powerusedbychassismodule
n fanmodule:powerusedbyfanmodule
powertotal:totalpowerconsumption
n
n averagepower:averagefortotalpowerconsumptionthatiscalculatedoveragivenperiod
n averageperiod:timetocalculatepoweraverage
Example
Showingthepowerconsumptionfora1RUswitch:
| switch#           | show | environment |           | power-consumption |               |           |         |        |         |
| ----------------- | ---- | ----------- | --------- | ----------------- | ------------- | --------- | ------- | ------ | ------- |
| Power Consumption |      |             | Averaging | Period            | : 600 seconds |           |         |        |         |
|                   |      |             |           |                   | Power         | Usage (W) | PSU     | Output | (W)     |
| Name Description  |      |             |           |                   | Instant       | Average   | Instant |        | Average |
----------------------------------------------------------------------------
| 1 8360-32Y4C |     | v2  | Switch |     | 120.00 | 111.16 | 111.00 |     | 102.62 |
| ------------ | --- | --- | ------ | --- | ------ | ------ | ------ | --- | ------ |
ShowingthepowerconsumptionforaVSFstack:
| switch#           | show | environment |           | power-consumption |               |           |         |        |         |
| ----------------- | ---- | ----------- | --------- | ----------------- | ------------- | --------- | ------- | ------ | ------- |
| Power Consumption |      |             | Averaging | Period            | : 600 seconds |           |         |        |         |
|                   |      |             |           |                   | Power         | Usage (W) | PSU     | Output | (W)     |
| Name Description  |      |             |           |                   | Instant       | Average   | Instant |        | Average |
----------------------------------------------------------------------------
| 1 6200M | 24G | 4SFP+ | Sw  |     | 350.00 | 349.62 | 300.00 |     | 311.50 |
| ------- | --- | ----- | --- | --- | ------ | ------ | ------ | --- | ------ |
| 2 6200M | 24G | 4SFP+ | Sw  |     | 300.00 | 299.50 | 280.00 |     | 275.50 |
Showingthepowerconsumptionforaswitchwhereinputreadingisnotsupported:
| switch#           | show | environment |           | power-consumption |               |           |         |        |         |
| ----------------- | ---- | ----------- | --------- | ----------------- | ------------- | --------- | ------- | ------ | ------- |
| Power Consumption |      |             | Averaging | Period            | : 600 seconds |           |         |        |         |
|                   |      |             |           |                   | Power         | Usage (W) | PSU     | Output | (W)     |
| Name Description  |      |             |           |                   | Instant       | Average   | Instant |        | Average |
----------------------------------------------------------------------------
| 1 6200M | 24G | 4SFP+ | Sw  |     | 321.00 | 330.30 |     | N/A | N/A |
| ------- | --- | ----- | --- | --- | ------ | ------ | --- | --- | --- |
Showingthepowerconsumptionforaswitchwithmultiplelinecards,inbrief:
Switchsystemandhardwarecommands|290

switch# show environment power-consumption
Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

Name Description
----------------------------------------------------------------------------
1

6410 v2 Chassis

Instant

Instant

Average

Average

803.23

900.00

798.00

905.62

Showing the power consumption for a switch with multiple line cards, in detail:

switch# show environment power-consumption detail
Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

Instant

1499.99

1307.00

1300.67

Average

Average

Instant

chassis total

Name Module Type
--------------------------------------------------------------
1
1/3
1/4
1/5
1/6
1/7
1/8
1/9
1/10
1/11
1/12
1/1
1/2

line
line
line
line
line
line
line
line
line
line
management
management
other

1495.00
97.00
95.00
90.00
58.00
90.00
93.00
96.00
92.00
100.00
99.00
14.00
13.00
370.00

Showing the power consumption for 4 member stack, in detail:

switch# show environment power-consumption detail

Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

Instant

Name Module Type
--------------------------------------------------------------
1
2
3
4

chassis total
chassis total
chassis total
chassis total

930.00
900.00
850.00
1200.00

905.17
920.00
857.25
1100.56

830.00
875.00
802.00
921.00

803.40
880.25
805.00
950.00

Instant

Average

Average

Total Power Consumption

3428.00

Showing the power consumption for VSF member 2:

switch# show environment power-consumption member 2

Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

Name Description
----------------------------------------------------------------------------
2

6200M 24G 4SFP+ Sw

Average

Average

Instant

Instant

280.00

275.50

300.00

299.50

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

291

ShowingthepowerconsumptionforVSFinvalidmember:
| switch# show    | environment    | power-consumption |                                                 | member 5 |     |
| --------------- | -------------- | ----------------- | ----------------------------------------------- | -------- | --- |
| Member 5        | is not present |                   |                                                 |          |     |
| Command History |                |                   |                                                 |          |     |
| Release         |                |                   | Modification                                    |          |     |
| 10.14.1000      |                |                   | Introducedenhancementtopowerconsumptionandpower |          |     |
consumptionaverage.
| 10.13               |         |         | Commandintroduced. |     |     |
| ------------------- | ------- | ------- | ------------------ | --- | --- |
| Command Information |         |         |                    |     |     |
| Platforms           | Command | context | Authority          |     |     |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show environment |                   | power-consumption |            |     | [vsx-peer] |
| ---------------- | ----------------- | ----------------- | ---------- | --- | ---------- |
| show environment | power-consumption |                   | [vsx-peer] |     |            |
Description
Showsthepowerbeingconsumedbyeachmanagementmodule,linecard,andfabriccardsubsystem,
andshowspowerconsumptionfortheentirechassis.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Thiscommandisonlyapplicabletosystemsthatsupportpowerconsumptionreadings.
Thepowerconsumptionvaluesareupdatedonceeveryminute.
Theoutputofthiscommandincludesthefollowinginformation:
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
Name
Showsthemembernumberandslotnumberofthemanagement
module,linemodule,orfabriccardmodule.
| Type |     |     | Showsthetypeofmoduleinstalledatthelocationspecifiedby |     |     |
| ---- | --- | --- | ----------------------------------------------------- | --- | --- |
Name.
Description Showstheproductnameandbriefdescriptionofthemodule.
Switchsystemandhardwarecommands|292

Parameter Description
Usage Showstheinstantaneouspowerconsumptionofthemodule.
PowerconsumptionisshowninWatts.
Module Total Power Usage Showsthetotalpowerconsumptionofallthemoduleslisted.
PowerconsumptionisshowninWatts.
Chassis Total Power Usage Showsthetotalinstantaneouspowerconsumedbytheentire
chassis,includingmodulesandcomponentsthatdonotsupport
individualpowerreporting.PowerconsumptionisshowninWatts.
Chassis Total Power Available Showsthetotalamountofpower,inWatts,thatcanbesupplied
tothechassis.
Chassis Total Power Allocated Showstotalpower,inWatts,thatisallocatedtopoweringthe
chassisanditsinstalledmodules.
Chassis Total Power Unallocated Showsthetotalamountofpower,inWatts,thathasnotbeen
allocatedtopoweringthechassisoritsinstalledmodules.This
powercanbeusedforadditionalhardwareyouinstallinthe
chassis.
Example
Showingpowerconsumptionusagefora8400switch
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 293

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
| Parameter | Description |     |     |
| --------- | ----------- | --- | --- |
Mbr/PSU
Showsthememberandslotnumberofthepowersupply.
| Product Number | Showstheproductnumberofthepowersupply. |     |     |
| -------------- | -------------------------------------- | --- | --- |
| Serial Number  |                                        |     |     |
Showstheserialnumberofthepowersupply,whichuniquelyidentifiesthepower
supply.
PSU Status
Thestatusofthepowersupply.Valuesare:
|     | n   | OK:Powersupplyisoperatingnormally. |     |
| --- | --- | ---------------------------------- | --- |
n OK*:Powersupplyisoperatingnormally,butitistheonlypowersupplyinthe
chassis.Onepowersupplyisnotsufficienttosupplyfullpowertotheswitch.When
thisvalueisshown,theoutputofthecommandalsoshowsamessageattheendof
thedisplayeddata.
|     | n   | Absent:Nopowersupplyisinstalledinthespecifiedslot.        |     |
| --- | --- | --------------------------------------------------------- | --- |
|     | n   | Inputfault:Thepowersupplyhasafaultconditiononitsinput.    |     |
|     | n   | Outputfault:Thepowersupplyhasafaultconditiononitsoutput.  |     |
|     | n   | Warning:Thepowersupplyisnotoperatingnormally.             |     |
|     | n   | WattageMaximum:Showsthemaximumamountofwattagethatthepower |     |
supplycanprovide.
Example
Switchsystemandhardwarecommands|294

Showingtheoutputwhenonlyonepowersupplyisactiveinthechassis:
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
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show environment |                     |     |     | rear-display-module |            |     |
| ---------------- | ------------------- | --- | --- | ------------------- | ---------- | --- |
| show environment | rear-display-module |     |     |                     | [vsx-peer] |     |
Description
Showsinformationaboutthedisplaymoduleonthebackoftheswitch.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 295

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
Validvaluesforstatusarethefollowing:\
| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
| normal    |     |     | Sensoriswithinnominaltemperaturerange. |
max
Highesttemperaturefromthissensor.
| low_critical |     |     | Lowestthresholdtemperatureforthissensor. |
| ------------ | --- | --- | ---------------------------------------- |
critical
Highestthresholdtemperatureforthissensor.
| fault |     |     | Faulteventforthissensor. |
| ----- | --- | --- | ------------------------ |
emergency
OvertemperatureeventforOvertemperatureeventforthis
sensor.
Examples
Showingcurrenttemperatureinformationforan8400switch:
Switchsystemandhardwarecommands|296

| switch# show | environment | temperature |     |     |     |
| ------------ | ----------- | ----------- | --- | --- | --- |
| Temperature  | information |             |     |     |     |
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
| switch# show | environment | temperature | detail |     |     |
| ------------ | ----------- | ----------- | ------ | --- | --- |
| Detailed     | temperature | information |        |     |     |
---------------------------------------------------
| Mbr/Slot-Sensor     |     | : 1/1-PCIE-Switch  |                        |          |     |
| ------------------- | --- | ------------------ | ---------------------- | -------- | --- |
| Module Type         |     | : line-card-module |                        |          |     |
| Module Description  |     | : JL363A           | 8400X 32P 10G SFP/SFP+ | Msec Mod |     |
| Status              |     | : normal           |                        |          |     |
| Fan-state           |     | : normal           |                        |          |     |
| Current temperature |     | : 95.82            | C                      |          |     |
| Minimum temperature |     | : 93.52            | C                      |          |     |
| Maximum temperature |     | : 96.15            | C                      |          |     |
...
| Detailed | temperature | information |     |     |     |
| -------- | ----------- | ----------- | --- | --- | --- |
---------------------------------------------------
| Mbr/Slot-Sensor     |     | : 1/1-PCIE-Switch  |                        |          |     |
| ------------------- | --- | ------------------ | ---------------------- | -------- | --- |
| Module Type         |     | : line-card-module |                        |          |     |
| Module Description  |     | : JL363A           | 8400X 32P 10G SFP/SFP+ | Msec Mod |     |
| Status              |     | : normal           |                        |          |     |
| Fan-state           |     | : normal           |                        |          |     |
| Current temperature |     | : 95.82            | C                      |          |     |
| Minimum temperature |     | : 93.52            | C                      |          |     |
| Maximum temperature |     | : 96.15            | C                      |          |     |
...
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 297

| show        | events          |     |     |
| ----------- | --------------- | --- | --- |
| show events | [ -e <EVENT-ID> | |   |     |
-s {emergency | alert | critical | error | warning | notice | info | debug} |
-r |
-a |
| -n <COUNT>       | |          |                |     |
| ---------------- | ---------- | -------------- | --- |
| -i <MEMBER-SLOT> |            | |              |     |
| -m {active       | | standby} | |              |     |
| -c {lldp         | | ospf     | | ...} |       |     |
| -d {lldpd        | | bgpd     | | fand | ...}] |     |
Description
Showseventlogsgeneratedbytheswitchmodulessincethelastreboot.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
-e <EVENT-ID>
ShowstheeventlogsforthespecifiedeventID.EventID
range:101through99999.
-s {emergency | alert | critical | Showstheeventlogsforthespecifiedseverity.Selectthe
| error | | warning | | notice | | severityfromthefollowinglist: |
| ----- | --------- | ---------- | ----------------------------- |
| info  | | debug}  |            |                               |
n emergency:Displayseventlogswithseverityemergency
only.
n alert:Displayseventlogswithseverityalertandabove.
n critical:Displayseventlogswithseveritycriticaland
above.
n error:Displayseventlogswithseverityerrorandabove.
n warning:Displayseventlogswithseveritywarningand
above.
n notice:Displayseventlogswithseveritynoticeandabove.
n info:Displayseventlogswithseverityinfoandabove.
n debug:Displayseventlogswithallseverities.
-r
Showsthemostrecenteventlogsfirst.
| -a  |     |     | Showsalleventlogs,includingthoseeventsfromprevious |
| --- | --- | --- | -------------------------------------------------- |
boots.
| -n <COUNT>       |     |     | Displaysthespecifiednumberofeventlogs.  |
| ---------------- | --- | --- | --------------------------------------- |
| -i <MEMBER-SLOT> |     |     | ShowstheeventlogsforthespecifiedslotID. |
-m {active | standby} Showstheeventlogsforthespecifiedmanagementcardrole.
SelectingactivedisplaystheeventlogfortheAMM
managementcardroleandstandbydisplayseventlogsfor
theSMMmanagementcardrole.
-c {lldp | ospf | ...} Showstheeventlogsforthespecifiedeventcategory.Enter
show event -cforafulllistingofsupportedcategorieswith
descriptions.
-d {lldpd | bgpd | fand | ...} Showstheeventlogsforthespecifiedprocess.Entershow
event -dforafulllistingofsupporteddaemonswith
descriptions.
Examples
Switchsystemandhardwarecommands|298

Showingeventlogs:
| switch# show | events |     |
| ------------ | ------ | --- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for | bridge_normal | interface |
| ------ | ------------- | --------- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
Showingthemostrecenteventlogsfirst:
| switch# show | events | -r  |
| ------------ | ------ | --- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for | bridge_normal | interface |
| ------ | ------------- | --------- |
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingalleventlogs:
| switch# show | events | -a  |
| ------------ | ------ | --- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for | bridge_normal | interface |
| ------ | ------------- | --------- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
ShowingeventlogsrelatedtoLACP:
switch#
| show | events | -c lacp |
| ---- | ------ | ------- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingeventlogsasperthespecifiedmanagementcardrole:
| switch# show | events | -m active |
| ------------ | ------ | --------- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 299

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
2017-08-17:22:33:06.181436|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll | interval is changed | to 512 |
| ----------- | ---- | ------------------- | ------ |
2017-08-17:22:33:06.181436|systemd-coredump|1201|LOG_CRIT|LC|1/1|hpe-sysmond
| crashed | due to signal:11 |     |     |
| ------- | ---------------- | --- | --- |
Showingeventlogsasperthespecifiedprocess:
| switch# show | events | -d lacpd |     |
| ------------ | ------ | -------- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Displayingthespecifiednumberofeventlogs:
| switch# show | events | -n 5 |     |
| ------------ | ------ | ---- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2018-03-21:06:12:15.500603|arpmgrd|6101|LOG_INFO|AMM|-|ARPMGRD daemon has started
2018-03-21:06:12:17.734405|lldpd|109|LOG_INFO|AMM|-|Configured LLDP tx-delay to 2
2018-03-21:06:12:17.740517|lacpd|1307|LOG_INFO|AMM|-|LACP system ID set to
70:72:cf:d4:34:42
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889
| Command History     |     |              |     |
| ------------------- | --- | ------------ | --- |
| Release             |     | Modification |     |
| 10.07orearlier      |     | --           |     |
| Command Information |     |              |     |
Switchsystemandhardwarecommands|300

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show        | fabric      |            |     |     |     |     |
| ----------- | ----------- | ---------- | --- | --- | --- | --- |
| show fabric | [<SLOT-ID>] | [vsx-peer] |     |     |     |     |
Description
Showsinformationabouttheinstalledfabrics.
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
switch#
show fabric
| Fabric | Modules |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
==============
|      | Product            |     |     |     | Serial |        |
| ---- | ------------------ | --- | --- | --- | ------ | ------ |
| Slot | Number Description |     |     |     | Number | Status |
---- ------- ---------------------------------- ---------- ------
| 1/1 | JL367A 8400X | 7.2Tbps | Fab | Mod | SG00000000 | Ready        |
| --- | ------------ | ------- | --- | --- | ---------- | ------------ |
| 1/2 | JL367A 8400X | 7.2Tbps | Fab | Mod | SG00000000 | Initializing |
| 1/3 | JL367A 8400X | 7.2Tbps | Fab | Mod | SG00000000 | Initializing |
Showingasinglefabric:
| switch#      | show fabric  | 1/1        |               |        |        |     |
| ------------ | ------------ | ---------- | ------------- | ------ | ------ | --- |
| Fabric       | module 1/1   | is ready   |               |        |        |     |
| Admin        | state: Up    |            |               |        |        |     |
| Description: | 8400X        | 7.2Tbps    | Fab           | Mod    |        |     |
| Full         | Description: | Aruba      | 8400X 7.2Tbps | Fabric | Module |     |
| Serial       | number:      | SG00000000 |               |        |        |     |
| Product      | number:      | JL367A     |               |        |        |     |
| Command      | History      |            |               |        |        |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 301

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show hostname
| show hostname | [vsx-peer] |     |     |
| ------------- | ---------- | --- | --- |
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
| switch# config      |          |          |              |
| ------------------- | -------- | -------- | ------------ |
| switch(config)#     | hostname | myswitch |              |
| myswitch(config)#   | show     | hostname |              |
| Command History     |          |          |              |
| Release             |          |          | Modification |
| 10.07orearlier      |          |          | --           |
| Command Information |          |          |              |
| Platforms           | Command  | context  | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show images
| show images | [vsx-peer] |     |     |
| ----------- | ---------- | --- | --- |
Switchsystemandhardwarecommands|302

Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
Parameter Description
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingtheprimaryandsecondaryimages:
| switch# | show images |     |
| ------- | ----------- | --- |
----------------------------------------------------------------------------
| AOS-CX | Primary Image |     |
| ------ | ------------- | --- |
----------------------------------------------------------------------------
| Version | : XL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 141 MB        |              |
| Date    | : 2017-06-30    | 14:02:34 PDT |
SHA-256 : 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
----------------------------------------------------------------------------
| AOS-CX | Secondary | Image |
| ------ | --------- | ----- |
----------------------------------------------------------------------------
| Version | : XL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 143 MB        |              |
| Date    | : 2017-06-30    | 14:02:34 PDT |
SHA-256 : 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
| Default | Image : secondary |     |
| ------- | ----------------- | --- |
------------------------------------------------------
| Management | Module | 1/5 (Active) |
| ---------- | ------ | ------------ |
------------------------------------------------------
| Active       | Image      | : primary       |
| ------------ | ---------- | --------------- |
| Service      | OS Version | : GT.01.01.0001 |
| BIOS Version |            | : GT-01-0013    |
------------------------------------------------------
| Management | Module | 1/6 (Standby) |
| ---------- | ------ | ------------- |
------------------------------------------------------
| Active       | Image       | : secondary     |
| ------------ | ----------- | --------------- |
| Service      | OS Version  | : GT.01.01.0001 |
| BIOS Version |             | : GT-01-0013    |
| switch#      | show images |                 |
---------------------------------------------------------------------------
| AOS-CX | Primary Image |     |
| ------ | ------------- | --- |
---------------------------------------------------------------------------
| Version | : TL.10.05.0001I |              |
| ------- | ---------------- | ------------ |
| Size    | : 405 MB         |              |
| Date    | : 2020-04-23     | 02:49:04 PDT |
SHA-256 : 7efe86a445e87e40f47de156add25720b7277cae1a8db2f9c4ea5f49e74f2a5a
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 303

---------------------------------------------------------------------------
| AOS-CX | Secondary Image |     |     |
| ------ | --------------- | --- | --- |
---------------------------------------------------------------------------
| Version | : TL.10.05.0001I |              |     |
| ------- | ---------------- | ------------ | --- |
| Size    | : 405 MB         |              |     |
| Date    | : 2020-04-23     | 02:49:04 PDT |     |
SHA-256 : 7efe86a445e87e40f47de156add25720b7277cae1a8db2f9c4ea5f49e74f2a5a
| Default | Image : primary |     |     |
| ------- | --------------- | --- | --- |
------------------------------------------------------
| Management | Module | 1/1 (Active) |     |
| ---------- | ------ | ------------ | --- |
------------------------------------------------------
| Active         | Image       | : primary                |              |
| -------------- | ----------- | ------------------------ | ------------ |
| Service        | OS Version  | : TL.01.05.0002-internal |              |
| BIOS Version   |             | : TL-01-0013             |              |
| Command        | History     |                          |              |
| Release        |             |                          | Modification |
| 10.07orearlier |             |                          | --           |
| Command        | Information |                          |              |
| Platforms      | Command     | context                  | Authority    |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show ip        | errors |                       |     |
| -------------- | ------ | --------------------- | --- |
| show ip errors | [{vrf  | <vrf-name>}|all-vrfs] |     |
Description
ShowsharwareandsoftwareIPerrorstatisticsforpacketsreceivedbytheswitchsincetheswitchwas
lastbooted.IfnoneoftheoptoinalVRFparametersareincluded,theshow ip errorscommanddisplays
thecurrentsystem-widehardwareIPerrorcountersandthedefaultVRF'ssoftwareIPerrorcounterson
theswitch
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <vrf-name> Optional.DisplayhardwareandsoftwareIPerrorcountersfora
specificVRF.
all-vrfs Optional.DisplayhardwareandsoftwareIPerrorcountersforall
VRFs
Usage
IPerrorinfoaboutreceivedpacketsiscollectedfromeachactivelinecardontheswitchandis
preservedduringfailoverevents.Errorcountsareclearedwhentheswitchisrebooted.
Dropreasonsmayincludethefollowing:
Switchsystemandhardwarecommands|304

| n Malformed | packet |     |     |     |
| ----------- | ------ | --- | --- | --- |
ThepacketdoesnotconformtoTCP/IPprotocolstandardssuchaspacketlengthorinternetheader
length.
Alargenumberofmalformedpacketscanindicatethattherearehardwaremalfunctionssuchas
loosecables,networkcardmalfunctions,orthataDOS(denialofservice)attackisoccurring.
| n IP address | error |     |     |     |
| ------------ | ----- | --- | --- | --- |
ThepackethasanerrorinthedestinationorsourceIPaddress.ExamplesofIPaddresserrors
includethefollowing:
o ThesourceIPaddressanddestinationIPaddressarethesame.
o
ThereisnodestinationIPaddress.
o ThesourceIPaddressisamulticastIPaddress.
o TheforwardingheaderofanIPv6addressisempty.
o ThereisnosourceIPaddressforanIPv6packet.
n Invalid TTLs
TheTTL(timetolive)valueofthepacketreachedzero.Thepacketwasdiscardedbecauseit
traversedthemaximumnumberofhopspermittedbytheTTLvalue.
TTLsareusedtopreventpacketsfrombeingcirculatedonthenetworkendlessly.
Example
Showingthecurrentsystem-widehardwareIPerrorcountersandthedefaultVRF'ssoftwareIPerror
countersontheswitch:
| switch#     | show ip errors |           |     |     |
| ----------- | -------------- | --------- | --- | --- |
| System-wide | (hardware)     | IP errors |     |     |
--------------------------------------------------
| Drop reason |     |     |     | Packets |
| ----------- | --- | --- | --- | ------- |
--------------------------------------------------
| Malformed  | packets       |        |     | 1   |
| ---------- | ------------- | ------ | --- | --- |
| IP address | errors        |        |     | 10  |
| Per-VRF    | (software) IP | errors |     |     |
--------------------------------------------------
VRF
| Drop reason |     |     | Packets |     |
| ----------- | --- | --- | ------- | --- |
--------------------------------------------------
default
| IPv4 maximum | transmission | unit |     | 3   |
| ------------ | ------------ | ---- | --- | --- |
| IPv4 time    | to live      |      |     | 0   |
| IPv6 maximum | transmission | unit |     | 0   |
| IPv6 hop     | limit        |      |     | 6   |
------------------------------
| Malformed | packets |     | 1   |     |
| --------- | ------- | --- | --- | --- |
...
Shoiwngthecurrentsystem-widehardwareIPerrorcounterandthesoftwareIPerrorcounterforall
VRFsontheswitch.
| switch#     | show ip errors | all-vrfs  |     |     |
| ----------- | -------------- | --------- | --- | --- |
| System-wide | (hardware)     | IP errors |     |     |
--------------------------------------------------
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 305

| Drop | reason |     |     | Packets |
| ---- | ------ | --- | --- | ------- |
--------------------------------------------------
| Malformed  | packets    |           |     | 1   |
| ---------- | ---------- | --------- | --- | --- |
| IP address | errors     |           |     | 10  |
| Per-VRF    | (software) | IP errors |     |     |
--------------------------------------------------
VRF
| Drop | reason |     | Packets |     |
| ---- | ------ | --- | ------- | --- |
--------------------------------------------------
default
| IPv4 | maximum transmission | unit |     | 3   |
| ---- | -------------------- | ---- | --- | --- |
| IPv4 | time to live         |      |     | 0   |
| IPv6 | maximum transmission | unit |     | 0   |
| IPv6 | hop limit            |      |     | 6   |
red
| IPv4 | maximum transmission | unit |     | 3   |
| ---- | -------------------- | ---- | --- | --- |
| IPv4 | time to live         |      |     | 7   |
| IPv6 | maximum transmission | unit |     | 0   |
| IPv6 | hop limit            |      |     | 6   |
blue
| IPv4 | maximum transmission | unit |     | 0   |
| ---- | -------------------- | ---- | --- | --- |
| IPv4 | time to live         |      |     | 1   |
| IPv6 | maximum transmission | unit |     | 0   |
| IPv6 | hop limit            |      |     | 6   |
...
| Command | History |     |              |     |
| ------- | ------- | --- | ------------ | --- |
| Release |         |     | Modification |     |
10.14.1000
CommandupdatedtodisplaybothhardwareandsoftwareIP
errorsinthecommandoutput.
| 10.07orearlier |             |         | --        |     |
| -------------- | ----------- | ------- | --------- | --- |
| Command        | Information |         |           |     |
| Platforms      | Command     | context | Authority |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show        | module      |            |     |     |
| ----------- | ----------- | ---------- | --- | --- |
| show module | [<SLOT-ID>] | [vsx-peer] |     |     |
Description
Showsinformationaboutinstalledlinemodulesandmanagementmodules.
| Parameter |     |     | Description                              |     |
| --------- | --- | --- | ---------------------------------------- | --- |
| <SLOT-ID> |     |     | Specifiesthememberandslotnumbersinformat |     |
Switchsystemandhardwarecommands|306

Parameter

Description

member/slot. For example, to show the module in
member 1, slot 3, enter 1/3.

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

vsx-peer

Usage

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
Present
The module hardware is installed in the chassis.
Ready
The module is available for use.
Updating
A firmware update is being applied to the module.

Examples

Showing all installed modules on an 8400 switch:

switch# show module

Management Modules
==================

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

307

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
TheoutputofthisshowcommandmayseemtoindicatethataJL363ALinecardsupportsMACsec.Thislinecard
ishardware-readytosupportMACsec,butthisfeatureisnotcurrentlysupportforthislinecardinAOS-CX
software.
Showingamanagementmoduleonan8400switch:
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
switch(config)#
|              |       | show module | 1/1          |          |     |     |
| ------------ | ----- | ----------- | ------------ | -------- | --- | --- |
| Line module  | 1/1   | is ready    |              |          |     |     |
| Admin state: | Up    |             |              |          |     |     |
| Description: | 8400X | 32P         | 10G SFP/SFP+ | Msec Mod |     |     |
Full Description: 8400X 32-port 10GbE SFP/SFP+ with MACsec Advanced Module
| Serial number: |         | SG00000000 |     |     |     |     |
| -------------- | ------- | ---------- | --- | --- | --- | --- |
| Product        | number: | JL363A     |     |     |     |     |
| Command        | History |            |     |     |     |     |
Switchsystemandhardwarecommands|308

| Release             |         |     |         |     | Modification |
| ------------------- | ------- | --- | ------- | --- | ------------ |
| 10.07orearlier      |         |     |         |     | --           |
| Command Information |         |     |         |     |              |
| Platforms           | Command |     | context |     | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show running-config |     |             |     |       |            |
| ------------------- | --- | ----------- | --- | ----- | ---------- |
| show running-config |     | [<FEATURE>] |     | [all] | [vsx-peer] |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
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
!
!
!
!
!
!
| aaa authentication |     |          | login | default | local |
| ------------------ | --- | -------- | ----- | ------- | ----- |
| aaa authorization  |     | commands |       | default | none  |
!
!
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 309

!
!
vlan 1
no shutdown
vlan 20
no shutdown
vlan 30
no shutdown
| interface | 1/1/1 |     |
| --------- | ----- | --- |
no shutdown
no routing
| vlan access | 30     |     |
| ----------- | ------ | --- |
| interface   | 1/1/32 |     |
no shutdown
no routing
| vlan access | 20              |     |
| ----------- | --------------- | --- |
| interface   | bridge_normal-1 |     |
no shutdown
| interface | bridge_normal-2 |     |
| --------- | --------------- | --- |
no shutdown
| interface | vlan20 |     |
| --------- | ------ | --- |
no shutdown
| vrf attach    | green          |     |
| ------------- | -------------- | --- |
| ip address    | 20.0.0.44/24   |     |
| ip ospf       | 1 area 0.0.0.0 |     |
| ip pim-sparse | enable         |     |
| interface     | vlan30         |     |
no shutdown
| vrf attach    | green          |     |
| ------------- | -------------- | --- |
| ip address    | 30.0.0.44/24   |     |
| ip ospf       | 1 area 0.0.0.0 |     |
| ip pim-sparse | enable         |     |
| ip pim-sparse | hello-interval | 100 |
Showingthecurrentrunningconfigurationinjsonformat:
| switch> show          | running-config | json  |
| --------------------- | -------------- | ----- |
| Running-configuration | in             | JSON: |
{
| "Monitoring_Policy_Script": |     | {   |
| --------------------------- | --- | --- |
"system_resource_monitor_mm1.1.0": {
"Monitoring_Policy_Instance": {
"system_resource_monitor_mm1.1.0/system_resource_monitor_
| mm1.1.0.default": | {         |                                            |
| ----------------- | --------- | ------------------------------------------ |
|                   | "name":   | "system_resource_monitor_mm1.1.0.default", |
|                   | "origin": | "system",                                  |
"parameters_values": {
"long_term_high_threshold": "70",
"long_term_normal_threshold": "60",
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
Switchsystemandhardwarecommands|310

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
!
!
snmp-server vrf mgmt
!
!
!
!
!
vlan 1
switch(config)#

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

311

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
commandisprovidedforonelevelbelowtheconfigcontext.Forexample,enteringthiscommand
forachildofachildoftheconfigcontextnotsupported.Ifyouenterthecommandonachildofthe
configcontext,thecurrentconfigurationofthatcontextandthechildrenofthatcontextare
displayed.
n Theglobalconfiguration(config)context.Ifyouenterthiscommandintheglobalconfiguration
(config)context,itshowstherunningconfigurationoftheentireswitch.Usetheshow
running-
configurationcommandinstead.
Switchsystemandhardwarecommands|312

Examples

Showing the running configuration for the current interface:

switch(config-if)# show running-config current-context
interface 1/1/1
vsx-sync qos vlans
no shutdown
description Example interface
no routing

vlan access 1
exit

Showing the current running configuration for the management interface:

switch(config-if-mgmt)# show running-config current-context
interface mgmt

no shutdown
ip static 10.0.0.1/24
default-gateway 10.0.0.8
nameserver 10.0.0.1

Showing the running configuration for the external storage share named nasfiles:

switch(config-external-storage-nasfiles)# show running-config current-context
external-storage nasfiles
address 192.168.0.1
vrf default
username nasuser
password ciphertext

AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=

type scp
directory /home/nas
enable

switch(config-external-storage-nasfiles)#

Showing the running configuration for a context that does not have instances:

switch(config-vsx)# show run current-context
vsx

inter-switch-link 1/1/1
role secondary
vsx-sync sflow time

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

313

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
vlan 1,195,197-200,4000
| interface       | mgmt         |          |     |
| --------------- | ------------ | -------- | --- |
| no shutdown     |              |          |     |
| ip static       | 10.6.9.24/24 |          |     |
| default-gateway |              | 10.6.9.1 |     |
| interface       | 1/1/1        |          |     |
| no shutdown     |              |          |     |
Switchsystemandhardwarecommands|314

| no routing   |                  |            |            |
| ------------ | ---------------- | ---------- | ---------- |
| vlan         | trunk native     | 1          |            |
| vlan         | trunk allowed    | 1,197-200  |            |
| interface    | vlan200          |            |            |
| ip address   | 10.3.200.3/24    |            |            |
| ip route     | 0.0.0.0/0        | 10.3.200.1 |            |
| https-server | rest access-mode |            | read-write |
| https-server | vrf mgmt         |            |            |
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
basic <PORT-NUM> Specifiesaphysicalportontheswitch.Usetheformat
member/slot/port(forexample,1/3/1).
| extended |     |     | Showsstatisticsforallinterfaces. |
| -------- | --- | --- | -------------------------------- |
Examples
Showingerrorcounterstatisticsforinterface1/1/1:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 315

| switch#       | show system   | error-counter-monitor | basic 1/1/1 |
| ------------- | ------------- | --------------------- | ----------- |
| Interface     | error counter | statistics            | for 1/1/1   |
| Error Counter |               |                       | Value       |
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
| switch#       | show system   | error-counter-monitor | extended  |
| ------------- | ------------- | --------------------- | --------- |
| Interface     | error counter | statistics            | for 1/1/1 |
| Error Counter |               |                       | Value     |
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
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show system
Switchsystemandhardwarecommands|316

| show system | [serviceos |     | password-prompt] |     | [vsx-peer] |     |
| ----------- | ---------- | --- | ---------------- | --- | ---------- | --- |
Description
Showsgeneralstatusinformationaboutthesystem.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
serviceos password-prompt ShowstheServiceOSpasswordpromptstatus.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemDescription,SystemContact,andSystemLocationcanbesetwiththesnmp-servercommand.
Whenvsx-peerisspecified,theUp TimevalueisnotshownbecauseitisnotsynchronizedbetweenVSX
peers.
Examples
Showingsysteminformation:
| switch#  | show        | system     |                 |             |          |            |
| -------- | ----------- | ---------- | --------------- | ----------- | -------- | ---------- |
| Hostname |             |            | : switch        |             |          |            |
| System   | Description |            | : switch        | description |          |            |
| System   | Contact     |            | : contact       |             |          |            |
| System   | Location    |            | : location      |             |          |            |
| Vendor   |             |            | : Aruba         |             |          |            |
| Product  | Name        |            | : Xxxxxx        | ...         |          |            |
| Chassis  | Serial      | Nbr        | : XXXXXXXXXX    |             |          |            |
| Base     | MAC Address |            | : xxxxxx-xxxxxx |             |          |            |
| AOS-CX   | Version     |            | : XX.99.99.9999 |             |          |            |
| Time     | Zone        |            | : UTC           |             |          |            |
| Up Time  |             |            | : 1             | week,       | 5 hours, | 28 minutes |
| CPU Util | (%)         |            | : 5             |             |          |            |
| CPU Util | (%          | avg 1 min) | : 11            |             |          |            |
| CPU Util | (%          | avg 5 min) | : 10            |             |          |            |
| Memory   | Usage       | (%)        | : 35            |             |          |            |
ShowingtheServiceOSpasswordpromptstatus:
| switch#          | show | system   | serviceos | password-prompt |     |     |
| ---------------- | ---- | -------- | --------- | --------------- | --- | --- |
| password-prompt: |      | disabled |           |                 |     |     |
ShowingsysteminformationforaVSXprimaryandsecondary(peer)switch:
| switch#  | show | system |               |     |     |     |
| -------- | ---- | ------ | ------------- | --- | --- | --- |
| Hostname |      |        | : vsx-primary |     |     |     |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 317

| System Description |               | : switch        | description  |             |              |             |     |
| ------------------ | ------------- | --------------- | ------------ | ----------- | ------------ | ----------- | --- |
| System Contact     |               | : contact       |              |             |              |             |     |
| System Location    |               | : location      |              |             |              |             |     |
| Vendor             |               | : Aruba         |              |             |              |             |     |
| Product Name       |               | : Xxxxxx        | ...          |             |              |             |     |
| Chassis Serial     | Nbr           | : XXXXXXXXXX    |              |             |              |             |     |
| Base MAC           | Address       | : xxxxxx-xxxxxx |              |             |              |             |     |
| Hostname           |               | : vsx-primary   |              |             |              |             |     |
| System Description |               | : switch        | description  |             |              |             |     |
| System Contact     |               | : contact       |              |             |              |             |     |
| System Location    |               | : location      |              |             |              |             |     |
| Vendor             |               | : Aruba         |              |             |              |             |     |
| Product Name       |               | : Xxxxxx        | ...          |             |              |             |     |
| Chassis Serial     | Nbr           | : XXXXXXXXXX    |              |             |              |             |     |
| Base MAC           | Address       | : xxxxxx-xxxxxx |              |             |              |             |     |
| AOS-CX Version     |               | : XX.99.99.9999 |              |             |              |             |     |
| Time Zone          |               | : UTC           |              |             |              |             |     |
| Up Time            |               | : 1 week,       | 2 hours,     | 15 minutes  |              |             |     |
| CPU Util           | (%)           | : 15            |              |             |              |             |     |
| CPU Util           | (% avg 1 min) | : 12            |              |             |              |             |     |
| CPU Util           | (% avg 5 min) | : 8             |              |             |              |             |     |
| Memory Usage       | (%)           | : 37            |              |             |              |             |     |
| switch# show       | system        | vsx-peer        |              |             |              |             |     |
| Hostname           |               | : vsx-secondary |              |             |              |             |     |
| System Description |               | : switch        | description  |             |              |             |     |
| System Contact     |               | : contact       |              |             |              |             |     |
| System Location    |               | : location      |              |             |              |             |     |
| Vendor             |               | : Aruba         |              |             |              |             |     |
| Product Name       |               | : Xxxxxx        | ...          |             |              |             |     |
| Chassis Serial     | Nbr           | : XXXXXXXXXX    |              |             |              |             |     |
| Base MAC           | Address       | : xxxxxx-xxxxxx |              |             |              |             |     |
| AOS-CX Version     |               | : XX.99.99.9999 |              |             |              |             |     |
| Time Zone          |               | : UTC           |              |             |              |             |     |
| CPU Util           | (%)           | : 7             |              |             |              |             |     |
| CPU Util           | (% avg 1 min) | : 13            |              |             |              |             |     |
| CPU Util           | (% avg 5 min) | : 9             |              |             |              |             |     |
| Memory Usage       | (%)           | : 32            |              |             |              |             |     |
| Command History    |               |                 |              |             |              |             |     |
| Release            |               |                 | Modification |             |              |             |     |
| 10.12              |               |                 | AddedCPU     | Util (% avg | 1 min)andCPU | Util (% avg | 5   |
min).
| 10.07orearlier      |     |     | --  |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| Command Information |     |     |     |     |     |     |     |
Switchsystemandhardwarecommands|318

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show system | resource-utilization |     |     |     |
| ----------- | -------------------- | --- | --- | --- |
show system resource-utilization [all | daemon <DAEMON-NAME>] |
| standby | | module | <SLOT-ID>] | [vsx-peer] |     |
| ------- | -------- | ---------- | ---------- | --- |
Description
Showsthesystemresourceutilizationdata.
| Parameter |     |     | Description                                        |     |
| --------- | --- | --- | -------------------------------------------------- | --- |
| all       |     |     | Showstheresourceutilizationdatafortheentireswitch. |     |
daemon <DAEMON-NAME> Showsonlytheresourceutilizationdatafortheprocessidentifiedby
<DAEMON-NAME>.
standby Showsonlytheresourceutilizationdataforthestandbymanagement
module.
module <SLOT-ID> Showsonlytheresourceutilizationdataforthelinemoduleidentifiedby
<SLOT-ID>.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonothave
theVSXconfigurationortheISLisdown,theoutputfromtheVSXpeer
switchisnotdisplayed.Thisparameterisavailableonswitchesthat
supportVSX.
Usage
Foralistofdaemonsthatlogevents,entershow events -d ?fromaswitchpromptinthemanager(#)
context.
Examples
Showingsystemresourceutilizationdata:
| switch#           | show system | resource-utilization |         |        |
| ----------------- | ----------- | -------------------- | ------- | ------ |
| System Resources: |             |                      |         |        |
| Processes         |             |                      |         | : 144  |
| CPU usage(%)      |             |                      |         | : 10   |
| CPU usage(%       | average     | over 1               | minute) | : 11   |
| CPU usage(%       | average     | over 5               | minute) | : 15   |
| Memory usage(%)   |             |                      |         | : 22   |
| Open FD's         |             |                      |         | : 1358 |
Storage 1: Endurance utilization = 10-20% (mmc-type-a), 0-10% (mmc-type-b),
| Health       | = normal   |            |     |            |
| ------------ | ---------- | ---------- | --- | ---------- |
| Data written | to various | partitions |     | since boot |
| Nos          | : 5 MB     |            |     |            |
| Log          | : 1 MB     |            |     |            |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 319

| Coredump | :         | 23 MB  |          |              |     |        |          |     |           |
| -------- | --------- | ------ | -------- | ------------ | --- | ------ | -------- | --- | --------- |
| Security | :         | 2 MB   |          |              |     |        |          |     |           |
| Selftest | :         | 405 KB |          |              |     |        |          |     |           |
| Swap     | :         | 14 MB  |          |              |     |        |          |     |           |
| Storage  | partition |        | usage(%) |              |     |        |          |     |           |
| Nos      | :         | 5      |          |              |     |        |          |     |           |
| Log      | :         | 60     |          |              |     |        |          |     |           |
| Coredump | :         | 23     |          |              |     |        |          |     |           |
| Security | :         | 2      |          |              |     |        |          |     |           |
| Selftest | :         | 1      |          |              |     |        |          |     |           |
| Swap     | :         | 0      |          |              |     |        |          |     |           |
| Process  |           |        |          | CPU Usage(%) |     | Memory | Usage(%) |     | Open FD's |
--------------------------------------------------------------------------
| hpe-sysmond |     |     |     | 1   |     |     | 2   |     | 11  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hpe-mgmdd   |     |     |     | 0   |     |     | 1   |     | 5   |
...
Attemptingtoshowresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# | show     | system      | resource-utilization |      |      |              |     |          |     |
| ------- | -------- | ----------- | -------------------- | ---- | ---- | ------------ | --- | -------- | --- |
| System  | resource | utilization |                      | data | poll | is currently |     | disabled |     |
Showingtheresourceutilizationdataforaparticularprocess:
| switch# | show | system | resource-utilization |              |     | daemon |          | hpe-sysmond |           |
| ------- | ---- | ------ | -------------------- | ------------ | --- | ------ | -------- | ----------- | --------- |
| Process |      |        |                      | CPU Usage(%) |     | Memory | Usage(%) |             | Open FD's |
--------------------------------------------------------------------------
| hpe-sysmond |     |     |     | 1   |     |     | 2   |     | 11  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdataforthestandbymanagementmodule:
switch#
|     | show | system | resource-utilization |     |     | standby |     |     |     |
| --- | ---- | ------ | -------------------- | --- | --- | ------- | --- | --- | --- |
System Resources:
| Processes    |           |            |             |            |     | : 244      |        |     |        |
| ------------ | --------- | ---------- | ----------- | ---------- | --- | ---------- | ------ | --- | ------ |
| CPU usage(%) |           |            |             |            |     | : 10       |        |     |        |
| CPU usage(%  |           | average    | over        | 1 minute)  |     | : 11       |        |     |        |
| CPU usage(%  |           | average    | over        | 5 minute)  |     | : 15       |        |     |        |
| Memory       | usage(%)  |            |             |            |     | : 11       |        |     |        |
| Open         | FD's      |            |             |            |     | : 1854     |        |     |        |
| Storage      | 1:        | Endurance  | utilization |            | =   | 18% (ssd), | Health | =   | normal |
| Data         | written   | to various |             | partitions |     | since boot |        |     |        |
| Nos          | :         | 15 MB      |             |            |     |            |        |     |        |
| Log          | :         | 1 MB       |             |            |     |            |        |     |        |
| Coredump     | :         | 23 MB      |             |            |     |            |        |     |        |
| Security     | :         | 2 MB       |             |            |     |            |        |     |        |
| Selftest     | :         | 405 KB     |             |            |     |            |        |     |        |
| Swap         | :         | 14 MB      |             |            |     |            |        |     |        |
| Storage      | partition |            | usage(%)    |            |     |            |        |     |        |
| Nos          | :         | 5          |             |            |     |            |        |     |        |
| Log          | :         | 60         |             |            |     |            |        |     |        |
Switchsystemandhardwarecommands|320

| Coredump | : 23 |     |     |          |     |        |          |           |
| -------- | ---- | --- | --- | -------- | --- | ------ | -------- | --------- |
| Security | :    | 2   |     |          |     |        |          |           |
| Selftest | :    | 1   |     |          |     |        |          |           |
| Swap     | :    | 0   |     |          |     |        |          |           |
| Process  |      |     | CPU | Usage(%) |     | Memory | Usage(%) | Open FD's |
--------------------------------------------------------------------------
| hpe-sysmond |     |     |     | 1   |     |     | 2   | 11  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| hpe-mgmdd   |     |     |     | 0   |     |     | 1   | 5   |
...
Showingresourceutilizationdataforalinemodule:
| switch# | show | system | resource-utilization |     |     | module | 1/1 |     |
| ------- | ---- | ------ | -------------------- | --- | --- | ------ | --- | --- |
--------------------------------------------------------------------------
| System Resource |     | utilization |     | for | line | card | module: 1/1 |     |
| --------------- | --- | ----------- | --- | --- | ---- | ---- | ----------- | --- |
--------------------------------------------------------------------------
| CPU usage(%)    |           |            |            |           | :     | 10   |     |     |
| --------------- | --------- | ---------- | ---------- | --------- | ----- | ---- | --- | --- |
| CPU usage(%     | average   |            | over       | 1 minute) | :     | 11   |     |     |
| CPU usage(%     | average   |            | over       | 5 minute) | :     | 15   |     |     |
| Memory usage(%) |           |            |            |           | :     | 11   |     |     |
| Open FD's       |           |            |            |           | :     | 754  |     |     |
| Data written    |           | to various | partitions |           | since | boot |     |     |
| Coredump        | : 23      | MB         |            |           |       |      |     |     |
| Storage         | partition |            | usage(%)   |           |       |      |     |     |
| Coredump        | : 45      |            |            |           |       |      |     |     |
Showingresourceutilizationdataforallmodules:
| switch# | show | system | resource-utilization |     |     | all |     |     |
| ------- | ---- | ------ | -------------------- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| Resource | utilization |     | data | for | Management | Module |     |     |
| -------- | ----------- | --- | ---- | --- | ---------- | ------ | --- | --- |
--------------------------------------------------------------------------
System Resources:
| Processes       |              |            |             |           | :     | 244    |          |        |
| --------------- | ------------ | ---------- | ----------- | --------- | ----- | ------ | -------- | ------ |
| CPU usage(%)    |              |            |             |           | :     | 10     |          |        |
| CPU usage(%     | average      |            | over        | 1 minute) | :     | 11     |          |        |
| CPU usage(%     | average      |            | over        | 5 minute) | :     | 15     |          |        |
| Memory usage(%) |              |            |             |           | :     | 11     |          |        |
| Open FD's       |              |            |             |           | :     | 1854   |          |        |
| Storage         | 1: Endurance |            | utilization |           | = 17% | (ssd), | Health = | normal |
| Data written    |              | to various | partitions  |           | since | boot   |          |        |
| Nos             | : 15         | MB         |             |           |       |        |          |        |
| Log             | :            | 1 MB       |             |           |       |        |          |        |
| Coredump        | : 23         | MB         |             |           |       |        |          |        |
| Security        | :            | 2 MB       |             |           |       |        |          |        |
| Selftest        | : 405        | KB         |             |           |       |        |          |        |
| Swap            | :            | 0 KB       |             |           |       |        |          |        |
| Storage         | partition    |            | usage(%)    |           |       |        |          |        |
| Nos             | :            | 5          |             |           |       |        |          |        |
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 321

| Log      | : 60 |     |     |          |     |        |          |     |           |
| -------- | ---- | --- | --- | -------- | --- | ------ | -------- | --- | --------- |
| Coredump | : 23 |     |     |          |     |        |          |     |           |
| Security | :    | 2   |     |          |     |        |          |     |           |
| Selftest | :    | 1   |     |          |     |        |          |     |           |
| Swap     | :    | 0   |     |          |     |        |          |     |           |
| Process  |      |     | CPU | Usage(%) |     | Memory | Usage(%) |     | Open FD's |
--------------------------------------------------------------------------
| (sd-pam) |     |     | 0   |     |     | 0   |     |     | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aaa
| utilspamcfg |     |     | 0   |     |     | 1   |     | 10  |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| Resource | utilization |     | data | for | Standby | Management | Module |     |     |
| -------- | ----------- | --- | ---- | --- | ------- | ---------- | ------ | --- | --- |
--------------------------------------------------------------------------
System Resources:
| Processes       |              |            |             |           |     | : 244      |        |     |        |
| --------------- | ------------ | ---------- | ----------- | --------- | --- | ---------- | ------ | --- | ------ |
| CPU usage(%)    |              |            |             |           |     | : 10       |        |     |        |
| CPU usage(%     | average      |            | over        | 1 minute) |     | : 11       |        |     |        |
| CPU usage(%     | average      |            | over        | 5 minute) |     | : 15       |        |     |        |
| Memory usage(%) |              |            |             |           |     | : 11       |        |     |        |
| Open FD's       |              |            |             |           |     | : 1854     |        |     |        |
| Storage         | 1: Endurance |            | utilization |           | =   | 17% (ssd), | Health | =   | normal |
| Data written    |              | to various | partitions  |           |     | since boot |        |     |        |
| Nos             | : 15         | MB         |             |           |     |            |        |     |        |
| Log             | :            | 1 MB       |             |           |     |            |        |     |        |
| Coredump        | : 23         | MB         |             |           |     |            |        |     |        |
| Security        | :            | 2 MB       |             |           |     |            |        |     |        |
| Selftest        | : 405        | KB         |             |           |     |            |        |     |        |
| Swap            | :            | 0 KB       |             |           |     |            |        |     |        |
| Storage         | partition    |            | usage(%)    |           |     |            |        |     |        |
| Nos             | :            | 5          |             |           |     |            |        |     |        |
| Log             | : 60         |            |             |           |     |            |        |     |        |
| Coredump        | : 23         |            |             |           |     |            |        |     |        |
| Security        | :            | 2          |             |           |     |            |        |     |        |
| Selftest        | :            | 1          |             |           |     |            |        |     |        |
| Swap            | :            | 0          |             |           |     |            |        |     |        |
--------------------------------------------------------------------------
| System Resource |     | utilization |     | for | line | card module: |     | 1/7 |     |
| --------------- | --- | ----------- | --- | --- | ---- | ------------ | --- | --- | --- |
--------------------------------------------------------------------------
| CPU usage(%)    |           |            |            |           |     | : 10       |     |     |     |
| --------------- | --------- | ---------- | ---------- | --------- | --- | ---------- | --- | --- | --- |
| CPU usage(%     | average   |            | over       | 1 minute) |     | : 11       |     |     |     |
| CPU usage(%     | average   |            | over       | 5 minute) |     | : 15       |     |     |     |
| Memory usage(%) |           |            |            |           |     | : 11       |     |     |     |
| Open FD's       |           |            |            |           |     | : 480      |     |     |     |
| Data written    |           | to various | partitions |           |     | since boot |     |     |     |
| Coredump        | : 23      | MB         |            |           |     |            |     |     |     |
| Storage         | partition |            | usage(%)   |           |     |            |     |     |     |
| Coredump        | : 23      |            |            |           |     |            |     |     |     |
--------------------------------------------------------------------------
| System Resource |     | utilization |     | for | line | card module: |     | 1/8 |     |
| --------------- | --- | ----------- | --- | --- | ---- | ------------ | --- | --- | --- |
--------------------------------------------------------------------------
| CPU usage(%) |     |     |     |     |     | : 10 |     |     |     |
| ------------ | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
Switchsystemandhardwarecommands|322

| CPU      | usage(%   | average    | over 1 minute) | : 11                                            |
| -------- | --------- | ---------- | -------------- | ----------------------------------------------- |
| CPU      | usage(%   | average    | over 5 minute) | : 15                                            |
| Memory   | usage(%)  |            |                | : 11                                            |
| Open     | FD's      |            |                | : 485                                           |
| Data     | written   | to various | partitions     | since boot                                      |
| Coredump |           | : 23 MB    |                |                                                 |
| Storage  | partition | usage(%)   |                |                                                 |
| Coredump |           | : 47       |                |                                                 |
| Command  | History   |            |                |                                                 |
| Release  |           |            |                | Modification                                    |
| 10.12    |           |            |                | TheoutputofthiscommandincludesCPUusage(%average |
over1minute)andCPUusage(%averageover5minute).
| 10.07orearlier |             |         |         | --        |
| -------------- | ----------- | ------- | ------- | --------- |
| Command        | Information |         |         |           |
| Platforms      |             | Command | context | Authority |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| show      | tech   |              |              |     |
| --------- | ------ | ------------ | ------------ | --- |
| show tech | [basic | | <FEATURE>] | [local-file] |     |
Description
Showsdetailedinformationaboutswitchfeaturesbyautomaticallyrunningtheshowcommands
associatedwiththefeature.Ifnoparametersarespecified,theshow techcommandshowsinformation
aboutallswitchfeatures.Technicalsupportpersonnelusetheoutputfromthiscommandfor
troubleshooting.
| Parameter |     |     |     | Description                             |
| --------- | --- | --- | --- | --------------------------------------- |
| basic     |     |     |     | Specifiesshowingabasicsetofinformation. |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow techcommand,followedbyaspace,followedbya
questionmark(?).
local-file Showstheoutputoftheshow techcommandtoalocaltextfile.
Usage
| Toterminatetheoutputoftheshow |     |     | techcommand,enterCtrl+C. |     |
| ----------------------------- | --- | --- | ------------------------ | --- |
IfthecommandwasnotterminatedwithCtrl+C,attheendoftheoutput,theshow techcommand
showsthefollowing:
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 323

n Thetimeconsumedtoexecutethecommand.
n Thelistoffailedshowcommands,ifany.
Togetacopyofthelocaltextfilecontentcreatedwiththeshowtechcommandthatisusedwiththe
| local-fileparameter,usethecopy |     | show-tech | local-filecommand. |
| ------------------------------ | --- | --------- | ------------------ |
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
| Failed  | command:     |     |     |
| ------- | ------------ | --- | --- |
| 1. show | boot-history |     |     |
=============================================================
| Show tech | took 3.000000 | seconds | for execution |
| --------- | ------------- | ------- | ------------- |
Directingtheoutputoftheshow tech basiccommandtothelocaltextfile:
| switch# | show tech basic | local-file |     |
| ------- | --------------- | ---------- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
| to copy-out    | this file.  |         |              |
| -------------- | ----------- | ------- | ------------ |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show usb |     |     |     |
| -------- | --- | --- | --- |
Switchsystemandhardwarecommands|324

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
switch>
show usb
| Enabled: | Yes |     |     |
| -------- | --- | --- | --- |
| Mounted: | No  |     |     |
IfUSBhasbeenenabledandadevicemounted:
| switch> show        | usb     |         |              |
| ------------------- | ------- | ------- | ------------ |
| Enabled:            | Yes     |         |              |
| Mounted:            | Yes     |         |              |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show usb             | file-system |     |     |
| -------------------- | ----------- | --- | --- |
| show usb file-system | [<PATH>]    |     |     |
Description
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 325

ShowsdirectorylistingsforamountedUSBdevice.Whenenteredwithoutthe<PATH>parameterthe
topleveldirectorytreeisshown.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<PATH>
Specifiesthefilepathtoshow.Aleading"/"inthepathisoptional.
Usage
Addingaleading"/"asthefirstcharacterofthe<PATH>parameterisoptional.
Attemptingtoenter'..'asanypartofthe<PATH>willgenerateaninvalidpathargumenterror.Only
fully-qualifiedpathnamesaresupported.
Examples
Showingthetopleveldirectorytree:
| switch# | show usb file-system |     |     |
| ------- | -------------------- | --- | --- |
/mnt/usb:
| 'System           | Volume Information' | dir1'          |     |
| ----------------- | ------------------- | -------------- | --- |
| /mnt/usb/System   | Volume              | Information':  |     |
| IndexerVolumeGuid |                     | WPSettings.dat |     |
/mnt/usb/dir1:
dir2 test1
/mnt/usb/dir1/dir2:
test2
Showingavailablepathoptionsfromthetoplevel:
| switch# | show usb file-system | /   |     |
| ------- | -------------------- | --- | --- |
total 64
| drwxrwxrwx | 2 32768 | Jan 22 16:27 'System | Volume Information' |
| ---------- | ------- | -------------------- | ------------------- |
| drwxrwxrwx | 3 32768 | Mar 5 15:26 dir1     |                     |
Showingthecontentsofaspecificfolder:
| switch# | show usb file-system | /dir1 |     |
| ------- | -------------------- | ----- | --- |
total 32
| drwxrwxrwx | 2 32768              | Mar 5 15:26 dir2  |     |
| ---------- | -------------------- | ----------------- | --- |
| -rwxrwxrwx | 1 0                  | Feb 5 18:08 test1 |     |
| switch#    | show usb file-system | dir1/dir2         |     |
total 0
| -rwxrwxrwx | 1 0 Feb | 6 05:35 test2 |     |
| ---------- | ------- | ------------- | --- |
Attemptingtoenteraninvalidcharacterinthepath:
| switch# | show usb file-system | dir1/../.. |     |
| ------- | -------------------- | ---------- | --- |
| Invalid | path argument        |            |     |
| Command | History              |            |     |
Switchsystemandhardwarecommands|326

| Release        |             |         | Modification |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
show version
| show version | [vsx-peer] |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- |
Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingversioninformationforan8400switch::
| switch> | show version |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
-----------------------------------------------------------------------------
AOS-CX
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 327

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| system | error-counter-monitor |     |     |
| ------ | --------------------- | --- | --- |
system error-counter-monitor
| no system | error-counter-monitor |     |     |
| --------- | --------------------- | --- | --- |
Description
Enablesthesystemerrorcountermonitoringfeature,whichrecordserrorcounterdataevery10
seconds.Default:Disabled.
Thenoformofthecommanddisableserrorcountermonitoringandstopstherecordingoferror
counterdata.
Example
Enablingthesystemerrorcountermonitor:
| switch(config)# | system      | error-counter-monitor |              |
| --------------- | ----------- | --------------------- | ------------ |
| Command         | History     |                       |              |
| Release         |             |                       | Modification |
| 10.07orearlier  |             |                       | --           |
| Command         | Information |                       |              |
| Platforms       | Command     | context               | Authority    |
config
| 8400 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| system                       | error-counter-monitor |               | poll-interval |
| ---------------------------- | --------------------- | ------------- | ------------- |
| system error-counter-monitor |                       | poll-interval | <INTERVAL>    |
Description
Setsthepollingintervalusedforthecollectionandrecordingoferrorcounterdata.
| Parameter  |     |     | Description                                       |
| ---------- | --- | --- | ------------------------------------------------- |
| <INTERVAL> |     |     | Specifiesthepollintervalinseconds.Range:10to3600. |
Default:10.
Example
Settingthesystemerrorcountermonitorpollinterval:
Switchsystemandhardwarecommands|328

| switch(config)# |             | system | error-counter-monitor |              | poll-interval | 20  |
| --------------- | ----------- | ------ | --------------------- | ------------ | ------------- | --- |
| Command         | History     |        |                       |              |               |     |
| Release         |             |        |                       | Modification |               |     |
| 10.07orearlier  |             |        |                       | --           |               |     |
| Command         | Information |        |                       |              |               |     |
| Platforms       | Command     |        | context               | Authority    |               |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| system                      | resource-utilization |     |               | poll-interval |     |     |
| --------------------------- | -------------------- | --- | ------------- | ------------- | --- | --- |
| system resource-utilization |                      |     | poll-interval | <SECONDS>     |     |     |
Description
ConfiguresthepollingintervalforsystemresourceinformationcollectionandrecordingsuchasCPU
andmemoryusage.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<SECONDS> Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Example
Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |             | system | resource-utilization |              | poll-interval | 20  |
| --------------- | ----------- | ------ | -------------------- | ------------ | ------------- | --- |
| Command         | History     |        |                      |              |               |     |
| Release         |             |        |                      | Modification |               |     |
| 10.07orearlier  |             |        |                      | --           |               |     |
| Command         | Information |        |                      |              |               |     |
| Platforms       | Command     |        | context              | Authority    |               |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
top cpu
top cpu
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 329

Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch# | top cpu |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
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
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
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
| Command | History |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Switchsystemandhardwarecommands|330

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
| switch(config)# | usb |     |     |
| --------------- | --- | --- | --- |
DisablingUSBportswhenaUSBdriveismounted:
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
AOS-CX10.14.xxxxFundamentalsGuide|(8400SwitchSeries) 331

EnablesordisablestheinsertedUSBdrive.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| mount     |     |     | EnablestheinsertedUSBdrive.                         |
| unmount   |     |     | DisablestheinsertedUSBdriveinpreparationforremoval. |
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
| switch# usb         | unmount |         |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Switchsystemandhardwarecommands|332

Chapter 15

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

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

333

HPEAruba https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
| Networking | htm |     |
| ---------- | --- | --- |
Hardware
Documentation
andTranslations
Portal
| HPEAruba | https://networkingsupport.hpe.com/downloads |     |
| -------- | ------------------------------------------- | --- |
Networking
software
| Software | https://lms.arubanetworks.com/ |     |
| -------- | ------------------------------ | --- |
licensingand
FeaturePacks
End-of-Life https://www.arubanetworks.com/support-services/end-of-life/
information
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheHPEArubaNetworkingSupportPortalat
https://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveHPEArubaNetworking
SupportPortalaccounttomanagesubscriptions).SecuritynoticesareviewablewithoutanHPEAruba
NetworkingSupportPortalaccount.
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
HPEArubaNetworkingiscommittedtoprovidingourcustomerswithinformationaboutthechemical
substancesinourproductsasneededtocomplywithlegalrequirements,environmentaldata(company
programs,productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSand
WEEE).Formoreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-
citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
HPEArubaNetworkingiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpus
improvethedocumentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback
SupportandOtherResources|334

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.14.xxxx Fundamentals Guide | (8400 Switch Series)

335