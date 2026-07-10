AOS-CX 10.09 Fundamentals
Guide

6300, 6400 Switch Series

Published: July 2022
Edition: 3

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
For more information, see the KM Process Guide. ?>
Acknowledgments

Bluetooth is a trademark owned by its proprietor and used by Hewlett Packard Enterprise under license.

| 2

Contents
Contents
| Contents                                     |                                                | 3   |
| -------------------------------------------- | ---------------------------------------------- | --- |
| About this                                   | document                                       | 11  |
| Applicableproducts                           |                                                | 11  |
| Latestversionavailableonline                 |                                                | 11  |
| Commandsyntaxnotationconventions             |                                                | 11  |
| Abouttheexamples                             |                                                | 12  |
| Identifyingswitchportsandinterfaces          |                                                | 12  |
| Identifyingmodularswitchcomponents           |                                                | 13  |
| About AOS-CX                                 |                                                | 14  |
| AOS-CXsystemdatabases                        |                                                | 14  |
| ArubaNetworkAnalyticsEngineintroduction      |                                                | 14  |
| AOS-CXCLI                                    |                                                | 15  |
| ArubaCXmobileapp                             |                                                | 15  |
| ArubaNetEdit                                 |                                                | 15  |
| Ansiblemodules                               |                                                | 16  |
| AOS-CXWebUI                                  |                                                | 16  |
| AOS-CXRESTAPI                                |                                                | 16  |
| In-bandandout-of-bandmanagement              |                                                | 16  |
| SNMP-basedmanagementsupport                  |                                                | 17  |
| Useraccounts                                 |                                                | 17  |
| Initial Configuration                        |                                                | 18  |
| InitialconfigurationusingZTP                 |                                                | 18  |
| InitialconfigurationusingtheArubaCXmobileapp |                                                | 19  |
|                                              | TroubleshootingBluetoothconnections            | 20  |
|                                              | BluetoothconnectionIPaddresses                 | 20  |
|                                              | Bluetoothisconnectedbuttheswitchisnotreachable | 20  |
|                                              | Bluetoothisnotconnected                        | 21  |
| InitialconfigurationusingtheCLI              |                                                | 24  |
|                                              | Connectingtotheconsoleport                     | 24  |
|                                              | Connectingtothemanagementport                  | 25  |
|                                              | ConfigureusingDHCPorstaticIP                   | 26  |
|                                              | Loggingintotheswitchforthefirsttime            | 26  |
|                                              | SettingswitchtimeusingtheNTPclient             | 27  |
| Configuringbanners                           |                                                | 28  |
| Configuringin-bandmanagementonadataport      |                                                | 28  |
| UsingtheWebUI                                |                                                | 29  |
| Configuringthemanagementinterface            |                                                | 29  |
| Selectingthesystemprofile                    |                                                | 30  |
| Restoringtheswitchtofactorydefaultsettings   |                                                | 30  |
| Managementinterfacecommands                  |                                                | 32  |
|                                              | default-gateway                                | 32  |
|                                              | ipstatic                                       | 33  |
|                                              | nameserver                                     | 34  |
|                                              | showinterfacemgmt                              | 35  |
| NTPcommands                                  |                                                | 36  |
|                                              | ntpauthentication                              | 36  |
3
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

|                               | ntpauthentication-key                 | 36  |
| ----------------------------- | ------------------------------------- | --- |
|                               | ntpdisable                            | 38  |
|                               | ntpenable                             | 38  |
|                               | ntpconductor                          | 39  |
|                               | ntpserver                             | 40  |
|                               | ntptrusted-key                        | 42  |
|                               | ntpvrf                                | 42  |
|                               | showntpassociations                   | 43  |
|                               | showntpauthentication-keys            | 44  |
|                               | showntpservers                        | 45  |
|                               | showntpstatistics                     | 46  |
|                               | showntpstatus                         | 47  |
| Telnet                        | access                                | 49  |
| Telnetcommands                |                                       | 49  |
|                               | showtelnetserver                      | 49  |
|                               | showtelnetserversessions              | 49  |
|                               | telnetserver                          | 50  |
| Interface                     | configuration                         | 52  |
| Configuringalayer2interface   |                                       | 52  |
| Configuringalayer3interface   |                                       | 52  |
| SinglesourceIPaddress         |                                       | 53  |
| Priority-basedflowcontrol     |                                       | 53  |
| Forwarderrorcorrection        |                                       | 53  |
| Unsupportedtransceiversupport |                                       | 54  |
| Interfacecommands             |                                       | 54  |
|                               | allow-unsupported-transceiver         | 54  |
|                               | defaultinterface                      | 56  |
|                               | description                           | 56  |
|                               | energy-efficient-ethernet             | 57  |
|                               | error-control                         | 58  |
|                               | flow-control                          | 59  |
|                               | interface                             | 60  |
|                               | interfaceloopback                     | 61  |
|                               | interfacevlan                         | 61  |
|                               | ipaddress                             | 62  |
|                               | ipmtu                                 | 63  |
|                               | ipsource-interface                    | 64  |
|                               | ipv6address                           | 66  |
|                               | ipv6source-interface                  | 67  |
|                               | l3-counters                           | 68  |
|                               | mtu                                   | 69  |
|                               | persona                               | 70  |
|                               | routing                               | 71  |
|                               | showallow-unsupported-transceiver     | 72  |
|                               | showinterface                         | 73  |
|                               | showinterfacedom                      | 76  |
|                               | showinterfaceenergy-efficientethernet | 77  |
|                               | showinterfaceflow-control             | 78  |
|                               | showinterfacetransceiver              | 80  |
|                               | showipinterface                       | 83  |
|                               | showipsource-interface                | 84  |
|                               | showipv6interface                     | 85  |
|                               | showipv6source-interface              | 86  |
|                               | shutdown                              | 87  |
Contents|4

|                                            | systeminterface-group                    |     | 88  |
| ------------------------------------------ | ---------------------------------------- | --- | --- |
| Subinterfaces                              |                                          |     | 90  |
| Configuringsubinterfaces                   |                                          |     | 90  |
| Subinterfaceinarouter-on-a-stickdeployment |                                          |     | 91  |
| Subinterfacecommands                       |                                          |     | 91  |
|                                            | encapsulationdot1q                       |     | 91  |
|                                            | interface                                |     | 92  |
|                                            | showcapacitiessubinterface               |     | 93  |
|                                            | showinterface                            |     | 94  |
| Source                                     | interface selection                      |     | 96  |
| Source-interfaceselectioncommands          |                                          |     | 96  |
|                                            | ipsource-interface(protocol<ip-addr>)    |     | 96  |
|                                            | ipsource-interface                       |     | 98  |
|                                            | ipv6source-interface                     |     | 99  |
|                                            | ipv6source-interface                     |     | 101 |
|                                            | showipsource-interface                   |     | 102 |
|                                            | showipv6source-interface                 |     | 103 |
|                                            | showrunning-config                       |     | 105 |
| VLANs                                      |                                          |     | 107 |
| Precision                                  | time protocol                            |     | 108 |
| PTPclocks                                  |                                          |     | 108 |
|                                            | Bestclock-sourcealgorithm                |     | 108 |
| PTPnetworkdiagram                          |                                          |     | 109 |
|                                            | Configurationexamples                    |     | 109 |
| PTPoverVSF                                 |                                          |     | 110 |
| Hardwareconsiderations                     |                                          |     | 110 |
| PTPcommands                                |                                          |     | 111 |
|                                            | clock-step                               |     | 111 |
|                                            | clearptpstatistics                       |     | 112 |
|                                            | enable                                   |     | 112 |
|                                            | ipsource-interface                       |     | 113 |
|                                            | mode                                     |     | 114 |
|                                            | ptpprofile                               |     | 115 |
|                                            | ptpenable                                |     | 116 |
|                                            | ptpvlan                                  |     | 117 |
|                                            | showptpclock                             |     | 118 |
|                                            | showptpinterface                         |     | 119 |
|                                            | showptpstatistics                        |     | 120 |
|                                            | transport-protocol                       |     | 122 |
| Recommendationsforconfiguration            |                                          |     | 123 |
|                                            | PTPCoPPclassconfigurationrecommendations |     | 123 |
QoSprioritizationconfigurationrecommendationfortransparentclock 123
|               | GeneralguidelinesforPTPIPv4multicast             |            | 123 |
| ------------- | ------------------------------------------------ | ---------- | --- |
| Usecases      |                                                  |            | 124 |
|               | Usecase1: PTP–IPv4overL2–SpineLeafTopology       |            | 124 |
|               | Usecase2:PTP–BCandTC(VSF)topologyconnectedviaLAG |            | 124 |
|               | Usecase3:PTP–L3spineleaftopology                 |            | 125 |
| Configuration | and firmware                                     | management | 127 |
| Checkpoints   |                                                  |            | 127 |
|               | Checkpointtypes                                  |            | 127 |
|               | Maximumnumberofcheckpoints                       |            | 127 |
|               | Usergeneratedcheckpoints                         |            | 127 |
5
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

|     | Systemgeneratedcheckpoints                      | 127 |
| --- | ----------------------------------------------- | --- |
|     | Supportedremotefileformats                      | 127 |
|     | Rollback                                        | 128 |
|     | Checkpointautomode                              | 128 |
|     | Testingaswitchconfigurationincheckpointautomode | 128 |
|     | Checkpointcommands                              | 128 |
|     | checkpointauto                                  | 128 |
|     | checkpointautoconfirm                           | 129 |
|     | checkpointdiff                                  | 130 |
|     | checkpointpost-configuration                    | 132 |
|     | checkpointpost-configurationtimeout             | 133 |
|     | checkpointrename                                | 133 |
|     | checkpointrollback                              | 134 |
|     | copycheckpoint<CHECKPOINT-NAME><REMOTE-URL>     | 135 |
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config} 136
|     | copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>    | 137 |
| --- | ----------------------------------------------- | --- |
|     | copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>     | 137 |
|     | copy<REMOTE-URL>{running-config|startup-config} | 138 |
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>} 140
|                              | copy{running-config|startup-config}<REMOTE-URL>  | 141 |
| ---------------------------- | ------------------------------------------------ | --- |
|                              | copy{running-config|startup-config}<STORAGE-URL> | 142 |
|                              | copystartup-configrunning-config                 | 143 |
|                              | copy<STORAGE-URL>running-config                  | 143 |
|                              | erase                                            | 145 |
|                              | showcheckpoint<CHECKPOINT-NAME>                  | 146 |
|                              | showcheckpoint<CHECKPOINT-NAME>hash              | 148 |
|                              | showcheckpointpost-configuration                 | 149 |
|                              | showcheckpoint                                   | 150 |
|                              | showcheckpointdate                               | 150 |
|                              | showrunning-confighash                           | 151 |
|                              | showstartup-confighash                           | 152 |
|                              | writememory                                      | 153 |
| Bootcommands                 |                                                  | 153 |
|                              | bootfabric-module                                | 153 |
|                              | bootline-module                                  | 154 |
|                              | bootmanagement-module                            | 155 |
|                              | bootset-default                                  | 157 |
|                              | bootsystem                                       | 158 |
|                              | showboot-history                                 | 159 |
| Firmwaremanagementcommands   |                                                  | 161 |
|                              | copy{primary|secondary}<REMOTE-URL>              | 161 |
|                              | copy{primary|secondary}<FIRMWARE-FILENAME>       | 162 |
|                              | copyprimarysecondary                             | 163 |
|                              | copy<REMOTE-URL>                                 | 164 |
|                              | copysecondaryprimary                             | 165 |
|                              | copy<STORAGE-URL>                                | 166 |
| Dynamic                      | Segmentation                                     | 168 |
| Virtualnetworkbasedtunneling |                                                  | 168 |
| User-basedtunneling          |                                                  | 173 |
|                              | Multi-zoneinUBT                                  | 175 |
| User-basedtunnelingcommands  |                                                  | 177 |
|                              | backup-controllerip                              | 177 |
|                              | enable                                           | 178 |
|                              | ipsource-interface                               | 178 |
|                              | papi-security-key                                | 180 |
Contents|6

| primary-controllerip                      |                                                    | 181 |
| ----------------------------------------- | -------------------------------------------------- | --- |
| sac-heartbeat-interval                    |                                                    | 181 |
| showipsource-interfaceubt                 |                                                    | 182 |
| showcapacitiesubt                         |                                                    | 183 |
| showubt                                   |                                                    | 184 |
| showubtinformation                        |                                                    | 187 |
| showubtstate                              |                                                    | 190 |
| showubtstatistics                         |                                                    | 193 |
| showubtusers                              |                                                    | 198 |
| uac-keepalive-interval                    |                                                    | 201 |
| ubt                                       |                                                    | 202 |
| ubt-client-vlan                           |                                                    | 203 |
| ubtmodevlan-extend                        |                                                    | 204 |
| SNMP                                      |                                                    | 206 |
| ConfiguringSNMP                           |                                                    | 206 |
| Aruba Central                             | integration                                        | 208 |
| ConnectingtoArubaCentral                  |                                                    | 208 |
| CustomCAcertificate                       |                                                    | 208 |
| SupportmodeinArubaCentral                 |                                                    | 209 |
| ArubaCentralcommands                      |                                                    | 209 |
| aruba-central                             |                                                    | 209 |
| aruba-centralsupport-mode                 |                                                    | 210 |
| configuration-lockoutcentralmanaged       |                                                    | 211 |
| disable                                   |                                                    | 212 |
| enable                                    |                                                    | 212 |
| location-override                         |                                                    | 213 |
| showaruba-central                         |                                                    | 214 |
| showrunning-configcurrent-context         |                                                    | 215 |
| Port filtering                            |                                                    | 216 |
| Portfilteringcommands                     |                                                    | 216 |
| portfilter                                |                                                    | 216 |
| showportfilter                            |                                                    | 217 |
| DNS                                       |                                                    | 220 |
| DNSclient                                 |                                                    | 220 |
| ConfiguringtheDNSclient                   |                                                    | 220 |
| DNSclientcommands                         |                                                    | 221 |
| ipdnsdomain-list                          |                                                    | 221 |
| ipdnsdomain-name                          |                                                    | 222 |
| ipdnshost                                 |                                                    | 223 |
| ipdnsserveraddress                        |                                                    | 224 |
| showipdns                                 |                                                    | 225 |
| Device discovery                          | and configuration                                  | 228 |
| Exampleconfigurationofdevicedeployment    |                                                    | 228 |
| Deviceprofiles                            |                                                    | 229 |
| ConfiguringadeviceprofileforLLDP          |                                                    | 230 |
| ConfiguringadeviceprofileforCDP           |                                                    | 230 |
| ConfiguringadeviceprofileforlocalMACmatch |                                                    | 231 |
| Deviceprofilecommands                     |                                                    | 231 |
|                                           | aaaauthenticationport-accessallow-cdp-bpdu         | 231 |
|                                           | aaaauthenticationport-accessallow-cdp-proxy-logoff | 232 |
|                                           | aaaauthenticationport-accessallow-lldp-bpdu        | 233 |
|                                           | associatecdp-group                                 | 235 |
7
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

associate lldp-group
associate mac-group
associate role
disable
enable
ignore (for CDP groups)
ignore (for LLDP groups)
ignore (for MAC groups)
mac-group
match (for CDP groups)
match (for LLDP groups)
match (for MAC groups)
port-access cdp-group
port-access device-profile
port-access device-profile mode block-until-profile-applied
port-access lldp-group
show port-access device-profile

LLDP

LLDP agent
LLDP MED support
Configuring the LLDP agent
LLDP commands

clear lldp neighbors
clear lldp statistics
lldp
lldp dot3
lldp holdtime
lldp management-ipv4-address
lldp management-ipv6-address
lldp med
lldp med-location
lldp receive
lldp reinit
lldp select-tlv
lldp timer
lldp transmit
lldp txdelay
lldp trap enable
show lldp configuration
show lldp configuration mgmt
show lldp local-device
show lldp neighbor-info
show lldp neighbor-info detail
show lldp neighbor-info mgmt
show lldp statistics
show lldp statistics mgmt
show lldp tlv

Cisco Discovery Protocol (CDP)

CDP support
CDP commands

cdp
clear cdp counters
clear cdp neighbor-info
show cdp
show cdp neighbor-info
show cdp traffic

235
236
237
238
238
239
240
241
245
246
248
249
253
254
255
256
257
258
259
261
261
262
262
262
263
264
264
265
266
267
268
269
270
271
272
273
274
275
277
279
279
281
284
287
288
290
290
291
291
292
292
293
293
294
295
295

Contents | 8

| Zero Touch                              | Provisioning       |           |          | 297 |
| --------------------------------------- | ------------------ | --------- | -------- | --- |
| ZTPsupport                              |                    |           |          | 297 |
| SettingupZTPonatrustednetwork           |                    |           |          | 298 |
| ZTPprocessduringswitchboot              |                    |           |          | 299 |
| ZTPVSFswitchoversupport                 |                    |           |          | 300 |
| ZTPcommands                             |                    |           |          | 300 |
|                                         | showztpinformation |           |          | 301 |
|                                         | ztpforceprovision  |           |          | 304 |
| Switch                                  | system and         | hardware  | commands | 306 |
| bluetoothdisable                        |                    |           |          | 306 |
| bluetoothenable                         |                    |           |          | 306 |
| clearevents                             |                    |           |          | 307 |
| cleariperrors                           |                    |           |          | 308 |
| consolebaud-rate                        |                    |           |          | 309 |
| domain-name                             |                    |           |          | 310 |
| hostname                                |                    |           |          | 310 |
| moduleadmin-state                       |                    |           |          | 311 |
| moduleproduct-number                    |                    |           |          | 312 |
| mtrace                                  |                    |           |          | 314 |
| showbluetooth                           |                    |           |          | 316 |
| showboot-history                        |                    |           |          | 317 |
| showcapacities                          |                    |           |          | 319 |
| showcapacities-status                   |                    |           |          | 320 |
| showconsole                             |                    |           |          | 321 |
| showcore-dump                           |                    |           |          | 322 |
| showdomain-name                         |                    |           |          | 324 |
| showenvironmentfan                      |                    |           |          | 324 |
| showenvironmentled                      |                    |           |          | 327 |
| showenvironmentpower-consumption        |                    |           |          | 327 |
| showenvironmentpower-supply             |                    |           |          | 329 |
| showenvironmentrear-display-module      |                    |           |          | 330 |
| showenvironmenttemperature              |                    |           |          | 331 |
| showevents                              |                    |           |          | 333 |
| showfabric                              |                    |           |          | 336 |
| showhostname                            |                    |           |          | 337 |
| showimages                              |                    |           |          | 338 |
| showiperrors                            |                    |           |          | 340 |
| showmodule                              |                    |           |          | 341 |
| showrunning-config                      |                    |           |          | 343 |
| showrunning-configcurrent-context       |                    |           |          | 346 |
| showstartup-config                      |                    |           |          | 348 |
| showsystemerror-counter-monitor         |                    |           |          | 349 |
| showsystem                              |                    |           |          | 351 |
| showsystemresource-utilization          |                    |           |          | 352 |
| showtech                                |                    |           |          | 354 |
| showusb                                 |                    |           |          | 355 |
| showusbfile-system                      |                    |           |          | 356 |
| showversion                             |                    |           |          | 357 |
| systemresource-utilizationpoll-interval |                    |           |          | 358 |
| topcpu                                  |                    |           |          | 359 |
| topmemory                               |                    |           |          | 360 |
| usb                                     |                    |           |          | 360 |
| usbmount|unmount                        |                    |           |          | 361 |
| Support                                 | and Other          | Resources |          | 363 |
9
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

Accessing Aruba Support
Accessing Updates

Aruba Support Portal
My Networking
Warranty Information
Regulatory Information
Documentation Feedback

363
364
364
364
364
364
365

Contents | 10

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

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

{ }

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

Braces. Indicates that at least one of the enclosed items is required.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

11

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
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchorenvironment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understandingthe | CLI prompts |     |     |
| ---------------- | ----------- | --- | --- |
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
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,wheninthe
VLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6300Switch | Series |     |     |
| ----------------- | ------ | --- | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
Aboutthisdocument|12

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

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

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

13

Chapter 2

About AOS-CX

About AOS-CX

AOS-CX is a new, modern, fully programmable operating system built using a database-centric design that
ensures higher availability and dynamic software process changes for reduced downtime. In addition to
robust hardware reliability, the AOS-CX operating system includes additional software elements not available
with traditional systems, including:

n Automated visibility to help IT organizations scale: The Aruba Network Analytics Engine allows IT to

monitor and troubleshoot network, system, application, and security-related issues easily through simple
scripts. This engine comes with a built-in time series database that enables customers and developers to
create software modules that allow historical troubleshooting, as well as analysis of historical trends to
predict and avoid future problems due to scale, security, and performance bottlenecks.

n Programmability simplified: A switch that is running the AOS-CX operating system is fully programmable
with a built-in Python interpreter as well as REST-based APIs, allowing easy integration with other devices
both on premise and in the cloud. This programmability accelerates IT organization understanding of and
response to network issues. The database holds all aspects of the configuration, statistics, and status
information in a highly structured and fully defined form.

n Faster resolution with network insights: With legacy switches, IT organizations must troubleshoot

problems after the fact, using traditional tools like CLI and SNMP, augmented by separate, expensive
monitoring, analytics, and troubleshooting solutions. These capabilities are built in to the AOS-CX
operating system and are extensible.

n High availability: For switches that support active and standby management modules, the AOS-CX

database can synchronize data between active and standby modules and maintain current configuration
and state information during a failover to the standby management module.

n Ease of roll-back to previous configurations: The built-in database acts as a network record, enabling

support for multiple configuration checkpoints and the ability to roll back to a previous configuration
checkpoint.

AOS-CX system databases
The AOS-CX operating system is a modular, database-centric operating system. Every aspect of the switch
configuration and state information is modeled in the AOS-CX switch configuration and state database,
including the following:

n Configuration information

n Status of all features

n Statistics

The AOS-CX operating system also includes a time series database, which acts as a built-in network record.
The time series database makes the data seamlessly available to Aruba Network Analytics Engine agents that
use rules that evaluate network conditions over time. Time-series data about the resources monitored by
agents are automatically collected and presented in graphs in the switch Web UI.

Aruba Network Analytics Engine introduction

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

14

The Aruba Network Analytics Engine is a first-of-its-kind built-in framework for network assurance and
remediation. Combining the full automation and deep visibility capabilities of the AOS-CX operating system,
this unique framework enables monitoring, collecting network data, evaluating conditions, and taking
corrective actions through simple scripting agents.

This engine is integrated with the AOS-CX system configuration and time series databases, enabling you to
examine historical trends and predict future problems due to scale, security, and performance bottlenecks.
With that information, you can create software modules that automatically detect such issues and take
appropriate actions.

With the faster network insights and automation provided by the Aruba Network Analytics Engine, you can
reduce the time spent on manual tasks and address current and future demands driven by Mobility and IoT.

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

n Connect to the switch for the first time and configure basic operational settings—all without requiring

you to connect a terminal emulator to the console port.

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

n Customized validation tests for corporate compliance and network design

n Automated large-scale configuration deployment without programming

About AOS-CX | 15

n Ability to track changes to hardware, software, and configurations (whether made through NetEdit or

directly on the switch) with automated versioning

For more information about Aruba NetEdit, search for NetEdit at the following website:

www.hpe.com/support/hpesc

Ansible modules
Ansible is an open-source IT automation platform.

Aruba publishes a set of Ansible configuration management modules designed for switches running AOS-CX
software. The modules are available from the following places:

n The arubanetworks.aoscx_role role in the Ansible Galaxy at:

https://galaxy.ansible.com/arubanetworks/aoscx_role

n The aoscx-ansible-role at the following GitHub repository: https://github.com/aruba/aoscx-ansible-

role

AOS-CX Web UI
The Web UI gives you quick and easy visibility into what is happening on your switch, providing faster
problem detection, diagnosis, and resolution. The Web UI provides dashboards and views to monitor the
status of the switch, including easy to read indicators for: power supply, temperature, fans, CPU use,
memory use, log entries, system information, firmware, interfaces, VLANs, and LAGs. In addition, you use
the Web UI to access the Network Analytics Engine, run certain diagnostics, and modify some aspects of the
switch configuration.

AOS-CX REST API
Switches running the AOS-CX software are fully programmable with a REST (REpresentational State Transfer)
API, allowing easy integration with other devices both on premises and in the cloud. This programmability—
combined with the Aruba Network Analytics Engine—accelerates network administrator understanding of
and response to network issues.

The AOS-CX REST API enables programmatic access to the AOS-CX configuration and state database at the
heart of the switch. By using a structured model, changes to the content and formatting of the CLI output
do not affect the programs you write. And because the configuration is stored in a structured database
instead of a text file, rolling back changes is easier than ever, thus dramatically reducing a risk of downtime
and performance issues.

The AOS-CX REST API is a web service that performs operations on switch resources using HTTPS POST, GET,
PUT, and DELETE methods.

A switch resource is indicated by its Uniform Resource Identifier (URI). A URI can be made up of several
components, including the host name or IP address, port number, the path, and an optional query string.
The AOS-CX operating system includes the AOS-CX REST API Reference, which is a web interface based on
the Swagger UI. The AOS-CX REST API Reference provides the reference documentation for the REST API,
including resources URIs, models, methods, and errors. The AOS-CX REST API Reference shows most of the
supported read and write methods for all switch resources.

In-band and out-of-band management
Management communications with a managed switch can be either of the following:

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

16

In band

In-band management communications occur through ports on the line modules of the switch, using
common communications protocols such as SSH and SNMP.

When you use an in-band management connection, management traffic from that connection uses the
same network infrastructure as user data. User data uses the data plane, which is responsible for
moving data from source to destination. Management traffic that uses the data plane is more likely to be
affected by traffic congestion and other issues affecting the user network.

Out of band

OOBM (out-of-band management) communications occur through a dedicated serial or USB console
port or though a dedicated networked management port.

OOBM operates on a management plane that is separate from the data plane used by data traffic on
the switch and by in-band management traffic. That separation means that OOBM can continue to
function even during periods of traffic congestion, equipment malfunction, or attacks on the network. In
addition, it can provide improved switch security: a properly configured switch can limit management
access to the management port only, preventing malicious attempts to gain access through the data
ports.

Networked OOBM typically occurs on a management network that connects multiple switches. It has the
added advantage that it can be done from a central location and does not require an individual physical
cable from the management station to the console port of each switch.

SNMP-based management support
The AOS-CX operating system provides SNMP read access to the switch. SNMP support includes support of
industry-standard MIB (Management Information Base) plus private extensions, including SNMP events,
alarms, history, statistics groups, and a private alarm extension group. SNMP access is disabled by default.

User accounts
To view or change configuration settings on the switch, users must log in with a valid account.
Authentication of user accounts can be performed locally on the switch, or by using the services of an
external TACACS+ or RADIUS server.

Two types of user accounts are supported:

n Operators: Operators can view configuration settings, but cannot change them. No operator accounts

are created by default.

n Administrators: Administrators can view and change configuration settings. A default locally stored

administrator account is created with username set to admin and no password. You set the
administrator account password as part of the initial configuration procedure for the switch.

About AOS-CX | 17

Chapter 3

Initial Configuration

Initial Configuration

Perform the initial configuration of a factory default switch using one of the following methods:

n Load a switch configuration using zero-touch provisioning (ZTP). When ZTP is used, the configuration is
loaded from a server automatically when the switch booted from the factory default configuration.

n Connect to the switch wirelessly with a mobile device through Bluetooth, and use the Aruba CX Mobile
App to deploy an initial configuration from a provided template. The template you choose during the
deployment process determines how the management interface is configured. Optionally, as the final
deployment step, you can select to import the switch into NetEdit through a WiFI connection to the
NetEdit server.

Alternatively, you can use the Aruba CX Mobile App to manually configure switch settings and features for a
subset of the features you can configure using the CLI. You can also access the CLI through the mobile
application.

n Connect the management port on the switch to your network, and then use SSH client software to reach
the switch from a computer connected to the same network. This requires that a DHCP server is installed
on the network. Configure switch settings and features by executing CLI commands.

n Connect a computer running terminal emulation software to the console port on the switch. Configure

switch settings and features by executing CLI commands.

Initial configuration using ZTP
Zero Touch Provisioning (ZTP) configures a switch automatically from a remote server.

Prerequisites

n The switch must be in the factory default configuration.

Do not change the configuration of the switch from its factory default configuration in any way, including by
setting the administrator password.

n Your network administrator or installation site coordinator must provide a Category 6 (Cat6) cable

connected to the network that provides access to the servers used for Zero Touch Provisioning (ZTP)
operations.

Procedure

1. Connect the network cable to the out-of-band management port on the switch. If your network

administrator or installation site coordinator has instructed you to connect network cable to a data
port, connect the cable to that data port instead.

See the Installation Guide for switch to determine the location of the switch ports.

2.

If the switch is powered on, power off the switch.

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image is
being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

18

Initial configuration using the Aruba CX mobile app

This procedure describes how to use your mobile device to connect to the Bluetooth interface of the switch
to connect to the switch for the first time so that you can configure basic operational settings using the
Aruba CX mobile app.

Prerequisites

n You have obtained the USB Bluetooth adapter that was shipped with the switch. Information about the
make and model of the supported adapter is included in the information about the Aruba CX mobile app
in the Apple Store or Google Play.

n The Aruba CX mobile app must be installed on your mobile device.

n Bluetooth must be enabled on your mobile device.

n Your mobile device must be within the communication range of the Bluetooth adapter.

n If you are planning to import the switch into NetEdit, your mobile device must be able to use a Wi-Fi

connection—not Bluetooth—to access the NetEdit server.

If your mobile device does not support simultaneous Bluetooth and Wi-Fi connections, you must use the
NetEdit interface to import the switch at a later time. You can use the Devices tab to display the IP address
of the switches you configured using your mobile device.

n The switch must be installed and powered on, with the network operating system boot sequence

complete.

For information about installing and powering on the switch, see the Installation Guide for the switch.

Because you are using this mobile application to configure the switch through the Bluetooth interface, it is
not necessary to connect a console to the switch.

n Bluetooth and USB must be enabled on the switch. On switches shipped from the factory, Bluetooth

and USB are enabled by default.

Procedure

1.

Install the USB Bluetooth adapter in the USB port of the switch.

For switches that have multiple management modules, you must install the USB Bluetooth adapter
in the USB port of the active management module. Typically, the active management module is the
module in slot 5. On the 6400, the active management module is typically installed in slot 1. When
configuring a stack, a USB Bluetooth adapter must be installed on each 6300 switch in the stack.

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

On some Android devices, you might need to change the settings of the paired device to specify that
it be used for Internet access.

Initial Configuration | 19

3. Open the Aruba CX mobile app on your mobile device.

;" />

The application attempts to connect to the switch using the switch Bluetooth IP address and the
default switch login credentials. The Home screen of the application shows the status of the
connection to the switch:

n If the login attempt was successful, the Bluetooth icon is displayed and the status message shows

the Bluetooth IP address of the switch. In addition, the connection graphic is green. You can
continue to the next step.

n If the login attempt was not successful, but a response was received, the Bluetooth icon is

displayed, but the status message is: Login Required. You can continue to the next step. When
you tap one of the tiles, you will be prompted for login credentials.

n If the login attempt did not receive a response, the Bluetooth icon is not displayed, and the status

message is: No Connection.

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

n Alternatively, you can complete the initial configuration of the switch by tapping Modify Config

and then selecting the features and settings to configure.

n You can also use the Modify Config feature to configure some switch features after the initial

configuration is complete. For more information about what you can configure using the Aruba CX
mobile app, see the online help for the application.

Troubleshooting Bluetooth connections

Bluetooth connection IP addresses

The Bluetooth connection uses IP addresses in the 192.168.99.0/24 subnet.

Switch

192.168.99.1

Mobile device

192.168.99.10

Bluetooth is connected but the switch is not reachable

Symptom

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

20

The mobile device settings indicate that the device is connected to the switch through Bluetooth. However,
the mobile application indicates that the switch is not reachable.

Solution 1

Cause

The mobile device is paired with a different nearby switch.

Action

1. Verify the model number and serial number of the switch to which you are attempting to connect.

2. Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile

device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following
format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify that
it be used for Internet access.

Solution 2

Cause

The mobile device is connected to a different network—such as through a Wi-Fi connection—that conflicts
with the subnet used for the switch Bluetooth connection.

Action

Disconnect the mobile device from the network that is using the conflicting subnet.

For example, use the mobile device settings to turn off or disable Wi-Fi. If you choose to disable Wi-Fi on the
mobile device, and you are not able to access cellular service, you will not be able to connect to the NetEdit
server to import the switch, but you can still deploy a switch configuration.

Bluetooth is not connected

Symptom

Your mobile device cannot establish a Bluetooth connection to the switch.

Solution 1

Cause

Bluetooth is not enabled on your mobile device.

Action

n Use your mobile device settings application to enable Bluetooth.

n Use the Bluetooth settings on your mobile device to pair and connect the switch to your mobile device.

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of available
devices. Switches running the AOS-CX operating system are displayed in the following format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

Initial Configuration | 21

On some Android devices, you might need to change the settings of the paired device to specify that it be
used for Internet access.

Solution 2

Cause

Your mobile device is not within the broadcast range of the Bluetooth adapter.

Action

Move closer to the switch.

Devices can communicate through Bluetooth when they are close, typically within a few feet of each other.

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

3. On some Android devices, you might need to change the settings of the paired device to specify that

it be used for Internet access.

Solution 4

Cause

Bluetooth is not enabled on the switch.

New switches are shipped from the factory with the USB port and Bluetooth enabled. However, an installed
switch might have been configured to disable Bluetooth or disable the USB port, which the USB Bluetooth
adapter uses.

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

Another mobile device has already connected to the switch through Bluetooth. This cause is likely if your
device is repeatedly disconnected within 1-2 seconds of establishing a connection.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

22

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

On some Android devices, you might need to change the settings of the paired device to specify that
it be used for Internet access.

Solution 7

Cause

The USB Bluetooth adapter is not installed in the switch.

If the switch has multiple management modules, the USB Bluetooth adapter might be installed in the
management module that is not the active management module.

Action

Install the USB Bluetooth adapter in the USB port of the switch.

For switches that have multiple management modules, you must install the USB Bluetooth adapter in the
USB port of the active management module. Typically, for new switches, the active management module is
the module in slot 5 (Aruba 8400 switches) or slot 1 (Aruba 6400 switches).

For information about the location of the USB port on the switch, see the Installation Guide for the switch.

Solution 8

Cause

A problem occurred with the Bluetooth feature on the switch. For example, the software daemon was
stopped and then restarted.

Action

Initial Configuration | 23

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

On some Android devices, you might need to change the settings of the paired device to specify that
it be used for Internet access.

Solution 9

Cause

A switch that is member of a stack (but is not the conductor switch), has a USB Bluetooth adapter installed,
but mobile application has lost contact with that switch.

Action

Remove and then reinstall the USB Bluetooth adapter.

Do not remove the USB Bluetooth adapter from the conductor switch.

Initial configuration using the CLI
This procedure describes how to connect to the switch for the first time and configure basic operational
settings using the CLI. In this procedure, you use a computer to connect to the switch using the either the
console port or management port.

Procedure

1. Connect to the console port or the management port.

2. Log into the switch for the first time.

3. Configure switch time using the NTP client.

Connecting to the console port

Prerequisites

n A switch installed as described in its hardware installation guide.

n A computer with terminal emulation software.

n A JL448A Aruba X2 C2 RJ45 to DB9 console cable. (6400 only), or a USB-C cable (6300/6400).

Procedure

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

24

1. Connecttheconsoleportontheswitchtotheserialportonthecomputerusingaconsolecable,or
connecttheUSB-CportontheswitchtotheUSB-CportonthecomputerusingaUSB-Ccable.
2. Starttheterminalemulationsoftwareonthecomputerandconfigureanewserialsessionwiththe
followingsettings:
n Speed:115200bps
n Databits:8
n Stopbits:1
n Parity:None
Flowcontrol:None
n
3. Starttheterminalemulationsession.
4. PressEnteronce.Iftheconnectionissuccessful,youarepromptedtologin.
| Optionalconsole | portspeedsetting |     |     |     |
| --------------- | ---------------- | --- | --- | --- |
Ifdesired,theconsoleportspeedcanbesetwiththeconsole baud-ratecommand.Forexample,setting
theconsoleportspeedto9600bps:
| switch(config)# | console | baud-rate | 9600 |     |
| --------------- | ------- | --------- | ---- | --- |
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
| settings | are updated | to match the | baud rate | of the switch. |
| -------- | ----------- | ------------ | --------- | -------------- |
| Continue | (y/n)? y    |              |           |                |
Showingtheconsoleportcurrentspeed:
| switch# show | console |     |     |     |
| ------------ | ------- | --- | --- | --- |
| Baud Rate:   | 9600    |     |     |     |
Fordetailsontheconsole baud-rateandshow consolecommands,seeSwitchsystemandhardware
commands.
| Connecting | to the | management | port |     |
| ---------- | ------ | ---------- | ---- | --- |
Prerequisites
n TwoEthernetcables
n SSHclientsoftware
Procedure
1. Bydefault,themanagementinterfaceissettoautomaticallyobtainanIPaddressfromaDHCP
server,andSSHsupportisenabled.IfthereisnoDHCPserveronyournetwork,youmustconfigurea
staticaddressonthemanagementinterface:
| a. Connecttotheconsoleport          |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- |
| b. Configurethemanagementinterface. |     |     |     |     |
2. UseanEthernetcabletoconnectthemanagementporttoyournetwork.
3. UseanEthernetcabletoconnectyourcomputertothesamenetwork.
InitialConfiguration |25

4. StartyourSSHclientsoftwareandconfigureanewsessionusingtheaddressassignedtothe
managementinterface.(IfthemanagementinterfaceissettooperateasaDHCPclient,retrievethe
IPaddressassignedtothemanagementinterfacefromyourDHCPserver.)
5. Startthesession.Iftheconnectionissuccessful,youarepromptedtologin.
| Configure | usingDHCPor |     | static | IP  |     |     |
| --------- | ----------- | --- | ------ | --- | --- | --- |
Userscanuseanydataportsforin-bandmanagementpurposes.IPDHCPissupportedoninterfaceVLAN1only.
AllswitchportsarepartofaccessVLAN1bydefault.StaticIPaddressandIPDHCPconfigurationcanco-existon
VLAN1,howeverstaticaddressestakeprecedencewheneverconfigured.
DHCPConfiguration
| switch#:                | config |      |             |     |            |      |
| ----------------------- | ------ | ---- | ----------- | --- | ---------- | ---- |
| switch(config)#:        |        | vlan | 1           |     |            |      |
| Switch(config-vlan-1)#: |        |      | description |     | Management | VLAN |
| Switch(config-vlan-1)#: |        |      | end         |     |            |      |
Switch#
!
| Switch(config)#:    |     | interface |             | 1/1/1   |            |      |
| ------------------- | --- | --------- | ----------- | ------- | ---------- | ---- |
| Switch(config-if)#: |     |           | description | IN-BAND | Management | Port |
| Switch(config-if)#: |     |           | vlan access | 1       |            |      |
| Switch(config-if)#: |     |           | no shutdown |         |            |      |
| Switch(config-if)#: |     |           | end         |         |            |      |
Switch#
!
| Switch(config)#: |     | interface |     | vlan 1 |     |     |
| ---------------- | --- | --------- | --- | ------ | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | ip  | dhcp     |     |     |
| ------------------------ | --- | --- | --- | -------- | --- | --- |
| Switch(config-if-vlan)#: |     |     | no  | shutdown |     |     |
| Switch(config-if-vlan)#: |     |     | end |          |     |     |
Switch#
!
WithoutDHCPConfiguration
| switch#:                | config |      |             |     |            |      |
| ----------------------- | ------ | ---- | ----------- | --- | ---------- | ---- |
| switch(config)#:        |        | vlan | 1           |     |            |      |
| Switch(config-vlan-1)#: |        |      | description |     | Management | VLAN |
| Switch(config-vlan-1)#: |        |      | end         |     |            |      |
Switch#
!
| Switch(config)#:    |     | interface |             | 1/1/1   |            |      |
| ------------------- | --- | --------- | ----------- | ------- | ---------- | ---- |
| Switch(config-if)#: |     |           | description | IN-BAND | Management | Port |
| Switch(config-if)#: |     |           | vlan access | 1       |            |      |
| Switch(config-if)#: |     |           | no shutdown |         |            |      |
| Switch(config-if)#: |     |           | end         |         |            |      |
Switch#
!
| Switch(config)#: |     | interface |     | vlan 1 |     |     |
| ---------------- | --- | --------- | --- | ------ | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | no  | ip dhcp  |                 |     |
| ------------------------ | --- | --- | --- | -------- | --------------- | --- |
| Switch(config-if-vlan)#: |     |     | ip  | address  | 192.168.10.1/24 |     |
| Switch(config-if-vlan)#: |     |     | no  | shutdown |                 |     |
| Switch(config-if-vlan)#: |     |     | end |          |                 |     |
Switch#
| Logging | into | the | switch | for | the first | time |
| ------- | ---- | --- | ------ | --- | --------- | ---- |
26
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

Thefirsttimeyoulogintotheswitchyoumustusethedefaultadministratoraccount.Thisaccounthasno
password,soyouwillbepromptedonlogintodefineonetosafeguardtheswitch.
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
whereswitchisthemodelnumberoftheswitch.Enterthecommandconfigtochangetotheglobal
configurationcontextconfig.
Forexample:
|     | switch# | config |     |     |     |
| --- | ------- | ------ | --- | --- | --- |
switch(config)#
| Setting | switch | time | using | the NTP client |     |
| ------- | ------ | ---- | ----- | -------------- | --- |
Prerequisites
n TheIPaddressordomainnameofanNTPserver.
n IftheNTPserverusesauthentication,obtainthepasswordrequiredtocommunicatewiththeNTP
server.
Procedure
1. IftheNTPserverrequiresauthentication,definetheauthenticationkeyfortheNTPclientwiththe
|     | commandntp                            | authentication. |     |         |     |
| --- | ------------------------------------- | --------------- | --- | ------- | --- |
| 2.  | ConfigureanNTPserverwiththecommandntp |                 |     | server. |     |
3. Bydefault,NTPtrafficissentonthedefaultVRF.IfyouwanttosendNTPtrafficonthemanagement
|     | VRF,usethecommandntp |     | vrf. |     |     |
| --- | -------------------- | --- | ---- | --- | --- |
4. ReviewyourNTPconfigurationsettingswiththecommandsshow ntp serversandshow ntp
status.
5. Seethecurrentswitchtime,date,andtimezonewiththecommandshow clock.
Example
InitialConfiguration |27

Thisexamplecreatesthefollowingconfiguration:
Definestheauthenticationkey1withthepasswordmyPassword.
n
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
|     | >> As   | you can       | see | it may | span | multiple  | lines     | and | the input |     |
| --- | ------- | ------------- | --- | ------ | ---- | --------- | --------- | --- | --------- | --- |
|     | >> will | be terminated |     | when   | the  | delimiter | character |     | is        |     |
>> encountered.^
|     | Banner | updated | successfully! |     |     |     |     |     |     |     |
| --- | ------ | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
2. Configurethebannerthatisdisplayedafterauserisauthenticated.Usethecommandbanner exec.
Forexample:
|     | switch(config)# |     | banner | exec | &   |     |     |     |     |     |
| --- | --------------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- |
Enter a new banner. Terminate the banner with the delimiter you have chosen.
|     | >> This | is an  | example | of   | a different |           | banner | text. | This     | time |
| --- | ------- | ------ | ------- | ---- | ----------- | --------- | ------ | ----- | -------- | ---- |
|     | >> the  | banner | entered | will | be          | displayed | after  | a     | user has |      |
>> authenticated.
>>
>> & This text will not be included because it comes after the '&'
|             | Banner | updated | successfully! |            |     |     |     |     |        |      |
| ----------- | ------ | ------- | ------------- | ---------- | --- | --- | --- | --- | ------ | ---- |
| Configuring |        | in-band |               | management |     |     |     | on  | a data | port |
Prerequisites
n AconnectiontotheCLIviaeithertheconsoleportorthemanagementport
n Ethernetcable
Procedure
1. UseanEthernetcabletoconnectadataporttoyournetwork.
2. Configurealayer3interfaceonthedataport.
3. EnableSSHsupportontheinterface(onthedefaultVRF)withthecommandssh server vrf
default.
28
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |

Forexample:
|     | switch# config  |            |             |     |
| --- | --------------- | ---------- | ----------- | --- |
|     | switch(config)# | ssh server | vrf default |     |
4. EnabletheWebUIontheinterface(onthedefaultVRF)withthecommandhttps-server vrf
default.
Forexample:
|       | switch(config)# | https-server | vrf default |     |
| ----- | --------------- | ------------ | ----------- | --- |
| Using | the             | Web UI       |             |     |
TheWebUIisdisabledbydefault.Followthesestepstoenableitonthemanagementportandlogin.
TheWebUIisenabledbydefaultonthedefaultVRF.
Prerequisites
n AconnectiontotheswitchCLI.
Procedure
1. LogintotheCLI.
2. SwitchtoconfigcontextandenabletheWebUIonthemanagementportVRFwiththecommand
|     | https-server | vrf mgmt. |     |     |
| --- | ------------ | --------- | --- | --- |
Forexample:
|     | switch#         | config       |          |     |
| --- | --------------- | ------------ | -------- | --- |
|     | switch(config)# | https-server | vrf mgmt |     |
3. StartyourwebbrowserandentertheIPaddressofthemanagementportintheaddressbar,
|     | Forexample: | https://192.168.1.1 |     |     |
| --- | ----------- | ------------------- | --- | --- |
4. TheWebUIstartsandyouarepromptedtologin.
| Configuring |     | the management |     | interface |
| ----------- | --- | -------------- | --- | --------- |
Prerequisites
Aconnectiontotheconsoleport.
Procedure
1. Switchtothemanagementinterfacecontextwiththecommandinterface mgmt.
2. Bydefault,themanagementinterfaceonthemanagementportisenabled.Ifitwasdisabled,re-
|     | enableitwiththecommandno |     | shutdown. |     |
| --- | ------------------------ | --- | --------- | --- |
3. Usethecommandip dhcptoconfigurethemanagementinterfacetoautomaticallyobtainan
addressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastaticIPv4orIPv6
address,defaultgateway,andDNSserverwiththecommandsip address,ipv6 address,ip
static,default-gateway,andnameserver.
4. SSHisenabledbydefaultonthemanagementVRF.Ifdisabled,enableSSHwiththecommandssh
|     | server vrf | mgmt. |     |     |
| --- | ---------- | ----- | --- | --- |
Examples
InitialConfiguration |29

ThisexampleenablesthemanagementinterfacewithdynamicaddressingusingDHCP:
| switch(config)#         | interface |     | mgmt     |     |     |     |
| ----------------------- | --------- | --- | -------- | --- | --- | --- |
| switch(config-if-mgmt)# |           | no  | shutdown |     |     |     |
| switch(config-if-mgmt)# |           | ip  | dhcp     |     |     |     |
Thisexampleenablesthemanagementinterfacewithstaticaddressingcreatingthefollowingconfiguration:
n SetsastaticIPv4addressof198.168.100.10withamaskof24bits.
n Setsthedefaultgatewayto198.168.100.200.
SetstheDNSserverto198.168.100.201.
n
switch(config)#
|                         | interface  |                 | mgmt     |                   |     |     |
| ----------------------- | ---------- | --------------- | -------- | ----------------- | --- | --- |
| switch(config-if-mgmt)# |            | no              | shutdown |                   |     |     |
| switch(config-if-mgmt)# |            | ip              | static   | 198.168.100.10/24 |     |     |
| switch(config-if-mgmt)# |            | default-gateway |          | 198.168.100.200   |     |     |
| switch(config-if-mgmt)# |            | nameserver      |          | 198.168.100.201   |     |     |
| Selecting               | the system |                 | profile  |                   |     |     |
Systemprofilessettheoverallcapabilitiesandcapacitiesoftheswitch,basedontheselectedprofileusedat
boottime.Systemprofilessetcapacitiessuchasthatofthehardwareforwardingtable.
Systemprofilesprovideyouwiththeflexibilitytoconfigureswitchesbasedontheirlocationinthenetwork
(forexample,core,spine,leaf).Whenaswitchbootswithoutaprofilespecificallyconfigured,itbootswith
thedefaultprofile.Whenaswitchisconfiguredwithanon-defaultprofile,theswitchrequiresarebootfor
theprofiletobeapplied.
Procedure
1. Setthesystemprofilewiththecommandprofile.
2. Reboottheswitchfortheprofilechangetotakeeffectwiththecommandboot system.
Examples
| Restoring | the switch |     | to  | factory | default | settings |
| --------- | ---------- | --- | --- | ------- | ------- | -------- |
Prerequisites
YouareconnectedtotheswitchthroughitsConsoleport.
ThisprocedureerasesalluserinformationandconfigurationsettingsConsiderbackingupyourrunning
configurationfirst.
1. Optionally,backuptherunningconfigurationwitheithercopy running-config <REMOTE-URL>or
copy running-config <STORAGE-URL>.Thejsonstorageformatisrequiredforlaterconfiguration
restoration.
2. Switchtotheconfigurationcontextwiththecommandconfig.
30
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- | --- |

3. Erasealluserinformationandconfiguration,restoringtheswitchtoitsfactorydefaultstatewiththe
commanderase all zeroize.EnterYwhenpromptedtocontinue.Theswitchautomatically
restarts.
4. Optionallyrestoreyoursavedconfiguration(itmustbeinjsonformat)witheithercopy <REMOTE-
|      | running-configorcopy |     |     |               |     |     | running-configfollowedbycopy |     |     |     |                |
| ---- | -------------------- | --- | --- | ------------- | --- | --- | ---------------------------- | --- | --- | --- | -------------- |
| URL> |                      |     |     | <STORAGE-URL> |     |     |                              |     |     |     | running-config |
startup-config.
Example
Backinguptherunningconfigurationtoafileonaremoteserver(usingTFTP),resettingtheswitchtoits
factorydefaultstate,andthenrestoringthesavedconfiguration.
switch# copy running-config tftp://192.168.1.10/backup_cfg json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload |     | Upload | Total | Spent | Left | Speed |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ----- | ----- | ---- | ----- |
100 10340 0 0 100 10340 0 1329k --:--:-- --:--:-- --:--:-- 1329k
100 10340 0 0 100 10340 0 1313k --:--:-- --:--:-- --:--:-- 1313k
switch#
switch#
switch#
|             | erase       | all zeroize |        |                  |          |      |              |              |            |     |     |
| ----------- | ----------- | ----------- | ------ | ---------------- | -------- | ---- | ------------ | ------------ | ---------- | --- | --- |
| This will   | securely    |             | erase  | all customer     |          | data | and          | reset        | the switch |     |     |
| to factory  | defaults.   |             | This   | will             | initiate |      | a reboot     | and          | render the |     |     |
| switch      | unavailable |             | until  | the zeroization  |          |      | is complete. |              |            |     |     |
| This should | take        | several     |        | minutes          | to       | one  | hour         | to complete. |            |     |     |
| Continue    | (y/n)?      | y           |        |                  |          |      |              |              |            |     |     |
| The system  | is          | going       | down   | for zeroization. |          |      |              |              |            |     |     |
| [  OK       | ] Stopped   | PSPO        | Module | Daemon.          |          |      |              |              |            |     |     |
| [  OK       | ] Stopped   | AOS-CX      |        | Switch           | Daemon   | for  | BCM.         |              |            |     |     |
...
| [  OK     | ] Stopped    | Remount |                                                   | Root      | and Kernel |     | File | Systems. |     |     |     |
| --------- | ------------ | ------- | ------------------------------------------------- | --------- | ---------- | --- | ---- | -------- | --- | --- | --- |
| [  OK     | ] Reached    | target  |                                                   | Shutdown. |            |     |      |          |     |     |     |
| reboot:   | Restarting   |         | system                                            |           |            |     |      |          |     |     |     |
| Press Esc | for          | boot    | options                                           |           |            |     |      |          |     |     |     |
| ServiceOS | Information: |         |                                                   |           |            |     |      |          |     |     |     |
| Version:  |              |         | GT.01.03.0006                                     |           |            |     |      |          |     |     |     |
| Build     | Date:        |         | 2018-10-30                                        |           | 14:20:44   |     | PDT  |          |     |     |     |
| Build     | ID:          |         | ServiceOS:GT.01.03.0006:8ee0faaa52da:201810301420 |           |            |     |      |          |     |     |     |
| SHA:      |              |         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx          |           |            |     |      |          |     |     |     |
...
| ################ |     | Preparing |        | for         | zeroization                 |                         | ################# |     |            |     |     |
| ---------------- | --- | --------- | ------ | ----------- | --------------------------- | ----------------------- | ----------------- | --- | ---------- | --- | --- |
| ################ |     | Storage   |        | zeroization |                             | ####################### |                   |     |            |     |     |
| ################ |     | WARNING:  |        | DO NOT      | POWER                       | OFF                     | UNTIL             |     | ########## |     |     |
| ################ |     |           |        | ZEROIZATION |                             | IS                      | COMPLETE          |     | ########## |     |     |
| ################ |     | This      | should | take        | several                     |                         | minutes           |     | ########## |     |     |
| ################ |     | to        | one    | hour to     | complete                    |                         |                   |     | ########## |     |     |
| ################ |     | Restoring |        | files       | ########################### |                         |                   |     |            |     |     |
Boot Profiles:
| 0. Service   | OS       | Console |       |                 |     |     |     |     |     |     |     |
| ------------ | -------- | ------- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| 1. Primary   | Software |         | Image | [XL.10.02.0010] |     |     |     |     |     |     |     |
| 2. Secondary | Software |         | Image | [XL.10.02.0010] |     |     |     |     |     |     |     |
Select profile(primary):
| Booting   | primary  | software |     | image... |     |     |     |     |     |     |     |
| --------- | -------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Verifying | Image... |          |     |          |     |     |     |     |     |     |     |
InitialConfiguration |31

| Image Info: |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
Name: AOS-CX
Version: XL.10.02.0010
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
AssignsanIPv4orIPv6defaultgatewaytothemanagementinterface.AnIPv4defaultgatewaycanonlybe
configuredifastaticIPv4addresswasassignedtothemanagementinterface.AnIPv6defaultgatewaycan
onlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.Thedefaultgateway
shouldbeonthesamenetworksegment.
Thenoformofthiscommandremovesthedefaultgatewayfromthemanagementinterface.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
SettingadefaultgatewaywiththeIPv4addressof198.168.5.1:
32
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- |

| switch(config)# | interface | mgmt |     |
| --------------- | --------- | ---- | --- |
switch(config-if-mgmt)#
|     |     | default-gateway | 198.168.5.1 |
| --- | --- | --------------- | ----------- |
SettinganIPv6addressof2001:DB8::1:
| switch(config)#         | interface | mgmt            |             |
| ----------------------- | --------- | --------------- | ----------- |
| switch(config-if-mgmt)# |           | default-gateway | 2001:DB8::1 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-if-mgmt
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
ip static
| ip static <IP-ADDR>/<MASK> |                  |     |     |
| -------------------------- | ---------------- | --- | --- |
| no ip static               | <IP-ADDR>/<MASK> |     |     |
Description
AssignsanIPv4orIPv6addresstothemanagementinterface.
ThenoformofthiscommandremovestheIPaddressfromthemanagementinterfaceandsetsthe
interfacetooperateasaDHCPclient.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| <MASK> |     |     | SpecifiesthenumberofbitsinanIPv4orIPv6addressmaskin |
| ------ | --- | --- | --------------------------------------------------- |
CIDRformat(x),wherexisadecimalnumberfrom0to32for
IPv4,and0to128forIPv6.
Examples
SettinganIPv4addressof198.51.100.1withamaskof24bits:
| switch(config)#         | interface | mgmt      |                 |
| ----------------------- | --------- | --------- | --------------- |
| switch(config-if-mgmt)# |           | ip static | 198.51.100.1/24 |
SettinganIPv6addressof2001:DB8::1withamaskof32bits:
InitialConfiguration |33

| switch(config)# |     | interface | mgmt |     |     |
| --------------- | --- | --------- | ---- | --- | --- |
switch(config-if-mgmt)#
|     |     |     | ip static | 2001:DB8::1/32 |     |
| --- | --- | --- | --------- | -------------- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
nameserver
| nameserver    | <PRIMARY-IP-ADDR> |     | [ <SECONDARY-IP-ADDR> |     | ]   |
| ------------- | ----------------- | --- | --------------------- | --- | --- |
| no nameserver | <PRIMARY-IP-ADDR> |     | [ <SECONDARY-IP-ADDR> |     | ]   |
Description
AssignsaprimaryorsecondaryIPv4orIPv6DNSservertothemanagementinterface.IPv4DNSserverscan
onlybeconfiguredifastaticIPv4addresswasassignedtothemanagementinterface.IPv6DNSserverscan
onlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.Thedefaultgateway
shouldbeonthesamenetworksegment.
ThenoformofthiscommandremovestheDNSserversfromthemanagementinterface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<PRIMARY-IP-ADDR>
SpecifiestheIPaddressoftheprimaryDNSserver.Specifythe
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
| switch(config)#         |     | interface | mgmt       |             |             |
| ----------------------- | --- | --------- | ---------- | ----------- | ----------- |
| switch(config-if-mgmt)# |     |           | nameserver | 198.168.5.1 | 198.168.5.2 |
SettingprimaryandsecondaryDNSserverswiththeIPv6addressesof2001:DB8::1and2001:DB8::2:
34
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| switch(config)# |     | interface | mgmt |     |     |
| --------------- | --- | --------- | ---- | --- | --- |
switch(config-if-mgmt)#
|     |     |     | nameserver | 2001:DB8::1 | 2001:DB8::2 |
| --- | --- | --- | ---------- | ----------- | ----------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
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
| switch#                  | show interface |                 | mgmt |                              |     |
| ------------------------ | -------------- | --------------- | ---- | ---------------------------- | --- |
| Address                  | Mode           |                 |      | : static                     |     |
| Admin                    | State          |                 |      | : up                         |     |
| Mac Address              |                |                 |      | : 02:42:ac:11:00:02          |     |
| IPv4 address/subnet-mask |                |                 |      | : 192.168.1.10/16            |     |
| Default                  | gateway        | IPv4            |      | : 192.168.1.1                |     |
| IPv6 address/prefix      |                |                 |      | : 2001:db8:0:1::129/64       |     |
| IPv6 link                | local          | address/prefix: |      | fe80::7272:cfff:fefd:e485/64 |     |
| Default                  | gateway        | IPv6            |      | : 2001:db8:0:1::1            |     |
| Primary                  | Nameserver     |                 |      | : 2001::1                    |     |
| Secondary                | Nameserver     |                 |      | : 2001::2                    |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
InitialConfiguration |35

| Platforms | Commandcontext |     | Authority                                            |     |     |
| --------- | -------------- | --- | ---------------------------------------------------- | --- | --- |
| 6300      |                |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Manager(#)
| 6400 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | ----------------------------------------------------- | --- | --- |
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
| switch(config)# |     | no ntp authentication |     |     |     |
| --------------- | --- | --------------------- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp authentication-key
| ntp authentication-key    |     | <KEY-ID>  | {md5 | sha1} |                 |     |
| ------------------------- | --- | --------- | ------------ | --------------- | --- |
| [{ <PLAINTXT-KEY>         |     | [trusted] | | ciphertext | <ENCRYPTED-KEY> | }]  |
| no ntp authentication-key |     | <KEY-ID>  | {md5 |       | sha1}           |     |
| [{ <PLAINTXT-KEY>         |     | [trusted] | | ciphertext | <ENCRYPTED-KEY> | }]  |
Description
DefinesanauthenticationkeythatisusedtosecuretheexchangewithanNTPtimeserver.Thiscommand
providesprotectionagainstaccidentallysynchronizingtoatimesourcethatisnottrusted.
Thenoformofthiscommandremovestheauthenticationkey.
36
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

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
| ciphertext | <ENCRYPTED-KEY> |     |     |     |     |
| ---------- | --------------- | --- | --- | --- | --- |
SpecifiestheciphertextauthenticationkeyinBase64format.This
isusedtorestoretheNTPauthenticationkeywhencopying
configurationfilesbetweenswitchesorwhenuploadinga
previouslysavedconfiguration.
NOTE:
Whenthekeyisnotprovidedonthecommandline,plaintextkey
promptingoccursuponpressingEnter,followedbypromptingasto
whetherthekeyistobetrusted.Theenteredkeycharactersaremasked
withasterisks.
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
| switch(config)# | no  | ntp authentication-key |     | 10  |     |
| --------------- | --- | ---------------------- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
InitialConfiguration |37

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp disable
ntp disable
Description
DisablestheNTPclientontheswitch.TheNTPclientisdisabledbydefault.
Examples
DisablingtheNTPclient.
| switch(config)# | ntp disable |     |
| --------------- | ----------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp enable
ntp enable
no ntp enable
Description
EnablestheNTPclientontheswitchtoautomaticallyadjustthelocaltimeanddateontheswitch.TheNTP
clientisdisabledbydefault.
ThenoformofthiscommanddisablestheNTPclient.
Examples
EnablingtheNTPclient.
| switch(config)# | ntp enable |     |
| --------------- | ---------- | --- |
DisablingtheNTPclient.
| switch(config)# | no ntp enable |     |
| --------------- | ------------- | --- |
38
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp conductor
| ntp conductor    | vrf | <VRF-NAME>     | {stratum | <NUMBER>] |     |
| ---------------- | --- | -------------- | -------- | --------- | --- |
| no ntp conductor |     | vrf <VRF-NAME> | {stratum | <NUMBER>] |     |
Description
SetstheswitchastheconductortimesourceforNTPclientsonthespecifiedVRF.Bydefault,theswitch
operatesatstratumlevel8.TheswitchcannotfunctionasbothNTPconductorandclientonthesameVRF.
Thenoformofthiscommandstopstheswitchfromoperatingastheconductortimesourceonthe
specifiedVRF.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vrf <VRF-NAME> SpecifiestheVRFonwhichtoactasconductortimesource.
stratum <NUMBER> Specifiesthestratumlevelatwhichtheswitchoperates.Range:1-
15.Default:8.
Examples
SettingtheswitchtoactasconductortimesourceonVRFprimary-vrfwithastratumlevelof9.
| switch(config)# |     | ntp conductor |     | vrf primary-vry | statum 9 |
| --------------- | --- | ------------- | --- | --------------- | -------- |
StopstheswitchfromactingasconductortimesourceonVRFprimary-vrf.
| switch(config)# |     | no ntp | conductor | vrf primary-vry |     |
| --------------- | --- | ------ | --------- | --------------- | --- |
CommandHistory
| Release        |     |     |     | Modification       |     |
| -------------- | --- | --- | --- | ------------------ | --- |
| 10.08          |     |     |     | Inclusivelanguage. |     |
| 10.07orearlier |     |     |     | --                 |     |
CommandInformation
InitialConfiguration |39

Platforms

Command context

Authority

6300
6400

config

Administrators or local user group members with execution rights
for this command.

ntp server
ntp server <IP-ADDR> [key <KEY-NUM>] [minpoll <MIN-NUM>] [maxpoll <MAX-NUM>][burst | iburst]
[prefer] [version <VER-NUM>]
no ntp server <IP-ADDR> <IP-ADDR> [key <KEY-NUM>] [minpoll <MIN-NUM>] [maxpoll <MAX-NUM>]
[burst | iburst] [prefer] [version <VER-NUM>]

Description

Defines an NTP server to use for time synchronization, or updates the settings of an existing server with
new values. Up to eight servers can be defined.

The no form of this command removes a configured NTP server.

The default NTP version is 4; it is backwards compatible with version 3.

Parameter

server <IP-ADDR>

key <KEY-NUM>

minpoll <MIN-NUM>

maxpoll <MAX-NUM>

burst

iburst

Description

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

Specifies the minimum polling interval in seconds, as a power of 2.
Range: 4 to 17. Default: 6 (64 seconds).

Specifies the maximum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 10 (1024 seconds).

Send a burst of packets instead of just one when connected to the
server. Useful for reducing phase noise when the polling interval is
long.

Send a burst of six packets when not connected to the server.
Useful for reducing synchronization time at startup.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

40

| Parameter |     | Description                 |     |     |
| --------- | --- | --------------------------- | --- | --- |
| prefer    |     | Makethisthepreferredserver. |     |     |
version <VER-NUM> SpecifiestheversionnumbertouseforalloutgoingNTPpackets.
Range:3or4.Default:4.
NOTE:NTPisbackwardscompatible.
Usage
ForfeaturessuchasActivateandZTP,aswitchthathasafactorydefaultconfigurationwillautomaticallybe
configuredwithpool.ntp.org.NTPserverconfigurationsviaDHCPoptionsaresupported.TheDHCPserver
canbeconfiguredwithmaximumoftwoNTPserveraddresseswhichwillbesupportedontheswitch.Only
IPV4addressesaresupported.
NTPusesastratumtodescribethedistancebetweenanetworkdeviceandanauthoritativetimesource:
n Astratum1timeserverisdirectlyattachedtoanauthoritativetimesource(suchasaradiooratomic
clockoraGPStimesource).
n Astratum2NTPserverreceivesitstimethroughNTPfromastratum1timeserver.
Whenusingmultipleserverswithsamestratumsetting,thebestpracticetoconfigureapreferredserver,so
NTPwillattempttousethepreferredserverastheprimaryNTPconnection.Ifapreferredserverisnot
manuallysetwhenNTPisenabled,theconfiguredserverwiththeloweststratumwillautomaticallybesetas
thepreferredserver.Ifthereareserverswiththesamestratum,thisautopreferstatuswillpreventAOS-CX
fromtogglingbetweendifferentserversastheprimaryserver.Autopreferselectionofserverswithsame
stratum(ifnotmanuallyselected)maychangeafterreconfiguringtheswitch,orafterexecutingthereboot
command.
Examples
Definingthentpserverpool.ntp.org,usingiburst,andNTPversion4.
| switch(config)# | ntp server | pool.ntp.org | iburst version | 4   |
| --------------- | ---------- | ------------ | -------------- | --- |
Removingthentpserverpool.ntp.org.
| switch(config)# | no ntp server | pool.ntp.org |     |     |
| --------------- | ------------- | ------------ | --- | --- |
Definingthentpservermy-ntp.mydomain.comandmakesitthepreferredserver.
| switch(config)# | ntp server | my-ntp.mydomain.com | prefer |     |
| --------------- | ---------- | ------------------- | ------ | --- |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
InitialConfiguration |41

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp trusted-key
| ntp trusted-key    | <KEY-ID> |     |
| ------------------ | -------- | --- |
| no ntp trusted-key | <KEY-ID> |     |
Description
Setsakeyastrusted.WhenNTPauthenticationisenabled,theswitchonlysynchronizeswithtimeservers
thattransmitpacketscontainingatrustedkey.
Thenoformofthiscommandremovesthetrusteddesignationfromakey.
| Parameter |     | Description |
| --------- | --- | ----------- |
<KEY-ID> Specifiestheidentificationnumberofthekeytosetastrusted.
Range:1to65534.
Examples
Definingkey10asatrustedkey.
| switch(config)# | ntp trusted-key | 10  |
| --------------- | --------------- | --- |
Removingtrusteddesignationfromkey10:
switch(config)#
|     | no ntp trusted-key | 10  |
| --- | ------------------ | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp vrf
ntp vrf <VRF-NAME>
| no ntp vrf <VRF-NAME> |     |     |
| --------------------- | --- | --- |
Description
SpecifiestheVRFonwhichtheNTPclientcommunicateswithanNTPserver.Theswitchcannotfunctionas
bothNTPconductorandclientonthesameVRF.
ThenoformofthecommandreturnstodefaultVRF.
42
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| Parameter  |     | Description             |
| ---------- | --- | ----------------------- |
| <VRF-NAME> |     | SpecifiesthenameofaVRF. |
Example
SettingtheswitchtousethedefaultVRFforNTPclienttraffic.
| switch(config)# | ntp vrf default |     |
| --------------- | --------------- | --- |
SettingtheswitchtousethedefaultmanagementVRFforNTPclienttraffic.
| switch(config)# | ntp vrf mgmt |     |
| --------------- | ------------ | --- |
ReturningtheswitchtousethedefaultVRFforNTPclienttraffic.
| switch(config)# | no ntp vrf |     |
| --------------- | ---------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ntp              | associations |     |
| --------------------- | ------------ | --- |
| show ntp associations | [vsx-peer]   |     |
Description
ShowsthestatusoftheconnectiontoeachNTPserver.Thefollowinginformationisdisplayedforeach
server:
n Tallycode:ThefirstcharacteristheTallycode:
o (blank):Nostateinformationavailable(e.g.non-respondingserver)
x:Outoftolerance(discardedbyintersectionalgorithm)
o
o .:Discardedbytableoverflow(notused)
o -:Outoftolerance(discardedbytheclusteralgorithm)
+:Goodandapreferredremotepeerorserver(includedbythecombinealgorithm)
o
o #:Goodremotepeerorserver,butnotutilized(readyasabackupsource)
o *:Remotepeerorserverpresentlyusedasaprimaryreference
o o:PPSpeer(whenthepreferpeerisvalid)
InitialConfiguration |43

ID:Servernumber.
n
NAME:NTPserverFQDN/IPaddress(Onlythefirst24charactersofthenamearedisplayed).
n
REMOTE:RemoteserverIPaddress.
n
n REF_ID:ReferenceIDfortheremoteserver(CanbeanIPaddress).
n ST:(Stratum)NumberofhopsbetweentheNTPclientandthereferenceclock.
n LAST:Timesincethelastpacketwasreceivedinsecondsunlessanotherunitisindicated.
n POLL:Interval(inseconds)betweenNTPpollpackets.Maximum(1024)reachedasserverandclient
sync.
n REACH:8-bitoctalnumberthatdisplaysstatusofthelasteightNTPmessages(377=allmessages
received).
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# | show ntp associations |     |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------
| ID  | NAME | REMOTE |     | REF-ID | ST LAST POLL | REACH |
| --- | ---- | ------ | --- | ------ | ------------ | ----- |
----------------------------------------------------------------------
| 1                  | 192.0.1.1 | 192.0.1.1    |     | .INIT. | 16 -     | 64 0 |
| ------------------ | --------- | ------------ | --- | ------ | -------- | ---- |
| * 2 time.apple.com |           | 17.253.2.253 |     | .GPSs. | 2 70 128 | 377  |
----------------------------------------------------------------------
CommandHistory
| Release        |     |     | Modification |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp                     | authentication-keys |            |     |     |     |     |
| ---------------------------- | ------------------- | ---------- | --- | --- | --- | --- |
| show ntp authentication-keys |                     | [vsx-peer] |     |     |     |     |
Description
Showsthecurrentlydefinedauthenticationkeys.
44
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- | --- |

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# |     | show ntp | authentication-keys |     |     |
| ------- | --- | -------- | ------------------- | --- | --- |
--------------------------------
| Auth | key | Trusted | MD5 password |     |     |
| ---- | --- | ------- | ------------ | --- | --- |
--------------------------------
| 10  |     | No  | ********** |     |     |
| --- | --- | --- | ---------- | --- | --- |
| 20  |     | Yes | ********** |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ntp | servers |     |     |     |
| ---- | --- | ------- | --- | --- | --- |
show ntp servers[vsx-peer]
Description
ShowsallconfiguredNTPservers,includinganyDHCPservers,defaultpoolserversoranyserverwiththe
statusautoprefer.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# |     | show ntp | servers |     |     |
| ------- | --- | -------- | ------- | --- | --- |
------------------------------------------------
|     | NTP | SERVER KEYID | MINPOLL | MAXPOLL OPTION | VER |
| --- | --- | ------------ | ------- | -------------- | --- |
------------------------------------------------
|     | 192.0.1.18 |     | -   | 5 10 iburst | 3   |
| --- | ---------- | --- | --- | ----------- | --- |
|     | 192.0.1.19 |     | -   | 6 10 none   | 4   |
InitialConfiguration |45

| 192.0.1.20 | - 6 | 8 burst | 3 prefer |
| ---------- | --- | ------- | -------- |
------------------------------------------------
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp            | statistics |     |     |
| ------------------- | ---------- | --- | --- |
| show ntp statistics | [vsx-peer] |     |     |
Description
ShowsglobalNTPstatistics.Thefollowinginformationisdisplayed:
n Rx-pkts:TotalNTPpacketsreceived.
n CurrentVersionRx-pkts:NumberofNTPpacketsthatmatchthecurrentNTPversion.
OldVersionRx-pkts:NumberofNTPpacketsthatmatchthepreviousNTPversion.
n
Errorpkts:Packetsdroppedduetoallothererrorreasons.
n
Auth-failedpkts:Packetsdroppedduetoauthenticationfailure.
n
n Declinedpkts:Packetsdeniedaccessforanyreason.
n Restrictedpkts:PacketsdroppedduetoNTPaccesscontrol.
n Rate-limitedpkts:Numberofpacketsdiscardedduetoratelimitation.
n KODpkts:NumberofKissofDeathpacketssent.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch(config)# | show ntp statistics |     |     |
| --------------- | ------------------- | --- | --- |
Rx-pkts 100
| Current | Version Rx-pkts 80 |     |     |
| ------- | ------------------ | --- | --- |
| Old     | Version Rx-pkts 20 |     |     |
Err-pkts 2
Auth-failed-pkts 1
Declined-pkts 0
46
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

|                   | Restricted-pkts |          | 0   |     |     |
| ----------------- | --------------- | -------- | --- | --- | --- |
| Rate-limited-pkts |                 |          | 0   |     |     |
|                   |                 | KoD-pkts | 0   |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp        | status     |     |     |     |     |
| --------------- | ---------- | --- | --- | --- | --- |
| show ntp status | [vsx-peer] |     |     |     |     |
Description
ShowsthestatusofNTPontheswitch.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingthestatusinformationwhentheswitchisnotsyncedtoanNTPserver:
| switch#            | show ntp    | status  |                |             |              |
| ------------------ | ----------- | ------- | -------------- | ----------- | ------------ |
| NTP is enabled.    |             |         |                |             |              |
| NTP authentication |             | is      | enabled.       |             |              |
| NTP is using       | the         | default | VRF for        | NTP server  | connections. |
| Wed Nov            | 23 23:29:10 | PDT     | 2016           |             |              |
| NTP uptime:        | 187         | days,   | 1 hours,       | 37 minutes, | 48 seconds   |
| Not synchronized   |             | with    | an NTP server. |             |              |
DisplayingthestatusinformationwhentheswitchissyncedtoanNTPserver:
| switch#            | show ntp | status  |          |            |              |
| ------------------ | -------- | ------- | -------- | ---------- | ------------ |
| NTP is enabled.    |          |         |          |            |              |
| NTP authentication |          | is      | enabled. |            |              |
| NTP is using       | the      | default | VRF for  | NTP server | connections. |
InitialConfiguration |47

| Wed Nov       | 23 23:29:10 | PDT      | 2016          |             |     |            |
| ------------- | ----------- | -------- | ------------- | ----------- | --- | ---------- |
| NTP uptime:   | 187 days,   | 1        | hours,        | 37 minutes, |     | 48 seconds |
| Synchronized  | to NTP      | Server   | 17.253.2.253  |             | at  | stratum 2. |
| Poll interval | = 1024      | seconds. |               |             |     |            |
| Time accuracy | is          | within   | 0.994 seconds |             |     |            |
| Reference     | time: Thu   | Jan      | 28 2016       | 0:57:06.647 |     | (UTC)      |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
48
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

Chapter 4
Telnet access
| Telnet | access |     |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- | --- |
TelnetserverenablesswitchestoacceptTelnetconnectionsfromclientstomanagetheswitch.Theuser
authenticationispasswordbasedauthentication(RADIUS,TACACS+orlocallystoredpassword).Theserver
canbeimplementedonanyVRFusingthetelnet servercommand.Themaximumnumberofsessionsper
VRF isfive(5).
Inthedefaultconfiguration,Telnetaccessisdisabled.
| Telnet | commands |        |     |     |     |     |
| ------ | -------- | ------ | --- | --- | --- | --- |
| show   | telnet   | server |     |     |     |     |
| show   | telnet   | server |     |     |     |     |
Description
DisplaystheTelnetserverconfiguration.
Examples
DisplaytheTelnetserverconfigurationontheswitch:
| switch(config)# |            | show           | telnet     | server |       |       |
| --------------- | ---------- | -------------- | ---------- | ------ | ----- | ----- |
| TELNET          | Server     | Configuration: |            |        |       |       |
|                 | IP Version |                | : IPv4     |        |       |       |
|                 | TCP        | Port           | : 23       |        |       |       |
|                 | Enabled    | VRFs           | : default, |        | vrf1, | vrf2, |
red, green
CommandHistory
| Release    |     |     |     |     | Modification      |     |
| ---------- | --- | --- | --- | --- | ----------------- | --- |
| 10.08.1021 |     |     |     |     | Commandintroduced |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
| show | telnet | server          | sessions |      |            |             |
| ---- | ------ | --------------- | -------- | ---- | ---------- | ----------- |
| show | telnet | server sessions |          | [vrf | <VRF-NAME> | | all-vrfs] |
49
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

Description
DisplaysallactiveTelnetsessionsforthespecifiedVRForallVRFs.IfnoVRFisprovided,thesessiononthe
defaultVRFisshown.
| Parameter      |     | Description                                |     |
| -------------- | --- | ------------------------------------------ | --- |
| vrf <VRF-NAME> |     | SpecifiestheTelnetsessionsforaspecificVRF. |     |
| all-vrfs       |     | SpecifiestheTelnetsessionsforallVRFs       |     |
Examples
DisplaytheTelnetsessiononthedefaultVRF:
| switch(config)# | show telnet      | server sessions |     |
| --------------- | ---------------- | --------------- | --- |
| TELNET sessions | on VRF default:  |                 |     |
| IPv4            | TELNET Sessions: |                 |     |
|                 | Server IP        | : 10.1.1.1      |     |
|                 | Client IP        | : 10.1.1.2      |     |
|                 | Client Port      | : 58835         |     |
DisplaytheTelnetsessiononallVRFs:
| switch(config)# | show telnet      | server sessions | all-vrfs |
| --------------- | ---------------- | --------------- | -------- |
| TELNET sessions | on VRF mgmt:     |                 |          |
| IPv4            | TELNET Sessions: |                 |          |
|                 | Server IP        | : 10.1.1.1      |          |
|                 | Client IP        | : 10.1.1.2      |          |
|                 | Client Port      | : 58835         |          |
| TELNET sessions | on VRF default:  |                 |          |
| IPv4            | TELNET Sessions: |                 |          |
|                 | Server IP        | : 20.1.1.1      |          |
|                 | Client IP        | : 20.1.1.2      |          |
|                 | Client Port      | : 58837         |          |
CommandHistory
| Release    |     | Modification      |     |
| ---------- | --- | ----------------- | --- |
| 10.08.1021 |     | Commandintroduced |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
telnet server
Telnetaccess|50

| telnet    | server vrf | <VRF-NAME>     |     |
| --------- | ---------- | -------------- | --- |
| no telnet | server     | vrf <VRF-NAME> |     |
Description
EnablestheTelnetserveronthedesiredVRF.Telnetisdisabledbydefault.
ThenoformofthiscommanddisablestheTelnetserver.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFonwhichtheTelnetserverwillbeenabled.
Examples
ConfiguringtheTelnetserveronthemgmtVRF:
| switch(config)# |     | telnet server | vrf mgmt |
| --------------- | --- | ------------- | -------- |
CommandHistory
| Release    |     |     | Modification      |
| ---------- | --- | --- | ----------------- |
| 10.08.1021 |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
51
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

Chapter 5
Interface configuration
Interface configuration
| Configuring | a layer | 2 interface |
| ----------- | ------- | ----------- |
Procedure
1. Changetotheinterfaceconfigurationcontextfortheinterfacewiththecommandinterface.
2. SettheinterfaceMTU(maximumtransmissionunit)withthecommandmtu.
3. Reviewinterfaceconfigurationsettingswiththecommandshow interface.
Example
Onthe6300switchseries:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | mtu       | 1900  |
Onthe6400switchseries:
| switch(config)#    | interface | 1/3/1       |
| ------------------ | --------- | ----------- |
| switch(config-if)# | mtu       | 1900        |
| Configuring        | a layer   | 3 interface |
Procedure
1. Changetotheinterfaceconfigurationcontextfortheinterfacewiththecommandinterface.
2. Enableroutingsupportwiththecommandrouting.
3. AssignanIPv4addresswiththecommandip address,oranIPv6addresswiththecommandipv6
address.
4. Ifrequired,enablesupportforlayer3counterswiththecommandl3-counters.
5. Ifrequired,settheIPMTUwiththecommandip mtu.
6. Reviewinterfaceconfigurationsettingswiththecommandshow interface.
Examples
Thisexamplecreatesthefollowingconfigurationonthe6300SwitchSeries:
Configuresinterface1/1/1asalayer3interface.
n
DefinesanIPv4addressof10.10.20.209witha24-bitmask.
n
| switch# config  |           |       |
| --------------- | --------- | ----- |
| switch(config)# | interface | 1/1/1 |
52
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| switch(config-if)# |     | routing    |                 |
| ------------------ | --- | ---------- | --------------- |
| switch(config-if)# |     | ip address | 10.10.20.209/24 |
Thisexamplecreatesthefollowingconfigurationonthe6400SwitchSeries:
Configuresinterface1/3/1asalayer3interface.
n
DefinesanIPv6addressof2001:0db8:85a3::8a2e:0370:7334witha24-bitmask.
n
n Enableslayer3transmitandreceivecounters.
| switch#            | config |           |       |
| ------------------ | ------ | --------- | ----- |
| switch(config)#    |        | interface | 1/3/1 |
| switch(config-if)# |        | routing   |       |
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
| switch(config-if)# |        | l3-counters | tx  |
| ------------------ | ------ | ----------- | --- |
| switch(config-if)# |        | l3-counters | rx  |
| Single             | source | IP address  |     |
CertainIP-basedprotocolsusedbytheswitch(suchasRADIUS,sFlow,TACACS,andTFTP),useaclient-server
modelinwhichtheclient'ssourceIPaddressuniquelyidentifiestheclientinpacketssenttotheserver.By
default,thesourceIPaddressisdefinedastheIPaddressoftheoutgoingswitchinterfaceonwhichthe
clientiscommunicatingwiththeserver.Sincetheswitchcanhavemultipleroutinginterfaces,outgoing
packetscanpotentiallybesentondifferentpathsatdifferenttimes.ThiscanresultindifferentsourceIP
addressesbeingusedforaclient,whichcancreateaclientidentificationproblemontheserver.For
example,itcanbedifficulttointerpretsystemlogsandaccountingdataontheserverwhenthesameclient
isassociatedwithmultipleIPaddresses.
Toresolvethisissue,youcanusethecommandsip source-interfaceandipv6 source-interfaceto
defineasinglesourceIPaddressthatappliestoallsupportedprotocols(RADIUS,sFlow,TACACS,andTFTP),
oranindividualaddressforeachprotocol.Thisensuresthatalltrafficsentbyaclienttoaserverusesthe
sameIPaddress.
| Priority-based |     | flow | control |
| -------------- | --- | ---- | ------- |
Priority-basedflowcontrol(PFC)isdefinedintheIEEE802.1Qbbstandard.Itisalink-levelflowcontrol
mechanismintendedtoeliminatepacketlossduetocongestiononanetworklink.
Forinterfacesthatauto-negotiate,link-levelflowcontrolissubjecttonegotiation,alongwithspeedand
otherparameters.Bothendsofthelinkmustnegotiatethesameflowcontrolmodeforittobeapplied.
Forinterfacesthatdonotauto-negotiate,theconfiguredlink-levelflowcontrolmodeisalwaysappliedand
theuserisresponsibleforensuringthatbothendsofthelinkareconfiguredforthesamemode.
| Forward | error | correction |     |
| ------- | ----- | ---------- | --- |
Appliesonlytothe6300SwitchSeries.
Forwarderrorcorrection(FEC)isusedtocontrolerrorsintransmissionswherethesourcesendsredundant
dataandthedestinationonlyrecognizesthedataportionthatcontainsnoapparenterrors.FECdoesnot
requireahandshakebetweenthesourceanddestinationatthecostofahigherforwardchannel
Interfaceconfiguration|53

bandwidth. It is therefore best used in scenarios where re-transmissions are costly or impossible, such as
using multicast one-way communication.

Unsupported transceiver support
Transceiver products (optical, DAC, AOCs) that are listed as supported by a switch model are detailed in the
Transceiver Guide. Transceiver products that are not listed, are considered unsupported; this would include
transceivers that are:

n Non-Aruba branded products

n HPE branded products that were designed for non-AOS-CX switch models (e.g. Comware)

n HPE branded products designated for use in HPE Compute Servers or Storage

n Transceivers originally designated for use in Aruba WLAN controllers or former Mobility Access Switch

(MAS) products

n End-of-life Aruba Transceivers

The unsupported transceiver mode (UT-mode) is designed to allow the possible use of these unsupported
products. Not all unsupported products can be recognized and enabled; they may be unable to be identified
(do not follow the proper MSA standards for identification). These unsupported transceiver products are
enabled only on a best-effort basis and there are no guarantees implied for their continued operation.

This feature is enabled by default. A periodic system log will be generated by default at an interval of 24
hours listing the ports on which unsupported transceivers are present. The log interval is configurable and
can be disabled by setting the log-interval to none.

Interface commands

allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver

Description

Allows unsupported transceivers to be enabled or establish connections. Only 1G and 10G transceivers are
enabled by this command, unsupported transceivers of other speeds will remain disabled.

As of AOS-CX 10.06.0100, this command is enabled by default, allowing the use of third party transceiver products
without adding the command in the config. Disabling this command with the no form will now display the
command in the running and stored configurations.

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

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

54

Usage
Whennoneoftheparametersarespecifieditwilldisplayawarningmessagetoacceptthewarrantyterms.
Withconfirmoptionthewarningmessageisdisplayedbuttheuserisnotpromptedto(y/n)answering.
Warrantytermsmustbeagreedtoaspartofenablementandthesupportisonbesteffortbasis.
Examples
Allowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | allow-unsupported-transceiver |     |     |     |     |
| --------------- | ----------------------------- | --- | --- | --- | --- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
| Do you agree | and do you | want to continue | (y/n)? | y   |     |
| ------------ | ---------- | ---------------- | ------ | --- | --- |
Allowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | allow-unsupported-transceiver |     |     | confirm |     |
| --------------- | ----------------------------- | --- | --- | ------- | --- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
Configuringunsupportedtransceiverloggingwithanintervalofevery48hours:
| switch(config)# | allow-unsupported-transceiver |     |     | log-interval | 2880 |
| --------------- | ----------------------------- | --- | --- | ------------ | ---- |
Disablingunsupportedtransceiverlogging:
| switch(config)# | allow-unsupported-transceiver |     |     | log-interval | none |
| --------------- | ----------------------------- | --- | --- | ------------ | ---- |
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no allow-unsupported-transceiver |     |     |     |     |
| --------------- | -------------------------------- | --- | --- | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |     |
| ----------- | ----------- | ------------- | --------- | ----- | --- |
| Continue    | (y/n)? y    |               |           |       |     |
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | no allow-unsupported-transceiver |     |     | confirm |     |
| --------------- | -------------------------------- | --- | --- | ------- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |     |
| ----------- | ----------- | ------------- | --------- | ----- | --- |
switch(config)#
CommandHistory
Interfaceconfiguration|55

| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400              |                | forthiscommand. |     |
| ----------------- | -------------- | --------------- | --- |
| default interface |                |                 |     |
| default interface | <INTERFACE-ID> |                 |     |
Description
Setsaninterface(orarangeofinterfaces)tofactorydefaultvalues.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<INTERFACE-ID> SpecifiestheIDofasingleinterfaceorrangeofinterfaces.
Format:member/slot/portormember/slot/port-
member/slot/porttospecifyarange.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Resettinganinterface:
| switch(config)# | default default | interface | 1/1/1 |
| --------------- | --------------- | --------- | ----- |
Resettinganrangeofinterfaces:
| switch(config)# | default default | interface | 1/1/1-1/1/10 |
| --------------- | --------------- | --------- | ------------ |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
description
| description | <DESCRIPTION> |     |     |
| ----------- | ------------- | --- | --- |
56
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

no description
Description
Associatesdescriptiveinformationwithaninterfacetohelpadministratorsandoperatorsidentifythe
purposeorroleofaninterface.
Thenoformofthiscommandremovesadescriptionfromaninterface.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<DESCRIPTION> Specifyadescriptionfortheinterface.Range:1to64ASCII
characters(includingspace,excludingquestionmark).
Examples
SettingthedescriptionforaninterfacetoDataLink01:
| switch(config-if)# |     | description |     | DataLink 01 |
| ------------------ | --- | ----------- | --- | ----------- |
Removingthedescriptionforaninterface.
| switch(config-if)# |     | no description |     |     |
| ------------------ | --- | -------------- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
energy-efficient-ethernet
energy-efficient-ethernet
Description
Enablesauto-negotiationofEnergy-EfficientEthernet(EEE)onaninterface.EEENegotiationisestablished
onlyonauto-linknegotiationwithsupportedlinkpartners.
Examples
Configuringaninterface:
| switch(config)#    |     | interface                 | 1/1/1 |     |
| ------------------ | --- | ------------------------- | ----- | --- |
| switch(config-if)# |     | energy-efficient-ethernet |       |     |
DisablingEnergyEfficientEthernetonaninterface:
Interfaceconfiguration|57

| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
no energy-efficient-ethernet
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
error-control
AppliesonlytotheAruba6300SwitchSeries.
| error-control    | {auto | | none  | | base-r-fec      | | rs-fec} |
| ---------------- | ----- | ------- | ----------------- | --------- |
| no error-control |       | {auto | | none | base-r-fec | | rs-fec} |
Description
Configurestheforwarderrorcorrection(FEC)modetouseforaninterface.Whennotconfigured,the
systemwillautomaticallyselecttheFECmodebasedontheinstalledtransceiver.Inmostcases,the
standardFECmodewillworkbest,butcertainlinkpartnersmayrequireanon-standardmode.
ThenoandautoformsofthiscommandconfiguretheinterfacetoautomaticallyusethestandardFEC
modeofthecurrentlyinstalledtransceiver.
FECconfigurationonlyappliesto25Gand100Gtransceivers.Thedefaultfortheinstalledtransceiverisusedin
allothercases.
TransceiversforwhichFECisauto-negotiatedwillrequestthemodeconfiguredbythiscommand,butmay
resolvetoadifferentmode.FEC modeispresentedasacommentedlineintheconfigurationshownwiththe
show runcommand.
| Parameter |     |     |     | Description               |
| --------- | --- | --- | --- | ------------------------- |
| auto      |     |     |     | Usethetransceiverdefault. |
none
DonotuseanyFEC.
| base-r-fec |     |     |     | UseIEEEClause74BASE-R(Firecode)FEC. |
| ---------- | --- | --- | --- | ----------------------------------- |
rs-fec
UseIEEE Clause91RS(Reed-Solomon)FEC.
58
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

Command History

Release

10.08.1021

Command Information

Modification

Command introduced

Platforms

Command context

Authority

6300

config-if

Administrators or local user group members with execution rights
for this command.

flow-control
flow-control rxtx
no flow-control rxtx

Description

Enables negotiation of IEEE 802.3x link-level flow control on the current interface. The switch advertises
link-level flow-control support to the link partner. The final configuration is determined based on the
capabilities of both partners.

The no form disables flow control support on the current interface.

Parameter

rxtx

Usage

Description

Enables the ability to respect and generate IEEE 802.3x link-level
pause frames on the current interface.

Care must be taken to ensure proper lossless flow control operation:

n Lossless flow control will only operate correctly when both the ingress and egress interfaces have flow

control enabled.

n All members of a LAG must have the same flow control configuration.

n Lossless flow control is only supported for single destination unicast traffic. Replicated traffic (e,g.

broadcast, multicast, mirroring) cannot be guaranteed to be lossless.

n Lossless behavior is not supported when operating in a VSF stack configuration.

n Any queue used by protocol or control traffic must not be configured for lossless behavior. Routing

protocols and VSX-synchronization messages use local-priority 7, therefore the CoS priority mapped to
local-priority 7 should not be used in any lossless configuration.

For example, in a default configuration, the CoS map assigns local-priority 7 to packets arriving with
VLAN priority 7. This means that lossless pools should not be configured to use priority 7, and that
interfaces should not be configured with 'flow-control priority 7', since that VLAN priority maps to local-
priority 7.

Examples

Interface configuration | 59

EnablesupportforRXandTXflowcontrol:
| switch(config)#    |     | interface    | 1/1/1 |      |
| ------------------ | --- | ------------ | ----- | ---- |
| switch(config-if)# |     | flow-control |       | rxtx |
DisablesupportforRXandTXflowcontrol:
| switch(config)#    |     | interface       | 1/1/1 |      |
| ------------------ | --- | --------------- | ----- | ---- |
| switch(config-if)# |     | no flow-control |       | rxtx |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
interface
| interface <PORT-NUM> |     |     |     |     |
| -------------------- | --- | --- | --- | --- |
Description
Switchestotheconfig-ifcontextforaphysicalport.Thisiswhereyoudefinetheconfigurationsettingsfor
thelogicalinterfaceassociatedwiththephysicalport.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<PORT-NUM> Specifiesaphysicalportnumber.Format:member/slot/port.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringaninterface:
| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
60
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| interface          | loopback      |     |
| ------------------ | ------------- | --- |
| interface loopback | <ID>          |     |
| no interface       | loopback <ID> |     |
Description
Createsaloopbackinterfaceandchangestotheconfig-loopback-ifcontext.Loopbackinterfacesare
layer3.
Thenoformofthiscommanddeletesaloopbackinterface.
Parameter Description
<INSTANCE> SpecifiestheloopbackinterfaceID.Range:1to256
Examples
| switch#         | config    |            |
| --------------- | --------- | ---------- |
| switch(config)# | interface | loopback 1 |
switch(config-loopback-if)#
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
| interface      | vlan           |     |
| -------------- | -------------- | --- |
| interface vlan | <VLAN-ID>      |     |
| no interface   | vlan <VLAN-ID> |     |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-if-
vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
Interfaceconfiguration|61

| Parameter |     |     |     | Description                                   |
| --------- | --- | --- | --- | --------------------------------------------- |
| <VLAN-ID> |     |     |     | SpecifiestheloopbackinterfaceID.Range:2to4094 |
Examples
| switch#                 | config |           |      |     |
| ----------------------- | ------ | --------- | ---- | --- |
| switch(config)#         |        | vlan 10   |      |     |
| switch(config-vlan-10)# |        |           | exit |     |
| switch(config)#         |        | interface | vlan | 10  |
switch(config-if-vlan)#
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip address
| ip address    | <IPV4-ADDR>/<MASK> |     | [secondary] |     |
| ------------- | ------------------ | --- | ----------- | --- |
| no ip address | <IPV4-ADDR>/<MASK> |     | [secondary] |     |
Description
SetsanIPv4addressforthecurrentlayer3interface.
ThenoformofthiscommandremovestheIPv4addressfromtheinterface.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<IPV4-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
<MASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom0to128.
| secondary |     |     |     | SpecifiesasecondaryIPaddress. |
| --------- | --- | --- | --- | ----------------------------- |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Creatingalayer3interfacesettingitsIPaddressto192.168.100.1withamaskof24bits.
| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
62
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| switch(config-if)# | routing |     |     |
| ------------------ | ------- | --- | --- |
switch(config-if)#
|     | ip  | address 192.168.100.1/24 |     |
| --- | --- | ------------------------ | --- |
AssigningtheIPaddress192.168.20.1withamaskof24bitstoloopbackinterface1:
| switch(config)#             | interface | loopback | 1                       |
| --------------------------- | --------- | -------- | ----------------------- |
| switch(config-loopback-if)# |           | routing  |                         |
| switch(config-loopback-if)# |           | ip       | address 192.168.20.1/24 |
AssigningtheIPaddress192.168.199.1withamaskof24bitstointerfaceVLAN10:
| switch(config)#         | interface | vlan       | 10               |
| ----------------------- | --------- | ---------- | ---------------- |
| switch(config-if-vlan)# |           | ip address | 192.168.199.1/24 |
RemovingtheIPaddress192.168.199.1withamaskof24bitsfrominterfaceVLAN10:
| switch(config)#         | interface | vlan          | 10               |
| ----------------------- | --------- | ------------- | ---------------- |
| switch(config-if-vlan)# |           | no ip address | 192.168.199.1/24 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-loopback-if |     | forthiscommand. |
| --- | ------------------ | --- | --------------- |
config-if-vlan
ip mtu
ip mtu <VALUE>
no ip mtu
Description
SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthatcanbe
sentorreceivedbytheinterface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.Thiscommandisonlyallowed
whenroutingisenabledontheinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE>
SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
Interfaceconfiguration|63

SettingtheIPMTUto576bytes:
| switch(config-if)# | ip mtu 576 |     |
| ------------------ | ---------- | --- |
SettingtheIPMTUtothedefaultvalue:
| switch(config-if)# | no ip mtu |     |
| ------------------ | --------- | --- |
SettingtheIPMTUvalueonasubinterface:
switch(config)#
interface 1/1/1.10
| switch(config-subif)# | ip mtu 6000 |     |
| --------------------- | ----------- | --- |
Usage
TheIP MTUvalueforsubinterfacemustbelessthanorequaltotheparentMTUforthesubinterface.The
subinterfaceusesitsIPMTUvalueandnottheparentIPMTUvalue.
CommandHistory
| Release        |     | Modification              |
| -------------- | --- | ------------------------- |
| 10.08          |     | Subinterfacesupportadded. |
| 10.07orearlier |     | --                        |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan | forthiscommand. |
| --- | -------------- | --------------- |
config-subif
ip source-interface
ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay |
simplivity | dns | all} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
no ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay |
simplivity | dns | all} [interface <IFNAME> | <IPV4-ADDR>] [vrf <VRF-NAME>]
Description
SetsasinglesourceIPaddressforafeatureontheswitch.Thisensuresthatalltrafficsentthefeaturehas
thesamesourceIPaddressregardlessofhowitegressestheswitch.Youcandefineasingleglobaladdress
thatappliestoallsupportedfeatures,oranindividualaddressforeachfeature.
ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,or
byusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIPaddress
takesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforallsupportedservices,oraspecific
service.
64
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| Parameter    |     |        |          |     | Description |     |
| ------------ | --- | ------ | -------- | --- | ----------- | --- |
| sflow | tftp | |   | radius | | tacacs | |   |             |     |
SetsasinglesourceIPaddressforaspecificservice.Theall
ntp | syslog | ubt | dhcp-relay | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
simplivity | dns | all nothaveanaddressset.ForDHCPrelay,theaddressisusedas
boththesourceIPandGIADDR.
| interface | <IFNAME> |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- |
Specifiesthenameoftheinterfacefromwhichthespecified
serviceobtainsitssourceIPaddress.Theinterfacemusthavea
validIPaddressassignedtoit.Iftheinterfacehasbothaprimary
andsecondaryIPaddress,theprimaryIPaddressisused.
<IPV4-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedservice.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionis
notused).SpecifytheaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesthenameofaVRF. |     |
| -------------- | --- | --- | --- | --- | ----------------------- | --- |
Examples
SettingtheIPv4address10.10.10.5astheglobalsinglesourceaddress:
| switch#         | config |     |                  |     |                |     |
| --------------- | ------ | --- | ---------------- | --- | -------------- | --- |
| switch(config)# |        | ip  | source-interface |     | all 10.10.10.5 |     |
SettingthesecondaryIPv4address10.10.10.5oninterface1/1/1astheglobalsinglesourceaddress.(On
the6400SwitchSeries,interfaceidentificationdiffers.)
| switch#            | config |           |                  |               |                |           |
| ------------------ | ------ | --------- | ---------------- | ------------- | -------------- | --------- |
| switch(config)#    |        | interface | 1/1/1            |               |                |           |
| switch(config-if)# |        |           | routing          |               |                |           |
| switch(config-if)# |        |           | ip address       | 10.10.10.1/24 |                |           |
| switch(config-if)# |        |           | ip address       | 10.10.10.5/24 |                | secondary |
| switch(config)#    |        | exit      |                  |               |                |           |
| switch(config)#    |        | ip        | source-interface |               | all 10.10.10.5 |           |
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)# |     | no  | ip source-interface |     | all | 10.10.10.5 |
| --------------- | --- | --- | ------------------- | --- | --- | ---------- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Interfaceconfiguration|65

ipv6 address
ipv6 address <IPV6-ADDR>/<MASK>{eui64 | [tag <ID>]}
no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets an IPv6 address on the interface.

The no form of this command removes the IPv6 address on the interface.

This command automatically creates an IPv6 link-local address on the interface. However, it does not add the
ipv6 address link-local command to the running configuration. If you remove the IPv6 address, the link-local
address is also removed. To maintain the link-local address, you must manually execute the ipv6 address
link-local command.

Parameter

<IPV6-ADDR>

<MASK>

eui64

tag <ID>

Examples

Description

Specifies the IP address in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. You can use two colons (::) to
represent consecutive zeros (but only once), remove leading
zeros, and collapse a hextet of four zeros to a single 0. For
example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes
2222:0:3333::4444:55.

Specifies the number of bits in the address mask in CIDR format
(x), where x is a decimal number from 0 to 128.

Configure the IPv6 address in the EUI-64 bit format.

Configure route tag for connected routes. Range: 0 to
4294967295. Default: 0.

Setting the IPv6 address 2001:0db8:85a3::8a2e:0370:7334 with a mask of 24 bits:

switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Removing the IP address 2001:0db8:85a3::8a2e:0370:7334 with mask of 24 bits:

switch(config-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

66

Platforms

Command context

Authority

All platforms

config-if

Administrators or local user group members with execution rights
for this command.

ipv6 source-interface
ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay |
simplivity | dns | all} {interface <IFNAME> | <IPV6-ADDR>} [vrf <VRF-NAME>]
no ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay
| simplivity | dns | all} [interface <IFNAME> | <IPV6-ADDR>] [vrf <VRF-NAME>]

Description

Sets a single source IP address for a feature on the switch. This ensures that all traffic sent the feature has
the same source IP address regardless of how it egresses the switch. You can define a single global address
that applies to all supported features, or an individual address for each feature.

This command provides two ways to set the source IP addresses: either by specifying a static IP address, or
by using the address assigned to a switch interface. If you define both options, then the static IP address
takes precedence.

The no form of this command deletes the single source IP address for all supported protocols, or a specific
protocol.

Parameter

Description

sflow | tftp | radius | tacacs |
ntp | syslog | ubt | dhcp-relay |
simplivity | dns | all

Sets a single source IP address for a specific protocol. The all
option sets a global address that applies to all protocols that do
not have an address set.

interface <IFNAME>

<IPV6-ADDR>

vrf <VRF-NAME>

Examples

Specifies the name of the interface from which the specified
protocol obtains its source IP address.

Specifies the source IP address to use for the specified protocol.
The IP address must be defined on the switch, and it must exist on
the specified VRF (which is the default VRF, if the vrf option is
not used). Specify the IP address in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

Specifies the name of the VRF from which the specified protocol
sets its source IP address.

Configuring the IPv6 address 2001:DB8::1 as the global single source address:

switch# config
switch(config)# ip source-interface all 2001:DB8::1/32

Configuring the IPv6 address 2001:DB8::1 on VRF sflow-vrf on interface 1/1/2 as the single source
address for sFlow:

switch(config)# vrf sflow-vrf
switch(config-vrf)# exit

Interface configuration | 67

| switch(config)# |     | interface | 1/1/2 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                    |     | no shutdown |         |                |     |
| ------------------ | --- | ----------- | ------- | -------------- | --- |
| switch(config-if)# |     | vrf         | attach  | sflow-vrf      |     |
| switch(config-if)# |     | ipv6        | address | 2001:DB8::1/32 |     |
| switch(config-if)# |     | exit        |         |                |     |
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
StopthesourceIPaddressfromusingtheIPaddressoninterface1/1/1onVRFone.
switch(config)# no ip source-interface all interface 1/1/1 vrf one
ClearthesourceIPaddress2001:DB8::1.
| switch(config)# |     | no ip source-interface |     |     | all 2001:DB8::1 |
| --------------- | --- | ---------------------- | --- | --- | --------------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
l3-counters
| l3-counters    | [rx | tx] |       |     |     |     |
| -------------- | --------- | ----- | --- | --- | --- |
| no l3-counters | [rx       | | tx] |     |     |     |
Description
Enablescountersonalayer3interface.Bydefault,allinterfacesarelayer3.Tochangealayer2interfaceto
layer3,usetheroutingcommand.
Thenoformofthiscommand,withnospecification,disablesbothtransmitandreceivecountersonalayer3
interface.Todisabletransmit(tx)orreceive(rx)countersonly,specifythecountertypeyouwanttodisable.
| Parameter |     |     |     | Description               |     |
| --------- | --- | --- | --- | ------------------------- | --- |
| rx        |     |     |     | Specifiesreceivecounters. |     |
tx
Specifiestransmitcounters.
Examples
Enablinglayer3transmitcounters
68
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

Onthe6300SwitchSeries:
| switch(config)#    | interface | 1/1/1       |     |
| ------------------ | --------- | ----------- | --- |
| switch(config-if)# |           | routing     |     |
| switch(config-if)# |           | l3-counters |     |
Onthe6400SwitchSeries:
| switch(config)#    | interface | 1/3/1       |     |
| ------------------ | --------- | ----------- | --- |
| switch(config-if)# |           | routing     |     |
| switch(config-if)# |           | l3-counters |     |
Enablinglayer3transmitcountersonsubinterfaces
Onthe6300SwitchSeries:
| switch(config)#       | interface | 1/1/1.10    |     |
| --------------------- | --------- | ----------- | --- |
| switch(config-subif)# |           | routing     |     |
| switch(config-subif)# |           | l3-counters | tx  |
Onthe6400SwitchSeries:
| switch(config)#       | interface | 1/3/1.10    |     |
| --------------------- | --------- | ----------- | --- |
| switch(config-subif)# |           | routing     |     |
| switch(config-subif)# |           | l3-counters | tx  |
CommandHistory
| Release        |     |     | Modification                             |
| -------------- | --- | --- | ---------------------------------------- |
| 10.08          |     |     | Addedsupportfor13countersonsubinterfaces |
| 10.07orearlier |     |     | --                                       |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 | config-subif |     | forthiscommand. |
| ---- | ------------ | --- | --------------- |
mtu
mtu <VALUE>
no mtu
Description
SetstheMTU(maximumtransmissionunit)foraninterface.Thisdefinesthemaximumsizeofalayer2
(Ethernet)frame.FrameslargerthantheMTU(1500bytesbydefault)aredroppedandcauseanICMP
fragmentation-neededmessagetobesentbacktotheoriginator.
Tosupportjumboframes(frameslargerthan1522bytes),increasetheMTUasrequiredbyyournetwork.A
framesizeofupto9198bytesissupported.
Interfaceconfiguration|69

Thelargestpossiblelayer1framewillbe18byteslargerthantheMTUvaluetoallowforlinklayerheaders
andtrailers.
ThenoformofthiscommandsetstheMTUtothedefaultvalue1500.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| <VALUE>   |     |     | SpecifiestheMTUinbytes.Range:46to9198.Default:1500. |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettingtheMTUoninterface1/1/1to1000bytes:
| switch(config)#    | interface | 1/1/1   |     |
| ------------------ | --------- | ------- | --- |
| switch(config-if)# | no        | routing |     |
| switch(config-if)# | mtu       | 1000    |     |
SettingtheMTUoninterface1/1/1tothedefaultvalue:
| switch(config)#    | interface | 1/1/1   |     |
| ------------------ | --------- | ------- | --- |
| switch(config-if)# | no        | routing |     |
| switch(config-if)# | no        | mtu     |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
persona
| persona {access | | uplink | | custom <PERSONA>} |     |
| --------------- | -------- | ------------------- | --- |
no persona
Description
Associatesoneofthreepersonatypeswithaninterfacetoclassifythepurposeorroleofaninterface.On
the10000SwitchSeries,“access”personaportsaretypicallyconnectedtoworkloads/VMs,andthe“uplink”
(fabric)personaportsareconnectedtothecore/spine.
Thenoformofthiscommandremovestheinterfacepersona.
70
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

| Parameter |     | Description                  |
| --------- | --- | ---------------------------- |
| access    |     | Selectstheaccesspersonatype. |
| uplink    |     | Selectstheuplinkpersonatype. |
custom <PERSONA> Selectsthecustompersonatypewithauser-providedname.
Range:1to64printableASCIIcharactersincludingspace.
Examples
Configuringanaccesspersona:
| switch(config-if)# | persona access |     |
| ------------------ | -------------- | --- |
Configuringanuplinkpersona:
| switch(config-if)# | persona uplink |     |
| ------------------ | -------------- | --- |
Configuringacustompersona:
| switch(config-if)# | persona custom | special |
| ------------------ | -------------- | ------- |
Removingthepersonasetting.
| switch(config-if)# | no persona |     |
| ------------------ | ---------- | --- |
CommandHistory
| Release |     | Modification       |
| ------- | --- | ------------------ |
| 10.09   |     | Commandintroduced. |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
routing
routing
no routing
Description
Enablesroutingsupportonaninterface,creatingaL3(layer3)interfaceonwhichtheswitchcanroute
IPv4/IPv6traffictootherdevices.
Bydefault,routingisdisabledonallinterfaces.
Thenoformofthiscommanddisablesroutingsupportonaninterface,creatingaL2(layer2)interface.
Interfaceconfiguration|71

Examples
Enablingroutingsupportonaninterface:
switch(config-if)#
routing
Disablingroutingsupportonaninterface:
| switch(config-if)# | no routing |     |     |
| ------------------ | ---------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-if
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
show allow-unsupported-transceiver
show allow-unsupported-transceiver
Description
Displaysconfigurationandstatusofunsupportedtransceivers.
Examples
Showingunallowedunsupportedtransceivers:
| switch(config)#   | show allow-unsupported-transceiver |     |                |
| ----------------- | ---------------------------------- | --- | -------------- |
| Allow unsupported | transceivers                       |     | : no           |
| Logging           | interval                           |     | : 1440 minutes |
---------------------------------------------
| Port | Type | Status |     |
| ---- | ---- | ------ | --- |
---------------------------------------------
| 1/1/31 | SFP-SX     | unsupported |     |
| ------ | ---------- | ----------- | --- |
| 1/1/32 | SFP-1G-BXD | unsupported |     |
| 1/1/2  | SFP28DAC3  | unsupported |     |
Showingallowedunsupportedtransceivers:
| switch#           | show allow-unsupported-transceiver |     |                |
| ----------------- | ---------------------------------- | --- | -------------- |
| Allow unsupported | transceivers                       |     | : yes          |
| Logging           | interval                           |     | : 1440 minutes |
72
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Type

---------------------------------------------
Port
---------------------------------------------
unsupported-allowed
1/1/31
unsupported-allowed
1/1/32
unsupported
1/1/2

SFP-SX
SFP-1G-BXD
SFP28DAC3

Status

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

Administrators or local user group members with execution rights
for this command.

show interface
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero]]
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]
show interface [lag | loopback | tunnel | vlan ] [<ID>] [extended [non-zero]]

Description

Shows active configurations and operational status information for interfaces.

Parameter

<IFNAME>

<IFRANGE>

brief

physical

extended

non-zero

LAG

LOOPBACK

TUNNEL

VLAN

<LAG-ID>

Description

Specifies a interface name.

Specifies the port identifier range.

Shows brief info in tabular format.

Shows the physical connection info in tabular format.

Shows additional statistics.

Shows only non zero statistics.

Shows LAG interface information.

Shows loopback interface information.

Shows tunnel interface information.

Shows VLAN interface information.

Specifies the LAG number. Range: 1-256

Interface configuration | 73

| Parameter     |     |     |     |     | Description                                    |     |     |     |
| ------------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| <LOOPBACK-ID> |     |     |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |     |     |     |
| <TUNNEL-ID>   |     |     |     |     | SpecifiesthetunnelID.Range:1-255               |     |     |     |
| <VLAN-ID>     |     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |     |     |
| VXLAN         |     |     |     |     | ShowstheVXLANinterfaceinformation.             |     |     |     |
| <VXLAN-ID>    |     |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |     |
Examples
Thefollowingexampleshowswhentheinterfaceisconfiguredasaroute-onlyport:
| switch#           | show interface |        | 1/1/1        |                   |                 |           |     |     |
| ----------------- | -------------- | ------ | ------------ | ----------------- | --------------- | --------- | --- | --- |
| Interface         | 1/1/1          | is up  |              |                   |                 |           |     |     |
| Admin state       | is             | up     |              |                   |                 |           |     |     |
| Link state:       | up             | for    | 2 days       | (since Sun        | Jun 21 05:30:22 | UTC 2020) |     |     |
| Link transitions: |                | 1      |              |                   |                 |           |     |     |
| Description:      |                | backup | data center  | link              |                 |           |     |     |
| Hardware:         | Ethernet,      |        | MAC Address: | 70:72:cf:fd:e7:b4 |                 |           |     |     |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |               |            |     |       |         |
| ---------------- | ---- | ----------- | --- | ------------- | ---------- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |               |            |     |       |         |
| Auto-negotiation |      | is          | on  |               |            |     |       |         |
| Flow-control:    |      | off         |     |               |            |     |       |         |
| Error-control:   |      | off         |     |               |            |     |       |         |
| Energy-Efficient |      | Ethernet    |     | is enabledMDI | mode: MDIX |     |       |         |
| L3 Counters:     |      | Rx Enabled, | Tx  | Enabled       |            |     |       |         |
| Rate collection  |      | interval:   |     | 300 seconds   |            |     |       |         |
| Rates            |      |             |     | RX            |            | TX  | Total | (RX+TX) |
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
74
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Collision |     |     |     |     | n/a |     |     | 0   |     |     | 0   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Runts     |     |     |     |     | 0   |     |     | n/a |     |     | 0   |
| Giants    |     |     |     |     | 0   |     |     | n/a |     |     | 0   |
| Other     |     |     |     |     | 0   |     |     | 0   |     |     | 0   |
Whentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface |     | 1/1/1 |     |     |     |     |     |     |
| ------------------ | ----- | ----- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |     |       |     |     |     |     |     |     |
...
| Auto-negotiation |     | is  | on with | downshift |     | active |     |     |     |     |     |
| ---------------- | --- | --- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- |
Whentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
| switch(config-if)# |       | show  | interface |     | 1/1/1 |     |     |     |     |     |     |
| ------------------ | ----- | ----- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |     |       |     |     |     |     |     |     |
...
| Energy-Efficient |     | Ethernet |     | is enabled |     | and active |     |     |     |     |     |
| ---------------- | --- | -------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
WhentheinterfaceisshutdownduringaVSX split:
switch(config-if)#
|                    |       | show     | interface |        | 1/1/1 |         |             |     |       |     |     |
| ------------------ | ----- | -------- | --------- | ------ | ----- | ------- | ----------- | --- | ----- | --- | --- |
| Interface          | 1/1/1 | is down  |           |        |       |         |             |     |       |     |     |
| Admin state        | is    | up       |           |        |       |         |             |     |       |     |     |
| State information: |       | Disabled |           | by     | VSX   |         |             |     |       |     |     |
| Link state:        | down  | for      | 3 days    | (since |       | Tue Mar | 16 05:20:47 | UTC | 2021) |     |     |
| Link transitions:  |       | 0        |           |        |       |         |             |     |       |     |     |
Description:
| Hardware: | Ethernet, |     | MAC Address: |     | 04:09:73:62:90:e7 |     |     |     |     |     |     |
| --------- | --------- | --- | ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |                 |     |     |         |     |     |     |     |       |         |
| ---------------- | --------------- | --------------- | --- | --- | ------- | --- | --- | --- | --- | ----- | ------- |
| Speed 0          | Mb/s            |                 |     |     |         |     |     |     |     |       |         |
| Auto-negotiation |                 | is              | off |     |         |     |     |     |     |       |         |
| Flow-control:    |                 | off             |     |     |         |     |     |     |     |       |         |
| Error-control:   |                 | off             |     |     |         |     |     |     |     |       |         |
| VLAN Mode:       | native-untagged |                 |     |     |         |     |     |     |     |       |         |
| Native           | VLAN:           | 1               |     |     |         |     |     |     |     |       |         |
| Allowed          | VLAN            | List: 1502-1505 |     |     |         |     |     |     |     |       |         |
| Rate collection  |                 | interval:       |     | 300 | seconds |     |     |     |     |       |         |
| Rate             |                 |                 |     |     |         | RX  |     |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     | 0.00 |     |     | 0.00 |     |     | 0.00  |
| ----------- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ----- |
| KPkts /     | sec |     |     |     | 0.00 |     |     | 0.00 |     |     | 0.00  |
| Unicast     |     |     |     |     | 0.00 |     |     | 0.00 |     |     | 0.00  |
| Multicast   |     |     |     |     | 0.00 |     |     | 0.00 |     |     | 0.00  |
| Broadcast   |     |     |     |     | 0.00 |     |     | 0.00 |     |     | 0.00  |
| Utilization |     |     |     |     | 0.00 |     |     | 0.00 |     |     | 0.00  |
| Statistic   |     |     |     |     |      | RX  |     |      | TX  |     | Total |
Interfaceconfiguration|75

---------------- -------------------- -------------------- --------------------
|     | Packets      |     |     |     | 0   |     |     | 0   |     | 0   |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Unicast      |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Multicast    |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Broadcast    |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Bytes        |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Jumbos       |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Dropped      |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Pause Frames |     |     |     | 0   |     |     | 0   |     | 0   |
|     | Errors       |     |     |     | 0   |     |     | 0   |     | 0   |
|     | CRC/FCS      |     |     |     | 0   |     |     | n/a |     | 0   |
|     | Collision    |     |     |     | n/a |     |     | 0   |     | 0   |
|     | Runts        |     |     |     | 0   |     |     | n/a |     | 0   |
|     | Giants       |     |     |     | 0   |     |     | n/a |     | 0   |
WhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
|     | switch(config-if)# |     | show | interface | 1/1/1 | physical |     |     |     |     |
| --- | ------------------ | --- | ---- | --------- | ----- | -------- | --- | --- | --- | --- |
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
----
|     |          |        |         | Link   | Admin       |        | Speed |        | Flow-Control    |     |
| --- | -------- | ------ | ------- | ------ | ----------- | ------ | ----- | ------ | --------------- | --- |
|     | EEE      | PoE    | Power   |        |             |        |       |        | Port            |     |
|     | Port     | Type   |         | Status | Config      | Status | |     | Config | Status | Config |     |
|     | Status | | Config | (Watts) | State  | Information |        |       |        | Description     |     |
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
----
|     | 1/1/1 | 1GbT |     | up          | up  | 1G  |     | auto | off off | on  |
| --- | ----- | ---- | --- | ----------- | --- | --- | --- | ---- | ------- | --- |
|     | on    |      | --  | 10M/100M/1G |     |     |     |      | --      |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | interface |                  | dom |     |          |            |     |     |     |     |
| ---- | --------- | ---------------- | --- | --- | -------- | ---------- | --- | --- | --- | --- |
| show | interface | [<INTERFACE-ID>] |     | dom | [detail] | [vsx-peer] |     |     |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+,QSFP+).This
informationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
76
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |

| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
| detail |     |     |     | Showdetailedinformation. |     |     |     |
| ------ | --- | --- | --- | ------------------------ | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch# | show interface |     | dom |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
Port Type Channel Temperature Voltage Tx Bias Rx Power Tx Power
|     |     |     | (Celsius) |     | (Volts) (mA) | (mW/dBm) | (mW/dBm) |
| --- | --- | --- | --------- | --- | ------------ | -------- | -------- |
----------------------------------------------------------------------------------
| 1/1/1 | SFP+SR   |     | 47.65 |     | 3.31 8.40 | 0.08, -10.96 | 0.63, -2.49 |
| ----- | -------- | --- | ----- | --- | --------- | ------------ | ----------- |
| 1/1/2 | SFP+SR   |     | n/a   |     | n/a n/a   | n/a          | n/a         |
| 1/1/3 | SFP+DA3  |     | 42.10 |     | 3.24 n/a  | n/a          | n/a         |
| 1/1/4 | QSFP+SR4 | 1   | 44.46 |     | 3.30 6.12 | 0.08, -10.96 | 0.63, -1.95 |
|       |          | 2   | 44.46 |     | 3.30 6.04 | 0.08, -10.96 | 0.63, -2.00 |
|       |          | 3   | 44.46 |     | 3.30 6.51 | 0.08, -10.96 | 0.60, -2.16 |
|       |          | 4   | 44.46 |     | 3.30 6.19 | 0.08, -10.96 | 0.63, -1.94 |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                      | energy-efficient |     |                           | ethernet |     |     |
| -------------- | -------------------- | ---------------- | --- | ------------------------- | -------- | --- | --- |
| show interface | [<IFNAME>|<IFRANGE>] |                  |     | energy-efficient-ethernet |          |     |     |
Description
DisplaysEnergy-EfficientEthernetinformationfortheinterface.
Interfaceconfiguration|77

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<IFNAME> Specifiesthenameofaninterfaceontheswitch.Usetheformat
member/slot/port(forexample,1/1/1).
<IFRANGE> Specifiestheportidentifierrangeofaninterfaceontheswitch.
Usetheformatmember/slot/port(forexample,1/1/1).
Example
ThefollowingexampleshowswhentheinterfacesareEnergy-EfficientEthernetcapable
|     | switch# | show interface | energy-efficient-ethernet |     |     |     |
| --- | ------- | -------------- | ------------------------- | --- | --- | --- |
-------------------------------------------------------------------
|     | Port | Enabled | Negotiated | Speed  | TX Wake  | RX Wake   |
| --- | ---- | ------- | ---------- | ------ | -------- | --------- |
|     |      |         |            | (MB/s) | Time(us) | Time (us) |
-------------------------------------------------------------------
|     | 1/1/1 | no  | no  | --   | --  | --  |
| --- | ----- | --- | --- | ---- | --- | --- |
|     | 1/1/2 | yes | yes | 100  | 36  | 36  |
|     | 1/1/3 | yes | yes | 1000 | 17  | 17  |
|     | 1/1/4 | no  | no  | --   | --  | --  |
|     | 1/1/5 | yes | no  | 1000 | --  | --  |
ThefollowingexampleshowswhentheinterfaceisnotEnergy-EfficientEthernetcapable:
|     | switch# | show interface | 1/1/1       | energy-efficient-ethernet |     |     |
| --- | ------- | -------------- | ----------- | ------------------------- | --- | --- |
|     | Port    | 1/1/1 does     | not support | Energy-Efficient-Ethernet |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- |
6300 config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | interface |                       | flow-control |              |          |     |
| ---- | --------- | --------------------- | ------------ | ------------ | -------- | --- |
| show | interface | [<IFNNAME>|<IFRANGE>] |              | flow-control | [detail] |     |
Description
Displaystheflowcontrolconfiguration,status,andstatisticsofthespecifiedinterface.
Ifdetailisnotspecified,thecommanddisplaysasummaryofallflowcontrolledinterfaceswithoneinterface
perline.Ifdetailisspecified,thecommanddisplaysdetailsandstatisticsaboutflowcontrolinalongformon
thespecifiedinterfaces.
78
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- |

| Parameter |     |     | Description                            |     |
| --------- | --- | --- | -------------------------------------- | --- |
| <IFNAME>  |     |     | Specifiesaninterfacename.              |     |
| <IFRANGE> |     |     | Specifiestheportidentifierrange.       |     |
| detail    |     |     | Showdetailsandstatisticsofflowcontrol. |     |
Examples
Showinginterfaceswithflowcontrolenabledinconfigorstatus:
| switch# show | interface | flow-control |     |     |
| ------------ | --------- | ------------ | --- | --- |
--------------------------------------
|      | Flow Control | Flow Control |     |     |
| ---- | ------------ | ------------ | --- | --- |
| Port | Config       | Status       |     |     |
--------------------------------------
| 1/1/1 | rxtx | rxtx |     |     |
| ----- | ---- | ---- | --- | --- |
| 1/1/2 | rxtx | off  |     |     |
Showingallinterfacesindetailform:
| switch# show  | interface | flow-control | detail |     |
| ------------- | --------- | ------------ | ------ | --- |
| Interface     | 1/1/1 is  | up           |        |     |
| Admin state   | is up     |              |        |     |
| Flow-control: | off       |              |        |     |
| Interface     | 1/1/2 is  | up           |        |     |
| Admin state   | is up     |              |        |     |
| Flow-control: | off       |              |        |     |
...
ShowingRXTXenabledflowcontrol:
| switch# show         | interface | 1/1/1 flow-control   | detail               |     |
| -------------------- | --------- | -------------------- | -------------------- | --- |
| Interface            | 1/1/1 is  | up                   |                      |     |
| Admin state          | is up     |                      |                      |     |
| Flow-control:        | rxtx      |                      |                      |     |
| Statistics           |           |                      | RX                   | TX  |
| -------------------- |           | -------------------- | -------------------- |     |
| Dot3 Pause           | Frames    |                      | 0                    | 0   |
CommandHistory
| Release |     |     | Modification       |     |
| ------- | --- | --- | ------------------ | --- |
| 10.08   |     |     | Commandintroduced. |     |
CommandInformation
Interfaceconfiguration|79

| Platforms | Commandcontext |     |     | Authority                                            |     |
| --------- | -------------- | --- | --- | ---------------------------------------------------- | --- |
| 6300      |                |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface | transceiver |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- |
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations] [vsx-peer]
Description
Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfordifferent
transceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPEandthird-party
transceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskintheoutput.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
| detail               |     |     |     | Showdetailedinformationfortheinterfaces. |     |
| -------------------- | --- | --- | --- | ---------------------------------------- | --- |
| threshold-violations |     |     |     | Showthresholdviolationsfortransceivers.  |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingsummarytransceiverinformationwithidentificationofunsupportedtransceivers:
| switch(config)# | show | interface | transceiver |     |     |
| --------------- | ---- | --------- | ----------- | --- | --- |
-------------------------------------------------------------------
| Port | Type | Product |     | Serial | Part   |
| ---- | ---- | ------- | --- | ------ | ------ |
|      |      | Number  |     | Number | Number |
-------------------------------------------------------------------
| 1/1/1         | SFP+SR      | J9150A     |     | MYxxxxxxxx | 1990-3657 |
| ------------- | ----------- | ---------- | --- | ---------- | --------- |
| 1/1/2         | SFP+ER*     | --         |     | --         | --        |
| 1/2/1         | QSFP+SR4    | JH233A     |     | MYxxxxxxxx | 2005-1234 |
| 1/2/2         | QSFP+ER4*   | --         |     | --         | --        |
| 1/3/1         | SFP28DAC3   | 844477-B21 |     | MYxxxxxxxx | 77fc-7ce7 |
| * unsupported | transceiver |            |     |            |           |
Showingdetailedtransceiverinformation:
| switch(config)# | show     | interface | transceiver | detail |     |
| --------------- | -------- | --------- | ----------- | ------ | --- |
| Transceiver     | in 1/1/1 |           |             |        |     |
| Interface       | Name     | : 1/1/1   |             |        |     |
| Type            |          | : SFP+SR  |             |        |     |
| Connector       | Type     | : LC      |             |        |     |
| Wavelength      |          | : 850nm   |             |        |     |
80
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- |

| Transfer    | Distance | : 0m (SMF), | 30m (OM1), | 80m (OM2), | 300m (OM3) |
| ----------- | -------- | ----------- | ---------- | ---------- | ---------- |
| Diagnostic  | Support  | : DOM       |            |            |            |
| Product     | Number   | : J9150A    |            |            |            |
| Serial      | Number   | : MYxxxxxxx |            |            |            |
| Part Number |          | : 1990-3657 |            |            |            |
Status
| Temperature | : 47.65C    |             |           |           |            |
| ----------- | ----------- | ----------- | --------- | --------- | ---------- |
| Voltage     | : 3.31V     |             |           |           |            |
| Tx Bias     | : 8.40mA    |             |           |           |            |
| Rx Power    | : 0.08mW,   | -10.96dBm   |           |           |            |
| Tx Power    | : 0.56mW,   | -2.49dBm    |           |           |            |
| Recent      | Alarms :    |             |           |           |            |
| Rx power    | low alarm   |             |           |           |            |
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
| Serial      | Number      | : ??        |           |           |            |
| Part Number |             | : ??        |           |           |            |
| Transceiver | in 1/2/1    |             |           |           |            |
| Interface   | Name        | : 1/2/1     |           |           |            |
| Type        |             | : QSFP+SR4  |           |           |            |
| Connector   | Type        | : MPO       |           |           |            |
| Wavelength  |             | : 850nm     |           |           |            |
| Transfer    | Distance    | : 0m (SMF), | 0m (OM1), | 0m (OM2), | 100m (OM3) |
| Diagnostic  | Support     | : DOM       |           |           |            |
| Product     | Number      | : JH233A    |           |           |            |
| Serial      | Number      | : MYxxxxxxx |           |           |            |
| Part Number |             | : 2005-1234 |           |           |            |
Status
| Temperature | : 44.46C |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
| Voltage     | : 3.30V  |     |     |     |     |
----------------------------------------------
|          | Tx Bias | Rx Power | Tx Power |     |     |
| -------- | ------- | -------- | -------- | --- | --- |
| Channel# | (mA)    | (mW/dBm) | (mW/dBm) |     |     |
----------------------------------------------
| 1       | 6.12      | 0.00, -inf | 0.63, -1.95 |     |     |
| ------- | --------- | ---------- | ----------- | --- | --- |
| 2       | 6.04      | 0.00, -inf | 0.63, -2.00 |     |     |
| 3       | 6.51      | 0.00, -inf | 0.60, -2.16 |     |     |
| 4       | 6.19      | 0.00, -inf | 0.63, -1.94 |     |     |
| Recent  | Alarms :  |            |             |     |     |
| Channel | 1 :       |            |             |     |     |
| Rx      | power low | alarm      |             |     |     |
| Rx      | power low | warning    |             |     |     |
| Channel | 2 :       |            |             |     |     |
| Rx      | power low | alarm      |             |     |     |
| Rx      | power low | warning    |             |     |     |
Interfaceconfiguration|81

| Channel     | 3 :            |                  |           |           |          |
| ----------- | -------------- | ---------------- | --------- | --------- | -------- |
| Rx          | power low      | alarm            |           |           |          |
| Rx          | power low      | warning          |           |           |          |
| Channel     | 4 :            |                  |           |           |          |
| Rx          | power low      | alarm            |           |           |          |
| Rx          | power low      | warning          |           |           |          |
| Recent      | Errors :       |                  |           |           |          |
| Channel     | 1 :            |                  |           |           |          |
| Rx          | Loss of Signal |                  |           |           |          |
| Channel     | 2 :            |                  |           |           |          |
| Rx          | Loss of Signal |                  |           |           |          |
| Channel     | 3 :            |                  |           |           |          |
| Rx          | Loss of Signal |                  |           |           |          |
| Channel     | 4 :            |                  |           |           |          |
| Rx          | Loss of Signal |                  |           |           |          |
| Transceiver | in 1/2/2       |                  |           |           |          |
| Interface   | Name           | : 1/2/2          |           |           |          |
| Type        |                | : unknown        |           |           |          |
| Connector   | Type           | : ??             |           |           |          |
| Wavelength  |                | : ??             |           |           |          |
| Transfer    | Distance       | : ??             |           |           |          |
| Diagnostic  | Support        | : ??             |           |           |          |
| Product     | Number         | : ??             |           |           |          |
| Serial      | Number         | : ??             |           |           |          |
| Part Number |                | : ??             |           |           |          |
| Transceiver | in 1/3/1       |                  |           |           |          |
| Interface   | Name           | : 1/3/1          |           |           |          |
| Type        |                | : SFP28DAC3      |           |           |          |
| Connector   | Type           | : Copper Pigtail |           |           |          |
| Transfer    | Distance       | : 0.00km (SMF),  | 0m (OM1), | 0m (OM2), | 0m (OM3) |
| Diagnostic  | Support        | : None           |           |           |          |
| Product     | Number         | : 844477-B21     |           |           |          |
| Serial      | Number         | : MYxxxxxxx      |           |           |          |
| Part Number |                | : 77fc-7ce7      |           |           |          |
Showingdetailedtransceiverinformationwithidentificationofunsupportedtransceivers:
| switch# show | interface      | transceiver            | detail    |           |          |
| ------------ | -------------- | ---------------------- | --------- | --------- | -------- |
| Transceiver  | in 1/1/2       |                        |           |           |          |
| Interface    | Name           | : 1/1/2                |           |           |          |
| Type         |                | : SFP+ER (unsupported) |           |           |          |
| Connector    | Type           | : LC                   |           |           |          |
| Wavelength   |                | : 3590nm               |           |           |          |
| Transfer     | Distance       | : 80m (SMF),           | 0m (OM1), | 0m (OM2), | 0m (OM3) |
| Diagnostic   | Support        | : DOM                  |           |           |          |
| Vendor       | Name           | : INNOLIGHT            |           |           |          |
| Vendor       | Part Number    | : TR-PX15Z-NHP         |           |           |          |
| Vendor       | Part Revision: | 1A                     |           |           |          |
| Vendor       | Serial number: | MYxxxxxxx              |           |           |          |
Status
| Temperature    | : 28.88C  |         |     |     |     |
| -------------- | --------- | ------- | --- | --- | --- |
| Voltage        | : 3.30V   |         |     |     |     |
| Tx Bias        | : 65.53mA |         |     |     |     |
| Rx Power       | : 0.00mW, | -inf    |     |     |     |
| Tx Power       | : 1.47mW, | 1.67dBm |     |     |     |
| Recent Alarms: |           |         |     |     |     |
82
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Rx Power | low     | alarm   |     |     |     |     |
| -------- | ------- | ------- | --- | --- | --- | --- |
| Rx Power | low     | warning |     |     |     |     |
| Recent   | Errors: |         |     |     |     |     |
| Rx loss  | of      | signal  |     |     |     |     |
Showingtransceiverthreshold-violations:
| switch(config)# |     | show | interface |     | transceiver | threshold-violations |
| --------------- | --- | ---- | --------- | --- | ----------- | -------------------- |
-----------------------------------------------------
| Port | Type |     | Channel |     | Type(s) of | Recent       |
| ---- | ---- | --- | ------- | --- | ---------- | ------------ |
|      |      |     |         |     | Threshold  | Violation(s) |
-----------------------------------------------------
| 1/1/1         | SFP+SR    |             |     |     | Tx bias high | warning     |
| ------------- | --------- | ----------- | --- | --- | ------------ | ----------- |
|               |           |             |     |     | 50.52 mA     | > 40.00 mA  |
| 1/1/2         | SFP+ER*   |             |     |     | ??           |             |
| 1/2/1         | QSFP+SR4  |             | 1   |     | Tx power     | low alarm   |
|               |           |             |     |     | -17.00 dBm   | < -0.50 dBm |
|               |           |             | 2   |     | Tx bias low  | warning     |
|               |           |             |     |     | 3.12 mA <    | 4.00 mA     |
| 1/2/2         | QSFP+ER4* |             |     |     | ??           |             |
| 1/3/1         | SFP28DAC3 |             |     |     | n/a          |             |
| * unsupported |           | transceiver |     |     |              |             |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip           | interface |                |     |            |     |     |
| ----------------- | --------- | -------------- | --- | ---------- | --- | --- |
| show ip interface |           | <INTERFACE-ID> |     | [vsx-peer] |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Interfaceconfiguration|83

Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
switch#
|              | show ip interface | 1/1/1        |                   |
| ------------ | ----------------- | ------------ | ----------------- |
| Interface    | 1/1/1 is          | up           |                   |
| Admin state  | is up             |              |                   |
| Hardware:    | Ethernet,         | MAC Address: | 70:72:cf:fd:e7:b4 |
| IPv4 address | 192.168.1.1/24    |              |                   |
MTU 1500
RX
|     | 0 packets, | 0 bytes |     |
| --- | ---------- | ------- | --- |
TX
|     | 0 packets, | 0 bytes |     |
| --- | ---------- | ------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip | source-interface |     |     |
| ------- | ---------------- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsettingthat
appliestoallprotocolsthatdonothaveanaddressset.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.                            |
| -------------- | --- | --- | -------------------------------------------------- |
| vsx-peer       |     |     | ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdo |
nothavetheVSXconfigurationortheISLisdown,theoutput
fromtheVSXpeerswitchisnotdisplayed.Thisparameteris
availableonswitchesthatsupportVSX.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
84
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

| switch#          | show | ip source-interface | sflow       |
| ---------------- | ---- | ------------------- | ----------- |
| Source-interface |      | Configuration       | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| sflow    |     | 10.10.10.1       |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show | ip source-interface | all         |
| ---------------- | ---- | ------------------- | ----------- |
| Source-interface |      | Configuration       | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| all      |     | 1/1/1            |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms |     | Commandcontext | Authority |
| --------- | --- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show      | ipv6      | interface      |            |
| --------- | --------- | -------------- | ---------- |
| show ipv6 | interface | <INTERFACE-ID> | [vsx-peer] |
Description
ShowsstatusandconfigurationinformationforanIPv6interface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<INTERFACE-ID> SpecifiesaninterfaceID.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Interfaceconfiguration|85

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

ff02::ff70:7334 ff02::ffe3:e800 ff02::1 ff02::1:ff00:0
ff02::2

IPv6 multicast (S,G) entries joined: none
IPv6 MTU: 1524 (using link MTU)
IPv6 unicast reverse path forwarding: none
IPv6 load sharing: none
RX

TX

0 packets, 0 bytes

0 packets, 0 bytes

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

show ipv6 source-interface
show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]

[vsx-peer]

Description

Shows single source IP address configuration settings.

Parameter

Description

sflow | tftp | radius | tacacs | all

vrf <VRF-NAME>

vsx-peer

Shows single source IP address configuration settings for a
specific protocol. The all option shows the global setting that
applies to all protocols that do not have an address set.

Specifies the name of a VRF.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output
from the VSX peer switch is not displayed. This parameter is
available on switches that support VSX.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

86

Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch#          | show ipv6 source-interface | sflow       |
| ---------------- | -------------------------- | ----------- |
| Source-interface | Configuration              | Information |
----------------------------------------
| Protocol | Source Interface |     |
| -------- | ---------------- | --- |
| -------- | ---------------- |     |
| sflow    | 2001:DB8::1      |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show ipv6 source-interface | all         |
| ---------------- | -------------------------- | ----------- |
| Source-interface | Configuration              | Information |
----------------------------------------
| Protocol | Source Interface |     |
| -------- | ---------------- | --- |
| -------- | ---------------- |     |
| all      | 1/1/1            |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
shutdown
shutdown
no shutdown
Description
Disablesaninterface.Interfacesaredisabledbydefaultwhencreated.
Thenoformofthiscommandenablesaninterface.
Examples
Disablinganinterface:
| switch(config-if)# | shutdown |     |
| ------------------ | -------- | --- |
Enablinganinterface:
Interfaceconfiguration|87

| switch(config-if)# |     | no shutdown |     |
| ------------------ | --- | ----------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| system | interface-group |     |     |
| ------ | --------------- | --- | --- |
Thiscommandonlyappliestothefollowingmodules:
R0X44AAruba640048p10G/25GSFP28Module
n
n R0X44CAruba640048p1G/10G/25GSFP28v2Module
system interface-group <GROUP> line-module <SLOT-ID> speed <SPEED>
| no system | interface-group | <GROUP> line-module | <SLOT-ID> |
| --------- | --------------- | ------------------- | --------- |
Description
Configuresspeedforaninterfacegroup.Afterchanginggroupspeed,onlytransceiverscompatiblewiththe
newspeedwillbeenabled.
n R0X44C(version2)istheonlymodulethatcanapply50Gspeedasanoption.Ifthecommandisattemptedto
anyothertypeofmodule,thecommandisignored.
n Allspeed-mismatchedinterfacesinthegroupwillbedisabled.
n Thiscommandcaninterruptactivenetworklinks,userconfirmationisrequiredtoproceed.
Thenoformofthiscommandresetsthespecifiedinterfacegrouptoitsdefault.
| Parameter |     |     | Description                         |
| --------- | --- | --- | ----------------------------------- |
| <GROUP>   |     |     | Specifiesinterfacegrouptoconfigure. |
<SPEED>
Configurestransceiverspeed(10g,25gor50g)foragroup.
Defaultis25g(seetheTransceiverGuideforfurtherdetail).
On6400SwitchSeries:
25gallowstransceiversupto25Gbps.
n
88
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

| Parameter |     | Description |
| --------- | --- | ----------- |
50gallows50GbpstransceiversandDACsontheR0X44C
n
version2module.Thiscommandisignoredonanyothertype
ofmodule(includingR0X44Aversion1).
| <SLOT-ID> |     | SpecifiesslotID ofthelinemodule. |
| --------- | --- | -------------------------------- |
Examples
Configuringinterfacegroup1online-module1/1toallow10Gbpsandslowertransceivers:
switch(config)# system interface-group 1 line-module 1/1 speed 10g
Changing the group speed will disable all member interfaces that do not match the
new speed.
| Continue | (y/n)? y |     |
| -------- | -------- | --- |
CommandHistory
| Release           |     | Modification      |
| ----------------- | --- | ----------------- |
| 10.09.0002orlater |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) | forthiscommand. |
| --- | --- | --------------- |
Interfaceconfiguration|89

Chapter 6

Subinterfaces

Subinterfaces

A subinterface is a virtual interface created by dividing one physical interface into multiple logical interfaces.
Subinterfaces use the parent physical interface for sending and receiving data.

Supported features

The following features are supported on L3 subinterfaces:

n RoP, L3 LAG and Hydra interface (split cable) support

n IPv4/IPv6 addressing

n ARP/ND

n Static unicast routing (IPv4/IPv6)

n Unicast routing (IPv4/IPv6) - OSPF and VRRP

n Unicast routing (IPv4/IPv6) - BGP and IVRL

n IPv4/IPv6 multicast routing (IGMP and PIM)

n Ingress ACLs and Ingress Policies

n MTU (maximum transmission unit)

n L3 counters

n VSX keep alive links

n SNMP read

n REST support

Configuring subinterfaces

n Subinterfaces can be configured for physical ports, split children of physical ports and L3 LAG interfaces.

n An L3 interface with subinterfaces must be attached to the default VRF.

n Subinterfaces on multiple ports can be assigned the same VLAN ID (there is no bridging between

subinterfaces or between subinterfaces and SVIs). Each subinterface is considered to be in a separate bridge

domain.

n The parent interface's IP MTU (maximum transmission unit) can be equal to or greater than the value

configured on the child subinterface.

Procedure

One router with one physical interface needs to be connected to two IP networks:

1. Create two subinterfaces within the physical interface.

2. Assign each subinterface an IP address within each subnet.

3. Route packets between the two subnets.

Limitations

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

90

n Subinterfaces can only be configured on L3 ports with routing enabled.

n A subinterface cannot be a member of a LAG.

n An L3 interface with subinterfaces cannot be a member of a LAG.

n An L3 interface with subinterfaces cannot be used for L3 services (for example IP address configuration

is not supported on an L3 interface if the interface is configured with subinterfaces).

n On physical interfaces, each subinterface must have a unique encapsulation ID.

Subinterface applications use VLAN context group selectors because they are matched on the subinterface's

internal VLAN number in hardware. For example, if one of the "Ingress VLAN" context group selectors is allocated

(due to one or more MAC ACLs applied to VLANs on ingress), it can be shared with one or more MAC ACLs

applied to subinterfaces on ingress.

Subinterface in a router-on-a-stick deployment

n Top-of-rack switch/router with an L3 interface connected to the trunk port of an L2 switch.

n Routing tables configured to forward outgoing traffic through a subinterface while applying a VLAN

ID tag.

n All outgoing traffic from the L3 interface is tagged with a VLAN ID which enables the switch to forward

traffic through different VLANs.

Subinterface commands

encapsulation dot1q
encapsulation dot1q <VLAN-ID>
no encapsulation dot1q <VLAN-ID>

Description

Configures 802.1Q encapsulation on a subinterface.

The no form of this command removes 802.1Q encapsulation on a subinterface.

Parameter

<VLAN-ID>

Usage

Description

Specifies encapsulation VLAN ID. Range 1 to 4094.

n Associates an 802.1Q VLAN ID with a subinterface.

Subinterfaces | 91

Examples
Configuring802.1Qencapsulationonasubinterface:
switch(config)#
|                       | interface | 1/1/1.201     |          |
| --------------------- | --------- | ------------- | -------- |
| switch(config-subif)# |           | encapsulation | dot1q 10 |
Removing802.1Qencapsulationonasubinterface:
| switch(config-subif)# |     | no encapsulation | dot1q 10 |
| --------------------- | --- | ---------------- | -------- |
CommandHistory
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-subif
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
interface
| interface <IFNAME>.<ID> |                   |     |     |
| ----------------------- | ----------------- | --- | --- |
| no interface            | <IFNAME>.<ID>     |     |     |
| interface lag           | <LAGNUM>.<ID>     |     |     |
| no interface            | lag <LAGNUM>.<ID> |     |     |
Description
CreatesasubinterfaceonanL3interfaceandenterssubinterfaceconfigurationmode.Thesubinterface
nameconsistsoftheparentinterfacename(forexample,1/1/1)followedbyaperiodandauniqueID
number.
ThenoformofthesecommandsdeletesasubinterfacefromanL3interface.
| Parameter |     |     | Description               |
| --------- | --- | --- | ------------------------- |
| <IFNAME>  |     |     | SpecifiesL3interfacename. |
<ID>
SpecifiessubinterfaceID.Range1to4094.
| <LAGNUM> |     |     | SpecifiesL3LAGinterfacenumber. |
| -------- | --- | --- | ------------------------------ |
Usage
n TocreateaLAGsubinterface,parentLAGmustexistbeforecreatingthesubinterface.
Examples
92
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

CreatingasubinterfaceonL3interface1/1/1.201andenteringsubinterfaceconfigurationmode:
| switch(config)# | interface | 1/1/1.201 |     |     |
| --------------- | --------- | --------- | --- | --- |
switch(config-subif)#
DeletingsubinterfaceonL3interface1/1/1.201:
| switch(config)# | no interface | 1/1/1.201 |     |     |
| --------------- | ------------ | --------- | --- | --- |
CreatingasubinterfaceonanL3LAGportandenteringsubinterfaceconfigurationmode:
| switch(config)# | interface | lag 1.201 |     |     |
| --------------- | --------- | --------- | --- | --- |
switch(config-subif)#
DeletingsubinterfaceonanL3LAG port:
| switch(config)# | no interface | lag | 1.201 |     |
| --------------- | ------------ | --- | ----- | --- |
CommandHistory
| Release |     |     | Modification      |     |
| ------- | --- | --- | ----------------- | --- |
| 10.08   |     |     | Commandintroduced |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400            |              |     | forthiscommand. |     |
| --------------- | ------------ | --- | --------------- | --- |
| show capacities | subinterface |     |                 |     |
| show capacities | subinterface |     |                 |     |
Description
Displaysmaximumsubinterfacecapacity.
Examples
Showingmaximumsubinterfacecapacity:
| switch#            | show capacities | subinterface |     |       |
| ------------------ | --------------- | ------------ | --- | ----- |
| System Capacities: | Filter          | Subinterface |     |       |
| Capacities         | Name            |              |     | Value |
-----------------------------------------------------------------------------------
Maximum number of LAG subinterfaces for the entire system 256
Maximum number of LAG members when the LAG has subinterfaces 4
Maximum number of normal subinterfaces for the entire system 1024
Subinterfaces|93

Maximum number of subinterface resources for the entire system (normal+(4*LAG) 1024
CommandHistory
| Release |     |     |     |     | Modification      |     |     |
| ------- | --- | --- | --- | --- | ----------------- | --- | --- |
| 10.08   |     |     |     |     | Commandintroduced |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
6300 Operator(>)orManager AuditorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     |     | executionrightsforthiscommand.Auditorscanexecutethis |     |     |
| ---- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- |
(#)
commandfromtheauditorcontext(auditor>)only.
show interface
| show interface | <IFNAME>.<ID> |               |     |     |     |     |     |
| -------------- | ------------- | ------------- | --- | --- | --- | --- | --- |
| show interface | lag           | <LAGNUM>.<ID> |     |     |     |     |     |
Description
Displayssubinterfaceconfiguration.
| Parameter |     |     |     |     | Description               |     |     |
| --------- | --- | --- | --- | --- | ------------------------- | --- | --- |
| <IFNAME>  |     |     |     |     | SpecifiesL3interfacename. |     |     |
<ID>
SpecifiessubinterfaceID.Range1to4094.
| <LAGNUM> |     |     |     |     | SpecifiesL3LAGinterfacenumber. |     |     |
| -------- | --- | --- | --- | --- | ------------------------------ | --- | --- |
Examples
Showingsubinterfaceconfiguration:
| switch#            | show interface |         | 1/1/1.201 |      |     |     |     |
| ------------------ | -------------- | ------- | --------- | ---- | --- | --- | --- |
| Interface          | 1/1/1.201      | is      | down      |      |     |     |     |
| Admin state        | is up          |         |           |      |     |     |     |
| State information: |                | Waiting | for       | link |     |     |     |
Description:
| Hardware:     | Ethernet, | MAC | Address: |     | 38:21:c7:5a:80:80 |     |       |
| ------------- | --------- | --- | -------- | --- | ----------------- | --- | ----- |
| Encapsulation | dot1Q     | ID: | 10       |     |                   |     |       |
| Statistic     |           |     |          |     | RX                | TX  | Total |
---------------- -------------------- -------------------- --------------------
| L3 Packets |     |     |     |     | 0   | 0   | 0   |
| ---------- | --- | --- | --- | --- | --- | --- | --- |
| L3 Bytes   |     |     |     |     | 0   | 0   | 0   |
ShowingsubinterfaceLAGconfiguration:
| switch#   | show interface |         | lag1.1 |     |     |     |     |
| --------- | -------------- | ------- | ------ | --- | --- | --- | --- |
| Interface | lag1.1         | is down |        |     |     |     |     |
94
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

| Admin state | is up |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
Description:
| Hardware:     | Ethernet, | MAC Address: | 38:21:c7:5a:80:80 |     |       |
| ------------- | --------- | ------------ | ----------------- | --- | ----- |
| Encapsulation | dot1Q     | ID: 2        |                   |     |       |
| Statistic     |           |              | RX                | TX  | Total |
---------------- -------------------- -------------------- --------------------
| L3 Packets |     |     | 0   | 0   | 0   |
| ---------- | --- | --- | --- | --- | --- |
| L3 Bytes   |     |     | 0   | 0   | 0   |
CommandHistory
| Release |     |     | Modification      |     |     |
| ------- | --- | --- | ----------------- | --- | --- |
| 10.08   |     |     | Commandintroduced |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 Operator(>)orManager AuditorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
Subinterfaces|95

Chapter 7
|                  |           |     |     | Source | interface | selection |
| ---------------- | --------- | --- | --- | ------ | --------- | --------- |
| Source interface | selection |     |     |        |           |           |
ThesourceIPaddressisdeterminedbythesystemandistypicallytheIPaddressoftheoutgoinginterfacein
theroutingtable.However,routingswitchesmayhavemultipleroutinginterfacesandoutgoingpacketscan
potentiallybesentbydifferentpathsatdifferenttimes.ThisresultsindifferentsourceIPaddresses.
AOS-CXprovidesaconfigurationmodelthatallowstheselectionofanIPaddresstouseasthesource
addressforalloutgoingtraffic.Thisallowsuniqueidentificationofthesoftwareapplicationontheserver
siteregardlessofwhichlocalinterfacehasbeenusedtoreachthedestinationserver.Thesourceinterface
selectionsupportsselectinganIPaddressorinterfacename.
IfthesourceinterfaceandsourceIPareconfigured,SourceIPwillhavepriority.
| Source-interface       | selection  |           | commands         |     |     |     |
| ---------------------- | ---------- | --------- | ---------------- | --- | --- | --- |
| ip source-interface    | (protocol  |           | <ip-addr>)       |     |     |     |
| ip source-interface    | <PROTOCOL> | <IP-ADDR> | [vrf <VRF-NAME>] |     |     |     |
| no ip source-interface | <PROTOCOL> | <IP-ADDR> | [vrf <VRF-NAME>] |     |     |     |
Description
Configuresthesource-interfaceIPv4addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.Ifnointerfaceoptionisgiven,thedevicefloodsthroughinterfacesandVRFstoreach
ArubaCentral.WhicheverreachesArubaCentralwillbepickedautomatically.
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
SelectssFLow.
96
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- | --- |

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
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
switch(config)#
|     | no ip source-interface | tftp 10.1.1.1 |     |
| --- | ---------------------- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationfortheDNSprotocolonVRFgreen:
Sourceinterfaceselection|97

switch(config)# no ip source-interface dns 10.1.1.2 vrf green

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

Administrators or local user group members with execution rights
for this command.

ip source-interface
ip source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
no ip source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]

Description

Configures the IPv4 source-interface interface to use for the specified protocol. If a VRF is not given, the
default VRF applies.

The no form of this command removes the specified configuration.

Parameter

<PROTOCOL>

Description

Specifies the protocol to configure.
all

Selects all protocols that can be configured by this
command.

central

Selects Aruba Central.

dhcp_relay

Selects DHCP relay.

dns

Selects DNS.

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

Selects TFTP.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

98

| Parameter      |     |     |     | Description                |     |     |
| -------------- | --- | --- | --- | -------------------------- | --- | --- |
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRF name.      |     |     |
| <IFNAME>       |     |     |     | Specifiestheinterfacename. |     |     |
Examples
ConfiguringIPv4source-interfaceinterface1/1/1tousefortheTFTP protocol:
| switch(config)# |     | ip source-interface |     | tftp | interface | 1/1/1 |
| --------------- | --- | ------------------- | --- | ---- | --------- | ----- |
ConfiguringIPv4source-interfaceinterface1/1/2tousefortheTFTP protocolonVRFgreen:
switch(config)# ip source-interface tftp interface 1/1/2 vrf green
RemovingIPv4source-interface1/1/1configurationfortheTFTP protocol:
| switch(config)# |     | no ip source-interface |     |     | tftp interface | 1/1/1 |
| --------------- | --- | ---------------------- | --- | --- | -------------- | ----- |
Removingsource-interfaceinterface1/1/2configurationforTFTP protocolonVRFgreen:
switch(config)# no ip source-interface tftp interface 1/1/2 vrf green
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 source-interface
| ipv6 source-interface |     | <PROTOCOL> | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |     |
| --------------------- | --- | ---------- | ----------- | --- | ---------------- | --- |
| no source-interface   |     | <PROTOCOL> | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |     |
Description
Configuresthesource-interfaceIPv6addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedprotocolconfiguration.
Sourceinterfaceselection|99

| Parameter  |     | Description                      |     |
| ---------- | --- | -------------------------------- | --- |
| <PROTOCOL> |     | Specifiestheprotocoltoconfigure. |     |
all:Selectsallprotocolssupportedbythiscommand.
n
n central:SelectsArubaCentral.
n ntp:SelectsNTP.
n radius:Selectsradius.
n sflow:SelectssFLow.
syslog:Selectssyslog.
n
tacacs:SelectsTACACS.
n
n tftp:SelectsTFTP.
<IPV6-ADDR>
SpecifiestheIPv6address.
| vrf <VRF-NAME> |     | SpecifiestheVRF name. |     |
| -------------- | --- | --------------------- | --- |
Examples
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
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
100
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

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

vrf <VRF-NAME>

Specifies the interface name.

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

Source interface selection | 101

switch(config)# no ipv6 source-interface tftp interface 1/1/2 vrf green
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip source-interface |     |            |                 |             |
| ------------------------ | --- | ---------- | --------------- | ----------- |
| show ip source-interface |     | <PROTOCOL> | [vrf <VRF-NAME> | | all-vrfs] |
Description
DisplaysthesourceinterfaceinformationforallVRFsoraspecificVRF.
IfaVRF isnotspecified,thedefaultisdisplayed.
| Parameter  |     |     | Description                 |     |
| ---------- | --- | --- | --------------------------- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoshow. |     |
all
Showsthesourceinterfaceconfigurationforallother
protocols.
central
ShowsthesourceinterfaceconfigurationforAruba
Central.
dhcp relay
ShowsthesourceinterfaceconfigurationforDHCPrelay.
dns
ShowsthesourceinterfaceconfigurationforDNS.
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
102
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| Parameter      |     | Description                                     |     |
| -------------- | --- | ----------------------------------------------- | --- |
| vrf <VRF-NAME> |     | SpecifiestheVRF name.                           |     |
| all-vrfs       |     | ShowsthesourceinterfaceconfigurationforallVRFs. |     |
Examples
Displayingallsource-interfaceprotocolconfigurationsforVRF red:
| switch#          | show ip source-interface | all vrf red |     |
| ---------------- | ------------------------ | ----------- | --- |
| Source-interface | Configuration            | Information |     |
---------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
---------------------------------------------------------------
| all | 1/1/1 |     | red |
| --- | ----- | --- | --- |
switch#
Displayingallsource-interfaceprotocolconfigurationsfordefaultVRF:
| switch#          | show ip source-interface | all         |     |
| ---------------- | ------------------------ | ----------- | --- |
| Source-interface | Configuration            | Information |     |
-------------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
-------------------------------------------------------------------
| all |     | 1.1.1.1 | default |
| --- | --- | ------- | ------- |
switch#
Displaying allsource-interfaceprotocolconfigurationsforallVRFs:
| switch#          | show ip source-interface | all all-vrfs |     |
| ---------------- | ------------------------ | ------------ | --- |
| Source-interface | Configuration            | Information  |     |
-------------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
-------------------------------------------------------------------
| all |         | 2.2.2.2 | all-vrfs |
| --- | ------- | ------- | -------- |
| all |         | 1.1.1.1 | default  |
| all | 1/1/1/1 |         | red      |
switch#
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ipv6 | source-interface |     |     |
| --------- | ---------------- | --- | --- |
Sourceinterfaceselection|103

show ipv6 source-interface <PROTOCOL> [detail] [vrf <VRF-NAME> | all-vrfs]
Description
DisplaystheIPV6sourceinterfaceinformationconfiguredintherouterforallVRFsoraspecificVRF.
IfaVRF isnotspecified,thedefaultisdisplayed.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<PROTOCOL>
Specifiestheprotocoltoshow.
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
switch#
104
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

Displaying allIPv6source-interfaceprotocolconfigurationsforallVRFs:
| switch#          | show ipv6 | source-interface |     |             | all | all-vrfs |     |     |
| ---------------- | --------- | ---------------- | --- | ----------- | --- | -------- | --- | --- |
| Source-interface |           | Configuration    |     | Information |     |          |     |     |
-------------------------------------------------------------------
| Protocol |     | Src-Interface |     |     | Src-IP |     |     | VRF |
| -------- | --- | ------------- | --- | --- | ------ | --- | --- | --- |
-------------------------------------------------------------------
| all |     |       |     |     | 2.2.2.2:3.3.3.3 |     |     | all-vrfs |
| --- | --- | ----- | --- | --- | --------------- | --- | --- | -------- |
| all |     |       |     |     | 1.1.1.1:2.2.2.2 |     |     | default  |
| all |     | 1/1/1 |     |     | 2::2            |     |     | red      |
switch#
CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show running-config
show running-config
Description
Displaysthecurrentrunningconfiguration.
Examples
Displayingtherunningconfiguration(onlyitemsofinteresttosourceinterfaceselectionareshowninthis
exampleoutputcommand):
ArubaCentralisthepriorityagent.Ifnocommandisspecifiedforipsource-interface,Centralwillchoosethe
commandautomaticallyifitisreachableonanyoftheknownports.
| switch# | show running-config |     |     |     |     |     |     |     |
| ------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
vrf green
| ip source-interface   |     |     | tftp interface   |            | 1/1/2 | vrf       | green     |     |
| --------------------- | --- | --- | ---------------- | ---------- | ----- | --------- | --------- | --- |
| ip source-interface   |     |     | radius interface |            | 1/1/2 | vrf       | green     |     |
| ip source-interface   |     |     | ntp interface    |            | 1/1/2 | vrf       | green     |     |
| ip source-interface   |     |     | tacacs interface |            | 1/1/2 | vrf       | green     |     |
| ip source-interface   |     |     | dns interface    |            | 1/1/2 | vrf       | green     |     |
| ip source-interface   |     |     | central          | interface  |       | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | all interface    |            | 1/1/2 | vrf       | green     |     |
| ipv6 source-interface |     |     | tftp 2222::3333  |            |       | vrf green |           |     |
| ipv6 source-interface |     |     | radius           | 2222::3333 |       | vrf       | green     |     |
| ipv6 source-interface |     |     | ntp 2222::3333   |            | vrf   | green     |           |     |
| ipv6 source-interface |     |     | tacacs           | 2222::3333 |       | vrf       | green     |     |
| ipv6 source-interface |     |     | central          | 2222::3333 |       | vrf       | green     |     |
Sourceinterfaceselection|105

| ipv6 source-interface |                      | all 2222::3333    | vrf green |
| --------------------- | -------------------- | ----------------- | --------- |
| ip source-interface   |                      | tftp 10.20.3.1    |           |
| ip source-interface   |                      | radius 10.20.3.1  |           |
| ip source-interface   |                      | ntp 10.20.3.1     |           |
| ip source-interface   |                      | tacacs 10.20.3.1  |           |
| ip source-interface   |                      | dns 10.20.3.1     |           |
| ip source-interface   |                      | central 10.20.3.1 |           |
| ip source-interface   |                      | all 10.20.3.1     |           |
| interface             | 1/1/1                |                   |           |
| no                    | shutdown             |                   |           |
| ip                    | address 10.20.3.1/24 |                   |           |
| interface             | 1/1/2                |                   |           |
| vrf                   | attach green         |                   |           |
| ip                    | address 20.1.1.1/24  |                   |           |
| ipv6                  | address              | 2222::3333/64     |           |
| interface             | 1/1/45               |                   |           |
| no                    | shutdown             |                   |           |
| ip                    | address 100.1.0.1/24 |                   |           |
| ipv6                  | address              | 1111::2222/64     |           |
| ip route              | 100.2.0.0/24         | 10.20.3.2         |           |
switch#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
106
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

Chapter 8

VLANs

VLANs

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of users
by logical function instead of physical location. They make managing bandwidth usage within networks
possible by:

n Allowing grouping of high-bandwidth users on low-traffic segments

n Organizing users from different LAN segments according to their need for common resources and

individual protocols

n Improving traffic control at the edge of networks by separating traffic of different protocol types.

n Enhancing network security by creating subnets to control in-band access to specific network resources

VLANs are generally assigned on an organizational basis rather than on a physical basis. For example, a
network administrator could assign all workstations and servers used by a particular workgroup to the same
VLAN, regardless of their physical locations.

Hosts in the same VLAN can directly communicate with one another. A router or a Layer 3 switch is required
for hosts in different VLANs to communicate with one another.

VLANs help reduce bandwidth waste, improve LAN security, and enable network administrators to address
issues such as scalability and network management.

Refer to the Layer 2 Bridging Guide for VLAN configuration and commands.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

107

Chapter 9

Precision time protocol

Precision time protocol

Precision Time Protocol (PTP) is defined in the IEEE 1588 standard (Standard for a Precision Clock
Synchronization Protocol for Networked Measurement and Control Systems). PTP synchronizes clocks in
packet-based networks that include distributed device clocks of varying precision and stability. On a local
area network, it achieves clock accuracy in the sub-microsecond range, making it suitable for measurement
and control systems. PTP is currently employed to synchronize financial transactions, mobile phone tower
transmissions, and networks that require precise timing but lack access to satellite navigation signals.

PTP clocks
A PTP network consists of PTP-enabled devices and devices that are not using PTP. The PTP-enabled devices
typically consist of clock-aware devices such as ordinary clocks (which are usually single-port end-stations)
and one or more grandsource clocks, transparent clocks, and boundary clocks (multi-port L2/L3 time-aware
devices).

The basic clock node types include:

Grandsource clock—A grandsource clock is the primary source of time for the downstream devices. This is
a device with greater clock quality which may have direct access to a reference clock.

Ordinary clock—An ordinary clock is a single port end-station (which can include a GM as the originating
PTP time-aware device).

Transparent clock—A transparent clock can have multiple network port connections but it does not act as
either a clock-source or a clock-sink. Rather, it updates the correction field within the PTP event messages
(SYNC/FOLLOW_UP, DELAY_REQUEST) to compensate for the transit time delay. Transparent clocks compensate
for switch latency and jitter, making network devices appear transparent to other PTP time-aware devices.
They help in reducing the end-station time errors and improving synchronization quality. But a transparent
clock itself does not synchronize its time. An End-to-End (E2E) transparent clock updates the
correctionField field in the PTP messages with the total time the PTP packet was resident in the network
device. This is called resident time correction.

Boundary clock—A boundary clock implements a local PTP clock where one port acts as clock-sink which
synchronizes itself with the clock-source while other ports act as clock-source ports to its downstream clock-
aware devices. The clock-source port is used to redistribute the clock to another set of clock-sinks. Boundary
clocks can also use E2E and can be configured based on the selected PTP profile. The best clock source
algorithm is used by the boundary clock to select the best or most precise configured acceptable clock-
source clock.

Based on hardware capability, the switch supports either boundary clock, transparent clock, or both modes.

Best clock-source algorithm

The best clock-source algorithm helps in choosing the source of timing on your network. It runs
independently on each clock in a domain. This algorithm specifies the way that a local clock can determine
which of all the clocks (including itself) is the best. Since it runs continuously, it continually re-adapts to
changes in the network or the clocks.

Each clock sends a message to the network describing its own properties. The best clock-source algorithm
running in the clock compares these properties to determine the best clock.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

108

The comparisons of attributes happens with the following precedence :

1. Priority1: user configurable absolute priority

2. ClockClass: Attribute defining a clock’s TAI traceability

3. Time Source: Attribute defining the accuracy of a clock

4. Variance: An attribute defining the precision of a clock

5. Priority2: This is a user configurable designation that provides finer grained ordering among otherwise
equivalent clocks

6. Clock Identity : A tiebreaker consisting of the MAC address of the clock

In addition to this precedence order, the distance measured by the number of boundary clocks between the
local clock and the best clock is used when two Announce messages reflect the same best clock. The
distance is indicated in the stepsRemoved field of announce messages.

PTP network diagram
The following diagram illustrates how the various PTP clock nodes are connected and how the timing
information flows from the origin to the end-stations to achieve the time synchronization. This diagram
depicts the PTP clocks in a source-sink hierarchy.

Figure 1 Example PTP network with clocks in a source-sink hierarchy

Configuration examples

Precision time protocol | 109

Configuringan end-to-endtransparentclock
FollowthesestepstoconfiguretheE2Etransparentclock:
1. Configurethemandatorycommands:
a. ConfigurethePTPmodeandthedelaymechanism.
b. ConfigurethePTPclock-stepmode.
c. Configurethetransportprotocol.
d. ConfigurePTPglobally.
Switch config:
| switch(config)#     | ptp profile        | 1588v2      |            |
| ------------------- | ------------------ | ----------- | ---------- |
| switch(config-ptp)# | mode               | transparent | end-to-end |
| switch(config-ptp)# | clock-step         | one-step    |            |
| switch(config-ptp)# | transport-protocol |             | ethernet   |
| switch(config-ptp)# | enable             |             |            |
2. EnablePTPontheconnectedinterfaces:
| switch(config)#    | int 1/1/1  |     |     |
| ------------------ | ---------- | --- | --- |
| switch(config-if)# | ptp enable |     |     |
switch(config-if)#
int 1/1/2
| switch(config-if)# | ptp enable |     |     |
| ------------------ | ---------- | --- | --- |
PTP over VSF
SupportedonlyontheAruba6300SwitchSeries
WhenPTPisconfiguredonaVirtualSwitchFramework(VSF)stack,eachmemberofthestackcalculates
n
theresidence-timeofthePTPpackets.
AllVSFportsarePTP-enabled(bydefault)whentransparentclockisconfiguredforaVSFstack.IftheVSF
n
linkisup,theinterfacestatusisdisplayedasRunningintheshow ptp interface briefcommand
output.
Hardware considerations
ThereisnoPTPsupportforbreakoutcables.QSAtransceiversandsub-interfacesarenotsupported.
6300switchseriesdownlinkportswithspeed1G(smartRate,non-smartRate&XCVR1GBT)haveaslightly
higherjittercomparedto6300switchseriesuplinkports,sothePTPoffsetofClientsconnectedon1GDownlink
portsof6300switchserieswouldbeslightlyhighercomparedtouplinkports.
PrecisionTimeProtocol(PTP)issupportedonlyonAruba6300Switchseriesandsecond-generationorlater
Aruba6400Switchseries.PTP isnotsupportedonthefollowing6400SwitchSeriesplatforms:
110
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

Table 1: 6400SwitchplatformsthatdonotsupportPTP
| Switch SKU |     | Description               |
| ---------- | --- | ------------------------- |
| R0X26A     |     | Aruba6405Switch(Aruba6405 |
Chassis,Aruba6400Management
Module,Aruba6400FanTray)
| R0X27A |     | Aruba6410Switch((Aruba6410 |
| ------ | --- | -------------------------- |
Chassis,Aruba6400Management
Module,Aruba6400FanTray)
| R0X29A |     | Aruba640596GCL4PoE4SFP56 |
| ------ | --- | ------------------------ |
Switch
| R0X30A |     | Aruba640548SFP+8SFP56Switch |
| ------ | --- | --------------------------- |
| JL741A |     | Aruba641096GCL4PoE4SFP56    |
Switch
PTP commands
clock-step
clock-step {one-step}
no clock-step
Description
Configurestheclockstepmodethatdetermineswhethertheegress-timeinformationissentalongwiththe
SYNCmessage(one-step),orasubsequentfollow-upmessage(two-step)withtheegresstimestampofthe
previouslysentSYNCmessage.
TheAruba6300supportsonlyone-steptransparentclockmode.
ThenoformofthiscommandremovesthePTPclock-stepconfigurationofthePTPclock.
| Parameter |     | Description |
| --------- | --- | ----------- |
one-step
SetsthePTPclock-stepmodetoone-stepmessaging.
Usage
MandatorycommandtostartthePTP clock.
n
Two-stepmodeiscurrentlynotsupportedonthetransparentclock.
n
Example
Settingtheclock-stepmodetoone-stepmessaging:
| switch(config-ptp)# | clock-step | one-step |
| ------------------- | ---------- | -------- |
switch(config-ptp)#
Removingtheclock-stepmodeconfiguration:
| switch(config-ptp)# | no clock-step |     |
| ------------------- | ------------- | --- |
Precisiontimeprotocol|111

switch(config-ptp)#
CommandHistory
| Release |     |     | Modification       |
| ------- | --- | --- | ------------------ |
| 10.08   |     |     | Commandintroduced. |
CommandInformation
| Platforms |     | Commandcontext | Authority |
| --------- | --- | -------------- | --------- |
6300 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
| 6400      |                |            | forthiscommand. |
| --------- | -------------- | ---------- | --------------- |
| clear     | ptp statistics |            |                 |
| clear ptp | statisctics    | [<IFNAME>] |                 |
Description
ClearsPTPcountersforthegiveninterface.
| Parameter |     |     | Description                         |
| --------- | --- | --- | ----------------------------------- |
| <IFNAME>  |     |     | Optional:Specifiestheinterfacename. |
Examples
ClearingPTPcountersforthegiveninterface:
| switch# | clear | ptp statistics | 1/1/8 |
| ------- | ----- | -------------- | ----- |
| switch# | clear | ptp statistics | lag1  |
| switch# | clear | ptp statistics |       |
CommandHistory
| Release |     |     | Modification       |
| ------- | --- | --- | ------------------ |
| 10.08   |     |     | Commandintroduced. |
CommandInformation
| Platforms |     | Commandcontext | Authority |
| --------- | --- | -------------- | --------- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
enable
enable
112
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

no enable
Description
EnablesthePTPprofileglobally.However,thePTPclockisstartedonlywhenallthemandatorycommands
areset.
ThenoformofthiscommanddisablesthePTPprofileglobally.
Usage
MandatorycommandtostartthePTPclock.
Examples
EnablingthePTPprofile:
| switch(config)#     |     | ptp profile | 1588v2 |     |     |
| ------------------- | --- | ----------- | ------ | --- | --- |
| switch(config-ptp)# |     | enable      |        |     |     |
DisablingthePTPprofile:
| switch(config)#     |     | ptp profile | 1588v2 |     |     |
| ------------------- | --- | ----------- | ------ | --- | --- |
| switch(config-ptp)# |     | no enable   |        |     |     |
CommandHistory
| Release |     |     |     | Modification       |     |
| ------- | --- | --- | --- | ------------------ | --- |
| 10.08   |     |     |     | Commandintroduced. |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip source-interface
ip source-interface {ptp | all} interface <IFNAME> [vrf <VRF-NAME>
| ip source-interface |     | {ptp | all} | <IPV4-ADDR> |     | [vrf <VRF-NAME>] |
| ------------------- | --- | ----------- | ----------- | --- | ---------------- |
no ip source-interface {ptp | all} interface <IFNAME> [vrf <VRF-NAME>
| no ip source-interface |     | {ptp | | all} | <IPV4-ADDR> | [vrf <VRF-NAME>] |
| ---------------------- | --- | ---- | ------ | ----------- | ---------------- |
Description
ConfiguresthesourceIPaddresstobeusedwhensendingPTPmessages.Usetheptpkeywordtoset
sourceIPaddressspecifictothePTPfeature.Ifthefeature-specificconfigurationisnotavailable,thesource
IPaddresscorrespondingtothealloptionwillbeused.
ThenoformofthiscommandremovestheconfigurationofthesourceIPaddressusedbythePTPfeature.
Precisiontimeprotocol|113

| Parameter |     | Description                                          |     |
| --------- | --- | ---------------------------------------------------- | --- |
| ptp       |     | SelectsthePTPprotocol.                               |     |
| all       |     | Selectsallprotocolsthatcanbeconfiguredbythiscommand. |     |
interface <IF-NAME> SpecifiesthenameoftheinterfacefromwhichthesourceIP
addressisobtained.TheinterfacemusthaveavalidIPaddress
assignedtoit.
IftheinterfacehasbothaprimaryandsecondaryIPaddress,the
primaryIPaddressisused.
vrf <VRF-NAME>
SpecifiestheVRF name.
| <IPV4-ADDR> |     | SpecifiesthesourceIPv4addresstobeused. |     |
| ----------- | --- | -------------------------------------- | --- |
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionisnot
used).SpecifytheaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
Usage
ThiscommandmustbeconfiguredontheswitchwhenPTPisenabledonVLAN trunkoraccessports,
n
andthetransportprotocolisIPv4.
n InthecurrentversionofPTP,onlythedefaultVRFissupported.
Thiscommandisnotapplicabletotheend-to-endtransparentclock.
n
Examples
ConfiguringthesourceIPaddressforsendingPTPmessages:
| switch(config)# | ip source-interface | ptp interface  | 1/1/1  |
| --------------- | ------------------- | -------------- | ------ |
| switch(config)# | ip source-interface | ptp 10.10.10.1 |        |
| switch(config)# | ip source-interface | ptp interface  | vlan10 |
CommandHistory
| Release |     | Modification       |     |
| ------- | --- | ------------------ | --- |
| 10.08   |     | Commandintroduced. |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
mode
| mode transparent | end-to-end |     |     |
| ---------------- | ---------- | --- | --- |
no mode
Description
114
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

ConfiguresthePTPclockmodeinwhichthedevicewilloperate.Thedevicecanbeinanysinglespecified
modewhenconfigured.Thedevicecanoperateinanend-to-endtransparentclockmode.Adevicein
transparent-clockmodedoesnotsynchronizeorsyntonizeitselftoaclock-source.
ThenoformofthiscommandremovesthePTPclockmodeconfigurationontheswitch.
| Parameter   |     |     |     | Description                |
| ----------- | --- | --- | --- | -------------------------- |
| transparent |     |     |     | Selectsthetransparentmode. |
end-to-end
Setsthedelay-requestmechanism.
Usage
MandatorycommandtostartthePTPclock.
Examples
ConfiguringPTPtransparentend-to-endclockmode:
| switch(config)#     |     | ptp profile | 1588v2      |            |
| ------------------- | --- | ----------- | ----------- | ---------- |
| switch(config-ptp)# |     | mode        | transparent | end-to-end |
switch(config-ptp)#
RemovingPTPclockmodeconfiguration:
| switch(config-ptp)# |     | no mode |     |     |
| ------------------- | --- | ------- | --- | --- |
switch(config-ptp)#
CommandHistory
| Release |     |     |     | Modification       |
| ------- | --- | --- | --- | ------------------ |
| 10.08   |     |     |     | Commandintroduced. |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
6300 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
ptp profile
| ptp profile | {<PROFILE | NAME>} |     |     |
| ----------- | --------- | ------ | --- | --- |
no PTP profile
Description
EntersthePTPcontexttoconfigurethePTPprofileinwhichthedevicewilloperate.
ConfigurePTPprofilebeforeconfiguringmodeorotherprofile-specificparameters.Thedevicecanbe
operatinginanyoneprofileatagivenpointoftime.ThenoformofthiscommandremovesthePTPprofile
configurationinwhichthedevicewilloperate.ThiscommandclearsthePTPprofileandallparameters
relatedtothatprofile.
Precisiontimeprotocol|115

| Parameter      |     |     | Description                                  |
| -------------- | --- | --- | -------------------------------------------- |
| <PROFILE NAME> |     |     | Specifiestheprofiletobeused.Profilesinclude: |
1588v2: SpecifiestheIEEE1588-2008profiletobeused.
n
n aes-r16: SpecifiestheIEEEAES-R16-2016profiletobeused.
aes67:SpecifiestheIEEEAES67profiletobeused.
n
n smpte: SpecifiestheIEEESMPTE-ST-2059-2profiletobeused.
Usage
ConfigurePTPprofilebeforeconfiguringmodeorotherprofile-specificparameters.
Example
ConfiguringPTPprofiles:
| switch(config)# | ptp profile | 1588v2 |     |
| --------------- | ----------- | ------ | --- |
switch(config-ptp)#
ConfiguringmorethanonePTPprofile:
| switch(config)#     | ptp profile | 1588v2 |     |
| ------------------- | ----------- | ------ | --- |
| switch(config-ptp)# | exit        |        |     |
| switch(config)#     | ptp profile | smpte  |     |
switch(config-ptp)#
The existing profile must be removed using the 'no ptp profile' command before
| configuring | a different | profile. |     |
| ----------- | ----------- | -------- | --- |
RemovingthePTPprofile:
| switch(config-ptp)# | no  | ptp profile |     |
| ------------------- | --- | ----------- | --- |
switch(config-ptp)#
CommandHistory
| Release |     |     | Modification       |
| ------- | --- | --- | ------------------ |
| 10.08   |     |     | Commandintroduced. |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp enable
ptp enable
no ptp enable
Description
116
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Enables PTP on the interface. The no form of this command disables PTP on the interface.

Examples

Enabling PTP on a physical interface:

switch(config)# interface 1/1/1
switch(config-if)# ptp enable
switch(config-if)#

Disabling PTP on the interface context:

switch(config)# interface 1/1/1
switch(config-if)# no ptp enable

Command History

Release

10.08

Command Information

Modification

Command introduced.

Platforms

Command context

Authority

6300
6400

config-if

Administrators or local user group members with execution rights
for this command.

ptp vlan
ptp vlan <VLAN-ID>
no ptp vlan

Description

Configures a VLAN for PTP messages. It is necessary when the boundary clock port is a VLAN trunk L2
interface (no routing). The no form of this command removes the VLAN configuration for PTP messages.

Parameter

<VLAN-ID>

Usage

Description

Specifies a VLAN. Range: 1-4094.

n This configuration has no bearing on the one-step transparent clock.

n In boundary clock mode, only PTP packets in PTP VLAN are processed; PTP packets from other VLANs are

dropped.

n ptp vlan should be configured on interfaces only when the specific VLAN is a trunk/tagged member of

that port. This configuration should not be performed on an access port.

Examples

Configuring a specific VLAN for PTP messages:

Precision time protocol | 117

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
ptp vlan 4
switch(config)#
RemovingtheVLANconfigurationforPTPmessages:
| switch(config)#    | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
| switch(config-if)# | no ptp    | vlan  |     |
switch(config)#
CommandHistory
| Release |     |     | Modification       |
| ------- | --- | --- | ------------------ |
| 10.08   |     |     | Commandintroduced. |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400     |       |     | forthiscommand. |
| -------- | ----- | --- | --------------- |
| show ptp | clock |     |                 |
show ptp clock
Description
ShowsPTPclock-relatedinformation.
Example
ShowingPTPclockinformation:
| switch#         | show ptp clock     |     |               |
| --------------- | ------------------ | --- | ------------- |
| PTP Profile     |                    |     | : smpte       |
| PTP Mode        |                    |     | : transparent |
| Delay Mechanism |                    |     | : end-to-end  |
| Clock Identity  |                    |     | : NA          |
| Network         | Transport Protocol |     | : ipv4        |
| Clock Step      |                    |     | : One         |
| Clock Domain    |                    |     | : NA          |
| Number          | of PTP Ports       |     | : 1           |
| Priority1       |                    |     | : NA          |
| Priority2       |                    |     | : NA          |
| Clock Quality   | :                  |     |               |
| Class           |                    |     | : NA          |
| Accuracy        |                    |     | : NA          |
| Offset          | (log variance)     |     | : NA          |
| Offset          | From Clock-Source  |     | : NA          |
| Mean Delay      |                    |     | : NA          |
| Steps Removed   |                    |     | : NA          |
CommandHistory
118
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

| Release |     |     |     | Modification       |
| ------- | --- | --- | --- | ------------------ |
| 10.08   |     |     |     | Commandintroduced. |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |
| --------- | --- | -------------- | --- | --------- |
6300 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand.Auditorscanexecutethis |
| ---- | --- | --- | --- | ---------------------------------------------------- |
commandfromtheauditorcontext(auditor>)only.
| show ptp           | interface |           |           |     |
| ------------------ | --------- | --------- | --------- | --- |
| show ptp interface |           | [<IFNAME> | | [brief] |     |
Description
ShowsPTPport-relatedinformation.
| Parameter |     |     |     | Description                     |
| --------- | --- | --- | --- | ------------------------------- |
| <IFNAME>  |     |     |     | Specifiestheinterfacename.      |
| brief     |     |     |     | Showsinformationinabriefformat. |
Examples
ShowingPTPportinformation:
| switch          | # show   | ptp interface | 1/1/1      |              |
| --------------- | -------- | ------------- | ---------- | ------------ |
| Port Identity   |          |               |            | : NA         |
| Port Number     |          |               |            | : NA         |
| PTP Version     |          |               |            | : 2          |
| PTP Enable      |          |               |            | : Enabled    |
| Transport       | of       | PTP           |            | : ipv4       |
| Port State      |          |               |            | : Running    |
| Delay Mechanism |          |               |            | : end-to-end |
| Announce        | Interval | (log          | mean)      | : NA         |
| Announce        | Receipt  | Timeout       |            | : NA         |
| Sync Interval   |          | (log mean)    |            | : NA         |
| Sync Timeout    |          |               |            | : NA         |
| Delay Request   |          | Interval      | (log mean) | : NA         |
switch#
| switch          | # show   | ptp interface | lag20 |              |
| --------------- | -------- | ------------- | ----- | ------------ |
| Port Identity   |          |               |       | : NA         |
| Port Number     |          |               |       | : NA         |
| PTP Version     |          |               |       | : 2          |
| PTP Enable      |          |               |       | : Enabled    |
| Transport       | of       | PTP           |       | : ipv4       |
| Port State      |          |               |       | : NA         |
| Delay Mechanism |          |               |       | : end-to-end |
| Announce        | Interval | (log          | mean) | : NA         |
| Announce        | Receipt  | Timeout       |       | : NA         |
| Sync Interval   |          | (log mean)    |       | : NA         |
| Sync Timeout    |          |               |       | : NA         |
Precisiontimeprotocol|119

| Delay | Request |     | Interval (log | mean) | : NA |     |     |     |     |
| ----- | ------- | --- | ------------- | ----- | ---- | --- | --- | --- | --- |
switch#
ShowingPTPportinformationinbriefformat:
| switch#   |     | show ptp | interface | brief |     |     |     |     |     |
| --------- | --- | -------- | --------- | ----- | --- | --- | --- | --- | --- |
| Interface |     | PTP      | State     |       |     |     |     |     |     |
--------------------------
| 1/1/1 |     | Running |     |     |     |     |     |     |     |
| ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     | Running |     |     |     |     |     |     |     |
CommandHistory
| Release |     |     |     |     | Modification       |     |     |     |     |
| ------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
| 10.08   |     |     |     |     | Commandintroduced. |     |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
6300 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     |     | executionrightsforthiscommand.Auditorscanexecutethis |     |     |     |     |
| ---- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
commandfromtheauditorcontext(auditor>)only.
| show | ptp            | statistics |            |     |     |     |     |     |     |
| ---- | -------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| show | ptp statistics |            | [<IFNAME>] |     |     |     |     |     |     |
Description
ShowsPTPportstatistics.
| Parameter |     |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
<IFNAME>
Optional.Specifiestheinterfacename.
Examples
ShowingPTPportstatistics:
| switch# |           | show ptp | statistics |         |      |         |           |         |      |
| ------- | --------- | -------- | ---------- | ------- | ---- | ------- | --------- | ------- | ---- |
| PTP     | Interface |          | Statistics |         |      |         |           |         |      |
|         |           |          | Received   | Packets | Sent | Packets | Discarded | Packets | Lost |
Packets
| Interface: |          | 1/1/15 |     |     |     |      |     |     |     |
| ---------- | -------- | ------ | --- | --- | --- | ---- | --- | --- | --- |
|            | Announce |        |     |     | 0   | 1019 |     |     | 0   |
0
|     | Sync |     |     |     | 0   | 2038 |     |     | 0   |
| --- | ---- | --- | --- | --- | --- | ---- | --- | --- | --- |
0
|     | Signaling |     |     |     | 0   | 0   |     |     | 0   |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
120
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |

0
| DelayReq |     | 0   |     | 0   | 0   |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
| DelayResp |     | 0   |     | 0   | 0   |     |
| --------- | --- | --- | --- | --- | --- | --- |
0
| FollowUp |     | 0   |     | 0   | 0   |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
| Management |     | 0   |     | 0   | 0   |     |
| ---------- | --- | --- | --- | --- | --- | --- |
0
|     | Received | Packets | Sent Packets | Discarded | Packets | Lost |
| --- | -------- | ------- | ------------ | --------- | ------- | ---- |
Packets
| Interface: | 1/1/16 |     |     |      |     |     |
| ---------- | ------ | --- | --- | ---- | --- | --- |
| Announce   |        | 0   |     | 1019 | 0   |     |
0
| Sync |     | 0   |     | 2038 | 0   |     |
| ---- | --- | --- | --- | ---- | --- | --- |
0
| Signaling |     | 0   |     | 0   | 0   |     |
| --------- | --- | --- | --- | --- | --- | --- |
0
| DelayReq |     | 0   |     | 0   | 0   |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
| DelayResp |     | 0   |     | 0   | 0   |     |
| --------- | --- | --- | --- | --- | --- | --- |
0
| FollowUp |     | 0   |     | 0   | 0   |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
| Management |     | 0   |     | 0   | 0   |     |
| ---------- | --- | --- | --- | --- | --- | --- |
0
ShowingPTPportstatisticsforthespecifiedinterface:
| switch# show  | ptp statistics | 1/1/15  |              |           |         |      |
| ------------- | -------------- | ------- | ------------ | --------- | ------- | ---- |
| PTP Interface | Statistics     |         |              |           |         |      |
|               | Received       | Packets | Sent Packets | Discarded | Packets | Lost |
Packets
| Interface: | 1/1/15 |     |     |      |     |     |
| ---------- | ------ | --- | --- | ---- | --- | --- |
| Announce   |        | 0   |     | 1024 | 0   |     |
0
| Sync |     | 0   |     | 2048 | 0   |     |
| ---- | --- | --- | --- | ---- | --- | --- |
0
| Signaling |     | 0   |     | 0   | 0   |     |
| --------- | --- | --- | --- | --- | --- | --- |
0
| DelayReq |     | 0   |     | 0   | 0   |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
| DelayResp |     | 0   |     | 0   | 0   |     |
| --------- | --- | --- | --- | --- | --- | --- |
0
| FollowUp |     | 0   |     | 0   | 0   |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
| Management |     | 0   |     | 0   | 0   |     |
| ---------- | --- | --- | --- | --- | --- | --- |
0
ThefollowingexampleofthePTPportstatisticsoutputappliesonlytotheAruba6300SwitchSeries:
| switch# show  | ptp statistics |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- |
| PTP Interface | Statistics     |     |     |     |     |     |
Precisiontimeprotocol|121

|     |     | Received | Packets |     | Sent Packets | Discarded | Packets | Lost |     |
| --- | --- | -------- | ------- | --- | ------------ | --------- | ------- | ---- | --- |
Packets
| Interface: |            | 1/1/25 |     |     |     |     |     |     |     |
| ---------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|            | Announce   |        |     | NA  |     | NA  | NA  |     | NA  |
|            | Sync       |        |     | NA  |     | NA  | NA  |     | NA  |
|            | Signaling  |        |     | NA  |     | NA  | NA  |     | NA  |
|            | DelayReq   |        |     | NA  |     | NA  | NA  |     | NA  |
|            | DelayResp  |        |     | NA  |     | NA  | NA  |     | NA  |
|            | FollowUp   |        |     | NA  |     | NA  | NA  |     | NA  |
|            | Management |        |     | NA  |     | NA  | NA  |     | NA  |
| Interface: |            | 1/1/26 |     |     |     |     |     |     |     |
|            | Announce   |        |     | NA  |     | NA  | NA  |     | NA  |
Sync
CommandHistory
| Release |     |     |     | Modification       |     |     |     |     |     |
| ------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
| 10.08   |     |     |     | Commandintroduced. |     |     |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |     |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400 |     |     |     | forthiscommand. |     |     |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
transport-protocol
| transport-protocol |     | {ethernet | |   | ipv4} |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ----- | --- | --- | --- | --- | --- |
no transport-protocol
Description
SetsthetransportprotocolforPTPpackets.InthecaseofIPv4,theUDPcheck-sumisreset.Thereisno
defaulttransport-protocol.Thenoformofthiscommanddisconnectstheclockfromitssource.
| Parameter |     |     |     | Description                                    |     |     |     |     |     |
| --------- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| ethernet  |     |     |     | SpecifiestheEthernet(Layer2)transportprotocol. |     |     |     |     |     |
| ipv4      |     |     |     | SpecifiestheIPv4transportprotocol.             |     |     |     |     |     |
Usage
MandatorycommandtostartthePTPclock.
Example
SettingtheEthernettransportprotocolforPTPpackets:
| switch(config-ptp)# |     |     | transport-protocol |     | ethernet |     |     |     |     |
| ------------------- | --- | --- | ------------------ | --- | -------- | --- | --- | --- | --- |
switch(config-ptp)#
RemovingthetransportprotocolforPTPpackets:
122
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |

| switch(config-ptp)# |     |     |     | no transport-protocol |     |     |     |
| ------------------- | --- | --- | --- | --------------------- | --- | --- | --- |
switch(config-ptp)#
CommandHistory
| Release |     |     |     |     |     | Modification       |     |
| ------- | --- | --- | --- | --- | --- | ------------------ | --- |
| 10.08   |     |     |     |     |     | Commandintroduced. |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- |
6300 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
| Recommendations |      |       |               |     | for | configuration   |     |
| --------------- | ---- | ----- | ------------- | --- | --- | --------------- | --- |
| PTP             | CoPP | class | configuration |     |     | recommendations |     |
QoSprioritization configuration recommendation for transparentclock
| class     | ip    | PTP     |         |        |                |       |     |
| --------- | ----- | ------- | ------- | ------ | -------------- | ----- | --- |
|           | 10    | match   | udp any | any    | eq 319         | count |     |
| policy    |       | PTP-POL |         |        |                |       |     |
|           | 10    | class   | ip PTP  | action | local-priority |       | 6   |
| policy    |       | test    |         |        |                |       |     |
| interface |       | lag     | 240     |        |                |       |     |
|           | apply | policy  | PTP-POL |        | in             |       |     |
| interface |       | 1/1/26  |         |        |                |       |     |
|           | apply | policy  | PTP-POL |        | in             |       |     |
| interface |       | 2/1/26  |         |        |                |       |     |
|           | apply | policy  | PTP-POL |        | in             |       |     |
PTPEventmessagescarryingacriticaltimestampuseUDPport319.
| General |     | guidelines |     | for | PTP | IPv4 | multicast |
| ------- | --- | ---------- | --- | --- | --- | ---- | --------- |
BoundaryclockisnotsupportedontheAruba6300or6400SwitchSeries.
n ForIPmulticast-basedPTPtimedistribution,itisrecommendedtousePIMSparse-Mode.
WhenconnectingTransparentClock(TC)andBoundaryClock(BC),ensurethattheTCbecomestheDR
n
bysettingtheDRpriority.
n EnsurethemroutesareprogrammedonTCssothatthereisreachabilityforPTPstreamsfromthe
upstream.
n Configurestatic-igmpgroupsonTCsiftheclientsthemselvescannotsendIGMPjoinsforthePTP
multicastgroup.
Precisiontimeprotocol|123

n The QoS trust dscp command needs to be explicitly configured on all non-BC switches in the network

to ensure that the incoming DSCP value of PTP traffic is honored.

Use cases
The use cases provide additional PTP configuration recommendations.

Use case 1: PTP – IPv4 over L2 – Spine Leaf Topology

Figure 2 Grand clock source connected to boundary clock (spines), followed by transparent clock leaves

The following considerations and best practices are recommended for the topology in :

n Configure candidate-RP on switches that are connected to a grand clock source. In the above topology,

the candidate-RP needs to be configured on the BC1 Spine A and BC2 Spine B.

n When the PTP clients are not capable of sending IGMP joins, be sure to configure ip igmp snooping

static-group 224.0.1.12 on the VLAN interface of a TC, where PTP is configured.

In this case, it is an L2 switch in leaf so ip igmp snooping enable also needs to be configured on the
transparent clock VLAN interface.

n Ensure that ip source-interface ptp <ip | interface information> is configured on both BC

switches. (VLAN interface where PTP is configured.)

n Ensure that spanning tree is configured in the above topology to avoid the loop. On the Aruba 6300 TC
Switches, spanning tree is enabled by default; it needs to be explicitly configured on the Aruba 8360 BC
Switches.

n It is recommended to have VRRP on boundary clock 8360 switches to have L3 redundancy for PTP end

clients.

Use case 2: PTP – BC and TC (VSF) topology connected via LAG

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

124

Figure 3 Grand clock source connected to a boundary clock serving time to other boundary clocks and VSF
transparent clocks in the network

The following considerations and best practices are recommended for the topology in :

n Configure candidate-RP on switches that are connected to a grand clock source. In this topology, the
Candidate-RP needs to be configured on the BC1 and BC2 switches. Each candidate-RP controls
multicast traffic forwarding for one or more multicast groups.

n When the PTP clients are not capable of sending IGMP joins, ensure that ip igmp static-group

224.0.1.129 is configured on all PTP-enabled interfaces of a TC.

igmp static-group config is not needed on boundary clock switches. In this case, it is an L3 network so ip
igmp enable also needs to be configured on all PTP enabled L3 interfaces of the transparent clock.

n For the primary or secondary LAG roles, ensure that the same link ports are configured on both ends of

the LAG across BC (this command is applicable only on BC switches).

When both the primary and secondary LAG role links are down, PTP packets will not be forwarded even if

other LAG links are up.

n Configure ip pim-sparse dr-priority <value> in order to configure higher dr-priority on the links

originating from the VSF (which are facing the BC switches).

Use case 3: PTP – L3 spine leaf topology

Precision time protocol | 125

Figure 4 Grand clock source connected to transparent clock, followed by boundary clock spines and
boundary clock leaves

The following considerations and best practices are recommended for the topology in :

n Configure candidate-RP on switches which are connected to a grand clock source. In this topology,
candidate-RP needs to be configured on TC1 and TC2. Each candidate-RP controls multicast traffic
forwarding for one or more multicast groups.

n Configure higher DR priority on switches in which candidate-RP is configured. In this topology, the DR

priority needs to be configured on the TC1 and TC2 on the BC facing ports.

n When the PTP clients are not capable of sending IGMP joins, ensure that ip igmp static-group

224.0.1.129 is configured on all PTP-enabled interfaces of a TC.

n The igmp static-group configuration is not needed on BC switches. In this case, it is an L3 network so

ip igmp enable also needs to be configured on all PTP-enabled L3 interfaces of the TC.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

126

Chapter 10

Configuration and firmware
management

Configuration and firmware management

Checkpoints
A checkpoint is a snapshot of the running configuration of a switch and its relevant metadata during the
time of creation. Checkpoints can be used to apply the switch configuration stored within a checkpoint
whenever needed, such as to revert to a previous, clean configuration. Checkpoints can be applied to other
switches of the same platform. A switch is able to store multiple checkpoints.

Checkpoint types

The switch supports two types of checkpoints:

n System generated checkpoints: The switch automatically generates a system checkpoint whenever a

configuration change occurs.

n User generated checkpoints: The administrator can manually generate a checkpoint whenever

required.

Maximum number of checkpoints

n Maximum checkpoints: 64 (including the startup configuration)

n Maximum user checkpoints: 32

n Maximum system checkpoints: 32

User generated checkpoints

User checkpoints can be created at any time, as long as one configuration difference exists since the last
checkpoint was created. Checkpoints can be applied to either the running or startup configurations on the
switch.

All user generated checkpoints include a time stamp to identify when a checkpoint was created.

A maximum of 32 user generated checkpoints can be created.

System generated checkpoints

System generated checkpoints are automatically created by default. Whenever a configuration change
occurs, the switch starts a timeout counter (300 seconds by default). For each additional configuration
change, the timeout counter is restarted. If the timeout expires with no additional configuration changes
being made, the switch generates a new checkpoint.

System generated checkpoints are named with the prefix CPC followed by a time stamp in the format
<YYYYMMDDHHMMSS>. For example: CPC20170630073127.

System checkpoints can be applied using the checkpoint rollback feature or copy command.

A maximum of 32 system checkpoints can be created. Beyond this limit, the newest system checkpoint
replaces the oldest system checkpoint.

Supported remote file formats

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

127

YoucanrestoreaswitchconfigurationbycopyingaswitchconfigurationstoredonaUSBdriveoraremote
networkdevicethroughSFTP/TFTP.Theremotefileformatsthattheswitchsupportsdependsonwhere
youplantorestorethecheckpoint.
| Restoring            | acheckpoint | toa... | File type supported |     |
| -------------------- | ----------- | ------ | ------------------- | --- |
| Runningconfiguration |             |        | CLI                 |     |
n
n JSON
Checkpoint
n
| Startupconfiguration |     |     | JSON |     |
| -------------------- | --- | --- | ---- | --- |
n
n Checkpoint
| Specifiedcheckpoint |     |     | Specifiedcheckpoint |     |
| ------------------- | --- | --- | ------------------- | --- |
Rollback
Thetermrollbackisusedtorefertowhenaswitchconfigurationisrevertedtoapre-existingcheckpoint.
Forexample,thefollowingcommandappliestheconfigurationfromcheckpointckpt1.Allprevious
configurationsarelostaftertheexecutionofthiscommand:checkpoint rollback ckpt1
Youcanalsospecifytherollbackoftherunningconfigurationorofthestartupconfigurationwitha
specifiedcheckpoint,asshownwiththefollowingcommand:copy checkpoint <checkpoint-name>
| {running-config | | startup-config} |      |     |     |
| --------------- | ----------------- | ---- | --- | --- |
| Checkpoint      | auto              | mode |     |     |
Checkpointautomodeconfigurestheswitchwithfailoversupport,causingittoautomaticallyreverttoa
previousconfigurationifitbecomesinoperableorinaccessibleduetoconfigurationchangesthatarebeing
made.
Afterenteringcheckpointautomode,youhaveasetamountoftimetoadd,remove,ormodifytheexisting
switchconfiguration.Tosaveyourchanges,youmustexecutethecheckpoint auto confirmcommand
beforetheautomodetimerexpires.Ifyoudonotexecutethecheckpoint auto confirmcommandwithin
thespecifiedtime,allconfigurationchangesyoumadearediscardedandtherunningconfigurationreverts
tothestateitwasbeforeenteringcheckpointautomode.
| Testing | a switch | configuration | in checkpoint | auto mode |
| ------- | -------- | ------------- | ------------- | --------- |
Processoverview:
1. Enablethecheckpointautomode.
2. Tosavetheconfiguration,enterthecheckpoint auto confirmcommandbeforethespecifiedtime
setinstep1.
| Checkpoint | commands |     |     |     |
| ---------- | -------- | --- | --- | --- |
checkpointauto
| checkpoint | auto <TIME-LAPSE-INTERVAL> |     |     |     |
| ---------- | -------------------------- | --- | --- | --- |
Description
Startsautocheckpointmode.Inautocheckpointmode,theswitchtemporarilysavestheruntime
configurationasacheckpointonlyforthespecifiedtimelapseinterval.Configurationchangesmustbe
Configurationandfirmwaremanagement |128

savedbeforetheintervalexpires,otherwisetheruntimeconfigurationisrestoredfromthetemporary
checkpoint.
| Parameter |     | Description |
| --------- | --- | ----------- |
<TIME-LAPSE-INTERVAL> Specifiesthetimelapseintervalinminutes.Range:1to60.
Usage
Tosavetheruntimecheckpointpermanently,runthecheckpoint auto confirmcommandduringthetime
lapseinterval.ThefilenameforthesavedcheckpointisnamedAUTO<YYYYMMDDHHMMSS>.Ifthecheckpoint
auto confirmcommandisnotenteredduringthespecifiedtimelapseinterval,thepreviousruntime
configurationisrestored.
Examples
Confirmingtheautocheckpoint:
| switch#         | checkpoint auto 20 |                 |
| --------------- | ------------------ | --------------- |
| Auto checkpoint | mode expires       | in 20 minute(s) |
switch# WARNING Please "checkpoint auto confirm" within 2 minutes
| switch#    | checkpoint auto confirm |         |
| ---------- | ----------------------- | ------- |
| checkpoint | AUTO20170801011154      | created |
Inthisexample,theruntimecheckpointwassavedbecausethecheckpoint auto confirmcommandwas
enteredwithinthevaluesetbythetime-lapse-intervalparameter,whichwas20minutes.
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
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
checkpointautoconfirm
| checkpoint | auto confirm |     |
| ---------- | ------------ | --- |
129
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Description

Signals to the switch to save the running configuration used during the auto checkpoint mode. This
command also ends the auto checkpoint mode.

Usage

To save the runtime checkpoint permanently, run the checkpoint auto confirm command during the time
lapse value set by the checkpoint auto <TIME-LAPSE-INTERVAL> command. The generated checkpoint
name will be in the format AUTO<YYYYMMDDHHMMSS>. If the checkpoint auto confirm command is not
entered during the specified time lapse interval, the previous runtime configuration is restored.

Examples

Confirming the auto checkpoint:

switch# checkpoint auto confirm

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

Administrators or local user group members with execution rights
for this command.

checkpoint diff

checkpoint diff {<CHECKPOINT-NAME1> | running-config | startup-config}

{<CHECKPOINT-NAME2> | running-config | startup-config}

Description

Shows the difference in configuration between two configurations. Compare checkpoints, the running
configuration, or the startup configuration.

Parameter

Description

{<CHECKPOINT-NAME1> | running-config | startup-config}

{<CHECKPOINT-NAME2> | running-config | startup-config}

Selects either a checkpoint, the running
configuration, or the startup
configuration as the baseline.

Selects either a checkpoint, the running
configuration, or the startup
configuration to compare.

Usability

The output of the checkpoint diff command has several symbols:

Configuration and firmware management | 130

Theplussign(+)atthebeginningofalineindicatesthatthelineexistsinthecomparisonbutnotinthe
n
baseline.
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
131
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| interface | 1/1/1              |     |
| --------- | ------------------ | --- |
| no        | shutdown           |     |
| ip        | address 1.0.0.1/24 |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
checkpointpost-configuration
| checkpoint post-configuration |                    |     |
| ----------------------------- | ------------------ | --- |
| no checkpoint                 | post-configuration |     |
Description
Enablescreationofsystemgeneratedcheckpointswhenconfigurationchangesoccur.Thisfeatureis
enabledbydefault.
Thenoformofthiscommanddisablessystemgeneratedcheckpoints.
Usage
Systemgeneratedcheckpointsareautomaticallycreatedbydefault.Wheneveraconfigurationchange
occurs,theswitchstartsatimeoutcounter(300secondsbydefault).Foreachadditionalconfiguration
change,thetimeoutcounterisrestarted.Ifthetimeoutexpireswithnoadditionalconfigurationchanges
beingmade,theswitchgeneratesanewcheckpoint.
SystemgeneratedcheckpointsarenamedwiththeprefixCPCfollowedbyatimestampintheformat
<YYYYMMDDHHMMSS>.Forexample:CPC20170630073127.
Systemcheckpointscanbeappliedusingthecheckpointrollbackfeatureorcopycommand.
Amaximumof32systemcheckpointscanbecreated.Beyondthislimit,thenewestsystemcheckpoint
replacestheoldestsystemcheckpoint.
Examples
Enablingsystemcheckpoints:
| switch(config)# | checkpoint | post-configuration |
| --------------- | ---------- | ------------------ |
Disablingsystemcheckpoints:
| switch(config)# | no checkpoint | post-configuration |
| --------------- | ------------- | ------------------ |
CommandHistory
Configurationandfirmwaremanagement |132

| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| checkpointpost-configuration |                    |     | timeout |           |     |
| ---------------------------- | ------------------ | --- | ------- | --------- | --- |
| checkpoint                   | post-configuration |     | timeout | <TIMEOUT> |     |
| no checkpoint                | post-configuration |     | timeout | <TIMEOUT> |     |
Description
Setsthetimeoutforthecreationofsystemcheckpoints.Thetimeoutspecifiestheamountoftimesincethe
latestconfigurationfortheswitchtocreateasystemcheckpoint.
Thenoformofthiscommandresetsthetimeoutto300seconds,regardlessofthevalueofthe<TIMEOUT>
parameter.
| Parameter |           |     |     | Description |     |
| --------- | --------- | --- | --- | ----------- | --- |
| timeout   | <TIMEOUT> |     |     |             |     |
Specifiesthetimeoutinseconds.Range:5to600.Default:300.
Examples
Settingthetimeoutforsystemcheckpointsto60seconds:
switch(config)#
|     |     | checkpoint | post-configuration |     | timeout 60 |
| --- | --- | ---------- | ------------------ | --- | ---------- |
Resettingthetimeoutforsystemcheckpointsto300seconds:
| switch(config)# |     | no checkpoint | post-configuration |     | timeout 1 |
| --------------- | --- | ------------- | ------------------ | --- | --------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
checkpointrename
133
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| checkpoint | rename <OLD-CHECKPOINT-NAME> |     | <NEW-CHECKPOINT-NAME> |
| ---------- | ---------------------------- | --- | --------------------- |
Description
Renamesanexistingcheckpoint.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<OLD-CHECKPOINT-NAME> Specifiesthenameofanexistingcheckpointtoberenamed.
<NEW-CHECKPOINT-NAME> Specifiesthenewnameforthecheckpoint.Thecheckpointname
canbealphanumeric.Itcanalsocontainunderscores(_)and
dashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitisusedfor
system-generatedcheckpoints.
Examples
Renamingcheckpointckpt1tocfg001:
| switch# | checkpoint | rename ckpt1 | cfg001 |
| ------- | ---------- | ------------ | ------ |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
checkpointrollback
| checkpoint | rollback | {<CHECKPOINT-NAME> | | startup-config} |
| ---------- | -------- | ------------------ | ----------------- |
Description
Appliestheconfigurationfromapre-existingcheckpointorthestartupconfigurationtotherunning
configuration.
| Parameter         |     |     | Description               |
| ----------------- | --- | --- | ------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesacheckpointname. |
startup-config
Specifiesthestartupconfiguration.
Examples
Applyingacheckpointnamedckpt1totherunningconfiguration:
Configurationandfirmwaremanagement |134

| switch# | checkpoint rollback | ckpt1 |     |
| ------- | ------------------- | ----- | --- |
Success
Applyingastartupcheckpointtotherunningconfiguration:
| switch# | checkpoint rollback | startup-config |     |
| ------- | ------------------- | -------------- | --- |
Success
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copycheckpoint<CHECKPOINT-NAME><REMOTE-URL>
| copy checkpoint | <CHECKPOINT-NAME> | <REMOTE-URL> | [vrf <VRF-NAME>] |
| --------------- | ----------------- | ------------ | ---------------- |
Description
Copiesacheckpointconfigurationtoaremotelocationasafile.Theconfigurationisexportedincheckpoint
format,whichincludesswitchconfigurationandrelevantmetadata.
| Parameter         |     | Description                    |     |
| ----------------- | --- | ------------------------------ | --- |
| <CHECKPOINT-NAME> |     | Specifiesthenameofacheckpoint. |     |
<REMOTE-URL> Specifiestheremotedestinationandfilenameusingthesyntax:
|     |     | {tftp | | sftp}://<IP-ADDRESS>[:<PORT-NUMBER>] |
| --- | --- | ----- | -------------------------------------- |
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>
| vrf <VRF-NAME> |     | SpecifiesaVRFname. |     |
| -------------- | --- | ------------------ | --- |
Examples
CopyingcheckpointconfigurationtoremotefilethroughTFTP:
switch# copy checkpoint ckpt1 tftp://192.168.1.10/ckptmeta vrf default
######################################################################### 100.0%
Success
CopyingcheckpointconfigurationtoremotefilethroughSFTP:
135
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

switch# copy checkpoint ckpt1 sftp://root@192.168.1.10/ckptmeta vrf default
The authenticity of host '192.168.1.10 (192.168.1.10)' can't be established.
ECDSA key fingerprint is SHA256:FtOm6Uxuxumil7VCwLnhz92H9LkjY+eURbdddOETy50.
| Are you             | sure you want | to continue       | connecting | (yes/no)? | yes |
| ------------------- | ------------- | ----------------- | ---------- | --------- | --- |
| root@192.168.1.10's | password:     |                   |            |           |     |
| sftp> put           | /tmp/ckptmeta | ckptmeta          |            |           |     |
| Uploading           | /tmp/ckptmeta | to /root/ckptmeta |            |           |     |
Warning: Permanently added '192.168.1.10' (ECDSA) to the list of known hosts.
| Connected | to 192.168.1.10. |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- |
Success
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config}
copy checkpoint <CHECKPOINT-NAME> {running-config | startup-config}
Description
Copiesanexistingcheckpointconfigurationtotherunningconfigurationortothestartupconfiguration.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<CHECKPOINT-NAME>
Specifiesthenameofanexistingcheckpoint.
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationreceivesthecopiedcheckpointconfiguration.Ifthe
startupconfigurationisalreadypresent,thecommandoverwrites
thestartupconfiguration.
Examples
Copyingckpt1checkpointtotherunningconfiguration:
| switch# | copy checkpoint | ckpt1 running-config |     |     |     |
| ------- | --------------- | -------------------- | --- | --- | --- |
Success
Copyingckpt1checkpointtothestartupconfiguration:
| switch# | copy checkpoint | ckpt1 startup-config |     |     |     |
| ------- | --------------- | -------------------- | --- | --- | --- |
Success
CommandHistory
Configurationandfirmwaremanagement |136

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>
| copy checkpoint | <CHECKPOINT-NAME> | <STORAGE-URL> |     |
| --------------- | ----------------- | ------------- | --- |
Description
CopiesanexistingcheckpointconfigurationtoaUSBdrive.Thefileformatisdefinedwhenthecheckpoint
wascreated.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<CHECKPOINT-NAME> Specifiesthenameofthecheckpointtocopy.Thecheckpoint
namecanbealphanumeric.Itcanalsocontainunderscores(_)
anddashes(-).
<STORAGE-URL>> SpecifiesthenameofthetargetfileontheUSBdriveusingthe
followingsyntax:usb:/<FILE>
TheUSBdrivemustbeformattedwiththeFATfilesystem.
Examples
CopyingthetestcheckpointtothetestCheckfileontheUSBdrive:
| switch# | copy checkpoint | test usb:/testCheck |     |
| ------- | --------------- | ------------------- | --- |
Success
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>
| copy <REMOTE-URL> | checkpoint | <CHECKPOINT-NAME> | [vrf <VRF-NAME>] |
| ----------------- | ---------- | ----------------- | ---------------- |
137
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Description

Copies a remote configuration file to a checkpoint. The remote configuration file must be in checkpoint
format.

Parameter

<REMOTE-URL>

<CHECKPOINT-NAME>

Description

Specifies a remote file using the following syntax: {tftp |
sftp}://<IP-ADDRESS>[:<PORT-NUMBER>]
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>>

Specifies the name of the target checkpoint. The checkpoint name
can be alphanumeric. It can also contain underscores (_) and
dashes (-). Required.

NOTE:
Do not start the checkpoint name with CPC because it is used for

system-generated checkpoints.

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Examples

Copying a checkpoint format file to checkpoint ckpt5 on the default VRF:

switch# copy tftp://192.168.1.10/ckptmeta checkpoint ckpt5
######################################################################### 100.0%
100.0%
Success

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

Administrators or local user group members with execution rights
for this command.

copy <REMOTE-URL> {running-config | startup-config}

copy <REMOTE-URL> {running-config | startup-config } [vrf <VRF-NAME>]

Description

Copies a remote file containing a switch configuration to the running configuration or to the startup
configuration.

Configuration and firmware management | 138

Parameter

<REMOTE-URL>

{running-config | startup-config}

Description

Specifies a remote file with the following syntax: {tftp |
sftp}://<IP-ADDRESS>[:<PORT-NUMBER>]
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>

Selects whether the running configuration or the startup
configuration receives the copied checkpoint configuration. If the
startup configuration is already present, the command overwrites
the startup configuration.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

Usage

The switch copies only certain file types. The format of the file is automatically detected from contents of
the file. The startup-config option only supports the JSON file format and checkpoints, but the running-
config option supports the JSON and CLI file formats and checkpoints.

When a file of the CLI format is copied, it overwrites the running configuration. The CLI command does not
clear the running configuration before applying the CLI commands. All of the CLI commands in the file are
applied line-by-line. If a particular CLI command fails, the switch logs the failure and it continues to the next
line in the CLI configuration. The event log (show events -d hpe-config) provides information as to which
command failed.

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

Copying a CLI format file to the startup configuration:

switch# copy tftp://192.168.1.10/startjson startup-config
######################################################################### 100.0%
100.0%
Success

Copying an unsupported file format to the startup configuration:

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

139

| switch# | copy tftp://192.168.1.10/startfile |     | startup-config |
| ------- | ---------------------------------- | --- | -------------- |
######################################################################### 100.0%
100.0%
| unsupported | file format |     |     |
| ----------- | ----------- | --- | --- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>}
copy running-config {startup-config | checkpoint <CHECKPOINT-NAME>}
Description
Copiestherunningconfigurationtothestartupconfigurationortoanewcheckpoint.Ifthestartup
configurationisalreadypresent,thecommandoverwritestheexistingstartupconfiguration.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
startup-config Specifiesthatthestartupconfigurationreceivesacopyofthe
runningconfiguration.
checkpoint <CHECKPOINT-NAME> Specifiesthenameofanewcheckpointtoreceiveacopyofthe
runningconfiguration.Thecheckpointnamecanbealphanumeric.
Itcanalsocontainunderscores(_)anddashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitisusedfor
system-generatedcheckpoints.
Examples
Copyingtherunningconfigurationtothestartupconfiguration:
| switch# | copy running-config | startup-config |     |
| ------- | ------------------- | -------------- | --- |
Success
Copyingtherunningconfigurationtoanewcheckpointnamedckpt1:
| switch# | copy running-config | checkpoint | ckpt1 |
| ------- | ------------------- | ---------- | ----- |
Success
CommandHistory
Configurationandfirmwaremanagement |140

| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy{running-config|startup-config} |     |     | <REMOTE-URL> |     |
| ----------------------------------- | --- | --- | ------------ | --- |
copy {running-config | startup-config} <REMOTE-URL> {cli | json} [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationorthestartupconfigurationtoaremotefileineitherCLIorJSONformat.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationiscopiedtoaremotefile.
<REMOTE-URL> {tftp |
Specifiestheremotefileusingthesyntax:
sftp}://<IP-ADDRESS>[:<PORT-NUMBER>]
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>
| {cli | json}   |     |     | Selectstheremotefileformat:P:CLIorJSON. |     |
| -------------- | --- | --- | --------------------------------------- | --- |
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |
Examples
CopyingarunningconfigurationtoaremotefileinCLIformat:
| switch# | copy running-config | tftp://192.168.1.10/runcli |     | cli |
| ------- | ------------------- | -------------------------- | --- | --- |
######################################################################### 100.0%
Success
CopyingarunningconfigurationtoaremotefileinJSONformat:
| switch# | copy running-config | tftp://192.168.1.10/runjson |     | json |
| ------- | ------------------- | --------------------------- | --- | ---- |
######################################################################### 100.0%
Success
CopyingastartupconfigurationtoaremotefileinCLIformat:
switch# copy startup-config sftp://root@192.168.1.10/startcli cli
| root@192.168.1.10's | password:     |                   |     |     |
| ------------------- | ------------- | ----------------- | --- | --- |
| sftp> put           | /tmp/startcli | startcli          |     |     |
| Uploading           | /tmp/startcli | to /root/startcli |     |     |
141
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- |

| Connected | to 192.168.1.10. |     |
| --------- | ---------------- | --- |
Success
CopyingastartupconfigurationtoaremotefileinJSONformat:
switch# copy startup-config sftp://root@192.168.1.10/startjson json
| root@192.168.1.10's | password:        |                    |
| ------------------- | ---------------- | ------------------ |
| sftp> put           | /tmp/startjson   | startjson          |
| Uploading           | /tmp/startjson   | to /root/startjson |
| Connected           | to 192.168.1.10. |                    |
Success
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy{running-config|startup-config} <STORAGE-URL>
copy {running-config | startup-config} <STORAGE-URL> {cli | json}
Description
CopiestherunningconfigurationorastartupconfigurationtoaUSBdrive.
Parameter Description
| {running-config | | startup-config} |     |
| --------------- | ----------------- | --- |
Selectstherunningconfigurationorthestartupconfigurationto
becopiedtotheswitchUSBdrive.
<STORAGE-URL> Specifiesaremotefilewiththefollowingsyntax:usb:/<file>
{cli | json} Selectstheformatoftheremotefile:CLIorJSON.
Usage
TheswitchsupportsJSONandCLIfileformatswhencopyingtherunningorstartingconfigurationtothe
USBdrive.TheUSBdrivemustbeformattedwiththeFATfilesystem.
TheUSBdrivemustbeenabledandmountedwiththefollowingcommands:
| switch(config)# | usb       |     |
| --------------- | --------- | --- |
| switch(config)# | end       |     |
| switch#         | usb mount |     |
Examples
Configurationandfirmwaremanagement |142

CopyingarunningconfigurationtoafilenamedrunCLIontheUSBdrive:
| switch# | copy running-config | usb:/runCLI | cli |
| ------- | ------------------- | ----------- | --- |
Success
CopyingastartupconfigurationtoafilenamedstartCLIontheUSBdrive:
| switch# | copy startup-config | usb:/startCLI | cli |
| ------- | ------------------- | ------------- | --- |
Success
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copystartup-configrunning-config
| copy startup-config | running-config |     |     |
| ------------------- | -------------- | --- | --- |
Description
Copiesthestartupconfigurationtotherunningconfiguration.
Examples
| switch# | copy startup-config | running-config |     |
| ------- | ------------------- | -------------- | --- |
Success
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy<STORAGE-URL>running-config
copy <STORAGE-URL> {running-config | startup-config | checkpoint <CHECKPOINT-NAME>}
143
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

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
Do not start the checkpoint name with CPC because it is used for

system-generated checkpoints.

Usage

This command requires that the USB drive is formatted with the FAT file system and that the file be in the
appropriate format as follows:

n running-config: This option requires the file on the USB drive be in CLI, JSON, or checkpoint format.

n startup-config: This option requires the file on the USB drive be in JSON or checkpoint format.

n checkpoint <checkpoint-name>: This option requires the file on the USB drive be in checkpoint format.

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

Configuration and firmware management | 144

| switch# | copy usb:/testCheck | checkpoint | abc |
| ------- | ------------------- | ---------- | --- |
Success
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
erase
erase
| checkpoint | <checkpont-name>          |     |     |
| ---------- | ------------------------- | --- | --- |
| core-dump  | all|daemon|dsm|kernel|vsf |     |     |
startup-config
all
Description
Deletesanexistingcheckpoint,startupconfiguration,orcore-dump.
| Parameter  |                   |     | Description                                 |
| ---------- | ----------------- | --- | ------------------------------------------- |
| checkpoint | <CHECKPOINT-NAME> |     | Specifiesthenameofacheckpoint.              |
| core-dump  |                   |     | Eraseoneofthefollowingsetsofcore-dumpfiles: |
| all|daemon | <daemon-name>     |     |                                             |
n all:Eraseallcore-dumpfiles.
|kernel|vsf
n daemon<daemon-name>:Erasedaemoncore-dumpfiles.
kerne:lErasethekernelcore-dump.
n
n vsfErasedaemoncore-dumpfilesforVSF.(For6300Switches
only.)
| startup-config |     |     | Specifiesthestartupconfiguration. |
| -------------- | --- | --- | --------------------------------- |
all
Specifiesallcheckpoints.
Examples
Erasingcheckpointckpt1:
| switch# | erase checkpoint | ckpt1 |     |
| ------- | ---------------- | ----- | --- |
Erasingthestartupconfiguration:
| switch# | erase startup-config |     |     |
| ------- | -------------------- | --- | --- |
145
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Erasingallcheckpoints:
| switch# | erase checkpoint | all |     |
| ------- | ---------------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show checkpoint<CHECKPOINT-NAME>
| show checkpoint | <CHECKPOINT-NAME> |     | [json] |
| --------------- | ----------------- | --- | ------ |
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
AQBapQjwipebv36io0jFfde7ZzrHckncal1D+3n8XFTZKQdmYgAAADEtYOeHSme93xzdD0uz6Vr9Kl+XBzB+
2GB0UBxSF7rvgN2x8KSgkqv7iqXVQ0Te6LkSMnH4BdNaT3Bf25qyvOqmr4YakO1V3rg8zAOADkPktQD8joTH
XflzwomoIzcmv/uX
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
Configurationandfirmwaremanagement |146

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

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

147

!
!
!
| https-server | vrf default |     |     |
| ------------ | ----------- | --- | --- |
Showingtheconfigurationoftheckpt1checkpointinJSONformat:
| switch#    | show checkpoint | ckpt1 json |     |
| ---------- | --------------- | ---------- | --- |
| Checkpoint | configuration:  |            |     |
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
...
...
...
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show checkpoint<CHECKPOINT-NAME>hash
| show checkpoint | <CHECKPOINT-NAME> | hash | [cli | json] |
| --------------- | ----------------- | ---- | ------------ |
Description
ShowsaconfigurationcheckpointhashcalculatedwiththeSHA-256algorithm.Whentheoutputformatis
notspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeenaconfiguration
changesinceaprevioushashwascalculated.
| Parameter         |     |     | Description                        |
| ----------------- | --- | --- | ---------------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesanexistingcheckpointname. |
| [cli | json]      |     |     |                                    |
SelectseithertheCLIorJSONformat.
Examples
ShowingacheckpointSHA-256hashinJSONformat:
Configurationandfirmwaremanagement |148

| switch#     | show checkpoint | ckpt1     | hash json |
| ----------- | --------------- | --------- | --------- |
| Calculating | the hash:       | [Success] |           |
The SHA-256 hash of the checkpoint in JSON format, created in image XX.10.08.xxxx:
cc7a57a9bbb4e6600d3b4180296a35f6af9e797ce9c439955dfe5de58b06da9e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version, | etc.). |     |     |
| ----------- | ------ | --- | --- |
CommandHistory
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show checkpointpost-configuration
| show checkpoint | post-configuration |     |     |
| --------------- | ------------------ | --- | --- |
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
149
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show checkpoint
show checkpoint
Description
Showsadetailedlistofallsavedcheckpoints.
Examples
Showingadetailedlistofallsavedcheckpoints:
| switch# | show checkpoint |                           |               |         |
| ------- | --------------- | ------------------------- | ------------- | ------- |
| NAME    | TYPE            | WRITER DATE(YYYY/MM/DD)   | IMAGE         | VERSION |
| ckpt1   | checkpoint      | User 2017-02-23T00:10:02Z | XX.01.01.000X |         |
| ckpt2   | checkpoint      | User 2017-03-08T18:10:01Z | XX.01.01.000X |         |
| ckpt3   | checkpoint      | User 2017-03-09T23:11:02Z | XX.01.01.000X |         |
| ckpt4   | checkpoint      | User 2017-03-11T00:00:03Z | XX.01.01.000X |         |
| ckpt5   | latest          | User 2017-03-14T01:12:27Z | XX.01.01.000X |         |
CommandHistory
| Release |     | Modification      |            |                        |
| ------- | --- | ----------------- | ---------- | ---------------------- |
| 10.08   |     | Commandsyntaxshow | checkpoint | list allisreplacedwith |
show checkpoint.
| 10.07orearlier |     | --  |     |     |
| -------------- | --- | --- | --- | --- |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show checkpointdate
| show checkpoint | date <START-DATE> | <END-DATE> |     |     |
| --------------- | ----------------- | ---------- | --- | --- |
Description
Showsdetailedlistofallsavedcheckpointscreatedwithinthespecifieddaterange.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Configurationandfirmwaremanagement |150

| Parameter |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
<END-DATE> Specifiestheendingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Examples
Showingadetailedlistofsavedcheckpointsforaspecificdaterange:
| switch# | show checkpoint |            | date | 2017-03-08 | 2017-03-12           |     |               |     |
| ------- | --------------- | ---------- | ---- | ---------- | -------------------- | --- | ------------- | --- |
| NAME    |                 | TYPE       |      | WRITER     | DATE(YYYY/MM/DD)     |     | IMAGE VERSION |     |
| ckpt2   |                 | checkpoint |      | User       | 2017-03-08T18:10:01Z |     | XX.01.01.000X |     |
| ckpt3   |                 | checkpoint |      | User       | 2017-03-09T23:11:02Z |     | XX.01.01.000X |     |
| ckpt4   |                 | checkpoint |      | User       | 2017-03-11T00:00:03Z |     | XX.01.01.000X |     |
CommandHistory
| Release        |     |     |     | Modification                 |            |            |            |              |
| -------------- | --- | --- | --- | ---------------------------- | ---------- | ---------- | ---------- | ------------ |
| 10.08          |     |     |     | Commandsyntaxshow            |            | checkpoint | list date  | <START-DATE> |
|                |     |     |     | <END-DATE>isreplacedwithshow |            |            | checkpoint | date <START- |
|                |     |     |     | DATE>                        | <END-DATE> |            |            |              |
| 10.07orearlier |     |     |     | --                           |            |            |            |              |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show running-confighash
| show running-config |     | hash [cli | |   | json] |     |     |     |     |
| ------------------- | --- | --------- | --- | ----- | --- | --- | --- | --- |
Description
Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutputformat
isnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description |     |     |     |     |
| ------------ | --- | --- | --- | ----------- | --- | --- | --- | --- |
| [cli | json] |     |     |     |             |     |     |     |     |
SelectseithertheCLIorJSONformat.
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
switch#
|             | show running-config |           | hash | cli |     |     |     |     |
| ----------- | ------------------- | --------- | ---- | --- | --- | --- | --- | --- |
| Calculating | the hash:           | [Success] |      |     |     |     |     |     |
151
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |

| SHA-256 | hash of the | config | in CLI | format: |
| ------- | ----------- | ------ | ------ | ------- |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version, | etc.). |     |     |     |
| ----------- | ------ | --- | --- | --- |
CommandHistory
| Release |     |     |     | Modification      |
| ------- | --- | --- | --- | ----------------- |
| 10.08   |     |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show startup-confighash
| show startup-config | hash | [cli | | json] |     |
| ------------------- | ---- | ---- | ------- | --- |
Description
Showsthestartup-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutputformat
isnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description                      |
| ------------ | --- | --- | --- | -------------------------------- |
| [cli | json] |     |     |     | SelectseithertheCLIorJSONformat. |
Examples
Showingthestartup-configcheckpointSHA-256hashinCLIformat:
| switch#     | show startup-config |           | hash   | cli     |
| ----------- | ------------------- | --------- | ------ | ------- |
| Calculating | the hash:           | [Success] |        |         |
| SHA-256     | hash of the         | config    | in CLI | format: |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version, | etc.). |     |     |     |
| ----------- | ------ | --- | --- | --- |
CommandHistory
Configurationandfirmwaremanagement |152

| Release |     | Modification      |
| ------- | --- | ----------------- |
| 10.08   |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
write memory
write memory
Description
Savestherunningconfigurationtothestartupconfiguration.Itisanaliasofthecommand copy running-
config startup-config.Ifthestartupconfigurationisalreadypresent,thiscommandoverwritesthe
startupconfiguration.
Examples
| switch# | write memory |     |
| ------- | ------------ | --- |
Success
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Boot commands
boot fabric-module
| boot fabric-module | <SLOT-ID> |     |
| ------------------ | --------- | --- |
Description
Rebootsthespecifiedfabricmodule.
153
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <SLOT-ID> |     |     | Specifiesthememberandslotofthemoduleintheformat |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Theboot fabric-modulecommandrebootsthespecifiedfabricmodule.Trafficperformanceisaffected
whilethemoduleisdown.
Ifthespecifiedmoduleistheonlyfabricmoduleinanupstate,rebootingthatmodulestopstraffic
switchingbetweenlinemodulesandthelinemodulespowerdown.Thelinemodulespowerupwhenone
fabricmodulereturnstoanupstate.
Thiscommandisvalidforfabricmodulesonly.
Examples
Rebootingthefabricmoduleinslot1/3whenauto-confirmisnotenabled:
| switch# | boot fabric-module | 1/3 |     |
| ------- | ------------------ | --- | --- |
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
| stop traffic | switching   | between | line modules. |
| ------------ | ----------- | ------- | ------------- |
| Do you want  | to continue | (y/n)?  | y             |
switch#
Rebootingthefabricmoduleinslot1/1whenauto-confirmisenabled:
| switch# | boot fabric-module | 1/3 |     |
| ------- | ------------------ | --- | --- |
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
| stop traffic | switching   | between | line modules.  |
| ------------ | ----------- | ------- | -------------- |
| Do you want  | to continue | (y/n) y | (auto-confirm) |
switch#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
boot line-module
| boot line-module | <SLOT-ID> |     |     |
| ---------------- | --------- | --- | --- |
Configurationandfirmwaremanagement |154

Description
Rebootsthespecifiedlinemodule.
| Parameter |     |     |     |     | Description                                     |
| --------- | --- | --- | --- | --- | ----------------------------------------------- |
| <SLOT-ID> |     |     |     |     | Specifiesthememberandslotofthemoduleintheformat |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Thiscommandissupportedonswitchesthathavemultiplelinemodules.
Rebootsthespecifiedlinemodule.Anytrafficfortheswitchpassingthroughtheaffectedmodule(SSH,
TELNET,andSNMP)isinterrupted.Itcantakeupto2minutestorebootthemodule.Duringthattime,you
canmonitorprogressbyviewingtheeventlog.
Thiscommandisvalidforlinemodulesonly.
Examples
Reloadingthemoduleinslot1/1:
| switch# | boot line-module |     | 1/1 |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
This command will reboot the specified line module and interfaces on this
module will not send or receive packets while the module is down. Any
traffic passing through the line module will be interrupted. Management
sessions connected through the line module will be affected. It might take
up to 2 minutes to complete rebooting the module. During that time, you can
| monitor     | progress | by viewing |        | the | event log. |
| ----------- | -------- | ---------- | ------ | --- | ---------- |
| Do you want | to       | continue   | (y/n)? |     | y          |
switch#
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
boot management-module
| boot management-module |     | {active |     | | standby | | <SLOT-ID>} |
| ---------------------- | --- | ------- | --- | --------- | ------------ |
Description
Rebootsthespecifiedmanagementmodule.Choosethemanagementmoduletorebootbyrole(activeor
standby)orbyslotnumber.
155
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| Parameter |     |     |     |     | Description                        |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
| active    |     |     |     |     | Selectstheactivemanagementmodule.  |     |     |
| standby   |     |     |     |     | Selectsthestandbymanagementmodule. |     |     |
<SLOT-ID> Specifiesthememberandslotofthemanagementmoduleinthe
formatmember/slot.Forexample,tospecifythemodulein
member1slot5,enter1/5.
Usage
Thiscommandissupportedonswitchesthathavemultiplemanagementmodules.
Thiscommandrebootsasinglemanagementmoduleinachassis.Choosethemanagementmoduleto
rebootbyrole(activeorstandby)orbyslotnumber.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisavailable,theactive
managementmodulerebootsandthestandbymanagementmodulebecomestheactivemanagement
module.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisnotavailable,you
arewarned,youarepromptedtosavetheconfiguration,andyouarepromptedtoconfirmtheoperation.
Ifyourebootthestandbymanagementmodule,thestandbymanagementmodulerebootsandremains
thestandbymanagementmodule.
Ifyouattempttorebootamanagementmodulethatisnotavailable,thebootcommandisaborted.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereisan
errorduringthesaveoperation,thebootcommandisaborted.
HewlettPackardEnterpriserecommendsthatyouusetheboot management-modulecommandinsteadof
pressingthemoduleresetbuttontorebootamanagementmodulebecauseifyouarerebootingtheonly
availablemanagementmodule,theboot management-modulecommandenablesyoutosavetheconfiguration,
cancelthereboot,orboth.
Examples
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisavailable:
| switch#               | boot | management-module |         | active |          |                 |      |
| --------------------- | ---- | ----------------- | ------- | ------ | -------- | --------------- | ---- |
| The management-module |      |                   | in slot | 1/5    | is going | down for reboot | now. |
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisnotavailable:
| switch#        | boot       | management-module |              | 1/5     |               |                |     |
| -------------- | ---------- | ----------------- | ------------ | ------- | ------------- | -------------- | --- |
| The management |            | module            | in slot      | 1/5     | is currently  | active and     | no  |
| standby        | management |                   | module was   | found.  |               |                |     |
| This will      | reboot     | the               | entire       | switch. |               |                |     |
| Do you         | want       | to save           | the current  |         | configuration | (y/n)? n       |     |
| This will      | reboot     | the               | entire       | switch  | and render    | it unavailable |     |
| until the      | process    |                   | is complete. |         |               |                |     |
Configurationandfirmwaremanagement |156

| Continue   | (y/n)? y |                  |     |
| ---------- | -------- | ---------------- | --- |
| The system | is going | down for reboot. |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
boot set-default
| boot set-default | {primary | | secondary} |     |
| ---------------- | -------- | ------------ | --- |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     | Description                                   |
| --------- | --- | --- | --------------------------------------------- |
| primary   |     |     | Selectstheprimarynetworkoperatingsystemimage. |
secondary
Selectsthesecondarynetworkoperatingsystemimage.
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch# | boot set-default | primary     |     |
| ------- | ---------------- | ----------- | --- |
| Default | boot image set   | to primary. |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
157
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

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

This command reboots the entire system. If you do not select one of the optional parameters, the system
reboots from the configured default boot image.

You can use the show images command to show information about the primary and secondary system
images.

Choosing one of the optional parameters affects the setting for the default boot image:

n If you select the primary or secondary optional parameter, that image becomes the configured default
boot image for future system reboots. The command fails if the switch is not able to set the operating
system image to the image you selected.

You can use the boot set-default command to change the configured default operating system image.

n If you select serviceos as the optional parameter, the configured default boot image remains the same,

and the system reboots all management modules with the service operating system.

If the configuration of the switch has changed since the last reboot, when you execute the boot system
command you are prompted to save the configuration and you are prompted to confirm the reboot
operation.

Saving the configuration is not required. However, if you attempt to save the configuration and there is an
error during the save operation, the boot system command is aborted.

Examples

Rebooting the system from the configured default operating system image:

switch# boot system
Do you want to save the current configuration (y/n)? y
The running configuration was saved to the startup configuration.

Configuration and firmware management | 158

| This will  | reboot the | entire switch    | and render | it unavailable |
| ---------- | ---------- | ---------------- | ---------- | -------------- |
| until the  | process    | is complete.     |            |                |
| Continue   | (y/n)? y   |                  |            |                |
| The system | is going   | down for reboot. |            |                |
Rebootingthesystemfromthesecondaryoperatingsystemimage,settingthesecondaryoperatingsystem
imageastheconfigureddefaultbootimage:
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
| Reboot    | aborted.     |               |               |                |
switch#
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show boot-history
| show boot-history | [all] |     |     |     |
| ----------------- | ----- | --- | --- | --- |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationaboutthe
bootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.Whentheall
parameterisspecified,showsthebootinformationfortheactivemanagementmoduleandallavailableline
modules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandbyconsole.
159
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| all       |     |     | Showsbootinformationfortheactivemanagementmoduleand |
allavailablelinemodules.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereisa
previousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
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
| Current | Boot, up for                       | 22 hrs 12 mins     | 22 secs          |
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
Configurationandfirmwaremanagement |160

| switch#    | show   | boot-history |     | all |     |     |
| ---------- | ------ | ------------ | --- | --- | --- | --- |
| Management | module |              |     |     |     |     |
=================
| Index :     | 3                                  |        |          |           |      |                  |
| ----------- | ---------------------------------- | ------ | -------- | --------- | ---- | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |        |          |           |      |                  |
| Current     | Boot,                              | up for | 22       | hrs 12    | mins | 22 secs          |
| Index :     | 2                                  |        |          |           |      |                  |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |        |          |           |      |                  |
| 07 Aug      | 18 16:28:01                        |        | : Reboot | requested |      | through database |
| Index :     | 1                                  |        |          |           |      |                  |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |        |          |           |      |                  |
| 07 Aug      | 18 14:08:46                        |        | : Reboot | requested |      | through database |
| Index :     | 0                                  |        |          |           |      |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |        |          |           |      |                  |
| 07 Aug      | 18 13:00:46                        |        | : Reboot | requested |      | through database |
| Line module | 1/1                                |        |          |           |      |                  |
=================
| Index : | 3           |     |              |     |         |     |
| ------- | ----------- | --- | ------------ | --- | ------- | --- |
| 10 Aug  | 17 12:45:46 |     | : dune_agent |     | crashed |     |
...
CommandHistory
| Release        |     |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Firmware      | management |            |            |              | commands     |                  |
| ------------- | ---------- | ---------- | ---------- | ------------ | ------------ | ---------------- |
| copy {primary |            | |          | secondary} |              | <REMOTE-URL> |                  |
| copy {primary | |          | secondary} |            | <REMOTE-URL> |              | [vrf <VRF-NAME>] |
Description
UploadsafirmwareimagetoaTFTPorSFTPserver.
| Parameter |     |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | --- | ----------- |
{primary | secondary} Selectstheprimaryorsecondaryimageprofiletoupload.
Required
161
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- |

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<REMOTE-URL> SpecifiestheURLtoreceivetheuploadedfirmwareusingSFTPor
TFTP.ForinformationonhowtoformattheremoteURL,seeURL
formattingforcopycommands.
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | ---------------------------------- | --- | --- |
Examples
TFTPupload:
| switch# | copy primary | tftp://192.0.2.0/00_10_00_0002.swi |     |     |     |
| ------- | ------------ | ---------------------------------- | --- | --- | --- |
######################################################################### 100.0%
| Verifying | and writing | system firmware... |     |     |     |
| --------- | ----------- | ------------------ | --- | --- | --- |
SFTPupload:
| switch#            | copy primary  | sftp://swuser@192.0.2.0/00_10_00_0002.swi |            |          |       |
| ------------------ | ------------- | ----------------------------------------- | ---------- | -------- | ----- |
| swuser@192.0.2.0's |               | password:                                 |            |          |       |
| Connected          | to 192.0.2.0. |                                           |            |          |       |
| sftp> put          | primary.swi   | XL_10_00_0002.swi                         |            |          |       |
| Uploading          | primary.swi   | to /users/swuser/00_10_00_0002.swi        |            |          |       |
| primary.swi        |               |                                           | 100% 179MB | 35.8MB/s | 00:05 |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy {primary | |            | secondary}          | <FIRMWARE-FILENAME> |     |     |
| ------------- | ------------ | ------------------- | ------------------- | --- | --- |
| copy {primary | | secondary} | <FIRMWARE-FILENAME> |                     |     |     |
Description
CopiesafirmwareimagetoUSBstorage.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{primary | secondary} Selectstheprimaryorsecondaryimagefromwhichtocopythe
firmware.Required
Configurationandfirmwaremanagement |162

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<FIRMWARE-FILENAME> SpecifiesthenameofthefirmwarefiletocreateontheUSB
storagedevice.Prefixthefilenamewithusb:/.Forexample:
usb:/firmware_v1.2.3.swi
Forinformationonhowtoformatthepathtoafirmwarefileona
USBdrive,seeUSBURL.
Examples
| switch# | copy primary | usb:/11.10.00.0002.swi |     |
| ------- | ------------ | ---------------------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy primary | secondary |     |     |
| ------------ | --------- | --- | --- |
| copy primary | secondary |     |     |
Description
Copiesthefirmwareimagefromtheprimarytothesecondarylocation.
Examples
| switch#       | copy primary | secondary          |     |
| ------------- | ------------ | ------------------ | --- |
| The secondary | image        | will be deleted.   |     |
| Continue      | (y/n)? y     |                    |     |
| Verifying     | and writing  | system firmware... |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
163
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

copy <REMOTE-URL>
copy <REMOTE-URL> {primary | secondary} [vrf <VRF-NAME>]

Description

Downloads and installs a firmware image from a TFTP or SFTP server.

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

{primary | secondary}

Selects the primary or secondary image profile for receiving the
downloaded firmware. Required.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

TFTP usage

To specify a URL with:

n an IPv4 address: tftp://1.1.1.1/a.txt

n an IPv6 address: tftp://[2000::2]/a.txt

n a hostname: tftp://hpe.com/a.txt

To specify TFTP with:

n the port number of the server in the URL: tftp://1.1.1.1:12/a.txt

n the blocksize in the URL: tftp://1.1.1.1;blocksize=1462/a.txt

The valid blocksize range is 8 to 65464.

n the port number of the server and blocksize in the URL: tftp://1.1.1.1:12;blocksize=1462/a.txt

To specify a file in a directory of URL: tftp://1.1.1.1/dir/a.txt

SFTP usage

To specify:

n A URL with an IPv4 address: sftp://user@1.1.1.1/a.txt

n A URL with an IPv6 address: sftp://user@[2000::2]/a.txt

n A URL with a hostname: sftp://user@hpe.com/a.txt

n SFTP port number of a server in the URL: sftp://user@1.1.1.1:12/a.txt

Configuration and firmware management | 164

AfileinadirectoryofURL:sftp://user@1.1.1.1/dir/a.txt
n
TospecifyafilewithabsolutepathintheURL:sftp://user@1.1.1.1//home/user/a.txt
n
Examples
TFTPdownload:
| switch#     | copy tftp://192.10.12.0/ss.10.00.0002.swi |             |     | primary |     |     |
| ----------- | ----------------------------------------- | ----------- | --- | ------- | --- | --- |
| The primary | image will                                | be deleted. |     |         |     |     |
| Continue    | (y/n)?                                    |             |     |         |     |     |
y
######################################################################### 100.0%
| Verifying | and writing | system firmware... |     |     |     |     |
| --------- | ----------- | ------------------ | --- | --- | --- | --- |
SFTPdownload:
| switch#     | copy sftp://swuser@192.10.12.0/ss.10.00.0002.swi |             |     |     | primary |     |
| ----------- | ------------------------------------------------ | ----------- | --- | --- | ------- | --- |
| The primary | image will                                       | be deleted. |     |     |         |     |
| Continue    | (y/n)? y                                         |             |     |     |         |     |
The authenticity of host '192.10.12.0 (192.10.12.0)' can't be established.
ECDSA key fingerprint is SHA256:L64khLwlyLgXlARKRMiwcAAK8oRaQ8C0oWP+PkGBXHY.
| Are you | sure you want | to continue | connecting | (yes/no)? | yes |     |
| ------- | ------------- | ----------- | ---------- | --------- | --- | --- |
Warning: Permanently added '192.10.12.0' (ECDSA) to the list of known hosts.
| swuser@192.10.12.0's |                 | password: |     |     |     |     |
| -------------------- | --------------- | --------- | --- | --- | --- | --- |
| Connected            | to 192.10.12.0. |           |     |     |     |     |
Fetching /users/swuser/ss.10.00.0002.swi to ss.10.00.0002.swi.dnld
| /users/swuser/ss.10.00.0002.swi |             |                    |     | 100% | 179MB 25.6MB/s | 00:07 |
| ------------------------------- | ----------- | ------------------ | --- | ---- | -------------- | ----- |
| Verifying                       | and writing | system firmware... |     |      |                |       |
CommandHistory
| Release        |     |     | Modification |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy secondary | primary |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- |
| copy secondary | primary |     |     |     |     |     |
Description
Copiesthefirmwareimagefromthesecondarytotheprimarylocation.
Examples
165
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

| switch#     | copy   | secondary  | primary     |             |     |     |     |     |
| ----------- | ------ | ---------- | ----------- | ----------- | --- | --- | --- | --- |
| The primary |        | image will | be deleted. |             |     |     |     |     |
| Continue    | (y/n)? | y          |             |             |     |     |     |     |
| Verifying   | and    | writing    | system      | firmware... |     |     |     |     |
switch# copy sftp://stor@192.22.1.0/im-switch.swi primary vrf mgmt
| The primary |        | image will | be deleted. |     |     |     |     |     |
| ----------- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- |
| Continue    | (y/n)? | y          |             |     |     |     |     |     |
The authenticity of host '192.22.1.0 (192.22.1.0)' can't be established.
ECDSA key fingerprint is SHA256:MyI1xbdKnehYut0NLfL69gDpNzCmZqBVvBaRR46m7o8.
| Are you | sure | you want | to continue | connecting |     | (yes/no)? | yes |     |
| ------- | ---- | -------- | ----------- | ---------- | --- | --------- | --- | --- |
Warning: Permanently added '192.22.1.0' (ECDSA) to the list of known hosts.
| stor@192.22.1.0's      |                        | password:   |        |                           |                           |       |          |       |
| ---------------------- | ---------------------- | ----------- | ------ | ------------------------- | ------------------------- | ----- | -------- | ----- |
| Connected              | to                     | 192.22.1.0. |        |                           |                           |       |          |       |
| sftp> get              | c8d5b9f-topflite.swi   |             |        | c8d5b9f-topflite.swi.dnld |                           |       |          |       |
| Fetching               | /home/dr/im-switch.swi |             |        | to                        | c8d5b9f-topflite.swi.dnld |       |          |       |
| /home/dr/im-switch.swi |                        |             |        |                           | 100%                      | 226MB | 56.6MB/s | 00:04 |
| Verifying              | and                    | writing     | system | firmware...               |                           |       |          |       |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy <STORAGE-URL>
| copy <STORAGE-URL> |     | {primary | | secondary} |     |     |     |     |     |
| ------------------ | --- | -------- | ------------ | --- | --- | --- | --- | --- |
Description
Copies,verifies,andinstallsafirmwareimagefromaUSBstoragedeviceconnectedtotheactive
managementmodule.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<STORAGE-URL> Specifiesthenameofthefirmwarefiletocopyfromthestorage
device.Required.
USBformat:
usb:/<FILENAME>
{primary | secondary} Selectstheprimaryorsecondaryimageprofileforreceivingthe
copiedfirmware.
USB usage
Configurationandfirmwaremanagement |166

Tospecifyafile:
InaUSBstoragedevice:usb:/a.txt
n
n InadirectoryofaUSBstoragedevice:usb:/dir/a.txt
Examples
| switch#     | copy usb:/11.10.00.0002.swi |                    | primary |
| ----------- | --------------------------- | ------------------ | ------- |
| The primary | image will                  | be deleted.        |         |
| Continue    | (y/n)? y                    |                    |         |
| Verifying   | and writing                 | system firmware... |         |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
167
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

Chapter 11

Dynamic Segmentation

Dynamic Segmentation

Dynamic Segmentation (DS) is an enterprise network solution that combines AOS-CX security and
networking features to dynamically place clients into network segments based on client credentials. The
client network segments are dynamically carved out of the enterprise networks when on-boarding secure
clients. With dynamic segmentation, there are multiple ways to handle client traffic:

n Locally switched to a VLAN

n User Based Tunnels (UBT).

n Virtual Network Based Tunnels (VNBT). Also called switch-to-switch dynamic segmentation.

In both solutions, once authenticated (using MAC-Auth or 802.1X) an enterprise client is bound to a network
role and a VLAN is associated with the role. User traffic is then placed on the VLAN (know as the role VLAN)
corresponding to the role to which the user belongs. Role association is defined using the individual client
authentication mode or using device-profile based authentication.

The administrator must pre-configure all potential role VLANs and VRFs in all access switches (and additional
configuration such as IGMP snooping on VLAN, PIM RP, etc.) at the gateway. The switch ensures that the
role VLANs and VRFs are instantiated only upon client on-boarding on the target VLAN (using the command
system vlan-client-presence-detect). This ensures that unnecessary broadcast domain creations and
route learning do not occur.

There is no need to provision VLANs on the switch for user-based tunneling. The reserved VLAN is used by default.

Virtual network based tunneling

Segment definition

Each segment has its own policies. For example, if a group of clients belong to an admin segment, then this
segment can have better QoS and security privileges as compared to the segments assigned to guest clients.

Inter-segment traffic is prohibited between two segments based on policy.

A segment does not map to a network construct such as a VLAN or a VRF. Multiple segments can co-exist
within a VLAN or a segment can span multiple VLANs and VRFs. However, the switch must realize
segmentation using network constructs such as VLANs, VRFs ACLs, etc.

Example

This example illustrates a simple deployment using two VLANs and VRFs.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

168

| Overlay Client | VLAN   | L2 VLAN      |        | Subnet     |             |
| -------------- | ------ | ------------ | ------ | ---------- | ----------- |
| 10             |        | 100          |        | 1.1.1.0/24 |             |
| 20             |        | 200          |        | 2.2.2.0/24 |             |
| Overlay Client |        |              |        |            |             |
|                | L3 VNI | Overlay SVIs | on VRF | Overlay    | ROPs on VRF |
VRF
| A   | 10000 | VLANinterfaceof10,20 |     | ROPinterfacestothenorthof |     |
| --- | ----- | -------------------- | --- | ------------------------- | --- |
n
Core.
onaccess.
VLANinterfacetothe
n
northofCore(ifany
needed).
| Configuration | on switches | A1  | A2  |     | Core |
| ------------- | ----------- | --- | --- | --- | ---- |
|               |             | Y   | Y   |     | N    |
n L2VNI100.
n AnycastGatewayfor1.1.1.0/24.
n VLANinterfacefor10.
|     |     | Y   | Y   |     | N   |
| --- | --- | --- | --- | --- | --- |
n L2VNI200.
AnycastGatewayfor2.2.2.0/24.
n
n VLANinterfacefor20.
|     |     | Y   | Y   |     | Y   |
| --- | --- | --- | --- | --- | --- |
n VRFA.
DynamicSegmentation|169

Configuration on switches

n L3 VRF for A.

n RD, RTs for VRF A. (Can be derived from

L3 VNI too.)

A1

Y

A2

Y

Core

Y

The two VRFs are configured on the core switch, and the two VLANs and VRFs are configured on the two
access switches as required. The two VLANs and the VRF are part of the running config on both access
switches.

Initially, the status of the two VLANs on the access switches is down. This means that:

n EVPN routes - RT-3 (IMET) route, and RT-5 and RT-2 with respect to the VLAN interfaces are not

announced by the switches.

n No VXLAN tunnels are established between any pairs of switches.

When Host H1 connects to A1, the host is authenticated with CPPM and the client is mapped to Role-1 on
VLAN 10. This results in the following:

n The VLAN state changes to up in show commands on A1.

n The L2 and L3 forwarding constructs for the local MAC of H1 are programmed onto VLAN 10 inside A1.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

170

n The IMET route for L2VNI is advertised by A1.

o This route is not used by the core as it does not have footprint of VLAN 10 on it.

o This route is not used by A2 either - this is because it does not have a local VLAN 10 on "up" state as

yet.

n RT-5 prefix route (if enabled) is advertised by A1.

o Upon receiving the route, the core programs the prefix route (1.1.1.0/24). This also results in VxLAN

tunnel programming on the core towards A1.

o A2 still does not use this route, because the VRF is not instantiated on A2 yet.

n The RT-4 and the RT-2 routes are advertised by A1.

o Upon receiving the route, the core programs the route host route (1.1.1.1/32) with BH as A1. But the

existing tunnel towards A1 is reused.

o A2 still does not use this route.

n The BUM domain for VLAN 10 on A1 is still the local host H1. This is because VLAN 10 is not instantiated

on any other switch as yet.

n Any prefix routes from the core is programmed by A1 and it also programs a VxLAN tunnel towards the

core.

When Host H2 connects to A2, the host is authenticated with CPPM and the client is mapped to say Role-1
and the role's VLAN is VLAN 10. This results in the following:

n The VLAN state is changes to "up" in the show commands.

n The L2 and L3 forwarding constructs for the local MAC of H2 is programmed into VLAN 10 inside A2.

Dynamic Segmentation | 171

n The IMET route for L2VNI is advertised by A2.

o This route is not used by the core again as it does not have footprint of VLAN 10 on it.

o This route is used by A1. It creates a VXLAN tunnel towards A2 and adds it to the BUM domain for

VLAN 10.

n RT-5 prefix route (if enabled) is advertised by A2.

o Upon receiving the route, the core programs the prefix route (1.1.1.0/24). In the absence of ECMP,
the existing route in the core is overwritten. This also results in VxLAN tunnel programming on the
core towards A2.

o A1 still does not use this route, this is because the local connected route for 1.1.1.0/24 has higher

priority.

n The RT-4 and the RT-2 routes are advertised by A2.

o Upon receiving the route, the core programs the route host route (1.1.1.2/32). The existing tunnel is

reused.

o A1 programs the 1.1.1.2/32 route into its FIB with NH as VTEP towards A2.

n Any prefix routes from the core are programmed by A2 and it also programs a VxLAN tunnel towards the

core

n Thus a full mesh of VxLAN tunnels is created.

If host H3 connects to A2 and it is on boarded on VLAN 20. This results in the following:

n The VLAN state of VLAN 20 changes to "up" in the show commands

n The L2 and L3 forwarding constructs for the local MAC of H3 is programmed into VLAN 20 inside A2.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

172

n The IMET route for L2VNI is advertised by A2

o This route is not used by the core again as it does not have footprint of VLAN 20 on it.

o This route is not used by A1 either for the same reason.

n RT-5 prefix route (if enabled) is advertised by A2

o Upon receiving the route, the core programs the prefix route (2.2.2.0/24). The core reuses the

existing tunnel.

o A1 also programs the prefix route with NH as A2.

n The RT-4 and the RT-2 routes with respect to H3 are advertised by A2.

o A1 programs its FIB for host route 2.2.2.2/24 with NH as A2. But it reuses the existing tunnel.

o Same behavior on the core.

Additional notes

n Reference counts maintained in the access switches ensure that existing tunnels are reused as and when

new clients come up.

n The clients leaving the VLAN (disconnect/Auth time out etc.) can lead to the reversal of the procedure

described above - i.e. deletion of local programming, withdrawal of routes, VLAN status change, etc. The
reversal is initiated based on reference count.

n Dynamic VLAN instantiation does not mandate VNI association for VLANs. Even local VLANs with secure

clients (if any) are also dynamically instantiated.

User-based tunneling
User-based tunneling uses GRE to tunnel ingress traffic on a switch interface to a mobility gateway for
further processing. User-based tunneling enables a mobility gateway to provide a centralized security policy,
using per-user authentication and access control to ensure consistent access and permissions.

Applications of user-based tunneling include:

n Traffic segmentation: Enables splitting of traffic based on user credentials, rather than the physical port
to which a user is connected. For example, guests on a corporate network can be assigned to a specific
VLAN with access and firewall policies defined to protect the network. Traffic from computers/laptops
can be tunneled, while allowing VoIP traffic to move freely through the wired network.

n Authentication of PoE devices: Many devices that require power over Ethernet (PoE) and network access,

such as security cameras, payment card readers, and medical devices, do not have built-in security
software. As a result, these devices can pose a risk to networks. User-based tunneling can authenticate
these devices and tunnel their traffic to a mobility gateway, harnessing the firewall and policy capabilities
to secure the network.

At the most basic level User-Based Tunneling has two components:

n User-Roles refers to the ability to assign roles, on the fly, to a wired device/user, based on such things as
the access method of a client. When leveraging ClearPass, additional context can be added, such as time-
of-day and type-of-machine. As a result, IT staff no longer must pre-configure an access-port to VLAN
and uplinks.

n Tunneling is the ability to tunnel traffic back to an Aruba Mobility Gateway (previously known as

tunneled-node).

User-based tunneling supports two types of gateway deployments:

Dynamic Segmentation | 173

n Standalone Gateway Support

n Clustered Gateway Support

The recommended gatewayversion for user-based tunneling is 8.5 or greater.

The following commands are required to configure UBT:

n ip source-interface

n ubt

n ubt-client-vlan

ubt-client-vlan is needed for the local vlan or reserved vlan mode, but it is not needed for vlan-extend mode.

ubt-mode vland-extend is needed for vlan extend mode.

Components of user-based tunneling

Clients and devices

Traditionally, ports were labeled with a color and a color was assigned to a specific device. With colorless
ports, all ports on an access switch are set to authenticate with both 802.1X and MAC Authentication. When
a device connects to the network it is authenticated using either MAC Authentication or 802.1X and triggers
an enforcement policy from ClearPass, which contains an enforcement profile with a user role configuration.

Access switches

Access switches authenticate users connected to the switch. Once a device or user is authenticated, a role is
applied to the device or user. A role is a set of attributes and policies that is applied to the device or user.
This user role can exist locally on an access switch or on ClearPass as part of an enforcement profile.

Mobility gateway cluster

The Aruba Mobility Gateway has many built-in security and application capabilities tailored specifically to
wireless traffic. However, this can be extended as well to wired traffic. This is the main reason to tunnel
traffic from an Aruba access switch to a gateway, so the wired, tunneled traffic can take advantage of the
gateway’s firewall capabilities and client applications.

Aruba ClearPass Policy Manager

ClearPass assigns enforcement policies and profiles containing user role information based on profiled
devices or authenticated user information.

How it works

When first configuring the switch, the tunneling profile must be configured first. This is done using the
command ubt zone. Within this context, the primary gateway IP address can be configured, which should
be the physical IP of one of the cluster members. Once the gateway information is known on the switch and
the UBT service is enabled, the switch then performs a handshake with the gateway to determine its
reachability and to discover the version information.

When reachability is confirmed, the switch executes a switch bootstrap, and sends a bootstrap message to
the gateway, similar to an AP Hello between an AP and a gateway. This bootstrap control packet contains
user role information. Once the gateway receives the message, it replies with an acknowledge message.
When acknowledged, the switch updates its local data structures with a bucket map and gateway node list,
which is used for mapping users to gateways and client load balancing.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

174

After the bucket map list is downloaded to the switch, a GRE heartbeat is then started between the switch
and the gateway, forming a tunnel. A regular heartbeat, using GRE, is exchanged with the gateway, which
then serves as the switch anchor gateway (SAC). This is the primary-gateway ip in the ubt zone command.
A secondary heartbeat is also established with a standby gateway, acting as a secondary switch anchor
gateway (s-SAC).

When a user connects to a secure port, the authentication sub-system on the switch sends a RADIUS
request to the RADIUS server (for example, ClearPass Policy Manager), which authenticates the user and
returns a user role to the switch in the form of a local user role (LUR), downloadable user role (DUR) or
vendor-specific attribute (VSA).

For a downloadable user role, the entire role itself is downloaded to the switch containing the user role via a VSA.

Aruba utilizes the concept of a user role which contains user policy and access to the network based on the
role. A user-role can contain ACL/QoS policy, captive portal, VLAN information (used for locally switched
traffic), and device attributes. When the user role VSA, received from the RADIUS server, is applied to the
user, a command to redirect traffic to a gateway can be included within the user role. This is defined with the
gateway zone command which causes tunneling to be enabled. The authentication sub-system notifies the
tunneling subsystem on the switch, providing a gateway or secondary role. The gateway or secondary role is
the user role on the gateway where policy will generally exist for tunneled users, and where firewall and
security policies are applied. This can also be the same role used for wireless users and can be reused for
wired users, if feasible.

The gateway role information sent to the switch tunneling subsystem is an indication to the gateway that it
has to enforce additional policies on the user’s traffic based on the policy configuration associated with the
secondary role and the tunnel. This secondary role can be downloaded directly to the gateway. When the
primary gateway or cluster is not reachable, the SAC tunnel is formed with the backup gateway and the
clients are tunneled to the backup.

Multi-zone in UBT

The multizone feature allows a switch to host users whose traffic is tunneled to different gateway clusters.
Each UBT zone corresponds to a unique Gateway cluster or a standalone gateway. Each UBT zone is
mapped to VRF on a switch/stack. The zone configuration is local to the switch and it provides isolation of
user traffic across different gateway clusters.

Multizone is supported for both UBT modes (local VLAN and VLAN extend). The maximum number of UBT
zones that can be configured is eight per switch/stack. All UBT zones configured on a switch/stack will either
be in local VLAN or VLAN extend mode. Mixed mode is not supported across zones on the same
switch/stack. Multiple UBT zones per single VRF on a switch/stack is also supported.

Points to remember

n UBT Mode: Local VLAN

o UBT is supported on the default VRF and non-default VRF.

o Source interface is specified using command ip source-interface.

o VLAN is specified using command ubt-client-vlan.

o ubt-client-vlan should not be used on any other feature on the switch except for the client IP

address tracking feature.

o UBT does not support tagged clients.

o UBT clients and non-UBT clients on same VLAN and same port is not supported.

o Source interface change: Disable UBT, change the source-interface, enable UBT.

Dynamic Segmentation | 175

| UBT Mode: | VLAN | extend |     |     |     |
| --------- | ---- | ------ | --- | --- | --- |
n
UBTissupportedonthedefaultVRFandnon-defaultVRF.
o
| o Sourceinterfaceisspecifiedusingcommandip |     |     |     |     | source-interface. |
| ------------------------------------------ | --- | --- | --- | --- | ----------------- |
o UBTclientvlanisdefinedunderrole.
DHCPsnoopingandND-snoopingshouldnotenabledonaUBTclientassignedVLAN.
o
o IGMPsnoopingshouldnotbeenabledonaUBTclientassignedVLAN.
o TheVLANonwhichUBTclientsareplacedshouldnotbeconfiguredontheswitchuplink.
o UBTclientsandnon-UBTclientsonthesameVLANonthesameswitchisnotsupported.
o Sourceinterfacechange:DisableUBT,changethesource-interface,enableUBT.
| n Gateway | DUR |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
o DownloadablegatewayroleissupportedwithswitchVSAonly.Mixedmoderoleconfigurationis
supported((switchLUR+gatewayradiusVSA)+gatewayDUR).Switchmixedroleisusedtosend
otherroleattributesalongwithVSA.
l Useaaa authentication port-access radius-overide enabletoenable.
o CPPMserverFQDN/hostnameconfigurationissupported.
ForinformationonIP ClientTracker,refertotheIPClientTrackerchapterintheFundamentalsGuide.
n Multi-zone
o TotalnumberofUBTzonessupportedonswitch/stackis8.
o MultipleUBTzonespersingleVRFisalsosupported.
o ThetotalnumberofsupportedUBTusersacrossdifferentzonesonaswitch/stackis1017.
o OverlappinguserroleVLAN(s)shouldnotbepresentacrossUBTzonesonaswitch.
Thiswillleadtoonezonetraffic(multicastandbroadcast)reachingotherzone(s)onthesameswitch.
| n PCbehindan | IPphone |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- |
YoushouldnothaveaPCandphoneonthesameVLANonthesameportwhenthePCisaUBTclient
andthephoneisanon-UBTclient.Ifyoudo,UBTclientsbroadcast/multicastpacketswillreturntothe
sameportandcorruptthephoneMACtable.
| Clients | behindan | L2 switch | on the | same VLAN |     |
| ------- | -------- | --------- | ------ | --------- | --- |
n
YoushouldnothaveclientsbehindanL2switchinaUBTenvironment.IfUBTandnon-UBTclientsare
behindanL2switchonthesameVLAN,thiswillcauseduplicatepackets.Broadcast/multicastpacketswill
becopiedtothetunnelandlocally,causingtheclienttoreceiveduplicatepacketsandnetworkinstability.
ConnectingtheclientdirectlyintoswitchportsorbehindVoIPisrecommended.
| Comparison                 | between   | UBTmodes |     |                         |             |
| -------------------------- | --------- | -------- | --- | ----------------------- | ----------- |
| UBT Mode:                  | LocalVLAN |          |     | UBT Mode:               | VLAN extend |
| SwitchunawareofUBTuserVLAN |           |          |     | SwitchisawareofuserVLAN |             |
Colorlessports:NoUBTuserVLANconfig Colorlessports:UBTUserVLANconfigisrequiredonswitch
atswitch
176
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| UBT Mode: | LocalVLAN | UBT Mode: | VLAN extend |
| --------- | --------- | --------- | ----------- |
VLANassignmentbygateway VLANassignmentbyswitch
SupportsonlyuntaggedUBTusers Supportsbothtagged/untaggedUBTusers
Gatewayreplicatesthe SinglededicatedmulticastGREtunnelwillbeestablishedbetween
broadcast/multicasttraffic(converting thegatewayandswitchforBroadcast/Multicasttraffic
bcast/mcasttounicast)andsendsitto
everyUBTclient
Gatewayforwardsallbroadcast/multicast Switchwillforwardthebroadcast/multicasttraffictotheUBT
traffictotheUBTclientswhicharepartof clientswhicharepartofthesameVLAN
thesameVLAN
Theunicast/multicast/broadcasttraffic TheunicasttrafficfromgatewaytoswitchissentthroughtheUAC
fromgatewaytoswitchissenttothe tunnelandmulticast/broadcasttrafficviaMulticastGREtunnel
clientsviathesameUACtunnel
Multicasttrafficwillbesenttotheclient MulticasttrafficwillbesenttoallUBTclientsonthesameVLAN
whichsendjoin
| User-based           | tunneling    | commands |     |
| -------------------- | ------------ | -------- | --- |
| backup-controller    | ip           |          |     |
| backup-controller    | ip <IP-ADDR> |          |     |
| no backup-controller | ip <IP-ADDR> |          |     |
Description
SpecifiestheIPaddressofthebackupcontrollerfortheUBTzone.
ThenoformofthiscommanddeletestheIPaddressofthebackupcontroller.
Parameter Description
<IP-ADDR> SpecifiestheIPaddressofthebackupcontroller.
Examples
Specifyingthebackupcontrolleripaddressforzone1:
| switch(config)#           | ubt zone | zone1             |                 |
| ------------------------- | -------- | ----------------- | --------------- |
| switch(config-ubt-zone1)# |          | backup-controller | ip 10.116.51.11 |
DeletetheconfiguredbackupcontrollerIPaddress:
| switch(config)#           | ubt zone | zone1                |                 |
| ------------------------- | -------- | -------------------- | --------------- |
| switch(config-ubt-zone1)# |          | no backup-controller | ip 10.116.51.11 |
CommandHistory
DynamicSegmentation|177

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
| 6400 |     | rightsforthiscommand. |
| ---- | --- | --------------------- |
enable
enable
no enable
Description
EnablestheUBTzone.
ThenoformofthiscommanddisablestheUBTzone.
Examples
EnablingUBTforzonezone1:
switch(config)#
ubt zone zone1
switch(config-ubt-zone1)# enable
DisablingUBTforzone1:
| switch(config)#           | ubt zone zone1 |     |
| ------------------------- | -------------- | --- |
| switch(config-ubt-zone1)# | no enable      |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
| 6400 |     | rightsforthiscommand. |
| ---- | --- | --------------------- |
ip source-interface
ip source-interface {all | ubt} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
no ip source-interface {all | ubt} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
Description
178
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Sets a single source IP address for the UBT zone VRF. This ensures that all traffic sent by UBT zone/VRF has
the same source IP address, regardless of how it egresses the switch.

This command provides two ways to set the source IP addresses: either by specifying a static IP address, or
by using the address assigned to a switch interface. If you define both options, then the static IP address
takes precedence.

The no form of this command deletes the single source IP address for UBT.

Parameter

all

interface <IFNAME>

<IPV4-ADDR>

vrf <VRF-NAME>

Examples

Description

When used no other parameters are required.

Specifies the name of the interface from which UBT obtains its
source IP address. The interface must have a valid IP address
assigned to it. If the interface has both a primary and secondary IP
address, the primary IP address is used.

Specifies the source IP address to use for UBT. The IP address
must be defined on the switch, and it must exist on the specified
VRF, Default: default. Specify the address in IPv4 format
(x.x.x.x), where x is a decimal number from 0 to 255.

Specifies the name of the VRF from which the UBT zone sets its
source IP address.

On the 6400 Switch Series, interface identification differs.

Setting interface 1/1/7 as the source address for UBT for VRF default:

switch(config)# ip source-interface ubt interface 1/1/7 vrf default

Deleting the configured source interface 1/1/7 as the source address for UBT for VRF default:

switch(config)# no ip source-interface ubt interface 1/1/7 vrf default

Specifying the static IP address 1.1.1.1 as the source address for UBT for VRF default:

switch(config)# ip source-interface ubt 1.1.1.1 vrf default

Deleting the configured ip address as the source address for UBT for VRF default:

switch(config)# no ip source-interface ubt 1.1.1.1 vrf default

Command History

Release

10.07 or earlier

Command Information

Modification

--

Dynamic Segmentation | 179

| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
papi-security-key
| papi-security-key | [{ciphertext | <SEC-KEY> | | plaintext | <SEC-KEY>}] |     |
| ----------------- | ------------ | --------- | ----------- | ----------- | --- |
no papi-security-key
Description
SpecifiesthesharedsecuritykeyusedtoencryptUBTPAPImessagesexchangedbetweentheswitchand
thecontrollerclusterforthezone.
Thenoformofthiscommanddeletesthesharedsecuritykey.
| Parameter  |           |     | Description |     |     |
| ---------- | --------- | --- | ----------- | --- | --- |
| ciphertext | <SEC-KEY> |     |             |     |     |
Specifiesanencryptedsecuritykey.
plaintext <SEC-KEY> Specifiesaplaintextsecuritykey.Range:10to64characters.
NOTE:
Whenthesecuritykeyisnotprovidedonthecommandline,plaintext
securitykeypromptingoccursuponpressingEnter.Theenteredsecurity
keycharactersaremaskedwithasterisks..
Examples
SpecifyingthePAPIsecuritykeyforUBTzonezone1asplaintext:
| switch(config)#                    | ubt zone          | zone1             |                              |           |          |
| ---------------------------------- | ----------------- | ----------------- | ---------------------------- | --------- | -------- |
| switch(config-ubt-zone1)#          |                   | papi-security-key |                              | plaintext | F82#450b |
| SpecifyingthePAPIsecuritykeyforUBT |                   |                   | zone2withplaintextprompting: |           |          |
| switch(config)#                    | ubt zone          | zone2             |                              |           |          |
| switch(config-ubt-zone2)#          |                   | papi-security-key |                              |           |          |
| Enter the                          | PAPI security     | key: **********   |                              |           |          |
| Re-Enter                           | the PAPI security | key:              | **********                   |           |          |
SpecifyingthePAPIsecuritykeyforUBTzone1asciphertext:
| switch(config)# | ubt zone | zone1 |     |     |     |
| --------------- | -------- | ----- | --- | --- | --- |
switch(config-ubt-zone1)# papi-security-key ciphertext AQBapdAVz5...RmH3+4cpg=
RemovingthePAPIsecuritykeyforUBTzone1:
| switch(config)#           | ubt zone | zone1                |     |     |     |
| ------------------------- | -------- | -------------------- | --- | --- | --- |
| switch(config-ubt-zone1)# |          | no papi-security-key |     |     |     |
CommandHistory
180
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- |

| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
| 6400                  |              |     | rightsforthiscommand. |     |
| --------------------- | ------------ | --- | --------------------- | --- |
| primary-controller    | ip           |     |                       |     |
| primary-controller    | ip <IP-ADDR> |     |                       |     |
| no primary-controller | ip <IP-ADDR> |     |                       |     |
Description
SpecifiestheIPaddressoftheprimarycontrollerIPaddressforthezone.
ThenoformofthiscommanddeletestheIPaddressoftheprimarycontroller.
| Parameter |     |     | Description                                  |     |
| --------- | --- | --- | -------------------------------------------- | --- |
| <IP-ADDR> |     |     | SpecifiestheIPaddressoftheprimarycontroller. |     |
Examples
SpecifytheprimarycontrollerIPaddressforzone1:
| switch(config)#           | ubt zone | zone1              |     |                 |
| ------------------------- | -------- | ------------------ | --- | --------------- |
| switch(config-ubt-zone1)# |          | primary-controller |     | ip 10.116.51.10 |
DeletetheconfiguredprimarycontrollerIPaddress:
| switch(config)#           | ubt zone | zone1                 |     |                 |
| ------------------------- | -------- | --------------------- | --- | --------------- |
| switch(config-ubt-zone1)# |          | no primary-controller |     | ip 10.116.51.10 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
sac-heartbeat-interval
DynamicSegmentation|181

| sac-heartbeat-interval    |     | <TIME> |        |     |     |
| ------------------------- | --- | ------ | ------ | --- | --- |
| no sac-heartbeat-interval |     |        | <TIME> |     |     |
Description
SpecifiestheSACheartbeatrefreshtimeintervalinseconds.
Thenoformofthiscommandsetstheheartbeatintervaltothedefaultvalue.
| Parameter |     |     |     | Description                                           |     |
| --------- | --- | --- | --- | ----------------------------------------------------- | --- |
| <TIME>    |     |     |     | SpecifiestheSACheartbeatrefreshtimeintervalinseconds. |     |
Range:1to8.Default:1.
Examples
Specifyingaheartbeatrefreshintervalof1forUBTzone1:
| switch(config)#           |     | ubt zone | zone1                  |     |     |
| ------------------------- | --- | -------- | ---------------------- | --- | --- |
| switch(config-ubt-zone1)# |     |          | sac-heartbeat-interval |     | 1   |
Deletingtheconfiguredheartbeatrefreshinterval:
| switch(config)#           |     | ubt zone | zone1                     |     |     |
| ------------------------- | --- | -------- | ------------------------- | --- | --- |
| switch(config-ubt-zone1)# |     |          | no sac-heartbeat-interval |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
| 6400    |                     |     |     | rightsforthiscommand. |     |
| ------- | ------------------- | --- | --- | --------------------- | --- |
| show    | ip source-interface |     | ubt |                       |     |
| show ip | source-interface    | ubt |     |                       |     |
Description
DisplayssourceIPaddressconfigurationinformationfortheUBTzone(s).
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingsourceIPaddressconfigurationinformation:
| switch(config)# |     | show ip | source-interface | ubt |     |
| --------------- | --- | ------- | ---------------- | --- | --- |
182
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| Source-interface |     | Configuration |     | Information |     |     |     |
| ---------------- | --- | ------------- | --- | ----------- | --- | --- | --- |
---------------------------------------------------------------------
| Protocol |     | Src-Interface |     |     | Src-IP | VRF |     |
| -------- | --- | ------------- | --- | --- | ------ | --- | --- |
---------------------------------------------------------------------
| ubt |     | vlan10 |     |     | 10.1.1.2 | default |     |
| --- | --- | ------ | --- | --- | -------- | ------- | --- |
| ubt |     | vlan20 |     |     | 20.1.1.2 | blue    |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 6400            | (#) |     |     |     | forthiscommand. |     |     |
| --------------- | --- | --- | --- | --- | --------------- | --- | --- |
| show capacities |     | ubt |     |     |                 |     |     |
| show capacities |     | ubt |     |     |                 |     |     |
Description
ShowsthemaximumnumberofUBTclientsandzoneswhichcanbeconfiguredinthesystem.
Example
| switch#            | show | capacities | ubt |     |     |     |       |
| ------------------ | ---- | ---------- | --- | --- | --- | --- | ----- |
| System Capacities: |      | Filter     | UBT |     |     |     |       |
| Capacities         | Name |            |     |     |     |     | Value |
--------------------------------------------------------------------------------
| Maximum | number | of UBT | clients | in      | a system |     | 1017 |
| ------- | ------ | ------ | ------- | ------- | -------- | --- | ---- |
| Maximum | number | of UBT | zones   | per VRF |          |     | 1    |
| Maximum | number | of UBT | zones   |         |          |     | 8    |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
DynamicSegmentation|183

| Platforms | Commandcontext |     | Authority                                            |     |
| --------- | -------------- | --- | ---------------------------------------------------- | --- |
| 6300      |                |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ubt         |             |         |     |     |
| ---------------- | ----------- | ------- | --- | --- |
| show ubt [brief] |             |         |     |     |
| show ubt zone    | <ZONE-NAME> | [brief] |     |     |
Description
ShowsglobalconfigurationinformationforUBTinadditiontodetailedorbriefinformationforaspecific
UBTzone.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
zone <ZONE-NAME> Specifiesthenameofazone.Length:1to64characters.
| brief |     |     | Displaysbriefinformation. |     |
| ----- | --- | --- | ------------------------- | --- |
Examples
ShowingglobalUBTconfigurationinformationwherelocal-VLANmodehasbeenconfigured:
| switch#       | show ubt        |                        |     |            |
| ------------- | --------------- | ---------------------- | --- | ---------- |
| Zone Name     |                 | : zone1                |     |            |
| UBT Mode      |                 | : local-vlan           |     |            |
| Primary       | Controller      | : 10.116.51.10         |     |            |
| Backup        | Controller      | : 10.116.51.11         |     |            |
| SAC HeartBeat | Interval        | : 1                    |     |            |
| UAC KeepAlive | Interval        | : 60                   |     |            |
| Reserved      | VLAN Identifier | : 4094                 |     |            |
| VRF Name      |                 | : default              |     |            |
| Admin State   |                 | : ENABLED              |     |            |
| PAPI Security | Key             | : AQBapdxySvGPvdTl     |     | ... bL4FE= |
| Zone Name     |                 | : zone2                |     |            |
| UBT Mode      |                 | : local-vlan           |     |            |
| Primary       | Controller      | : 1.1.5.10             |     |            |
| Backup        | Controller      | : 1.1.5.11             |     |            |
| SAC HeartBeat | Interval        | : 1                    |     |            |
| UAC KeepAlive | Interval        | : 60                   |     |            |
| Reserved      | VLAN Identifier | : 4094                 |     |            |
| VRF Name      |                 | : blue                 |     |            |
| Admin State   |                 | : ENABLED              |     |            |
| PAPI Security | Key             | : TRQapdxySvGPvdTlkYn1 |     | ... zP4FE= |
ShowingglobalUBTconfigurationinformationwhereVLAN-extendmodehasbeenconfigured:
| switch#   | show ubt   |                |     |     |
| --------- | ---------- | -------------- | --- | --- |
| Zone Name |            | : zone1        |     |     |
| UBT Mode  |            | : vlan-extend  |     |     |
| Primary   | Controller | : 10.116.51.10 |     |     |
184
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| Backup Controller  |                 | : 10.116.51.11         |            |
| ------------------ | --------------- | ---------------------- | ---------- |
| SAC HeartBeat      | Interval        | : 1                    |            |
| UAC KeepAlive      | Interval        | : 60                   |            |
| Reserved           | VLAN Identifier | : -NA-                 |            |
| VRF Name           |                 | : default              |            |
| Admin State        |                 | : ENABLED              |            |
| PAPI Security      | Key             | : AQBapdxySvGPvdTlkYn1 | ... bL4FE= |
| Zone Name          |                 | : zone2                |            |
| UBT Mode           |                 | : vlan-extend          |            |
| Primary Controller |                 | : 1.1.5.10             |            |
| Backup Controller  |                 | : 1.1.5.11             |            |
| SAC HeartBeat      | Interval        | : 1                    |            |
| UAC KeepAlive      | Interval        | : 60                   |            |
| Reserved           | VLAN Identifier | : -NA-                 |            |
| VRF Name           |                 | : blue                 |            |
| Admin State        |                 | : ENABLED              |            |
| PAPI Security      | Key             | : TRQapdxySvGPvdTlkYn1 | ... zP4FE= |
ShowingglobalUBTconfigurationinformationwheremulti-zonehasbeenconfigured:
| switch# show       | ubt             |                |     |
| ------------------ | --------------- | -------------- | --- |
| Zone Name          |                 | : zone1        |     |
| UBT Mode           |                 | : vlan-extend  |     |
| Primary Controller |                 | : 10.10.10.251 |     |
| Backup Controller  |                 | : ---/---      |     |
| SAC HeartBeat      | Interval        | : 1            |     |
| UAC KeepAlive      | Interval        | : 60           |     |
| Reserved           | VLAN Identifier | : ---/---      |     |
| VRF Name           |                 | : default      |     |
| Admin State        |                 | : ENABLED      |     |
| PAPI Security      | Key             | : DISABLED     |     |
| Operational        | State           | : Up           |     |
| Zone Name          |                 | : zone2        |     |
| UBT Mode           |                 | : vlan-extend  |     |
| Primary Controller |                 | : 162.10.0.6   |     |
| Backup Controller  |                 | : ---/---      |     |
| SAC HeartBeat      | Interval        | : 1            |     |
| UAC KeepAlive      | Interval        | : 60           |     |
| Reserved           | VLAN Identifier | : ---/---      |     |
| VRF Name           |                 | : default      |     |
| Admin State        |                 | : ENABLED      |     |
| PAPI Security      | Key             | : DISABLED     |     |
| Operational        | State           | : Up           |     |
| Zone Name          |                 | : zone3        |     |
| UBT Mode           |                 | : vlan-extend  |     |
| Primary Controller |                 | : 20.20.20.11  |     |
| Backup Controller  |                 | : ---/---      |     |
| SAC HeartBeat      | Interval        | : 1            |     |
| UAC KeepAlive      | Interval        | : 60           |     |
| Reserved           | VLAN Identifier | : ---/---      |     |
| VRF Name           |                 | : default      |     |
| Admin State        |                 | : ENABLED      |     |
| PAPI Security      | Key             | : DISABLED     |     |
| Operational        | State           | : Up           |     |
ShowingglobalUBTconfigurationinformationwithoperationalstatedownfailurereason:
DynamicSegmentation|185

| switch# show       | ubt             |                |     |     |     |
| ------------------ | --------------- | -------------- | --- | --- | --- |
| Zone Name          |                 | : my-zone      |     |     |     |
| UBT Mode           |                 | : local-vlan   |     |     |     |
| Primary Controller |                 | : 10.116.51.10 |     |     |     |
| Backup Controller  |                 | : 10.116.51.11 |     |     |     |
| SAC HeartBeat      | Interval        | : 1            |     |     |     |
| UAC KeepAlive      | Interval        | : 60           |     |     |     |
| Reserved           | VLAN Identifier | : 4094         |     |     |     |
| VRF Name           |                 | : my-vrf       |     |     |     |
| Admin State        |                 | : ENABLED      |     |     |     |
| PAPI Security      | Key             | :              |     |     |     |
AQBapdxySvGPvdTlkYn1/naKX4O3jKHrm28xLYfO6mLOK499BwAAAHdJp/bL4FE=
| Operational        | State           | : up           |     |     |     |
| ------------------ | --------------- | -------------- | --- | --- | --- |
| Zone Name          |                 | : my-zone2     |     |     |     |
| UBT Mode           |                 | : local-vlan   |     |     |     |
| Primary Controller |                 | : 10.116.51.10 |     |     |     |
| Backup Controller  |                 | : 10.116.51.11 |     |     |     |
| SAC HeartBeat      | Interval        | : 1            |     |     |     |
| UAC KeepAlive      | Interval        | : 60           |     |     |     |
| Reserved           | VLAN Identifier | : 4094         |     |     |     |
| VRF Name           |                 | : my-vrf2      |     |     |     |
| Admin State        |                 | : ENABLED      |     |     |     |
| PAPI Security      | Key             | :              |     |     |     |
AQBapdxySvGPvdTlkYn1/naKX4O3jKHrm28xLYfO6mLOK499BwAAAHdJp/bL4FE=
| Operational    | State | : down       |                |     |     |
| -------------- | ----- | ------------ | -------------- | --- | --- |
| Failure Reason |       | : Controller | is unreachable |     |     |
ShowingbriefglobalUBTconfigurationinformationwherelocal-VLANmodehasbeenconfigured:
| switch(config)# | show ubt | brief |     |     |     |
| --------------- | -------- | ----- | --- | --- | --- |
------------------------------------------------------------------------------------
------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
| Operational | State |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
------------------------------------------------------------------------------------
------------------
| zone1 | local-vlan | 10.116.51.10 |     | default | Enabled |
| ----- | ---------- | ------------ | --- | ------- | ------- |
up
| zone2 | local-vlan | 20.116.51.20 |     | vrf2 | Enabled |
| ----- | ---------- | ------------ | --- | ---- | ------- |
down
| zone3 | local-vlan | 30.116.51.30 |     | vrf3 | Enabled |
| ----- | ---------- | ------------ | --- | ---- | ------- |
up
ShowingbriefglobalUBTconfigurationinformationwhereVLAN-extendmodehasbeenconfigured:
| switch# show | ubt brief |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
------------------------------------------------------------------------------------
------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
| Operational | State |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
------------------------------------------------------------------------------------
------------------
| zone1 | vlan-extend | 10.116.51.10 |     | default | Enabled |
| ----- | ----------- | ------------ | --- | ------- | ------- |
up
| zone2 | vlan-extend | 20.116.51.20 |     | vrf2 | Enabled |
| ----- | ----------- | ------------ | --- | ---- | ------- |
down
186
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| zone3 | vlan-extend | 30.116.51.30 |     | vrf3 | Enabled |
| ----- | ----------- | ------------ | --- | ---- | ------- |
up
ShowingbriefconfigurationforUBTzone1wherelocal-VLANmodehasbeenconfigured:
| switch# | show ubt zone zone1 | brief |     |     |     |
| ------- | ------------------- | ----- | --- | --- | --- |
--------------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
--------------------------------------------------------------------------------
| zone1 | local-vlan | 10.116.51.10 |     | default | Enabled |
| ----- | ---------- | ------------ | --- | ------- | ------- |
ShowingbriefconfigurationforUBTzone1whereVLAN-extendmodehasbeenconfigured:
switch#
|     | show ubt zone zone1 | brief |     |     |     |
| --- | ------------------- | ----- | --- | --- | --- |
--------------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
--------------------------------------------------------------------------------
| zone1 | vlan-extend | 10.116.51.10 |     | default | Enabled |
| ----- | ----------- | ------------ | --- | ------- | ------- |
ShowingbriefglobalUBTconfigurationinformationwhereVLAN-extendmodehasbeenconfigured:
| switch# | show ubt zone zone1 | brief |     |     |     |
| ------- | ------------------- | ----- | --- | --- | --- |
--------------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
--------------------------------------------------------------------------------
| zone1 | vlan-extend | 10.116.51.10 |     | default | Enabled |
| ----- | ----------- | ------------ | --- | ------- | ------- |
CommandHistory
| Release |     | Modification                             |     |     |     |
| ------- | --- | ---------------------------------------- | --- | --- | --- |
| 10.09   |     | FailureReasonfieldaddedintheoutputofshow |     |     | ubt |
n
command.
|     |     | n Operational | Statecolumnaddedintheoutputofshow |     | ubt |
| --- | --- | ------------- | --------------------------------- | --- | --- |
briefcommand.
| 10.07orearlier |     | --  |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 6400 | (#) |     |     |     |     |
| ---- | --- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ubt | information |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
show ubt information
| show ubt information | zone <ZONE-NAME> |     |     |     |     |
| -------------------- | ---------------- | --- | --- | --- | --- |
Description
DynamicSegmentation|187

ShowsSACandUACinformationforUBT.SpecifyingazonenamedisplaysUBTinformationforthatzone.
Parameter Description
ZONE-NAME SpecifiesUBTzonename.Maximumcharacters:64.
Examples
ShowingSACandUACinformationforthetunnelednodeserver:
| switch(config)# | show | ubt information |     |
| --------------- | ---- | --------------- | --- |
=====================================================================
Zone zone1:
=====================================================================
| SAC Information | :           |            |     |
| --------------- | ----------- | ---------- | --- |
| Active          | :           | 10.1.1.2   |     |
| Standby         | :           | 10.1.1.3   |     |
| Node List       | Information | :          |     |
| Cluster         | Name        | : cluster1 |     |
| Cluster         | Alias Name  | :          |     |
| Node            | List :      |            |     |
----------------
10.1.1.2
10.1.1.3
10.1.1.4
| Bucket | Map Information | :           |              |
| ------ | --------------- | ----------- | ------------ |
| Bucket | Map Active      | : [0...255] |              |
| Bucket | ID A-UAC        | S-UAC       | Connectivity |
----------------------------------------------------------
| 0   | 10.1.1.2 | 10.1.1.3 | L2  |
| --- | -------- | -------- | --- |
| 1   | 10.1.1.3 | 10.1.1.4 | L2  |
| 2   | 10.1.1.4 | 10.1.1.2 | L2  |
...
=====================================================================
Zone zone2:
=====================================================================
| SAC Information | :           |            |     |
| --------------- | ----------- | ---------- | --- |
| Active          | :           | 20.1.1.2   |     |
| Standby         | :           | 20.1.1.3   |     |
| Node List       | Information | :          |     |
| Cluster         | Name        | : cluster2 |     |
| Cluster         | Alias Name  | :          |     |
| Node            | List :      |            |     |
----------------
20.1.1.2
188
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

20.1.1.3
20.1.1.4
| Bucket | Map Information | :           |     |              |
| ------ | --------------- | ----------- | --- | ------------ |
| Bucket | Map Active      | : [0...255] |     |              |
| Bucket | ID A-UAC        | S-UAC       |     | Connectivity |
----------------------------------------------------------
| 0   | 20.1.1.2 | 20.1.1.3 |     | L2  |
| --- | -------- | -------- | --- | --- |
| 1   | 20.1.1.3 | 20.1.1.4 |     | L2  |
| 2   | 20.1.1.4 | 20.1.1.2 |     | L2  |
...
ShowingSACandUACinformationforzone1:
| switch(config)# | show | ubt information | zone zone1 |     |
| --------------- | ---- | --------------- | ---------- | --- |
=====================================================================
Zone zone1:
=====================================================================
| SAC Information | :           |            |     |     |
| --------------- | ----------- | ---------- | --- | --- |
| Active          | :           | 10.1.1.2   |     |     |
| Standby         | :           | 10.1.1.3   |     |     |
| Node List       | Information | :          |     |     |
| Cluster         | Name        | : cluster1 |     |     |
| Cluster         | Alias Name  | :          |     |     |
| Node            | List :      |            |     |     |
----------------
10.1.1.2
10.1.1.3
10.1.1.4
| Bucket | Map Information | :           |     |              |
| ------ | --------------- | ----------- | --- | ------------ |
| Bucket | Map Active      | : [0...255] |     |              |
| Bucket | ID A-UAC        | S-UAC       |     | Connectivity |
----------------------------------------------------------
| 0   | 10.1.1.2 | 10.1.1.3 |     | L2  |
| --- | -------- | -------- | --- | --- |
| 1   | 10.1.1.3 | 10.1.1.4 |     | L2  |
| 2   | 10.1.1.4 | 10.1.1.2 |     | L2  |
...
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
DynamicSegmentation|189

| Platforms | Commandcontext |     |     | Authority                                            |     |     |     |
| --------- | -------------- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
| 6300      |                |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ubt       | state |             |        |            |     |     |     |
| -------------- | ----- | ----------- | ------ | ---------- | --- | --- | --- |
| show ubt state |       |             |        |            |     |     |     |
| show ubt state | zone  | <ZONE-NAME> |        |            |     |     |     |
| show ubt state | zone  | <ZONE-NAME> | uac-ip | <UAC-ADDR> |     |     |     |
Description
ShowstheglobalUBTstate.
SpecifyingazoneshowstheUBTstateofthatzone.
SpecifyingaUACIPaddressshowstheUBTstateofthatUAC.
| Parameter        |     |     |     | Description                                |     |     |     |
| ---------------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
| zone <ZONE-NAME> |     |     |     | SpecifiesUBTzonename.Maximumcharacters:64. |     |     |     |
uac-ip <UAC-ADDR> SpecifiestheIPaddressoftheuseranchorcontrollerforwhichto
viewuserinformation.SpecifytheaddressinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingtheUBTstatewherelocal-VLANmodehasbeenconfigured:
switch#
show ubt state
=====================================================================
| Zone zone1: |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
=====================================================================
| Local Conductor |     | Server (LCS) | State: |     |      |     |     |
| --------------- | --- | ------------ | ------ | --- | ---- | --- | --- |
| LCS Type        | IP  | Address      | State  |     | Role |     |     |
---------------------------------------------------------------------
| Primary | : 10.1.1.2 |     | ready_for_bootstrap |     | operational_primary |     |     |
| ------- | ---------- | --- | ------------------- | --- | ------------------- | --- | --- |
Secondary : 10.1.1.10 ready_for_bootstrap operational_secondary
| Switch Anchor | Controller |         | (SAC) | State:  |       |     |     |
| ------------- | ---------- | ------- | ----- | ------- | ----- | --- | --- |
|               | IP         | Address | MAC   | Address | State |     |     |
-----------------------------------------------------------------
| Active      | : 10.1.1.2       |      | 00:0b:86:b7:62:9f |     | registered |           |              |
| ----------- | ---------------- | ---- | ----------------- | --- | ---------- | --------- | ------------ |
| Standby     | : 10.1.1.3       |      | 00:0b:86:b7:64:0f |     | registered |           |              |
| User Anchor | Controller(UAC): |      | 10.1.1.2          |     |            |           |              |
| User        |                  | Port | State             |     |            | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:01 |                  | 1/1/1 | registered |     |     | 5         | 13 4094      |
| ----------------- | ---------------- | ----- | ---------- | --- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): |       | 10.1.1.3   |     |     |           |              |
| User              |                  | Port  | State      |     |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:02 |     | 1/1/2 | registered |     |     | 4   | 14 4094 |
| ----------------- | --- | ----- | ---------- | --- | --- | --- | ------- |
=====================================================================
| Zone zone2: |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
190
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

=====================================================================
| Local Conductor | Server     | (LCS) State: |      |     |     |
| --------------- | ---------- | ------------ | ---- | --- | --- |
| LCS Type        | IP Address | State        | Role |     |     |
---------------------------------------------------------------------
| Primary | : 20.1.1.2 | ready_for_bootstrap | operational_primary |     |     |
| ------- | ---------- | ------------------- | ------------------- | --- | --- |
Secondary : 20.1.1.10 ready_for_bootstrap operational_secondary
| Switch Anchor | Controller | (SAC) State: |       |     |     |
| ------------- | ---------- | ------------ | ----- | --- | --- |
|               | IP Address | MAC Address  | State |     |     |
-----------------------------------------------------------------
| Active      | : 20.1.1.2       | 00:0b:86:b7:62:9f | registered |           |              |
| ----------- | ---------------- | ----------------- | ---------- | --------- | ------------ |
| Standby     | : 20.1.1.3       | 00:0b:86:b7:64:0f | registered |           |              |
| User Anchor | Controller(UAC): | 20.1.1.2          |            |           |              |
| User        | Port             | State             |            | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:03 | 1/1/1            | registered |     | 5         | 13 4094      |
| ----------------- | ---------------- | ---------- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): | 20.1.1.3   |     |           |              |
| User              | Port             | State      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:04 | 1/1/2 | registered |     | 4   | 14 4094 |
| ----------------- | ----- | ---------- | --- | --- | ------- |
ShowingtheUBTstatewhereVLAN-extendmodehasbeenconfigured:
| switch# show | ubt state |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
=====================================================================
Zone zone1:
=====================================================================
| Local Conductor | Server     | (LCS) State: |      |     |     |
| --------------- | ---------- | ------------ | ---- | --- | --- |
| LCS Type        | IP Address | State        | Role |     |     |
---------------------------------------------------------------------
| Primary | : 10.1.1.2 | ready_for_bootstrap | operational_primary |     |     |
| ------- | ---------- | ------------------- | ------------------- | --- | --- |
Secondary : 10.1.1.10 ready_for_bootstrap operational_secondary
| Switch Anchor | Controller | (SAC) State: |       |     |     |
| ------------- | ---------- | ------------ | ----- | --- | --- |
|               | IP Address | MAC Address  | State |     |     |
-----------------------------------------------------------------
| Active      | : 10.1.1.2       | 00:0b:86:b7:62:9f | registered |           |              |
| ----------- | ---------------- | ----------------- | ---------- | --------- | ------------ |
| Standby     | : 10.1.1.3       | 00:0b:86:b7:64:0f | registered |           |              |
| User Anchor | Controller(UAC): | 10.1.1.2          |            |           |              |
| User        | Port             | State             |            | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:01 | 1/1/1            | registered |     | 5         | 13 10        |
| ----------------- | ---------------- | ---------- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): | 10.1.1.3   |     |           |              |
| User              | Port             | State      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:02 | 1/1/2 | registered |     | 4   | 14 20 |
| ----------------- | ----- | ---------- | --- | --- | ----- |
=====================================================================
Zone zone2:
=====================================================================
| Local Conductor | Server     | (LCS) State: |      |     |     |
| --------------- | ---------- | ------------ | ---- | --- | --- |
| LCS Type        | IP Address | State        | Role |     |     |
---------------------------------------------------------------------
| Primary | : 20.1.1.2 | ready_for_bootstrap | operational_primary |     |     |
| ------- | ---------- | ------------------- | ------------------- | --- | --- |
Secondary : 20.1.1.10 ready_for_bootstrap operational_secondary
| Switch Anchor | Controller | (SAC) State: |       |     |     |
| ------------- | ---------- | ------------ | ----- | --- | --- |
|               | IP Address | MAC Address  | State |     |     |
-----------------------------------------------------------------
| Active | : 20.1.1.2 | 00:0b:86:b7:62:9f | registered |     |     |
| ------ | ---------- | ----------------- | ---------- | --- | --- |
DynamicSegmentation|191

| Standby     | : 20.1.1.3       |      |     | 00:0b:86:b7:64:0f | registered |           |              |
| ----------- | ---------------- | ---- | --- | ----------------- | ---------- | --------- | ------------ |
| User Anchor | Controller(UAC): |      |     | 20.1.1.2          |            |           |              |
| User        |                  | Port |     | State             |            | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:03 |                  | 1/1/1 |     | registered |     | 5         | 13 30        |
| ----------------- | ---------------- | ----- | --- | ---------- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): |       |     | 20.1.1.3   |     |           |              |
| User              |                  | Port  |     | State      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:04 |     | 1/1/2 |     | registered |     | 4   | 14 40 |
| ----------------- | --- | ----- | --- | ---------- | --- | --- | ----- |
ShowingtheUBTstateofzone1:
| switch# show | ubt | state | zone | zone1 |     |     |     |
| ------------ | --- | ----- | ---- | ----- | --- | --- | --- |
=====================================================================
Zone zone1:
=====================================================================
| Local Conductor |     | Server  | (LCS) | State: |      |     |     |
| --------------- | --- | ------- | ----- | ------ | ---- | --- | --- |
| LCS Type        | IP  | Address |       | State  | Role |     |     |
---------------------------------------------------------------------
| Primary | : 10.1.1.2 |     |     | ready_for_bootstrap | operational_primary |     |     |
| ------- | ---------- | --- | --- | ------------------- | ------------------- | --- | --- |
Secondary : 10.1.1.10 ready_for_bootstrap operational_secondary
| Switch Anchor | Controller |         | (SAC) | State:      |       |     |     |
| ------------- | ---------- | ------- | ----- | ----------- | ----- | --- | --- |
|               | IP         | Address |       | MAC Address | State |     |     |
-----------------------------------------------------------------
| Active      | : 10.1.1.2       |      |     | 00:0b:86:b7:62:9f | registered |           |              |
| ----------- | ---------------- | ---- | --- | ----------------- | ---------- | --------- | ------------ |
| Standby     | : 10.1.1.3       |      |     | 00:0b:86:b7:64:0f | registered |           |              |
| User Anchor | Controller(UAC): |      |     | 10.1.1.2          |            |           |              |
| User        |                  | Port |     | State             |            | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:01 |                  | 1/1/1 |     | registered |     | 5         | 13 10        |
| ----------------- | ---------------- | ----- | --- | ---------- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): |       |     | 10.1.1.3   |     |           |              |
| User              |                  | Port  |     | State      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:02 |     | 1/1/2 |     | registered |     | 4   | 14 20 |
| ----------------- | --- | ----- | --- | ---------- | --- | --- | ----- |
ShowingtheUBTstateofaUACwithIPaddress15.212.219.57wherelocal-VLANmodehasbeen
configured:
| switch# show | ubt              | state | zone | zone1 uac-ip 15.212.219.57 |     |           |              |
| ------------ | ---------------- | ----- | ---- | -------------------------- | --- | --------- | ------------ |
| User Anchor  | Controller(UAC): |       |      | 15.212.219.57              |     |           |              |
| User         |                  | Port  |      | State                      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:04 |     | 1/1/20 |     | registered |     | 4   | 14 4000 |
| ----------------- | --- | ------ | --- | ---------- | --- | --- | ------- |
ShowingtheUBTstateofaUACwithIPaddress15.212.219.55whereVLAN-extendmodehasbeen
configured:
192
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| switch#     | show ubt         | state zone | zone1 uac-ip 15.212.219.55 |           |              |
| ----------- | ---------------- | ---------- | -------------------------- | --------- | ------------ |
| User Anchor | Controller(UAC): |            | 15.212.219.55              |           |              |
| User        |                  | Port       | State                      | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:07 |     | 1/1/10 | registered | 40  | 14 20 |
| ----------------- | --- | ------ | ---------- | --- | ----- |
| 00:00:00:00:00:08 |     | 1/1/12 | registered | 28  | 14 30 |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                | (#)        |                  | forthiscommand.   |     |     |
| ------------------- | ---------- | ---------------- | ----------------- | --- | --- |
| show ubt            | statistics |                  |                   |     |     |
| show ubt statistics |            |                  |                   |     |     |
| show ubt statistics |            | zone <ZONE-NAME> |                   |     |     |
| show ubt statistics |            | zone <ZONE-NAME> | uac-ip <UAC-ADDR> |     |     |
Description
DisplaysstatisticsforUBT.
SpecifyingazoneshowstheUBTstatisticsforthatzone.
SpecifyingaUACIPaddressshowstheUBTstatisticsforthatUAC.
| Parameter        |     |     | Description                                |     |     |
| ---------------- | --- | --- | ------------------------------------------ | --- | --- |
| zone <ZONE-NAME> |     |     | SpecifiesUBTzonename.Maximumcharacters:64. |     |     |
uac-ip <UAC-ADDR> SpecifiestheIPaddressoftheuseranchorcontrollerforwhichto
viewuserinformation.SpecifytheaddressinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
Examples
ShowingUBTstatisticswherelocal-VLANmodehasbeenconfigured:
| switch#        | show ubt | statistics |     |     |     |
| -------------- | -------- | ---------- | --- | --- | --- |
| UBT Statistics |          |            |     |     |     |
=====================================================================
| Zone zone1: |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
=====================================================================
| Control | Plane Statistics |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
| Active  | : 10.1.1.1       |     |     |     |     |
DynamicSegmentation|193

| Bootstrap   | Tx :       | 10  | Bootstrap   | Rx     | : 10 |
| ----------- | ---------- | --- | ----------- | ------ | ---- |
| Nodelist    | Rx :       | 25  | Nodelist    | Ack Rx | : 6  |
| Bucketmap   | Rx :       | 21  | Bucketmap   | Ack Rx | : 10 |
| Failover    | Tx :       | 4   | Failover    | Ack Rx | : 3  |
| Unbootstrap | Tx :       | 7   | Unbootstrap | Ack Rx | : 5  |
| Heartbeat   | Tx :       | 5   | Heartbeat   | Rx     | : 3  |
| Standby     | : 10.1.1.2 |     |             |        |      |
| Bootstrap   | Tx : 10    |     | Bootstrap   | Rx     | : 10 |
| Nodelist    | Rx : 25    |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap   | Rx : 21    |     | Bucketmap   | Ack Rx | : 12 |
| Failover    | Tx : 4     |     | Failover    | Ack Rx | : 3  |
| Unbootstrap | Tx : 5     |     | Unbootstrap | Ack Rx | : 3  |
| Heartbeat   | Tx : 7     |     | Heartbeat   | Rx     | : 4  |
UAC : 10.1.1.1
| Bootstrap   | Tx : 10 |     | Bootstrap   | Ack Rx | : 5 |
| ----------- | ------- | --- | ----------- | ------ | --- |
| Unbootstrap | Tx : 5  |     | Unbootstrap | Ack Rx | : 5 |
| Keepalive   | Tx : 2  |     | Keepalive   | Ack Rx | : 2 |
UAC : 10.1.1.2
| Bootstrap   | Tx : 5     |            | Bootstrap   | Ack Rx | : 5 |
| ----------- | ---------- | ---------- | ----------- | ------ | --- |
| Unbootstrap | Tx : 0     |            | Unbootstrap | Ack Rx | : 0 |
| Keepalive   | Tx : 0     |            | Keepalive   | Ack Rx | : 0 |
| Data Plane  | Statistics |            |             |        |     |
| UAC         | Packets Tx | Packets Rx |             |        |     |
---------------------------------
| 10.1.1.1 | 45678 | 23456 |     |     |     |
| -------- | ----- | ----- | --- | --- | --- |
| 10.1.1.2 | 34567 | 23457 |     |     |     |
User Statistics
| UAC | User Count |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
-----------------------
| 10.1.1.1 | 1   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
| 10.1.1.2 | 2   |     |     |     |     |
=====================================================================
Zone zone2:
=====================================================================
| Control Plane | Statistics |     |             |        |      |
| ------------- | ---------- | --- | ----------- | ------ | ---- |
| Active        | : 20.1.1.3 |     |             |        |      |
| Bootstrap     | Tx :       | 10  | Bootstrap   | Rx     | : 10 |
| Nodelist      | Rx :       | 25  | Nodelist    | Ack Rx | : 6  |
| Bucketmap     | Rx :       | 21  | Bucketmap   | Ack Rx | : 10 |
| Failover      | Tx :       | 4   | Failover    | Ack Rx | : 3  |
| Unbootstrap   | Tx :       | 7   | Unbootstrap | Ack Rx | : 5  |
| Heartbeat     | Tx :       | 5   | Heartbeat   | Rx     | : 3  |
| Standby       | : 20.1.1.4 |     |             |        |      |
| Bootstrap     | Tx : 10    |     | Bootstrap   | Rx     | : 10 |
| Nodelist      | Rx : 25    |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap     | Rx : 21    |     | Bucketmap   | Ack Rx | : 12 |
| Failover      | Tx : 4     |     | Failover    | Ack Rx | : 3  |
| Unbootstrap   | Tx : 5     |     | Unbootstrap | Ack Rx | : 3  |
| Heartbeat     | Tx : 7     |     | Heartbeat   | Rx     | : 4  |
UAC : 20.1.1.3
| Bootstrap   | Tx : 10 |     | Bootstrap   | Ack Rx | : 5 |
| ----------- | ------- | --- | ----------- | ------ | --- |
| Unbootstrap | Tx : 5  |     | Unbootstrap | Ack Rx | : 5 |
| Keepalive   | Tx : 2  |     | Keepalive   | Ack Rx | : 2 |
UAC : 20.1.1.4
| Bootstrap   | Tx : 5 |     | Bootstrap   | Ack Rx | : 5 |
| ----------- | ------ | --- | ----------- | ------ | --- |
| Unbootstrap | Tx : 0 |     | Unbootstrap | Ack Rx | : 0 |
| Keepalive   | Tx : 0 |     | Keepalive   | Ack Rx | : 0 |
194
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Data Plane | Statistics |     |         |     |     |     |
| ---------- | ---------- | --- | ------- | --- | --- | --- |
| UAC        | Packets    | Tx  | Packets | Rx  |     |     |
---------------------------------
| 20.1.1.3 | 45670 |     | 33456 |     |     |     |
| -------- | ----- | --- | ----- | --- | --- | --- |
| 20.1.1.4 | 34561 |     | 33457 |     |     |     |
User Statistics
| UAC | User | Count |     |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- |
-----------------------
| 20.1.1.3 | 1   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| 20.1.1.4 | 2   |     |     |     |     |     |
ShowingUBTstatisticswhereVLAN-extendmodehasbeenconfigured:
| switch# show | ubt | statistics |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- |
UBT Statistics
=====================================================================
Zone zone1:
=====================================================================
| Control Plane | Statistics |        |     |             |        |      |
| ------------- | ---------- | ------ | --- | ----------- | ------ | ---- |
| Active        | : 10.1.1.3 |        |     |             |        |      |
| Bootstrap     | Tx         | : 10   |     | Bootstrap   | Rx     | : 10 |
| Nodelist      | Rx         | : 25   |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap     | Rx         | : 21   |     | Bucketmap   | Ack Rx | : 10 |
| Failover      | Tx         | : 4    |     | Failover    | Ack Rx | : 3  |
| Unbootstrap   |            | Tx : 7 |     | Unbootstrap | Ack Rx | : 5  |
| Heartbeat     | Tx         | : 5    |     | Heartbeat   | Rx     | : 3  |
| Standby       | : 10.1.1.4 |        |     |             |        |      |
| Bootstrap     | Tx         | : 10   |     | Bootstrap   | Rx     | : 10 |
| Nodelist      | Rx         | : 25   |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap     | Rx         | : 21   |     | Bucketmap   | Ack Rx | : 12 |
| Failover      | Tx         | : 4    |     | Failover    | Ack Rx | : 3  |
| Unbootstrap   |            | Tx : 5 |     | Unbootstrap | Ack Rx | : 3  |
| Heartbeat     | Tx         | : 7    |     | Heartbeat   | Rx     | : 4  |
UAC : 10.1.1.3
| Bootstrap   | Tx  | : 10   |     | Bootstrap   | Ack Rx | : 5 |
| ----------- | --- | ------ | --- | ----------- | ------ | --- |
| Unbootstrap |     | Tx : 5 |     | Unbootstrap | Ack Rx | : 5 |
| Keepalive   | Tx  | : 2    |     | Keepalive   | Ack Rx | : 2 |
UAC : 10.1.1.4
| Bootstrap   | Tx         | : 5    |         | Bootstrap   | Ack Rx | : 5 |
| ----------- | ---------- | ------ | ------- | ----------- | ------ | --- |
| Unbootstrap |            | Tx : 0 |         | Unbootstrap | Ack Rx | : 0 |
| Keepalive   | Tx         | : 0    |         | Keepalive   | Ack Rx | : 0 |
| Data Plane  | Statistics |        |         |             |        |     |
| SAC tunnel  | Rx         |        |         | : 444       |        |     |
| Standby-SAC | tunnel     | Rx     |         | : 0         |        |     |
| UAC         | Packets    | Tx     | Packets | Rx          |        |     |
---------------------------------
| 10.1.1.3 | 45678 |     | 23456 |     |     |     |
| -------- | ----- | --- | ----- | --- | --- | --- |
| 10.1.1.4 | 34567 |     | 23457 |     |     |     |
User Statistics
| UAC | User | Count |     |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- |
-----------------------
| 10.1.1.3 | 1   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| 10.1.1.4 | 2   |     |     |     |     |     |
=====================================================================
Zone zone2:
=====================================================================
DynamicSegmentation|195

| Control Plane  | Statistics |        |            |             |        |      |
| -------------- | ---------- | ------ | ---------- | ----------- | ------ | ---- |
| Active         | : 20.1.1.3 |        |            |             |        |      |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx         | : 25   |            | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |            | Bucketmap   | Ack Rx | : 10 |
| Failover       | Tx         | : 4    |            | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 7 |            | Unbootstrap | Ack Rx | : 5  |
| Heartbeat      | Tx         | : 5    |            | Heartbeat   | Rx     | : 3  |
| Standby        | : 20.1.1.4 |        |            |             |        |      |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx         | : 25   |            | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |            | Bucketmap   | Ack Rx | : 12 |
| Failover       | Tx         | : 4    |            | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 5 |            | Unbootstrap | Ack Rx | : 3  |
| Heartbeat      | Tx         | : 7    |            | Heartbeat   | Rx     | : 4  |
| UAC : 20.1.1.3 |            |        |            |             |        |      |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 5 |            | Unbootstrap | Ack Rx | : 5  |
| Keepalive      | Tx         | : 2    |            | Keepalive   | Ack Rx | : 2  |
| UAC : 20.1.1.4 |            |        |            |             |        |      |
| Bootstrap      | Tx         | : 5    |            | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 0 |            | Unbootstrap | Ack Rx | : 0  |
| Keepalive      | Tx         | : 0    |            | Keepalive   | Ack Rx | : 0  |
| Data Plane     | Statistics |        |            |             |        |      |
| SAC tunnel     | Rx         |        | :          | 222         |        |      |
| Standby-SAC    | tunnel     | Rx     | :          | 0           |        |      |
| UAC            | Packets    | Tx     | Packets Rx |             |        |      |
---------------------------------
| 20.1.1.3 | 45678 |     | 23456 |     |     |     |
| -------- | ----- | --- | ----- | --- | --- | --- |
| 20.1.1.4 | 34567 |     | 23457 |     |     |     |
User Statistics
| UAC | User | Count |     |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- |
-----------------------
| 20.1.1.3 | 1   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| 20.1.1.4 | 2   |     |     |     |     |     |
ShowingUBTstatisticsforzone1wherelocal-vlanmodehasbeenconfigured:
| switch# show | ubt | statistics | zone zone1 |     |     |     |
| ------------ | --- | ---------- | ---------- | --- | --- | --- |
UBT Statistics
Zone zone1:
| Control Plane | Statistics |        |     |             |        |      |
| ------------- | ---------- | ------ | --- | ----------- | ------ | ---- |
| Active        | : 10.1.1.3 |        |     |             |        |      |
| Bootstrap     | Tx         | : 10   |     | Bootstrap   | Rx     | : 10 |
| Nodelist      | Rx         | : 25   |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap     | Rx         | : 21   |     | Bucketmap   | Ack Rx | : 10 |
| Failover      | Tx         | : 4    |     | Failover    | Ack Rx | : 3  |
| Unbootstrap   |            | Tx : 7 |     | Unbootstrap | Ack Rx | : 5  |
| Heartbeat     | Tx         | : 5    |     | Heartbeat   | Rx     | : 3  |
| Standby       | : 10.1.1.4 |        |     |             |        |      |
| Bootstrap     | Tx         | : 10   |     | Bootstrap   | Rx     | : 10 |
| Nodelist      | Rx         | : 25   |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap     | Rx         | : 21   |     | Bucketmap   | Ack Rx | : 12 |
| Failover      | Tx         | : 4    |     | Failover    | Ack Rx | : 3  |
196
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Unbootstrap    |            | Tx : 5 |            | Unbootstrap | Ack Rx | : 3 |
| -------------- | ---------- | ------ | ---------- | ----------- | ------ | --- |
| Heartbeat      | Tx         | : 7    |            | Heartbeat   | Rx     | : 4 |
| UAC : 10.1.1.3 |            |        |            |             |        |     |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Ack Rx | : 5 |
| Unbootstrap    |            | Tx : 5 |            | Unbootstrap | Ack Rx | : 5 |
| Keepalive      | Tx         | : 2    |            | Keepalive   | Ack Rx | : 2 |
| UAC : 10.1.1.4 |            |        |            |             |        |     |
| Bootstrap      | Tx         | : 5    |            | Bootstrap   | Ack Rx | : 5 |
| Unbootstrap    |            | Tx : 0 |            | Unbootstrap | Ack Rx | : 0 |
| Keepalive      | Tx         | : 0    |            | Keepalive   | Ack Rx | : 0 |
| Data Plane     | Statistics |        |            |             |        |     |
| UAC            | Packets    | Tx     | Packets Rx |             |        |     |
---------------------------------
| 10.1.1.3 | 45678 |     | 23456 |     |     |     |
| -------- | ----- | --- | ----- | --- | --- | --- |
| 10.1.1.4 | 34567 |     | 23457 |     |     |     |
User Statistics
| UAC | User | Count |     |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- |
-----------------------
| 10.1.1.3 | 1   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| 10.1.1.4 | 2   |     |     |     |     |     |
ShowingUBTstatisticsforzone1whereVLAN-extendmodehasbeenconfigured:
| switch# show | ubt | statistics | zone zone1 |     |     |     |
| ------------ | --- | ---------- | ---------- | --- | --- | --- |
UBT Statistics
Zone zone1:
| Control Plane  | Statistics |        |     |             |        |      |
| -------------- | ---------- | ------ | --- | ----------- | ------ | ---- |
| Active         | : 10.1.1.3 |        |     |             |        |      |
| Bootstrap      | Tx         | : 10   |     | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx         | : 25   |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |     | Bucketmap   | Ack Rx | : 10 |
| Failover       | Tx         | : 4    |     | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 7 |     | Unbootstrap | Ack Rx | : 5  |
| Heartbeat      | Tx         | : 5    |     | Heartbeat   | Rx     | : 3  |
| Standby        | : 10.1.1.4 |        |     |             |        |      |
| Bootstrap      | Tx         | : 10   |     | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx         | : 25   |     | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |     | Bucketmap   | Ack Rx | : 12 |
| Failover       | Tx         | : 4    |     | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 5 |     | Unbootstrap | Ack Rx | : 3  |
| Heartbeat      | Tx         | : 7    |     | Heartbeat   | Rx     | : 4  |
| UAC : 10.1.1.3 |            |        |     |             |        |      |
| Bootstrap      | Tx         | : 10   |     | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 5 |     | Unbootstrap | Ack Rx | : 5  |
| Keepalive      | Tx         | : 2    |     | Keepalive   | Ack Rx | : 2  |
| UAC : 10.1.1.4 |            |        |     |             |        |      |
| Bootstrap      | Tx         | : 5    |     | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 0 |     | Unbootstrap | Ack Rx | : 0  |
| Keepalive      | Tx         | : 0    |     | Keepalive   | Ack Rx | : 0  |
DynamicSegmentation|197

| Data Plane  | Statistics |     |         |     |     |
| ----------- | ---------- | --- | ------- | --- | --- |
| SAC tunnel  | Rx         |     |         | :   | 444 |
| Standby-SAC | tunnel     | Rx  |         | :   | 0   |
| UAC         | Packets    | Tx  | Packets | Rx  |     |
---------------------------------
| 10.1.1.3 | 45678 |     | 23456 |     |     |
| -------- | ----- | --- | ----- | --- | --- |
| 10.1.1.4 | 34567 |     | 23457 |     |     |
User Statistics
| UAC | User | Count |     |     |     |
| --- | ---- | ----- | --- | --- | --- |
-----------------------
| 10.1.1.3 | 1   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
| 10.1.1.4 | 2   |     |     |     |     |
ShowingtheUBTstatisticsofaUACwithIPaddress101.101.101.11:
| switch#     | show ubt   | statistics | zone | zone1 | uac-ip 101.101.101.11 |
| ----------- | ---------- | ---------- | ---- | ----- | --------------------- |
| Data Plane  | Statistics |            |      |       |                       |
| SAC tunnel  | Rx         |            |      | :     | 6457                  |
| Standby-SAC | tunnel     | Rx         |      | :     | 0                     |
| UAC         |            | Packets    | Tx   |       | Packets Rx            |
------------------------------------------------
| 101.101.101.11 |     | : 145379605 |     |     | 145450113 |
| -------------- | --- | ----------- | --- | --- | --------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ubt | users |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
show ubt users [ all | count | down | mac <MAC-ADDR> | {port <IF-NAME> | <IF-RANGE>} | up]
zone <ZONE-NAME>
Description
DisplaysuserinformationforUBT.
198
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| Parameter      |     |     | Description                                            |     |     |
| -------------- | --- | --- | ------------------------------------------------------ | --- | --- |
| all            |     |     | Displayinformationforallusers.                         |     |     |
| count          |     |     | Displaythetotalnumberofusersconfiguredtotunneltraffic. |     |     |
| down           |     |     | Displaytheusersthatarenotabletotunneltraffic.          |     |     |
| mac <MAC-ADDR> |     |     | DisplayuserinformationbasedonMACaddress.               |     |     |
port <IF-NAME> | <IF-RANGE> Displayuserinformationforaspecificinterfaceorrangeof
|                  |     |     | interfaces.Forexample,port                 | 1/1/1orport | 1/1/1-1/1/10. |
| ---------------- | --- | --- | ------------------------------------------ | ----------- | ------------- |
| up               |     |     | Displayuserinformationthatareactive.       |             |               |
| zone <ZONE-NAME> |     |     | SpecifiesUBTzonename.Maximumcharacters:64. |             |               |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallusers:
| switch# | show ubt users | all |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
=====================================================================
| Displaying | All UBT | Users for Zone: | zone1 |     |     |
| ---------- | ------- | --------------- | ----- | --- | --- |
=====================================================================
| Downloaded | user roles | are preceded | by * |     |     |
| ---------- | ---------- | ------------ | ---- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 1/25 | 00:00:00:11:12:03 | activated | authenticated | ---/--- |     |
| ---- | ----------------- | --------- | ------------- | ------- | --- |
=====================================================================
| Displaying | All UBT | Users for Zone: | zone2 |     |     |
| ---------- | ------- | --------------- | ----- | --- | --- |
=====================================================================
| Downloaded | user roles | are preceded | by * |     |     |
| ---------- | ---------- | ------------ | ---- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 2/25 | 00:00:00:13:12:03 | activated | authenticated | ---/--- |     |
| ---- | ----------------- | --------- | ------------- | ------- | --- |
Showinginformationforusersofzone1:
| switch# | show ubt users | all zone | zone1 |     |     |
| ------- | -------------- | -------- | ----- | --- | --- |
=====================================================================
| Displaying | All UBT | Users for Zone: | zone1 |     |     |
| ---------- | ------- | --------------- | ----- | --- | --- |
=====================================================================
| Downloaded | user roles | are preceded | by * |     |     |
| ---------- | ---------- | ------------ | ---- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 1/25 | 00:00:00:11:12:03 | activated | authenticated | ---/--- |     |
| ---- | ----------------- | --------- | ------------- | ------- | --- |
Displayingthenumberofusersthataretunnelingtraffic:
| switch#      | show ubt users | count     |                   |     |     |
| ------------ | -------------- | --------- | ----------------- | --- | --- |
| Total Number | of Users       | using ubt | Zone : zone2 is 1 |     |     |
DynamicSegmentation|199

| Total Number | of Users | using | ubt | Zone | : zone1 is | 2   |     |
| ------------ | -------- | ----- | --- | ---- | ---------- | --- | --- |
===================================================
| Total Number | of Users | in  | all the | zones | : 3 |     |     |
| ------------ | -------- | --- | ------- | ----- | --- | --- | --- |
===================================================
Showingusersthataredown:
| switch# | show ubt users |     | down |     |     |     |     |
| ------- | -------------- | --- | ---- | --- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of  | Zone: | zone1 | having Tunnel | Status DOWN |     |
| ---------- | --------- | --- | ----- | ----- | ------------- | ----------- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by  | *   |     |     |
| ---------- | ---------- | --- | -------- | --- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
----------------------------------------------------------------------------------
1/25 00:00:00:11:12:03 activation_failed authenticated User bootstrap has
failed
Showinginformationforusersofzone1thataredown:
| switch# | show ubt users |     | down zone | zone1 |     |     |     |
| ------- | -------------- | --- | --------- | ----- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of  | Zone: | zone1 | having Tunnel | Status DOWN |     |
| ---------- | --------- | --- | ----- | ----- | ------------- | ----------- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by  | *   |     |     |
| ---------- | ---------- | --- | -------- | --- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
1/25 00:00:00:11:12:03 activation_failed authenticated User bootstrap has
failed
Showinginformationforusersonport2/25:
| switch# | show ubt users |     | port 2/25 |     |     |     |     |
| ------- | -------------- | --- | --------- | --- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of  | Zone: | zone1 |     |     |     |
| ---------- | --------- | --- | ----- | ----- | --- | --- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by  | *   |     |     |
| ---------- | ---------- | --- | -------- | --- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 2/25 | 00:00:00:11:12:03 |     | activated |     | authenticated |     | ---/--- |
| ---- | ----------------- | --- | --------- | --- | ------------- | --- | ------- |
Showinginformationforusersthatareup:
| switch# | show ubt users |     | up  |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of  | Zone: | zone1 | having Tunnel | Status UP |     |
| ---------- | --------- | --- | ----- | ----- | ------------- | --------- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by  | *   |     |     |
| ---------- | ---------- | --- | -------- | --- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 1/25 | 00:00:00:11:12:03 |     | activated |     | authenticated |     | ---/--- |
| ---- | ----------------- | --- | --------- | --- | ------------- | --- | ------- |
200
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

Showinginformationforusersofzone1thatareup:
| switch# | show ubt users | up zone | zone1 |     |     |
| ------- | -------------- | ------- | ----- | --- | --- |
=====================================================================
| Displaying | UBT Users | of Zone: zone1 | having Tunnel | Status UP |     |
| ---------- | --------- | -------------- | ------------- | --------- | --- |
=====================================================================
| Downloaded | user roles | are preceded | by * |     |     |
| ---------- | ---------- | ------------ | ---- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 1/25 | 00:00:00:11:12:03 | activated | authenticated |     | ---/--- |
| ---- | ----------------- | --------- | ------------- | --- | ------- |
ShowinginformationfortheuserwithMACaddress00:00:00:11:12:03:
| switch# | show ubt users | mac 00:00:00:11:12:03 |     |     |     |
| ------- | -------------- | --------------------- | --- | --- | --- |
Displaying UBT User of Zone: zone1 having MAC-Address: 00:00:00:11:12:03
| Downloaded | user roles | are preceded | by * |     |     |
| ---------- | ---------- | ------------ | ---- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 1/25 | 00:00:00:11:12:03 | activated | authenticated |     | ---/--- |
| ---- | ----------------- | --------- | ------------- | --- | ------- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 6400 | (#) |     |     |     |     |
| ---- | --- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
uac-keepalive-interval
| uac-keepalive-interval    |     | <TIME> |     |     |     |
| ------------------------- | --- | ------ | --- | --- | --- |
| no uac-keepalive-interval |     | <TIME> |     |     |     |
Description
SpecifiestheUACkeepaliverefreshtimeintervalinsecondsfortheUBT zone.
Thenoformofthiscommandsetsthekeepaliveintervaltothedefaultvalue.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<TIME>
SpecifiestheUACkeep-aliverefreshtimeintervalinseconds.
Range:1to60.Default:60.
Examples
Specifyingakeepaliveintervalof60secondsforUBTzone1:
DynamicSegmentation|201

| switch(config)# |     | ubt zone | zone1 |     |     |     |
| --------------- | --- | -------- | ----- | --- | --- | --- |
switch(config-ubt-zone1)#
|     |     |     | uac-keepalive-interval |     |     | 60  |
| --- | --- | --- | ---------------------- | --- | --- | --- |
DeletingtheconfiguredUACkeepaliveinterval:
| switch(config)#           |     | ubt zone | zone1 |                        |     |     |
| ------------------------- | --- | -------- | ----- | ---------------------- | --- | --- |
| switch(config-ubt-zone1)# |     |          | no    | uac-keepalive-interval |     | 60  |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
config-ubt-<ZONE-NAME>
| 6300 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- |
| 6400 |     |     |     |     | rightsforthiscommand.                              |     |
ubt
| ubt zone    | <ZONE-NAME> | vrf <VRF-NAME> |            |     |     |     |
| ----------- | ----------- | -------------- | ---------- | --- | --- | --- |
| no ubt zone | <ZONE-NAME> | vrf            | <VRF-NAME> |     |     |     |
Description
CreatesaUserBasedTunnel(UBT)zonewithaspecifiedzonenameandVRFname.AUBTnameisusedto
configureallUBTpropertiesadvertisedbytheUBTfeature.
ThenoformofthiscommandremovesthespecifiedUBTzone.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<ZONE-NAME>
SpecifiesanamefortheUBTzone.Length:1to64characters.
| <VRF-NAME> |     |     |     |     | SpecifiestheVRFonwhichtoestablishtheUBTtunnel. |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
Examples
CreatingUBTzonecalledzone1associatedwithaVRFcalleddefault:
| switch(config)# |     | ubt zone | zone1 | vrf | default |     |
| --------------- | --- | -------- | ----- | --- | ------- | --- |
RemovingUBTzonezone1onVRFdefault:
| switch(config)# |     | no ubt | zone | zone1 vrf | default |     |
| --------------- | --- | ------ | ---- | --------- | ------- | --- |
DeletingallUBTconfigurations:
202
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

| switch(config)# | no ubt |     |     |
| --------------- | ------ | --- | --- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
6400 forthiscommand.
ubt-client-vlan
| ubt-client-vlan    | <VLAN-ID> |     |     |
| ------------------ | --------- | --- | --- |
| no ubt-client-vlan | <VLAN-ID> |     |     |
Description
SpecifiestheUBTClientVLANorlocalVLAN.ThisVLANisusedinlocal-VLANmodeonly.IftheUBTclient
VLANisconfiguredinVLAN-extendmodeitisignored,thisisthereservedVLANthatallclienttrafficusesto
gettothegateway.Atthegateway,VLAN andpolicywillbeassignedtotheclienttraffic.Nootherfeature
shouldbeenabledontheUBTclientVLAN.
ThenoformofthiscommandremovestheVLANtousefortunneledclients.
Parameter Description
<VLAN-ID> SpecifiestheVLANIDtousefortunneledclients.Range:1-4094.
Examples
CreatingVLAN4000:
| switch(config)#           | vlan 4000 |             |     |
| ------------------------- | --------- | ----------- | --- |
| switch(config-vlan-4000)# |           | no shutdown |     |
SpecifyingUBTclientVLAN4000:
| switch(config)# | ubt-client-vlan | 4000 |     |
| --------------- | --------------- | ---- | --- |
Settingmulti-zone:
| switch(config)#           | ubt-client-vlan | 4000               |                |
| ------------------------- | --------------- | ------------------ | -------------- |
| switch(config)#           | ubt zone        | zone8 vrf default  |                |
| switch(config-ubt-zone8)# |                 | primary-controller | ip 20.20.20.13 |
| switch(config-ubt-zone8)# |                 | enable             |                |
| switch(config)#           | ubt zone        | zone5 vrf default  |                |
DynamicSegmentation|203

| switch(config-ubt-zone5)# |     | primary-controller |     | ip 20.20.20.10 |
| ------------------------- | --- | ------------------ | --- | -------------- |
switch(config-ubt-zone5)#
enable
| switch(config)#           | ubt | zone zone3         | vrf default |                 |
| ------------------------- | --- | ------------------ | ----------- | --------------- |
| switch(config-ubt-zone3)# |     | primary-controller |             | ip 10.10.10.248 |
| switch(config-ubt-zone3)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone2         | vrf default |                 |
| switch(config-ubt-zone2)# |     | primary-controller |             | ip 162.10.0.6   |
| switch(config-ubt-zone2)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone7         | vrf default |                 |
| switch(config-ubt-zone7)# |     | primary-controller |             | ip 20.20.20.12  |
| switch(config-ubt-zone7)# |     | enable             |             |                 |
switch(config)#
|                           | ubt | zone zone4         | vrf default |                 |
| ------------------------- | --- | ------------------ | ----------- | --------------- |
| switch(config-ubt-zone4)# |     | primary-controller |             | ip 10.10.10.251 |
| switch(config-ubt-zone4)# |     | enable             |             |                 |
| ip source-interface       |     | ubt interface      | loopback200 |                 |
RemovingconfiguredUBTclientVLAN4000:
| switch(config)# | no  | ubt-client-vlan | 4000 |     |
| --------------- | --- | --------------- | ---- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400     |             |     | forthiscommand. |     |
| -------- | ----------- | --- | --------------- | --- |
| ubt mode | vlan-extend |     |                 |     |
ubt-mode vlan-extend
| no ubt-mode | [vlan-extend] |     |     |     |
| ----------- | ------------- | --- | --- | --- |
Description
SelectsVLANextendedmode.WhenVLAN-extendmodeisenabledclientsareassignedtotheirUBTrole-
basedVLANinthehardwaredatapath.
Thenoformofthecommandselectsthedefaultlocal-VLANmode.Inlocal-VLANmodeclientsareassigned
toalocalswitchVLANandassociatedwiththeirUBTrole-basedVLANwhenclienttrafficreachesthe
controller.
ThedefaultUBTmodeislocal-VLAN.
Examples
SettingtheUBTmodetoVLAN-extend:
| switch(config)# | ubt-mode | vlan-extend |     |     |
| --------------- | -------- | ----------- | --- | --- |
Settingmulti-zone:
204
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| switch(config)# | ubt-mode | vlan-extend |     |     |
| --------------- | -------- | ----------- | --- | --- |
switch(config)#
|                           | ubt | zone zone8         | vrf default |                 |
| ------------------------- | --- | ------------------ | ----------- | --------------- |
| switch(config-ubt-zone8)# |     | primary-controller |             | ip 20.20.20.13  |
| switch(config-ubt-zone8)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone5         | vrf default |                 |
| switch(config-ubt-zone5)# |     | primary-controller |             | ip 20.20.20.10  |
| switch(config-ubt-zone5)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone3         | vrf default |                 |
| switch(config-ubt-zone3)# |     | primary-controller |             | ip 10.10.10.248 |
| switch(config-ubt-zone3)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone2         | vrf default |                 |
switch(config-ubt-zone2)#
|                           |     | primary-controller |             | ip 162.10.0.6   |
| ------------------------- | --- | ------------------ | ----------- | --------------- |
| switch(config-ubt-zone2)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone7         | vrf default |                 |
| switch(config-ubt-zone7)# |     | primary-controller |             | ip 20.20.20.12  |
| switch(config-ubt-zone7)# |     | enable             |             |                 |
| switch(config)#           | ubt | zone zone4         | vrf default |                 |
| switch(config-ubt-zone4)# |     | primary-controller |             | ip 10.10.10.251 |
| switch(config-ubt-zone4)# |     | enable             |             |                 |
| ip source-interface       |     | ubt interface      | loopback200 |                 |
SettingtheUBTmodebacktothedefaultoflocal-VLAN:
| switch(config)# | no  | ubt-mode |     |     |
| --------------- | --- | -------- | --- | --- |
CommandHistory
| Release        |     |     | Modification            |     |
| -------------- | --- | --- | ----------------------- | --- |
| 10.09          |     |     | Addedmulti-zonesupport. |     |
| 10.07orearlier |     |     | --                      |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
DynamicSegmentation|205

Chapter 12

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing and modifying information about
managed devices on IP networks.

Configuring SNMP
(The SNMP agent provides read-only access.)

Procedure

1. Enable SNMP on a VRF using the command snmp-server vrf.

2. Set the system contact, location, and description for the switch with the following commands:

n snmp-server system-contact

n snmp-server system-location

n snmp-server system-description

3.

If required, change the default SNMP port on which the agent listens for requests with the command
snmp-server agent-port.

4. By default, the agent uses the community string public to protect access through SNMPv1/v2c. Set a

new community string with the command snmp-server community.

5. Configure the trap receivers to which the SNMP agent will send trap notifications with the command

snmp-server host.

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

n Enables SNMP on the out-of-band management interface (VRF mgmt).

n Sets the contact, location, and description for the switch to: JaniceM, Building2, LabSwitch.

n Sets the community string to Lab8899X.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

206

| switch(config)# | snmp-server | vrf mgmt |     |
| --------------- | ----------- | -------- | --- |
switch(config)#
|                 | snmp-server | system-contact     | JaniceM   |
| --------------- | ----------- | ------------------ | --------- |
| switch(config)# | snmp-server | system-location    | Building2 |
| switch(config)# | snmp-server | system-description | LabSwitch |
| switch(config)# | snmp-server | community          | Lab8899X  |
Example 2
Thisexamplecreatesthefollowingconfiguration:
n CreatesanSNMPv3usernamedAdminusingshaauthenticationwiththeplaintextpassword
mypasswordandusingdessecuritywiththeplaintextpasswordmyprivpass.
n AssociatestheSNMPv3userAdminwithacontextnamednewContext.
switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
| priv-pass       | plaintext | myprivpass         |            |
| --------------- | --------- | ------------------ | ---------- |
| switch(config)# | snmpv3    | user Admin context | newContext |
RefertotheSNMP GuideforSNMP Commands.
SNMP|207

Chapter 13

Aruba Central integration

Aruba Central integration

The Aruba Central network management solution, a software-as-a-service subscription in the cloud, provides
streamlined management of multiple network devices. AOS-CX switches are able to talk to Aruba Central and
utilize cloud-based management functionality. Cloud-based management functionality allows for the
deployment of network devices at sites with no or few dedicated IT personnel (branch offices, retail stores,
and so forth). AOS-CX switches utilize secure communication protocols to connect to the Aruba Central
cloud portal, and can coexist with corporate security standards, such as those mandating the use of
firewalls.

When Aruba Central manages AOS-CX switches, it functions as the single source of truth and the Web UI operates

in read-only mode.

This feature provides:

n Zero-touch provisioning

n Network Management/Remote monitoring

n Events/alerts notification

n Switch Configuration using templates

n Firmware management

Connecting to Aruba Central
AOS-CX switch downloads the location of Aruba Central server using:

n Command-line interface (CLI).

n Aruba Activate server.

n DHCP options provided during ZTP.

DHCP servers are used to connect to Central on-premise management.

If switch is unable to connect to Activate server, it retries to establish connection in exponential back off of
1s, 2s, 8s, 16s, 32s, 64s, 128s, and 256s. After the maximum back off of 256s, switch retries happen for
every 5 minutes.

If the Network Time Protocol (NTP) is not enabled on the switch, it will synchronize the system time with the

Activate server.

Custom CA certificate
To use custom CA certificate to connect to Aruba Central, AOS-CX switch downloads the certificate from
Aruba Activate server.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

208

n If there is no custom CA provided by Aruba Activate, the CA certificate present in the device is used.

n Duplicate CA certificates from Aruba Activate server will be ignored.

n If CA certificate is absent in consecutive responses from Aruba Activate server, the installed custom CA

certificate in device will be removed.

n Switch will have only one custom CA certificate installed from Aruba Activate Server.

n The certificate installed from Aruba Activate server will not be displayed in the show commands.

Support mode in Aruba Central
When the AOS-CX switch is managed by Aruba Central, the switch configuration cannot be modified using
other interfaces such as CLI or Web UI. The following command categories are blocked:

n auto-confirm

n boot

n checkpoint

n copy-in commands

n erase

n erps

n https-server

n mfgread

n mfgwrite

n port-access

n vsf

n All configuration commands except the aruba-central command

In cases where a maintenance or troubleshooting activity requires configuration updates, aruba-central
support-mode can be enabled to allow these operations.

The aruba-central support-mode enable or disable operation is effective only in the CLI session where it is

executed and does not impact the other CLI sessions.

If the user tries to execute any command that is not allowed, an Invalid input: error message is displayed.

Aruba Central commands

aruba-central
aruba-central
no aruba-central

Description

Creates or enters the Aruba Central configuration context (config-aruba-central).

Example

Administrators or local user group members with execution rights for this command.

Creating the Aruba Central configuration context:

Aruba Central integration | 209

| switch(config)# | aruba-central |     |     |
| --------------- | ------------- | --- | --- |
switch(config-aruba-central)#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
| aruba-central    | support-mode |     |     |
| ---------------- | ------------ | --- | --- |
| aruba-central    | support-mode |     |     |
| no aruba-central | support-mode |     |     |
Description
Allowsthedevicetobewritableforalloperationsin ArubaCentrallockoutmodefortroubleshooting.The
noformofthiscommanddisablesthisactivity.
Support-modeisdisabledbydefaultwhentheswitchismanagedbyArubaCentral.Thiscommandisonly
effectiveintheCLI sessionwhereitisexecuted.
Examples
ConfiguringthedevicetobewritableforalloperationsinArubaCentrallockoutmode:
| switch# | aruba-central | support-mode |     |
| ------- | ------------- | ------------ | --- |
switch#
RemovingtheconfigurationthatallowsthedevicetobewritableforalloperationsinArubaCentrallockout
mode:
| switch# | no aruba-central | support-mode |     |
| ------- | ---------------- | ------------ | --- |
switch#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
210
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400                     |     |         |         | forthiscommand. |     |     |
| ------------------------ | --- | ------- | ------- | --------------- | --- | --- |
| configuration-lockout    |     |         | central | managed         |     |     |
| configuration-lockout    |     | central | managed |                 |     |     |
| no configuration-lockout |     | central | managed |                 |     |     |
Description
ConfiguresthedevicetoonlybewritablefromArubaCentral.ArubaCentralwillbetheonlyagentthatcan
add,modify,ordeleteconfigurationsonthedevice.Thenoformofthiscommanddisablesthisfeature.
ThenoformofthiscommandisonlyavailablewhenthedeviceisdisconnectedfromArubaCentral.
Usage
TheAOS-CXswitchconnectstoArubaCentralineitheroftwomodes:monitorormanaged.Whenthedevice
isconnectedinmonitormode,ArubaCentralmonitorstheconfigurationsontheswitch.Whenthedeviceis
connectedinmanagedmode,theconfiguration-lockout central managedcommanddoesnotallow
configurationchangesfromotherinterfacessuchasCLIorWebUI.
Examples
ConfiguringthedevicetoonlybewritablefromArubaCentral:
| switch(config)# |                            | configuration-lockout |     |     | central managed |     |
| --------------- | -------------------------- | --------------------- | --- | --- | --------------- | --- |
| switch#         | show configuration-lockout |                       |     |     |                 |     |
| configuration   | lockout                    |                       |     |     |                 |     |
---------------------
| central:        | managed           |           |        |                               |                |          |
| --------------- | ----------------- | --------- | ------ | ----------------------------- | -------------- | -------- |
| switch#         | sh aruba-central  |           |        |                               |                |          |
| Central         | admin state       |           |        | :enable                       |                |          |
| Central         | location          |           |        | :20.0.0.2:8083                |                |          |
| VRF for         | connection        |           |        | :default                      |                |          |
| Central         | connection        | status    |        | :connected                    |                |          |
| Central         | source            |           |        | :cli                          |                |          |
| Central         | source connection |           | status | :connected                    |                |          |
| Central         | source last       | connected | on     | :Tue                          | Feb 9 17:53:13 | UTC 2021 |
| Activate        | Server            | URL       |        | :devices-v2.arubanetworks.com |                |          |
| CLI location    |                   |           |        | :20.0.2:8083                  |                |          |
| CLI VRF         |                   |           |        | :default                      |                |          |
| switch(config)# |                   | end       |        |                               |                |          |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
ArubaCentralintegration|211

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |
| ---- | --- | --------------- |
disable
disable
Description
DisablesconnectiontoArubaCentralserver.
Whentheconnectionisdisabled,theswitchdoesnotattempttoconnecttotheArubaCentralserveror
fetchcentrallocationfromanyofthethreesources(CLI/ArubaActivate/DHCP).Italsodisconnectsany
activeconnectiontotheArubaCentralserver.
Example
| switch(config-aruba-central)# | disable |     |
| ----------------------------- | ------- | --- |
switch(config-aruba-central)#
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 config-aruba-central Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |
| ---- | --- | --------------- |
enable
enable
Description
EnablesconnectiontoArubaCentralserver.Whentheconnectionisenabled,theswitchattemptsto
downloadthelocationoftheArubaCentralserverinoneofthefollowingwaysatstartupandafterthe
connectionislost:
n Usingcommand-lineinterface(CLI).
ConnectingtoArubaActivateserver.
n
UsingDHCPoptionsprovidedduringZTP.
n
DHCPserversprovidetheoptionsrequestedbythedevicetoconnecttoCentral,CentralOn-premise
managment,ortheTFTPserver.
Examples
212
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

switch(config-aruba-central)# enable
switch(config-aruba-central)#

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6300
6400

config-aruba-central

Administrators or local user group members with execution rights
for this command.

location-override
location-override <location> [vrf <VRF-NAME>]
no location-override

Description

When location and vrf are configured, the switch overrides existing connections to Aruba Central. The
switch attempts to establish connection to Aruba Central with the specified location and VRF with highest
priority.

The no form of this command removes location override values from the Aruba Central configuration
context.

Parameter

<location>

vrf <VRF-NAME>

Description

Specifies one of these values:
n <FQDN>: a fully qualified domain name.
n <IPV4>: an IPv4 address.
n <IPV6>: an IPv6 address.

Specifies the VRF name to be used for communicating with the
server. If no VRF name is provided, the default VRF named
default is used.

Examples

Configuring location override with location and VRF:

switch(config-aruba-central)# location-override aruba-central.com vrf default
switch(config-aruba-central)#

Configuring location override with location only:

switch(config-aruba-central)# location-override aruba-central.com
switch(config-aruba-central)#

Aruba Central integration | 213

RemovinglocationoverridevaluesfromtheArubaCentralconfigurationcontext:
| switch(config-aruba-central)# |     |     |     | no location-override |     |
| ----------------------------- | --- | --- | --- | -------------------- | --- |
switch(config-aruba-central)#
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 config-aruba-central Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
show aruba-central
show aruba-central
Description
ShowsinformationaboutArubaCentralconnectionandthestatusoftheActivateserverconnection.
Examples
ExampleofaswitchthathastheArubaCentralconnection:
| switch#              | show aruba-central |           |        |          |                      |
| -------------------- | ------------------ | --------- | ------ | -------- | -------------------- |
| Central              | admin state        |           |        |          | :enabled             |
| Central              | location           |           |        |          | : N/A                |
| VRF for              | connection         |           |        |          | : N/A                |
| Central              | connection         | status    |        |          | : N/A                |
| Central              | source             |           |        |          | : dhcp               |
| Central              | source connection  |           | status |          | : connection_failure |
| Central              | source last        | connected |        | on       | : N/A                |
| System time          | synchronized       |           | from   | Activate | : True               |
| Activate             | server             | URL       |        |          | : 172.17.0.1         |
| CLI location         |                    |           |        |          | : N/A                |
| CLI VRF              |                    |           |        |          | : N/A                |
| Source IP            |                    |           |        |          | : N/A                |
| Source IP Overridden |                    |           |        |          | : false              |
| Central              | support            | mode      |        |          | : disabled           |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
214
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| Platforms | Commandcontext | Authority                                            |
| --------- | -------------- | ---------------------------------------------------- |
| 6300      |                | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show running-config current-context
| show running-config | current-context |     |
| ------------------- | --------------- | --- |
Description
Showstherunningconfigurationforthecurrent-context.IfuserisinthecontextofAruba-Central(config-
aruba-central),thenArubaCentralrunningconfigurationisdisplayed.
Examples
ShowstherunningconfigurationofArubaCentral:
switch(config-aruba-central)# show running-config current-context
aruba-central
disable
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
ArubaCentralintegration|215

Chapter 14

Port filtering

Port filtering

Port filtering is a feature in which packets that are ingressed through a source port can be blocked for
egressing on a specific set of ports.

Figure 5 Port Filter Application

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

<INTERFACE-LIST>

Usage

Description

Specifies a list of ports/LAGs to be blocked for egressing. Specify a
single interface or LAG, or a range as a comma-separated list, or
both. For example: 1/1/1, 1/1/3-1/1/6,lag2, lag1-lag4.

On the 6400 Switch Series, interface identification differs.

When a port filter configuration is applied on the same ingress physical port/LAG, the configuration is
updated with the new sets of egress ports/LAGs that are to be blocked for egressing and that are not a part
of its previous configuration. Duplicate updates on an existing port filter configuration are ignored.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

216

Whenegressports/LAGsareremovedfromtheexistingportfilterconfigurationofaningressport/LAG,
egressingisallowedagainonthoseegressports/LAGsforallpacketsoriginatingfromtheingressport/LAG.
Theno portfilter [<IF-NAME-LIST>]commandremovesportfilterconfigurationsfromtheegress
ports/LAGslistedinthe<IF-NAME-LIST>parameteronly.Allotheregressports/LAGsintheportfilter
configurationoftheingressport/LAGremainintact.
IfnophysicalportsorLAGsareprovidedfortheno portfiltercommand,thecommandremovesthe
entireportfilterconfigurationfortheingressport/LAG.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Creatingafilterthatpreventspacketsreceivedonport1/1/1fromforwardingtoports1/1/3-1/1/6andto
LAGs1through4:
| switch(config)#    |     | interface  | 1/1/1 |                       |
| ------------------ | --- | ---------- | ----- | --------------------- |
| switch(config-if)# |     | portfilter |       | 1/1/3-1/1/6,lag1-lag4 |
CreatingafilterthatpreventspacketsreceivedonLAG1fromforwardingtoports1/1/6andLAGs2and4:
| switch(config)#        |     | interface | lag        | 1               |
| ---------------------- | --- | --------- | ---------- | --------------- |
| switch(config-lag-if)# |     |           | portfilter | 1/1/6,lag2,lag4 |
Removingfiltersfromanexistingconfigurationthatallowsbackpacketsreceivedonport1/1/1toforward
toports1/1/6andLAGs3and4:
| switch(config)#    |     | interface     | 1/1/1 |                 |
| ------------------ | --- | ------------- | ----- | --------------- |
| switch(config-if)# |     | no portfilter |       | 1/1/6,lag3,lag4 |
RemovingallfiltersfromanexistingconfigurationthatallowsbackpacketsreceivedonLAG1toforwardto
alltheportsandLAGs:
| switch(config)#        |     | interface | lag           | 1   |
| ---------------------- | --- | --------- | ------------- | --- |
| switch(config-lag-if)# |     |           | no portfilter |     |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     |     | forthiscommand. |
| --- | ------------- | --- | --- | --------------- |
show portfilter
| show portfilter | [<IFNAME>][vsx-peer] |     |     |     |
| --------------- | -------------------- | --- | --- | --- |
Portfiltering|217

Description
Displaysfiltersettingsforallinterfacesoraspecificinterface.
Parameter Description
<IFNAME> Specifiestheingressinterfacename.
Specifiesoneofthesevalues:
n <FQDN>:afullyqualifieddomainname.
<IPV4>:anIPv4address.
n
n <IPV6>:anIPv6address.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
| lag2 | 1/1/1,1/1/3-1/1/6 |     |
| ---- | ----------------- | --- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
218
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Portfiltering|219

Chapter 15

DNS

DNS

The Domain Name System (DNS) is the Internet protocol for mapping a hostname to its IP address. DNS
allows users to enter more readily memorable and intuitive hostnames, rather than IP addresses, to identify
devices connected to a network. It also allows a host to keep the same hostname even if it changes its IP
address.

Hostname resolution can be either static or dynamic.

n In static resolution, a local table is defined on the switch that associates hostnames with their IP
addresses. Static tables can be used to speed up the resolution of frequently queried hosts.

n Dynamic resolution requires that the switch query a DNS server located elsewhere on the network.

Dynamic name resolution takes more time than static name resolution, but requires far less configuration
and management.

DNS client
The DNS client resolves hostnames to IP addresses for protocols that are running on the switch. When the
DNS client receives a request to resolve a hostname, it can do so in one of two ways:

n Forward the request to a DNS name server for resolution.

n Reply to the request without using a DNS name server, by resolving the name using a statically defined

table of hostnames and their associated IP addresses.

Configuring the DNS client

Procedure

1. Configure one or more DNS name servers with the command ip dns server.

2. To resolve DNS requests by appending a domain name to the requests, either configure a single

domain name with the command ip dns domain-name, or configure a list of up to six domain names
with the command ip dns domain-list.

3. To use static name resolution for certain hosts, associate an IP address to a host with the command

ip dns host.

4. Review your DNS configuration settings with the command show ip dns.

Examples

This example creates the following configuration:

n Defines the domain switch.com to append to all requests.

n Defines a DNS server with IPv4 address of 1.1.1.1.

n Defines a static DNS host named myhost1 with an IPv4 address of 3.3.3.3.

n DNS client traffic is sent on the default VRF (named default).

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

220

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
n DefinesthreedomainstoappendtoDNSrequestsdomain1.com,domain2.com,domain3.comwith
trafficforwardingonVRFmainvrf.
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
DNS|221

Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     | ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | ------ | ----------- | --- | ----------- | --- |
| switch(config)# |     | ip dns | domain-list |     | domain2.com |     |
Thisexampledefinesalistwithtwoentries,domain2.comanddomain5.com,withrequestsbeingsenton
mainvrf.
| switch(config)# |     | ip dns | domain-list |     | domain2.com | vrf mainvrf |
| --------------- | --- | ------ | ----------- | --- | ----------- | ----------- |
| switch(config)# |     | ip dns | domain-list |     | domain5.com | vrf mainvrf |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |     | no ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | --------- | ----------- | --- | ----------- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | domain-name |               |     |       |            |     |
| --------- | ----------- | ------------- | --- | ----- | ---------- | --- |
| ip dns    | domain-name | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | domain-name | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.By
default,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip dns
domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
222
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     | ip  | dns | domain-name | domain.com |     |
| --------------- | --- | --- | --- | ----------- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |     | no  | ip dns | domain-name | domain.com |     |
| --------------- | --- | --- | ------ | ----------- | ---------- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | host |             |           |           |                  |     |
| --------- | ---- | ----------- | --------- | --------- | ---------------- | --- |
| ip dns    | host | <HOST-NAME> | <IP-ADDR> |           | [ vrf <VRF-NAME> | ]   |
| no ip dns | host | <HOST-NAME> |           | <IP-ADDR> | [ vrf <VRF-NAME> | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadofqueryinga
DNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFisdefined,the
defaultVRFisused.
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
DNS|223

Examples
| ThisexampledefinesanIPv4addressof |     |     |     |     | 3.3.3.3forhost1. |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
switch(config)#
|                                          |     |     | ip dns    | host | host1 | 3.3.3.3           |     |
| ---------------------------------------- | --- | --- | --------- | ---- | ----- | ----------------- | --- |
| ThisexampledefinesanIPv6addressofb::5    |     |     |           |      |       | forhost           | 1.  |
| switch(config)#                          |     |     | ip dns    | host | host1 | b::5              |     |
| Thisexampledefinesremovestheentryforhost |     |     |           |      |       | 1withaddressb::5. |     |
| switch(config)#                          |     |     | no ip dns | host | host1 | b::5              |     |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | server         | address |           |     |       |            |     |
| --------- | -------------- | ------- | --------- | --- | ----- | ---------- | --- |
| ip dns    | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
224
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |

| switch(config)# | ip dns | server-address | 1.1.1.1 |
| --------------- | ------ | -------------- | ------- |
Thisexampledefinesanameserverata::1.
| switch(config)# | ip dns | server-address | a::1 |
| --------------- | ------ | -------------- | ---- |
Thisexampleremovesanameserverata::1.
| switch(config)# | no ip dns | server-address | a::1 |
| --------------- | --------- | -------------- | ---- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip dns |                            |     |     |
| ----------- | -------------------------- | --- | --- |
| show ip dns | [vrf <VRF-NAME>][vsx-peer] |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow ip dns
command.
| switch(config)# | ip dns | domain-name    | domain.com  |
| --------------- | ------ | -------------- | ----------- |
| switch(config)# | ip dns | domain-list    | domain5.com |
| switch(config)# | ip dns | domain-list    | domain8.com |
| switch(config)# | ip dns | server-address | 4.4.4.4     |
| switch(config)# | ip dns | server-address | 6.6.6.6     |
DNS|225

| switch(config)# |     | ip dns | host | host3 | 5.5.5.5 |     |     |
| --------------- | --- | ------ | ---- | ----- | ------- | --- | --- |
switch(config)#
|                 |     | ip dns | host           | host2 | 2.2.2.2        |     |         |
| --------------- | --- | ------ | -------------- | ----- | -------------- | --- | ------- |
| switch(config)# |     | ip dns | host           | host3 | c::12          |     |         |
| switch(config)# |     | ip dns | domain-name    |       | reddomain.com  |     | vrf red |
| switch(config)# |     | ip dns | domain-list    |       | reddomain5.com |     | vrf red |
| switch(config)# |     | ip dns | domain-list    |       | reddomain8.com |     | vrf red |
| switch(config)# |     | ip dns | server-address |       | 4.4.4.5        |     | vrf red |
| switch(config)# |     | ip dns | server-address |       | 6.6.6.7        |     | vrf red |
| switch(config)# |     | ip dns | host           | host3 | 5.5.5.6        | vrf | red     |
| switch(config)# |     | ip dns | host           | host2 | 2.2.2.3        | vrf | red     |
| switch(config)# |     | ip dns | host           | host3 | c::13          | vrf | red     |
switch#
show ip dns
| VRF Name       | : default |                |         |             |     |     |     |
| -------------- | --------- | -------------- | ------- | ----------- | --- | --- | --- |
| Domain Name    | :         | domain.com     |         |             |     |     |     |
| DNS Domain     | list      | : domain5.com, |         | domain8.com |     |     |     |
| Name Server(s) |           | : 4.4.4.4,     | 6.6.6.6 |             |     |     |     |
| Host Name      |           | Address        |         |             |     |     |     |
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
| host2           |     | 2.2.2.3   |                |       |             |     |         |
| --------------- | --- | --------- | -------------- | ----- | ----------- | --- | ------- |
| host3           |     | 5.5.5.6   |                |       |             |     |         |
| host3           |     | c::13     |                |       |             |     |         |
| switch(config)# |     | ip dns    | domain-name    |       | domain.com  |     | vrf red |
| switch(config)# |     | ip dns    | domain-list    |       | domain5.com |     | vrf red |
| switch(config)# |     | ip dns    | domain-list    |       | domain8.com |     | vrf red |
| switch(config)# |     | ip dns    | server-address |       | 4.4.4.4     |     | vrf red |
| switch(config)# |     | ip dns    | server-address |       | 6.6.6.6     |     | vrf red |
| switch(config)# |     | ip dns    | host           | host3 | 5.5.5.5     | vrf | red     |
| switch(config)# |     | no ip dns | host           | host2 | 2.2.2.2     |     | vrf red |
| switch(config)# |     | ip dns    | host           | host3 | c::12       | vrf | red     |
switch#
|                | show  | ip dns vrf     | red     |             |     |     |     |
| -------------- | ----- | -------------- | ------- | ----------- | --- | --- | --- |
| VRF Name       | : red |                |         |             |     |     |     |
| Domain Name    | :     | domain.com     |         |             |     |     |     |
| DNS Domain     | list  | : domain5.com, |         | domain8.com |     |     |     |
| Name Server(s) |       | : 4.4.4.4,     | 6.6.6.6 |             |     |     |     |
| Host Name      |       | Address        |         |             |     |     |     |
-------------------------------
| host3 |     | 5.5.5.5 |     |     |     |     |     |
| ----- | --- | ------- | --- | --- | --- | --- | --- |
| host3 |     | c::12   |     |     |     |     |     |
CommandHistory
226
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|227

Device discovery and configuration

Chapter 16

Device discovery and configuration

The switch provides support for LLDP, CDP, and local MAC match by using device profiles to enable
automatic discovery and configuration of other devices on the network.

Based on the type of devices connected to the interface, device profiles enable predefined configurations
that can be applied to the interface. Connected devices are identified using corresponding protocol packets.
When the protocol information on the interface ages, the profile or role is revoked from the interface. Only
devices connected directly to the switch are detected and processed to apply a device profile. When a device
of a configured type is connected to an interface, the switch automatically applies the corresponding Device
profiles .

Local MAC match enables dynamic assignment of client attributes, such QoS and VLANs by using a locally
configured authentication repository. Local MAC match involves creating MAC groups that are used to
classify connected devices based on MAC address, MAC address mask, and MAC OUI. Local MAC match
feature is useful when you do not want to afford RADIUS infrastructure or when you want to use local
authentication as a backup method in case the RADIUS server is unreachable.

The following parameters can be configured for each role:

n associate: Used to associate captive-portal-profile or policy with the role.

n auth-mode: Used to configure authentication mode for the role.

There is no need to configure auth-mode for a plain device profile.

n mtu: Used to configure MTU for the role.

n poe-priority: Used to configure the PoE priority for the role.

n trust-mode: Used to configure trust mode for the role.

n vlan: Used to configure VLAN mode for the role.

n stp-admin-edge-port: Used to configure STP administrative edge port for the role.

For information on role configurations, see the Security Guide.

The following commands are not supported in local MAC match feature:

n aaa authentication port-access mac-auth cached-reauth

n aaa authentication port-access mac-auth cached-reauth-period

n aaa authentication port-access mac-auth quiet-period

n aaa authentication port-access mac-auth reauth-period

Extra line to keep the above line from following the figure onto the next page.

Example configuration of device deployment
The switch provides simplified deployment of devices, such as access points, IP phones, security cameras,
and printers, through the use of a locally configured repository that provides authentication and dynamic
port assignment, such as QoS, PoE, and tagged VLANs.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

228

Device profiles

Device profiles rely on role configurations. For information on role configurations, see the Security Guide.

Device profiles are used to dynamically assign port attributes based on the type of devices connected,
without having to create a RADIUS infrastructure. You can map device profiles to device groups. A device
group contains various match criteria, which can be obtained from multiple sources, such as LLDP, CDP, and
local MAC match. Device profiles contain port attributes to be assigned to the port when a connected device
matches a device group.

Device profiles are supported on different scenarios. It can be applied on interfaces that are configured with
security (802.1X or MAC authentication), or applied based on L2 port (LLDP, CDP), or applied on standalone
ports with the block-until-profile-applied command enabled. All the methods are mutually exclusive of each
other. The block-until-profile-applied mode must be configured only when there is a standalone port where
no security has been configured and when you want the port to be offline until at least one client is
onboarded based on the match and ignore criteria that you configure. Local MAC match is supported when
you configure block-until-profile-applied command or device profile with security.

Up to 16 device profiles can be configured on the 6400.

See the Security Guide for the following commands:

Device discovery and configuration | 229

n The port-access onboarding-method precedence command—If you are configuring both security and
device profile on the port, and you want to configure the order in which the methods will be executed.

n The port-access fallback-role command—If you want to configure a role that must be applied to

devices when no other role exists or can be derived for that device.

If you configure a match criteria that matches across multiple device profiles, then the priority considered is
LLDP, CDP, and then local MAC match. That is, LLDP precedes over CDP, which in turn precedes over local
MAC match.

The following figure displays a simple configuration of device profile and AAA authentication with RADIUS
server and Aruba ClearPass Policy Manager. Local MAC match feature is useful when you do not want to
afford RADIUS infrastructure or when you want to use local authentication as a backup method in case the
RADIUS server is unreachable.

Figure 6 Example of device profile setup along with RADIUS infrastructure

;" />

Configuring a device profile for LLDP

Procedure

1. Create an LLDP group with the command port-access lldp-group.

2. Define rules for adding devices to an LLDP group with the command match.

3. Define rules for ignoring devices so that they are not added to an LLDP group with the command

ignore.

4. Create a device profile with the command port-access device-profile.

5. Add the LLDP group with the command associate lldp-group.

6. Add a role to a device profile with the command associate role. Make sure that the role is already
created. For information on how to create a role, see port access role information in the Security
Guide.

7. Enable the device profile with the command enable.

Configuring a device profile for CDP

1. Create a CDP group with the command port-access cdp-group.

2. Define rules for adding devices to a CDP group with the command match.

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

230

3. DefinerulesforignoringdevicessothattheyarenotaddedtoaCDPgroupwiththecommand
ignore.
4. Createadeviceprofilewiththecommandport-access device-profile.
5. AddaCDPgrouptoadeviceprofilewiththecommandassociate cdp-group.
6. Addaroletoadeviceprofilewiththecommandassociate role.Makesurethattheroleisalready
created.Forinformationonhowtocreatearole,seeportaccessroleinformationintheSecurity
Guide.
7. Enableadeviceprofilewiththecommandenable.
| Configuring |     | a device |     | profile | for local | MAC match |
| ----------- | --- | -------- | --- | ------- | --------- | --------- |
Procedure
1. CreateaMACgroupwiththemac-groupcommand.
2. DefinerulesforaddingdevicestoaMACgroupwiththematch groups)command.
(for MAC
3. DefinerulesforignoringdevicessothattheyarenotaddedtoaMACgroupwiththeignore (for
| MAC | groups)command. |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- |
4. Createadeviceprofilewiththeport-access device-profilecommand.
5. AssociateaMACgroupwithadeviceprofilewiththeassociate mac-groupcommand.
6. Addaroletoadeviceprofilewiththeassociate rolecommand.Makesurethattheroleisalready
created.Forinformationonhowtocreatearole,seeportaccessroleinformationintheSecurity
Guide.
7. Enableadeviceprofilewiththeenablecommand.
| Device             | profile        |     | commands                  |                |     |     |
| ------------------ | -------------- | --- | ------------------------- | -------------- | --- | --- |
| aaa authentication |                |     | port-accessallow-cdp-bpdu |                |     |     |
| aaa authentication |                |     | port-access               | allow-cdp-bpdu |     |     |
| no aaa             | authentication |     | port-access               | allow-cdp-bpdu |     |     |
Description
AllowsallpacketsrelatedtotheCDP(CiscoDiscoveryProtocol)BPDU(BridgeProtocolDataUnit)ona
secureport.
ThenoformofthiscommandblockstheCDPBPDUonasecureport.Onanonsecureport,thecommand
hasnoeffect.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AllowingaCDPBPDUonsecureport1/1/1:
| switch(config)#    |                |     | interface | 1/1/1          |             |                |
| ------------------ | -------------- | --- | --------- | -------------- | ----------- | -------------- |
| switch(config-if)# |                |     | aaa       | authentication | port-access | allow-cdp-bpdu |
| switch(config-if)# |                |     | do show   | running-config |             |                |
| Current            | configuration: |     |           |                |             |                |
!
| !Version |         | AOS-CX | 10.0X.0000 |     |     |     |
| -------- | ------- | ------ | ---------- | --- | --- | --- |
| led      | locator | on     |            |     |     |     |
!
!
Devicediscoveryandconfiguration|231

vlan 1
aaa authentication port-access mac-auth

enable

aaa authentication port-access dot1x authenticator

enable
interface 1/1/1
no shutdown
vlan access 1
aaa authentication port-access allow-cdp-bpdu
aaa authentication port-access mac-auth

enable

aaa authentication port-access dot1x authenticator
enable

switch(config-if)# do show port-access device-profile interface all
Port 1/1/1, Neighbor-Mac 00:0c:29:9e:d1:20

Profile Name
LLDP Group
CDP Group
Role
Status
Failure Reason :

: access_switches
:
: aruba-ap_cdp
: test_ap_role
: In Progress

Blocking LLDP packet on secure port 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no aaa authentication port-access allow-cdp-bpdu
switch(config-if)# do show running-config
Current configuration:
!
!Version AOS-CX 10.0X.0000
led locator on
!
!
vlan 1
aaa authentication port-access mac-auth

enable
interface 1/1/1
no shutdown
vlan access 1
aaa authentication port-access mac-auth

enable

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6300
6400

config-if

Administrators or local user group members with execution rights
for this command.

aaa authentication port-access allow-cdp-proxy-logoff

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

232

| aaa    | authentication |     | port-access | allow-cdp-proxy-logoff |                        |     |     |     |
| ------ | -------------- | --- | ----------- | ---------------------- | ---------------------- | --- | --- | --- |
| no aaa | authentication |     | port-access |                        | allow-cdp-proxy-logoff |     |     |     |
Description
AllowsaclienttobeloggedofffromthesystemviaaspecialTLVintheCDPpacket.Bydefault,proxylogoff
viaCDPpacketsupportisdisabled.Whenallow-cdp-proxy-logoffisenabled,TLVreceivedfromCDP
packetscorrespondingtologoffprocessingwillbereadandlogoffisissuedtotheclients.Thisonlyworkson
clientauthenticationenabledportsandaaa authentication port-access allow-cdp-bpdumustbe
enabledtoprocess.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AllowingaclienttobeloggedofffromthesystemviaaspecialTLVintheCDP packet:
| switch(config)# |     |     | interface | 1/1/1 |     |     |     |     |
| --------------- | --- | --- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)# aaa authentication port-access allow-cdp-proxy-logoff
| switch(config-if)# |     |       | show | running-config |     | interface | 1/1/1 |     |
| ------------------ | --- | ----- | ---- | -------------- | --- | --------- | ----- | --- |
| interface          |     | 1/1/1 |      |                |     |           |       |     |
no shutdown
|     | vlan | access         | 1   |             |                        |               |     |     |
| --- | ---- | -------------- | --- | ----------- | ---------------------- | ------------- | --- | --- |
|     | aaa  | authentication |     | port-access | allow-cdp-bpdu         |               |     |     |
|     | aaa  | authentication |     | port-access | allow-cdp-proxy-logoff |               |     |     |
|     | aaa  | authentication |     | port-access | allow                  | client-limit  |     | 2   |
|     | aaa  | authentication |     | port-access | dot1x                  | authenticator |     |     |
enable
|     | aaa | authentication |     | port-accss | mac-auth |     |     |     |
| --- | --- | -------------- | --- | ---------- | -------- | --- | --- | --- |
enable
exit
CommandHistory
| Release    |     |     |     |     | Modification       |     |     |     |
| ---------- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
| 10.09.1000 |     |     |     |     | Commandintroduced. |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400   |                |     |                            |                 | forthiscommand. |     |     |     |
| ------ | -------------- | --- | -------------------------- | --------------- | --------------- | --- | --- | --- |
| aaa    | authentication |     | port-accessallow-lldp-bpdu |                 |                 |     |     |     |
| aaa    | authentication |     | port-access                | allow-lldp-bpdu |                 |     |     |     |
| no aaa | authentication |     | port-access                |                 | allow-lldp-bpdu |     |     |     |
Description
AllowsallpacketsrelatedtotheLLDPBPDU(BridgeProtocolDataUnit)onasecureport.
ThenoformofthiscommandblockstheLLDPBPDUonasecureport.Onanonsecureport,thecommand
hasnoeffect.
Examples
Devicediscoveryandconfiguration|233

Onthe6400SwitchSeries,interfaceidentificationdiffers.
AllowinganLLDPBPDUonsecureport1/1/1:
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# aaa authentication port-access allow-lldp-bpdu
| switch(config-if)#     |     | do  | show | running-config |     |
| ---------------------- | --- | --- | ---- | -------------- | --- |
| Current configuration: |     |     |      |                |     |
!
| !Version    | AOS-CX | 10.0X.0000 |     |     |     |
| ----------- | ------ | ---------- | --- | --- | --- |
| led locator | on     |            |     |     |     |
!
!
vlan 1
| aaa authentication |     | port-access |     | mac-auth |     |
| ------------------ | --- | ----------- | --- | -------- | --- |
enable
| interface | 1/1/1 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
| vlan access        | 1   |     |             |     |                 |
| ------------------ | --- | --- | ----------- | --- | --------------- |
| aaa authentication |     |     | port-access |     | allow-lldp-bpdu |
| aaa authentication |     |     | port-access |     | mac-auth        |
enable
switch(config-if)# do show port-access device-profile interface all
| Port 1/1/1, | Neighbor-Mac |     | 00:0c:29:9e:d1:20 |         |     |
| ----------- | ------------ | --- | ----------------- | ------- | --- |
| Profile     | Name         | :   | access_switches   |         |     |
| LLDP        | Group        | :   | 2920-grp          |         |     |
| CDP Group   |              | :   |                   |         |     |
| Role        |              | :   | local_2920_role   |         |     |
| Status      |              | :   | Profile           | Applied |     |
| Failure     | Reason       | :   |                   |         |     |
BlockingLLDPBPDUonsecureport1/1/1:
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# no aaa authentication port-access allow-lldp-bpdu
| switch(config-if)#     |     | do  | show | running-config |     |
| ---------------------- | --- | --- | ---- | -------------- | --- |
| Current configuration: |     |     |      |                |     |
!
| !Version | AOS-CX | 10.0X.0000led |     | locator | on  |
| -------- | ------ | ------------- | --- | ------- | --- |
!
!
vlan 1
| aaa authentication |     | port-access |     | mac-auth |     |
| ------------------ | --- | ----------- | --- | -------- | --- |
enable
| interface | 1/1/1 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
| vlan               | access | 1   |             |     |          |
| ------------------ | ------ | --- | ----------- | --- | -------- |
| aaa authentication |        |     | port-access |     | mac-auth |
enable
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
234
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400         |           |           |              |     | forthiscommand. |     |     |
| ------------ | --------- | --------- | ------------ | --- | --------------- | --- | --- |
| associate    | cdp-group |           |              |     |                 |     |     |
| associate    | cdp-group |           | <GROUP-NAME> |     |                 |     |     |
| no associate |           | cdp-group | <GROUP-NAME> |     |                 |     |     |
Description
AssociatesaCDP(CiscoDiscoveryProtocol)groupwithadeviceprofile.AmaximumoftwoCDPgroupscan
beassociatedwithadeviceprofile.
ThenoformofthiscommandremovesaCDPgroupfromadeviceprofile.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME> SpecifiesthenameoftheCDPgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheCDPgroupmy-cdp-groupwiththedeviceprofileprofile01:
| switch(config)#                |     |     | port-access | device-profile |           | profile01 |              |
| ------------------------------ | --- | --- | ----------- | -------------- | --------- | --------- | ------------ |
| switch(config-device-profile)# |     |     |             |                | associate | cdp-group | my-cdp-group |
RemovingtheCDPgroupmy-cdp-groupfromthedeviceprofileprofile01:
| switch(config)# |     |     | port-access | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | -------------- | --- | --------- | --- |
switch(config-device-profile)# no associate cdp-group my-cdp-group
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
6300 config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6400         |            |            |              |     | forthiscommand. |     |     |
| ------------ | ---------- | ---------- | ------------ | --- | --------------- | --- | --- |
| associate    | lldp-group |            |              |     |                 |     |     |
| associate    | lldp-group |            | <GROUP-NAME> |     |                 |     |     |
| no associate |            | lldp-group | <GROUP-NAME> |     |                 |     |     |
Description
Devicediscoveryandconfiguration|235

AssociatesanLLDPgroupwithadeviceprofile.AmaximumoftwoLLDPgroupscanbeassociatedwitha
deviceprofile
ThenoformofthiscommandremovesanLLDPgroupfromadeviceprofile.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME> SpecifiesthenameoftheLLDPgrouptoassociatewiththedevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheLLDPgroupmy-lldp-groupwiththedeviceprofileprofile01:
| switch(config)# |     | port-access | device-profile |     | profile01 |     |
| --------------- | --- | ----------- | -------------- | --- | --------- | --- |
switch(config-device-profile)#
|     |     |     | associate |     | lldp-group | my-lldp-group |
| --- | --- | --- | --------- | --- | ---------- | ------------- |
RemovingtheLLDPgroupmy-lldp-groupfromthedeviceprofileprofile01:
| switch(config)# |     | port-access | device-profile |     | profile01 |     |
| --------------- | --- | ----------- | -------------- | --- | --------- | --- |
switch(config-device-profile)# no associate lldp-group my-lldp-group
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
config-device-profile
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400         |           |              |     | forthiscommand. |     |     |
| ------------ | --------- | ------------ | --- | --------------- | --- | --- |
| associate    | mac-group |              |     |                 |     |     |
| associate    | mac-group | <GROUP-NAME> |     |                 |     |     |
| no associate | mac-group | <GROUP-NAME> |     |                 |     |     |
Description
AssociatesaMACgroupwithadeviceprofile.AmaximumoftwoMACgroupscanbeassociatedwitha
deviceprofile.
ThenoformofthiscommandremovesaMACgroupfromadeviceprofile.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME>
SpecifiesthenameoftheMACgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheMACgroupmac01-groupwiththedeviceprofileprofile01:
236
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

| switch(config)# | port-access | device-profile | profile01 |     |
| --------------- | ----------- | -------------- | --------- | --- |
switch(config-device-profile)#
|     |     | associate | mac-group | mac01-group |
| --- | --- | --------- | --------- | ----------- |
RemovingtheMACgroupmac01-groupfromthedeviceprofileprofile01:
| switch(config)# | port-access | device-profile | profile01 |     |
| --------------- | ----------- | -------------- | --------- | --- |
switch(config-device-profile)# no associate mac-group mac01-group
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
config-device-profile
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400           |                  | forthiscommand. |     |     |
| -------------- | ---------------- | --------------- | --- | --- |
| associate role |                  |                 |     |     |
| associate role | <ROLE-NAME>      |                 |     |     |
| no associate   | role <ROLE-NAME> |                 |     |     |
Description
Associatesarolewithadeviceprofile.Onlyonerolecanbeassociatedwithadeviceprofile.Forinformation
onhowtoconfigurearole,seetheportaccessroleinformationintheSecurityGuide.
Thenoformofthiscommandremovesarolefromadeviceprofile.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<ROLE-NAME>
Specifiesthenameoftheroletoassociatewiththedeviceprofile.
Range:1to64alphanumericcharacters.
Examples
Associatingtherolemy-rolewiththedeviceprofileprofile01:
| switch(config)#                | port-access | device-profile | profile01    |     |
| ------------------------------ | ----------- | -------------- | ------------ | --- |
| switch(config-device-profile)# |             | associate      | role my-role |     |
Removingtherolemy-rolefromthedeviceprofileprofile01:
| switch(config)#                | port-access | device-profile | profile01 |         |
| ------------------------------ | ----------- | -------------- | --------- | ------- |
| switch(config-device-profile)# |             | no associate   | role      | my-role |
CommandHistory
Devicediscoveryandconfiguration|237

| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
disable
disable
no disable
Description
Disablesadeviceprofile.
Thenoformofthiscommandenablesadeviceprofile.
Examples
Disablingadeviceprofile:
| switch(config)#                | port-access | device-profile | profile01 |
| ------------------------------ | ----------- | -------------- | --------- |
| switch(config-device-profile)# |             | disable        |           |
Enablingadeviceprofilenamedprofile01:
| switch(config)#                | port-access | device-profile | profile01 |
| ------------------------------ | ----------- | -------------- | --------- |
| switch(config-device-profile)# |             | no disable     |           |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
enable
enable
no enable
Description
Enablesadeviceprofile.
238
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Thenoformofthiscommanddisablesadeviceprofile.
Examples
Enablingadeviceprofile:
| switch(config)#                | port-access | device-profile | profile01 |
| ------------------------------ | ----------- | -------------- | --------- |
| switch(config-device-profile)# |             | enable         |           |
Disablingadeviceprofilenamedprofile01:
| switch(config)#                | port-access | device-profile | profile01 |
| ------------------------------ | ----------- | -------------- | --------- |
| switch(config-device-profile)# |             | no enable      |           |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6300 config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6400        |            | forthiscommand. |     |
| ----------- | ---------- | --------------- | --- |
| ignore (for | CDPgroups) |                 |     |
ignore [seq <SEQ-NUM>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query | <VLAN-ID>} |     |     |
| ---------------- | ---------- | --- | --- |
no ignore [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query | <VLAN-ID>} |     |     |
| ---------------- | ---------- | --- | --- |
Description
DefinesaruletoignoredevicesforaCDP(CiscoDiscoveryProtocol)group.Upto64match/ignorerulescan
bedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaCDPgroup.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
platform <PLATFORM> Specifiesthehardwareormodeldetailsoftheneighbor.Range:1
to128alphanumericcharacters.
sw-version <SWVERSION> Specifiesthesoftwareversionoftheneighbor.Range:1to128
alphanumericcharacters.
voice-vlan-query <VLAN-ID> SpecifiestheVLANqueryvalueoftheneighbor.Range:1to65535.
Devicediscoveryandconfiguration|239

Examples
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01intheplatform
TLV:
| switch(config)#           | port-access | cdp-group | grp01    |            |
| ------------------------- | ----------- | --------- | -------- | ---------- |
| switch(config-cdp-group)# |             | ignore    | platform | PLATFORM01 |
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsSWVERSIONinsoftwareversion
TLV:
| switch(config)#           | port-access | cdp-group | grp01      |           |
| ------------------------- | ----------- | --------- | ---------- | --------- |
| switch(config-cdp-group)# |             | ignore    | sw-version | SWVERSION |
Removingtherulethatmatchesthesequencenumber25fromtheCDPgroupnamedgrp01.
| switch(config)#           | port-access | cdp-group | grp01 |     |
| ------------------------- | ----------- | --------- | ----- | --- |
| switch(config-cdp-group)# |             | no ignore | seq   | 25  |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config-cdp-group
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400        |             |     | forthiscommand. |     |
| ----------- | ----------- | --- | --------------- | --- |
| ignore (for | LLDPgroups) |     |                 |     |
ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type | <KEY> [value | <VALUE>]]} |
| ---------- | ------------ | ----- | ------------ | ---------- |
no ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type | <KEY> [value | <VALUE>]]} |
| ---------- | ------------ | ----- | ------------ | ---------- |
Description
DefinesaruletoignoredevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromanLLDPgroup.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
240
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname <SYS-NAME> SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
| vendor-oui | <VENDOR-OUI> |     |     |     |
| ---------- | ------------ | --- | --- | --- |
SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY>    |     |     | SpecifiesthevendorOUIsubtypekey.Optional.      |     |
| ------------- | --- | --- | ---------------------------------------------- | --- |
| value <VALUE> |     |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |     |
alphanumericcharacters.
Examples
AddingaruletotheLLDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01inthesystem
descriptionTLV:
| switch(config)#            | port-access | lldp-group | grp01    |            |
| -------------------------- | ----------- | ---------- | -------- | ---------- |
| switch(config-lldp-group)# |             | ignore     | sys-desc | PLATFORM01 |
Removingtherulethatmatchesthesequencenumber25fromtheLLDPgroupnamedgrp01.
| switch(config)#            | port-access | lldp-group | grp01 |     |
| -------------------------- | ----------- | ---------- | ----- | --- |
| switch(config-lldp-group)# |             | no match   | seq   | 25  |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6300 config-lldp-group Administratorsorlocalusergroupmemberswithexecutionrights
| 6400        |            |     | forthiscommand. |     |
| ----------- | ---------- | --- | --------------- | --- |
| ignore (for | MACgroups) |     |                 |     |
[seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
DefinesaruletoignoredevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddressmask,
orMACOrganizationalUniqueIdentifier(OUI).Upto64ignorerulescanbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaMACgroup.
Devicediscoveryandconfiguration|241

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
seq <SEQ-ID> SpecifiestheentrysequenceIDoftheruletocreateormodifya
MACgroup.IfnoIDisspecifiedwhenaddingarule,anIDis
automaticallyassignedinincrementsof10intheorderinwhich
rulesareadded.Whenmorethanonerulematchesthecommand
entered,therulewiththelowestIDtakesprecedence.Range:1to
4294967295.
| mac <MAC-ADDR> |     |     | SpecifiestheMACaddressofthedevicetoignore. |
| -------------- | --- | --- | ------------------------------------------ |
mac-mask <MAC-MASK>
SpecifiestheMACaddressmasktoignoredevicesinthatrange.
SupportedMACaddressmasks:/32and/40.
mac-oui <MAC-OUI> SpecifiestheMACOUItoignoredevicesinthatrange.Supports
MACOUIaddressofmaximumlengthof24bits.
Usage
Toachievetherequiredconfigurationofmatchesfordevices,itisrecommendedtofirstignorethedevices
thatyoudonotwanttoadd.Thenmatchthecriteriafortherestofthedevicesthatyouwanttoaddtothe
MACgroup.
Forexample,ifyouwanttoignoreaspecificdevicebutaddalltheotherdevicesthatbelongtoaMACOUI,
thenyoumustfirstconfiguretheignorecriteriawithalowersequencenumber.Andthenconfigurematch
criteriawithahighersequencenumber.
Examples
AddingaruletotheMACgroupgrp01toignoreadevicebasedonMACaddress,butmatchallotherdevices
belongingtoaMACOUI:
| switch(config)#           | mac-group | grp01          |                   |
| ------------------------- | --------- | -------------- | ----------------- |
| switch(config-mac-group)# |           | ignore mac     | 1a:2b:3c:4d:5e:6f |
| switch(config-mac-group)# |           | match mac-oui  | 1a:2b:3c          |
| switch(config-mac-group)# |           | exit           |                   |
| switch(config)#           | do show   | running-config |                   |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
!
!
| ssh server vrf | mgmtdefault |     |     |
| -------------- | ----------- | --- | --- |
!
!
!
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |         |                   |     |
| --------------- | ------- | ----------------- | --- |
| seq 10 ignore   | mac     | 1a:2b:3c:4d:5e:6f |     |
| seq 20 match    | mac-oui | 1a:2b:3c          |     |
242
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

```
AddingaruletotheMACgroupgrp01toignoredevicesbasedonMACaddressmask,butmatchallother
devicesbelongingtoaMACOUI:
switch(config)#
|                           | mac-group | grp01           |                |
| ------------------------- | --------- | --------------- | -------------- |
| switch(config-mac-group)# |           | ignore mac-mask | 1a:2b:3c:4d/32 |
| switch(config-mac-group)# |           | match mac-oui   | 1a:2b:3c       |
| switch(config-mac-group)# |           | exit            |                |
| switch(config)#           | do show   | running-config  |                |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
!
!
| ssh server vrf | mgmtdefault |     |     |
| -------------- | ----------- | --- | --- |
!
!
!
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |          |                |     |
| --------------- | -------- | -------------- | --- |
| seq 10 ignore   | mac-mask | 1a:2b:3c:4d/32 |     |
| seq 20 match    | mac-oui  | 1a:2b:3c       |     |
```
AddingaruletotheMACgroupgrp01thatignoresadevicebasedoncompleteMACaddress:
| switch(config)#           | mac-group | grp01      |                   |
| ------------------------- | --------- | ---------- | ----------------- |
| switch(config-mac-group)# |           | ignore mac | 1a:2b:3c:4d:5e:6f |
AddingaruletotheMACgroupgrp02thatignoresdevicesbasedonMACmask:
| switch(config)#           | mac-group | grp01           |                   |
| ------------------------- | --------- | --------------- | ----------------- |
| switch(config-mac-group)# |           | ignore mac-mask | 1a:2b:3c:4d:5e/40 |
| switch(config-mac-group)# |           | ignore mac-mask | 18:e3:ab:73/32    |
AddingaruletotheMACgroupgrp03thatignoresdevicesbasedonMACOUI:
switch(config)#
|                           | mac-group | grp03          |          |
| ------------------------- | --------- | -------------- | -------- |
| switch(config-mac-group)# |           | ignore mac-oui | 81:cd:93 |
AddingaruletotheMACgroupgrp01thatignoresdeviceswithasequencenumberandbasedonMAC
address:
Devicediscoveryandconfiguration|243

| switch(config)# | mac-group | grp01 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|                           |         | seq 10         | ignore mac b2:c3:44:12:78:11 |
| ------------------------- | ------- | -------------- | ---------------------------- |
| switch(config-mac-group)# |         | exit           |                              |
| switch(config)#           | do show | running-config |                              |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |     |     |
| --------------- | --------------------- | --- | --- |
| seq 10 ignore   | mac b2:c3:44:12:78:11 |     |     |
```
RemovingtherulefromtheMACgroupgrp01basedonsequencenumber:
switch(config)#
|                           | mac-group | grp01          |        |
| ------------------------- | --------- | -------------- | ------ |
| switch(config-mac-group)# |           | no ignore      | seq 10 |
| switch(config-mac-group)# |           | exit           |        |
| switch(config)#           | do show   | running-config |        |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |
| --------------- | --- | --- | --- |
```
AddingaruletotheMACgroupgrp01thatignoresdeviceswithMACentrysequencenumberandbasedon
MACOUI:
| switch(config)#           | mac-group | grp01  |                              |
| ------------------------- | --------- | ------ | ---------------------------- |
| switch(config-mac-group)# |           | seq 10 | ignore mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | seq 20 | ignore mac-oui 1a:2b:3c      |
switch(config-mac-group)#
|                           |         | seq 30         | ignore mac-mask 71:14:89:f3/32 |
| ------------------------- | ------- | -------------- | ------------------------------ |
| switch(config-mac-group)# |         | exit           |                                |
| switch(config)#           | do show | running-config |                                |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
244
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| no shutdown |                    |                   |     |     |
| ----------- | ------------------ | ----------------- | --- | --- |
| ip dhcp     |                    |                   |     |     |
| mac-group   | grp01              |                   |     |     |
| seq         | 10 ignore mac      | b2:c3:44:12:78:11 |     |     |
| seq         | 20 ignore mac-oui  | 1a:2b:3c          |     |     |
| seq         | 30 ignore mac-mask | 71:14:89:f3/32    |     |     |
```
RemovingtherulefromtheMACgroupgrp01basedonsequencenumberandMACOUI:
| switch(config)# | mac-group | grp01 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-mac-group)#
|                           |                | no seq         | 20 ignore mac-oui | 1a:2b:3c |
| ------------------------- | -------------- | -------------- | ----------------- | -------- |
| switch(config-mac-group)# |                | exit           |                   |          |
| switch(config)#           | do show        | running-config |                   |          |
| Current                   | configuration: |                |                   |          |
!
| !Version          | AOS-CX Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------------- | --- | --- | --- |
| !export-password: | default                   |     |     |     |
| led locator       | on                        |     |     |     |
!
!
vlan 1
| interface   | mgmt               |                   |     |     |
| ----------- | ------------------ | ----------------- | --- | --- |
| no shutdown |                    |                   |     |     |
| ip dhcp     |                    |                   |     |     |
| mac-group   | grp01              |                   |     |     |
| seq         | 10 ignore mac      | b2:c3:44:12:78:11 |     |     |
| seq         | 30 ignore mac-mask | 71:14:89:f3/32    |     |     |
```
Removingtherulethatmatchesthesequencenumber25fromtheMACgroupnamedgrp01.
| switch(config)#           | mac-group | grp01     |        |     |
| ------------------------- | --------- | --------- | ------ | --- |
| switch(config-mac-group)# |           | no ignore | seq 25 |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config-mac-group
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
mac-group
| mac-group <MAC-GROUP-NAME> |                  |     |     |     |
| -------------------------- | ---------------- | --- | --- | --- |
| no mac-group               | <MAC-GROUP-NAME> |     |     |     |
Devicediscoveryandconfiguration|245

Description
CreatesaMACgroupormodifiesanexistingMACgroup.AMACgroupisusedtoclassifyconnecteddevices
basedontheMACaddressdetails,suchasmaskorOUI.
Amaximumof32MACgroupscanbeconfiguredontheswitch.Amaximumof2MACgroupscanbe
associatedwithadeviceprofile.Eachgroupaccepts64matchorignorecommands.
ThenoformofthiscommandremovesaMACgroup.
Parameter Description
<MAC-GROUP-NAME> SpecifiesthenameoftheMACgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.
Examples
CreatingaMACgroupnamedgrp01:
| switch(config)#           | mac-group | grp01 |
| ------------------------- | --------- | ----- |
| switch(config-mac-group)# |           | exit  |
RemovingaMACgroupnamedgrp01:
| switch(config)# | no mac-group | grp01 |
| --------------- | ------------ | ----- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
6400 forthiscommand.
| match (for | CDPgroups) |     |
| ---------- | ---------- | --- |
match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query | <VLAN-ID>} |     |
| ---------------- | ---------- | --- |
no match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query | <VLAN-ID>} |     |
| ---------------- | ---------- | --- |
Description
DefinesaruletomatchdevicesforaCDPgroup.Amaximumof32CDPgroupscanbeconfiguredonthe
switch.Upto64matchorignorerulescanbedefinedforeachgroup.
ThenoformofthiscommandremovesaruleforaddingdevicestoaCDPgroup.
246
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
platform <PLATFORM> Specifiesthehardwareormodeldetailsoftheneighbor.Range:1
to128alphanumericcharacters.
sw-version <SWVERSION> Specifiesthesoftwareversionoftheneighbor.Range:1to128
alphanumericcharacters.
| voice-vlan-query |     |     | <VLAN-ID> |     |     |     |     |
| ---------------- | --- | --- | --------- | --- | --- | --- | --- |
SpecifiestheVLANqueryvalueoftheneighbor.Range:1to65535.
Examples
AddingrulestomatchaCiscodevicewithaspecificsoftwareversiononVLAN512totheCDPgroupgrp01:
| switch(config)#           |     |     | port-access | cdp-group |                  | grp01     |     |
| ------------------------- | --- | --- | ----------- | --------- | ---------------- | --------- | --- |
| switch(config-cdp-group)# |     |     |             | match     | platform         | CISCO     |     |
| switch(config-cdp-group)# |     |     |             | match     | sw-version       | 11.2(12)P |     |
| switch(config-cdp-group)# |     |     |             | match     | voice-vlan-query |           | 512 |
switch(config-cdp-group)# match seq 50 platform cisco sw-version 11.2(12)P voice-
| vlan-query                |                | 512 |         |                |     |     |     |
| ------------------------- | -------------- | --- | ------- | -------------- | --- | --- | --- |
| switch(config-cdp-group)# |                |     |         | exit           |     |     |     |
| switch(config)#           |                |     | do show | running-config |     |     |     |
| Current                   | configuration: |     |         |                |     |     |     |
!
| !Version          |         | AOS-CX | Virtual.10.0X.000 |     |     |     |     |
| ----------------- | ------- | ------ | ----------------- | --- | --- | --- | --- |
| !export-password: |         |        | default           |     |     |     |     |
| led               | locator | on     |                   |     |     |     |     |
!
!
vlan 1
| port-access |     | cdp-group | grp01            |           |     |     |     |
| ----------- | --- | --------- | ---------------- | --------- | --- | --- | --- |
|             | seq | 10 match  | platform         | CISCO     |     |     |     |
|             | seq | 20 match  | sw-version       | 11.2(12)P |     |     |     |
|             | seq | 30 match  | voice-vlan-query |           | 512 |     |     |
seq 50 match platform cisco sw-version 11.2(12)P voice-vlan-query 512
Removingarulethatmatchesthesequencenumber25fromtheCDPgroupnamedgrp01:
| switch(config)#           |     |     | port-access | cdp-group |     | grp01 |     |
| ------------------------- | --- | --- | ----------- | --------- | --- | ----- | --- |
| switch(config-cdp-group)# |     |     |             | no match  | seq | 25    |     |
Addingarulethatmatchesthevalueofvendor-OUI000b86totheCDPgroupnamedgrp01:
| switch(config)#           |     |     | port-access | cdp-group |            | grp01  |     |
| ------------------------- | --- | --- | ----------- | --------- | ---------- | ------ | --- |
| switch(config-cdp-group)# |     |     |             | match     | vendor-oui | 000b86 |     |
CommandHistory
Devicediscoveryandconfiguration|247

| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
6300 config-cdp-group Administratorsorlocalusergroupmemberswithexecutionrights
| 6400       |                  |              |            | forthiscommand. |                   |            |     |
| ---------- | ---------------- | ------------ | ---------- | --------------- | ----------------- | ---------- | --- |
| match      | (for LLDPgroups) |              |            |                 |                   |            |     |
| match [seq | <SEQ-ID>]        | {sys-desc    | <SYS-DESC> |                 | | sysname         | <SYS-NAME> | |   |
| vendor-oui |                  | <VENDOR-OUI> | [type      | <KEY>           | [value <VALUE>]]} |            |     |
no match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui |     | <VENDOR-OUI> | [type | <KEY> | [value <VALUE>]]} |     |     |
| ---------- | --- | ------------ | ----- | ----- | ----------------- | --- | --- |
Description
DefinesaruletomatchdevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedforagroup.
Thenoformofthiscommandremovesarule.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
seq <SEQ-ID>
SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
| sys-desc | <SYS-DESC> |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | --- |
SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname <SYS-NAME> SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY> |         |     |     | SpecifiesthevendorOUIsubtypekey.               |     |     |     |
| ---------- | ------- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| value      | <VALUE> |     |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |     |     |     |
alphanumericcharacters.
Examples
AddingrulesthatmatchtheLLDPsystemdescriptionArubaSwitchandsystemnameArubatotheLLDP
groupnamedgrp01:
switch(config)#
|                            |                | port-access | lldp-group     |          | grp01       |     |     |
| -------------------------- | -------------- | ----------- | -------------- | -------- | ----------- | --- | --- |
| switch(config-lldp-group)# |                |             | match          | sys-desc | ArubaSwitch |     |     |
| switch(config-lldp-group)# |                |             | match          | sysname  | Aruba       |     |     |
| switch(config)#            |                | do show     | running-config |          |             |     |     |
| Current                    | configuration: |             |                |          |             |     |     |
248
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

!
| !Version          | AOS-CX Virtual.10.0X.000 |     |     |     |     |
| ----------------- | ------------------------ | --- | --- | --- | --- |
| !export-password: | default                  |     |     |     |     |
| led locator       | on                       |     |     |     |     |
!
!
vlan 1
| port-access | lldp-group        | grp01       |     |     |     |
| ----------- | ----------------- | ----------- | --- | --- | --- |
| seq         | 10 match sys-desc | ArubaSwitch |     |     |     |
| seq         | 20 match sysname  | Aruba       |     |     |     |
Removingarulethatmatchesthesequencenumber25fromanLLDPgroupnamedgrp01:
| switch(config)#            | port-access | lldp-group | grp01  |     |     |
| -------------------------- | ----------- | ---------- | ------ | --- | --- |
| switch(config-lldp-group)# |             | no match   | seq 25 |     |     |
Addingarulethatmatchesthevalueofvendor-OUI000b86withtypeof1totheLLDPgroupnamed
grp01:
| switch(config)#            | port-access | lldp-group | grp01      |             |     |
| -------------------------- | ----------- | ---------- | ---------- | ----------- | --- |
| switch(config-lldp-group)# |             | match      | vendor-oui | 000b86 type | 1   |
Addingarulethatmatchesthevalueofvendor-OUI000c34totheLLDPgroupnamedgrp01:
| switch(config)#            | port-access | lldp-group | grp01      |        |     |
| -------------------------- | ----------- | ---------- | ---------- | ------ | --- |
| switch(config-lldp-group)# |             | match      | vendor-oui | 000c34 |     |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 config-lldp-group Administratorsorlocalusergroupmemberswithexecutionrights
| 6400       |            |     | forthiscommand. |     |     |
| ---------- | ---------- | --- | --------------- | --- | --- |
| match (for | MACgroups) |     |                 |     |     |
[seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
DefinesaruletomatchdevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddressmask,
orMACOrganizationalUniqueIdentifier(OUI).Upto64matchrulescanbedefinedforagroup.
Devicediscoveryandconfiguration|249

YoumustnotconfigurethefollowingspecialMACaddresses:
n NullMAC—Forexample,00:00:00:00:00:00or00:00:00/32
n MulticastMAC
n BroadcastMAC—Forexample,ff:ff:ff:ff:ff:ff:ff
SystemMAC
n
Althoughtheswitchacceptstheseaddresses,itwillnotprocesstheseaddressesforthelocalMACmatchfeature.
ThenoformofthiscommandremovesaruleforaddingdevicestoaMACgroup.
Thenumberofclientsthatcanonboardbasedonthematchcriteriaisconfiguredintheaaa
authentication port-access client-limitcommand.Forinformationaboutthiscommand,seethe
SecurityGuideforyourswitch.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
seq <SEQ-ID>
SpecifiestheentrysequenceIDoftheruletocreateormodifya
MACgroup.IfnoIDisspecifiedwhenaddingarule,anIDis
automaticallyassignedinincrementsof10intheorderinwhich
rulesareadded.Whenmorethanonerulematchesthecommand
entered,therulewiththelowestIDtakesprecedence.Range:1to
4294967295.
| mac <MAC-ADDR> |     |     | SpecifiestheMACaddressofthedevice. |
| -------------- | --- | --- | ---------------------------------- |
mac-mask <MAC-MASK>
SpecifiestheMACaddressmasktoadddevicesinthatrange.
SupportedMACaddressmasks:/32and/40.
mac-oui <MAC-OUI>
SpecifiestheMACOUItoadddevicesinthatrange.SupportsMAC
OUIaddressofmaximumlengthof24bits.
Examples
AddingadevicetotheMACgroupgrp01basedoncompleteMACaddress:
| switch(config)#           | mac-group | grp01     |                   |
| ------------------------- | --------- | --------- | ----------------- |
| switch(config-mac-group)# |           | match mac | 1a:2b:3c:4d:5e:6f |
| switch(config-mac-group)# |           | exit      |                   |
AddingdevicestotheMACgroupgrp02basedonMACmask:
| switch(config)#           | mac-group | grp01          |                   |
| ------------------------- | --------- | -------------- | ----------------- |
| switch(config-mac-group)# |           | match mac-mask | 1a:2b:3c:4d:5e/40 |
| switch(config-mac-group)# |           | match mac-mask | 18:e3:ab:73/32    |
| switch(config-mac-group)# |           | exit           |                   |
AddingdevicestotheMACgroupgrp03basedonMACOUI:
| switch(config)#           | mac-group | grp03         |          |
| ------------------------- | --------- | ------------- | -------- |
| switch(config-mac-group)# |           | match mac-oui | 81:cd:93 |
| switch(config-mac-group)# |           | exit          |          |
250
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress:
| switch(config)#           | mac-group | grp01          |                       |
| ------------------------- | --------- | -------------- | --------------------- |
| switch(config-mac-group)# |           | seq 10 match   | mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | exit           |                       |
| switch(config)#           | do show   | running-config |                       |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |     |     |
| --------------- | --------------------- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |     |     |
```
RemovingdevicesfromtheMACgroupgrp01basedonsequencenumber:
| switch(config)#           | mac-group | grp01          |     |
| ------------------------- | --------- | -------------- | --- |
| switch(config-mac-group)# |           | no match seq   | 10  |
| switch(config-mac-group)# |           | exit           |     |
| switch(config)#           | do show   | running-config |     |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |
| --------------- | --- | --- | --- |
```
AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress,MAC
addressmask,andMACOUI:
| switch(config)#           | mac-group | grp01          |                         |
| ------------------------- | --------- | -------------- | ----------------------- |
| switch(config-mac-group)# |           | seq 10 match   | mac b2:c3:44:12:78:11   |
| switch(config-mac-group)# |           | seq 20 match   | mac-oui 1a:2b:3c        |
| switch(config-mac-group)# |           | seq 30 match   | mac-mask 71:14:89:f3/32 |
| switch(config-mac-group)# |           | exit           |                         |
| switch(config)#           | do show   | running-config |                         |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
Devicediscoveryandconfiguration|251

vlan 1
| interface mgmt |     |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |                |     |     |
| --------------- | --------------------- | -------------- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |                |     |     |
| seq 20 match    | mac-oui               | 1a:2b:3c       |     |     |
| seq 30 match    | mac-mask              | 71:14:89:f3/32 |     |     |
```
RemovingdevicesfromtheMACgroupgrp01basedonMACOUI:
| switch(config)#           | mac-group | grp01          |                  |          |
| ------------------------- | --------- | -------------- | ---------------- | -------- |
| switch(config-mac-group)# |           | no seq         | 20 match mac-oui | 1a:2b:3c |
| switch(config-mac-group)# |           | exit           |                  |          |
| switch(config)#           | do show   | running-config |                  |          |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------ | --- | --- | --- |
| !export-password: | default            |     |     |     |
| led locator on    |                    |     |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |                |     |     |
| --------------- | --------------------- | -------------- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |                |     |     |
| seq 30 match    | mac-mask              | 71:14:89:f3/32 |     |     |
```
AddingdevicestotheMACgroupgrp03withMACentrysequencenumberandbasedonMACaddress
mask:
| switch(config)# | mac-group | grp03 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-mac-group)# seq 10 match mac-mask 10:14:a3:b7:55/40
| switch(config-mac-group)# |         | exit           |     |     |
| ------------------------- | ------- | -------------- | --- | --- |
| switch(config)#           | do show | running-config |     |     |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------ | --- | --- | --- |
| !export-password: | default            |     |     |     |
| led locator on    |                    |     |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp03 |          |                   |     |     |
| --------------- | -------- | ----------------- | --- | --- |
| seq 10 match    | mac-mask | 10:14:a3:b7:55/40 |     |     |
```
RemovingdevicesfromtheMACgroupgrp03basedonMACaddressmask:
252
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| switch(config)# |     | mac-group |     | grp03 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
switch(config-mac-group)#
|                           |                |     |                     | no seq | 10 match | mac-mask | 10:14:a3:b7:55/40 |
| ------------------------- | -------------- | --- | ------------------- | ------ | -------- | -------- | ----------------- |
| switch(config-mac-group)# |                |     |                     | exit   |          |          |                   |
| switch(config)#           |                | do  | show running-config |        |          |          |                   |
| Current                   | configuration: |     |                     |        |          |          |                   |
!
| !Version          | AOS-CX | Virtual.10.0X.0001 |         |     |     |     |     |
| ----------------- | ------ | ------------------ | ------- | --- | --- | --- | --- |
| !export-password: |        |                    | default |     |     |     |     |
| led locator       | on     |                    |         |     |     |     |     |
!
!
| vlan      | 1    |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- |
| interface | mgmt |     |     |     |     |     |     |
no shutdown
ip dhcp
| mac-group | grp03 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
```
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
6300 config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
port-accesscdp-group
| port-access    | cdp-group |     | <CDP-GROUP-NAME> |     |     |     |     |
| -------------- | --------- | --- | ---------------- | --- | --- | --- | --- |
| no port-access | cdp-group |     | <CDP-GROUP-NAME> |     |     |     |     |
Description
CreatesaCDP(CiscoDiscoveryProtocol)groupormodifiesanexistingCDPgroup.ACDPGroupisusedto
classifyconnecteddevicesbasedontheCDPpacketdetailsadvertisedbythedevice.Amaximumof32CDP
groupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesaCDPgroup.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<CDP-GROUP-NAME>
SpecifiesthenameoftheCDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatingaCDPgroupnamedgrp01:
| switch(config)#           |     | port-access |     | cdp-group |          | grp01 |     |
| ------------------------- | --- | ----------- | --- | --------- | -------- | ----- | --- |
| switch(config-cdp-group)# |     |             |     | match     | platform | CISCO |     |
Devicediscoveryandconfiguration|253

switch(config-cdp-group)# match sw-version 11.2(12)P
switch(config-cdp-group)# match voice-vlan-query 512
switch(config-cdp-group)# seq 50 match platform cisco sw-version 11.2(12)P voice-
vlan-query 512
switch(config-cdp-group)# exit
switch(config)# do show running-config

Current configuration:
!
!Version AOS-CX Virtual.10.0X.000
!export-password: default
led locator on
!
!
vlan 1
port-access cdp-group grp01

seq 10 match platform CISCO
seq 20 match sw-version 11.2(12)P
seq 30 match voice-vlan-query 512
seq 50 match platform cisco sw-version 11.2(12)P voice-vlan-query 512

Removing a CDP group named grp01:

switch(config)# no port-access cdp-group grp01

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6300
6400

config

Administrators or local user group members with execution rights
for this command.

port-access device-profile

port-access device-profile <DEVICE-PROFILE-NAME>
no port-access device-profile <DEVICE-PROFILE-NAME>

Description

Creates a new device profile and switches to the config-device-profile context. A maximum of 32 device
profiles can be created.

The no form of this command removes a device profile.

Parameter

Description

<DEVICE-PROFILE-NAME>

Specifies the name of a device profile. Range: 1 to 32
alphanumeric characters.

Examples

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

254

Creatingadeviceprofilenamedprofile01:
| switch(config)# |     | port-access |     | device-profile | profile01 |
| --------------- | --- | ----------- | --- | -------------- | --------- |
switch(config-device-profile)#
Removingadeviceprofilenamedprofile01:
| switch(config)# |     | no port-access |     | device-profile | profile01 |
| --------------- | --- | -------------- | --- | -------------- | --------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                      |     |     |      | forthiscommand.             |     |
| ------------------------- | --- | --- | ---- | --------------------------- | --- |
| port-accessdevice-profile |     |     | mode | block-until-profile-applied |     |
Youmustconfigurethismodeindeviceprofileonlyonstandaloneportswherethereisnosecurityconfiguredand
whenyounotwanttheporttobeofflineuntiloneclientisonboarded.
| port-access    | device-profile |     | mode | block-until-profile-applied |     |
| -------------- | -------------- | --- | ---- | --------------------------- | --- |
| no port-access | device-profile |     | mode | block-until-profile-applied |     |
Description
Configurestheswitchtoblocktheportuntilaprofilematchoccursforadevice.Thisconfigurationis
requiredwhennosecurityfeatureisenabledontheport.
YoumustenablethismodeorsecurityontheportforlocalMACmatchfeaturetooperate.Youmustnot
enablebothfeaturesonthesameportatthesametime.
YoumustnotcombineanyotherAAAconfigurationswiththeblock-until-profile-appliedmode.
ThenoformofthiscommandremovesaruleforaddingdevicestoaMACgroup.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringblock-until-profileappliedmodeonport1/1/1:
| switch(config)#    |     | interface   | 1/1/1 |                |     |
| ------------------ | --- | ----------- | ----- | -------------- | --- |
| switch(config-if)# |     | port-access |       | device-profile |     |
switch(config-if-deviceprofile)# mode block-until-profile-applied
| switch(config-if-deviceprofile)# |     |     |     | end |     |
| -------------------------------- | --- | --- | --- | --- | --- |
Devicediscoveryandconfiguration|255

CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400 | config-if-deviceprofile |     |     |     | rightsforthiscommand. |     |
| ---- | ----------------------- | --- | --- | --- | --------------------- | --- |
port-accesslldp-group
| port-access    | lldp-group |     | <LLDP-GROUP-NAME> |     |     |     |
| -------------- | ---------- | --- | ----------------- | --- | --- | --- |
| no port-access | lldp-group |     | <LLDP-GROUP-NAME> |     |     |     |
Description
CreatesanLLDPgroupormodifiesanexistingLLDPgroup.AnLLDPgroupisusedtoclassifyconnected
devicesbasedontheLLDPtype-length-values(TLVs)advertisedbythedevice.Amaximumof32LLDP
groupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesanLLDPgroup.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<LLDP-GROUP-NAME>
SpecifiesthenameoftheLLDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatinganLLDPgroupnamedgrp01:
| switch(config)# |     | port-access |     | lldp-group |     | grp01 |
| --------------- | --- | ----------- | --- | ---------- | --- | ----- |
switch(config-lldp-group)#
RemovinganLLDPgroupnamedgrp01:
| switch(config)# |     | no  | port-access | lldp-group |     | grp01 |
| --------------- | --- | --- | ----------- | ---------- | --- | ----- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
256
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- |

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
show port-accessdevice-profile
show port-access device-profile [[interface {all | <INTERFACE-ID>}
| [client-status | <MAC-ADDR>]] | |   | name <DEVICE-PROFILE-NAME>] |
| -------------- | ------------ | --- | --------------------------- |
Description
ShowstheclientstatusforaspecificMACaddressorprofilename.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
interface {all | <INTERFACE-ID>} Selectallforallinterfacesorspecifythenameofaninterfacein
theformat:member/slot/port.
| client-status | <MAC-ADDR> |     |     |
| ------------- | ---------- | --- | --- |
SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.
name <DEVICE-PROFILE-NAME> Specifiesthenameofthedeviceprofile.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingtheappliedstateofthedeviceprofiles:
| switch# | show port-access | device-profile                   |     |
| ------- | ---------------- | -------------------------------- | --- |
| Profile | Name :           | accesspoints                     |     |
| LLDP    | Groups :         | 2920-grp                         |     |
| CDP     | Groups :         |                                  |     |
| MAC     | Groups :         | 2920-mac-grp1,2920-iot-grp2      |     |
| Role    | :                | local_role_1                     |     |
| State   | :                | Enabled                          |     |
| Profile | Name :           | access_switches                  |     |
| LLDP    | Groups :         | 2920-grp                         |     |
| CDP     | Groups :         |                                  |     |
| MAC     | Groups :         |                                  |     |
| Role    | :                | local_2920_role                  |     |
| State   | :                | Enabled                          |     |
| Profile | Name :           | iot_devices                      |     |
| LLDP    | Groups :         |                                  |     |
| CDP     | Groups :         |                                  |     |
| MAC     | Groups :         | iot_camera-grp1,iot_sensors-grp1 |     |
| Role    | :                | local_2920_role                  |     |
| State   | :                | Enabled                          |     |
| Profile | Name :           | lobbyaps                         |     |
| LLDP    | Groups :         |                                  |     |
| CDP     | Groups :         | lobby_ap_cdp_grp                 |     |
| MAC     | Groups :         |                                  |     |
| Role    | :                | test_ap_role                     |     |
| State   | :                | Disabled                         |     |
Devicediscoveryandconfiguration|257

Showingtheappliedstateofthedeviceprofileoninterface1/1/3:
switch# show port-access device-profile interface 1/1/3 client-status
00:0c:29:9e:d1:20
| Port | 1/1/3,  | Neighbor-Mac |                | 00:0c:29:9e:d1:20 |          |           |      |
| ---- | ------- | ------------ | -------------- | ----------------- | -------- | --------- | ---- |
|      | Profile | Name         | : lobbyaps     |                   |          |           |      |
|      | LLDP    | Group        | :              |                   |          |           |      |
|      | CDP     | Group        | : aruba-ap_cdp |                   |          |           |      |
|      | MAC     | Group        | :              |                   |          |           |      |
|      | Role    |              | : test_ap_role |                   |          |           |      |
|      | Status  |              | : Failed       |                   |          |           |      |
|      | Failure | Reason       | : Failed       |                   | to apply | MAC based | VLAN |
Showingtheappliedstateofaspecificdeviceprofile:
| switch# |         | show port-access |     | device-profile |                  | name | lldp-group |
| ------- | ------- | ---------------- | --- | -------------- | ---------------- | ---- | ---------- |
|         | Profile | Name             |     | :              | lldp-group       |      |            |
|         | LLDP    | Groups           |     | :              |                  |      |            |
|         | CDP     | Groups           |     | :              |                  |      |            |
|         | MAC     | Groups           |     | :              | pc-behind-phone, |      | lldp       |
|         | Role    |                  |     | :              | auth_role        |      |            |
|         | State   |                  |     | :              | Enabled          |      |            |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
LLDP
TheIEEE802.1ABLinkLayerDiscoveryProtocol(LLDP)providesastandards-basedmethodfornetwork
devicestodiscovereachotherandexchangeinformationabouttheircapabilities.AnLLDPdeviceadvertises
itselftoadjacent(neighbor)devicesbytransmittingLLDPdatapacketsonallinterfacesonwhichoutbound
LLDPisenabled,andreadingLLDPadvertisementsfromneighbordevicesonportsonwhichinboundLLDP
isenabled.InboundpacketsfromneighbordevicesarestoredinaspecialLLDPMIB(management
informationbase).ThisinformationcanthenbequeriedbyotherdevicesthroughSNMP.
LLDPinformationisusedbynetworkmanagementtoolstocreateaccuratephysicalnetworktopologiesby
determiningwhichdevicesareneighborsandthroughwhichinterfacestheyconnect.LLDPoperatesatlayer
2andrequiresanLLDPagenttobeactiveoneachinterfacethatsendsandreceivesLLDPadvertisements.
LLDPadvertisementscancontainavariablenumberofTLV(type,length,value)informationelements.Each
TLVdescribesasingleattributeofadevicesuchas:systemcapabilities,managementIPaddress,deviceID,
portID.
258
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |

Packet boundaries

When multiple LLDP devices are directly connected, an outbound LLDP packet travels only to the next LLDP
device. An LLDP-capable device does not forward LLDP packets to any other devices, regardless of whether
they are LLDP-enabled.

An intervening hub or repeater forwards the LLDP packets it receives in the same manner as any other
multicast packets it receives. Therefore, two LLDP switches joined by a hub or repeater handle LLDP traffic
in the same way that they would if directly connected.

Any intervening 802.1D device or Layer-3 device that is either LLDP-unaware or has disabled LLDP
operation drops the packet.

LLDP-MED

LLDP-MED (ANSI/TIA-1057/D6) extends the LLDP (IEEE 802.1AB) industry standard to support advanced
features on the network edge for Voice Over IP (VoIP) endpoint devices with specialized capabilities and
LLDP-MED standards-based functionality. LLDP-MED in the switches uses the standard LLDP commands
described earlier in this section, with some extensions, and also introduces new commands unique to LLDP-
MED operation. The show commands described elsewhere in this section are applicable to both LLDP and
LLDP-MED operation. LLDP-MED enables:

n Configure Voice VLAN and advertise it to connected MED endpoint devices.

n Power over Ethernet (PoE) status and troubleshooting support via SNMP.

LLDP agent

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

n Receive only (Rx): Enables a port to receive and read LLDP packets from LLDP neighbors and to store the

packet data in the switch's MIB. However, the port does not transmit outbound LLDP packets. This
prevents LLDP neighbors from learning about the switch through that port.

Device discovery and configuration | 259

n Disabled: Disables LLDP packet transmissions and reception on a port. In this state, the switch does not
use the port for either learning about LLDP neighbors or informing LLDP neighbors of its presence.

An LLDP agent operating in TxRx mode or Tx mode sends LLDP frames to its directly connected devices
both periodically and when the local configuration changes.

Sending LLDP frames

Each time the LLDP operating mode of an LLDP agent changes, its LLDP protocol state machine reinitializes.
A configurable reinitialization delay prevents frequent initializations caused by frequent changes to the
operating mode. If you configure the reinitialization delay, an LLDP agent must wait the specified amount of
time to initialize LLDP after the LLDP operating mode changes.

Receiving LLDP frames

An LLDP agent operating in TxRx mode or Rx mode confirms the validity of TLVs carried in every received
LLDP frame. If the TLVs are valid, the LLDP agent saves the information and starts an aging timer. The initial
value of the aging timer is equal to the TTL value in the Time To Live TLV carried in the LLDP frame. When
the LLDP agent receives a new LLDP frame, the aging timer restarts. When the aging timer decreases to zero,
all saved information ages out.

TLV support

By default, the agent sends and receives the following mandatory TLVs on each interface:

n Port ID

n Chassis ID

n TTL

By default, the following ANSI/TIA-1057 TLVs for LLDP Media Endpoint Discovery (MED) are enabled on an
agent. Sending them depends on the configuration and reception of any MED TLVs:

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

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

260

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

Trunk allowed VLANs information are not advertised as part of the Port VLAN ID TLV. (Not supported on
the OOBM interface)

LLDP MED support

LLDP-MED interoperates with directly connected IP telephony (endpoint) clients and provides the following
features:

n Advertisement of the voice VLAN configured on the interface which is used by connected IP telephony

(endpoint) clients.

n Advertisement of the configured location on the switch that can be used by the connected endpoint.

n Support for the fast-start capability

LLDP-MED is intended for use with VoIP endpoints and is not designed to support links between network

infrastructure devices (such as switch-to-switch or switch-to-router links).

Configuring the LLDP agent

Procedure

1. By default, the LLDP agent is enabled on all active interfaces. If LLDP was disabled, enable it with the

command lldp.

2. By default, the LLDP agent transmits and receive on all interfaces. To customize LLDP behavior on a

specific interface, use the commands lldp transmit and lldp receive.

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

Device discovery and configuration | 261

4. Bydefault,allsupportedTLVsaresentandreceived.Tocustomizethelist,usethecommandlldp
select-tlv.
5. Bydefault,supportfortheLLDP-MEDTLVisenabled.Tocustomizesettings,usethecommandslldp
| medandlldp | med-location. |     |
| ---------- | ------------- | --- |
6. Ifrequired,adjustLLDPtimer,holdtime,reinitializationdelay,andtransmitdelayfromtheirdefault
valueswiththecommandslldp timer,lldp holdtime,lldp reinit,andlldp txdelay.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexamplecreatesthefollowingconfiguration:
EnablesLLDPsupport.
n
DisablesLLDPtransmissiononinterface1/1/1.
n
| switch(config)#      | lldp      |               |
| -------------------- | --------- | ------------- |
| switch(config)#      | interface | 1/1/1         |
| switch(config-copp)# | no        | lldp transmit |
LLDP commands
clear lldpneighbors
| clear lldp neighbors |     |     |
| -------------------- | --- | --- |
Description
ClearsallLLDPneighbordetails.
Examples
ClearingallLLDPneighbordetails:
| switch# | clear lldp neighbors |     |
| ------- | -------------------- | --- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
clear lldpstatistics
| clear lldp statistics |     |     |
| --------------------- | --- | --- |
Description
262
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

ClearsallLLDPneighborstatistics.
Examples
ClearingallLLDPneighborstatistics:
| switch# | clear lldp statistics |     |
| ------- | --------------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
lldp
lldp
no lldp
Description
EnablesLLDPsupportgloballyonallactiveinterfaces.Bydefault,LLDPisenabled.
ThenoformofthiscommanddisablesLLDPsupportgloballyonallactiveinterfaces.Itdoesnotremoveany
LLDPconfigurationsettings.
Examples
EnablingLLDP:
| switch(config)# | lldp |     |
| --------------- | ---- | --- |
DisablingLLDP:
| switch(config)# | no lldp |     |
| --------------- | ------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
Devicediscoveryandconfiguration|263

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpdot3
| lldp dot3 {poe | | macphy}      |     |
| -------------- | -------------- | --- |
| no lldp dot3   | {poe | macphy} |     |
Description
Setsthe802.3TLVstobeadvertised.Bydefault,advertisementofbothPOEandMAC/PHYTLVsisenabled.
NotsupportedontheOOBMinterface.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     | Description                                       |
| --------- | --- | ------------------------------------------------- |
| poe       |     | SpecifiesadvertisementofpoweroverEthernetdatalink |
classification.
| macphy |     | Specifiesadvertisementofmediaaccesscontrolandphysical |
| ------ | --- | ----------------------------------------------------- |
layerinformation.
Examples
EnablingadvertisementofthePOETLV:
| switch(config-if)# | lldp dot3 | poe |
| ------------------ | --------- | --- |
DisablingadvertisementofthePOETLV:
| switch(config-if)# | no lldp | dot3 poe |
| ------------------ | ------- | -------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpholdtime
| lldp holdtime | <TIME> |     |
| ------------- | ------ | --- |
no lldp holdtime
Description
264
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

SetstheholdtimethatisusedtocalculatetheLLDPTime-to-Livevalue.Time-to-Livedefinesthelengthof
timethatneighborsconsiderLLDPinformationsentbythisagentasvalid.WhenTime-to-Liveexpires,the
informationisdeletedbytheneighbor.Time-to-liveiscalculatedbymultiplyingholdtimebythevalueof
lldp timer.
Thenoformofthiscommandsetstheholdtimetoitsdefaultvalueof4.
| Parameter |     | Description                                          |
| --------- | --- | ---------------------------------------------------- |
| <TIME>    |     | Specifiestheholdtimeinseconds.Range:2to10.Default:4. |
Examples
Settingtheholdtimeto8seconds:
| switch(config)# | lldp holdtime | 8   |
| --------------- | ------------- | --- |
Settingtheholdtimetothedefaultvalueof4seconds:
| switch(config)# | no lldp holdtime |     |
| --------------- | ---------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpmanagement-ipv4-address
| lldp management-ipv4-address | <IPV4-ADDR> |     |
| ---------------------------- | ----------- | --- |
no lldp management-ipv4-address
Description
DefinestheIPv4managementaddressoftheswitchwhichissentinthemanagementaddressTLV.One
IPv4andoneIPv6managementaddresscanbeconfigured.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
n IPaddressoftheport
n IPaddressofthemanagementinterface
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv4managementaddressoftheswitch.
Devicediscoveryandconfiguration|265

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesthemanagementaddressoftheswitchasanIPv4format
(x.x.x.x),wherexisadecimalvaluefrom0to255.
Examples
Settingthemanagementaddressto10.10.10.2:
| switch(config)# | lldp management-ipv4-address |     | 10.10.10.2 |
| --------------- | ---------------------------- | --- | ---------- |
Removingthemanagementaddress:
| switch(config)# | no lldp management-ipv4-address |     |     |
| --------------- | ------------------------------- | --- | --- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpmanagement-ipv6-address
lldp management-ipv6-address <IPV6-ADDR>
no lldp management-ipv6-address
Description
DefinestheIPv6managementaddressoftheswitch.Themanagementaddressisencapsulatedinthe
managementaddressTLV.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
n IPaddressoftheport
n IPaddressofthemanagementinterface
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv6managementaddressoftheswitch.
| Parameter   |     | Description                      |     |
| ----------- | --- | -------------------------------- | --- |
| <IPV6-ADDR> |     | SpecifiesanIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
266
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Settingthemanagementaddressto2001:db8:85a3::8a2e:370:7334:
switch(config)# lldp management-ipv6-address 2001:0db8:85a3::8a2e:0370:7334
Removingthemanagementaddress:
| switch(config)# | no lldp management-ipv6-address |     |     |     |     |
| --------------- | ------------------------------- | --- | --- | --- | --- |
CommandHistory
| Release        |     | Modification |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpmed
| lldp med    | [poe [priority-override] | | capability | | network-policy] |     |     |
| ----------- | ------------------------ | ------------ | ----------------- | --- | --- |
| no med [poe | [priority-override]      | | capability | | network-policy] |     |     |
Description
ConfiguressupportfortheLLDP-MEDTLV.LLDP-MED(mediaendpointdevices)isanextensiontoLLDP
developedbyTIAtosupportinteroperabilitybetweenVoIPendpointdevicesandothernetworkingend-
devices.TheswitchonlysendstheLLDPMEDTLVafterreceivingaMEDTLVfromandconnectedendpoint
device.
NotsupportedontheOOBMinterface.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
poe [priority-override]
SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
|     |     | dot3 | poeandlldp | med poeareenabled,thelldp | dot3 poe3 |
| --- | --- | ---- | ---------- | ------------------------- | --------- |
settingtakesprecedence.Default:enabled.
| capability |     | SpecifiesadvertisementofsupportedLLDPMEDTLVs.The |     |     |     |
| ---------- | --- | ------------------------------------------------ | --- | --- | --- |
capabilityTLVisalwayssentwithotherMEDTLVs,thereforeit
cannotbedisabledwhenotherMEDTLVsareenabled.Default:
enabled.
network-policy Networkpolicydiscoveryletsendpointsandnetworkdevices
advertisetheirVLANIDs,andIEEE802.1p(PCPandDSCP)values
forvoiceapplications.ThisTLVisonlysentwhenavoiceVLAN
policyispresent.Default:enabled.
Devicediscoveryandconfiguration|267

Examples
EnablingadvertisementofthenetworkpolicyTLV:
switch(config-if)#
|     |     | lldp | med | network-policy |     |     |
| --- | --- | ---- | --- | -------------- | --- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |     | no  | lldp med | network-policy |     |     |
| ------------------ | --- | --- | -------- | -------------- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpmed-location
| lldp med-location | {civic-addr |     |             | | elin-addr | }   |     |
| ----------------- | ----------- | --- | ----------- | ----------- | --- | --- |
| no med-location   | {civic-addr |     | | elin-addr |             | }   |     |
Description
ConfiguressupportfortheLLDP-MEDTLV.Supportsonlycivicaddressandemergencylocationinformation
number(ELIN).Coordinate-basedlocationisnotsupported.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
civic-addr
ConfigurestheLLDPMEDciviclocationTLV.
elin-addr ConfiguressupportfortheLLDPMEDemergencylocationTLV.
Examples
EnablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | lldp | med-location |     | elin-addr | gher |
| ------------------ | --- | ---- | ------------ | --- | --------- | ---- |
DisablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | no  | lldp med-location |     | elin-addr | gher |
| ------------------ | --- | --- | ----------------- | --- | --------- | ---- |
EnablingsupportfortheLLDPMEDcivicaddressTLV:
268
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

switch(config-if)# lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
DisablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# no lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpreceive
lldp receive
no lldp receive
Description
EnablesreceptionofLLDPinformationonaninterface.Bydefault,LLDPreceptionisenabledonallactive
interfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablesreceptionofLLDPinformationonaninterface.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1   |
| ------------------ | --------- | ------- |
| switch(config-if)# | lldp      | receive |
DisablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1   |
| ------------------ | --------- | ------- |
| switch(config-if)# | no lldp   | receive |
EnablingLLDPreceptionontheOOBMinterface:
| switch(config)#    | interface | mgmt    |
| ------------------ | --------- | ------- |
| switch(config-if)# | lldp      | receive |
DisablingLLDPreceptionontheOOBMinterface:
Devicediscoveryandconfiguration|269

| switch(config)# | interface | mgmt |
| --------------- | --------- | ---- |
switch(config-if)#
|     | no lldp | receive |
| --- | ------- | ------- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpreinit
| lldp reinit | <TIME> |     |
| ----------- | ------ | --- |
no lldp reinit
Description
Setstheamountoftime(inseconds)towaitbeforeperformingLLDPinitializationonaninterface.
Thenoformofthiscommandsetsthereinitializationtimetoitsdefaultvalueof2seconds.
Parameter Description
<TIME>
Specifiesthereinitializationtimeinseconds.Range:1to10.
Default:2seconds.
Examples
Settingthereinitializationtimeto5seconds:
| switch(config)# | lldp reinit | 5   |
| --------------- | ----------- | --- |
Settingthereinitializationtimetothedefaultvalueof2seconds:
| switch(config)# | no lldp | reinit |
| --------------- | ------- | ------ |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
270
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution rights
for this command.

lldp select-tlv

lldp select-tlv <TLV-NAME>
no lldp select-tlv <TLV-NAME>

Description

Selects a TLV that the LLDP agent will send and receive. By default, all supported TLVs are sent and received.

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
If layer 3, then the route-only port IP address. If layer

2, the IP address of the SVI.
4. OOBM interface IP address.
5. Base MAC address of the switch.

n port-description: A description of the port.

n port-vlan-id: VLAN ID assigned to the port.

n system-capabilities: Identifies the primary switch

functions that are enabled, such as routing.

n system-description: Description of the system,
comprised of the following information: hardware
serial number, hardware revision number, and firmware
version.

n system-name: Host name assigned to the switch.

Examples

Stopping the LLDP agent from sending the port-description TLV:

switch(config)# no lldp select-tlv port-description

Enabling the LLDP agent to send the port-description TLV:

switch(config)# lldp select-tlv port-description

Command History

Device discovery and configuration | 271

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptimer
| lldp timer <TIME> |     |     |
| ----------------- | --- | --- |
no lldp timer
Description
Setstheinterval(inseconds)atwhichlocalLLDPinformationisupdatedandTLVsaresenttoneighboring
networkdevicesbytheLLDPagent.Theminimumsettingforthistimermustbefourtimesthevalueof
lldp txdelay.
Forexample,thisisavalidconfiguration:
n lldp timer=16
n lldp txdelay=4
And,thisisaninvalidconfiguration:
n lldp timer=5
n lldp txdelay=2
Whencopyingasavedconfigurationtotherunningconfiguration,thevalueforlldp timerisappliedbeforethe
valueoflldp txdelay.Thiscanresultinaconfigurationerrorifthesavedconfigurationhasavalueoflldp
timerthatisnotfourtimesthevalueoflldp txdelayintherunningconfiguration.
Forexample,ifthesavedconfigurationhasthesettings:
| n lldp timer=16  |     |     |
| ---------------- | --- | --- |
| n lldp txdelay=4 |     |     |
Andtherunningconfigurationhasthesettings:
| lldp timer=30 |     |     |
| ------------- | --- | --- |
n
| n lldp txdelay=7 |     |     |
| ---------------- | --- | --- |
Thenyouwillseeanerrorindicatingthatcertainconfigurationsettingscouldnotbeapplied,andyouwillhaveto
manuallyadjustthevalueoflldp txdelayintherunningconfiguration.
Thenoformofthiscommandsetstheupdateintervaltoitsdefaultvalueof30seconds.
| Parameter |     | Description                                           |
| --------- | --- | ----------------------------------------------------- |
| <TIME>    |     | Specifiestheupdateinterval(inseconds).Range:5to32768. |
Default:30.
272
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Examples
Settingtheupdateintervalto7seconds:
switch(config)#
|     | lldp timer | 7   |
| --- | ---------- | --- |
Settingtheupdateintervaltothedefaultvalueof30seconds:
| switch(config)# | no lldp | timer |
| --------------- | ------- | ----- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptransmit
lldp transsmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionisenabledon
allactiveinterfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablestransmissionofLLDPinformationonaninterface.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | lldp      | transsmit |
DisablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | no lldp   | transsmit |
EnablingLLDPtransmissionontheOOBMinterface:
Devicediscoveryandconfiguration|273

| switch(config)# | interface | mgmt |
| --------------- | --------- | ---- |
switch(config-if)#
|     | lldp | transsmit |
| --- | ---- | --------- |
DisablingLLDPtransmissionontheOOBMinterface:
| switch(config)#    | interface | mgmt      |
| ------------------ | --------- | --------- |
| switch(config-if)# | no lldp   | transsmit |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptxdelay
| lldp txdelay | <TIME> |     |
| ------------ | ------ | --- |
no lldp txdelay
Description
Setstheamountoftime(inseconds)towaitbeforesendingLLDPinformationfromanyinterface.The
maximumvaluefortxdelayis25%ofthevalueoflldp tx timer.
Thenoformofthiscommandsetsthedelaytimetoitsdefaultvalueof2seconds.
Parameter Description
<TIME>
Specifiesthedelaytimeinseconds.Range:0to10.Default:2.
Examples
Settingthedelaytimeto8seconds:
| switch(config)# | lldp txdelay | 8   |
| --------------- | ------------ | --- |
Settingthedelaytimetothedefaultvalueof2seconds:
| switch(config)# | no lldp | txdelay |
| --------------- | ------- | ------- |
CommandHistory
274
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptrapenable
| lldp trap enable |        |     |     |     |
| ---------------- | ------ | --- | --- | --- |
| no lldp trap     | enable |     |     |     |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenotrequired
tobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | lldp trap | enable |     |
| --------------- | --- | --------- | ------ | --- |
EnablingLLDPtrapgenerationoninterfacelevel:
switch(config-if)#
|     |     | lldp | trap | enable |
| --- | --- | ---- | ---- | ------ |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp | trap | enable |
| --------------- | --- | ------- | ---- | ------ |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | no lldp | trap | enable |
| ------------------ | --- | ------- | ---- | ------ |
DisplayingLLDPglobalconfiguration:
| switch# | show lldp | configuration |     |     |
| ------- | --------- | ------------- | --- | --- |
Devicediscoveryandconfiguration|275

| LLDP Global | Configuration |     |     |
| ----------- | ------------- | --- | --- |
=========================
| LLDP Enabled  |                 | : No |     |
| ------------- | --------------- | ---- | --- |
| LLDP Transmit | Interval        | : 30 |     |
| LLDP Hold     | Time Multiplier | : 4  |     |
| LLDP Transmit | Delay Interval  | : 2  |     |
| LLDP Reinit   | Timer Interval  | : 2  |     |
| LLDP Trap     | Enabled         | : No |     |
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
| LLDP Enabled |     | : Yes |     |
| ------------ | --- | ----- | --- |
276
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| LLDP | Transmit | Interval        |          | : 30  |     |     |
| ---- | -------- | --------------- | -------- | ----- | --- | --- |
| LLDP | Hold     | Time Multiplier |          | : 4   |     |     |
| LLDP | Transmit | Delay           | Interval | : 2   |     |     |
| LLDP | Reinit   | Timer           | Interval | : 2   |     |     |
| LLDP | Trap     | Enabled         |          | : Yes |     |     |
| LLDP | Port     | Configuration   |          |       |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt |     | Yes |     |     | Yes | Yes |
| ---- | --- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show lldpconfiguration
| show lldp | configuration |     | [<INTERFACE-ID>][vsx-peer] |     |     |     |
| --------- | ------------- | --- | -------------------------- | --- | --- | --- |
Description
ShowsLLDPconfigurationsettingsforallinterfacesoraspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingconfigurationsettingsforallinterfaces:
| switch# | show   | lldp          | configuration |     |     |     |
| ------- | ------ | ------------- | ------------- | --- | --- | --- |
| LLDP    | Global | Configuration |               |     |     |     |
=========================
| LLDP | Enabled  |          |     | : No |     |     |
| ---- | -------- | -------- | --- | ---- | --- | --- |
| LLDP | Transmit | Interval |     | : 30 |     |     |
Devicediscoveryandconfiguration|277

| LLDP Hold     | Time Multiplier | : 4  |     |
| ------------- | --------------- | ---- | --- |
| LLDP Transmit | Delay Interval  | : 2  |     |
| LLDP Reinit   | Timer Interval  | : 2  |     |
| LLDP Trap     | Enabled         | : No |     |
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
Thisexampleshowsconfigurationsettingsforinterface1/1/1.
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
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
278
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldpconfiguration |               |     | mgmt |     |     |     |
| ---------------------- | ------------- | --- | ---- | --- | --- | --- |
| show lldp              | configuration |     | mgmt |     |     |     |
Description
ShowsLLDPconfigurationsettingsfortheOOBMinterface.
Example
Showingconfigurationsettingsforallinterfaces:
| switch# | show   | lldp          | configuration |     | mgmt |     |
| ------- | ------ | ------------- | ------------- | --- | ---- | --- |
| LLDP    | Global | Configuration |               |     |      |     |
=========================
| LLDP | Enabled  |                 |          | :   | Yes |     |
| ---- | -------- | --------------- | -------- | --- | --- | --- |
| LLDP | Transmit | Interval        |          | :   | 30  |     |
| LLDP | Hold     | Time Multiplier |          | :   | 4   |     |
| LLDP | Transmit | Delay           | Interval | :   | 2   |     |
| LLDP | Reinit   | Timer           | Interval | :   | 2   |     |
| LLDP | Trap     | Enabled         |          | :   | Yes |     |
| LLDP | Port     | Configuration   |          |     |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt |     | Yes |     |     | Yes | Yes |
| ---- | --- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
6300 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
show lldplocal-device
| show lldp | local-device[vsx-peer] |     |     |     |     |     |
| --------- | ---------------------- | --- | --- | --- | --- | --- |
Description
Devicediscoveryandconfiguration|279

ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsareconfigured
onanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDsonaccess
interfaces.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingglobalLLDPinformationonly(allportsincludingOOBMportareadministrativelydown):
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
280
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

switch# show lldp local-device

Global Data
===========

Chassis-ID
System Name
System Description
Management Address
Capabilities Available : Bridge, Router
: Bridge, Router
Capabilities Enabled
: 120
TTL

: 1c:98:ec:e3:45:00
: switch
: Aruba
: 192.168.10.1

Port Based Data
===============

Port-ID
Port-Desc
Port VLAN ID
Parent Interface : interface 1/1/11

: 1/1/11
: "1/1/11"
: 100

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

show lldp neighbor-info

show lldp neighbor-info [<INTERFACE-NAME>][vsx-peer]

Description

Displays information about neighboring devices for all interfaces or for a specific interface. The information
displayed varies depending on the type of neighbor connected and the type of TLVs sent by the neighbor.

Parameter

<INTERFACE-NAME>

vsx-peer

Examples

Description

Specifies the interface for which to show information for
neighboring devices. Use the format member/slot/port (for
example, 1/3/1).

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

On the 6400 Switch Series, interface identification differs.

Device discovery and configuration | 281

ShowingLLDPinformationforallinterfaces:
| switch# show  | lldp neighbor-info |     |     |     |
| ------------- | ------------------ | --- | --- | --- |
| LLDP Neighbor | Information        |     |     |     |
=========================
| Total Neighbor | Entries          | : 3     |           |              |
| -------------- | ---------------- | ------- | --------- | ------------ |
| Total Neighbor | Entries Deleted  | : 0     |           |              |
| Total Neighbor | Entries Dropped  | : 0     |           |              |
| Total Neighbor | Entries Aged-Out | : 0     |           |              |
| LOCAL-PORT     | CHASSIS-ID       | PORT-ID | PORT-DESC | TTL SYS-NAME |
--------------------------------------------------------------------------------
| 1/1/1  | 70:72:cf:a4:7d:50 | 1/1/1  | 1/1/1  | 32 switch  |
| ------ | ----------------- | ------ | ------ | ---------- |
| 1/1/2  | 48:0f:cf:af:73:80 | 1/1/2  | 1/1/2  | 120 switch |
| 1/1/46 | 48:0f:cf:af:73:80 | 1/1/46 | 1/1/46 | 120 switch |
| mgmt   | 48:0f:cf:af:73:80 | mgmt   | mgmt   | 120 switch |
Showinginformationforinterface1/3/1whenithasonlyoneswitchconnectedasaneighbor:
| switch# show | lldp neighbor-info | 1/3/1                  |     |     |
| ------------ | ------------------ | ---------------------- | --- | --- |
| Port         |                    | : 1/1/1                |     |     |
| Neighbor     | Entries            | : 1                    |     |     |
| Neighbor     | Entries Deleted    | : 0                    |     |     |
| Neighbor     | Entries Dropped    | : 0                    |     |     |
| Neighbor     | Entries Aged-Out   | : 0                    |     |     |
| Neighbor     | Chassis-Name       | : HP-3800-24G-PoEP-2XG |     |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor             | Chassis-ID         | : 10:60:4b:39:3e:80 |        |     |
| -------------------- | ------------------ | ------------------- | ------ | --- |
| Neighbor             | Management-Address | : 192.168.1.1       |        |     |
| Chassis Capabilities | Available          | : Bridge,           | Router |     |
| Chassis Capabilities | Enabled            | : Bridge            |        |     |
| Neighbor             | Port-ID            | : 1/1/1             |        |     |
| Neighbor             | Port-Desc          | : 1/1/1             |        |     |
| Neighbor             | Port VLAN ID       | :                   |        |     |
| TTL                  |                    | : 120               |        |     |
Showinginformationforinterface1/3/10whentheneighborsendsaDOT3powerTLV:
| switch# show | lldp neighbor-info | 1/3/10              |     |     |
| ------------ | ------------------ | ------------------- | --- | --- |
| Port         |                    | : 1/3/10            |     |     |
| Neighbor     | Entries            | : 1                 |     |     |
| Neighbor     | Entries Deleted    | : 0                 |     |     |
| Neighbor     | Entries Dropped    | : 0                 |     |     |
| Neighbor     | Entries Aged-Out   | : 0                 |     |     |
| Neighbor     | Chassis-Name       | : 84:d4:7e:ce:5d:68 |     |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor             | Chassis-ID         | : 84:d4:7e:ce:5d:68 |      |     |
| -------------------- | ------------------ | ------------------- | ---- | --- |
| Neighbor             | Management-Address | : 169.254.41.250    |      |     |
| Chassis Capabilities | Available          | : Bridge,           | WLAN |     |
| Chassis Capabilities | Enabled            | : WLAN              |      |     |
| Neighbor             | Port-ID            | : 84:d4:7e:ce:5d:68 |      |     |
| Neighbor             | Port-Desc          | : eth0              |      |     |
| TTL                  |                    | : 120               |      |     |
| Neighbor             | Port VLAN ID       | :                   |      |     |
| Neighbor             | PoE information    | : DOT3              |      |     |
| Neighbor             | Power Type         | : TYPE2             | PD   |     |
282
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Neighbor      | Power |       | Priority    |      | : Unkown  |     |
| ------------- | ----- | ----- | ----------- | ---- | --------- | --- |
| Neighbor      | Power |       | Source      |      | : Primary |     |
| PD Requested  |       | Power | Value       |      | : 25.0    | W   |
| PSE Allocated |       | Power | Value:      | 25.0 | W         |     |
| Neighbor      | Power |       | Supported   |      | : Yes     |     |
| Neighbor      | Power |       | Enabled     |      | : Yes     |     |
| Neighbor      | Power |       | Class       |      | : 5       |     |
| Neighbor      | Power |       | Paircontrol |      | : No      |     |
| PSE Power     |       | Pairs |             |      | : Signal  |     |
Showinginformationforinterface1/1/1whenithasmultipleneighbors(displaysamaximumoffour):
switch#
|          | show         | lldp | neighbor-info |     | 1/1/1    |     |
| -------- | ------------ | ---- | ------------- | --- | -------- | --- |
| Port     |              |      |               |     | : 1/1/1  |     |
| Neighbor | Entries      |      |               |     | : 4      |     |
| Neighbor | Entries      |      | Deleted       |     | : 0      |     |
| Neighbor | Entries      |      | Dropped       |     | : 0      |     |
| Neighbor | Entries      |      | Aged-Out      |     | : 0      |     |
| Neighbor | Chassis-Name |      |               |     | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           |     | : 1c:98:ec:fe:25:00 |        |
| -------- | ------------------ | ---- | --------- | --- | ------------------- | ------ |
| Neighbor | Management-Address |      |           |     | : 10.1.1.2          |        |
| Chassis  | Capabilities       |      | Available |     | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   |     | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           |     | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           |     | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        |     | :                   |        |
| TTL      |                    |      |           |     | : 120               |        |
| Neighbor | Chassis-Name       |      |           |     | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           |     | : 1c:98:ec:fe:25:01 |        |
| -------- | ------------------ | ---- | --------- | --- | ------------------- | ------ |
| Neighbor | Management-Address |      |           |     | : 10.1.1.3          |        |
| Chassis  | Capabilities       |      | Available |     | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   |     | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           |     | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           |     | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        |     | :                   |        |
| TTL      |                    |      |           |     | : 120               |        |
| Neighbor | Chassis-Name       |      |           |     | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           |     | : 1c:98:ec:fe:25:02 |        |
| -------- | ------------------ | ---- | --------- | --- | ------------------- | ------ |
| Neighbor | Management-Address |      |           |     | : 10.1.1.4          |        |
| Chassis  | Capabilities       |      | Available |     | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   |     | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           |     | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           |     | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        |     | : 50                |        |
| TTL      |                    |      |           |     | : 120               |        |
| Neighbor | Chassis-Name       |      |           |     | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           |     | : 1c:98:ec:fe:25:03 |        |
| -------- | ------------------ | ---- | --------- | --- | ------------------- | ------ |
| Neighbor | Management-Address |      |           |     | : 10.1.1.5          |        |
| Chassis  | Capabilities       |      | Available |     | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   |     | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           |     | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           |     | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        |     | : 100               |        |
| TTL      |                    |      |           |     | : 120               |        |
Showingneighborinformationforinterface1/3/2whenithasEEEenabledandsuccessfullyauto-
negotiated:
Devicediscoveryandconfiguration|283

| switch#  | show         | lldp                | neighbor-info | 1/3/2               |        |                 |
| -------- | ------------ | ------------------- | ------------- | ------------------- | ------ | --------------- |
| Port     |              |                     |               | : 1/3/2             |        |                 |
| Neighbor |              | Entries             |               | : 1                 |        |                 |
| Neighbor |              | Entries             | Deleted       | : 1                 |        |                 |
| Neighbor |              | Entries             | Dropped       | : 0                 |        |                 |
| Neighbor |              | Entries             | Aged-Out      | : 1                 |        |                 |
| Neighbor |              | Chassis-Name        |               | : BLDG01-F1-6300    |        |                 |
| Neighbor |              | Chassis-Description |               | : Aruba             | JL668A | FL.10.07.0001BN |
| Neighbor |              | Chassis-ID          |               | : 88:3a:30:92:a5:c0 |        |                 |
| Neighbor |              | Management-Address  |               | : 10.6.9.15         |        |                 |
| Chassis  | Capabilities |                     | Available     | : Bridge,           | Router |                 |
| Chassis  | Capabilities |                     | Enabled       | : Bridge,           | Router |                 |
| Neighbor |              | Port-ID             |               | : 1/1/1             |        |                 |
| Neighbor |              | Port-Desc           |               | : 1/1/1             |        |                 |
| Neighbor |              | Port VLAN           | ID            | : 1                 |        |                 |
| TTL      |              |                     |               | : 120               |        |                 |
| Neighbor |              | Mac-Phy             | details       |                     |        |                 |
| Neighbor |              | Auto-neg            | Supported     | : true              |        |                 |
| Neighbor |              | Auto-Neg            | Enabled       | : true              |        |                 |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor |     | MAU type        |      | : 1000  | BASETFD |     |
| -------- | --- | --------------- | ---- | ------- | ------- | --- |
| Neighbor |     | EEE information |      | : DOT3  |         |     |
| Neighbor |     | TX Wake         | time | : 17 us |         |     |
| Neighbor |     | RX Wake         | time | : 17 us |         |     |
| Neighbor |     | Fallback        | time | : 17 us |         |     |
| Neighbor |     | TX Echo         | time | : 17 us |         |     |
| Neighbor |     | RX Echo         | time | : 17 us |         |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show lldpneighbor-infodetail
| show lldp | neighbor-info |     | detail | [vsx-peer] |     |     |
| --------- | ------------- | --- | ------ | ---------- | --- | --- |
Description
ShowsdetailedLLDPneighborinformationforallLLDPneighborconnectedinterfaces.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
284
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- |

Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingdetailedLLDPinformationforallinterfaces:
| switch# show  | lldp neighbor-info | detail |     |
| ------------- | ------------------ | ------ | --- |
| LLDP Neighbor | Information        |        |     |
=========================
| Total Neighbor | Entries          | : 6 |     |
| -------------- | ---------------- | --- | --- |
| Total Neighbor | Entries Deleted  | : 2 |     |
| Total Neighbor | Entries Dropped  | : 0 |     |
| Total Neighbor | Entries Aged-Out | : 2 |     |
--------------------------------------------------------------------------------
| Port                         |           | : 1/1/1             |        |
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
| Neighbor Port-ID             |           | : 1/1/4             |        |
| Neighbor Port-Desc           |           | : 1/1/4             |        |
| Neighbor Port                | VLAN ID   | : 1                 |        |
| TTL                          |           | : 120               |        |
| Neighbor Mac-Phy             | details   |                     |        |
| Neighbor Auto-neg            | Supported | : true              |        |
| Neighbor Auto-Neg            | Enabled   | : true              |        |
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
| TTL                          |           | : 120               |        |
| Neighbor Mac-Phy             | details   |                     |        |
| Neighbor Auto-neg            | Supported | : true              |        |
| Neighbor Auto-Neg            | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor MAU | type | : 1000 | BASETFD |
| ------------ | ---- | ------ | ------- |
Devicediscoveryandconfiguration|285

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
| Neighbor MAU | type | : 1000 | BASETFD |
| ------------ | ---- | ------ | ------- |
--------------------------------------------------------------------------------
| Port                         |          | : 1/1/47            |     |
| ---------------------------- | -------- | ------------------- | --- |
| Neighbor Entries             |          | : 1                 |     |
| Neighbor Entries             | Deleted  | : 0                 |     |
| Neighbor Entries             | Dropped  | : 0                 |     |
| Neighbor Entries             | Aged-Out | : 0                 |     |
| Neighbor Chassis-Name        |          | : 6300              |     |
| Neighbor Chassis-Description |          | : Aruba             | ... |
| Neighbor Chassis-ID          |          | : 38:11:17:1a:d5:00 |     |
| Neighbor Management-Address  |          | : 38:11:17:1a:d5:00 |     |
| Chassis Cap                  |          |                     |     |
CommandHistory
286
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show lldpneighbor-infomgmt
| show lldp | neighbor-info |     | mgmt |     |     |
| --------- | ------------- | --- | ---- | --- | --- |
Description
DisplaysinformationaboutneighboringdevicesconnectedtotheOOBMinterface.
Examples
ShowingLLDPinformationfortheOOBMinterface:
| switch#  | show         | lldp | neighbor-info | mgmt                   |     |
| -------- | ------------ | ---- | ------------- | ---------------------- | --- |
| Port     |              |      |               | : mgmt                 |     |
| Neighbor | Entries      |      |               | : 1                    |     |
| Neighbor | Entries      |      | Deleted       | : 0                    |     |
| Neighbor | Entries      |      | Dropped       | : 0                    |     |
| Neighbor | Entries      |      | Aged-Out      | : 0                    |     |
| Neighbor | Chassis-Name |      |               | : HP-3800-24G-PoEP-2XG |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor | Chassis-ID         |      |           | : 10:60:4b:39:3e:80 |        |
| -------- | ------------------ | ---- | --------- | ------------------- | ------ |
| Neighbor | Management-Address |      |           | : 192.168.1.1       |        |
| Chassis  | Capabilities       |      | Available | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   | : Bridge            |        |
| Neighbor | Port-ID            |      |           | : mgmt              |        |
| Neighbor | Port-Desc          |      |           | : mgmt              |        |
| Neighbor | Port               | VLAN | ID        | :                   |        |
| TTL      |                    |      |           | : 120               |        |
ShowingLLDPinformationfortheOOBMinterfacewhentherearefourneighbors:
| switch#  | show         | lldp | neighbor-info | mgmt     |     |
| -------- | ------------ | ---- | ------------- | -------- | --- |
| Port     |              |      |               | : mgmt   |     |
| Neighbor | Entries      |      |               | : 4      |     |
| Neighbor | Entries      |      | Deleted       | : 0      |     |
| Neighbor | Entries      |      | Dropped       | : 0      |     |
| Neighbor | Entries      |      | Aged-Out      | : 0      |     |
| Neighbor | Chassis-Name |      |               | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |     |           | : 1c:98:ec:fe:25:00 |        |
| -------- | ------------------ | --- | --------- | ------------------- | ------ |
| Neighbor | Management-Address |     |           | : 10.1.1.2          |        |
| Chassis  | Capabilities       |     | Available | : Bridge,           | Router |
| Chassis  | Capabilities       |     | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |     |           | : 1/1/1             |        |
Devicediscoveryandconfiguration|287

| Neighbor | Port-Desc    |      |     | : 1/1/1  |     |
| -------- | ------------ | ---- | --- | -------- | --- |
| Neighbor | Port         | VLAN | ID  | :        |     |
| TTL      |              |      |     | : 120    |     |
| Neighbor | Chassis-Name |      |     | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           | : 1c:98:ec:fe:25:01 |        |
| -------- | ------------------ | ---- | --------- | ------------------- | ------ |
| Neighbor | Management-Address |      |           | : 10.1.1.3          |        |
| Chassis  | Capabilities       |      | Available | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        | :                   |        |
| TTL      |                    |      |           | : 120               |        |
| Neighbor | Chassis-Name       |      |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           | : 1c:98:ec:fe:25:02 |        |
| -------- | ------------------ | ---- | --------- | ------------------- | ------ |
| Neighbor | Management-Address |      |           | : 10.1.1.4          |        |
| Chassis  | Capabilities       |      | Available | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        | :                   |        |
| TTL      |                    |      |           | : 120               |        |
| Neighbor | Chassis-Name       |      |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |      |           | : 1c:98:ec:fe:25:03 |        |
| -------- | ------------------ | ---- | --------- | ------------------- | ------ |
| Neighbor | Management-Address |      |           | : 10.1.1.5          |        |
| Chassis  | Capabilities       |      | Available | : Bridge,           | Router |
| Chassis  | Capabilities       |      | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |      |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |      |           | : 1/1/1             |        |
| Neighbor | Port               | VLAN | ID        | :                   |        |
| TTL      |                    |      |           | : 120               |        |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
6300 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
show lldpstatistics
| show lldp | statistics |     | [<INTERFACE-ID>][vsx-peer] |     |     |
| --------- | ---------- | --- | -------------------------- | --- | --- |
Description
ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
288
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingglobalstatisticsforallinterfaces:
| switch#     | show lldp statistics |     |     |     |
| ----------- | -------------------- | --- | --- | --- |
| LLDP Global | Statistics           |     |     |     |
======================
| Total Packets | Transmitted  |           | : 19 |     |
| ------------- | ------------ | --------- | ---- | --- |
| Total Packets | Received     |           | : 19 |     |
| Total Packets | Received And | Discarded | : 0  |     |
| Total TLVs    | Unrecognized |           | : 0  |     |
| LLDP Port     | Statistics   |           |      |     |
====================
| PORT-ID | TX-PACKETS | RX-PACKETS | RX-DISCARDED | TLVS-UNKNOWN |
| ------- | ---------- | ---------- | ------------ | ------------ |
-------------------------------------------------------------------------
| 1/1/1 | 7   | 7   | 0   | 0   |
| ----- | --- | --- | --- | --- |
| 1/1/2 | 7   | 7   | 0   | 0   |
| 1/1/3 | 0   | 0   | 0   | 0   |
| 1/1/4 | 0   | 0   | 0   | 0   |
| 1/1/5 | 0   | 0   | 0   | 0   |
...
| mgmt | 5   | 5   | 0   | 0   |
| ---- | --- | --- | --- | --- |
```
Showingstatisticsforinterface1/1/1:
| switch# | show lldp statistics | 1/1/1 |     |     |
| ------- | -------------------- | ----- | --- | --- |
LLDP Statistics
===============
| Port Name |                           |     | : 1/1/1 |     |
| --------- | ------------------------- | --- | ------- | --- |
| Packets   | Transmitted               |     | : 159   |     |
| Packets   | Received                  |     | : 163   |     |
| Packets   | Received And Discarded    |     | : 0     |     |
| Packets   | Received And Unrecognized |     | : 0     |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
Devicediscoveryandconfiguration|289

CommandInformation
| Platforms |     | Commandcontext |     | Authority |
| --------- | --- | -------------- | --- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show lldpstatisticsmgmt
| show lldp | statistics | mgmt |     |     |
| --------- | ---------- | ---- | --- | --- |
Description
ShowsLLDPstatisticsfortheOOBMinterface.
Example
ShowingLLDPstatisticsfortheOOBMinterface:
| switch# | show       | lldp statistics | mgmt |     |
| ------- | ---------- | --------------- | ---- | --- |
| LLDP    | Statistics |                 |      |     |
===============
| Port    | Name        |                  |     | : mgmt |
| ------- | ----------- | ---------------- | --- | ------ |
| Packets | Transmitted |                  |     | : 20   |
| Packets | Received    |                  |     | : 23   |
| Packets | Received    | And Discarded    |     | : 0    |
| Packets | Received    | And Unrecognized |     | : 0    |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |
| --------- | --- | -------------- | --- | --------- |
6300 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show lldptlv
| show lldp | tlv[vsx-peer] |     |     |     |
| --------- | ------------- | --- | --- | --- |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
290
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#         | show lldp | tlv |     |
| --------------- | --------- | --- | --- |
| TLVs Advertised |           |     |     |
===============
| Management          | Address |     |     |
| ------------------- | ------- | --- | --- |
| Port Description    |         |     |     |
| Port VLAN-ID        |         |     |     |
| System Capabilities |         |     |     |
| System Description  |         |     |     |
| System Name         |         |     |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| Cisco Discovery |     | Protocol | (CDP) |
| --------------- | --- | -------- | ----- |
CiscoDiscoveryProtocol(CDP)isaproprietarylayer2protocolsupportedbymostCiscodevices.Itisused
toexchangeinformation,suchassoftwareversion,devicecapabilities,andvoiceVLANinformation,
betweendirectlyconnecteddevices,suchasaVoIPphoneandaswitch.
CDP support
Bydefault,CDPisenabledoneachactiveswitchport.Thisisaread-onlycapability,whichmeanstheswitch
canreceiveandstoreinformationaboutadjacentCDPdevices,butdoesnotgenerateCDPpackets(except
whencommunicatingwithCiscoIPphones.)
TheswitchsupportsCDPv2onlyanddoesnotsupportSNMPMIBtraps.
WhenaCDP-enabledportreceivesaCDPpacketfromanotherCDPdevice,itentersdataforthatdeviceinto
theCDPNeighborstable,alongwiththeportnumberonwhichthedatawasreceived.Itdoesnotforward
thepacket.Theswitchalsoperiodicallypurgesthetableofanyentriesthathaveexpired.(Theholdtimefor
anydataentryintheswitchCDPNeighborstableisconfiguredinthedevicetransmittingtheCDPpacket
andcannotbecontrolledintheswitchreceivingthepacket.)AswitchreviewsthelistofCDPneighbor
entrieseverythreesecondsandpurgesanyexpiredentries.
Devicediscoveryandconfiguration|291

Support for legacy Cisco IP phones

Autoconfiguration of legacy Cisco IP phones for tagged voice VLAN support requires CDPv2.

On initial boot-up, and sometimes periodically, a Cisco phone queries the switch and advertises information
about itself using CDPv2. When the switch receives the VoIP VLAN Query TLV (type 0x0f) from the phone,
the switch immediately responds with the voice VLAN ID in a reply packet using the VoIP VLAN Reply TLV
(type 0x0e). This enables the Cisco phone to boot properly and send traffic on the advertised voice VLAN ID.

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

Configures CDP support globally on all active interfaces or on a specific interface. By default, CDP is enabled
on all active interfaces.

When CDP is enabled, the switch adds entries to its CDP Neighbors table for any CDP packets it receives
from neighboring CDP devices.

When CDP is disabled, the CDP Neighbors table is cleared and the switch drops all inbound CDP packets
without entering the data in the CDP Neighbors table.

The no form of this command disables CDP support globally on all active interfaces or on a specific interface.

Examples

Enabling CDP globally:

switch(config)# cdp

Disabling CDP globally:

switch(config)# no cdp

Enabling CDP on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# cdp

Disabling CDP on interface 1/1/1:

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

292

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|     | no  | cdp |     |
| --- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if |     | forthiscommand. |
| --- | --------- | --- | --------------- |
clear cdpcounters
| clear cdp counters |     |     |     |
| ------------------ | --- | --- | --- |
Description
ClearsCDPcounters.
Examples
ClearingCDPcounters:
| switch(config) | clear cdp | counters |     |
| -------------- | --------- | -------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
clear cdpneighbor-info
| clear cdp neighbor-info |     |     |     |
| ----------------------- | --- | --- | --- |
Description
ClearsCDPneighborinformation.
Examples
ClearingCDPneighborinformation:
Devicediscoveryandconfiguration|293

| switch(config) | clear neighbor-info |     |
| -------------- | ------------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show cdp
show cdp
Description
ShowsCDPinformationforallinterfaces.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingCDPinformation:
| switch(config)# | show cdp    |     |
| --------------- | ----------- | --- |
| CDP Global      | Information |     |
======================
| CDP      | : Enabled          |     |
| -------- | ------------------ | --- |
| CDP Mode | : Rx only          |     |
| CDP Hold | Time : 180 seconds |     |
| Port     | CDP                |     |
| -------- | --------------     |     |
| 1/1/1    | Enabled            |     |
| 1/1/2    | Enabled            |     |
| 1/1/3    | Enabled            |     |
| 1/1/4    | Enabled            |     |
| 1/1/5    | Enabled            |     |
| 1/1/6    | Enabled            |     |
| 1/1/7    | Enabled            |     |
| 1/1/8    | Enabled            |     |
| 1/1/9    | Enabled            |     |
| 1/1/10   | Enabled            |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
294
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show cdpneighbor-info
| show cdp neighbor-info |     | <INTERFACE-ID> |     |     |
| ---------------------- | --- | -------------- | --- | --- |
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
| Parameter      |     |     | Description                                   |     |
| -------------- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |     |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingallCDPneighborinformation:
| switch(config)# | show   | cdp neighbor-info |          |            |
| --------------- | ------ | ----------------- | -------- | ---------- |
| Port            | Device | ID                | Platform | Capability |
-------------------------------------------------------------------------------
| 1/1/1 | myswitch |     | cisco WS-C2950-12 | SI  |
| ----- | -------- | --- | ----------------- | --- |
ShowingCDPinformationforinterface1/1/1:
| switch(config)# | show    | cdp neighbor-info   | 1/1/1 |     |
| --------------- | ------- | ------------------- | ----- | --- |
| Local Port      | : 1/1/1 |                     |       |     |
| MAC             |         | : 3c:a8:2a:7b:6b:2b |       |     |
| Device ID       |         | : SEPd4adbd2a30d6   |       |     |
| Address         |         | : 2.71.0.230        |       |     |
| Platform        |         | : Cisco IP Phone    | 3905  |     |
| Duplex          |         | : full              |       |     |
| Capability      |         | : host              |       |     |
| Voice VLAN      | Support | : Yes               |       |     |
| Neighbor        | Port-ID | : Port 1            |       |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show cdptraffic
Devicediscoveryandconfiguration|295

show cdp neighbor-info
Description
ShowsCDPstatisticsforeachinterface.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingCDPtrafficstatistics:
| switch(config)# | show | cdp traffic |     |     |     |
| --------------- | ---- | ----------- | --- | --- | --- |
CDP Statistics
====================
| Port | Transmitted | Frames | Received Frames | Discarded | Frames |
| ---- | ----------- | ------ | --------------- | --------- | ------ |
--------------------------------------------------------------------------------
| 1/1/1 | 0   |     | 4   | 0   |     |
| ----- | --- | --- | --- | --- | --- |
| 1/1/2 | 0   |     | 0   | 0   |     |
| 1/1/3 | 0   |     | 2   | 0   |     |
| 1/1/4 | 0   |     | 0   | 0   |     |
| 1/1/5 | 0   |     | 0   | 0   |     |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
296
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- |

Chapter 17

Zero Touch Provisioning

Zero Touch Provisioning

Zero Touch Provisioning (ZTP) enables the auto-configuration of factory default switches without a network
administrator onsite.

When a switch is booted from its factory default configuration, ZTP autoprovisions the switch by
automatically downloading and installing a firmware file, a configuration file, or both. With ZTP, even a
nontechnical user (for example: a store manager in a retail chain or a teacher in a school) can deploy devices
at a site.

ZTP support
The switch supports standards-based Zero Touch Provisioning (ZTP) operations as follows:

n The switch must be running the factory default configuration.

n The switch can connect to the DHCP server from the OOBM management port.

The switch can connect to the DHCP server from either the OOBM management port, or a data port on
the default VLAN.

n ZTP operations are supported over IPv4 connections only. IPv6 connections are not supported for ZTP

operations.

n You must configure the DHCP server to provide a standards-based ZTP server solution. Options and
features that are specific to Network Management Solution (NMS) tools, such as AirWave, are not
supported.

o Aruba Central on-premise can manage AOS-CX switches on supported models through DHCP ZTP

using two approaches:

l On the DHCP server, configure DHCP option-60 as "ArubaInstantAP" 90 and provide the value in
option-43 in the format <group-details>, <aruba-central-on-prem-ip-or-fqdn>, <shared-token>.

l On the DHCP server, configure DHCP option-60 as HPE vendor VCI and provide the value in

option-43 in the tag-length-value (TLV) format. Next, enter the Aruba Central on-premise fully
qualified domain name (FQDN) or IPv4 address as the value for sub-option code 146 using the
format: <group-details>, <aruba-central-on-prem-ip-or-fqdn>, <shared-token>.

o Supported DHCP options are:

DHCP option

Description

43

43 suboption 144

43 suboption 145

Vendor Specific Information

Name of the configuration file

Name of the firmware image file

43 suboption 146

FQDN or IPv4 address of the Aruba Central on-premise server

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

297

DHCP option

43 suboption 148

60

66

67

Description

FQDN or IPv4 address of the HTTP Proxy

Vendor Class Identifier (VCI)

IPv4 address of the TFTP server (Specifying a host name instead
of an IP address is not supported.)

Name of the configuration file (Option 43 suboption 144 takes
precedence over this option.)

n The configuration file is a text file or JSON file that becomes the startup and running configuration on the

switch after the ZTP operation is complete. The configuration can be in CLI or in JSON format.

n When the switch is started using the factory default configuration, the ZTP operation is started

automatically and is active until any running configuration of the switch is modified. There is no CLI
command required to start the operation.

The switch supports the following standards:

n RFC 2131, Dynamic Host Configuration Protocol.

n RFC 2132, DHCP Options and BOOTP Vendor Extensions. Support is limited to the options listed in the

table "Supported DHCP options for ZTP on AOS-CX."

Hewlett Packard Enterprise recommends that you implement ZTP in a secure and private environment. Any
public access can compromise the security of the switch, as follows:

n ZTP is enabled only in the factory default configuration of the switch, DHCP snooping is not enabled. The

Rogue DHCP server must be manually managed.

n The DHCP offer is in plain data without encryption.

Setting up ZTP on a trusted network
The following procedure is an overview of setting up a Zero Touch Provisioning (ZTP) environment to
provision newly installed switches automatically. The procedure is intended for network administrators who
are familiar with automatically provisioning switches in a network, and does not provide detailed
information about configuring or managing switches.

Procedure

1. For each switch model to be provisioned using ZTP, do the following:

a. Obtain the switch firmware image file.
b. Prepare the switch configuration file. The configuration file becomes the running configuration

and the startup configuration on the switch.

2. Set up a TFTP server and record its IP address. The address is required when you set up the DHCP
server. The switch must be able to reach the TFTP server and DHCP server, either on the same
subnet, or on a remote subnet via DHCP relay.

Switches support provisioning through a network connected to a data port or through a network
connected to the management port.

Zero Touch Provisioning | 298

3. Publish the configuration files and image files to the TFTP server. You need to know the locations of

the files and the IP address of the TFTP server when you set up the vendor class options on the DHCP
server.

4. On the DHCP server, set up vendor classes for each switch model you plan to provision. To do this

you need the following information:
n The IP address of the TFTP server. Using a host name is not supported.

n The path to the switch configuration and firmware image files on the TFTP server.

n The vendor class identifier (VCI) for each switch model.

You can obtain the VCI by entering the show dhcp client vendor-class-identifier command
from a switch CLI command prompt in the manager context. The VCI is the text string in the response
that starts with Aruba.

For example:

switch# show dhcp client vendor-class-identifier
Vendor Class Identifier: Aruba xxxxx xxxx

Where x indicates the switch model number.

5. At the installation site, provide the switch installer with a Cat6 network cable connected to the

network that includes the DHCP and TFTP servers, and information about the switch port to use. The
switch installer plugs the cable into the data port you specify.

The ZTP operation begins when power is applied to the switch after the network cable is installed.

6. Assuming the downloaded configuration includes a way to access the CLI of the switch, you can enter
the following command to show the options offered by the DHCP server and the status of the ZTP
operation:
show ztp information

ZTP process during switch boot

1. The switch boots up with the factory default configuration.

If the ZTP operation detects that the switch configuration is different from the factory default
configuration, the ZTP operation ends. The switch must be configured at the installation site.

2. The switch sends out a DHCP discovery from the management port.

On switches that support ZTP operations on data ports, the switch also sends out a DHCP discovery
from all data ports in the default VLAN.

The switch waits to receive DHCP options indefinitely or until the running configuration is modified. If
a DHCP IP address is received but no DHCP options are received, the switch waits an additional
minute before ending the ZTP operation.

On switches that support ZTP operations on data ports, DHCP options received on the management
port have priority over DHCP options received on data ports:

n If DHCP options are received on the management port before being received on a data port, the

switch processes those options immediately.

n If DHCP options are received on a data port, the switch waits an additional 30 seconds for options
to be received on the management port. If no DHCP options are received on the management
port during those 30 seconds, the switch processes the DHCP options it received on the data port.

After the ZTP operation ends, there is no automatic retry. You can either attempt to boot the switch
with the factory default configuration again, configure the switch at the installation site, or use the

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

299

ZTP force-provision CLI to trigger the ZTP process, ignoring the present running configuration of the
switch.

n Once force-provision is enabled, new DHCP requests are sent from the switch. Disabling force-

provision does not stop the DHCP already in progress, but only changes the switch configuration
status of force-provision.

n If ZTP fails while force-provision is enabled, there is no automatic retry. To retry, ztp force-

provision should be disabled and re-enabled to clear the current ZTP state and send a new DHCP
request. When ztp force-provision is already enabled on the switch, re-enabling it results in no
operation.

n If the DHCP server is configured to provide both ZTP image and configuration options and there is

a non-default startup configuration present on the switch, clearing the non-default startup
configuration before triggering ztp force-provision is recommended. If an image is downloaded
via ZTP, the switch reboots once the image download is complete and ZTP force-provision
configuration is lost, causing ZTP to enter into a failed state. ZTP force-provision will need to be
enabled again to continue the process.

3. The DHCP server responds with an offer containing the following:

n The IPv4 address of the TFTP server

n One or both of the following:

o The name of the firmware image file

o The name of the configuration file

n Aruba Central Location (optional) including the shared token value for the on-premise server

n HTTP Proxy Location (optional)

4.

If a firmware image file is offered, the ZTP operation downloads the image file from the TFTP server
to the switch. If the current switch image and downloaded firmware image version do not match,
then the switch boots with the downloaded image:
n If the image upgrade fails, the switch retains its original firmware image and the ZTP operation

ends with a failed status.

n If the image upgrade succeeds, the ZTP operation is started again after the switch reboots.
Because the downloaded image file matches the image file installed on the switch, the ZTP
operation continues, and checks if a configuration file is offered.

5.

If a configuration file is offered, the ZTP operation downloads the configuration file copies the file to
the running-config and then to the startup-config of the switch:
n If the startup configuration update fails, the switch retains its factory-default running

configuration and the ZTP operation ends with a failed status.

o If the copy operation fails, the ZTP operation ends with a failed status.

o If the copy operation succeeds, the ZTP operation ends successfully.

ZTP VSF switchover support
ZTP status is not synced in the VSF stack. When the VSF stack is formed, configuration changes are applied
on the conductor switch, which is then synced to standby switch. When the switchover is performed on the
VSF stack, the standby becomes the new conductor switch.

As part of the switchover process, the ZTP daemon starts on the new conductor. The status of the ZTP is
failed because there are configuration changes present.

ZTP commands

Zero Touch Provisioning | 300

show ztp information
show ztp information

Description

Shows information about Zero Touch Provisioning (ZTP) operations performed on the switch.

Usage

When a switch configured to use ZTP is booted from a factory default configuration, the switch contacts a
DHCP server, which offers options for obtaining files used to provision the switch:

n The IP address of the TFTP server

n The name of the image file

n The name of the configuration file

The show ztp information command shows the options offered by the DHCP server and the status of the
ZTP operation.

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

The switch was booted from a configuration that is not the factory default configuration. For example, the
administrator password has been set.

Failed - Timed out while waiting to receive ZTP options

Either the switch received the DHCP IPv4 address but no ZTP options were received within 1 minute or ZTP
force-provision is triggered and no ZTP options are received within 3 minutes.

Failed - Detected change in running configuration

The running configuration was modified by a user while the ZTP operation was in progress.

Failed - TFTP server unreachable

The TFTP server is not reachable at the specified IP address.

Failed - TFTP server information unavailable

The image file name or config file name is provided without the TFTP server location to fetch the files from
and ZTP enters failed state.

Failed - Invalid configuration file received

Either the file transfer of the configuration file failed, or the configuration file is invalid (an error occurred
while attempting to apply the configuration).

Failed - Invalid image file received

Either the file transfer of the firmware image file failed, or the firmware image file is invalid (an error
occurred while verifying the image).

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

301

Examples
ShowingswitchimagedownloadinprogressafterreceivingZTP options:
switch#
show ztp information
| TFTP Server     |              | : 10.0.0.2                     |         |          |                  |
| --------------- | ------------ | ------------------------------ | ------- | -------- | ---------------- |
| Image File      |              | : TL_10_02_0001.swi            |         |          |                  |
| Configuration   | File         | : config_file                  |         |          |                  |
| ZTP Status      |              | : In-progress                  | - Image | download | and verification |
| Aruba Central   | Location     | : secure.arubanetworks.com     |         |          |                  |
| Aruba Central   | Shared Token | : aruba123                     |         |          |                  |
| Force-Provision |              | : Disabled                     |         |          |                  |
| HTTP Proxy      | Location     | : http.proxy.arubanetworks.com |         |          |                  |
ShowingswitchimagedownloadfailureafterreceivingZTPoptions:
| switch#         | show ztp information |                                |          |             |       |
| --------------- | -------------------- | ------------------------------ | -------- | ----------- | ----- |
| TFTP Server     |                      | : 10.0.0.2                     |          |             |       |
| Image File      |                      | : TL_10_02_0001.swi            |          |             |       |
| Configuration   | File                 | : config_file                  |          |             |       |
| ZTP Status      |                      | : Failed                       | - Unable | to download | image |
| Aruba Central   | Location             | : secure.arubanetworks.com     |          |             |       |
| Aruba Central   | Shared Token         | : aruba123                     |          |             |       |
| Force-Provision |                      | : Disabled                     |          |             |       |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |          |             |       |
ShowingswitchconfigurationdownloadinprogressafterreceivingZTPoptions:
| switch#         | show ztp information |                                |                 |     |          |
| --------------- | -------------------- | ------------------------------ | --------------- | --- | -------- |
| TFTP Server     |                      | : 10.0.0.2                     |                 |     |          |
| Image File      |                      | : TL_10_02_0001.swi            |                 |     |          |
| Configuration   | File                 | : config_file                  |                 |     |          |
| ZTP Status      |                      | : In-progress                  | - Configuration |     | download |
| Aruba Central   | Location             | : secure.arubanetworks.com     |                 |     |          |
| Aruba Central   | Shared Token         | : aruba123                     |                 |     |          |
| Force-Provision |                      | : Disabled                     |                 |     |          |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |                 |     |          |
ShowingswitchconfigurationdownloadfailureafterreceivingZTPoptions:
| switch#         | show ztp information |                                |          |             |               |
| --------------- | -------------------- | ------------------------------ | -------- | ----------- | ------------- |
| TFTP Server     |                      | : 10.0.0.2                     |          |             |               |
| Image File      |                      | : TL_10_02_0001.swi            |          |             |               |
| Configuration   | File                 | : config_file                  |          |             |               |
| ZTP Status      |                      | : Failed                       | - Unable | to download | configuration |
| Aruba Central   | Location             | : secure.arubanetworks.com     |          |             |               |
| Aruba Central   | Shared Token         | : aruba123                     |          |             |               |
| Force-Provision |                      | : Disabled                     |          |             |               |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |          |             |               |
Showingswitchfailuretoupdatestart-upconfrigurationafterdownloadingconfigurationreceivedfromZTP
options:
| switch#     | show ztp information |            |     |     |     |
| ----------- | -------------------- | ---------- | --- | --- | --- |
| TFTP Server |                      | : 10.0.0.2 |     |     |     |
ZeroTouchProvisioning|302

| Image File    |      | : TL_10_02_0001.swi |     |     |
| ------------- | ---- | ------------------- | --- | --- |
| Configuration | File | : config_file       |     |     |
ZTP Status : Failed - Could not copy to start-up configuration
| Aruba Central   | Location     | : secure.arubanetworks.com     |     |     |
| --------------- | ------------ | ------------------------------ | --- | --- |
| Aruba Central   | Shared Token | : aruba123                     |     |     |
| Force-Provision |              | : Disabled                     |     |     |
| HTTP Proxy      | Location     | : http.proxy.arubanetworks.com |     |     |
Inthefollowingexample,theZTPoperationsucceeded,andbothanimagefileandaconfigurationfilewere
provided.
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
Inthefollowingexample,theZTPoptionsucceeded.Aconfigurationfilewasnotprovided,butanimagefile
wasprovided.
| VSF-10-Mbr#     | show ztp information |                     |     |     |
| --------------- | -------------------- | ------------------- | --- | --- |
| TFTP Server     |                      | : 10.1.84.160       |     |     |
| Image File      |                      | : TL_10_02_0001.swi |     |     |
| Configuration   | File                 | : NA                |     |     |
| Status          |                      | : Success           |     |     |
| Aruba Central   | Location             | : NA                |     |     |
| Aruba Central   | Shared Token         | : aruba123          |     |     |
| Force-Provision |                      | : Disabled          |     |     |
| HTTP Proxy      | Location             | : NA                |     |     |
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
303
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| VSF-10-Mbr##  | show ztp information |      |     |     |     |
| ------------- | -------------------- | ---- | --- | --- | --- |
| TFTP Server   |                      | : NA |     |     |     |
| Image File    |                      | : NA |     |     |     |
| Configuration | File                 | : NA |     |     |     |
Status : Failed - Timed out while waiting to receive ZTP options
| Aruba Central   | Location     | : NA       |     |     |     |
| --------------- | ------------ | ---------- | --- | --- | --- |
| Aruba Central   | Shared Token | : NA       |     |     |     |
| Force-Provision |              | : Disabled |     |     |     |
| HTTP Proxy      | Location     | : NA       |     |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchwasbootedfroma
configurationthatwasnotthefactorydefaultconfiguration.
| switch#         | show ztp information |                     |                  |               |          |
| --------------- | -------------------- | ------------------- | ---------------- | ------------- | -------- |
| TFTP Server     |                      | : 10.0.0.2          |                  |               |          |
| Image File      |                      | : TL_10_02_0001.swi |                  |               |          |
| Configuration   | File                 | : ztp.cfg           |                  |               |          |
| Status          |                      | : Failed            | - Custom startup | configuration | detected |
| Aruba Central   | Location             | : NA                |                  |               |          |
| Aruba Central   | Shared Token         | : NA                |                  |               |          |
| Force-Provision |                      | : Disabled          |                  |               |          |
| HTTP Proxy      | Location             | : NA                |                  |               |          |
CommandHistory
| Release        |     | Modification |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| ztp force | provision |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
ztp force-provision
no ztp force-provision
Description
Startson-demandZTP.
Usage
DHCPoptionsreceivedareprocessedindependentofhecurrentstateofconfigurationontheswitch.
PreviousZTPTFTPServer,ImageFile,ConfigurationFile,ArubaCentralLocation,andHTTPProxylocation
optionsareclearedandtheswitchsendsaDHCPrequest.
Examples
Inthefollowingexample,force-provisionisenabled.
ZeroTouchProvisioning|304

| switch# | configure terminal |     |
| ------- | ------------------ | --- |
switch(config)#
ztp force-provision
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
| switch#         | show ztp information |                     |
| --------------- | -------------------- | ------------------- |
| TFTP Server     |                      | : 10.0.0.2          |
| Image File      |                      | : TL_10_02_0001.swi |
| Configuration   | File                 | : ztp.cfg           |
| Status          |                      | : Success           |
| Aruba Central   | Location             | : NA                |
| Aruba Central   | Shared Token         | : NA                |
| Force-Provision |                      | : Enabled           |
| HTTP Proxy      | Location             | : NA                |
Inthefollowingexample,force-provisionisdisabled.
| switch#         | configure terminal     |     |
| --------------- | ---------------------- | --- |
| switch(config)# | no ztp force-provision |     |
Inthefollowingexample,force-provisionstatusischeckedwhiledisabled.
| switch#         | show ztp information |                     |
| --------------- | -------------------- | ------------------- |
| TFTP Server     |                      | : 10.0.0.2          |
| Image File      |                      | : TL_10_02_0001.swi |
| Configuration   | File                 | : ztp.cfg           |
| Status          |                      | : Success           |
| Aruba Central   | Location             | : NA                |
| Aruba Central   | Shared Token         | : NA                |
| Force-Provision |                      | : Disabled          |
| HTTP Proxy      | Location             | : NA                |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) | forthiscommand. |
| --- | --- | --------------- |
305
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Chapter 18
|                   |              | Switch   | system | and hardware | commands |
| ----------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system     | and hardware | commands |        |              |          |
| bluetooth         | disable      |          |        |              |          |
| bluetooth disable |              |          |        |              |          |
| no bluetooth      | disable      |          |        |              |          |
Description
DisablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesbothBluetoothClassicand
BluetoothLowEnergy(BLE).Bluetoothisenabledbydefault.
ThenoformofthiscommandenablestheBluetoothfeatureontheswitch.
Example
DisablingBluetoothontheswitch.<XXXX>istheswitchplatformand<NNNNNNNNNN>isthedevice
identifier.
| switch(config)# | bluetooth             | disable |     |     |     |
| --------------- | --------------------- | ------- | --- | --- | --- |
| switch#         | show bluetooth        |         |     |     |     |
| Enabled         | : No                  |         |     |     |     |
| Device name     | : <XXXX>-<NNNNNNNNNN> |         |     |     |     |
switch(config)#
|     | show running-config |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
...
| bluetooth | disabled |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
...
CommandHistory
| Release        |     | Modification |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
config
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400             |        | forthiscommand. |     |     |     |
| ---------------- | ------ | --------------- | --- | --- | --- |
| bluetooth        | enable |                 |     |     |     |
| bluetooth enable |        |                 |     |     |     |
| no bluetooth     | enable |                 |     |     |     |
Description
306
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- | --- |

This command enables the Bluetooth feature on the switch. The Bluetooth feature includes both Bluetooth
Classic and Bluetooth Low Energy (BLE).

Default: Bluetooth is enabled by default.

The no form of this command disables the Bluetooth feature on the switch.

Usage

The default configuration of the Bluetooth feature is enabled. The output of the show running-config
command includes Bluetooth information only if the Bluetooth feature is disabled.

The Bluetooth feature includes both Bluetooth Classic and Bluetooth Low Energy (BLE).

The Bluetooth feature requires the USB feature to be enabled. If the USB feature has been disabled, you
must enable the USB feature before you can enable the Bluetooth feature.

Examples

switch(config)# bluetooth enable

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6300
6400

config

Administrators or local user group members with execution rights
for this command.

clear events
clear events

Description

Clears up event logs. Using the show events command will only display the logs generated after the clear
events command.

Examples

Clearing all generated event logs:

switch# show events
---------------------------------------------------
show event logs
---------------------------------------------------
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
utilization poll interval is changed to 27
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to 36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
utilization poll interval is changed to 49

Switch system and hardware commands | 307

switch#
clear events
| switch# | show events |     |     |
| ------- | ----------- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2018-10-14:07:03:05.637544|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 34 |
| ----------- | ------------- | ---------- | ----- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
308
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400       |           |         |     | forthiscommand. |     |
| ---------- | --------- | ------- | --- | --------------- | --- |
| console    | baud-rate |         |     |                 |     |
| console    | baud-rate | <SPEED> |     |                 |     |
| no console | baud-rate | <SPEED> |     |                 |     |
Description
Setstheconsoleserialportspeed.
Thenoformofthiscommandresetstheconsoleportspeedtoitsdefaultof115200bps.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<SPEED>
Selectstheconsoleportspeedinbps,either9600or115200.
Usage
Thespeedchangeoccursimmediatelyfortheactiveconsolesession.Theconsolewillbeinaccessibleuntil
theclientterminalsettingsareupdatedtomatchtheconsoleportspeedthatyouset.Afterthecommandis
executedyouwillbepromptedtologinagain.
Examples
Settingtheconsoleportspeedto9600bps:
| switch(config)# |     | console | baud-rate | 9600 |     |
| --------------- | --- | ------- | --------- | ---- | --- |
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
| settings | are    | updated | to match the | baud rate | of the switch. |
| -------- | ------ | ------- | ------------ | --------- | -------------- |
| Continue | (y/n)? | y       |              |           |                |
Resettingtheconsoleporttoitsdefaultspeed115200bps:
| switch(config)# |     | no console | baud-rate |     |     |
| --------------- | --- | ---------- | --------- | --- | --- |
CommandHistory
| Release |     |     |     | Modification      |     |
| ------- | --- | --- | --- | ----------------- | --- |
| 10.08   |     |     |     | Commandintroduced |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Switchsystemandhardwarecommands|309

domain-name
| domain-name    | <NAME>   |     |
| -------------- | -------- | --- |
| no domain-name | [<NAME>] |     |
Description
Specifiesthedomainnameoftheswitch.
Thenoformofthiscommandsetsthedomainnametothedefault,whichisnodomainname.
| Parameter |     | Description |
| --------- | --- | ----------- |
<NAME> Specifiesthedomainnametobeassignedtotheswitch.Thefirst
characterofthenamemustbealetteroranumber.Length:1to
32characters.
Examples
Settingandshowingthedomainname:
| switch#         | show domain-name |             |
| --------------- | ---------------- | ----------- |
| switch#         | config           |             |
| switch(config)# | domain-name      | example.com |
| switch(config)# | show domain-name |             |
example.com
switch(config)#
Settingthedomainnametothedefaultvalue:
| switch(config)# | no domain-name   |     |
| --------------- | ---------------- | --- |
| switch(config)# | show domain-name |     |
switch(config)#
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
hostname
hostname <HOSTNAME>
| no hostname | [<HOSTNAME>] |     |
| ----------- | ------------ | --- |
Description
310
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<HOSTNAME> Specifiesthehostname.Thefirstcharacterofthehostname
mustbealetteroranumber.Length:1to32characters.Default:
switch
Examples
Settingandshowingthehostname:
| switch# | show | hostname |     |     |     |
| ------- | ---- | -------- | --- | --- | --- |
switch
| switch#         | config |          |          |     |     |
| --------------- | ------ | -------- | -------- | --- | --- |
| switch(config)# |        | hostname | myswitch |     |     |
myswitch(config)#
|     |     | show | hostname |     |     |
| --- | --- | ---- | -------- | --- | --- |
myswitch
Settingthehostnametothedefaultvalue:
| myswitch(config)# |     | no hostname |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- |
switch(config)#
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| module    | admin-state |              |             |     |               |
| --------- | ----------- | ------------ | ----------- | --- | ------------- |
| module    | <SLOT-ID>   | admin-state  | {diagnostic | |   | down | up}    |
| no module | <SLOT-ID>   | [admin-state | [diagnostic |     | | down | up]] |
Description
Setstheadministrativestateofthespecifiedlinemodule.
Thenoformofthecommandconfiguresadministrativestatetothedefaultup.
Switchsystemandhardwarecommands|311

| Parameter |     |     |     |     |     | Description                                        |
| --------- | --- | --- | --- | --- | --- | -------------------------------------------------- |
| <SLOT-ID> |     |     |     |     |     | Specifiesthememberandslotofthemodule.Forexample,to |
specifythemoduleinmember1,slot3,enterthefollowing:
1/3
| admin-state |     | {diagnostic | |   | down | | up} |     |
| ----------- | --- | ----------- | --- | ---- | ----- | --- |
Selectstheadministrativestateinwhichtoputthespecified
module:
diagnostic Selectsthediagnosticadministrativestate.Networktraffic
doesnotpassthroughthemodule.
| down |     |     |     |     |     | Selectsthedownadministrativestate.Networktrafficdoesnot |
| ---- | --- | --- | --- | --- | --- | ------------------------------------------------------- |
passthroughthemodule.
| up  |     |     |     |     |     | Selectstheupadministrativestate.Thelinemoduleisfully |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------- |
operational.Theupstateisthedefaultadministrativestate.
Example
Settingtheadministrativestateofthemoduleinslot1/3todown:
| switch(config)# |     | module | 1/3 | admin-state |     | down |
| --------------- | --- | ------ | --- | ----------- | --- | ---- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
6400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| module    |           | product-number  |     |                 |                  |     |
| --------- | --------- | --------------- | --- | --------------- | ---------------- | --- |
| module    | <SLOT-ID> | product-number  |     | [<PRODUCT-NUM>] |                  |     |
| no module | <SLOT-ID> | [product-number |     |                 | [<PRODUCT-NUM>]] |     |
Description
Changestheconfigurationoftheswitchtoindicatethatthespecifiedmemberandslotnumbercontains,or
willcontain,alinemodule.
Thenoformofthiscommandremovesthelinemoduleanditsinterfacesfromtheconfiguration.Ifthereis
alinemoduleinstalledintheslot,thelinemoduleispoweredoffandthenpoweredon.
312
| AOS-CX10.09FundamentalsGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- |

Parameter

<SLOT-ID>

<PRODUCT-NUM>

Description

Specifies the member and slot in the form m/s, where m is the
member number, and s is the slot number.

Specifies the product number of the line module. For example:
JL363A
If there is a line module installed in the slot when you execute this
command, <PRODUCT-NUM> is optional. The switch reads the
product number information from the module that is installed in
the slot.
If there is no line module installed in the slot when you execute
this command, <PRODUCT-NUM> is required.

Usage

The default configuration associated with a line module slot is:

n There is no module product number or interface configuration information associated with the slot. The

slot is available for the installation with any supported line module.

n The Admin State is Up (which is the default value for Admin State).

To add a line module to the configuration, you must use the module command either before or after you
install the physical module.

If you execute the module command after you install a line module in an empty slot, you can omit the
<PRODUCT-NUM> variable. The switch reads the product information from the installed module.

If the module is not installed in the slot when you execute the module command, you must specify a value
for the <PRODUCT-NUM> variable:

n The switch validates the product number of the module against the slot number you specify to ensure

that the right type of module is configured for the specified slot.

For example, the switch returns an error if you specify the product number of a line module for a slot
reserved for management modules.

n You can configure the line module interfaces before the line module is installed.

When you install the physical line module in a preconfigured slot, the following actions occur:

n If a product number was specified in the command and it matches the product number of the installed

module, the switch initializes the module.

n If a product number was specified in the command and the product number of the module does not

match what was specified, the module device initialization fails.

The no form of the command removes the line module and its interfaces from the configuration and
restores the line module slot to the default configuration.

If there is a line module installed in the slot when you execute the no form of the command, the command
also powers off and then powers on the module. Traffic passing through the line module is stopped.
Management sessions connected through the line module are also affected.

If the slot associated with the line module is in the default configuration, you can remove the module from
the chassis without disrupting the operation of the switch.

Examples

Configuring slot 1/1 for future installation of a line module:

Switch system and hardware commands | 313

| switch(config)# |     | module | 1/1 product-number |     | jl363a |
| --------------- | --- | ------ | ------------------ | --- | ------ |
Configuringalinemodulethatisalreadyinstalledinslot1/1:
| switch(config)# |     | module | 1/1 product-number |     |     |
| --------------- | --- | ------ | ------------------ | --- | --- |
Attemptingtoconfigureslot1/1forthefutureinstallationofalinemodulewithoutspecifyingtheproduct
number(returnederrorshown):
| switch(config)# |     | module | 1/1 product-number |     |     |
| --------------- | --- | ------ | ------------------ | --- | --- |
Line module '1/4' is not physically available. Please provide the product
| number | to preconfigure |     | the line | module. |     |
| ------ | --------------- | --- | -------- | ------- | --- |
Removingamodulefromtheconfiguration:
| switch(config)# |     | no module | 1/1 |     |     |
| --------------- | --- | --------- | --- | --- | --- |
This command will power cycle the specified line module and restore its default
configuration. Any traffic passing through the line module will be interrupted.
Management sessions connected through the line module will be affected. It
| might take | a       | few minutes | to complete | this | operation. |
| ---------- | ------- | ----------- | ----------- | ---- | ---------- |
| Do you     | want to | continue    | (y/n)?      | y    |            |
switch(config)#
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
config
6400 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mtrace
mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
[vrf <VRF-NAME>]
Description
TracesthespecifiedIPv4sourceandgroupaddresses.
| Parameter     |     |     |     | Description                           |     |
| ------------- | --- | --- | --- | ------------------------------------- | --- |
| IPV4-SRC-ADDR |     |     |     | SpecifiesthesourceIPv4addresstotrace. |     |
314
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| Parameter       |     |     |     |     | Description                          |     |     |
| --------------- | --- | --- | --- | --- | ------------------------------------ | --- | --- |
| IPV4-GROUP-ADDR |     |     |     |     | SpecifiesthegroupIPv4addresstotrace. |     |     |
lhr <IPV4-LHR-ADDR> Specifiesthelasthoprouteraddressfromwhichtostartthetrace.
ttl <HOPS> SpecifiestheTime-To-Livedurationinhops.Range:1to255hops.
Default:8hops.
vrf <VRF-NAME> SpecifiesthenameoftheVRF.Ifanameisnotspecifiedthe
defaultVRFwillbeused.
Examples
Tracingwithsource,group,andLHRaddressesandTTL:
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
| -1 30.0.0.1  | PIM | 0 ms |     |     |     |     |     |
| ------------ | --- | ---- | --- | --- | --- | --- | --- |
| -2 40.0.0.1  | PIM | 2 ms |     |     |     |     |     |
| -3 50.0.0.1  | PIM | 100  | ms  |     |     |     |     |
| -4 60.0.0.1  | PIM | 156  | ms  |     |     |     |     |
| -5 200.0.0.1 | PIM | 123  | ms  |     |     |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
Switchsystemandhardwarecommands|315

| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
show bluetooth
show bluetooth
Description
ShowsgeneralstatusinformationabouttheBluetoothwirelessmanagementfeatureontheswitch.
Usage
Thiscommandshowsstatusinformationaboutthefollowing:
TheUSBBluetoothadapter
n
n ClientsconnectedusingBluetooth
n TheswitchBluetoothfeature.
Theoutputoftheshow running-configcommandincludesBluetoothinformationonlyiftheBluetooth
featureisdisabled.
Thedevicenamegiventotheswitchincludestheswitchserialnumbertouniquelyidentifytheswitchwhile
pairingwithamobiledevice.
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
316
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| switch# | show bluetooth             |     |
| ------- | -------------------------- | --- |
| Enabled | : No                       |     |
| Device  | name : <XXXX>-<NNNNNNNNNN> |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 6400 | (#) |     |
| ---- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show boot-history |       |     |
| ----------------- | ----- | --- |
| show boot-history | [all] |     |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationaboutthe
bootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.Whentheall
parameterisspecified,showsthebootinformationfortheactivemanagementmoduleandallavailableline
modules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandbyconsole.
| Parameter |     | Description                                         |
| --------- | --- | --------------------------------------------------- |
| all       |     | Showsbootinformationfortheactivemanagementmoduleand |
allavailablelinemodules.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereisa
previousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | up for <SECONDS> | seconds |
| ------------- | ---------------- | ------- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
| Timestamp boot | reason |     |
| -------------- | ------ | --- |
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperationoccurred
andthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |
| ------------- | ----- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernel crash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
| Reboot requested | through database |     |
| ---------------- | ---------------- | --- |
Switchsystemandhardwarecommands|317

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
CommandHistory
318
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Release        |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities |           |            |     |     |     |     |     |
| --------------- | --------- | ---------- | --- | --- | --- | --- | --- |
| show capacities | <FEATURE> | [vsx-peer] |     |     |     |     |     |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description |     |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- | --- |
<FEATURE>
Specifiesafeature.Forexample,aaaorvrrp.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardwareor
softwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
ShowingallavailablecapacitiesforBGP:
| switch#            | show capacities | bgp    |     |     |     |       |     |
| ------------------ | --------------- | ------ | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter | BGP |     |     |       |     |
| Capacities         | Name            |        |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of AS | numbers | in as-path | attribute |     |     | 32  |
| ------- | ------------ | ------- | ---------- | --------- | --- | --- | --- |
...
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring |           |     |     |       |     |
| ------------------ | --------------- | --------- | --------- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter    | Mirroring |     |     |       |     |
| Capacities         | Name            |           |           |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of Mirror | Sessions | configurable |     | in a system |     | 4   |
| ------- | ---------------- | -------- | ------------ | --- | ----------- | --- | --- |
Switchsystemandhardwarecommands|319

| Maximum number | of  | enabled Mirror |     | Sessions | in  | a system | 4   |
| -------------- | --- | -------------- | --- | -------- | --- | -------- | --- |
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp   |      |     |     |     |       |
| ------------------ | --------------- | ------ | ---- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter | MSTP |     |     |     |       |
| Capacities         | Name            |        |      |     |     |     | Value |
-----------------------------------------------------------------------------------
| Maximum | number of | mstp instances |     | configurable |     | in a system | 64  |
| ------- | --------- | -------------- | --- | ------------ | --- | ----------- | --- |
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities | vlan-count |      |       |     |     |       |
| ------------------ | --------------- | ---------- | ---- | ----- | --- | --- | ----- |
| System Capacities: |                 | Filter     | VLAN | Count |     |     |       |
| Capacities         | Name            |            |      |       |     |     | Value |
-----------------------------------------------------------------------------------
| Maximum | number of | VLANs supported |     | in  | the system |     | 4094 |
| ------- | --------- | --------------- | --- | --- | ---------- | --- | ---- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities-status |     |           |            |     |     |     |     |
| ---------------------- | --- | --------- | ---------- | --- | --- | --- | --- |
| show capacities-status |     | <FEATURE> | [vsx-peer] |     |     |     |     |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<FEATURE> Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplay
capacities,values,andstatus.Required.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
320
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

Examples
Showingthesystemcapacitiesstatusforallfeatures:
switch#
show capacities-status
| System     | Capacities | Status |     |     |     |     |               |
| ---------- | ---------- | ------ | --- | --- | --- | --- | ------------- |
| Capacities | Status     | Name   |     |     |     |     | Value Maximum |
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
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
Switchsystemandhardwarecommands|321

| switch#    | show console |     |
| ---------- | ------------ | --- |
| Baud Rate: | 9600         |     |
CommandHistory
| Release |     | Modification      |
| ------- | --- | ----------------- |
| 10.08   |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show core-dump
| show core-dump | [all | <SLOT-ID>] |     |
| -------------- | ----------------- | --- |
Description
Showscoredumpinformationaboutthespecifiedmodule.Whennoparametersarespecified,showsonly
thecoredumpsgeneratedinthecurrentbootofthemanagementmodule.Whentheallparameteris
specified,showsallavailablecoredumps.
| Parameter |     | Description                               |
| --------- | --- | ----------------------------------------- |
| all       |     | Showsallavailablecoredumps.               |
| <SLOT-ID> |     | Showsthecoredumpsforthemanagementmoduleor |
linemodulein<SLOT-ID>.<SLOT-ID>specifiesaphysical
locationontheswitch.Usetheformatmember/slot/port
(forexample,1/3/1)forlinemodules.Usetheformat
member/slotformanagementmodules.
YoumustspecifytheslotIDforeithertheactive
managementmodule,orthelinemodule.
Usage
Whennoparametersarespecified,theshow core-dumpcommandshowsonlythecoredumpsgeneratedin
thecurrentbootofthemanagementmodule.Youcanusethiscommandtodeterminewhenanycrashes
areoccurringinthecurrentboot.
Ifnocoredumpshaveoccurred,thefollowingmessageisdisplayed:No core dumps are present
Toshowcoredumpinformationforthestandbymanagementmodule,youmustusethestandby
commandtoswitchtothestandbymanagementmoduleandthenexecutetheshow core-dumpcommand.
Intheoutput,themeaningoftheinformationisthefollowing:
Daemon Name
Identifiesnameofthedaemonforwhichthereisdumpinformation.
Instance ID
IdentifiesthespecificinstanceofthedaemonshownintheDaemon Namecolumn.
322
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

Present
Indicatesthestatusofthecoredump:
Yes
Thecoredumphascompletedandavailableforcopying.
In Progress
Coredumpgenerationisinprogress.Donotattempttocopythiscoredump.
Timestamp
Indicatesthetimethedaemoncrashoccurred.Thetimeisthelocaltimeusingthetimezoneconfiguredonthe
switch.
Build ID
Identifiesadditionalinformationaboutthesoftwareimageassociatedwiththedaemon.
Examples
Showingcoredumpinformationforthecurrentbootoftheactivemanagementmoduleonly:
| switch# show | core-dump |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
==================================================================================
| Daemon Name | | Instance | ID | Present | | Timestamp |     | | Build ID |
| ----------- | ---------- | ------------ | ----------- | --- | ---------- |
==================================================================================
| hpe-fand    | 1399 | Yes | 2017-08-04 | 19:05:34 | 1246d2a |
| ----------- | ---- | --- | ---------- | -------- | ------- |
| hpe-sysmond | 957  | Yes | 2017-08-04 | 19:05:29 | 1246d2a |
==================================================================================
| Total number | of core | dumps : 2 |     |     |     |
| ------------ | ------- | --------- | --- | --- | --- |
==================================================================================
Showingallcoredumps:
| switch# show | core-dump | all |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
=============================================================================
| Management | Module core-dumps |     |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
=============================================================================
| Daemon Name | | Instance | ID | Present | | Timestamp |     | | Build ID |
| ----------- | ---------- | ------------ | ----------- | --- | ---------- |
=============================================================================
| hpe-sysmond | 513        | Yes | 2017-07-31 | 13:58:05 | e70f101 |
| ----------- | ---------- | --- | ---------- | -------- | ------- |
| hpe-tempd   | 1048       | Yes | 2017-08-13 | 13:31:53 | e70f101 |
| hpe-tempd   | 1052       | Yes | 2017-08-13 | 13:41:44 | e70f101 |
| Line Module | core-dumps |     |            |          |         |
=============================================================================
| Line Module | : 1/1 |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
=============================================================================
| dune_agent_0 | 18958 | Yes | 2017-08-12 | 11:50:17 | e70f101 |
| ------------ | ----- | --- | ---------- | -------- | ------- |
| dune_agent_0 | 18842 | Yes | 2017-08-12 | 11:50:09 | e70f101 |
=============================================================================
| Total number | of core | dumps : 5 |     |     |     |
| ------------ | ------- | --------- | --- | --- | --- |
=============================================================================
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
Switchsystemandhardwarecommands|323

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show domain-name |            |     |     |
| ---------------- | ---------- | --- | --- |
| show domain-name | [vsx-peer] |     |     |
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
switch#
show domain-name
| switch#         | config      |             |     |
| --------------- | ----------- | ----------- | --- |
| switch(config)# | domain-name | example.com |     |
| switch(config)# | show        | domain-name |     |
example.com
switch(config)#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show environment |          | fan         |     |
| ---------------- | -------- | ----------- | --- |
| show environment | fan [vsf | | vsx-peer] |     |
Description
324
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |
| ----------------------------- | ----------------------- | --- | --- |

Shows the status information for all fans and fan trays (if present) in the system.

Parameter

vsf

vsx-peer

Usage

Description

Shows output from the VSF member-id on switches that
support VSF.

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

Switch system and hardware commands | 325

Showingoutputforsystemswithfantraysfor6400switchseries:
| switch#  | show environment | fan |     |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- | --- | --- |
| Fan tray | information      |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Mbr/Tray | Description |     |     |     | Status | Serial Number | Fans |
| -------- | ----------- | --- | --- | --- | ------ | ------------- | ---- |
------------------------------------------------------------------------------
| 1/1 | R0X32A Aruba | 6400 | Fan Tray |     | ready | SG9ZKJL7JW | 4   |
| --- | ------------ | ---- | -------- | --- | ----- | ---------- | --- |
| 1/2 | R0X32A Aruba | 6400 | Fan Tray |     | ready | SG9ZKJL7GL | 4   |
| 1/3 | R0X32A Aruba | 6400 | Fan Tray |     | ready | SG9ZKJL78L | 4   |
| 1/4 | R0X32A Aruba | 6400 | Fan Tray |     | ready | SG9ZKJL7GJ | 4   |
Fan information
---------------------------------------------------------------------------
Mbr/Tray/Fan Product Serial Number Speed Direction Status RPM
Name
---------------------------------------------------------------------------
| 1/1/1 | N/A | N/A |     | slow front-to-back |     | ok 5371 |     |
| ----- | --- | --- | --- | ------------------ | --- | ------- | --- |
| 1/1/2 | N/A | N/A |     | slow front-to-back |     | ok 5320 |     |
| 1/1/3 | N/A | N/A |     | slow front-to-back |     | ok 5328 |     |
| 1/1/4 | N/A | N/A |     | slow front-to-back |     | ok 5256 |     |
| 1/2/1 | N/A | N/A |     | slow front-to-back |     | ok 5371 |     |
| 1/2/2 | N/A | N/A |     | slow front-to-back |     | ok 5349 |     |
| 1/2/3 | N/A | N/A |     | slow front-to-back |     | ok 5292 |     |
| 1/2/4 | N/A | N/A |     | slow front-to-back |     | ok 5349 |     |
| 1/3/1 | N/A | N/A |     | slow front-to-back |     | ok 5313 |     |
| 1/3/2 | N/A | N/A |     | slow front-to-back |     | ok 5371 |     |
| 1/3/3 | N/A | N/A |     | slow front-to-back |     | ok 5379 |     |
| 1/3/4 | N/A | N/A |     | slow front-to-back |     | ok 5379 |     |
| 1/4/1 | N/A | N/A |     | slow front-to-back |     | ok 5313 |     |
| 1/4/2 | N/A | N/A |     | slow front-to-back |     | ok 5299 |     |
| 1/4/3 | N/A | N/A |     | slow front-to-back |     | ok 5285 |     |
| 1/4/4 | N/A | N/A |     | slow front-to-back |     | ok 5371 |     |
Showingoutputforasystemwithoutafantray:
| switch# | show environment | fan |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- | --- |
Fan information
---------------------------------------------------------------
| Fan Serial | Number | Speed | Direction | Status |     | RPM |     |
| ---------- | ------ | ----- | --------- | ------ | --- | --- | --- |
---------------------------------------------------------------
| 1 SGXXXXXXXXXX |     | slow   | front-to-back | ok    |     | 6000  |     |
| -------------- | --- | ------ | ------------- | ----- | --- | ----- | --- |
| 2 SGXXXXXXXXXX |     | normal | front-to-back | ok    |     | 8000  |     |
| 3 SGXXXXXXXXXX |     | medium | front-to-back | ok    |     | 11000 |     |
| 4 SGXXXXXXXXXX |     | fast   | front-to-back | ok    |     | 14000 |     |
| 5 SGXXXXXXXXXX |     | max    | front-to-back | fault |     | 16500 |     |
| 6 N/A          |     | N/A    | N/A           | empty |     |       |     |
...
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
326
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |                 | led |            |
| ---------------- | --------------- | --- | ---------- |
| show environment | led <MEMBER-ID> |     | [vsx-peer] |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
| Parameter   |     |     | Description                               |
| ----------- | --- | --- | ----------------------------------------- |
| <MEMBER-ID> |     |     | ShowsoutputfromthespecifiedVSFmemberID on |
switchesthatsupportVSF.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingstateandstatusforLED:
| switch#  | show environment | led    |     |
| -------- | ---------------- | ------ | --- |
| Mbr/Name | State            | Status |     |
-------------------------------
| 1/locator | off | ok  |     |
| --------- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show environment |     | power-consumption |     |
| ---------------- | --- | ----------------- | --- |
Notsupportedonthe6300SwitchSeries.
| show environment | power-consumption |     | [vsx-peer] |
| ---------------- | ----------------- | --- | ---------- |
Description
Switchsystemandhardwarecommands|327

Showsthepowerbeingconsumedbyeachmanagementmodule,linecard,andfabriccardsubsystem,and
showspowerconsumptionfortheentirechassis.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Thiscommandisonlyapplicabletosystemsthatsupportpowerconsumptionreadings.
Thepowerconsumptionvaluesareupdatedonceeveryminute.
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
ShowingthepowerconsumptionforanAruba6400switch:
| switch> show | environment | power-consumption |     |     |     |
| ------------ | ----------- | ----------------- | --- | --- | --- |
Power
| Name Type |     | Description |     |     | Usage |
| --------- | --- | ----------- | --- | --- | ----- |
------------------------------------------------------------------------------
| 1/1 management-module |     | R0X31A 6400 | Management | Module | 18 W |
| --------------------- | --- | ----------- | ---------- | ------ | ---- |
| 1/2 management-module |     |             |            |        | 0 W  |
| 1/3 line-card-module  |     |             |            |        | 0 W  |
1/4 line-card-module R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod 54 W
| 1/5 line-card-module |     |     |     |     | 0 W |
| -------------------- | --- | --- | --- | --- | --- |
1/6 line-card-module R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod 56 W
1/7 line-card-module R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod 51 W
| 1/1 fabric-card-module |                 | R0X24A 6405 | Chassis |     | 71 W   |
| ---------------------- | --------------- | ----------- | ------- | --- | ------ |
| Module Total           | Power Usage     |             |         |     | 250 W  |
| Chassis Total          | Power Usage     |             |         |     | 294 W  |
| Chassis Total          | Power Available |             |         |     | 1800 W |
328
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6400

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show environment power-supply
show environment power-supply [vsf | vsx-peer]

Description

Shows status information about all power supplies in the switch.

Parameter

vsf

vsx-peer

Usage

Description

Shows output from the VSF member-id on switches that support
VSF.

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

The following information is provided for each power supply:
Mbr/PSU
Shows the member and slot number of the power supply.
Product Number
Shows the product number of the power supply.
Serial Number
Shows the serial number of the power supply, which uniquely identifies the power supply.
PSU Status

The status of the power supply. Values are:

OK

Power supply is operating normally.

OK*

Power supply is operating normally, but it is the only power supply in the chassis. One power supply is
not sufficient to supply full power to the switch. When this value is shown, the output of the
command also shows a message at the end of the displayed data.

Absent

No power supply is installed in the specified slot.

Input fault

The power supply has a fault condition on its input.

Output fault

The power supply has a fault condition on its output.

Switch system and hardware commands | 329

Warning
Thepowersupplyisnotoperatingnormally.
| Wattage Maximum |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
Showsthemaximumamountofwattagethatthepowersupplycanprovide.
Example
ShowingtheoutputwhenonlyonepowersupplyisinstalledinanAruba6400switchchassis:
switch#
|         | show environment |        | power-supply |     |        |         |
| ------- | ---------------- | ------ | ------------ | --- | ------ | ------- |
|         | Product          | Serial |              |     | PSU    | Wattage |
| Mbr/PSU | Number           | Number |              |     | Status | Maximum |
--------------------------------------------------------------
| 1/1 | R0X36A | CN91KMM2H3 |     |     | OK     | 3000 |
| --- | ------ | ---------- | --- | --- | ------ | ---- |
| 1/2 | N/A    | N/A        |     |     | Absent | 0    |
| 1/3 | N/A    | N/A        |     |     | Absent | 0    |
| 1/4 | N/A    | N/A        |     |     | Absent | 0    |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show             | environment         |     | rear-display-module |            |     |     |
| ---------------- | ------------------- | --- | ------------------- | ---------- | --- | --- |
| show environment | rear-display-module |     |                     | [vsx-peer] |     |     |
Description
Showsinformationaboutthedisplaymoduleonthebackoftheswitch.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingthereardisplaymoduleinformationonthebackoftheswitch:
| switch>      | show environment |     | rear-display-module |     |     |     |
| ------------ | ---------------- | --- | ------------------- | --- | --- | --- |
| Rear display | module           | is  | ready               |     |     |     |
330
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- |

| Description:      | 8400      | Rear       | Display      | Mod    |
| ----------------- | --------- | ---------- | ------------ | ------ |
| Full Description: |           | 8400       | Rear Display | Module |
| Serial number:    |           | SG00000000 |              |        |
| Part number:      | 5300_0272 |            |              |        |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority                                            |
| --------- | -------------- | --- | --- | ---------------------------------------------------- |
| 6300      |                |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |             |     | temperature |                  |
| ---------------- | ----------- | --- | ----------- | ---------------- |
| show environment | temperature |     | [detail]    | [vsf | vsx-peer] |
Description
Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
| Parameter |     |     |     | Description                                         |
| --------- | --- | --- | --- | --------------------------------------------------- |
| detail    |     |     |     | Showsdetailedinformationfromeachtemperaturesensor.  |
| vsf       |     |     |     | ShowsoutputfromtheVSFmember-idonswitchesthatsupport |
VSF
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
Switchsystemandhardwarecommands|331

emergency
Overtemperatureeventforthissensor.
Examples
Showingcurrenttemperatureinformationfora6300switch:
| switch# show | environment | temperature |     |     |     |
| ------------ | ----------- | ----------- | --- | --- | --- |
| Temperature  | information |             |     |     |     |
------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     |     | Module Type | temperature | Status |
| --------------- | --- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-PHY-01-04            |     |     | line-card-module  | 45.00 | C normal |
| ------------------------ | --- | --- | ----------------- | ----- | -------- |
| 1/1-PHY-05-08            |     |     | line-card-module  | 45.00 | C normal |
| 1/1-PHY-09-12            |     |     | line-card-module  | 46.00 | C normal |
| 1/1-PHY-13-16            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-17-20            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-21-24            |     |     | line-card-module  | 50.00 | C normal |
| 1/1-PHY-25-28            |     |     | line-card-module  | 45.00 | C normal |
| 1/1-PHY-29-32            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-33-36            |     |     | line-card-module  | 48.00 | C normal |
| 1/1-PHY-37-40            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-41-44            |     |     | line-card-module  | 48.00 | C normal |
| 1/1-PHY-45-48            |     |     | line-card-module  | 49.00 | C normal |
| 1/1-Switch-ASIC-Internal |     |     | line-card-module  | 56.25 | C normal |
| 1/1-CPU-Zone-0           |     |     | management-module | 50.00 | C normal |
| 1/1-CPU-Zone-1           |     |     | management-module | 50.00 | C normal |
| 1/1-CPU-Zone-2           |     |     | management-module | 50.00 | C normal |
| 1/1-CPU-Zone-3           |     |     | management-module | 51.00 | C normal |
| 1/1-CPU-Zone-4           |     |     | management-module | 51.00 | C normal |
| 1/1-CPU-diode            |     |     | management-module | 53.12 | C normal |
| 1/1-DDR                  |     |     | management-module | 45.25 | C normal |
| 1/1-Inlet-Air            |     |     | management-module | 24.88 | C normal |
| 1/1-MB-IBC               |     |     | management-module | 45.62 | C normal |
| 1/1-Switch-ASIC-diode    |     |     | management-module | 58.06 | C normal |
Showingdetailedtemperatureinformationfora6300switch:
| switch# show         | environment | temperature | detail |     |     |
| -------------------- | ----------- | ----------- | ------ | --- | --- |
| Detailed temperature |             | information |        |     |     |
----------------------------------------------------------------
| Mbr/Slot-Sensor     |     | : 1/1-PHY-01-04    |                 |            |      |
| ------------------- | --- | ------------------ | --------------- | ---------- | ---- |
| Module Type         |     | : line-card-module |                 |            |      |
| Module Description  |     | : JL659A           | 6300M 48SR5 CL6 | PoE 4SFP56 | Swch |
| Status              |     | : normal           |                 |            |      |
| Fan-state           |     | : normal           |                 |            |      |
| Current temperature |     | : 45.00            | C               |            |      |
| Minimum temperature |     | : 41.00            | C               |            |      |
| Maximum temperature |     | : 50.00            | C               |            |      |
| Mbr/Slot-Sensor     |     | : 1/1-PHY-05-08    |                 |            |      |
| Module Type         |     | : line-card-module |                 |            |      |
| Module Description  |     | : JL659A           | 6300M 48SR5 CL6 | PoE 4SFP56 | Swch |
| Status              |     | : normal           |                 |            |      |
| Fan-state           |     | : normal           |                 |            |      |
| Current temperature |     | : 45.00            | C               |            |      |
| Minimum temperature |     | : 41.00            | C               |            |      |
| Maximum temperature |     | : 50.00            | C               |            |      |
332
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

...
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |
| --------- | --- | -------------- | --- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show |        | events          |     |     |     |
| ---- | ------ | --------------- | --- | --- | --- |
| show | events | [ -e <EVENT-ID> |     | |   |     |
-s {emergency | alert | critical | error | warning | notice | info | debug} |
-r |
-a |
|     | -n <COUNT>       | |          |        |         |     |
| --- | ---------------- | ---------- | ------ | ------- | --- |
|     | -i <MEMBER-SLOT> |            | |      |         |     |
|     | -m {active       | | standby} |        | |       |     |
|     | -c {lldp         | | ospf     | | ...} | |       |     |
|     | -d {lldpd        | | bgpd     | | fand | | ...}] |     |
Description
Showseventlogsgeneratedbytheswitchmodulessincethelastreboot.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
-e <EVENT-ID>
ShowstheeventlogsforthespecifiedeventID.EventIDrange:
101through99999.
-s {emergency | alert | critical | Showstheeventlogsforthespecifiedseverity.Selecttheseverity
|     | error | | warning | |   | notice | | fromthefollowinglist: |
| --- | ----- | --------- | --- | -------- | --------------------- |
|     | info  | | debug}  |     |          |                       |
n emergency:Displayseventlogswithseverityemergencyonly.
n alert:Displayseventlogswithseverityalertandabove.
critical:Displayseventlogswithseveritycriticalandabove.
n
n error:Displayseventlogswithseverityerrorandabove.
warning:Displayseventlogswithseveritywarningandabove.
n
n notice:Displayseventlogswithseveritynoticeandabove.
info:Displayseventlogswithseverityinfoandabove.
n
n debug:Displayseventlogswithallseverities.
-r
Showsthemostrecenteventlogsfirst.
| -a  |     |     |     |     | Showsalleventlogs,includingthoseeventsfrompreviousboots. |
| --- | --- | --- | --- | --- | -------------------------------------------------------- |
Switchsystemandhardwarecommands|333

Parameter

-n <COUNT>

-i <MEMBER-SLOT>

-i <MEMBER-SLOT>

-m {active | standby}

-m {active | standby}

-c {lldp | ospf | ...}

Description

Displays the specified number of event logs.

On a 6400: Shows the event logs for the specified slot ID.

On a 6300: Shows the event logs for the specified VSF member ID.

On a 6400: Shows the event logs for the specified management
card role. Selecting active displays the event log for the AMM
management card role and standby displays event logs for the
SMM management card role.

On a 6300: Shows the event logs for the specified role. Selecting
active displays the event log for the VSF conductor role and
standby displays event logs for the VSF standby role.

Shows the event logs for the specified event category. Enter show
event -c for a full listing of supported categories with
descriptions.

-d {lldpd | bgpd | fand | ...}

Shows the event logs for the specified process. Enter show event
-d for a full listing of supported daemons with descriptions.

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

switch# show events -r
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1

in Hardware

2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to

up for bridge_normal interface

2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to

70:72:cf:51:50:7c

Showing all event logs:

switch# show events -a
---------------------------------------------------

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

334

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
Showingeventlogsasperthespecifiedmanagementcardrolefora6400switch:
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
Switchsystemandhardwarecommands|335

| switch# | show events | -n 5 |     |
| ------- | ----------- | ---- | --- |
---------------------------------------------------
| show | event logs |     |     |
| ---- | ---------- | --- | --- |
---------------------------------------------------
2018-03-21:06:12:15.500603|arpmgrd|6101|LOG_INFO|AMM|-|ARPMGRD daemon has started
2018-03-21:06:12:17.734405|lldpd|109|LOG_INFO|AMM|-|Configured LLDP tx-delay to 2
2018-03-21:06:12:17.740517|lacpd|1307|LOG_INFO|AMM|-|LACP system ID set to
70:72:cf:d4:34:42
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show | fabric |     |     |
| ---- | ------ | --- | --- |
Notsupportedonthe6300SwitchSeries.
| show fabric | [<SLOT-ID>] | [vsx-peer] |     |
| ----------- | ----------- | ---------- | --- |
Description
Showsinformationabouttheinstalledfabrics.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<SLOT-ID>
Specifiesthememberandslotofthefabrictoshow.Forexample,
toshowthemoduleinmember1,slot2,enterthefollowing:
1/2
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingallfabricsonAruba6400switchesthathavetwofabrics:
| switch# | show fabric |     |     |
| ------- | ----------- | --- | --- |
| Fabric  | Modules     |     |     |
336
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

==============
| Product     |             |     | Serial |        |
| ----------- | ----------- | --- | ------ | ------ |
| Name Number | Description |     | Number | Status |
---- ------- -------------------------------- ---------- ----------------
| 1/1 R0X25A | 6410 Chassis |     | SG9ZKM9999 | Ready |
| ---------- | ------------ | --- | ---------- | ----- |
| 1/2 R0X25A | 6410 Chassis |     | SG9ZKM9999 | Ready |
ShowingallfabricsonAruba6400switchesthathaveonefabric:
| switch#        | show fabric |     |     |     |
| -------------- | ----------- | --- | --- | --- |
| Fabric Modules |             |     |     |     |
==============
| Product     |             |     | Serial |        |
| ----------- | ----------- | --- | ------ | ------ |
| Name Number | Description |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 R0X24A | 6405 Chassis |     | SG9ZKM9076 | Ready |
| ---------- | ------------ | --- | ---------- | ----- |
ShowingasinglefabricmoduleonAruba6400switches:
| switch#           | show fabric 1/1 |     |     |     |
| ----------------- | --------------- | --- | --- | --- |
| Fabric module     | 1/1 is ready    |     |     |     |
| Admin state:      | Up              |     |     |     |
| Description:      | 6405 Chassis    |     |     |     |
| Full Description: | 6405 Chassis    |     |     |     |
| Serial number:    | SG00000000      |     |     |     |
| Product           | number: R0X24A  |     |     |     |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
show hostname
| show hostname | [vsx-peer] |     |     |     |
| ------------- | ---------- | --- | --- | --- |
Description
Showsthecurrenthostname.
Switchsystemandhardwarecommands|337

| Parameter |     | Description |
| --------- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Settingandshowingthehostname:
| switch# | show hostname |     |
| ------- | ------------- | --- |
switch
| switch#           | config            |     |
| ----------------- | ----------------- | --- |
| switch(config)#   | hostname myswitch |     |
| myswitch(config)# | show hostname     |     |
myswitch
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show images
| show images | [vsx-peer] |     |
| ----------- | ---------- | --- |
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
| Parameter |     | Description |
| --------- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingtheprimaryandsecondaryimagesona6300switch:
| switch(config)# | show images |     |
| --------------- | ----------- | --- |
---------------------------------------------------------------------------
| AOS-CX Primary | Image |     |
| -------------- | ----- | --- |
338
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 722 MB        |              |
| Date    | : 2019-10-22    | 17:00:46 PDT |
SHA-256 : 4c84e49c0961fc56b5c7eab064750a333f1050212b7ce2fab587d13469d24cfa
---------------------------------------------------------------------------
| AOS-CX | Secondary Image |     |
| ------ | --------------- | --- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 722 MB        |              |
| Date    | : 2019-10-22    | 17:00:46 PDT |
SHA-256 : 4c84e49c0961fc56b5c7eab064750a333f1050212b7ce2fab587d13469d24cfa
| Default | Image : secondary |     |
| ------- | ----------------- | --- |
------------------------------------------------------
| Management | Module | 1/1 (Active) |
| ---------- | ------ | ------------ |
------------------------------------------------------
| Active       | Image      | : secondary              |
| ------------ | ---------- | ------------------------ |
| Service      | OS Version | : FL.01.05.0001-internal |
| BIOS Version |            | : FL.01.0001             |
Showingtheprimaryandsecondaryimagesona6400switch:
| switch(config)# | show | images |
| --------------- | ---- | ------ |
---------------------------------------------------------------------------
| AOS-CX | Primary Image |     |
| ------ | ------------- | --- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxxQ-2710-gd4ac39f30c9 |              |
| ------- | ---------------------------------- | ------------ |
| Size    | : 766 MB                           |              |
| Date    | : 2019-10-30                       | 17:22:01 PDT |
SHA-256 : e560ca9141f425d19024d122573c5ff730df2a9a726488212263b45ea00382cf
---------------------------------------------------------------------------
| AOS-CX | Secondary Image |     |
| ------ | --------------- | --- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 722 MB        |              |
| Date    | : 2019-10-21    | 19:36:26 PDT |
SHA-256 : 657e28adc1b512217ce780e3523c37c94db3d3420231deac1ab9aaa8324dc6b9
| Default | Image : secondary |     |
| ------- | ----------------- | --- |
------------------------------------------------------
| Management | Module | 1/1 (Active) |
| ---------- | ------ | ------------ |
------------------------------------------------------
| Active       | Image      | : secondary              |
| ------------ | ---------- | ------------------------ |
| Service      | OS Version | : FL.01.05.0001-internal |
| BIOS Version |            | : FL.01.0001             |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
Switchsystemandhardwarecommands|339

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show ip        | errors     |     |
| -------------- | ---------- | --- |
| show ip errors | [vsx-peer] |     |
Description
ShowsIPerrorstatisticsforpacketsreceivedbytheswitchsincetheswitchwaslastbooted.
| Parameter |     | Description |
| --------- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
IPerrorinfoaboutreceivedpacketsiscollectedfromeachactivelinecardontheswitchandispreserved
duringfailoverevents.Errorcountsareclearedwhentheswitchisrebooted.
Dropreasonsarethefollowing:
n Malformedpacket
ThepacketdoesnotconformtoTCP/IPprotocolstandardssuchaspacketlengthorinternetheaderlength.
Alargenumberofmalformedpacketscanindicatethattherearehardwaremalfunctionssuchasloosecables,
networkcardmalfunctions,orthataDOS(denialofservice)attackisoccurring.
| n IPaddress | error |     |
| ----------- | ----- | --- |
ThepackethasanerrorinthedestinationorsourceIPaddress.ExamplesofIPaddresserrorsincludethe
following:
o ThesourceIPaddressanddestinationIPaddressarethesame.
o ThereisnodestinationIPaddress.
o ThesourceIPaddressisamulticastIPaddress.
o TheforwardingheaderofanIPv6addressisempty.
ThereisnosourceIPaddressforanIPv6packet.
o
n InvalidTTLs
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
| Malformed | packets | 1   |
| --------- | ------- | --- |
340
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| IP address | errors |     | 10  |
| ---------- | ------ | --- | --- |
...
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 6400 | (#) |     |     |
| ---- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show        | module      |            |     |
| ----------- | ----------- | ---------- | --- |
| show module | [<SLOT-ID>] | [vsx-peer] |     |
Description
Showsinformationaboutinstalledlinemodulesandmanagementmodules.
| Parameter |     |     | Description                              |
| --------- | --- | --- | ---------------------------------------- |
| <SLOT-ID> |     |     | Specifiesthememberandslotnumbersinformat |
member/slot.Forexample,toshowthemodulein
member1,slot3,enter1/3.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Identifiesandshowsstatusinformationaboutthelinemodulesandmanagementmodulesthatare
installedintheswitch.
Ifyouusethe<SLOT-ID>parametertospecifyaslotthatdoesnothavealinemoduleinstalled,amessage
similartothefollowingexampleisdisplayed:
| Module 1/4 | is not physically | present. |     |
| ---------- | ----------------- | -------- | --- |
Toshowtheconfigurationinformation—ifany—associatedwiththatlinemoduleslot,usetheshow
running-configurationcommand.
Statusisoneofthefollowingvalues:
Active
Thismoduleistheactivemanagementmodule.
Standby
Thismoduleisthestandbymanagementmodule.
Deinitializing
Themoduleisbeingdeinitialized.
Switchsystemandhardwarecommands|341

Diagnostic
Themoduleisinastateusedfortroubleshooting.
Down
Themoduleisphysicallypresentbutispowereddown.
Empty
Themodulehardwareisnotinstalledinthechassis.
Failed
Themodulehasexperiencedanerrorandfailed.
Failover
Thismoduleisafabricmoduleoralinemodule,anditisintheprocessofconnectingtothenewactive
managementmoduleduringamanagementmodulefailoverevent.
Initializing
Themoduleisbeinginitialized.
Present
Themodulehardwareisinstalledinthechassis.
Ready
Themoduleisavailableforuse.
Updating
Afirmwareupdateisbeingappliedtothemodule.
Examples
Showingallinstalledmodules(Aruba6300switch):
| switch(config)# | show module |     |     |     |     |
| --------------- | ----------- | --- | --- | --- | --- |
| Management      | Modules     |     |     |     |     |
==================
| Product     |             |     |     | Serial |        |
| ----------- | ----------- | --- | --- | ------ | ------ |
| Name Number | Description |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
1/1 JL659A 6300M 48SR5 CL6 PoE 4SFP56 Swch ID9ZKHN090 Active (local)
Line Modules
============
| Product     |             |     |     | Serial |        |
| ----------- | ----------- | --- | --- | ------ | ------ |
| Name Number | Description |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL659A | 6300M 48SR5 | CL6 PoE 4SFP56 | Swch | ID9ZKHN090 | Ready |
| ---------- | ----------- | -------------- | ---- | ---------- | ----- |
Showingalinemodule(Aruba6400switch):
| switch# show      | module 1/3   |                   |            |              |     |
| ----------------- | ------------ | ----------------- | ---------- | ------------ | --- |
| Line module       | 1/3 is ready |                   |            |              |     |
| Admin state:      | Up           |                   |            |              |     |
| Description:      | 6400 24p     | 10GT 4SFP56 Mod   |            |              |     |
| Full Description: | 6400         | 24-port 10GBASE-T | and 4-port | SFP56 Module |     |
| Serial number:    | SG9ZKMS045   |                   |            |              |     |
| Product number:   | R0X42A       |                   |            |              |     |
| Power priority:   | 128          |                   |            |              |     |
Showingaslotthatdoesnotcontainalinemodule:
342
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| switch(config)# |     | show module    | 1/3     |     |
| --------------- | --- | -------------- | ------- | --- |
| Module 1/3      | is  | not physically | present |     |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show running-config |     |             |       |            |
| ------------------- | --- | ----------- | ----- | ---------- |
| show running-config |     | [<FEATURE>] | [all] | [vsx-peer] |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<FEATURE>
Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).Whenthejsonparameteris
used,thevsx-peerparameterisnotapplicable.
| all |     |     |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |
| --- | --- | --- | --- | ------------------------------------------------------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthecurrentrunningconfiguration:
| switch> | show           | running-config |     |     |
| ------- | -------------- | -------------- | --- | --- |
| Current | configuration: |                |     |     |
!
| !Version | AOS-CX | 10.0X.XXXX |     |     |
| -------- | ------ | ---------- | --- | --- |
!
| lldp enable     |     |                 |     |        |
| --------------- | --- | --------------- | --- | ------ |
| linecard-module |     | LC1 part-number |     | JL363A |
| vrf green       |     |                 |     |        |
!
!
!
Switchsystemandhardwarecommands|343

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
"long_term_time_period": "480",
"medium_term_high_threshold": "80",
"medium_term_normal_threshold": "60",
344
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

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
!
!
snmp-server vrf mgmt

Switch system and hardware commands | 345

!
!
!
!
!
vlan 1
switch(config)#
switch(config)#
| switch(config)# | show           | running-config | all |
| --------------- | -------------- | -------------- | --- |
| Current         | configuration: |                |     |
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show running-config |                 | current-context |     |
| ------------------- | --------------- | --------------- | --- |
| show running-config | current-context |                 |     |
Description
Showsthecurrentnon-defaultconfigurationrunningontheswitchinthecurrentcommandcontext.
Usage
Youcanenterthiscommandfromthefollowingconfigurationcontexts:
n Anychildoftheglobalconfiguration(config)context.Ifthechildcontexthasinstances—suchas
interfaces—youcanenterthecommandinthecontextofaspecificinstance.Supportforthiscommand
isprovidedforonelevelbelowtheconfigcontext.Forexample,enteringthiscommandforachildofa
childoftheconfigcontextnotsupported.Ifyouenterthecommandonachildoftheconfigcontext,
346
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

thecurrentconfigurationofthatcontextandthechildrenofthatcontextaredisplayed.
Theglobalconfiguration(config)context.Ifyouenterthiscommandintheglobalconfiguration(config)
n
context,itshowstherunningconfigurationoftheentireswitch.Usetheshow running-configuration
commandinstead.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingtherunningconfigurationforthecurrentinterface:
| switch(config-if)# | show running-config | current-context |
| ------------------ | ------------------- | --------------- |
interface 1/1/1
| vsx-sync qos vlans |     |     |
| ------------------ | --- | --- |
no shutdown
| description   | Example interface |     |
| ------------- | ----------------- | --- |
| vlan access 1 |                   |     |
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
switch(config-external-storage-nasfiles)# show running-config current-context
| external-storage | nasfiles |     |
| ---------------- | -------- | --- |
address 192.168.0.1
vrf default
| username nasuser |     |     |
| ---------------- | --- | --- |
password ciphertext AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
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
CommandHistory
| Release        | Modification |     |
| -------------- | ------------ | --- |
| 10.07orearlier | --           |     |
Switchsystemandhardwarecommands|347

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
configorachildof
forthiscommand.
config.SeeUsage.
show startup-config
| show startup-config | [json] |     |
| ------------------- | ------ | --- |
Description
Showsthecontentsofthestartupconfiguration.
Switchesinthefactory-defaultconfigurationdonothaveastartupconfigurationtodisplay.
| Parameter |     | Description                |
| --------- | --- | -------------------------- |
| json      |     | DisplayoutputinJSONformat. |
Examples
Showingthestartup-configurationinnon-JSONformatfora6300switch:
| switch(config)# | show startup-config |     |
| --------------- | ------------------- | --- |
| Startup         | configuration:      |     |
!
| !Version          | AOS-CX FL.xx.xx.xxxx |                     |
| ----------------- | -------------------- | ------------------- |
| !export-password: | default              |                     |
| hostname          | BLDG01-F1            |                     |
| user admin        | group administrators | password ciphertext |
AQBapWl8I2ZunZ43NE/8KlbQ7zYC4gTT6uSFYi6n6wyY9PdBYgAAACONCR/3+AcNvzRBch0DoG7W9z84LpJA
+6C9SKfNwCqi5/
nUPk/ZOvN91/EQXvPNkHtBtQWyYZqfkebbEH78VWRHfWZjApv4II9qmQfxpA79wEvzshdzZmuAKrm
| user ateam | group administrators | password ciphertext |
| ---------- | -------------------- | ------------------- |
AQBapcPqMXoF+H10NKrqAedXLvlSRwf4wUEL22hXGD6ZBhicYgAAAGsbh70DKg1u+Ze1wxgmDXjkGO3bseYi
R3LKQg66vrfrqR/
M3oLlliPdZDnq9XMMvCL+7jBbYhYes8+uDxuSTh8kdkd/qj3lo5FUuC5fENgCjU0YI1l7qtU+YEnsj
!
!
!
!
| radius-server | host 10.10.10.15 |     |
| ------------- | ---------------- | --- |
!
| radius dyn-authorization | enable      |     |
| ------------------------ | ----------- | --- |
| ssh server               | vrf default |     |
| ssh server               | vrf mgmt    |     |
!
!
!
!
!
| router ospf | 1   |     |
| ----------- | --- | --- |
348
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

| router-id | 1.63.63.1 |     |
| --------- | --------- | --- |
| area      | 0.0.0.0   |     |
vlan 1
vlan 66
| name | vlan66 |     |
| ---- | ------ | --- |
vlan 67
| name | vlan67 |     |
| ---- | ------ | --- |
vlan 999
| name | vlan999 |     |
| ---- | ------- | --- |
vlan 4000
spanning-tree
| interface   | mgmt         |     |
| ----------- | ------------ | --- |
| no shutdown |              |     |
| ip static   | 10.6.9.15/24 |     |
default-gateway 10.6.9.1
Showingthestartup-configurationinJSONformat:
| switch# | show startup-config | json |
| ------- | ------------------- | ---- |
| Startup | configuration:      |      |
{
| "AAA_Server_Group": | {   |     |
| ------------------- | --- | --- |
"local": {
|     | "group_name": | "local" |
| --- | ------------- | ------- |
},
"none": {
|     | "group_name": | "none" |
| --- | ------------- | ------ |
}
},
...
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show system | error-counter-monitor |     |
| ----------- | --------------------- | --- |
show system error-counter-monitor {basic <PORT-NUM> | extended} [vsx-peer]
Description
Showserrorcounterstatistics.
Switchsystemandhardwarecommands|349

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
CommandHistory
350
AOS-CX10.09FundamentalsGuide| (6300,6400SwitchSeries)

| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | forthiscommand. |     |     |
| ---- | --- | --------------- | --- | --- |
show system
| show system | [vsx-peer] |     |     |     |
| ----------- | ---------- | --- | --- | --- |
Description
Showsgeneralstatusinformationaboutthesystem.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemContact,SystemLocation,andSystemDescriptioncanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformationona6300switch:
| switch(config)#    | show system             |             |                |      |
| ------------------ | ----------------------- | ----------- | -------------- | ---- |
| Hostname           | : switch                |             |                |      |
| System Description | : FL.10.xx.xxxxx        |             |                |      |
| System Contact     | :                       |             |                |      |
| System Location    | :                       |             |                |      |
| Vendor             | : Aruba                 |             |                |      |
| Product            | Name : JL659A           | 6300M 48SR5 | CL6 PoE 4SFP56 | Swch |
| Chassis            | Serial Nbr : ID9ZKHN090 |             |                |      |
| Base MAC           | Address : 9020c2-245080 |             |                |      |
| AOS-CX Version     | : FL.10.xx.xxxx         |             |                |      |
| Time Zone          | : UTC                   |             |                |      |
| Up Time            | : 5 days,               | 15 hours,   | 33 minutes     |      |
| CPU Util           | (%) : 21                |             |                |      |
| Memory Usage       | (%) : 19                |             |                |      |
Showingsysteminformationoma6400switch:
Switchsystemandhardwarecommands|351

| switch(config)#    | show system             |         |     |     |
| ------------------ | ----------------------- | ------- | --- | --- |
| Hostname           | : switch                |         |     |     |
| System Description | : FL.10.xx.xxxxx        |         |     |     |
| System Contact     | :                       |         |     |     |
| System Location    | :                       |         |     |     |
| Vendor             | : Aruba                 |         |     |     |
| Product            | Name : R0X24A 6405      | Chassis |     |     |
| Chassis            | Serial Nbr : SG9ZKM7206 |         |     |     |
| Base MAC           | Address : 9020c2-dc4700 |         |     |     |
| AOS-CX Version     | : FL.10.xx.xxxxx        |         |     |     |
| Time Zone          | : UTC                   |         |     |     |
| Up Time            | : 32 minutes            |         |     |     |
| CPU Util           | (%) : 3                 |         |     |     |
| Memory Usage       | (%) : 10                |         |     |     |
BLDG02-F3(config)#
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show system | resource-utilization |     |     |     |
| ----------- | -------------------- | --- | --- | --- |
show system resource-utilization [daemon <DAEMON-NAME> | all | module <SLOT-ID> | standby]
[vsx-peer]
Description
ShowsinformationabouttheusageofsystemresourcessuchasCPU,memory,andopenfiledescriptors.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
daemon <DAEMON-NAME> Showsthefilteredresourceutilizationdatafortheprocess
specifiedby<DAEMON-NAME> only.
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
NOTE:
|     |     | Foralistofdaemonsthatlogevents,entershow | events | -d ?from |
| --- | --- | ---------------------------------------- | ------ | -------- |
aswitchpromptinthemanager(#)context.
352
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------- | --- | --- | --- |

| Parameter |     |     |     | Description                                  |     |     |     |
| --------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
| all       |     |     |     | ShowsutilizationinformationforallVSFmembers. |     |     |     |
module <SLOT-ID> Showsthefilteredresourceutilizationdataforthelinemodule
specifiedby<SLOT-ID>only.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingallsystemresourceutilizationdata:
| switch# show | system | resource-utilization |     |     |     |     |     |
| ------------ | ------ | -------------------- | --- | --- | --- | --- | --- |
System Resources:
| Processes:       | 70   |              |     |        |     |          |           |
| ---------------- | ---- | ------------ | --- | ------ | --- | -------- | --------- |
| CPU usage(%):    | 20   |              |     |        |     |          |           |
| Memory usage(%): |      | 25           |     |        |     |          |           |
| Open FD's:       | 1024 |              |     |        |     |          |           |
| Process          |      | CPU Usage(%) |     | Memory |     | Usage(%) | Open FD's |
-----------------------------------------------------------------------
| pmd         |     | 2   |     |     | 1   |     | 14  |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
| hpe-sysmond |     | 1   |     |     | 2   |     | 11  |
| hpe-mgmdd   |     | 0   |     |     | 1   |     | 5   |
...
Showingtheresourceutilizationdataforthepmdprocess:
| switch# show | system | resource-utilization |     | daemon |       | pmd  |      |
| ------------ | ------ | -------------------- | --- | ------ | ----- | ---- | ---- |
| Process      |        | CPU Usage            |     | Memory | Usage | Open | FD's |
-----------------------------------------------------------------------
| pmd |     | 2   |     | 1   |     | 14  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# show    | system      | resource-utilization |           |              |     |          |     |
| --------------- | ----------- | -------------------- | --------- | ------------ | --- | -------- | --- |
| System resource | utilization |                      | data poll | is currently |     | disabled |     |
Showingresourceutilizationdataforalinemodule:
| switch# show     | system      | resource-utilization |          | module       |     | 1/1 |     |
| ---------------- | ----------- | -------------------- | -------- | ------------ | --- | --- | --- |
| System Resource  | utilization |                      | for line | card module: |     | 1/1 |     |
| CPU usage(%):    | 0           |                      |          |              |     |     |     |
| Memory usage(%): |             | 35                   |          |              |     |     |     |
| Open FD's:       | 512         |                      |          |              |     |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
Switchsystemandhardwarecommands|353

CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show      | tech                |              |     |
| --------- | ------------------- | ------------ | --- |
| show tech | [basic | <FEATURE>] | [local-file] |     |
Description
Showsdetailedinformationaboutswitchfeaturesbyautomaticallyrunningtheshowcommandsassociated
withthefeature.Ifnoparametersarespecified,theshow techcommandshowsinformationaboutall
switchfeatures.Technicalsupportpersonnelusetheoutputfromthiscommandfortroubleshooting.
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
IfthecommandwasnotterminatedwithCtrl+C,attheendoftheoutput,theshow techcommandshows
thefollowing:
Thetimeconsumedtoexecutethecommand.
n
Thelistoffailedshowcommands,ifany.
n
Togetacopyofthelocaltextfilecontentcreatedwiththeshowtechcommandthatisusedwiththelocal-
| fileparameter,usethecopy |     |     | local-filecommand. |
| ------------------------ | --- | --- | ------------------ |
show-tech
Example
Showingthebasicsetofsysteminformation:
| switch# | show tech basic |     |     |
| ------- | --------------- | --- | --- |
=============================================================
| Show | Tech executed | on Wed Sep | 6 16:50:37 2017 |
| ---- | ------------- | ---------- | --------------- |
=============================================================
=============================================================
| [Begin] | Feature basic |     |     |
| ------- | ------------- | --- | --- |
=============================================================
*******************************
| Command | : show core-dump | all |     |
| ------- | ---------------- | --- | --- |
*******************************
| no  | core dumps are present |     |     |
| --- | ---------------------- | --- | --- |
354
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |
| ----------------------------- | --- | ----------------------- | --- |

...
=============================================================
| [End] Feature | basic |     |     |
| ------------- | ----- | --- | --- |
=============================================================
=============================================================
| 1 show | tech command failed |     |     |
| ------ | ------------------- | --- | --- |
=============================================================
| Failed  | command:     |     |     |
| ------- | ------------ | --- | --- |
| 1. show | boot-history |     |     |
=============================================================
| Show tech | took 3.000000 | seconds | for execution |
| --------- | ------------- | ------- | ------------- |
Directingtheoutputoftheshowtech basiccommandtothelocaltextfile:
| switch# | show tech basic | local-file |     |
| ------- | --------------- | ---------- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
| to copy-out | this file. |     |     |
| ----------- | ---------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Switchsystemandhardwarecommands|355

| switch>  | show usb |     |
| -------- | -------- | --- |
| Enabled: | No       |     |
| Mounted: | No       |     |
IfUSBhasbeenenabled,butnodevicehasbeenmounted:
| switch>  | show usb |     |
| -------- | -------- | --- |
| Enabled: | Yes      |     |
| Mounted: | No       |     |
IfUSBhasbeenenabledandadevicemounted:
| switch>  | show usb |     |
| -------- | -------- | --- |
| Enabled: | Yes      |     |
| Mounted: | Yes      |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show usb             | file-system |     |
| -------------------- | ----------- | --- |
| show usb file-system | [<PATH>]    |     |
Description
ShowsdirectorylistingsforamountedUSBdevice.Whenenteredwithoutthe<PATH>parameterthetop
leveldirectorytreeisshown.
| Parameter |     | Description |
| --------- | --- | ----------- |
<PATH> Specifiesthefilepathtoshow.Aleading"/"inthepathisoptional.
Usage
Addingaleading"/"asthefirstcharacterofthe<PATH>parameterisoptional.
Attemptingtoenter'..'asanypartofthe<PATH>willgenerateaninvalidpathargumenterror.Onlyfully-
qualifiedpathnamesaresupported.
Examples
Showingthetopleveldirectorytree:
356
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

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
Showingthecontentsofaspecificfolder:
| switch#    | show usb file-system |         | /dir1       |     |
| ---------- | -------------------- | ------- | ----------- | --- |
| total 32   |                      |         |             |     |
| drwxrwxrwx | 2 32768              | Mar 5   | 15:26 dir2  |     |
| -rwxrwxrwx | 1 0                  | Feb 5   | 18:08 test1 |     |
| switch#    | show usb file-system |         | dir1/dir2   |     |
| total 0    |                      |         |             |     |
| -rwxrwxrwx | 1 0 Feb              | 6 05:35 | test2       |     |
Attemptingtoenteraninvalidcharacterinthepath:
| switch# | show usb file-system |     | dir1/../.. |     |
| ------- | -------------------- | --- | ---------- | --- |
| Invalid | path argument        |     |            |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show version
| show version | [vsx-peer] |     |     |     |
| ------------ | ---------- | --- | --- | --- |
Switchsystemandhardwarecommands|357

Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingversioninformationfora6300switch:
| switch(config)# | show | version |     |     |     |
| --------------- | ---- | ------- | --- | --- | --- |
-----------------------------------------------------------------------------
AOS-CX
(c) Copyright 2017-2020 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx                                     |                          |          |     |     |
| ------- | --------------------------------------------------- | ------------------------ | -------- | --- | --- |
| Build   | Date : 2020-10-22                                   |                          | 17:00:46 | PDT |     |
| Build   | ID : AOS-CX:FL.xx.xx.xxxx:85c3c2f3d59e:201910222335 |                          |          |     |     |
| Build   | SHA : 85c3c2f3d59ec8318ba97178fad387aecb671b33      |                          |          |     |     |
| Active  | Image : secondary                                   |                          |          |     |     |
| Service | OS Version                                          | : FL.01.05.0001-internal |          |     |     |
| BIOS    | Version                                             | : FL.01.0001             |          |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| system                      | resource-utilization |     |               |     | poll-interval |
| --------------------------- | -------------------- | --- | ------------- | --- | ------------- |
| system resource-utilization |                      |     | poll-interval |     | <SECONDS>     |
Description
ConfiguresthepollingintervalforsystemresourceinformationcollectionandrecordingsuchasCPUand
memoryusage.
358
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- |

| Parameter |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
<SECONDS> Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Example
Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |     | system | resource-utilization |     |     | poll-interval |     | 20  |     |
| --------------- | --- | ------ | -------------------- | --- | --- | ------------- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
top cpu
top cpu
Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch#        | top cpu   |            |          |              |          |            |             |          |      |
| -------------- | --------- | ---------- | -------- | ------------ | -------- | ---------- | ----------- | -------- | ---- |
| top - 09:42:55 |           | up 3 min,  | 3 users, | load         | average: |            | 3.44, 3.78, |          | 1.70 |
| Tasks:         | 76 total, | 2 running, |          | 74 sleeping, |          | 0 stopped, |             | 0 zombie |      |
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used, 661948 buff/cache
| KiB Swap: |     | 0 total, |      | 0 free, |     | 0      | used, | 2859196 | avail Mem     |
| --------- | --- | -------- | ---- | ------- | --- | ------ | ----- | ------- | ------------- |
| PID USER  |     | PRI NI   | VIRT | RES     | SHR | S %CPU | %MEM  |         | TIME+ COMMAND |
...
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |     |
CommandInformation
Switchsystemandhardwarecommands|359

| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
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
| switch>        | top memory |            |          |              |          |            |             |      |
| -------------- | ---------- | ---------- | -------- | ------------ | -------- | ---------- | ----------- | ---- |
| top - 09:42:55 |            | up 3 min,  | 3 users, | load         | average: |            | 3.44, 3.78, | 1.70 |
| Tasks:         | 76 total,  | 2 running, |          | 74 sleeping, |          | 0 stopped, | 0 zombie    |      |
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used, 661948 buff/cache
| KiB Swap: |     | 0 total, |      | 0 free, |     | 0      | used, 2859196 | avail Mem     |
| --------- | --- | -------- | ---- | ------- | --- | ------ | ------------- | ------------- |
| PID USER  |     | PRI NI   | VIRT | RES     | SHR | S %CPU | %MEM          | TIME+ COMMAND |
...
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
360
| AOS-CX10.09FundamentalsGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |

EnablingUSBports:
| switch(config)# | usb |     |
| --------------- | --- | --- |
DisablingUSBportswhenaUSBdriveismounted:
| switch(config)# | no usb |     |
| --------------- | ------ | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| usb mount    | | unmount |     |
| ------------ | --------- | --- |
| usb {mount | | unmount}  |     |
Description
EnablesordisablestheinsertedUSBdrive.
| Parameter |     | Description                                         |
| --------- | --- | --------------------------------------------------- |
| mount     |     | EnablestheinsertedUSBdrive.                         |
| unmount   |     | DisablestheinsertedUSBdriveinpreparationforremoval. |
Usage
IfUSBhasbeenenabledintheconfiguration,theUSBportontheactivemanagementmoduleisavailable
formountingaUSBdrive.TheUSBportonthestandbymanagementmoduleisnotavailable.
AninsertedUSBdrivemustbemountedeachtimetheswitchbootsorfailsovertoadifferentmanagement
module.
AUSBdrivemustbeunmountedbeforeremoval.
ThesupportedUSBfilesystemsareFAT16andFAT32.
Examples
MountingaUSBdriveintheUSBport:
switch#
usb mount
UnmountingaUSBdrive:
Switchsystemandhardwarecommands|361

| switch# | usb unmount |     |
| ------- | ----------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
362
| AOS-CX10.09FundamentalsGuide| | (6300,6400SwitchSeries) |     |
| ----------------------------- | ----------------------- | --- |

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

Airheads social
forums and
Knowledge
Base

AOS-CX Switch
Software
Documentation
Portal

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

363

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.htm

Aruba
Hardware
Documentation
and
Translations
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

Support and Other Resources | 364

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

AOS-CX 10.09 Fundamentals Guide | (6300, 6400 Switch Series)

365