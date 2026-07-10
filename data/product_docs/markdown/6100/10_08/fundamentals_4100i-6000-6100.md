AOS-CX 10.08 Fundamentals
Guide

4100i, 6000, 6100 Switch Series

Published: September 2021
Edition: 2

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
For more information, see the KM Process Guide. ?>
Acknowledgments

Bluetooth is a trademark owned by its proprietor and used by Hewlett Packard Enterprise under license.

| 2

Contents
Contents
| Contents                                   |                                      | 3   |
| ------------------------------------------ | ------------------------------------ | --- |
| About this                                 | document                             | 9   |
| Applicableproducts                         |                                      | 9   |
| Latestversionavailableonline               |                                      | 9   |
| Commandsyntaxnotationconventions           |                                      | 9   |
| Abouttheexamples                           |                                      | 10  |
| Identifyingswitchportsandinterfaces        |                                      | 10  |
| About AOS-CX                               |                                      | 12  |
| AOS-CXsystemdatabases                      |                                      | 12  |
| ArubaNetworkAnalyticsEngineintroduction    |                                      | 12  |
| AOS-CXCLI                                  |                                      | 13  |
| ArubaNetEdit                               |                                      | 13  |
| Ansiblemodules                             |                                      | 13  |
| AOS-CXWebUI                                |                                      | 13  |
| AOS-CXRESTAPI                              |                                      | 14  |
| In-bandmanagement                          |                                      | 14  |
| SNMP-basedmanagementsupport                |                                      | 14  |
| Useraccounts                               |                                      | 14  |
| Initial Configuration                      |                                      | 16  |
| InitialconfigurationusingZTP               |                                      | 16  |
| InitialconfigurationusingtheCLI            |                                      | 16  |
|                                            | Connectingtotheconsoleport           | 17  |
|                                            | Connectingtothein-bandmanagementport | 17  |
|                                            | ConfigureusingDHCPorstaticIP         | 18  |
|                                            | Loggingintotheswitchforthefirsttime  | 19  |
|                                            | SettingswitchtimeusingtheNTPclient   | 19  |
| Configuringbanners                         |                                      | 20  |
| UsingtheWebUI                              |                                      | 20  |
| Configuringthein-bandmanagementinterface   |                                      | 21  |
| Restoringtheswitchtofactorydefaultsettings |                                      | 21  |
| NTPcommands                                |                                      | 23  |
|                                            | ntpauthentication                    | 23  |
|                                            | ntpauthentication-key                | 24  |
|                                            | ntpdisable                           | 25  |
|                                            | ntpenable                            | 26  |
|                                            | ntpserver                            | 27  |
|                                            | ntptrusted-key                       | 28  |
|                                            | ntpvrf                               | 29  |
|                                            | showntpassociations                  | 30  |
|                                            | showntpauthentication-keys           | 31  |
|                                            | showntpservers                       | 32  |
|                                            | showntpstatistics                    | 32  |
|                                            | showntpstatus                        | 33  |
| Interfaces                                 |                                      | 35  |
| Configuringalayer2interface                |                                      | 35  |
3
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| SinglesourceIPaddress                           |                                     |            | 35  |
| ----------------------------------------------- | ----------------------------------- | ---------- | --- |
| Unsupportedtransceiversupport                   |                                     |            | 35  |
| Interfacecommands                               |                                     |            | 36  |
| allow-unsupported-transceiver                   |                                     |            | 36  |
| defaultinterface                                |                                     |            | 37  |
| description                                     |                                     |            | 38  |
| energy-efficient-ethernet                       |                                     |            | 39  |
| flow-control                                    |                                     |            | 39  |
| interface                                       |                                     |            | 40  |
| interfacevlan                                   |                                     |            | 41  |
| ipaddress                                       |                                     |            | 41  |
| ipmtu                                           |                                     |            | 42  |
| ipsource-interface                              |                                     |            | 43  |
| ipv6address                                     |                                     |            | 44  |
| ipv6source-interface                            |                                     |            | 45  |
| mtu                                             |                                     |            | 46  |
| showallow-unsupported-transceiver               |                                     |            | 47  |
| showinterface                                   |                                     |            | 48  |
| showinterfacedom                                |                                     |            | 51  |
| showinterfaceenergy-efficientethernet           |                                     |            | 51  |
| showinterfaceflow-control                       |                                     |            | 52  |
| showinterfacetransceiver                        |                                     |            | 54  |
| showipinterface                                 |                                     |            | 56  |
| showipsource-interface                          |                                     |            | 57  |
| showipv6interface                               |                                     |            | 58  |
| showipv6source-interface                        |                                     |            | 59  |
| shutdown                                        |                                     |            | 59  |
| Source interface                                | selection                           |            | 61  |
| Source-interfaceselectioncommands               |                                     |            | 61  |
| ipsource-interface                              |                                     |            | 61  |
| ipsource-interfaceinterface                     |                                     |            | 63  |
| ipv6source-interface                            |                                     |            | 64  |
| ipv6source-interfaceinterface                   |                                     |            | 65  |
| showipsource-interface                          |                                     |            | 67  |
| showipv6source-interface                        |                                     |            | 68  |
| showrunning-config                              |                                     |            | 70  |
| VLANs                                           |                                     |            | 72  |
| Configuration                                   | and firmware                        | management | 73  |
| Checkpoints                                     |                                     |            | 73  |
| Checkpointtypes                                 |                                     |            | 73  |
| Maximumnumberofcheckpoints                      |                                     |            | 73  |
| Usergeneratedcheckpoints                        |                                     |            | 73  |
| Systemgeneratedcheckpoints                      |                                     |            | 73  |
| Supportedremotefileformats                      |                                     |            | 73  |
| Rollback                                        |                                     |            | 74  |
| Checkpointautomode                              |                                     |            | 74  |
| Testingaswitchconfigurationincheckpointautomode |                                     |            | 74  |
| Checkpointcommands                              |                                     |            | 74  |
|                                                 | checkpointauto                      |            | 74  |
|                                                 | checkpointautoconfirm               |            | 75  |
|                                                 | checkpointdiff                      |            | 76  |
|                                                 | checkpointpost-configuration        |            | 77  |
|                                                 | checkpointpost-configurationtimeout |            | 78  |
Contents|4

|     | checkpointrename                            | 79  |
| --- | ------------------------------------------- | --- |
|     | checkpointrollback                          | 80  |
|     | copycheckpoint<CHECKPOINT-NAME><REMOTE-URL> | 80  |
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config} 81
|     | copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>    | 82  |
| --- | ----------------------------------------------- | --- |
|     | copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>     | 83  |
|     | copy<REMOTE-URL>{running-config|startup-config} | 84  |
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>} 85
|                             | copy{running-config|startup-config}<REMOTE-URL>       | 86  |
| --------------------------- | ----------------------------------------------------- | --- |
|                             | copy{running-config|startup-config}<STORAGE-URL>      | 87  |
|                             | copystartup-configrunning-config                      | 88  |
|                             | copy<STORAGE-URL>running-config                       | 89  |
|                             | erase{checkpoint<CHECKPOINT-NAME>|startup-config|all} | 90  |
|                             | showcheckpoint<CHECKPOINT-NAME>                       | 91  |
|                             | showcheckpoint<CHECKPOINT-NAME>hash                   | 93  |
|                             | showcheckpointpost-configuration                      | 94  |
|                             | showcheckpoint                                        | 95  |
|                             | showcheckpointdate                                    | 96  |
|                             | showrunning-confighash                                | 96  |
|                             | showstartup-confighash                                | 97  |
|                             | writememory                                           | 98  |
| Bootcommands                |                                                       | 99  |
|                             | bootset-default                                       | 99  |
|                             | bootsystem                                            | 99  |
|                             | showboot-history                                      | 101 |
| Firmwaremanagementcommands  |                                                       | 102 |
|                             | copy{primary|secondary}<REMOTE-URL>                   | 102 |
|                             | copy{primary|secondary}<FIRMWARE-FILENAME>            | 103 |
|                             | copyprimarysecondary                                  | 104 |
|                             | copy<REMOTE-URL>                                      | 105 |
|                             | copysecondaryprimary                                  | 106 |
|                             | copy<STORAGE-URL>                                     | 107 |
| Dynamic                     | Segmentation                                          | 109 |
| User-basedtunneling         |                                                       | 109 |
| User-basedtunnelingcommands |                                                       | 113 |
|                             | backup-controllerip                                   | 113 |
|                             | enable                                                | 114 |
|                             | ipsource-interface                                    | 114 |
|                             | papi-security-key                                     | 115 |
|                             | primary-controllerip                                  | 117 |
|                             | sac-heartbeat-interval                                | 117 |
|                             | showipsource-interfaceubt                             | 118 |
|                             | showcapacitiesubt                                     | 119 |
|                             | showubt                                               | 120 |
|                             | showubtinformation                                    | 121 |
|                             | showubtstate                                          | 123 |
|                             | showubtstatistics                                     | 126 |
|                             | showubtusers                                          | 130 |
|                             | uac-keepalive-interval                                | 132 |
|                             | ubt                                                   | 133 |
|                             | ubt-client-vlan                                       | 134 |
|                             | ubtmodevlan-extend                                    | 135 |
| SNMP                        |                                                       | 136 |
| ConfiguringSNMP             |                                                       | 136 |
5
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Aruba Central                             | integration                                              | 138 |
| ----------------------------------------- | -------------------------------------------------------- | --- |
| ConnectingtoArubaCentral                  |                                                          | 138 |
| CustomCAcertificate                       |                                                          | 138 |
| SupportmodeinArubaCentral                 |                                                          | 139 |
| ArubaCentralcommands                      |                                                          | 139 |
| aruba-central                             |                                                          | 139 |
| aruba-centralsupport-mode                 |                                                          | 140 |
| configuration-lockoutcentralmanaged       |                                                          | 141 |
| disable                                   |                                                          | 142 |
| enable                                    |                                                          | 142 |
| location-override                         |                                                          | 143 |
| showaruba-central                         |                                                          | 144 |
| showrunning-configcurrent-context         |                                                          | 145 |
| Port filtering                            |                                                          | 147 |
| Portfilteringcommands                     |                                                          | 147 |
| portfilter                                |                                                          | 147 |
| showportfilter                            |                                                          | 148 |
| DNS                                       |                                                          | 150 |
| DNSclient                                 |                                                          | 150 |
| ConfiguringtheDNSclient                   |                                                          | 150 |
| DNSclientcommands                         |                                                          | 151 |
| ipdnsdomain-list                          |                                                          | 151 |
| ipdnsdomain-name                          |                                                          | 152 |
| ipdnshost                                 |                                                          | 152 |
| ipdnsserveraddress                        |                                                          | 153 |
| showipdns                                 |                                                          | 154 |
| Device discovery                          | and configuration                                        | 156 |
| Deviceprofiles                            |                                                          | 156 |
| ConfiguringadeviceprofileforLLDP          |                                                          | 157 |
| ConfiguringadeviceprofileforCDP           |                                                          | 157 |
| ConfiguringadeviceprofileforlocalMACmatch |                                                          | 157 |
| Deviceprofilecommands                     |                                                          | 158 |
|                                           | aaaauthenticationport-accessallow-cdp-bpdu               | 158 |
|                                           | aaaauthenticationport-accessallow-lldp-bpdu              | 159 |
|                                           | associatecdp-group                                       | 161 |
|                                           | associatelldp-group                                      | 161 |
|                                           | associatemac-group                                       | 162 |
|                                           | associaterole                                            | 163 |
|                                           | disable                                                  | 164 |
|                                           | enable                                                   | 164 |
|                                           | ignore(forCDPgroups)                                     | 165 |
|                                           | ignore(forLLDPgroups)                                    | 166 |
|                                           | ignore(forMACgroups)                                     | 167 |
|                                           | mac-group                                                | 173 |
|                                           | match(forCDPgroups)                                      | 173 |
|                                           | match(forLLDPgroups)                                     | 175 |
|                                           | match(forMACgroups)                                      | 176 |
|                                           | port-accesscdp-group                                     | 180 |
|                                           | port-accessdevice-profile                                | 181 |
|                                           | port-accessdevice-profilemodeblock-until-profile-applied | 182 |
|                                           | port-accesslldp-group                                    | 183 |
|                                           | showport-accessdevice-profile                            | 184 |
| LLDP                                      |                                                          | 185 |
Contents|6

|                               | LLDPagent                   |          | 186 |
| ----------------------------- | --------------------------- | -------- | --- |
|                               | LLDPMEDsupport              |          | 188 |
|                               | ConfiguringtheLLDPagent     |          | 188 |
|                               | LLDPcommands                |          | 189 |
|                               | clearlldpneighbors          |          | 189 |
|                               | clearlldpstatistics         |          | 189 |
|                               | lldp                        |          | 190 |
|                               | lldpdot3                    |          | 191 |
|                               | lldpholdtime                |          | 191 |
|                               | lldpmanagement-ipv4-address |          | 192 |
|                               | lldpmanagement-ipv6-address |          | 193 |
|                               | lldpmed                     |          | 194 |
|                               | lldpmed-location            |          | 195 |
|                               | lldpreceive                 |          | 196 |
|                               | lldpreinit                  |          | 197 |
|                               | lldpselect-tlv              |          | 197 |
|                               | lldptimer                   |          | 198 |
|                               | lldptransmit                |          | 200 |
|                               | lldptxdelay                 |          | 200 |
|                               | lldptrapenable              |          | 201 |
|                               | showlldpconfiguration       |          | 203 |
|                               | showlldplocal-device        |          | 204 |
|                               | showlldpneighbor-info       |          | 206 |
|                               | showlldpneighbor-infodetail |          | 208 |
|                               | showlldpstatistics          |          | 210 |
|                               | showlldptlv                 |          | 212 |
| CiscoDiscoveryProtocol(CDP)   |                             |          | 213 |
|                               | CDPsupport                  |          | 213 |
|                               | CDPcommands                 |          | 213 |
|                               | cdp                         |          | 213 |
|                               | clearcdpcounters            |          | 214 |
|                               | clearcdpneighbor-info       |          | 215 |
|                               | showcdp                     |          | 215 |
|                               | showcdpneighbor-info        |          | 216 |
|                               | showcdptraffic              |          | 217 |
| Zero Touch                    | Provisioning                |          | 219 |
| ZTPsupport                    |                             |          | 219 |
| SettingupZTPonatrustednetwork |                             |          | 220 |
| ZTPprocessduringswitchboot    |                             |          | 221 |
| ZTPcommands                   |                             |          | 222 |
|                               | showztpinformation          |          | 222 |
|                               | ztpforceprovision           |          | 225 |
| Switch system                 | and hardware                | commands | 227 |
| clearevents                   |                             |          | 227 |
| consolebaud-rate              |                             |          | 227 |
| domain-name                   |                             |          | 228 |
| hostname                      |                             |          | 229 |
| ledlocator                    |                             |          | 230 |
| showcapacities                |                             |          | 231 |
| showcapacities-status         |                             |          | 234 |
| showconsole                   |                             |          | 235 |
| showcore-dump                 |                             |          | 235 |
| showdomain-name               |                             |          | 237 |
| showenvironmentfan            |                             |          | 238 |
7
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| showenvironmentled                      |                    |           | 239 |
| --------------------------------------- | ------------------ | --------- | --- |
| showenvironmentpower-supply             |                    |           | 240 |
| showenvironmenttemperature              |                    |           | 241 |
| showevents                              |                    |           | 242 |
| showhostname                            |                    |           | 245 |
| showimages                              |                    |           | 245 |
| showmodule                              |                    |           | 246 |
| showrunning-config                      |                    |           | 248 |
| showrunning-configcurrent-context       |                    |           | 251 |
| showstartup-config                      |                    |           | 253 |
| showsystem                              |                    |           | 253 |
| showsystemresource-utilization          |                    |           | 254 |
| showtech                                |                    |           | 256 |
| showusb                                 |                    |           | 257 |
| showusbfile-system                      |                    |           | 258 |
| showversion                             |                    |           | 259 |
| systemresource-utilizationpoll-interval |                    |           | 260 |
| topcpu                                  |                    |           | 261 |
| topmemory                               |                    |           | 261 |
| usb                                     |                    |           | 262 |
| usbmount|unmount                        |                    |           | 263 |
| Support                                 | and Other          | Resources | 265 |
| AccessingArubaSupport                   |                    |           | 265 |
| AccessingUpdates                        |                    |           | 265 |
|                                         | ArubaSupportPortal |           | 265 |
|                                         | MyNetworking       |           | 266 |
| WarrantyInformation                     |                    |           | 266 |
| RegulatoryInformation                   |                    |           | 266 |
| DocumentationFeedback                   |                    |           | 266 |
Contents|8

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

9

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
| On the 4100iSwitch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|10

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

11

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

12

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

Aruba NetEdit
Aruba NetEdit enables the automation of multidevice configuration change workflows without the
overhead of programming.

The key capabilities of NetEdit include the following:

n Intelligent configuration with validation for consistency and compliance

n Time savings by simultaneously viewing and editing multiple configurations

n Customized validation tests for corporate compliance and network design

n Automated large-scale configuration deployment without programming

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

About AOS-CX | 13

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

In-band management
Management communications with a managed switch can be:

In band

In-band management communications occur through ports on the line modules of the switch, using
common communications protocols such as SSH and SNMP.

When you use an in-band management connection, management traffic from that connection uses the
same network infrastructure as user data. User data uses the data plane, which is responsible for
moving data from source to destination. Management traffic that uses the data plane is more likely to be
affected by traffic congestion and other issues affecting the user network.

SNMP-based management support
The AOS-CX operating system provides SNMP read access to the switch. SNMP support includes support of
industry-standard MIB (Management Information Base) plus private extensions, including SNMP events,
alarms, history, statistics groups, and a private alarm extension group. SNMP access is disabled by default.

User accounts
To view or change configuration settings on the switch, users must log in with a valid account.
Authentication of user accounts can be performed locally on the switch, or by using the services of an
external TACACS+ or RADIUS server.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

14

Two types of user accounts are supported:

n Operators: Operators can view configuration settings, but cannot change them. No operator accounts

are created by default.

n Administrators: Administrators can view and change configuration settings. A default locally stored

administrator account is created with username set to admin and no password. You set the
administrator account password as part of the initial configuration procedure for the switch.

About AOS-CX | 15

Chapter 3

Initial Configuration

Initial Configuration

Perform the initial configuration of a factory default switch using one of the following methods:

n Load a switch configuration using zero-touch provisioning (ZTP). When ZTP is used, the configuration is
loaded from a server automatically when the switch booted from the factory default configuration.

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

1. Connect the network to a data port.

See the Installation Guide for switch to determine the location of the switch ports.

2.

If the switch is powered on, power off the switch.

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image is
being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

Initial configuration using the CLI
This procedure describes how to connect to the switch for the first time and configure basic operational
settings using the CLI. In this procedure, you use a computer to connect to the switch using the either the
console port or management port.

Procedure

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

16

1. Connect to the console port or the management port.

2. Log into the switch for the first time.

3. Configure switch time using the NTP client.

Connecting to the console port

Prerequisites

n A switch installed as described in its hardware installation guide.

n A computer with terminal emulation software.

Procedure

1. Start the terminal emulation software on the computer and configure a new serial session with the

following settings:
n Speed: 115200 bps

n Data bits: 8

n Stop bits: 1

n Parity: None

n Flow control: None

2. Start the terminal emulation session.

3. Press Enter once. If the connection is successful, you are prompted to login.

Optional console port speed setting

If desired, the console port speed can be set with the console baud-rate command. For example, setting
the console port speed to 9600 bps:

switch(config)# console baud-rate 9600
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
settings are updated to match the baud rate of the switch.
Continue (y/n)? y

Showing the console port current speed:

switch# show console
Baud Rate: 9600

For details on the console baud-rate and show console commands, see Switch system and hardware
commands.

Connecting to the in-band management port

Prerequisites

n Two Ethernet cables

n SSH client software

Procedure

Initial Configuration | 17

1. Bydefault,the in-bandmanagementinterfaceissettoautomaticallyobtainanIPaddressfroma
DHCPserver,andSSHsupportisenabled.IfthereisnoDHCPserveronyournetwork,youmust
configureastaticaddressonthein-bandmanagementinterface:
| a.  | Connecttotheconsoleport                                  |     |                 |     |     |
| --- | -------------------------------------------------------- | --- | --------------- | --- | --- |
| b.  | Configureusing                                           |     | DHCPorstaticIP. |     |     |
| c.  | Configurethein-bandmanagementinterfaceandinterfaceVLAN1. |     |                 |     |     |
2. UseanEthernetcabletoconnectthemanagementporttoyournetwork.
3. UseanEthernetcabletoconnectyourcomputertothesamenetwork.
4. StartyourSSHclientsoftwareandconfigureanewsessionusingtheaddressassignedtothe in-band
managementinterface.(Ifthe in-bandmanagementinterfaceissettooperateasaDHCPclient,
retrievetheIPaddressassignedtothe in-bandmanagementinterfacefromyourDHCPserver.)
5. Startthesession.Iftheconnectionissuccessful,youarepromptedtologin.
| Configure | usingDHCPor |     | static | IP  |     |
| --------- | ----------- | --- | ------ | --- | --- |
Userscanuseanydataportsforin-bandmanagementpurposes.IPDHCPissupportedoninterfaceVLAN1only.
AllswitchportsarepartofaccessVLAN1bydefault.StaticIPaddressandIPDHCPconfigurationcanco-existon
VLAN1,howeverstaticaddressestakeprecedencewheneverconfigured.
DHCPConfiguration
| switch#:                | config |      |             |            |      |
| ----------------------- | ------ | ---- | ----------- | ---------- | ---- |
| switch(config)#:        |        | vlan | 1           |            |      |
| Switch(config-vlan-1)#: |        |      | description | Management | VLAN |
| Switch(config-vlan-1)#: |        |      | end         |            |      |
Switch#
!
| Switch(config)#:    |     | interface | 1/1/1       |                    |      |
| ------------------- | --- | --------- | ----------- | ------------------ | ---- |
| Switch(config-if)#: |     |           | description | IN-BAND Management | Port |
| Switch(config-if)#: |     |           | vlan access | 1                  |      |
| Switch(config-if)#: |     |           | no shutdown |                    |      |
| Switch(config-if)#: |     |           | end         |                    |      |
Switch#
!
| Switch(config)#: |     | interface | vlan | 1   |     |
| ---------------- | --- | --------- | ---- | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | ip dhcp     |     |     |
| ------------------------ | --- | --- | ----------- | --- | --- |
| Switch(config-if-vlan)#: |     |     | no shutdown |     |     |
| Switch(config-if-vlan)#: |     |     | end         |     |     |
Switch#
!
WithoutDHCPConfiguration
| switch#:                | config |      |             |            |      |
| ----------------------- | ------ | ---- | ----------- | ---------- | ---- |
| switch(config)#:        |        | vlan | 1           |            |      |
| Switch(config-vlan-1)#: |        |      | description | Management | VLAN |
| Switch(config-vlan-1)#: |        |      | end         |            |      |
Switch#
!
| Switch(config)#:    |     | interface | 1/1/1       |                    |      |
| ------------------- | --- | --------- | ----------- | ------------------ | ---- |
| Switch(config-if)#: |     |           | description | IN-BAND Management | Port |
| Switch(config-if)#: |     |           | vlan access | 1                  |      |
| Switch(config-if)#: |     |           | no shutdown |                    |      |
18
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Switch(config-if)#: |     |     | end |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
Switch#
!
| Switch(config)#: |     | interface |     | vlan | 1   |     |     |
| ---------------- | --- | --------- | --- | ---- | --- | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     |     | no ip       | dhcp            |     |     |
| ------------------------ | --- | --- | --- | ----------- | --------------- | --- | --- |
| Switch(config-if-vlan)#: |     |     |     | ip address  | 192.168.10.1/24 |     |     |
| Switch(config-if-vlan)#: |     |     |     | no shutdown |                 |     |     |
| Switch(config-if-vlan)#: |     |     |     | end         |                 |     |     |
Switch#
| Logging | into | the | switch | for | the first |     | time |
| ------- | ---- | --- | ------ | --- | --------- | --- | ---- |
Thefirsttimeyoulogintotheswitchyoumustusethedefaultadministratoraccount.Thisaccounthasno
password,soyouwillbepromptedonlogintodefineonetosafeguardtheswitch.
Procedure
1. Whenpromptedtologin,specifyadmin.Whenpromptedforthepassword,pressENTER.(By
default,nopasswordisdefined.)
Forexample:
|     | switch | login: | admin |     |     |     |     |
| --- | ------ | ------ | ----- | --- | --- | --- | --- |
password:
2. Defineapasswordfortheadminaccount.Thepasswordcancontainupto32alphanumeric
charactersintherangeASCII32to127,whichincludesspecialcharacterssuchasasterisk(*),
ampersand(&),exclamationpoint(!),dash(-),underscore(_),andquestionmark(?).
Forexample:
|     | Please    | configure     | the | 'admin' | user | account | password. |
| --- | --------- | ------------- | --- | ------- | ---- | ------- | --------- |
|     | Enter new | password:     |     | ******* |      |         |           |
|     | Confirm   | new password: |     | ******* |      |         |           |
switch#
3. Youareplacedintothemanagercommandcontext,whichisidentifiedbytheprompt:switch#,
whereswitchisthemodelnumberoftheswitch.Enterthecommandconfigtochangetotheglobal
configurationcontextconfig.
Forexample:
|     | switch# | config |     |     |     |     |     |
| --- | ------- | ------ | --- | --- | --- | --- | --- |
switch(config)#
| Setting | switch | time | using |     | the NTP | client |     |
| ------- | ------ | ---- | ----- | --- | ------- | ------ | --- |
Prerequisites
n TheIPaddressordomainnameofanNTPserver.
n IftheNTPserverusesauthentication,obtainthepasswordrequiredtocommunicatewiththeNTP
server.
InitialConfiguration |19

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
1. Configurethebannerthatisdisplayedwhenauserconnectstoadeviceusingaconsoleportorin-
|     | bandmanagementinterface.Usethecommandbanner |     |        |      |     |     |     | motd.Forexample: |     |     |
| --- | ------------------------------------------- | --- | ------ | ---- | --- | --- | --- | ---------------- | --- | --- |
|     | switch(config)#                             |     | banner | motd | ^   |     |     |                  |     |     |
Enter a new banner. Terminate the banner with the delimiter you have chosen.
|     | >> This | is an      | example | of   | a banner     | text | which     | a   | connecting | user |
| --- | ------- | ---------- | ------- | ---- | ------------ | ---- | --------- | --- | ---------- | ---- |
|     | >> will | see before |         | they | are prompted |      | for their |     | password.  |      |
>>
|     | >> As you | can           | see | it may | span | multiple  | lines     | and | the input |     |
| --- | --------- | ------------- | --- | ------ | ---- | --------- | --------- | --- | --------- | --- |
|     | >> will   | be terminated |     | when   | the  | delimiter | character |     | is        |     |
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
|       | Banner | updated | successfully! |     |     |     |     |     |     |     |
| ----- | ------ | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Using | the    | Web     | UI            |     |     |     |     |     |     |     |
Prerequisites
20
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |

AconnectiontotheswitchCLI.
n
Onthe6100,theHTTPSservercanonlybeenabledbythedefaultVRF.
Onthe4100i,theHTTPSservercanonlybeenabledbythedefaultVRF.
Procedure
1. LogintotheCLI.
2. Switchtoconfigcontext.
Forexample:
|     | switch#         | config |              |     |             |     |     |
| --- | --------------- | ------ | ------------ | --- | ----------- | --- | --- |
|     | switch(config)# |        | https-server |     | vrf default |     |     |
3. TheWebUIstartsandyouarepromptedtologin.
| Configuring |     | the | in-band |     | management |     | interface |
| ----------- | --- | --- | ------- | --- | ---------- | --- | --------- |
Prerequisites
Aconnectiontotheconsoleport.
Procedure
1. Switchtothe in-bandmanagementinterfacecontextwiththecommandinterface vlan 1.
2. Bydefault,thein-bandmanagementinterfaceisenabled.Ifitwasdisabled,re-enableitwiththe
|     | commandno | shutdown. |     |     |     |     |     |
| --- | --------- | --------- | --- | --- | --- | --- | --- |
3. Usethecommandip dhcptoconfigurethein-bandmanagementinterfacetoautomaticallyobtain
anaddressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastaticIPv4or
|     | IPv6addresswiththecommandsip |     |     |     | addressoripv6address. |     |     |
| --- | ---------------------------- | --- | --- | --- | --------------------- | --- | --- |
4. SSHisenabledbydefaultonthedefaultVRF.Ifdisabled,enableSSHwiththecommandssh
server
|     | vrf default. |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- |
Examples
Thisexampleenablesthe in-bandmanagementinterfacewithstaticaddressing:
| switch(config)#         |     | interface |        | vlan 1   |                    |         |          |
| ----------------------- | --- | --------- | ------ | -------- | ------------------ | ------- | -------- |
| switch(config-if-vlan)# |     |           | no     | ip dhcp  |                    |         |          |
| switch(config-if-vlan)# |     |           | ip     | address  | 192.168.100.200/24 |         |          |
| switch(config-if-vlan)# |     |           | no     | shutdown |                    |         |          |
| Restoring               |     | the       | switch | to       | factory            | default | settings |
Prerequisites
YouareconnectedtotheswitchthroughitsConsoleport.
InitialConfiguration |21

ThisprocedureerasesalluserinformationandconfigurationsettingsConsiderbackingupyourrunning
configurationfirst.
1. Optionally,backuptherunningconfigurationwitheithercopy running-config <REMOTE-URL>or
copy running-config <STORAGE-URL>.Thejsonstorageformatisrequiredforlaterconfiguration
restoration.
2. Switchtotheconfigurationcontextwiththecommandconfig.
3. Erasealluserinformationandconfiguration,restoringtheswitchtoitsfactorydefaultstatewiththe
commanderase all zeroize.EnterYwhenpromptedtocontinue.Theswitchautomatically
restarts.
4. Optionallyrestoreyoursavedconfiguration(itmustbeinjsonformat)witheithercopy <REMOTE-
URL> running-configorcopy <STORAGE-URL> running-configfollowedbycopy running-config
startup-config.
Example
Backinguptherunningconfigurationtoafileonaremoteserver(usingTFTP),resettingtheswitchtoits
factorydefaultstate,andthenrestoringthesavedconfiguration.
switch#
copy running-config tftp://10.100.1.12/backup_cfg json vrf default
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload |     | Upload | Total | Spent | Left Speed |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ----- | ----- | ---------- |
100 10340 0 0 100 10340 0 1329k --:--:-- --:--:-- --:--:-- 1329k
100 10340 0 0 100 10340 0 1313k --:--:-- --:--:-- --:--:-- 1313k
switch#
switch#
| switch#     | erase       | all zeroize |        |                  |          |        |              |              |            |     |
| ----------- | ----------- | ----------- | ------ | ---------------- | -------- | ------ | ------------ | ------------ | ---------- | --- |
| This will   | securely    |             | erase  | all customer     |          | data   | and          | reset        | the switch |     |
| to factory  | defaults.   |             | This   | will             | initiate |        | a reboot     | and          | render the |     |
| switch      | unavailable |             | until  | the zeroization  |          |        | is complete. |              |            |     |
| This should | take        | several     |        | minutes          | to       | one    | hour         | to complete. |            |     |
| Continue    | (y/n)?      | y           |        |                  |          |        |              |              |            |     |
| The system  | is          | going       | down   | for zeroization. |          |        |              |              |            |     |
| [  OK       | ] Stopped   | PSPO        | Module | Daemon.          |          |        |              |              |            |     |
| [  OK       | ] Stopped   | ArubaOS-CX  |        | Switch           |          | Daemon | for          | BCM.         |            |     |
...
| [  OK     | ] Stopped    | Remount |                                                   | Root      | and Kernel |     | File | Systems. |     |     |
| --------- | ------------ | ------- | ------------------------------------------------- | --------- | ---------- | --- | ---- | -------- | --- | --- |
| [  OK     | ] Reached    | target  |                                                   | Shutdown. |            |     |      |          |     |     |
| reboot:   | Restarting   |         | system                                            |           |            |     |      |          |     |     |
| Press Esc | for          | boot    | options                                           |           |            |     |      |          |     |     |
| ServiceOS | Information: |         |                                                   |           |            |     |      |          |     |     |
| Version:  |              |         | GT.01.03.0006                                     |           |            |     |      |          |     |     |
| Build     | Date:        |         | 2018-10-30                                        |           | 14:20:44   |     | PDT  |          |     |     |
| Build     | ID:          |         | ServiceOS:GT.01.03.0006:8ee0faaa52da:201810301420 |           |            |     |      |          |     |     |
| SHA:      |              |         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx          |           |            |     |      |          |     |     |
...
| ################ |     | Preparing |        | for         | zeroization                 |                         | ################# |     |            |     |
| ---------------- | --- | --------- | ------ | ----------- | --------------------------- | ----------------------- | ----------------- | --- | ---------- | --- |
| ################ |     | Storage   |        | zeroization |                             | ####################### |                   |     |            |     |
| ################ |     | WARNING:  |        | DO NOT      | POWER                       | OFF                     | UNTIL             |     | ########## |     |
| ################ |     |           |        | ZEROIZATION |                             | IS                      | COMPLETE          |     | ########## |     |
| ################ |     | This      | should | take        | several                     |                         | minutes           |     | ########## |     |
| ################ |     | to        | one    | hour to     | complete                    |                         |                   |     | ########## |     |
| ################ |     | Restoring |        | files       | ########################### |                         |                   |     |            |     |
22
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

Boot Profiles:
| 0. Service   | OS Console     |                       |     |     |     |
| ------------ | -------------- | --------------------- | --- | --- | --- |
| 1. Primary   | Software Image | [XL.10.02.0010]       |     |     |     |
| 2. Secondary | Software       | Image [XL.10.02.0010] |     |     |     |
Select profile(primary):
| Booting   | primary software | image... |     |     |     |
| --------- | ---------------- | -------- | --- | --- | --- |
| Verifying | Image...         |          |     |     |     |
Image Info:
Name: ArubaOS-CX
| Version:   | XL.10.02.0010                                          |          |     |     |     |
| ---------- | ------------------------------------------------------ | -------- | --- | --- | --- |
| Build      | Id: ArubaOS-CX:XL.10.02.0010:feaf5b9b7f09:201901292014 |          |     |     |     |
| Build      | Date: 2019-01-29                                       | 12:43:50 | PST |     |     |
| Extracting | Image...                                               |          |     |     |     |
| Loading    | Image...                                               |          |     |     |     |
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
switch#
copy tftp://192.168.1.10/backup_cfg running-config json vrf default
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     | Dload Upload | Total Spent | Left Speed |
| --- | --- | --- | ------------ | ----------- | ---------- |
100 10340 100 10340 0 0 2858k 0 --:--:-- --:--:-- --:--:-- 2858k
100 10340 100 10340 0 0 2804k 0 --:--:-- --:--:-- --:--:-- 2804k
Large configuration changes will take time to process, please be patient.
switch#
switch#
| switch# | copy running-config | startup-config |     |     |     |
| ------- | ------------------- | -------------- | --- | --- | --- |
Large configuration changes will take time to process, please be patient.
switch#
NTP commands
ntp authentication
ntp authentication
no ntp authentication
Description
EnablessupportforauthenticationwhencommunicatingwithanNTPserver.
Thenoformofthiscommanddisablesauthenticationsupport.
Examples
Enablingauthenticationsupport:
InitialConfiguration |23

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
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
24
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
ciphertext <ENCRYPTED-KEY> SpecifiestheciphertextauthenticationkeyinBase64format.This
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
| switch(config)# |     | ntp authentication-key |     |     | 10 md5 F82#450b | trusted |
| --------------- | --- | ---------------------- | --- | --- | --------------- | ------- |
Definingkey5withSHA1encryptionandapromptedplaintexttrustedkey:
| switch(config)# |     | ntp authentication-key |        |                | 5 sha1 |     |
| --------------- | --- | ---------------------- | ------ | -------------- | ------ | --- |
| Enter the       | NTP | authentication         | key:   | *********      |        |     |
| Re-Enter        | the | NTP authentication     |        | key: ********* |        |     |
| Configure       | the | key as trusted         | (y/n)? | y              |        |     |
Removingkey10:
| switch(config)# |     | no ntp authentication-key |     |     | 10  |     |
| --------------- | --- | ------------------------- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp disable
ntp disable
Description
DisablestheNTPclientontheswitch.TheNTPclientisdisabledbydefault.
InitialConfiguration |25

Examples
DisablingtheNTPclient.
switch(config)#
ntp disable
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
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
26
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Platforms

Command context

Authority

All platforms

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

prefer

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
server. Useful for reducing phase noise when the polling interval
is long.

Send a burst of six packets when not connected to the server.
Useful for reducing synchronization time at startup.

Make this the preferred server.

Initial Configuration | 27

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
version <VER-NUM> SpecifiestheversionnumbertouseforalloutgoingNTPpackets.
Range:3or4.
Usage
ForfeaturessuchasActivateandZTP,aswitchthathasafactorydefaultconfigurationwillautomaticallybe
configuredwithpool.ntp.org.NTPserverconfigurationsviaDHCPoptionsaresupported.TheDHCPserver
canbeconfiguredwithmaximumoftwoNTPserveraddresseswhichwillbesupportedontheswitch.Only
IPV4addressesaresupported.
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
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp trusted-key
| ntp trusted-key    | <KEY-ID> |     |     |     |
| ------------------ | -------- | --- | --- | --- |
| no ntp trusted-key | <KEY-ID> |     |     |     |
Description
Setsakeyastrusted.WhenNTPauthenticationisenabled,theswitchonlysynchronizeswithtimeservers
thattransmitpacketscontainingatrustedkey.
Thenoformofthiscommandremovesthetrusteddesignationfromakey.
28
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Parameter |     | Description |
| --------- | --- | ----------- |
<KEY-ID> Specifiestheidentificationnumberofthekeytosetastrusted.
Range:1to65534.
Examples
Definingkey10asatrustedkey.
| switch(config)# | ntp trusted-key | 10  |
| --------------- | --------------- | --- |
Removingtrusteddesignationfromkey10:
| switch(config)# | no ntp trusted-key | 10  |
| --------------- | ------------------ | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp vrf
ntp vrf <VRF-NAME>
| no ntp vrf <VRF-NAME> |     |     |
| --------------------- | --- | --- |
Description
6000and6100onlysupportdefaultVRF.
4100ionlysupportsdefaultVRF.
SpecifiestheVRFonwhichtheNTPclientcommunicateswithanNTPserver.
ThenoformofthecommandreturnstodefaultVRF.
| Parameter  |     | Description             |
| ---------- | --- | ----------------------- |
| <VRF-NAME> |     | SpecifiesthenameofaVRF. |
Example
SettingtheswitchtousethedefaultVRFforNTPclienttraffic.
InitialConfiguration |29

switch(config)# ntp vrf default

Returning the switch to use the default VRF for NTP client traffic.

switch(config)# no ntp vrf

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

show ntp associations
show ntp associations

Description

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

30

Example
| switch# | show ntp | associations |     |     |     |     |     |
| ------- | -------- | ------------ | --- | --- | --- | --- | --- |
----------------------------------------------------------------------
| ID  | NAME |     | REMOTE |     | REF-ID | ST LAST POLL | REACH |
| --- | ---- | --- | ------ | --- | ------ | ------------ | ----- |
----------------------------------------------------------------------
| 1                  | 192.0.1.1 |     | 192.0.1.1    |     | .INIT. | 16 -     | 64 0 |
| ------------------ | --------- | --- | ------------ | --- | ------ | -------- | ---- |
| * 2 time.apple.com |           |     | 17.253.2.253 |     | .GPSs. | 2 70 128 | 377  |
----------------------------------------------------------------------
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
| show ntp | authentication-keys |     |     |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- | --- | --- |
show ntp authentication-keys
Description
Showsthecurrentlydefinedauthenticationkeys.
Examples
| switch# | show ntp | authentication-keys |     |     |     |     |     |
| ------- | -------- | ------------------- | --- | --- | --- | --- | --- |
--------------------------------
| Auth key | Trusted | MD5 | password |     |     |     |     |
| -------- | ------- | --- | -------- | --- | --- | --- | --- |
--------------------------------
| 10  | No  | ********** |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- |
| 20  | Yes | ********** |     |     |     |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
InitialConfiguration |31

| show ntp | servers |     |     |     |
| -------- | ------- | --- | --- | --- |
show ntp servers
Description
ShowsallconfiguredNTPservers.
Example
| switch# | show ntp | servers |     |     |
| ------- | -------- | ------- | --- | --- |
------------------------------------------------
| NTP | SERVER KEYID | MINPOLL | MAXPOLL OPTION | VER |
| --- | ------------ | ------- | -------------- | --- |
------------------------------------------------
| 192.0.1.18 |     | -   | 5 10 iburst | 3        |
| ---------- | --- | --- | ----------- | -------- |
| 192.0.1.19 |     | -   | 6 10 none   | 4        |
| 192.0.1.20 |     | -   | 6 8 burst   | 3 prefer |
------------------------------------------------
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp | statistics |     |     |     |
| -------- | ---------- | --- | --- | --- |
show ntp statistics
Description
ShowsglobalNTPstatistics.Thefollowinginformationisdisplayed:
n Rx-pkts:TotalNTPpacketsreceived.
n CurrentVersionRx-pkts:NumberofNTPpacketsthatmatchthecurrentNTPversion.
n OldVersionRx-pkts:NumberofNTPpacketsthatmatchthepreviousNTPversion.
Errorpkts:Packetsdroppedduetoallothererrorreasons.
n
Auth-failedpkts:Packetsdroppedduetoauthenticationfailure.
n
Declinedpkts:Packetsdeniedaccessforanyreason.
n
n Restrictedpkts:PacketsdroppedduetoNTPaccesscontrol.
n Rate-limitedpkts:Numberofpacketsdiscardedduetoratelimitation.
n KODpkts:NumberofKissofDeathpacketssent.
Examples
32
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

| switch(config)#   |                 | show     | ntp statistics |     |     |
| ----------------- | --------------- | -------- | -------------- | --- | --- |
|                   |                 | Rx-pkts  | 100            |     |     |
| Current           | Version         | Rx-pkts  | 80             |     |     |
| Old               | Version         | Rx-pkts  | 20             |     |     |
|                   |                 | Err-pkts | 2              |     |     |
| Auth-failed-pkts  |                 |          | 1              |     |     |
|                   | Declined-pkts   |          | 0              |     |     |
|                   | Restricted-pkts |          | 0              |     |     |
| Rate-limited-pkts |                 |          | 0              |     |     |
|                   |                 | KoD-pkts | 0              |     |     |
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
| show ntp | status |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
show ntp status
Description
ShowsthestatusofNTPontheswitch.
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
| switch#            | show ntp    | status  |          |            |              |
| ------------------ | ----------- | ------- | -------- | ---------- | ------------ |
| NTP is enabled.    |             |         |          |            |              |
| NTP authentication |             | is      | enabled. |            |              |
| NTP is using       | the         | default | VRF for  | NTP server | connections. |
| Wed Nov            | 23 23:29:10 | PDT     | 2016     |            |              |
InitialConfiguration |33

| NTP uptime:   | 187 days, | 1        | hours,        | 37 minutes, |     | 48 seconds |
| ------------- | --------- | -------- | ------------- | ----------- | --- | ---------- |
| Synchronized  | to NTP    | Server   | 17.253.2.253  |             | at  | stratum 2. |
| Poll interval | = 1024    | seconds. |               |             |     |            |
| Time accuracy | is        | within   | 0.994 seconds |             |     |            |
| Reference     | time: Thu | Jan      | 28 2016       | 0:57:06.647 |     | (UTC)      |
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
34
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

Chapter 4

Interfaces

Interfaces

Configuring a layer 2 interface

Procedure

1. Change to the interface configuration context for the interface with the command interface.

2. Set the interface MTU (maximum transmission unit) with the command mtu.

3. Review interface configuration settings with the command show interface.

Single source IP address
Certain IP-based protocols used by the switch (such as RADIUS, sFlow, TACACS, and TFTP), use a client-server
model in which the client's source IP address uniquely identifies the client in packets sent to the server. By
default, the source IP address is defined as the IP address of the outgoing switch interface on which the
client is communicating with the server. Since the switch can have multiple routing interfaces, outgoing
packets can potentially be sent on different paths at different times. This can result in different source IP
addresses being used for a client, which can create a client identification problem on the server. For example,
it can be difficult to interpret system logs and accounting data on the server when the same client is
associated with multiple IP addresses.

To resolve this issue, you can use the commands ip source-interface and ipv6 source-interface to
define a single source IP address that applies to all supported protocols (RADIUS, sFlow, TACACS, and TFTP),
or an individual address for each protocol. This ensures that all traffic sent by a client to a server uses the
same IP address.

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

35

Thefeatureisdisabledbydefault.Aperiodicsystemlogwillbegeneratedbydefaultatanintervalof24
hourslistingtheportsonwhichunsupportedtransceiversarepresent.Thelogintervalisconfigurableand
canbedisabledbysettingthelog-intervaltonone.
| Interface | commands |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver
Description
Allowsunsupportedtransceiverstobeenabledorestablishconnections.Only1Gand10Gtransceiversare
enabledbythiscommandandunsupportedtransceiversofotherspeedswillremaindisabled.
Thenoformofthiscommanddisallowsusingunsupportedtransceivers.Thisisthedefault.
| Parameter |     |     | Description                                        |     |     |
| --------- | --- | --- | -------------------------------------------------- | --- | --- |
| confirm   |     |     | Specifiesthatunsupportedtransceiverwarningsaretobe |     |     |
automaticallyconfirmed.
| log-interval | none       |     | Disablesunsupportedtransceiverlogging. |     |     |
| ------------ | ---------- | --- | -------------------------------------- | --- | --- |
| log-interval | <INTERVAL> |     |                                        |     |     |
Setstheunsupportedtransceiverloggingintervalinminutes.
Default:1440minutes.Range:1440to10080minutes.
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
| Do you agree | and do you | want to | continue (y/n)? | y   |     |
| ------------ | ---------- | ------- | --------------- | --- | --- |
Allowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | allow-unsupported-transceiver |     |     | confirm |     |
| --------------- | ----------------------------- | --- | --- | ------- | --- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
Configuringunsupportedtransceiverloggingwithanintervalofevery48hours:
| switch(config)# | allow-unsupported-transceiver |     |     | log-interval | 2880 |
| --------------- | ----------------------------- | --- | --- | ------------ | ---- |
Interfaces|36

Disablingunsupportedtransceiverlogging:
| switch(config)# | allow-unsupported-transceiver |     |     | log-interval | none |
| --------------- | ----------------------------- | --- | --- | ------------ | ---- |
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no allow-unsupported-transceiver |     |     |     |     |
| --------------- | -------------------------------- | --- | --- | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, | and AOCs. |     |
| ----------- | ----------- | ------------- | ----- | --------- | --- |
| Continue    | (y/n)? y    |               |       |           |     |
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | no allow-unsupported-transceiver |     |     | confirm |     |
| --------------- | -------------------------------- | --- | --- | ------- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, | and AOCs. |     |
| ----------- | ----------- | ------------- | ----- | --------- | --- |
switch(config)#
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| default interface |                |     |     |     |     |
| ----------------- | -------------- | --- | --- | --- | --- |
| default interface | <INTERFACE-ID> |     |     |     |     |
Description
Setsaninterface(orarangeofinterfaces)tofactorydefaultvalues.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> SpecifiestheIDofasingleinterfaceorrangeofinterfaces.
Format:member/slot/portormember/slot/port-
member/slot/porttospecifyarange.
Examples
Resettinganinterface:
37
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

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
no description
Description
Associatesdescriptiveinformationwithaninterfacetohelpadministratorsandoperatorsidentifythe
purposeorroleofaninterface.
Thenoformofthiscommandremovesadescriptionfromaninterface.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<DESCRIPTION> Specifyadescriptionfortheinterface.Range:1to64ASCII
characters(includingspace,excludingquestionmark).
Examples
SettingthedescriptionforaninterfacetoDataLink01:
| switch(config-if)# | description | DataLink | 01  |
| ------------------ | ----------- | -------- | --- |
Removingthedescriptionforaninterface.
switch(config-if)#
no description
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
Interfaces|38

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
energy-efficient-ethernet
energy-efficient-ethernet
Description
Enablesauto-negotiationofEnergy-EfficientEthernet(EEE)onaninterface.EEENegotiationisestablished
onlyonauto-linknegotiationwithsupportedlinkpartners.
Examples
Configuringaninterface:
switch(config)#
|                    | interface                 | 1/1/1 |
| ------------------ | ------------------------- | ----- |
| switch(config-if)# | energy-efficient-ethernet |       |
DisablingEnergyEfficientEthernetonaninterface:
| switch(config)#    | interface                    | 1/1/1 |
| ------------------ | ---------------------------- | ----- |
| switch(config-if)# | no energy-efficient-ethernet |       |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
6000 forthiscommand.
6100
flow-control
| flow-control    | rxtx |     |
| --------------- | ---- | --- |
| no flow-control | rxtx |     |
Description
EnablesnegotiationofIEEE802.3xlink-levelflowcontrolonthecurrentinterface.Theswitchadvertiseslink-
levelflow-controlsupporttothelinkpartner.Thefinalconfigurationisdeterminedbasedonthecapabilities
ofbothpartners.
Thenoformdisablesflowcontrolsupportonthecurrentinterface.
39
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
rxtx EnablestheabilitytorespectandgenerateIEEE802.3xlink-level
pauseframesonthecurrentinterface.
Examples
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
Switchestotheconfig-ifcontextforaphysicalport.Thisiswhereyoudefinetheconfigurationsettings
forthelogicalinterfaceassociatedwiththephysicalport.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<PORT-NUM> Specifiesaphysicalportnumber.Format:member/slot/port.
Examples
Configuringaninterface:
| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
CommandHistory
Interfaces|40

| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| interface    | vlan           |           |     |     |
| ------------ | -------------- | --------- | --- | --- |
| interface    | vlan <VLAN-ID> |           |     |     |
| no interface | vlan           | <VLAN-ID> |     |     |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-if-
vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
| Parameter |     |     |     | Description                           |
| --------- | --- | --- | --- | ------------------------------------- |
| <VLAN-ID> |     |     |     | SpecifiestheinterfaceID.Range:2to4094 |
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
41
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

SetsanIP/IPv6addressontheinterfaceVLAN.
ThenoformofthiscommandremovestheIP/IPv6addressfromtheinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
| secondary |     |     | SpecifiesasecondaryIPaddress. |
| --------- | --- | --- | ----------------------------- |
Examples
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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip mtu
ip mtu <VALUE>
no ip mtu
Description
SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthatcanbe
sentorreceivedbytheinterface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.
Interfaces|42

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE> SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
SettingtheIPMTUto576bytes:
| switch(config-if-vlan)# |     | ip mtu | 576 |
| ----------------------- | --- | ------ | --- |
CommandHistory
| Release        |     |     | Modification              |
| -------------- | --- | --- | ------------------------- |
| 10.08          |     |     | Subinterfacesupportadded. |
| 10.07orearlier |     |     | --                        |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip source-interface
ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity | dns |
| all} {interface | <IFNAME> | | <IPV4-ADDR>} | [vrf <VRF-NAME>] |
| --------------- | -------- | -------------- | ---------------- |
no ip source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity | dns |
| all} [interface | <IFNAME> | | <IPV4-ADDR>] | [vrf <VRF-NAME>] |
| --------------- | -------- | -------------- | ---------------- |
Description
SetsasinglesourceIPaddressforafeatureontheswitch.Thisensuresthatalltrafficsentthefeaturehas
thesamesourceIPaddressregardlessofhowitegressestheswitch.Youcandefineasingleglobaladdress
thatappliestoallsupportedfeatures,oranindividualaddressforeachfeature.
ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,or
byusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIPaddress
takesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforallsupportedservices,oraspecific
service.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | SetsasinglesourceIPaddressforaspecificservice.Theall
ntp | syslog | simplivity | dns | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
| all |     |     | nothaveanaddressset. |
| --- | --- | --- | -------------------- |
43
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
interface <IFNAME> Specifiesthenameoftheinterfacefromwhichthespecified
serviceobtainsitssourceIPaddress.Theinterfacemusthavea
validIPaddressassignedtoit.Iftheinterfacehasbothaprimary
andsecondaryIPaddress,theprimaryIPaddressisused.
<IPV4-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedservice.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionisnot
used).SpecifytheaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
Examples
SettingtheIPv4address10.10.10.5astheglobalsinglesourceaddress:
| switch#         | config |                     |                |
| --------------- | ------ | ------------------- | -------------- |
| switch(config)# |        | ip source-interface | all 10.10.10.5 |
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)# |     | no ip source-interface | all 10.10.10.5 |
| --------------- | --- | ---------------------- | -------------- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK>{eui64 |                    | | [tag <ID>]} |
| --------------- | ------------------------ | ------------------ | ------------- |
| no ipv6 address |                          | <IPV6-ADDR>/<MASK> |               |
Description
SetsanIPv6addressontheinterface.
ThenoformofthiscommandremovestheIPv6addressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-local
addressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6 address
link-localcommand.
Interfaces|44

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
<MASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 source-interface
ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity | dns |
| all} {interface | <IFNAME> | | <IPV6-ADDR>} |     |
| --------------- | -------- | -------------- | --- |
no ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | simplivity | dns
| | all} [interface | <IFNAME> | | <IPV6-ADDR>] |     |
| ----------------- | -------- | -------------- | --- |
Description
SetsasinglesourceIPaddressforafeatureontheswitch.Thisensuresthatalltrafficsentthefeaturehas
thesamesourceIPaddressregardlessofhowitegressestheswitch.Youcandefineasingleglobaladdress
thatappliestoallsupportedfeatures,oranindividualaddressforeachfeature.
45
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,or
byusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIPaddress
takesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforallsupportedprotocols,oraspecific
protocol.
| Parameter |     | Description |
| --------- | --- | ----------- |
sflow | tftp | radius | tacacs | SetsasinglesourceIPaddressforaspecificprotocol.Theall
ntp | syslog | simplivity | dns | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
nothaveanaddressset.
all
interface <IFNAME> Specifiesthenameoftheinterfacefromwhichthespecified
protocolobtainsitssourceIPaddress.
<IPV6-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedprotocol.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF).SpecifytheIP
addressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
ConfiguringtheIPv6address2001:DB8::1astheglobalsinglesourceaddress:
| switch#         | config              |                    |
| --------------- | ------------------- | ------------------ |
| switch(config)# | ip source-interface | all 2001:DB8::1/32 |
StopthesourceIPaddressfromusingtheIPaddressoninterface1/1/1onVRFdefault.
switch(config)# no ip source-interface all interface 1/1/1 vrf default
ClearthesourceIPaddress2001:DB8::1.
| switch(config)# | no ip source-interface | all 2001:DB8::1 |
| --------------- | ---------------------- | --------------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mtu
Interfaces|46

mtu <VALUE>
no mtu
Description
SetstheMTU(maximumtransmissionunit)foraninterface.Thisdefinesthemaximumsizeofalayer2
(Ethernet)frame.FrameslargerthantheMTU(1500bytesbydefault)aredropped.
Tosupportjumboframes(frameslargerthan1522bytes),increasetheMTUasrequiredbyyournetwork.A
framesizeofupto9198bytesissupported.
Thelargestpossiblelayer1framewillbe18byteslargerthantheMTUvaluetoallowforlinklayerheaders
andtrailers.
ThenoformofthiscommandsetstheMTUtothedefaultvalue1500.
Parameter Description
<VALUE> SpecifiestheMTUinbytes.Range:46to9198.Default:1500.
Examples
SettingtheMTUoninterface1/1/1to1000bytes:
| switch(config)#    | interface  | 1/1/1 |
| ------------------ | ---------- | ----- |
| switch(config-if)# | no routing |       |
| switch(config-if)# | mtu        | 1000  |
SettingtheMTUoninterface1/1/1tothedefaultvalue:
| switch(config)#    | interface  | 1/1/1 |
| ------------------ | ---------- | ----- |
| switch(config-if)# | no routing |       |
| switch(config-if)# | no mtu     |       |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show allow-unsupported-transceiver
show allow-unsupported-transceiver
Description
Displaysconfigurationandstatusofunsupportedtransceivers.
Examples
47
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Showingunallowedunsupportedtransceivers:
| switch(config)#   |          | show allow-unsupported-transceiver |     |                |     |
| ----------------- | -------- | ---------------------------------- | --- | -------------- | --- |
| Allow unsupported |          | transceivers                       |     | : no           |     |
| Logging           | interval |                                    |     | : 1440 minutes |     |
---------------------------------------------
| Port | Type |     | Status |     |     |
| ---- | ---- | --- | ------ | --- | --- |
---------------------------------------------
| 1/1/31 | SFP-SX     |     | unsupported |     |     |
| ------ | ---------- | --- | ----------- | --- | --- |
| 1/1/32 | SFP-1G-BXD |     | unsupported |     |     |
| 1/1/2  | SFP28DAC3  |     | unsupported |     |     |
Showingallowedunsupportedtransceivers:
| switch#           | show allow-unsupported-transceiver |              |     |                |     |
| ----------------- | ---------------------------------- | ------------ | --- | -------------- | --- |
| Allow unsupported |                                    | transceivers |     | : yes          |     |
| Logging           | interval                           |              |     | : 1440 minutes |     |
---------------------------------------------
| Port | Type |     | Status |     |     |
| ---- | ---- | --- | ------ | --- | --- |
---------------------------------------------
| 1/1/31 | SFP-SX     |     | unsupported-allowed |     |     |
| ------ | ---------- | --- | ------------------- | --- | --- |
| 1/1/32 | SFP-1G-BXD |     | unsupported-allowed |     |     |
| 1/1/2  | SFP28DAC3  |     | unsupported         |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero]]
| show interface | [lag | | vlan | ] [<ID>] | [brief    | | physical] |
| -------------- | ---- | ------ | -------- | --------- | ----------- |
| show interface | [lag | | vlan | ] [<ID>] | [extended | [non-zero]] |
Description
Displaysactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     |     | Description              |     |
| --------- | --- | --- | --- | ------------------------ | --- |
| <IFNAME>  |     |     |     | Specifiesainterfacename. |     |
Interfaces|48

| Parameter |     |     |     |     | Description                                    |     |     |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
| <IFRANGE> |     |     |     |     | Specifiestheportidentifierrange.               |     |     |     |     |
| brief     |     |     |     |     | Showsbriefinfointabularformat.                 |     |     |     |     |
| physical  |     |     |     |     | Showsthephysicalconnectioninfointabularformat. |     |     |     |     |
| extended  |     |     |     |     | Showsadditionalstatistics.                     |     |     |     |     |
| non-zero  |     |     |     |     | Showsonlynonzerostatistics.                    |     |     |     |     |
| LAG       |     |     |     |     | ShowsLAGinterfaceinformation.                  |     |     |     |     |
| VLAN      |     |     |     |     | ShowsVLANinterfaceinformation.                 |     |     |     |     |
| <LAG-ID>  |     |     |     |     | SpecifiestheLAGnumber.Range:1-256              |     |     |     |     |
| <VLAN-ID> |     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |     |     |     |
Examples
Thefollowingexampleshowswheninterface1/1/1isconfigured:
| switch#           | show  | interface |          | 1/1/1 |            |                 |           |     |     |
| ----------------- | ----- | --------- | -------- | ----- | ---------- | --------------- | --------- | --- | --- |
| Interface         | 1/1/1 | is        | up       |       |            |                 |           |     |     |
| Admin state       |       | is up     |          |       |            |                 |           |     |     |
| Link state:       |       | up for    | 1 minute |       | (since Thu | Nov 26 10:26:34 | UTC 2020) |     |     |
| Link transitions: |       |           | 3        |       |            |                 |           |     |     |
Description:
| Hardware: | Ethernet, |     | MAC | Address: | 88:3a:30:47:d1:df |     |     |     |     |
| --------- | --------- | --- | --- | -------- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | cos             |           |          |     |          |     |     |       |         |
| ---------------- | --------------- | --------- | -------- | --- | -------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s            |           |          |     |          |     |     |       |         |
| Auto-negotiation |                 |           | is on    |     |          |     |     |       |         |
| Energy-Efficient |                 |           | Ethernet | is  | disabled |     |     |       |         |
| Flow-control:    |                 | off       |          |     |          |     |     |       |         |
| Error-control:   |                 | off       |          |     |          |     |     |       |         |
| MDI mode:        | MDIX            |           |          |     |          |     |     |       |         |
| VLAN Mode:       | native-untagged |           |          |     |          |     |     |       |         |
| Native           | VLAN:           | 1         |          |     |          |     |     |       |         |
| Allowed          | VLAN            | List:     | all      |     |          |     |     |       |         |
| Rate collection  |                 | interval: |          | 300 | seconds  |     |     |       |         |
| Rates            |                 |           |          |     | RX       |     | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization |     | %   |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistics  |     |     |     |     | RX   |     | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets |     |     |     |     | 0   |     | 0   |     | 0   |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast |     |     |     |     | 0   |     | 0   |     | 0   |
49
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

|          | Multicast |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          | Broadcast |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| Bytes    |           |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| Jumbos   |           |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| Dropped  |           |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| Filtered |           |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| Pause    | Frames    |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
| Errors   |           |     |     |     | 0   |     |     |     | 0   |     | 0   |     |
|          | CRC/FCS   |     |     |     | 0   |     |     |     | n/a |     | 0   |     |
|          | Collision |     |     |     | n/a |     |     |     | 0   |     | 0   |     |
|          | Runts     |     |     |     | 0   |     |     |     | n/a |     | 0   |     |
|          | Giants    |     |     |     | 0   |     |     |     | n/a |     | 0   |     |
Whentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |     |     |
...
| Auto-negotiation |     |     | is on | with | downshift | active |     |     |     |     |     |     |
| ---------------- | --- | --- | ----- | ---- | --------- | ------ | --- | --- | --- | --- | --- | --- |
Whentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
switch(config-if)#
|           |     |       | show  | interface | 1/1/1 |     |     |     |     |     |     |     |
| --------- | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Interface |     | 1/1/1 | is up |           |       |     |     |     |     |     |     |     |
...
| Energy-Efficient |     |     | Ethernet |     | is enabled | and | active |     |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
WhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 | physical |     |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
----
|        |     |        |         |     | Link              | Admin  |        | Speed |          | Flow-Control |        |     |
| ------ | --- | ------ | ------- | --- | ----------------- | ------ | ------ | ----- | -------- | ------------ | ------ | --- |
|        | EEE | PoE    | Power   |     |                   |        |        |       |          | Port         |        |     |
| Port   |     | Type   |         |     | Status            | Config | Status |       | | Config | Status |     | Config |     |
| Status | |   | Config | (Watts) |     | State Information |        |        |       |          | Description  |        |     |
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
----
| 1/1/1 |     | 1GbT |     |             | up  | up  | 1G  |     | auto | off | off | on  |
| ----- | --- | ---- | --- | ----------- | --- | --- | --- | --- | ---- | --- | --- | --- |
|       | on  |      | --  | 10M/100M/1G |     |     |     |     |      | --  |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |     |     |     |     |
CommandInformation
Interfaces|50

| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show interface |                  | dom |     |     |          |     |     |
| -------------- | ---------------- | --- | --- | --- | -------- | --- | --- |
| show interface | [<INTERFACE-ID>] |     |     | dom | [detail] |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+).This
informationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
| detail |     |     |     |     | Showdetailedinformation. |     |     |
| ------ | --- | --- | --- | --- | ------------------------ | --- | --- |
Example
| switch# | show interface |     | dom |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
Port Type Channel Temperature Voltage Tx Bias Rx Power Tx Power
|     |     |     |     | (Celsius) | (Volts) (mA) | (mW/dBm) | (mW/dBm) |
| --- | --- | --- | --- | --------- | ------------ | -------- | -------- |
----------------------------------------------------------------------------------
| 1/1/1 | SFP+SR   |     |     | 47.65 | 3.31 8.40 | 0.08, -10.96 | 0.63, -2.49 |
| ----- | -------- | --- | --- | ----- | --------- | ------------ | ----------- |
| 1/1/2 | SFP+SR   |     |     | n/a   | n/a n/a   | n/a          | n/a         |
| 1/1/3 | SFP+DA3  |     |     | 42.10 | 3.24 n/a  | n/a          | n/a         |
| 1/1/4 | QSFP+SR4 | 1   |     | 44.46 | 3.30 6.12 | 0.08, -10.96 | 0.63, -1.95 |
|       |          | 2   |     | 44.46 | 3.30 6.04 | 0.08, -10.96 | 0.63, -2.00 |
|       |          | 3   |     | 44.46 | 3.30 6.51 | 0.08, -10.96 | 0.60, -2.16 |
|       |          | 4   |     | 44.46 | 3.30 6.19 | 0.08, -10.96 | 0.63, -1.94 |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                      | energy-efficient |     |     | ethernet                  |     |     |
| -------------- | -------------------- | ---------------- | --- | --- | ------------------------- | --- | --- |
| show interface | [<IFNAME>|<IFRANGE>] |                  |     |     | energy-efficient-ethernet |     |     |
51
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |

Description
DisplaysEnergy-EfficientEthernetinformationfortheinterface.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IFNAME> Specifiesthenameofaninterfaceontheswitch.Usetheformat
member/slot/port(forexample,1/1/1).
<IFRANGE> Specifiestheportidentifierrangeofaninterfaceontheswitch.
Usetheformatmember/slot/port(forexample,1/1/1).
Example
ThefollowingexampleshowswhentheinterfacesareEnergy-EfficientEthernetcapable
| switch# | show interface | energy-efficient-ethernet |     |     |     |     |
| ------- | -------------- | ------------------------- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Port | Enabled | Negotiated | Speed  | TX Wake  | RX   | Wake |
| ---- | ------- | ---------- | ------ | -------- | ---- | ---- |
|      |         |            | (MB/s) | Time(us) | Time | (us) |
-------------------------------------------------------------------
| 1/1/1   | no             | no                              | --   | --  | --  |     |
| ------- | -------------- | ------------------------------- | ---- | --- | --- | --- |
| 1/1/2   | yes            | yes                             | 100  | 36  | 36  |     |
| 1/1/3   | yes            | yes                             | 1000 | 17  | 17  |     |
| 1/1/4   | no             | no                              | --   | --  | --  |     |
| 1/1/5   | yes            | no                              | 1000 | --  | --  |     |
| switch# | show interface | 1/1/1 energy-efficient-ethernet |      |     |     |     |
------------------------------------------------------------------------
| Port | Enabled | Negotiated | Speed  | TX Wake |      | RX Wake   |
| ---- | ------- | ---------- | ------ | ------- | ---- | --------- |
|      |         |            | (Mb/s) | Time    | (us) | Time (us) |
------------------------------------------------------------------------
| 1/1/1 | no  | no  | 1000 | --  |     | --  |
| ----- | --- | --- | ---- | --- | --- | --- |
switch#
CommandHistory
| Release        |     |     | Modification |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
4100i config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
6000
commandfromtheoperatorcontext(>)only.
6100
| show interface |                       | flow-control |              |          |     |     |
| -------------- | --------------------- | ------------ | ------------ | -------- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |              | flow-control | [detail] |     |     |
Description
Displaystheflowcontrolconfiguration,status,andstatisticsofthespecifiedinterface.
Interfaces|52

Ifdetailisnotspecified,thecommanddisplaysasummaryofallflowcontrolledinterfaceswithoneinterface
perline.Ifdetailisspecified,thecommanddisplaysdetailsandstatisticsaboutflowcontrolinalongformon
thespecifiedinterfaces.
| Parameter |     |     | Description               |     |
| --------- | --- | --- | ------------------------- | --- |
| <IFNAME>  |     |     | Specifiesaninterfacename. |     |
<IFRANGE>
Specifiestheportidentifierrange.
| detail |     |     | Showdetailsandstatisticsofflowcontrol. |     |
| ------ | --- | --- | -------------------------------------- | --- |
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
53
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Release |     |     |     |     | Modification       |     |
| ------- | --- | --- | --- | --- | ------------------ | --- |
| 10.08   |     |     |     |     | Commandintroduced. |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
4100 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 6000 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6100
| show interface |     | transceiver |     |     |     |     |
| -------------- | --- | ----------- | --- | --- | --- | --- |
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations]
Description
Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfordifferent
transceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPEandthird-party
transceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskintheoutput.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
| detail               |     |     |     |     | Showdetailedinformationfortheinterfaces. |     |
| -------------------- | --- | --- | --- | --- | ---------------------------------------- | --- |
| threshold-violations |     |     |     |     | Showthresholdviolationsfortransceivers.  |     |
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
| Connector       | Type |        | : LC      |             |        |     |
| Wavelength      |      |        | : 850nm   |             |        |     |
Transfer Distance : 0.00km (SMF), 20m (OM1), 80m (OM2), 300m (OM3)
| Diagnostic | Support |     | : DOM        |     |     |     |
| ---------- | ------- | --- | ------------ | --- | --- | --- |
| Product    | Number  |     | : J9150D     |     |     |     |
| Serial     | Number  |     | : xxxxxxxxxx |     |     |     |
Interfaces|54

| Part Number |     | : 1990-4634 |     |     |     |
| ----------- | --- | ----------- | --- | --- | --- |
Status
| Temperature | : 30.38C  |          |     |     |     |
| ----------- | --------- | -------- | --- | --- | --- |
| Voltage     | : 3.26V   |          |     |     |     |
| Tx Bias     | : 5.54mA  |          |     |     |     |
| Rx Power    | : 0.56mW, | -2.52dBm |     |     |     |
| Tx Power    | : 0.62mW, | -2.08dBm |     |     |     |
| Recent      | Alarms:   |          |     |     |     |
| Recent      | Errors:   |          |     |     |     |
| Transceiver | in 1/1/16 |          |     |     |     |
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
| Recent      | Alarms:   |          |     |     |     |
| Recent      | Errors:   |          |     |     |     |
Showingdetailedtransceiverinformationwithidentificationofunsupportedtransceivers:
| switch#     | show interface | transceiver            | detail    |           |          |
| ----------- | -------------- | ---------------------- | --------- | --------- | -------- |
| Transceiver | in 1/1/2       |                        |           |           |          |
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
| Temperature | : 28.88C    |         |     |     |     |
| ----------- | ----------- | ------- | --- | --- | --- |
| Voltage     | : 3.30V     |         |     |     |     |
| Tx Bias     | : 65.53mA   |         |     |     |     |
| Rx Power    | : 0.00mW,   | -inf    |     |     |     |
| Tx Power    | : 1.47mW,   | 1.67dBm |     |     |     |
| Recent      | Alarms:     |         |     |     |     |
| Rx Power    | low alarm   |         |     |     |     |
| Rx Power    | low warning |         |     |     |     |
55
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Recent  | Errors: |        |     |     |     |     |
| ------- | ------- | ------ | --- | --- | --- | --- |
| Rx loss | of      | signal |     |     |     |     |
Showingtransceiverthreshold-violations:
| switch(config)# |     | show interface |     | transceiver | threshold-violations |     |
| --------------- | --- | -------------- | --- | ----------- | -------------------- | --- |
----------------------------------------------------------------
| Port | Type |     | Channel# | Recent | Threshold | Violations |
| ---- | ---- | --- | -------- | ------ | --------- | ---------- |
----------------------------------------------------------------
| 1/1/15 | SFP+SR |     |     | none |     |     |
| ------ | ------ | --- | --- | ---- | --- | --- |
| 1/1/16 | SFP+SR |     |     | none |     |     |
switch#
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
| show ip           | interface |                |     |     |     |     |
| ----------------- | --------- | -------------- | --- | --- | --- | --- |
| show ip interface |           | <INTERFACE-ID> |     |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
Example
| switch#      | show      | ip interface  | vlan1    |                   |     |     |
| ------------ | --------- | ------------- | -------- | ----------------- | --- | --- |
| Interface    | vlan1     | is up         |          |                   |     |     |
| Admin        | state     | is up         |          |                   |     |     |
| Hardware:    | Ethernet, | MAC           | Address: | f8:60:f0:c9:11:60 |     |     |
| IP MTU       | 1500      |               |          |                   |     |     |
| IPv4 address |           | 10.120.3.8/26 |          |                   |     |     |
CommandHistory
Interfaces|56

| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip source-interface |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsettingthat
appliestoallprotocolsthatdonothaveanaddressset.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch#          | show ip | source-interface |             | sflow |     |
| ---------------- | ------- | ---------------- | ----------- | ----- | --- |
| Source-interface |         | Configuration    | Information |       |     |
----------------------------------------
| Protocol |     | Source Interface |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| -------- |     | ---------------- |     |     |     |
| sflow    |     | 10.10.10.1       |     |     |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show ip | source-interface |             | all |     |
| ---------------- | ------- | ---------------- | ----------- | --- | --- |
| Source-interface |         | Configuration    | Information |     |     |
----------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP | VRF |
| -------- | --- | ------------- | --- | ------ | --- |
----------------------------------------------------------------
| all |     | vlan2 |     | 2.2.2.2 | default |
| --- | --- | ----- | --- | ------- | ------- |
switch#
CommandHistory
57
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ipv6           | interface |                |     |     |     |     |
| ---- | -------------- | --------- | -------------- | --- | --- | --- | --- |
| show | ipv6 interface |           | <INTERFACE-ID> |     |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv6interface.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
SpecifiesaninterfaceID.Format:member/slot/port.
Examples
|     | switch#         | show ipv6      | interface      | vlan2                       |         |                |         |
| --- | --------------- | -------------- | -------------- | --------------------------- | ------- | -------------- | ------- |
|     | Interface       | vlan2          | is up          |                             |         |                |         |
|     | Admin state     | is             | up             |                             |         |                |         |
|     | IPv6 address:   |                |                |                             |         |                |         |
|     | 2001::1/64      |                | [VALID]        |                             |         |                |         |
|     | IPv6 link-local |                | address:       | fe80::883a:3080:247:c1c0/64 |         |                | [VALID] |
|     | IPv6 Forwarding |                | feature:       | enabled                     |         |                |         |
|     | IPv6 multicast  |                | groups locally |                             | joined: |                |         |
|     | ff02::1         | ff02::1:ff00:1 |                | ff02::1:ff47:c1c0           |         | ff02::1:ff00:0 |         |
ff02::2
|     | IPv6 MTU     | 1500     |      |             |      |     |     |
| --- | ------------ | -------- | ---- | ----------- | ---- | --- | --- |
|     | IPv6 unicast | reverse  | path | forwarding: | none |     |     |
|     | IPv6 load    | sharing: | none |             |      |     |     |
switch#
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Interfaces|58

| show ipv6 | source-interface |     |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- | --- |
show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter    |     |        |          |       | Description |     |
| ------------ | --- | ------ | -------- | ----- | ----------- | --- |
| sflow | tftp | |   | radius | | tacacs | | all |             |     |
ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsettingthat
appliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch#          | show | ipv6 source-interface |     |             | sflow |     |
| ---------------- | ---- | --------------------- | --- | ----------- | ----- | --- |
| Source-interface |      | Configuration         |     | Information |       |     |
----------------------------------------
| Protocol |     | Source           | Interface |     |     |     |
| -------- | --- | ---------------- | --------- | --- | --- | --- |
| -------- |     | ---------------- |           |     |     |     |
| sflow    |     | 2001:DB8::1      |           |     |     |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show | ipv6 source-interface |     |             | all |     |
| ---------------- | ---- | --------------------- | --- | ----------- | --- | --- |
| Source-interface |      | Configuration         |     | Information |     |     |
---------------------------------------------------------------
| Protocol |     | Src-Interface |     |     | Src-IP | VRF |
| -------- | --- | ------------- | --- | --- | ------ | --- |
---------------------------------------------------------------
| all |     | vlan2 |     |     | 2001::1 | default |
| --- | --- | ----- | --- | --- | ------- | ------- |
switch#
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
shutdown
59
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

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
| switch(config-if)# | no shutdown |     |
| ------------------ | ----------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Interfaces|60

Chapter 5
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
| Source-interface | selection |     | commands |     |     |     |
| ---------------- | --------- | --- | -------- | --- | --- | --- |
ip source-interface
| ip source-interface    | <PROTOCOL> | <IP-ADDR> | [vrf <VRF-NAME>] |     |     |     |
| ---------------------- | ---------- | --------- | ---------------- | --- | --- | --- |
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
dns
SelectsDNS.
ntp
SelectsNTP.
radius
Selectsradius.
sflow
SelectssFLow.
simplivity
Selectssimplivity.
61
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
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
switch(config)#
|     | ip source-interface | dns 10.1.1.1 |     |
| --- | ------------------- | ------------ | --- |
Configuringsource-interfaceIPv410.1.1.2tousefortheDNSprotoclonVRF green:
| switch(config)# | ip source-interface | dns 10.1.1.2 | vrf green |
| --------------- | ------------------- | ------------ | --------- |
Removingsource-interfaceIPv410.1.1.1configurationfortheDNSprotocol:
| switch(config)# | no ip source-interface | tftp 10.1.1.1 |     |
| --------------- | ---------------------- | ------------- | --- |
Removingsource-interfaceIPv410.1.1.2configurationfortheDNSprotocolonVRFgreen:
| switch(config)# | no ip source-interface | dns 10.1.1.2 | vrf green |
| --------------- | ---------------------- | ------------ | --------- |
Sourceinterfaceselection|62

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

ip source-interface interface
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

vrf <VRF-NAME>

Specifies the VRF name.

<IFNAME>

Examples

Specifies the interface name.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

63

ConfiguringIPv4source-interfaceinterface1/1/1tousefortheTFTP protocol:
| switch(config)# |     | ip source-interface |     | tftp | interface | 1/1/1 |
| --------------- | --- | ------------------- | --- | ---- | --------- | ----- |
ConfiguringIPv4source-interfaceinterface1/1/2tousefortheTFTP protocolonVRFgreen:
switch(config)# ip source-interface tftp interface 1/1/2 vrf green
RemovingIPv4source-interface1/1/1configurationfortheTFTP protocol:
switch(config)#
|     |     | no ip source-interface |     |     | tftp interface | 1/1/1 |
| --- | --- | ---------------------- | --- | --- | -------------- | ----- |
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
| Parameter  |     |     |     | Description                      |     |     |
| ---------- | --- | --- | --- | -------------------------------- | --- | --- |
| <PROTOCOL> |     |     |     | Specifiestheprotocoltoconfigure. |     |     |
all
Selectsallprotocolssupportedbythiscommand.
central
SelectsArubaCentral.
ntp
SelectsNTP.
radius
Sourceinterfaceselection|64

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
Selectsradius.
sflow
SelectssFLow.
syslog
Selectssyslog.
tacacs
SelectsTACACS.
tftp
SelectsTFTP.
| <IPV6-ADDR>    |     | SpecifiestheIPv6address. |     |
| -------------- | --- | ------------------------ | --- |
| vrf <VRF-NAME> |     | SpecifiestheVRF name.    |     |
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
ipv6 source-interface interface
ipv6 source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
no ipv6 source-interface <PROTOCOL> interface <IFNAME> [vrf <VRF-NAME>]
65
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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

switch(config)# no ipv6 source-interface tftp interface 1/1/2 vrf green

Command History

Source interface selection | 66

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
| vrf <VRF-NAME> |     |     | SpecifiestheVRF name. |     |
| -------------- | --- | --- | --------------------- | --- |
all-vrfs
ShowsthesourceinterfaceconfigurationforallVRFs.
Examples
Displayingallsource-interfaceprotocolconfigurationsforVRF red:
67
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

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
show ipv6 source-interface <PROTOCOL> [detail] [vrf <VRF-NAME> | all-vrfs]
Description
DisplaystheIPV6sourceinterfaceinformationconfiguredintherouterforallVRFsoraspecificVRF.
IfaVRF isnotspecified,thedefaultisdisplayed.
Sourceinterfaceselection|68

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
switch#
Displaying allIPv6source-interfaceprotocolconfigurationsforallVRFs:
| switch# show     | ipv6 source-interface | all all-vrfs |     |
| ---------------- | --------------------- | ------------ | --- |
| Source-interface | Configuration         | Information  |     |
-------------------------------------------------------------------
69
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Protocol |     | Src-Interface |     | Src-IP |     |     | VRF |
| -------- | --- | ------------- | --- | ------ | --- | --- | --- |
-------------------------------------------------------------------
| all |     |       |     | 2.2.2.2:3.3.3.3 |     |     | all-vrfs |
| --- | --- | ----- | --- | --------------- | --- | --- | -------- |
| all |     |       |     | 1.1.1.1:2.2.2.2 |     |     | default  |
| all |     | 1/1/1 |     | 2::2            |     |     | red      |
switch#
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
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
| switch# | show running-config |     |     |     |     |     |     |
| ------- | ------------------- | --- | --- | --- | --- | --- | --- |
vrf green
| ip source-interface   |     |     | tftp interface     | 1/1/2 | vrf       | green     |     |
| --------------------- | --- | --- | ------------------ | ----- | --------- | --------- | --- |
| ip source-interface   |     |     | radius interface   |       | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | ntp interface      | 1/1/2 | vrf       | green     |     |
| ip source-interface   |     |     | tacacs interface   |       | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | dns interface      | 1/1/2 | vrf       | green     |     |
| ip source-interface   |     |     | central interface  |       | 1/1/2     | vrf green |     |
| ip source-interface   |     |     | all interface      | 1/1/2 | vrf       | green     |     |
| ipv6 source-interface |     |     | tftp 2222::3333    |       | vrf       | green     |     |
| ipv6 source-interface |     |     | radius 2222::3333  |       | vrf       | green     |     |
| ipv6 source-interface |     |     | ntp 2222::3333     |       | vrf green |           |     |
| ipv6 source-interface |     |     | tacacs 2222::3333  |       | vrf       | green     |     |
| ipv6 source-interface |     |     | central 2222::3333 |       | vrf       | green     |     |
| ipv6 source-interface |     |     | all 2222::3333     |       | vrf green |           |     |
| ip source-interface   |     |     | tftp 10.20.3.1     |       |           |           |     |
| ip source-interface   |     |     | radius 10.20.3.1   |       |           |           |     |
| ip source-interface   |     |     | ntp 10.20.3.1      |       |           |           |     |
| ip source-interface   |     |     | tacacs 10.20.3.1   |       |           |           |     |
Sourceinterfaceselection|70

ip source-interface dns 10.20.3.1
| ip source-interface | central 10.20.3.1 |     |
| ------------------- | ----------------- | --- |
ip source-interface all 10.20.3.1
| interface | 1/1/1                  |     |
| --------- | ---------------------- | --- |
| no        | shutdown               |     |
| ip        | address 10.20.3.1/24   |     |
| interface | 1/1/2                  |     |
| vrf       | attach green           |     |
| ip        | address 20.1.1.1/24    |     |
| ipv6      | address 2222::3333/64  |     |
| interface | 1/1/45                 |     |
| no        | shutdown               |     |
| ip        | address 100.1.0.1/24   |     |
| ipv6      | address 1111::2222/64  |     |
| ip route  | 100.2.0.0/24 10.20.3.2 |     |
switch#
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
71
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Chapter 6

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

72

Chapter 7

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

73

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
Configurationandfirmwaremanagement |74

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
75
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

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

Configuration and firmware management | 76

Theplussign(+)atthebeginningofalineindicatesthatthelineexistsinthecomparisonbutnotinthe
n
baseline.
n Theminussign(-)atthebeginningofalineindicatesthatthelineexistsinthebaselinebutnotinthe
comparison.
Examples
Inthefollowingexample,theconfigurationsofcheckpointscp1andcp2aredisplayedbeforethe
checkpoint diffcommand,sothatyoucanseethecontextofthecheckpoint diffcommand.
| switch# | checkpoint | diff chkpt01 | chkpt02 |
| ------- | ---------- | ------------ | ------- |
--- /tmp/chkpt011607564301327
+++ /tmp/chkpt021607564301353
| @@ -1,7 | +1,7 @@ |     |     |
| ------- | ------- | --- | --- |
!
| !Version          | ArubaOS-CX | PL.10.06.0100V |                     |
| ----------------- | ---------- | -------------- | ------------------- |
| !export-password: |            | default        |                     |
| -hostname         | Switch     |                |                     |
| +hostname         | Switch1    |                |                     |
| user admin        | group      | administrators | password ciphertext |
AQBapTyg9tpaiAaTfSVV5eNdFzOORRvZ6CMpglh1P+LQUHQLYgAAAGAhmRqFbkNvrgy2SBVk7H8C5hvg/Iib
8rWYFZLEaSCrobNP9EwMu+hLNM0xmsh45yG8dncP7WkxjwrW4p4Qra6dVfr0EW8xh/lpQf8F/2Wki20Lc9JL
XiYge7ti0H6cVn+G
| radius-server | tracking | interval | 60  |
| ------------- | -------- | -------- | --- |
no usb
switch#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
checkpointpost-configuration
| checkpoint post-configuration |                    |     |     |
| ----------------------------- | ------------------ | --- | --- |
| no checkpoint                 | post-configuration |     |     |
Description
Enablescreationofsystemgeneratedcheckpointswhenconfigurationchangesoccur.Thisfeatureis
enabledbydefault.
Thenoformofthiscommanddisablessystemgeneratedcheckpoints.
Usage
Systemgeneratedcheckpointsareautomaticallycreatedbydefault.Wheneveraconfigurationchange
occurs,theswitchstartsatimeoutcounter(300secondsbydefault).Foreachadditionalconfiguration
77
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

change,thetimeoutcounterisrestarted.Ifthetimeoutexpireswithnoadditionalconfigurationchanges
beingmade,theswitchgeneratesanewcheckpoint.
SystemgeneratedcheckpointsarenamedwiththeprefixCPCfollowedbyatimestampintheformat
<YYYYMMDDHHMMSS>.Forexample:CPC20170630073127.
Systemcheckpointscanbeappliedusingthecheckpointrollbackfeatureorcopycommand.
Amaximumof32systemcheckpointscanbecreated.Beyondthislimit,thenewestsystemcheckpoint
replacestheoldestsystemcheckpoint.
Examples
Enablingsystemcheckpoints:
| switch(config)# |     | checkpoint | post-configuration |     |
| --------------- | --- | ---------- | ------------------ | --- |
Disablingsystemcheckpoints:
| switch(config)# |     | no checkpoint | post-configuration |     |
| --------------- | --- | ------------- | ------------------ | --- |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| checkpointpost-configuration |                    |     | timeout |           |
| ---------------------------- | ------------------ | --- | ------- | --------- |
| checkpoint                   | post-configuration |     | timeout | <TIMEOUT> |
| no checkpoint                | post-configuration |     | timeout | <TIMEOUT> |
Description
Setsthetimeoutforthecreationofsystemcheckpoints.Thetimeoutspecifiestheamountoftimesincethe
latestconfigurationfortheswitchtocreateasystemcheckpoint.
Thenoformofthiscommandresetsthetimeoutto300seconds,regardlessofthevalueofthe<TIMEOUT>
parameter.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
timeout <TIMEOUT> Specifiesthetimeoutinseconds.Range:5to600.Default:300.
Examples
Settingthetimeoutforsystemcheckpointsto60seconds:
Configurationandfirmwaremanagement |78

| switch(config)# |     | checkpoint | post-configuration |     | timeout 60 |
| --------------- | --- | ---------- | ------------------ | --- | ---------- |
Resettingthetimeoutforsystemcheckpointsto300seconds:
| switch(config)# |     | no checkpoint |     | post-configuration | timeout 1 |
| --------------- | --- | ------------- | --- | ------------------ | --------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
checkpointrename
| checkpoint | rename | <OLD-CHECKPOINT-NAME> |     | <NEW-CHECKPOINT-NAME> |     |
| ---------- | ------ | --------------------- | --- | --------------------- | --- |
Description
Renamesanexistingcheckpoint.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<OLD-CHECKPOINT-NAME> Specifiesthenameofanexistingcheckpointtoberenamed.
<NEW-CHECKPOINT-NAME>
Specifiesthenewnameforthecheckpoint.Thecheckpointname
canbealphanumeric.Itcanalsocontainunderscores(_)and
dashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitisusedfor
system-generatedcheckpoints.
Examples
Renamingcheckpointckpt1tocfg001:
| switch# | checkpoint | rename | ckpt1 | cfg001 |     |
| ------- | ---------- | ------ | ----- | ------ | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
79
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
checkpointrollback
| checkpoint | rollback {<CHECKPOINT-NAME> | | startup-config} |     |
| ---------- | --------------------------- | ----------------- | --- |
Description
Appliestheconfigurationfromapre-existingcheckpointorthestartupconfigurationtotherunning
configuration.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<CHECKPOINT-NAME>
Specifiesacheckpointname.
| startup-config |     | Specifiesthestartupconfiguration. |     |
| -------------- | --- | --------------------------------- | --- |
Examples
Applyingacheckpointnamedckpt1totherunningconfiguration:
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
Configurationandfirmwaremanagement |80

Copiesacheckpointconfigurationtoaremotelocationasafile.Theconfigurationisexportedincheckpoint
format,whichincludesswitchconfigurationandrelevantmetadata.
| Parameter         |     |     | Description                    |     |     |
| ----------------- | --- | --- | ------------------------------ | --- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint. |     |     |
<REMOTE-URL>
Specifiestheremotedestinationandfilenameusingthesyntax:
|     |     |     | {tftp | | sftp}://<IP-ADDRESS>[:<PORT-NUMBER>] |     |
| --- | --- | --- | ------- | ------------------------------------ | --- |
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname. |     |     |
| -------------- | --- | --- | ------------------ | --- | --- |
Examples
CopyingcheckpointconfigurationtoremotefilethroughTFTP:
switch# copy checkpoint ckpt1 tftp://192.168.1.10/ckptmeta vrf default
######################################################################### 100.0%
Success
CopyingcheckpointconfigurationtoremotefilethroughSFTP:
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
81
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| Parameter         |     |     | Description                             |
| ----------------- | --- | --- | --------------------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofanexistingcheckpoint. |
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationreceivesthecopiedcheckpointconfiguration.Ifthe
startupconfigurationisalreadypresent,thecommandoverwrites
thestartupconfiguration.
Examples
Copyingckpt1checkpointtotherunningconfiguration:
| switch# | copy checkpoint | ckpt1 running-config |     |
| ------- | --------------- | -------------------- | --- |
Success
Copyingckpt1checkpointtothestartupconfiguration:
| switch# | copy checkpoint | ckpt1 startup-config |     |
| ------- | --------------- | -------------------- | --- |
Success
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
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
Configurationandfirmwaremanagement |82

CopyingthetestcheckpointtothetestCheckfileontheUSBdrive:
| switch# | copy checkpoint | test usb:/testCheck |     |     |
| ------- | --------------- | ------------------- | --- | --- |
Success
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>
| copy <REMOTE-URL> | checkpoint | <CHECKPOINT-NAME> | [vrf <VRF-NAME>] |     |
| ----------------- | ---------- | ----------------- | ---------------- | --- |
Description
Copiesaremoteconfigurationfiletoacheckpoint.Theremoteconfigurationfilemustbeincheckpoint
format.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<REMOTE-URL> Specifiesaremotefileusingthefollowingsyntax:{tftp |
sftp}://<IP-ADDRESS>[:<PORT-NUMBER>]
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>>
<CHECKPOINT-NAME>
Specifiesthenameofthetargetcheckpoint.Thecheckpointname
canbealphanumeric.Itcanalsocontainunderscores(_)and
dashes(-).Required.
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitisusedfor
system-generatedcheckpoints.
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
Copyingacheckpointformatfiletocheckpointckpt5onthedefaultVRF:
| switch# | copy tftp://192.168.1.10/ckptmeta |     | checkpoint | ckpt5 |
| ------- | --------------------------------- | --- | ---------- | ----- |
######################################################################### 100.0%
100.0%
Success
CommandHistory
83
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

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

copy <REMOTE-URL> {running-config | startup-config}

copy <REMOTE-URL> {running-config | startup-config } [vrf <VRF-NAME>]

Description

Copies a remote file containing a switch configuration to the running configuration or to the startup
configuration.

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

Configuration and firmware management | 84

CopyingaCLIformatfiletotherunningconfigurationwithanerrorinthefile:
| switch# | copy tftp://192.168.1.10/runcli |     | running-config |
| ------- | ------------------------------- | --- | -------------- |
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Some of the configuration lines from the file were NOT applied. Use 'show
| events | -d hpe-config' | for more | info. |
| ------ | -------------- | -------- | ----- |
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>}
copy running-config {startup-config | checkpoint <CHECKPOINT-NAME>}
Description
Copiestherunningconfigurationtothestartupconfigurationortoanewcheckpoint.Ifthestartup
configurationisalreadypresent,thecommandoverwritestheexistingstartupconfiguration.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
startup-config Specifiesthatthestartupconfigurationreceivesacopyofthe
runningconfiguration.
85
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
checkpoint <CHECKPOINT-NAME> Specifiesthenameofanewcheckpointtoreceiveacopyofthe
runningconfiguration.Thecheckpointnamecanbealphanumeric.
Itcanalsocontainunderscores(_)anddashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitisusedfor
system-generatedcheckpoints.
Examples
Copyingtherunningconfigurationtothestartupconfiguration:
| switch# | copy running-config | startup-config |     |     |
| ------- | ------------------- | -------------- | --- | --- |
Success
Copyingtherunningconfigurationtoanewcheckpointnamedckpt1:
| switch# | copy running-config | checkpoint | ckpt1 |     |
| ------- | ------------------- | ---------- | ----- | --- |
Success
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy{running-config|startup-config} |     |     | <REMOTE-URL> |     |
| ----------------------------------- | --- | --- | ------------ | --- |
copy {running-config | startup-config} <REMOTE-URL> {cli | json} [vrf <VRF-NAME>]
Description
CopiestherunningconfigurationorthestartupconfigurationtoaremotefileineitherCLIorJSONformat.
| Parameter       |                   | Description |     |     |
| --------------- | ----------------- | ----------- | --- | --- |
| {running-config | | startup-config} |             |     |     |
Selectswhethertherunningconfigurationorthestartup
configurationiscopiedtoaremotefile.
| <REMOTE-URL> |     | Specifiestheremotefileusingthesyntax: |     | {tftp | |
| ------------ | --- | ------------------------------------- | --- | ------- |
sftp}://<IP-ADDRESS>[:<PORT-NUMBER>]
[;blocksize=<BLOCKSIZE-VALUE>]/<FILE-NAME>
Configurationandfirmwaremanagement |86

| Parameter      |     |     | Description                             |     |
| -------------- | --- | --- | --------------------------------------- | --- |
| {cli | json}   |     |     | Selectstheremotefileformat:P:CLIorJSON. |     |
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
| root@192.168.1.10's | password:        |                   |     |     |
| ------------------- | ---------------- | ----------------- | --- | --- |
| sftp> put           | /tmp/startcli    | startcli          |     |     |
| Uploading           | /tmp/startcli    | to /root/startcli |     |     |
| Connected           | to 192.168.1.10. |                   |     |     |
Success
CopyingastartupconfigurationtoaremotefileinJSONformat:
switch# copy startup-config sftp://root@192.168.1.10/startjson json
| root@192.168.1.10's | password:        |                    |     |     |
| ------------------- | ---------------- | ------------------ | --- | --- |
| sftp> put           | /tmp/startjson   | startjson          |     |     |
| Uploading           | /tmp/startjson   | to /root/startjson |     |     |
| Connected           | to 192.168.1.10. |                    |     |     |
Success
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy{running-config|startup-config} |     |     | <STORAGE-URL> |     |
| ----------------------------------- | --- | --- | ------------- | --- |
87
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

copy {running-config | startup-config} <STORAGE-URL> {cli | json}
Description
CopiestherunningconfigurationorastartupconfigurationtoaUSBdrive.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
{running-config | startup-config} Selectstherunningconfigurationorthestartupconfigurationto
becopiedtotheswitchUSBdrive.
<STORAGE-URL> Specifiesaremotefilewiththefollowingsyntax:usb:/<file>
| {cli | json} |     | Selectstheformatoftheremotefile:CLIorJSON. |     |
| ------------ | --- | ------------------------------------------ | --- |
Usage
TheswitchsupportsJSONandCLIfileformatswhencopyingtherunningorstartingconfigurationtothe
USBdrive.TheUSBdrivemustbeformattedwiththeFATfilesystem.
TheUSBdrivemustbeenabledandmountedwiththefollowingcommands:
| switch(config)# | usb       |     |     |
| --------------- | --------- | --- | --- |
| switch(config)# | end       |     |     |
| switch#         | usb mount |     |     |
Examples
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
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
copystartup-configrunning-config
| copy startup-config | running-config |     |     |
| ------------------- | -------------- | --- | --- |
Configurationandfirmwaremanagement |88

Description

Copies the startup configuration to the running configuration.

Examples

switch# copy startup-config running-config
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

Usage

Description

Specifies the name of a configuration file on the USB drive with the
syntax: usb:/<FILE>

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

89

ThiscommandrequiresthattheUSBdriveisformattedwiththeFATfilesystemandthatthefilebeinthe
appropriateformatasfollows:
n running-config:ThisoptionrequiresthefileontheUSBdrivebeinCLI,JSON,orcheckpointformat.
startup-config:ThisoptionrequiresthefileontheUSBdrivebeinJSONorcheckpointformat.
n
checkpoint <checkpoint-name>:ThisoptionrequiresthefileontheUSBdrivebeincheckpointformat.
n
Examples
CopyingthefilerunClifromtheUSBdrivetotherunningconfiguration:
| switch# | copy | usb:/runCli | running-config |     |     |     |
| ------- | ---- | ----------- | -------------- | --- | --- | --- |
Configuration may take several minutes to complete according to configuration
| file size |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Success
CopyingthefilestartUpfromtheUSBdrivetothestartupconfiguration:
| switch# | copy | usb:/startUp | startup-config |     |     |     |
| ------- | ---- | ------------ | -------------- | --- | --- | --- |
Success
CopyingthefiletestCheckfromtheUSBdrivetotheabccheckpoint:
| switch# | copy | usb:/testCheck | checkpoint |     | abc |     |
| ------- | ---- | -------------- | ---------- | --- | --- | --- |
Success
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
erase {checkpoint<CHECKPOINT-NAME>|startup-config|all}
| erase {checkpoint |     | <CHECKPOINT-NAME> |     | | startup-config |     | | all} |
| ----------------- | --- | ----------------- | --- | ---------------- | --- | ------ |
Description
Deletesanexistingcheckpoint,startupconfiguration,orallcheckpoints.
| Parameter  |                   |     |     | Description                    |     |     |
| ---------- | ----------------- | --- | --- | ------------------------------ | --- | --- |
| checkpoint | <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint. |     |     |
Configurationandfirmwaremanagement |90

| Parameter      |     |     | Description                       |
| -------------- | --- | --- | --------------------------------- |
| startup-config |     |     | Specifiesthestartupconfiguration. |
| all            |     |     | Specifiesallcheckpoints.          |
Examples
Erasingcheckpointckpt1:
| switch# | erase checkpoint | ckpt1 |     |
| ------- | ---------------- | ----- | --- |
Erasingthestartupconfiguration:
| switch# | erase startup-config |     |     |
| ------- | -------------------- | --- | --- |
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
| show checkpoint | <CHECKPOINT-NAME> | [json] |     |
| --------------- | ----------------- | ------ | --- |
Description
Showstheconfigurationofacheckpoint.
| Parameter         |     |     | Description                                    |
| ----------------- | --- | --- | ---------------------------------------------- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofacheckpoint.                 |
| [json]            |     |     | SpecifiesthattheoutputisdisplayedinJSONformat. |
Examples
Showingtheconfigurationoftheckpt1checkpointinCLIformat:
91
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| switch#    | show checkpoint | ckpt1 |
| ---------- | --------------- | ----- |
| Checkpoint | configuration:  |       |
!
| !Version             | ArubaOS-CX PL.10.07.0000K-75-g55e5193 |                     |
| -------------------- | ------------------------------------- | ------------------- |
| !export-password:    | default                               |                     |
| lacp system-priority |                                       | 65535               |
| user admin           | group administrators                  | password ciphertext |
AQBapQjwipebv36io0jFfde7ZzrHckncal1D+3n8XFTZKQdmYgAAADEtYOeHSme93xzdD0uz6Vr9Kl+XBzB+
2GB0UBxSF7rvgN2x8KSgkqv7iqXVQ0Te6LkSMnH4BdNaT3Bf25qyvOqmr4YakO1V3rg8zAOADkPktQD8joTH
XflzwomoIzcmv/uX
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
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/8    |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/9    |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/10   |     |
no shutdown
| vlan      | access 1 |     |
| --------- | -------- | --- |
| interface | 1/1/11   |     |
no shutdown
Configurationandfirmwaremanagement |92

| vlan        | access 1    |     |     |
| ----------- | ----------- | --- | --- |
| interface   | 1/1/12      |     |     |
| no shutdown |             |     |     |
| vlan        | access 1    |     |     |
| interface   | 1/1/13      |     |     |
| no shutdown |             |     |     |
| vlan        | access 1    |     |     |
| interface   | 1/1/14      |     |     |
| no shutdown |             |     |     |
| vlan        | access 1    |     |     |
| interface   | 1/1/15      |     |     |
| no shutdown |             |     |     |
| vlan        | access 1    |     |     |
| interface   | 1/1/16      |     |     |
| no shutdown |             |     |     |
| vlan        | access 1    |     |     |
| interface   | vlan 1      |     |     |
| ip dhcp     |             |     |     |
| snmp-server | vrf default |     |     |
!
!
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
93
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| show checkpoint | <CHECKPOINT-NAME> |     | hash [cli | | json] |
| --------------- | ----------------- | --- | --------- | ------- |
Description
ShowsaconfigurationcheckpointhashcalculatedwiththeSHA-256algorithm.Whentheoutputformatis
notspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeenaconfiguration
changesinceaprevioushashwascalculated.
| Parameter         |     |     | Description                        |     |
| ----------------- | --- | --- | ---------------------------------- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesanexistingcheckpointname. |     |
| [cli | json]      |     |     | SelectseithertheCLIorJSONformat.   |     |
Examples
ShowingacheckpointSHA-256hashinJSONformat:
| switch#     | show checkpoint | ckpt1     | hash json |     |
| ----------- | --------------- | --------- | --------- | --- |
| Calculating | the hash:       | [Success] |           |     |
The SHA-256 hash of the checkpoint in JSON format, created in image XX.10.08.xxxx:
cc7a57a9bbb4e6600d3b4180296a35f6af9e797ce9c439955dfe5de58b06da9e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version, | etc.). |     |     |     |
| ----------- | ------ | --- | --- | --- |
CommandHistory
| Release |     |     | Modification      |     |
| ------- | --- | --- | ----------------- | --- |
| 10.08   |     |     | Commandintroduced |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show checkpointpost-configuration
| show checkpoint | post-configuration |     |     |     |
| --------------- | ------------------ | --- | --- | --- |
Description
Showstheconfigurationsettingsforcreatingsystemcheckpoints.
Examples
| switch# | show checkpoint | post-configuration |     |     |
| ------- | --------------- | ------------------ | --- | --- |
Configurationandfirmwaremanagement |94

| Checkpoint | Post-Configuration | feature |     |     |
| ---------- | ------------------ | ------- | --- | --- |
-------------------------------------
| Status  | : enabled   |     |     |     |
| ------- | ----------- | --- | --- | --- |
| Timeout | (sec) : 300 |     |     |     |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
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
95
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show checkpointdate
| show checkpoint | date | <START-DATE> |     | <END-DATE> |     |     |     |     |
| --------------- | ---- | ------------ | --- | ---------- | --- | --- | --- | --- |
Description
Showsdetailedlistofallsavedcheckpointscreatedwithinthespecifieddaterange.
| Parameter |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
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
Configurationandfirmwaremanagement |96

Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutputformat
isnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description                      |
| ------------ | --- | --- | --- | -------------------------------- |
| [cli | json] |     |     |     | SelectseithertheCLIorJSONformat. |
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
| switch#     | show running-config |           | hash   | cli     |
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
| Release |     |     |     | Modification      |
| ------- | --- | --- | --- | ----------------- |
| 10.08   |     |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
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
97
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

| switch#     | show startup-config | hash          | cli     |
| ----------- | ------------------- | ------------- | ------- |
| Calculating | the hash:           | [Success]     |         |
| SHA-256     | hash of the         | config in CLI | format: |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
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
write memory
write memory
Description
Savestherunningconfigurationtothestartupconfiguration.Itisanaliasofthecommand copy running-
config startup-config.Ifthestartupconfigurationisalreadypresent,thiscommandoverwritesthe
startupconfiguration.
Examples
| switch# | write memory |     |     |
| ------- | ------------ | --- | --- |
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
Configurationandfirmwaremanagement |98

| Boot commands |     |     |     |     |
| ------------- | --- | --- | --- | --- |
boot set-default
| boot set-default | {primary |     | | secondary} |     |
| ---------------- | -------- | --- | ------------ | --- |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
primary
Selectstheprimarynetworkoperatingsystemimage.
| secondary |     |     |     | Selectsthesecondarynetworkoperatingsystemimage. |
| --------- | --- | --- | --- | ----------------------------------------------- |
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch# | boot set-default |     | primary     |     |
| ------- | ---------------- | --- | ----------- | --- |
| Default | boot image       | set | to primary. |     |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
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
99
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
secondary Selectsthesecondaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetosecondary
forfuturereboots.
serviceos Selectstheserviceoperatingsystemforthisreboot.Doesnot
changetheconfigureddefaultoperatingsystemimage.The
serviceoperatingsystemactsasastandalonebootloaderand
recoveryOSforswitchesrunningtheAOS-CXoperatingsystem
andisusedinrarecaseswhentroubleshootingaswitch.
Usage
Thiscommandrebootstheentiresystem.Ifyoudonotselectoneoftheoptionalparameters,thesystem
rebootsfromtheconfigureddefaultbootimage.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Choosingoneoftheoptionalparametersaffectsthesettingforthedefaultbootimage:
Ifyouselecttheprimaryorsecondaryoptionalparameter,thatimagebecomestheconfigureddefault
n
bootimageforfuturesystemreboots.Thecommandfailsiftheswitchisnotabletosettheoperating
systemimagetotheimageyouselected.
Youcanusetheboot set-defaultcommandtochangetheconfigureddefaultoperatingsystemimage.
Ifyouselectserviceosastheoptionalparameter,theconfigureddefaultbootimageremainsthesame,
n
andthesystemrebootsallmanagementmoduleswiththeserviceoperatingsystem.
Iftheconfigurationoftheswitchhaschangedsincethelastreboot,whenyouexecutetheboot system
commandyouarepromptedtosavetheconfigurationandyouarepromptedtoconfirmthereboot
operation.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereisan
| errorduringthesaveoperation,theboot |     |     | systemcommandisaborted. |     |
| ----------------------------------- | --- | --- | ----------------------- | --- |
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
Rebootingthesystemfromthesecondaryoperatingsystemimage,settingthesecondaryoperatingsystem
imageastheconfigureddefaultbootimage:
| switch# | boot system  | secondary         |               |          |
| ------- | ------------ | ----------------- | ------------- | -------- |
| Default | boot image   | set to secondary. |               |          |
| Do you  | want to save | the current       | configuration | (y/n)? n |
Configurationandfirmwaremanagement |100

| This will  | reboot the | entire switch    | and render | it unavailable |
| ---------- | ---------- | ---------------- | ---------- | -------------- |
| until the  | process    | is complete.     |            |                |
| Continue   | (y/n)? y   |                  |            |                |
| The system | is going   | down for reboot. |            |                |
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
parameterisspecified,showsthebootinformationfortheactivemanagementmodule.
| Parameter |     |     | Description                                         |     |
| --------- | --- | --- | --------------------------------------------------- | --- |
| all       |     |     | Showsbootinformationfortheactivemanagementmoduleand |     |
allavailablelinemodules.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereisa
previousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
101
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

CurrentBoot,upfor<SECONDS>seconds
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
Timestampbootreason
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperationoccurred
andthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |     |     |
| ------------- | ----- | --- | --- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernel crash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
| Reboot requested |     | through | database |     |
| ---------------- | --- | ------- | -------- | --- |
TherebootoccurredbecauseofarequestmadethroughtheCLIorotherAPI.
| Uncontrolled | reboot |     |     |     |
| ------------ | ------ | --- | --- | --- |
Thereasonfortherebootisnotknown.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show   | boot-history |     |     |
| ---------- | ------ | ------------ | --- | --- |
| Management | module |              |     |     |
=================
| Index : | 3                                  |        |                    |                  |
| ------- | ---------------------------------- | ------ | ------------------ | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |        |                    |                  |
| Current | Boot,                              | up for | 22 hrs 12          | mins 22 secs     |
| Index : | 2                                  |        |                    |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |        |                    |                  |
| 07 Aug  | 18 16:28:01                        |        | : Reboot requested | through database |
| Index : | 1                                  |        |                    |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |        |                    |                  |
| 07 Aug  | 18 14:08:46                        |        | : Reboot requested | through database |
| Index : | 0                                  |        |                    |                  |
| Boot ID | : 23da2b0e26d048d7b3f4b6721b69c110 |        |                    |                  |
| 07 Aug  | 18 13:00:46                        |        | : Reboot requested | through database |
switch#
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Firmware      | management |     |            | commands     |
| ------------- | ---------- | --- | ---------- | ------------ |
| copy {primary |            | |   | secondary} | <REMOTE-URL> |
Configurationandfirmwaremanagement |102

| copy {primary | | secondary} | <REMOTE-URL> | [vrf <VRF-NAME>] |     |     |
| ------------- | ------------ | ------------ | ---------------- | --- | --- |
Description
UploadsafirmwareimagetoaTFTPorSFTPserver.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
{primary | secondary} Selectstheprimaryorsecondaryimageprofiletoupload.
Required
<REMOTE-URL> SpecifiestheURLtoreceivetheuploadedfirmwareusingSFTPor
TFTP.ForinformationonhowtoformattheremoteURL,seeURL
formattingforcopycommands.
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
103
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

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
Configurationandfirmwaremanagement |104

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

Specifies the URL from which to download the firmware using SFTP
or TFTP.
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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

105

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
Configurationandfirmwaremanagement |106

| switch#     | copy   | secondary  | primary     |             |     |     |     |     |
| ----------- | ------ | ---------- | ----------- | ----------- | --- | --- | --- | --- |
| The primary |        | image will | be deleted. |             |     |     |     |     |
| Continue    | (y/n)? | y          |             |             |     |     |     |     |
| Verifying   | and    | writing    | system      | firmware... |     |     |     |     |
switch# copy sftp://stor@192.22.1.0/im-switch.swi primary vrf default
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
107
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

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
Configurationandfirmwaremanagement |108

Chapter 8

Dynamic Segmentation

Dynamic Segmentation

Applies only to the Aruba 4100i Switch Series.

Dynamic Segmentation (DS) is an enterprise network solution that combines AOS-CX security and
networking features to dynamically place clients into network segments based on client credentials. The
client network segments are dynamically carved out of the enterprise networks when on-boarding secure
clients. With dynamic segmentation, there are multiple ways to handle client traffic:

n Locally switched to a VLAN

n User Based Tunnels (UBT).

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

User-based tunneling

Applies only to the Aruba 4100i Switch Series.

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

109

At the most basic level User-Based Tunneling has two components:

n User-Roles refers to the ability to assign roles, on the fly, to a wired device/user, based on such things as
the access method of a client. When leveraging ClearPass, additional context can be added, such as time-
of-day and type-of-machine. As a result, IT staff no longer must pre-configure an access-port to VLAN
and uplinks.

n Tunneling is the ability to tunnel traffic back to an Aruba Mobility Gateway (previously known as

tunneled-node).

User-based tunneling supports two types of gateway deployments:

n Standalone Gateway Support

n Clustered Gateway Support

The recommended gatewayversion for user-based tunneling is 8.5 or greater.

The following commands are required to configure UBT:

n ip source-interface

n ubt

n ubt-client-vlan

ubt-client-vlan is needed for the local vlan or reserved vlan mode, but i is not needed for vlan-extend mode.

ubt-mode vland-extend is needed for vlan extend mode.

Components of user-based tunneling

Clients and devices

Traditionally, ports were labeled with a color and a color was assigned to a specific device. With colorless
ports, all ports on an access switch are set to authenticate with both 802.1X and MAC Authentication. When
a device connects to the network it is authenticated using either MAC Authentication or 802.1X and triggers
an enforcement policy from ClearPass, which contains an enforcement profile with a user role
configuration.

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

Dynamic Segmentation | 110

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

After the bucket map list is downloaded to the switch, a GRE heartbeat is then started between the switch
and the gateway, forming a tunnel. A regular heartbeat, using GRE, is exchanged with the gateway, which
then serves as the switch anchor gateway (SAC). This is the primary-gateway ip in the ubt zone command.
A secondary heartbeat is also established with a standby gateway, acting as a secondary switch anchor
gateway (s-SAC).

When a user connects to a secure port, the authentication sub-system on the switch sends a RADIUS
request to the RADIUS server (for example, ClearPass Policy Manager), which authenticates the user and
returns a user role to the switch in the form of a local user role (LUR) or vendor-specific attribute (VSA).

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

Points to remember

n UBT Mode: Local VLAN

o UBT is supported only on the default VRF.

o Source interface is specified using command ip source-interface.

o VLAN is specified using command ubt-client-vlan.

o ubt-client-vlan should not be used on any other feature on the switch except for the client IP

address tracking feature.

o UBT does not support tagged clients.

o UBT clients and non-UBT clients on same VLAN and same port is not supported.

o Source interface change: Disable UBT, change the source-interface, enable UBT.

n UBT Mode: VLAN extend

o UBT is supported only on the default VRF.

o Source interface is specified using command ip source-interface.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

111

o UBT client vlan is defined under role.

o DHCP snooping and ND-snooping should not enabled on a UBT client assigned VLAN.

o IGMP snooping should not be enabled on a UBT client assigned VLAN.

o The VLAN on which UBT clients are placed should not be configured on the switch uplink.

o UBT clients and non-UBT clients on the same VLAN on the same switch is not supported.

o Source interface change: Disable UBT, change the source-interface, enable UBT.

n Gateway DUR

o Downloadable gateway role is supported with switch VSA only. Mixed mode role configuration is
supported ((switch LUR + gateway radius VSA) + gateway DUR). Switch mixed role is used to send
other role attributes along with VSA.

l Use aaa authentication port-access radius-overide enable to enable.

o CPPM server FQDN/hostname configuration is supported.

Downloadable switch user role and multi-zone are not supported on the 4100i switch.

For information on IP Client Tracker, refer to the IP Client Tracker chapter in the Fundamentals Guide.

n PC behind an IP phone

You should not have a PC and phone on the same VLAN on the same port when the PC is a UBT client
and the phone is a non-UBT client. If you do, UBT clients broadcast/multicast packets will return to the
same port and corrupt the phone MAC table.

n Clients behind an L2 switch on the same VLAN

You should not have clients behind an L2 switch in a UBT environment. If UBT and non-UBT clients are
behind an L2 switch on the same VLAN, this will cause duplicate packets. Broadcast/multicast packets will
be copied to the tunnel and locally, causing the client to receive duplicate packets and network instability.

n Different user role access VLANs on the same port in UBT 1.0 mode for the 4100i switch

Two users with different user role access VLANs on the same switch port is not supported. This will lead
to a boostrap failure on the controller for the second user.

Connecting the client directly into switch ports or behind VoIP is recommended.

Comparison between UBT modes

UBT Mode: Local VLAN

UBT Mode: VLAN extend

Switch unaware of UBT user VLAN

Switch is aware of user VLAN

Colorless ports: No UBT user VLAN config
at switch

Colorless ports: UBT User VLAN config is required on switch

VLAN assignment by gateway

VLAN assignment by switch

Supports only untagged UBT users

Supports both tagged/untagged UBT users

Dynamic Segmentation | 112

| UBT Mode: | LocalVLAN | UBT Mode: | VLAN extend |
| --------- | --------- | --------- | ----------- |
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
Release Modification
10.08 --
CommandInformation
113
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
enable
enable
no enable
Description
EnablestheUBTzone.
ThenoformofthiscommanddisablestheUBTzone.
Examples
EnablingUBTforzonezone1:
| switch(config)# | ubt zone zone1 |     |
| --------------- | -------------- | --- |
switch(config-ubt-zone1)# enable
DisablingUBTforzone1:
| switch(config)#           | ubt zone zone1 |     |
| ------------------------- | -------------- | --- |
| switch(config-ubt-zone1)# | no enable      |     |
CommandHistory
| Release |     | Modification |
| ------- | --- | ------------ |
| 10.08   |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip source-interface
ip source-interface {all | ubt} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
no ip source-interface {all | ubt} {interface <IFNAME> | <IPV4-ADDR>} [vrf <VRF-NAME>]
Description
SetsasinglesourceIPaddressfortheUBTzoneVRF.ThisensuresthatalltrafficsentbyUBTzone/VRFhas
thesamesourceIPaddress,regardlessofhowitegressestheswitch.
ThiscommandprovidestwowaystosetthesourceIPaddresses:eitherbyspecifyingastaticIPaddress,or
byusingtheaddressassignedtoaswitchinterface.Ifyoudefinebothoptions,thenthestaticIPaddress
takesprecedence.
ThenoformofthiscommanddeletesthesinglesourceIPaddressforUBT.
DynamicSegmentation|114

| Parameter |     |     | Description                           |     |
| --------- | --- | --- | ------------------------------------- | --- |
| all       |     |     | Whenusednootherparametersarerequired. |     |
interface <IFNAME> SpecifiesthenameoftheinterfacefromwhichUBTobtainsits
sourceIPaddress.TheinterfacemusthaveavalidIPaddress
assignedtoit.IftheinterfacehasbothaprimaryandsecondaryIP
address,theprimaryIPaddressisused.
<IPV4-ADDR> SpecifiesthesourceIPaddresstouseforUBT.TheIPaddress
mustbedefinedontheswitch,anditmustexistonthespecified
VRF,Default:default.SpecifytheaddressinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
vrf <VRF-NAME> SpecifiesthenameoftheVRFfromwhichtheUBTzonesetsits
sourceIPaddress.
Examples
Settinginterface1/1/7asthesourceaddressforUBTforVRFdefault:
switch(config)# ip source-interface ubt interface 1/1/7 vrf default
Deletingtheconfiguredsourceinterface1/1/7asthesourceaddressforUBTforVRFdefault:
switch(config)# no ip source-interface ubt interface 1/1/7 vrf default
SpecifyingthestaticIPaddress1.1.1.1asthesourceaddressforUBTforVRFdefault:
| switch(config)# | ip source-interface |     | ubt 1.1.1.1 | vrf default |
| --------------- | ------------------- | --- | ----------- | ----------- |
DeletingtheconfiguredipaddressasthesourceaddressforUBTforVRFdefault:
| switch(config)# | no ip source-interface |     | ubt 1.1.1.1 | vrf default |
| --------------- | ---------------------- | --- | ----------- | ----------- |
CommandHistory
| Release |     |     | Modification |     |
| ------- | --- | --- | ------------ | --- |
| 10.08   |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
papi-security-key
| papi-security-key | [{ciphertext | <SEC-KEY> | | plaintext | <SEC-KEY>}] |
| ----------------- | ------------ | --------- | ----------- | ----------- |
no papi-security-key
115
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

Description
SpecifiesthesharedsecuritykeyusedtoencryptUBTPAPImessagesexchangedbetweentheswitchand
thecontrollerclusterforthezone.
Thenoformofthiscommanddeletesthesharedsecuritykey.
| Parameter  |           |     | Description                      |     |
| ---------- | --------- | --- | -------------------------------- | --- |
| ciphertext | <SEC-KEY> |     | Specifiesanencryptedsecuritykey. |     |
| plaintext  | <SEC-KEY> |     |                                  |     |
Specifiesaplaintextsecuritykey.Range:10to64characters.
NOTE:
Whenthesecuritykeyisnotprovidedonthecommandline,plaintext
securitykeypromptingoccursuponpressingEnter.Theentered
securitykeycharactersaremaskedwithasterisks..
Examples
SpecifyingthePAPIsecuritykeyforUBTzonezone1asplaintext:
| switch(config)#                         | ubt zone          | zone1             |                         |          |
| --------------------------------------- | ----------------- | ----------------- | ----------------------- | -------- |
| switch(config-ubt-zone1)#               |                   | papi-security-key | plaintext               | F82#450b |
| SpecifyingthePAPIsecuritykeyforUBTzone1 |                   |                   | withplaintextprompting: |          |
| switch(config)#                         | ubt zone          | zone1             |                         |          |
| switch(config-ubt-zone1)#               |                   | papi-security-key |                         |          |
| Enter                                   | the PAPI security | key: **********   |                         |          |
| Re-Enter                                | the PAPI security | key:              | **********              |          |
SpecifyingthePAPIsecuritykeyforUBTzone1asciphertext:
| switch(config)# | ubt zone | zone1 |     |     |
| --------------- | -------- | ----- | --- | --- |
switch(config-ubt-zone1)# papi-security-key ciphertext AQBapdAVz5...RmH3+4cpg=
RemovingthePAPIsecuritykeyforUBTzone1:
| switch(config)#           | ubt zone | zone1                |     |     |
| ------------------------- | -------- | -------------------- | --- | --- |
| switch(config-ubt-zone1)# |          | no papi-security-key |     |     |
CommandHistory
| Release |     |     | Modification |     |
| ------- | --- | --- | ------------ | --- |
| 10.08   |     |     | --           |     |
CommandInformation
DynamicSegmentation|116

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
4100i config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| primary-controller    | ip           |     |     |     |
| --------------------- | ------------ | --- | --- | --- |
| primary-controller    | ip <IP-ADDR> |     |     |     |
| no primary-controller | ip <IP-ADDR> |     |     |     |
Description
SpecifiestheIPaddressoftheprimarycontrollerIPaddressforthezone.
ThenoformofthiscommanddeletestheIPaddressoftheprimarycontroller.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IP-ADDR>
SpecifiestheIPaddressoftheprimarycontroller.
Examples
SpecifytheprimarycontrollerIPaddressforzone1:
| switch(config)# | ubt zone | zone1 |     |     |
| --------------- | -------- | ----- | --- | --- |
switch(config-ubt-zone1)#
|     |     | primary-controller |     | ip 10.116.51.10 |
| --- | --- | ------------------ | --- | --------------- |
DeletetheconfiguredprimarycontrollerIPaddress:
| switch(config)#           | ubt zone | zone1                 |     |                 |
| ------------------------- | -------- | --------------------- | --- | --------------- |
| switch(config-ubt-zone1)# |          | no primary-controller |     | ip 10.116.51.10 |
CommandHistory
| Release |     |     | Modification |     |
| ------- | --- | --- | ------------ | --- |
| 10.08   |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config-ubt-<ZONE-NAME>
| 4100i |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ----- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
sac-heartbeat-interval
| sac-heartbeat-interval    | <TIME> |        |     |     |
| ------------------------- | ------ | ------ | --- | --- |
| no sac-heartbeat-interval |        | <TIME> |     |     |
Description
SpecifiestheSACheartbeatrefreshtimeintervalinseconds.
Thenoformofthiscommandsetstheheartbeatintervaltothedefaultvalue.
117
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Parameter |     |     |     | Description                                           |     |     |
| --------- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
| <TIME>    |     |     |     | SpecifiestheSACheartbeatrefreshtimeintervalinseconds. |     |     |
Range:1to8.Default:1.
Examples
Specifyingaheartbeatrefreshintervalof1forUBTzone1:
| switch(config)#           |     | ubt zone | zone1                  |     |     |     |
| ------------------------- | --- | -------- | ---------------------- | --- | --- | --- |
| switch(config-ubt-zone1)# |     |          | sac-heartbeat-interval |     | 1   |     |
Deletingtheconfiguredheartbeatrefreshinterval:
| switch(config)#           |     | ubt zone | zone1                     |     |     |     |
| ------------------------- | --- | -------- | ------------------------- | --- | --- | --- |
| switch(config-ubt-zone1)# |     |          | no sac-heartbeat-interval |     |     |     |
CommandHistory
| Release |     |     |     | Modification |     |     |
| ------- | --- | --- | --- | ------------ | --- | --- |
| 10.08   |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
4100i config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show    | ip source-interface |     | ubt |     |     |     |
| ------- | ------------------- | --- | --- | --- | --- | --- |
| show ip | source-interface    | ubt |     |     |     |     |
Description
DisplayssourceIPaddressconfigurationinformationfortheUBTzone.
Examples
ShowingsourceIPaddressconfigurationinformation:
| switch(config)#  |     | show ip       | source-interface | ubt |     |     |
| ---------------- | --- | ------------- | ---------------- | --- | --- | --- |
| Source-interface |     | Configuration | Information      |     |     |     |
---------------------------------------------------------------------
| Protocol |     | Src-Interface |     | Src-IP |     | VRF |
| -------- | --- | ------------- | --- | ------ | --- | --- |
---------------------------------------------------------------------
| ubt |     | vlan10 |     | 10.1.1.2 |     | default |
| --- | --- | ------ | --- | -------- | --- | ------- |
CommandHistory
DynamicSegmentation|118

| Release |     |     | Modification |     |
| ------- | --- | --- | ------------ | --- |
| 10.08   |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
4100i Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
| show capacities | ubt |     |     |     |
| --------------- | --- | --- | --- | --- |
| show capacities | ubt |     |     |     |
Description
ShowsthemaximumnumberofUBTclientsandzoneswhichcanbeconfiguredinthesystem.
Example
ShowingmaximumnumberofUBTclientsandzoneswhichcanbeconfigured:
| switch#            | show capacities | ubt |     |       |
| ------------------ | --------------- | --- | --- | ----- |
| System Capacities: | Filter          | UBT |     |       |
| Capacities         | Name            |     |     | Value |
-------------------------------------------------------------------------------
| Maximum | number of UBT | clients in | a system | 768 |
| ------- | ------------- | ---------- | -------- | --- |
| Maximum | number of UBT | zones      |          | 1   |
Ona24port4100iswitch,themaxnumberofUBT clientsis768.Ona12port4100iswitch,themaxnumberof
UBT clientsis384.
IfTCAMresourcesareutilizedbyotherfeaturesandnotavailableforUBT,UBTuser-bootstrapwillfailandresult
inaresourceunavailableerrormessage.
CommandHistory
| Release |     |     | Modification |     |
| ------- | --- | --- | ------------ | --- |
| 10.08   |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
119
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| show ubt         |             |         |     |     |     |
| ---------------- | ----------- | ------- | --- | --- | --- |
| show ubt [brief] |             |         |     |     |     |
| show ubt zone    | <ZONE-NAME> | [brief] |     |     |     |
Description
ShowsglobalconfigurationinformationforUBTinadditiontodetailedorbriefinformationforaspecific
UBTzone.
Parameter Description
zone <ZONE-NAME>
Specifiesthenameofazone.Length:1to64characters.
brief Displaysbriefinformation.
Examples
ShowingglobalUBTconfigurationinformationwherelocal-VLANmodehasbeenconfigured:
| switch#       | show ubt        |                    |            |     |     |
| ------------- | --------------- | ------------------ | ---------- | --- | --- |
| Zone Name     |                 | : zone1            |            |     |     |
| UBT Mode      |                 | : local-vlan       |            |     |     |
| Primary       | Controller      | : 10.116.51.10     |            |     |     |
| Backup        | Controller      | : 10.116.51.11     |            |     |     |
| SAC HeartBeat | Interval        | : 1                |            |     |     |
| UAC KeepAlive | Interval        | : 60               |            |     |     |
| Reserved      | VLAN Identifier | : 4094             |            |     |     |
| VRF Name      |                 | : default          |            |     |     |
| Admin State   |                 | : ENABLED          |            |     |     |
| PAPI Security | Key             | : AQBapdxySvGPvdTl | ... bL4FE= |     |     |
ShowingglobalUBTconfigurationinformationwhereVLAN-extendmodehasbeenconfigured:
| switch#       | show ubt        |                        |     |        |     |
| ------------- | --------------- | ---------------------- | --- | ------ | --- |
| Zone Name     |                 | : zone1                |     |        |     |
| UBT Mode      |                 | : vlan-extend          |     |        |     |
| Primary       | Controller      | : 10.116.51.10         |     |        |     |
| Backup        | Controller      | : 10.116.51.11         |     |        |     |
| SAC HeartBeat | Interval        | : 1                    |     |        |     |
| UAC KeepAlive | Interval        | : 60                   |     |        |     |
| Reserved      | VLAN Identifier | : -NA-                 |     |        |     |
| VRF Name      |                 | : default              |     |        |     |
| Admin State   |                 | : ENABLED              |     |        |     |
| PAPI Security | Key             | : AQBapdxySvGPvdTlkYn1 | ... | bL4FE= |     |
ShowingbriefglobalUBTconfigurationinformationwherelocal-VLANmodehasbeenconfigured:
| switch(config)# | show | ubt brief |     |     |     |
| --------------- | ---- | --------- | --- | --- | --- |
----------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
----------------------------------------------------------------------------
| zone1 | local-vlan | 10.116.51.10 |     | default | Enabled |
| ----- | ---------- | ------------ | --- | ------- | ------- |
ShowingbriefglobalUBTconfigurationinformationwhereVLAN-extendmodehasbeenconfigured:
DynamicSegmentation|120

| switch# | show ubt brief |     |     |     |
| ------- | -------------- | --- | --- | --- |
--------------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
--------------------------------------------------------------------------------
| zone1 | vlan-extend | 10.116.51.10 | default | Enabled |
| ----- | ----------- | ------------ | ------- | ------- |
ShowingbriefconfigurationforUBTzone1wherelocal-VLANmodehasbeenconfigured:
| switch# | show ubt zone zone1 | brief |     |     |
| ------- | ------------------- | ----- | --- | --- |
--------------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
--------------------------------------------------------------------------------
| zone1 | local-vlan | 30.116.51.10 | default | Enabled |
| ----- | ---------- | ------------ | ------- | ------- |
ShowingbriefconfigurationforUBTzone1whereVLAN-extendmodehasbeenconfigured:
| switch# | show ubt zone zone1 | brief |     |     |
| ------- | ------------------- | ----- | --- | --- |
--------------------------------------------------------------------------------
Zone Name UBT Mode Primary Controller Address VRF Name Status
--------------------------------------------------------------------------------
| zone1 | vlan-extend | 10.116.51.10 | default | Enabled |
| ----- | ----------- | ------------ | ------- | ------- |
CommandHistory
| Release |     | Modification |     |     |
| ------- | --- | ------------ | --- | --- |
| 10.08   |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ubt | information |     |     |     |
| -------- | ----------- | --- | --- | --- |
show ubt information
| show ubt information | zone <ZONE-NAME> |     |     |     |
| -------------------- | ---------------- | --- | --- | --- |
Description
ShowsSACandUACinformationforUBT.SpecifyingazonenamedisplaysUBTinformationforthatzone.
| Parameter |     | Description                                |     |     |
| --------- | --- | ------------------------------------------ | --- | --- |
| ZONE-NAME |     | SpecifiesUBTzonename.Maximumcharacters:64. |     |     |
Examples
ShowingSACandUACinformationforthetunnelednodeserver:
121
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| switch(config)# | show | ubt information |     |     |
| --------------- | ---- | --------------- | --- | --- |
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
| Bucket | Map Information | :   |     |     |
| ------ | --------------- | --- | --- | --- |
DynamicSegmentation|122

| Bucket Map | Active | : [0...255] |       |     |              |
| ---------- | ------ | ----------- | ----- | --- | ------------ |
| Bucket ID  | A-UAC  |             | S-UAC |     | Connectivity |
----------------------------------------------------------
| 0   | 10.1.1.2 |     | 10.1.1.3 |     | L2  |
| --- | -------- | --- | -------- | --- | --- |
| 1   | 10.1.1.3 |     | 10.1.1.4 |     | L2  |
| 2   | 10.1.1.4 |     | 10.1.1.2 |     | L2  |
...
CommandHistory
| Release |     |     |     | Modification |     |
| ------- | --- | --- | --- | ------------ | --- |
| 10.08   |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show ubt       | state            |     |        |            |     |
| -------------- | ---------------- | --- | ------ | ---------- | --- |
| show ubt state |                  |     |        |            |     |
| show ubt state | zone <ZONE-NAME> |     |        |            |     |
| show ubt state | zone <ZONE-NAME> |     | uac-ip | <UAC-ADDR> |     |
Description
ShowstheglobalUBTstate.
SpecifyingazoneshowstheUBTstateofthatzone.
SpecifyingaUACIPaddressshowstheUBTstateofthatUAC.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
zone <ZONE-NAME>
SpecifiesUBTzonename.Maximumcharacters:64.
uac-ip <UAC-ADDR> SpecifiestheIPaddressoftheuseranchorcontrollerforwhichto
viewuserinformation.SpecifytheaddressinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
Examples
ShowingtheUBTstatewherelocal-VLANmodehasbeenconfigured:
switch#
show ubt state
=====================================================================
| Zone zone1: |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
=====================================================================
| Local Conductor | Server     | (LCS) | State: |     |      |
| --------------- | ---------- | ----- | ------ | --- | ---- |
| LCS Type        | IP Address |       | State  |     | Role |
123
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

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
| 00:00:00:00:00:01 |                  | 1/1/1 |     | registered |     | 5         | 13 4094      |
| ----------------- | ---------------- | ----- | --- | ---------- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): |       |     | 10.1.1.3   |     |           |              |
| User              |                  | Port  |     | State      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:02 |     | 1/1/2 |     | registered |     | 4   | 14 4094 |
| ----------------- | --- | ----- | --- | ---------- | --- | --- | ------- |
ShowingtheUBTstatewhereVLAN-extendmodehasbeenconfigured:
| switch# show | ubt | state |     |     |     |     |     |
| ------------ | --- | ----- | --- | --- | --- | --- | --- |
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
DynamicSegmentation|124

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
| 00:00:00:00:00:01 |                  | 1/1/1 | registered |     |     | 5         | 13 10        |
| ----------------- | ---------------- | ----- | ---------- | --- | --- | --------- | ------------ |
| User Anchor       | Controller(UAC): |       | 10.1.1.3   |     |     |           |              |
| User              |                  | Port  | State      |     |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:02 |     | 1/1/2 | registered |     |     | 4   | 14 20 |
| ----------------- | --- | ----- | ---------- | --- | --- | --- | ----- |
ShowingtheUBTstateofaUACwithIPaddress15.212.219.57wherelocal-VLANmodehasbeen
configured:
| switch#     | show ubt         | state | zone zone1    | uac-ip 15.212.219.57 |     |           |              |
| ----------- | ---------------- | ----- | ------------- | -------------------- | --- | --------- | ------------ |
| User Anchor | Controller(UAC): |       | 15.212.219.57 |                      |     |           |              |
| User        |                  | Port  | State         |                      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:04 |     | 1/1/20 | registered |     |     | 4   | 14 4000 |
| ----------------- | --- | ------ | ---------- | --- | --- | --- | ------- |
ShowingtheUBTstateofaUACwithIPaddress15.212.219.55whereVLAN-extendmodehasbeen
configured:
| switch#     | show ubt         | state | zone zone1    | uac-ip 15.212.219.55 |     |           |              |
| ----------- | ---------------- | ----- | ------------- | -------------------- | --- | --------- | ------------ |
| User Anchor | Controller(UAC): |       | 15.212.219.55 |                      |     |           |              |
| User        |                  | Port  | State         |                      |     | Bucket ID | Gre Key VLAN |
----------------------------------------------------------------------------------
| 00:00:00:00:00:07 |     | 1/1/10 | registered |     |     | 40  | 14 20 |
| ----------------- | --- | ------ | ---------- | --- | --- | --- | ----- |
| 00:00:00:00:00:08 |     | 1/1/12 | registered |     |     | 28  | 14 30 |
CommandHistory
| Release |     |     |     | Modification |     |     |     |
| ------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.08   |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
4100i Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
125
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |

| show ubt            | statistics |             |                   |     |     |
| ------------------- | ---------- | ----------- | ----------------- | --- | --- |
| show ubt statistics |            |             |                   |     |     |
| show ubt statistics | zone       | <ZONE-NAME> |                   |     |     |
| show ubt statistics | zone       | <ZONE-NAME> | uac-ip <UAC-ADDR> |     |     |
Description
DisplaysstatisticsforUBT.
SpecifyingazoneshowstheUBTstatisticsforthatzone.
SpecifyingaUACIPaddressshowstheUBTstatisticsforthatUAC.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
zone <ZONE-NAME>
SpecifiesUBTzonename.Maximumcharacters:64.
uac-ip <UAC-ADDR> SpecifiestheIPaddressoftheuseranchorcontrollerforwhichto
viewuserinformation.SpecifytheaddressinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
Examples
ShowingUBTstatisticswherelocal-VLANmodehasbeenconfigured:
| switch# show | ubt statistics |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
UBT Statistics
=====================================================================
| Zone zone1: |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
=====================================================================
| Control Plane  | Statistics |         |             |        |      |
| -------------- | ---------- | ------- | ----------- | ------ | ---- |
| Active         | : 10.1.1.1 |         |             |        |      |
| Bootstrap      | Tx :       | 10      | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx :       | 25      | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx :       | 21      | Bucketmap   | Ack Rx | : 10 |
| Failover       | Tx :       | 4       | Failover    | Ack Rx | : 3  |
| Unbootstrap    | Tx :       | 7       | Unbootstrap | Ack Rx | : 5  |
| Heartbeat      | Tx :       | 5       | Heartbeat   | Rx     | : 3  |
| Standby        | : 10.1.1.2 |         |             |        |      |
| Bootstrap      | Tx : 10    |         | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx : 25    |         | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx : 21    |         | Bucketmap   | Ack Rx | : 12 |
| Failover       | Tx : 4     |         | Failover    | Ack Rx | : 3  |
| Unbootstrap    | Tx : 5     |         | Unbootstrap | Ack Rx | : 3  |
| Heartbeat      | Tx : 7     |         | Heartbeat   | Rx     | : 4  |
| UAC : 10.1.1.1 |            |         |             |        |      |
| Bootstrap      | Tx : 10    |         | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    | Tx : 5     |         | Unbootstrap | Ack Rx | : 5  |
| Keepalive      | Tx : 2     |         | Keepalive   | Ack Rx | : 2  |
| UAC : 10.1.1.2 |            |         |             |        |      |
| Bootstrap      | Tx : 5     |         | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    | Tx : 0     |         | Unbootstrap | Ack Rx | : 0  |
| Keepalive      | Tx : 0     |         | Keepalive   | Ack Rx | : 0  |
| Data Plane     | Statistics |         |             |        |      |
| UAC            | Packets Tx | Packets | Rx          |        |      |
---------------------------------
| 10.1.1.1 | 45678 | 23456 |     |     |     |
| -------- | ----- | ----- | --- | --- | --- |
| 10.1.1.2 | 34567 | 23457 |     |     |     |
DynamicSegmentation|126

User Statistics
| UAC | User Count |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
-----------------------
| 10.1.1.1 | 1   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
| 10.1.1.2 | 2   |     |     |     |     |
ShowingUBTstatisticswhereVLAN-extendmodehasbeenconfigured:
| switch# show | ubt statistics |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
UBT Statistics
=====================================================================
Zone zone1:
=====================================================================
| Control Plane  | Statistics |         |             |        |      |
| -------------- | ---------- | ------- | ----------- | ------ | ---- |
| Active         | : 10.1.1.3 |         |             |        |      |
| Bootstrap      | Tx : 10    |         | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx : 25    |         | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx : 21    |         | Bucketmap   | Ack Rx | : 10 |
| Failover       | Tx : 4     |         | Failover    | Ack Rx | : 3  |
| Unbootstrap    | Tx : 7     |         | Unbootstrap | Ack Rx | : 5  |
| Heartbeat      | Tx : 5     |         | Heartbeat   | Rx     | : 3  |
| Standby        | : 10.1.1.4 |         |             |        |      |
| Bootstrap      | Tx : 10    |         | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx : 25    |         | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx : 21    |         | Bucketmap   | Ack Rx | : 12 |
| Failover       | Tx : 4     |         | Failover    | Ack Rx | : 3  |
| Unbootstrap    | Tx : 5     |         | Unbootstrap | Ack Rx | : 3  |
| Heartbeat      | Tx : 7     |         | Heartbeat   | Rx     | : 4  |
| UAC : 10.1.1.3 |            |         |             |        |      |
| Bootstrap      | Tx : 10    |         | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    | Tx : 5     |         | Unbootstrap | Ack Rx | : 5  |
| Keepalive      | Tx : 2     |         | Keepalive   | Ack Rx | : 2  |
| UAC : 10.1.1.4 |            |         |             |        |      |
| Bootstrap      | Tx : 5     |         | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    | Tx : 0     |         | Unbootstrap | Ack Rx | : 0  |
| Keepalive      | Tx : 0     |         | Keepalive   | Ack Rx | : 0  |
| Data Plane     | Statistics |         |             |        |      |
| SAC tunnel     | Rx         |         | : 444       |        |      |
| Standby-SAC    | tunnel Rx  |         | : 0         |        |      |
| UAC            | Packets Tx | Packets | Rx          |        |      |
---------------------------------
| 10.1.1.3 | 45678 | 23456 |     |     |     |
| -------- | ----- | ----- | --- | --- | --- |
| 10.1.1.4 | 34567 | 23457 |     |     |     |
User Statistics
| UAC | User Count |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
-----------------------
| 10.1.1.3 | 1   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
| 10.1.1.4 | 2   |     |     |     |     |
ShowingUBTstatisticsforzone1wherelocal-vlanmodehasbeenconfigured:
| switch# show | ubt statistics | zone | zone1 |     |     |
| ------------ | -------------- | ---- | ----- | --- | --- |
UBT Statistics
127
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

Zone zone1:
| Control Plane  | Statistics |        |            |             |        |      |
| -------------- | ---------- | ------ | ---------- | ----------- | ------ | ---- |
| Active         | : 10.1.1.3 |        |            |             |        |      |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx         | : 25   |            | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |            | Bucketmap   | Ack Rx | : 10 |
| Failover       | Tx         | : 4    |            | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 7 |            | Unbootstrap | Ack Rx | : 5  |
| Heartbeat      | Tx         | : 5    |            | Heartbeat   | Rx     | : 3  |
| Standby        | : 10.1.1.4 |        |            |             |        |      |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Rx     | : 10 |
| Nodelist       | Rx         | : 25   |            | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |            | Bucketmap   | Ack Rx | : 12 |
| Failover       | Tx         | : 4    |            | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 5 |            | Unbootstrap | Ack Rx | : 3  |
| Heartbeat      | Tx         | : 7    |            | Heartbeat   | Rx     | : 4  |
| UAC : 10.1.1.3 |            |        |            |             |        |      |
| Bootstrap      | Tx         | : 10   |            | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 5 |            | Unbootstrap | Ack Rx | : 5  |
| Keepalive      | Tx         | : 2    |            | Keepalive   | Ack Rx | : 2  |
| UAC : 10.1.1.4 |            |        |            |             |        |      |
| Bootstrap      | Tx         | : 5    |            | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 0 |            | Unbootstrap | Ack Rx | : 0  |
| Keepalive      | Tx         | : 0    |            | Keepalive   | Ack Rx | : 0  |
| Data Plane     | Statistics |        |            |             |        |      |
| UAC            | Packets    | Tx     | Packets Rx |             |        |      |
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
DynamicSegmentation|128

| Bootstrap      | Tx         | : 10   |         |       | Bootstrap   | Rx     | : 10 |
| -------------- | ---------- | ------ | ------- | ----- | ----------- | ------ | ---- |
| Nodelist       | Rx         | : 25   |         |       | Nodelist    | Ack Rx | : 6  |
| Bucketmap      | Rx         | : 21   |         |       | Bucketmap   | Ack Rx | : 12 |
| Failover       | Tx         | : 4    |         |       | Failover    | Ack Rx | : 3  |
| Unbootstrap    |            | Tx : 5 |         |       | Unbootstrap | Ack Rx | : 3  |
| Heartbeat      | Tx         | : 7    |         |       | Heartbeat   | Rx     | : 4  |
| UAC : 10.1.1.3 |            |        |         |       |             |        |      |
| Bootstrap      | Tx         | : 10   |         |       | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 5 |         |       | Unbootstrap | Ack Rx | : 5  |
| Keepalive      | Tx         | : 2    |         |       | Keepalive   | Ack Rx | : 2  |
| UAC : 10.1.1.4 |            |        |         |       |             |        |      |
| Bootstrap      | Tx         | : 5    |         |       | Bootstrap   | Ack Rx | : 5  |
| Unbootstrap    |            | Tx : 0 |         |       | Unbootstrap | Ack Rx | : 0  |
| Keepalive      | Tx         | : 0    |         |       | Keepalive   | Ack Rx | : 0  |
| Data Plane     | Statistics |        |         |       |             |        |      |
| SAC tunnel     | Rx         |        |         | : 444 |             |        |      |
| Standby-SAC    | tunnel     | Rx     |         | : 0   |             |        |      |
| UAC            | Packets    | Tx     | Packets | Rx    |             |        |      |
---------------------------------
| 10.1.1.3 | 45678 |     | 23456 |     |     |     |     |
| -------- | ----- | --- | ----- | --- | --- | --- | --- |
| 10.1.1.4 | 34567 |     | 23457 |     |     |     |     |
User Statistics
| UAC | User | Count |     |     |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- | --- |
-----------------------
| 10.1.1.3 | 1   |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 10.1.1.4 | 2   |     |     |     |     |     |     |
ShowingtheUBTstatisticsofaUACwithIPaddress101.101.101.11:
| switch# show | ubt        | statistics | zone | zone1  | uac-ip  | 101.101.101.11 |     |
| ------------ | ---------- | ---------- | ---- | ------ | ------- | -------------- | --- |
| Data Plane   | Statistics |            |      |        |         |                |     |
| SAC tunnel   | Rx         |            |      | : 6457 |         |                |     |
| Standby-SAC  | tunnel     | Rx         |      | : 0    |         |                |     |
| UAC          |            | Packets    | Tx   |        | Packets | Rx             |     |
------------------------------------------------
| 101.101.101.11 |     | : 145379605 |     |     | 145450113 |     |     |
| -------------- | --- | ----------- | --- | --- | --------- | --- | --- |
CommandHistory
| Release |     |     |     | Modification |     |     |     |
| ------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.08   |     |     |     | --           |     |     |     |
CommandInformation
129
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Platforms | Commandcontext |     | Authority                                            |     |     |
| --------- | -------------- | --- | ---------------------------------------------------- | --- | --- |
| 4100i     |                |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ubt | users |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
show ubt users [ all | count | down | mac <MAC-ADDR> | {port <IF-NAME> | <IF-RANGE>} | up]
zone <ZONE-NAME>
Description
DisplaysuserinformationforUBT.
| Parameter |     |     | Description                    |     |     |
| --------- | --- | --- | ------------------------------ | --- | --- |
| all       |     |     | Displayinformationforallusers. |     |     |
count
Displaythetotalnumberofusersconfiguredtotunneltraffic.
| down |     |     | Displaytheusersthatarenotabletotunneltraffic. |     |     |
| ---- | --- | --- | --------------------------------------------- | --- | --- |
mac <MAC-ADDR>
DisplayuserinformationbasedonMACaddress.
port <IF-NAME> | <IF-RANGE> Displayuserinformationforaspecificinterfaceorrangeof
|     |     |     | interfaces.Forexample,port           | 1/1/1orport | 1/1/1-1/1/10. |
| --- | --- | --- | ------------------------------------ | ----------- | ------------- |
| up  |     |     | Displayuserinformationthatareactive. |             |               |
zone <ZONE-NAME>
SpecifiesUBTzonename.Maximumcharacters:64.
Examples
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
Showinginformationforusersofzone1:
switch#
|     | show ubt users | all zone | zone1 |     |     |
| --- | -------------- | -------- | ----- | --- | --- |
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
DynamicSegmentation|130

Displayingthenumberofusersthataretunnelingtraffic:
| switch#      | show ubt users | count |     |              |     |     |     |
| ------------ | -------------- | ----- | --- | ------------ | --- | --- | --- |
| Total Number | of Users       | using | ubt | Zone : zone1 | is  | 2   |     |
===================================================
| Total Number | of Users | in  | all the | zones : | 2   |     |     |
| ------------ | -------- | --- | ------- | ------- | --- | --- | --- |
===================================================
Showingusersthataredown:
| switch# | show ubt users | down |     |     |     |     |     |
| ------- | -------------- | ---- | --- | --- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of Zone: | zone1 | having | Tunnel | Status DOWN |     |
| ---------- | --------- | -------- | ----- | ------ | ------ | ----------- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by * |     |     |     |
| ---------- | ---------- | --- | -------- | ---- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
----------------------------------------------------------------------------------
1/25 00:00:00:11:12:03 activation_failed authenticated User bootstrap has
failed
Showinginformationforusersofzone1thataredown:
| switch# | show ubt users | down | zone | zone1 |     |     |     |
| ------- | -------------- | ---- | ---- | ----- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of Zone: | zone1 | having | Tunnel | Status DOWN |     |
| ---------- | --------- | -------- | ----- | ------ | ------ | ----------- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by * |     |     |     |
| ---------- | ---------- | --- | -------- | ---- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
1/25 00:00:00:11:12:03 activation_failed authenticated User bootstrap has
failed
Showinginformationforusersonport2/25:
| switch# | show ubt users | port | 2/25 |     |     |     |     |
| ------- | -------------- | ---- | ---- | --- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of Zone: | zone1 |     |     |     |     |
| ---------- | --------- | -------- | ----- | --- | --- | --- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by * |     |     |     |
| ---------- | ---------- | --- | -------- | ---- | --- | --- | --- |
Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 2/25 | 00:00:00:11:12:03 |     | activated |     | authenticated |     | ---/--- |
| ---- | ----------------- | --- | --------- | --- | ------------- | --- | ------- |
Showinginformationforusersthatareup:
| switch# | show ubt users | up  |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
=====================================================================
| Displaying | UBT Users | of Zone: | zone1 | having | Tunnel | Status UP |     |
| ---------- | --------- | -------- | ----- | ------ | ------ | --------- | --- |
=====================================================================
| Downloaded | user roles | are | preceded | by * |     |     |     |
| ---------- | ---------- | --- | -------- | ---- | --- | --- | --- |
131
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

Port Mac Address Tunnel Status Secondary UserRole Failure Reason
--------------------------------------------------------------------------
| 1/25 | 00:00:00:11:12:03 | activated | authenticated |     | ---/--- |
| ---- | ----------------- | --------- | ------------- | --- | ------- |
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
| Release |     |     | Modification |     |     |
| ------- | --- | --- | ------------ | --- | --- |
| 10.08   |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
DynamicSegmentation|132

Examples
Specifyingakeepaliveintervalof60secondsforUBTzone1:
switch(config)#
|                           |     | ubt zone | zone1                  |     |     |     |
| ------------------------- | --- | -------- | ---------------------- | --- | --- | --- |
| switch(config-ubt-zone1)# |     |          | uac-keepalive-interval |     |     | 60  |
DeletingtheconfiguredUACkeepaliveinterval:
| switch(config)#           |     | ubt zone | zone1 |                        |     |     |
| ------------------------- | --- | -------- | ----- | ---------------------- | --- | --- |
| switch(config-ubt-zone1)# |     |          | no    | uac-keepalive-interval |     | 60  |
CommandHistory
| Release |     |     |     |     | Modification |     |
| ------- | --- | --- | --- | --- | ------------ | --- |
| 10.08   |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
4100i config-ubt-<ZONE-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
133
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

DeletingallUBTconfigurations:
| switch(config)# | no ubt |     |
| --------------- | ------ | --- |
CommandHistory
| Release |     | Modification |
| ------- | --- | ------------ |
| 10.08   |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ubt-client-vlan
| ubt-client-vlan    | <VLAN-ID> |     |
| ------------------ | --------- | --- |
| no ubt-client-vlan | <VLAN-ID> |     |
Description
SpecifiestheUBTClientVLANorlocalVLAN.ThisVLANisusedinlocal-VLANmodeonly.IftheUBTclient
VLANisconfiguredinVLAN-extendmodeitisignored,thisisthereservedVLANthatallclienttrafficusesto
gettothegateway.Atthegateway,VLAN andpolicywillbeassignedtotheclienttraffic.Nootherfeature
shouldbeenabledontheUBTclientVLAN.
ThenoformofthiscommandremovestheVLANtousefortunneledclients.
| Parameter |     | Description |
| --------- | --- | ----------- |
<VLAN-ID> SpecifiestheVLANIDtousefortunneledclients.Range:1-4094.
Examples
CreatingVLAN4000:
| switch(config)#           | vlan 4000 |          |
| ------------------------- | --------- | -------- |
| switch(config-vlan-4000)# | no        | shutdown |
SpecifyingUBTclientVLAN4000:
| switch(config)# | ubt-client-vlan | 4000 |
| --------------- | --------------- | ---- |
RemovingconfiguredUBTclientVLAN4000:
| switch(config)# | no ubt-client-vlan | 4000 |
| --------------- | ------------------ | ---- |
CommandHistory
DynamicSegmentation|134

| Release |     | Modification |
| ------- | --- | ------------ |
| 10.08   |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ubt mode | vlan-extend |     |
| -------- | ----------- | --- |
ubt-mode vlan-extend
no ubt-mode
Description
SelectsVLANextendedmode.WhenVLAN-extendmodeisenabledclientsareassignedtotheirUBTrole-
basedVLANinthehardwaredatapath.
Thenoformofthecommandselectslocal-VLANmode.Inlocal-VLANmodeclientsareassignedtoalocal
switchVLANandassociatedwiththeirUBTrole-basedVLANwhenclienttrafficreachesthecontroller.
ThedefaultUBTmodeislocal-VLAN.
Examples
SettingtheUBTmodetoVLAN-extend:
| switch(config)# | ubt-mode vlan-extend |     |
| --------------- | -------------------- | --- |
SettingtheUBTmodebacktothedefaultoflocal-VLAN:
| switch(config)# | no ubt-mode |     |
| --------------- | ----------- | --- |
CommandHistory
| Release |     | Modification |
| ------- | --- | ------------ |
| 10.08   |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
135
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Chapter 9

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing and modifying information about
managed devices on IP networks.

Configuring SNMP
(The SNMP agent provides read-only access.)

Procedure

1. Enable SNMP on a VRF using the command snmp-server vrf default.

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

n Sets the contact, location, and description for the switch to: JaniceM, Building2, LabSwitch.

n Sets the community string to Lab8899X.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

136

| switch(config)# | snmp-server | vrf default |     |
| --------------- | ----------- | ----------- | --- |
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
SNMP|137

Chapter 10

Aruba Central integration

Aruba Central integration

Aruba Central integration is only available on the 4100i swtich.

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

138

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

n https-server

n mfgread

n mfgwrite

n port-access

n All configuration commands except the aruba-central command

In cases where a maintenance or troubleshooting activity requires configuration updates, aruba-central
support-mode can be enabled to allow these operations.

The aruba-central support-mode enable or disable operation is effective only in the CLI session where it is

executed and does not impact the other CLI sessions.

If the user tries to execute any command that is not allowed, an Invalid input: error message is displayed.

Aruba Central commands

aruba-central

Applies only to the 4100i switch.

aruba-central
no aruba-central

Description

Creates or enters the Aruba Central configuration context (config-aruba-central).

Example

Administrators or local user group members with execution rights for this command.

Creating the Aruba Central configuration context:

Aruba Central integration | 139

| switch(config)# | aruba-central |     |     |
| --------------- | ------------- | --- | --- |
switch(config-aruba-central)#
CommandHistory
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| aruba-central | support-mode |     |     |
| ------------- | ------------ | --- | --- |
Appliesonlytothe4100iswitch.
| aruba-central    | support-mode |     |     |
| ---------------- | ------------ | --- | --- |
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
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
140
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| configuration-lockout |     |     | central | managed |     |     |
| --------------------- | --- | --- | ------- | ------- | --- | --- |
Appliesonlytothe4100iswitch.
| configuration-lockout    |     | central | managed |     |     |     |
| ------------------------ | --- | ------- | ------- | --- | --- | --- |
| no configuration-lockout |     | central | managed |     |     |     |
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
ArubaCentralintegration|141

| Release |     | Modification      |
| ------- | --- | ----------------- |
| 10.08   |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
disable
Appliesonlytothe4100iswitch.
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
| Release |     | Modification      |
| ------- | --- | ----------------- |
| 10.08   |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config-aruba-central
4100i Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
enable
Appliesonlytothe4100iswitch.
enable
Description
142
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

EnablesconnectiontoArubaCentralserver.Whentheconnectionisenabled,theswitchattemptsto
downloadthelocationoftheArubaCentralserverinoneofthefollowingwaysatstartupandafterthe
connectionislost:
n Usingcommand-lineinterface(CLI).
n ConnectingtoArubaActivateserver.
n UsingDHCPoptionsprovidedduringZTP.
DHCPserversprovidetheoptionsrequestedbythedevicetoconnecttoCentral,CentralOn-premise
managment,ortheTFTPserver.
Examples
| switch(config-aruba-central)# |     | enable |     |
| ----------------------------- | --- | ------ | --- |
switch(config-aruba-central)#
CommandHistory
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
4100i config-aruba-central Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
location-override
Appliesonlytothe4100iswitch.
| location-override | <location> | [vrf <VRF | default>] |
| ----------------- | ---------- | --------- | --------- |
no location-override
Description
Whenlocationandvrfareconfigured,theswitchoverridesexistingconnectionstoArubaCentral.The
switchattemptstoestablishconnectiontoArubaCentralwiththespecifiedlocationandVRFwithhighest
priority.
ThenoformofthiscommandremoveslocationoverridevaluesfromtheArubaCentralconfiguration
context.
| Parameter  |     |     | Description                |
| ---------- | --- | --- | -------------------------- |
| <location> |     |     | Specifiesoneofthesevalues: |
n <FQDN>:afullyqualifieddomainname.
<IPV4>:anIPv4address.
n
n <IPV6>:anIPv6address.
ArubaCentralintegration|143

Parameter

vrf <VRF-NAME>

Description

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

Removing location override values from the Aruba Central configuration context:

switch(config-aruba-central)# no location-override
switch(config-aruba-central)#

Command History

Release

10.08

Command Information

Modification

Command introduced

Platforms

Command context

Authority

4100i

config-aruba-central

Administrators or local user group members with execution rights
for this command.

show aruba-central

Applies only to the 4100i switch.

show aruba-central

Description

Shows information about Aruba Central connection and the status of the Activate server connection.

Examples

Example of a switch that has the Aruba Central connection:

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

144

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
| Release |     |     |     | Modification      |     |
| ------- | --- | --- | --- | ----------------- | --- |
| 10.08   |     |     |     | Commandintroduced |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |     |     | current-context |     |     |
| ------------------- | --- | --- | --------------- | --- | --- |
Appliesonlytothe4100iswitch.
| show running-config |     | current-context |     |     |     |
| ------------------- | --- | --------------- | --- | --- | --- |
Description
Showstherunningconfigurationforthecurrent-context.IfuserisinthecontextofAruba-Central(config-
aruba-central),thenArubaCentralrunningconfigurationisdisplayed.
Examples
ShowstherunningconfigurationofArubaCentral:
switch(config-aruba-central)# show running-config current-context
aruba-central
disable
CommandHistory
| Release |     |     |     | Modification      |     |
| ------- | --- | --- | --- | ----------------- | --- |
| 10.08   |     |     |     | Commandintroduced |     |
ArubaCentralintegration|145

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
146
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Chapter 11

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

<INTERFACE-LIST>

Usage

Description

Specifies a list of ports/LAGs to be blocked for egressing. Specify a
single interface or LAG, or a range as a comma-separated list, or
both. For example: 1/1/1, 1/1/3-1/1/6,lag2, lag1-lag4.

When a port filter configuration is applied on the same ingress physical port/LAG, the configuration is
updated with the new sets of egress ports/LAGs that are to be blocked for egressing and that are not a part
of its previous configuration. Duplicate updates on an existing port filter configuration are ignored.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

147

Whenegressports/LAGsareremovedfromtheexistingportfilterconfigurationofaningressport/LAG,
egressingisallowedagainonthoseegressports/LAGsforallpacketsoriginatingfromtheingressport/LAG.
Theno portfilter [<IF-NAME-LIST>]commandremovesportfilterconfigurationsfromtheegress
ports/LAGslistedinthe<IF-NAME-LIST>parameteronly.Allotheregressports/LAGsintheportfilter
configurationoftheingressport/LAGremainintact.
IfnophysicalportsorLAGsareprovidedfortheno portfiltercommand,thecommandremovesthe
entireportfilterconfigurationfortheingressport/LAG.
Examples
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
| show portfilter | [<IFNAME>] |     |     |     |
| --------------- | ---------- | --- | --- | --- |
Description
Portfiltering|148

Displaysfiltersettingsforallinterfacesoraspecificinterface.
| Parameter |     |     | Description                       |
| --------- | --- | --- | --------------------------------- |
| <IFNAME>  |     |     | Specifiestheingressinterfacename. |
Specifiesoneofthesevalues:
<FQDN>:afullyqualifieddomainname.
n
n <IPV4>:anIPv4address.
<IPV6>:anIPv6address.
n
Examples
Displayingallportfiltersettingsontheswitch:
switch#
show portfilter
| Incoming  | Blocked             |     |     |
| --------- | ------------------- | --- | --- |
| Interface | Outgoing Interfaces |     |     |
-------------------------------------------------------------------------------
| 1/1/1 | 1/1/3-1/1/6,lag1-lag2 |     |     |
| ----- | --------------------- | --- | --- |
1/1/3 1/1/1,1/1/5,1/1/7,1/1/9,1/1/11,1/1/13,1/1/15,1/1/17,1/1/19,1/1/21,
1/1/23,1/1/25,1/1/27,1/1/29,1/1/31,1/1/33,1/1/35
| lag2 | 1/1/1,1/1/3-1/1/6 |     |     |
| ---- | ----------------- | --- | --- |
Displayingtheportfiltersettingsforport1/1/1:
switch#
|           | show portfilter     | 1/1/1 |     |
| --------- | ------------------- | ----- | --- |
| Incoming  | Blocked             |       |     |
| Interface | Outgoing Interfaces |       |     |
-------------------------------------------------------------------------------
| 1/1/1 | 1/1/3-1/1/6,lag1-lag2 |     |     |
| ----- | --------------------- | --- | --- |
DisplayingtheportfiltersettingsforLAG2:
| switch#   | show portfilter     | lag2 |     |
| --------- | ------------------- | ---- | --- |
| Incoming  | Blocked             |      |     |
| Interface | Outgoing Interfaces |      |     |
-------------------------------------------------------------------------------
| lag2 | 1/1/1,1/1/3-1/1/6 |     |     |
| ---- | ----------------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
149
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Chapter 12

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

150

| switch(config)# |     | ip dns | domain-name | switch.com |
| --------------- | --- | ------ | ----------- | ---------- |
switch(config)#
|                 |                | ip dns     | server-address | 1.1.1.1 |
| --------------- | -------------- | ---------- | -------------- | ------- |
| switch(config)# |                | ip dns     | host myhost1   | 3.3.3.3 |
| switch(config)# |                | exit       |                |         |
| switch#         | show           | ip dns     |                |         |
| VRF             | Name : default |            |                |         |
| Domain          | Name:          | switch.com |                |         |
| Name            | Server(s):     | 1.1.1.1    |                |         |
| Host            | Name           |            |                | Address |
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
| switch(config)# |     | ip dns | domain-list | domain1.com |
| --------------- | --- | ------ | ----------- | ----------- |
| switch(config)# |     | ip dns | domain-list | domain2.com |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |     | no ip dns | domain-list | domain1.com |
| --------------- | --- | --------- | ----------- | ----------- |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
DNS|151

| Platforms |     | Commandcontext |     |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | domain-name |     |               |     |       |                  |     |
| --------- | ----------- | --- | ------------- | --- | ----- | ---------------- | --- |
| ip dns    | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME>       | ]   |
| no ip dns | domain-name |     | <DOMAIN-NAME> |     |       | [ vrf <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.By
default,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip dns
domain-list,thedomainnamedefinedwiththiscommandisignored.
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
| switch(config)# |     |     | no ip | dns | domain-name | domain.com |     |
| --------------- | --- | --- | ----- | --- | ----------- | ---------- | --- |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | host |             |     |           |       |                  |     |
| --------- | ---- | ----------- | --- | --------- | ----- | ---------------- | --- |
| ip dns    | host | <HOST-NAME> |     | <IP-ADDR> | [ vrf | <VRF-NAME>       | ]   |
| no ip dns | host | <HOST-NAME> |     | <IP-ADDR> |       | [ vrf <VRF-NAME> | ]   |
Description
152
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadofqueryinga
DNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFisdefined,the
defaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
| ThisexampledefinesanIPv4addressof        |     |     |        |      | 3.3.3.3forhost1. |                   |     |
| ---------------------------------------- | --- | --- | ------ | ---- | ---------------- | ----------------- | --- |
| switch(config)#                          |     |     | ip dns | host | host1            | 3.3.3.3           |     |
| ThisexampledefinesanIPv6addressofb::5    |     |     |        |      |                  | forhost           | 1.  |
| switch(config)#                          |     |     | ip dns | host | host1            | b::5              |     |
| Thisexampledefinesremovestheentryforhost |     |     |        |      |                  | 1withaddressb::5. |     |
switch(config)#
|     |     |     | no ip dns | host | host1 | b::5 |     |
| --- | --- | --- | --------- | ---- | ----- | ---- | --- |
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
DNS|153

ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
Thisexampledefinesanameserverat1.1.1.1.
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
| show ip dns |                  |     |     |
| ----------- | ---------------- | --- | --- |
| show ip dns | [vrf <VRF-NAME>] |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
154
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter |     | Description |
| --------- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
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
DNS|155

Device discovery and configuration

Chapter 13

Device discovery and configuration

The switch supports automatic discovery and configuration of other devices on the network.

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

Up to eight device profiles can be configured.

See the Security Guide for the following commands:

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

156

| Figure 2 ExampleofdeviceprofilesetupalongwithRADIUSinfrastructure |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- |
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
6. Addaroletoadeviceprofilewiththecommandassociate role.Makesurethattheroleisalready
created.Forinformationonhowtocreatearole,seeportaccessroleinformationintheSecurity
Guide.
7. Enablethedeviceprofilewiththecommandenable.
| Configuring                                 | a device | profile | for CDP |            |
| ------------------------------------------- | -------- | ------- | ------- | ---------- |
| 1. CreateaCDPgroupwiththecommandport-access |          |         |         | cdp-group. |
2. DefinerulesforaddingdevicestoaCDPgroupwiththecommandmatch.
3. DefinerulesforignoringdevicessothattheyarenotaddedtoaCDPgroupwiththecommand
ignore.
4. Createadeviceprofilewiththecommandport-access device-profile.
5. AddaCDPgrouptoadeviceprofilewiththecommandassociate cdp-group.
6. Addaroletoadeviceprofilewiththecommandassociate role.Makesurethattheroleisalready
created.Forinformationonhowtocreatearole,seeportaccessroleinformationintheSecurity
Guide.
7. Enableadeviceprofilewiththecommandenable.
| Configuring | a device | profile | for local | MAC match |
| ----------- | -------- | ------- | --------- | --------- |
Procedure
Devicediscoveryandconfiguration|157

1. CreateaMACgroupwiththemac-groupcommand.
2. DefinerulesforaddingdevicestoaMACgroupwiththematch (for MAC groups)command.
3. DefinerulesforignoringdevicessothattheyarenotaddedtoaMACgroupwiththeignore
(for
|     | MAC groups)command. |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- | --- |
4. Createadeviceprofilewiththeport-access device-profilecommand.
5. AssociateaMACgroupwithadeviceprofilewiththeassociate mac-groupcommand.
6. Addaroletoadeviceprofilewiththeassociate rolecommand.Makesurethattheroleisalready
created.Forinformationonhowtocreatearole,seeportaccessroleinformationintheSecurity
Guide.
7. Enableadeviceprofilewiththeenablecommand.
| Device | profile        |     | commands                  |     |                |     |     |
| ------ | -------------- | --- | ------------------------- | --- | -------------- | --- | --- |
| aaa    | authentication |     | port-accessallow-cdp-bpdu |     |                |     |     |
| aaa    | authentication |     | port-access               |     | allow-cdp-bpdu |     |     |
| no aaa | authentication |     | port-access               |     | allow-cdp-bpdu |     |     |
Description
AllowsallpacketsrelatedtotheCDP(CiscoDiscoveryProtocol)BPDU(BridgeProtocolDataUnit)ona
secureport.
ThenoformofthiscommandblockstheCDPBPDUonasecureport.Onanonsecureport,thecommand
hasnoeffect.
Examples
AllowingaCDPBPDUonsecureport1/1/1:
| switch(config)#    |                |     | interface | 1/1/1          |                |             |                |
| ------------------ | -------------- | --- | --------- | -------------- | -------------- | ----------- | -------------- |
| switch(config-if)# |                |     | aaa       | authentication |                | port-access | allow-cdp-bpdu |
| switch(config-if)# |                |     | do        | show           | running-config |             |                |
| Current            | configuration: |     |           |                |                |             |                |
!
| !Version |         | ArubaOS-CX | 10.0X.0000 |     |     |     |     |
| -------- | ------- | ---------- | ---------- | --- | --- | --- | --- |
| led      | locator | on         |            |     |     |     |     |
!
!
| vlan | 1              |     |             |     |          |     |     |
| ---- | -------------- | --- | ----------- | --- | -------- | --- | --- |
| aaa  | authentication |     | port-access |     | mac-auth |     |     |
enable
| aaa | authentication |     | port-access |     | dot1x | authenticator |     |
| --- | -------------- | --- | ----------- | --- | ----- | ------------- | --- |
enable
| interface |     | 1/1/1 |     |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- | --- |
no shutdown
|     | vlan               | access | 1   |             |     |                |     |
| --- | ------------------ | ------ | --- | ----------- | --- | -------------- | --- |
|     | aaa authentication |        |     | port-access |     | allow-cdp-bpdu |     |
|     | aaa authentication |        |     | port-access |     | mac-auth       |     |
enable
|     | aaa authentication |     |     | port-access |     | dot1x authenticator |     |
| --- | ------------------ | --- | --- | ----------- | --- | ------------------- | --- |
enable
switch(config-if)# do show port-access device-profile interface all
| Port | 1/1/1,    | Neighbor-Mac |     | 00:0c:29:9e:d1:20 |     |     |     |
| ---- | --------- | ------------ | --- | ----------------- | --- | --- | --- |
|      | Profile   | Name         | :   | access_switches   |     |     |     |
|      | LLDP      | Group        | :   |                   |     |     |     |
|      | CDP Group |              | :   | aruba-ap_cdp      |     |     |     |
158
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

|     | Role    |        | : test_ap_role |          |     |
| --- | ------- | ------ | -------------- | -------- | --- |
|     | Status  |        | : In           | Progress |     |
|     | Failure | Reason | :              |          |     |
BlockingLLDPpacketonsecureport1/1/1:
| switch(config)# |     |     | interface | 1/1/1 |     |
| --------------- | --- | --- | --------- | ----- | --- |
switch(config-if)# no aaa authentication port-access allow-cdp-bpdu
| switch(config-if)# |     |                | do show | running-config |     |
| ------------------ | --- | -------------- | ------- | -------------- | --- |
| Current            |     | configuration: |         |                |     |
!
| !Version |         | ArubaOS-CX | 10.0X.0000 |     |     |
| -------- | ------- | ---------- | ---------- | --- | --- |
| led      | locator | on         |            |     |     |
!
!
| vlan | 1              |     |             |     |          |
| ---- | -------------- | --- | ----------- | --- | -------- |
| aaa  | authentication |     | port-access |     | mac-auth |
enable
| interface |     | 1/1/1 |     |     |     |
| --------- | --- | ----- | --- | --- | --- |
no shutdown
|     | vlan | access         | 1   |             |          |
| --- | ---- | -------------- | --- | ----------- | -------- |
|     | aaa  | authentication |     | port-access | mac-auth |
enable
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |
| --------- | --- | -------------- | --- | --- | --------- |
4100i config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6000
6100
| aaa    | authentication |     | port-accessallow-lldp-bpdu |     |                 |
| ------ | -------------- | --- | -------------------------- | --- | --------------- |
| aaa    | authentication |     | port-access                |     | allow-lldp-bpdu |
| no aaa | authentication |     | port-access                |     | allow-lldp-bpdu |
Description
AllowsallpacketsrelatedtotheLLDPBPDU(BridgeProtocolDataUnit)onasecureport.
ThenoformofthiscommandblockstheLLDPBPDUonasecureport.Onanonsecureport,thecommand
hasnoeffect.
Examples
AllowinganLLDPBPDUonsecureport1/1/1:
Devicediscoveryandconfiguration|159

| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|                        |     | aaa | authentication |                | port-access | allow-lldp-bpdu |
| ---------------------- | --- | --- | -------------- | -------------- | ----------- | --------------- |
| switch(config-if)#     |     | do  | show           | running-config |             |                 |
| Current configuration: |     |     |                |                |             |                 |
!
| !Version    | ArubaOS-CX | 10.0X.0000 |     |     |     |     |
| ----------- | ---------- | ---------- | --- | --- | --- | --- |
| led locator | on         |            |     |     |     |     |
!
!
vlan 1
| aaa authentication |     | port-access |     | mac-auth |     |     |
| ------------------ | --- | ----------- | --- | -------- | --- | --- |
enable
| interface | 1/1/1 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
no shutdown
| vlan access        | 1   |     |             |     |                 |     |
| ------------------ | --- | --- | ----------- | --- | --------------- | --- |
| aaa authentication |     |     | port-access |     | allow-lldp-bpdu |     |
| aaa authentication |     |     | port-access |     | mac-auth        |     |
enable
switch(config-if)# do show port-access device-profile interface all
| Port 1/1/1, | Neighbor-Mac |     | 00:0c:29:9e:d1:20 |         |     |     |
| ----------- | ------------ | --- | ----------------- | ------- | --- | --- |
| Profile     | Name         | :   | access_switches   |         |     |     |
| LLDP        | Group        | :   | 2920-grp          |         |     |     |
| CDP Group   |              | :   |                   |         |     |     |
| Role        |              | :   | local_2920_role   |         |     |     |
| Status      |              | :   | Profile           | Applied |     |     |
| Failure     | Reason       | :   |                   |         |     |     |
BlockingLLDPBPDUonsecureport1/1/1:
| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)# no aaa authentication port-access allow-lldp-bpdu
switch(config-if)#
|                        |     | do  | show | running-config |     |     |
| ---------------------- | --- | --- | ---- | -------------- | --- | --- |
| Current configuration: |     |     |      |                |     |     |
!
| !Version | ArubaOS-CX | 10.0X.0000led |     |     | locator on |     |
| -------- | ---------- | ------------- | --- | --- | ---------- | --- |
!
!
vlan 1
| aaa authentication |     | port-access |     | mac-auth |     |     |
| ------------------ | --- | ----------- | --- | -------- | --- | --- |
enable
| interface | 1/1/1 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
no shutdown
| vlan               | access | 1   |             |     |          |     |
| ------------------ | ------ | --- | ----------- | --- | -------- | --- |
| aaa authentication |        |     | port-access |     | mac-auth |     |
enable
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
160
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
4100i config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
6100
| associate    | cdp-group |           |              |     |     |     |     |
| ------------ | --------- | --------- | ------------ | --- | --- | --- | --- |
| associate    | cdp-group |           | <GROUP-NAME> |     |     |     |     |
| no associate |           | cdp-group | <GROUP-NAME> |     |     |     |     |
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
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
6100
| associate    | lldp-group |            |              |     |     |     |     |
| ------------ | ---------- | ---------- | ------------ | --- | --- | --- | --- |
| associate    | lldp-group |            | <GROUP-NAME> |     |     |     |     |
| no associate |            | lldp-group | <GROUP-NAME> |     |     |     |     |
Description
Devicediscoveryandconfiguration|161

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
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
6100
| associate    | mac-group |              |     |     |     |     |
| ------------ | --------- | ------------ | --- | --- | --- | --- |
| associate    | mac-group | <GROUP-NAME> |     |     |     |     |
| no associate | mac-group | <GROUP-NAME> |     |     |     |     |
Description
AssociatesaMACgroupwithadeviceprofile.AmaximumoftwoMACgroupscanbeassociatedwitha
deviceprofile.
ThenoformofthiscommandremovesaMACgroupfromadeviceprofile.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME> SpecifiesthenameoftheMACgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
162
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

AssociatingtheMACgroupmac01-groupwiththedeviceprofileprofile01:
| switch(config)#                | port-access | device-profile | profile01 |             |
| ------------------------------ | ----------- | -------------- | --------- | ----------- |
| switch(config-device-profile)# |             | associate      | mac-group | mac01-group |
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
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     | forthiscommand. |     |     |
| ---- | --- | --------------- | --- | --- |
6100
| associate role |                  |     |     |     |
| -------------- | ---------------- | --- | --- | --- |
| associate role | <ROLE-NAME>      |     |     |     |
| no associate   | role <ROLE-NAME> |     |     |     |
Description
Associatesarolewithadeviceprofile.Onlyonerolecanbeassociatedwithadeviceprofile.Forinformation
onhowtoconfigurearole,seetheportaccessroleinformationintheSecurityGuide.
Thenoformofthiscommandremovesarolefromadeviceprofile.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<ROLE-NAME> Specifiesthenameoftheroletoassociatewiththedeviceprofile.
Range:1to64alphanumericcharacters.
Examples
Associatingtherolemy-rolewiththedeviceprofileprofile01:
| switch(config)# | port-access | device-profile | profile01 |     |
| --------------- | ----------- | -------------- | --------- | --- |
switch(config-device-profile)#
|     |     | associate | role my-role |     |
| --- | --- | --------- | ------------ | --- |
Removingtherolemy-rolefromthedeviceprofileprofile01:
| switch(config)#                | port-access | device-profile | profile01 |         |
| ------------------------------ | ----------- | -------------- | --------- | ------- |
| switch(config-device-profile)# |             | no associate   | role      | my-role |
Devicediscoveryandconfiguration|163

CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
6100
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
4100i config-device-profile Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
6100
enable
enable
no enable
164
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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
| switch(config-device-profile)# |             | no enable      |           |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
config-device-profile
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     | forthiscommand. |     |
| ---- | --- | --------------- | --- |
6100
| ignore (for | CDPgroups) |     |     |
| ----------- | ---------- | --- | --- |
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
Devicediscoveryandconfiguration|165

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
sw-version <SWVERSION> Specifiesthesoftwareversionoftheneighbor.Range:1to128
alphanumericcharacters.
voice-vlan-query <VLAN-ID> SpecifiestheVLANqueryvalueoftheneighbor.Range:1to65535.
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
4100i config-cdp-group Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
6100
| ignore (for | LLDPgroups) |     |     |     |
| ----------- | ----------- | --- | --- | --- |
ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type | <KEY> [value | <VALUE>]]} |
| ---------- | ------------ | ----- | ------------ | ---------- |
no ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type | <KEY> [value | <VALUE>]]} |
| ---------- | ------------ | ----- | ------------ | ---------- |
Description
DefinesaruletoignoredevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromanLLDPgroup.
166
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname <SYS-NAME> SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
| vendor-oui | <VENDOR-OUI> |     |     |     |
| ---------- | ------------ | --- | --- | --- |
SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY> |     |     | SpecifiesthevendorOUIsubtypekey.Optional. |     |
| ---------- | --- | --- | ----------------------------------------- | --- |
value <VALUE>
SpecifiesthevendorOUIsubtypevalue.Range:1to256
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
config-lldp-group
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
6100
| ignore (for | MACgroups) |     |     |     |
| ----------- | ---------- | --- | --- | --- |
[seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
Devicediscoveryandconfiguration|167

DefinesaruletoignoredevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddressmask,
orMACOrganizationalUniqueIdentifier(OUI).Upto64ignorerulescanbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaMACgroup.
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
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |
| ------------------- | ------------------ | --- | --- |
| !export-password:   | default            |     |     |
| led locator on      |                    |     |     |
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
| interface vlan1 |     |     |     |
| --------------- | --- | --- | --- |
168
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

no shutdown
ip dhcp
| mac-group grp01 |         |                   |     |
| --------------- | ------- | ----------------- | --- |
| seq 10 ignore   | mac     | 1a:2b:3c:4d:5e:6f |     |
| seq 20 match    | mac-oui | 1a:2b:3c          |     |
```
AddingaruletotheMACgroupgrp01toignoredevicesbasedonMACaddressmask,butmatchallother
devicesbelongingtoaMACOUI:
| switch(config)#           | mac-group | grp01           |                |
| ------------------------- | --------- | --------------- | -------------- |
| switch(config-mac-group)# |           | ignore mac-mask | 1a:2b:3c:4d/32 |
| switch(config-mac-group)# |           | match mac-oui   | 1a:2b:3c       |
| switch(config-mac-group)# |           | exit            |                |
| switch(config)#           | do show   | running-config  |                |
Current configuration:
!
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |
| ------------------- | ------------------ | --- | --- |
| !export-password:   | default            |     |     |
| led locator on      |                    |     |     |
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
| interface vlan1 |     |     |     |
| --------------- | --- | --- | --- |
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
switch(config)#
|                           | mac-group | grp01           |                   |
| ------------------------- | --------- | --------------- | ----------------- |
| switch(config-mac-group)# |           | ignore mac-mask | 1a:2b:3c:4d:5e/40 |
| switch(config-mac-group)# |           | ignore mac-mask | 18:e3:ab:73/32    |
AddingaruletotheMACgroupgrp03thatignoresdevicesbasedonMACOUI:
Devicediscoveryandconfiguration|169

| switch(config)# | mac-group | grp03 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|     |     | ignore | mac-oui 81:cd:93 |
| --- | --- | ------ | ---------------- |
AddingaruletotheMACgroupgrp01thatignoresdeviceswithasequencenumberandbasedonMAC
address:
switch(config)#
|                           | mac-group | grp01          |                              |
| ------------------------- | --------- | -------------- | ---------------------------- |
| switch(config-mac-group)# |           | seq 10         | ignore mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | exit           |                              |
| switch(config)#           | do show   | running-config |                              |
Current configuration:
!
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |
| ------------------- | ------------------ | --- | --- |
| !export-password:   | default            |     |     |
| led locator on      |                    |     |     |
!
!
vlan 1
| interface vlan1 |     |     |     |
| --------------- | --- | --- | --- |
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
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |
| ------------------- | ------------------ | --- | --- |
| !export-password:   | default            |     |     |
| led locator on      |                    |     |     |
!
!
vlan 1
| interface vlan1 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |
| --------------- | --- | --- | --- |
```
AddingaruletotheMACgroupgrp01thatignoresdeviceswithMACentrysequencenumberandbasedon
MACOUI:
| switch(config)# | mac-group | grp01 |     |
| --------------- | --------- | ----- | --- |
| switch(config)# | mac-group | grp01 |     |
switch(config-mac-group)#
|                           |     | seq 10 | ignore mac b2:c3:44:12:78:11   |
| ------------------------- | --- | ------ | ------------------------------ |
| switch(config-mac-group)# |     | seq 20 | ignore mac-oui 1a:2b:3c        |
| switch(config-mac-group)# |     | seq 30 | ignore mac-mask 71:14:89:42/32 |
| switch(config-mac-group)# |     | exit   |                                |
switch(config)#
170
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

switch(config)# ^Z

switch#
switch#
switch# show running-config
Current configuration:
!
!Version ArubaOS-CX PL.10.06.0002
!export-password: default
!
!
!
!
ssh server vrf default
vlan 1
spanning-tree
mac-group grp01

seq 10 ignore mac b2:c3:44:12:78:11
seq 20 ignore mac-oui 1a:2b:3c
seq 30 ignore mac-mask 71:14:89:42/32

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

Device discovery and configuration | 171

| interface 1/1/15 |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
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
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
| !export-password:   | default            |     |     |     |
| led locator on      |                    |     |     |     |
!
!
vlan 1
| interface vlan1 |     |     |     |     |
| --------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |          |                   |     |     |
| --------------- | -------- | ----------------- | --- | --- |
| seq 10 ignore   | mac      | b2:c3:44:12:78:11 |     |     |
| seq 30 ignore   | mac-mask | 71:14:89:f3/32    |     |     |
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
172
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
4100i config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights
6000 forthiscommand.
6100
mac-group
| mac-group <MAC-GROUP-NAME> |                  |     |
| -------------------------- | ---------------- | --- |
| no mac-group               | <MAC-GROUP-NAME> |     |
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
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
6000 forthiscommand.
6100
| match (for | CDPgroups) |     |
| ---------- | ---------- | --- |
match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query | <VLAN-ID>} |     |
| ---------------- | ---------- | --- |
Devicediscoveryandconfiguration|173

no match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
|     | voice-vlan-query |     | <VLAN-ID>} |     |     |     |     |
| --- | ---------------- | --- | ---------- | --- | --- | --- | --- |
Description
DefinesaruletomatchdevicesforaCDPgroup.Amaximumof32CDPgroupscanbeconfiguredonthe
switch.Upto64matchorignorerulescanbedefinedforeachgroup.
ThenoformofthiscommandremovesaruleforaddingdevicestoaCDPgroup.
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
| !Version          |         | ArubaOS-CX | Virtual.10.0X.000 |     |     |     |     |
| ----------------- | ------- | ---------- | ----------------- | --- | --- | --- | --- |
| !export-password: |         |            | default           |     |     |     |     |
| led               | locator | on         |                   |     |     |     |     |
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
174
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| switch(config)# |     | port-access | cdp-group | grp01 |     |     |
| --------------- | --- | ----------- | --------- | ----- | --- | --- |
switch(config-cdp-group)#
|     |     |     | match | vendor-oui 000b86 |     |     |
| --- | --- | --- | ----- | ----------------- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
4100i config-cdp-group Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6000
6100
| match      | (for LLDPgroups) |              |            |                         |            |     |
| ---------- | ---------------- | ------------ | ---------- | ----------------------- | ---------- | --- |
| match [seq | <SEQ-ID>]        | {sys-desc    | <SYS-DESC> | | sysname               | <SYS-NAME> | |   |
| vendor-oui |                  | <VENDOR-OUI> | [type      | <KEY> [value <VALUE>]]} |            |     |
no match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui |     | <VENDOR-OUI> | [type | <KEY> [value <VALUE>]]} |     |     |
| ---------- | --- | ------------ | ----- | ----------------------- | --- | --- |
Description
DefinesaruletomatchdevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedforagroup.
Thenoformofthiscommandremovesarule.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
| sysname | <SYS-NAME> |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- |
SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY> |         |     |     | SpecifiesthevendorOUIsubtypekey.               |     |     |
| ---------- | ------- | --- | --- | ---------------------------------------------- | --- | --- |
| value      | <VALUE> |     |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |     |     |
alphanumericcharacters.
Examples
AddingrulesthatmatchtheLLDPsystemdescriptionArubaSwitchandsystemnameArubatotheLLDP
groupnamedgrp01:
Devicediscoveryandconfiguration|175

| switch(config)# | port-access | lldp-group | grp01 |     |     |
| --------------- | ----------- | ---------- | ----- | --- | --- |
switch(config-lldp-group)#
|                            |                | match          | sys-desc | ArubaSwitch |     |
| -------------------------- | -------------- | -------------- | -------- | ----------- | --- |
| switch(config-lldp-group)# |                | match          | sysname  | Aruba       |     |
| switch(config)#            | do show        | running-config |          |             |     |
| Current                    | configuration: |                |          |             |     |
!
| !Version          | ArubaOS-CX | Virtual.10.0X.000 |     |     |     |
| ----------------- | ---------- | ----------------- | --- | --- | --- |
| !export-password: | default    |                   |     |     |     |
| led locator       | on         |                   |     |     |     |
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
config-lldp-group
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
6100
| match (for | MACgroups) |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
[seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
176
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

DefinesaruletomatchdevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddressmask,
orMACOrganizationalUniqueIdentifier(OUI).Upto64matchrulescanbedefinedforagroup.
YoumustnotconfigurethefollowingspecialMACaddresses:
n NullMAC—Forexample,00:00:00:00:00:00or00:00:00/32
n MulticastMAC
n BroadcastMAC—Forexample,ff:ff:ff:ff:ff:ff:ff
SystemMAC
n
Althoughtheswitchacceptstheseaddresses,itwillnotprocesstheseaddressesforthelocalMACmatch
feature.
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
Devicediscoveryandconfiguration|177

| switch(config)# | mac-group | grp03 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|                           |     | match mac-oui | 81:cd:93 |
| ------------------------- | --- | ------------- | -------- |
| switch(config-mac-group)# |     | exit          |          |
AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress:
| switch(config)#           | mac-group | grp01          |                       |
| ------------------------- | --------- | -------------- | --------------------- |
| switch(config-mac-group)# |           | seq 10 match   | mac b2:c3:44:12:78:11 |
| switch(config-mac-group)# |           | exit           |                       |
| switch(config)#           | do show   | running-config |                       |
Current configuration:
!
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |
| ------------------- | ------------------ | --- | --- |
| !export-password:   | default            |     |     |
| led locator on      |                    |     |     |
!
!
vlan 1
| interface vlan1 |     |     |     |
| --------------- | --- | --- | --- |
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
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |
| ------------------- | ------------------ | --- | --- |
| !export-password:   | default            |     |     |
| led locator on      |                    |     |     |
!
!
vlan 1
| interface vlan1 |     |     |     |
| --------------- | --- | --- | --- |
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
178
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

!
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
| !export-password:   | default            |     |     |     |
| led locator on      |                    |     |     |     |
!
!
vlan 1
| interface vlan1 |     |     |     |     |
| --------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |                |     |     |
| --------------- | --------------------- | -------------- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |                |     |     |
| seq 20 match    | mac-oui               | 1a:2b:3c       |     |     |
| seq 30 match    | mac-mask              | 71:14:89:f3/32 |     |     |
```
RemovingdevicesfromtheMACgroupgrp01basedonMACOUI:
| switch(config)#           | mac-group | grp01  |                  |          |
| ------------------------- | --------- | ------ | ---------------- | -------- |
| switch(config-mac-group)# |           | no seq | 20 match mac-oui | 1a:2b:3c |
| switch(config-mac-group)# |           | exit   |                  |          |
switch(config)#
|     | do show | running-config |     |     |
| --- | ------- | -------------- | --- | --- |
Current configuration:
!
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
| !export-password:   | default            |     |     |     |
| led locator on      |                    |     |     |     |
!
!
vlan 1
interface
vlan1
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
| switch(config-mac-group)# |     | exit |     |     |
| ------------------------- | --- | ---- | --- | --- |
switch(config)#
|     | do show | running-config |     |     |
| --- | ------- | -------------- | --- | --- |
Current configuration:
!
| !Version ArubaOS-CX | Virtual.10.0X.0001 |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
| !export-password:   | default            |     |     |     |
| led locator on      |                    |     |     |     |
!
!
vlan 1
interface
vlan1
no shutdown
ip dhcp
Devicediscoveryandconfiguration|179

| mac-group | grp03        |     |                            |     |
| --------- | ------------ | --- | -------------------------- | --- |
|           | seq 10 match |     | mac-mask 10:14:a3:b7:55/40 |     |
```
RemovingdevicesfromtheMACgroupgrp03basedonMACaddressmask:
| switch(config)# |     | mac-group | grp03 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-mac-group)# no seq 10 match mac-mask 10:14:a3:b7:55/40
| switch(config-mac-group)# |                |     | exit                |     |
| ------------------------- | -------------- | --- | ------------------- | --- |
| switch(config)#           |                | do  | show running-config |     |
| Current                   | configuration: |     |                     |     |
!
| !Version          | ArubaOS-CX |     | Virtual.10.0X.0001 |     |
| ----------------- | ---------- | --- | ------------------ | --- |
| !export-password: |            |     | default            |     |
| led locator       | on         |     |                    |     |
!
!
| vlan      | 1     |     |     |     |
| --------- | ----- | --- | --- | --- |
| interface | vlan1 |     |     |     |
no shutdown
ip dhcp
| mac-group | grp03 |     |     |     |
| --------- | ----- | --- | --- | --- |
```
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
4100i config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
6100
port-accesscdp-group
| port-access    | cdp-group |     | <CDP-GROUP-NAME> |     |
| -------------- | --------- | --- | ---------------- | --- |
| no port-access | cdp-group |     | <CDP-GROUP-NAME> |     |
Description
CreatesaCDP(CiscoDiscoveryProtocol)groupormodifiesanexistingCDPgroup.ACDPGroupisusedto
classifyconnecteddevicesbasedontheCDPpacketdetailsadvertisedbythedevice.Amaximumof32CDP
groupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesaCDPgroup.
180
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | --- | --- | ----------------------------- | --- |

| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<CDP-GROUP-NAME> SpecifiesthenameoftheCDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatingaCDPgroupnamedgrp01:
| switch(config)#           |     |     | port-access |     | cdp-group |                  | grp01     |     |
| ------------------------- | --- | --- | ----------- | --- | --------- | ---------------- | --------- | --- |
| switch(config-cdp-group)# |     |     |             |     | match     | platform         | CISCO     |     |
| switch(config-cdp-group)# |     |     |             |     | match     | sw-version       | 11.2(12)P |     |
| switch(config-cdp-group)# |     |     |             |     | match     | voice-vlan-query |           | 512 |
switch(config-cdp-group)# seq 50 match platform cisco sw-version 11.2(12)P voice-
| vlan-query                |     | 512            |         |                |      |     |     |     |
| ------------------------- | --- | -------------- | ------- | -------------- | ---- | --- | --- | --- |
| switch(config-cdp-group)# |     |                |         |                | exit |     |     |     |
| switch(config)#           |     |                | do show | running-config |      |     |     |     |
| Current                   |     | configuration: |         |                |      |     |     |     |
!
| !Version          |         | ArubaOS-CX |         | Virtual.10.0X.000 |     |     |     |     |
| ----------------- | ------- | ---------- | ------- | ----------------- | --- | --- | --- | --- |
| !export-password: |         |            | default |                   |     |     |     |     |
| led               | locator | on         |         |                   |     |     |     |     |
!
!
| vlan        | 1   |           |                  |       |           |     |     |     |
| ----------- | --- | --------- | ---------------- | ----- | --------- | --- | --- | --- |
| port-access |     | cdp-group |                  | grp01 |           |     |     |     |
|             | seq | 10 match  | platform         |       | CISCO     |     |     |     |
|             | seq | 20 match  | sw-version       |       | 11.2(12)P |     |     |     |
|             | seq | 30 match  | voice-vlan-query |       |           | 512 |     |     |
seq 50 match platform cisco sw-version 11.2(12)P voice-vlan-query 512
RemovingaCDPgroupnamedgrp01:
| switch(config)# |     |     | no port-access |     |     | cdp-group | grp01 |     |
| --------------- | --- | --- | -------------- | --- | --- | --------- | ----- | --- |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- | --- |
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --- | --------------- | --- | --- |
6100
port-accessdevice-profile
| port-access    |     | device-profile |     | <DEVICE-PROFILE-NAME> |                       |     |     |     |
| -------------- | --- | -------------- | --- | --------------------- | --------------------- | --- | --- | --- |
| no port-access |     | device-profile |     |                       | <DEVICE-PROFILE-NAME> |     |     |     |
Description
Devicediscoveryandconfiguration|181

Createsanewdeviceprofileandswitchestotheconfig-device-profilecontext.Amaximumof32device
profilescanbecreated.
Thenoformofthiscommandremovesadeviceprofile.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<DEVICE-PROFILE-NAME> Specifiesthenameofadeviceprofile.Range:1to32
alphanumericcharacters.
Examples
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
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
6100
| port-accessdevice-profile |     |     | mode | block-until-profile-applied |     |
| ------------------------- | --- | --- | ---- | --------------------------- | --- |
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
182
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

ThenoformofthiscommandremovesaruleforaddingdevicestoaMACgroup.
Example
Configuringblock-until-profileappliedmodeonport1/1/1:
| switch(config)#    |     | interface |             | 1/1/1          |     |     |
| ------------------ | --- | --------- | ----------- | -------------- | --- | --- |
| switch(config-if)# |     |           | port-access | device-profile |     |     |
switch(config-if-deviceprofile)# mode block-until-profile-applied
| switch(config-if-deviceprofile)# |     |     |     |     | end |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
config-if
| 4100i |                         |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ----- | ----------------------- | --- | --- | --- | -------------------------------------------------- | --- |
| 6000  | config-if-deviceprofile |     |     |     | rightsforthiscommand.                              |     |
6100
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
<LLDP-GROUP-NAME> SpecifiesthenameoftheLLDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatinganLLDPgroupnamedgrp01:
| switch(config)# |     | port-access |     | lldp-group |     | grp01 |
| --------------- | --- | ----------- | --- | ---------- | --- | ----- |
switch(config-lldp-group)#
RemovinganLLDPgroupnamedgrp01:
| switch(config)# |     | no  | port-access | lldp-group |     | grp01 |
| --------------- | --- | --- | ----------- | ---------- | --- | ----- |
Devicediscoveryandconfiguration|183

CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6100
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
client-status <MAC-ADDR> SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.
name <DEVICE-PROFILE-NAME> Specifiesthenameofthedeviceprofile.
Examples
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
184
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

|     | Role    |        | :   | local_2920_role  |     |     |     |
| --- | ------- | ------ | --- | ---------------- | --- | --- | --- |
|     | State   |        | :   | Enabled          |     |     |     |
|     | Profile | Name   | :   | lobbyaps         |     |     |     |
|     | LLDP    | Groups | :   |                  |     |     |     |
|     | CDP     | Groups | :   | lobby_ap_cdp_grp |     |     |     |
|     | MAC     | Groups | :   |                  |     |     |     |
|     | Role    |        | :   | test_ap_role     |     |     |     |
|     | State   |        | :   | Disabled         |     |     |     |
Showingtheappliedstateofthedeviceprofileoninterface1/1/3:
switch#
|     |     | show port-access |     | device-profile |     | interface | 1/1/3 client-status |
| --- | --- | ---------------- | --- | -------------- | --- | --------- | ------------------- |
00:0c:29:9e:d1:20
| Port | 1/1/3,  | Neighbor-Mac |     | 00:0c:29:9e:d1:20 |          |           |      |
| ---- | ------- | ------------ | --- | ----------------- | -------- | --------- | ---- |
|      | Profile | Name         | :   | lobbyaps          |          |           |      |
|      | LLDP    | Group        | :   |                   |          |           |      |
|      | CDP     | Group        | :   | aruba-ap_cdp      |          |           |      |
|      | MAC     | Group        | :   |                   |          |           |      |
|      | Role    |              | :   | test_ap_role      |          |           |      |
|      | Status  |              | :   | Failed            |          |           |      |
|      | Failure | Reason       | :   | Failed            | to apply | MAC based | VLAN |
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
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6000
6100
LLDP
TheIEEE802.1ABLinkLayerDiscoveryProtocol(LLDP)providesastandards-basedmethodfornetwork
devicestodiscovereachotherandexchangeinformationabouttheircapabilities.AnLLDPdeviceadvertises
itselftoadjacent(neighbor)devicesbytransmittingLLDPdatapacketsonallinterfacesonwhichoutbound
Devicediscoveryandconfiguration|185

LLDP is enabled, and reading LLDP advertisements from neighbor devices on ports on which inbound LLDP
is enabled. Inbound packets from neighbor devices are stored in a special LLDP MIB (management
information base). This information can then be queried by other devices through SNMP.

LLDP information is used by network management tools to create accurate physical network topologies by
determining which devices are neighbors and through which interfaces they connect. LLDP operates at layer
2 and requires an LLDP agent to be active on each interface that sends and receives LLDP advertisements.
LLDP advertisements can contain a variable number of TLV (type, length, value) information elements. Each
TLV describes a single attribute of a device such as: system capabilities, management IP address, device ID,
port ID.

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

LLDP is supported on interfaces mapped to a physical port. It is not supported on logical interfaces, such as
loopback, tunnels, and SVIs.

Operating modes

When LLDP is enabled, the switch periodically transmits an LLDP advertisement (packet) out each active
port enabled for outbound LLDP transmissions and receives LLDP advertisements on each active port
enabled to receive LLDP traffic.

The LLDP agent can operate in one of the following modes:

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

186

n Transmit and receive (TxRx): This is the default setting on all ports. It enables a given port to both

transmit and receive LLDP packets and to store the data from received (inbound) LLDP packets in the
switch's MIB.

n Transmit only (Tx): Enables a port to transmit LLDP packets that can be read by LLDP neighbors.

However, the port drops inbound LLDP packets from LLDP neighbors without reading them. This
prevents the switch from learning about LLDP neighbors on that port.

n Receive only (Rx): Enables a port to receive and read LLDP packets from LLDP neighbors and to store the

packet data in the switch's MIB. However, the port does not transmit outbound LLDP packets. This
prevents LLDP neighbors from learning about the switch through that port.

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
the LLDP agent receives a new LLDP frame, the aging timer restarts. When the aging timer decreases to
zero, all saved information ages out.

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

Device discovery and configuration | 187

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

n Port VLAN ID: On an L2 port, contains access or native VLAN ID. Trunk allowed VLANs information are

not advertised as part of the Port VLAN ID TLV.

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
b. SVI.
c. Base MAC.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

188

4. Bydefault,allsupportedTLVsaresentandreceived.Tocustomizethelist,usethecommandlldp
select-tlv.
5. Bydefault,supportfortheLLDP-MEDTLVisenabled.Tocustomizesettings,usethecommandslldp
| medandlldp | med-location. |     |
| ---------- | ------------- | --- |
6. Ifrequired,adjustLLDPtimer,holdtime,reinitializationdelay,andtransmitdelayfromtheirdefault
valueswiththecommandslldp timer,lldp holdtime,lldp reinit,andlldp txdelay.
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablesLLDPsupport.
n DisablesLLDPtransmissiononinterface1/1/1.
| switch(config)# | lldp |     |
| --------------- | ---- | --- |
switch(config)#
interface 1/1/1
| switch(config-copp)# | no lldp transmit |     |
| -------------------- | ---------------- | --- |
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
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
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
ClearsallLLDPneighborstatistics.
Devicediscoveryandconfiguration|189

Examples
ClearingallLLDPneighborstatistics:
switch#
clear lldp statistics
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
190
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

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
Devicediscoveryandconfiguration|191

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
n IPaddressofSVI[interfaceVLAN<vid>]
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv4managementaddressoftheswitch.
192
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

| Parameter   |     | Description                                      |     |
| ----------- | --- | ------------------------------------------------ | --- |
| <IPV4-ADDR> |     | SpecifiesthemanagementaddressoftheswitchasanIPv4 |     |
format(x.x.x.x),wherexisadecimalvaluefrom0to255.
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
n IPaddressofSVI[interfaceVLAN<vid>]
n BaseMACaddressoftheswitch
ThenoformofthiscommandremovestheIPv6managementaddressoftheswitch.
| Parameter   |     | Description                      |     |
| ----------- | --- | -------------------------------- | --- |
| <IPV6-ADDR> |     | SpecifiesanIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
Settingthemanagementaddressto2001:db8:85a3::8a2e:370:7334:
Devicediscoveryandconfiguration|193

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
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
poe [priority-override] SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
|     |     | dot3 | poeandlldp | med poeareenabled,thelldp | dot3 poe3 |
| --- | --- | ---- | ---------- | ------------------------- | --------- |
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
194
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| switch(config-if)# |     | lldp | med | network-policy |     |     |
| ------------------ | --- | ---- | --- | -------------- | --- | --- |
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
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpmed-location
| lldp med-location | {civic-addr |     |             | | elin-addr | }   |     |
| ----------------- | ----------- | --- | ----------- | ----------- | --- | --- |
| no med-location   | {civic-addr |     | | elin-addr |             | }   |     |
Description
ConfiguressupportfortheLLDP-MEDTLV.Supportsonlycivicaddressandemergencylocationinformation
number(ELIN).Coordinate-basedlocationisnotsupported.
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
switch(config-if)# lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
Devicediscoveryandconfiguration|195

DisablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# no lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpreceive
lldp receive
no lldp receive
Description
EnablesreceptionofLLDPinformationonaninterface.Bydefault,LLDPreceptionisenabledonallactive
interfaces.
ThenoformofthiscommanddisablesreceptionofLLDPinformationonaninterface.
Examples
EnablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1   |
| ------------------ | --------- | ------- |
| switch(config-if)# | lldp      | receive |
DisablingLLDPreceptiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1   |
| ------------------ | --------- | ------- |
| switch(config-if)# | no lldp   | receive |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
196
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

lldpreinit
| lldp reinit | <TIME> |     |
| ----------- | ------ | --- |
no lldp reinit
Description
Setstheamountoftime(inseconds)towaitbeforeperformingLLDPinitializationonaninterface.
Thenoformofthiscommandsetsthereinitializationtimetoitsdefaultvalueof2seconds.
| Parameter |     | Description |
| --------- | --- | ----------- |
<TIME> Specifiesthereinitializationtimeinseconds.Range:1to10.
Default:2seconds.
Examples
Settingthereinitializationtimeto5seconds:
| switch(config)# | lldp reinit | 5   |
| --------------- | ----------- | --- |
Settingthereinitializationtimetothedefaultvalueof2seconds:
| switch(config)# | no lldp reinit |     |
| --------------- | -------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldpselect-tlv
| lldp select-tlv    | <TLV-NAME> |     |
| ------------------ | ---------- | --- |
| no lldp select-tlv | <TLV-NAME> |     |
Description
SelectsaTLVthattheLLDPagentwillsendandreceive.Bydefault,allsupportedTLVsaresentandreceived.
ThenoformofthiscommandstopstheLLDPagentfromsendingandreceivingaspecificTLV.
| Parameter |     | Description |
| --------- | --- | ----------- |
select-tlv <TLV-NAME> SpecifiestheTLVnametosend.ThefollowingTLVnamesare
supported:
Devicediscoveryandconfiguration|197

| Parameter |     | Description |
| --------- | --- | ----------- |
n management-address: Selectedasfollows:
1. IPv4orIPV6managementaddress.
2. Iflayer2,theIPaddressoftheSVI.
3. BaseMACaddressoftheswitch.
n port-description: Adescriptionoftheport.
n port-vlan-id: VLANIDassignedtotheport.
system-capabilities: Identifiestheprimaryswitch
n
functionsthatareenabled,suchasrouting.
n system-description: Descriptionofthesystem,
comprisedofthefollowinginformation:hardware
serialnumber,hardwarerevisionnumber,andfirmware
version.
system-name: Hostnameassignedtotheswitch.
n
Examples
StoppingtheLLDPagentfromsendingtheport-descriptionTLV:
| switch(config)# | no lldp select-tlv | port-description |
| --------------- | ------------------ | ---------------- |
EnablingtheLLDPagenttosendtheport-descriptionTLV:
| switch(config)# | lldp select-tlv | port-description |
| --------------- | --------------- | ---------------- |
CommandHistory
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
198
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

lldp timer=16
n
lldp txdelay=4
n
And,thisisaninvalidconfiguration:
lldp timer=5
n
txdelay=2
n lldp
Whencopyingasavedconfigurationtotherunningconfiguration,thevalueforlldp timerisappliedbeforethe
valueoflldp txdelay.Thiscanresultinaconfigurationerrorifthesavedconfigurationhasavalueoflldp
timerthatisnotfourtimesthevalueoflldp txdelayintherunningconfiguration.
Forexample,ifthesavedconfigurationhasthesettings:
n lldp timer=16
lldp txdelay=4
n
Andtherunningconfigurationhasthesettings:
n lldp timer=30
n lldp txdelay=7
Thenyouwillseeanerrorindicatingthatcertainconfigurationsettingscouldnotbeapplied,andyouwillhaveto
| manuallyadjustthevalueoflldp |     | txdelayintherunningconfiguration. |
| ---------------------------- | --- | --------------------------------- |
Thenoformofthiscommandsetstheupdateintervaltoitsdefaultvalueof30seconds.
| Parameter |     | Description                                           |
| --------- | --- | ----------------------------------------------------- |
| <TIME>    |     | Specifiestheupdateinterval(inseconds).Range:5to32768. |
Default:30.
Examples
Settingtheupdateintervalto7seconds:
| switch(config)# | lldp timer | 7   |
| --------------- | ---------- | --- |
Settingtheupdateintervaltothedefaultvalueof30seconds:
| switch(config)# | no lldp | timer |
| --------------- | ------- | ----- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
Devicediscoveryandconfiguration|199

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptransmit
lldp transsmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionisenabledon
allactiveinterfaces.
ThenoformofthiscommanddisablestransmissionofLLDPinformationonaninterface.
Examples
EnablingLLDPtransmissiononinterface1/1/1:
switch(config)#
|                    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | lldp      | transsmit |
DisablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | no lldp   | transsmit |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptxdelay
| lldp txdelay | <TIME> |     |
| ------------ | ------ | --- |
no lldp txdelay
Description
Setstheamountoftime(inseconds)towaitbeforesendingLLDPinformationfromanyinterface.The
maximumvaluefortxdelayis25%ofthevalueoflldp tx timer.
Thenoformofthiscommandsetsthedelaytimetoitsdefaultvalueof2seconds.
200
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

| Parameter |     | Description                                           |
| --------- | --- | ----------------------------------------------------- |
| <TIME>    |     | Specifiesthedelaytimeinseconds.Range:0to10.Default:2. |
Examples
Settingthedelaytimeto8seconds:
| switch(config)# | lldp txdelay | 8   |
| --------------- | ------------ | --- |
Settingthedelaytimetothedefaultvalueof2seconds:
| switch(config)# | no lldp txdelay |     |
| --------------- | --------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldptrapenable
| lldp trap enable |        |     |
| ---------------- | ------ | --- |
| no lldp trap     | enable |     |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenotrequired
tobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
switch(config)#
|     | lldp trap | enable |
| --- | --------- | ------ |
EnablingLLDPtrapgenerationoninterfacelevel:
Devicediscoveryandconfiguration|201

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
202
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

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
| show lldp | configuration |     | [<INTERFACE-ID>] |     |     |     |
| --------- | ------------- | --- | ---------------- | --- | --- | --- |
Description
ShowsLLDPconfigurationsettingsforallinterfacesoraspecificinterface.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
Devicediscoveryandconfiguration|203

Example
Showingconfigurationsettingsforallinterfaces:
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
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show lldplocal-device
| show lldp | local-device |     |     |
| --------- | ------------ | --- | --- |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsareconfigured
onanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDsonaccess
interfaces.
Example
ShowingglobalLLDPinformationonly:
| switch# | show lldp local-device |     |     |
| ------- | ---------------------- | --- | --- |
| Global  | Data                   |     |     |
===========
204
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Chassis-ID |      | : 88:3a:30:47:c1:c0 |     |     |
| ---------- | ---- | ------------------- | --- | --- |
| System     | Name | : 6100              |     |     |
System Description : Aruba JL679A PL.10.06.0001-346-g56a12a8f4cf15
| Management   | Address   | : 88:3a:30:47:c1:c0 |        |     |
| ------------ | --------- | ------------------- | ------ | --- |
| Capabilities | Available | : Bridge,           | Router |     |
| Capabilities | Enabled   | : Bridge,           | Router |     |
| TTL          |           | : 120               |        |     |
Showingallportsexcept1/1/11asadministrativelydown:
| switch# | show lldp | local-device |     |     |
| ------- | --------- | ------------ | --- | --- |
Global Data
===========
| Chassis-ID |      | : 88:3a:30:47:c1:c0 |     |     |
| ---------- | ---- | ------------------- | --- | --- |
| System     | Name | : 6100              |     |     |
System Description : Aruba JL679A PL.10.06.0001-346-g56a12a8f4cf15
| Management   | Address   | : 11.11.11.11 |        |     |
| ------------ | --------- | ------------- | ------ | --- |
| Capabilities | Available | : Bridge,     | Router |     |
| Capabilities | Enabled   | : Bridge,     | Router |     |
| TTL          |           | : 120         |        |     |
| Port Based   | Data      |               |        |     |
===============
| Port-ID           |           | : 1/1/11      |        |     |
| ----------------- | --------- | ------------- | ------ | --- |
| Port-Desc         |           | : "1/1/11"    |        |     |
| Port Mgmt-Address |           | : 11.11.11.11 |        |     |
| Port VLAN         | ID        | : 1           |        |     |
| Parent            | Interface | : interface   | 1/1/11 |     |
switch#
| switch# | show lldp | local-device |     |     |
| ------- | --------- | ------------ | --- | --- |
Global Data
===========
| Chassis-ID   |             | : 88:3a:30:47:c1:c0 |        |               |
| ------------ | ----------- | ------------------- | ------ | ------------- |
| System       | Name        | : 4100i             |        |               |
| System       | Description | : Aruba             | JL817A | RL.10.08.0001 |
| Management   | Address     | : 11.11.11.11       |        |               |
| Capabilities | Available   | : Bridge,           | Router |               |
| Capabilities | Enabled     | : Bridge,           | Router |               |
| TTL          |             | : 120               |        |               |
| Port Based   | Data        |                     |        |               |
===============
| Port-ID           |           | : 1/1/11      |        |     |
| ----------------- | --------- | ------------- | ------ | --- |
| Port-Desc         |           | : "1/1/11"    |        |     |
| Port Mgmt-Address |           | : 11.11.11.11 |        |     |
| Port VLAN         | ID        | : 1           |        |     |
| Parent            | Interface | : interface   | 1/1/11 |     |
switch#
Inthisexample,alltheportsexcept1/1/11areadministrativelydown,andVLANID100isconfiguredon
thisaccessinterface.
Devicediscoveryandconfiguration|205

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

show lldp neighbor-info [<INTERFACE-NAME>]

Description

Displays information about neighboring devices for all interfaces or for a specific interface. The information
displayed varies depending on the type of neighbor connected and the type of TLVs sent by the neighbor.

Parameter

<INTERFACE-NAME>

Description

Specifies the interface for which to show information for
neighboring devices. Use the format member/slot/port (for
example, 1/3/1).

Examples

Showing LLDP information for all interfaces:

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

206

| switch# show  | lldp | neighbor-info |     |     |     |     |
| ------------- | ---- | ------------- | --- | --- | --- | --- |
| LLDP Neighbor |      | Information   |     |     |     |     |
=========================
| Total Neighbor |            | Entries          | : 1     |     |           |              |
| -------------- | ---------- | ---------------- | ------- | --- | --------- | ------------ |
| Total Neighbor |            | Entries Deleted  | : 5     |     |           |              |
| Total Neighbor |            | Entries Dropped  | : 0     |     |           |              |
| Total Neighbor |            | Entries Aged-Out | : 3     |     |           |              |
| LOCAL-PORT     | CHASSIS-ID |                  | PORT-ID |     | PORT-DESC | TTL SYS-NAME |
--------------------------------------------------------------------------------
| 1/1/2 | 38:21:c7:5c:df:40 |     | 1/1/2 |     | 1/1/2 | 120 switch |
| ----- | ----------------- | --- | ----- | --- | ----- | ---------- |
| 1/1/3 | f8:60:f0:c9:e0:a0 |     | 1/1/3 |     | 1/1/3 | 120 switch |
Showinginformationforinterface1/1/3whenithasonlyoneswitchconnectedasaneighbor:
| Aruba-6100-Switch2#  |                     | show lldp | neighbor-info       |        | 1/1/3         |     |
| -------------------- | ------------------- | --------- | ------------------- | ------ | ------------- | --- |
| Port                 |                     |           | : 1/1/3             |        |               |     |
| Neighbor             | Entries             |           | : 1                 |        |               |     |
| Neighbor             | Entries             | Deleted   | : 1                 |        |               |     |
| Neighbor             | Entries             | Dropped   | : 0                 |        |               |     |
| Neighbor             | Entries             | Aged-Out  | : 1                 |        |               |     |
| Neighbor             | Chassis-Name        |           | : 6100              |        |               |     |
| Neighbor             | Chassis-Description |           | : Aruba             | JL679A | PL.10.06.0001 |     |
| Neighbor             | Chassis-ID          |           | : 88:3a:30:47:d1:c0 |        |               |     |
| Neighbor             | Management-Address  |           | : 88:3a:30:47:d1:c0 |        |               |     |
| Chassis Capabilities |                     | Available | : Bridge,           | Router |               |     |
| Chassis Capabilities |                     | Enabled   | : Bridge,           | Router |               |     |
| Neighbor             | Port-ID             |           | : 1/1/3             |        |               |     |
| Neighbor             | Port-Desc           |           | : 1/1/3             |        |               |     |
| Neighbor             | Port                | VLAN ID   | : 1                 |        |               |     |
| TTL                  |                     |           | : 120               |        |               |     |
| Neighbor             | Mac-Phy             | details   |                     |        |               |     |
| Neighbor             | Auto-neg            | Supported | : True              |        |               |     |
| Neighbor             | Auto-neg            | Enabled   | : True              |        |               |     |
Neighbor Auto-ned Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighnor | MAU Type |     | : 1000 | BASETFD |     |     |
| -------- | -------- | --- | ------ | ------- | --- | --- |
Showingneighborinformationforinterface1/3/2whenithasEEEenabledandsuccessfullyauto-
negotiated:
| switch# show         | lldp                | neighbor-info | 1/3/2               |        |                 |     |
| -------------------- | ------------------- | ------------- | ------------------- | ------ | --------------- | --- |
| Port                 |                     |               | : 1/3/2             |        |                 |     |
| Neighbor             | Entries             |               | : 1                 |        |                 |     |
| Neighbor             | Entries             | Deleted       | : 1                 |        |                 |     |
| Neighbor             | Entries             | Dropped       | : 0                 |        |                 |     |
| Neighbor             | Entries             | Aged-Out      | : 1                 |        |                 |     |
| Neighbor             | Chassis-Name        |               | : BLDG01-F1-6300    |        |                 |     |
| Neighbor             | Chassis-Description |               | : Aruba             | JL668A | FL.10.07.0001BN |     |
| Neighbor             | Chassis-ID          |               | : 88:3a:30:92:a5:c0 |        |                 |     |
| Neighbor             | Management-Address  |               | : 10.6.9.15         |        |                 |     |
| Chassis Capabilities |                     | Available     | : Bridge,           | Router |                 |     |
| Chassis Capabilities |                     | Enabled       | : Bridge,           | Router |                 |     |
| Neighbor             | Port-ID             |               | : 1/1/1             |        |                 |     |
| Neighbor             | Port-Desc           |               | : 1/1/1             |        |                 |     |
| Neighbor             | Port                | VLAN ID       | : 1                 |        |                 |     |
Devicediscoveryandconfiguration|207

| TTL      |     |          |           | : 120  |
| -------- | --- | -------- | --------- | ------ |
| Neighbor |     | Mac-Phy  | details   |        |
| Neighbor |     | Auto-neg | Supported | : true |
| Neighbor |     | Auto-Neg | Enabled   | : true |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor |     | MAU type        |      | : 1000 BASETFD |
| -------- | --- | --------------- | ---- | -------------- |
| Neighbor |     | EEE information |      | : DOT3         |
| Neighbor |     | TX Wake         | time | : 17 us        |
| Neighbor |     | RX Wake         | time | : 17 us        |
| Neighbor |     | Fallback        | time | : 17 us        |
| Neighbor |     | TX Echo         | time | : 17 us        |
| Neighbor |     | RX Echo         | time | : 17 us        |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |
| --------- | --- | -------------- | --- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show lldpneighbor-infodetail
| show lldp | neighbor-info |     | detail |     |
| --------- | ------------- | --- | ------ | --- |
Description
ShowsdetailedLLDPneighborinformationforallLLDPneighborconnectedinterfaces.
Examples
ShowingdetailedLLDPinformationforallinterfaces:
| switch# |          | show lldp | neighbor-info | detail |
| ------- | -------- | --------- | ------------- | ------ |
| LLDP    | Neighbor |           | Information   |        |
=========================
| Total | Neighbor |     | Entries          | : 6 |
| ----- | -------- | --- | ---------------- | --- |
| Total | Neighbor |     | Entries Deleted  | : 2 |
| Total | Neighbor |     | Entries Dropped  | : 0 |
| Total | Neighbor |     | Entries Aged-Out | : 2 |
--------------------------------------------------------------------------------
| Port     |     |         |         | : 1/1/1 |
| -------- | --- | ------- | ------- | ------- |
| Neighbor |     | Entries |         | : 1     |
| Neighbor |     | Entries | Deleted | : 0     |
| Neighbor |     | Entries | Dropped | : 0     |
208
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | --- | --- | ----------------------------- | --- |

| Neighbor Entries             | Aged-Out  | : 0                 |        |
| ---------------------------- | --------- | ------------------- | ------ |
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
Devicediscoveryandconfiguration|209

| Neighbor | Auto-Neg |     | Enabled | : true |     |
| -------- | -------- | --- | ------- | ------ | --- |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor | MAU | type |     | : 1000 | BASETFD |
| -------- | --- | ---- | --- | ------ | ------- |
--------------------------------------------------------------------------------
| Port     |                     |          |           | : 1/1/46            |        |
| -------- | ------------------- | -------- | --------- | ------------------- | ------ |
| Neighbor | Entries             |          |           | : 1                 |        |
| Neighbor | Entries             | Deleted  |           | : 0                 |        |
| Neighbor | Entries             | Dropped  |           | : 0                 |        |
| Neighbor | Entries             | Aged-Out |           | : 0                 |        |
| Neighbor | Chassis-Name        |          |           | : 6300              |        |
| Neighbor | Chassis-Description |          |           | : Aruba             | ...    |
| Neighbor | Chassis-ID          |          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor | Management-Address  |          |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities        |          | Available | : Bridge,           | Router |
| Chassis  | Capabilities        |          | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID             |          |           | : 1/1/19            |        |
| Neighbor | Port-Desc           |          |           | : 1/1/19            |        |
| Neighbor | Port                | VLAN     | ID        | : 1                 |        |
| TTL      |                     |          |           | : 120               |        |
| Neighbor | Mac-Phy             | details  |           |                     |        |
| Neighbor | Auto-neg            |          | Supported | : true              |        |
| Neighbor | Auto-Neg            |          | Enabled   | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor | MAU | type |     | : 1000 | BASETFD |
| -------- | --- | ---- | --- | ------ | ------- |
--------------------------------------------------------------------------------
| Port     |                     |          |     | : 1/1/47            |     |
| -------- | ------------------- | -------- | --- | ------------------- | --- |
| Neighbor | Entries             |          |     | : 1                 |     |
| Neighbor | Entries             | Deleted  |     | : 0                 |     |
| Neighbor | Entries             | Dropped  |     | : 0                 |     |
| Neighbor | Entries             | Aged-Out |     | : 0                 |     |
| Neighbor | Chassis-Name        |          |     | : 6300              |     |
| Neighbor | Chassis-Description |          |     | : Aruba             | ... |
| Neighbor | Chassis-ID          |          |     | : 38:11:17:1a:d5:00 |     |
| Neighbor | Management-Address  |          |     | : 38:11:17:1a:d5:00 |     |
| Chassis  | Cap                 |          |     |                     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show lldpstatistics
| show lldp | statistics |     | [<INTERFACE-ID>] |     |     |
| --------- | ---------- | --- | ---------------- | --- | --- |
Description
210
| AOS-CX10.08FundamentalsGuide| |     |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- |

ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
Example
Showingglobalstatisticsforallinterfaces:
| switch#     | show copp-policy     | statistics |     |     |
| ----------- | -------------------- | ---------- | --- | --- |
| switch#     | show lldp statistics |            |     |     |
| LLDP Global | Statistics           |            |     |     |
==========================================================================
| Total Packets | Transmitted  |               | : 25 |     |
| ------------- | ------------ | ------------- | ---- | --- |
| Total Packets | Received     |               | : 20 |     |
| Total Packets | Received     | And Discarded | : 0  |     |
| Total TLVs    | Unrecognized |               | : 0  |     |
| LLDP Port     | Statistics   |               |      |     |
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
Devicediscoveryandconfiguration|211

LLDP Statistics
===============
| Port Name |                           | : 1/1/1 |
| --------- | ------------------------- | ------- |
| Packets   | Transmitted               | : 159   |
| Packets   | Received                  | : 163   |
| Packets   | Received And Discarded    | : 0     |
| Packets   | Received And Unrecognized | : 0     |
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
show lldptlv
| show lldp tlv |     |     |
| ------------- | --- | --- |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
Example
| switch# | show lldp tlv |     |
| ------- | ------------- | --- |
TLVs Advertised
===============
| Management | Address |     |
| ---------- | ------- | --- |
Port Description
Port VLAN-ID
| System Capabilities |     |     |
| ------------------- | --- | --- |
| System Description  |     |     |
| System Name         |     |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
212
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Platforms

Command context

Authority

All platforms

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

Cisco Discovery Protocol (CDP)
Cisco Discovery Protocol (CDP) is a proprietary layer 2 protocol supported by most Cisco devices. It is used
to exchange information, such as software version, device capabilities, and voice VLAN information,
between directly connected devices, such as a VoIP phone and a switch.

CDP support

By default, CDP is enabled on each active switch port. This is a read-only capability, which means the switch
can receive and store information about adjacent CDP devices, but does not generate CDP packets (except
when communicating with Cisco IP phones.)

The switch supports CDPv2 only and does not support SNMP MIB traps.

When a CDP-enabled port receives a CDP packet from another CDP device, it enters data for that device into
the CDP Neighbors table, along with the port number on which the data was received. It does not forward
the packet. The switch also periodically purges the table of any entries that have expired. (The holdtime for
any data entry in the switch CDP Neighbors table is configured in the device transmitting the CDP packet
and cannot be controlled in the switch receiving the packet.) A switch reviews the list of CDP neighbor
entries every three seconds and purges any expired entries.

Support for legacy Cisco IP phones

Autoconfiguration of legacy Cisco IP phones for tagged voice VLAN support requires CDPv2.

On initial boot-up, and sometimes periodically, a Cisco phone queries the switch and advertises information
about itself using CDPv2. When the switch receives the VoIP VLAN Query TLV (type 0x0f) from the phone,
the switch immediately responds with the voice VLAN ID in a reply packet using the VoIP VLAN Reply TLV
(type 0x0e). This enables the Cisco phone to boot properly and send traffic on the advertised voice VLAN
ID.

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

Device discovery and configuration | 213

ConfiguresCDPsupportgloballyonallactiveinterfacesoronaspecificinterface.Bydefault,CDPisenabled
onallactiveinterfaces.
WhenCDPisenabled,theswitchaddsentriestoitsCDPNeighborstableforanyCDPpacketsitreceives
fromneighboringCDPdevices.
WhenCDPisdisabled,theCDPNeighborstableisclearedandtheswitchdropsallinboundCDPpackets
withoutenteringthedataintheCDPNeighborstable.
ThenoformofthiscommanddisablesCDPsupportgloballyonallactiveinterfacesoronaspecificinterface.
Examples
EnablingCDPglobally:
| switch(config)# | cdp |     |
| --------------- | --- | --- |
DisablingCDPglobally:
| switch(config)# | no cdp |     |
| --------------- | ------ | --- |
EnablingCDPoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | cdp       |       |
DisablingCDPoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | no cdp    |       |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
config-if forthiscommand.
clear cdpcounters
| clear cdp counters |     |     |
| ------------------ | --- | --- |
Description
ClearsCDPcounters.
Examples
ClearingCDPcounters:
214
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

switch(config) clear cdp counters

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

clear cdp neighbor-info

clear cdp neighbor-info

Description

Clears CDP neighbor information.

Examples

Clearing CDP neighbor information:

switch(config) clear neighbor-info

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

show cdp

show cdp

Description

Shows CDP information for all interfaces.

Examples

Showing CDP information:

Device discovery and configuration | 215

| switch(config)# | show cdp    |     |     |
| --------------- | ----------- | --- | --- |
| CDP Global      | Information |     |     |
======================
| CDP      | : Enabled          |     |     |
| -------- | ------------------ | --- | --- |
| CDP Mode | : Rx only          |     |     |
| CDP Hold | Time : 180 seconds |     |     |
| Port     | CDP                |     |     |
| -------- | --------------     |     |     |
| 1/1/1    | Enabled            |     |     |
| 1/1/2    | Enabled            |     |     |
| 1/1/3    | Enabled            |     |     |
| 1/1/4    | Enabled            |     |     |
| 1/1/5    | Enabled            |     |     |
| 1/1/6    | Enabled            |     |     |
| 1/1/7    | Enabled            |     |     |
| 1/1/8    | Enabled            |     |     |
| 1/1/9    | Enabled            |     |     |
| 1/1/10   | Enabled            |     |     |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show cdpneighbor-info
show cdp neighbor-info <INTERFACE-ID>
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
Examples
ShowingallCDPneighborinformation:
| switch(config)# | show cdp neighbor-info |          |            |
| --------------- | ---------------------- | -------- | ---------- |
| Port            | Device ID              | Platform | Capability |
-------------------------------------------------------------------------------
| 1/1/1 | myswitch | cisco WS-C2950-12 | SI  |
| ----- | -------- | ----------------- | --- |
ShowingCDPinformationforinterface1/1/1:
216
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| switch(config)# |         | show  | cdp neighbor-info   |          | 1/1/1 |     |     |
| --------------- | ------- | ----- | ------------------- | -------- | ----- | --- | --- |
| Local Port      | :       | 1/1/1 |                     |          |       |     |     |
| MAC             |         |       | : 3c:a8:2a:7b:6b:2b |          |       |     |     |
| Device ID       |         |       | : SEPd4adbd2a30d6   |          |       |     |     |
| Address         |         |       | : 2.71.0.230        |          |       |     |     |
| Platform        |         |       | : Cisco             | IP Phone | 3905  |     |     |
| Duplex          |         |       | : full              |          |       |     |     |
| Capability      |         |       | : host              |          |       |     |     |
| Voice VLAN      | Support |       | : Yes               |          |       |     |     |
| Neighbor        | Port-ID |       | : Port 1            |          |       |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show cdptraffic
show cdp neighbor-info
Description
ShowsCDPstatisticsforeachinterface.
Examples
ShowingCDPtrafficstatistics:
| switch(config)# |     | show | cdp traffic |     |     |     |     |
| --------------- | --- | ---- | ----------- | --- | --- | --- | --- |
CDP Statistics
====================
| Port | Transmitted |     | Frames |     | Received Frames | Discarded | Frames |
| ---- | ----------- | --- | ------ | --- | --------------- | --------- | ------ |
--------------------------------------------------------------------------------
| 1/1/1 |     | 0   |     |     | 4   | 0   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     | 0   |     |     | 0   | 0   |     |
| 1/1/3 |     | 0   |     |     | 2   | 0   |     |
| 1/1/4 |     | 0   |     |     | 0   | 0   |     |
| 1/1/5 |     | 0   |     |     | 0   | 0   |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
Devicediscoveryandconfiguration|217

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution rights
for this command.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

218

Chapter 14

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

n ZTP operations are supported over IPv4 connections only. IPv6 connections are not supported for ZTP

operations.

n You must configure the DHCP server to provide a standards-based ZTP server solution. Options and
features that are specific to Network Management Solution (NMS) tools, such as AirWave, are not
supported.

o Supported DHCP options are:

DHCP option

Description

43

43 suboption 144

43 suboption 145

Vendor Specific Information

Name of the configuration file

Name of the firmware image file

43 suboption 148

HTTP Proxy FQDN or IPv4 address

60

66

67

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

219

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
server. The switch must be able to reach the TFTP server and DHCP server on the same subnet.

Switches support provisioning through a network connected to a data port or through a network
connected to the in-band management interface VLAN 1.

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

Zero Touch Provisioning | 220

The ZTP operation begins when power is applied to the switch after the network cable is installed.

6. Assuming the downloaded configuration includes a way to access the CLI of the switch, you can enter
the following command to show the options offered by the DHCP server and the status of the ZTP
operation:
show ztp information

ZTP process during switch boot

1. The switch boots up with the factory default configuration.

If the ZTP operation detects that the switch configuration is different from the factory default
configuration, the ZTP operation ends. The switch must be configured at the installation site.

2. The switch sends out a DHCP discovery from the in-band management interface.

The switch waits to receive DHCP options indefinitely or until the running configuration is modified. If
a DHCP IP address is received but no DHCP options are received, the switch waits an additional
minute before ending the ZTP operation.

After the ZTP operation ends, there is no automatic retry. You can either attempt to boot the switch
with the factory default configuration again, configure the switch at the installation site, or use the
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

n Aruba Central Location (optional)

n HTTP Proxy Location (optional)

4.

If a firmware image file is offered, the ZTP operation downloads the image file from the TFTP server
to the switch. If the current switch image and downloaded firmware image version do not match,
then the switch boots with the downloaded image:
n If the image upgrade fails, the switch retains its original firmware image and the ZTP operation

ends with a failed status.

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

221

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

ZTP commands

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

Zero Touch Provisioning | 222

TherunningconfigurationwasmodifiedbyauserwhiletheZTPoperationwasinprogress.
Failed-TFTPserverunreachable
TheTFTPserverisnotreachableatthespecifiedIPaddress.
| Failed-TFTPserverinformation |     | unavailable |     |     |     |
| ---------------------------- | --- | ----------- | --- | --- | --- |
TheimagefilenameorconfigfilenameisprovidedwithouttheTFTPserverlocationtofetchthefilesfrom
andZTPentersfailedstate.
| Failed-Invalidconfiguration |     | file received |     |     |     |
| --------------------------- | --- | ------------- | --- | --- | --- |
Eitherthefiletransferoftheconfigurationfilefailed,ortheconfigurationfileisinvalid(anerroroccurred
whileattemptingtoapplytheconfiguration).
| Failed-Invalidimage | file received |     |     |     |     |
| ------------------- | ------------- | --- | --- | --- | --- |
Eitherthefiletransferofthefirmwareimagefilefailed,orthefirmwareimagefileisinvalid(anerror
occurredwhileverifyingtheimage).
Examples
ShowingswitchimagedownloadinprogressafterreceivingZTP options:
| switch#         | show ztp information |                                |         |          |                  |
| --------------- | -------------------- | ------------------------------ | ------- | -------- | ---------------- |
| TFTP Server     |                      | : 10.0.0.2                     |         |          |                  |
| Image File      |                      | : TL_10_02_0001.swi            |         |          |                  |
| Configuration   | File                 | : config_file                  |         |          |                  |
| ZTP Status      |                      | : In-progress                  | - Image | download | and verification |
| Aruba Central   | Location             | : secure.arubanetworks.com     |         |          |                  |
| Force-Provision |                      | : Disabled                     |         |          |                  |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |         |          |                  |
ShowingswitchimagedownloadfailureafterreceivingZTPoptions:
| switch#         | show ztp information |                                |          |             |       |
| --------------- | -------------------- | ------------------------------ | -------- | ----------- | ----- |
| TFTP Server     |                      | : 10.0.0.2                     |          |             |       |
| Image File      |                      | : TL_10_02_0001.swi            |          |             |       |
| Configuration   | File                 | : config_file                  |          |             |       |
| ZTP Status      |                      | : Failed                       | - Unable | to download | image |
| Aruba Central   | Location             | : secure.arubanetworks.com     |          |             |       |
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
| Force-Provision |                      | : Disabled                     |                 |     |          |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |                 |     |          |
ShowingswitchconfigurationdownloadfailureafterreceivingZTPoptions:
| switch#     | show ztp information |            |     |     |     |
| ----------- | -------------------- | ---------- | --- | --- | --- |
| TFTP Server |                      | : 10.0.0.2 |     |     |     |
223
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

| Image File      |          | : TL_10_02_0001.swi            |          |                           |
| --------------- | -------- | ------------------------------ | -------- | ------------------------- |
| Configuration   | File     | : config_file                  |          |                           |
| ZTP Status      |          | : Failed                       | - Unable | to download configuration |
| Aruba Central   | Location | : secure.arubanetworks.com     |          |                           |
| Force-Provision |          | : Disabled                     |          |                           |
| HTTP Proxy      | Location | : http.proxy.arubanetworks.com |          |                           |
Showingswitchfailuretoupdatestart-upconfrigurationafterdownloadingconfigurationreceivedfromZTP
options:
| switch#       | show ztp information |                     |     |     |
| ------------- | -------------------- | ------------------- | --- | --- |
| TFTP Server   |                      | : 10.0.0.2          |     |     |
| Image File    |                      | : TL_10_02_0001.swi |     |     |
| Configuration | File                 | : config_file       |     |     |
ZTP Status : Failed - Could not copy to start-up configuration
| Aruba Central   | Location | : secure.arubanetworks.com     |     |     |
| --------------- | -------- | ------------------------------ | --- | --- |
| Force-Provision |          | : Disabled                     |     |     |
| HTTP Proxy      | Location | : http.proxy.arubanetworks.com |     |     |
Inthefollowingexample,theZTPoperationsucceeded,andbothanimagefileandaconfigurationfilewere
provided.
| switch#         | show ztp information |                       |     |     |
| --------------- | -------------------- | --------------------- | --- | --- |
| TFTP Server     |                      | : 20.1.1.4            |     |     |
| Image File      |                      | : PL_10_06_0001BT.swi |     |     |
| Configuration   | File                 | : bristol_maxlimit    |     |     |
| Status          |                      | : Success             |     |     |
| Force-Provision |                      | : Disabled            |     |     |
switch#
Inthefollowingexample,theZTPoptionsucceeded.Aconfigurationfilewasnotprovided,butanimagefile
wasprovided.
switch#
show ztp information
| TFTP Server     |      | : 20.1.1.4         |     |     |
| --------------- | ---- | ------------------ | --- | --- |
| Image File      |      | : NA               |     |     |
| Configuration   | File | : bristol_maxlimit |     |     |
| Status          |      | : Success          |     |     |
| Force-Provision |      | : Disabled         |     |     |
switch#
Inthefollowingexample,theZTPoperationfailedbecausetheTFTPserverwasunreachable.
| switch#         | show ztp information |                       |               |             |
| --------------- | -------------------- | --------------------- | ------------- | ----------- |
| TFTP Server     |                      | : 20.1.1.4            |               |             |
| Image File      |                      | : PL_10_06_0001BT.swi |               |             |
| Configuration   | File                 | : bristol_maxlimit    |               |             |
| Status          |                      | : Failed              | - TFTP server | unreachable |
| Force-Provision |                      | : Disabled            |               |             |
switch#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchdidnotreceiveanyoptions
fromtheDHCPserverforZTPwithin1minuteofreceivingtheIPaddressfromtheserver.
ZeroTouchProvisioning|224

| switch##      | show ztp information |      |     |     |     |
| ------------- | -------------------- | ---- | --- | --- | --- |
| TFTP Server   |                      | : NA |     |     |     |
| Image File    |                      | : NA |     |     |     |
| Configuration | File                 | : NA |     |     |     |
Status : Failed - Timed out while waiting to receive ZTP options
| Force-Provision |     | : Disabled |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- |
switch#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchwasbootedfroma
configurationthatwasnotthefactorydefaultconfiguration.
| switch#         | show ztp information |                       |                  |               |          |
| --------------- | -------------------- | --------------------- | ---------------- | ------------- | -------- |
| TFTP Server     |                      | : 20.1.1.4            |                  |               |          |
| Image File      |                      | : PL_10_06_0001BT.swi |                  |               |          |
| Configuration   | File                 | : bristol_maxlimit    |                  |               |          |
| Status          |                      | : Failed              | - Custom startup | configuration | detected |
| Force-Provision |                      | : Disabled            |                  |               |          |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
| switch# | configure terminal |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- |
switch(config)#
|     | ztp | force-provision |     |     |     |
| --- | --- | --------------- | --- | --- | --- |
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
225
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| switch#         | show ztp information |                     |     |
| --------------- | -------------------- | ------------------- | --- |
| TFTP Server     |                      | : 10.0.0.2          |     |
| Image File      |                      | : TL_10_02_0001.swi |     |
| Configuration   | File                 | : ztp.cfg           |     |
| Status          |                      | : Success           |     |
| Aruba Central   | Location             | : NA                |     |
| Force-Provision |                      | : Enabled           |     |
| HTTP Proxy      | Location             | : NA                |     |
Inthefollowingexample,force-provisionisdisabled.
| switch# | configure terminal |     |     |
| ------- | ------------------ | --- | --- |
switch(config)#
|     | no ztp | force-provision |     |
| --- | ------ | --------------- | --- |
Inthefollowingexample,force-provisionstatusischeckedwhiledisabled.
| switch#         | show ztp information |                     |     |
| --------------- | -------------------- | ------------------- | --- |
| TFTP Server     |                      | : 10.0.0.2          |     |
| Image File      |                      | : TL_10_02_0001.swi |     |
| Configuration   | File                 | : ztp.cfg           |     |
| Status          |                      | : Success           |     |
| Aruba Central   | Location             | : NA                |     |
| Force-Provision |                      | : Disabled          |     |
| HTTP Proxy      | Location             | : NA                |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
ZeroTouchProvisioning|226

Chapter 15
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
| clear events  |              |          |        |              |          |
clear events
Description
Clearsupeventlogs.Usingtheshow eventscommandwillonlydisplaythelogsgeneratedaftertheclear
eventscommand.
Examples
Clearingallgeneratedeventlogs:
| switch# | show events |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- |
---------------------------------------------------
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 27 |     |     |
| ----------- | ------------- | ---------- | ----- | --- | --- |
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to 36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 49 |     |     |
| ----------- | ------------- | ---------- | ----- | --- | --- |
| switch#     | clear events  |            |       |     |     |
| switch#     | show events   |            |       |     |     |
---------------------------------------------------
| show event | logs |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- |
---------------------------------------------------
2018-10-14:07:03:05.637544|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 34 |     |     |
| ----------- | ------------- | ---------- | ----- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| console           | baud-rate |     |     |     |     |
| ----------------- | --------- | --- | --- | --- | --- |
| console baud-rate | <SPEED>   |     |     |     |     |
227
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| no console | baud-rate | <SPEED> |     |     |     |
| ---------- | --------- | ------- | --- | --- | --- |
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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
domain-name
| domain-name    | <NAME>   |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
| no domain-name | [<NAME>] |     |     |     |     |
Description
Specifiesthedomainnameoftheswitch.
Switchsystemandhardwarecommands|228

Thenoformofthiscommandsetsthedomainnametothedefault,whichisnodomainname.
| Parameter |     | Description |
| --------- | --- | ----------- |
<NAME> Specifiesthedomainnametobeassignedtotheswitch.Thefirst
characterofthenamemustbealetteroranumber.Length:1to
32characters.
Examples
Settingandshowingthedomainname:
switch#
show domain-name
| switch#         | config           |             |
| --------------- | ---------------- | ----------- |
| switch(config)# | domain-name      | example.com |
| switch(config)# | show domain-name |             |
example.com
switch(config)#
Settingthedomainnametothedefaultvalue:
| switch(config)# | no domain-name |     |
| --------------- | -------------- | --- |
switch(config)#
|     | show domain-name |     |
| --- | ---------------- | --- |
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
Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
229
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<HOSTNAME> Specifiesthehostname.Thefirstcharacterofthehostname
mustbealetteroranumber.Length:1to32characters.Default:
switch
Examples
Settingandshowingthehostname:
| switch# | show hostname |     |     |
| ------- | ------------- | --- | --- |
switch
| switch#           | config |                   |     |
| ----------------- | ------ | ----------------- | --- |
| switch(config)#   |        | hostname myswitch |     |
| myswitch(config)# |        | show hostname     |     |
myswitch
Settingthehostnametothedefaultvalue:
| myswitch(config)# |     | no hostname |     |
| ----------------- | --- | ----------- | --- |
switch(config)#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
led locator
| led locator    | {on | off | | flashing}       |     |
| -------------- | --------- | ----------------- | --- |
| no led locator | {on       | | off | flashing} |     |
Description
SetsthestateofthelocatorLEDtoon,off(default),orflashing.
| Parameter |     |     | Description    |
| --------- | --- | --- | -------------- |
| on        |     |     | TurnsontheLED. |
off
TurnsofftheLED,whichisthedefaultvalue.
| flashing |     |     | SetstheLEDtoblinkonandoffrepeatedly. |
| -------- | --- | --- | ------------------------------------ |
Example
Switchsystemandhardwarecommands|230

SettingthestateofthelocatorLED:
| switch# | led locator flashing |     |     |     |
| ------- | -------------------- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
6100
show capacities
| show capacities | <FEATURE> |     |     |     |
| --------------- | --------- | --- | --- | --- |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description                       |     |
| --------- | --- | --- | --------------------------------- | --- |
| <FEATURE> |     |     | Specifiesafeature.Forexample,aaa. |     |
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardwareor
softwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
Showingclassifier-relatedcapacitiesonthe6100:
| switch#            | show capacities | classifier |     |       |
| ------------------ | --------------- | ---------- | --- | ----- |
| System Capacities: | Filter          | Classifier |     |       |
| Capacities         | Name            |            |     | Value |
------------------------------------------------------------------------------------
Maximum number of Access Control Entries configurable in a system 4096
Maximum number of Access Control Lists configurable in a system 512
Maximum number of class entries configurable in a system 4096
| Maximum | number of classes | configurable | in a system         | 512  |
| ------- | ----------------- | ------------ | ------------------- | ---- |
| Maximum | number of entries | in an        | Access Control List | 1024 |
| Maximum | number of entries | in a         | class               | 1024 |
| Maximum | number of entries | in a         | policy              | 64   |
Maximum number of classifier policies configurable in a system 512
Maximum number of policy entries configurable in a system 4096
231
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

Showingallavailablecapacitiesonthe6100:
| switch# show | capacities |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- |
System Capacities:
| Capacities Name |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
Value
------------------------------------------------------------------------------------
------
Maximum number of Access Control Entries configurable in a system
4096
| Maximum number | of Access | Control |     | Lists | configurable |     | in a system |
| -------------- | --------- | ------- | --- | ----- | ------------ | --- | ----------- |
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
Switchsystemandhardwarecommands|232

Maximum number of Device Profiles allowed to be created on the system
8
Maximum number of Port Access Roles allowed to be created on the system
32
| Maximum | number of | MAC | Address | that | can | be authorized |     | on a port |     |     |
| ------- | --------- | --- | ------- | ---- | --- | ------------- | --- | --------- | --- | --- |
32
Maximum number of Port Access Role VLAN IDs allowed to be created on the system
50
Maximum number of Port Access Role VLAN names allowed to be created on the system
50
| Maximum | number of | RBAC | rules | per | user | group |     |     |     |     |
| ------- | --------- | ---- | ----- | --- | ---- | ----- | --- | --- | --- | --- |
1024
| Maximum | number of | RPVST | VLANs | configurable |     |     | on the | system |     |     |
| ------- | --------- | ----- | ----- | ------------ | --- | --- | ------ | ------ | --- | --- |
16
| Maximum | number of | RPVST | VPORTs |     | supported | in  | a system |     |     |     |
| ------- | --------- | ----- | ------ | --- | --------- | --- | -------- | --- | --- | --- |
512
| Maximum | number of | SVIs | supported |     | in the | system |     |     |     |     |
| ------- | --------- | ---- | --------- | --- | ------ | ------ | --- | --- | --- | --- |
16
| Maximum | number of | routes | (IPv4+IPv6) |     | on  | the | system |     |     |     |
| ------- | --------- | ------ | ----------- | --- | --- | --- | ------ | --- | --- | --- |
512
| Maximum | number of | IPv4 | routes | on  | the system |     |     |     |     |     |
| ------- | --------- | ---- | ------ | --- | ---------- | --- | --- | --- | --- | --- |
512
| Maximum | number of | IPv6 | routes | on  | the system |     |     |     |     |     |
| ------- | --------- | ---- | ------ | --- | ---------- | --- | --- | --- | --- | --- |
512
| Maximum | number of | VLANs | supported |     | in the | system |     |     |     |     |
| ------- | --------- | ----- | --------- | --- | ------ | ------ | --- | --- | --- | --- |
512
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities |        | mirroring |           |     |     |     |     |       |     |
| ------------------ | --------------- | ------ | --------- | --------- | --- | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |           | Mirroring |     |     |     |     |       |     |
| Capacities         | Name            |        |           |           |     |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of | Mirror  | Sessions |        | configurable |     | in       | a system |     | 4   |
| ------- | --------- | ------- | -------- | ------ | ------------ | --- | -------- | -------- | --- | --- |
| Maximum | number of | enabled |          | Mirror | Sessions     | in  | a system |          |     | 4   |
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities |        | mstp |      |     |     |     |     |       |     |
| ------------------ | --------------- | ------ | ---- | ---- | --- | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |      | MSTP |     |     |     |     |       |     |
| Capacities         | Name            |        |      |      |     |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of | mstp | instances |     | configurable |     | in a | system |     | 64  |
| ------- | --------- | ---- | --------- | --- | ------------ | --- | ---- | ------ | --- | --- |
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities |        | vlan-count |      |       |     |     |     |       |     |
| ------------------ | --------------- | ------ | ---------- | ---- | ----- | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |            | VLAN | Count |     |     |     |       |     |
| Capacities         | Name            |        |            |      |       |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of | VLANs | supported |     | in the | system |     |     |     | 4094 |
| ------- | --------- | ----- | --------- | --- | ------ | ------ | --- | --- | --- | ---- |
233
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show capacities-status
| show | capacities-status |     | <FEATURE> |     |     |     |     |     |
| ---- | ----------------- | --- | --------- | --- | --- | --- | --- | --- |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     |     |     | Description                                        |     |     |     |
| --------- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
| <FEATURE> |     |     |     |     | Specifiesthefeature,forexampleaaaforwhichtodisplay |     |     |     |
capacities,values,andstatus.Required.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
switch#
|     |            | show capacities-status |        |     |     |     |     |       |
| --- | ---------- | ---------------------- | ------ | --- | --- | --- | --- | ----- |
|     | System     | Capacities             | Status |     |     |     |     |       |
|     | Capacities | Status                 | Name   |     |     |     |     | Value |
Maximum
------------------------------------------------------------------------------------
--
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
|     | Tunnels | currently             | configured |           |            |            |     | 0 1024 |
| --- | ------- | --------------------- | ---------- | --------- | ---------- | ---------- | --- | ------ |
|     | Number  | of Mirror Sessions    |            | currently |            | configured |     | 0 4    |
|     | Number  | of Mirror Sessions    |            | currently |            | enabled    |     | 0 4    |
|     | Number  | of mstp instances     |            | currently | configured |            |     | 0 16   |
|     | Number  | of RPVST VLANs        | currently  |           | configured |            |     | 0 16   |
|     | Number  | of routes (IPv4+IPv6) |            |           | currently  | configured |     | 1 512  |
|     | Number  | of IPv4 routes        | currently  |           | configured |            |     | 1 512  |
Switchsystemandhardwarecommands|234

| Number | of IPv6 routes     | currently  | configured | 0 512 |
| ------ | ------------------ | ---------- | ---------- | ----- |
| Number | of VLANs currently | configured |            | 1 512 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
| switch#    | show console |     |     |     |
| ---------- | ------------ | --- | --- | --- |
| Baud Rate: | 9600         |     |     |     |
CommandHistory
| Release |     |     | Modification      |     |
| ------- | --- | --- | ----------------- | --- |
| 10.08   |     |     | Commandintroduced |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
show core-dump
| show core-dump | all |     |     |     |
| -------------- | --- | --- | --- | --- |
Description
235
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

Shows core dump information about the specified module. When no parameters are specified, shows only
the core dumps generated in the current boot of the management module. When the all parameter is
specified, shows all available core dumps.

Parameter

Description

all

Usage

Shows all available core dumps.

When no parameters are specified, the show core-dump command shows only the core dumps generated in
the current boot of the management module. You can use this command to determine when any crashes
are occurring in the current boot.

If no core dumps have occurred, the following message is displayed: No core dumps are present

To show core dump information for the standby management module, you must use the standby
command to switch to the standby management module and then execute the show core-dump command.

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

Showing all core dumps:

switch# show core-dump all
=============================================================================
Management Module core-dumps
=============================================================================
Daemon Name
=============================================================================

| Instance ID | Present

| Timestamp

| Build ID

Switch system and hardware commands | 236

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
| Total number | of core dumps | : 5 |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- |
=============================================================================
CommandHistory
| Release        |     | Modification |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show domain-name
show domain-name
Description
Showsthecurrentdomainname.
Usage
Ifthereisnodomainnameconfigured,theCLIdisplaysablankline.
Example
Settingandshowingthedomainname:
| switch#         | show domain-name |             |     |     |     |
| --------------- | ---------------- | ----------- | --- | --- | --- |
| switch#         | config           |             |     |     |     |
| switch(config)# | domain-name      | example.com |     |     |     |
| switch(config)# | show domain-name |             |     |     |     |
example.com
switch(config)#
CommandHistory
237
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

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

show environment fan

show environment fan is not available for JL679A.

show environment fan

Description

Shows the status information for all fans and fan trays (if present) in the system.

Usage

For fan trays, Status is one of the following values:
ready
The fan tray is operating normally.
fault
The fan tray is in a fault event. The status of the fan tray does not indicate the status of fans.
empty
The fan tray is not installed in the system.

For fans:
Speed

Indicates the relative speed of the fan based on the nominal speed range of the fan.
N/A

This value is not applicable to the 6000 or 6100.

Direction
The direction of airflow through the fan. Values are:

left-to-right

Air flows from the left of the system to the right of the system.

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

Switch system and hardware commands | 238

Showingoutputforsystemswithfantraysfor6100switchseries:
| switch# | show environment | fan |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
Fan information
---------------------------------------------------------------------------
| Mbr/Fan | Product | Serial Number | Speed | Direction | Status RPM |
| ------- | ------- | ------------- | ----- | --------- | ---------- |
Name
---------------------------------------------------------------------------
| 1/1 | N/A | N/A | N/A | left-to-right | ok N/A |
| --- | --- | --- | --- | ------------- | ------ |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |     | led |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
| show environment | led |     |     |     |     |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
Example
ShowingstateandstatusforLED:
| switch#  | show environment | led    |     |     |     |
| -------- | ---------------- | ------ | --- | --- | --- |
| Mbr/Name | State            | Status |     |     |     |
-------------------------------
| 1/locator | off | ok  |     |     |     |
| --------- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
239
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show environment power-supply
show environment power-supply

Description

Shows status information about all power supplies in the switch.

Usage

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

Warning

The power supply is not operating normally.

Wattage Maximum
Shows the maximum amount of wattage that the power supply can provide.

Example

Showing the output when only one power supply is installed in the switch:

switch# show environment power-supply

Product Serial
Number

Mbr/PSU Number
--------------------------------------------------------------
1/1

N/A

N/A

500

OK

PSU
Status

Wattage
Maximum

Command History

Switch system and hardware commands | 240

| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show environment |             | temperature |     |     |     |
| ---------------- | ----------- | ----------- | --- | --- | --- |
| show environment | temperature | [detail]    |     |     |     |
Description
Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
detail
Showsdetailedinformationfromeachtemperaturesensor.
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
Showingcurrenttemperatureinformationfora6100switch:
| switch#     | show environment | temperature |     |     |     |
| ----------- | ---------------- | ----------- | --- | --- | --- |
| Temperature | information      |             |     |     |     |
------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     |     | Module Type | temperature | Status |
| --------------- | --- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-COMe-Daughter-Boar |     |     | line-card-module | 66.45 C | normal |
| ---------------------- | --- | --- | ---------------- | ------- | ------ |
| 1/1-PCIE-Switch        |     |     | line-card-module | 95.82 C | normal |
241
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| 1/1-Processor            |     |     | line-card-module |     | 00.00 C  | fault     |
| ------------------------ | --- | --- | ---------------- | --- | -------- | --------- |
| 1/1-Switch-ASIC          |     |     | line-card-module |     | 116.36 C | emergency |
| 1/1-Switch-ASIC-Internal |     |     | line-card-module |     | 108.25 C | critical  |
| 1/2-COMe-Daughter-Boar   |     |     | line-card-module |     | 67.29 C  | normal    |
| 1/2-PCIE-Switch          |     |     | line-card-module |     | 95.82 C  | normal    |
| 1/2-Processor-1          |     |     | line-card-module |     | 72.92 C  | normal    |
| 1/2-Processor-2          |     |     | line-card-module |     | 73.05 C  | normal    |
| 1/2-Switch-ASIC          |     |     | line-card-module |     | 97.41 C  | normal    |
| 1/2-Switch-ASIC-Internal |     |     | line-card-module |     | 97.62 C  | normal    |
...
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show        | events              |              |            |                 |         |     |
| ----------- | ------------------- | ------------ | ---------- | --------------- | ------- | --- |
| show events | [ -e <EVENT-ID>     | |            |            |                 |         |     |
| -s {alert   | | crit |            | debug | emer | | err      | | info | notice | | warn} | |   |
| -r |        | -a | -i <MEMBER-ID> | |            | -n <count> | |               |         |     |
| -c {lldp    | | ospf |            | ... | } |    |            |                 |         |     |
| -d {lldpd   | | hpe-fand          | | ... |}]    |            |                 |         |     |
Description
Showseventlogsgeneratedbytheswitchmodulessincethelastreboot.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
-e <EVENT-ID> ShowstheeventlogsforthespecifiedeventID.EventIDrange:
101through99999.
-s {alert | crit | debug | emer | Showstheeventlogsforthespecifiedseverity.Selecttheseverity
| err | | info | notice | | warn} |     | fromthefollowinglist: |     |     |
| ----- | ------------- | ------- | --- | --------------------- | --- | --- |
n alert:Displayseventlogswithseverityalertandabove.
crit:Displayseventlogswithseveritycriticalandabove.
n
n debug:Displayseventlogswithallseverities.
emer:Displayseventlogswithseverityemergencyonly.
n
n err:Displayseventlogswithseverityerrorandabove.
n info:Displayseventlogswithseverityinfoandabove.
notice:Displayseventlogswithseveritynoticeandabove.
n
n warn:Displayseventlogswithseveritywarningandabove.
Switchsystemandhardwarecommands|242

Parameter

Description

-r

-a

Shows the most recent event logs first.

Shows all event logs, including those events from previous boots.

-n <count>

Displays the specified number of event logs.

-c {lldp | ospf | ... | }

Shows the event logs for the specified event category. Enter show
event -c for a full listing of supported categories with
descriptions.

-d {lldpd | hpe-fand | ... |}

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
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
bridge_normal interface
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware

Showing the most recent event logs first:

switch# show events -r
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
bridge_normal interface
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c

Showing all event logs:

switch# show events -a
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
bridge_normal interface
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware

Showing event logs related to IRDP:

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

243

| switch# | switch# show | events -c irdp |
| ------- | ------------ | -------------- |
2016-05-31:06:26:27.363923|hpe-rdiscd|111001|LOG_INFO|IRDP enabled on interface %s
2016-05-31:07:08:51.351755|hpe-rdiscd|111002|LOG_INFO|IRDP disabled on interface %s
ShowingeventlogsrelatedtoLACP:
| switch# | show events | -c lacp |
| ------- | ----------- | ------- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
ShowingeventlogsasperthespecifiedslotID:
| switch# | show events | -i 1 |
| ------- | ----------- | ---- |
---------------------------------------------------
| Event logs | from current | boot |
| ---------- | ------------ | ---- |
---------------------------------------------------
2020-04-22T05:36:14.430166+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_
INFO|MSTR|1|Created a vrf entity b1721d27-41c2-485d-9bae-2cfcbc9bd13d
2020-04-22T05:36:14.942597+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_
INFO|MSTR|1|Created a vrf entity 5eb532c9-5b4d-4d83-b34a-db24ae542d4e
2020-04-22T05:36:15.886252+00:00 6300 vsfd[710]: Event|9903|LOG_INFO|MSTR|1|Master 1
boot complete
Showingeventlogsasperthespecifiedprocess:
| switch# | show events | -d lacpd |
| ------- | ----------- | -------- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Displayingthespecifiednumberofeventlogs:
| switch# | show events | -n 5 |
| ------- | ----------- | ---- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
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
Release Modification
10.07orearlier --
Switchsystemandhardwarecommands|244

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
show hostname
show hostname
Description
Showsthecurrenthostname.
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
show images
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
Example
245
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Showingtheprimaryandsecondaryimagesona6100switch:
| switch(config)# | show | images |     |
| --------------- | ---- | ------ | --- |
---------------------------------------------------------------------------
| ArubaOS-CX | Primary | Image |     |
| ---------- | ------- | ----- | --- |
---------------------------------------------------------------------------
| Version | : PL.10.06.0002E |              |     |
| ------- | ---------------- | ------------ | --- |
| Size    | : 243 MB         |              |     |
| Date    | : 2020-11-25     | 22:00:47 PST |     |
SHA-256 : 61fe9233b2c842e8ac1731ad46949bd63e269c5c72d69290932ef19c1ebb0730
---------------------------------------------------------------------------
| ArubaOS-CX | Secondary | Image |     |
| ---------- | --------- | ----- | --- |
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
| Active       | Image      | : primary                |     |
| ------------ | ---------- | ------------------------ | --- |
| Service      | OS Version | : PL.01.07.0003-internal |     |
| BIOS Version |            | : PL.01.0001             |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show module
show module
Description
Showsinformationaboutinstalledlinemodulesandmanagementmodules.
Althoughthisswitchdoesnothaveremovablemodules,thiscommandwillstillreturninformationaboutthe
switch,referringtomanagementmodulesandlinemodules.
Usage
Switchsystemandhardwarecommands|246

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

Showing all installed modules:

switch# show module

Management Modules
==================

Product

Name Number Description
---- ------- -------------------------------------- ---------- ----------------
1/1 JL678A 6100F 24G 4SFP+ Swch

SG0ZKW600P Active (local)

Status

Line Modules
============

Product

Name Number Description
---- ------- -------------------------------------- ---------- ----------------
1/1 JL678A 6100F 24G 4SFP+ Swch

SG0ZKW600P Ready

Status

Serial
Number

Serial
Number

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

247

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show running-config |             |       |     |
| ------------------- | ----------- | ----- | --- |
| show running-config | [<FEATURE>] | [all] |     |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).
| all |     |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |
| --- | --- | --- | ------------------------------------------------------- |
Examples
Showingthecurrentrunningconfiguration:
| switch> | show running-config |     |     |
| ------- | ------------------- | --- | --- |
| Current | configuration:      |     |     |
!
| !Version          | ArubaOS-CX PL.10.06.0001-346-g56a12a8f4cf15 |     |     |
| ----------------- | ------------------------------------------- | --- | --- |
| !export-password: | default                                     |     |     |
| ntp enable        |                                             |     |     |
!
!
!
!
| ssh server | vrf default |     |     |
| ---------- | ----------- | --- | --- |
| vlan 1     |             |     |     |
spanning-tree
| spanning-tree | instance | 1 vlan 1,2,4-10 |     |
| ------------- | -------- | --------------- | --- |
| interface     | 1/1/1    |                 |     |
no shutdown
vlan access 1
portfilter 1/1/2-1/1/3
| interface | 1/1/2 |     |     |
| --------- | ----- | --- | --- |
no shutdown
vlan access 1
| interface | 1/1/3 |     |     |
| --------- | ----- | --- | --- |
no shutdown
vlan access 1
| interface | 1/1/4 |     |     |
| --------- | ----- | --- | --- |
no shutdown
vlan access 1
| interface | 1/1/5 |     |     |
| --------- | ----- | --- | --- |
no shutdown
vlan access 1
| interface | 1/1/6 |     |     |
| --------- | ----- | --- | --- |
Switchsystemandhardwarecommands|248

no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/7    |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/8    |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/9    |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/10   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/11   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/12   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/13   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/14   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/15   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/16   |     |     |
no shutdown
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | vlan 1   |     |     |
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
249
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

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
!Version ArubaOS-CX PL.10.06.0001-346-g56a12a8f4cf15
!export-password: default
!
!
!
!
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

Switch system and hardware commands | 250

| vlan        | access 1 |     |
| ----------- | -------- | --- |
| interface   | 1/1/12   |     |
| no shutdown |          |     |
| vlan        | access 1 |     |
| interface   | 1/1/13   |     |
| no shutdown |          |     |
| vlan        | access 1 |     |
| interface   | 1/1/14   |     |
| no shutdown |          |     |
| vlan        | access 1 |     |
| interface   | 1/1/15   |     |
| no shutdown |          |     |
| vlan        | access 1 |     |
| interface   | 1/1/16   |     |
| no shutdown |          |     |
| vlan        | access 1 |     |
| interface   | vlan 1   |     |
| ip dhcp     |          |     |
!
!
!
!
!
| https-server | vrf default |     |
| ------------ | ----------- | --- |
switch#
switch#
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show running-config | current-context |     |
| ------------------- | --------------- | --- |
| show running-config | current-context |     |
Description
Showsthecurrentnon-defaultconfigurationrunningontheswitchinthecurrentcommandcontext.
Usage
Youcanenterthiscommandfromthefollowingconfigurationcontexts:
Anychildoftheglobalconfiguration(config)context.Ifthechildcontexthasinstances—suchas
n
interfaces—youcanenterthecommandinthecontextofaspecificinstance.Supportforthiscommand
isprovidedforonelevelbelowtheconfigcontext.Forexample,enteringthiscommandforachildofa
childoftheconfigcontextnotsupported.Ifyouenterthecommandonachildoftheconfigcontext,
thecurrentconfigurationofthatcontextandthechildrenofthatcontextaredisplayed.
251
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Theglobalconfiguration(config)context.Ifyouenterthiscommandintheglobalconfiguration(config)
n
context,itshowstherunningconfigurationoftheentireswitch.Usetheshow running-configuration
commandinstead.
Examples
Showingtherunningconfigurationforthecurrentinterface:
| switch(config-if)# | show | running-config | current-context |     |
| ------------------ | ---- | -------------- | --------------- | --- |
| interface 1/1/1    |      |                |                 |     |
no shutdown
| description   | Example | interface |     |     |
| ------------- | ------- | --------- | --- | --- |
| vlan access 1 |         |           |     |     |
exit
Showingthecurrentrunningconfigurationforthein-bandmanagementinterface:
| switch(config)#                    | interface | vlan 1   |            |           |
| ---------------------------------- | --------- | -------- | ---------- | --------- |
| switch(config-if-vlan)#description |           | IN-BAND  | Management | Interface |
| switch(config-if-vlan)#ip          |           | dhcp     |            |           |
| switch(config-if-vlan)#no          |           | shutdown |            |           |
switch(config-if-vlan)#end
switch#
Showingthecurrentrunningconfigurationforthein-bandmanagementinterfacewithoutDHCP:
| switch(config)#                    | interface | vlan 1                  |            |           |
| ---------------------------------- | --------- | ----------------------- | ---------- | --------- |
| switch(config-if-vlan)#description |           | IN-BAND                 | Management | Interface |
| switch(config-if-vlan)#no          |           | ip dhcp                 |            |           |
| switch(config-if-vlan)#ip          |           | address 192.168.10.1/24 |            |           |
| switch(config-if-vlan)#no          |           | shutdown                |            |           |
switch(config-if-vlan)#end
switch#
Showingtherunningconfigurationfortheexternalstoragesharenamednasfiles:
switch(config-external-storage-nasfiles)# show running-config current-context
| external-storage    | nasfiles |     |     |     |
| ------------------- | -------- | --- | --- | --- |
| address 192.168.0.1 |          |     |     |     |
vrf default
| username nasuser |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
password ciphertext AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
type scp
| directory | /home/nas |     |     |     |
| --------- | --------- | --- | --- | --- |
enable
switch(config-external-storage-nasfiles)#
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
Switchsystemandhardwarecommands|252

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
show system
show system
253
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Description
Showsgeneralstatusinformationaboutthesystem.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemContact,SystemLocation,andSystemDescriptioncanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformation:
| switch(config)# |             | show system      |                |      |
| --------------- | ----------- | ---------------- | -------------- | ---- |
| Hostname        |             | : switch         |                |      |
| System          | Description | : PL.10.xx.xxxxx |                |      |
| System          | Contact     | :                |                |      |
| System          | Location    | :                |                |      |
| Vendor          |             | : Aruba          |                |      |
| Product         | Name        | : JL678A         | 6100 24G 4SFP+ | Swch |
| Chassis         | Serial Nbr  | : CN9ZKRD058     |                |      |
| Base            | MAC Address | : f860f0-c91160  |                |      |
| ArubaOS-CX      | Version     | : PL.10.xx.xxxxx |                |      |
| Time            | Zone        | : UTC            |                |      |
| Up Time         |             | : 9 hours,       | 10 minutes     |      |
| CPU Util        | (%)         | : 3              |                |      |
| Memory          | Usage (%)   | : 15             |                |      |
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
| show        | system               | resource-utilization |                        |     |
| ----------- | -------------------- | -------------------- | ---------------------- | --- |
| show system | resource-utilization |                      | [daemon <DAEMON-NAME>] |     |
Description
ShowsinformationabouttheusageofsystemresourcessuchasCPU,memory,andopenfiledescriptors.
Switchsystemandhardwarecommands|254

| Parameter |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
daemon <DAEMON-NAME> Showsthefilteredresourceutilizationdatafortheprocess
|     |     |     |     | specifiedby<DAEMON-NAME> |     |     | only. |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | ----- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
NOTE:
|     |     |     |     | Foralistofdaemonsthatlogevents,entershow |     |     |     | events | -d ?from |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ------ | -------- |
aswitchpromptinthemanager(#)context.
Examples
Showingallsystemresourceutilizationdata:
| switch# show | system | resource-utilization |     |     |     |     |     |     |     |
| ------------ | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- |
System Resources:
| Processes:       | 147       |             |     |          |        |     |        |     |     |
| ---------------- | --------- | ----------- | --- | -------- | ------ | --- | ------ | --- | --- |
| CPU usage(%):    | 12        |             |     |          |        |     |        |     |     |
| Memory usage(%): |           | 13          |     |          |        |     |        |     |     |
| Open FD's:       | 4128      |             |     |          |        |     |        |     |     |
| mmc-type-a:      | Endurance | utilization |     | = 0-10%, | Health | =   | normal |     |     |
| mmc-type-b:      | Endurance | utilization |     | = 0-10%, | Health | =   | normal |     |     |
switch#
Showingtheresourceutilizationdataforthepmdprocess:
| switch# show | system | resource-utilization |     |     | daemon       | pmd |           |     |     |
| ------------ | ------ | -------------------- | --- | --- | ------------ | --- | --------- | --- | --- |
| Process      |        | CPU Usage            |     |     | Memory Usage |     | Open FD's |     |     |
-----------------------------------------------------------------------
| pmd |     | 2   |     |     | 1   |     | 14  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# show    | system      | resource-utilization |      |      |              |          |     |     |     |
| --------------- | ----------- | -------------------- | ---- | ---- | ------------ | -------- | --- | --- | --- |
| System resource | utilization |                      | data | poll | is currently | disabled |     |     |     |
Showingresourceutilizationdataforalinemodule:
| switch# show     | system      | resource-utilization |     |           | module  | 1/1 |     |     |     |
| ---------------- | ----------- | -------------------- | --- | --------- | ------- | --- | --- | --- | --- |
| System Resource  | utilization |                      | for | line card | module: | 1/1 |     |     |     |
| CPU usage(%):    | 0           |                      |     |           |         |     |     |     |     |
| Memory usage(%): |             | 35                   |     |           |         |     |     |     |     |
| Open FD's:       | 512         |                      |     |           |         |     |     |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |     |
255
AOS-CX10.08FundamentalsGuide| (4100i,6000,6100SwitchSeries)

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
Switchsystemandhardwarecommands|256

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
show usb
Description
ShowstheUSBportconfigurationandmountsettings.
Examples
IfUSBhasnotbeenenabled:
| switch>  | show usb |     |     |
| -------- | -------- | --- | --- |
| Enabled: | No       |     |     |
| Mounted: | No       |     |     |
IfUSBhasbeenenabled,butnodevicehasbeenmounted:
257
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
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
| switch# | show usb file-system |     |
| ------- | -------------------- | --- |
/mnt/usb:
| 'System | Volume Information' | dir1' |
| ------- | ------------------- | ----- |
Switchsystemandhardwarecommands|258

| /mnt/usb/System   | Volume | Information':  |     |     |
| ----------------- | ------ | -------------- | --- | --- |
| IndexerVolumeGuid |        | WPSettings.dat |     |     |
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
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
show version
show version
Description
259
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
Example
Showingversioninformation:
| switch(config)# |     | show | version |     |     |     |     |
| --------------- | --- | ---- | ------- | --- | --- | --- | --- |
-----------------------------------------------------------------------------
ArubaOS-CX
(c) Copyright 2017-2020 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version |      | : PL.10.xx.xxxxx |     |          |     |     |     |
| ------- | ---- | ---------------- | --- | -------- | --- | --- | --- |
| Build   | Date | : 2020-12-06     |     | 22:13:46 | UTC |     |     |
Build ID : ArubaOS-CX:PL.10.xx.xxxxx:9e8bf51170a6:202012062115
| Build   | SHA        | : 9e8bf51170a602370f12e0bde814e8d8f49bf706 |                           |     |     |     |     |
| ------- | ---------- | ------------------------------------------ | ------------------------- | --- | --- | --- | --- |
| Active  | Image      | : secondary                                |                           |     |     |     |     |
| Service | OS Version |                                            | : PL.10.xx.xxxxx-internal |     |     |     |     |
| BIOS    | Version    |                                            | : PL.01.0002              |     |     |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| system                      | resource-utilization |     |     |               |     | poll-interval |     |
| --------------------------- | -------------------- | --- | --- | ------------- | --- | ------------- | --- |
| system resource-utilization |                      |     |     | poll-interval |     | <SECONDS>     |     |
Description
ConfiguresthepollingintervalforsystemresourceinformationcollectionandrecordingsuchasCPUand
memoryusage.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<SECONDS> Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Example
Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |     | system |     | resource-utilization |     | poll-interval | 20  |
| --------------- | --- | ------ | --- | -------------------- | --- | ------------- | --- |
Switchsystemandhardwarecommands|260

CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
top cpu
top cpu
Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch#        | top cpu   |            |          |              |          |            |             |      |
| -------------- | --------- | ---------- | -------- | ------------ | -------- | ---------- | ----------- | ---- |
| top - 09:42:55 |           | up 3 min,  | 3 users, | load         | average: |            | 3.44, 3.78, | 1.70 |
| Tasks:         | 76 total, | 2 running, |          | 74 sleeping, |          | 0 stopped, | 0 zombie    |      |
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
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
top memory
top memory
Description
261
| AOS-CX10.08FundamentalsGuide| |     | (4100i,6000,6100SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |

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
| switch(config)# |     | usb |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
DisablingUSBportswhenaUSBdriveismounted:
| switch(config)# |     | no usb |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
CommandHistory
Switchsystemandhardwarecommands|262

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
| switch# | usb mount |     |
| ------- | --------- | --- |
UnmountingaUSBdrive:
| switch# | usb unmount |     |
| ------- | ----------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
263
| AOS-CX10.08FundamentalsGuide| | (4100i,6000,6100SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

Switch system and hardware commands | 264

Support and Other Resources

Chapter 16

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

AOS-CX 10.08 Fundamentals Guide | (4100i, 6000, 6100 Switch Series)

265

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

Support and Other Resources | 266