AOS-CX 10.15.xxxx
Fundamentals Guide

4100i, 6000, 6100 Switch Series

Published: May 2025

Version: 1

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

3

Contents
| About this                                 | document                             | 10  |
| ------------------------------------------ | ------------------------------------ | --- |
| Applicableproducts                         |                                      | 10  |
| Latestversionavailableonline               |                                      | 10  |
| Commandsyntaxnotationconventions           |                                      | 10  |
| Abouttheexamples                           |                                      | 11  |
| Identifyingswitchportsandinterfaces        |                                      | 11  |
| About AOS-CX                               |                                      | 13  |
| AOS-CXsystemdatabases                      |                                      | 13  |
| NetworkAnalyticsEngineintroduction         |                                      | 14  |
| AOS-CXCLI                                  |                                      | 14  |
| HPE ArubaNetworkingNetEdit                 |                                      | 14  |
| Ansiblemodules                             |                                      | 14  |
| AOS-CXWebUI                                |                                      | 15  |
| AOS-CXRESTAPI                              |                                      | 15  |
| In-bandmanagement                          |                                      | 15  |
| SNMP-basedmanagementsupport                |                                      | 15  |
| Useraccounts                               |                                      | 15  |
| Initial Configuration                      |                                      | 17  |
| InitialconfigurationusingZTP               |                                      | 17  |
| InitialconfigurationusingtheCLI            |                                      | 17  |
|                                            | Connectingtotheconsoleport           | 18  |
|                                            | Connectingtothein-bandmanagementport | 18  |
|                                            | ConfigureusingDHCPorstaticIP         | 19  |
|                                            | Loggingintotheswitchforthefirsttime  | 20  |
|                                            | SettingswitchtimeusingtheNTPclient   | 20  |
| Configuringbanners                         |                                      | 21  |
| UsingtheWebUI                              |                                      | 22  |
| Configuringthein-bandmanagementinterface   |                                      | 22  |
| Restoringtheswitchtofactorydefaultsettings |                                      | 23  |
| NTPcommands                                |                                      | 24  |
|                                            | ntpauthentication                    | 24  |
|                                            | ntpauthentication-key                | 25  |
|                                            | ntpdisable                           | 27  |
|                                            | ntpenable                            | 27  |
|                                            | ntpserver                            | 28  |
|                                            | ntptrusted-key                       | 30  |
|                                            | ntpvrf                               | 30  |
|                                            | showntpassociations                  | 31  |
|                                            | showntpauthentication-keys           | 32  |
|                                            | showntpservers                       | 33  |
|                                            | showntpstatistics                    | 33  |
|                                            | showntpstatus                        | 34  |
| Telnet access                              |                                      | 36  |
| Telnetcommands                             |                                      | 36  |
|                                            | showtelnetserver                     | 36  |
|                                            | showtelnetserversessions             | 37  |
4
AOS-CX10.15.xxxxFundamentalsGuide| (4100i,6000,6100SwitchSeries)

|                                   | telnetserver                               |           | 38  |
| --------------------------------- | ------------------------------------------ | --------- | --- |
| Interface                         | configuration                              |           | 39  |
| Configuringalayer2interface       |                                            |           | 39  |
| SinglesourceIPaddress             |                                            |           | 39  |
| Unsupportedtransceiversupport     |                                            |           | 39  |
| Configuringaninterfacepersona     |                                            |           | 40  |
|                                   | Modes                                      |           | 41  |
|                                   | Predefinedandcustompersonanames            |           | 41  |
|                                   | Creatingandconfiguringaninterfacepersona   |           | 41  |
|                                   | Examples                                   |           | 41  |
| Monitormode                       |                                            |           | 42  |
| Interfacecommands                 |                                            |           | 42  |
|                                   | allow-unsupported-transceiver              |           | 42  |
|                                   | defaultinterface                           |           | 44  |
|                                   | description(interface)                     |           | 45  |
|                                   | energy-efficient-ethernet                  |           | 46  |
|                                   | flow-control                               |           | 46  |
|                                   | interface(port)                            |           | 47  |
|                                   | interfacevlan                              |           | 48  |
|                                   | ipaddress(interface)                       |           | 49  |
|                                   | ipmtu                                      |           | 50  |
|                                   | ipsource-interface                         |           | 50  |
|                                   | iptcpmss                                   |           | 51  |
|                                   | ipv6address                                |           | 52  |
|                                   | ipv6source-interface                       |           | 53  |
|                                   | ipv6tcpmss                                 |           | 55  |
|                                   | mtu                                        |           | 55  |
|                                   | persona                                    |           | 56  |
|                                   | rate-interval                              |           | 59  |
|                                   | showallow-unsupported-transceiver          |           | 60  |
|                                   | showinterface                              |           | 61  |
|                                   | showinterfacedom                           |           | 67  |
|                                   | showinterfaceenergy-efficientethernet      |           | 67  |
|                                   | showinterfaceflow-control                  |           | 68  |
|                                   | showinterfacelink-diagnostics              |           | 73  |
|                                   | showinterfacestatistics                    |           | 76  |
|                                   | showinterfacetransceiver                   |           | 79  |
|                                   | showinterfaceutilization                   |           | 81  |
|                                   | showipinterface                            |           | 82  |
|                                   | showipsource-interface                     |           | 83  |
|                                   | showipv6interface                          |           | 84  |
|                                   | showipv6source-interface                   |           | 86  |
|                                   | shutdown(interface)                        |           | 87  |
|                                   | speed                                      |           | 87  |
| Source                            | interface                                  | selection | 91  |
| Source-interfaceselectioncommands |                                            |           | 91  |
|                                   | ipsource-interface(protocol<ip-addr>)      |           | 91  |
|                                   | ipsource-interface                         |           | 93  |
|                                   | ipv6source-interface (<protocol><ip-addr>) |           | 95  |
|                                   | ipv6source-interfacedns                    |           | 96  |
|                                   | ipv6source-interface                       |           | 98  |
|                                   | showipsource-interface                     |           | 100 |
|                                   | showipv6source-interface                   |           | 102 |
|                                   | showrunning-config                         |           | 104 |
|5

VLANs

Configuration and firmware management

Upgrade and downgrade scenarios

Upgrades
Downgrades
Limitations

Hot-patch software
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
copy <REMOTE-URL> startup-config|running-config
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

boot set-default
boot system
show boot-history

Firmware management commands

copy {primary | secondary} <REMOTE-URL>
copy {primary | secondary} <FIRMWARE-FILENAME>
copy primary secondary
copy <REMOTE-URL>
copy secondary primary
copy <STORAGE-URL>
copy hot-patch

106

107
107
107
107
107
108
110
110
110
110
110
110
111
111
111
111
111
112
113
115
116
117
118
118
119
120
121
122
124
125
126
127
128
129
130
133
133
134
135
135
136
137
138
138
138
140
142
142
143
144
144
146
147
148

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

6

|                                         | hot-patch                                          |                   |             | 149 |
| --------------------------------------- | -------------------------------------------------- | ----------------- | ----------- | --- |
|                                         | showhot-patch                                      |                   |             | 150 |
| Dynamic                                 | Segmentation                                       |                   |             | 152 |
| SNMP                                    |                                                    |                   |             | 153 |
| ConfiguringSNMP                         |                                                    |                   |             | 153 |
| HPE Aruba                               | Networking                                         | Central           | integration | 155 |
| ConnectingtoHPE ArubaNetworkingCentral  |                                                    |                   |             | 155 |
| CustomCAcertificate                     |                                                    |                   |             | 155 |
| SupportmodeinHPE ArubaNetworkingCentral |                                                    |                   |             | 156 |
| OneTouchProvisioning                    |                                                    |                   |             | 156 |
| HPE ArubaNetworkingCentralcommands      |                                                    |                   |             | 158 |
|                                         | hpe-anw-central                                    |                   |             | 158 |
|                                         | hpe-anw-centralsupport-mode                        |                   |             | 158 |
|                                         | configuration-lockoutcentralmanaged                |                   |             | 159 |
|                                         | diag-dumprestbasic                                 |                   |             | 160 |
|                                         | disable                                            |                   |             | 161 |
|                                         | enable(HPE ArubaNetworkingCentral)                 |                   |             | 162 |
|                                         | location-override                                  |                   |             | 163 |
|                                         | location-override-alternative                      |                   |             | 165 |
|                                         | showhpe-anw-central                                |                   |             | 166 |
|                                         | showrunning-configcurrent-context                  |                   |             | 169 |
| Port                                    | filtering                                          |                   |             | 171 |
| Portfilteringcommands                   |                                                    |                   |             | 171 |
|                                         | portfilter                                         |                   |             | 171 |
|                                         | showportfilter                                     |                   |             | 173 |
| DNS                                     |                                                    |                   |             | 175 |
| Configuration                           |                                                    |                   |             | 175 |
| DNSclient                               |                                                    |                   |             | 175 |
| ConfiguringtheDNSclient                 |                                                    |                   |             | 175 |
| DNSclientcommands                       |                                                    |                   |             | 176 |
|                                         | ipdnsdomain-list                                   |                   |             | 176 |
|                                         | ipdnsdomain-name                                   |                   |             | 177 |
|                                         | ipdnshost                                          |                   |             | 178 |
|                                         | ipdnsserveraddress                                 |                   |             | 179 |
|                                         | showipdns                                          |                   |             | 180 |
| Device                                  | discovery                                          | and configuration |             | 181 |
| Deviceprofiles                          |                                                    |                   |             | 181 |
|                                         | ConfiguringadeviceprofileforLLDP                   |                   |             | 182 |
|                                         | ConfiguringadeviceprofileforCDP                    |                   |             | 182 |
|                                         | ConfiguringadeviceprofileforlocalMACmatch          |                   |             | 182 |
|                                         | DeviceProfileUsageConsiderations                   |                   |             | 183 |
|                                         | Deviceprofilecommands                              |                   |             | 184 |
|                                         | aaaauthenticationport-accessallow-cdp-auth         |                   |             | 184 |
|                                         | aaaauthenticationport-accessallow-cdp-bpdu         |                   |             | 185 |
|                                         | aaaauthenticationport-accessallow-cdp-proxy-logoff |                   |             | 186 |
|                                         | aaaauthenticationport-accessallow-lldp-bpdu        |                   |             | 187 |
|                                         | associatecdp-group                                 |                   |             | 189 |
|                                         | associatelldp-group                                |                   |             | 190 |
|                                         | associatemac-group                                 |                   |             | 191 |
|7

associate role
disable (port-access device-profile)
enable (port-access device-profile)
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
LLDP EEE
Configuring the LLDP agent
LLDP commands

clear lldp neighbors
clear lldp statistics
lldp
lldp dot3
lldp dot3 eee
lldp dot3 mfs
lldp holdtime-multiplier
lldp management-address vlan
lldp management-ip-address
lldp management-ipv6-address
lldp med
lldp med location
lldp receive
lldp reinit
lldp select-tlv
lldp timer
lldp transmit
lldp txdelay
lldp trap enable
show lldp configuration
show lldp local-device
show lldp neighbor-info
show lldp neighbor-info detail
show lldp statistics
show lldp tlv

Cisco Discovery Protocol (CDP)

CDP support
CDP commands
cdp (global)
clear cdp counters
clear cdp neighbor-info
show cdp
show cdp neighbor-info
show cdp traffic
show cdp voice-vlan mode

191
192
193
193
195
196
201
202
203
205
209
210
211
212
213
214
215
217
217
217
218
218
219
219
220
221
221
222
223
224
225
226
227
229
229
230
231
233
233
234
236
238
240
242
244
246
247
247
247
247
248
249
249
250
251
252

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

8

| Zero                                                | Touch Provisioning |                 |          | 253 |
| --------------------------------------------------- | ------------------ | --------------- | -------- | --- |
| ZTPconnectionpriorities                             |                    |                 |          | 253 |
| ZTPsupport                                          |                    |                 |          | 253 |
| SettingupZTPonatrustednetwork                       |                    |                 |          | 254 |
| ZTPprocessduringswitchboot                          |                    |                 |          | 255 |
| ZTPcommands                                         |                    |                 |          | 256 |
|                                                     | showztpinformation |                 |          | 256 |
|                                                     | ztpforceprovision  |                 |          | 259 |
| Switch                                              | system             | and hardware    | commands | 261 |
| clearevents                                         |                    |                 |          | 261 |
| consolebaud-rate                                    |                    |                 |          | 261 |
| domain-name                                         |                    |                 |          | 262 |
| front-panel-securityfactory-reset                   |                    |                 |          | 263 |
| hostname                                            |                    |                 |          | 264 |
| powerconsumption-average-period                     |                    |                 |          | 265 |
| showboot-history                                    |                    |                 |          | 266 |
| showcapacities                                      |                    |                 |          | 268 |
| showcapacities-status                               |                    |                 |          | 275 |
| showconsole                                         |                    |                 |          | 276 |
| showcore-dump                                       |                    |                 |          | 277 |
| showdeprecatedcommands                              |                    |                 |          | 278 |
| showdomain-name                                     |                    |                 |          | 280 |
| showenvironmentfan                                  |                    |                 |          | 280 |
| showenvironmentled                                  |                    |                 |          | 282 |
| showenvironmentpower-consumption                    |                    |                 |          | 282 |
| showenvironmentpower-consumptionpower-over-ethernet |                    |                 |          | 285 |
| showenvironmentpower-supply                         |                    |                 |          | 289 |
| showenvironmenttemperature                          |                    |                 |          | 290 |
| showevents                                          |                    |                 |          | 291 |
| showfront-panel-securitystatus                      |                    |                 |          | 294 |
| showhostname                                        |                    |                 |          | 295 |
| showimages                                          |                    |                 |          | 296 |
| showmodule                                          |                    |                 |          | 297 |
| showrunning-config                                  |                    |                 |          | 298 |
| showrunning-configcurrent-context                   |                    |                 |          | 303 |
| showstartup-config                                  |                    |                 |          | 304 |
| showsystem                                          |                    |                 |          | 305 |
| showsystemresource-utilization                      |                    |                 |          | 306 |
| showtech                                            |                    |                 |          | 308 |
| showusb                                             |                    |                 |          | 309 |
| showusbfile-system                                  |                    |                 |          | 310 |
| showversion                                         |                    |                 |          | 312 |
| systemresource-utilizationpoll-interval             |                    |                 |          | 313 |
| topcpu                                              |                    |                 |          | 313 |
| topmemory                                           |                    |                 |          | 314 |
| usb                                                 |                    |                 |          | 315 |
| usbmount|unmount                                    |                    |                 |          | 315 |
| Support                                             | and                | Other Resources |          | 317 |
| AccessingHPE ArubaNetworkingSupport                 |                    |                 |          | 317 |
| AccessingUpdates                                    |                    |                 |          | 318 |
| WarrantyInformation                                 |                    |                 |          | 318 |
| RegulatoryInformation                               |                    |                 |          | 318 |
| DocumentationFeedback                               |                    |                 |          | 318 |
|9

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

n HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

n HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

10

| Convention |     | Usage |     |
| ---------- | --- | ----- | --- |
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
| …or |     | Ellipsis:                                                |     |
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
format:member/slot/port.
| On the HPE Aruba | Networking | 4100i Switch | Series |
| ---------------- | ---------- | ------------ | ------ |
Aboutthisdocument|11

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

12

Chapter 2

About AOS-CX

About AOS-CX

AOS-CX is a new, modern, fully programmable operating system built using a database-centric design
that ensures higher availability and dynamic software process changes for reduced downtime. In
addition to robust hardware reliability, the AOS-CX operating system includes additional software
elements not available with traditional systems, including:

n Automated visibility to help IT organizations scale: The HPE Aruba Networking Network Analytics
Engine allows IT to monitor and troubleshoot network, system, application, and security-related
issues easily through simple scripts. This engine comes with a built-in time series database that
enables customers and developers to create software modules that allow historical troubleshooting,
as well as analysis of historical trends to predict and avoid future problems due to scale, security, and
performance bottlenecks.

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
record. The time series database makes the data seamlessly available to HPE Aruba Networking
Network Analytics Engine agents that use rules that evaluate network conditions over time. Time-series
data about the resources monitored by agents are automatically collected and presented in graphs in
the switch Web UI.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

13

Network Analytics Engine introduction

The HPE Aruba Networking Network Analytics Engine is a first-of-its-kind built-in framework for network
assurance and remediation. Combining the full automation and deep visibility capabilities of the AOS-CX
operating system, this unique framework enables monitoring, collecting network data, evaluating
conditions, and taking corrective actions through simple scripting agents.

This engine is integrated with the AOS-CX system configuration and time series databases, enabling you
to examine historical trends and predict future problems due to scale, security, and performance
bottlenecks. With that information, you can create software modules that automatically detect such
issues and take appropriate actions.

With the faster network insights and automation provided by the HPE Aruba Networking Network
Analytics Engine, you can reduce the time spent on manual tasks and address current and future
demands driven by Mobility and IoT.

AOS-CX CLI

The AOS-CX CLI is an industry standard text-based command-line interface with hierarchical structure
designed to reduce training time and increase productivity in multivendor installations.

The CLI gives you access to the full set of commands for the switch while providing the same password
protection that is used in the Web UI. You can use the CLI to configure, manage, and monitor devices
running the AOS-CX operating system.

HPE Aruba Networking NetEdit

HPE Aruba Networking NetEdit enables the automation of multidevice configuration change workflows
without the overhead of programming.

The key capabilities of NetEdit include the following:

n Intelligent configuration with validation for consistency and compliance

n Time savings by simultaneously viewing and editing multiple configurations

n Customized validation tests for corporate compliance and network design

n Automated large-scale configuration deployment without programming

n Ability to track changes to hardware, software, and configurations (whether made through NetEdit or

directly on the switch) with automated versioning

For more information about HPE Aruba Networking NetEdit, search for NetEdit at the following website:

www.hpe.com/support/hpesc

Ansible modules

Ansible is an open-source IT automation platform.

HPE Aruba Networking publishes a set of Ansible configuration management modules designed for
switches running AOS-CX software. The modules are available from the following places:

n The arubanetworks.aoscx_role role in the Ansible Galaxy at:

https://galaxy.ansible.com/arubanetworks/aoscx_role

n The aoscx-ansible-role at the following GitHub repository: https://github.com/aruba/aoscx-ansible-

role

About AOS-CX | 14

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
programmability—combined with the HPE Aruba Networking Network Analytics Engine—accelerates
network administrator understanding of and response to network issues.

The AOS-CX REST API enables programmatic access to the AOS-CX configuration and state database at
the heart of the switch. By using a structured model, changes to the content and formatting of the CLI
output do not affect the programs you write. And because the configuration is stored in a structured
database instead of a text file, rolling back changes is easier than ever, thus dramatically reducing a risk
of downtime and performance issues.

The AOS-CX REST API is a web service that performs operations on switch resources using HTTPS POST,
GET, PUT, DELETE, and PATCH methods.

A switch resource is indicated by its Uniform Resource Identifier (URI). A URI can be made up of several
components, including the host name or IP address, port number, the path, and an optional query
string. The AOS-CX operating system includes the AOS-CX REST API Reference, which is a web interface
based on the Swagger UI. The AOS-CX REST API Reference provides the reference documentation for the
REST API, including resources URIs, models, methods, and errors. The AOS-CX REST API Reference shows
most of the supported read and write methods for all switch resources.

In-band management

Management communications with a managed switch can be:

In band

In-band management communications occur through ports on the line modules of the switch, using
common communications protocols such as SSH and SNMP.

When you use an in-band management connection, management traffic from that connection uses
the same network infrastructure as user data. User data uses the data plane, which is responsible
for moving data from source to destination. Management traffic that uses the data plane is more
likely to be affected by traffic congestion and other issues affecting the user network.

SNMP-based management support

The AOS-CX operating system provides SNMP read access to the switch. SNMP support includes support
of industry-standard MIB (Management Information Base) plus private extensions, including SNMP
events, alarms, history, statistics groups, and a private alarm extension group. SNMP access is disabled
by default.

User accounts

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

15

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

1. Connect the network to a data port.

See the Installation Guide for switch to determine the location of the switch ports.

2.

If the switch is powered on, power off the switch.

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image
is being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

Initial configuration using the CLI

This procedure describes how to connect to the switch for the first time and configure basic operational
settings using the CLI. In this procedure, you use a computer to connect to the switch using the either
the console port or management port.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

17

Procedure
1. Connecttotheconsoleportorthemanagementport.
2. Logintotheswitchforthefirsttime.
3. ConfigureswitchtimeusingtheNTPclient.
| Connecting |     | to the | console | port |     |
| ---------- | --- | ------ | ------- | ---- | --- |
Prerequisites
n Aswitchinstalledasdescribedinitshardwareinstallationguide.
Acomputerwithterminalemulationsoftware.
n
Procedure
1. Starttheterminalemulationsoftwareonthecomputerandconfigureanewserialsessionwith
thefollowingsettings:
| n   | Speed:115200bps  |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- |
| n   | Databits:8       |     |     |     |     |
| n   | Stopbits:1       |     |     |     |     |
| n   | Parity:None      |     |     |     |     |
| n   | Flowcontrol:None |     |     |     |     |
2. Starttheterminalemulationsession.
3. PressEnteronce.Iftheconnectionissuccessful,youarepromptedtologin.
| Optional | console | port | speed setting |     |     |
| -------- | ------- | ---- | ------------- | --- | --- |
Ifdesired,theconsoleportspeedcanbesetwiththeconsole baud-ratecommand.Forexample,
settingtheconsoleportspeedto9600bps:
| switch(config)# |     |     | console baud-rate | 9600 |     |
| --------------- | --- | --- | ----------------- | ---- | --- |
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
| settings |     | are updated | to match | the baud rate | of the switch. |
| -------- | --- | ----------- | -------- | ------------- | -------------- |
| Continue |     | (y/n)?      | y        |               |                |
Showingtheconsoleportcurrentspeed:
| switch# | show  | console |     |     |     |
| ------- | ----- | ------- | --- | --- | --- |
| Baud    | Rate: | 9600    |     |     |     |
Fordetailsontheconsole baud-rateandshow consolecommands,seeSwitchsystemandhardware
commands.
| Connecting |     | to the | in-band | management | port |
| ---------- | --- | ------ | ------- | ---------- | ---- |
Prerequisites
n TwoEthernetcables
n SSHclientsoftware
InitialConfiguration |18

Procedure
1. Bydefault,the in-bandmanagementinterfaceissettoautomaticallyobtainanIPaddressfroma
DHCPserver,andSSHsupportisenabled.IfthereisnoDHCPserveronyournetwork,youmust
configureastaticaddressonthein-bandmanagementinterface:
| a.  | Connecttotheconsoleport                                  |                 |     |     |     |     |
| --- | -------------------------------------------------------- | --------------- | --- | --- | --- | --- |
| b.  | Configureusing                                           | DHCPorstaticIP. |     |     |     |     |
| c.  | Configurethein-bandmanagementinterfaceandinterfaceVLAN1. |                 |     |     |     |     |
2. UseanEthernetcabletoconnectthemanagementporttoyournetwork.
3. UseanEthernetcabletoconnectyourcomputertothesamenetwork.
4. StartyourSSHclientsoftwareandconfigureanewsessionusingtheaddressassignedtothe in-
bandmanagementinterface.(Ifthe in-bandmanagementinterfaceissettooperateasaDHCP
client,retrievetheIPaddressassignedtothe in-bandmanagementinterfacefromyourDHCP
server.)
5. Startthesession.Iftheconnectionissuccessful,youarepromptedtologin.
| Configure | using DHCP | or  | static | IP  |     |     |
| --------- | ---------- | --- | ------ | --- | --- | --- |
Userscanuseanydataportsforin-bandmanagementpurposes.IPDHCPissupportedoninterfaceVLAN1only.
AllswitchportsarepartofaccessVLAN1bydefault.StaticIPaddressandIPDHCPconfigurationcanco-existon
VLAN1,howeverstaticaddressestakeprecedencewheneverconfigured.
DHCPConfiguration
| switch#:                | config |      |             |            |      |     |
| ----------------------- | ------ | ---- | ----------- | ---------- | ---- | --- |
| switch(config)#:        |        | vlan | 1           |            |      |     |
| Switch(config-vlan-1)#: |        |      | description | Management | VLAN |     |
| Switch(config-vlan-1)#: |        |      | end         |            |      |     |
Switch#
!
| Switch(config)#:    |     | interface   | 1/1/1    |                    |      |     |
| ------------------- | --- | ----------- | -------- | ------------------ | ---- | --- |
| Switch(config-if)#: |     | description |          | IN-BAND Management | Port |     |
| Switch(config-if)#: |     | vlan        | access   | 1                  |      |     |
| Switch(config-if)#: |     | no          | shutdown |                    |      |     |
| Switch(config-if)#: |     | end         |          |                    |      |     |
Switch#
!
| Switch(config)#: |     | interface | vlan | 1   |     |     |
| ---------------- | --- | --------- | ---- | --- | --- | --- |
Switch(config-if-vlan)#:
|                          |     |     | description | IN-BAND | Management | Interface |
| ------------------------ | --- | --- | ----------- | ------- | ---------- | --------- |
| Switch(config-if-vlan)#: |     |     | ip dhcp     |         |            |           |
| Switch(config-if-vlan)#: |     |     | no shutdown |         |            |           |
| Switch(config-if-vlan)#: |     |     | end         |         |            |           |
Switch#
!
WithoutDHCPConfiguration
| switch#:         | config |      |     |     |     |     |
| ---------------- | ------ | ---- | --- | --- | --- | --- |
| switch(config)#: |        | vlan | 1   |     |     |     |
Switch(config-vlan-1)#:
|                         |     |     | description | Management | VLAN |     |
| ----------------------- | --- | --- | ----------- | ---------- | ---- | --- |
| Switch(config-vlan-1)#: |     |     | end         |            |      |     |
Switch#
!
| Switch(config)#: |     | interface | 1/1/1 |     |     |     |
| ---------------- | --- | --------- | ----- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 19

| Switch(config-if)#: |     |     | description | IN-BAND | Management | Port |
| ------------------- | --- | --- | ----------- | ------- | ---------- | ---- |
Switch(config-if)#:
|                     |     |     | vlan access | 1   |     |     |
| ------------------- | --- | --- | ----------- | --- | --- | --- |
| Switch(config-if)#: |     |     | no shutdown |     |     |     |
| Switch(config-if)#: |     |     | end         |     |     |     |
Switch#
!
| Switch(config)#: |     | interface | vlan | 1   |     |     |
| ---------------- | --- | --------- | ---- | --- | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | no ip       | dhcp            |     |     |
| ------------------------ | --- | --- | ----------- | --------------- | --- | --- |
| Switch(config-if-vlan)#: |     |     | ip address  | 192.168.10.1/24 |     |     |
| Switch(config-if-vlan)#: |     |     | no shutdown |                 |     |     |
Switch(config-if-vlan)#:
end
Switch#
| Logging | into | the switch | for | the first | time |     |
| ------- | ---- | ---------- | --- | --------- | ---- | --- |
Thefirsttimeyoulogintotheswitchyoumustusethedefaultadministratoraccount.Thisaccounthas
nopassword,soyouwillbepromptedonlogintodefineonetosafeguardtheswitch.
Procedure
1. Whenpromptedtologin,specifyadmin.Whenpromptedforthepassword,pressENTER.(By
default,nopasswordisdefined.)
Forexample:
|     | switch | login: | admin |     |     |     |
| --- | ------ | ------ | ----- | --- | --- | --- |
password:
2. Defineapasswordfortheadminaccount.Thepasswordcancontainupto32alphanumeric
charactersintherangeASCII32to127,whichincludesspecialcharacterssuchasasterisk(*),
ampersand(&),exclamationpoint(!),dash(-),underscore(_),andquestionmark(?).
Forexample:
|     | Please    | configure     | the 'admin' | user account |     | password. |
| --- | --------- | ------------- | ----------- | ------------ | --- | --------- |
|     | Enter new | password:     | *******     |              |     |           |
|     | Confirm   | new password: |             |              |     |           |
*******
switch#
3. Youareplacedintothemanagercommandcontext,whichisidentifiedbytheprompt:switch#,
whereswitchisthemodelnumberoftheswitch.Enterthecommandconfigtochangetothe
globalconfigurationcontextconfig.
Forexample:
|     | switch# | config |     |     |     |     |
| --- | ------- | ------ | --- | --- | --- | --- |
switch(config)#
| Setting | switch | time | using | the NTP | client |     |
| ------- | ------ | ---- | ----- | ------- | ------ | --- |
Prerequisites
InitialConfiguration |20

n TheIPaddressordomainnameofanNTPserver.
n IftheNTPserverusesauthentication,obtainthepasswordrequiredtocommunicatewiththeNTP
server.
Procedure
1. IftheNTPserverrequiresauthentication,definetheauthenticationkeyfortheNTPclientwiththe
|     | commandntp                            | authentication. |     |     |     |     |         |     |     |     |
| --- | ------------------------------------- | --------------- | --- | --- | --- | --- | ------- | --- | --- | --- |
| 2.  | ConfigureanNTPserverwiththecommandntp |                 |     |     |     |     | server. |     |     |     |
3. Bydefault,NTPtrafficissentonthedefaultVRF.
4. ReviewyourNTPconfigurationsettingswiththecommandsshow ntp serversandshow ntp
status.
5. Seethecurrentswitchtime,date,andtimezonewiththecommandshow clock.
Example
Thisexamplecreatesthefollowingconfiguration:
n Definestheauthenticationkey1withthepasswordmyPassword.
n DefinestheNTPservermy-ntp.mydomain.comandmakesitthepreferredserver.
| switch(config)# |     | ntp     | authentication-key |                     |     | 1   | md5 myPassword |        |        |     |
| --------------- | --- | ------- | ------------------ | ------------------- | --- | --- | -------------- | ------ | ------ | --- |
| switch(config)# |     | ntp     | server             | my-ntp.mydomain.com |     |     |                | key 10 | prefer |     |
| switch(config)# |     | ntp     | vrf                | default             |     |     |                |        |        |     |
| Configuring     |     | banners |                    |                     |     |     |                |        |        |     |
1. Configurethebannerthatisdisplayedwhenauserconnectstoadeviceusingaconsoleportor
in-bandmanagementinterface.Usethecommandbanner motd.Forexample:
|     | switch(config)# |     | banner | motd | ^   |     |     |     |     |     |
| --- | --------------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 21

>> & This text will not be included because it comes after the '&'
| Banner updated | successfully! |     |     |
| -------------- | ------------- | --- | --- |
| Using the      | Web UI        |     |     |
Prerequisites
n AconnectiontotheswitchCLI.
Onthe6000and6100,theHTTPSservercanonlybeenabledbythedefaultVRF.
Onthe4100i,theHTTPSservercanonlybeenabledbythedefaultVRF.
Procedure
1. LogintotheCLI.
2. Switchtoconfigcontext.
Forexample:
switch# config
| switch(config)# | https-server | vrf default |     |
| --------------- | ------------ | ----------- | --- |
3. TheWebUIstartsandyouarepromptedtologin.
| Configuring | the in-band | management | interface |
| ----------- | ----------- | ---------- | --------- |
Prerequisites
Aconnectiontotheconsoleport.
Procedure
1. Switchtothe in-bandmanagementinterfacecontextwiththecommandinterface 1.
vlan
2. Bydefault,thein-bandmanagementinterfaceisenabled.Ifitwasdisabled,re-enableitwiththe
| commandno | shutdown. |     |     |
| --------- | --------- | --- | --- |
3. Usethecommandip dhcptoconfigurethein-bandmanagementinterfacetoautomatically
obtainanaddressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastatic
IPv4orIPv6addresswiththecommandsip addressoripv6address.
4. SSHisenabledbydefaultonthedefaultVRF.Ifdisabled,enableSSHwiththecommandssh
| server vrf | default. |     |     |
| ---------- | -------- | --- | --- |
Examples
Thisexampleenablesthe in-bandmanagementinterfacewithstaticaddressing:
InitialConfiguration |22

| switch(config)# |     | interface |     | vlan 1 |     |     |     |     |     |
| --------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- |
switch(config-if-vlan)#
no ip dhcp
| switch(config-if-vlan)# |     |        | ip  | address  | 192.168.100.200/24 |         |     |          |     |
| ----------------------- | --- | ------ | --- | -------- | ------------------ | ------- | --- | -------- | --- |
| switch(config-if-vlan)# |     |        | no  | shutdown |                    |         |     |          |     |
| Restoring               | the | switch |     | to       | factory            | default |     | settings |     |
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
4. Optionallyrestoreyoursavedconfiguration(itmustbeinjsonformat)witheithercopy
<REMOTE-URL> running-configorcopy <STORAGE-URL> running-configfollowedbycopy
| running-config |     | startup-config. |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Example
Backinguptherunningconfigurationtoafileonaremoteserver(usingTFTP),resettingtheswitchtoits
factorydefaultstate,andthenrestoringthesavedconfiguration.
switch# copy running-config tftp://10.100.1.12/backup_cfg json vrf default
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload | Upload | Total | Spent | Left Speed |
| --- | --- | --- | --- | --- | ----- | ------ | ----- | ----- | ---------- |
100 10340 0 0 100 10340 0 1329k --:--:-- --:--:-- --:--:-- 1329k
100 10340 0 0 100 10340 0 1313k --:--:-- --:--:-- --:--:-- 1313k
switch#
switch#
| switch# | erase | all zeroize |     |     |     |     |     |     |     |
| ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the
| switch unavailable |         | until      | the     | zeroization  |        | is complete. |              |     |     |
| ------------------ | ------- | ---------- | ------- | ------------ | ------ | ------------ | ------------ | --- | --- |
| This should        | take    | several    | minutes |              | to one | hour         | to complete. |     |     |
| Continue           | (y/n)?  | y          |         |              |        |              |              |     |     |
| The system         | is      | going down | for     | zeroization. |        |              |              |     |     |
| [  OK ]            | Stopped | PSPO       | Module  | Daemon.      |        |              |              |     |     |
| [  OK ]            | Stopped | AOS-CX     | Switch  | Daemon       |        | for BCM.     |              |     |     |
...
| [  OK ]   | Stopped      | Remount      | Root          | and | Kernel | File | Systems. |     |     |
| --------- | ------------ | ------------ | ------------- | --- | ------ | ---- | -------- | --- | --- |
| [  OK ]   | Reached      | target       | Shutdown.     |     |        |      |          |     |     |
| reboot:   | Restarting   | system       |               |     |        |      |          |     |     |
| Press Esc | for          | boot options |               |     |        |      |          |     |     |
| ServiceOS | Information: |              |               |     |        |      |          |     |     |
| Version:  |              |              | GT.01.03.0006 |     |        |      |          |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 23

| Build | Date: |     | 2018-10-30                                        |     | 14:20:44 |     | PDT |     |     |
| ----- | ----- | --- | ------------------------------------------------- | --- | -------- | --- | --- | --- | --- |
| Build | ID:   |     | ServiceOS:GT.01.03.0006:8ee0faaa52da:201810301420 |     |          |     |     |     |     |
| SHA:  |       |     | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx          |     |          |     |     |     |     |
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
| Version:   |          | XL.10.02.0010                                  |     |          |     |     |     |     |     |
| ---------- | -------- | ---------------------------------------------- | --- | -------- | --- | --- | --- | --- | --- |
| Build      | Id:      | AOS-CX:XL.10.02.0010:feaf5b9b7f09:201901292014 |     |          |     |     |     |     |     |
| Build      | Date:    | 2019-01-29                                     |     | 12:43:50 | PST |     |     |     |     |
| Extracting | Image... |                                                |     |          |     |     |     |     |     |
| Loading    | Image... |                                                |     |          |     |     |     |     |     |
Done.
| kexec_core: | Starting     |     | new | kernel |     |     |     |     |     |
| ----------- | ------------ | --- | --- | ------ | --- | --- | --- | --- | --- |
| System is   | initializing |     |     |        |     |     |     |     |     |
fips_post_check[5473]: FIPS_POST: Cryptographic selftest started...SUCCESS
| [  OK ] | Started | Login | banner |     | readiness |     | check. |     |     |
| ------- | ------- | ----- | ------ | --- | --------- | --- | ------ | --- | --- |
...
| 8400X login: | admin |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Password:
switch#
switch#
switch# copy tftp://192.168.1.10/backup_cfg running-config json vrf default
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload |     | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ----------- | ---------- |
100 10340 100 10340 0 0 2858k 0 --:--:-- --:--:-- --:--:-- 2858k
100 10340 100 10340 0 0 2804k 0 --:--:-- --:--:-- --:--:-- 2804k
Large configuration changes will take time to process, please be patient.
switch#
switch#
| switch# | copy running-config |     |     | startup-config |     |     |     |     |     |
| ------- | ------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Large configuration changes will take time to process, please be patient.
switch#
NTP commands
ntp authentication
ntp authentication
InitialConfiguration |24

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
| Parameter |     |     | Description                                     |     |     |
| --------- | --- | --- | ----------------------------------------------- | --- | --- |
| <KEY-ID>  |     |     | SpecifiestheauthenticationkeyID.Range:1to65534. |     |     |
| md5       |     |     | SelectsMD5keyencryption.                        |     |     |
| sha1      |     |     | SpecifiesSHA1keyencryption.                     |     |     |
<PLAINTXT-KEY> Specifiestheplaintextauthenticationkey.Range:8to40
characters.ThekeymaycontainprintableASCIIcharacters
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 25

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
excluding"#"orbeenteredinhex.Keyslongerthan20characters
areassumedtobehex.TouseanASCIIkeylongerthan20
characters,convertittohex.
trusted
Specifiesthatthisisatrustedkey.WhenNTPauthenticationis
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
| switch(config)# |     | ntp | authentication-key |     |     | 10 md5 F82#450b | trusted |
| --------------- | --- | --- | ------------------ | --- | --- | --------------- | ------- |
Definingkey5withSHA1encryptionandapromptedplaintexttrustedkey:
| switch(config)# |     | ntp                | authentication-key |        |           | 5 sha1 |     |
| --------------- | --- | ------------------ | ------------------ | ------ | --------- | ------ | --- |
| Enter the       | NTP | authentication     |                    | key:   | ********* |        |     |
| Re-Enter        | the | NTP authentication |                    | key:   | ********* |        |     |
| Configure       | the | key as             | trusted            | (y/n)? | y         |        |     |
Removingkey10:
| switch(config)# |             | no  | ntp authentication-key |     |              | 10  |     |
| --------------- | ----------- | --- | ---------------------- | --- | ------------ | --- | --- |
| Command         | History     |     |                        |     |              |     |     |
| Release         |             |     |                        |     | Modification |     |     |
| 10.07orearlier  |             |     |                        |     | --           |     |     |
| Command         | Information |     |                        |     |              |     |     |
| Platforms       | Command     |     | context                |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
InitialConfiguration |26

ntp disable
ntp disable
Description
DisablestheNTPclientontheswitch.TheNTPclientisdisabledbydefault.
Examples
DisablingtheNTPclient.
| switch(config)#     | ntp     | disable |              |
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
| switch(config)# | no  | ntp enable |              |
| --------------- | --- | ---------- | ------------ |
| Command History |     |            |              |
| Release         |     |            | Modification |
| 10.07orearlier  |     |            | --           |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 27

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp server
ntp server <IP-ADDR> [key <KEY-NUM>] [minpoll <MIN-NUM>] [maxpoll <MAX-NUM>][burst |
| iburst][prefer] | [version | <VER-NUM>] |     |
| --------------- | -------- | ---------- | --- |
no ntp server <IP-ADDR> <IP-ADDR> [key <KEY-NUM>] [minpoll <MIN-NUM>] [maxpoll <MAX-NUM>]
| [burst | iburst] | [prefer] | [version | <VER-NUM>] |
| ---------------- | -------- | -------- | ---------- |
Description
DefinesanNTPservertousefortimesynchronization,orupdatesthesettingsofanexistingserverwith
newvalues.Uptoeightserverscanbedefined.
ThenoformofthiscommandremovesaconfiguredNTPserver.
ThedefaultNTPversionis4;itisbackwardscompatiblewithversion3.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
server <IP-ADDR> SpecifiestheaddressofanNTPserverasaDNSname,anIPv4
address(x.x.x.x),wherexisadecimalnumberfrom0to255,or
anIPv6address(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
wherexisahexadecimalnumberfrom0toF.
WhenspecifyinganIPv4address,youcanremoveleadingzeros.
Forexample,theaddress192.169.005.100becomes
192.168.5.100.
WhenspecifyinganIPv6address,youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress2222:0000:3333:0000:0000:0000:4444:0055
becomes2222:0:3333::4444:55.
key <KEY-NUM> Specifiesthekeytousewhencommunicatingwiththeserver.A
trustedkeymustbedefinedwiththecommandntp
authentication-keyandauthenticationmustbeenabledwiththe
commandntpauthentication.Range:1to65534.
| minpoll <MIN-NUM> |     |     |     |
| ----------------- | --- | --- | --- |
Specifiestheminimumpollingintervalinseconds,asapowerof
2.Range:4to17.Default:6(64seconds).
maxpoll <MAX-NUM> Specifiesthemaximumpollingintervalinseconds,asapowerof
2.Range:4to17.Default:10(1024seconds).
| burst |     |     | Sendaburstofpacketsinsteadofjustonewhenconnectedtothe |
| ----- | --- | --- | ----------------------------------------------------- |
server.Usefulforreducingphasenoisewhenthepollinginterval
islong.
| iburst |     |     | Sendaburstofsixpacketswhennotconnectedtotheserver. |
| ------ | --- | --- | -------------------------------------------------- |
Usefulforreducingsynchronizationtimeatstartup.
| prefer |     |     | Makethisthepreferredserver. |
| ------ | --- | --- | --------------------------- |
InitialConfiguration |28

Parameter

Description

version <VER-NUM>

Specifies the version number to use for all outgoing NTP packets.
Range: 3 or 4. Default: 4.

NOTE: NTP is backwards compatible.

Usage

For features such as Activate and ZTP, a switch that has a factory default configuration will automatically
be configured with pool.ntp.org. NTP server configurations via DHCP options are supported. The DHCP
server can be configured with maximum of two NTP server addresses which will be supported on the
switch. Only IPV4 addresses are supported.

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

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

29

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
ntp vrf <VRF-NAME>
| no ntp vrf <VRF-NAME> |     |     |     |
| --------------------- | --- | --- | --- |
Description
6000and6100onlysupportdefaultVRF.
InitialConfiguration |30

4100ionlysupportsdefaultVRF.
SpecifiestheVRFonwhichtheNTPclientcommunicateswithanNTPserver.
ThenoformofthecommandreturnstodefaultVRF.
| Parameter  |     |     | Description             |
| ---------- | --- | --- | ----------------------- |
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |
Example
SettingtheswitchtousethedefaultVRFforNTPclienttraffic.
| switch(config)# | ntp | vrf default |     |
| --------------- | --- | ----------- | --- |
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
| show ntp | associations |     |     |
| -------- | ------------ | --- | --- |
show ntp associations
Description
ShowsthestatusoftheconnectiontoeachNTPserver.Thefollowinginformationisdisplayedforeach
server:
n Tallycode:ThefirstcharacteristheTallycode:
o
(blank):Nostateinformationavailable(e.g.non-respondingserver)
o x:Outoftolerance(discardedbyintersectionalgorithm)
o .:Discardedbytableoverflow(notused)
o -:Outoftolerance(discardedbytheclusteralgorithm)
o +:Goodandapreferredremotepeerorserver(includedbythecombinealgorithm)
o #:Goodremotepeerorserver,butnotutilized(readyasabackupsource)
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 31

o *:Remotepeerorserverpresentlyusedasaprimaryreference
o o:PPSpeer(whenthepreferpeerisvalid)
n ID:Servernumber.
n NAME:NTPserverFQDN/IPaddress(Onlythefirst24charactersofthenamearedisplayed).
n REMOTE:RemoteserverIPaddress.
n REF_ID:ReferenceIDfortheremoteserver(CanbeanIPaddress).
n ST:(Stratum)NumberofhopsbetweentheNTPclientandthereferenceclock.
n LAST:Timesincethelastpacketwasreceivedinsecondsunlessanotherunitisindicated.
n POLL:Interval(inseconds)betweenNTPpollpackets.Maximum(1024)reachedasserverandclient
sync.
n REACH:8-bitoctalnumberthatdisplaysstatusofthelasteightNTPmessages(377=allmessages
received).
Example
| switch# | show | ntp | associations |     |     |     |     |     |
| ------- | ---- | --- | ------------ | --- | --- | --- | --- | --- |
----------------------------------------------------------------------
| ID  |     | NAME |     | REMOTE |     | REF-ID | ST LAST POLL | REACH |
| --- | --- | ---- | --- | ------ | --- | ------ | ------------ | ----- |
----------------------------------------------------------------------
| 1                  | 192.0.1.1 |     |     | 192.0.1.1    |     | .INIT. | 16 -     | 64 0 |
| ------------------ | --------- | --- | --- | ------------ | --- | ------ | -------- | ---- |
| * 2 time.apple.com |           |     |     | 17.253.2.253 |     | .GPSs. | 2 70 128 | 377  |
----------------------------------------------------------------------
| Command        | History     |         |         |     |              |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- | --- |
| Release        |             |         |         |     | Modification |     |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |     |
| Command        | Information |         |         |     |              |     |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp | authentication-keys |     |     |     |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
show ntp authentication-keys
Description
Showsthecurrentlydefinedauthenticationkeys.
Examples
| switch# | show | ntp | authentication-keys |     |     |     |     |     |
| ------- | ---- | --- | ------------------- | --- | --- | --- | --- | --- |
--------------------------------
| Auth key | Trusted |     | MD5 | password |     |     |     |     |
| -------- | ------- | --- | --- | -------- | --- | --- | --- | --- |
--------------------------------
InitialConfiguration |32

| 10                  | No      | ********** |              |     |
| ------------------- | ------- | ---------- | ------------ | --- |
| 20                  | Yes     | ********** |              |     |
| Command History     |         |            |              |     |
| Release             |         |            | Modification |     |
| 10.07orearlier      |         |            | --           |     |
| Command Information |         |            |              |     |
| Platforms           | Command | context    | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ntp | servers |     |     |     |
| -------- | ------- | --- | --- | --- |
show ntp servers
Description
ShowsallconfiguredNTPservers,includinganyDHCPservers,defaultpoolserversoranyserverwith
| thestatusauto | prefer. |     |     |     |
| ------------- | ------- | --- | --- | --- |
Example
| switch# show | ntp | servers |     |     |
| ------------ | --- | ------- | --- | --- |
------------------------------------------------
| NTP | SERVER KEYID | MINPOLL | MAXPOLL OPTION | VER |
| --- | ------------ | ------- | -------------- | --- |
------------------------------------------------
| 192.0.1.18 |     | -   | 5 10 iburst | 3        |
| ---------- | --- | --- | ----------- | -------- |
| 192.0.1.19 |     | -   | 6 10 none   | 4        |
| 192.0.1.20 |     | -   | 6 8 burst   | 3 prefer |
------------------------------------------------
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp | statistics |     |     |     |
| -------- | ---------- | --- | --- | --- |
show ntp statistics
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 33

Description
ShowsglobalNTPstatistics.Thefollowinginformationisdisplayed:
n Rx-pkts:TotalNTPpacketsreceived.
n CurrentVersionRx-pkts:NumberofNTPpacketsthatmatchthecurrentNTPversion.
n OldVersionRx-pkts:NumberofNTPpacketsthatmatchthepreviousNTPversion.
Errorpkts:Packetsdroppedduetoallothererrorreasons.
n
n Auth-failedpkts:Packetsdroppedduetoauthenticationfailure.
n Declinedpkts:Packetsdeniedaccessforanyreason.
n Restrictedpkts:PacketsdroppedduetoNTPaccesscontrol.
n Rate-limitedpkts:Numberofpacketsdiscardedduetoratelimitation.
n KODpkts:NumberofKissofDeathpacketssent.
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
| show ntp | status |     |     |
| -------- | ------ | --- | --- |
show ntp status
Description
ShowsthestatusofNTPontheswitch.
Examples
DisplayingthestatusinformationwhentheswitchisnotsyncedtoanNTPserver:
InitialConfiguration |34

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 35

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
36
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries)

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
Telnetaccess|37

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
| switch(config)# |             | telnet | server  | vrf mgmt                                            |
| --------------- | ----------- | ------ | ------- | --------------------------------------------------- |
| Command         | History     |        |         |                                                     |
| Release         |             |        |         | Modification                                        |
| 10.11           |             |        |         | Commandintroducedon9300,1000,4100iand8xxxplatforms. |
| Command         | Information |        |         |                                                     |
| Platforms       | Command     |        | context | Authority                                           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 38

Chapter 5

Interface configuration

Interface configuration

Configuring a layer 2 interface

Procedure

1. Change to the interface configuration context for the interface with the command interface.

2. Set the interface MTU (maximum transmission unit) with the command mtu.

3. Review interface configuration settings with the command show interface.

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

Unsupported transceiver support

Transceiver products (optical, DAC, AOCs) that are listed as supported by a switch model are detailed in
the Transceiver Guide. Transceiver products that are not listed, are considered unsupported; this would
include transceivers that are:

n Non-HPE Aruba Networking branded products

n HPE branded products that were designed for non-AOS-CX switch models (e.g. Comware)

n HPE branded products designated for use in HPE Compute Servers or Storage

n Transceivers originally designated for use in HPE Aruba Networking WLAN controllers or former

Mobility Access Switch (MAS) products

n End-of-life HPE Aruba Networking Transceivers

The unsupported transceiver mode (UT-mode) is designed to allow the possible use of these
unsupported products. Not all unsupported products can be recognized and enabled; they may be
unable to be identified (do not follow the proper MSA standards for identification). These unsupported
transceiver products are enabled only on a best-effort basis and there are no guarantees implied for
their continued operation.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

39

Thisfeatureisenabledbydefault.Aperiodicsystemlogwillbegeneratedbydefaultatanintervalof24
hourslistingtheportsonwhichunsupportedtransceiversarepresent.Thelogintervalisconfigurable
andcanbedisabledbysettingthelog-intervaltonone.
| Configuring |     | an  | interface |     | persona |     |     |
| ----------- | --- | --- | --------- | --- | ------- | --- | --- |
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
| aaa authentication |             | port-access |            | dot1x | authenticator |     | macsec |
| ------------------ | ----------- | ----------- | ---------- | ----- | ------------- | --- | ------ |
| arp ipv4           | <IPV4_ADDR> | mac         | <MAC_ADDR> |       |               |     |        |
downshift-enable
energy-efficient-ethernet
| error-control              |     | { auto |          | none        | | base-r-fec  |              | | rs-fec     | }             |
| -------------------------- | --- | ----------------- | ----------- | ------------- | ------------ | ------------ | ------------- |
| ip bootp-gateway           |     | <IPV4-ADDR>       |             |               |              |              |               |
| ip forward-protocol        |     | udp               | <IPV4-ADDR> |               | {<PORT-NUM>  |              | | <PROTOCOL>} |
| ip helper-address          |     | <IPV4-ADDR>       |             | [vrf          | <VRF-NAME>]  |              |               |
| ip igmp router-alert-check |     |                   |             | [enable       | | disable]   |              |               |
| ip igmp snooping           |     | [auto             | vlan        | <VLAN-LIST>]  |              |              |               |
| ip igmp snooping           |     | [blocked          | vlan        | <VLAN-LIST>]  |              |              |               |
| ip igmp snooping           |     | [fastleave        |             | vlan          | <VLAN-LIST>] |              |               |
| ip igmp snooping           |     | [forced-fastleave |             |               | vlan         | <VLAN-LIST>] |               |
| ip igmp snooping           |     | [forward          | vlan        | <VLAN-LIST>]  |              |              |               |
| ip ospf <PROCESS-ID>       |     | area              | <AREA-ID>   |               |              |              |               |
| ip ospf passive            |     |                   |             |               |              |              |               |
| ip rip <PROCESS-ID>        |     | {all-ip           |             | | ip-address} |              |              |               |
| ip rip all-ip              |     | disable           |             |               |              |              |               |
| ip rip all-ip              |     | enable            |             |               |              |              |               |
| ip rip all-ip              |     | receive           | disable     |               |              |              |               |
| ip rip all-ip              |     | send disable      |             |               |              |              |               |
ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
| ipv6 mld           | snooping     | [auto             | vlan | <VLAN-LIST>] |              |              |     |
| ------------------ | ------------ | ----------------- | ---- | ------------ | ------------ | ------------ | --- |
| ipv6 mld           | snooping     | [blocked          |      | vlan         | <VLAN-LIST>] |              |     |
| ipv6 mld           | snooping     | [fastleave        |      | vlan         | <VLAN-LIST>] |              |     |
| ipv6 mld           | snooping     | [forced-fastleave |      |              | vlan         | <VLAN-LIST>] |     |
| ipv6 mld           | snooping     | [forward          |      | vlan         | <VLAN-LIST>] |              |     |
| ipv6 neighbor      |              | <IPV6-ADDR>       | mac  | <MAC-ADDR>   |              |              |     |
| ipv6 ospfv3        | <PROCESS-ID> |                   | area | <AREA-ID>    |              |              |     |
| ipv6 ospfv3        | passive      |                   |      |              |              |              |     |
| ipv6 ripng         | <PROCESS-ID> |                   |      |              |              |              |     |
| lacp port-id       | <PORT-ID>    |                   |      |              |              |              |     |
| lacp port-priority |              | <PORT-PRIORITY>   |      |              |              |              |     |
lag <ID>
link-poe
| lldp dot3 | eee                     |     |     |     |     |     |     |
| --------- | ----------------------- | --- | --- | --- | --- | --- | --- |
| lldp dot3 | poe                     |     |     |     |     |     |     |
| lldp med  | poe                     |     |     |     |     |     |     |
| lldp med  | poe [priority-override] |     |     |     |     |     |     |
persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
Interfaceconfiguration|40

| port-access | device-profile |     | <DEVICE-PROFILE-NAME> |     |     |     |     |
| ----------- | -------------- | --- | --------------------- | --- | --- | --- | --- |
power-over-ethernet
| power-over-ethernet |          | allocate-by       |            | {usage                  |      | | class}    |      |
| ------------------- | -------- | ----------------- | ---------- | ----------------------- | ---- | ----------- | ---- |
| power-over-ethernet |          | assigned-class    |            |                         | {3 | | 4 | 6       | | 8} |
| power-over-ethernet |          | pd-class-override |            |                         |      |             |      |
| power-over-ethernet |          | power-pairs       |            | {alt-a|alt-a-and-alt-b} |      |             |      |
| power-over-ethernet |          | pre-std-detect    |            |                         |      |             |      |
| power-over-ethernet |          | priority          |            | {critical|high|low}     |      |             |      |
| ptp lag-role        | {primary | |                 | secondary} |                         |      |             |      |
| spanning-tree       | cost     | <PORT-COST>       |            |                         |      |             |      |
| spanning-tree       | instance | <INSTANCE-ID>     |            |                         | cost | <PORT-COST> |      |
spanning-tree instance <INSTANCE-ID> port-priority <PRIORITY-MULTIPLIER>
| spanning-tree | port-priority |            | <PRIORITY-MULTIPLIER> |               |               |        |     |
| ------------- | ------------- | ---------- | --------------------- | ------------- | ------------- | ------ | --- |
| spanning-tree | vlan          | <A:1-4094> |                       | cost          | <0-200000000> |        |     |
| spanning-tree | vlan          | <A:1-4094> |                       | port-priority |               | <0-15> |     |
split [confirm]
| track by | <OBJECT-ID> |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- |
vsx-sync {access-lists | qos | rate-limits | vlans | policies | irdp}
Modes
Therearetwosupportedmodes:
1.Copy—Thecopymodeisaone-stepconfigurationthatcopiesthepersonaconfigurationtoan
interface.Furtherchangestothepersonawillnotbeappliedtotheinterfacesusingthatmode.
2.Attach—Unlikethecopymode,besidesapplyingtheconfigurationtotheinterfaceimmediately,the
attachmodealsofollowsthepersonaconfiguration.Itmeansthatthesubsequentchangestothe
personawillbeappliedtotheinterfacesattachedtoit.
| Predefined | and | custom |     | persona |     | names |     |
| ---------- | --- | ------ | --- | ------- | --- | ----- | --- |
Therearetwopredefinedinterfacepersonanames:
n uplink
n access
Thesenameshavenopredefinedconfiguration.Tousethem,theymustbemanuallyconfiguredas
needed.Youcanalsocreatepersonaswithacustomname.Thesecustompersonascanbecreatedand
configuredinthesamemannerasthepredefinedones.Theonlydifferenceisthecommandusedto
applythemtotheinterface.Theprocedurebelowprovidesthedetails.
| Creating | and | configuring |     | an  | interface |     | persona |
| -------- | --- | ----------- | --- | --- | --------- | --- | ------- |
Followthesestepstocreateandconfigureaninterfacepersona:
1. Createtheinterfacepersonawiththecommandinterface persona <PERSONA-NAME>.
2. Settheinterfaceconfigurationasanyotherphysicalinterface.
3. Reviewtheconfigurationwiththecommandshow running-configuration current-context.
4. Switchtoaninterfacecontextwiththecommandinterface <PORT>.
5. Applythepersonaconfigurationtotheinterfaceandsetthemodewiththecommandpersona
custom <PERSONA-NAME> <mode>.Notethat<custom>isanoptionalargument,required
onlyifthepersonaisnotoneofthepredefinednames(neitheruplinknoraccess).
Forinformationonthisfeature,seetherelatedvideoontheAirHeadsBroadcastingChannel.
Examples
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 41

Tocopyapredefinedpersonanameconfigurationtoaninterface:
1.Configuretheinterfacepersona:
| switch(config)#    | interface   | persona | uplink |     |
| ------------------ | ----------- | ------- | ------ | --- |
| switch(config-if)# | no shutdown |         |        |     |
| switch(config-if)# | no routing  |         |        |     |
| switch(config-if)# | vlan        | access  | 100    |     |
| switch(config-if)# | exit        |         |        |     |
2.Applytheconfigurationwithcopymode:
| switch(config)#    | interface | 1/1/1  |           |      |
| ------------------ | --------- | ------ | --------- | ---- |
| switch(config-if)# | persona   | custom | mypersona | copy |
| switch(config-if)# | exit      |        |           |      |
Toattachacustompersonanametoseveralinterfacessimultaneously:
1.Configuretheinterfacepersona:
| switch(config)#    | interface   | persona         | mytemplate |     |
| ------------------ | ----------- | --------------- | ---------- | --- |
| switch(config-if)# | no shutdown |                 |            |     |
| switch(config-if)# | vrf         | attach upstream |            |     |
| switch(config-if)# | exit        |                 |            |     |
2.Applytheconfigurationwithattachmode:
| switch(config)#    | interface | 1/1/1-1/1/24 |           |        |
| ------------------ | --------- | ------------ | --------- | ------ |
| switch(config-if)# | persona   | custom       | mypersona | attach |
| switch(config-if)# | exit      |              |           |        |
| Monitor mode       |           |              |           |        |
Monitormodedisplaysinterfacestatisticsinrealtime,updatingfrequently.Theupdateintervalvaries
byproduct,numberofvisibleports,anddisplayoptionsinuse.Viewthecurrentupdateintervalinthe
helpmenu.
Formattingoptionscanbesuppliedeitheratcommandlaunchorwhilemonitormodeisactive.Press?
toseetheavailableformattingoptionsavailableinthecurrentcommandcontext.Exitthehelpmenu
withq.
Monitormodedetectsterminalsizetoadjustthenumberofinterfacesandstatisticsviewableon
screen.Additionalinterfacesorstatisticscolumnscanbeviewedwiththenavigationkeys: Arrowkeys,
PageUp,PageDown,Home,andEnd.Serialconsoledoesnotautomaticallydetectterminalsetting
changes,resultinginunexpectedoutput.Recommendedrecoverystepsaretoexitandrestart.
Monitormoderefreshesdataautomaticallyuntilexitedwithq.
| Interface commands |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver
Interfaceconfiguration|42

Description

Allows unsupported transceivers to be enabled or establish connections. Transceivers with speeds up to
100G are enabled by this command.

This command is enabled by default, allowing the use of third party transceiver products without adding the

command in the configuration. Disabling this command with the no form will now disable the command in the

running and stored configurations.

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

43

switch(config)# allow-unsupported-transceiver log-interval none
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no  | allow-unsupported-transceivers |     |     |
| --------------- | --- | ------------------------------ | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
| Ccontinue   | (y/n)? y    |               |           |       |
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
switch(config)#
|     | no  | allow-unsupported-transceiver |     | confirm |
| --- | --- | ----------------------------- | --- | ------- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
switch(config)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
config
| 4100i |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ----- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
6100
| default interface |                |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
| default interface | <INTERFACE-ID> |     |     |     |
Description
Setsaninterface(orarangeofinterfaces)tofactorydefaultvalues.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID>
SpecifiestheIDofasingleinterfaceorrangeofinterfaces.
Format:member/slot/portormember/slot/port-
member/slot/porttospecifyarange.
Examples
Resettinganinterface:
Interfaceconfiguration|44

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
| description | (interface)   |     |     |     |
| ----------- | ------------- | --- | --- | --- |
| description | <DESCRIPTION> |     |     |     |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 45

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
energy-efficient-ethernet
energy-efficient-ethernet
Description
Enablesauto-negotiationofEnergy-EfficientEthernet(EEE)onaninterface.EEENegotiationis
establishedonlyonauto-linknegotiationwithsupportedlinkpartners.
Examples
Configuringaninterface:
| switch(config)#    | interface | 1/1/1                     |     |
| ------------------ | --------- | ------------------------- | --- |
| switch(config-if)# |           | energy-efficient-ethernet |     |
DisablingEnergyEfficientEthernetonaninterface:
| switch(config)#     | interface | 1/1/1                        |              |
| ------------------- | --------- | ---------------------------- | ------------ |
| switch(config-if)#  |           | no energy-efficient-ethernet |              |
| Command History     |           |                              |              |
| Release             |           |                              | Modification |
| 10.07orearlier      |           |                              | --           |
| Command Information |           |                              |              |
| Platforms           | Command   | context                      | Authority    |
4100i config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6000
6100
flow-control
| flow-control    | rxtx |     |     |
| --------------- | ---- | --- | --- |
| no flow-control | rxtx |     |     |
Description
Commandflow-controlenablesnegotiationofIEEE802.3xlink-levelflowcontrolonthecurrent
interface.Theswitchadvertiseslink-levelflowcontrolsupporttothelinkpartner.Thefinalconfiguration
isdeterminedbasedonthecapabilitiesofbothpartners.
Eachinvocationofthiscommandreplacesthepreviousconfiguration.
Thenoformofthesecommandsdisablesanyconfiguredflowcontrolontheselectedinterface.
Interfaceconfiguration|46

| Parameter |     |     |     | Description                                             |
| --------- | --- | --- | --- | ------------------------------------------------------- |
| rxtx      |     |     |     | EnablestheabilitytohonorreceivedandtotransmitIEEE802.3x |
LLFCpauseframestotheremotedevice.
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
n Losslessflowcontrolwillonlyoperatecorrectlywhenboththeingressandegressinterfaceshave
flowcontrolenabled.
Examples
EnablingsupportforRXTXflowcontrol:
| switch(config)#    |     | interface    | 1/1/1 |      |
| ------------------ | --- | ------------ | ----- | ---- |
| switch(config-if)# |     | flow-control |       | txrx |
DisablingsupportforRXTXflowcontrol:
| switch(config)#     |         | interface       | 1/1/1 |              |
| ------------------- | ------- | --------------- | ----- | ------------ |
| switch(config-if)#  |         | no flow-control |       | txrx         |
| Command History     |         |                 |       |              |
| Release             |         |                 |       | Modification |
| 10.07orearlier      |         |                 |       | --           |
| Command Information |         |                 |       |              |
| Platforms           | Command | context         |       | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| interface            | (port) |     |     |     |
| -------------------- | ------ | --- | --- | --- |
| interface <PORT-NUM> |        |     |     |     |
Description
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 47

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
| interface      | vlan           |     |     |
| -------------- | -------------- | --- | --- |
| interface vlan | <VLAN-ID>      |     |     |
| no interface   | vlan <VLAN-ID> |     |     |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-if-
vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
| Parameter |     |     | Description              |
| --------- | --- | --- | ------------------------ |
| <VLAN-ID> |     |     | SpecifiestheinterfaceID. |
DonotreserveanyinternalVLANs.
none
Examples
| switch# config          |           |      |     |
| ----------------------- | --------- | ---- | --- |
| switch(config)#         | vlan      | 10   |     |
| switch(config-vlan-10)# |           | exit |     |
| switch(config)#         | interface | vlan | 10  |
switch(config-if-vlan)#
Interfaceconfiguration|48

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip address                  | (interface)      |     |     |
| --------------------------- | ---------------- | --- | --- |
| ip address <IP-ADDR>/<MASK> |                  |     |     |
| no ip address               | <IP-ADDR>/<MASK> |     |     |
Description
SetsanIP/IPv6addressontheinterfaceVLAN.
ThenoformofthiscommandremovestheIP/IPv6addressfromtheinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes192.168.5.100.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
Examples
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 49

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip mtu
ip mtu <VALUE>
no ip mtu
Description
SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthat
canbesentorreceivedbytheinterface.ThisvalueshouldbelessthanorequaltotheoverallMTUfor
theinterface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VALUE> SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
SettingtheIPMTUto576bytes:
| switch(config-if-vlan)# |             | ip      | mtu 576 |                           |
| ----------------------- | ----------- | ------- | ------- | ------------------------- |
| Command                 | History     |         |         |                           |
| Release                 |             |         |         | Modification              |
| 10.08                   |             |         |         | Subinterfacesupportadded. |
| 10.07orearlier          |             |         |         | --                        |
| Command                 | Information |         |         |                           |
| Platforms               | Command     | context |         | Authority                 |
config-if-vlan
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip source-interface
ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity | dns |
| all} {interface | <IFNAME> | | <IPV4-ADDR>} |     | [vrf <VRF-NAME>] |
| --------------- | -------- | -------------- | --- | ---------------- |
no ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity |
| dns | all} | [interface | <IFNAME> | | <IPV4-ADDR>] | [vrf <VRF-NAME>] |
| ---------- | ---------- | -------- | -------------- | ---------------- |
Description
Interfaceconfiguration|50

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
ntp | syslog | simplivity | dns | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
nothaveanaddressset.
all
| interface <IFNAME> |     |     |     |
| ------------------ | --- | --- | --- |
Specifiesthenameoftheinterfacefromwhichthespecified
serviceobtainsitssourceIPaddress.Theinterfacemusthavea
validIPaddressassignedtoit.Iftheinterfacehasbothaprimary
andsecondaryIPaddress,theprimaryIPaddressisused.
<IPV4-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedservice.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionis
notused).SpecifytheaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
Examples
SettingtheIPv4address10.10.10.5astheglobalsinglesourceaddress:
| switch# config  |     |                  |                |
| --------------- | --- | ---------------- | -------------- |
| switch(config)# | ip  | source-interface | all 10.10.10.5 |
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)#     | no      | ip source-interface | all 10.10.10.5 |
| ------------------- | ------- | ------------------- | -------------- |
| Command History     |         |                     |                |
| Release             |         |                     | Modification   |
| 10.07orearlier      |         |                     | --             |
| Command Information |         |                     |                |
| Platforms           | Command | context             | Authority      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip tcp mss
| ip tcp mss <VALUE> |     |     |     |
| ------------------ | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 51

| no ip tcp | mss <VALUE> |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
Description
SetstheTCP(TransmissionControlProtocol)MSS(MaximumSegmentSize)foraninterface.When
configured,theMSS optionintheTCPheaderissetintheTCP handshakefornegotiationduring
connectionestablishment.OncetheTCPsessionisestablished,changingtheTCP MSSvalueonthe
interfacewillnotaffecttheexistingsession.
ThenoformofthiscommandremovestheTCP MSS configurationfromtheinterface.
TCPMSSissupportedonROP,SVI,subinterface,andL3GREtunnelinterface.
| Parameter |     |     |     |     | Description                                    |
| --------- | --- | --- | --- | --- | ---------------------------------------------- |
| <VALUE>   |     |     |     |     | SpecifiestheIPv4TCPMSSinbytes.Range:68to65495. |
Examples
ConfiguringtheIPv4TCPMSSfortheinterface:
| switch(config)#    |     | interface |        | 1/1/1    |     |
| ------------------ | --- | --------- | ------ | -------- | --- |
| switch(config-if)# |     |           | ip tcp | mss 1460 |     |
RemovingtheIPv4TCPMSSconfigurationfromtheinterface:
| switch(config)#    |             | interface |           | 1/1/1 |                    |
| ------------------ | ----------- | --------- | --------- | ----- | ------------------ |
| switch(config-if)# |             |           | no ip tcp | mss   | 1460               |
| Command            | History     |           |           |       |                    |
| Release            |             |           |           |       | Modification       |
| 10.14.1000         |             |           |           |       | Commandintroduced. |
| Command            | Information |           |           |       |                    |
| Platforms          | Command     |           | context   |       | Authority          |
config-if-vlan
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK>{eui64 |                    |     |     | | [tag <ID>]} |
| --------------- | ------------------------ | ------------------ | --- | --- | ------------- |
| no ipv6 address |                          | <IPV6-ADDR>/<MASK> |     |     |               |
Description
SetsanIPv6addressontheinterface.
ThenoformofthiscommandremovestheIPv6addressontheinterface.
Interfaceconfiguration|52

ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6addresslink-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-local
addressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6addresslink-
localcommand.
| Parameter   |     |     |     | Description                       |
| ----------- | --- | --- | --- | --------------------------------- |
| <IPV6-ADDR> |     |     |     | SpecifiestheIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress2222:0000:3333:0000:0000:0000:4444:0055
becomes2222:0:3333::4444:55.
| <MASK> |     |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
| eui64    |     |     |     | ConfiguretheIPv6addressintheEUI-64bitformat.  |
| -------- | --- | --- | --- | --------------------------------------------- |
| tag <ID> |     |     |     | Configureroutetagforconnectedroutes.Range:0to |
4294967295.Default:0.
Examples
SettingtheIPv6address2001:0db8:85a3::8a2e:0370:7334withamaskof24bits:
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
RemovingtheIPaddress2001:0db8:85a3::8a2e:0370:7334withmaskof24bits:
switch(config-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
| Command        | History     |         |         |              |
| -------------- | ----------- | ------- | ------- | ------------ |
| Release        |             |         |         | Modification |
| 10.07orearlier |             |         |         | --           |
| Command        | Information |         |         |              |
| Platforms      |             | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 source-interface
ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity | dns
| | all} {interface |     | <IFNAME> | | <IPV6-ADDR>} |     |
| ----------------- | --- | -------- | -------------- | --- |
no ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity |
| dns | all} | [interface |     | <IFNAME> | | <IPV6-ADDR>] |
| ---------- | ---------- | --- | -------- | -------------- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 53

Description

Sets a single source IP address for a feature on the switch. This ensures that all traffic sent the feature
has the same source IP address regardless of how it egresses the switch. You can define a single global
address that applies to all supported features, or an individual address for each feature.

This command provides two ways to set the source IP addresses: either by specifying a static IP address,
or by using the address assigned to a switch interface. If you define both options, then the static IP
address takes precedence.

The no form of this command deletes the single source IP address for all supported protocols, or a
specific protocol.

Parameter

Description

sflow | tftp | radius | tacacs |
ntp | syslog | simplivity | dns |
all

Sets a single source IP address for a specific protocol. The all
option sets a global address that applies to all protocols that do
not have an address set.

interface <IFNAME>

<IPV6-ADDR>

Specifies the name of the interface from which the specified
protocol obtains its source IP address.

Specifies the source IP address to use for the specified protocol.
The IP address must be defined on the switch, and it must exist
on the specified VRF (which is the default VRF). Specify the IP
address in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

Examples

Configuring the IPv6 address 2001:DB8::1 as the global single source address:

switch# config
switch(config)# ip source-interface all 2001:DB8::1/32

Stop the source IP address from using the IP address on interface 1/1/1 on VRF default.

switch(config)# no ip source-interface all interface 1/1/1 vrf default

Clear the source IP address 2001:DB8::1.

switch(config)# no ip source-interface all 2001:DB8::1

Command History

Release

10.07 or earlier

Command Information

Modification

--

Interface configuration | 54

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 tcp mss |             |     |     |     |
| ------------ | ----------- | --- | --- | --- |
| ipv6 tcp mss | <VALUE>     |     |     |     |
| no ipv6 tcp  | mss <VALUE> |     |     |     |
Description
SetstheTCP(TransmissionControlProtocol)MSS(MaximumSegmentSize)foraninterface.When
configured,theMSS optionintheTCPheaderissetintheTCP handshakefornegotiationduring
connectionestablishment.OncetheTCPsessionisestablished,changingtheTCP MSSvalueonthe
interfacewillnotaffecttheexistingsession.
ThenoformofthiscommandremovestheTCP MSS configurationfromtheinterface.
TCPMSSissupportedonROP,SVI,subinterface,andL3GREtunnelinterface.
| Parameter |     |     |     | Description                                    |
| --------- | --- | --- | --- | ---------------------------------------------- |
| <VALUE>   |     |     |     | SpecifiestheIPv6TCPMSSinbytes.Range:68to65495. |
Examples
ConfiguringtheIPv6TCPMSSfortheinterface:
| switch(config)#    |     | interface | 1/1/1 |          |
| ------------------ | --- | --------- | ----- | -------- |
| switch(config-if)# |     | ipv6      | tcp   | mss 1440 |
RemovingtheIPv6TCPMSSconfigurationfromtheinterface:
| switch(config)#     |         | interface | 1/1/1 |                    |
| ------------------- | ------- | --------- | ----- | ------------------ |
| switch(config-if)#  |         | no ipv6   | tcp   | mss 1440           |
| Command History     |         |           |       |                    |
| Release             |         |           |       | Modification       |
| 10.14.1000          |         |           |       | Commandintroduced. |
| Command Information |         |           |       |                    |
| Platforms           | Command | context   |       | Authority          |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
mtu
mtu <VALUE>
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 55

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
persona
persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
no persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
Description
Associatesoneofthreepersonatypeswithaninterfacetoclassifythepurposeorroleofaninterface.
Onthe10000SwitchSeries,“access”personaportsaretypicallyconnectedtoworkloads/VMs,andthe
“uplink”(fabric)personaportsareconnectedtothecore/spine.
Interfaceconfiguration|56

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

switch(config)# interface 1/1/1
switch(config-if)# persona access

Configuring an uplink persona:

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

57

| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|     | persona | uplink |     |     |
| --- | ------- | ------ | --- | --- |
Configuringacustompersonanamed"mypersona":
| switch(config)#           | interface | 1/1/1  |           |     |
| ------------------------- | --------- | ------ | --------- | --- |
| switch(config-if)#persona |           | custom | mypersona |     |
Removingthepersonasetting.
| switch(config-if)# | no persona |     |     |     |
| ------------------ | ---------- | --- | --- | --- |
Copyingapredefinedpersonanameconfigurationtoaninterface:
1.Configuringtheinterfacepersona:
| switch(config)#    | interface   | persona | uplink |     |
| ------------------ | ----------- | ------- | ------ | --- |
| switch(config-if)# | no shutdown |         |        |     |
| switch(config-if)# | no routing  |         |        |     |
| switch(config-if)# | vlan        | access  | 100    |     |
| switch(config-if)# | exit        |         |        |     |
2.Applyingtheconfigurationfromthepersonanamed"mypersona"withcopymode:
switch(config)#
|                    | interface | 1/1/1  |           |      |
| ------------------ | --------- | ------ | --------- | ---- |
| switch(config-if)# | persona   | custom | mypersona | copy |
| switch(config-if)# | exit      |        |           |      |
Attachingacustompersonanamenamed"mypersona"toseveralinterfacessimultaneously:
1.Configuringaninterfacepersonanamed"mypersona":
| switch(config)#    | interface   | persona         | mypersona |     |
| ------------------ | ----------- | --------------- | --------- | --- |
| switch(config-if)# | no shutdown |                 |           |     |
| switch(config-if)# | vrf         | attach upstream |           |     |
| switch(config-if)# | exit        |                 |           |     |
2.Applyingthe"mypersona"configurationwithattachmode:
| switch(config)#    | interface | 1/1/1-1/1/24 |           |        |
| ------------------ | --------- | ------------ | --------- | ------ |
| switch(config-if)# | persona   | custom       | mypersona | attach |
| switch(config-if)# | exit      |              |           |        |
Command History
| Release |     |     | Modification                         |     |
| ------- | --- | --- | ------------------------------------ | --- |
| 10.10   |     |     | Addedoptionalparameters:attach,copy. |     |
| 10.09   |     |     | Commandintroduced.                   |     |
Interfaceconfiguration|58

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
Examples
Settingtheratecollectionintervalto50seconds
| switch(config)#    |     | interface     | 1/1/1 |     |
| ------------------ | --- | ------------- | ----- | --- |
| switch(config-if)# |     | rate-interval |       | 50  |
Settingtheratecollectionintervaltothedefaultvalue:
| switch(config-if)# |     | no rate-interval |     |     |
| ------------------ | --- | ---------------- | --- | --- |
Thefollowingexampleshowsthecommand-lineinterfacewarningthatappearswhileconfiguringan
invalidrate-interval.
| switch(config)#    |      | interface | 1/1/1    |       |
| ------------------ | ---- | --------- | -------- | ----- |
| switch(config-if)# |      | rate      | interval | 6     |
| The interval       | must | be a      | multiple | of 5. |
Usage
Theratecollectionintervalmustbeconfiguredinthemultiplesof5.Anyothervaluewillberejectedand
theCLIwilldisplaytheerrormessage,The interval must be a multiple of 5.
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 59

| Release    |             |         |     | Modification                                       |
| ---------- | ----------- | ------- | --- | -------------------------------------------------- |
| 10.12.1000 |             |         |     | Commandsupportedonallplatforms.                    |
| 10.12      |             |         |     | CommandIntroducedon6300and8360Switchseries.        |
| Command    | Information |         |     |                                                    |
| Platforms  | Command     | context |     | Authority                                          |
|            | config-if   |         |     | Administratorsorlocalusergroupmemberswithexecution |
Allplatforms
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
Interfaceconfiguration|60

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show interface |                       |     |                    |
| -------------- | --------------------- | --- | ------------------ |
| show interface | [<IFNNAME>|<IFRANGE>] |     | [brief | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] | monitor       | [human-readable] |
| -------------- | ----------- | ------------- | ---------------- |
| show interface | [lag |      | vlan ] [<ID>] | [brief]          |
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
VLAN
ShowsVLANinterfaceinformation.
| <LAG-ID> |     |     | SpecifiestheLAGnumber.Range:1-256 |
| -------- | --- | --- | --------------------------------- |
<VLAN-ID>
SpecifiestheVLANID.Range:1-4094
Examples
Showinginformationwheninterface1/1/1isconfigured:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 61

| MDI     | mode:      | MDIX            |           |     |         |     |     |     |       |         |
| ------- | ---------- | --------------- | --------- | --- | ------- | --- | --- | --- | ----- | ------- |
| VLAN    | Mode:      | native-untagged |           |     |         |     |     |     |       |         |
| Native  | VLAN:      | 1               |           |     |         |     |     |     |       |         |
| Allowed | VLAN       | List:           | all       |     |         |     |     |     |       |         |
| Rate    | collection |                 | interval: | 300 | seconds |     |     |     |       |         |
| Rates   |            |                 |           |     | RX      |     |     | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits       | / sec |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| ----------- | ----- | --- | --- | --- | ---- | --- | --- | ---- | --- | ----- |
| KPkts       | / sec |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Unicast     |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Multicast   |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Broadcast   |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Utilization |       | %   |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Statistics  |       |     |     |     | RX   |     |     | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets   |        |     |     |     | 0   |     |     | 0   |     | 0   |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast   |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Multicast |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Broadcast |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Bytes     |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Jumbos    |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Dropped   |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Filtered  |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Pause     | Frames |     |     |     | 0   |     |     | 0   |     | 0   |
| Errors    |        |     |     |     | 0   |     |     | 0   |     | 0   |
| CRC/FCS   |        |     |     |     | 0   |     |     | n/a |     | 0   |
| Collision |        |     |     |     | n/a |     |     | 0   |     | 0   |
| Runts     |        |     |     |     | 0   |     |     | n/a |     | 0   |
| Giants    |        |     |     |     | 0   |     |     | n/a |     | 0   |
Showinginformationwhentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |
...
| Auto-negotiation |     |     | is on | with | downshift | active |     |     |     |     |
| ---------------- | --- | --- | ----- | ---- | --------- | ------ | --- | --- | --- | --- |
Showinginformationwhentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |
...
| Energy-Efficient |     |     | Ethernet | is  | enabled | and active |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | ------- | ---------- | --- | --- | --- | --- |
ShowinginformationwhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 | physical |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | ----- | -------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------------------------------------
|        |     |        |           |        | Link              | Admin  |        | Speed       | Flow-Control |          |
| ------ | --- | ------ | --------- | ------ | ----------------- | ------ | ------ | ----------- | ------------ | -------- |
|        | EEE |        | PoE Power |        |                   |        | Port   |             |              |          |
| Port   |     | Type   |           | Status |                   | Config | Status | | Config    | Status       | | Config |
| Status | |   | Config | (Watts)   |        | State Information |        |        | Description |              |          |
----------------------------------------------------------------------------------
----------------------------------------------------------
Interfaceconfiguration|62

| 1/1/1 | 1GbT |     | up          | up  | 1G  |     | auto | off |     | off |
| ----- | ---- | --- | ----------- | --- | --- | --- | ---- | --- | --- | --- |
| on    | on   | --  | 10M/100M/1G |     |     | --  |      |     |     |     |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| Interface | 1/1/1 | is up |     |     |     |     |     |     |       |         |
| --------- | ----- | ----- | --- | --- | --- | --- | --- | --- | ----- | ------- |
| Rate      |       |       |     | RX  |     |     | TX  |     | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| MBits /     | sec |     |     | 30196.43 |     | 30196.43 |       |     | 60392.85  |         |
| ----------- | --- | --- | --- | -------- | --- | -------- | ----- | --- | --------- | ------- |
| MPkts /     | sec |     |     | 58977.39 |     | 58977.40 |       |     | 117954.79 |         |
| Unicast     |     |     |     | 0.00     |     |          | 0.00  |     |           | 0.00    |
| Multicast   |     |     |     | 58977.39 |     | 58977.40 |       |     | 117954.79 |         |
| Broadcast   |     |     |     | 0.00     |     |          | 0.00  |     |           | 0.00    |
| Utilization | %   |     |     | 75.49    |     |          | 75.49 |     |           | 150.98  |
| Statistic   |     |     |     | RX       |     |          | TX    |     | Total     | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Packets      |                |            | 4756527649   |     |              | 4756527865  |     |     | 9513055514   |     |
| ------------ | -------------- | ---------- | ------------ | --- | ------------ | ----------- | --- | --- | ------------ | --- |
| Unicast      |                |            |              | 0   |              |             | 0   |     |              | 0   |
| Multicast    |                |            | 4756527649   |     |              | 4756527865  |     |     | 9513055514   |     |
| Broadcast    |                |            |              | 2   |              |             | 0   |     |              | 2   |
| Bytes        |                |            | 304417778668 |     | 304417795428 |             |     |     | 608835574096 |     |
| Jumbos       |                |            |              | 0   |              |             | 0   |     |              | 0   |
| Dropped      |                |            |              | 0   |              | 19028847730 |     |     | 19028847730  |     |
| Pause Frames |                |            |              | 0   |              |             | 0   |     |              | 0   |
| Errors       |                |            |              | 0   |              |             | 0   |     |              | 0   |
| CRC/FCS      |                |            |              | 0   |              |             | n/a |     |              | 0   |
| help: ?,     | quit:          | q          |              |     |              |             |     |     |              |     |
| Help for     | Interface      | Monitor    |              |     |              |             |     |     |              |     |
| h Toggle     | human-readable |            | mode         |     |              |             |     |     |              |     |
| c Clear      | interface      | statistics |              |     |              |             |     |     |              |     |
| Does not     | apply          | to rates   |              |     |              |             |     |     |              |     |
| Arrows,      | PgUp, PgDn,    | Home,      | End          |     |              |             |     |     |              |     |
| Navigate     | interface      | statistics |              |     |              |             |     |     |              |     |
Delay: 2
| help: ?, | quit: | q   |     |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the<1symbolforUtilizationindicatesthattheamountofpacketsisbetweenzero
andone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |     |     |       |         |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | --- | --- | ----- | ------- |
| Interface          | 1/1/1 | is up |           |                      |     |     |     |     |       |         |
| Rate               |       |       |           | RX                   |     |     | TX  |     | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Bits / | sec |     |     | 3M  |     |     | 3M  |     |     | 6M  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pkts / | sec |     |     | 316 |     |     | 316 |     |     | 633 |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 63

| Unicast     |     |     |     |     | 319 |     | 319 | 638   |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Multicast   |     |     |     |     | 0   |     | 0   | 0     |
| Broadcast   |     |     |     |     | 0   |     | 0   | 0     |
| Utilization | %   |     |     |     | < 1 |     | < 1 | < 1   |
| Statistic   |     |     |     |     | RX  |     | TX  | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     |     | 577K |     | 577K | 1M  |
| ------------ | --- | --- | --- | --- | ---- | --- | ---- | --- |
| Unicast      |     |     |     |     | 577K |     | 577K | 1M  |
| Multicast    |     |     |     |     | 0    |     | 51   | 51  |
| Broadcast    |     |     |     |     | 0    |     | 15   | 15  |
| Bytes        |     |     |     |     | 744M |     | 745M | 1G  |
| Jumbos       |     |     |     |     | 0    |     | 0    | 0   |
| Dropped      |     |     |     |     | 0    |     | 0    | 0   |
| Filtered     |     |     |     |     | 0    |     | 0    | 0   |
| Pause Frames |     |     |     |     | 0    |     | 0    | 0   |
| Errors       |     |     |     |     | 0    |     | 0    | 0   |
| CRC/FCS      |     |     |     |     | 0    |     | n/a  | 0   |
| Collision    |     |     |     |     | n/a  |     | 0    | 0   |
| Runts        |     |     |     |     | 0    |     | n/a  | 0   |
| Giants       |     |     |     |     | 0    |     | n/a  | 0   |
Showinginformationaboutextendedcounters:
Theoutputoftheshow interface extendedcommandvariesdependingontheswitchmodeland
configuration.
| switch(config-if)# |     | show | interface |     | 1/1/17 extended |     |     |     |
| ------------------ | --- | ---- | --------- | --- | --------------- | --- | --- | --- |
-------------------------------------------------------------------
| Interface | 1/1/17 |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Statistics |     |     |     |     |     | Value |     |     |
| ---------- | --- | --- | --- | --- | --- | ----- | --- | --- |
-------------------------------------------------------------------
| Dot1d Tp | Port In         | Frames |         |     |     | 547   |     |     |
| -------- | --------------- | ------ | ------- | --- | --- | ----- | --- | --- |
| Dot1d Tp | Port Out        | Frames |         |     |     | 608   |     |     |
| Dot3 In  | Pause Frames    |        |         |     |     | 0     |     |     |
| Dot3 Out | Pause Frames    |        |         |     |     | 0     |     |     |
| Ethernet | Stats Broadcast |        | Packets |     |     | 19    |     |     |
| Ethernet | Stats Bytes     |        |         |     |     | 40162 |     |     |
| Ethernet | Stats Packets   |        |         |     |     | 342   |     |     |
...
-------------------------------------------------------------------
| Error-Statistics |     |     |     |     |     | Value |     |     |
| ---------------- | --- | --- | --- | --- | --- | ----- | --- | --- |
-------------------------------------------------------------------
| Dot1d Base   | Port        | MTU Exceeded |          | Discards |        | 0   |     |     |
| ------------ | ----------- | ------------ | -------- | -------- | ------ | --- | --- | --- |
| Dot3 Control | In          | Unknown      | Opcodes  |          |        | 0   |     |     |
| Dot3 Stats   | Alignment   |              | Errors   |          |        | 0   |     |     |
| Dot3 Stats   | FCS Errors  |              |          |          |        | 0   |     |     |
| Dot3 Stats   | Frame       | Too          | Longs    |          |        | 0   |     |     |
| Dot3 Stats   | Internal    | Mac          | Transmit |          | Errors | 0   |     |     |
| Ethernet     | RX Oversize |              | Packets  |          |        | 0   |     |     |
...
Showinginterfacelink-status:
| switch# | show interface |     | link-status |     |     |     |     |     |
| ------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------
Interfaceconfiguration|64

| Port |     | Type |     | Physical   | Link        | Last   |     |
| ---- | --- | ---- | --- | ---------- | ----------- | ------ | --- |
|      |     |      |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/1    |     | 1G-BT |     | down | 0   | --       |                 |
| -------- | --- | ----- | --- | ---- | --- | -------- | --------------- |
| 1/1/2    |     | 1G-BT |     | up   | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC | 2018) |     |      |     |          |                 |
| 1/1/3    |     | 1G-BT |     | up   | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC | 2018) |     |      |     |          |                 |
| 1/1/4    |     | --    |     | down | 0   | --       |                 |
| 1/1/5    |     | --    |     | down | 0   | --       |                 |
Showinginterfaceloopback1link-status:
-------------------------------------------------------------
|      |     |      |     | Physical   | Link        | Last   |     |
| ---- | --- | ---- | --- | ---------- | ----------- | ------ | --- |
| Port |     | Type |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| loopback1 |     | --  |     | up  | --  | --  |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Showinginterface1/1/2-1/1/3link-status:
-------------------------------------------------------------
|      |     |      |     | Physical   | Link        | Last   |     |
| ---- | --- | ---- | --- | ---------- | ----------- | ------ | --- |
| Port |     | Type |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/2    |     | 1G-BT |     | up  | 1   | 1 minute | ago (Fri Mar 09 |
| -------- | --- | ----- | --- | --- | --- | -------- | --------------- |
| 12:36:56 | UTC | 2018) |     |     |     |          |                 |
| 1/1/3    |     | 1G-BT |     | up  | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC | 2018) |     |     |     |          |                 |
Showinginterfacelink-status:
| switch# | show | interface | link-status |     |     |     |     |
| ------- | ---- | --------- | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Port |     | Type |     | Physical   | Link        | Link Flaps | Last   |
| ---- | --- | ---- | --- | ---------- | ----------- | ---------- | ------ |
|      |     |      |     | Link State | Transitions | Ignored    | Change |
-------------------------------------------------------------------------
| 1/1/1    |     | 1G-BT    |           | down | 0   | 0   | --           |
| -------- | --- | -------- | --------- | ---- | --- | --- | ------------ |
| 1/1/2    |     | 1G-BT    |           | up   | 1   | 0   | 1 minute ago |
| (Fri Mar | 09  | 12:36:56 | UTC 2018) |      |     |     |              |
| 1/1/3    |     | 1G-BT    |           | up   | 1   | 0   | 1 minute ago |
| (Fri Mar | 09  | 12:36:56 | UTC 2018) |      |     |     |              |
| 1/1/4    |     | --       |           | down | 0   | 0   | --           |
| 1/1/5    |     | --       |           | down | 0   | 0   | --           |
Showingstateinformationwheninterfaceisblocked:
| 8360(config-if)#   |       | show  | interface    | 1/1/1   |     |     |     |
| ------------------ | ----- | ----- | ------------ | ------- | --- | --- | --- |
| Interface          | 1/1/1 | is    | up (Blocked) |         |     |     |     |
| Admin state        |       | is up |              |         |     |     |     |
| State information: |       |       | Blocked      | by UDLD |     |     |     |
Link state: up for 1 minute (since Mon Jun 10 09:25:27 UTC 2024)
| Link transitions: |     | 1   |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
Description:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 65

Persona:
| Hardware: | Ethernet, |     | MAC Address: | 00:fd:45:67:85:91 |     |     |     |
| --------- | --------- | --- | ------------ | ----------------- | --- | --- | --- |
MTU 1500
| Type 10G-LR | /   | 10G SFP+ | LR  |     |     |     |     |
| ----------- | --- | -------- | --- | --- | --- | --- | --- |
Full-duplex
| qos trust        | none   |           |     |         |     |       |         |
| ---------------- | ------ | --------- | --- | ------- | --- | ----- | ------- |
| Speed 10000      | Mb/s   |           |     |         |     |       |         |
| Auto-negotiation |        | is        | off |         |     |       |         |
| Flow-control:    |        | off       |     |         |     |       |         |
| Error-control:   |        | off       |     |         |     |       |         |
| VLAN Mode:       | access |           |     |         |     |       |         |
| Access           | VLAN:  | 1         |     |         |     |       |         |
| Rate collection  |        | interval: | 300 | seconds |     |       |         |
| Rate             |        |           |     | RX      | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     | 0.00 | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | ---- | ---- | --- | ----- |
| KPkts /     | sec |     |     | 0.00 | 0.00 |     | 0.00  |
| Unicast     |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Multicast   |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Broadcast   |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Utilization | %   |     |     | 0.00 | 0.00 |     | 0.00  |
| Statistic   |     |     |     | RX   | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |         |     |     | 15                                              | 15   |     | 30   |
| ------------ | ------- | --- | --- | ----------------------------------------------- | ---- | --- | ---- |
| Unicast      |         |     |     | 12                                              | 12   |     | 24   |
| Multicast    |         |     |     | 3                                               | 3    |     | 6    |
| Broadcast    |         |     |     | 0                                               | 0    |     | 0    |
| Bytes        |         |     |     | 1350                                            | 1350 |     | 2700 |
| Jumbos       |         |     |     | 0                                               | 0    |     | 0    |
| Dropped      |         |     |     | 0                                               | 0    |     | 0    |
| Pause Frames |         |     |     | 0                                               | 0    |     | 0    |
| Errors       |         |     |     | 0                                               | 0    |     | 0    |
| CRC/FCS      |         |     |     | 0                                               | n/a  |     | 0    |
| Collision    |         |     |     | n/a                                             | 0    |     | 0    |
| Runts        |         |     |     | 0                                               | n/a  |     | 0    |
| Giants       |         |     |     | 0                                               | n/a  |     | 0    |
| Command      | History |     |     |                                                 |      |     |      |
| Release      |         |     |     | Modification                                    |      |     |      |
| 10.15        |         |     |     | Addedstateinformationwhenportgoesintodownstate. |      |     |      |
10.11
Addedmonitorparameter.
10.10
Addedhuman-readableparameter.
| 10.07orearlier |             |     |         | --        |     |     |     |
| -------------- | ----------- | --- | ------- | --------- | --- | --- | --- |
| Command        | Information |     |         |           |     |     |     |
| Platforms      | Command     |     | context | Authority |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
Interfaceconfiguration|66

| show interface |                  | dom |     |     |          |     |     |     |
| -------------- | ---------------- | --- | --- | --- | -------- | --- | --- | --- |
| show interface | [<INTERFACE-ID>] |     |     | dom | [detail] |     |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+).This
informationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
| detail |     |     |     |     | Showdetailedinformation. |     |     |     |
| ------ | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
Example
| switch# | show | interface | dom |     |     |     |     |     |
| ------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
Port Type Channel Temperature Voltage Tx Bias Rx Power Tx Power
|     |     |     |     | (Celsius) |     | (Volts) (mA) | (mW/dBm) | (mW/dBm) |
| --- | --- | --- | --- | --------- | --- | ------------ | -------- | -------- |
----------------------------------------------------------------------------------
| 1/1/1               | SFP+SR   |     |         | 47.65 |              | 3.31 8.40 | 0.08, -10.96 | 0.63, -2.49 |
| ------------------- | -------- | --- | ------- | ----- | ------------ | --------- | ------------ | ----------- |
| 1/1/2               | SFP+SR   |     |         | n/a   |              | n/a n/a   | n/a          | n/a         |
| 1/1/3               | SFP+DA3  |     |         | 42.10 |              | 3.24 n/a  | n/a          | n/a         |
| 1/1/4               | QSFP+SR4 | 1   |         | 44.46 |              | 3.30 6.12 | 0.08, -10.96 | 0.63, -1.95 |
| 2                   |          |     |         | 44.46 |              | 3.30 6.04 | 0.08, -10.96 | 0.63, -2.00 |
| 3                   |          |     |         | 44.46 |              | 3.30 6.51 | 0.08, -10.96 | 0.60, -2.16 |
| 4                   |          |     |         | 44.46 |              | 3.30 6.19 | 0.08, -10.96 | 0.63, -1.94 |
| Command History     |          |     |         |       |              |           |              |             |
| Release             |          |     |         |       | Modification |           |              |             |
| 10.07orearlier      |          |     |         |       | --           |           |              |             |
| Command Information |          |     |         |       |              |           |              |             |
| Platforms           | Command  |     | context |       | Authority    |           |              |             |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                      | energy-efficient |     |     |                           | ethernet |     |     |
| -------------- | -------------------- | ---------------- | --- | --- | ------------------------- | -------- | --- | --- |
| show interface | [<IFNAME>|<IFRANGE>] |                  |     |     | energy-efficient-ethernet |          |     |     |
Description
DisplaysEnergy-EfficientEthernetinformationfortheinterface.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 67

| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IFNAME> Specifiesthenameofaninterfaceontheswitch.Usetheformat
member/slot/port(forexample,1/1/1).
<IFRANGE>
Specifiestheportidentifierrangeofaninterfaceontheswitch.
Usetheformatmember/slot/port(forexample,1/1/1).
Example
ThefollowingexampleshowswhentheinterfacesareEnergy-EfficientEthernetcapable.
| switch# | show interface | energy-efficient-ethernet |     |     |     |     |
| ------- | -------------- | ------------------------- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Port | Enabled | Negotiated | Speed  | TX Wake  | RX Wake |      |
| ---- | ------- | ---------- | ------ | -------- | ------- | ---- |
|      |         |            | (MB/s) | Time(us) | Time    | (us) |
-------------------------------------------------------------------
| 1/1/1   | no             | no                              | --   | --  | --  |     |
| ------- | -------------- | ------------------------------- | ---- | --- | --- | --- |
| 1/1/2   | yes            | yes                             | 100  | 36  | 36  |     |
| 1/1/3   | yes            | yes                             | 1000 | 17  | 17  |     |
| 1/1/4   | no             | no                              | --   | --  | --  |     |
| 1/1/5   | yes            | no                              | 1000 | --  | --  |     |
| switch# | show interface | 1/1/1 energy-efficient-ethernet |      |     |     |     |
------------------------------------------------------------------------
| Port | Enabled | Negotiated | Speed  | TX   | Wake | RX Wake   |
| ---- | ------- | ---------- | ------ | ---- | ---- | --------- |
|      |         |            | (Mb/s) | Time | (us) | Time (us) |
------------------------------------------------------------------------
| 1/1/1 | no  | no  | 1000 | --  |     | --  |
| ----- | --- | --- | ---- | --- | --- | --- |
switch#
| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
4100i config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6000           |                       |              | executionrightsforthiscommand.Operatorscanexecutethis |          |     |     |
| -------------- | --------------------- | ------------ | ----------------------------------------------------- | -------- | --- | --- |
| 6100           |                       |              | commandfromtheoperatorcontext(>)only.                 |          |     |     |
| show interface |                       | flow-control |                                                       |          |     |     |
| show interface | [<IFNNAME>|<IFRANGE>] |              | flow-control                                          | [detail] |     |     |
Description
Showstheflowcontrolconfiguration,status,andstatisticsofthespecifiedinterfaceforinterfaceson
whichflowcontrolisenabled.
Interfaceconfiguration|68

Ifdetailisnotspecified,thiscommandshowsasummaryofallflowcontrolledinterfaceswithoneinterfaceper
line.Ifdetailisspecified,thiscommandshowsflowcontroldetailedstatistics.
AsofAOS-CX10.10,theseparateshowflow-controlcommandhasbeenremoved,withitbeingeffectively
replacedbythiscommand.
Parameter Description
<IFNNAME>|<IFRANGE> Specifiestheinterface(port)nameorrange.Whennointerface
rangeisspecified,onlyinterfaceswithflowcontrolenabledinthe
configurationorstatusareshown.
detail
Showsdetailedinformation.
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
| 1/1/1 | config: | llfc rx |              |     |
| ----- | ------- | ------- | ------------ | --- |
|       | status: | llfc rx |              |     |
| 1/1/2 | config: | llfc rx | incompatible | 0   |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 69

|          | status: | llfc | rx       |     |         |     |      |
| -------- | ------- | ---- | -------- | --- | ------- | --- | ---- |
| 1/1/10   | config: | pfc  | rxtx-1,2 |     | enabled |     | 1234 |
|          | status: | pfc  | rxtx-1,2 |     |         |     |      |
| 1/1/12   | config: | pfc  | rxtx-1,2 |     | error   |     | 0    |
|          | status: | pfc  | rxtx-1,2 |     |         |     |      |
| 1/1/32:4 | config: | pfc  | rxtx-5   |     |         |     |      |
|          | status: | pfc  | rxtx-5   |     |         |     |      |
Showingsummaryflowcontrolinformationwheretheconfigurationdoesnotmatchstatusduetoa
rebootrequiredtoapplyPFCconfigurationinhardware:
| switch# show | interface |     | flow-control |          |              |     |     |
| ------------ | --------- | --- | ------------ | -------- | ------------ | --- | --- |
| Flow Control | Watchdog  |     | Settings     |          |              |     |     |
| Trigger      | Timeout:  | 100 | milliseconds | (actual: | not applied) |     |     |
| Resume       | Time:     | 100 | milliseconds | (actual: | not applied) |     |     |
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
| Flow-control: | llfc      | rx  |          |     |     |     |     |
| ------------- | --------- | --- | -------- | --- | --- | --- | --- |
| Flow-control  | watchdog: |     | disabled |     |     |     |     |
Interfaceconfiguration|70

| Statistics           |        |                      | RX  |     |
| -------------------- | ------ | -------------------- | --- | --- |
| -------------------- |        | -------------------- |     |     |
| Dot3 Pause           | Frames |                      | 0   |     |
ShowingdetailedflowcontrolinformationwithRXTXflowcontrolenabled:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | llfc   | rxtx                 |                      |     |
| -------------------- | ------ | -------------------- | -------------------- | --- |
| Statistics           |        |                      | RX                   | TX  |
| -------------------- |        | -------------------- | -------------------- |     |
| Dot3 Pause           | Frames |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabled:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | pfc      | rxtx-4,5             |                      |     |
| -------------------- | -------- | -------------------- | -------------------- | --- |
| Statistics           |          |                      | RX                   | TX  |
| -------------------- |          | -------------------- | -------------------- |     |
| Priority             | 0 Pauses |                      | 0                    | 0   |
| Priority             | 1 Pauses |                      | 0                    | 0   |
| Priority             | 2 Pauses |                      | 0                    | 0   |
| Priority             | 3 Pauses |                      | 0                    | 0   |
| Priority             | 4 Pauses |                      | 0                    | 0   |
| Priority             | 5 Pauses |                      | 0                    | 0   |
| Priority             | 6 Pauses |                      | 0                    | 0   |
| Priority             | 7 Pauses |                      | 0                    | 0   |
| Total Pause          | Frames   |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabledandflowcontrolwatchdogdisabled:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | pfc       | rxtx-4,5             |                      |     |
| -------------------- | --------- | -------------------- | -------------------- | --- |
| Flow-control         | watchdog: | disabled             |                      |     |
| Statistics           |           |                      | RX                   | TX  |
| -------------------- |           | -------------------- | -------------------- |     |
| Priority             | 0 Pauses  |                      | 0                    | 0   |
| Priority             | 1 Pauses  |                      | 0                    | 0   |
| Priority             | 2 Pauses  |                      | 0                    | 0   |
| Priority             | 3 Pauses  |                      | 0                    | 0   |
| Priority             | 4 Pauses  |                      | 0                    | 0   |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 71

| Priority    | 5 Pauses |     | 0   | 0   |
| ----------- | -------- | --- | --- | --- |
| Priority    | 6 Pauses |     | 0   | 0   |
| Priority    | 7 Pauses |     | 0   | 0   |
| Total Pause | Frames   |     | 0   | 0   |
| Interface   | 1/1/1 is | up  |     |     |
| Admin state | is up    |     |     |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | pfc       | rxtx-4,5             |                      |     |
| -------------------- | --------- | -------------------- | -------------------- | --- |
| Flow-control         | watchdog: | disabled             |                      |     |
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
Interfaceconfiguration|72

| switch#     | show interface | 1/1/1 flow-control |     | detail |
| ----------- | -------------- | ------------------ | --- | ------ |
| Interface   | 1/1/1 is       | up                 |     |        |
| Admin state | is up          |                    |     |        |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: | llfc      | rx           |     |     |
| ------------- | --------- | ------------ | --- | --- |
| Flow-control  | watchdog: | incompatible |     |     |
Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butcouldnotbeappliedbecauseacompatibleflowcontrolmodefirstrequiresareboot:
| switch#     | show interface | 1/1/1 flow-control |     | detail |
| ----------- | -------------- | ------------------ | --- | ------ |
| Interface   | 1/1/1 is       | up                 |     |        |
| Admin state | is up          |                    |     |        |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:       | off       |         |                                                 |     |
| ------------------- | --------- | ------- | ----------------------------------------------- | --- |
| Flow-control        | watchdog: | pending |                                                 |     |
| Command History     |           |         |                                                 |     |
| Release             |           |         | Modification                                    |     |
| 10.10               |           |         | Examplesupdatedwithnewandchangedoutputelements. |     |
| 10.08               |           |         | Commandintroduced.                              |     |
| Command Information |           |         |                                                 |     |
| Platforms           | Command   | context | Authority                                       |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show interface | link-diagnostics      |     |                  |     |
| -------------- | --------------------- | --- | ---------------- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | link-diagnostics |     |
Description
Showsinformationaboutselectlinkdiagnostics,includingMAC,PHY,andTransceiverdiagnostics.
| Parameter |     |     | Description              |     |
| --------- | --- | --- | ------------------------ | --- |
| <IFNAME>  |     |     | Specifiesainterfacename. |     |
<IFRANGE>
Specifiestheportidentifierrange.
| link-diagnostics |     |     | Showslinkdiagnosticsinformation. |     |
| ---------------- | --- | --- | -------------------------------- | --- |
Examples
Showinginterfaceinformationfor1/1/12linkdiagnostics:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 73

| switch# | show interface | 1/1/12 link-diagnostics |     |     |     |     |
| ------- | -------------- | ----------------------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| Interface | 1/1/12 | Current | State | Changes | Last Change |     |
| --------- | ------ | ------- | ----- | ------- | ----------- | --- |
----------------------------------------------------------------------------------
| Port Status |        | Waiting | for link |     |     |     |
| ----------- | ------ | ------- | -------- | --- | --- | --- |
| Link Down   | Reason | Local   | fault    |     |     |     |
Transceiver
| No transceiver |                | --                      |     | 0   | --         |     |
| -------------- | -------------- | ----------------------- | --- | --- | ---------- | --- |
| TX Fault       |                | --                      |     | 0   | --         |     |
| Transceiver    | error          | --                      |     | 0   | --         |     |
| System         | error          | --                      |     | 0   | --         |     |
| DOM error      |                | --                      |     | 0   | --         |     |
| Configuring    | transceiver    | --                      |     | 0   | --         |     |
| Transceiver    | disabled       | --                      |     | 0   | --         |     |
| Transceiver    | unsupported    | --                      |     | 0   | --         |     |
| MAC and        | PHY            |                         |     |     |            |     |
| TX Disabled    |                | --                      |     | 0   | --         |     |
| Autoneg        | Incomplete     | --                      |     | 0   | --         |     |
| No Signal      | Detected       | --                      |     | 0   | --         |     |
| No RX Lock     |                | True                    |     | 1   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48    | UTC 2023)               |     |     |            |     |
| Remote         | Fault          | --                      |     | 0   | --         |     |
| Local Fault    |                | True                    |     | 1   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48    | UTC 2023)               |     |     |            |     |
| Link State     |                | Down                    |     | 1   | 16 seconds | ago |
| (Tue Nov       | 14 14:30:54    | UTC 2023)               |     |     |            |     |
| switch#        | show interface | 1/1/12 link-diagnostics |     |     |            |     |
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
Interfaceconfiguration|74

--------------------------------------------------------------------------------
| Interface | 1/1/7 | Current State | Changes | Last Change |     |
| --------- | ----- | ------------- | ------- | ----------- | --- |
-------------------------------------------------------------------------------
| Port Status |        | Link up |     |     |     |
| ----------- | ------ | ------- | --- | --- | --- |
| Link Down   | Reason | --      |     |     |     |
Transceiver
| No transceiver |                 | --        | 0   | --         |     |
| -------------- | --------------- | --------- | --- | ---------- | --- |
| TX Fault       |                 | --        | 0   | --         |     |
| Transceiver    | error           | --        | 0   | --         |     |
| System         | error           | --        | 0   | --         |     |
| DOM error      |                 | --        | 0   | --         |     |
| Configuring    | transceiver     | --        | 0   | --         |     |
| Transceiver    | disabled        | --        | 0   | --         |     |
| Transceiver    | unsupported     | --        | 0   | --         |     |
| MAC and        | PHY             |           |     |            |     |
| TX Disabled    |                 | --        | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| Autoneg        | Incomplete      | --        | 0   | --         |     |
| No Signal      | Detected        | --        | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| No RX          | Lock            | --        | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| Remote         | Fault           | --        | 2   | 21 seconds |     |
| ago (Tue       | Nov 14 14:30:49 | UTC 2023) |     |            |     |
| Local          | Fault           | --        | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |            |     |
| Link State     |                 | Up        | 1   | 16 seconds |     |
| ago (Tue       | Nov 14 14:30:54 | UTC 2023) |     |            |     |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 75

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.14               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
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
Description
Showsstatisticsforswitchinterfacessuchaspacketstransmittedandreceived,bytestransmittedand
received,broadcastandmulticastpackets.
| Parameter |     |     | Description                             |
| --------- | --- | --- | --------------------------------------- |
| <IFNAME>  |     |     | Specifiesainterfacename.                |
| <IFRANGE> |     |     | Specifiestheportidentifierrange.        |
| LAG       |     |     | ShowsLAGinterfaceinformation.           |
| <LAG-ID>  |     |     | SpecifiestheLAGnumber.Range:1-256       |
| monitor   |     |     | Continuouslymonitorinterfacestatistics. |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.
| non-zero |     |     | Showsonlynonzerostatistics. |
| -------- | --- | --- | --------------------------- |
Examples
Showingstatisticsofallinterfaces:
Interfaceconfiguration|76

Showing statistics of all interfaces with only non-zero statistics:

Showing statistics of all interfaces in the human-readable format:

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

Showing monitor statistics:

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

77

Showing monitor error statistics in human-readable format:

Command History

Interface configuration | 78

| Release |     |     |     | Modification          |     |     |
| ------- | --- | --- | --- | --------------------- | --- | --- |
| 10.11   |     |     |     | Addedmoitorparameter. |     |     |
10.10
Addedhuman-readableparameter.
| 10.07orearlier |             |     |         | --        |     |     |
| -------------- | ----------- | --- | ------- | --------- | --- | --- |
| Command        | Information |     |         |           |     |     |
| Platforms      | Command     |     | context | Authority |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show interface |     | transceiver |     |     |     |     |
| -------------- | --- | ----------- | --- | --- | --- | --- |
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations]
Description
Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfor
differenttransceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPE
andthird-partytransceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskinthe
output.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
| detail               |     |     |     | Showdetailedinformationfortheinterfaces. |     |     |
| -------------------- | --- | --- | --- | ---------------------------------------- | --- | --- |
| threshold-violations |     |     |     | Showthresholdviolationsfortransceivers.  |     |     |
Example
Showingsummarytransceiverinformationwithidentificationofunsupportedtransceivers:
| switch(config)# |     | show | interface | transceiver |     |     |
| --------------- | --- | ---- | --------- | ----------- | --- | --- |
------------------------------------------------------------------
| Port | Type |     | Product |     | Serial | Part   |
| ---- | ---- | --- | ------- | --- | ------ | ------ |
|      |      |     | Number  |     | Number | Number |
------------------------------------------------------------------
| 1/1/15 | SFP+SR |     | J9150D |     | xxxxxxxxxx | 1990-4634 |
| ------ | ------ | --- | ------ | --- | ---------- | --------- |
| 1/1/16 | SFP+SR |     | J9150D |     | xxxxxxxxxx | 1990-4634 |
Showingdetailedtransceiverinformation:
| switch(config)# |      | show   | interface | transceiver | detail |     |
| --------------- | ---- | ------ | --------- | ----------- | ------ | --- |
| Transceiver     | in   | 1/1/15 |           |             |        |     |
| Interface       | Name |        | : 1/1/15  |             |        |     |
| Type            |      |        | : SFP+SR  |             |        |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 79

| Connector  | Type | : LC    |     |     |     |
| ---------- | ---- | ------- | --- | --- | --- |
| Wavelength |      | : 850nm |     |     |     |
Transfer Distance : 0.00km (SMF), 20m (OM1), 80m (OM2), 300m (OM3)
| Diagnostic  | Support | : DOM        |     |     |     |
| ----------- | ------- | ------------ | --- | --- | --- |
| Product     | Number  | : J9150D     |     |     |     |
| Serial      | Number  | : xxxxxxxxxx |     |     |     |
| Part Number |         | : 1990-4634  |     |     |     |
Status
| Temperature | : 30.38C  |          |     |     |     |
| ----------- | --------- | -------- | --- | --- | --- |
| Voltage     | : 3.26V   |          |     |     |     |
| Tx Bias     | : 5.54mA  |          |     |     |     |
| Rx Power    | : 0.56mW, | -2.52dBm |     |     |     |
| Tx Power    | : 0.62mW, | -2.08dBm |     |     |     |
Recent Alarms:
Recent Errors:
| Transceiver | in 1/1/16 |          |     |     |     |
| ----------- | --------- | -------- | --- | --- | --- |
| Interface   | Name      | : 1/1/16 |     |     |     |
| Type        |           | : SFP+SR |     |     |     |
| Connector   | Type      | : LC     |     |     |     |
| Wavelength  |           | : 850nm  |     |     |     |
Transfer Distance : 0.00km (SMF), 20m (OM1), 80m (OM2), 300m (OM3)
| Diagnostic  | Support | : DOM        |     |     |     |
| ----------- | ------- | ------------ | --- | --- | --- |
| Product     | Number  | : J9150D     |     |     |     |
| Serial      | Number  | : xxxxxxxxxx |     |     |     |
| Part Number |         | : 1990-4634  |     |     |     |
Status
| Temperature | : 30.62C  |          |     |     |     |
| ----------- | --------- | -------- | --- | --- | --- |
| Voltage     | : 3.28V   |          |     |     |     |
| Tx Bias     | : 5.64mA  |          |     |     |     |
| Rx Power    | : 0.61mW, | -2.15dBm |     |     |     |
| Tx Power    | : 0.59mW, | -2.29dBm |     |     |     |
Recent Alarms:
Recent Errors:
Showingdetailedtransceiverinformationwithidentificationofunsupportedtransceivers:
| Transceiver | in 1/1/2       |                        |           |           |          |
| ----------- | -------------- | ---------------------- | --------- | --------- | -------- |
| Interface   | Name           | : 1/1/2                |           |           |          |
| Type        |                | : SFP+ER (unsupported) |           |           |          |
| Connector   | Type           | : LC                   |           |           |          |
| Wavelength  |                | : 3590nm               |           |           |          |
| Transfer    | Distance       | : 80m (SMF),           | 0m (OM1), | 0m (OM2), | 0m (OM3) |
| Diagnostic  | Support        | : DOM                  |           |           |          |
| Vendor      | Name           | : INNOLIGHT            |           |           |          |
| Vendor      | Part Number    | : TR-PX15Z-NHP         |           |           |          |
| Vendor      | Part Revision: | 1A                     |           |           |          |
| Vendor      | Serial number: | MYxxxxxxx              |           |           |          |
Status
| Temperature | : 28.88C  |         |     |     |     |
| ----------- | --------- | ------- | --- | --- | --- |
| Voltage     | : 3.30V   |         |     |     |     |
| Tx Bias     | : 65.53mA |         |     |     |     |
| Rx Power    | : 0.00mW, | -inf    |     |     |     |
| Tx Power    | : 1.47mW, | 1.67dBm |     |     |     |
Recent Alarms:
| Rx Power | low alarm |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- |
Interfaceconfiguration|80

| Rx Power | low warning |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Recent   | Errors:     |     |     |     |
Showingtransceiverthreshold-violations:
switch(config)# show interface transceiver threshold-violations
----------------------------------------------------------------
| Port | Type | Channel# | Recent | Threshold Violations |
| ---- | ---- | -------- | ------ | -------------------- |
----------------------------------------------------------------
| 1/1/15 | SFP+SR |     | none |     |
| ------ | ------ | --- | ---- | --- |
| 1/1/16 | SFP+SR |     | none |     |
switch#
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface | utilization           |     |             |            |
| -------------- | --------------------- | --- | ----------- | ---------- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | utilization | [non-zero] |
Description
Displaysphysicalportthroughputandutilization.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IFNAME>
Specifiesaninterfacename.
| <IFRANGE> |     |     | Specifiestheportidentifierrange. |     |
| --------- | --- | --- | -------------------------------- | --- |
utilization
Displaysutilizationstatistics.
| non-zero |     |     | Displaysnon-zerostatistics |     |
| -------- | --- | --- | -------------------------- | --- |
Examples
Thefollowingexampleshowsportutilizationofallinterfaces:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 81

| switch# show | interface | utilization |     |     |     |     |     |     |
| ------------ | --------- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|----------------
-----------|----------------------
| Interval | |     | RX  | |   |     | TX  | | Total | (RX+TX) | |   |
| ---------- | --- | --- | --- | --- | --- | ------- | ------- | --- |
Interface seconds | Mbps KPkt/s Util % | Mbps KPkt/s Util % | Mbps
| KPkt/s Util | % | | Description |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|----------------
-----------|----------------------
| 1/1/1               |         | 300 9578.02           |           | 788.70       | 95.78 25.70   | 45.89  | 0.26 9603.72   |     |
| ------------------- | ------- | --------------------- | --------- | ------------ | ------------- | ------ | -------------- | --- |
| 834.59              | 96.04   | Aruba-AP              |           |              |               |        |                |     |
| 1/1/2               |         | 300                   | 25.71     | 45.90        | 0.26 9581.09  | 788.96 | 95.81 9606.80  |     |
| 834.86              | 96.07   | Aruba2530-AP-conce... |           |              |               |        |                |     |
| 1/1/3 - lag123      |         | 300                   | 0.00      | 0.00         | 0.00 0.00     | 0.00   | 0.00 0.00      |     |
| 0.00 0.00           | ISL:    | SWRTS-0064-1          |           |              |               |        |                |     |
| 1/1/4               |         | 300 9261.79           |           | 804.52       | 92.62 9496.70 | 823.97 | 94.97 18758.50 |     |
| 1628.48             | 187.58  | Backup data           | center... |              |               |        |                |     |
| 1/1/5               |         | 300 9496.70           |           | 823.97       | 94.97 9261.79 | 804.52 | 92.62 18758.50 |     |
| 1628.48             | 187.58  | --                    |           |              |               |        |                |     |
| Command History     |         |                       |           |              |               |        |                |     |
| Release             |         |                       |           | Modification |               |        |                |     |
| 10.07orearlier      |         |                       |           | --           |               |        |                |     |
| Command Information |         |                       |           |              |               |        |                |     |
| Platforms           | Command | context               |           | Authority    |               |        |                |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ip interface |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
show ip interface <INTERFACE-ID>|{lag|loopback|vlan|tunnel <ID>}
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
lag <ID>
ShowLAGinterfaceinformation,where<ID>is1-256.
loopback <ID> Showloopbackinterfaceinformation,where<ID>is0-255.
tunnel <ID>
Showtunnelinterfaceinformation,where<ID>is1-255.
| vlan <ID> |     |     |     | ShowVLANinterfaceinformation,where<ID>is1-4094. |     |     |     |     |
| --------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
Example
Interfaceconfiguration|82

| switch#      | show ip interface | 1/1/1        |                   |     |       |
| ------------ | ----------------- | ------------ | ----------------- | --- | ----- |
| Interface    | 1/1/1 is          | up           |                   |     |       |
| Admin state  | is up             |              |                   |     |       |
| Hardware:    | Ethernet,         | MAC Address: | 70:72:cf:fd:e7:b4 |     |       |
| IP MTU       | 1500              |              |                   |     |       |
| IP TCP       | MSS 1460          |              |                   |     |       |
| IPv4 address | 192.168.1.1/24    |              |                   |     |       |
| L3 Counters: | Rx Enabled,       | Tx Enabled   |                   |     |       |
| Statistic    |                   |              | RX                | TX  | Total |
---------------- -------------------- -------------------- --------------------
| L3 Packets   |                   |              | 0                 | 0   | 0   |
| ------------ | ----------------- | ------------ | ----------------- | --- | --- |
| L3 Bytes     |                   |              | 0                 | 0   | 0   |
| switch#      | show ip interface | 1/1/1        |                   |     |     |
| Interface    | 1/1/1 is          | up           |                   |     |     |
| Admin state  | is up             |              |                   |     |     |
| Hardware:    | Ethernet,         | MAC Address: | 70:72:cf:fd:e7:b4 |     |     |
| IP MTU       | 1500              |              |                   |     |     |
| IP TCP       | MSS 1460          |              |                   |     |     |
| IP Directed  | Broadcast         | is Disabled  |                   |     |     |
| IPv4 address | 2.2.2.2/32        | [unnumbered  | to loopback1]     |     |     |
| L3 Counters: | Rx Disabled,      | Tx Disabled  |                   |     |     |
| switch#      | show ip interface | loopback     | 1                 |     |     |
| Interface    | loopback1         | is up        |                   |     |     |
| Admin state  | is up             |              |                   |     |     |
| Hardware:    | Loopback          |              |                   |     |     |
| IP Directed  | Broadcast         | is Disabled  |                   |     |     |
| IPv4 address | 192.168.1.1/24    |              |                   |     |     |
| Command      | History           |              |                   |     |     |
| Release      |                   |              | Modification      |     |     |
10.14.1000 CommandoutputcandisplayinformationforanIPunnumbered
interfaceandIPTCPMSSconfiguration.
| 10.07orearlier |             |         | --        |     |     |
| -------------- | ----------- | ------- | --------- | --- | --- |
| Command        | Information |         |           |     |     |
| Platforms      | Command     | context | Authority |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip | source-interface |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
Description
ShowssinglesourceIPaddressconfigurationsettings.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 83

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
Examples
Showing single source IP address configuration settings for sFlow:
| switch#          | show | ip source-interface |     | sflow       |     |
| ---------------- | ---- | ------------------- | --- | ----------- | --- |
| Source-interface |      | Configuration       |     | Information |     |
----------------------------------------
| Protocol |     | Source           | Interface |     |     |
| -------- | --- | ---------------- | --------- | --- | --- |
| -------- |     | ---------------- |           |     |     |
| sflow    |     | 10.10.10.1       |           |     |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show | ip source-interface |     | all         |     |
| ---------------- | ---- | ------------------- | --- | ----------- | --- |
| Source-interface |      | Configuration       |     | Information |     |
----------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP | VRF |
| -------- | --- | ------------- | --- | ------ | --- |
----------------------------------------------------------------
| all |     | vlan2 |     | 2.2.2.2 | default |
| --- | --- | ----- | --- | ------- | ------- |
switch#
| Command        | History     |         |         |              |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- |
| Release        |             |         |         | Modification |     |
| 10.07orearlier |             |         |         | --           |     |
| Command        | Information |         |         |              |     |
| Platforms      |             | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | ipv6      | interface      |     |     |     |
| --------- | --------- | -------------- | --- | --- | --- |
| show ipv6 | interface | <INTERFACE-ID> |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv6interface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID>
SpecifiesaninterfaceID.Format:member/slot/port.
Examples
Interfaceconfiguration|84

| switch#   | show            | ipv6           | interface |         | vlan2                       |         |     |                |         |
| --------- | --------------- | -------------- | --------- | ------- | --------------------------- | ------- | --- | -------------- | ------- |
| Interface |                 | vlan2          | is up     |         |                             |         |     |                |         |
| Admin     | state           | is             | up        |         |                             |         |     |                |         |
|           | IPv6 address:   |                |           |         |                             |         |     |                |         |
|           | 2001::1/64      |                | [VALID]   |         |                             |         |     |                |         |
|           | IPv6 link-local |                | address:  |         | fe80::883a:3080:247:c1c0/64 |         |     |                | [VALID] |
|           | IPv6 Forwarding |                | feature:  |         | enabled                     |         |     |                |         |
|           | IPv6 multicast  |                | groups    | locally |                             | joined: |     |                |         |
|           | ff02::1         | ff02::1:ff00:1 |           |         | ff02::1:ff47:c1c0           |         |     | ff02::1:ff00:0 |         |
ff02::2
|           | IPv6 MTU        | 1500              |           |             |                             |                |      |                |         |
| --------- | --------------- | ----------------- | --------- | ----------- | --------------------------- | -------------- | ---- | -------------- | ------- |
|           | IPv6 TCP        | MSS               | 1440      |             |                             |                |      |                |         |
|           | IPv6 unicast    |                   | reverse   | path        | forwarding:                 |                | none |                |         |
|           | IPv6 load       | sharing:          |           | none        |                             |                |      |                |         |
| switch#   | show            | ipv6              | interface |             | 1/1/14.1                    |                |      |                |         |
| Interface |                 | 1/1/14.1          | is        | up          |                             |                |      |                |         |
| Admin     | state           | is                | up        |             |                             |                |      |                |         |
|           | IPv6 address:   |                   |           |             |                             |                |      |                |         |
|           | 30::1/64        | [VALID]           |           |             |                             |                |      |                |         |
|           | IPv6 link-local |                   | address:  |             | fe80::b86a:97c0:122:2f42/64 |                |      |                | [VALID] |
|           | IPv6 virtual    |                   | address   | configured: |                             | none           |      |                |         |
|           | IPv6 multicast  |                   | routing:  |             | disable                     |                |      |                |         |
|           | IPv6 Forwarding |                   | feature:  |             | enabled                     |                |      |                |         |
|           | IPv6 multicast  |                   | groups    | locally     |                             | joined:        |      |                |         |
|           | ff02::1         | ff02::1:ff22:2f42 |           |             |                             | ff02::1:ff00:1 |      | ff02::1:ff00:0 |         |
ff02::2
|               | IPv6 multicast  |                   | (S,G)     | entries     | joined:                     |                | none |                |         |
| ------------- | --------------- | ----------------- | --------- | ----------- | --------------------------- | -------------- | ---- | -------------- | ------- |
|               | IPv6 MTU        | 1500              |           |             |                             |                |      |                |         |
|               | IPv6 TCP        | MSS               | 1440      |             |                             |                |      |                |         |
|               | IPv6 unicast    |                   | reverse   | path        | forwarding:                 |                | none |                |         |
|               | IPv6 load       | sharing:          |           | none        |                             |                |      |                |         |
| Encapsulation |                 | dot1q             | ID:       | 20          |                             |                |      |                |         |
| switch#       | show            | ipv6              | interface |             | lag2.1                      |                |      |                |         |
| Interface     |                 | lag2.1            | is up     |             |                             |                |      |                |         |
| Admin         | state           | is                | up        |             |                             |                |      |                |         |
|               | IPv6 address:   |                   |           |             |                             |                |      |                |         |
|               | 40::1/64        | [VALID]           |           |             |                             |                |      |                |         |
|               | IPv6 link-local |                   | address:  |             | fe80::b86a:97c0:122:2f42/64 |                |      |                | [VALID] |
|               | IPv6 virtual    |                   | address   | configured: |                             | none           |      |                |         |
|               | IPv6 multicast  |                   | routing:  |             | disable                     |                |      |                |         |
|               | IPv6 Forwarding |                   | feature:  |             | enabled                     |                |      |                |         |
|               | IPv6 multicast  |                   | groups    | locally     |                             | joined:        |      |                |         |
|               | ff02::1         | ff02::1:ff22:2f42 |           |             |                             | ff02::1:ff00:1 |      | ff02::1:ff00:0 |         |
ff02::2
|               | IPv6 multicast |          | (S,G)   | entries | joined:     |     | none |     |     |
| ------------- | -------------- | -------- | ------- | ------- | ----------- | --- | ---- | --- | --- |
|               | IPv6 MTU       | 1500     |         |         |             |     |      |     |     |
|               | IPv6 TCP       | MSS      | 1440    |         |             |     |      |     |     |
|               | IPv6 unicast   |          | reverse | path    | forwarding: |     | none |     |     |
|               | IPv6 load      | sharing: |         | none    |             |     |      |     |     |
| Encapsulation |                |          | dot1q   | ID: 30  |             |     |      |     |     |
| Command       | History        |          |         |         |             |     |      |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 85

| Release |     |     |     | Modification |     |
| ------- | --- | --- | --- | ------------ | --- |
10.14.1000 CommandoutputcandisplayinformationforanIPunnumbered
interfaceandIPv6TCPMSSconfiguration.
| 10.07orearlier      |         |         |     | --        |     |
| ------------------- | ------- | ------- | --- | --------- | --- |
| Command Information |         |         |     |           |     |
| Platforms           | Command | context |     | Authority |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ipv6 | source-interface |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- |
show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch# show     | ipv6 | source-interface |             | sflow |     |
| ---------------- | ---- | ---------------- | ----------- | ----- | --- |
| Source-interface |      | Configuration    | Information |       |     |
----------------------------------------
| Protocol |     | Source Interface |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| -------- |     | ---------------- |     |     |     |
| sflow    |     | 2001:DB8::1      |     |     |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch# show     | ipv6 | source-interface |             | all |     |
| ---------------- | ---- | ---------------- | ----------- | --- | --- |
| Source-interface |      | Configuration    | Information |     |     |
---------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP | VRF |
| -------- | --- | ------------- | --- | ------ | --- |
---------------------------------------------------------------
| all |     | vlan2 |     | 2001::1 | default |
| --- | --- | ----- | --- | ------- | ------- |
switch#
Interfaceconfiguration|86

| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| shutdown | (interface) |     |     |     |
| -------- | ----------- | --- | --- | --- |
shutdown
no shutdown
Description
Disablesaninterface.Interfacesaredisabledbydefaultwhencreated.
Thenoformofthiscommandenablesaninterface.
Examples
Disablinganinterface:
| switch(config-if)# |     | shutdown |     |     |
| ------------------ | --- | -------- | --- | --- |
Enablinganinterface:
| switch(config-if)#  |         | no shutdown |              |     |
| ------------------- | ------- | ----------- | ------------ | --- |
| Command History     |         |             |              |     |
| Release             |         |             | Modification |     |
| 10.07orearlier      |         |             | --           |     |
| Command Information |         |             |              |     |
| Platforms           | Command | context     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
speed
| speed {<SPEED> | | <SPEED-DUPLEX> | | auto | [<SPEED>] | }   |
| -------------- | ---------------- | ------ | --------- | --- |
no speed
Description
Configuresthelinkspeed,duplex,andauto-negotiationsettingsforaninterface.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 87

The no form of this command removes the configurations and returns to the defaults.

Parameter

Speed

10-full

10-half

100-full

100-half

1000-full

10g

25g

40g

50g

100g

200g

400g

Description

Configures interface speed, duplex, and auto-negotiation.

10 Mbps, full duplex, no auto-negotiation

10 Mbps, half duplex, no auto-negotiation

100 Mbps, full duplex, no auto-negotiation

100 Mbps, half duplex, no auto-negotiation

1000 Mbps, full duplex, no auto-negotiation

10 Gbps, full duplex, no auto-negotiation

25 Gbps, full duplex, no auto-negotiation

40 Gbps, full duplex, no auto-negotiation

50 Gbps, full duplex, no auto-negotiation

100 Gbps, full duplex, no auto-negotiation

200 Gbps, full duplex, no auto-negotiation

NOTE: Not applicable for override.

400 Gbps, full duplex, no auto-negotiation

NOTE: Not applicable for override.

auto

Auto-negotiate speed and duplex. More than one speed can be
set at a time.

10m

100m

1g

2.5g

5g

10g

25g

40g

50g

100g

Allow interface to link at 10 Mbps.

Allow interface to link at 100 Mbps.

Allow interface to link at 1 Gbps.

Allow interface to link at 2.5 Gbps.

Allow interface to link at 5 Gbps.

Allow interface to link at 10 Gbps.

Allow interface to link at 25 Gbps.

Allow interface to link at 40 Gbps.

Allow interface to link at 50 Gbps.

Allow interface to link at 100 Gbps.

Interface configuration | 88

Parameter Description
200g Allowinterfacetolinkat200Gbps.
400g Allowinterfacetolinkat400Gbps.
Usage
Thefollowingoptionscanbeconfiguredforaninterface.Theoptionavailableisbasedontheinterface
type.
speed <SPEED-DUPLEX>
Usesafixedspeedandduplexmodewithnoauto-negotiation.Half-duplexisonlysupportedfor10
Mbpsand100Mbpslinkspeeds.
speed <SPEED>
Usesafixedspeedwithnoauto-negotiation.Ifthecurrentlyinstalledtransceiverdoesnotsupport
thespeed,thesettingisignoredandtheportwillusethehighestspeedthatissupported.
speed auto
Usesauto-negotiationandoffersallspeedssupportedbytheportandtransceiver.Thisisthe
default.Ifthelinktechnologydoesnotsupportauto-negotiationthissettingisignored,andtheport
usesthehighestpossiblefixedspeed.
speed auto <SPEED>
Usesauto-negotiationandoffersthespecifiedspeedsonly.Forportsthatsupportpluggable
transceivers,onlyspeedssupportedbythetransceiverareofferedandotherspeedsareignored.If
thelinktechnologydoesnotsupportauto-negotiation,thissettingisignoredandtheportusesthe
highestpossiblefixedspeed.
Examples
Configuringaninterfacetooperateatafixedspeedof1000Mbpswithfullduplexandnoauto-
negotiation:
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | speed     | 1000-full |
Configuringaninterfacetooperateatafixedspeedof10Gbpswithnoauto-negotiation:
| switch(config)#    | interface | 1/1 |
| ------------------ | --------- | --- |
| switch(config-if)# | speed     | 10g |
Configuringaninterfacetoauto-negotiateandadvertiseonly1Gbpsand2.5Gbpsspeeds:
| switch(config)#    | interface | 1/1/1        |
| ------------------ | --------- | ------------ |
| switch(config-if)# | speed     | auto 1g 2.5g |
Configuringaninterfacetooverridethedetectedtransceiverspeedandusetheconfiguredspeedifthe
installedtransceiverdoesnotsupportauto-negotiation:
| switch(config)#         | interface | 1/1/1             |
| ----------------------- | --------- | ----------------- |
| switch(config-if)#speed |           | auto 50g override |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 89

Configuringaninterfacetousedefaultsettingsforspeed,duplex,andauto-negotiation:
| switch(config)#      | interface | 1/1/1   |                                          |
| -------------------- | --------- | ------- | ---------------------------------------- |
| switch(config-if)#no |           | speed   |                                          |
| Command History      |           |         |                                          |
| Release              |           |         | Modification                             |
| 10.09.0001           |           |         | SpeedsnotsupportedbyhardwarehiddenbyCLI. |
| 10.07orearlier       |           |         | --                                       |
| Command Information  |           |         |                                          |
| Platforms            | Command   | context | Authority                                |
4100i config-if Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
Interfaceconfiguration|90

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
dns
SelectsDNS.
ntp
SelectsNTP.
radius
Selectsradius.
sflow
SelectssFLow.
simplivity
91
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries)

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
Selectssimplivity.
syslog
Selectssyslog.
tacacs
SelectsTACACS.
tftp
SelectsTFTP.
| <IP-ADDR> |     | SpecifiestheIPv4address. |     |
| --------- | --- | ------------------------ | --- |
vrf <VRF-NAME>
SpecifiestheVRF name.
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
Sourceinterfaceselection|92

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
n all:Selectsthesourceforallprotocolscoveredbythis
command.
n central:SelectsHPE ArubaNetworkingCentral.
n dhcp_relay:SelectsDHCPrelay.Whenyouconfigureadhcp_
relaysourceinterface,youmustalsoenableDHCPrelay
Option82usingthedhcp-relayoption82source-interface
command.
n dns:SelectsDNS.
n http:SelectsHTTP.
n ntp:SelectsNTP.
n radius:SelectsRADIUS.
n sflow:SelectssFLow.
n sftp-scp:SelectsSFTPandSCP.
n ssh-client:SelectsSSHClient.
syslog:Selectsthesourceforsyslogpackets.
n
n tacacs:SelectsthesourceforTACACSpackets.
n tftp:SelectsTFTP.
n ubt:SelectsUBT.
SpecifiestheVRF name.
| <IFNAME> |     |     | Specifiestheinterfacename. |     |
| -------- | --- | --- | -------------------------- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 93

| Parameter      |     | Description              |     |
| -------------- | --- | ------------------------ | --- |
| <IP-ADDR>      |     | SpecifiestheIPv4address. |     |
| vrf <VRF-NAME> |     | SpecifiestheVRF name.    |     |
Examples
ConfiguringIPv4source-interfaceinterface1/1/1tousefortheTFTP protocol:
| switch(config)# | ip source-interface | tftp interface | 1/1/1 |
| --------------- | ------------------- | -------------- | ----- |
ConfiguringIPv4source-interfaceinterface1/1/2tousefortheTFTP protocolonVRFgreen:
switch(config)# ip source-interface tftp interface 1/1/2 vrf green
RemovingIPv4source-interface1/1/1configurationfortheTFTP protocol:
| switch(config)# | no ip source-interface | tftp interface | 1/1/1 |
| --------------- | ---------------------- | -------------- | ----- |
Removingsource-interfaceinterface1/1/2configurationforTFTP protocolonVRFgreen:
switch(config)# no ip source-interface tftp interface 1/1/2 vrf green
Configuringsource-interfaceIPv410.1.1.1tousefortheTFTPprotocol:
switch(config)#
|     | ip source-interface | tftp 10.1.1.1 |     |
| --- | ------------------- | ------------- | --- |
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
Sourceinterfaceselection|94

| switch(config)# |     | ip  | source-interface |     |     | dns 10.1.1.2 | vrf green |
| --------------- | --- | --- | ---------------- | --- | --- | ------------ | --------- |
Removingsource-interfaceIPv410.1.1.1configurationfortheDNSprotocol:
| switch(config)# |     | no  | ip source-interface |     |     | tftp 10.1.1.1 |     |
| --------------- | --- | --- | ------------------- | --- | --- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationfortheDNSprotocolonVRFgreen:
| switch(config)#     |         | no  | ip source-interface |     |                                                | dns 10.1.1.2 | vrf green |
| ------------------- | ------- | --- | ------------------- | --- | ---------------------------------------------- | ------------ | --------- |
| Command History     |         |     |                     |     |                                                |              |           |
| Release             |         |     |                     |     | Modification                                   |              |           |
| 10.12.1000          |         |     |                     |     | Addedcentral,sftp-scp,andssh-clientparameters. |              |           |
| 10.07orearlier      |         |     |                     |     | --                                             |              |           |
| Command Information |         |     |                     |     |                                                |              |           |
| Platforms           | Command |     | context             |     | Authority                                      |              |           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 source-interface (<protocol> |     |            |            |             |     | <ip-addr>)       |             |
| --------------------------------- | --- | ---------- | ---------- | ----------- | --- | ---------------- | ----------- |
| ipv6 source-interface             |     |            | <PROTOCOL> | <IPV6-ADDR> |     | [vrf             | <VRF-NAME>] |
| no source-interface               |     | <PROTOCOL> |            | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |             |
Description
Configuresthesource-interfaceIPv6addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedprotocolconfiguration.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<PROTOCOL>
Specifiestheprotocoltoconfigure.
n all:Selectsallprotocolssupportedbythiscommand.
n central:SelectsArubaCentral.
n ntp:SelectsNTP.
n radius:Selectsradius.
n sflow:SelectssFLow.
n syslog:Selectssyslog.
tacacs:SelectsTACACS.
n
n tftp:SelectsTFTP.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 95

| Parameter      |     |     | Description              |     |
| -------------- | --- | --- | ------------------------ | --- |
| <IPV6-ADDR>    |     |     | SpecifiestheIPv6address. |     |
| vrf <VRF-NAME> |     |     | SpecifiestheVRF name.    |     |
Examples
Configuringsource-interfaceIPv61111:2222tousefortheTFTP protocol:
| switch(config)# | ipv6 | source-interface | tftp 1111:2222 |     |
| --------------- | ---- | ---------------- | -------------- | --- |
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
| ipv6 source-interface |     | dns |     |     |
| --------------------- | --- | --- | --- | --- |
ipv6 source-interface {dns | all} {interface | X:X::X:X} [vrf <VRF-NAME>]
[no] ipv6 source-interface {dns | all} {interface | X:X::X:X} [vrf <VRF-NAME>]
Description
ConfigurestheIPv6source-interfaceorsourceIP forIPv6DNS clients.
Thenoformofthiscommandremovesallconfigurations.
Sourceinterfaceselection|96

| Parameter  |     |     |     | Description                      |     |
| ---------- | --- | --- | --- | -------------------------------- | --- |
| <PROTOCOL> |     |     |     | Specifiestheprotocoltoconfigure. |     |
n all:Selectsallprotocolssupportedbythiscommand.
n central:SelectsHPE ArubaNetworkingCentral.
n dhcp_relay:SelectsDHCPrelay.
n dns:SelectsDNS packetsource.
n http:SelectsHTTP.
n ntp:SelectsNTP.
n radius:Selectsradius.
sftp-scp:SelectsSFTPandSCP.
n
n sflow:SelectssFLow.
n ssh-client:SelectsSSHClient.
n syslog:Selectssyslog.
n tacacs:SelectsTACACS.
| <IPV6-ADDR>    |     |     |     | SpecifiestheIPv6address. |     |
| -------------- | --- | --- | --- | ------------------------ | --- |
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRF name.    |     |
Examples
ConfiguringIPv6source-interfacedns:
| switch(config)# |            | ipv6 | source-interface |               |                  |
| --------------- | ---------- | ---- | ---------------- | ------------- | ---------------- |
|                 | all        |      | All protocols    |               |                  |
|                 | central    |      | HPE Aruba        | Networking    | Central protocol |
|                 | dhcp_relay |      | DHCP_RELAY       | protocol      |                  |
|                 | dns        |      | DNS protocol     |               |                  |
|                 | http       |      | HTTP protocol    |               |                  |
|                 | ntp        |      | NTP protocol     |               |                  |
|                 | radius     |      | RADIUS           | protocol      |                  |
|                 | sflow      |      | sFlow protocol   |               |                  |
|                 | sftp-scp   |      | SFTP and         | SCP protocols |                  |
|                 | ssh-client |      | SSH Client       | protocol      |                  |
|                 | syslog     |      | syslog           | protocol      |                  |
|                 | tacacs     |      | TACACS           | protocol      |                  |
|                 | tftp       |      | TFTP protocol    |               |                  |
ConfiguringIPv6source-interfacedns:
| switch(config)# |         | ipv6 | source-interface |         | dns |
| --------------- | ------- | ---- | ---------------- | ------- | --- |
| X:X::X:X        | Specify |      | an IPv6          | address |     |
interface
|     | Interface |     | information |     |     |
| --- | --------- | --- | ----------- | --- | --- |
ConfiguringIPv6source-interfacednson1::1:
| switch(config)# |                   | ipv6 | source-interface |     | dns 1::1 |
| --------------- | ----------------- | ---- | ---------------- | --- | -------- |
| vrf             | VRF Configuration |      |                  |     |          |
<cr>
ConfiguringIPv6source-interfacednson1::1:vrf:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 97

| switch(config)# | ipv6 | source-interface | dns 1::1 | vrf |
| --------------- | ---- | ---------------- | -------- | --- |
VRF_NAME
VRF name
ConfiguringIPv6source-interfacednson1::1vrfBLUE
| switch(config)# | ipv6          | source-interface | dns 1::1 vrf  | BLUE   |
| --------------- | ------------- | ---------------- | ------------- | ------ |
| switch(config)# | ipv6          | source-interface | dns interface | vlan10 |
| vrf VRF         | Configuration |                  |               |        |
<cr>
ConfiguringIPv6source-interfacednsonvlan10vrfBLUE:
switch(config)# ipv6 source-interface dns interface vlan10 vrf BLUE
| Command History |     |     |              |     |
| --------------- | --- | --- | ------------ | --- |
| Release         |     |     | Modification |     |
10.13
Commandintroduced.
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 source-interface
ipv6 source-interface <PROTOCOL> {<IPV6-ADDR>|interface <IFNAME>} [vrf <VRF-NAME>]
no ipv6 source-interface <PROTOCOL> {<IPV6-ADDR>|interface <IFNAME>} [vrf <VRF-NAME>]
Description
ConfigurestheIPv6source-interfaceinterfacetouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesallconfigurations.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PROTOCOL>
Specifiestheprotocoltoconfigure.
all
Selectsallprotocolssupportedbythiscommand.
central
SelectsHPE ArubaNetworkingCentral.
dhcp_relay
SelectsDHCPrelay.
dns
Sourceinterfaceselection|98

Parameter

Description

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

Configuring IPv6 source-interface interface 1/1/1 to use for the TFTP protocol :

switch(config)# ipv6 source-interface tftp interface 1/1/1

Configuring IPv6 source-interface interface 1/1/2 to use for the TFTP protocol on VRF green :

switch(config)# ipv6 source-interface tftp interface 1/1/2 vrf green

Removing IPv6 source-interface interface 1/1/1 configuration for the TFTP protocol:

switch(config)# no ipv6 source-interface tftp interface 1/1/1

Removing IPv6 source-interface interface 1/1/2 configuration for the TFTP protocol on VRF green:

switch(config)# no ipv6 source-interface tftp interface 1/1/2 vrf green

Configuring source-interface IPv6 1111:2222 to use for the TFTP protocol:

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

99

| switch(config)# | ipv6 | source-interface | tftp 1111:2222 |     |
| --------------- | ---- | ---------------- | -------------- | --- |
Configuringsource-interfaceIPv61111:3333touseforTFTPprotocolonVRF green:
| switch(config)# | ipv6 | source-interface | tftp 1111:3333 | vrf green |
| --------------- | ---- | ---------------- | -------------- | --------- |
Removingsource-interfaceIPv61111:2222configurationforTFTPprotocol:
| switch(config)# | no  | ipv6 source-interface | tftp 1111:2222 |     |
| --------------- | --- | --------------------- | -------------- | --- |
Removingsource-interfaceIPv61111:3333configurationforTFTPprotocolonVRFgreen:
switch(config)# no ipv6 source-interface tftp 1111:3333 vrf green
| Command History |     |     |                               |     |
| --------------- | --- | --- | ----------------------------- | --- |
| Release         |     |     | Modification                  |     |
| 10.13.0001      |     |     | Addedthednsprotocolparameter. |     |
10.12.1000 Addedcentral,sftp-scp,dhcp_relayandssh-clientparameters.
| 10.07orearlier      |         |         | --        |     |
| ------------------- | ------- | ------- | --------- | --- |
| Command Information |         |         |           |     |
| Platforms           | Command | context | Authority |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip source-interface |     |     |     |     |
| ------------------------ | --- | --- | --- | --- |
show ip source-interface <PROTOCOL> [vrf <VRF-NAME> | all-vrfs]
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
ShowsthesourceinterfaceconfigurationforHPE Aruba
NetworkingCentral.
Sourceinterfaceselection|100

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
dhcp relay
ShowsthesourceinterfaceconfigurationforDHCP
relay.
dns
ShowsthesourceinterfaceconfigurationforDNS.
http
ShowsthesourceinterfaceconfigurationforHTTP.
ntp
ShowsthesourceinterfaceconfigurationforNTP.
radius
Showsthesourceinterfaceconfigurationforradius.
sflow
ShowsthesourceinterfaceconfigurationforsFLow.
sftp-scp
ShowssourceinterfaceconfigurationforSFTPandSCP.
ssh-client
ShowssourceinterfaceconfigurationforSSHClient.
syslog
Showsthesourceinterfaceconfigurationforsyslog.
tacacs
ShowsthesourceinterfaceconfigurationforTACACS.
tftp
ShowsthesourceinterfaceconfigurationforTFTP.
ubt
ShowsthesourceinterfaceconfigurationforPTP.
vrf <VRF-NAME>
SpecifiestheVRF name.
| all-vrfs |     | ShowsthesourceinterfaceconfigurationforallVRFs. |     |
| -------- | --- | ----------------------------------------------- | --- |
Examples
Displayingallsource-interfaceprotocolconfigurationsforVRF red:
| switch# show     | ip source-interface | all vrf red |     |
| ---------------- | ------------------- | ----------- | --- |
| Source-interface | Configuration       | Information |     |
---------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
---------------------------------------------------------------
| all | 1/1/1 |     | red |
| --- | ----- | --- | --- |
switch#
Displayingallsource-interfaceprotocolconfigurationsfordefaultVRF:
| switch# show     | ip source-interface | all         |     |
| ---------------- | ------------------- | ----------- | --- |
| Source-interface | Configuration       | Information |     |
-------------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
-------------------------------------------------------------------
| all |     | 1.1.1.1 | default |
| --- | --- | ------- | ------- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 101

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
| Parameter  |     |     | Description                 |     |
| ---------- | --- | --- | --------------------------- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoshow. |     |
all
Showsthesourceinterfaceconfigurationforallother
protocols.
central
ShowsthesourceinterfaceconfigurationforHPE Aruba
NetworkingCentral.
dhcp_relay
ShowsthesourceinterfaceconfigurationforDHCP
realy.
dns
Sourceinterfaceselection|102

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
ShowsthesourceinterfaceconfigurationforDNS.
http
ShowsthesourceinterfaceconfigurationforHTTP.
ntp
ShowsthesourceinterfaceconfigurationforNTP.
radius
Showsthesourceinterfaceconfigurationforradius.
sflow
ShowsthesourceinterfaceconfigurationforsFLow.
sftp-scp
ShowssourceinterfaceconfigurationforSFTPandSCP.
ssh-client
ShowssourceinterfaceconfigurationforSSHClient.
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
| all |     | 1111::2222 | default |
| --- | --- | ---------- | ------- |
switch#
DisplayingallIPv6source-interfaceprotocolconfigurationforVRFred:
| switch# show     | ipv6 source-interface | all vrf red |     |
| ---------------- | --------------------- | ----------- | --- |
| Source-interface | Configuration         | Information |     |
---------------------------------------------------------------
| Protocol | Src-Interface | Src-IP | VRF |
| -------- | ------------- | ------ | --- |
---------------------------------------------------------------
| all | 1/1/1 | 2005::2 | red |
| --- | ----- | ------- | --- |
switch#
Displaying allIPv6source-interfaceprotocolconfigurationsforallVRFs:
| switch# show     | ipv6 source-interface | all all-vrfs |     |
| ---------------- | --------------------- | ------------ | --- |
| Source-interface | Configuration         | Information  |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 103

-------------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP | VRF |
| -------- | --- | ------------- | --- | ------ | --- |
-------------------------------------------------------------------
| all |     |       |     | 2222::3333 | all-vrfs |
| --- | --- | ----- | --- | ---------- | -------- |
| all |     |       |     | 1111::2222 | default  |
| all |     | 1/1/1 |     | 2::2       | red      |
DisplayingallIPv6source-interfaceprotocolconfirgurationsfordnsallVRFs:
| switch# show     | ipv6 | source-interface |             | dns all-vrfs |     |
| ---------------- | ---- | ---------------- | ----------- | ------------ | --- |
| Source-interface |      | Configuration    | Information |              |     |
----------------------------------------------------------------------------------
--
| Protocol |     | Src-Interface |     | Src-IP | VRF |
| -------- | --- | ------------- | --- | ------ | --- |
----------------------------------------------------------------------------------
--
| dns             |     |     |     | 1::3                | blue    |
| --------------- | --- | --- | --- | ------------------- | ------- |
| dns             |     |     |     | 1::4                | default |
| dns             |     |     |     | 1::2                | red     |
| Command History |     |     |     |                     |         |
| Release         |     |     |     | Modification        |         |
| 10.13           |     |     |     | Addeddnsparameters. |         |
10.12.1000
|                     |         |         |     | Added central,sftp-scp,andssh-clientparameters. |     |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- | --- |
| 10.07orearlier      |         |         |     | --                                              |     |
| Command Information |         |         |     |                                                 |     |
| Platforms           | Command | context |     | Authority                                       |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show running-config
show running-config
Description
Displaysthecurrentrunningconfiguration.
Examples
Displayingtherunningconfiguration(onlyitemsofinteresttosourceinterfaceselectionareshownin
thisexampleoutputcommand):
HPE ArubaNetworkingCentralisthepriorityagent.Ifnocommandisspecifiedforipsource-interface,Central
willchoosethecommandautomaticallyifitisreachableonanyoftheknownports.
Sourceinterfaceselection|104

| switch# show | running-config |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
vrf green
| ip source-interface   |                      | tftp interface     | 1/1/2 | vrf       | green     |
| --------------------- | -------------------- | ------------------ | ----- | --------- | --------- |
| ip source-interface   |                      | radius interface   |       | 1/1/2     | vrf green |
| ip source-interface   |                      | ntp interface      | 1/1/2 | vrf       | green     |
| ip source-interface   |                      | tacacs interface   |       | 1/1/2     | vrf green |
| ip source-interface   |                      | dns interface      | 1/1/2 | vrf       | green     |
| ip source-interface   |                      | central interface  |       | 1/1/2     | vrf green |
| ip source-interface   |                      | all interface      | 1/1/2 | vrf       | green     |
| ipv6 source-interface |                      | tftp 2222::3333    |       | vrf       | green     |
| ipv6 source-interface |                      | radius 2222::3333  |       | vrf       | green     |
| ipv6 source-interface |                      | ntp 2222::3333     |       | vrf green |           |
| ipv6 source-interface |                      | tacacs 2222::3333  |       | vrf       | green     |
| ipv6 source-interface |                      | central 2222::3333 |       | vrf       | green     |
| ipv6 source-interface |                      | all 2222::3333     |       | vrf green |           |
| ip source-interface   |                      | tftp 10.20.3.1     |       |           |           |
| ip source-interface   |                      | radius 10.20.3.1   |       |           |           |
| ip source-interface   |                      | ntp 10.20.3.1      |       |           |           |
| ip source-interface   |                      | tacacs 10.20.3.1   |       |           |           |
| ip source-interface   |                      | dns 10.20.3.1      |       |           |           |
| ip source-interface   |                      | central 10.20.3.1  |       |           |           |
| ip source-interface   |                      | all 10.20.3.1      |       |           |           |
| interface             | 1/1/1                |                    |       |           |           |
| no                    | shutdown             |                    |       |           |           |
| ip                    | address 10.20.3.1/24 |                    |       |           |           |
| interface             | 1/1/2                |                    |       |           |           |
| vrf                   | attach green         |                    |       |           |           |
| ip                    | address 20.1.1.1/24  |                    |       |           |           |
| ipv6                  | address              | 2222::3333/64      |       |           |           |
| interface             | 1/1/45               |                    |       |           |           |
| no                    | shutdown             |                    |       |           |           |
| ip                    | address 100.1.0.1/24 |                    |       |           |           |
| ipv6                  | address              | 1111::2222/64      |       |           |           |
| ip route              | 100.2.0.0/24         | 10.20.3.2          |       |           |           |
switch#
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 105

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

106

Chapter 8
|               |               |            | Configuration | and firmware |
| ------------- | ------------- | ---------- | ------------- | ------------ |
| Configuration | and firmware  | management |               |              |
| Upgrade       | and downgrade | scenarios  |               |              |
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
107
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries)

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

n AOS-CX hot-patch software can be obtained from HPE Aruba Networking customer support, and is

identified with a .patch extension. The name of the patch indicates the version of AOS-CX to which it
can be applied. For example, the patch FL.10.12.XXXX-YYYY.patch indicates that the patch can be
applied on top of switch image FL.10.12.XXXX.swi and brings software up to date with the
FL.10.12.YYYY release.

n Hot-patch software can be applied only after it has been downloaded to the switch.

Caveats and limitations

n Hot-patch files cannot be managed when the switch is loaded with a .swi image that does not

support the hot-patch feature.

n Only restartable daemons can be updated with a hot-patch file.

Configuration and firmware management | 108

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
1. Requestahot-patchfromHPE ArubaNetworkingcustomersupport,thenplacethehot-patchon
anFTP-SFTPserver.
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 109

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

Configuration and firmware management | 110

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 111

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
Configurationandfirmwaremanagement |112

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 113

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
Configurationandfirmwaremanagement |114

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 115

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
Configurationandfirmwaremanagement |116

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 117

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
Configurationandfirmwaremanagement |118

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 119

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
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<CHECKPOINT-NAME> Specifiesthenameofthecheckpointtocopy.Thecheckpoint
namecanbealphanumeric.Itcanalsocontainunderscores(_)
anddashes(-).
Configurationandfirmwaremanagement |120

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
NOTE:DonotstartthecheckpointnamewithCPCbecauseitis
usedforsystem-generatedcheckpoints.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 121

| Parameter      |     |     | Description                        |     |
| -------------- | --- | --- | ---------------------------------- | --- |
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname.Default:default. |     |
Examples
Copyingacheckpointformatfiletocheckpointckpt5onthedefaultVRF:
| switch# copy | tftp://192.168.1.10/ckptmeta |     | checkpoint | ckpt5 |
| ------------ | ---------------------------- | --- | ---------- | ----- |
######################################################################### 100.0%
100.0%
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy <REMOTE-URL> |     | startup-config|running-config |     |     |
| ----------------- | --- | ----------------------------- | --- | --- |
copy <REMOTE-URL> startup-config|{running-config [overwrite]} [vrf <VRF-NAME>]
Description
Copiesaremotefilecontainingaswitchconfigurationtotherunningconfigurationortothestartup
configuration.
| Parameter    |     |     | Description                                 |     |
| ------------ | --- | --- | ------------------------------------------- | --- |
| <REMOTE-URL> |     |     | Specifiesaremotefilewiththefollowingsyntax: |     |
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
startup-config Indicatesthatthestartupconfigurationreceivesthecopiedcheckpoint
configuration.Ifthestartupconfigurationisalreadypresent,the
commandoverwritesthestartupconfiguration.
running-config Indicatesthattherunningconfigurationreceivesthecopied
checkpointconfiguration.
Configurationandfirmwaremanagement |122

Parameter

overwrite

Description

By default, the CLI configuration contained in the coped file is applied
on top of the running-config, so the CLI command does not clear the
running-config before applying the CLI commands. In the event that a
particular CLI command fails then the failure is logged in event logs
and the next line in CLI configuration is processed.

When you include the overwrite parameter, the configuration is only
applied to the running-config if all the commands succeeded without
errors. If there are any errors during the copy process, the existing
running-config will remain intact. You can then inspect the event logs
to check and fix the errors and retry the operation. If more than 20
errors are present, the operation stops processing any further
commands. The event logs will display only those errors procesed up
to that point.

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

123

| switch# copy | tftp://192.168.1.10/startjson |     | startup-config |
| ------------ | ----------------------------- | --- | -------------- |
######################################################################### 100.0%
100.0%
Success
Copyinganunsupportedfileformattothestartupconfiguration:
| switch# copy | tftp://192.168.1.10/startfile |     | startup-config |
| ------------ | ----------------------------- | --- | -------------- |
######################################################################### 100.0%
100.0%
| unsupported         | file format |         |                                    |
| ------------------- | ----------- | ------- | ---------------------------------- |
| Command History     |             |         |                                    |
| Release             |             |         | Modification                       |
| 10.15               |             |         | Theoverwriteparameterisintroduced. |
| 10.07orearlier      |             |         | --                                 |
| Command Information |             |         |                                    |
| Platforms           | Command     | context | Authority                          |
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
Configurationandfirmwaremanagement |124

| switch# copy | running-config | startup-config |     |     |
| ------------ | -------------- | -------------- | --- | --- |
Success
Copyingtherunningconfigurationtoanewcheckpointnamedckpt1:
| switch# copy | running-config | checkpoint | ckpt1 |     |
| ------------ | -------------- | ---------- | ----- | --- |
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
| copy {running-config |     | | startup-config} |     | <REMOTE-URL> |
| -------------------- | --- | ----------------- | --- | ------------ |
copy {running-config | startup-config} <REMOTE-URL> {cli | json} [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationorthestartupconfigurationtoaremotefileineitherCLIorJSON
format.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationiscopiedtoaremotefile.
| <REMOTE-URL> |     |     | Specifiestheremotefileusingthesyntax: |     |
| ------------ | --- | --- | ------------------------------------- | --- |
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
| {cli | json}   |     |     | Selectstheremotefileformat:P:CLIorJSON. |     |
| -------------- | --- | --- | --------------------------------------- | --- |
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |
Examples
CopyingarunningconfigurationtoaremotefileinCLIformat:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 125

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
CopyingastartupconfigurationtoaremotefileinJSONformat:
switch# copy startup-config sftp://root@192.168.1.10/startjson json
| root@192.168.1.10's |     | password: |     |     |     |
| ------------------- | --- | --------- | --- | --- | --- |
sftp>
| root@192.168.1.10's |                  | password:          |     |     |     |
| ------------------- | ---------------- | ------------------ | --- | --- | --- |
| sftp> put           | /tmp/startjson   | startjson          |     |     |     |
| Uploading           | /tmp/startjson   | to /root/startjson |     |     |     |
| Connected           | to 192.168.1.10. |                    |     |     |     |
Success
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| copy {running-config |     | | startup-config} |     | <STORAGE-URL> |     |
| -------------------- | --- | ----------------- | --- | ------------- | --- |
copy {running-config | startup-config} <STORAGE-URL> {cli | json}
Description
CopiestherunningconfigurationorastartupconfigurationtoaUSBdrive.
Configurationandfirmwaremanagement |126

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{running-config | startup-config} Selectstherunningconfigurationorthestartupconfigurationto
becopiedtotheswitchUSBdrive.
<STORAGE-URL>
Specifiesaremotefilewiththefollowingsyntax:usb:/<file>
| {cli | json} |     |     | Selectstheformatoftheremotefile:CLIorJSON. |     |
| ------------ | --- | --- | ------------------------------------------ | --- |
Usage
TheswitchsupportsJSONandCLIfileformatswhencopyingtherunningorstartingconfigurationtothe
USBdrive.TheUSBdrivemustbeformattedwiththeFATfilesystem.
TheUSBdrivemustbeenabledandmountedwiththefollowingcommands:
| switch(config)# | usb   |     |     |     |
| --------------- | ----- | --- | --- | --- |
| switch(config)# | end   |     |     |     |
| switch# usb     | mount |     |     |     |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 127

| switch# copy | startup-config | running-config |     |
| ------------ | -------------- | -------------- | --- |
Success
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy <STORAGE-URL> |     | running-config |     |
| ------------------ | --- | -------------- | --- |
copy <STORAGE-URL> {running-config | startup-config | checkpoint <CHECKPOINT-NAME>}
Description
ThiscommandcopiesaspecifiedconfigurationfromtheUSBdrivetotherunningconfiguration,toa
startupconfiguration,ortoacheckpoint.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<STORAGE-URL> SpecifiesthenameofaconfigurationfileontheUSBdrivewith
thesyntax:usb:/<FILE>
running-config
Specifiesthattheconfigurationfileiscopiedtotherunning
configuration.ThefilemustbeinCLI,JSON,orcheckpointformat
orthecopywillfail.thecopywillnotwork.
startup-config Specifiesthattheconfigurationfileiscopiedtothestartup
configuration.Theswitchstoresthisconfigurationbetween
reboots.Thestartupconfigurationisusedastheoperating
configurationfollowingarebootoftheswitch.Thefilemustbein
JSONorcheckpointformatorthecopywillfail.
checkpoint <CHECKPOINT-NAME> Specifiesthenameofanewcheckpointfiletoreceiveacopyof
theconfiguration.TheconfigurationfileontheUSBdrivemustbe
incheckpointformat.
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitis
usedforsystem-generatedcheckpoints.
Usage
ThiscommandrequiresthattheUSBdriveisformattedwiththeFATfilesystemandthatthefilebein
theappropriateformatasfollows:
Configurationandfirmwaremanagement |128

n running-config:ThisoptionrequiresthefileontheUSBdrivebeinCLI,JSON,orcheckpointformat.
n startup-config:ThisoptionrequiresthefileontheUSBdrivebeinJSONorcheckpointformat.
checkpoint <checkpoint-name>:ThisoptionrequiresthefileontheUSBdrivebeincheckpoint
n
format.
Examples
CopyingthefilerunClifromtheUSBdrivetotherunningconfiguration:
| switch# copy | usb:/runCli |     | running-config |     |
| ------------ | ----------- | --- | -------------- | --- |
Configuration may take several minutes to complete according to configuration
file size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Success
CopyingthefilestartUpfromtheUSBdrivetothestartupconfiguration:
| switch# copy | usb:/startUp |     | startup-config |     |
| ------------ | ------------ | --- | -------------- | --- |
Success
CopyingthefiletestCheckfromtheUSBdrivetotheabccheckpoint:
| switch# copy | usb:/testCheck |     | checkpoint | abc |
| ------------ | -------------- | --- | ---------- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 129

| Parameter  |                   |     | Description                                 |
| ---------- | ----------------- | --- | ------------------------------------------- |
| checkpoint | <CHECKPOINT-NAME> |     | Specifiesthenameofacheckpoint.              |
| core-dump  |                   |     | Eraseoneofthefollowingsetsofcore-dumpfiles: |
| all|daemon | <daemon-name>     |     |                                             |
n all:Eraseallcore-dumpfiles.
|kernel|vsf
n daemon<daemon-name>:Erasedaemoncore-dumpfiles.
n kerne:lErasethekernelcore-dump.
n
| startup-config |     |     | Specifiesthestartupconfiguration. |
| -------------- | --- | --- | --------------------------------- |
| all            |     |     | Specifiesallcheckpoints.          |
Examples
Erasingcheckpointckpt1:
| switch# | erase checkpoint | ckpt1 |     |
| ------- | ---------------- | ----- | --- |
Erasingthestartupconfiguration:
| switch# | erase startup-config |     |     |
| ------- | -------------------- | --- | --- |
Erasingallcheckpoints:
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
Configurationandfirmwaremanagement |130

Parameter Description
<CHECKPOINT-NAME> Specifiesthenameofacheckpoint.
[json] SpecifiesthattheoutputisdisplayedinJSONformat.
Examples
Showingtheconfigurationoftheckpt1checkpointinCLIformat:
| switch#    | show checkpoint | ckpt1 |
| ---------- | --------------- | ----- |
| Checkpoint | configuration:  |       |
!
| !Version             | AOS-CX PL.10.07.0000K-75-g55e5193 |                     |
| -------------------- | --------------------------------- | ------------------- |
| !export-password:    | default                           |                     |
| lacp system-priority |                                   | 65535               |
| user admin           | group administrators              | password ciphertext |
AQBapQjwipebv36io0jFfde7ZzrHckncal1D+3n8XFTZKQdmYgAAADEtYOeHSme93xzdD0uz6Vr9Kl+XBz
B+2GB0UBxSF7rvgN2x8KSgkqv7iqXVQ0Te6LkSMnH4BdNaT3Bf25qyvOqmr4YakO1V3rg8zAOADkPktQD8
joTHXflzwomoIzcmv/uX
cli-session
| timeout | 0   |     |
| ------- | --- | --- |
!
!
!
!
| ssh server | vrf default |     |
| ---------- | ----------- | --- |
vlan 1
spanning-tree
| interface | lag 1 |     |
| --------- | ----- | --- |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | lag 128  |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | lag 129  |     |
shutdown
| vlan      | access 1    |     |
| --------- | ----------- | --- |
| lacp      | mode active |     |
| interface | 1/1/1       |     |
no shutdown
| lag       | 128           |     |
| --------- | ------------- | --- |
| lacp      | port-id 65535 |     |
| interface | 1/1/2         |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/3    |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/4    |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/5    |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/6    |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/7    |     |
no shutdown
| vlan | access 1 |     |
| ---- | -------- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 131

| interface | 1/1/8 |     |
| --------- | ----- | --- |
no shutdown
| vlan access | 1     |     |
| ----------- | ----- | --- |
| interface   | 1/1/9 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/10 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/11 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/12 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/13 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/14 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/15 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | 1/1/16 |     |
no shutdown
| vlan access | 1      |     |
| ----------- | ------ | --- |
| interface   | vlan 1 |     |
ip dhcp
| snmp-server | vrf default |     |
| ----------- | ----------- | --- |
!
!
!
!
!
| https-server | vrf default |     |
| ------------ | ----------- | --- |
Showingtheconfigurationoftheckpt1checkpointinJSONformat:
| switch# show | checkpoint     | ckpt1 json |
| ------------ | -------------- | ---------- |
| Checkpoint   | configuration: |            |
{
| "AAA_Server_Group": |     | {   |
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
...
...
...
| Command History |     |     |
| --------------- | --- | --- |
Release Modification
10.07orearlier --
Configurationandfirmwaremanagement |132

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |                   | <CHECKPOINT-NAME> |           | hash    |
| --------------- | ----------------- | ----------------- | --------- | ------- |
| show checkpoint | <CHECKPOINT-NAME> |                   | hash [cli | | json] |
Description
ShowsaconfigurationcheckpointhashcalculatedwiththeSHA-256algorithm.Whentheoutputformat
isnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter         |     |     | Description                        |     |
| ----------------- | --- | --- | ---------------------------------- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesanexistingcheckpointname. |     |
| [cli | json]      |     |     | SelectseithertheCLIorJSONformat.   |     |
Examples
ShowingacheckpointSHA-256hashinJSONformat:
| switch# show | checkpoint | ckpt1           | hash json |     |
| ------------ | ---------- | --------------- | --------- | --- |
| Calculating  | the        | hash: [Success] |           |     |
The SHA-256 hash of the checkpoint in JSON format, created in image XX.10.08.xxxx:
cc7a57a9bbb4e6600d3b4180296a35f6af9e797ce9c439955dfe5de58b06da9e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,         | etc.).  |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Command History     |         |         |                   |     |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | Commandintroduced |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |                    | post-configuration |     |     |
| --------------- | ------------------ | ------------------ | --- | --- |
| show checkpoint | post-configuration |                    |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 133

Description
Showstheconfigurationsettingsforcreatingsystemcheckpoints.
Examples
| switch#    | show checkpoint    |     | post-configuration |         |     |     |
| ---------- | ------------------ | --- | ------------------ | ------- | --- | --- |
| Checkpoint | Post-Configuration |     |                    | feature |     |     |
-------------------------------------
| Status         |             |       | : enabled |              |     |     |
| -------------- | ----------- | ----- | --------- | ------------ | --- | --- |
| Timeout        | (sec)       | : 300 |           |              |     |     |
| Command        | History     |       |           |              |     |     |
| Release        |             |       |           | Modification |     |     |
| 10.07orearlier |             |       |           | --           |     |     |
| Command        | Information |       |           |              |     |     |
| Platforms      | Command     |       | context   | Authority    |     |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
show checkpoint
show checkpoint
Description
Showsadetailedlistofallsavedcheckpoints.
Examples
Showingadetailedlistofallsavedcheckpoints:
| switch# | show checkpoint |            |     |                           |            |                        |
| ------- | --------------- | ---------- | --- | ------------------------- | ---------- | ---------------------- |
| NAME    |                 | TYPE       |     | WRITER DATE(YYYY/MM/DD)   |            | IMAGE VERSION          |
| ckpt1   |                 | checkpoint |     | User 2017-02-23T00:10:02Z |            | XX.01.01.000X          |
| ckpt2   |                 | checkpoint |     | User 2017-03-08T18:10:01Z |            | XX.01.01.000X          |
| ckpt3   |                 | checkpoint |     | User 2017-03-09T23:11:02Z |            | XX.01.01.000X          |
| ckpt4   |                 | checkpoint |     | User 2017-03-11T00:00:03Z |            | XX.01.01.000X          |
| ckpt5   |                 | latest     |     | User 2017-03-14T01:12:27Z |            | XX.01.01.000X          |
| Command | History         |            |     |                           |            |                        |
| Release |                 |            |     | Modification              |            |                        |
| 10.08   |                 |            |     | Commandsyntaxshow         | checkpoint | list allisreplacedwith |
show checkpoint.
| 10.07orearlier |     |     |     | --  |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
Configurationandfirmwaremanagement |134

| Command   | Information |     |         |           |     |     |     |     |     |
| --------- | ----------- | --- | ------- | --------- | --- | --- | --- | --- | --- |
| Platforms | Command     |     | context | Authority |     |     |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show checkpoint |      |              | date |            |     |     |     |     |     |
| --------------- | ---- | ------------ | ---- | ---------- | --- | --- | --- | --- | --- |
| show checkpoint | date | <START-DATE> |      | <END-DATE> |     |     |     |     |     |
Description
Showsdetailedlistofallsavedcheckpointscreatedwithinthespecifieddaterange.
| Parameter |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
<END-DATE>
Specifiestheendingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Examples
Showingadetailedlistofsavedcheckpointsforaspecificdaterange:
switch#
|                | show        | checkpoint | date       | 2017-03-08        | 2017-03-12                   |            |               |            |         |
| -------------- | ----------- | ---------- | ---------- | ----------------- | ---------------------------- | ---------- | ------------- | ---------- | ------- |
| NAME           |             |            | TYPE       | WRITER            | DATE(YYYY/MM/DD)             |            | IMAGE         | VERSION    |         |
| ckpt2          |             |            | checkpoint | User              | 2017-03-08T18:10:01Z         |            | XX.01.01.000X |            |         |
| ckpt3          |             |            | checkpoint | User              | 2017-03-09T23:11:02Z         |            | XX.01.01.000X |            |         |
| ckpt4          |             |            | checkpoint | User              | 2017-03-11T00:00:03Z         |            | XX.01.01.000X |            |         |
| Command        | History     |            |            |                   |                              |            |               |            |         |
| Release        |             |            |            | Modification      |                              |            |               |            |         |
| 10.08          |             |            |            | Commandsyntaxshow |                              | checkpoint | list          | date       | <START- |
|                |             |            |            | DATE>             | <END-DATE>isreplacedwithshow |            |               | checkpoint | date    |
|                |             |            |            | <START-DATE>      | <END-DATE>                   |            |               |            |         |
| 10.07orearlier |             |            |            | --                |                              |            |               |            |         |
| Command        | Information |            |            |                   |                              |            |               |            |         |
| Platforms      | Command     |            | context    | Authority         |                              |            |               |            |         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show running-config |     |      | hash   |       |     |     |     |     |     |
| ------------------- | --- | ---- | ------ | ----- | --- | --- | --- | --- | --- |
| show running-config |     | hash | [cli | | json] |     |     |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 135

Description
Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutput
formatisnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description                      |
| ------------ | --- | --- | --- | -------------------------------- |
| [cli | json] |     |     |     | SelectseithertheCLIorJSONformat. |
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
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
| Parameter    |     |     |     | Description                      |
| ------------ | --- | --- | --- | -------------------------------- |
| [cli | json] |     |     |     | SelectseithertheCLIorJSONformat. |
Examples
Configurationandfirmwaremanagement |136

Showingthestartup-configcheckpointSHA-256hashinCLIformat:
| switch# show | startup-config |           | hash cli       |
| ------------ | -------------- | --------- | -------------- |
| Calculating  | the hash:      | [Success] |                |
| SHA-256 hash | of the         | config    | in CLI format: |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,         | etc.).  |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Command History     |         |         |                   |
| Release             |         |         | Modification      |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 137

Boot commands

boot set-default
boot set-default {primary | secondary}

Description

Sets the default operating system image to use when the system is booted.

Parameter

primary

secondary

Example

Description

Selects the primary network operating system image.

Selects the secondary network operating system image.

Selecting the primary image as the default boot image:

switch# boot set-default primary
Default boot image set to primary.

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

boot system
boot system [primary | secondary | serviceos]

Description

Reboots all modules on the switch. By default, the configured default operating system image is used.
Optional parameters enable you to specify which system image to use for the reboot operation and for
future reboot operations.

Parameter

primary

Description

Selects the primary operating system image for this reboot and
sets the configured default operating system image to primary
for future reboots.

Configuration and firmware management | 138

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
secondary Selectsthesecondaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetosecondary
forfuturereboots.
serviceos
Selectstheserviceoperatingsystemforthisreboot.Doesnot
changetheconfigureddefaultoperatingsystemimage.The
serviceoperatingsystemactsasastandalonebootloaderand
recoveryOSforswitchesrunningtheAOS-CXoperatingsystem
andisusedinrarecaseswhentroubleshootingaswitch.
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
| The system | is going   | down for reboot. |            |                |
Rebootingthesystemfromthesecondaryoperatingsystemimage,settingthesecondaryoperating
systemimageastheconfigureddefaultbootimage:
switch#
|         | boot system | secondary         |     |     |
| ------- | ----------- | ----------------- | --- | --- |
| Default | boot image  | set to secondary. |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 139

| Do you     | want to save | the current      | configuration | (y/n)? n       |
| ---------- | ------------ | ---------------- | ------------- | -------------- |
| This will  | reboot the   | entire switch    | and render    | it unavailable |
| until the  | process      | is complete.     |               |                |
| Continue   | (y/n)? y     |                  |               |                |
| The system | is going     | down for reboot. |               |                |
Cancelingasystemreboot:
| switch#   | boot system  |               |               |                |
| --------- | ------------ | ------------- | ------------- | -------------- |
| Do you    | want to save | the current   | configuration | (y/n)? n       |
| This will | reboot the   | entire switch | and render    | it unavailable |
| until the | process      | is complete.  |               |                |
| Continue  | (y/n)? n     |               |               |                |
| Reboot    | aborted.     |               |               |                |
switch#
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show boot-history |           |        |          |     |
| ----------------- | --------- | ------ | -------- | --- |
| show boot-history | [all|{vsf | member | <1-10>}] |     |
Description
Showsboothistoryinformation.Whennoparametersarespecified,showsthemostrecentinformation
aboutthecurrentbootoperation,andthethreepreviousbootoperationsfortheswitch.Whentheall
parameterisspecified,theoutputofthiscommandshowsthebootinformationfortheactive
managementmodule.
.
Toviewboot-historyonastandby,thecommandmustbesentontheconductorconsole.
| Parameter |     |     | Description                                         |     |
| --------- | --- | --- | --------------------------------------------------- | --- |
| all       |     |     | Optional.Showsbootinformationfortheactivemanagement |     |
module.
vsf member <1-10> Optional.DisplayboothistoryforthespecifiedVSFmember
Configurationandfirmwaremanagement |140

Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Theoutputofthiscommandincludesthefollowinginformation:
Parameter Description
Index Thepositionofthebootinthehistoryfile.Range:0
to3.
Boot ID AuniqueIDfortheboot.Asystem-generated128-
bitstring.
Current Boot, up for <time> Forthecurrentboot,theshowboot-history
commandshowsthenumberofsecondsthe
modulehasbeenrunningonthecurrentsoftware.
<Timestamp>: boot reason Forpreviousbootoperations,theshowboot-
historycommandshowsthetimeatwhichthe
operationoccurredandthereasonfortheboot.
Thereasonforthebootisoneofthefollowing
values:
n <DAEMON-NAME>crash:Thedaemonidentified
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
| switch#    | show boot-history |     |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index : | 2                                  |           |                     |
| ------- | ---------------------------------- | --------- | ------------------- |
| Boot ID | : c34a2c2499004a02bbeeff4992e1fdbd |           |                     |
| Current | Boot, up for                       | 1 days 13 | hrs 13 mins 27 secs |
| Index : | 1                                  |           |                     |
| Boot ID | : bfba9bc486304e57904ac717a0ccbdcd |           |                     |
02 Sep 23 02:55:33 : CPU request reset with 0x20201, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:55:33                        | : Switch boot | count is 2 |
| ------- | ---------------------------------- | ------------- | ---------- |
| Index : | 0                                  |               |            |
| Boot ID | : a88a71b7ca9a4574af7e3b811ddfdc7e |               |            |
02 Sep 23 02:49:26 : Reboot requested by user, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 141

| 02 Sep  | 23 02:50:02                        | : Switch boot | count is 1 |
| ------- | ---------------------------------- | ------------- | ---------- |
| Index : | 3                                  |               |            |
| Boot ID | : f00ba10c8c44457f83fee303d014a89a |               |            |
25 Aug 23 10:27:42 : Power on reset with 0x1, Version: FL.10.14.0000-1465-
g9df95249d06b0~dirty
| 25 Aug | 23 10:28:18 | : Switch | boot count is 3 |
| ------ | ----------- | -------- | --------------- |
25 Aug 23 10:29:02 : Primary overtemperature fault detected with 0x2 in PSU 1/1
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| Firmware      | management   |              | commands         |
| ------------- | ------------ | ------------ | ---------------- |
| copy {primary | |            | secondary}   | <REMOTE-URL>     |
| copy {primary | | secondary} | <REMOTE-URL> | [vrf <VRF-NAME>] |
Description
UploadsafirmwareimagetoaTFTPorSFTPserver.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{primary | secondary} Selectstheprimaryorsecondaryimageprofiletoupload.
Required
<REMOTE-URL>
SpecifiestheURLtoreceivetheuploadedfirmwareusingSFTP,
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
Configurationandfirmwaremanagement |142

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
switch#
|         | copy primary | usb:/11.10.00.0002.swi |     |     |     |
| ------- | ------------ | ---------------------- | --- | --- | --- |
| Command | History      |                        |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 143

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
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
| Command        | Information  |                    |              |
| Platforms      | Command      | context            | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <REMOTE-URL>
copy <REMOTE-URL> {hot-patch|primary|secondary} [vrf <VRF-NAME>]
Description
Downloadsahot-patchorfirmwareimagefromaTFTPorSFTPserver.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<REMOTE-URL> SpecifiestheURLfromwhichtodownloadthefirmwareusing
SFTPorTFTP.
TFTPformat:
Configurationandfirmwaremanagement |144

Parameter

Description

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

n A URL with an IPv4 address: sftp://user@192.0.2.1/a.txt

n A URL with an IPv6 address: sftp://user@[2000::2]/a.txt

n A URL with a hostname: sftp://user@hpe.com/a.txt

n SFTP port number of a server in the URL: sftp://user@192.0.2.1:12/a.txt

n A file in a directory of URL: sftp://user@192.0.2.1/dir/a.txt

n To specify a file with absolute path in the URL: sftp://user@192.0.2.1//home/user/a.txt

SCP Usage

To specify:

n A username with an IP address: scp://user@192.0.2.1:12/a.txt

n A username with a remote host: scp://user@hpe.com/a.txt

Examples

TFTP download for a hot-patch:

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

145

switch# copy tftp://192.168.1.1/FL.10.12.0001-0002.patch hot-patch vrf vrf1
Fetching /users/swuser/FL.10.10.0001-0002.patch to hotpatch.dnld.uE2YT1
| FL.10.12.0001-0002.patch |             |              |     | 100% | 62KB | 12.4MB/s | 00:00 |     |
| ------------------------ | ----------- | ------------ | --- | ---- | ---- | -------- | ----- | --- |
| Verifying                | and writing | hot-patch... |     |      |      |          |       |     |
TFTPdownloadforprimarysoftwareimage:
| switch#     | copy tftp://192.10.12.0/FL_10_12_0001.swi |             |     |     | primary |     |     |     |
| ----------- | ----------------------------------------- | ----------- | --- | --- | ------- | --- | --- | --- |
| The primary | image will                                | be deleted. |     |     |         |     |     |     |
| Continue    | (y/n)?                                    |             |     |     |         |     |     |     |
y
######################################################################### 100.0%
| Verifying | and writing | system firmware... |     |     |     |     |     |     |
| --------- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- |
SFTPdownload:
switch# copy sftp://swuser@192.10.12.0/FL_10_12_0001.swi primary
| The primary | image will | be deleted. |     |     |     |     |     |     |
| ----------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
| Continue    | (y/n)? y   |             |     |     |     |     |     |     |
The authenticity of host '192.10.12.0 (192.10.12.0)' can't be established.
ECDSA key fingerprint is SHA256:L64khLwlyLgXlARKRMiwcAAK8oRaQ8C0oWP+PkGBXHY.
| Are you | sure you want | to continue | connecting | (yes/no)? |     | yes |     |     |
| ------- | ------------- | ----------- | ---------- | --------- | --- | --- | --- | --- |
Warning: Permanently added '192.10.12.0' (ECDSA) to the list of known hosts.
| swuser@192.10.12.0's |                 | password: |     |     |     |     |     |     |
| -------------------- | --------------- | --------- | --- | --- | --- | --- | --- | --- |
| Connected            | to 192.10.12.0. |           |     |     |     |     |     |     |
Fetching /users/swuser/ss.10.00.0002.swi to ss.10.00.0002.swi.dnld
| /users/swuser/ss.10.00.0002.swi |             |                    |                                                 |     | 100% | 179MB 25.6MB/s |     | 00:07 |
| ------------------------------- | ----------- | ------------------ | ----------------------------------------------- | --- | ---- | -------------- | --- | ----- |
| Verifying                       | and writing | system firmware... |                                                 |     |      |                |     |       |
| Command                         | History     |                    |                                                 |     |      |                |     |       |
| Release                         |             |                    | Modification                                    |     |      |                |     |       |
| 10.12                           |             |                    | Thehot-patchparameterissupportedonallplatforms. |     |      |                |     |       |
| 10.07orearlier                  |             |                    | --                                              |     |      |                |     |       |
| Command                         | Information |                    |                                                 |     |      |                |     |       |
| Platforms                       | Command     | context            | Authority                                       |     |      |                |     |       |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| copy secondary | primary |     |     |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| copy secondary | primary |     |     |     |     |     |     |     |
Description
Copiesthefirmwareimagefromthesecondarytotheprimarylocation.
Examples
Configurationandfirmwaremanagement |146

| switch#     | copy secondary | primary     |             |     |     |     |     |
| ----------- | -------------- | ----------- | ----------- | --- | --- | --- | --- |
| The primary | image will     | be deleted. |             |     |     |     |     |
| Continue    | (y/n)? y       |             |             |     |     |     |     |
| Verifying   | and writing    | system      | firmware... |     |     |     |     |
switch# copy sftp://stor@192.22.1.0/im-switch.swi primary vrf default
| The primary | image will | be deleted. |     |     |     |     |     |
| ----------- | ---------- | ----------- | --- | --- | --- | --- | --- |
| Continue    | (y/n)? y   |             |     |     |     |     |     |
The authenticity of host '192.22.1.0 (192.22.1.0)' can't be established.
ECDSA key fingerprint is SHA256:MyI1xbdKnehYut0NLfL69gDpNzCmZqBVvBaRR46m7o8.
| Are you | sure you want | to continue | connecting |     | (yes/no)? | yes |     |
| ------- | ------------- | ----------- | ---------- | --- | --------- | --- | --- |
Warning: Permanently added '192.22.1.0' (ECDSA) to the list of known hosts.
| stor@192.22.1.0's      | password:              |         |                           |                           |                |     |       |
| ---------------------- | ---------------------- | ------- | ------------------------- | ------------------------- | -------------- | --- | ----- |
| Connected              | to 192.22.1.0.         |         |                           |                           |                |     |       |
| sftp> get              | c8d5b9f-topflite.swi   |         | c8d5b9f-topflite.swi.dnld |                           |                |     |       |
| Fetching               | /home/dr/im-switch.swi |         | to                        | c8d5b9f-topflite.swi.dnld |                |     |       |
| /home/dr/im-switch.swi |                        |         |                           | 100%                      | 226MB 56.6MB/s |     | 00:04 |
| Verifying              | and writing            | system  | firmware...               |                           |                |     |       |
| Command                | History                |         |                           |                           |                |     |       |
| Release                |                        |         | Modification              |                           |                |     |       |
| 10.07orearlier         |                        |         | --                        |                           |                |     |       |
| Command                | Information            |         |                           |                           |                |     |       |
| Platforms              | Command                | context | Authority                 |                           |                |     |       |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy <STORAGE-URL>
| copy <STORAGE-URL> | {hot-patch|primary|secondary} |     |     |     |     |     |     |
| ------------------ | ----------------------------- | --- | --- | --- | --- | --- | --- |
Description
Copies,verifies,andinstallsahot-patchorfirmwareimagefromaUSBstoragedeviceconnectedtothe
activemanagementmodule.
| Parameter |     |     | Description |     |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- | --- |
<STORAGE-URL>
Specifiesthenameofthefirmwarefiletocopyfromthestorage
device.Required.
USBformat:
usb:/<FILENAME>
{hot-patch|primary|secondary}
Selectahot-patchimageoraprimaryorsecondaryprofilefor
receivingthecopiedfirmware.
NOTE:Formoreinformationabouthot-patch,seehot-patch.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 147

USB usage
Tospecifyafile:
n InaUSBstoragedevice:usb:/a.txt
n InadirectoryofaUSBstoragedevice:usb:/dir/a.txt
Examples
| switch#        | copy usb:/FL.10.12.0001-0002.patch |                    |                                                 |
| -------------- | ---------------------------------- | ------------------ | ----------------------------------------------- |
| switch#        | copy usb:/FL.10.12.0001.swi        |                    | primary                                         |
| The primary    | image will                         | be deleted.        |                                                 |
| Continue       | (y/n)? y                           |                    |                                                 |
| Verifying      | and writing                        | system firmware... |                                                 |
| Command        | History                            |                    |                                                 |
| Release        |                                    |                    | Modification                                    |
| 10.12          |                                    |                    | Thehot-patchparameterissupportedonallplatforms. |
| 10.07orearlier |                                    |                    | --                                              |
| Command        | Information                        |                    |                                                 |
| Platforms      | Command                            | context            | Authority                                       |
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
Configurationandfirmwaremanagement |148

Examples
switch# copy hot-patch FL_10_12_0001-0002.patch tftp:172.21.18.170/FL_10_12_0001-
| 0002.patch | vrf vrf1 |     |             |
| ---------- | -------- | --- | ----------- |
| Related    | Commands |     |             |
| Command    |          |     | Description |
Downloadsahot-patchimagefromaTFTPorSFTPserver.
copy <REMOTE-URL>
| hot-patch |             |         | Applyahot-patchimageorremoveitfromtheswitch. |
| --------- | ----------- | ------- | -------------------------------------------- |
| Command   | History     |         |                                              |
| Release   |             |         | Modification                                 |
| 10.12     |             |         | Hot-patchisnowsupportedonallplatforms.       |
| 10.10     |             |         | Commandintroduced                            |
| Command   | Information |         |                                              |
| Platforms | Command     | context | Authority                                    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
hot-patch
| hot-patch    | apply|remove       | <name.patch> |     |
| ------------ | ------------------ | ------------ | --- |
| no hot-patch | apply <name.patch> |              |     |
Description
Applyhot-patchsoftwareorremoveitfromtheswitch.Thenoformofthehot-patch applycommand
disablesthehot-patchimage,butdoesnotremoveitfromtheswitch.Rebootingthesystemafter
disablingorremovingthepatchisnotrequired.
| Profile | names |     | Description |
| ------- | ----- | --- | ----------- |
apply <name.patch> Applythespecifiedhot-patchimagetoastandaloneswitchorVSF
stack.AOS-CXhot-patchsoftwareimagescanbeobtainedfrom
HPE ArubaNetworkingcustomersupport,andareidentifiedwith
a.patchextension.
remove <name.patch> Disablesthehot-patchimageandremovesthepatchfromthe
switch.Thisremovalwillalsodisablethepatch.Onceremoved,a
hot-patchmustbedownloadedagaininordertobeapplied.
Usage
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 149

Ahot-patchcanbedownloadedfromaremoteserverontoaswitchthenappliedwithoutrebootingthe
switch.Whenthehot-patchisdisabled,thehot-patchwillstillremainonthesystem.Thedisabledhot-
patchcanberemovedfromthesystemwithouttheneedforarebootofthesystem.
Ifacheckpointconfigurationthatdoesnotcontainahot-patchisrestoredtoarunningconfiguration
thatdoeshaveahot-patch,thepatchisnotdeleted,itremainsasnotappliedbutispresentinthe
devicememory.
Examples
| switch(config)# | hot-patch | apply | FL_10_12_0001-0002.patch |
| --------------- | --------- | ----- | ------------------------ |
Related Commands
| Command |     |     | Description |
| ------- | --- | --- | ----------- |
copy <REMOTE-URL> Downloadsandinstallsahot-patchimagefromaTFTPorSFTP
server.
copy hot-patch Copiesahot-patchsoftwareimagefromaswitchtoaspecified
remoteURL orstorageURL.
| Command History     |         |         |                                        |
| ------------------- | ------- | ------- | -------------------------------------- |
| Release             |         |         | Modification                           |
| 10.12               |         |         | Hot-patchisnowsupportedonallplatforms. |
| 10.10               |         |         | Commandintroduced.                     |
| Command Information |         |         |                                        |
| Platforms           | Command | context | Authority                              |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
Configurationandfirmwaremanagement |150

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
copy <REMOTE-URL> Downloadsahot-patchimagefromaTFTPorSFTPserver.
| hot-patch |             |         | Applyahot-patchimageorremoveitfromtheswitch. |
| --------- | ----------- | ------- | -------------------------------------------- |
| Command   | History     |         |                                              |
| Release   |             |         | Modification                                 |
| 10.12     |             |         | Commandsupportedonallplatforms.              |
| 10.10     |             |         | Commandintroducedon6300Switchseries.         |
| Command   | Information |         |                                              |
| Platforms | Command     | context | Authority                                    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 151

Chapter 9

Dynamic Segmentation

Dynamic Segmentation

For information on dynamic segmentation, view the Security Guide.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

152

Chapter 10

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing and modifying information
about managed devices on IP networks.

Configuring SNMP

(The SNMP agent provides read-only access.)

Procedure

1. Enable SNMP on a VRF using the command snmp-server vrf default.

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

n Sets the contact, location, and description for the switch to: JaniceM, Building2, LabSwitch.

n Sets the community string to Lab8899X.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

153

| switch(config)# | snmp-server | vrf default |     |     |
| --------------- | ----------- | ----------- | --- | --- |
switch(config)#
|                 | snmp-server | system-contact     | JaniceM  |           |
| --------------- | ----------- | ------------------ | -------- | --------- |
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
SNMP|154

Chapter 11

HPE Aruba Networking Central

HPE Aruba Networking Central integration

The HPE Aruba Networking Central network management solution, a software-as-a-service subscription
in the cloud, provides streamlined management of multiple network devices. AOS-CX switches are able
to talk to HPE Aruba Networking Central and utilize cloud-based management functionality. Cloud-based
management functionality allows for the deployment of network devices at sites with no or few
dedicated IT personnel (branch offices, retail stores, and so forth). AOS-CX switches utilize secure
communication protocols to connect to the HPE Aruba Networking Central cloud portal, and can coexist
with corporate security standards, such as those mandating the use of firewalls.

When HPE Aruba Networking Central manages AOS-CX switches, it functions as the single source of truth and the

Web UI operates in read-only mode.

This feature provides:

n Zero-touch provisioning

n Network Management/Remote monitoring

n Events/alerts notification

n Switch Configuration using templates

n Firmware management

Connecting to HPE Aruba NetworkingCentral

AOS-CX switch downloads the location of HPE Aruba Networking Central server using:

n Command-line interface (CLI).

n HPE GreenLake server.

n DHCP options provided during ZTP.

DHCP servers are used to connect to Central on-premise management.

When a switch is able to connect to HPE Aruba Networking Central, but is not registered in the HPE Aruba

Networking Central inventory or does not have a proper license, the switch will get disconnected. If the HPE Aruba

Networking Central feature is enabled using this command, the switch will then reconnect back to HPE Aruba

Networking Central and will get disconnected again. This connect/disconnect process will continue until the

switch is properly registered in HPE Aruba Networking Central. To avoid this unnecessary reconnection cycle, best

practices is to disable HPE Aruba Networking Central until the switch is registered in HPE Aruba Networking

Central, or a license is obtained for that device.

Custom CA certificate

To use a custom CA certificate to connect to HPE Aruba Networking Central, AOS-CX switch downloads
the certificate from the HPE GreenLake server.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

155

n If there is no custom CA provided by HPE GreenLake, the CA certificate present in the device is used.

n Duplicate CA certificates from HPE GreenLake server will be ignored.

n If CA certificate is absent in consecutive responses from the HPE GreenLake server, the installed custom CA

certificate in device will be removed.

n Switch will have only one custom CA certificate installed from the HPE GreenLake Server.

n The certificate installed from the HPE GreenLake server will not be displayed in the show commands.

Support mode in HPE Aruba Networking Central

When the AOS-CX switch is managed by HPE Aruba Networking Central, the switch configuration cannot
be modified using other interfaces such as CLI or Web UI. The following command categories are
blocked:

n auto-confirm

n boot

n checkpoint

n copy-in commands

n erase

n https-server

n mfgread

n mfgwrite

n port-access

n All configuration commands except the aruba-central command

In cases where a maintenance or troubleshooting activity requires configuration updates, aruba-central
support-mode can be enabled to allow these operations.

The aruba-central support-mode enable or disable operation is effective only in the CLI session where it is

executed and does not impact the other CLI sessions.

If the user tries to execute any command that is not allowed, an Invalid input: error message is
displayed.

One Touch Provisioning

One Touch Provisioning (OTP) allows a switch to be provisioned on HPE Aruba Networking Central with
the minimum user configuration.

Configuring One Touch Provisioning

To provision a switch to HPE Aruba Networking Central by using an OTP scenario, you can configure:

n The HPE Aruba Networking Central Location

Following configurations can be done optionally:

HPE Aruba Networking Central integration | 156

n TheDomainNameSystem(DNS)serveraddress.
n TheHTTPproxylocation.
| Configuring | HPE Aruba | Networking | Central location |     |     |
| ----------- | --------- | ---------- | ---------------- | --- | --- |
1. Createthehpe-anw-centralcontext.
|     | switch(config)# | hpe-anw-central |     |     |     |
| --- | --------------- | --------------- | --- | --- | --- |
2. ConfiguretheHPE ArubaNetworkingCentralserverlocation
switch(hpe-anw-central)# location-override <LOCATION> vrf <VRF>
IPv4orIPv6addresscanbeused.
3. ValidatetheconnectivitystatustoHPE ArubaNetworkingCentral
|             | switch# show | hpe-anw-central |     |     |     |
| ----------- | ------------ | --------------- | --- | --- | --- |
| Configuring | DNS server   | address         |     |     |     |
1. ConfiguretheDNSserveraddress.
|     | switch(config)# | ip dns           | server-address | <ADDRESS> | vrf <VRF> |
| --- | --------------- | ---------------- | -------------- | --------- | --------- |
|     | IPv4orIPv6a     | ddresscanbeused. |                |           |           |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 157

n SupportforobtaningtheHPE ArubaNetworkingCentrallocationviaDHCP.
n SupportforconnectivitytoanHPE ArubaNetworkingCentralon-premiseinstance.
Supportability
Debugloggingcanbeenabledwiththefollowingcommand:
ThecentraldebuglogsarehelpfultodetermineconnectivityissueswithHPE ArubaNetworkingCentral.
| switch# debug | central    | all |         |          |
| ------------- | ---------- | --- | ------- | -------- |
| HPE Aruba     | Networking |     | Central | commands |
hpe-anw-central
AppliesonlytotheHPE ArubaNetworking4100iswitch.
hpe-anw-central
no hpe-anw-central
Description
CreatesorenterstheHPE ArubaNetworkingCentralconfigurationcontext(config-hpe-anw-central).
Example
CreatingtheHPE ArubaNetworkingCentralconfigurationcontext:
| switch(config)# | hpe-anw-central |     |     |     |
| --------------- | --------------- | --- | --- | --- |
switch(config-hpe-anw-central)#
| Command History |     |     |                                                 |     |
| --------------- | --- | --- | ----------------------------------------------- | --- |
| Release         |     |     | Modification                                    |     |
| 10.15           |     |     | Commandsyntaxchangedfromaruba-centraltohpe-anw- |     |
central.
| 10.08               |         |         | Commandintroduced |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
4100i config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| hpe-anw-central |     | support-mode |     |     |
| --------------- | --- | ------------ | --- | --- |
AppliesonlytotheHPE ArubaNetworking4100iswitch.
HPE ArubaNetworkingCentralintegration|158

| hpe-anw-central    | support-mode |     |     |
| ------------------ | ------------ | --- | --- |
| no hpe-anw-central | support-mode |     |     |
Description
Allowsthedevicetobewritableforalloperationsin HPE ArubaNetworkingCentrallockoutmodefor
troubleshooting.Thenoformofthiscommanddisablesthisactivity.
Support-modeisdisabledbydefaultwhentheswitchismanagedbyHPE ArubaNetworkingCentral.This
commandisonlyeffectiveintheCLI sessionwhereitisexecuted.
Examples
ConfiguringthedevicetobewritableforalloperationsinHPE ArubaNetworkingCentrallockoutmode:
| switch# | hpe-anw-central | support-mode |     |
| ------- | --------------- | ------------ | --- |
RemovingtheconfigurationthatallowsthedevicetobewritableforalloperationsinHPE Aruba
NetworkingCentrallockoutmode:
| switch# | no hpe-anw-central | support-mode |     |
| ------- | ------------------ | ------------ | --- |
switch#
| Command | History |     |              |
| ------- | ------- | --- | ------------ |
| Release |         |     | Modification |
10.15
Commandsyntaxchangedfromaruba-centraltohpe-anw-
central.
| 10.08     |             |         | Commandintroduced |
| --------- | ----------- | ------- | ----------------- |
| Command   | Information |         |                   |
| Platforms | Command     | context | Authority         |
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| configuration-lockout |     | central | managed |
| --------------------- | --- | ------- | ------- |
AppliesonlytotheHPE ArubaNetworking4100iswitch.
| configuration-lockout    |     | central managed |     |
| ------------------------ | --- | --------------- | --- |
| no configuration-lockout |     | central managed |     |
Description
ConfiguresthedevicetoonlybewritablefromHPE ArubaNetworkingCentral.HPE ArubaNetworking
Centralwillbetheonlyagentthatcanadd,modify,ordeleteconfigurationsonthedevice.Thenoform
ofthiscommanddisablesthisfeature.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 159

ThenoformofthiscommandisonlyavailablewhenthedeviceisdisconnectedfromHPE ArubaNetworking
Central.
Usage
TheAOS-CXswitchconnectstoHPE ArubaNetworkingCentralineitheroftwomodes:monitoror
managed.Whenthedeviceisconnectedinmonitormode,HPE ArubaNetworkingCentralmonitorsthe
configurationsontheswitch.Whenthedeviceisconnectedinmanagedmode,theconfiguration-
lockout central managedcommanddoesnotallowconfigurationchangesfromotherinterfacessuch
asCLIorWebUI.
Examples
ConfiguringthedevicetoonlybewritablefromHPE ArubaNetworkingCentral:
| switch(config)# |                       | configuration-lockout |     | central managed |
| --------------- | --------------------- | --------------------- | --- | --------------- |
| switch# show    | configuration-lockout |                       |     |                 |
| configuration   | lockout               |                       |     |                 |
---------------------
| central:            | managed         |        |        |                |
| ------------------- | --------------- | ------ | ------ | -------------- |
| switch# sh          | hpe-anw-central |        |        |                |
| Central admin       | state           |        |        | :enable        |
| Central location    |                 |        |        | :20.0.0.2:8083 |
| VRF for connection  |                 |        |        | :default       |
| Central connection  |                 | status |        | :connected     |
| Central source      |                 |        |        | :cli           |
| Central source      | connection      |        | status | :connected     |
Central source last connected on :Tue Feb 9 17:53:13 UTC 2021
| Activate     | Server | URL |     | :devices-v2.arubanetworks.com |
| ------------ | ------ | --- | --- | ----------------------------- |
| CLI location |        |     |     | :20.0.2:8083                  |
| CLI VRF      |        |     |     | :default                      |
switch(config)#
end
| Command History     |         |         |     |                   |
| ------------------- | ------- | ------- | --- | ----------------- |
| Release             |         |         |     | Modification      |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
4100i config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| diag-dump      | rest  | basic |     |     |
| -------------- | ----- | ----- | --- | --- |
| diag-dump rest | basic |       |     |     |
Description
DisplayRESTpathsanddiagnosticsinformationfortheRESTfeature.Theoutputofthiscommand
includesdiagnosticsinformationforHPE ArubaNetworkingCentral.
HPE ArubaNetworkingCentralintegration|160

Example
ThefollowingexampledisplaysjusttheCentral Countersportionoftheoutputforthiscommand.
switch#
| diag-dump |     | rest | basic |     |     |
| --------- | --- | ---- | ----- | --- | --- |
=========================================================================
| [Start] Feature |     | rest | Time : Sun | Sep 17 17:06:50 | 2023 |
| --------------- | --- | ---- | ---------- | --------------- | ---- |
=========================================================================
...
...
...
| Central Counters: |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
---------------------------------------
| Logins:         |     |     |     | 1   |     |
| --------------- | --- | --- | --- | --- | --- |
| Connections:    |     |     |     | 1   |     |
| Disconnections: |     |     |     | 0   |     |
---------------------------------------
| Pings: |     |     |     | 50  |     |
| ------ | --- | --- | --- | --- | --- |
| Pongs: |     |     |     | 50  |     |
---------------------------------------
| API Requests: |               |     |     | 20  |     |
| ------------- | ------------- | --- | --- | --- | --- |
| Response      | API Requests: |     |     | 20  |     |
---------------------------------------
| v1 Notification    |     | Requests | Received: | 5   |     |
| ------------------ | --- | -------- | --------- | --- | --- |
| v1 Notifications   |     | Sent:    |           | 15  |     |
| Initial Snapshots: |     |          |           | 5   |     |
| Notifications:     |     |          |           | 10  |     |
| Errors:            |     |          |           | 0   |     |
---------------------------------------
| v2 Notification    |     | Requests | Received: | 10  |     |
| ------------------ | --- | -------- | --------- | --- | --- |
| v2 Notifications   |     | Sent:    |           | 24  |     |
| Initial Snapshots: |     |          |           | 10  |     |
| Unsubscribes:      |     |          |           | 0   |     |
| Notifications:     |     |          |           | 14  |     |
| Errors:            |     |          |           | 0   |     |
---------------------------------------
| Views Notification |            |     | Requests:  | 0   |     |
| ------------------ | ---------- | --- | ---------- | --- | --- |
| Views Notification |            |     | Responses: | 0   |     |
| Views Unary        | Requests:  |     |            | 0   |     |
| Views Unary        | Responses: |     |            | 0   |     |
---------------------------------------
| Packet Capture |     | Responses: |     | 0   |     |
| -------------- | --- | ---------- | --- | --- | --- |
---------------------------------------
| Command History     |         |     |         |              |     |
| ------------------- | ------- | --- | ------- | ------------ | --- |
| Release             |         |     |         | Modification |     |
| 10.07orearlier      |         |     |         | --           |     |
| Command Information |         |     |         |              |     |
| Platforms           | Command |     | context | Authority    |     |
allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
disable
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 161

AppliesonlytotheHPE ArubaNetworking4100iswitch.
disable
Description
DisablesconnectiontoHPE ArubaNetworkingCentralserver.
Whentheconnectionisdisabled,theswitchdoesnotattempttoconnecttotheHPE ArubaNetworking
Centralserverorfetchcentrallocationfromanyofthethreesources(CLI/HPEGreenLake/DHCP).Italso
disconnectsanyactiveconnectiontotheHPE ArubaNetworkingCentralserver.
Example
| switch(config-hpe-anw-central)# |     | disable |     |
| ------------------------------- | --- | ------- | --- |
switch(config-hpe-anw-central)#
| Command   | History     |                   |           |
| --------- | ----------- | ----------------- | --------- |
| Release   |             | Modification      |           |
| 10.08     |             | Commandintroduced |           |
| Command   | Information |                   |           |
| Platforms | Command     | context           | Authority |
4100i config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| enable | (HPE Aruba | Networking | Central) |
| ------ | ---------- | ---------- | -------- |
enable
Description
EnablesconnectiontoHPE ArubaNetworkingCentralserver.Whentheconnectionisenabled,the
switchattemptstodownloadthelocationoftheHPE ArubaNetworkingCentralserverinoneofthe
followingwaysatstartupandaftertheconnectionislost:
n Usingcommand-lineinterface(CLI).
n ConnectingtotheHPEGreenLakeserver.
n UsingDHCPoptionsprovidedduringZTP.
DHCPserversprovidetheoptionsrequestedbythedevicetoconnecttoCentral,CentralOn-premise
managment,ortheTFTPserver.
HPE ArubaNetworkingCentralintegration|162

WhenaswitchisabletoconnecttoHPE ArubaNetworkingCentral,butisnotregisteredintheHPE Aruba
NetworkingCentralinventoryordoesnothaveaproperlicense,theswitchwillgetdisconnected.Ifthe
HPE ArubaNetworkingCentralfeatureisenabledusingthiscommand,theswitchwillthenreconnectbackto
HPE ArubaNetworkingCentralandwillgetdisconnectedagain.Thisconnect/disconnectprocesswillcontinue
untiltheswitchisproperlyregisteredinHPE ArubaNetworkingCentral.Toavoidthisunnecessaryreconnection
cycle,bestpracticesistodisableHPE ArubaNetworkingCentraluntiltheswitchisregisteredinHPE Aruba
NetworkingCentral,oralicenseisobtainedforthatdevice.
Examples
| switch(config-hpe-anw-central)# |     | enable |     |
| ------------------------------- | --- | ------ | --- |
switch(config-hpe-anw-central)#
| Command History     |         |                   |           |
| ------------------- | ------- | ----------------- | --------- |
| Release             |         | Modification      |           |
| 10.08               |         | Commandintroduced |           |
| Command Information |         |                   |           |
| Platforms           | Command | context           | Authority |
4100i config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
location-override
AppliesonlytotheHPE ArubaNetworking4100iswitch.
| location-override | <location> | [vrf <VRF>] |     |
| ----------------- | ---------- | ----------- | --- |
no location-override
Description
Whenlocationandvrfareconfigured,theswitchoverridesexistingconnectionstoHPE Aruba
NetworkingCentral.TheswitchattemptstoestablishconnectiontoHPE ArubaNetworkingCentralwith
thespecifiedlocationandVRFwithhighestpriority.
Locationcantakeoneofthefollowingvalues:
n Afullyqualifieddomainname(FQDN)alongwithanoptionalportnumber.
n AnIPv4addresswithanoptionalportnumber.
n AnIPv6addresswithanoptionalportnumber.
Iftheportnumberisnotspecified,thenport443isusedbydefault.Ifthecommandisexecutedwithout
theVRFparameter,theswitchuses
the'default'VRF.
ThenoformofthiscommandremoveslocationoverridevaluesfromtheHPE ArubaNetworkingCentral
configurationcontext.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 163

When you configure an IPv6 address with a port number, specify the address part inside square brackets,

optionally followed by the port number, e.g. [2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443.

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

switch(config-hpe-anw-central)# location-override hpe-anw-central.com vrf default
switch(config-hpe-anw-central)#
switch(config-hpe-anw-central)# location-override hpe-anw-central.com vrf red
switch(config-hpe-anw-central)# location-override 10.0.0.1 vrf red
switch(config-hpe-anw-central)# location-override 10.0.0.1:443 vrf red
switch(config-hpe-anw-central)# location-override
2001:0db8:85a3:0000:0000:8a2e:0370:7334 vrf red
switch(config-hpe-anw-central)# location-override
[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443 vrf red

Configuring location override with location only:

switch(config-hpe-anw-central)# location-override hpe-anw-central.com
switch(config-hpe-anw-central)#

Removing location override values from the HPE Aruba Networking Central configuration context:

switch(config-hpe-anw-central)# no location-override
switch(config-hpe-anw-central)#

Command History

Release

10.13.1000

10.08

Command Information

Modification

Command updated to reflect a OTP scenario..

Command introduced

HPE Aruba Networking Central integration | 164

Platforms

Command context

Authority

All platforms

config-hpe_anw-central

Administrators or local user group members with execution
rights for this command.

location-override-alternative

Applies only to the HPE Aruba Networking 4100i switch.

location-override-alternative <LOCATION> [vrf <VRF>]
no location-override-alternative <LOCATION> [vrf <VRF>]

Description

Configures information about HPE Aruba Networking Central connection when the alternative location
is used.

The no form of this command removes the location-override-alternative configuration.

Parameter

<LOCATION>

vrf <VRF>

Usage

Description

Specifies the HPE Aruba Networking Central location.

Specifies the VRF used to connect to HPE Aruba Networking
Central.

When the main and alternative HPE Aruba Networking Central server locations are specified, the switch
attempts to connect to the main HPE Aruba Networking Central server. If there is connectivity failure
with the main HPE Aruba Networking Central server location, it attempts to establish a connection with
the alternative server location.

If the alternative location is configured without a main location, the user is prompted for confirmation.
In this case, there is no redundancy and the switch attempts to connect to the alternative location.

Location can take one of the following values:

n A fully qualified domain name (FQDN) along with an optional port number.

n An IPv4 address with an optional port number.

n An IPv6 address with an optional port number.

If the port number is not specified, then port 443 is used by default. If the command is executed without
the VRF parameter, the switch uses

the 'default' VRF.

An HPE Aruba Networking Central server location can only be a fully qualified domain name (FQDN) or a
valid IP address. If the command is entered without the VRF parameter, the switch uses the default VRF.

Examples

Example of configuring with the hpe-anw-central.com location and VRF red:

switch(config-hpe-anw-central)# location-override-alternative hpe-anw-central.com
vrf red
switch(config-hpe-anw-central)#

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

165

Exampleofaconfigurationwithlocationonly:
switch(config-hpe-anw-central)# location-override-alternative hpe-anw-central.com
switch(config-hpe-anw-central)#
Exampleofremovingtheoverrideconfiguration:
switch(config-hpe-anw-central)# no location-override-alternative
switch(config-hpe-anw-central)# location-override-alternative 10.0.0.1 vrf red
switch(config-hpe-anw-central)#
|                                         |     |     | location-override-alternative |         | 10.0.0.1:443 | vrf red |
| --------------------------------------- | --- | --- | ----------------------------- | ------- | ------------ | ------- |
| switch(config-hpe-anw-central)#         |     |     | location-override-alternative |         |              |         |
| 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |     |                               | vrf red |              |         |
| switch(config-hpe-anw-central)#         |     |     | location-override-alternative |         |              |         |
[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443 vrf red
| Command History     |         |         |                                     |           |     |     |
| ------------------- | ------- | ------- | ----------------------------------- | --------- | --- | --- |
| Release             |         |         | Modification                        |           |     |     |
| 10.13.1000          |         |         | CommandupdatedtoreflectOTPscenario. |           |     |     |
| 10.12.1000          |         |         | Commandintroduced.                  |           |     |     |
| Command Information |         |         |                                     |           |     |     |
| Platforms           | Command | context |                                     | Authority |     |     |
Allplatforms config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show hpe-anw-central
AppliesonlytotheHPE ArubaNetworking4100iswitch.
show hpe-anw-central
Description
ShowsinformationaboutHPE ArubaNetworkingCentralconnectionandthestatusoftheActivate
serverconnection.
Examples
ExampleofaswitchthathastheHPE ArubaNetworkingCentralconnection:
| switch# show       | hpe-anw-central |        |        |             |     |     |
| ------------------ | --------------- | ------ | ------ | ----------- | --- | --- |
| Central admin      | state           |        |        | : enabled   |     |     |
| Central location   |                 |        |        | : 10.0.0.1  |     |     |
| VRF for connection |                 |        |        | : mgmt      |     |     |
| Shared Token       |                 |        |        | : N/A       |     |     |
| Central connection |                 | status |        | : connected |     |     |
| Central source     |                 |        |        | : activate  |     |     |
| Central source     | connection      |        | status | : connected |     |     |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
HPE ArubaNetworkingCentralintegration|166

| Main location |                   |      |               | : 10.0.0.1                     |
| ------------- | ----------------- | ---- | ------------- | ------------------------------ |
| Main VRF      |                   |      |               | : mgmt                         |
| Alternative   | location          |      |               | : N/A                          |
| Alternative   | VRF               |      |               | : N/A                          |
| Activate      | Server            | URL  |               | : devices-v2.arubanetworks.com |
| System        | time synchronized |      | from Activate | : N/A                          |
| Source        | IP                |      |               | : N/A                          |
| Source        | IP Overridden     |      |               | : False                        |
| Central       | support           | mode |               | : disabled                     |
ExampleofaswitchwhenthemainCLIlocationisused:
| switch# | show       | hpe-anw-central |        |             |
| ------- | ---------- | --------------- | ------ | ----------- |
| Central | admin      | state           |        | : enabled   |
| Central | location   |                 |        | : 10.0.0.1  |
| VRF for | connection |                 |        | : mgmt      |
| Shared  | secret     |                 |        | : N/A       |
| Central | connection | status          |        | : connected |
| Central | source     |                 |        | : cli       |
| Central | source     | connection      | status | : connected |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
| Main location |                   |      |               | : 10.0.0.1                     |
| ------------- | ----------------- | ---- | ------------- | ------------------------------ |
| Main VRF      |                   |      |               | : mgmt                         |
| Alternative   | location          |      |               | : 20.0.0.1                     |
| Alternative   | VRF               |      |               | : default                      |
| Activate      | server            | URL  |               | : devices-v2.arubanetworks.com |
| System        | time synchronized |      | from Activate | : N/A                          |
| Source        | IP                |      |               | : N/A                          |
| Source        | IP Overridden     |      |               | : False                        |
| Central       | support           | mode |               | : disabled                     |
ExampleofaswitchwhenthealternativeCLI locationisused:
| switch# | show       | hpe-anw-central |        |             |
| ------- | ---------- | --------------- | ------ | ----------- |
| Central | admin      | state           |        | : enabled   |
| Central | location   |                 |        | : 20.0.0.1  |
| VRF for | connection |                 |        | : default   |
| Shared  | secret     |                 |        | : N/A       |
| Central | connection | status          |        | : connected |
| Central | source     |                 |        | : cli       |
| Central | source     | connection      | status | : connected |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
| Main location |                   |            |               | : 10.0.0.1                     |
| ------------- | ----------------- | ---------- | ------------- | ------------------------------ |
| Main VRF      |                   |            |               | : mgmt                         |
| Alternative   | location          |            |               | : 20.0.0.1                     |
| Alternative   | VRF               |            |               | : default                      |
| Activate      | server            | URL        |               | : devices-v2.arubanetworks.com |
| System        | time synchronized |            | from Activate | : N/A                          |
| Source        | IP                |            |               | : N/A                          |
| Source        | IP Overridden     |            |               | : False                        |
| Central       | support           | mode       |               | : disabled                     |
| Central       | admin             | state      |               | : enabled                      |
| Central       | location          |            |               | : 20.0.0.1                     |
| VRF for       | connection        |            |               | : default                      |
| Shared        | secret            |            |               | : N/A                          |
| Central       | connection        | status     |               | : connected                    |
| Central       | source            |            |               | : cli                          |
| Central       | source            | connection | status        | : connected                    |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 167

| Main location        |              |      |               | : 10.0.0.1                     |
| -------------------- | ------------ | ---- | ------------- | ------------------------------ |
| Main VRF             |              |      |               | : mgmt                         |
| Alternative          | location     |      |               | : 20.0.0.1                     |
| Alternative          | VRF          |      |               | : default                      |
| Activate             | server       | URL  |               | : devices-v2.arubanetworks.com |
| System time          | synchronized |      | from Activate | : N/A                          |
| Source IP            |              |      |               | : N/A                          |
| Source IP Overridden |              |      |               | : False                        |
| Central support      |              | mode |               | : disabled                     |
Exampleofaswitchwhenthelocationisobtainedfrom DHCPoptions:
| switch# show       | hpe-anw-central |        |        |                                        |
| ------------------ | --------------- | ------ | ------ | -------------------------------------- |
| Central admin      | state           |        |        | : enabled                              |
| Central location   |                 |        |        | : central-western-us.arubanetworks.com |
| VRF for connection |                 |        |        | : RED                                  |
| Shared secret      |                 |        |        | : N/A                                  |
| Central connection |                 | status |        | : connected                            |
| Central source     |                 |        |        | : DHCP                                 |
| Central source     | connection      |        | status | : connected                            |
Central source last connected on : Fri Jun 30 20:22:33 UTC 2023
| Main location        |              |      |               | : central-western-us.arubanetworks.com |
| -------------------- | ------------ | ---- | ------------- | -------------------------------------- |
| Main VRF             |              |      |               | : mgmt                                 |
| Alternative          | location     |      |               | : N/A                                  |
| Alternative          | VRF          |      |               | : N/A                                  |
| Activate             | server       | URL  |               | : devices-v2.arubanetworks.com         |
| System time          | synchronized |      | from Activate | : N/A                                  |
| Source IP            |              |      |               | : 100.0.0.1                            |
| Source IP Overridden |              |      |               | : False                                |
| Central support      |              | mode |               | : disabled                             |
Exampleofaswitchwhen HPE ArubaNetworkingCentralisdisabled:
| switch# show         | hpe-anw-central |           |               |                                |
| -------------------- | --------------- | --------- | ------------- | ------------------------------ |
| Central admin        | state           |           |               | : disabled                     |
| Central location     |                 |           |               | : N/A                          |
| VRF for connection   |                 |           |               | : N/A                          |
| Shared secret        |                 |           |               | : N/A                          |
| Central connection   |                 | status    |               | : N/A                          |
| Central source       |                 |           |               | : none                         |
| Central source       | connection      |           | status        | : N/A                          |
| Central source       | last            | connected | on            | : N/A                          |
| Main location        |                 |           |               | : N/A                          |
| Main VRF             |                 |           |               | : N/A                          |
| Alternative          | location        |           |               | : N/A                          |
| Alternative          | VRF             |           |               | : N/A                          |
| Activate             | server          | URL       |               | : devices-v2.arubanetworks.com |
| System time          | synchronized    |           | from Activate | : N/A                          |
| Source IP            |                 |           |               | : N/A                          |
| Source IP Overridden |                 |           |               | : False                        |
| Central support      |                 | mode      |               | : disabled                     |
| Central admin        | state           |           |               | : disabled                     |
| Central location     |                 |           |               | : N/A                          |
| VRF for connection   |                 |           |               | : N/A                          |
| Shared secret        |                 |           |               | : N/A                          |
| Central connection   |                 | status    |               | : N/A                          |
| Central source       |                 |           |               | : none                         |
| Central source       | connection      |           | status        | : N/A                          |
| Central source       | last            | connected | on            | : N/A                          |
HPE ArubaNetworkingCentralintegration|168

| Main location        |              |      |               |     | : N/A                          |
| -------------------- | ------------ | ---- | ------------- | --- | ------------------------------ |
| Main VRF             |              |      |               |     | : N/A                          |
| Alternative          | location     |      |               |     | : N/A                          |
| Alternative          | VRF          |      |               |     | : N/A                          |
| Activate             | server       | URL  |               |     | : devices-v2.arubanetworks.com |
| System time          | synchronized |      | from Activate |     | : N/A                          |
| Source IP            |              |      |               |     | : N/A                          |
| Source IP Overridden |              |      |               |     | : False                        |
| Central support      |              | mode |               |     | : disabled                     |
Exampleofaswitchwhen HPE ArubaNetworkingCentralisnotreachable:
| switch# show       | hpe-anw-central |        |        |     |                 |
| ------------------ | --------------- | ------ | ------ | --- | --------------- |
| Central admin      | state           |        |        |     | : enabled       |
| Central location   |                 |        |        |     | : N/A           |
| VRF for connection |                 |        |        |     | : N/A           |
| Shared secret      |                 |        |        |     | : N/A           |
| Central connection |                 | status |        |     | : not-reachable |
| Central source     |                 |        |        |     | : activate      |
| Central source     | connection      |        | status |     | : connected     |
Central source last connected on : Fri Jun 30 20:22:33 UTC 2023
| Main location        |              |      |               |                                                 | : N/A                          |
| -------------------- | ------------ | ---- | ------------- | ----------------------------------------------- | ------------------------------ |
| Main VRF             |              |      |               |                                                 | : N/A                          |
| Alternative          | location     |      |               |                                                 | : N/A                          |
| Alternative          | VRF          |      |               |                                                 | : N/A                          |
| Activate             | server       | URL  |               |                                                 | : devices-v2.arubanetworks.com |
| System time          | synchronized |      | from Activate |                                                 | : N/A                          |
| Source IP            |              |      |               |                                                 | : N/A                          |
| Source IP Overridden |              |      |               |                                                 | : False                        |
| Central support      |              | mode |               |                                                 | : disabled                     |
| Command History      |              |      |               |                                                 |                                |
| Release              |              |      |               | Modification                                    |                                |
| 10.15                |              |      |               | Commandsyntaxchangedfromaruba-centraltohpe-anw- |                                |
central.
| 10.12.1000          |         |     |         | Enhancedtosupportmorescenarios   |     |
| ------------------- | ------- | --- | ------- | -------------------------------- | --- |
| 10.08               |         |     |         | Commandintroducedon4100iSwitches |     |
| Command Information |         |     |         |                                  |     |
| Platforms           | Command |     | context | Authority                        |     |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show running-config |     |     | current-context |     |     |
| ------------------- | --- | --- | --------------- | --- | --- |
AppliesonlytotheHPE ArubaNetworking4100iswitch.
| show running-config |     | current-context |     |     |     |
| ------------------- | --- | --------------- | --- | --- | --- |
Description
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 169

Showstherunningconfigurationforthecurrent-context.IfuserisinthecontextofHPE Aruba
NetworkingCentral(config-hpe-anw-central),thentheHPE ArubaNetworkingCentralrunning
configurationisdisplayed.
Examples
ShowstherunningconfigurationofHPE ArubaNetworkingCentral:
switch(config-hpe-anw-central)# show running-config current-context
hpe-anw-central
disable
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
HPE ArubaNetworkingCentralintegration|170

Chapter 12

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

This configuration will disable flow tracking statistics collection.

Parameter

Description

<INTERFACE-LIST>

Usage

Specifies a list of ports/LAGs to be blocked for egressing. Specify a
single interface or LAG, or a range as a comma-separated list, or
both. For example: 1/1/1, 1/1/3-1/1/6,lag2, lag1-lag4.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

171

Whenaportfilterconfigurationisappliedonthesameingressphysicalport/LAG,theconfigurationis
updatedwiththenewsetsofegressports/LAGsthataretobeblockedforegressingandthatarenota
partofitspreviousconfiguration.Duplicateupdatesonanexistingportfilterconfigurationareignored.
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
| switch(config)#    | interface  | 1/1/1 |                       |
| ------------------ | ---------- | ----- | --------------------- |
| switch(config-if)# | portfilter |       | 1/1/3-1/1/6,lag1-lag4 |
CreatingafilterthatpreventspacketsreceivedonLAG1fromforwardingtoports1/1/6andLAGs2and
4:
| switch(config)#        | interface | lag        | 1               |
| ---------------------- | --------- | ---------- | --------------- |
| switch(config-lag-if)# |           | portfilter | 1/1/6,lag2,lag4 |
Removingfiltersfromanexistingconfigurationthatallowsbackpacketsreceivedonport1/1/1to
forwardtoports1/1/6andLAGs3and4:
| switch(config)#    | interface | 1/1/1      |                 |
| ------------------ | --------- | ---------- | --------------- |
| switch(config-if)# | no        | portfilter | 1/1/6,lag3,lag4 |
RemovingallfiltersfromanexistingconfigurationthatallowsbackpacketsreceivedonLAG1to
forwardtoalltheportsandLAGs:
| switch(config)#        | interface | lag           | 1   |
| ---------------------- | --------- | ------------- | --- |
| switch(config-lag-if)# |           | no portfilter |     |
Command History
| Release        |     |     | Modification                             |
| -------------- | --- | --- | ---------------------------------------- |
| 10.14          |     |     | AddedinformationrelatedtorolebasedIPFIX. |
| 10.07orearlier |     |     | --                                       |
Command Information
Portfiltering|172

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
4100 config-if Administratorsorlocalusergroupmemberswithexecution
| 6000 | config-lag-if |     | rightsforthiscommand. |
| ---- | ------------- | --- | --------------------- |
6100
show portfilter
| show portfilter | [<IFNAME>] |     |     |
| --------------- | ---------- | --- | --- |
Description
Displaysfiltersettingsforallinterfacesoraspecificinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IFNAME>
Specifiestheingressinterfacename.
Specifiesoneofthesevalues:
<FQDN>:afullyqualifieddomainname.
n
n <IPV4>:anIPv4address.
<IPV6>:anIPv6address.
n
Examples
Displayingallportfiltersettingsontheswitch:
| switch# show | portfilter |            |     |
| ------------ | ---------- | ---------- | --- |
| Incoming     | Blocked    |            |     |
| Interface    | Outgoing   | Interfaces |     |
-------------------------------------------------------------------------------
| 1/1/1 | 1/1/3-1/1/6,lag1-lag2 |     |     |
| ----- | --------------------- | --- | --- |
1/1/3 1/1/1,1/1/5,1/1/7,1/1/9,1/1/11,1/1/13,1/1/15,1/1/17,1/1/19,1/1/21,
1/1/23,1/1/25,1/1/27,1/1/29,1/1/31,1/1/33,1/1/35
| lag2 | 1/1/1,1/1/3-1/1/6 |     |     |
| ---- | ----------------- | --- | --- |
Displayingtheportfiltersettingsforport1/1/1:
| switch# show | portfilter | 1/1/1      |     |
| ------------ | ---------- | ---------- | --- |
| Incoming     | Blocked    |            |     |
| Interface    | Outgoing   | Interfaces |     |
-------------------------------------------------------------------------------
| 1/1/1 | 1/1/3-1/1/6,lag1-lag2 |     |     |
| ----- | --------------------- | --- | --- |
DisplayingtheportfiltersettingsforLAG2:
| switch# show | portfilter | lag2       |     |
| ------------ | ---------- | ---------- | --- |
| Incoming     | Blocked    |            |     |
| Interface    | Outgoing   | Interfaces |     |
-------------------------------------------------------------------------------
| lag2            | 1/1/1,1/1/3-1/1/6 |     |     |
| --------------- | ----------------- | --- | --- |
| Command History |                   |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 173

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
4100 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6000 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6100 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
Portfiltering|174

Chapter 13

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

175

1. ConfigureoneormoreDNSnameserverswiththecommandip dns server.
2. ToresolveDNSrequestsbyappendingadomainnametotherequests,eitherconfigureasingle
domainnamewiththecommandip dns domain-name,orconfigurealistofuptosixdomain
| nameswiththecommandip |     |     | dns | domain-list. |
| --------------------- | --- | --- | --- | ------------ |
3. Tousestaticnameresolutionforcertainhosts,associateanIPaddresstoahostwiththe
| commandip |     | dns host. |     |     |
| --------- | --- | --------- | --- | --- |
4. ReviewyourDNSconfigurationsettingswiththecommandshow ip dns.
Examples
Thisexamplecreatesthefollowingconfiguration:
n Definesthedomainswitch.comtoappendtoallrequests.
n DefinesaDNSserverwithIPv4addressof1.1.1.1.
n DefinesastaticDNShostnamedmyhost1withanIPv4addressof3.3.3.3.
n DNSclienttrafficissentonthedefaultVRF(nameddefault).
| switch(config)# |                | ip dns domain-name    |         | switch.com |
| --------------- | -------------- | --------------------- | ------- | ---------- |
| switch(config)# |                | ip dns server-address |         | 1.1.1.1    |
| switch(config)# |                | ip dns host           | myhost1 | 3.3.3.3    |
| switch(config)# |                | exit                  |         |            |
| switch#         | show           | ip dns                |         |            |
| VRF             | Name : default |                       |         |            |
| Domain          | Name:          | switch.com            |         |            |
| Name            | Server(s):     | 1.1.1.1               |         |            |
| Host            | Name           |                       |         | Address    |
--------------------------------------------------------------------------------
myhost1 3.3.3.3
switch#
| DNS       | client      | commands      |      |               |
| --------- | ----------- | ------------- | ---- | ------------- |
| ip dns    | domain-list |               |      |               |
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | default]      |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf default] |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
DNS|176

| switch(config)# |     |     | ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ----------- | --- |
switch(config)#
|     |     |     | ip dns | domain-list |     | domain2.com |     |
| --- | --- | --- | ------ | ----------- | --- | ----------- | --- |
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
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<DOMAIN-NAME>
SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     |     | ip dns | domain-name |     | domain.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |         |     | no ip dns | domain-name |     | domain.com |     |
| --------------- | ------- | --- | --------- | ----------- | --- | ---------- | --- |
| Command         | History |     |           |             |     |            |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 177

| Release        |             |         |         |     | Modification |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | host |             |           |           |                  |     |     |
| --------- | ---- | ----------- | --------- | --------- | ---------------- | --- | --- |
| ip dns    | host | <HOST-NAME> | <IP-ADDR> |           | [ vrf <VRF-NAME> | ]   |     |
| no ip dns | host | <HOST-NAME> |           | <IP-ADDR> | [ vrf <VRF-NAME> |     | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadof
queryingaDNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFis
defined,thedefaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
| ThisexampledefinesanIPv4addressof     |         |     |        |            | 3.3.3.3forhost1.  |     |       |
| ------------------------------------- | ------- | --- | ------ | ---------- | ----------------- | --- | ----- |
| switch(config)#                       |         | ip  | dns    | host host1 | 3.3.3.3           |     |       |
| ThisexampledefinesanIPv6addressofb::5 |         |     |        |            | forhost 1.        |     |       |
| switch(config)#                       |         | ip  | dns    | host host1 | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |         |     |        |            | host 1withaddress |     | b::5. |
| switch(config)#                       |         | no  | ip dns | host       | host1 b::5        |     |       |
| Command                               | History |     |        |            |                   |     |       |
DNS|178

| Release        |             |         |         |     | Modification |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | server         | address |           |     |       |            |     |
| --------- | -------------- | ------- | --------- | --- | ----- | ---------- | --- |
| ip dns    | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
| switch(config)# |     |     | ip dns | server-address |     | 1.1.1.1 |     |
| --------------- | --- | --- | ------ | -------------- | --- | ------- | --- |
Thisexampledefinesanameserverata::1.
| switch(config)# |     |     | ip dns | server-address |     | a::1 |     |
| --------------- | --- | --- | ------ | -------------- | --- | ---- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)# |         |     | no ip dns | server-address |              | a::1 |     |
| --------------- | ------- | --- | --------- | -------------- | ------------ | ---- | --- |
| Command         | History |     |           |                |              |      |     |
| Release         |         |     |           |                | Modification |      |     |
| 10.07orearlier  |         |     |           |                | --           |      |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 179

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip dns |                  |     |     |
| ----------- | ---------------- | --- | --- |
| show ip dns | [vrf <VRF-NAME>] |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
DNSclientarbitrationontheMGMTinterfaceonaMGMTVRFcanbeupdatedviathreedifferentmethods.
1. Usingthedomain-name<name>ornameservers<servers>commandsinthecommand-lineinterface.
2. Usingthe ipdnsdomain-name<DOMAIN-NAME>vrfMGMToripdnsserver-address<SERVER>vrf
MGMTcommandsinthecommand-lineinterface.
3. Usingtheipdhcpcommandinthecommand-lineinterface(dynamicenties).
AOS-CXgivesthefollowingprioritylevelstothethesethreeupdatemothods.
n Priority1-standaloneCLIconfiguration
Priority2-staticipdnsconfiguration
n
n Priority3-Dynamicconfig
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|180

Device discovery and configuration

Chapter 14

Device discovery and configuration

The switch supports automatic discovery and configuration of other devices on the network.

Device profiles

Device profiles rely on role configurations. For information on role configurations, see the Security Guide.

Device profiles are used to dynamically assign port attributes based on the type of devices connected,
without having to create a RADIUS infrastructure. You can map device profiles to device groups. A device
group contains various match criteria, which can be obtained from multiple sources, such as LLDP, CDP,
and local MAC match. Device profiles contain port attributes to be assigned to the port when a
connected device matches a device group.

Device profiles are supported on different scenarios. It can be applied on interfaces that are configured
with security (802.1X or MAC authentication), or applied based on L2 port (LLDP, CDP), or applied on
standalone ports with the block-until-profile-applied command enabled. All the methods are mutually
exclusive of each other. The block-until-profile-applied mode must be configured only when there is a
standalone port where no security has been configured and when you want the port to be offline until at
least one client is onboarded based on the match and ignore criteria that you configure. Local MAC
match is supported when you configure block-until-profile-applied command or device profile with
security.

Up to eight device profiles can be configured.

See the Security Guide for the following commands:

n The port-access onboarding-method precedence command—If you are configuring both security
and device profile on the port, and you want to configure the order in which the methods will be
executed.

n The port-access fallback-role command—If you want to configure a role that must be applied to

devices when no other role exists or can be derived for that device.

If you configure a match criteria that matches across multiple device profiles, then the priority
considered is LLDP, CDP, and then local MAC match. That is, LLDP precedes over CDP, which in turn
precedes over local MAC match.

The following figure displays a simple configuration of device profile and AAA authentication with
RADIUS server and HPE Aruba Networking ClearPass Policy Manager. Local MAC match feature is useful
when you do not want to afford RADIUS infrastructure or when you want to use local authentication as a
backup method in case the RADIUS server is unreachable.

Figure 1 Example of device profile setup along with RADIUS infrastructure

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

181

;"/>
| Configuring | a device | profile | for LLDP |     |
| ----------- | -------- | ------- | -------- | --- |
Procedure
| 1. CreateanLLDPgroupwiththecommandport-access |     |     |     | lldp-group. |
| --------------------------------------------- | --- | --- | --- | ----------- |
2. DefinerulesforaddingdevicestoanLLDPgroupwiththecommandmatch.
3. DefinerulesforignoringdevicessothattheyarenotaddedtoanLLDPgroupwiththecommand
ignore.
4. Createadeviceprofilewiththecommandport-access device-profile.
| 5. AddtheLLDPgroupwiththecommandassociate |     |     |     | lldp-group. |
| ----------------------------------------- | --- | --- | --- | ----------- |
6. Addaroletoadeviceprofilewiththecommandassociate role.Makesurethattheroleis
alreadycreated.Forinformationonhowtocreatearole,seeportaccessroleinformationinthe
SecurityGuide.
7. Enablethedeviceprofilewiththecommandenable.
| Configuring                                 | a device | profile | for CDP |            |
| ------------------------------------------- | -------- | ------- | ------- | ---------- |
| 1. CreateaCDPgroupwiththecommandport-access |          |         |         | cdp-group. |
2. DefinerulesforaddingdevicestoaCDPgroupwiththecommandmatch.
3. DefinerulesforignoringdevicessothattheyarenotaddedtoaCDPgroupwiththecommand
ignore.
4. Createadeviceprofilewiththecommandport-access device-profile.
5. AddaCDPgrouptoadeviceprofilewiththecommandassociate cdp-group.
6. Addaroletoadeviceprofilewiththecommandassociate role.Makesurethattheroleis
alreadycreated.Forinformationonhowtocreatearole,seeportaccessroleinformationinthe
SecurityGuide.
7. Enableadeviceprofilewiththecommandenable.
| Configuring | a device | profile | for local | MAC match |
| ----------- | -------- | ------- | --------- | --------- |
Procedure
Devicediscoveryandconfiguration|182

1. Create a MAC group with the mac-group command.

2. Define rules for adding devices to a MAC group with the match (for MAC groups) command.

3. Define rules for ignoring devices so that they are not added to a MAC group with the ignore (for

MAC groups) command.

4. Create a device profile with the port-access device-profile command.

5. Associate a MAC group with a device profile with the associate mac-group command.

6. Add a role to a device profile with the associate role command. Make sure that the role is

already created. For information on how to create a role, see port access role information in the
Security Guide.

7. Enable a device profile with the enable command.

Device Profile Usage Considerations

The following behaviors and limitations should be taken into consideration when configuring a device
profile on Link Aggregation Group (LAG) or Multi-chassis Link Aggregation Group (MCLAG).

Device Profiles on LAG and MCLAG

n When using Device profile to onboard a device with multiple interfaces (such as a dual port AP) over a

LAG, set the authentication mode in the role applied to the device to device-mode. The multi-
domain authentication mode is not supported with a device profile on a LAG.

n When using Device profile to onboard a device on MCLAG port, set the authentication mode in the
role applied to the device to device-mode or proxy-mode. The multi-domain and client-mode
authentication mode is not supported with device profile on MCLAG.

n It is not recommended to connect different devices to the same LAG when using a device profile on

the LAG.

n When updating a LAG membership, all the device profile clients on the LAG are logged off

automatically from the switch and from both peers on MCLAG port.

n If you issue the command aaa authentication port-access allow-cdp-proxy-logoff on the LAG, a
proxy-logoff TLV received on any member interface of the LAG will log off all clients onboarded on
the LAG.

n Depending on resource availability or auth/role application status on each peer, the same MAC may

be allowed in one peer and denied in another for a MAC learned on MCLAG port.

Security Considerations

n Each individual interface of a LAG must successfully match a Device profile for the corresponding

interface to be unblocked on the data plane.

n An onboarded client on the LAG is authorized to send and receive packets on any of the member
interface of the LAG that is unblocked on the data plane. This is true even for a different client
connected to the same LAG.

n When using LLDP packets to authenticate a device using a device profile on a LAG, issue the
command aaa authentication port-access allow-lldp-auth mac chassis-mac to set the
authentication MAC address as the chassis MAC address

n LLDP BPDUs are blocked by default. Issue the command aaa authentication port-access allow-

lldp-bpdu to allow the LLDP BPDUs.

n If a Device profile is used to onboard multiple devices connected to the same LAG, the client limit on

the LAG must be configured to match the number of clients onboarding the LAG.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

183

n WhenusingLLDPpacketstoauthenticateaDualPortAPusingadeviceprofileonaLAG,issuethe
commandaaa authentication port-access allow-lldp-auth mac source-mactosetthe
authenticationMACaddressastheport/interfaceMACaddress.
| Supported | Role | Attributes |     |
| --------- | ---- | ---------- | --- |
Thefollowingport-accessroleattributesaresupportedforclientsthatonboardviadeviceprofileona
LAG.
n Authenticationmode
n Clientinactivitytimeout
n Sessiontimeout
n AccessandTrunkVLANs
n Port-Accesspolicy(notsupportedonMCLAG)
n MTU
n PoEPriority
n PoEAllocate-By
n Private-VLAN
n STPadminedgeport
n Trustmode
n GBProle
| Device             | profile        | commands    |                |
| ------------------ | -------------- | ----------- | -------------- |
| aaa authentication |                | port-access | allow-cdp-auth |
| aaa authentication |                | port-access | allow-cdp-auth |
| no aaa             | authentication | port-access | allow-cdp-auth |
Description
UsethiscommandtoalloworblockauthenticationontheCDP(CiscoDiscoveryProtocol)BPDU(Bridge
ProtocolDataUnit).Thisisallowedbydefault.Thenoformofthiscommandpreventsauthentication
onCDPpacketsreceivedontheport.Thiscommandcanbeissuedfromtheinterface(config-if)orLink
AggregationGroup(config-lag-if)contexts.
Examples
AllowingauthenticationonaCDPCPDUoninterface1/1/1:
| switch(config)# |     | interface | 1/1/1 |
| --------------- | --- | --------- | ----- |
switch(config-if)# aaa authentication port-access allow-cdp-auth
AllowingauthenticationonaCDPCPDUonaLAGport:
| switch(config)# |     | interface | lag 1 |
| --------------- | --- | --------- | ----- |
switch(config-lag-if)# aaa authentication port-access allow-cdp-auth
| Command | History |     |     |
| ------- | ------- | --- | --- |
Devicediscoveryandconfiguration|184

Release

10.13

Modification

This command can be issued from a Link Aggregation Group (LAG)
context.

10.07 or earlier

--

Command Information

Platforms

Command context

Authority

4100i
6000
6100

config-if
config-lag-if

Administrators or local user group members with execution
rights for this command.

aaa authentication port-access allow-cdp-bpdu

aaa authentication port-access allow-cdp-bpdu
no aaa authentication port-access allow-cdp-bpdu

Description

Allows all packets related to the CDP (Cisco Discovery Protocol) BPDU (Bridge Protocol Data Unit) on a
secure port or LAG. This command can be issued from the interface (config-if) or Link Aggregation
Group (config-lag-if) contexts. The no form of this command blocks the CDP BPDU on a secure port.
On a nonsecure port, the command has no effect.

Examples

Allowing a CDP BPDU on secure port 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# aaa authentication port-access allow-cdp-bpdu
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

: access_switches
:

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

185

CDP Group
Role
Status
Failure Reason

: hpe-anw-ap_cdp
: test_ap_role
: In Progress
:

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

Allowing a CDP BPDU on LAG 1:

switch(config)# interface lag 1
switch(config-lag-if)# aaa authentication port-access allow-cdp-bpdu

Command History

Release

10.13

Modification

This command can be issued from a Link Aggregation Group (LAG)
context.

10.07 or earlier

--

Command Information

Platforms

Command context

Authority

4100i
6000
6100

config-if
config-lag-if

Administrators or local user group members with execution
rights for this command.

aaa authentication port-access allow-cdp-proxy-logoff

aaa authentication port-access allow-cdp-proxy-logoff
no aaa authentication port-access allow-cdp-proxy-logoff

Description

Device discovery and configuration | 186

AllowsaclienttobeloggedofffromthesystemviaaspecialTLVintheCDPpacket.Bydefault,proxy
logoffviaCDPpacketsupportisdisabled.Whenallow-cdp-proxy-logoffisenabled,TLVreceivedfrom
CDPpacketscorrespondingtologoffprocessingwillbereadandlogoffisissuedtotheclients.Thisonly
worksonclientauthenticationenabledportsandaaa authentication port-access allow-cdp-bpdu
mustbeenabledtoprocess.Thiscommandcanbeissuedfromtheinterface(config-if)orLink
AggregationGroup(config-lag-if)contexts.
Examples
AllowingaclienttobeloggedofffromthesystemviaaspecialTLVintheCDP packet:
| switch(config)# |     |     | interface |     | 1/1/1 |     |     |     |     |
| --------------- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
switch(config-if)# aaa authentication port-access allow-cdp-proxy-logoff
| switch(config-if)# |     |       |     | show | running-config |     | interface | 1/1/1 |     |
| ------------------ | --- | ----- | --- | ---- | -------------- | --- | --------- | ----- | --- |
| interface          |     | 1/1/1 |     |      |                |     |           |       |     |
no shutdown
|     | vlan               | access | 1   |             |     |                        |               |     |     |
| --- | ------------------ | ------ | --- | ----------- | --- | ---------------------- | ------------- | --- | --- |
|     | aaa authentication |        |     | port-access |     | allow-cdp-bpdu         |               |     |     |
|     | aaa authentication |        |     | port-access |     | allow-cdp-proxy-logoff |               |     |     |
|     | aaa authentication |        |     | port-access |     | allow                  | client-limit  |     | 2   |
|     | aaa authentication |        |     | port-access |     | dot1x                  | authenticator |     |     |
enable
|     | aaa authentication |     |     | port-accss |     | mac-auth |     |     |     |
| --- | ------------------ | --- | --- | ---------- | --- | -------- | --- | --- | --- |
enable
exit
Theaaaauthenticationport-accessallow-cdp-proxy-logoffcommandcanalsobeissuedfromaLAGport
context
| switch(config)# |     |     | interface |     | lag 1 |     |     |     |     |
| --------------- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
switch(config-lag if)# aaa authentication port-access allow-cdp-proxy-logoff
| Command | History |     |     |     |     |                                                      |     |     |     |
| ------- | ------- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
| Release |         |     |     |     |     | Modification                                         |     |     |     |
| 10.13   |         |     |     |     |     | ThiscommandcanbeissuedfromaLinkAggregationGroup(LAG) |     |     |     |
context.
| 10.09.1000 |             |         |     |         |     | Commandintroduced. |     |     |     |
| ---------- | ----------- | ------- | --- | ------- | --- | ------------------ | --- | --- | --- |
| Command    | Information |         |     |         |     |                    |     |     |     |
| Platforms  |             | Command |     | context |     | Authority          |     |     |     |
config-if
| 4100i |     |               |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |     |
| ----- | --- | ------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
| 6000  |     | config-lag-if |     |     |     | rightsforthiscommand.                              |     |     |     |
6100
| aaa    | authentication |     | port-access |             | allow-lldp-bpdu |                 |     |     |     |
| ------ | -------------- | --- | ----------- | ----------- | --------------- | --------------- | --- | --- | --- |
| aaa    | authentication |     | port-access |             | allow-lldp-bpdu |                 |     |     |     |
| no aaa | authentication |     |             | port-access |                 | allow-lldp-bpdu |     |     |     |
Description
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 187

AllowsallpacketsrelatedtotheLLDPBPDU(BridgeProtocolDataUnit)onasecureport.Thiscommand
canbeissuedfromtheinterface(config-if)orLinkAggregationGroup(config-lag-if)contexts.
ThenoformofthiscommandblockstheLLDPBPDUonasecureport.Onanonsecureport,the
commandhasnoeffect.
Examples
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
| vlan               | access | 1   |             |     |                 |
| ------------------ | ------ | --- | ----------- | --- | --------------- |
| aaa authentication |        |     | port-access |     | allow-lldp-bpdu |
| aaa authentication |        |     | port-access |     | mac-auth        |
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
AllowinganLLDPBPDUonaLAGport:
Devicediscoveryandconfiguration|188

| switch(config)# |     |     | interface |     | lag 1 |     |     |
| --------------- | --- | --- | --------- | --- | ----- | --- | --- |
switch(config-lag-if)#aaa authentication port-access allow-lldp-bpdu
| Command | History |     |     |     |     |                                                      |     |
| ------- | ------- | --- | --- | --- | --- | ---------------------------------------------------- | --- |
| Release |         |     |     |     |     | Modification                                         |     |
| 10.13   |         |     |     |     |     | ThiscommandcanbeissuedfromaLinkAggregationGroup(LAG) |     |
context.
| 10.07orearlier |             |         |     |         |     | --        |     |
| -------------- | ----------- | ------- | --- | ------- | --- | --------- | --- |
| Command        | Information |         |     |         |     |           |     |
| Platforms      |             | Command |     | context |     | Authority |     |
config-if
| 4100i |     |               |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ----- | --- | ------------- | --- | --- | --- | -------------------------------------------------- | --- |
| 6000  |     | config-lag-if |     |     |     | rightsforthiscommand.                              |     |
6100
| associate    | cdp-group |           |              |              |     |     |     |
| ------------ | --------- | --------- | ------------ | ------------ | --- | --- | --- |
| associate    | cdp-group |           | <GROUP-NAME> |              |     |     |     |
| no associate |           | cdp-group |              | <GROUP-NAME> |     |     |     |
Description
AssociatesaCDP(CiscoDiscoveryProtocol)groupwithadeviceprofile.AmaximumoftwoCDPgroups
canbeassociatedwithadeviceprofile.
ThenoformofthiscommandremovesaCDPgroupfromadeviceprofile.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
<GROUP-NAME> SpecifiesthenameoftheCDPgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheCDPgroupmy-cdp-groupwiththedeviceprofileprofile01:
| switch(config)# |     |     | port-access |     | device-profile |     | profile01 |
| --------------- | --- | --- | ----------- | --- | -------------- | --- | --------- |
switch(config-device-profile)# associate cdp-group my-cdp-group
RemovingtheCDPgroupmy-cdp-groupfromthedeviceprofileprofile01:
| switch(config)# |     |     | port-access |     | device-profile |     | profile01 |
| --------------- | --- | --- | ----------- | --- | -------------- | --- | --------- |
switch(config-device-profile)# no associate cdp-group my-cdp-group
| Command | History |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 189

| Release        |             |     |         | Modification |           |
| -------------- | ----------- | --- | ------- | ------------ | --------- |
| 10.07orearlier |             |     |         | --           |           |
| Command        | Information |     |         |              |           |
| Platforms      | Command     |     | context |              | Authority |
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --- | --------------------- |
6100
| associate    | lldp-group |              |              |     |     |
| ------------ | ---------- | ------------ | ------------ | --- | --- |
| associate    | lldp-group | <GROUP-NAME> |              |     |     |
| no associate | lldp-group |              | <GROUP-NAME> |     |     |
Description
AssociatesanLLDPgroupwithadeviceprofile.AmaximumoftwoLLDPgroupscanbeassociatedwith
adeviceprofile
ThenoformofthiscommandremovesanLLDPgroupfromadeviceprofile.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<GROUP-NAME>
SpecifiesthenameoftheLLDPgrouptoassociatewiththedevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheLLDPgroupmy-lldp-groupwiththedeviceprofileprofile01:
| switch(config)# |     | port-access |     | device-profile | profile01 |
| --------------- | --- | ----------- | --- | -------------- | --------- |
switch(config-device-profile)# associate lldp-group my-lldp-group
RemovingtheLLDPgroupmy-lldp-groupfromthedeviceprofileprofile01:
| switch(config)# |     | port-access |     | device-profile | profile01 |
| --------------- | --- | ----------- | --- | -------------- | --------- |
switch(config-device-profile)# no associate lldp-group my-lldp-group
| Command        | History     |     |         |              |           |
| -------------- | ----------- | --- | ------- | ------------ | --------- |
| Release        |             |     |         | Modification |           |
| 10.07orearlier |             |     |         | --           |           |
| Command        | Information |     |         |              |           |
| Platforms      | Command     |     | context |              | Authority |
config-device-profile
| 4100i |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ----- | --- | --- | --- | --- | -------------------------------------------------- |
| 6000  |     |     |     |     | rightsforthiscommand.                              |
6100
Devicediscoveryandconfiguration|190

| associate    | mac-group |           |              |              |     |     |     |     |
| ------------ | --------- | --------- | ------------ | ------------ | --- | --- | --- | --- |
| associate    | mac-group |           | <GROUP-NAME> |              |     |     |     |     |
| no associate |           | mac-group |              | <GROUP-NAME> |     |     |     |     |
Description
AssociatesaMACgroupwithadeviceprofile.AmaximumoftwoMACgroupscanbeassociatedwitha
deviceprofile.
ThenoformofthiscommandremovesaMACgroupfromadeviceprofile.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<GROUP-NAME> SpecifiesthenameoftheMACgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheMACgroupmac01-groupwiththedeviceprofileprofile01:
| switch(config)#                |     |     | port-access |     | device-profile |     | profile01 |             |
| ------------------------------ | --- | --- | ----------- | --- | -------------- | --- | --------- | ----------- |
| switch(config-device-profile)# |     |     |             |     | associate      |     | mac-group | mac01-group |
RemovingtheMACgroupmac01-groupfromthedeviceprofileprofile01:
| switch(config)# |     |     | port-access |     | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | --- | -------------- | --- | --------- | --- |
switch(config-device-profile)# no associate mac-group mac01-group
| Command        | History     |         |     |         |              |           |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --------- | --- | --- |
| Release        |             |         |     |         | Modification |           |     |     |
| 10.07orearlier |             |         |     |         | --           |           |     |     |
| Command        | Information |         |     |         |              |           |     |     |
| Platforms      |             | Command |     | context |              | Authority |     |     |
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
6100
| associate    | role |             |             |     |     |     |     |     |
| ------------ | ---- | ----------- | ----------- | --- | --- | --- | --- | --- |
| associate    | role | <ROLE-NAME> |             |     |     |     |     |     |
| no associate |      | role        | <ROLE-NAME> |     |     |     |     |     |
Description
Associatesarolewithadeviceprofile.Onlyonerolecanbeassociatedwithadeviceprofile.For
informationonhowtoconfigurearole,seetheportaccessroleinformationintheSecurityGuide.
Thenoformofthiscommandremovesarolefromadeviceprofile.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 191

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<ROLE-NAME> Specifiesthenameoftheroletoassociatewiththedeviceprofile.
Range:1to64alphanumericcharacters.
Examples
Associatingtherolemy-rolewiththedeviceprofileprofile01:
| switch(config)#                | port-access |     | device-profile |     | profile01    |
| ------------------------------ | ----------- | --- | -------------- | --- | ------------ |
| switch(config-device-profile)# |             |     | associate      |     | role my-role |
Removingtherolemy-rolefromthedeviceprofileprofile01:
| switch(config)#                | port-access |         | device-profile |           | profile01    |
| ------------------------------ | ----------- | ------- | -------------- | --------- | ------------ |
| switch(config-device-profile)# |             |         | no             | associate | role my-role |
| Command History                |             |         |                |           |              |
| Release                        |             |         | Modification   |           |              |
| 10.07orearlier                 |             |         | --             |           |              |
| Command Information            |             |         |                |           |              |
| Platforms                      | Command     | context |                | Authority |              |
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --------------------- | --- |
6100
| disable (port-access | device-profile) |     |     |     |     |
| -------------------- | --------------- | --- | --- | --- | --- |
disable
no disable
Description
Disablesadeviceprofile.
Thenoformofthiscommandenablesadeviceprofile.
Examples
Disablingadeviceprofile:
| switch(config)#                | port-access |     | device-profile |     | profile01 |
| ------------------------------ | ----------- | --- | -------------- | --- | --------- |
| switch(config-device-profile)# |             |     | disable        |     |           |
Enablingadeviceprofilenamedprofile01:
| switch(config)#                | port-access |     | device-profile |         | profile01 |
| ------------------------------ | ----------- | --- | -------------- | ------- | --------- |
| switch(config-device-profile)# |             |     | no             | disable |           |
Devicediscoveryandconfiguration|192

| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
| enable (port-access | device-profile) |     |     |
| ------------------- | --------------- | --- | --- |
enable
no enable
Description
Enablesadeviceprofile.
Thenoformofthiscommanddisablesadeviceprofile.
Examples
Enablingadeviceprofile:
| switch(config)#                | port-access | device-profile | profile01 |
| ------------------------------ | ----------- | -------------- | --------- |
| switch(config-device-profile)# |             | enable         |           |
Disablingadeviceprofilenamedprofile01:
| switch(config)#                | port-access | device-profile | profile01 |
| ------------------------------ | ----------- | -------------- | --------- |
| switch(config-device-profile)# |             | no             | enable    |
| Command History                |             |                |           |
| Release                        |             | Modification   |           |
| 10.07orearlier                 |             | --             |           |
| Command Information            |             |                |           |
| Platforms                      | Command     | context        | Authority |
config-device-profile
| 4100i |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ----- | --- | --- | -------------------------------------------------- |
| 6000  |     |     | rightsforthiscommand.                              |
6100
| ignore (for CDP | groups) |     |     |
| --------------- | ------- | --- | --- |
ignore [seq <SEQ-NUM>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |
| ---------------- | --- | ---------- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 193

no ignore [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query | <VLAN-ID>} |     |     |     |
| ---------------- | ---------- | --- | --- | --- |
Description
DefinesaruletoignoredevicesforaCDP(CiscoDiscoveryProtocol)group.Upto64match/ignorerules
canbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaCDPgroup.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
platform <PLATFORM> Specifiesthehardwareormodeldetailsoftheneighbor.Range:1
to128alphanumericcharacters.
sw-version <SWVERSION> Specifiesthesoftwareversionoftheneighbor.Range:1to128
alphanumericcharacters.
voice-vlan-query <VLAN-ID> SpecifiestheVLANqueryvalueoftheneighbor.Range:1to
65535.
Examples
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01intheplatform
TLV:
| switch(config)#           | port-access | cdp-group | grp01    |            |
| ------------------------- | ----------- | --------- | -------- | ---------- |
| switch(config-cdp-group)# |             | ignore    | platform | PLATFORM01 |
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsSWVERSIONinsoftware
versionTLV:
| switch(config)#           | port-access | cdp-group | grp01      |           |
| ------------------------- | ----------- | --------- | ---------- | --------- |
| switch(config-cdp-group)# |             | ignore    | sw-version | SWVERSION |
Removingtherulethatmatchesthesequencenumber25fromtheCDPgroupnamedgrp01.
| switch(config)#           | port-access | cdp-group | grp01  |     |
| ------------------------- | ----------- | --------- | ------ | --- |
| switch(config-cdp-group)# |             | no ignore | seq 25 |     |
Command History
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
Command Information
Devicediscoveryandconfiguration|194

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
4100i config-cdp-group Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --------------------- | --- |
6100
| ignore (for LLDP | groups) |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> |     | [type | <KEY> | [value <VALUE>]]} |
| ---------- | ------------ | --- | ----- | ----- | ----------------- |
no ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> |     | [type | <KEY> | [value <VALUE>]]} |
| ---------- | ------------ | --- | ----- | ----- | ----------------- |
Description
DefinesaruletoignoredevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedfora
group.
ThenoformofthiscommandremovesaruleforignoringdevicesfromanLLDPgroup.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
| sys-desc <SYS-DESC> |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname<SYS-NAME> SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY>    |     |     |     | SpecifiesthevendorOUIsubtypekey.Optional.      |     |
| ------------- | --- | --- | --- | ---------------------------------------------- | --- |
| value <VALUE> |     |     |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |     |
alphanumericcharacters.
Examples
AddingaruletotheLLDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01inthesystem
descriptionTLV:
| switch(config)#            | port-access |     | lldp-group |          | grp01      |
| -------------------------- | ----------- | --- | ---------- | -------- | ---------- |
| switch(config-lldp-group)# |             |     | ignore     | sys-desc | PLATFORM01 |
Removingtherulethatmatchesthesequencenumber25fromtheLLDPgroupnamedgrp01.
| switch(config)#            | port-access |     | lldp-group |     | grp01  |
| -------------------------- | ----------- | --- | ---------- | --- | ------ |
| switch(config-lldp-group)# |             |     | no match   |     | seq 25 |
| Command History            |             |     |            |     |        |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 195

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

4100i
6000
6100

config-lldp-group

Administrators or local user group members with execution
rights for this command.

ignore (for MAC groups)

[seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}

Description

Defines a rule to ignore devices for a MAC group based on the criteria of MAC address, MAC address
mask, or MAC Organizational Unique Identifier (OUI). Up to 64 ignore rules can be defined for a group.

The no form of this command removes a rule for ignoring devices from a MAC group.

Parameter

seq <SEQ-ID>

Description

Specifies the entry sequence ID of the rule to create or modify a
MAC group. If no ID is specified when adding a rule, an ID is
automatically assigned in increments of 10 in the order in which
rules are added. When more than one rule matches the command
entered, the rule with the lowest ID takes precedence. Range: 1 to
4294967295.

mac <MAC-ADDR>

Specifies the MAC address of the device to ignore.

mac-mask <MAC-MASK>

mac-oui <MAC-OUI>

Usage

Specifies the MAC address mask to ignore devices in that range.
Supported MAC address masks: /32 and /40.

Specifies the MAC OUI to ignore devices in that range. Supports
MAC OUI address of maximum length of 24 bits.

To achieve the required configuration of matches for devices, it is recommended to first ignore the
devices that you do not want to add. Then match the criteria for the rest of the devices that you want to
add to the MAC group.

For example, if you want to ignore a specific device but add all the other devices that belong to a MAC
OUI, then you must first configure the ignore criteria with a lower sequence number. And then
configure match criteria with a higher sequence number.

Examples

Adding a rule to the MAC group grp01 to ignore a device based on MAC address, but match all other
devices belonging to a MAC OUI:

Device discovery and configuration | 196

| switch(config)# | mac-group | grp01 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|                           |         | ignore mac     | 1a:2b:3c:4d:5e:6f |
| ------------------------- | ------- | -------------- | ----------------- |
| switch(config-mac-group)# |         | match mac-oui  | 1a:2b:3c          |
| switch(config-mac-group)# |         | exit           |                   |
| switch(config)#           | do show | running-config |                   |
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
| ssh server vrf |     |     |     |
| -------------- | --- | --- | --- |
!
!
!
!
!
vlan 1
| interface vlan | 1   |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |         |                   |     |
| --------------- | ------- | ----------------- | --- |
| seq 10 ignore   | mac     | 1a:2b:3c:4d:5e:6f |     |
| seq 20 match    | mac-oui | 1a:2b:3c          |     |
```
AddingaruletotheMACgroupgrp01toignoredevicesbasedonMACaddressmask,butmatchall
otherdevicesbelongingtoaMACOUI:
| switch(config)#           | mac-group | grp01           |                |
| ------------------------- | --------- | --------------- | -------------- |
| switch(config-mac-group)# |           | ignore mac-mask | 1a:2b:3c:4d/32 |
| switch(config-mac-group)# |           | match mac-oui   | 1a:2b:3c       |
switch(config-mac-group)#
exit
| switch(config)# | do show | running-config |     |
| --------------- | ------- | -------------- | --- |
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
| ssh server vrf |     |     |     |
| -------------- | --- | --- | --- |
!
!
!
!
!
vlan 1
| interface vlan | 1   |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |          |                |     |
| --------------- | -------- | -------------- | --- |
| seq 10 ignore   | mac-mask | 1a:2b:3c:4d/32 |     |
| seq 20 match    | mac-oui  | 1a:2b:3c       |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 197

```
AddingaruletotheMACgroupgrp01thatignoresadevicebasedoncompleteMACaddress:
| switch(config)#           | mac-group | grp01  |                       |
| ------------------------- | --------- | ------ | --------------------- |
| switch(config-mac-group)# |           | ignore | mac 1a:2b:3c:4d:5e:6f |
AddingaruletotheMACgroupgrp02thatignoresdevicesbasedonMACmask:
| switch(config)#           | mac-group | grp01  |                            |
| ------------------------- | --------- | ------ | -------------------------- |
| switch(config-mac-group)# |           | ignore | mac-mask 1a:2b:3c:4d:5e/40 |
| switch(config-mac-group)# |           | ignore | mac-mask 18:e3:ab:73/32    |
AddingaruletotheMACgroupgrp03thatignoresdevicesbasedonMACOUI:
| switch(config)#           | mac-group | grp03  |                  |
| ------------------------- | --------- | ------ | ---------------- |
| switch(config-mac-group)# |           | ignore | mac-oui 81:cd:93 |
AddingaruletotheMACgroupgrp01thatignoresdeviceswithasequencenumberandbasedonMAC
address:
| switch(config)#           | mac-group | grp01          |                              |
| ------------------------- | --------- | -------------- | ---------------------------- |
| switch(config-mac-group)# |           | seq 10         | ignore mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | exit           |                              |
| switch(config)#           | do show   | running-config |                              |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface vlan | 1   |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |     |     |
| --------------- | --------------------- | --- | --- |
| seq 10 ignore   | mac b2:c3:44:12:78:11 |     |     |
```
RemovingtherulefromtheMACgroupgrp01basedonsequencenumber:
| switch(config)#           | mac-group | grp01          |        |
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
Devicediscoveryandconfiguration|198

!
vlan 1
| interface vlan | 1   |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |
| --------------- | --- | --- | --- |
```
AddingaruletotheMACgroupgrp01thatignoresdeviceswithMACentrysequencenumberandbased
onMACOUI:
| switch(config)#           | mac-group | grp01         |                       |
| ------------------------- | --------- | ------------- | --------------------- |
| switch(config)#           | mac-group | grp01         |                       |
| switch(config-mac-group)# |           | seq 10 ignore | mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | seq 20 ignore | mac-oui 1a:2b:3c      |
switch(config-mac-group)#
|                           |     | seq 30 ignore | mac-mask 71:14:89:42/32 |
| ------------------------- | --- | ------------- | ----------------------- |
| switch(config-mac-group)# |     | exit          |                         |
switch(config)#
| switch(config)# | ^Z  |     |     |
| --------------- | --- | --- | --- |
switch#
switch#
| switch# show | running-config |     |     |
| ------------ | -------------- | --- | --- |
Current configuration:
!
| !Version AOS-CX   | PL.10.06.0002 |     |     |
| ----------------- | ------------- | --- | --- |
| !export-password: | default       |     |     |
!
!
!
!
| ssh server vrf | default |     |     |
| -------------- | ------- | --- | --- |
vlan 1
spanning-tree
| mac-group grp01 |          |                   |     |
| --------------- | -------- | ----------------- | --- |
| seq 10 ignore   | mac      | b2:c3:44:12:78:11 |     |
| seq 20 ignore   | mac-oui  | 1a:2b:3c          |     |
| seq 30 ignore   | mac-mask | 71:14:89:42/32    |     |
| interface 1/1/1 |          |                   |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/2 |     |     |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/3 |     |     |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/4 |     |     |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/5 |     |     |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/6 |     |     |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/7 |     |     |     |
no shutdown
| vlan access     | 1   |     |     |
| --------------- | --- | --- | --- |
| interface 1/1/8 |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 199

no shutdown
| vlan access     | 1   |     |     |     |
| --------------- | --- | --- | --- | --- |
| interface 1/1/9 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/10 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/11 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/12 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/13 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/14 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/15 |     |     |     |     |
no shutdown
| vlan access      | 1   |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/16 |     |     |     |     |
no shutdown
| vlan access    | 1   |     |     |     |
| -------------- | --- | --- | --- | --- |
| interface vlan | 1   |     |     |     |
ip dhcp
!
!
!
!
!
| https-server | vrf default |     |     |     |
| ------------ | ----------- | --- | --- | --- |
RemovingtherulefromtheMACgroupgrp01basedonsequencenumberandMACOUI:
| switch(config)#           | mac-group | grp01          |                   |          |
| ------------------------- | --------- | -------------- | ----------------- | -------- |
| switch(config-mac-group)# |           | no seq         | 20 ignore mac-oui | 1a:2b:3c |
| switch(config-mac-group)# |           | exit           |                   |          |
| switch(config)#           | do show   | running-config |                   |          |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------ | --- | --- | --- |
| !export-password: | default            |     |     |     |
| led locator on    |                    |     |     |     |
!
!
vlan 1
| interface vlan | 1   |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |          |                   |     |     |
| --------------- | -------- | ----------------- | --- | --- |
| seq 10 ignore   | mac      | b2:c3:44:12:78:11 |     |     |
| seq 30 ignore   | mac-mask | 71:14:89:f3/32    |     |     |
```
Removingtherulethatmatchesthesequencenumber25fromtheMACgroupnamedgrp01.
Devicediscoveryandconfiguration|200

| switch(config)# | mac-group |     | grp01 |
| --------------- | --------- | --- | ----- |
switch(config-mac-group)#
|                     |         |         | no ignore seq 25 |
| ------------------- | ------- | ------- | ---------------- |
| Command History     |         |         |                  |
| Release             |         |         | Modification     |
| 10.07orearlier      |         |         | --               |
| Command Information |         |         |                  |
| Platforms           | Command | context | Authority        |
4100i config-mac-group Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
mac-group
| mac-group <MAC-GROUP-NAME> |                  |     |     |
| -------------------------- | ---------------- | --- | --- |
| no mac-group               | <MAC-GROUP-NAME> |     |     |
Description
CreatesaMACgroupormodifiesanexistingMACgroup.AMACgroupisusedtoclassifyconnected
devicesbasedontheMACaddressdetails,suchasmaskorOUI.
Amaximumof32MACgroupscanbeconfiguredontheswitch.Amaximumof2MACgroupscanbe
associatedwithadeviceprofile.Eachgroupaccepts64matchorignorecommands.
ThenoformofthiscommandremovesaMACgroup.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MAC-GROUP-NAME> SpecifiesthenameoftheMACgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.
Examples
CreatingaMACgroupnamedgrp01:
| switch(config)#           | mac-group |     | grp01 |
| ------------------------- | --------- | --- | ----- |
| switch(config-mac-group)# |           |     | exit  |
RemovingaMACgroupnamedgrp01:
| switch(config)# | no  | mac-group | grp01        |
| --------------- | --- | --------- | ------------ |
| Command History |     |           |              |
| Release         |     |           | Modification |
| 10.07orearlier  |     |           | --           |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 201

| Command Information |         |         |     |           |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- |
| Platforms           | Command | context |     | Authority |     |     |
config
| 4100i |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |
| ----- | --- | --- | --- | -------------------------------------------------- | --- | --- |
| 6000  |     |     |     | rightsforthiscommand.                              |     |     |
6100
| match (for CDP | groups) |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- |
match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- |
no match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- |
Description
DefinesaruletomatchdevicesforaCDPgroup.Amaximumof32CDPgroupscanbeconfiguredon
theswitch.Upto64matchorignorerulescanbedefinedforeachgroup.
ThenoformofthiscommandremovesaruleforaddingdevicestoaCDPgroup.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
seq <SEQ-ID>
SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
platform <PLATFORM> Specifiesthehardwareormodeldetailsoftheneighbor.Range:1
to128alphanumericcharacters.
sw-version <SWVERSION> Specifiesthesoftwareversionoftheneighbor.Range:1to128
alphanumericcharacters.
| voice-vlan-query | <VLAN-ID> |     |     |     |     |     |
| ---------------- | --------- | --- | --- | --- | --- | --- |
SpecifiestheVLANqueryvalueoftheneighbor.Range:1to
65535.
Examples
AddingrulestomatchaCiscodevicewithaspecificsoftwareversiononVLAN512totheCDPgroup
grp01:
| switch(config)#           | port-access |     | cdp-group |                  | grp01     |     |
| ------------------------- | ----------- | --- | --------- | ---------------- | --------- | --- |
| switch(config-cdp-group)# |             |     | match     | platform         | CISCO     |     |
| switch(config-cdp-group)# |             |     | match     | sw-version       | 11.2(12)P |     |
| switch(config-cdp-group)# |             |     | match     | voice-vlan-query |           | 512 |
switch(config-cdp-group)# match seq 50 platform cisco sw-version 11.2(12)P voice-
| vlan-query                | 512 |                     |      |     |     |     |
| ------------------------- | --- | ------------------- | ---- | --- | --- | --- |
| switch(config-cdp-group)# |     |                     | exit |     |     |     |
| switch(config)#           | do  | show running-config |      |     |     |     |
| Current configuration:    |     |                     |      |     |     |     |
!
| !Version          | AOS-CX Virtual.10.0X.000 |     |     |     |     |     |
| ----------------- | ------------------------ | --- | --- | --- | --- | --- |
| !export-password: | default                  |     |     |     |     |     |
| led locator       | on                       |     |     |     |     |     |
!
Devicediscoveryandconfiguration|202

!
vlan 1
| port-access |     | cdp-group |                  | grp01     |     |     |
| ----------- | --- | --------- | ---------------- | --------- | --- | --- |
|             | seq | 10 match  | platform         | CISCO     |     |     |
|             | seq | 20 match  | sw-version       | 11.2(12)P |     |     |
|             | seq | 30 match  | voice-vlan-query |           | 512 |     |
seq 50 match platform cisco sw-version 11.2(12)P voice-vlan-query 512
Removingarulethatmatchesthesequencenumber25fromtheCDPgroupnamedgrp01:
| switch(config)#           |             |         | port-access | cdp-group |              | grp01 |
| ------------------------- | ----------- | ------- | ----------- | --------- | ------------ | ----- |
| switch(config-cdp-group)# |             |         |             | no match  | seq          | 25    |
| Command                   | History     |         |             |           |              |       |
| Release                   |             |         |             |           | Modification |       |
| 10.07orearlier            |             |         |             |           | --           |       |
| Command                   | Information |         |             |           |              |       |
| Platforms                 |             | Command |             | context   | Authority    |       |
4100i config-cdp-group Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------------- | --- |
6100
| match | (for LLDP | groups) |     |     |     |     |
| ----- | --------- | ------- | --- | --- | --- | --- |
match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
|     | vendor-oui | <VENDOR-OUI> |     | [type | <KEY> | [value <VALUE>]]} |
| --- | ---------- | ------------ | --- | ----- | ----- | ----------------- |
no match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
|     | vendor-oui | <VENDOR-OUI> |     | [type | <KEY> | [value <VALUE>]]} |
| --- | ---------- | ------------ | --- | ----- | ----- | ----------------- |
Description
DefinesaruletomatchdevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedfora
group.
Thenoformofthiscommandremovesarule.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).The
sys-descparameterbeconfiguredwithasubstringinsteadofa
completestringtomatch.Range:1to256alphanumeric
characters.
| sysname | <SYS-NAME> |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- |
SpecifiestheLLDPsystemnameTLV.Thesysnameparameterbe
configuredwithasubstringinsteadofacompletestringtomatch.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 203

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
Range:1to64alphanumericcharacters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY> |     | SpecifiesthevendorOUIsubtypekey. |     |     |
| ---------- | --- | -------------------------------- | --- | --- |
value <VALUE>
SpecifiesthevendorOUIsubtypevalue.Range:1to256
alphanumericcharacters.
Examples
AddingrulesthatmatchtheLLDPsystemdescriptionHPE_ANW-SwitchandsystemnameHPE_ANWto
theLLDPgroupnamedgrp01:
| switch(config)#            | port-access | lldp-group     | grp01          |     |
| -------------------------- | ----------- | -------------- | -------------- | --- |
| switch(config-lldp-group)# |             | match sys-desc | HPE_ANW-Switch |     |
| switch(config-lldp-group)# |             | match sysname  | HPE_ANW        |     |
switch(config)#
|                        | do show | running-config |     |     |
| ---------------------- | ------- | -------------- | --- | --- |
| Current configuration: |         |                |     |     |
!
| !Version          | AOS-CX Virtual.10.0X.000 |     |     |     |
| ----------------- | ------------------------ | --- | --- | --- |
| !export-password: | default                  |     |     |     |
| led locator       | on                       |     |     |     |
!
!
vlan 1
| port-access | lldp-group        | grp01          |     |     |
| ----------- | ----------------- | -------------- | --- | --- |
| seq         | 10 match sys-desc | HPE_ANW-Switch |     |     |
| seq         | 20 match sysname  | HPE_ANW        |     |     |
Removingarulethatmatchesthesequencenumber25fromanLLDPgroupnamedgrp01:
| switch(config)#            | port-access | lldp-group | grp01  |     |
| -------------------------- | ----------- | ---------- | ------ | --- |
| switch(config-lldp-group)# |             | no match   | seq 25 |     |
Addingarulethatmatchesthevalueofvendor-OUI000b86withtypeof1totheLLDPgroupnamed
grp01:
| switch(config)#            | port-access | lldp-group       | grp01       |     |
| -------------------------- | ----------- | ---------------- | ----------- | --- |
| switch(config-lldp-group)# |             | match vendor-oui | 000b86 type | 1   |
Addingarulethatmatchesthevalueofvendor-OUI000c34totheLLDPgroupnamedgrp01:
switch(config)#
|                            | port-access | lldp-group       | grp01  |     |
| -------------------------- | ----------- | ---------------- | ------ | --- |
| switch(config-lldp-group)# |             | match vendor-oui | 000c34 |     |
| Command History            |             |                  |        |     |
Devicediscoveryandconfiguration|204

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
4100i config-lldp-group Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
| match (for MAC | groups) |     |     |
| -------------- | ------- | --- | --- |
[seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
DefinesaruletomatchdevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddress
mask,orMACOrganizationalUniqueIdentifier(OUI).Upto64matchrulescanbedefinedforagroup.
YoumustnotconfigurethefollowingspecialMACaddresses:
n NullMAC—Forexample,00:00:00:00:00:00or00:00:00/32
n MulticastMAC
n BroadcastMAC—Forexample,ff:ff:ff:ff:ff:ff:ff
n SystemMAC
Althoughtheswitchacceptstheseaddresses,itwillnotprocesstheseaddressesforthelocalMACmatchfeature.
ThenoformofthiscommandremovesaruleforaddingdevicestoaMACgroup.
Thenumberofclientsthatcanonboardbasedonthematchcriteriaisconfiguredintheaaa
authentication port-access client-limitcommand.Forinformationaboutthiscommand,seethe
SecurityGuideforyourswitch.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
seq <SEQ-ID> SpecifiestheentrysequenceIDoftheruletocreateormodifya
MACgroup.IfnoIDisspecifiedwhenaddingarule,anIDis
automaticallyassignedinincrementsof10intheorderinwhich
rulesareadded.Whenmorethanonerulematchesthecommand
entered,therulewiththelowestIDtakesprecedence.Range:1to
4294967295.
| mac <MAC-ADDR> |     |     | SpecifiestheMACaddressofthedevice. |
| -------------- | --- | --- | ---------------------------------- |
mac-mask <MAC-MASK> SpecifiestheMACaddressmasktoadddevicesinthatrange.
SupportedMACaddressmasks:/32and/40.
mac-oui <MAC-OUI> SpecifiestheMACOUItoadddevicesinthatrange.SupportsMAC
OUIaddressofmaximumlengthof24bits.
Examples
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 205

AddingadevicetotheMACgroupgrp01basedoncompleteMACaddress:
| switch(config)#           | mac-group | grp01     |                   |
| ------------------------- | --------- | --------- | ----------------- |
| switch(config-mac-group)# |           | match mac | 1a:2b:3c:4d:5e:6f |
| switch(config-mac-group)# |           | exit      |                   |
AddingdevicestotheMACgroupgrp02basedonMACmask:
| switch(config)# | mac-group | grp01 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|                           |     | match mac-mask | 1a:2b:3c:4d:5e/40 |
| ------------------------- | --- | -------------- | ----------------- |
| switch(config-mac-group)# |     | match mac-mask | 18:e3:ab:73/32    |
| switch(config-mac-group)# |     | exit           |                   |
AddingdevicestotheMACgroupgrp03basedonMACOUI:
| switch(config)#           | mac-group | grp03         |          |
| ------------------------- | --------- | ------------- | -------- |
| switch(config-mac-group)# |           | match mac-oui | 81:cd:93 |
| switch(config-mac-group)# |           | exit          |          |
AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress:
switch(config)#
|                           | mac-group | grp01          |                             |
| ------------------------- | --------- | -------------- | --------------------------- |
| switch(config-mac-group)# |           | seq 10         | match mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | exit           |                             |
| switch(config)#           | do show   | running-config |                             |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------ | --- | --- |
| !export-password: | default            |     |     |
| led locator on    |                    |     |     |
!
!
vlan 1
| interface vlan | 1   |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |     |     |
| --------------- | --------------------- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |     |     |
```
RemovingdevicesfromtheMACgroupgrp01basedonsequencenumber:
| switch(config)#           | mac-group | grp01          |        |
| ------------------------- | --------- | -------------- | ------ |
| switch(config-mac-group)# |           | no match       | seq 10 |
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
Devicediscoveryandconfiguration|206

| interface vlan | 1   |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |     |
| --------------- | --- | --- | --- | --- |
```
AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress,
MACaddressmask,andMACOUI:
| switch(config)#           | mac-group | grp01          |                             |                |
| ------------------------- | --------- | -------------- | --------------------------- | -------------- |
| switch(config-mac-group)# |           | seq 10         | match mac b2:c3:44:12:78:11 |                |
| switch(config-mac-group)# |           | seq 20         | match mac-oui               | 1a:2b:3c       |
| switch(config-mac-group)# |           | seq 30         | match mac-mask              | 71:14:89:f3/32 |
| switch(config-mac-group)# |           | exit           |                             |                |
| switch(config)#           | do show   | running-config |                             |                |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------ | --- | --- | --- |
| !export-password: | default            |     |     |     |
| led locator on    |                    |     |     |     |
!
!
vlan 1
| interface vlan | 1   |     |     |     |
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
| switch(config)# | mac-group | grp01 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-mac-group)#
|                           |         | no seq         | 20 match mac-oui | 1a:2b:3c |
| ------------------------- | ------- | -------------- | ---------------- | -------- |
| switch(config-mac-group)# |         | exit           |                  |          |
| switch(config)#           | do show | running-config |                  |          |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------ | --- | --- | --- |
| !export-password: | default            |     |     |     |
| led locator on    |                    |     |     |     |
!
!
vlan 1
| interface vlan | 1   |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |                |     |     |
| --------------- | --------------------- | -------------- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |                |     |     |
| seq 30 match    | mac-mask              | 71:14:89:f3/32 |     |     |
```
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 207

AddingdevicestotheMACgroupgrp03withMACentrysequencenumberandbasedonMACaddress
mask:
| switch(config)# | mac-group | grp03 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)# seq 10 match mac-mask 10:14:a3:b7:55/40
| switch(config-mac-group)# |     | exit                |     |
| ------------------------- | --- | ------------------- | --- |
| switch(config)#           | do  | show running-config |     |
| Current configuration:    |     |                     |     |
!
| !Version          | AOS-CX Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------------- | --- | --- |
| !export-password: | default                   |     |     |
| led locator       | on                        |     |     |
!
!
vlan 1
| interface   | vlan 1            |                   |     |
| ----------- | ----------------- | ----------------- | --- |
| no shutdown |                   |                   |     |
| ip dhcp     |                   |                   |     |
| mac-group   | grp03             |                   |     |
| seq         | 10 match mac-mask | 10:14:a3:b7:55/40 |     |
```
RemovingdevicesfromtheMACgroupgrp03basedonMACaddressmask:
| switch(config)# | mac-group | grp03 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)# no seq 10 match mac-mask 10:14:a3:b7:55/40
| switch(config-mac-group)# |     | exit                |     |
| ------------------------- | --- | ------------------- | --- |
| switch(config)#           | do  | show running-config |     |
| Current configuration:    |     |                     |     |
!
| !Version          | AOS-CX Virtual.10.0X.0001 |     |     |
| ----------------- | ------------------------- | --- | --- |
| !export-password: | default                   |     |     |
| led locator       | on                        |     |     |
!
!
vlan 1
| interface   | vlan 1 |     |     |
| ----------- | ------ | --- | --- |
| no shutdown |        |     |     |
| ip dhcp     |        |     |     |
| mac-group   | grp03  |     |     |
```
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
4100i config-mac-group Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
Devicediscoveryandconfiguration|208

| port-access    |     | cdp-group |                  |     |     |     |     |     |
| -------------- | --- | --------- | ---------------- | --- | --- | --- | --- | --- |
| port-access    |     | cdp-group | <CDP-GROUP-NAME> |     |     |     |     |     |
| no port-access |     | cdp-group | <CDP-GROUP-NAME> |     |     |     |     |     |
Description
CreatesaCDP(CiscoDiscoveryProtocol)groupormodifiesanexistingCDPgroup.ACDPGroupisused
toclassifyconnecteddevicesbasedontheCDPpacketdetailsadvertisedbythedevice.Amaximumof
32CDPgroupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesaCDPgroup.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<CDP-GROUP-NAME>
SpecifiesthenameoftheCDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatingaCDPgroupnamedgrp01:
switch(config)#
|                           |     |     | port-access |       | cdp-group        | grp01 |           |     |
| ------------------------- | --- | --- | ----------- | ----- | ---------------- | ----- | --------- | --- |
| switch(config-cdp-group)# |     |     |             | match | platform         |       | CISCO     |     |
| switch(config-cdp-group)# |     |     |             | match | sw-version       |       | 11.2(12)P |     |
| switch(config-cdp-group)# |     |     |             | match | voice-vlan-query |       |           | 512 |
switch(config-cdp-group)# seq 50 match platform cisco sw-version 11.2(12)P voice-
| vlan-query                |     | 512            |         |                |     |     |     |     |
| ------------------------- | --- | -------------- | ------- | -------------- | --- | --- | --- | --- |
| switch(config-cdp-group)# |     |                |         | exit           |     |     |     |     |
| switch(config)#           |     |                | do show | running-config |     |     |     |     |
| Current                   |     | configuration: |         |                |     |     |     |     |
!
| !Version          |         | AOS-CX | Virtual.10.0X.000 |     |     |     |     |     |
| ----------------- | ------- | ------ | ----------------- | --- | --- | --- | --- | --- |
| !export-password: |         |        | default           |     |     |     |     |     |
| led               | locator | on     |                   |     |     |     |     |     |
!
!
| vlan        | 1   |           |                  |       |           |     |     |     |
| ----------- | --- | --------- | ---------------- | ----- | --------- | --- | --- | --- |
| port-access |     | cdp-group | grp01            |       |           |     |     |     |
|             | seq | 10 match  | platform         | CISCO |           |     |     |     |
|             | seq | 20 match  | sw-version       |       | 11.2(12)P |     |     |     |
|             | seq | 30 match  | voice-vlan-query |       |           | 512 |     |     |
seq 50 match platform cisco sw-version 11.2(12)P voice-vlan-query 512
RemovingaCDPgroupnamedgrp01:
| switch(config)# |             |     | no port-access |     | cdp-group    |     | grp01 |     |
| --------------- | ----------- | --- | -------------- | --- | ------------ | --- | ----- | --- |
| Command         | History     |     |                |     |              |     |       |     |
| Release         |             |     |                |     | Modification |     |       |     |
| 10.07orearlier  |             |     |                |     | --           |     |       |     |
| Command         | Information |     |                |     |              |     |       |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 209

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
4100i config Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------------- | --- |
6100
| port-access    |     | device-profile |     |                       |     |     |
| -------------- | --- | -------------- | --- | --------------------- | --- | --- |
| port-access    |     | device-profile |     | <DEVICE-PROFILE-NAME> |     |     |
| no port-access |     | device-profile |     | <DEVICE-PROFILE-NAME> |     |     |
Description
Createsanewdeviceprofileandswitchestotheconfig-device-profilecontext.Amaximumof32
deviceprofilescanbecreated.Thiscommandcanbeissuedfromtheinterface(config-if)orLink
AggregationGroup(config-lag-if)contexts.
Thenoformofthiscommandremovesadeviceprofile.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DEVICE-PROFILE-NAME> Specifiesthenameofadeviceprofile.Range:1to32
alphanumericcharacters.
Usage
Whenmultipledeviceprofilesarecreatedontheswitchusingtheport-access device-profile <device-
profile-name>command,theswitchgoesthroughthelistofdeviceprofilesnamesinalphabetical
ordertofindthedeviceprofiletoassociatetoaclient.Forexample,iftheswitchhadthefollowing
configuration:
| port-access |           | device-profile |     | Switch |     |     |
| ----------- | --------- | -------------- | --- | ------ | --- | --- |
|             | associate | lldp-group     |     | lldp1  |     |     |
| port-access |           | device-profile |     | AP     |     |     |
|             | associate | lldp-group     |     | lldp1  |     |     |
TheorderoftheattemptedmatchwouldbedeviceprofileAP,andthendeviceprofileSwitch.
Examples
Creatingadeviceprofilenamedprofile01:
| switch(config)# |     | port-access |     | device-profile |     | profile01 |
| --------------- | --- | ----------- | --- | -------------- | --- | --------- |
switch(config-device-profile)#
Removingadeviceprofilenamedprofile01:
| switch(config)# |     | no  | port-access |     | device-profile | profile01 |
| --------------- | --- | --- | ----------- | --- | -------------- | --------- |
Creatingadeviceprofilenamedprofile02onaLAGport:
| switch(config)#interface |     |     |     | lag 1 |     |     |
| ------------------------ | --- | --- | --- | ----- | --- | --- |
Devicediscoveryandconfiguration|210

| switch(config-lag-if)# |     |     | port-access | device-profile | profile01 |
| ---------------------- | --- | --- | ----------- | -------------- | --------- |
switch(config-device-profile)#
| Command | History |     |     |                                                      |     |
| ------- | ------- | --- | --- | ---------------------------------------------------- | --- |
| Release |         |     |     | Modification                                         |     |
| 10.13   |         |     |     | ThiscommandcanbeissuedfromaLinkAggregationGroup(LAG) |     |
context.
| 10.07orearlier |             |     |         | --        |     |
| -------------- | ----------- | --- | ------- | --------- | --- |
| Command        | Information |     |         |           |     |
| Platforms      | Command     |     | context | Authority |     |
config
| 4100i       |                |     |      | Administratorsorlocalusergroupmemberswithexecution |     |
| ----------- | -------------- | --- | ---- | -------------------------------------------------- | --- |
| 6000        | config-if      |     |      | rightsforthiscommand.                              |     |
| 6100        | config-lag-if  |     |      |                                                    |     |
| port-access | device-profile |     | mode | block-until-profile-applied                        |     |
Youmustconfigurethismodeindeviceprofileonlyonstandaloneportswherethereisnosecurityconfigured
andwhenyounotwanttheporttobeofflineuntiloneclientisonboarded.
| port-access    | device-profile |     | mode | block-until-profile-applied |     |
| -------------- | -------------- | --- | ---- | --------------------------- | --- |
| no port-access | device-profile |     | mode | block-until-profile-applied |     |
Description
Configurestheswitchtoblocktheportuntilaprofilematchoccursforadevice.Thisconfigurationis
requiredwhennosecurityfeatureisenabledontheport.
YoumustenablethismodeorsecurityontheportforlocalMACmatchfeaturetooperate.Youmust
notenablebothfeaturesonthesameportatthesametime.
YoumustnotcombineanyotherAAAconfigurationswiththeblock-until-profile-appliedmode.
Thiscommandcanbeissuedfromtheinterface(config-if)orLinkAggregationGroup(config-lag-if)
contexts. ThenoformofthiscommandremovesaruleforaddingdevicestoaMACgroup.
Example
Configuringblock-until-profileappliedmodeonport1/1/1:
| switch(config)#    |     | interface | 1/1/1       |                |     |
| ------------------ | --- | --------- | ----------- | -------------- | --- |
| switch(config-if)# |     |           | port-access | device-profile |     |
switch(config-if-deviceprofile)# mode block-until-profile-applied
| switch(config-if-deviceprofile)# |         |     |     | end |     |
| -------------------------------- | ------- | --- | --- | --- | --- |
| Command                          | History |     |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 211

| Release |     |     |     | Modification                                         |     |
| ------- | --- | --- | --- | ---------------------------------------------------- | --- |
| 10.13   |     |     |     | ThiscommandcanbeissuedfromaLinkAggregationGroup(LAG) |     |
context.
| 10.07orearlier |             |     |         | --  |           |
| -------------- | ----------- | --- | ------- | --- | --------- |
| Command        | Information |     |         |     |           |
| Platforms      | Command     |     | context |     | Authority |
config-if
| 4100i          |                         |     |                   |     | Administratorsorlocalusergroupmemberswith |
| -------------- | ----------------------- | --- | ----------------- | --- | ----------------------------------------- |
| 6000           | config-if-deviceprofile |     |                   |     | executionrightsforthiscommand.            |
| 6100           | config-lag-if           |     |                   |     |                                           |
| port-access    | lldp-group              |     |                   |     |                                           |
| port-access    | lldp-group              |     | <LLDP-GROUP-NAME> |     |                                           |
| no port-access | lldp-group              |     | <LLDP-GROUP-NAME> |     |                                           |
Description
CreatesanLLDPgroupormodifiesanexistingLLDPgroup.AnLLDPgroupisusedtoclassifyconnected
devicesbasedontheLLDPtype-length-values(TLVs)advertisedbythedevice.Amaximumof32LLDP
groupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesanLLDPgroup.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<LLDP-GROUP-NAME> SpecifiesthenameoftheLLDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatinganLLDPgroupnamedgrp01:
| switch(config)# |     | port-access |     | lldp-group | grp01 |
| --------------- | --- | ----------- | --- | ---------- | ----- |
switch(config-lldp-group)#
RemovinganLLDPgroupnamedgrp01:
| switch(config)# |             | no  | port-access | lldp-group   | grp01 |
| --------------- | ----------- | --- | ----------- | ------------ | ----- |
| Command         | History     |     |             |              |       |
| Release         |             |     |             | Modification |       |
| 10.07orearlier  |             |     |             | --           |       |
| Command         | Information |     |             |              |       |
Devicediscoveryandconfiguration|212

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
| show port-access | device-profile |     |     |
| ---------------- | -------------- | --- | --- |
show port-access device-profile [[interface {all | <INTERFACE-ID>}
| [client-status | <MAC-ADDR>]] | |   | name <DEVICE-PROFILE-NAME>] |
| -------------- | ------------ | --- | --------------------------- |
Description
ShowstheclientstatusforaspecificMACaddressorprofilename.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
interface {all | <INTERFACE-ID>} Selectallforallinterfacesorspecifythenameofaninterfacein
theformat:member/slot/port.
client-status <MAC-ADDR> SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.
name <DEVICE-PROFILE-NAME>
Specifiesthenameofthedeviceprofile.
Examples
Showingtheappliedstateofthedeviceprofiles:
switch#
| show       | port-access | device-profile                     |     |
| ---------- | ----------- | ---------------------------------- | --- |
| Profile    | Name        | : accesspoints                     |     |
| LLDP       | Groups      | : 2920-grp                         |     |
| CDP Groups |             | :                                  |     |
| MAC Groups |             | : 2920-mac-grp1,2920-iot-grp2      |     |
| Role       |             | : local_role_1                     |     |
| State      |             | : Enabled                          |     |
| Profile    | Name        | : access_switches                  |     |
| LLDP       | Groups      | : 2920-grp                         |     |
| CDP Groups |             | :                                  |     |
| MAC Groups |             | :                                  |     |
| Role       |             | : local_2920_role                  |     |
| State      |             | : Enabled                          |     |
| Profile    | Name        | : iot_devices                      |     |
| LLDP       | Groups      | :                                  |     |
| CDP Groups |             | :                                  |     |
| MAC Groups |             | : iot_camera-grp1,iot_sensors-grp1 |     |
| Role       |             | : local_2920_role                  |     |
| State      |             | : Enabled                          |     |
| Profile    | Name        | : lobbyaps                         |     |
| LLDP       | Groups      | :                                  |     |
| CDP Groups |             | : lobby_ap_cdp_grp                 |     |
| MAC Groups |             | :                                  |     |
| Role       |             | : test_ap_role                     |     |
| State      |             | : Disabled                         |     |
Showingtheappliedstateofthedeviceprofileoninterface1/1/3:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 213

switch# show port-access device-profile interface 1/1/3 client-status
00:0c:29:9e:d1:20
| Port | 1/1/3,    | Neighbor-Mac |     | 00:0c:29:9e:d1:20 |          |           |      |
| ---- | --------- | ------------ | --- | ----------------- | -------- | --------- | ---- |
|      | Profile   | Name         | :   | lobbyaps          |          |           |      |
|      | LLDP      | Group        | :   |                   |          |           |      |
|      | CDP Group |              | :   | hpe-anw-ap_cdp    |          |           |      |
|      | MAC Group |              | :   |                   |          |           |      |
|      | Role      |              | :   | test_ap_role      |          |           |      |
|      | Status    |              | :   | Failed            |          |           |      |
|      | Failure   | Reason       | :   | Failed            | to apply | MAC based | VLAN |
Showingtheappliedstateofaspecificdeviceprofile:
| switch#        | show        | port-access |     | device-profile |                  | name | lldp-group |
| -------------- | ----------- | ----------- | --- | -------------- | ---------------- | ---- | ---------- |
|                | Profile     | Name        |     | :              | lldp-group       |      |            |
|                | LLDP        | Groups      |     | :              |                  |      |            |
|                | CDP Groups  |             |     | :              |                  |      |            |
|                | MAC Groups  |             |     | :              | pc-behind-phone, |      | lldp       |
|                | Role        |             |     | :              | auth_role        |      |            |
|                | State       |             |     | :              | Enabled          |      |            |
| Command        | History     |             |     |                |                  |      |            |
| Release        |             |             |     |                | Modification     |      |            |
| 10.07orearlier |             |             |     |                | --               |      |            |
| Command        | Information |             |     |                |                  |      |            |
| Platforms      |             | Command     |     | context        | Authority        |      |            |
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------------- | --- | --- |
6100
LLDP
TheIEEE802.1ABLinkLayerDiscoveryProtocol(LLDP)providesastandards-basedmethodfornetwork
devicestodiscovereachotherandexchangeinformationabouttheircapabilities.AnLLDPdevice
advertisesitselftoadjacent(neighbor)devicesbytransmittingLLDPdatapacketsonallinterfaceson
whichoutboundLLDPisenabled,andreadingLLDPadvertisementsfromneighbordevicesonportson
whichinboundLLDPisenabled.InboundpacketsfromneighbordevicesarestoredinaspecialLLDP
MIB(managementinformationbase).Thisinformationcanthenbequeriedbyotherdevicesthrough
SNMP.
LLDPinformationisusedbynetworkmanagementtoolstocreateaccuratephysicalnetworktopologies
bydeterminingwhichdevicesareneighborsandthroughwhichinterfacestheyconnect.LLDPoperates
atlayer2andrequiresanLLDPagenttobeactiveoneachinterfacethatsendsandreceivesLLDP
advertisements.LLDPadvertisementscancontainavariablenumberofTLV(type,length,value)
informationelements.EachTLVdescribesasingleattributeofadevicesuchas:systemcapabilities,
managementIPaddress,deviceID,portID.
Devicediscoveryandconfiguration|214

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

When you enable LLDP on the switch, it is automatically enabled on all data plane interfaces. You can
customize this behavior by manually enabling/disabling support on each interface.

Supported standards

The LLDP agent supports the following standards: IEEE 802.1AB-2005, Station, and Media Access Control
Connectivity Discovery.

Supported interfaces

LLDP is supported on interfaces mapped to a physical port. It is not supported on logical interfaces,
such as loopback, tunnels, and SVIs.

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

215

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

Device discovery and configuration | 216

n Chassis-ID: Base MAC address of the switch.

n Port-ID: Port number of the physical port.

n Time-to-Live (TTL): Length of time an LLDP neighbor retains advertised data before discarding it.

n System capabilities: Identifies the primary switch capabilities (bridge, router). Identifies the primary

switch functions that are enabled, such as routing.

n System description: Includes switch model name and running software version, and ROM version.

n System name: Name assigned to the switch.

n Management address: Default address selection method unless an optional address is configured.

n Port description: Physical port identifier.

n Port VLAN ID: On an L2 port, contains access or native VLAN ID. Trunk allowed VLANs information are

not advertised as part of the Port VLAN ID TLV.

n Port VLAN Name: Access or native VLAN name. Enabled by default.

n Port MFS: Maximum Frame Size. Enabled by default.

LLDP MED support

LLDP-MED interoperates with directly connected IP telephony (endpoint) clients and provides the
following features:

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

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

217

1. By default, the LLDP agent is enabled on all active interfaces. If LLDP was disabled, enable it with

the command lldp.

2. By default, the LLDP agent transmits and receive on all interfaces. To customize LLDP behavior on

a specific interface, use the commands lldp transmit and lldp receive.

3. By default, the LLDP agent sets the management address in all TLVs in the following order:

a. LLDP management IP address.
b. SVI.
c. Base MAC.

4. By default, all supported TLVs are sent and received. To customize the list, use the command

lldp select-tlv.

5. By default, support for the LLDP-MED TLV is enabled. To customize settings, use the commands

lldp med and lldp med-location.

6.

If required, adjust LLDP timer, holdtime, reinitialization delay, and transmit delay from their
default values with the commands lldp timer, lldp holdtime, lldp reinit, and lldp txdelay.

Example

This example creates the following configuration:

n Enables LLDP support.

n Disables LLDP transmission on interface 1/1/1.

switch(config)# lldp
switch(config)# interface 1/1/1
switch(config-copp)# no lldp transmit

LLDP commands

clear lldp neighbors

clear lldp neighbors

Description

Clears all LLDP neighbor details.

Examples

Clearing all LLDP neighbor details:

switch# clear lldp neighbors

Command History

Release

10.07 or earlier

Command Information

Modification

--

Device discovery and configuration | 218

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| switch(config)# | no  | lldp |     |
| --------------- | --- | ---- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 219

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp dot3
| lldp dot3 {poe | | macphy} |         |     |
| -------------- | --------- | ------- | --- |
| no lldp dot3   | {poe |    | macphy} |     |
Description
Setsthe802.3TLVstobeadvertised.Bydefault,advertisementofbothPOEandMAC/PHYTLVsis
enabled.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     |     | Description                                       |
| --------- | --- | --- | ------------------------------------------------- |
| poe       |     |     | SpecifiesadvertisementofpoweroverEthernetdatalink |
classification.
| macphy |     |     | Specifiesadvertisementofmediaaccesscontrolandphysical |
| ------ | --- | --- | ----------------------------------------------------- |
layerinformation.
Examples
EnablingadvertisementofthePOETLV:
| switch(config-if)# |     | lldp dot3 | poe |
| ------------------ | --- | --------- | --- |
DisablingadvertisementofthePOETLV:
| switch(config-if)#  |     | no lldp | dot3 poe     |
| ------------------- | --- | ------- | ------------ |
| Command History     |     |         |              |
| Release             |     |         | Modification |
| 10.07orearlier      |     |         | --           |
| Command Information |     |         |              |
Devicediscoveryandconfiguration|220

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp dot3 eee |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 eee |     |     |     |
| no lldp dot3  | eee |     |     |
Description
Setsthe802.3TLVsforEnergy-EfficientEthernet(EEE) tobeadvertised.Bydefault,advertisementofEEE
TLVsisenabled.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     |     | Description                              |
| --------- | --- | --- | ---------------------------------------- |
| eee       |     |     | Specifiesadvertisementof802.3TLVsforEEE. |
Examples
EnablingadvertisementoftheEEETLVs:
| switch(config-if)# |     | lldp dot3 eee |     |
| ------------------ | --- | ------------- | --- |
DisablingadvertisementoftheEEETLVs:
switch(config-if)#
|                     |         | no lldp dot3 | eee          |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
4100i config-if Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
| lldp dot3 mfs |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 mfs |     |     |     |
| no lldp dot3  | mfs |     |     |
Description
Enablesthe802.3TLVlistinLLDP toadvertiseformaximumframesize(MFS).Enabledbydefault.
ThenoformofthiscommanddisablestheadvertisementofmaximumframesizeTLVs.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 221

Examples
EnablingadvertisementofmaximumframesizeTLVs:
| switch(config)#    |     | interface | 1/1/1 |     |
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
<multiplier>
SpecifiestheTTLmultiplierintherangeof2to10.Default:4.
Formula
TTL=Holdtime-multiplierxlldptimer
where:
TTL=Time-to-Live
Holdtime-multiplier=Multiplyingholdtimevalue
Devicediscoveryandconfiguration|222

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp management-address    |     | vlan           |     |
| -------------------------- | --- | -------------- | --- |
| lldp management-address    |     | vlan <VLAN-ID> |     |
| no lldp management-address |     | vlan <VLAN-ID> |     |
Description
SetstheVLANwhoseIPv4orIPv6addressisadvertisedastheLLDPmanagementauthority.
ThenoformofthiscommandremovestheVLANwhoseIPv4orIPv6addressisadvertisedastheLLDP
managementauthority.
ThefollowingistheprecedenceforthemanagementIPaddressTLVintheLLDPpacket(inorder):
LLDPmanagement-IP-addressandmanagement-ipv6-address,ifconfigured.
n
n LLDPmanagementVLAN'sIPv4andIPv6address,ifconfigured.
n LoopbackIPaddressfromthesmallestconfiguredloopbackinterfaceidentifier.
n Route-only-portIP address(Layer-3interface)orIPaddressoftheSVI(Layer-2interface).
n OOBMIPaddress.
n BaseMACaddressoftheswitch.
| Parameter |     |     | Description         |
| --------- | --- | --- | ------------------- |
| <VLAN-ID> |     |     | SpecifiestheVLANID. |
Examples
SettingthemanagementauthorityforVLAN10:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 223

| switch(config)# | lldp | management-address |     | vlan 10 |
| --------------- | ---- | ------------------ | --- | ------- |
RemovingthemanagementauthorityforVLAN10:
| switch(config)#     | no      | lldp management-address |                    | vlan 10 |
| ------------------- | ------- | ----------------------- | ------------------ | ------- |
| Command History     |         |                         |                    |         |
| Release             |         |                         | Modification       |         |
| 10.12               |         |                         | Commandintroduced. |         |
| Command Information |         |                         |                    |         |
| Platforms           | Command | context                 | Authority          |         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp management-ip-address
| lldp management-ip-address |     | <IPV-ADDR> |     |     |
| -------------------------- | --- | ---------- | --- | --- |
no lldp management-ip-address
Description
DefinestheIPmanagementaddressoftheswitchwhichissentinthemanagementaddressTLV.One
IPv4andoneIPv6managementaddresscanbeconfigured.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
n IPaddressofSVI[interfaceVLAN<vid>]
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv4managementaddressoftheswitch.
| Parameter   |     |     | Description                                      |     |
| ----------- | --- | --- | ------------------------------------------------ | --- |
| <IPV4-ADDR> |     |     | SpecifiesthemanagementaddressoftheswitchasanIPv4 |     |
format(x.x.x.x),wherexisadecimalvaluefrom0to255.
Examples
Settingthemanagementaddressto10.10.10.2:
| switch(config)# | lldp | management-ip-address |     | 10.10.10.2 |
| --------------- | ---- | --------------------- | --- | ---------- |
Removingthemanagementaddress:
| switch(config)# | no  | lldp management-ip-address |     |     |
| --------------- | --- | -------------------------- | --- | --- |
| Command History |     |                            |     |     |
Devicediscoveryandconfiguration|224

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
IPaddressofSVI[interfaceVLAN<vid>]
n
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
switch(config)#
|                     | no  | lldp management-ipv6-address |              |
| ------------------- | --- | ---------------------------- | ------------ |
| Command History     |     |                              |              |
| Release             |     |                              | Modification |
| 10.07orearlier      |     |                              | --           |
| Command Information |     |                              |              |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 225

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
poe [priority-override] SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
dot3poeandlldpmedpoeareenabled,thelldpdot3poe3
settingtakesprecedence.Default:enabled.
capability
SpecifiesadvertisementofsupportedLLDPMEDTLVs.The
capabilityTLVisalwayssentwithotherMEDTLVs,thereforeit
cannotbedisabledwhenotherMEDTLVsareenabled.Default:
enabled.
network-policy Networkpolicydiscoveryletsendpointsandnetworkdevices
advertisetheirVLANIDs,andIEEE802.1p(PCPandDSCP)values
forvoiceapplications.ThisTLVisonlysentwhenavoiceVLAN
policyispresent.Default:enabled.
Examples
EnablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |     | lldp med | network-policy |     |
| ------------------ | --- | -------- | -------------- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |             | no lldp | med network-policy |     |
| ------------------ | ----------- | ------- | ------------------ | --- |
| Command            | History     |         |                    |     |
| Release            |             |         | Modification       |     |
| 10.07orearlier     |             |         | --                 |     |
| Command            | Information |         |                    |     |
Devicediscoveryandconfiguration|226

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

nCA-TYPE: This is the first entry in a type/value pair and is a number defining the type of data contained in
the second entry in the type/value pair (CA-VALUE.) Some examples of CA-TYPE specifiers include: 3=city
6=street (name) 25=building name (Range: 0 - 255)

nCA-VALUE: This is the second entry in a type/value pair and is an alphanumeric string containing the
location information corresponding to the immediately preceding CA-TYPE entry. Strings are delimited by
either blank spaces, single quotes (' … '), or double quotes ("… ".) Each string should represent a specific
data type in a set of unique type/value pairs comprising the description of a location, and each string
must be preceded by a CA-TYPE number identifying the type of data in the string.

The following LLDP-MED TLV values are supported. For details on these value types, refer to RFC 4776

n 1: national subdivisions (state, canton, region, province, prefecture)

n 2: county, parish, gun (JP), district (IN)

n 3: city, township, shi (JP)

n 4: city division, borough, city district, ward, chou (JP)

n 5: neighborhood, block

n 6: group of streets below the neighborhood level

n 16: leading street direction N

n 17: trailing street suffix SW

n 18: street suffix or type

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

227

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

Release

10.07 or earlier

Command Information

Modification

--

Device discovery and configuration | 228

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp receive
lldp receive
no lldp receive
Description
EnablesreceptionofLLDPinformationonaninterface.Bydefault,LLDPreceptionisenabledonall
activeinterfaces.
ThenoformofthiscommanddisablesreceptionofLLDPinformationonaninterface.
Examples
EnablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1        |     |
| ------------------ | --------- | ------------ | --- |
| switch(config-if)# |           | lldp receive |     |
DisablingLLDPreceptiononinterface1/1/1:
| switch(config)#     | interface | 1/1/1           |              |
| ------------------- | --------- | --------------- | ------------ |
| switch(config-if)#  |           | no lldp receive |              |
| Command History     |           |                 |              |
| Release             |           |                 | Modification |
| 10.07orearlier      |           |                 | --           |
| Command Information |           |                 |              |
| Platforms           | Command   | context         | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp reinit
| lldp reinit | <TIME> |     |     |
| ----------- | ------ | --- | --- |
no lldp reinit
Description
Setstheamountoftime(inseconds)towaitbeforeperformingLLDPinitializationonaninterface.
Thenoformofthiscommandsetsthereinitializationtimetoitsdefaultvalueof2seconds.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 229

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<TIME> Specifiesthereinitializationtimeinseconds.Range:1to10.
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
LLDPsupportsOrganizationUniqueIdentifiers(OUIs)withthefollowingOrganization-specificTLVs:
n IEEE802.1(DOT1)(oui:0x00,0x80,0xc2)
IEEE802.3(DOT3)(oui:0x00,0x12,0x0f)
n
n HPE ArubaNetworking(oui:0x88,0x3a,0x30)
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
select-tlv <TLV-NAME> SpecifiestheTLVnametosend.ThefollowingTLVnamesare
supported:
Devicediscoveryandconfiguration|230

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
management-address: Selectionisbasedonpriority
n
inthefollowinglist(forexampleiffirstTLVnameisn't
selected,thenextwillbe,progressingthroughthis
listuntilaselectionismade):
1. IPv4orIPV6managementaddress.
2. Iflayer2,theIPaddressoftheSVI.
3. BaseMACaddressoftheswitch.
n port-description: Selectport-descriptionTLV.
n port-vlan-id: Selectport-vlan-idTLV.
n port-vlan-name: Selectport-vlan-nameTLV.
n system-capabilities: Selectsystem-capabilitiesTLV.
n system-description: Selectsystem-descriptionTLV.
n system-name: Selectsystem-nameTLV.
Examples
StoppingtheLLDPagentfromsendingtheport-descriptionTLV:
| switch(config)# | no  | lldp select-tlv | port-description |
| --------------- | --- | --------------- | ---------------- |
EnablingtheLLDPagenttosendtheport-descriptionTLV:
| switch(config)#     | lldp    | select-tlv | oui          |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 231

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

Description

Specifies the update interval (in seconds). Range: 5 to 32768.
Default: 30.

Setting the update interval to 7 seconds:

switch(config)# lldp timer 7

Setting the update interval to the default value of 30 seconds:

switch(config)# no lldp timer

Command History

Release

10.07 or earlier

Command Information

Modification

--

Device discovery and configuration | 232

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp transmit
lldp transmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionisenabled
onallactiveinterfaces.
ThenoformofthiscommanddisablestransmissionofLLDPinformationonaninterface.
Examples
EnablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1         |     |
| ------------------ | --------- | ------------- | --- |
| switch(config-if)# |           | lldp transmit |     |
DisablingLLDPtransmissiononinterface1/1/1:
| switch(config)#     | interface | 1/1/1            |              |
| ------------------- | --------- | ---------------- | ------------ |
| switch(config-if)#  |           | no lldp transmit |              |
| Command History     |           |                  |              |
| Release             |           |                  | Modification |
| 10.07orearlier      |           |                  | --           |
| Command Information |           |                  |              |
| Platforms           | Command   | context          | Authority    |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 233

| Parameter |     |     | Description                                           |
| --------- | --- | --- | ----------------------------------------------------- |
| <TIME>    |     |     | Specifiesthedelaytimeinseconds.Range:0to10.Default:2. |
Examples
Settingthedelaytimeto8seconds:
| switch(config)# | lldp | txdelay | 8   |
| --------------- | ---- | ------- | --- |
Settingthedelaytimetothedefaultvalueof2seconds:
| switch(config)#     | no      | lldp txdelay |              |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp trap enable |        |     |     |
| ---------------- | ------ | --- | --- |
| lldp trap enable |        |     |     |
| no lldp trap     | enable |     |     |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenot
requiredtobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# | lldp | trap | enable |
| --------------- | ---- | ---- | ------ |
EnablingLLDPtrapgenerationoninterfacelevel:
Devicediscoveryandconfiguration|234

| switch(config-if)# |     | lldp trap | enable |     |     |
| ------------------ | --- | --------- | ------ | --- | --- |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp trap | enable |     |     |
| --------------- | --- | ------------ | ------ | --- | --- |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | no lldp | trap | enable |     |
| ------------------ | --- | ------- | ---- | ------ | --- |
DisplayingLLDPglobalconfiguration:
| switch#     | show | lldp configuration |     |     |     |
| ----------- | ---- | ------------------ | --- | --- | --- |
| LLDP Global |      | Configuration      |     |     |     |
=========================
| LLDP Enabled  |         |                | : No |     |     |
| ------------- | ------- | -------------- | ---- | --- | --- |
| LLDP Transmit |         | Interval       | : 30 |     |     |
| LLDP Hold     | Time    | Multiplier     | : 4  |     |     |
| LLDP Transmit |         | Delay Interval | : 2  |     |     |
| LLDP Reinit   |         | Timer Interval | : 2  |     |     |
| LLDP Trap     | Enabled |                | : No |     |     |
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
--------------------------------------------------------------------------
| 1/1/1 |     | Yes |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- |
| 1/1/2 |     | Yes |     | Yes | Yes |
| 1/1/3 |     | Yes |     | Yes | Yes |
| 1/1/4 |     | Yes |     | Yes | Yes |
| 1/1/5 |     | Yes |     | Yes | Yes |
| 1/1/6 |     | Yes |     | Yes | Yes |
...........
...........
| mgmt |     | Yes |     | Yes | Yes |
| ---- | --- | --- | --- | --- | --- |
DisplayingLLDPConfigurationfortheinterface:
| switch#     | show | lldp configuration |     | 1/1/1 |     |
| ----------- | ---- | ------------------ | --- | ----- | --- |
| LLDP Global |      | Configuration      |     |       |     |
=========================
| LLDP Enabled  |      |            | : Yes |     |     |
| ------------- | ---- | ---------- | ----- | --- | --- |
| LLDP Transmit |      | Interval   | : 30  |     |     |
| LLDP Hold     | Time | Multiplier | : 4   |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 235

| LLDP | Transmit | Delay         | Interval | :   | 2   |     |
| ---- | -------- | ------------- | -------- | --- | --- | --- |
| LLDP | Reinit   | Timer         | Interval | :   | 2   |     |
| LLDP | Trap     | Enabled       |          | :   | No  |     |
| LLDP | Port     | Configuration |          |     |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 |     | Yes |     |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- | --- |
DisplayingLLDPConfigurationforthemanagementinterface:
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
| mgmt           |             | Yes     |         |     | Yes          | Yes |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Command        | History     |         |         |     |              |     |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show lldp | configuration |     |                  |     |     |     |
| --------- | ------------- | --- | ---------------- | --- | --- | --- |
| show lldp | configuration |     | [<INTERFACE-ID>] |     |     |     |
Description
ShowsLLDPconfigurationsettingsforallinterfacesoraspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |
Devicediscoveryandconfiguration|236

Example
Showingconfigurationsettingsforallinterfaces:
switch#
show lldp configuration
| LLDP Global | Configuration |     |     |     |
| ----------- | ------------- | --- | --- | --- |
=========================
| LLDP Enabled  |                 | : No |     |     |
| ------------- | --------------- | ---- | --- | --- |
| LLDP Transmit | Interval        | : 30 |     |     |
| LLDP Hold     | Time Multiplier | : 4  |     |     |
| LLDP Transmit | Delay Interval  | : 2  |     |     |
| LLDP Reinit   | Timer Interval  | : 2  |     |     |
| LLDP Trap     | Enabled         | : No |     |     |
TLVs Advertised
===============
| Management | Address |     |     |     |
| ---------- | ------- | --- | --- | --- |
Port Description
Port VLAN-ID
System Description
System Name
| LLDP Port | Configuration |     |     |     |
| --------- | ------------- | --- | --- | --- |
=======================
| PORT | TX-ENABLED | RX-ENABLED |     | INTF-TRAP-ENABLED |
| ---- | ---------- | ---------- | --- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 | Yes | Yes |     | Yes |
| ----- | --- | --- | --- | --- |
| 1/1/2 | Yes | Yes |     | Yes |
| 1/1/3 | Yes | Yes |     | Yes |
| 1/1/4 | Yes | Yes |     | Yes |
| 1/1/5 | Yes | Yes |     | Yes |
| 1/1/6 | Yes | Yes |     | Yes |
...........
...........
| mgmt | Yes | Yes |     | Yes |
| ---- | --- | --- | --- | --- |
Thisexampleshowsconfigurationsettingsforinterface1/1/1.
| switch#     | show lldp configuration | 1/1/1 |     |     |
| ----------- | ----------------------- | ----- | --- | --- |
| LLDP Global | Configuration           |       |     |     |
=========================
| LLDP Enabled  |                 | : Yes |     |     |
| ------------- | --------------- | ----- | --- | --- |
| LLDP Transmit | Interval        | : 30  |     |     |
| LLDP Hold     | Time Multiplier | : 4   |     |     |
| LLDP Transmit | Delay Interval  | : 2   |     |     |
| LLDP Reinit   | Timer Interval  | : 2   |     |     |
| LLDP Trap     | Enabled         | : No  |     |     |
| LLDP Port     | Configuration   |       |     |     |
=======================
| Auto Flush   | On Link Down | : Yes         |               |                   |
| ------------ | ------------ | ------------- | ------------- | ----------------- |
| Management   | IPv4 Address | : 10.1.1.1    |               |                   |
| Management   | IPv6 Address | : 3001:1::1:1 |               |                   |
| Med Priority | Override     | : Yes         |               |                   |
| Med Location | Civic-addr   | : US 1 4 ret  | 6 tyu 7 tiyuo |                   |
| Med Location | Elin-addr    | : gher        |               |                   |
| PORT         | TX-ENABLED   | RX-ENABLED    |               | INTF-TRAP-ENABLED |
--------------------------------------------------------------------------
| 1/1/1 | Yes | Yes |     | Yes |
| ----- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 237

| Command | History |     |              |
| ------- | ------- | --- | ------------ |
| Release |         |     | Modification |
10.14.1000 WhendisplayingtheLLDP configurationforaspecificinterface,
theoutputofthiscommanddisplaysanyconfiguredmanagement
IPaddresses.
| 10.07orearlier |             |         | --        |
| -------------- | ----------- | ------- | --------- |
| Command        | Information |         |           |
| Platforms      | Command     | context | Authority |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp local-device |     |     |     |
| ---------------------- | --- | --- | --- |
| show lldp local-device |     |     |     |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsare
configuredonanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDson
accessinterfaces.
Example
ShowingglobalLLDPinformationonly:
| switch#     | show lldp | local-device |     |
| ----------- | --------- | ------------ | --- |
| Global Data |           |              |     |
===========
| Chassis-ID  |     | : 88:3a:30:47:c1:c0 |     |
| ----------- | --- | ------------------- | --- |
| System Name |     | : 6100              |     |
System Description : HPE ANW JL679A PL.10.06.0001-346-g56a12a8f4cf15
| Management   | Address   | : 88:3a:30:47:c1:c0 |        |
| ------------ | --------- | ------------------- | ------ |
| Capabilities | Available | : Bridge,           | Router |
| Capabilities | Enabled   | : Bridge,           | Router |
| TTL          |           | : 120               |        |
Showingallportsexcept1/1/11asadministrativelydown:
| switch#     | show lldp | local-device |     |
| ----------- | --------- | ------------ | --- |
| Global Data |           |              |     |
===========
| Chassis-ID  |     | : 88:3a:30:47:c1:c0 |     |
| ----------- | --- | ------------------- | --- |
| System Name |     | : 6100              |     |
System Description : HPE ANW JL679A PL.10.06.0001-346-g56a12a8f4cf15
| Management | Address | : 11.11.11.11 |     |
| ---------- | ------- | ------------- | --- |
Devicediscoveryandconfiguration|238

| Capabilities | Available |     | : Bridge, | Router |
| ------------ | --------- | --- | --------- | ------ |
| Capabilities | Enabled   |     | : Bridge, | Router |
| TTL          |           |     | : 120     |        |
| Port Based   | Data      |     |           |        |
===============
| Port-ID           |           | :   | 1/1/11      |        |
| ----------------- | --------- | --- | ----------- | ------ |
| Port-Desc         |           | :   | "1/1/11"    |        |
| Port Mgmt-Address |           | :   | 11.11.11.11 |        |
| Port VLAN         | ID        | :   | 1           |        |
| Parent            | Interface | :   | interface   | 1/1/11 |
switch#
switch#
|     | show lldp | local-device |     |     |
| --- | --------- | ------------ | --- | --- |
Global Data
===========
| Chassis-ID   |             |     | : 88:3a:30:47:c1:c0 |                      |
| ------------ | ----------- | --- | ------------------- | -------------------- |
| System       | Name        |     | : 4100i             |                      |
| System       | Description |     | : HPE ANW           | JL817A RL.10.08.0001 |
| Management   | Address     |     | : 11.11.11.11       |                      |
| Capabilities | Available   |     | : Bridge,           | Router               |
| Capabilities | Enabled     |     | : Bridge,           | Router               |
| TTL          |             |     | : 120               |                      |
| Port Based   | Data        |     |                     |                      |
===============
| Port-ID           |           | :   | 1/1/11      |        |
| ----------------- | --------- | --- | ----------- | ------ |
| Port-Desc         |           | :   | "1/1/11"    |        |
| Port Mgmt-Address |           | :   | 11.11.11.11 |        |
| Port VLAN         | ID        | :   | 1           |        |
| Parent            | Interface | :   | interface   | 1/1/11 |
switch#
Inthisexample,alltheportsexcept1/1/11areadministrativelydown,andVLANID100isconfiguredon
thisaccessinterface.
| switch# | show lldp | local-device |     |     |
| ------- | --------- | ------------ | --- | --- |
Global Data
===========
| Chassis-ID   |             |     | : 1c:98:ec:e3:45:00 |        |
| ------------ | ----------- | --- | ------------------- | ------ |
| System       | Name        |     | : switch            |        |
| System       | Description |     | : HPE               | ANW    |
| Management   | Address     |     | : 192.168.10.1      |        |
| Capabilities | Available   |     | : Bridge,           | Router |
| Capabilities | Enabled     |     | : Bridge,           | Router |
| TTL          |             |     | : 120               |        |
| Port Based   | Data        |     |                     |        |
===============
| Port-ID |     | :   | 1/1/11 |     |
| ------- | --- | --- | ------ | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 239

| Port-Desc      |             |         | : "1/1/11"  |              |     |     |
| -------------- | ----------- | ------- | ----------- | ------------ | --- | --- |
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
| show lldp | neighbor-info |     |                    |     |     |     |
| --------- | ------------- | --- | ------------------ | --- | --- | --- |
| show lldp | neighbor-info |     | [<INTERFACE-NAME>] |     |     |     |
Description
Displaysinformationaboutneighboringdevicesforallinterfacesorforaspecificinterface.The
informationdisplayedvariesdependingonthetypeofneighborconnectedandthetypeofTLVssentby
theneighbor.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-NAME> Specifiestheinterfaceforwhichtoshowinformationfor
neighboringdevices.Usetheformatmember/slot/port(for
example,1/3/1).
Examples
ShowingLLDPinformationforallinterfaces:
| switch# |          | show lldp   | neighbor-info |     |     |     |
| ------- | -------- | ----------- | ------------- | --- | --- | --- |
| LLDP    | Neighbor | Information |               |     |     |     |
=========================
| Total      | Neighbor |            | Entries          | : 1     |           |              |
| ---------- | -------- | ---------- | ---------------- | ------- | --------- | ------------ |
| Total      | Neighbor |            | Entries Deleted  | : 5     |           |              |
| Total      | Neighbor |            | Entries Dropped  | : 0     |           |              |
| Total      | Neighbor |            | Entries Aged-Out | : 3     |           |              |
| LOCAL-PORT |          | CHASSIS-ID |                  | PORT-ID | PORT-DESC | TTL SYS-NAME |
--------------------------------------------------------------------------------
| 1/1/2 |     | 38:21:c7:5c:df:40 |     | 1/1/2 | 1/1/2 | 120 switch |
| ----- | --- | ----------------- | --- | ----- | ----- | ---------- |
| 1/1/3 |     | f8:60:f0:c9:e0:a0 |     | 1/1/3 | 1/1/3 | 120 switch |
Showinginformationforinterface1/1/3whenithasonlyoneswitchconnectedasaneighbor:
Devicediscoveryandconfiguration|240

Switch2#
|          | show                | lldp | neighbor-info | 1/1/3               |                      |
| -------- | ------------------- | ---- | ------------- | ------------------- | -------------------- |
| Port     |                     |      |               | : 1/1/3             |                      |
| Neighbor | Entries             |      |               | : 1                 |                      |
| Neighbor | Entries             |      | Deleted       | : 1                 |                      |
| Neighbor | Entries             |      | Dropped       | : 0                 |                      |
| Neighbor | Entries             |      | Aged-Out      | : 1                 |                      |
| Neighbor | Chassis-Name        |      |               | : 6100              |                      |
| Neighbor | Chassis-Description |      |               | : HPE ANW           | JL679A PL.10.15.0001 |
| Neighbor | Chassis-ID          |      |               | : 88:3a:30:47:d1:c0 |                      |
| Neighbor | Management-Address  |      |               | : 88:3a:30:47:d1:c0 |                      |
| Chassis  | Capabilities        |      | Available     | : Bridge,           | Router               |
| Chassis  | Capabilities        |      | Enabled       | : Bridge,           | Router               |
| Neighbor | Port-ID             |      |               | : 1/1/3             |                      |
| Neighbor | Port-Desc           |      |               | : 1/1/3             |                      |
| Neighbor | Port                | VLAN | ID            | : 1                 |                      |
| Neighbor | Port                | VLAN | Name          | : DEFAULT_VLAN_1    |                      |
| Neighbor | Port                | MFS  |               | : 1500              |                      |
| TTL      |                     |      |               | : 120               |                      |
| Neighbor | Mac-Phy             |      | details       |                     |                      |
| Neighbor | Auto-neg            |      | Supported     | : True              |                      |
| Neighbor | Auto-neg            |      | Enabled       | : True              |                      |
Neighbor Auto-ned Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighnor | MAU | Type |     | : 1000 | BASETFD |
| -------- | --- | ---- | --- | ------ | ------- |
Showingneighborinformationforinterface1/3/2whenithasEEEenabledandsuccessfullyauto-
negotiated:
| switch#  | show                | lldp | neighbor-info | 1/3/2               |                      |
| -------- | ------------------- | ---- | ------------- | ------------------- | -------------------- |
| Port     |                     |      |               | : 1/3/2             |                      |
| Neighbor | Entries             |      |               | : 1                 |                      |
| Neighbor | Entries             |      | Deleted       | : 1                 |                      |
| Neighbor | Entries             |      | Dropped       | : 0                 |                      |
| Neighbor | Entries             |      | Aged-Out      | : 1                 |                      |
| Neighbor | Chassis-Name        |      |               | : BLDG01-F1-6300    |                      |
| Neighbor | Chassis-Description |      |               | : hpe_anw           | JL668A FL.10.15.0001 |
| Neighbor | Chassis-ID          |      |               | : 88:3a:30:92:a5:c0 |                      |
| Neighbor | Management-Address  |      |               | : 10.6.9.15         |                      |
| Chassis  | Capabilities        |      | Available     | : Bridge,           | Router               |
| Chassis  | Capabilities        |      | Enabled       | : Bridge,           | Router               |
| Neighbor | Port-ID             |      |               | : 1/1/1             |                      |
| Neighbor | Port-Desc           |      |               | : 1/1/1             |                      |
| Neighbor | Port                | VLAN | ID            | : 1                 |                      |
| Neighbor | Port                | VLAN | Name          | : DEFAULT_VLAN_1    |                      |
| Neighbor | Port                | MFS  |               | : 1500              |                      |
| TTL      |                     |      |               | : 120               |                      |
| Neighbor | Mac-Phy             |      | details       |                     |                      |
| Neighbor | Auto-neg            |      | Supported     | : true              |                      |
| Neighbor | Auto-Neg            |      | Enabled       | : true              |                      |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor | MAU      | type        |      | : 1000  | BASETFD |
| -------- | -------- | ----------- | ---- | ------- | ------- |
| Neighbor | EEE      | information |      | : DOT3  |         |
| Neighbor | TX       | Wake        | time | : 17 us |         |
| Neighbor | RX       | Wake        | time | : 17 us |         |
| Neighbor | Fallback |             | time | : 17 us |         |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 241

| Neighbor       |             | TX Echo | time    | : 17 us      |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- |
| Neighbor       |             | RX Echo | time    | : 17 us      |     |
| Command        | History     |         |         |              |     |
| Release        |             |         |         | Modification |     |
| 10.07orearlier |             |         |         | --           |     |
| Command        | Information |         |         |              |     |
| Platforms      |             | Command | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     | detail |     |     |
| --------- | ------------- | --- | ------ | --- | --- |
| show lldp | neighbor-info |     | detail |     |     |
Description
ShowsdetailedLLDPneighborinformationforallLLDPneighborconnectedinterfaces.
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
| Neighbor |              | Chassis-Description |           | : hpe_anw           | ...    |
| Neighbor |              | Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor |              | Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities |                     | Available | : Bridge,           | Router |
| Chassis  | Capabilities |                     | Enabled   | : Bridge,           | Router |
| Neighbor |              | Port-ID             |           | : 1/1/4             |        |
| Neighbor |              | Port-Desc           |           | : 1/1/4             |        |
| Neighbor |              | Port                | VLAN ID   | : 1                 |        |
| Neighbor |              | Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor |              | Port                | MFS       | : 1500              |        |
Devicediscoveryandconfiguration|242

| TTL               |           | : 120  |     |
| ----------------- | --------- | ------ | --- |
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
| Neighbor Chassis-Description |           | : hpe_anw...        |        |
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
| Neighbor Chassis-Description |           | : hpe_anw           | ...    |
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 243

| Port     |                     |          |           | : 1/1/46            |        |
| -------- | ------------------- | -------- | --------- | ------------------- | ------ |
| Neighbor | Entries             |          |           | : 1                 |        |
| Neighbor | Entries             | Deleted  |           | : 0                 |        |
| Neighbor | Entries             | Dropped  |           | : 0                 |        |
| Neighbor | Entries             | Aged-Out |           | : 0                 |        |
| Neighbor | Chassis-Name        |          |           | : 6300              |        |
| Neighbor | Chassis-Description |          |           | : hpe_anw           | ...    |
| Neighbor | Chassis-ID          |          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor | Management-Address  |          |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities        |          | Available | : Bridge,           | Router |
| Chassis  | Capabilities        |          | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID             |          |           | : 1/1/19            |        |
| Neighbor | Port-Desc           |          |           | : 1/1/19            |        |
| Neighbor | Port                | VLAN     | ID        | : 1                 |        |
| Neighbor | Port                | VLAN     | Name      | : DEFAULT_VLAN_1    |        |
| Neighbor | Port                | MFS      |           | : 1500              |        |
| TTL      |                     |          |           | : 120               |        |
| Neighbor | Mac-Phy             | details  |           |                     |        |
| Neighbor | Auto-neg            |          | Supported | : true              |        |
| Neighbor | Auto-Neg            |          | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor | MAU | type |     | : 1000 | BASETFD |
| -------- | --- | ---- | --- | ------ | ------- |
--------------------------------------------------------------------------------
| Port           |                     |          |         | : 1/1/47            |     |
| -------------- | ------------------- | -------- | ------- | ------------------- | --- |
| Neighbor       | Entries             |          |         | : 1                 |     |
| Neighbor       | Entries             | Deleted  |         | : 0                 |     |
| Neighbor       | Entries             | Dropped  |         | : 0                 |     |
| Neighbor       | Entries             | Aged-Out |         | : 0                 |     |
| Neighbor       | Chassis-Name        |          |         | : 6300              |     |
| Neighbor       | Chassis-Description |          |         | : hpe_anw           | ... |
| Neighbor       | Chassis-ID          |          |         | : 38:11:17:1a:d5:00 |     |
| Neighbor       | Management-Address  |          |         | : 38:11:17:1a:d5:00 |     |
| Chassis        | Cap                 |          |         |                     |     |
| Command        | History             |          |         |                     |     |
| Release        |                     |          |         | Modification        |     |
| 10.07orearlier |                     |          |         | --                  |     |
| Command        | Information         |          |         |                     |     |
| Platforms      |                     | Command  | context | Authority           |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | statistics |     |                  |     |     |
| --------- | ---------- | --- | ---------------- | --- | --- |
| show lldp | statistics |     | [<INTERFACE-ID>] |     |     |
Description
ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
Devicediscoveryandconfiguration|244

| Parameter      |     |     | Description                                   |     |
| -------------- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |     |
Example
Showingglobalstatisticsforallinterfaces:
switch#
|             | show copp-policy     | statistics |     |     |
| ----------- | -------------------- | ---------- | --- | --- |
| switch#     | show lldp statistics |            |     |     |
| LLDP Global | Statistics           |            |     |     |
==========================================================================
| Total Packets | Transmitted  |           | : 25 |     |
| ------------- | ------------ | --------- | ---- | --- |
| Total Packets | Received     |           | : 20 |     |
| Total Packets | Received And | Discarded | : 0  |     |
| Total TLVs    | Unrecognized |           | : 0  |     |
| LLDP Port     | Statistics   |           |      |     |
==========================================================================
| PORT-ID | TX-PACKETS | RX-PACKETS | RX-DISCARDED | TLVS-UNKNOWN |
| ------- | ---------- | ---------- | ------------ | ------------ |
--------------------------------------------------------------------------
| 1/1/1  | 25  | 20  | 0   | 0   |
| ------ | --- | --- | --- | --- |
| 1/1/2  | 0   | 0   | 0   | 0   |
| 1/1/3  | 0   | 0   | 0   | 0   |
| 1/1/4  | 0   | 0   | 0   | 0   |
| 1/1/5  | 0   | 0   | 0   | 0   |
| 1/1/6  | 0   | 0   | 0   | 0   |
| 1/1/7  | 0   | 0   | 0   | 0   |
| 1/1/8  | 0   | 0   | 0   | 0   |
| 1/1/9  | 0   | 0   | 0   | 0   |
| 1/1/10 | 0   | 0   | 0   | 0   |
| 1/1/11 | 0   | 0   | 0   | 0   |
| 1/1/12 | 0   | 0   | 0   | 0   |
| 1/1/13 | 0   | 0   | 0   | 0   |
| 1/1/14 | 0   | 0   | 0   | 0   |
| 1/1/15 | 0   | 0   | 0   | 0   |
| 1/1/16 | 0   | 0   | 0   | 0   |
| 1/1/17 | 0   | 0   | 0   | 0   |
| 1/1/18 | 0   | 0   | 0   | 0   |
| 1/1/19 | 0   | 0   | 0   | 0   |
| 1/1/20 | 0   | 0   | 0   | 0   |
| 1/1/21 | 0   | 0   | 0   | 0   |
| 1/1/22 | 0   | 0   | 0   | 0   |
| 1/1/23 | 0   | 0   | 0   | 0   |
| 1/1/24 | 0   | 0   | 0   | 0   |
| 1/1/25 | 0   | 0   | 0   | 0   |
| 1/1/26 | 0   | 0   | 0   | 0   |
| 1/1/27 | 0   | 0   | 0   | 0   |
| 1/1/28 | 0   | 0   | 0   | 0   |
Showingstatisticsforinterface1/1/1:
| switch# | show lldp statistics | 1/1/1 |     |     |
| ------- | -------------------- | ----- | --- | --- |
LLDP Statistics
===============
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 245

| Port Name           |              |              | : 1/1/1      |
| ------------------- | ------------ | ------------ | ------------ |
| Packets             | Transmitted  |              | : 159        |
| Packets             | Received     |              | : 163        |
| Packets             | Received And | Discarded    | : 0          |
| Packets             | Received And | Unrecognized | : 0          |
| Command History     |              |              |              |
| Release             |              |              | Modification |
| 10.07orearlier      |              |              | --           |
| Command Information |              |              |              |
| Platforms           | Command      | context      | Authority    |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp tlv |     |     |     |
| ------------- | --- | --- | --- |
| show lldp tlv |     |     |     |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
Example
| switch# | show lldp | tlv |     |
| ------- | --------- | --- | --- |
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
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
Devicediscoveryandconfiguration|246

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

cdp (global)

cdp

Description

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

247

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|                    | config-if |     | rightsforthiscommand. |
| ------------------ | --------- | --- | --------------------- |
| clear cdp counters |           |     |                       |
| clear cdp counters |           |     |                       |
Description
ClearsCDPcounters.
Examples
Devicediscoveryandconfiguration|248

ClearingCDPcounters:
| switch(config)      | clear   | cdp counters |              |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show cdp
show cdp
Description
ShowsCDPinformationforallinterfaces.
Examples
ShowingCDPinformation:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 249

| switch(config)# | show        | cdp |     |     |
| --------------- | ----------- | --- | --- | --- |
| CDP Global      | Information |     |     |     |
======================
| CDP                 | : Enabled      |         |              |     |
| ------------------- | -------------- | ------- | ------------ | --- |
| CDP Mode            | : Rx           | only    |              |     |
| CDP Hold            | Time : 180     | seconds |              |     |
| Port                | CDP            |         |              |     |
| --------            | -------------- |         |              |     |
| 1/1/1               | Enabled        |         |              |     |
| 1/1/2               | Enabled        |         |              |     |
| 1/1/3               | Enabled        |         |              |     |
| 1/1/4               | Enabled        |         |              |     |
| 1/1/5               | Enabled        |         |              |     |
| 1/1/6               | Enabled        |         |              |     |
| 1/1/7               | Enabled        |         |              |     |
| 1/1/8               | Enabled        |         |              |     |
| 1/1/9               | Enabled        |         |              |     |
| 1/1/10              | Enabled        |         |              |     |
| Command History     |                |         |              |     |
| Release             |                |         | Modification |     |
| 10.07orearlier      |                |         | --           |     |
| Command Information |                |         |              |     |
| Platforms           | Command        | context | Authority    |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp neighbor-info |     |                |     |     |
| ---------------------- | --- | -------------- | --- | --- |
| show cdp neighbor-info |     | <INTERFACE-ID> |     |     |
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
| Parameter      |     |     | Description                                   |     |
| -------------- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |     |
Examples
ShowingallCDPneighborinformation:
| switch(config)# | show    | cdp neighbor-info |          |            |
| --------------- | ------- | ----------------- | -------- | ---------- |
| Total Neighbor  | Entries | : 1               |          |            |
| Port            | Device  | ID                | Platform | Capability |
---------------------------------------------------------------------------
| 1/1/1 | HPE_ANW-3810M-24G-1-slot... |     | HPE ANW Sw | S   |
| ----- | --------------------------- | --- | ---------- | --- |
ShowingCDPinformationforinterface1/1/1:
Devicediscoveryandconfiguration|250

| switch(config)# |             | show | cdp neighbor-info                         |                |              | 1/1/1 |                  |     |     |
| --------------- | ----------- | ---- | ----------------------------------------- | -------------- | ------------ | ----- | ---------------- | --- | --- |
| Local Port      |             |      | : 1/1/1                                   |                |              |       |                  |     |     |
| MAC             |             |      | : 70:10:6f:86:78:7f                       |                |              |       |                  |     |     |
| Device ID       |             |      | : HPE_ANW-3810M-24G-1-slot(70106f-867800) |                |              |       |                  |     |     |
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
| switch(config)# |     | show | cdp traffic |     |     |     |     |     |     |
| --------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
CDP Statistics
====================
| Port | Transmitted |     | Frames |     |     | Received | Frames | Discarded | Frames |
| ---- | ----------- | --- | ------ | --- | --- | -------- | ------ | --------- | ------ |
--------------------------------------------------------------------------------
| 1/1/1          |             | 0   |     |     |              | 4   |     | 0   |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 1/1/2          |             | 0   |     |     |              | 0   |     | 0   |     |
| 1/1/3          |             | 0   |     |     |              | 2   |     | 0   |     |
| 1/1/4          |             | 0   |     |     |              | 0   |     | 0   |     |
| 1/1/5          |             | 0   |     |     |              | 0   |     | 0   |     |
| Command        | History     |     |     |     |              |     |     |     |     |
| Release        |             |     |     |     | Modification |     |     |     |     |
| 10.07orearlier |             |     |     |     | --           |     |     |     |     |
| Command        | Information |     |     |     |              |     |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 251

| Platforms |     | Command | context |     | Authority |
| --------- | --- | ------- | ------- | --- | --------- |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp | voice-vlan |     | mode |     |     |
| -------- | ---------- | --- | ---- | --- | --- |
| show cdp | voice-vlan |     | mode |     |     |
Description
ShowsCDPvoice-vlanandmode.
Examples
ShowingCDPvoice-vlanandmode:
| switch(config)# |       |      | show cdp voice-vlan |     | mode |
| --------------- | ----- | ---- | ------------------- | --- | ---- |
| CDP             | voice | VLAN | mode                |     |      |
====================
| Port           |             | Voice       | VLAN    | Mode       |              |
| -------------- | ----------- | ----------- | ------- | ---------- | ------------ |
| --------       |             | ----------- |         | ---------- |              |
| 1/1/1          |             | N/A         |         | Rx         | only         |
| 1/1/2          |             | N/A         |         | Rx         | only         |
| 1/1/3          |             | N/A         |         | Rx         | only         |
| 1/1/4          |             | N/A         |         | Rx         | only         |
| 1/1/5          |             | N/A         |         | Rx         | only         |
| 1/1/6          |             | N/A         |         | Rx         | only         |
| 1/1/7          |             | N/A         |         | Rx         | only         |
| 1/1/8          |             | N/A         |         | Rx         | only         |
| 1/1/9          |             | N/A         |         | Rx         | only         |
| Command        | History     |             |         |            |              |
| Release        |             |             |         |            | Modification |
| 10.07orearlier |             |             |         |            | --           |
| Command        | Information |             |         |            |              |
| Platforms      |             | Command     | context |            | Authority    |
config
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Devicediscoveryandconfiguration|252

Chapter 15

Zero Touch Provisioning

Zero Touch Provisioning

Zero Touch Provisioning (ZTP) enables the auto-configuration of factory default switches without a
network administrator onsite.

When a switch is booted from its factory default configuration, ZTP autoprovisions the switch by
automatically downloading and installing a firmware file, a configuration file, or both. With ZTP, even a
nontechnical user (for example: a store manager in a retail chain or a teacher in a school) can deploy
devices at a site.

ZTP connection priorities

An HPE Aruba Networking CX switch supports ZTP provisioning on an Out-of-Band Management (OOBM)
port or a data port (vlan 1). Priority is given to ZTP options received on the OOBM port. If the switch
receives ZTP configuration options on a data port first or from a DHCPv6 server connected to an OOBM
port, the switch waits for an additional 30 seconds to see if higher-priority ZTP options will be received
on an OOBM port also.

Priority is given to ZTPv4 options over ZTPv6 options, so connection priorities are as follows, from
highest to lowest prioritiy:

1. ZTPv4 options received on an OOBM port.

2. ZTPv4 options on a data port.

3. ZTPv6 options on an OOBM port.

ZTP support

The switch supports standards-based Zero Touch Provisioning (ZTP) operations as follows:

n ZTP operations are supported over IPv4 and IPv6 connections.

n The switch must be running the factory default configuration.

n The configuration file is a text file or JSON file that becomes the startup and running configuration on
the switch after the ZTP operation is complete. The configuration can be in CLI or in JSON format.

n When the switch is started using the factory default configuration, the ZTP operation is started

automatically and is active until any running configuration of the switch is modified. There is no CLI
command required to start the operation.

n You must configure the DHCP server to provide a standards-based ZTP server solution. Options and
features that are specific to Network Management Solution (NMS) tools, such as AirWave, are not
supported.

Supported ZTP options from a DHCPv4 server are:

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

253

| DHCP           | option |     | Description                                        |
| -------------- | ------ | --- | -------------------------------------------------- |
| 43             |        |     | VendorSpecificInformation                          |
| 43suboption144 |        |     | Nameoftheconfigurationfile                         |
| 43suboption145 |        |     | Nameofthefirmwareimagefile                         |
| 43suboption148 |        |     | FQDNorIPv4orIPv6addressoftheHTTPProxy              |
| 60             |        |     | VendorClassIdentifier(VCI)                         |
| 66             |        |     | IPv4orIPv6addressoftheTFTPorHTTPserver(Specifyinga |
hostnameinsteadofanIPaddressisnotsupported.)
| 67  |     |     | Nameoftheconfigurationfile(Option43suboption144takes |
| --- | --- | --- | ---------------------------------------------------- |
precedenceoverthisoption.)
UniqueZTPIPv6optionscanbesentfromtheDHCPv6ServerbasedonMACaddressoftheswitchor
basedontheDHCPVendorclassIdentifieroftheswitch.SupportedZTPoptionsfromaDHCPv6server
are:
| DHCP option |     | Description                                          |     |
| ----------- | --- | ---------------------------------------------------- | --- |
| 59          |     | IPv6addressoftheTFTP/HTTPserver.Theimagefilenamealso |     |
canbegiveninthisURLorintheVCAoption-17.
NOTE:thebootfileURLwillsupportTFTPv6ServerorHTTPServer
optionwithIPv6addressorFQDNname.
| 17suboption145 |     | Nameoftheimagefile.         |     |
| -------------- | --- | --------------------------- | --- |
| 17suboption144 |     | Nameoftheconfigurationfile. |     |
Theswitchsupportsthefollowingstandards:
n RFC2131,DynamicHostConfigurationProtocol.
n RFC2132,DHCPOptionsandBOOTPVendorExtensions.Supportislimitedtotheoptionslistedinthe
table"SupportedDHCPoptionsforZTPonAOS-CX."
n RFC5970,DHCPv6OptionsforNetworkBoot.Supportislimitedtotheoptionslistedinthetable
"SupportedDHCPoptionsforZTPonAOS-CX."
HewlettPackardEnterpriserecommendsthatyouimplementZTPinasecureandprivateenvironment.
Anypublicaccesscancompromisethesecurityoftheswitch,asfollows:
n ZTPisenabledonlyinthefactorydefaultconfigurationoftheswitch,DHCPsnoopingisnotenabled.
TheRogueDHCPservermustbemanuallymanaged.
n TheDHCPofferisinplaindatawithoutencryption.
| Setting | up ZTP | on a trusted | network |
| ------- | ------ | ------------ | ------- |
ThefollowingprocedureisanoverviewofsettingupaZeroTouchProvisioning(ZTP)environmentto
provisionnewlyinstalledswitchesautomatically.Theprocedureisintendedfornetworkadministrators
ZeroTouchProvisioning|254

who are familiar with automatically provisioning switches in a network, and does not provide detailed
information about configuring or managing switches.

Procedure

1. For each switch model to be provisioned using ZTP, do the following:

a. Obtain the switch firmware image file.
b. Prepare the switch configuration file. The configuration file becomes the running

configuration and the startup configuration on the switch.

2. Set up a TFTP or HTTP server and record its IPv4 or IPv6 address. The address is required when

you set up the DHCP server. The switch must be able to reach the TFTP or HTTP server and DHCP
server on the same subnet.

Switches support provisioning through a network connected to a data port or through a network
connected to the in-band management interface VLAN 1.

3. Publish the configuration files and image files to the TFTP or HTTP server. You need to know the
locations of the files and the IPv4/IPv6 address of theTFTP or HTTP server when you set up the
vendor class options on the DHCP server.

4. On the DHCP server, set up vendor classes for each switch model you plan to provision. To do this

you need the following information:
n The IPv4/IPv6 address of the TFTP or HTTP server. Using a host name is not supported.

n The path to the switch configuration and firmware image files on the TFTP or HTTP server.

n The vendor class identifier (VCI) for each switch model.

You can obtain the VCI by entering the show dhcp client vendor-class-identifier command
from a switch CLI command prompt in the manager context. The VCI is the text string in the
response that starts with Aruba.

For example:

switch# show dhcp client vendor-class-identifier
Vendor Class Identifier: Aruba xxxxx xxxx

Where x indicates the switch model number.

5. At the installation site, provide the switch installer with a Cat6 network cable connected to the

network that includes the DHCP and TFTP or HTTP servers, and information about the switch port
to use. The switch installer plugs the cable into the data port you specify.

The ZTP operation begins when power is applied to the switch after the network cable is installed.

6. Assuming the downloaded configuration includes a way to access the CLI of the switch, you can
enter the following command to show the options offered by the DHCP server and the status of
the ZTP operation:
show ztp information

ZTP process during switch boot

1. The switch boots up with the factory default configuration.

If the ZTP operation detects that the switch configuration is different from the factory default
configuration, the ZTP operation ends. The switch must be configured at the installation site.

2. The switch sends out a DHCP discovery from the in-band management interface.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

255

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
provision configuration is lost, causing ZTP to enter into a failed state. ZTP force-provision will
need to be enabled again to continue the process.

3. The DHCP server responds with an offer containing the following:

n The IPv4 or IPv6 address of the TFTP or HTTP server

n One or both of the following:

o The name of the firmware image file

o The name of the configuration file

n Aruba Central Location (optional) including the shared token value for the on-premise server

n HTTP Proxy Location (optional)

4.

If a firmware image file is offered, the ZTP operation downloads the image file from the TFTP or
HTTP server to the switch. If the current switch image and downloaded firmware image version
do not match, then the switch boots with the downloaded image:
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

ZTP commands

show ztp information
show ztp information

Zero Touch Provisioning | 256

Description

Shows information about Zero Touch Provisioning (ZTP) operations performed on the switch.

Usage

When a switch configured to use ZTP is booted from a factory default configuration, the switch contacts
a DHCP server, which offers options for obtaining files used to provision the switch:

n The IPv4/IPv6 address of TFTP Server or the IPv6 address of HTTP server

n The name of the image file

n The name of the configuration file

n The HPE Aruba Networking Central FDQN or IPv4/IPv6 address

n The HTTP proxy FDQN or IPv4/IPv6 address

The show ztp information command shows the options offered by the DHCP server and the status of
the ZTP operation.

The status of the ZTP operation is one of the following:

Success

The ZTP operation succeeded.
One of the following is true:

n Both the running configuration and the startup configuration were updated.
n The IP address of the TFTP/HTTP server was received, but the offer did not include a

configuration file or a firmware image file.

n Any combination of vendor encapsulated DHCP options are received as configured,

along with the firmware image and switch configuration file.

n Only vendor encapsulated DHCP options are configured and are received accordingly.

The switch was booted from a configuration that is not the factory default configuration. For
example, the administrator password has been set.

Either the switch received the DHCP IPv4 or IPv6 address but no ZTP options were received
within 1 minute or ZTP force-provision is triggered and no ZTP options are received within 3
minutes.

The running configuration was modified by a user while the ZTP operation was in progress.

The TFTP server is not reachable at the specified IP address.

The image file name or config file name is provided without the TFTP server location to fetch
the files from and ZTP enters failed state.

Either the file transfer of the configuration file failed, or the configuration file is invalid (an
error occurred while attempting to apply the configuration).

Failed - Custom
startup
configuration
detected

Failed - Timed
out while
waiting to
receive ZTP
options

Failed -
Detected
change in
running
configuration

Failed - TFTP
server
unreachable

Failed - TFTP
server
information
unavailable

Failed - Invalid
configuration
file received

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

257

Failed-Invalid Eitherthefiletransferofthefirmwareimagefilefailed,orthefirmwareimagefileisinvalid
| imagefile | (anerroroccurredwhileverifyingtheimage). |     |     |     |     |
| --------- | ---------------------------------------- | --- | --- | --- | --- |
received
| Failed-HTTP | TheHTTPserverisnotreachableatthespecifiedIPaddress |     |     |     |     |
| ----------- | -------------------------------------------------- | --- | --- | --- | --- |
server
unreachable
Inthecaseofreconnection,connectwithamainoralternativelocationtotheCOPinstanceasauser.The
currentconnectionisshownintheCentrallocationfield.
Scenario1: Ifthelocationthedeviceiscurrentlyconnectedonisupdated,thesystemreconnectsinorderto
connectwiththenewlocation.
Scenario2:Ifthelocationinwhichthedeviceisnotcurrentlyconnectedonisupdated,theDUTdoesnotgo
throughthereconnectionprocess.
Examples
ShowingswitchimageandconfigdownloadfromanIPv4TFTPserverinprogressafterreceiving
ZTP options:
| switch#         | show ztp information |          |                     |         |                           |
| --------------- | -------------------- | -------- | ------------------- | ------- | ------------------------- |
| TFTP Server     |                      |          | : 10.0.0.2          |         |                           |
| Image File      |                      |          | : TL_10_02_0001.swi |         |                           |
| Configuration   | File                 |          | : ztp.cfg           |         |                           |
| ZTP Status      |                      |          | : In-progress       | - Image | download and verification |
| HPE ANW         | Central Location     |          | : NA                |         |                           |
| Alternative     | HPE ANW Central      | Location | : NA                |         |                           |
| HPE ANW         | Central Shared Token |          | : NA                |         |                           |
| Force-Provision |                      |          | : Enabled           |         |                           |
| HTTP Proxy      | Location             |          | : NA                |         |                           |
ShowingswitchimagedownloadfailurefromanIPv4TFTPserverbecausetheserverwasunreachable
| switch#         | show ztp information |          |                     |               |             |
| --------------- | -------------------- | -------- | ------------------- | ------------- | ----------- |
| TFTP Server     |                      |          | : 10.0.0.2          |               |             |
| Image File      |                      |          | : TL_10_02_0001.swi |               |             |
| Configuration   | File                 |          | : ztpv6.cfg         |               |             |
| ZTP Status      |                      |          | : Failed            | - TFTP server | unreachable |
| HPE ANW         | Central Location     |          | : NA                |               |             |
| Alternative     | HPE ANW Central      | Location | : NA                |               |             |
| HPE ANW         | Central Shared Token |          | : NA                |               |             |
| Force-Provision |                      |          | : Enabled           |               |             |
| HTTP Proxy      | Location             |          | : NA                |               |             |
ShowingasuccessfulswitchconfigurationdownloadfromanIPv6HTTPserver
| switch#       | show ztp information |          |                     |     |     |
| ------------- | -------------------- | -------- | ------------------- | --- | --- |
| HTTP Server   |                      |          | : http://[2001::50] |     |     |
| Image File    |                      |          | : TL_10_15_0001.swi |     |     |
| Configuration | File                 |          | : config_file       |     |     |
| ZTP Status    |                      |          | : Success           |     |     |
| HPE ANW       | Central Location     |          | : NA                |     |     |
| Alternative   | HPE ANW Central      | Location | : NA                |     |     |
ZeroTouchProvisioning|258

| HPE ANW         | Central Shared | Token   |              | : NA      |
| --------------- | -------------- | ------- | ------------ | --------- |
| Force-Provision |                |         |              | : Enabled |
| HTTP Proxy      | Location       |         |              | : NA      |
| Command         | History        |         |              |           |
| Release         |                |         | Modification |           |
| 10.07orearlier  |                |         | --           |           |
| Command         | Information    |         |              |           |
| Platforms       | Command        | context | Authority    |           |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| ztp force | provision |     |     |     |
| --------- | --------- | --- | --- | --- |
ztp force-provision
no ztp force-provision
Description
Startson-demandZTP.
Usage
DHCPoptionsreceivedareprocessedindependentofthecurrentstateofconfigurationontheswitch.
PreviousZTPTFTPServer,ImageFile,ConfigurationFile,HPE ArubaNetworkingCentralLocation,and
HTTPProxylocationoptionsareclearedandtheswitchsendsaDHCPrequest.
Examples
Inthefollowingexample,force-provisionisenabled.
| switch#         | configure terminal |                 |     |     |
| --------------- | ------------------ | --------------- | --- | --- |
| switch(config)# | ztp                | force-provision |     |     |
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
| switch#         | show ztp information |       |     |                     |
| --------------- | -------------------- | ----- | --- | ------------------- |
| TFTP Server     |                      |       |     | : 10.0.0.2          |
| Image File      |                      |       |     | : TL_10_02_0001.swi |
| Configuration   | File                 |       |     | : ztp.cfg           |
| Status          |                      |       |     | : Success           |
| HPE ANW         | Central Location     |       |     | : NA                |
| HPE ANW         | Central Shared       | Token |     | : NA                |
| Force-Provision |                      |       |     | : Enabled           |
| HTTP Proxy      | Location             |       |     | : NA                |
Inthefollowingexample,force-provisionisdisabled.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 259

| switch# | configure terminal |     |     |     |
| ------- | ------------------ | --- | --- | --- |
switch(config)#
|     | no  | ztp force-provision |     |     |
| --- | --- | ------------------- | --- | --- |
Inthefollowingexample,force-provisionstatusischeckedwhiledisabled.
| switch#         | show ztp information |         |              |                     |
| --------------- | -------------------- | ------- | ------------ | ------------------- |
| TFTP Server     |                      |         |              | : 10.0.0.2          |
| Image File      |                      |         |              | : TL_10_02_0001.swi |
| Configuration   | File                 |         |              | : ztp.cfg           |
| Status          |                      |         |              | : Success           |
| HPE ANW         | Central Location     |         |              | : NA                |
| HPE ANW         | Central Shared       | Token   |              | : NA                |
| Force-Provision |                      |         |              | : Disabled          |
| HTTP Proxy      | Location             |         |              | : NA                |
| Command         | History              |         |              |                     |
| Release         |                      |         | Modification |                     |
| 10.07orearlier  |                      |         | --           |                     |
| Command         | Information          |         |              |                     |
| Platforms       | Command              | context | Authority    |                     |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
ZeroTouchProvisioning|260

Chapter 16
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
| clear events  |              |          |        |              |          |
clear events
Description
Clearsupeventlogs.Usingtheshow eventscommandwillonlydisplaythelogsgeneratedafterthe
clear eventscommand.
Examples
Clearingallgeneratedeventlogs:
| switch# show | events |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- |
---------------------------------------------------
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 27 |     |     |
| ----------- | ------------- | ---------- | ----- | --- | --- |
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to
36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization   | poll interval | is changed | to 49 |     |     |
| ------------- | ------------- | ---------- | ----- | --- | --- |
| switch# clear | events        |            |       |     |     |
switch#
show events
---------------------------------------------------
| show event | logs |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- |
---------------------------------------------------
2018-10-14:07:03:05.637544|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization         | poll interval | is changed | to 34        |     |     |
| ------------------- | ------------- | ---------- | ------------ | --- | --- |
| Command History     |               |            |              |     |     |
| Release             |               |            | Modification |     |     |
| 10.07orearlier      |               |            | --           |     |     |
| Command Information |               |            |              |     |     |
| Platforms           | Command       | context    | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| console | baud-rate |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
261
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries)

| console    | baud-rate | <SPEED> |     |     |     |     |
| ---------- | --------- | ------- | --- | --- | --- | --- |
| no console | baud-rate | <SPEED> |     |     |     |     |
Description
Setstheconsoleserialportspeed.
Thenoformofthiscommandresetstheconsoleportspeedtoitsdefaultof115200bps.
| Parameter |     |     |     |     | Description                                         |     |
| --------- | --- | --- | --- | --- | --------------------------------------------------- | --- |
| <SPEED>   |     |     |     |     | Selectstheconsoleportspeedinbps,either9600or115200. |     |
Usage
Thespeedchangeoccursimmediatelyfortheactiveconsolesession.Theconsolewillbeinaccessible
untiltheclientterminalsettingsareupdatedtomatchtheconsoleportspeedthatyouset.Afterthe
commandisexecutedyouwillbepromptedtologinagain.
Examples
Settingtheconsoleportspeedto9600bps:
switch(config)#
|     |     | console |     | baud-rate | 9600 |     |
| --- | --- | ------- | --- | --------- | ---- | --- |
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
domain-name
| domain-name    | <NAME> |          |     |     |     |     |
| -------------- | ------ | -------- | --- | --- | --- | --- |
| no domain-name |        | [<NAME>] |     |     |     |     |
Description
Specifiesthedomainnameoftheswitch.
Switchsystemandhardwarecommands|262

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
| front-panel-security    |               | factory-reset |     |
| ----------------------- | ------------- | ------------- | --- |
| front-panel-security    | factory-reset |               |     |
| no front-panel-security |               | factory-reset |     |
Description
Enablethefront-panel factory-resetfeaturetoallowafactoryresetviatheresetbuttononthefront
paneloftheswitch,withoutconsoleaccess.Oncethefeatureisenabled,thissettingwillbesavedacross
reboots,untilafactory-resetisperformed.Thenoformofthiscommanddisablesthefront-panel
factory-resetfeatureafterithasbeenenabled.Thisfeatureisdisabledbydefault.
Usage
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 263

Ifyouenablefront-panelfactory-resetfeature:
n pressingtheresetbuttonandreleasingitbefore5secondswillrebootthesystem.
n pressingtheresetbuttonandreleasingitbetween5to20secondswillstartahardresetofthe
system
n pressingtheresetbuttonandreleasingitbetween20to25secondswillstartahardresetofthe
system,andthesystemwillundergothefactoryresetprocess.
n pressingtheresetbuttonformorethan25secondswillnottriggeranyaction.
Ifthefront-panelfactory-resetfeatureisleftatitsdefaultdisabledsettingintherunningconfiguration:
n pressingtheresetbuttonandreleasingitbefore5secondswillrebootthesystem.
n pressingtheresetbuttonandreleasingitbetween5to20secondsmarkwillstartahardresetofthe
system.
n pressingtheresetbuttonformorethan20secondswillnottriggeranyaction.
FormoreinformationabouttheLEDindicatorsonthisswitch,refertotheInstallationGuideforyour
switch.
Example
| switch(config)# | front-panel-security |     | factory-reset |
| --------------- | -------------------- | --- | ------------- |
This command will enable front-panel factory reset capability, where user can
trigger factory-reset via reset button. This feature will remain enabled until
| it is disabled,     | or      | a factory-reset | is performed.                              |
| ------------------- | ------- | --------------- | ------------------------------------------ |
| Continue            | (y/n)?  |                 |                                            |
| Command History     |         |                 |                                            |
| Release             |         |                 | Modification                               |
| 10.14.1000          |         |                 | Commandsupportedon4100and6200SwitchSeries. |
| 10.13.1000          |         |                 | Commandintroduced                          |
| Command Information |         |                 |                                            |
| Platforms           | Command | context         | Authority                                  |
4100 config Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
hostname
hostname <HOSTNAME>
| no hostname | [<HOSTNAME>] |     |     |
| ----------- | ------------ | --- | --- |
Description
Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
Switchsystemandhardwarecommands|264

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
| power consumption-average-period |     |                     |     |
| -------------------------------- | --- | ------------------- | --- |
| power consumption-average-period |     | <PERIOD-IN-SECONDS> |     |
Description
Configuresatimeperiodforaveragepowerconsumptioninseconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PERIOD-IN-SECONDS> Specifiestheperiodinsecondsforaveragepowerconsumed.
Range:60-3600.Default:600
Formoreinformationonthisfeature,seethevideoAOS-CX10.14ReleaseUpdate:Sustainability
Update.
Example
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 265

Configuringatimeperiodof60secondsforaveragepowerconsumption:
| switch(config)#     | power   | consumption-average-period |                    | 60  |
| ------------------- | ------- | -------------------------- | ------------------ | --- |
| Command History     |         |                            |                    |     |
| Release             |         |                            | Modification       |     |
| 10.13               |         |                            | Commandintroduced. |     |
| Command Information |         |                            |                    |     |
| Platforms           | Command | context                    | Authority          |     |
4100i config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show boot-history |           |        |          |     |
| ----------------- | --------- | ------ | -------- | --- |
| show boot-history | [all|{vsf | member | <1-10>}] |     |
Description
Showsboothistoryinformation.Whennoparametersarespecified,showsthemostrecentinformation
aboutthecurrentbootoperation,andthethreepreviousbootoperationsfortheswitch.Whentheall
parameterisspecified,theoutputofthiscommandshowsthebootinformationfortheactive
managementmodule.
.
Toviewboot-historyonastandby,thecommandmustbesentontheconductorconsole.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
all
Optional.Showsbootinformationfortheactivemanagement
module.
vsf member <1-10> Optional.DisplayboothistoryforthespecifiedVSFmember
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Theoutputofthiscommandincludesthefollowinginformation:
| Parameter |     |     | Description                                  |     |
| --------- | --- | --- | -------------------------------------------- | --- |
| Index     |     |     | Thepositionofthebootinthehistoryfile.Range:0 |     |
to3.
Switchsystemandhardwarecommands|266

Parameter Description
Boot ID AuniqueIDfortheboot.Asystem-generated128-
bitstring.
Current Boot, up for <time> Forthecurrentboot,theshowboot-history
commandshowsthenumberofsecondsthe
modulehasbeenrunningonthecurrentsoftware.
<Timestamp>: boot reason Forpreviousbootoperations,theshowboot-
historycommandshowsthetimeatwhichthe
operationoccurredandthereasonfortheboot.
Thereasonforthebootisoneofthefollowing
values:
n <DAEMON-NAME>crash:Thedaemonidentified
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
| Command | History |     |     |     |
| ------- | ------- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 267

| Release        |             |         | Modification |     |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |             |         | --           |     |     |     |     |
| Command        | Information |         |              |     |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show capacities
| show capacities | <FEATURE> |     |     |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- | --- | --- |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description                       |     |     |     |     |
| --------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| <FEATURE> |     |     | Specifiesafeature.Forexample,aaa. |     |     |     |     |
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
Showingclassifier-relatedcapacitiesonthe6100:
| switch#            | show capacities | classifier |            |     |     |     |       |
| ------------------ | --------------- | ---------- | ---------- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter     | Classifier |     |     |     |       |
| Capacities         | Name            |            |            |     |     |     | Value |
----------------------------------------------------------------------------------
--
Maximum number of Access Control Entries configurable in a system
4096
Maximum number of Access Control Lists configurable in a system
512
| Maximum | number of class | entries | configurable |     | in  | a system |     |
| ------- | --------------- | ------- | ------------ | --- | --- | -------- | --- |
4096
| Maximum | number of classes |     | configurable | in  | a system |     |     |
| ------- | ----------------- | --- | ------------ | --- | -------- | --- | --- |
512
| Maximum | number of entries |     | in an Access | Control | List |     |     |
| ------- | ----------------- | --- | ------------ | ------- | ---- | --- | --- |
1024
| Maximum | number of entries |     | in a class |     |     |     |     |
| ------- | ----------------- | --- | ---------- | --- | --- | --- | --- |
1024
| Maximum | number of entries |     | in a policy |     |     |     |     |
| ------- | ----------------- | --- | ----------- | --- | --- | --- | --- |
64
| Maximum | number of classifier |     | policies | configurable |     | in a system |     |
| ------- | -------------------- | --- | -------- | ------------ | --- | ----------- | --- |
512
| Maximum | number of policy | entries | configurable |     | in  | a system |     |
| ------- | ---------------- | ------- | ------------ | --- | --- | -------- | --- |
4096
Switchsystemandhardwarecommands|268

Showingallavailablecapacitiesonthe6100:
| switch# show | capacities |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- |
System Capacities:
| Capacities Name |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
Value
----------------------------------------------------------------------------------
--------
Maximum number of Access Control Entries configurable in a system
4096
Maximum number of Access Control Lists configurable in a system
512
| Maximum number | of class | entries | configurable |     |     | in a | system |
| -------------- | -------- | ------- | ------------ | --- | --- | ---- | ------ |
4096
| Maximum number | of classes | configurable |     |     | in a | system |     |
| -------------- | ---------- | ------------ | --- | --- | ---- | ------ | --- |
512
| Maximum number | of entries | in  | an Access |     | Control | List |     |
| -------------- | ---------- | --- | --------- | --- | ------- | ---- | --- |
1024
| Maximum number | of entries | in  | a class |     |     |     |     |
| -------------- | ---------- | --- | ------- | --- | --- | --- | --- |
1024
| Maximum number | of entries | in  | a policy |     |     |     |     |
| -------------- | ---------- | --- | -------- | --- | --- | --- | --- |
64
| Maximum number | of classifier |     | policies | configurable |     |     | in a system |
| -------------- | ------------- | --- | -------- | ------------ | --- | --- | ----------- |
512
| Maximum number | of policy | entries |     | configurable |     | in  | a system |
| -------------- | --------- | ------- | --- | ------------ | --- | --- | -------- |
4096
Maximum number of clients supported for tracking the IP address in the system
128
| Maximum number | of dynamic | VLANs | that | can | be  | allowed | using MVRP |
| -------------- | ---------- | ----- | ---- | --- | --- | ------- | ---------- |
256
| Maximum number | of nexthops | per | IP  | ECMP | group |     |     |
| -------------- | ----------- | --- | --- | ---- | ----- | --- | --- |
1
Maximum number of IP neighbors (IPv4+IPv6) supported in the system
1024
Maximum number of IPv4 neighbors(# of ARP entries) supported in the system
1024
Maximum number of IPv6 neighbors(# of ND entries) supported in the system
512
| Maximum number | of L2 MAC | addresses |     | supported |     | in the | system |
| -------------- | --------- | --------- | --- | --------- | --- | ------ | ------ |
8192
| Maximum number | of L3 Groups |     | for IP | Tunnels | and | ECMP | Groups |
| -------------- | ------------ | --- | ------ | ------- | --- | ---- | ------ |
1
Maximum number of L3 Destinations for Routes, Nexthops in Tunnels and ECMP groups
1024
| Maximum number | of configurable |     | LAG | ports |     |     |     |
| -------------- | --------------- | --- | --- | ----- | --- | --- | --- |
8
| Maximum number | of members | supported |     | by  | a LAG | port |     |
| -------------- | ---------- | --------- | --- | --- | ----- | ---- | --- |
8
| Maximum number | of VLANs | across | ports | allowed |     | in loop-protect |     |
| -------------- | -------- | ------ | ----- | ------- | --- | --------------- | --- |
3328
| Maximum number | of IGMP/MLD | groups |     | supported |     |     |     |
| -------------- | ----------- | ------ | --- | --------- | --- | --- | --- |
512
| Maximum number | of IGMP/MLD | snooping |     | groups | supported |     |     |
| -------------- | ----------- | -------- | --- | ------ | --------- | --- | --- |
512
| Maximum number | of Mirror | Sessions |     | configurable |     | in  | a system |
| -------------- | --------- | -------- | --- | ------------ | --- | --- | -------- |
4
| Maximum number | of enabled | Mirror |     | Sessions | in  | a system |     |
| -------------- | ---------- | ------ | --- | -------- | --- | -------- | --- |
4
| Maximum number | of mstp | instances |     | configurable |     | in  | a system |
| -------------- | ------- | --------- | --- | ------------ | --- | --- | -------- |
16
| Maximum number | of Clients | that | can | be authenticated |     |     | on a port |
| -------------- | ---------- | ---- | --- | ---------------- | --- | --- | --------- |
32
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 269

Maximum number of Device Profiles allowed to be created on the system
8
Maximum number of Port Access Roles allowed to be created on the system
32
| Maximum number | of MAC | Address | that | can | be authorized | on a port |
| -------------- | ------ | ------- | ---- | --- | ------------- | --------- |
32
Maximum number of Port Access Role VLAN IDs allowed to be created on the system
50
Maximum number of Port Access Role VLAN names allowed to be created on the system
50
| Maximum number | of RBAC | rules | per user | group |     |     |
| -------------- | ------- | ----- | -------- | ----- | --- | --- |
1024
| Maximum number | of RPVST | VLANs | configurable |     | on the | system |
| -------------- | -------- | ----- | ------------ | --- | ------ | ------ |
16
| Maximum number | of RPVST | VPORTs | supported |     | in a system |     |
| -------------- | -------- | ------ | --------- | --- | ----------- | --- |
512
| Maximum number | of SVIs | supported | in  | the | system |     |
| -------------- | ------- | --------- | --- | --- | ------ | --- |
16
| Maximum number | of routes | (IPv4+IPv6) |     | on  | the system |     |
| -------------- | --------- | ----------- | --- | --- | ---------- | --- |
512
| Maximum number | of IPv4 | routes | on the | system |     |     |
| -------------- | ------- | ------ | ------ | ------ | --- | --- |
512
| Maximum number | of IPv6 | routes | on the | system |     |     |
| -------------- | ------- | ------ | ------ | ------ | --- | --- |
512
| Maximum number | of VLANs | supported |     | in the | system |     |
| -------------- | -------- | --------- | --- | ------ | ------ | --- |
512
System Capacities:
| Capacities Name |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
Value
----------------------------------------------------------------------------------
--------
Maximum number of Access Control Entries configurable in a system
4096
Maximum number of Access Control Lists configurable in a system
512
| Maximum number | of class | entries | configurable |     | in  | a system |
| -------------- | -------- | ------- | ------------ | --- | --- | -------- |
4096
| Maximum number | of classes | configurable |     |     | in a system |     |
| -------------- | ---------- | ------------ | --- | --- | ----------- | --- |
512
| Maximum number | of entries | in  | an Access |     | Control List |     |
| -------------- | ---------- | --- | --------- | --- | ------------ | --- |
1024
| Maximum number | of entries | in  | a class |     |     |     |
| -------------- | ---------- | --- | ------- | --- | --- | --- |
1024
| Maximum number | of entries | in  | a policy |     |     |     |
| -------------- | ---------- | --- | -------- | --- | --- | --- |
64
| Maximum number | of classifier |     | policies | configurable |     | in a system |
| -------------- | ------------- | --- | -------- | ------------ | --- | ----------- |
512
| Maximum number | of policy | entries | configurable |     | in  | a system |
| -------------- | --------- | ------- | ------------ | --- | --- | -------- |
4096
Maximum number of clients supported for tracking the IP address in the system
128
| Maximum number | of dynamic | VLANs | that | can | be allowed | using MVRP |
| -------------- | ---------- | ----- | ---- | --- | ---------- | ---------- |
256
| Maximum number | of nexthops |     | per IP | ECMP | group |     |
| -------------- | ----------- | --- | ------ | ---- | ----- | --- |
1
Maximum number of IP neighbors (IPv4+IPv6) supported in the system
1024
Maximum number of IPv4 neighbors(# of ARP entries) supported in the system
1024
Maximum number of IPv6 neighbors(# of ND entries) supported in the system
512
Switchsystemandhardwarecommands|270

| Maximum number | of L2 MAC | addresses |     | supported |     | in the | system |
| -------------- | --------- | --------- | --- | --------- | --- | ------ | ------ |
8192
| Maximum number | of L3 Groups |     | for | IP Tunnels |     | and ECMP | Groups |
| -------------- | ------------ | --- | --- | ---------- | --- | -------- | ------ |
1
Maximum number of L3 Destinations for Routes, Nexthops in Tunnels and ECMP groups
1024
| Maximum number | of configurable |     | LAG | ports |     |     |     |
| -------------- | --------------- | --- | --- | ----- | --- | --- | --- |
8
| Maximum number | of members | supported |     | by  | a LAG | port |     |
| -------------- | ---------- | --------- | --- | --- | ----- | ---- | --- |
8
| Maximum number | of VLANs | across | ports | allowed |     | in loop-protect |     |
| -------------- | -------- | ------ | ----- | ------- | --- | --------------- | --- |
3328
| Maximum number | of IGMP/MLD |     | groups | supported |     |     |     |
| -------------- | ----------- | --- | ------ | --------- | --- | --- | --- |
512
| Maximum number | of IGMP/MLD |     | snooping | groups |     | supported |     |
| -------------- | ----------- | --- | -------- | ------ | --- | --------- | --- |
512
| Maximum number | of Mirror | Sessions |     | configurable |     | in  | a system |
| -------------- | --------- | -------- | --- | ------------ | --- | --- | -------- |
4
| Maximum number | of enabled | Mirror |     | Sessions | in  | a system |     |
| -------------- | ---------- | ------ | --- | -------- | --- | -------- | --- |
4
| Maximum number | of mstp | instances |     | configurable |     | in  | a system |
| -------------- | ------- | --------- | --- | ------------ | --- | --- | -------- |
16
| Maximum number | of Clients | that | can | be  | authenticated |     | on a port |
| -------------- | ---------- | ---- | --- | --- | ------------- | --- | --------- |
32
Maximum number of Device Profiles allowed to be created on the system
8
Maximum number of Port Access Roles allowed to be created on the system
32
| Maximum number | of MAC | Address | that | can | be authorized |     | on a port |
| -------------- | ------ | ------- | ---- | --- | ------------- | --- | --------- |
32
Maximum number of Port Access Role VLAN IDs allowed to be created on the system
50
Maximum number of Port Access Role VLAN names allowed to be created on the system
50
| Maximum number | of RBAC | rules | per | user | group |     |     |
| -------------- | ------- | ----- | --- | ---- | ----- | --- | --- |
1024
| Maximum number | of RPVST | VLANs | configurable |     |     | on the | system |
| -------------- | -------- | ----- | ------------ | --- | --- | ------ | ------ |
16
| Maximum number | of RPVST | VPORTs | supported |     | in  | a system |     |
| -------------- | -------- | ------ | --------- | --- | --- | -------- | --- |
512
| Maximum number | of SVIs | supported |     | in the | system |     |     |
| -------------- | ------- | --------- | --- | ------ | ------ | --- | --- |
16
| Maximum number | of routes | (IPv4+IPv6) |     | on  | the | system |     |
| -------------- | --------- | ----------- | --- | --- | --- | ------ | --- |
512
| Maximum number | of IPv4 | routes | on  | the system |     |     |     |
| -------------- | ------- | ------ | --- | ---------- | --- | --- | --- |
512
| Maximum number | of IPv6 | routes | on  | the system |     |     |     |
| -------------- | ------- | ------ | --- | ---------- | --- | --- | --- |
512
| Maximum number | of VLANs | supported |     | in the | system |     |     |
| -------------- | -------- | --------- | --- | ------ | ------ | --- | --- |
512
| switch# show | capacities |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- |
System Capacities:
| Capacities Name |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
Value
----------------------------------------------------------------------------------
--------
Maximum number of Access Control Entries configurable in a system
4096
Maximum number of Access Control Lists configurable in a system
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 271

512
| Maximum number | of class | entries |     | configurable |     | in a | system |
| -------------- | -------- | ------- | --- | ------------ | --- | ---- | ------ |
4096
| Maximum number | of classes | configurable |     |     | in a | system |     |
| -------------- | ---------- | ------------ | --- | --- | ---- | ------ | --- |
512
| Maximum number | of entries | in  | an  | Access | Control | List |     |
| -------------- | ---------- | --- | --- | ------ | ------- | ---- | --- |
1024
| Maximum number | of entries | in  | a class |     |     |     |     |
| -------------- | ---------- | --- | ------- | --- | --- | --- | --- |
1024
| Maximum number | of entries | in  | a policy |     |     |     |     |
| -------------- | ---------- | --- | -------- | --- | --- | --- | --- |
64
| Maximum number | of classifier |     | policies | configurable |     |     | in a system |
| -------------- | ------------- | --- | -------- | ------------ | --- | --- | ----------- |
512
| Maximum number | of policy | entries |     | configurable |     | in  | a system |
| -------------- | --------- | ------- | --- | ------------ | --- | --- | -------- |
4096
Maximum number of clients supported for tracking the IP address in the system
128
| Maximum number | of dynamic | VLANs |     | that can | be  | allowed | using MVRP |
| -------------- | ---------- | ----- | --- | -------- | --- | ------- | ---------- |
256
| Maximum number | of nexthops |     | per IP | ECMP | group |     |     |
| -------------- | ----------- | --- | ------ | ---- | ----- | --- | --- |
1
Maximum number of IP neighbors (IPv4+IPv6) supported in the system
1024
Maximum number of IPv4 neighbors(# of ARP entries) supported in the system
1024
Maximum number of IPv6 neighbors(# of ND entries) supported in the system
512
| Maximum number | of L2 MAC | addresses |     | supported |     | in the | system |
| -------------- | --------- | --------- | --- | --------- | --- | ------ | ------ |
8192
| Maximum number | of L3 Groups |     | for | IP Tunnels | and | ECMP | Groups |
| -------------- | ------------ | --- | --- | ---------- | --- | ---- | ------ |
1
Maximum number of L3 Destinations for Routes, Nexthops in Tunnels and ECMP groups
1024
| Maximum number | of configurable |     | LAG | ports |     |     |     |
| -------------- | --------------- | --- | --- | ----- | --- | --- | --- |
8
| Maximum number | of members | supported |     | by  | a LAG | port |     |
| -------------- | ---------- | --------- | --- | --- | ----- | ---- | --- |
8
| Maximum number | of VLANs | across | ports | allowed |     | in loop-protect |     |
| -------------- | -------- | ------ | ----- | ------- | --- | --------------- | --- |
3328
| Maximum number | of IGMP/MLD |     | groups | supported |     |     |     |
| -------------- | ----------- | --- | ------ | --------- | --- | --- | --- |
512
| Maximum number | of IGMP/MLD |     | snooping | groups | supported |     |     |
| -------------- | ----------- | --- | -------- | ------ | --------- | --- | --- |
512
| Maximum number | of Mirror | Sessions |     | configurable |     | in  | a system |
| -------------- | --------- | -------- | --- | ------------ | --- | --- | -------- |
4
| Maximum number | of enabled | Mirror |     | Sessions | in  | a system |     |
| -------------- | ---------- | ------ | --- | -------- | --- | -------- | --- |
4
| Maximum number | of mstp | instances |     | configurable |     | in  | a system |
| -------------- | ------- | --------- | --- | ------------ | --- | --- | -------- |
16
| Maximum number | of Clients | that | can | be authenticated |     |     | on a port |
| -------------- | ---------- | ---- | --- | ---------------- | --- | --- | --------- |
32
Maximum number of Device Profiles allowed to be created on the system
8
Maximum number of Port Access Roles allowed to be created on the system
32
| Maximum number | of MAC | Address | that | can | be authorized |     | on a port |
| -------------- | ------ | ------- | ---- | --- | ------------- | --- | --------- |
32
Maximum number of Port Access Role VLAN IDs allowed to be created on the system
50
Maximum number of Port Access Role VLAN names allowed to be created on the system
50
| Maximum number | of RBAC | rules | per | user group |     |     |     |
| -------------- | ------- | ----- | --- | ---------- | --- | --- | --- |
Switchsystemandhardwarecommands|272

1024
| Maximum number | of RPVST | VLANs | configurable |     |     | on the | system |
| -------------- | -------- | ----- | ------------ | --- | --- | ------ | ------ |
16
| Maximum number | of RPVST | VPORTs | supported |     | in  | a system |     |
| -------------- | -------- | ------ | --------- | --- | --- | -------- | --- |
512
| Maximum number | of SVIs | supported |     | in the | system |     |     |
| -------------- | ------- | --------- | --- | ------ | ------ | --- | --- |
16
| Maximum number | of routes | (IPv4+IPv6) |     | on  | the | system |     |
| -------------- | --------- | ----------- | --- | --- | --- | ------ | --- |
512
| Maximum number | of IPv4 | routes | on  | the system |     |     |     |
| -------------- | ------- | ------ | --- | ---------- | --- | --- | --- |
512
| Maximum number | of IPv6 | routes | on  | the system |     |     |     |
| -------------- | ------- | ------ | --- | ---------- | --- | --- | --- |
512
| Maximum number | of VLANs | supported |     | in the | system |     |     |
| -------------- | -------- | --------- | --- | ------ | ------ | --- | --- |
512
System Capacities:
| Capacities Name |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
Value
----------------------------------------------------------------------------------
--------
Maximum number of Access Control Entries configurable in a system
4096
Maximum number of Access Control Lists configurable in a system
512
| Maximum number | of class | entries |     | configurable |     | in  | a system |
| -------------- | -------- | ------- | --- | ------------ | --- | --- | -------- |
4096
| Maximum number | of classes | configurable |     |     | in a | system |     |
| -------------- | ---------- | ------------ | --- | --- | ---- | ------ | --- |
512
| Maximum number | of entries | in  | an  | Access | Control | List |     |
| -------------- | ---------- | --- | --- | ------ | ------- | ---- | --- |
1024
| Maximum number | of entries | in  | a class |     |     |     |     |
| -------------- | ---------- | --- | ------- | --- | --- | --- | --- |
1024
| Maximum number | of entries | in  | a policy |     |     |     |     |
| -------------- | ---------- | --- | -------- | --- | --- | --- | --- |
64
| Maximum number | of classifier |     | policies |     | configurable |     | in a system |
| -------------- | ------------- | --- | -------- | --- | ------------ | --- | ----------- |
512
| Maximum number | of policy | entries |     | configurable |     | in  | a system |
| -------------- | --------- | ------- | --- | ------------ | --- | --- | -------- |
4096
Maximum number of clients supported for tracking the IP address in the system
128
| Maximum number | of dynamic | VLANs |     | that can | be  | allowed | using MVRP |
| -------------- | ---------- | ----- | --- | -------- | --- | ------- | ---------- |
256
| Maximum number | of nexthops |     | per IP | ECMP | group |     |     |
| -------------- | ----------- | --- | ------ | ---- | ----- | --- | --- |
1
Maximum number of IP neighbors (IPv4+IPv6) supported in the system
1024
Maximum number of IPv4 neighbors(# of ARP entries) supported in the system
1024
Maximum number of IPv6 neighbors(# of ND entries) supported in the system
512
| Maximum number | of L2 MAC | addresses |     | supported |     | in  | the system |
| -------------- | --------- | --------- | --- | --------- | --- | --- | ---------- |
8192
| Maximum number | of L3 Groups |     | for | IP Tunnels |     | and ECMP | Groups |
| -------------- | ------------ | --- | --- | ---------- | --- | -------- | ------ |
1
Maximum number of L3 Destinations for Routes, Nexthops in Tunnels and ECMP groups
1024
| Maximum number | of configurable |     | LAG | ports |     |     |     |
| -------------- | --------------- | --- | --- | ----- | --- | --- | --- |
8
| Maximum number | of members | supported |     | by  | a LAG | port |     |
| -------------- | ---------- | --------- | --- | --- | ----- | ---- | --- |
8
| Maximum number | of VLANs | across | ports | allowed |     | in  | loop-protect |
| -------------- | -------- | ------ | ----- | ------- | --- | --- | ------------ |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 273

3328
| Maximum | number of IGMP/MLD |     | groups | supported |     |     |     |     |
| ------- | ------------------ | --- | ------ | --------- | --- | --- | --- | --- |
512
| Maximum | number of IGMP/MLD |     | snooping | groups |     | supported |     |     |
| ------- | ------------------ | --- | -------- | ------ | --- | --------- | --- | --- |
512
| Maximum | number of Mirror | Sessions |     | configurable |     | in  | a system |     |
| ------- | ---------------- | -------- | --- | ------------ | --- | --- | -------- | --- |
4
| Maximum | number of enabled |     | Mirror | Sessions | in  | a system |     |     |
| ------- | ----------------- | --- | ------ | -------- | --- | -------- | --- | --- |
4
| Maximum | number of mstp | instances |     | configurable |     | in  | a system |     |
| ------- | -------------- | --------- | --- | ------------ | --- | --- | -------- | --- |
16
| Maximum | number of Clients |     | that | can be | authenticated |     | on a port |     |
| ------- | ----------------- | --- | ---- | ------ | ------------- | --- | --------- | --- |
32
Maximum number of Device Profiles allowed to be created on the system
8
Maximum number of Port Access Roles allowed to be created on the system
32
| Maximum | number of MAC | Address | that | can | be authorized |     | on a port |     |
| ------- | ------------- | ------- | ---- | --- | ------------- | --- | --------- | --- |
32
Maximum number of Port Access Role VLAN IDs allowed to be created on the system
50
Maximum number of Port Access Role VLAN names allowed to be created on the system
50
| Maximum | number of RBAC | rules | per | user | group |     |     |     |
| ------- | -------------- | ----- | --- | ---- | ----- | --- | --- | --- |
1024
| Maximum | number of RPVST | VLANs | configurable |     |     | on the | system |     |
| ------- | --------------- | ----- | ------------ | --- | --- | ------ | ------ | --- |
16
| Maximum | number of RPVST | VPORTs |     | supported | in  | a system |     |     |
| ------- | --------------- | ------ | --- | --------- | --- | -------- | --- | --- |
512
| Maximum | number of SVIs | supported |     | in the | system |     |     |     |
| ------- | -------------- | --------- | --- | ------ | ------ | --- | --- | --- |
16
| Maximum | number of routes | (IPv4+IPv6) |     | on  | the | system |     |     |
| ------- | ---------------- | ----------- | --- | --- | --- | ------ | --- | --- |
512
| Maximum | number of IPv4 | routes | on  | the system |     |     |     |     |
| ------- | -------------- | ------ | --- | ---------- | --- | --- | --- | --- |
512
| Maximum | number of IPv6 | routes | on  | the system |     |     |     |     |
| ------- | -------------- | ------ | --- | ---------- | --- | --- | --- | --- |
512
| Maximum | number of VLANs | supported |     | in the | system |     |     |     |
| ------- | --------------- | --------- | --- | ------ | ------ | --- | --- | --- |
512
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring |           |     |     |     |     |       |
| ------------------ | --------------- | --------- | --------- | --- | --- | --- | --- | ----- |
| System Capacities: | Filter          |           | Mirroring |     |     |     |     |       |
| Capacities         | Name            |           |           |     |     |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of Mirror | Sessions |     | configurable |     | in  | a system |     |
| ------- | ---------------- | -------- | --- | ------------ | --- | --- | -------- | --- |
4
| Maximum | number of enabled |     | Mirror | Sessions | in  | a system |     |     |
| ------- | ----------------- | --- | ------ | -------- | --- | -------- | --- | --- |
4
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp |      |     |     |     |     |       |
| ------------------ | --------------- | ---- | ---- | --- | --- | --- | --- | ----- |
| System Capacities: | Filter          |      | MSTP |     |     |     |     |       |
| Capacities         | Name            |      |      |     |     |     |     | Value |
Switchsystemandhardwarecommands|274

----------------------------------------------------------------------------------
-
| Maximum | number of | mstp instances | configurable | in a system |     |
| ------- | --------- | -------------- | ------------ | ----------- | --- |
64
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities | vlan-count  |       |     |       |
| ------------------ | --------------- | ----------- | ----- | --- | ----- |
| System Capacities: |                 | Filter VLAN | Count |     |       |
| Capacities         | Name            |             |       |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | VLANs supported | in the system |     |     |
| ------- | --------- | --------------- | ------------- | --- | --- |
4094
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show capacities-status
| show capacities-status |     | <FEATURE> |     |     |     |
| ---------------------- | --- | --------- | --- | --- | --- |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<FEATURE> Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplay
capacities,values,andstatus.Required.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
| switch#           | show capacities-status |        |     |     |       |
| ----------------- | ---------------------- | ------ | --- | --- | ----- |
| System Capacities |                        | Status |     |     |       |
| Capacities        | Status                 | Name   |     |     | Value |
Maximum
----------------------------------------------------------------------------------
----
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 275

|     | Number | of Access Control     |             | Entries    | currently  | configured |      | 0 4096 |
| --- | ------ | --------------------- | ----------- | ---------- | ---------- | ---------- | ---- | ------ |
|     | Number | of Access Control     |             | Lists      | currently  | configured |      | 0 512  |
|     | Number | of class entries      |             | currently  | configured |            |      | 0 4096 |
|     | Number | of classes            | currently   | configured |            |            |      | 0 512  |
|     | Number | of policies           | currently   |            | configured |            |      | 0 512  |
|     | Number | of policy entries     |             | currently  | configured |            |      | 0 4096 |
|     | Number | of dynamic            | VLANs       | currently  | learnt     | using      | MVRP | 0 256  |
|     | Number | of IP neighbor        | (IPv4+IPv6) |            | entries    |            |      | 1 1024 |
|     | Number | of IPv4 neighbor(ARP) |             |            | entries    |            |      | 1 1024 |
|     | Number | of IPv6 neighbor(ND)  |             | entries    |            |            |      | 0 512  |
Number of L3 Groups for IP Tunnels and ECMP Groups currently configured 0 1
Number of L3 Destinations for Routes, Nexthops in ECMP groups and
|                | Tunnels | currently             | configured |            |              |            |     | 0 1024 |
| -------------- | ------- | --------------------- | ---------- | ---------- | ------------ | ---------- | --- | ------ |
|                | Number  | of Mirror Sessions    |            | currently  |              | configured |     | 0 4    |
|                | Number  | of Mirror Sessions    |            | currently  |              | enabled    |     | 0 4    |
|                | Number  | of mstp instances     |            | currently  | configured   |            |     | 0 16   |
|                | Number  | of RPVST VLANs        | currently  |            | configured   |            |     | 0 16   |
|                | Number  | of routes (IPv4+IPv6) |            |            | currently    | configured |     | 1 512  |
|                | Number  | of IPv4 routes        | currently  |            | configured   |            |     | 1 512  |
|                | Number  | of IPv6 routes        | currently  |            | configured   |            |     | 0 512  |
|                | Number  | of VLANs currently    |            | configured |              |            |     | 1 512  |
| Command        |         | History               |            |            |              |            |     |        |
| Release        |         |                       |            |            | Modification |            |     |        |
| 10.07orearlier |         |                       |            |            | --           |            |     |        |
| Command        |         | Information           |            |            |              |            |     |        |
| Platforms      |         | Command               | context    |            | Authority    |            |     |        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
|         | switch#    | show console |     |     |                   |     |     |     |
| ------- | ---------- | ------------ | --- | --- | ----------------- | --- | --- | --- |
|         | Baud Rate: | 9600         |     |     |                   |     |     |     |
| Command |            | History      |     |     |                   |     |     |     |
| Release |            |              |     |     | Modification      |     |     |     |
| 10.08   |            |              |     |     | Commandintroduced |     |     |     |
Switchsystemandhardwarecommands|276

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
show core-dump all

Description

Shows core dump information about the specified module. When no parameters are specified, shows
only the core dumps generated in the current boot of the management module. When the all
parameter is specified, shows all available core dumps.

Parameter

Description

all

Usage

Shows all available core dumps.

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

switch# show core-dump
==================================================================================

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

277

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
| show deprecated          |     | commands    |     |     |     |     |     |
| ------------------------ | --- | ----------- | --- | --- | --- | --- | --- |
| show deprecated-commands |     | [<feature>] |     |     |     |     |     |
Description
Switchsystemandhardwarecommands|278

ShowsthelistofCLIcommandsthatwillbedeprecatedinafuturereleasealongwiththenewformof
thesamecommandwhichisrecommendedforuse.
Boththecommandoptionswillbesupporteduntilacertainrelease,afterwhichonlythenewer
replacementcommandwillbesupported.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
feature
Optional.
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
| Deprecated:  | vrrp <1-255> | address-family |         |     | (ipv4 | | ipv6) |
| ------------ | ------------ | -------------- | ------- | --- | ----- | ------- |
| Replacement: | vrrp <1-255> | address-family |         |     | (ip   | | ipv6) |
| Deprecated:  | show bgp     | ipv4           | unicast |     |       |         |
| Replacement: | show bgp     | ip unicast     |         |     |       |         |
...
| switch# show | deprecated-commands |     |     | vrrp |     |     |
| ------------ | ------------------- | --- | --- | ---- | --- | --- |
----------------------------------------------------------------------------------
-----------
The following commands with ipv4 keyword will be replaced with ip
----------------------------------------------------------------------------------
-----------
| Deprecated:  | vrrp <1-255> | address-family |        |         | (ipv4 | | ipv6)            |
| ------------ | ------------ | -------------- | ------ | ------- | ----- | ------------------ |
| Replacement: | vrrp <1-255> | address-family |        |         | (ip   | | ipv6)            |
| Deprecated:  | show vrrp    | (ipv4          | | ipv6 | |       | brief | | detail)(<1-255>) |
| Replacement: | show vrrp    | (ip            | | ipv6 | | brief | |     | detail)(<1-255>)   |
...
| switch# show        | deprecated-commands |     |           | vsf                |     |     |
| ------------------- | ------------------- | --- | --------- | ------------------ | --- | --- |
| Feature vsf         | has no deprecated   |     | commands. |                    |     |     |
| Command History     |                     |     |           |                    |     |     |
| Release             |                     |     |           | Modification       |     |     |
| 10.14               |                     |     |           | Commandintroduced. |     |     |
| Command Information |                     |     |           |                    |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 279

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show domain-name
show domain-name
Description
Showsthecurrentdomainname.
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
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| show environment |                             | fan |     |
| ---------------- | --------------------------- | --- | --- |
| show environment | fanisnotavailableforJL679A. |     |     |
| show environment | fan                         |     |     |
Description
Showsthestatusinformationforallfansandfantrays(ifpresent)inthesystem.
Usage
Switchsystemandhardwarecommands|280

Forfantrays,Statusisoneofthefollowingvalues:
n ready:Thefantrayisoperatingnormally.
n fault:Thefantrayisinafaultevent.Thestatusofthefantraydoesnotindicatethestatusoffans.
n empty:Thefantrayisnotinstalledinthesystem.
Forfans:
Speed: Indicates the relative speed of the fan based on the nominal speed range of the
fan.
| N/A:This | value | is  | not applicable |     | to  | the 6000 | or 6100. |     |
| -------- | ----- | --- | -------------- | --- | --- | -------- | -------- | --- |
Direction: The direction of airflow through the fan. Values are:
left-to-right:Air flows from the left of the system to the right of the system.
| N/A:The           | fan     | is not       | installed.     |           |           |                 |     |     |
| ----------------- | ------- | ------------ | -------------- | --------- | --------- | --------------- | --- | --- |
| Status: Fan       | status. |              | Values         | are:      |           |                 |     |     |
| uninitialized:The |         |              | fan has        | not       | completed | initialization. |     |     |
| ok: The           | fan     | is operating |                | normally. |           |                 |     |     |
| fault:            | The fan | is           | in a           | fault     | state.    |                 |     |     |
| empty:            | The fan | is           | not installed. |           |           |                 |     |     |
Examples
| switch#         | show | environment |     | fan |     |     |     |     |
| --------------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
| Fan information |      |             |     |     |     |     |     |     |
---------------------------------------------------------------------------
| Mbr/Fan |     | Product |     | Serial | Number | Speed | Direction | Status RPM |
| ------- | --- | ------- | --- | ------ | ------ | ----- | --------- | ---------- |
Name
---------------------------------------------------------------------------
| 1/1             |      | N/A         |     | N/A |     | N/A | left-to-right | ok N/A |
| --------------- | ---- | ----------- | --- | --- | --- | --- | ------------- | ------ |
| switch#         | show | environment |     | fan |     |     |               |        |
| Fan information |      |             |     |     |     |     |               |        |
---------------------------------------------------------------
| Fan | Serial | Number | Speed |     | Direction |     | Status | RPM |
| --- | ------ | ------ | ----- | --- | --------- | --- | ------ | --- |
---------------------------------------------------------------
| 1   | SGXXXXXXXXXX |     | slow   |     | front-to-back |     | ok    | 6000  |
| --- | ------------ | --- | ------ | --- | ------------- | --- | ----- | ----- |
| 2   | SGXXXXXXXXXX |     | normal |     | front-to-back |     | ok    | 8000  |
| 3   | SGXXXXXXXXXX |     | medium |     | front-to-back |     | ok    | 11000 |
| 4   | SGXXXXXXXXXX |     | fast   |     | front-to-back |     | ok    | 14000 |
| 5   | SGXXXXXXXXXX |     | max    |     | front-to-back |     | fault | 16500 |
| 6   | N/A          |     | N/A    |     | N/A           |     | empty |       |
...
| Command        | History     |         |     |         |              |     |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- | --- | --- |
| Release        |             |         |     |         | Modification |     |     |     |
| 10.07orearlier |             |         |     |         | --           |     |     |     |
| Command        | Information |         |     |         |              |     |     |     |
| Platforms      |             | Command |     | context | Authority    |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 281

| show environment |     | led |     |
| ---------------- | --- | --- | --- |
| show environment | led |     |     |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
Example
ShowingstateandstatusforLED:
| switch# show | environment | led    |     |
| ------------ | ----------- | ------ | --- |
| Mbr/Name     | State       | Status |     |
-------------------------------
| 1/locator           | off     | ok      |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show environment |                   | power-consumption |          |
| ---------------- | ----------------- | ----------------- | -------- |
| show environment | power-consumption |                   | [detail] |
Description
Displayspowerconsumptioninformation.
| Parameter   |     |     | Description                                   |
| ----------- | --- | --- | --------------------------------------------- |
| [detail}    |     |     | Displaysdetailedpowerconsumptioninformation.  |
| <MEMBER-ID> |     |     | ForVSFsupportedplatformsonly.Displaysthepower |
consumptioninformationforthespecifiedVSF member. Range:1-
10.
Usage
Powerconsumedvaluesareupdatedevery5seconds.Thetotalpowerconsumedisthetotalpower
usedinachassis.Thepowerconsumedaverageiscalculatedfromthetotalpowerconsumedasa
runningaverageoveraperiodoftime.Theaverageperiodhasadefaultof10minutes.Theperiodcan
beconfiguredusingpower-consumption-average-period.
Onchassiswherepowerinputisnotsupported,powerconsumedisdisplayedasPowerUsageandPSU
OutputPowerisdisplayedasN/A.
Switchsystemandhardwarecommands|282

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
Formoreinformation,seethevideoAOS-CX10.14ReleaseUpdate:SustainabilityUpdate.
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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 283

switch# show environment power-consumption
Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

Name Description
----------------------------------------------------------------------------
1

6410 v2 Chassis

Average

Instant

Average

Instant

900.00

798.00

803.23

905.62

Showing the power consumption for a switch with multiple line cards, in detail:

switch# show environment power-consumption detail
Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

1300.67

1499.99

Average

Instant

1307.00

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

803.40
880.25
805.00
950.00

830.00
875.00
802.00
921.00

Average

Instant

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

Instant

Instant

Average

300.00

280.00

275.50

299.50

Switch system and hardware commands | 284

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
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show environment |     | power-consumption |     |     | power-over- |
| ---------------- | --- | ----------------- | --- | --- | ----------- |
ethernet
| show environment | power | consumption | power-over-ethernet |     |     |
| ---------------- | ----- | ----------- | ------------------- | --- | --- |
show environment power-consumption power-over-ethernet detail <DETAIL>
show environment power-consumption power-over-ethernet member <MEMBER-ID>
show environment power-consumption power-over-ethernet interface <INTERFACE>
Description
DisplaysthePoEpowerconsumptioninformation.
| Parameter |     |     | Description                                       |     |     |
| --------- | --- | --- | ------------------------------------------------- | --- | --- |
| <DETAIL>  |     |     | DisplaysdetailedPoEpowerconsumptioninformation.   |     |     |
| <ARG-1>   |     |     | ForVSFsupportedplatformsonly.DisplaystheVSFmember |     |     |
command.
| <ARG-2> |     |     | ForVSFsupportedplatformsonly.Displaysthepower |     |     |
| ------- | --- | --- | --------------------------------------------- | --- | --- |
consumptioninformationforthespecifiedVSF member. Range:1-
10.
| INTERFACE |     |     | DisplaystheinterfacenamewithPoEcapability.       |     |     |
| --------- | --- | --- | ------------------------------------------------ | --- | --- |
| <MEMBER>  |     |     | ForVSFsupportedplatformsonly.DisplaysthePoEpower |     |     |
consumptionforastackmember.
Usage
ForeachPoEcapablemodule,thePoEpowerconsumedisdisplayed.PoEpowerconsumedvaluesare
collectedonceeverysamplingperiodandtheaveragevalueiscalculatedovertheaverageperiod.The
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 285

totalpowerconsumedisthetotalpowerofthePoEdevicesinachassis.TheaveragePoEpower
consumediscalculatedfromthetotalPoEpowerconsumedasarunningaverageoveraperiodoftime.
Thedefaultaverageperiodis10minutes.Theminimumaverageperiodcanbesetto60secondsand
maximumto3600seconds.Theaverageperiodcanbeconfiguredusingpower consumption-average-
period.ForVSFplatforms,thiscommanddisplaysthePoEpowerconsumedforallmembers.
Thefollowinginformationisprovidedforsummaryofpowerconsumption:
linemodule-PoEpowerusedbylinemodule
n
n chassismodule-PoEpowerusedbychassismodule
n PoEPowertotal-totalPoEpowerconsumption
n PoEPoweraverage-averagefortotalPoEpowerconsumptionthatiscalculatedoveragivenperiod
n averageperiod-timetocalculatepoweraverage
Example
ShowingthePOEinstantaneouspowerconsumptionforaswitch,inbrief:
| switch#           | show environment |           |     | power-consumption |       | power-over-ethernet |
| ----------------- | ---------------- | --------- | --- | ----------------- | ----- | ------------------- |
| Power Consumption |                  | Averaging |     | Period            | : 600 | seconds             |
|                   |                  |           |     |                   | PoE   | Average             |
| Name Description  |                  |           |     |                   |       | Usage (W)           |
--------------------------------------------------
| 1 6300M | 48SR10 | CL8 | PoE | 4p100G | Sw  | 401.41 |
| ------- | ------ | --- | --- | ------ | --- | ------ |
ShowingthePOEpowerconsumptionforaVSFstack,inbrief:
| switch#           | show environment |           |     | power-consumption |       | power-over-ethernet |
| ----------------- | ---------------- | --------- | --- | ----------------- | ----- | ------------------- |
| Power Consumption |                  | Averaging |     | Period            | : 120 | seconds             |
|                   |                  |           |     |                   | PoE   | Average             |
| Name Description  |                  |           |     |                   |       | Usage (W)           |
--------------------------------------------------
| 1 6300M | 24SR5 | CL6     | PoE    | 4SFP56 | Swc  | 23.86  |
| ------- | ----- | ------- | ------ | ------ | ---- | ------ |
| 2 6300M | 48G   | CL4 PoE | 4SFP56 |        | Swch | 11.27  |
| 3 6300F | 24G   | CL4 PoE | 4SFP56 |        | Sw   | 197.60 |
ShowingthePOEpowerconsumptionforachassis,inbrief:
| switch#           | show environment |           |     | power-consumption |       | power-over-ethernet |
| ----------------- | ---------------- | --------- | --- | ----------------- | ----- | ------------------- |
| Power Consumption |                  | Averaging |     | Period            | : 600 | seconds             |
|                   |                  |           |     |                   | PoE   | Average             |
| Name Description  |                  |           |     |                   |       | Usage (W)           |
--------------------------------------------------
| 1 6405 | Chassis |     |     |     |     | 120.11 |
| ------ | ------- | --- | --- | --- | --- | ------ |
ShowingthePOEpowerconsumptionforastandaloneswitch,indetail:
switch# show environment power-consumption power-over-ethernet detail
Switchsystemandhardwarecommands|286

| Power Consumption |     |     | Averaging | Period | : 600 | seconds   |
| ----------------- | --- | --- | --------- | ------ | ----- | --------- |
|                   |     |     |           |        | PoE   | Average   |
| Name Description  |     |     |           |        |       | Usage (W) |
--------------------------------------------------
| 1 6300M | 48SR10        |     | CL8 PoE   | 4p100G  | Sw  | 432.23 |
| ------- | ------------- | --- | --------- | ------- | --- | ------ |
| PoE     | Instantaneous |     |           | Average |     |        |
| Port    | Power         |     | (W) Power |         | (W) |        |
-----------------------------------
| 1/1/1 |     | 0.00 |     | 0.00 |     |     |
| ----- | --- | ---- | --- | ---- | --- | --- |
| 1/1/2 |     | 0.00 |     | 0.00 |     |     |
...
| 1/1/47 |     | 16.27 |     | 16.27 |     |     |
| ------ | --- | ----- | --- | ----- | --- | --- |
| 1/1/48 |     | 16.76 |     | 16.76 |     |     |
ShowingthePOEpowerconsumptionforachassis,indetail:
switch# show environment power-consumption power-over-ethernet detail
| Power Consumption |     |     | Averaging | Period | : 600 | seconds   |
| ----------------- | --- | --- | --------- | ------ | ----- | --------- |
|                   |     |     |           |        | PoE   | Average   |
| Name Description  |     |     |           |        |       | Usage (W) |
--------------------------------------------------
| 1 6405 | Chassis       |     |           |         |     | 542.49 |
| ------ | ------------- | --- | --------- | ------- | --- | ------ |
| PoE    | Instantaneous |     |           | Average |     |        |
| Port   | Power         |     | (W) Power |         | (W) |        |
-----------------------------------
| 1/3/1 |     | 0.00  |     | 0.00  |     |     |
| ----- | --- | ----- | --- | ----- | --- | --- |
| 1/3/2 |     | 15.56 |     | 15.56 |     |     |
...
| 1/7/23 |     | 1.59 |     | 1.59 |     |     |
| ------ | --- | ---- | --- | ---- | --- | --- |
| 1/7/24 |     | 0.00 |     | 0.00 |     |     |
ShowingthePOEpowerconsumptionfor3memberVSFstack,indetail:
switch# show environment power-consumption power-over-ethernet detail
| Power Consumption |     |     | Averaging | Period | : 120 | seconds   |
| ----------------- | --- | --- | --------- | ------ | ----- | --------- |
|                   |     |     |           |        | PoE   | Average   |
| Name Description  |     |     |           |        |       | Usage (W) |
--------------------------------------------------
| 1 6300M | 24SR5         | CL6 | PoE        | 4SFP56  | Swc  | 24.09  |
| ------- | ------------- | --- | ---------- | ------- | ---- | ------ |
| 2 6300M | 48G           | CL4 | PoE 4SFP56 |         | Swch | 11.26  |
| 3 6300F | 24G           | CL4 | PoE 4SFP56 |         | Sw   | 197.60 |
| PoE     | Instantaneous |     |            | Average |      |        |
| Port    | Power         |     | (W) Power  |         | (W)  |        |
-----------------------------------
| 1/1/1 |     | 1.54 |     | 1.54 |     |     |
| ----- | --- | ---- | --- | ---- | --- | --- |
| 1/1/2 |     | 0.00 |     | 0.00 |     |     |
...
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 287

| 2/1/1 |     | 3.21 |     | 3.21 |     |
| ----- | --- | ---- | --- | ---- | --- |
| 2/1/2 |     | 0.00 |     | 0.00 |     |
ShowingthePOEpowerconsumptionforVSFmember3:
switch# show environment power-consumption power-over-ethernet member 3
| Power Consumption |     | Averaging |     | Period : | 120 seconds |
| ----------------- | --- | --------- | --- | -------- | ----------- |
PoE Average
| Name Description |     |     |     |     | Usage (W) |
| ---------------- | --- | --- | --- | --- | --------- |
--------------------------------------------------
| 3 6300F | 24G           | CL4 PoE | 4SFP56 | Sw      | 197.60 |
| ------- | ------------- | ------- | ------ | ------- | ------ |
| PoE     | Instantaneous |         |        | Average |        |
| Port    | Power         | (W)     | Power  | (W)     |        |
-----------------------------------
| 3/1/1 |     | 14.07 |     | 14.07 |     |
| ----- | --- | ----- | --- | ----- | --- |
| 3/1/2 |     | 14.44 |     | 14.44 |     |
...
| 3/1/23 |     | 0.00 |     | 0.00 |     |
| ------ | --- | ---- | --- | ---- | --- |
| 3/1/24 |     | 0.00 |     | 0.00 |     |
ShowingthePOEpowerconsumptionforVSFinvalidmember:
switch# show environment power-consumption power-over-ethernet member 5
| Member 5 | is not | present |     |     |     |
| -------- | ------ | ------- | --- | --- | --- |
Showingtheinterfacespecifics:
switch# show environment power-consumption power-over-ethernet interface 3/1/1
| Power Consumption |               | Averaging |       | Period : | 60 seconds |
| ----------------- | ------------- | --------- | ----- | -------- | ---------- |
| PoE               | Instantaneous |           |       | Average  |            |
| Port              | Power         | (W)       | Power | (W)      |            |
-----------------------------------
| 3/1/1 |     | 14.07 |     | 14.07 |     |
| ----- | --- | ----- | --- | ----- | --- |
Showingtherangeofinterfaces:
switch# show environment power-consumption power-over-ethernet interface 3/1/1-
3/1/3,3/1/15
| Power Consumption |               | Averaging |       | Period : | 60 seconds |
| ----------------- | ------------- | --------- | ----- | -------- | ---------- |
| PoE               | Instantaneous |           |       | Average  |            |
| Port              | Power         | (W)       | Power | (W)      |            |
-----------------------------------
| 3/1/1  |     | 14.07 |     | 14.07 |     |
| ------ | --- | ----- | --- | ----- | --- |
| 3/1/2  |     | 14.44 |     | 14.44 |     |
| 3/1/3  |     | 14.09 |     | 14.09 |     |
| 3/1/15 |     | 14.44 |     | 14.44 |     |
Switchsystemandhardwarecommands|288

| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.14.1000          |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
4100i Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6000 | (#) |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6100
| show environment |              | power-supply |     |
| ---------------- | ------------ | ------------ | --- |
| show environment | power-supply |              |     |
Description
Showsstatusinformationaboutallpowersuppliesintheswitch.
Usage
Thefollowinginformationisprovidedforeachpowersupply:
| Parameter | Description |     |     |
| --------- | ----------- | --- | --- |
Mbr/PSU
Showsthememberandslotnumberofthepowersupply.
| Product Number | Showstheproductnumberofthepowersupply. |     |     |
| -------------- | -------------------------------------- | --- | --- |
Serial Number
Showstheserialnumberofthepowersupply,whichuniquelyidentifiesthepower
supply.
| PSU Status | Thestatusofthepowersupply.Valuesare: |                                    |     |
| ---------- | ------------------------------------ | ---------------------------------- | --- |
|            | n                                    | OK:Powersupplyisoperatingnormally. |     |
n OK*:Powersupplyisoperatingnormally,butitistheonlypowersupplyinthe
chassis.Onepowersupplyisnotsufficienttosupplyfullpowertotheswitch.When
thisvalueisshown,theoutputofthecommandalsoshowsamessageattheendof
thedisplayeddata.
|     | n   | Absent:Nopowersupplyisinstalledinthespecifiedslot.     |     |
| --- | --- | ------------------------------------------------------ | --- |
|     | n   | Inputfault:Thepowersupplyhasafaultconditiononitsinput. |     |
Outputfault:Thepowersupplyhasafaultconditiononitsoutput.
n
|     | n   | Warning:Thepowersupplyisnotoperatingnormally.             |     |
| --- | --- | --------------------------------------------------------- | --- |
|     | n   | WattageMaximum:Showsthemaximumamountofwattagethatthepower |     |
supplycanprovide.
Example
Showingtheoutputwhenonlyonepowersupplyisinstalledintheswitch:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 289

| switch# | show environment |        | power-supply |        |         |
| ------- | ---------------- | ------ | ------------ | ------ | ------- |
|         | Product          | Serial |              | PSU    | Wattage |
| Mbr/PSU | Number           | Number |              | Status | Maximum |
--------------------------------------------------------------
| 1/1            | N/A         | N/A |         | OK           | 500 |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| Command        | History     |     |         |              |     |
| Release        |             |     |         | Modification |     |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show environment |             |     | temperature |     |     |
| ---------------- | ----------- | --- | ----------- | --- | --- |
| show environment | temperature |     | [detail]    |     |     |
Description
Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
detail
Showsdetailedinformationfromeachtemperaturesensor.
Usage
TemperaturesareshowninCelsius.
Validvaluesforstatusarethefollowing:\
| Parameter    |     |     |     | Description                                        |     |
| ------------ | --- | --- | --- | -------------------------------------------------- | --- |
| normal       |     |     |     | Sensoriswithinnominaltemperaturerange.             |     |
| max          |     |     |     | Highesttemperaturefromthissensor.                  |     |
| low_critical |     |     |     | Lowestthresholdtemperatureforthissensor.           |     |
| critical     |     |     |     | Highestthresholdtemperatureforthissensor.          |     |
| fault        |     |     |     | Faulteventforthissensor.                           |     |
| emergency    |     |     |     | OvertemperatureeventforOvertemperatureeventforthis |     |
sensor.
Examples
Switchsystemandhardwarecommands|290

Showingcurrenttemperatureinformationfora6100switch:
| switch#     | show environment | temperature |     |     |     |
| ----------- | ---------------- | ----------- | --- | --- | --- |
| Temperature | information      |             |     |     |     |
------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     |     | Module Type | temperature | Status |
| --------------- | --- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-COMe-Daughter-Boar   |     |     | line-card-module | 66.45 C  | normal    |
| ------------------------ | --- | --- | ---------------- | -------- | --------- |
| 1/1-PCIE-Switch          |     |     | line-card-module | 95.82 C  | normal    |
| 1/1-Processor            |     |     | line-card-module | 00.00 C  | fault     |
| 1/1-Switch-ASIC          |     |     | line-card-module | 116.36 C | emergency |
| 1/1-Switch-ASIC-Internal |     |     | line-card-module | 108.25 C | critical  |
| 1/2-COMe-Daughter-Boar   |     |     | line-card-module | 67.29 C  | normal    |
| 1/2-PCIE-Switch          |     |     | line-card-module | 95.82 C  | normal    |
| 1/2-Processor-1          |     |     | line-card-module | 72.92 C  | normal    |
| 1/2-Processor-2          |     |     | line-card-module | 73.05 C  | normal    |
| 1/2-Switch-ASIC          |     |     | line-card-module | 97.41 C  | normal    |
| 1/2-Switch-ASIC-Internal |     |     | line-card-module | 97.62 C  | normal    |
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
| -n <COUNT>       | |          |              |     |     |     |
| ---------------- | ---------- | ------------ | --- | --- | --- |
| -i <MEMBER-SLOT> |            | |            |     |     |     |
| -m {active       | | standby} | |            |     |     |     |
| -c {lldp         | | ospf |   | ...} |       |     |     |     |
| -d {lldpd        | | bgpd |   | fand | ...}] |     |     |     |
Description
Showseventlogsgeneratedbytheswitchmodulessincethelastreboot.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
-e <EVENT-ID> ShowstheeventlogsforthespecifiedeventID.EventID
range:101through99999.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 291

| Parameter |     | Description |
| --------- | --- | ----------- |
-s {emergency | alert | critical | Showstheeventlogsforthespecifiedseverity.Selectthe
| error | warning | | notice | | severityfromthefollowinglist: |
| --------------- | ---------- | ----------------------------- |
info | debug}
n emergency:Displayseventlogswithseverityemergency
only.
n alert:Displayseventlogswithseverityalertandabove.
n critical:Displayseventlogswithseveritycriticalandabove.
n error:Displayseventlogswithseverityerrorandabove.
n warning:Displayseventlogswithseveritywarningand
above.
n notice:Displayseventlogswithseveritynoticeandabove.
n info:Displayseventlogswithseverityinfoandabove.
n debug:Displayseventlogswithallseverities.
-r
Showsthemostrecenteventlogsfirst.
| -a  |     | Showsalleventlogs,includingthoseeventsfromprevious |
| --- | --- | -------------------------------------------------- |
boots.
| -n <COUNT> |     | Displaysthespecifiednumberofeventlogs. |
| ---------- | --- | -------------------------------------- |
-c {lldp | ospf | ...} Showstheeventlogsforthespecifiedeventcategory.Enter
showevent-cforafulllistingofsupportedcategorieswith
descriptions.
-d {lldpd | bgpd | fand | ...} Showstheeventlogsforthespecifiedprocess.Entershow
event -dforafulllistingofsupporteddaemonswith
descriptions.
Examples
Showingeventlogs:
| switch# show events |     |     |
| ------------------- | --- | --- |
---------------------------------------------------
| show event logs |     |     |
| --------------- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for bridge_normal | interface |     |
| -------------------- | --------- | --- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
Showingthemostrecenteventlogsfirst:
| switch# show events | -r  |     |
| ------------------- | --- | --- |
---------------------------------------------------
| show event logs |     |     |
| --------------- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
in Hardware
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up for bridge_normal | interface |     |
| -------------------- | --------- | --- |
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Switchsystemandhardwarecommands|292

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 293

2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show front-panel-security |     |        | status |     |     |
| ------------------------- | --- | ------ | ------ | --- | --- |
| show front-panel-security |     | status |        |     |     |
Description
Displaystheconfigurationstatusofthefrontpanelfactoryresetfeatureandthetimestampofthefirst
occurrenceoffactoryresetusingtheresetbutton.
Example
Displaysthestatusofthefrontpanelfactoryresetfeature:
| switch# show | front-panel-security |       | status |           |     |
| ------------ | -------------------- | ----- | ------ | --------- | --- |
| Front panel  | factory              | reset |        | : enabled |     |
First occurrence of front-panel factory reset : Wed 2023-09-06 02:57:50 +08
Displaysthestatusofthefrontpanelfactoryresetfeature:
| switch# show     | front-panel-security |             | status        |           |                 |
| ---------------- | -------------------- | ----------- | ------------- | --------- | --------------- |
| Front panel      | factory              | reset       |               | : enabled | but unsupported |
| First occurrence | of                   | front-panel | factory reset | : NA      |                 |
Ifthestatusofthefeatureisdisplayedasenabled but unsupported,thenusersshouldissuethe
allow-unsafe-updatescommandandreboottheswitch.
| switch# config  |                      |     |     |     |     |
| --------------- | -------------------- | --- | --- | --- | --- |
| switch(config)# | allow-unsafe-updates |     | 30  |     |     |
This command will enable non-failsafe updates of programmable devices for
the next 30 minutes. You will first need to wait for all line and fabric
modules to reach the ready state, and then reboot the switch to begin
applying any needed updates. Ensure that the switch will not lose power,
Switchsystemandhardwarecommands|294

be rebooted again, or have any modules removed until all updates have
finished and all line and fabric modules have returned to the ready state.
WARNING: Interrupting these updates may make the product unusable!
| Continue            | (y/n)? y |           |                                            |              |            |
| ------------------- | -------- | --------- | ------------------------------------------ | ------------ | ---------- |
| Unsafe              | updates  | : allowed | (less than                                 | 30 minute(s) | remaining) |
| Command History     |          |           |                                            |              |            |
| Release             |          |           | Modification                               |              |            |
| 10.14.1000          |          |           | Commandsupportedon4100and6200SwitchSeries. |              |            |
| 10.13.1000          |          |           | Commandintroduced                          |              |            |
| Command Information |          |           |                                            |              |            |
| Platforms           | Command  | context   | Authority                                  |              |            |
4100 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6000 |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --------------------- | --- | --- |
6100
show hostname
show hostname
Description
Showsthecurrenthostname.
Example
Settingandshowingthehostname:
| switch# show | hostname |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- |
switch
| switch# config      |          |          |              |     |     |
| ------------------- | -------- | -------- | ------------ | --- | --- |
| switch(config)#     | hostname | myswitch |              |     |     |
| myswitch(config)#   | show     | hostname |              |     |     |
| Command History     |          |          |              |     |     |
| Release             |          |          | Modification |     |     |
| 10.07orearlier      |          |          | --           |     |     |
| Command Information |          |          |              |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 295

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show images
show images
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
Example
Showingtheprimaryandsecondaryimagesona6100switch:
| switch(config)# | show | images |     |
| --------------- | ---- | ------ | --- |
---------------------------------------------------------------------------
| AOS-CX | Primary Image |     |     |
| ------ | ------------- | --- | --- |
---------------------------------------------------------------------------
| Version | : PL.10.06.0002E |              |     |
| ------- | ---------------- | ------------ | --- |
| Size    | : 243 MB         |              |     |
| Date    | : 2020-11-25     | 22:00:47 PST |     |
SHA-256 : 61fe9233b2c842e8ac1731ad46949bd63e269c5c72d69290932ef19c1ebb0730
---------------------------------------------------------------------------
| AOS-CX | Secondary Image |     |     |
| ------ | --------------- | --- | --- |
---------------------------------------------------------------------------
| Version | : PL.10.07.0000E-201-gba0c336 |              |     |
| ------- | ----------------------------- | ------------ | --- |
| Size    | : 271 MB                      |              |     |
| Date    | : 2020-11-25                  | 21:09:08 UTC |     |
SHA-256 : 2fdfc646a8013efcca75729584bbb0fa54604086bad3f46e1c5d4e706b8b30ee
| Default      | Image : primary |             |     |
| ------------ | --------------- | ----------- | --- |
| Boot Profile | Timeout         | : 2 seconds |     |
---------------------------------------------------------------------------
| Management | Module | 1/1 (Active) |     |
| ---------- | ------ | ------------ | --- |
---------------------------------------------------------------------------
| Active         | Image       | : primary                |              |
| -------------- | ----------- | ------------------------ | ------------ |
| Service        | OS Version  | : PL.01.07.0003-internal |              |
| BIOS Version   |             | : PL.01.0001             |              |
| Command        | History     |                          |              |
| Release        |             |                          | Modification |
| 10.07orearlier |             |                          | --           |
| Command        | Information |                          |              |
| Platforms      | Command     | context                  | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Switchsystemandhardwarecommands|296

show module
show module

Description

Shows information about installed line modules and management modules.

Although this switch does not have removable modules, this command will still return information about the

switch, referring to management modules and line modules.

Usage

Identifies and shows status information about the line modules and management modules that are
installed in the switch.

To show the configuration information—if any—associated with that line module slot, use the show
running-configuration command.

Status is one of the following values:
Active
This is the active management module.
Deinitializing
The switch is being deinitialized.
Diagnostic
The switch is in a state used for troubleshooting.
Down
The switch is physically present but is powered down.
Failed
The switch has experienced an error and failed.
Initializing
The switch is being initialized.
Present
The switch hardware is installed in the chassis.
Ready
The switch is available for use.
Updating
A firmware update is being applied to the switch.

Examples

Showing all installed modules on a 6100 switch:

switch# show module

Management Modules
==================

Product

Name Number
---- ------- -------------------------------------- ---------- ----------------
1/1

SG0ZKW600P Active (local)

6100F 24G 4SFP+ Swch

Description

JL678A

Status

Line Modules
============

Product

Name Number
---- ------- -------------------------------------- ---------- ----------------
1/1

6100F 24G 4SFP+ Swch

SG0ZKW600P Ready

Description

JL678A

Status

Serial
Number

Serial
Number

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

297

| Management | Modules |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
==================
| Product     |             |     |     | Serial |        |
| ----------- | ----------- | --- | --- | ------ | ------ |
| Name Number | Description |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL678A   | 6100F | 24G 4SFP+ | Swch | SG0ZKW600P | Active (local) |
| ------------ | ----- | --------- | ---- | ---------- | -------------- |
| Line Modules |       |           |      |            |                |
============
| Product     |             |     |     | Serial |        |
| ----------- | ----------- | --- | --- | ------ | ------ |
| Name Number | Description |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL678A          | 6100F   | 24G 4SFP+ | Swch         | SG0ZKW600P | Ready |
| ------------------- | ------- | --------- | ------------ | ---------- | ----- |
| Command History     |         |           |              |            |       |
| Release             |         |           | Modification |            |       |
| 10.07orearlier      |         |           | --           |            |       |
| Command Information |         |           |              |            |       |
| Platforms           | Command | context   | Authority    |            |       |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |             |     |       |     |     |
| ------------------- | ----------- | --- | ----- | --- | --- |
| show running-config | [<FEATURE>] |     | [all] |     |     |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).
| all |     |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |     |     |
| --- | --- | --- | ------------------------------------------------------- | --- | --- |
Examples
Showingthecurrentrunningconfiguration:
| switch> show           | running-config |     |     |     |     |
| ---------------------- | -------------- | --- | --- | --- | --- |
| Current configuration: |                |     |     |     |     |
!
Switchsystemandhardwarecommands|298

| !Version AOS-CX   | PL.10.06.0001-346-g56a12a8f4cf15 |     |
| ----------------- | -------------------------------- | --- |
| !export-password: | default                          |     |
ntp enable
!
!
!
!
| ssh server | vrf default |     |
| ---------- | ----------- | --- |
vlan 1
spanning-tree
| spanning-tree   | instance | 1 vlan 1,2,4-10 |
| --------------- | -------- | --------------- |
| interface 1/1/1 |          |                 |
no shutdown
| vlan access     | 1           |     |
| --------------- | ----------- | --- |
| portfilter      | 1/1/2-1/1/3 |     |
| interface 1/1/2 |             |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/3 |     |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/4 |     |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/5 |     |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/6 |     |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/7 |     |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/8 |     |     |
no shutdown
| vlan access     | 1   |     |
| --------------- | --- | --- |
| interface 1/1/9 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/10 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/11 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/12 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/13 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/14 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/15 |     |     |
no shutdown
| vlan access      | 1   |     |
| ---------------- | --- | --- |
| interface 1/1/16 |     |     |
no shutdown
| vlan access    | 1   |     |
| -------------- | --- | --- |
| interface vlan | 1   |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 299

ip dhcp
| snmp-server    | vrf default  |                |     |
| -------------- | ------------ | -------------- | --- |
| snmp-server    | community    | public         |     |
| snmp-server    | host 1.1.1.1 | inform version | v2c |
| snmp-server    | host 1.1.1.1 | trap version   | v2c |
| snmpv3 context | A vrf        | default        |     |
!
!
!
!
!
| https-server | vrf default |     |     |
| ------------ | ----------- | --- | --- |
Showingthecurrentrunningconfigurationinjsonformat:
| switch> show          | running-config | json     |     |
| --------------------- | -------------- | -------- | --- |
| Running-configuration |                | in JSON: |     |
{
| "Monitoring_Policy_Script":        |                               | {   |     |
| ---------------------------------- | ----------------------------- | --- | --- |
| "system_resource_monitor_mm1.1.0": |                               |     | {   |
|                                    | "Monitoring_Policy_Instance": |     | {   |
"system_resource_monitor_mm1.1.0/system_resource_monitor_
| mm1.1.0.default": | {   |     |     |
| ----------------- | --- | --- | --- |
"name": "system_resource_monitor_mm1.1.0.default",
"origin": "system",
|     |     | "parameters_values": | {   |
| --- | --- | -------------------- | --- |
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
...
...
...
...
Showthecurrentrunningconfigurationwithoutdefaultvalues:
| switch(config)#        | show | running-config |     |
| ---------------------- | ---- | -------------- | --- |
| Current configuration: |      |                |     |
!
| !Version          | AOS-CX PL.10.06.0001-346-g56a12a8f4cf15 |     |     |
| ----------------- | --------------------------------------- | --- | --- |
| !export-password: | default                                 |     |     |
!
!
!
!
| ssh server | vrf default |     |     |
| ---------- | ----------- | --- | --- |
vlan 1
spanning-tree
| interface | 1/1/1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
Switchsystemandhardwarecommands|300

vlan access 1

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

!
!
!
!
!
https-server vrf default
switch#
switch#
g56a12a8f4cf15
!export-password: default
!
!
!
!

PL.10.06.0001-346-

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

301

ssh server vrf default
vlan 1
spanning-tree
interface 1/1/1
no shutdown
vlan access 1

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

!
!
!
!
!
https-server vrf default
switch#
switch#

Command History

Switch system and hardware commands | 302

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show running-config |     |                 | current-context |     |
| ------------------- | --- | --------------- | --------------- | --- |
| show running-config |     | current-context |                 |     |
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
(config)context,itshowstherunningconfigurationoftheentireswitch.Usetheshow running-
configurationcommandinstead.
Examples
Showingtherunningconfigurationforthecurrentinterface:
| switch(config-if)# |       | show    | running-config | current-context |
| ------------------ | ----- | ------- | -------------- | --------------- |
| interface          | 1/1/1 |         |                |                 |
| no shutdown        |       |         |                |                 |
| description        |       | Example | interface      |                 |
| vlan access        | 1     |         |                |                 |
exit
Showingthecurrentrunningconfigurationforthein-bandmanagementinterface:
| switch(config)# |     | interface | vlan | 1   |
| --------------- | --- | --------- | ---- | --- |
switch(config-if-vlan)#description IN-BAND Management Interface
| switch(config-if-vlan)#ip |     |     | dhcp     |     |
| ------------------------- | --- | --- | -------- | --- |
| switch(config-if-vlan)#no |     |     | shutdown |     |
switch(config-if-vlan)#end
switch#
Showingthecurrentrunningconfigurationforthein-bandmanagementinterfacewithoutDHCP:
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 303

| switch(config)# | interface | vlan | 1   |
| --------------- | --------- | ---- | --- |
switch(config-if-vlan)#description IN-BAND Management Interface
| switch(config-if-vlan)#no |     | ip dhcp  |                 |
| ------------------------- | --- | -------- | --------------- |
| switch(config-if-vlan)#ip |     | address  | 192.168.10.1/24 |
| switch(config-if-vlan)#no |     | shutdown |                 |
switch(config-if-vlan)#end
switch#
Showingtherunningconfigurationfortheexternalstoragesharenamednasfiles:
switch(config-external-storage-nasfiles)# show running-config current-context
| external-storage | nasfiles    |     |     |
| ---------------- | ----------- | --- | --- |
| address          | 192.168.0.1 |     |     |
| vrf default      |             |     |     |
| username         | nasuser     |     |     |
| password         | ciphertext  |     |     |
AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
| type scp  |           |     |     |
| --------- | --------- | --- | --- |
| directory | /home/nas |     |     |
enable
switch(config-external-storage-nasfiles)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
Showingthestartup-configurationinJSONformat:
Switchsystemandhardwarecommands|304

| switch# | show startup-config |     | json |
| ------- | ------------------- | --- | ---- |
| Startup | configuration:      |     |      |
{
| "AAA_Server_Group": |               | {   |         |
| ------------------- | ------------- | --- | ------- |
|                     | "local":      | {   |         |
|                     | "group_name": |     | "local" |
},
|     | "none":       | {   |        |
| --- | ------------- | --- | ------ |
|     | "group_name": |     | "none" |
}
},
...
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show        | system     |                  |     |
| ----------- | ---------- | ---------------- | --- |
| show system | [serviceos | password-prompt] |     |
Description
Showsgeneralstatusinformationaboutthesystem.
| Parameter |                 |     | Description |
| --------- | --------------- | --- | ----------- |
| serviceos | password-prompt |     |             |
ShowstheServiceOSpasswordpromptstatus.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemDescription,SystemContact,andSystemLocationcanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformation:
| switch#  | show system |     |                    |
| -------- | ----------- | --- | ------------------ |
| Hostname |             | :   | switch             |
| System   | Description | :   | switch description |
| System   | Contact     | :   | contact            |
| System   | Location    | :   | location           |
| Vendor   |             | :   | Aruba              |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 305

| Product  | Name          | : Xxxxxx        | ...      |            |     |     |     |
| -------- | ------------- | --------------- | -------- | ---------- | --- | --- | --- |
| Chassis  | Serial Nbr    | : XXXXXXXXXX    |          |            |     |     |     |
| Base     | MAC Address   | : xxxxxx-xxxxxx |          |            |     |     |     |
| AOS-CX   | Version       | : XX.99.99.9999 |          |            |     |     |     |
| Time     | Zone          | : UTC           |          |            |     |     |     |
| Up Time  |               | : 1 week,       | 5 hours, | 28 minutes |     |     |     |
| CPU Util | (%)           | : 5             |          |            |     |     |     |
| CPU Util | (% avg 1 min) | : 11            |          |            |     |     |     |
| CPU Util | (% avg 5 min) | : 10            |          |            |     |     |     |
| Memory   | Usage (%)     | : 35            |          |            |     |     |     |
ShowingtheServiceOSpasswordpromptstatus:
| switch#          | show system | serviceos | password-prompt |     |     |     |     |
| ---------------- | ----------- | --------- | --------------- | --- | --- | --- | --- |
| password-prompt: | disabled    |           |                 |     |     |     |     |
| Command          | History     |           |                 |     |     |     |     |
| Release          |             |           | Modification    |     |     |     |     |
10.12
|     |     |     | AddedCPU | Util (% avg | 1 min)andCPU | Util (% avg | 5   |
| --- | --- | --- | -------- | ----------- | ------------ | ----------- | --- |
min).
| 10.07orearlier |             |         | --        |     |     |     |     |
| -------------- | ----------- | ------- | --------- | --- | --- | --- | --- |
| Command        | Information |         |           |     |     |     |     |
| Platforms      | Command     | context | Authority |     |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show        | system resource-utilization |     |       |     |     |     |     |
| ----------- | --------------------------- | --- | ----- | --- | --- | --- | --- |
| show system | resource-utilization        |     | [all] |     |     |     |     |
Description
Showsthesystemresourceutilizationdata.
| Parameter |     | Description                                        |     |     |     |     |     |
| --------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| all       |     | Showstheresourceutilizationdatafortheentireswitch. |     |     |     |     |     |
Examples
Showingsystemresourceutilizationdata:
Switchsystemandhardwarecommands|306

switch#
| show | system | resource-utilization |     |     |     |     |
| ---- | ------ | -------------------- | --- | --- | --- | --- |
System Resources:
| Processes       |         |      |           | :      | 144 |     |
| --------------- | ------- | ---- | --------- | ------ | --- | --- |
| CPU usage(%)    |         |      |           | :      | 10  |     |
| CPU usage(%     | average | over | 1 minute) | :      | 11  |     |
| CPU usage(%     | average | over | 5 minute) | :      | 15  |     |
| Memory usage(%) |         |      |           | :      | 22  |     |
| Open FD's       |         |      |           | : 1358 |     |     |
Storage 1: Endurance utilization = 10-20% (mmc-type-a), 0-10% (mmc-type-b),
| Health            | = normal   |            |     |       |      |     |
| ----------------- | ---------- | ---------- | --- | ----- | ---- | --- |
| Data written      | to various | partitions |     | since | boot |     |
| Nos               | : 5 MB     |            |     |       |      |     |
| Log               | : 1 MB     |            |     |       |      |     |
| Coredump          | : 23 MB    |            |     |       |      |     |
| Security          | : 2 MB     |            |     |       |      |     |
| Selftest          | : 405 KB   |            |     |       |      |     |
| Swap              | : 14 MB    |            |     |       |      |     |
| Storage partition |            | usage(%)   |     |       |      |     |
| Nos               | : 5        |            |     |       |      |     |
| Log               | : 60       |            |     |       |      |     |
| Coredump          | : 23       |            |     |       |      |     |
| Security          | : 2        |            |     |       |      |     |
| Selftest          | : 1        |            |     |       |      |     |
| Swap              | : 0        |            |     |       |      |     |
Attemptingtoshowresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# show    | system      | resource-utilization |      |      |              |          |
| --------------- | ----------- | -------------------- | ---- | ---- | ------------ | -------- |
| System resource | utilization |                      | data | poll | is currently | disabled |
Showingsystemresourceutilizationdataforall:
| switch# show | system | resource-utilization |     |     | all |     |
| ------------ | ------ | -------------------- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| Resource | utilization | data | for Management |     | Module |     |
| -------- | ----------- | ---- | -------------- | --- | ------ | --- |
--------------------------------------------------------------------------
System Resources:
| Processes       |         |      |           | :      | 244 |     |
| --------------- | ------- | ---- | --------- | ------ | --- | --- |
| CPU usage(%)    |         |      |           | :      | 10  |     |
| CPU usage(%     | average | over | 1 minute) | :      | 11  |     |
| CPU usage(%     | average | over | 5 minute) | :      | 15  |     |
| Memory usage(%) |         |      |           | :      | 11  |     |
| Open FD's       |         |      |           | : 1854 |     |     |
Storage 1: Endurance utilization = 0-10% (mmc-type-a), 0-10% (mmc-type-b),
| Health       | = normal   |            |     |       |      |     |
| ------------ | ---------- | ---------- | --- | ----- | ---- | --- |
| Data written | to various | partitions |     | since | boot |     |
| Nos          | : 15 MB    |            |     |       |      |     |
| Log          | : 1 MB     |            |     |       |      |     |
| Coredump     | : 23 MB    |            |     |       |      |     |
| Security     | : 2 MB     |            |     |       |      |     |
| Selftest     | : 405 KB   |            |     |       |      |     |
| Swap         | : 0 KB     |            |     |       |      |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 307

| Storage  | partition usage(%) |     |                                                 |
| -------- | ------------------ | --- | ----------------------------------------------- |
| Nos      | : 5                |     |                                                 |
| Log      | : 60               |     |                                                 |
| Coredump | : 23               |     |                                                 |
| Security | : 2                |     |                                                 |
| Selftest | : 1                |     |                                                 |
| Swap     | : 0                |     |                                                 |
| Command  | History            |     |                                                 |
| Release  |                    |     | Modification                                    |
| 10.12    |                    |     | TheoutputofthiscommandincludesCPUusage(%average |
over1minute)andCPUusage(%averageover5minute).
| 10.07orearlier |             |         | --        |
| -------------- | ----------- | ------- | --------- |
| Command        | Information |         |           |
| Platforms      | Command     | context | Authority |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | tech                |              |     |
| --------- | ------------------- | ------------ | --- |
| show tech | [basic | <FEATURE>] | [local-file] |     |
Description
Showsdetailedinformationaboutswitchfeaturesbyautomaticallyrunningtheshowcommands
associatedwiththefeature.Ifnoparametersarespecified,theshow techcommandshowsinformation
aboutallswitchfeatures.Technicalsupportpersonnelusetheoutputfromthiscommandfor
troubleshooting.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
basic
Specifiesshowingabasicsetofinformation.
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow techcommand,followedbyaspace,followedbya
questionmark(?).
local-file Showstheoutputoftheshow techcommandtoalocaltextfile.
Usage
| Toterminatetheoutputoftheshow |     | techcommand,enterCtrl+C. |     |
| ----------------------------- | --- | ------------------------ | --- |
IfthecommandwasnotterminatedwithCtrl+C,attheendoftheoutput,theshow techcommand
showsthefollowing:
Switchsystemandhardwarecommands|308

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
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 309

show usb
Description
ShowstheUSBportconfigurationandmountsettings.
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
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show usb             | file-system |     |     |
| -------------------- | ----------- | --- | --- |
| show usb file-system | [<PATH>]    |     |     |
Description
ShowsdirectorylistingsforamountedUSBdevice.Whenenteredwithoutthe<PATH>parameterthe
topleveldirectorytreeisshown.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PATH> Specifiesthefilepathtoshow.Aleading"/"inthepathisoptional.
Switchsystemandhardwarecommands|310

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
| switch#        | show usb file-system | dir1/../..   |     |
| -------------- | -------------------- | ------------ | --- |
| Invalid        | path argument        |              |     |
| Command        | History              |              |     |
| Release        |                      | Modification |     |
| 10.07orearlier |                      | --           |     |
| Command        | Information          |              |     |
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 311

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show version
show version
Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
Example
Showingversioninformationfora4100iswitch:
| DocTeam-4100i# | show | version |     |
| -------------- | ---- | ------- | --- |
-----------------------------------------------------------------------------
ArubaOS-CX
(c) Copyright 2017-2023 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version    | : RL.10.13.1000S |          |     |
| ---------- | ---------------- | -------- | --- |
| Build Date | : 2023-11-15     | 15:29:10 | UTC |
Build ID : ArubaOS-CX:RL.10.13.1000S:ac4c3941a38c:202311151508
| Build SHA    | : ac4c3941a38c5d66f8f0212706af8f35fa01adfd |                 |     |
| ------------ | ------------------------------------------ | --------------- | --- |
| Hot Patches  | :                                          |                 |     |
| Active Image | : secondary                                |                 |     |
| Service      | OS Version                                 | : RL.01.09.0003 |     |
| BIOS Version |                                            | : RL.01.0003    |     |
Showingversioninformationfora6100switch:
| switch(config)# | show | version |     |
| --------------- | ---- | ------- | --- |
-----------------------------------------------------------------------------
AOS-CX
(c) Copyright 2017-2022 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version        | : PL.10.xx.xxxxx                                  |                  |              |
| -------------- | ------------------------------------------------- | ---------------- | ------------ |
| Build Date     | : 2022-05-27                                      | 17:00:46         | PDT          |
| Build ID       | : AOS-CX:PL©10.xx.xxxxx:9e8bf51170a6:202012062115 |                  |              |
| Build SHA      | : 9e8bf51170a602370f12e0bde814e8d8f49bf706        |                  |              |
| Active Image   | : secondary                                       |                  |              |
| Service        | OS Version                                        | : PL.10.xx.xxxxx |              |
| BIOS Version   |                                                   | : PL.01.0002     |              |
| Command        | History                                           |                  |              |
| Release        |                                                   |                  | Modification |
| 10.07orearlier |                                                   |                  | --           |
| Command        | Information                                       |                  |              |
Switchsystemandhardwarecommands|312

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
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
Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch# | top cpu |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 313

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
| Command        | History     |     |     |     |              |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| Release        |             |     |     |     | Modification |     |     |     |     |
| 10.07orearlier |             |     |     |     | --           |     |     |     |     |
| Command        | Information |     |     |     |              |     |     |     |     |
Switchsystemandhardwarecommands|314

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
EnablesordisablestheinsertedUSBdrive.
AOS-CX10.15.xxxxFundamentalsGuide|(4100i,6000,6100SwitchSeries) 315

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
Switchsystemandhardwarecommands|316

Chapter 17

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.hpe.com/us/en/networking/hpe-aruba-networking-
support-services.html

AOS-CX Switch Software Documentation
Portal

https://arubanetworking.hpe.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1-800-943-4526 (US & Canada Toll-Free Number)

+1-650-750-0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

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

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

Videos on new features introduced in this release:

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

AOS-CX

Software

Technical

Update channel

on YouTube.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

317

HPE Aruba https://arubanetworking.hpe.com/techdocs/hardware/DocumentationPortal/Content/home.
| Networking | htmm |     |
| ---------- | ---- | --- |
Hardware
Documentation
andTranslations
Portal
| HPE Aruba | https://networkingsupport.hpe.com/downloads |     |
| --------- | ------------------------------------------- | --- |
Networking
software
| Software | https://licensemanagement.hpe.com/ |     |
| -------- | ---------------------------------- | --- |
licensingand
FeaturePacks
| End-of-Life | https://networkingsupport.hpe.com/end-of-life |     |
| ----------- | --------------------------------------------- | --- |
information
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheHPE ArubaNetworkingSupportPortalat
https://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveHPE ArubaNetworking
SupportPortalaccounttomanagesubscriptions).SecuritynoticesareviewablewithoutanHPE Aruba
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
HPE ArubaNetworkingiscommittedtoprovidingourcustomerswithinformationaboutthechemical
substancesinourproductsasneededtocomplywithlegalrequirements,environmentaldata(company
programs,productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSand
WEEE).Formoreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-
citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
HPE ArubaNetworkingiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpus
improvethedocumentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback
SupportandOtherResources|318

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.15.xxxx Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

319