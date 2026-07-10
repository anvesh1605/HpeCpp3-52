AOS-CX 10.11 Fundamentals
Guide

8320, 8325, 8360, 9300, 10000 Switch Series

Published: February 2023
Edition: 2

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General
Public License, and/or certain other open source licenses. A complete machine-readable copy of the
source code corresponding to such code is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, send a check or
money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

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

Bluetooth is a trademark owned by its proprietor and used by Hewlett Packard Enterprise under
license.

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
| InitialconfigurationusingtheArubaCXmobileapp |                                                | 18  |
|                                              | TroubleshootingBluetoothconnections            | 20  |
|                                              | BluetoothconnectionIPaddresses                 | 20  |
|                                              | Bluetoothisconnectedbuttheswitchisnotreachable | 20  |
|                                              | Bluetoothisnotconnected                        | 21  |
| InitialconfigurationusingtheCLI              |                                                | 24  |
|                                              | Connectingtotheconsoleport                     | 24  |
|                                              | Connectingtothemanagementport                  | 25  |
|                                              | Loggingintotheswitchforthefirsttime            | 26  |
|                                              | SettingswitchtimeusingtheNTPclient             | 26  |
| Configuringbanners                           |                                                | 27  |
| Configuringin-bandmanagementonadataport      |                                                | 27  |
| UsingtheWebUI                                |                                                | 28  |
| Configuringthemanagementinterface            |                                                | 28  |
| IPprefixpriority                             |                                                | 29  |
|                                              | SystemprofilesandconfigurableIPprefixpriority  | 29  |
|                                              | IPprefixprioritydefaults                       | 30  |
| IPPrefixprioritycommands                     |                                                | 30  |
|                                              | ipprefix-priority                              | 30  |
|                                              | ipv6prefix-priority                            | 31  |
|                                              | showipprefix-priority                          | 32  |
|                                              | showipv6prefix-priority                        | 33  |
| Selectingthesystemprofile                    |                                                | 34  |
| Systemprofilecommands                        |                                                | 35  |
|                                              | profile                                        | 35  |
3
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

|                                            | showprofilesavailable                      | 36  |
| ------------------------------------------ | ------------------------------------------ | --- |
|                                            | showprofilecurrent                         | 38  |
| Restoringtheswitchtofactorydefaultsettings |                                            | 39  |
| Managementinterfacecommands                |                                            | 41  |
|                                            | default-gateway                            | 41  |
|                                            | ipstatic                                   | 42  |
|                                            | nameserver                                 | 43  |
|                                            | psm                                        | 44  |
|                                            | showinterfacemgmt                          | 45  |
|                                            | showpsm                                    | 46  |
| NTPcommands                                |                                            | 47  |
|                                            | ntpauthentication                          | 47  |
|                                            | ntpauthentication-key                      | 47  |
|                                            | ntpdisable                                 | 49  |
|                                            | ntpenable                                  | 49  |
|                                            | ntpconductor                               | 50  |
|                                            | ntpserver                                  | 51  |
|                                            | ntptrusted-key                             | 53  |
|                                            | ntpvrf                                     | 54  |
|                                            | showntpassociations                        | 54  |
|                                            | showntpauthentication-keys                 | 56  |
|                                            | showntpservers                             | 56  |
|                                            | showntpstatistics                          | 57  |
|                                            | showntpstatus                              | 58  |
| Telnet                                     | access                                     | 60  |
| Telnetcommands                             |                                            | 60  |
|                                            | showtelnetserver                           | 60  |
|                                            | showtelnetserversessions                   | 61  |
|                                            | telnetserver                               | 62  |
| Interface                                  | configuration                              | 63  |
| Configuringalayer2interface                |                                            | 63  |
| Configuringalayer3interface                |                                            | 63  |
| SinglesourceIPaddress                      |                                            | 64  |
| Priority-basedflowcontrol(PFC)             |                                            | 64  |
|                                            | (Appliestothe8325,9300,10000)              | 64  |
|                                            | (Appliestothe8325,9300,10000)AsymmetricPFC | 65  |
|                                            | (Appliestothe8360)                         | 65  |
| Configurableflowcontrolbufferthresholds    |                                            | 65  |
|                                            | Forthe8325,9300,and10000seriesswitch:      | 65  |
| Flowcontrolandlosslessbuffering            |                                            | 68  |
|                                            | Forthe8325,9300,and10000seriesswitch:      | 68  |
|                                            | Requirementsforproperlosslessbuffering:    | 68  |
|                                            | Forthe8360seriesswitch:                    | 68  |
|                                            | Requirementsforproperlosslessbuffering     | 69  |
| Forwarderrorcorrection                     |                                            | 70  |
| Unsupportedtransceiversupport              |                                            | 70  |
| Configuringaninterfacepersona              |                                            | 70  |
|                                            | Modes                                      | 72  |
|                                            | Predefinedandcustompersonanames            | 72  |
|                                            | Creatingandconfiguringaninterfacepersona   | 72  |
|                                            | Examples                                   | 72  |
| Monitormode                                |                                            | 73  |
| Interfacecommands                          |                                            | 73  |
|                                            | allow-unsupported-transceiver              | 73  |
Contents|4

default interface
description
error-control
flow-control
flow-control buffer headroom
flow-control buffer xoff dynamic
flow-control buffer xoff static
flow-control buffer xon
flow-control watchdog
flow-control watchdog timeout resume
interface
interface loopback
interface vlan
ip address
ip mtu
ip source-interface
ipv6 address
ipv6 source-interface
l3-counters
mtu
persona
routing
show allow-unsupported-transceiver
show interface
show interface dom
show interface flow-control
show interface statistics
show interface transceiver
show interface utilization
show ip interface
show ip source-interface
show ipv6 interface
show ipv6 source-interface
shutdown
speed
system interface-group

Subinterfaces

Configuring subinterfaces
Subinterface in a router-on-a-stick deployment
Subinterface commands

encapsulation dot1q
interface
show capacities subinterface
show interface

Source interface selection

Source-interface selection commands

ip source-interface (protocol <ip-addr>)
ip source-interface
ipv6 source-interface
ipv6 source-interface
show ip source-interface
show ipv6 source-interface
show running-config

75
76
77
78
83
84
85
86
88
89
90
90
91
92
93
94
96
97
98
100
101
103
103
104
109
110
115
117
121
122
123
124
126
127
128
131

133
133
134
134
134
135
137
138

140
140
140
142
143
145
146
147
149

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

5

| VLANs                        |                                               |       | 151 |
| ---------------------------- | --------------------------------------------- | ----- | --- |
| Precision                    | time protocol                                 | (PTP) | 152 |
| PTPclocks                    |                                               |       | 152 |
|                              | Bestclock-sourcealgorithm                     |       | 153 |
| PTPnetworkdiagram            |                                               |       | 153 |
|                              | Configurationexamples                         |       | 154 |
| Hardwareconsiderations       |                                               |       | 155 |
| Configurationrecommendations |                                               |       | 156 |
|                              | PTPCoPPclassconfigurationrecommendations      |       | 156 |
|                              | Configurationrecommendationsforaboundaryclock |       | 156 |
QoSprioritizationconfigurationrecommendationsforatransparentclock 156
|                              | GeneralguidelinesforPTPIPv4multicast     |            | 156 |
| ---------------------------- | ---------------------------------------- | ---------- | --- |
| Usecases                     |                                          |            | 157 |
|                              | Usecase: PTP–IPv4overL2spineleaftopology |            | 157 |
|                              | Usecase:PTP–L3spineleaftopology          |            | 158 |
| PTPcommands                  |                                          |            | 159 |
|                              | clearptpstatistics                       |            | 159 |
|                              | clock-domain                             |            | 159 |
|                              | clock-step                               |            | 160 |
|                              | enable                                   |            | 161 |
|                              | ipsource-interface                       |            | 162 |
|                              | mode                                     |            | 163 |
|                              | priority1                                |            | 165 |
|                              | priority2                                |            | 166 |
|                              | ptpannounce-interval                     |            | 166 |
|                              | ptpannounce-timeout                      |            | 167 |
|                              | ptpclock-source-only                     |            | 168 |
|                              | ptpdelay-req-interval                    |            | 169 |
|                              | ptpenable                                |            | 170 |
|                              | ptplag-role                              |            | 171 |
|                              | ptppdelay-req-interval                   |            | 172 |
|                              | ptppeerip                                |            | 173 |
|                              | ptpprofile                               |            | 174 |
|                              | ptpsync-interval                         |            | 175 |
|                              | ptpvlan                                  |            | 176 |
|                              | showptpclock                             |            | 177 |
|                              | showptpforeign-clock-sources             |            | 178 |
|                              | showptpinterface                         |            | 179 |
|                              | showptpparent                            |            | 182 |
|                              | showptpstatistics                        |            | 183 |
|                              | showptptime-property                     |            | 184 |
|                              | showrunning-configptp                    |            | 185 |
|                              | transport-protocol                       |            | 185 |
| Configuration                | and firmware                             | management | 187 |
| Upgradeanddowngradescenarios |                                          |            | 187 |
|                              | Upgrades                                 |            | 187 |
|                              | Downgrades                               |            | 187 |
|                              | Limitations                              |            | 187 |
| Checkpoints                  |                                          |            | 188 |
|                              | Checkpointtypes                          |            | 188 |
|                              | Maximumnumberofcheckpoints               |            | 188 |
|                              | Usergeneratedcheckpoints                 |            | 188 |
|                              | Systemgeneratedcheckpoints               |            | 188 |
|                              | Supportedremotefileformats               |            | 189 |
Contents|6

|                    | Rollback                                        | 189 |
| ------------------ | ----------------------------------------------- | --- |
|                    | Checkpointautomode                              | 189 |
|                    | Testingaswitchconfigurationincheckpointautomode | 189 |
| Checkpointcommands |                                                 | 190 |
|                    | checkpointauto                                  | 190 |
|                    | checkpointautoconfirm                           | 191 |
|                    | checkpointdiff                                  | 191 |
|                    | checkpointpost-configuration                    | 193 |
|                    | checkpointpost-configurationtimeout             | 194 |
|                    | checkpointrename                                | 195 |
|                    | checkpointrollback                              | 195 |
|                    | copycheckpoint<CHECKPOINT-NAME><REMOTE-URL>     | 196 |
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config} 197
|     | copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>    | 198 |
| --- | ----------------------------------------------- | --- |
|     | copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>     | 199 |
|     | copy<REMOTE-URL>{running-config|startup-config} | 200 |
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>} 202
|                            | copy{running-config|startup-config}<REMOTE-URL>  | 202 |
| -------------------------- | ------------------------------------------------ | --- |
|                            | copy{running-config|startup-config}<STORAGE-URL> | 204 |
|                            | copystartup-configrunning-config                 | 205 |
|                            | copy<STORAGE-URL>running-config                  | 205 |
|                            | erase                                            | 207 |
|                            | showcheckpoint<CHECKPOINT-NAME>                  | 208 |
|                            | showcheckpoint<CHECKPOINT-NAME>hash              | 210 |
|                            | showcheckpointpost-configuration                 | 211 |
|                            | showcheckpoint                                   | 212 |
|                            | showcheckpointdate                               | 212 |
|                            | showrunning-confighash                           | 213 |
|                            | showstartup-confighash                           | 214 |
|                            | writememory                                      | 215 |
| Bootcommands               |                                                  | 215 |
|                            | bootset-default                                  | 215 |
|                            | bootsystem                                       | 216 |
|                            | showboot-history                                 | 218 |
| Firmwaremanagementcommands |                                                  | 220 |
|                            | copy{primary|secondary}<REMOTE-URL>              | 220 |
|                            | copy{primary|secondary}<FIRMWARE-FILENAME>       | 221 |
|                            | copyprimarysecondary                             | 222 |
|                            | copy<REMOTE-URL>                                 | 222 |
|                            | copysecondaryprimary                             | 224 |
|                            | copy<STORAGE-URL>                                | 225 |
| Dynamic                    | Segmentation                                     | 227 |
| SNMP                       |                                                  | 228 |
| ConfiguringSNMP            |                                                  | 228 |
| Aruba                      | Central integration                              | 230 |
| ConnectingtoArubaCentral   |                                                  | 230 |
| CustomCAcertificate        |                                                  | 230 |
| SupportmodeinArubaCentral  |                                                  | 231 |
| ArubaCentralcommands       |                                                  | 231 |
|                            | aruba-central                                    | 231 |
|                            | aruba-centralsupport-mode                        | 232 |
|                            | configuration-lockoutcentralmanaged              | 233 |
|                            | disable                                          | 234 |
7
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

enable 234
location-override 235
showaruba-central 236
showrunning-configcurrent-context 237
| Port filtering        |     | 239 |
| --------------------- | --- | --- |
| Portfilteringcommands |     | 239 |
portfilter 239
showportfilter 240
| DNS                     |     | 243 |
| ----------------------- | --- | --- |
| DNSclient               |     | 243 |
| ConfiguringtheDNSclient |     | 243 |
| DNSclientcommands       |     | 244 |
ipdnsdomain-list 244
ipdnsdomain-name 245
ipdnshost 246
ipdnsserveraddress 247
showipdns 248
| Device discovery | and configuration | 251 |
| ---------------- | ----------------- | --- |
| LLDP             |                   | 251 |
LLDPagent 251
LLDPMEDsupport 253
LLDPEEE 254
ConfiguringtheLLDPagent 254
LLDPcommands 255
| clearlldpneighbors          |     | 255 |
| --------------------------- | --- | --- |
| clearlldpstatistics         |     | 255 |
| lldp                        |     | 256 |
| lldpdot3                    |     | 257 |
| lldpdot3mfs                 |     | 257 |
| lldpholdtime-multiplier     |     | 258 |
| lldpmanagement-ipv4-address |     | 259 |
| lldpmanagement-ipv6-address |     | 260 |
| lldpmed                     |     | 261 |
| lldpmed-location            |     | 262 |
| lldpreceive                 |     | 263 |
| lldpreinit                  |     | 263 |
| lldpselect-tlv              |     | 264 |
| lldptimer                   |     | 266 |
| lldptransmit                |     | 267 |
| lldptxdelay                 |     | 268 |
| lldptrapenable              |     | 268 |
| showlldpconfiguration       |     | 271 |
| showlldpconfigurationmgmt   |     | 272 |
| showlldplocal-device        |     | 273 |
| showlldpneighbor-info       |     | 275 |
| showlldpneighbor-infodetail |     | 278 |
| showlldpneighbor-infomgmt   |     | 280 |
| showlldpstatistics          |     | 282 |
| showlldpstatisticsmgmt      |     | 283 |
| showlldptlv                 |     | 284 |
| CiscoDiscoveryProtocol(CDP) |     | 285 |
CDPsupport 285
CDPcommands 286
Contents|8

|                                         | cdp                   |          | 286 |
| --------------------------------------- | --------------------- | -------- | --- |
|                                         | clearcdpcounters      |          | 287 |
|                                         | clearcdpneighbor-info |          | 287 |
|                                         | showcdp               |          | 288 |
|                                         | showcdpneighbor-info  |          | 288 |
|                                         | showcdptraffic        |          | 289 |
| Zero Touch                              | Provisioning          |          | 291 |
| ZTPsupport                              |                       |          | 291 |
| SettingupZTPonatrustednetwork           |                       |          | 292 |
| ZTPprocessduringswitchboot              |                       |          | 293 |
| ZTPVSFswitchoversupport                 |                       |          | 294 |
| ZTPcommands                             |                       |          | 294 |
|                                         | showztpinformation    |          | 294 |
|                                         | ztpforceprovision     |          | 298 |
| Switch system                           | and hardware          | commands | 300 |
| bluetoothdisable                        |                       |          | 300 |
| bluetoothenable                         |                       |          | 300 |
| clearevents                             |                       |          | 301 |
| cleariperrors                           |                       |          | 302 |
| consolebaud-rate                        |                       |          | 303 |
| domain-name                             |                       |          | 304 |
| hostname                                |                       |          | 305 |
| ledlocator                              |                       |          | 305 |
| mtrace                                  |                       |          | 306 |
| showbluetooth                           |                       |          | 308 |
| showboot-history                        |                       |          | 309 |
| showcapacities                          |                       |          | 311 |
| showcapacities-status                   |                       |          | 312 |
| showconsole                             |                       |          | 313 |
| showcore-dump                           |                       |          | 314 |
| showdomain-name                         |                       |          | 315 |
| showenvironmentfan                      |                       |          | 316 |
| showenvironmentled                      |                       |          | 318 |
| showenvironmentpower-supply             |                       |          | 319 |
| showenvironmenttemperature              |                       |          | 320 |
| showevents                              |                       |          | 321 |
| showhostname                            |                       |          | 323 |
| showimages                              |                       |          | 324 |
| showiperrors                            |                       |          | 325 |
| showmodule                              |                       |          | 326 |
| showrunning-config                      |                       |          | 328 |
| showrunning-configcurrent-context       |                       |          | 331 |
| showstartup-config                      |                       |          | 333 |
| showsystem                              |                       |          | 334 |
| showsystemresource-utilization          |                       |          | 335 |
| showtech                                |                       |          | 337 |
| showusb                                 |                       |          | 338 |
| showusbfile-system                      |                       |          | 339 |
| showversion                             |                       |          | 341 |
| systemresource-utilizationpoll-interval |                       |          | 342 |
| topcpu                                  |                       |          | 342 |
| topmemory                               |                       |          | 343 |
| usb                                     |                       |          | 344 |
| usbmount|unmount                        |                       |          | 344 |
9
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Support               | and Other          | Resources | 346 |
| --------------------- | ------------------ | --------- | --- |
| AccessingArubaSupport |                    |           | 346 |
| AccessingUpdates      |                    |           | 347 |
|                       | ArubaSupportPortal |           | 347 |
|                       | MyNetworking       |           | 347 |
| WarrantyInformation   |                    |           | 347 |
| RegulatoryInformation |                    |           | 347 |
| DocumentationFeedback |                    |           | 348 |
Contents|10

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba8320SwitchSeries(JL479A,JL579A,JL581A)
Aruba8325SwitchSeries(JL624A,JL625A,JL626A,JL627A)
n
n Aruba8360SwitchSeries(JL700A,JL701A,JL702A,JL703A,JL706A,JL707A,JL708A,JL709A,JL710A,
JL711A,JL700C,JL701C,JL702C,JL703C,JL706C,JL707C,JL708C,JL709C,JL710C,JL711C,JL704C,JL705C,
JL719C,JL718C,JL717C,JL720C,JL722C,JL721C)
n Aruba9300SwitchSeries(R9A29A,R9A30A,R8Z96A)
n Aruba10000SwitchSeries(R8P13A,R8P14A)
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Items
thatappearliketheexampletextinthepreviouscolumnaretobeentered
exactlyasshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
n <example-text> substitutewithanactualvalueinacommandorincode:
<example-text>
n
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ------------------------------------------------------------ | --- |
n example-text
areenclosedinanglebrackets(< >).Substitutethetext—including
n example-text
theenclosinganglebrackets—withanactualvalue.
|     |     | n Foroutputformatswhereitalictextcanbedisplayed,variables |     |
| --- | --- | --------------------------------------------------------- | --- |
mightormightnotbeenclosedinanglebrackets.Substitutethe
textincludingtheenclosinganglebrackets,ifany,withanactual
value.
11
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

Convention

Usage

|

{ }

[ ]

… or

...

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

Braces. Indicates that at least one of the enclosed items is required.

Brackets. Indicates that the enclosed item or items are optional.

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

About this document | 12

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 83xx, 9300, and 10000 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

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

Aruba Network Analytics Engine introduction

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

14

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

n Customized validation tests for corporate compliance and network design

n Automated large-scale configuration deployment without programming

About AOS-CX | 15

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

In-band and out-of-band management
Management communications with a managed switch can be either of the following:

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

16

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

18

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

Initial Configuration | 19

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

20

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

If you are in range of multiple Bluetooth devices, more than one device is displayed on the list of
available devices. Switches running the AOS-CX operating system are displayed in the following format:
Switch_model-Serial_number

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify that it
be used for Internet access.

Initial Configuration | 21

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

n An inserted USB drive must be mounted each time the switch boots or fails over to a different

management module. To mount the drive, enter the CLI command: usb mount

n To enable Bluetooth, enter the CLI command: bluetooth enable

Solution 5

Cause

Another mobile device has already connected to the switch through Bluetooth. This cause is likely if
your device is repeatedly disconnected within 1-2 seconds of establishing a connection.

Action

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

22

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

24

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
InitialConfiguration |25

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
26
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

2. ConfigureanNTPserverwiththecommandntp server.Whenconfiguringatimebackward
morethanfiveminutesontheAruba8320,8325,or9300SwitchSeries,arebootis
recommendedtoavoidunusualswitchbehavior.
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
| switch(config)# |     |     | ntp authentication-key |     |     | 1   | md5 myPassword |     |     |     |
| --------------- | --- | --- | ---------------------- | --- | --- | --- | -------------- | --- | --- | --- |
switch(config)#
|                 |     |         | ntp server | my-ntp.mydomain.com |     |     |     | key 10 | prefer |     |
| --------------- | --- | ------- | ---------- | ------------------- | --- | --- | --- | ------ | ------ | --- |
| switch(config)# |     |         | ntp vrf    | mgmt                |     |     |     |        |        |     |
| Configuring     |     | banners |            |                     |     |     |     |        |        |     |
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
InitialConfiguration |27

Prerequisites
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
|     | https-server | vrf | mgmt. |     |     |
| --- | ------------ | --- | ----- | --- | --- |
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
28
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

1. Switchtothemanagementinterfacecontextwiththecommandinterface mgmt.
2. Bydefault,themanagementinterfaceonthemanagementportisenabled.Ifitwasdisabled,re-
| enableitwiththecommandno |     |     | shutdown. |     |     |
| ------------------------ | --- | --- | --------- | --- | --- |
3. Usethecommandip dhcptoconfigurethemanagementinterfacetoautomaticallyobtainan
addressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastaticIPv4or
IPv6address,defaultgateway,andDNSserverwiththecommandsip address,ipv6 address,ip
static,default-gateway,andnameserver.
4. SSHisenabledbydefaultonthemanagementVRF.Ifdisabled,enableSSHwiththecommand
| ssh | server | vrf mgmt. |     |     |     |
| --- | ------ | --------- | --- | --- | --- |
Examples
ThisexampleenablesthemanagementinterfacewithdynamicaddressingusingDHCP:
| switch(config)#         |     | interface | mgmt        |     |     |
| ----------------------- | --- | --------- | ----------- | --- | --- |
| switch(config-if-mgmt)# |     |           | no shutdown |     |     |
| switch(config-if-mgmt)# |     |           | ip dhcp     |     |     |
Thisexampleenablesthemanagementinterfacewithstaticaddressingcreatingthefollowing
configuration:
n SetsastaticIPv4addressof198.168.100.10withamaskof24bits.
n Setsthedefaultgatewayto198.168.100.200.
n SetstheDNSserverto198.168.100.201.
| switch(config)#         |     | interface | mgmt        |     |     |
| ----------------------- | --- | --------- | ----------- | --- | --- |
| switch(config-if-mgmt)# |     |           | no shutdown |     |     |
switch(config-if-mgmt)#
|                         |          |     | ip static 198.168.100.10/24 |                 |     |
| ----------------------- | -------- | --- | --------------------------- | --------------- | --- |
| switch(config-if-mgmt)# |          |     | default-gateway             | 198.168.100.200 |     |
| switch(config-if-mgmt)# |          |     | nameserver 198.168.100.201  |                 |     |
| IP prefix               | priority |     |                             |                 |     |
IPprefixpriorityappliestothe8360SwitchSeries.
IPprefixpriorityconfigurationisusedtooptimizeroutelookupbasedontheIPaddressprefixlength,
sometimesknownastheIPsubnetmasklength.SwitchmodelssupportingIPprefixpriority
configurationhavesixlookuptableswiththefirstfivebeingconfigurableforspecificprefixlengthsand
thelastonebeingusedforallotherprefixlengths.
ThedefaultconfigurationofthefiveexactIPprefixtablesusecommonlengthstypicaltomany
networks.ForsitesthatmakeextensiveuseofatypicalIPprefixlengths(lengthsthatdifferfromthe
defaults),theexactprefixtablescanbecustomizedbyconfiguringIPprefixpriority.Doingsoavoids
overfillingthe“other”tableandkeepsasmanyroutesaspossibleinthefast-path.
Commandsshow ip prefix-priorityandshow ipv6 prefix-priorityshowthedefault,current,and
anypendingIPprefixpriorityconfigurationforaswitch.
SeealsoIPPrefixprioritycommands.
| System | profiles | and | configurable | IP prefix | priority |
| ------ | -------- | --- | ------------ | --------- | -------- |
InitialConfiguration |29

System profiles set the overall capabilities and capacities of the switch (including IP prefix partitions),
based on the selected profile used at boot time. Only certain profiles support configurable IP prefix
priority.

To use configurable IP prefix priority, the switch must be booted into a capable profile. If a switch is
booted into a profile that does not support configurable IP prefix priority, a warning is displayed before
the reboot, and upon reboot, the default IP prefix tables are used and any configured IP prefix priority is
discarded.

See also Selecting the system profile.

IP prefix priority defaults

This default IP prefix priority information only applies to system profiles specifically named here. Any profile

unnamed here does not support configurable IP prefix priority.

8360 Switch Series, profile: Core-Spine (five prefix values required):

n IPv4: 24, 23, 22, 21, 20

n IPv6: 64, 48, 44, 36, 32

IP Prefix priority commands

ip prefix-priority
ip prefix-priority <PREFIX-LENGTHS>
no ip prefix-priority [<PREFIX-LENGTHS>>]

Description

Configures custom IPv4 route prefix lengths for the exact prefix match tables of the switch. The switch
must be rebooted to apply the change.

Following the reboot, IPv4 prefix priorities will remain in a pending state until at least one route is learned. A

connected route counts so this can be as simple as having an L3 interface with an IP address in the up state.

The no form of this command resets the prefix lengths to their default

Parameter

Description

<PREFIX-LENGTHS>>

Specifies a space-separated list of exactly five prefix lengths, in
descending order. Range: 8 to 31.

Examples

Configuring custom IPv4 route prefix lengths:

switch(config)# ip prefix-priority 29 28 27 24 16
Save this config and reboot the switch for the changes to take effect
...

Resetting IPv4 route prefix lengths to their default:

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

30

| switch(config)# | no  | ip prefix-priority |     |     |
| --------------- | --- | ------------------ | --- | --- |
Save this config and reboot the switch for the changes to take effect
...
AttemptingtoconfigurecustomIPv4routeprefixlengthswithsomelengthsnotindescendingorder:
| switch(config)# | ip   | prefix-priority | 28 29 27      | 23 16 |
| --------------- | ---- | --------------- | ------------- | ----- |
| Prefix lengths  | must | be specified    | in descending | order |
Attemptingtoconfigureeightprefixlengths:
| switch(config)# | ip        | prefix-priority | 29 28 27 | 24 23 16 12 8 |
| --------------- | --------- | --------------- | -------- | ------------- |
| Invalid         | input: 16 |                 |          |               |
Attemptingtoconfigurethreeprefixlengths:
| switch(config)#     | ip          | prefix-priority | 29 28 27           |     |
| ------------------- | ----------- | --------------- | ------------------ | --- |
| % Command           | incomplete. |                 |                    |     |
| Command History     |             |                 |                    |     |
| Release             |             |                 | Modification       |     |
| 10.10               |             |                 | Commandintroduced. |     |
| Command Information |             |                 |                    |     |
| Platforms           | Command     | context         | Authority          |     |
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 prefix-priority
| ipv6 prefix-priority    | <PREFIX-LENGTHS> |                     |     |     |
| ----------------------- | ---------------- | ------------------- | --- | --- |
| no ipv6 prefix-priority |                  | [<PREFIX-LENGTHS>>] |     |     |
Description
ConfigurescustomIPv6routeprefixlengthsfortheexactprefixmatchtablesoftheswitch.Theswitch
mustberebootedtoapplythechange.
Followingthereboot,IPv6prefixprioritieswillremaininapendingstateuntilatleastonerouteislearned.A
connectedroutecountssothiscanbeassimpleashavinganL3interfacewithanIPaddressintheupstate.
Thenoformofthiscommandresetstheprefixlengthstotheirdefault
InitialConfiguration |31

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PREFIX-LENGTHS>> Specifiesaspace-separatedlistofexactlyfiveprefixlengths,in
descendingorder.Range:8to64.
Examples
ConfiguringcustomIPv6routeprefixlengths:
| switch(config)# | ipv6 | prefix-priority | 64 63 62 | 32 28 |
| --------------- | ---- | --------------- | -------- | ----- |
Save this config and reboot the switch for the changes to take effect
...
ResettingIPv6routeprefixlengthstotheirdefault:
| switch(config)# | no  | ipv6 prefix-priority |     |     |
| --------------- | --- | -------------------- | --- | --- |
Save this config and reboot the switch for the changes to take effect
...
AttemptingtoconfigurecustomIPv6routeprefixlengthswithsomelengthsnotindescendingorder:
| switch(config)# | ipv6 | prefix-priority | 64 62 63      | 31 32 |
| --------------- | ---- | --------------- | ------------- | ----- |
| Prefix lengths  | must | be specified    | in descending | order |
Attemptingtoconfigureeightprefixlengths:
| switch(config)# | ipv6      | prefix-priority | 64 63 62 | 32 31 28 24 23 |
| --------------- | --------- | --------------- | -------- | -------------- |
| Invalid         | input: 28 |                 |          |                |
Attemptingtoconfigurethreeprefixlengths:
| switch(config)# | ipv6        | prefix-priority | 64 63 31     |     |
| --------------- | ----------- | --------------- | ------------ | --- |
| % Command       | incomplete. |                 |              |     |
| Command History |             |                 |              |     |
| Release         |             |                 | Modification |     |
10.10
Commandintroduced.
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip prefix-priority |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
show ip prefix-priority
32
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

Description

Shows the configuration, status, and defaults of the IPv4 route prefix lengths for the exact prefix match
tables of the switch.

Examples

Showing configured IPv4 route prefix lengths that are pending until the switch is rebooted and at least
one route is learned:

switch# show ip prefix-priority

IP Exact-Prefix Table Information

Configuration Status: Ready to apply on next reboot

Default
Length

Current
Length

Pending
Length
Table
-----------------------------------
1
2
3
4
5

24
23
22
21
20

24
23
22
21
20

29*
28*
27*
24*
23*

* Pending values will be applied on the next reboot

Command History

Release

10.10

Command Information

Modification

Command introduced.

Platforms

Command context

Authority

8360

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show ipv6 prefix-priority
show ipv6 prefix-priority

Description

Shows the configuration, status, and defaults of the IPv6 route prefix lengths for the exact prefix match
tables of the switch.

Examples

Showing configured IPv6 route prefix lengths that are pending until the switch is rebooted and at least
one route is learned:

Initial Configuration | 33

switch# show ipv6 prefix-priority

IPv6 Exact-Prefix Table Information

Configuration Status: Ready to apply on next reboot

Current
Length

Default
Length

Pending
Table
Length
-----------------------------------
64
1
63*
2
62*
3
32*
4
31*
5

64
48
44
36
32

64
48
44
36
32

* Pending values will be applied on the next reboot

Command History

Release

10.10

Command Information

Modification

Command introduced.

Platforms

Command context

Authority

8360

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

Selecting the system profile
System profiles set the overall capabilities and capacities of the switch, based on the selected profile
used at boot time. System profiles set capacities such as that of the hardware forwarding table.

System profiles provide you with the flexibility to configure switches based on their location in the
network (for example, core, spine, leaf). When a switch boots without a profile specifically configured, it
boots with the default profile. When a switch is configured with a non-default profile, the switch
requires a reboot for the profile to be applied.

Command show profiles available shows all profiles available on a particular switch.

See also System profile commands.

Procedure

1. Set the system profile with the command profile.

2. Reboot the switch for the profile change to take effect with the command boot system.

Examples

(8320, 8325, 9300, 10000) Selecting the l3-agg profile and then rebooting the system:

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

34

| switch(config)# |     | profile l3-agg |
| --------------- | --- | -------------- |
switch(config)#
exit
| switch# | boot system |     |
| ------- | ----------- | --- |
...
(8320,8325,9300,10000)SelectingtheSpineprofileandthenrebootingthesystem:
| switch(config)# |             | profile Spine |
| --------------- | ----------- | ------------- |
| switch(config)# |             | exit          |
| switch#         | boot system |               |
...
(8360)SelectingtheCore-Spineprofileandthenrebootingthesystem:
| switch(config)# |             | profile Core-Spine |
| --------------- | ----------- | ------------------ |
| switch(config)# |             | exit               |
| switch#         | boot system |                    |
...
| System | profile | commands |
| ------ | ------- | -------- |
profile
| profile    | <PROFILE-NAME>   |     |
| ---------- | ---------------- | --- |
| no profile | [<PROFILE-NAME>] |     |
Description
Selectsthesystemprofile.Systemprofilessettheoverallcapabilitiesandcapacitiesoftheswitchbased
ontheselectedprofileusedatboottime.Switchprofilessetcapacitiessuchasthatofthehardware
forwardingtable.Usecommandshowprofilesavailabletoshowthedetailsofeachavailableprofile.
Whenaswitchisconfiguredwithanon-defaultprofile,theswitchrequiresarebootfortheprofiletobeapplied.
Youarepromptedforthereboot.
Thenoformofthiscommandresetsthespecifiedprofiletoitsdefaults.
8320,8325,9300,and10000SwitchSeries:
| Profile | names | Description |
| ------- | ----- | ----------- |
L3-agg Optimizesforlayer3forwardingwithmoretablespaceallocated
tohost(ARP/ND)entries.
L3-core (Thedefaultonthe8320SwitchSeries.)Optimizeforlayer3
forwardingwithmoretablespaceallocatedtorouteentries.
Leaf (Thedefaultonthe8325,9300,and10000SwitchSeries.)
Optimizesforlayer2forwardingwithmoretablespaceallocated
tooverlayhostentries(VXLAN).
spine Optimizesforlayer3forwardingwithmoretablespaceallocated
torouteentries.
InitialConfiguration |35

8360SwitchSeries:
| Profile names    |     |     | Description                               |
| ---------------- | --- | --- | ----------------------------------------- |
| Aggregation-Leaf |     |     | (Thedefault.)Optimizesforaggregationleaf. |
| Core-Spine       |     |     | Optimizesforcorespine.                    |
| Leaf-Extended    |     |     | Optimizesforleafextended.                 |
Examples
(8320,8325,9300,10000)SelectingtheL3-aggprofileandthenrebootingthesystem:
| switch(config)# | profile | l3-agg |     |
| --------------- | ------- | ------ | --- |
| switch(config)# | exit    |        |     |
switch#
boot system
...
(8320,8325,9300,10000)SelectingtheSpineprofileandthenrebootingthesystem:
| switch(config)# | profile     | Spine |     |
| --------------- | ----------- | ----- | --- |
| switch(config)# | exit        |       |     |
| switch#         | boot system |       |     |
...
(8360)SelectingtheCore-Spineprofileandthenrebootingthesystem:
switch(config)#
|                 | profile     | Core-Spine |     |
| --------------- | ----------- | ---------- | --- |
| switch(config)# | exit        |            |     |
| switch#         | boot system |            |     |
...
| Command History     |         |         |                              |
| ------------------- | ------- | ------- | ---------------------------- |
| Release             |         |         | Modification                 |
| 10.09               |         |         | CommandIntroducedonthe10000. |
| 10.07orearlier      |         |         | --                           |
| Command Information |         |         |                              |
| Platforms           | Command | context | Authority                    |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
9300
10000
| show profiles | available |     |     |
| ------------- | --------- | --- | --- |
| show profiles | available |     |     |
36
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Description

Shows all system profile names available and profile details.

Examples

Showing all available profiles for an 8320:

switch# show profiles available

Available profiles
-------------------
L3-agg

98304 L2 entries 120000 Host entries 16384

Route entries

L3-core

32768 L2 entries 14000

Host entries 131064 Route entries (Default)

Leaf

98304 L2 entries 120000 Host entries 16384

Route entries

Spine

32768 L2 entries 14000 Host entries 131064 Route entries

Showing all available profiles for an 8325 or 1000:

switch# show profiles available

Available profiles
-------------------
L3-agg

98304 L2 entries, 120000 Host entries (8190 unique overlay

neighbors, 48638 unique underlay neighbors), 29696 Route entries

L3-core

32768 L2 entries, 28000 Host entries (16382 unique overlay

neighbors, 32766 unique underlay neighbors), 163796 Route entries

Leaf

98304 L2 entries, 120000 Host entries (32766 unique overlay

neighbors, 12286 unique underlay neighbors), 29696 Route entries
(Default)

Spine

32768 L2 entries, 28000 Host entries (16382 unique overlay

neighbors, 32766 unique underlay neighbors), 163796 Route entries

Showing all available profiles for a 9300:

switch# show profiles available

Available profiles
-------------------
L3-agg

98304 L2 entries, 120000 Host entries (8190 unique overlay

neighbors, 48638 unique underlay neighbors), 29696 Route entries

L3-core

32768 L2 entries, 28000 Host entries (16382 unique overlay

neighbors, 32766 unique underlay neighbors), 163796 Route entries

Leaf

98304 L2 entries, 120000 Host entries (32766 unique overlay

neighbors, 12286 unique underlay neighbors), 29696 Route entries
(Default)

Spine

32768 L2 entries, 28000 Host entries (16382 unique overlay

neighbors, 32766 unique underlay neighbors), 163796 Route entries

Showing all available profiles for an 8360:

Initial Configuration | 37

| switch#   | show profiles | available |     |
| --------- | ------------- | --------- | --- |
| Available | profiles      |           |     |
-------------------
Aggregation-Leaf 114688 L2 entries, 163840 Host entries, 65536 Route entries
Core-Spine 32768 L2 entries, 65536 Host entries, 630784 Route entries
Leaf-Extended 212992 L2 entries, 16384 Host entries, 65536 Route entries
Showingallavailableprofilesfora10000:
switch#
|           | show profiles | available |     |
| --------- | ------------- | --------- | --- |
| Available | profiles      |           |     |
-------------------
L3-agg 98304 L2 entries, 120000 Host entries (8190 unique overlay
neighbors, 48638 unique underlay neighbors), 29696 Route entries
L3-core 32768 L2 entries, 28000 Host entries (16382 unique overlay
neighbors, 32764 unique underlay neighbors), 163796 Route entries
Leaf 98304 L2 entries, 120000 Host entries (32766 unique overlay
neighbors, 12284 unique underlay neighbors), 29696 Route entries
(Default)
Spine 32768 L2 entries, 28000 Host entries (16382 unique overlay
neighbors, 32764 unique underlay neighbors), 163796 Route entries
| Command History     |         |         |                              |
| ------------------- | ------- | ------- | ---------------------------- |
| Release             |         |         | Modification                 |
| 10.09               |         |         | CommandIntroducedonthe10000. |
| 10.07orearlier      |         |         | --                           |
| Command Information |         |         |                              |
| Platforms           | Command | context | Authority                    |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
| show profile | current |     |     |
| ------------ | ------- | --- | --- |
| show profile | current |     |     |
Description
Showsthecurrentsystemprofile.
Examples
38
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Showingthecurrentprofileonthe8320,8325,9300,or10000:
| switch# | show profile | current |     |     |     |
| ------- | ------------ | ------- | --- | --- | --- |
| Current | profile      |         |     |     |     |
-------------------
L3-core
Showingthecurrentprofileonthe8360:
| switch# | show profile | current |     |     |     |
| ------- | ------------ | ------- | --- | --- | --- |
| Current | profile      |         |     |     |     |
-------------------
Core-Spine
| Command History     |         |         |                              |     |     |
| ------------------- | ------- | ------- | ---------------------------- | --- | --- |
| Release             |         |         | Modification                 |     |     |
| 10.09               |         |         | CommandIntroducedonthe10000. |     |     |
| 10.07orearlier      |         |         | --                           |     |     |
| Command Information |         |         |                              |     |     |
| Platforms           | Command | context | Authority                    |     |     |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
| Restoring | the switch | to  | factory | default | settings |
| --------- | ---------- | --- | ------- | ------- | -------- |
Prerequisites
YouareconnectedtotheswitchthroughitsConsoleport.
ThisprocedureerasesalluserinformationandconfigurationsettingsConsiderbackingupyourrunning
configurationfirst.
1. Optionally,backuptherunningconfigurationwitheithercopy <REMOTE-URL>or
running-config
copy running-config <STORAGE-URL>.Thejsonstorageformatisrequiredforlater
configurationrestoration.
2. Switchtotheconfigurationcontextwiththecommandconfig.
3. Erasealluserinformationandconfiguration,restoringtheswitchtoitsfactorydefaultstatewith
thecommanderase all zeroize.EnterYwhenpromptedtocontinue.Theswitchautomatically
restarts.
InitialConfiguration |39

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
40
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

|     | Build            | Id:      | AOS-CX:XL.10.02.0010:feaf5b9b7f09:201901292014 |          |     |     |     |     |
| --- | ---------------- | -------- | ---------------------------------------------- | -------- | --- | --- | --- | --- |
|     | Build Date:      |          | 2019-01-29                                     | 12:43:50 | PST |     |     |     |
|     | Extracting       | Image... |                                                |          |     |     |     |     |
|     | Loading Image... |          |                                                |          |     |     |     |     |
Done.
|     | kexec_core: | Starting     |     | new kernel |     |     |     |     |
| --- | ----------- | ------------ | --- | ---------- | --- | --- | --- | --- |
|     | System is   | initializing |     |            |     |     |     |     |
fips_post_check[5473]: FIPS_POST: Cryptographic selftest started...SUCCESS
|     | [  OK ] | Started | Login | banner | readiness | check. |     |     |
| --- | ------- | ------- | ----- | ------ | --------- | ------ | --- | --- |
...
|     | 8400X login: | admin |     |     |     |     |     |     |
| --- | ------------ | ----- | --- | --- | --- | --- | --- | --- |
Password:
switch#
switch#
switch# copy tftp://192.168.1.10/backup_cfg running-config json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | --- | ----- | ------ | ----------- | ---------- |
100 10340 100 10340 0 0 2858k 0 --:--:-- --:--:-- --:--:-- 2858k
100 10340 100 10340 0 0 2804k 0 --:--:-- --:--:-- --:--:-- 2804k
Large configuration changes will take time to process, please be patient.
switch#
switch#
|     | switch# copy | running-config |     |     | startup-config |     |     |     |
| --- | ------------ | -------------- | --- | --- | -------------- | --- | --- | --- |
Large configuration changes will take time to process, please be patient.
switch#
| Management |     |     | interface |     | commands |     |     |     |
| ---------- | --- | --- | --------- | --- | -------- | --- | --- | --- |
default-gateway
| default-gateway |                 | <IP-ADDR> |           |     |     |     |     |     |
| --------------- | --------------- | --------- | --------- | --- | --- | --- | --- | --- |
| no              | default-gateway |           | <IP-ADDR> |     |     |     |     |     |
Description
AssignsanIPv4orIPv6defaultgatewaytothemanagementinterface.AnIPv4defaultgatewaycanonly
beconfiguredifastaticIPv4addresswasassignedtothemanagementinterface.AnIPv6default
gatewaycanonlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.The
defaultgatewayshouldbeonthesamenetworksegment.
Thenoformofthiscommandremovesthedefaultgatewayfromthemanagementinterface.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
SettingadefaultgatewaywiththeIPv4addressof198.168.5.1:
|     | switch(config)#         |     | interface | mgmt            |     |             |     |     |
| --- | ----------------------- | --- | --------- | --------------- | --- | ----------- | --- | --- |
|     | switch(config-if-mgmt)# |     |           | default-gateway |     | 198.168.5.1 |     |     |
InitialConfiguration |41

SettinganIPv6addressof2001:DB8::1:
| switch(config)#         | interface | mgmt            |              |             |
| ----------------------- | --------- | --------------- | ------------ | ----------- |
| switch(config-if-mgmt)# |           | default-gateway |              | 2001:DB8::1 |
| Command History         |           |                 |              |             |
| Release                 |           |                 | Modification |             |
| 10.07orearlier          |           |                 | --           |             |
| Command Information     |           |                 |              |             |
| Platforms               | Command   | context         | Authority    |             |
8320 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
9300
10000
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
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
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
42
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

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
8320 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
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
InitialConfiguration |43

| switch(config)# | interface | mgmt |     |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-mgmt)#
|                     |         | nameserver | 2001:DB8::1  | 2001:DB8::2 |
| ------------------- | ------- | ---------- | ------------ | ----------- |
| Command History     |         |            |              |             |
| Release             |         |            | Modification |             |
| 10.07orearlier      |         |            | --           |             |
| Command Information |         |            |              |             |
| Platforms           | Command | context    | Authority    |             |
8320 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
psm
psm {host <psm-ip-addr-1> <psm-ip-addr-2> <psm-ip-addr-3> [vrf default|mgmt]}| list | no
Description
ThePensandoPolicyandServicesManager(PSM)isaprogrammable,secure,highlyavailable,
centralizedsystemformanaginginfrastructurepolicy,withcapabilitiesfor:
n Deployingandcontrollingdistributedfirewallsecurity
Telemetryandanalytics
n
n Troubleshooting
n Operationsandmaintenance:events,alerts,technicalsupport
n Authentication,authorization,andaccounting(AAA)
ThePSMisdesignedtoestablishandmanageconsistentpoliciesforeach10000SwitchSeries
DistributedServicesSwitch(DSS).
Parameter Description
| host <psm-ip-addr-1> |     | <psm-ip-addr-2> | <psm-ip-addr-3> |     |
| -------------------- | --- | --------------- | --------------- | --- |
ProvidetheIPaddressesforthecluster
nodesofthePSMtowhichtheDSSwill
associate.Themaximumnumberof
hostsisthree,andbestpracticesisto
specifyallthree.
vrf default|mgmt
DefinethePSMconnectivitytype.
n defaultVRFconnectivityisin-band
tothePSM
n mgmtVRFconnectivityisout-of-
bandviamanagementVRFtothe
PSM
44
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

Parameter Description
list Printacommandlist
no Negateacommandorsetitsdefaults.
Usage
BeforeassociatingaDSSwithaPSM:
1. EnsurethattherewillbeLayer3connectivitybetweentheDSSandthePSMthroughthe
managementorin-bandinterface.
2. MakesurethattheDSSisnotcurrentlyassociatedwithanotherPSM.
3. Verifythatthetimeissetcorrectlyontheswitch.
ForcompleteinformationonthePensandoPolicyandServicesManager,refertothePensandoPolicy
andServicesManagerforDistributedServicesSwitches:UserGuide.
Examples
ConfiguringaDSStoassociatewithaPSMwiththreenodeswiththeIPaddresses192.168.68.49,
192.168.68.50,and192.168.68.51
| switch(config)# | psm |     |     |
| --------------- | --- | --- | --- |
switch(config-psm)# host 192.168.68.49 192.168.68.50 192.168.68.51 vrf default
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09.100           |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
config
9300 Administratorsorlocalusergroupmemberswithexecutionrights
| 10000          |                 |     | forthiscommand. |
| -------------- | --------------- | --- | --------------- |
| show interface | mgmt            |     |                 |
| show interface | mgmt [vsx-peer] |     |                 |
Description
Showsstatusandconfigurationinformationforthemanagementinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
InitialConfiguration |45

Example
| switch#                  | show interface |                 | mgmt    |                              |     |
| ------------------------ | -------------- | --------------- | ------- | ---------------------------- | --- |
| Address                  | Mode           |                 |         | : static                     |     |
| Admin                    | State          |                 |         | : up                         |     |
| Mac Address              |                |                 |         | : 02:42:ac:11:00:02          |     |
| IPv4 address/subnet-mask |                |                 |         | : 192.168.1.10/16            |     |
| Default                  | gateway        | IPv4            |         | : 192.168.1.1                |     |
| IPv6 address/prefix      |                |                 |         | : 2001:db8:0:1::129/64       |     |
| IPv6 link                | local          | address/prefix: |         | fe80::7272:cfff:fefd:e485/64 |     |
| Default                  | gateway        | IPv6            |         | : 2001:db8:0:1::1            |     |
| Primary                  | Nameserver     |                 |         | : 2001::1                    |     |
| Secondary                | Nameserver     |                 |         | : 2001::2                    |     |
| Command                  | History        |                 |         |                              |     |
| Release                  |                |                 |         | Modification                 |     |
| 10.07orearlier           |                |                 |         | --                           |     |
| Command                  | Information    |                 |         |                              |     |
| Platforms                | Command        |                 | context | Authority                    |     |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
show psm
show psm
Description
ShowconfiguringsettingsthatassociateaPensandoPolicyandServicesManager(PSM)witha10000
SwitchseriesDistributedServicesSwitch(DSS).
Examples
ThefollowingexampleshowsthePSM configurationonaDSS,wheretheDSS isassociatedwithaPSM
withthreenodeswiththeIPaddresses192.168.68.49,192.168.68.50,and192.168.68.51
| switch)#       | show     | psm |                     |                |               |
| -------------- | -------- | --- | ------------------- | -------------- | ------------- |
| Policy and     | Services |     | Manager Information |                |               |
| Operational    | Status   |     | : admitted          |                |               |
| Host Addresses |          |     | : 192.168.68.49,    | 192.168.68.50, | 192.168.68.51 |
| VRF            |          |     | : default           |                |               |
| Source IP      |          |     | : 18.127.1.1        |                |               |
| Command        | History  |     |                     |                |               |
46
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Release             |         |         | Modification      |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- |
| 10.09.100           |         |         | Commandintroduced |     |     |
| Command Information |         |         |                   |     |     |
| Platforms           | Command | context | Authority         |     |     |
9300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 10000 |     |     | forthiscommand. |     |     |
| ----- | --- | --- | --------------- | --- | --- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp authentication-key
| ntp authentication-key    |     | <KEY-ID>  | {md5 | sha1} |                 |     |
| ------------------------- | --- | --------- | ------------ | --------------- | --- |
| [{ <PLAINTXT-KEY>         |     | [trusted] | | ciphertext | <ENCRYPTED-KEY> | }]  |
| no ntp authentication-key |     | <KEY-ID>  | {md5 |       | sha1}           |     |
| [{ <PLAINTXT-KEY>         |     | [trusted] | | ciphertext | <ENCRYPTED-KEY> | }]  |
InitialConfiguration |47

Description
DefinesanauthenticationkeythatisusedtosecuretheexchangewithanNTPtimeserver.This
commandprovidesprotectionagainstaccidentallysynchronizingtoatimesourcethatisnottrusted.
Thenoformofthiscommandremovestheauthenticationkey.
| Parameter |     |     | Description                                     |     |     |
| --------- | --- | --- | ----------------------------------------------- | --- | --- |
| <KEY-ID>  |     |     | SpecifiestheauthenticationkeyID.Range:1to65534. |     |     |
md5
SelectsMD5keyencryption.
| sha1 |     |     | SpecifiesSHA1keyencryption. |     |     |
| ---- | --- | --- | --------------------------- | --- | --- |
<PLAINTXT-KEY>
Specifiestheplaintextauthenticationkey.Range:8to40
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
| Configure       | the key                | as trusted         | (y/n)?         |        |     |
y
Removingkey10:
| switch(config)# | no      | ntp authentication-key |     | 10  |     |
| --------------- | ------- | ---------------------- | --- | --- | --- |
| Command         | History |                        |     |     |     |
48
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp enable
ntp enable
no ntp enable
Description
EnablestheNTPclientontheswitchtoautomaticallyadjustthelocaltimeanddateontheswitch.The
NTPclientisdisabledbydefault.
ThenoformofthiscommanddisablestheNTPclient.
Examples
EnablingtheNTPclient.
InitialConfiguration |49

| switch(config)# |     | ntp | enable |     |     |     |
| --------------- | --- | --- | ------ | --- | --- | --- |
DisablingtheNTPclient.
| switch(config)# |             | no  | ntp enable |     |              |     |
| --------------- | ----------- | --- | ---------- | --- | ------------ | --- |
| Command         | History     |     |            |     |              |     |
| Release         |             |     |            |     | Modification |     |
| 10.07orearlier  |             |     |            |     | --           |     |
| Command         | Information |     |            |     |              |     |
| Platforms       | Command     |     | context    |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
vrf <VRF-NAME>
SpecifiestheVRFonwhichtoactasconductortimesource.
stratum <NUMBER> Specifiesthestratumlevelatwhichtheswitchoperates.Range:1-
15.Default:8.
Examples
SettingtheswitchtoactasconductortimesourceonVRFprimary-vrfwithastratumlevelof9.
| switch(config)# |     | ntp | conductor | vrf | primary-vry | statum 9 |
| --------------- | --- | --- | --------- | --- | ----------- | -------- |
StopstheswitchfromactingasconductortimesourceonVRFprimary-vrf.
| switch(config)# |         | no  | ntp conductor |     | vrf primary-vry |     |
| --------------- | ------- | --- | ------------- | --- | --------------- | --- |
| Command         | History |     |               |     |                 |     |
50
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.08               |         |         | Inclusivelanguage. |
| 10.07orearlier      |         |         | --                 |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
config
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
9300
10000
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
anIPv6address
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
WhenspecifyinganIPv4address,youcanremoveleadingzeros.
Forexample,theaddress192.169.005.100becomes
192.168.5.100.
WhenspecifyinganIPv6address,youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
key <KEY-NUM>
Specifiesthekeytousewhencommunicatingwiththeserver.A
trustedkeymustbedefinedwiththecommandntp
authentication-keyandauthenticationmustbeenabledwith
thecommandntp authentication.Range:1to65534.
minpoll <MIN-NUM> Specifiestheminimumpollingintervalinseconds,asapowerof
2.Range:4to17.Default:6(64seconds).
InitialConfiguration |51

Parameter

Description

maxpoll <MAX-NUM>

Specifies the maximum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 10 (1024 seconds).

burst

iburst

prefer

Send a burst of packets instead of just one when connected to the
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

When configuring a time backward more than five minutes on the Aruba 8320, 8325, or 9300 Switch Series, a

reboot is recommended to avoid unusual switch behavior.

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

52

Definingthentpservermy-ntp.mydomain.comandmakesitthepreferredserver.
| switch(config)#     | ntp     | server my-ntp.mydomain.com |              | prefer |
| ------------------- | ------- | -------------------------- | ------------ | ------ |
| Command History     |         |                            |              |        |
| Release             |         |                            | Modification |        |
| 10.07orearlier      |         |                            | --           |        |
| Command Information |         |                            |              |        |
| Platforms           | Command | context                    | Authority    |        |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
InitialConfiguration |53

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp vrf
ntp vrf <VRF-NAME>
| no ntp vrf <VRF-NAME> |     |     |     |
| --------------------- | --- | --- | --- |
Description
SpecifiestheVRFonwhichtheNTPclientcommunicateswithanNTPserver.Theswitchcannotfunction
asbothNTPconductorandclientonthesameVRF.
ThenoformofthecommandreturnstodefaultVRF.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VRF-NAME>
SpecifiesthenameofaVRF.
Example
SettingtheswitchtousethedefaultVRFforNTPclienttraffic.
switch(config)#
|     | ntp | vrf default |     |
| --- | --- | ----------- | --- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ntp              | associations |            |     |
| --------------------- | ------------ | ---------- | --- |
| show ntp associations |              | [vsx-peer] |     |
Description
54
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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

Initial Configuration | 55

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
switch#
show ntp authentication-keys
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ntp                   | servers |     |     |
| -------------------------- | ------- | --- | --- |
| show ntp servers[vsx-peer] |         |     |     |
Description
ShowsallconfiguredNTPservers,includinganyDHCPservers,defaultpoolserversoranyserverwith
| thestatusauto | prefer. |     |     |
| ------------- | ------- | --- | --- |
56
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

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
n Rx-pkts:TotalNTPpacketsreceived.
n CurrentVersionRx-pkts:NumberofNTPpacketsthatmatchthecurrentNTPversion.
n OldVersionRx-pkts:NumberofNTPpacketsthatmatchthepreviousNTPversion.
n Errorpkts:Packetsdroppedduetoallothererrorreasons.
n Auth-failedpkts:Packetsdroppedduetoauthenticationfailure.
n Declinedpkts:Packetsdeniedaccessforanyreason.
n Restrictedpkts:PacketsdroppedduetoNTPaccesscontrol.
n Rate-limitedpkts:Numberofpacketsdiscardedduetoratelimitation.
n KODpkts:NumberofKissofDeathpacketssent.
InitialConfiguration |57

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch(config)#     | show            | ntp statistics |              |
| ------------------- | --------------- | -------------- | ------------ |
|                     | Rx-pkts         | 100            |              |
| Current             | Version Rx-pkts | 80             |              |
| Old                 | Version Rx-pkts | 20             |              |
|                     | Err-pkts        | 2              |              |
| Auth-failed-pkts    |                 | 1              |              |
|                     | Declined-pkts   | 0              |              |
|                     | Restricted-pkts | 0              |              |
| Rate-limited-pkts   |                 | 0              |              |
|                     | KoD-pkts        | 0              |              |
| Command History     |                 |                |              |
| Release             |                 |                | Modification |
| 10.07orearlier      |                 |                | --           |
| Command Information |                 |                |              |
| Platforms           | Command         | context        | Authority    |
config
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
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
58
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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
InitialConfiguration |59

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
|                 | TCP        | Port           | : 23       |        |             |
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
60
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| show telnet | server          | sessions        |             |
| ----------- | --------------- | --------------- | ----------- |
| show telnet | server sessions | [vrf <VRF-NAME> | | all-vrfs] |
Description
ShowsallactiveTelnetsessionsforthespecifiedVRForallVRFs.IfnoVRFisprovided,theTelnet
sessionsonthedefaultVRFareshown.
| Parameter      |     | Description                                |     |
| -------------- | --- | ------------------------------------------ | --- |
| vrf <VRF-NAME> |     | SpecifiestheTelnetsessionsforaspecificVRF. |     |
all-vrfs
SpecifiestheTelnetsessionsforallVRFs
Examples
ShowingtheTelnetsessiononthedefaultVRF:
switch(config)#
|        | show            | telnet server sessions |     |
| ------ | --------------- | ---------------------- | --- |
| TELNET | sessions on VRF | default:               |     |
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
Telnetaccess|61

| Command   | Information |     |         |           |
| --------- | ----------- | --- | ------- | --------- |
| Platforms | Command     |     | context | Authority |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
62
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

Chapter 5
Interface configuration
| Interface configuration |         |             |
| ----------------------- | ------- | ----------- |
| Configuring             | a layer | 2 interface |
Procedure
1. Changetotheinterfaceconfigurationcontextfortheinterfacewiththecommandinterface.
2. Bydefault,interfacesarelayer3.Tocreatealayer2interface,disableroutingwiththecommand
no routing.
3. SettheinterfaceMTU(maximumtransmissionunit)withthecommandmtu.
4. Reviewinterfaceconfigurationsettingswiththecommandshow interface.
Example
| switch(config)#    | interface | 1/1/1       |
| ------------------ | --------- | ----------- |
| switch(config-if)# | no        | routing     |
| switch(config-if)# | mtu       | 1900        |
| Configuring        | a layer   | 3 interface |
Procedure
1. Changetotheinterfaceconfigurationcontextfortheinterfacewiththecommandinterface.
2. Interfacesarelayer3bydefault.Ifyoupreviouslysettheinterfacetolayer2,thenenablerouting
supportwiththecommandrouting.
3. AssignanIPv4addresswiththecommandip address,oranIPv6addresswiththecommand
ipv6 address.
4. Ifrequired,enablesupportforlayer3counterswiththecommandl3-counters.
5. Ifrequired,settheIPMTUwiththecommandip mtu.
6. Reviewinterfaceconfigurationsettingswiththecommandshow interface.
Examples
Thisexamplecreatesthefollowingconfiguration:
n Configuresinterface1/1/1asalayer3interface.
n DefinesanIPv4addressof10.10.20.209witha24-bitmask.
| switch# config     |           |                         |
| ------------------ | --------- | ----------------------- |
| switch(config)#    | interface | 1/1/1                   |
| switch(config-if)# | ip        | address 10.10.20.209/24 |
63
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

This example creates the following configuration:

n Configures interface 1/1/2 as a layer 3 interface.

n Defines an IPv6 address of 2001:0db8:85a3::8a2e:0370:7334 with a 24-bit mask.

n Enables layer 3 transmit and receive counters.

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

(Applies to the 8325, 9300, 10000)

Interface configuration | 64

On 8325 and 10000 series switches, a maximum of three unique PFC priority combinations can be
configured for the entire switch. On 9300 series switches, a maximum of seven unique PFC priority
combinations can be configured for the entire switch. Note that ports with a PFC configuration that
cannot be applied can still link up, but will not have any flow control. For example, when ports 1 to 4 are
configured for PFC priorities 3 and 4, ports 5 to 8 for PFC priority 4, and ports 9 to 12 for PFC priority 5,
then any other ports can only be configured for priority combinations of 3, 4, or 5. If a fourth priority
combination is configured the following error message will be displayed:

The number of unique priority-based flow control (PFC) configuration combinations
cannot be more than 3.

With PFC configured for TX, RXTX, or both, PFC cannot be enabled on an interface if the PFC priority is
not mapped to a lossless pool. If you attempt to configure a PFC priority on an interface without
mapping it to a lossless pool, the switch will display the following message:

All TX flow-controlled priorities must first be mapped to a lossless pool using
the 'qos pool' command.

Best practices is to configure priority-based flow control (PFC) or link-level flow control RXTX mode and
pools only once on a running system. Changing the pool or flow control configuration on a running
system will cause brief traffic disruption and packets may be lost in the data flow while the
reconfiguration occurs. This may effect one, multiple, or all ports depending on the existing
configuration and changes made to it.

(Applies to the 8325, 9300, 10000) Asymmetric PFC

Although PFC is typically symmetric in that it applies to both the receiving (RX) and sending (TX) of PFC
pause frames, it can be configured (using the flow-control command) to only respond to received (RX)
PFC pause frames or to only send (TX) PFC pause frames. This is referred to as asymmetric PFC.
Asymmetric PFC can be useful to implement PFC in only one direction in parts of the network. For
example, it could be desirable to have an uplink port that treats arriving traffic as lossless (respecting
PFC pause frames) but not transmit PFC pause frames into the spine or core of the network. This
capability can be used to deal with the unique requirements of some NICs which require asymmetric
PFC configuration to ensure proper behavior.

(Applies to the 8360)

PFC cannot be enabled on an interface that also has a MACsec policy configured. If both PFC and
MACsec are configured on an interface, it will remain down until one or the other is removed.

Reboot is required to split or unsplit a port that has had link up with PFC or RXTX enabled. Until reboot,
the interface will remain down with a status of Split in progress or Unsplit in progress.

Configurable flow control buffer thresholds

For the 8325, 9300, and 10000 series switch:

The switch supports the configuration of XOFF limit, XON delta and headroom limit buffer thresholds on
flow control enabled interfaces using flow-control buffer commands. QoS buffer configuration using
flow-control buffer commands are only applicable to ports or priorities only when flow control is
enabled. The flow control buffer configurations are optional. If the configurations are not done, defaults
are used.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

65

QoS buffer configuration for PFC priorities are not applicable to LLFC RXTX ports.

For information on this feature, see the related video on the Aruba AirHeads Broadcasting Channel.

XOFF limit

XOFF limit defines the amount of shared buffer space flow-controlled packets allowed to consume
before a pause is asserted to the link partner. The lossless buffer limits for traffic arriving on flow
control enabled ports or priorities can be optionally configured using one of the following two modes:

n Dynamic XOFF limit: The dynamic limit scales as a function of available buffer resources and is

configured by specifying an alpha value in the range between -7 and 3. The dynamic limit is based on
the currently available free space, multiplied by 2 raised to the power of the specified alpha value. A
value less than zero means that the limit is a fraction of the pool free space. For example, -1
corresponds to half. A value greater than zero means that the limit is a multiple of the free-space
size. For example, an alpha value of 1 corresponds to double.

If the user-configured limit is not specified, the default limit of dynamic alpha 1 is configured.

n Static XOFF limit: The static limit sets a fixed size for the XOFF threshold.

XON delta

XON delta defines the offset value below the XOFF limit when a pause is de-asserted to the link partner.
The delta value is relative to the XOFF limit and applies to both dynamic and static XOFF limit
configurations. When the buffer in-use amount from a source port (LLFC RXTX) or source port with
priority (PFC) reaches the XOFF limit, a pause is asserted to the link peer. At this point, the pause will
remain asserted until the shared buffer in-use amount by the LLFC RXTX port or priority decreases by
the XON delta amount. Once enough packets are transmitted to reduce in-use by this amount, the
pause is de-asserted.

It is important to note that the XON delta value will impact the amount of flow control pause frames sent to the

link peer and can have a negative impact on performance. A value that is too small can result in many more

pause frames sent to the link peer as the buffer in-use amount reaches the XOFF limit, drops slightly, and meets

the XON delta, then immediately jumps back to the XOFF limit. Conversely, a value that is too large can result in

poor link bandwidth utilization due to insufficient buffered packets as the buffer drains too far before more

packets arrive to utilize the link. The default XON Delta value is 12288 bytes.

Headroom limit

Headroom limit defines the amount of buffer space reserved to absorb any in-flight packets from the
time that the XOFF message is transmitted by the local device until the time that the last packet is sent
by the link partner and received by the local device. Headroom Limit for an LLFC RXTX port or PFC
priority sets a fixed size of headroom pool buffer space for in-flight packets that arrive after XOFF is
asserted.

Default buffer thresholds

By default, when the LLFC RXTX or PFC is enabled, the switch uses a dynamic buffer threshold for the
XOFF limit, a delta value for XON, and a headroom buffer limit based on 350m cable length.

For many scenarios, these defaults are sufficient to provide good performance without any issues.
However, in some situations it is useful to tune the XOFF limit, XON delta, and headroom parameters
based on the unique requirements of a particular deployment. In those situations, the buffer tuning
capabilities described in this section can be useful to optimize memory usage.

Interface configuration | 66

Theflowcontrolbufferconfigurationsareoptional.Iftheconfigurationsarenotdone,defaultsareused.
| Flow control | buffer | tasks |     |     |     |
| ------------ | ------ | ----- | --- | --- | --- |
Theflowcontrolbuffertasksareasfollows:
| Tasks     | Command      |                 | Examples           |              |       |
| --------- | ------------ | --------------- | ------------------ | ------------ | ----- |
| Configuri | flow-control | buffer priority |                    |              |       |
| ng        | <PRIORITY>   |                 | switch(config)#    | interface    | 1/1/1 |
| dynamic   | xoff dynamic | <ALPHA>         | switch(config-if)# | flow-control |       |
| XOFFlimit | flow-control | buffer llfc     | buffer priority    | 5            |       |
|           |              |                 | xoff dynamic       | -3           |       |
|           | xoff dynamic | <ALPHA>         |                    |              |       |
|           |              |                 | switch(config)#    | interface    | 1/1/1 |
|           |              |                 | switch(config-if)# | flow-control |       |
|           |              |                 | buffer llfc        |              |       |
|           |              |                 | xoff dynamic       | -3           |       |
| Configuri | flow-control | buffer priority |                    |              |       |
| ngstatic  | <PRIORITY>   |                 | switch(config)#    | interface    | 1/1/1 |
XOFFlimit xoff static <LIMIT> kbytes switch(config-if)# flow-control
|           | flow-control | buffer llfc     | buffer priority    | 6            |       |
| --------- | ------------ | --------------- | ------------------ | ------------ | ----- |
|           | xoff static  | <LIMIT> kbytes  | xoff static        | 128 kbytes   |       |
|           |              |                 | switch(config)#    | interface    | 1/1/1 |
|           |              |                 | switch(config-if)# | flow-control |       |
|           |              |                 | buffer llfc        |              |       |
|           |              |                 | xoff static        | 128 kbytes   |       |
| Configuri | flow-control | buffer priority |                    |              |       |
| ng        | <PRIORITY>   |                 | switch(config)#    | interface    | 1/1/1 |
| XON delta | xon <VALUE>  | kbytes          | switch(config-if)# | flow-control |       |
|           | flow-control | buffer llfc     | buffer priority    | 4            |       |
|           | xon <VALUE>  | kbytes          | xon 24 kbytes      |              |       |
|           |              |                 | switch(config)#    | interface    | 1/1/1 |
|           |              |                 | switch(config-if)# | flow-control |       |
|           |              |                 | buffer llfc        |              |       |
|           |              |                 | xon 24 kbytes      |              |       |
|           | flow-control | buffer priority |                    |              |       |
Configuri
|     | <PRIORITY> |     | switch(config)# | interface | 1/1/1 |
| --- | ---------- | --- | --------------- | --------- | ----- |
ng
|         |              |                | switch(config-if)# | flow-control |       |
| ------- | ------------ | -------------- | ------------------ | ------------ | ----- |
| headroo | headroom     | <LIMIT> kbytes |                    |              |       |
| mlimit  | flow-control | buffer llfc    | buffer priority    | 4            |       |
|         | headroom     | <LIMIT> kbytes | headroom           | 36 kbytes    |       |
|         |              |                | switch(config)#    | interface    | 1/1/1 |
|         |              |                | switch(config-if)# | flow-control |       |
|         |              |                | buffer llfc        |              |       |
|         |              |                | headroom           | 36 kbytes    |       |
67
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

Flow control and lossless buffering

For the 8325, 9300, and 10000 series switch:

The switch supports IEEE 802.1Q Priority-based Flow Control (PFC). The PFC standard specifies
additional frames exchanged between the Ethernet Media Access Controllers (MACs) on both sides of a
link to pause and resume transmissions. The goal is to prevent packet loss despite congestion.

Prerequisites

1. A Priority Code Point (PCP) chosen for PFC must not share a local priority with any other PCP in

the Class of Service (CoS) map.

2. A local priority mapped to the PCP via the CoS Map must be the only local priority assigned to its

queue in the queue profile.

NOTE: These prerequisites should be configured during initial switch provisioning and only changed during

maintenance periods where all ports are disabled and the switch is then rebooted.

Requirements for proper lossless buffering:

n Lossless buffering is only supported for single destination (i.e. unicast) traffic. Multi-destination traffic

cannot be guaranteed to be lossless.

n All traffic with the specified PCP arriving on PFC-configured ports must be destined for another PFC-

configured-port with an egress queue with the same PCP.

n All packets arriving on PFC-configured ports or arriving on non-PFC ports must not be destined for an

egress port queue used by PFC traffic with a different PCP.

n If traffic path contains Layer 3 interface then ECN would also need to be added to the configuration.

n The switch has maximum of 3 PFC lossless priorities and does not support PFC below 10 Gbps.

By default, all switch buffering is in one pool shared by all ports called the Lossy pool. Any packet
intending to use the Lossy pool can be dropped if the egress port queue is above its limit. Egress queue
limits are dynamic based on the amount of free buffers available in the Lossy pool. The TX Drops
columns displayed from the show interface <IF-NAME> command will display the number of drops that
have occurred.

All traffic with the specified PCP arriving on PFC-configured ports will share the Lossless or Headroom
pools. Any packets using these pools will never be dropped when an egress queue exceeds its limit. All
other packets arriving on PFC-configured ports with different PCPs or on non-PFC ports will share the
Lossy pool and be subject to dropping when an egress queue is over its limit.

Each PFC-configured port priority is given a limit for the amount of Lossless pool buffering its arriving
packets can use. Once the limit is exceeded, the switch will transmit a priority pause frame from the
port to stop further packets arriving. Due to link propagation time and processing time on the receiving
switch additional packets may be received and stored in the Headroom pool.

When the switch receives a PFC pause frame for the configured PCP the port will cease transmitting
further packets from that queue until the timeout specified in the Quanta field has expired or a resume
frame is received.

For the 8360 series switch:

The switch supports IEEE 802.1Q Priority-based Flow Control (PFC) and 802.3x Link Level Flow Control
(LLFC). These standards specify additional frames exchanged between the Ethernet Media Access

Interface configuration | 68

Controllers (MACs) on both sides of a link to pause and resume transmissions. The goal is to prevent
packet loss despite congestion.

Prerequisites

1. A Priority Code Point (PCP) chosen for PFC must not share a local priority with any other PCP in the
Class of Service (CoS) map.

2. A local priority mapped to the PCP via the CoS map must be the only local priority assigned to its
queue in the queue profile.

NOTE: These prerequisites should be configured during initial switch provisioning and only changed during

maintenance periods where all ports are disabled.

Requirements for proper lossless buffering

n Lossless buffering is only supported for single-destination (i.e. unicast) traffic. Multi-destination traffic

is not guaranteed to be lossless.

n All arriving flow-controlled traffic must only be transmitted by flow-controlled ports or port queue(s):

o For LLFC-operating ports all arriving traffic must be destined for another LLFC port.

o For PFC-enabled ports all arriving packets with the configured PCP must be destined for another

PFC-enabled port queue with the same PCP.

n All arriving non-flow-controlled traffic must only be transmitted by non-flow-controlled ports or port

queue(s).

n For traffic arriving on non-LLFC ports and on PFC ports with different PCPs, packets must not be

destined to be transmitted out an LLFC-operating port or a PFC-enabled port queue.

n PFC cannot be used on MACsec configured ports

n The switch can support 2 PCPs for per port

By default, all switch buffering is in one pool shared by all ports called the Lossy pool. Any packet
attempting to use the Lossy pool can be dropped if the egress port queue is above its limit. Egress port
queues have a limit of 2 MB divided equally among the number of queues in the applied queue profile.
For example, when using the 8-queue factory-default profile the egress queue limit is 256 KB. The TX
Drops columns of show interface <IF-NAME> command will display the number of drops that may have
occurred.

Flow Control reconfigures buffering. After the first interface is configured for PFC the switch will
segregate buffering into multiple pools:

n Lossy Pool (default)

n Lossless Pool

n Headroom Pool

Buffers are moved from the Lossy to the Lossless and Headroom pools depending on the number and
maximum possible speed of the ports on the switch model. The Headroom pool size assumes that all
port cables are 300 meters in length.

NOTE: Using slower port speeds or different cable lengths will not change the pool allocations.

All traffic with the specified PCP arriving on PFC-configured ports or on an LLFC-operating port will share
the Lossless and Headroom pools. Any packets stored in these pools will never be dropped if an egress
queue exceeds its limit. All other packets arriving on non-flow-control ports, or on PFC-enabled port(s)

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

69

with different PCPs will share the Lossy pool and be subject to drops when an egress queue exceeds its
limit.

Each LLFC port and each PFC-port priority has a limited amount of Lossless pool buffer space that
arriving packets are allowed to use. Once the limit is exceeded the switch will transmit a pause frame
out the port to stop further packets from arriving. Due to link propagation time and processing time on
the receiving switch, additional packets in flight may be received and will share the Headroom pool. The
switch will periodically transmit priority pause frames until none of packets on the arriving port are in
the Headroom pool and half of the port's shared buffer below the pause limit is available.

When the switch receives a PFC pause frame for the configured PCP, the port will cease transmitting
further packets from that queue until the timeout specified in the Quanta field has expired or a resume
frame is received.

Forward error correction
Forward error correction (FEC) is used to control errors in transmissions where the source sends
redundant data and the destination only recognizes the data portion that contains no apparent errors.
FEC does not require a handshake between the source and destination at the cost of a higher forward
channel bandwidth. It is therefore best used in scenarios where re-transmissions are costly or
impossible, such as using multicast one-way communication.

Unsupported transceiver support
Transceiver products (optical, DAC, AOCs) that are listed as supported by a switch model are detailed in
the Transceiver Guide. Transceiver products that are not listed, are considered unsupported; this would
include transceivers that are:

n Non-Aruba branded products

n HPE branded products that were designed for non-AOS-CX switch models (e.g. Comware)

n HPE branded products designated for use in HPE Compute Servers or Storage

n Transceivers originally designated for use in Aruba WLAN controllers or former Mobility Access

Switch (MAS) products

n End-of-life Aruba Transceivers

The unsupported transceiver mode (UT-mode) is designed to allow the possible use of these
unsupported products. Not all unsupported products can be recognized and enabled; they may be
unable to be identified (do not follow the proper MSA standards for identification). These unsupported
transceiver products are enabled only on a best-effort basis and there are no guarantees implied for
their continued operation.

This feature is enabled by default. A periodic system log will be generated by default at an interval of 24
hours listing the ports on which unsupported transceivers are present. The log interval is configurable
and can be disabled by setting the log-interval to none.

Configuring an interface persona
A persona is a template interface. It is a mechanism intended to eases the process of configuring one or
multiple interfaces that behave in the same manner. For example, a persona could be an uplink
interface with a well-known collection of VLANs to which it belongs. Instead of manually configuring
each interface one-by-one, the persona collects the common configuration settings and allows them to
be applied on the interface or a collection of interfaces.

Interface configuration | 70

Personaconfigurationissimilartoconfiguringotherinterfaces.Mostofthecommandsintheinterface
contextareavailable.Becauseofthenatureofthecommands,severalofthemdonotapplytothe
persona(forexample,applyingthesameIPaddressconfigurationtoseveralports)andhavebeen
removedfromtheavailablelist.
Thefollowingcommandsarenotsupportedwithintheinterfacecontextwhenconfiguringapersona:
| aaa authentication |             | port-access |                | dot1x | authenticator |     |     | macsec |
| ------------------ | ----------- | ----------- | -------------- | ----- | ------------- | --- | --- | ------ |
| arp ipv4           | <IPV4_ADDR> |             | mac <MAC_ADDR> |       |               |     |     |        |
downshift-enable
energy-efficient-ethernet
| error-control              |     | { auto            | | none      | | base-r-fec      |              | |            | rs-fec | }             |
| -------------------------- | --- | ----------------- | ----------- | ----------------- | ------------ | ------------ | ------ | ------------- |
| ip bootp-gateway           |     | <IPV4-ADDR>       |             |                   |              |              |        |               |
| ip forward-protocol        |     | udp               | <IPV4-ADDR> |                   | {<PORT-NUM>  |              |        | | <PROTOCOL>} |
| ip helper-address          |     | <IPV4-ADDR>       |             | [vrf              | <VRF-NAME>]  |              |        |               |
| ip igmp router-alert-check |     |                   |             | [enable           | | disable]   |              |        |               |
| ip igmp snooping           |     | [auto             | vlan        | <VLAN-LIST>]      |              |              |        |               |
| ip igmp snooping           |     | [blocked          |             | vlan <VLAN-LIST>] |              |              |        |               |
| ip igmp snooping           |     | [fastleave        |             | vlan              | <VLAN-LIST>] |              |        |               |
| ip igmp snooping           |     | [forced-fastleave |             |                   | vlan         | <VLAN-LIST>] |        |               |
| ip igmp snooping           |     | [forward          |             | vlan <VLAN-LIST>] |              |              |        |               |
| ip ospf <PROCESS-ID>       |     |                   | area        | <AREA-ID>         |              |              |        |               |
| ip ospf passive            |     |                   |             |                   |              |              |        |               |
| ip rip <PROCESS-ID>        |     | {all-ip           |             | | ip-address}     |              |              |        |               |
| ip rip all-ip              |     | disable           |             |                   |              |              |        |               |
| ip rip all-ip              |     | enable            |             |                   |              |              |        |               |
| ip rip all-ip              |     | receive           | disable     |                   |              |              |        |               |
| ip rip all-ip              |     | send disable      |             |                   |              |              |        |               |
ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
| ipv6 mld           | snooping     | [auto             | vlan | <VLAN-LIST>]   |              |              |     |     |
| ------------------ | ------------ | ----------------- | ---- | -------------- | ------------ | ------------ | --- | --- |
| ipv6 mld           | snooping     | [blocked          |      | vlan           | <VLAN-LIST>] |              |     |     |
| ipv6 mld           | snooping     | [fastleave        |      | vlan           | <VLAN-LIST>] |              |     |     |
| ipv6 mld           | snooping     | [forced-fastleave |      |                | vlan         | <VLAN-LIST>] |     |     |
| ipv6 mld           | snooping     | [forward          |      | vlan           | <VLAN-LIST>] |              |     |     |
| ipv6 neighbor      |              | <IPV6-ADDR>       |      | mac <MAC-ADDR> |              |              |     |     |
| ipv6 ospfv3        | <PROCESS-ID> |                   | area | <AREA-ID>      |              |              |     |     |
| ipv6 ospfv3        | passive      |                   |      |                |              |              |     |     |
| ipv6 ripng         | <PROCESS-ID> |                   |      |                |              |              |     |     |
| lacp port-id       | <PORT-ID>    |                   |      |                |              |              |     |     |
| lacp port-priority |              | <PORT-PRIORITY>   |      |                |              |              |     |     |
lag <ID>
link-poe
| lldp dot3 | eee                     |     |     |     |     |     |     |     |
| --------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| lldp dot3 | poe                     |     |     |     |     |     |     |     |
| lldp med  | poe                     |     |     |     |     |     |     |     |
| lldp med  | poe [priority-override] |     |     |     |     |     |     |     |
persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
| port-access | device-profile |     |     | <DEVICE-PROFILE-NAME> |     |     |     |     |
| ----------- | -------------- | --- | --- | --------------------- | --- | --- | --- | --- |
power-over-ethernet
| power-over-ethernet |          | allocate-by       |               |                     | {usage                  | | class}    |     |     |
| ------------------- | -------- | ----------------- | ------------- | ------------------- | ----------------------- | ----------- | --- | --- |
| power-over-ethernet |          | assigned-class    |               |                     | {3                      | | 4 |       | 6 | | 8}  |
| power-over-ethernet |          | pd-class-override |               |                     |                         |             |     |     |
| power-over-ethernet |          | power-pairs       |               |                     | {alt-a|alt-a-and-alt-b} |             |     |     |
| power-over-ethernet |          | pre-std-detect    |               |                     |                         |             |     |     |
| power-over-ethernet |          | priority          |               | {critical|high|low} |                         |             |     |     |
| ptp lag-role        | {primary |                   | | secondary}  |                     |                         |             |     |     |
| spanning-tree       |          | cost <PORT-COST>  |               |                     |                         |             |     |     |
| spanning-tree       |          | instance          | <INSTANCE-ID> |                     | cost                    | <PORT-COST> |     |     |
spanning-tree instance <INSTANCE-ID> port-priority <PRIORITY-MULTIPLIER>
| spanning-tree |     | port-priority   |     | <PRIORITY-MULTIPLIER> |               |     |     |     |
| ------------- | --- | --------------- | --- | --------------------- | ------------- | --- | --- | --- |
| spanning-tree |     | vlan <A:1-4094> |     | cost                  | <0-200000000> |     |     |     |
71
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

| spanning-tree | vlan | <A:1-4094> | port-priority | <0-15> |     |
| ------------- | ---- | ---------- | ------------- | ------ | --- |
split [confirm]
| track by | <OBJECT-ID> |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
vsx-sync {access-lists | qos | rate-limits | vlans | policies | irdp}
Modes
Therearetwosupportedmodes:
1.Copy—Thecopymodeisaone-stepconfigurationthatcopiesthepersonaconfigurationtoan
interface.Furtherchangestothepersonawillnotbeappliedtotheinterfacesusingthatmode.
2.Attach—Unlikethecopymode,besidesapplyingtheconfigurationtotheinterfaceimmediately,the
attachmodealsofollowsthepersonaconfiguration.Itmeansthatthesubsequentchangestothe
personawillbeappliedtotheinterfacesattachedtoit.
| Predefined | and | custom | persona | names |     |
| ---------- | --- | ------ | ------- | ----- | --- |
Therearetwopredefinedinterfacepersonanames:
uplink
n
n access
Thesenameshavenopredefinedconfiguration.Tousethem,theymustbemanuallyconfiguredas
needed.Youcanalsocreatepersonaswithacustomname.Thesecustompersonascanbecreatedand
configuredinthesamemannerasthepredefinedones.Theonlydifferenceisthecommandusedto
applythemtotheinterface.Theprocedurebelowprovidesthedetails.
| Creating | and | configuring | an interface |     | persona |
| -------- | --- | ----------- | ------------ | --- | ------- |
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
| switch(config)#    |     | interface   | persona uplink |     |     |
| ------------------ | --- | ----------- | -------------- | --- | --- |
| switch(config-if)# |     | no shutdown |                |     |     |
| switch(config-if)# |     | no routing  |                |     |     |
| switch(config-if)# |     | vlan        | access 100     |     |     |
| switch(config-if)# |     | exit        |                |     |     |
2.Applytheconfigurationwithcopymode:
Interfaceconfiguration|72

| switch(config)#    | interface | 1/1/1            |      |
| ------------------ | --------- | ---------------- | ---- |
| switch(config-if)# | persona   | custom mypersona | copy |
| switch(config-if)# | exit      |                  |      |
Toattachacustompersonanametoseveralinterfacessimultaneously:
1.Configuretheinterfacepersona:
| switch(config)#    | interface   | persona mytemplate |     |
| ------------------ | ----------- | ------------------ | --- |
| switch(config-if)# | no shutdown |                    |     |
| switch(config-if)# | vrf         | attach upstream    |     |
| switch(config-if)# | exit        |                    |     |
2.Applytheconfigurationwithattachmode:
| switch(config)#    | interface | 1/1/1-1/1/24     |        |
| ------------------ | --------- | ---------------- | ------ |
| switch(config-if)# | persona   | custom mypersona | attach |
| switch(config-if)# | exit      |                  |        |
| Monitor mode       |           |                  |        |
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
| Interface commands |     |     |     |
| ------------------ | --- | --- | --- |
allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver
Description
Allowsunsupportedtransceiverstobeenabledorestablishconnections.Transceiverswithspeedsupto
100Gareenabledbythiscommand.
73
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

n The following models will enable unsupported transceivers for speeds up to 100G when running AOS-CX

10.09.0001 or later:

o 8325 (Models 48Y8C and 32C)

o 8360 (Models 48Y6C, 32Y4C, 16Y2C, 48XT4C, 24XF2C and 12C)

o 9300 Series Switches

o 10000 Series Switches

n The 8320 Series Switches will enable unsupported transceivers for speeds up to 40G when running AOS-CX

10.10 or later.

As of AOS-CX 10.06.0100, this command is enabled by default, allowing the use of third party transceiver
products without adding the command in the configuration. Disabling this command with the no form will now
disable the command in the running and stored configurations.

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

Interface configuration | 74

Configuringunsupportedtransceiverloggingwithanintervalofevery48hours:
switch(config)# allow-unsupported-transceiver log-interval 2880
Disablingunsupportedtransceiverlogging:
switch(config)# allow-unsupported-transceiver log-interval none
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
switch(config)#
|     | no  | allow-unsupported-transceiver |     |     |
| --- | --- | ----------------------------- | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
| Continue    | (y/n)? y    |               |           |       |
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | no  | allow-unsupported-transceiver |     | confirm |
| --------------- | --- | ----------------------------- | --- | ------- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
switch(config)#
| Command History |     |     |                                                     |     |
| --------------- | --- | --- | --------------------------------------------------- | --- |
| Release         |     |     | Modification                                        |     |
| 10.10           |     |     | Upto100G supportenabledforunsupportedtransceiverson |     |
8320(Upto40G)seriesswitchesinUT mode.
| 10.09 |     |     | Upto100G supportenabledforunsupportedtransceiverson |     |
| ----- | --- | --- | --------------------------------------------------- | --- |
8325,8360and10000seriesswitchesinUT mode.
| 10.07orearlier      |         |         | --        |     |
| ------------------- | ------- | ------- | --------- | --- |
| Command Information |         |         |           |     |
| Platforms           | Command | context | Authority |     |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
9300
10000
| default interface |                |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
| default interface | <INTERFACE-ID> |     |     |     |
Description
75
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

Setsaninterface(orarangeofinterfaces)tofactorydefaultvalues.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID> SpecifiestheIDofasingleinterfaceorrangeofinterfaces.
Format:member/slot/portormember/slot/port-
member/slot/porttospecifyarange.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| SettingthedescriptionforaninterfacetoDataLink |     |     |     | 01: |
| --------------------------------------------- | --- | --- | --- | --- |
Interfaceconfiguration|76

| switch(config-if)# |     | description |     | DataLink | 01  |
| ------------------ | --- | ----------- | --- | -------- | --- |
Removingthedescriptionforaninterface.
| switch(config-if)# |             | no description |     |              |     |
| ------------------ | ----------- | -------------- | --- | ------------ | --- |
| Command            | History     |                |     |              |     |
| Release            |             |                |     | Modification |     |
| 10.07orearlier     |             |                |     | --           |     |
| Command            | Information |                |     |              |     |
| Platforms          | Command     | context        |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
case.TheycanonlysetFECtononewhenauto-negotiationisdisabledthroughthespeed overridecommand.
Thedefaultfortheinstalledtransceiverisusedinallothercases.
TransceiversforwhichFECisauto-negotiatedwillrequestthemodeconfiguredbythiscommand,butmay
resolvetoadifferentmode.TheappliedFEC modeisdisplayedasacommentedlineintheconfigurationshown
withtheshow runcommand.Itisalsodisplayedwithshow interfacecommand.
| Parameter |     |     |     | Description               |     |
| --------- | --- | --- | --- | ------------------------- | --- |
| auto      |     |     |     | Usethetransceiverdefault. |     |
| none      |     |     |     | DonotuseanyFEC.           |     |
77
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Parameter  |             |         | Description                 |
| ---------- | ----------- | ------- | --------------------------- |
| base-r-fec |             |         | UseIEEEBASE-R(Firecode)FEC. |
| rs-fec     |             |         | UseIEEERS(Reed-Solomon)FEC. |
| Command    | History     |         |                             |
| Release    |             |         | Modification                |
| 10.08.1021 |             |         | Commandintroduced.          |
| Command    | Information |         |                             |
| Platforms  | Command     | context | Authority                   |
8325 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8360
9300
10000
flow-control
Onthe8320:
| flow-control    | rx  |     |     |
| --------------- | --- | --- | --- |
| no flow-control | rx  |     |     |
Onthe8325:
| flow-control    | {rx | rxtx | [pool <POOL-NUM>]}      |     |
| --------------- | ---------- | ----------------------- | --- |
| no flow-control | {rx |      | rxtx [pool <POOL-NUM>]} |     |
flow-control priority {rxtx <PRIORITY-LIST> | rx <PRIORITY-LIST> | tx <PRIORITY-LIST>}
...
no flow-control priority {rxtx <PRIORITY-LIST> | rx <PRIORITY-LIST> | tx <PRIORITY-LIST>}
...
Note:Uptothreeprioritylistsinthesamecommandaresupported,oneeachforrxtx,rx,andtx.
Onthe8360:
| flow-control    | {rx | rxtx} |                      |     |
| --------------- | ----------- | -------------------- | --- |
| no flow-control | {rx |       | rxtx}                |     |
| flow-control    | priority    | rxtx <PRIORITY-LIST> |     |
| no flow-control | priority    | rxtx <PRIORITY-LIST> |     |
Onthe9300:
| flow-control    | {rx | rxtx | [pool <POOL-NUM>]}      |     |
| --------------- | ---------- | ----------------------- | --- |
| no flow-control | {rx |      | rxtx [pool <POOL-NUM>]} |     |
flow-control priority {rxtx <PRIORITY-LIST> | rx <PRIORITY-LIST> | tx <PRIORITY-LIST>}
...
no flow-control priority {rxtx <PRIORITY-LIST> | rx <PRIORITY-LIST> | tx <PRIORITY-LIST>}
...
Note:Uptothreeprioritylistsinthesamecommandaresupported,oneeachforrxtx,rx,andtx.
Onthe10000:
| flow-control    | {rx | rxtx | [pool <POOL-NUM>]}      |     |
| --------------- | ---------- | ----------------------- | --- |
| no flow-control | {rx |      | rxtx [pool <POOL-NUM>]} |     |
flow-control priority {rxtx <PRIORITY-LIST> | rx <PRIORITY-LIST> | tx <PRIORITY-LIST>}
Interfaceconfiguration|78

...
no flow-control priority {rxtx <PRIORITY-LIST> | rx <PRIORITY-LIST> | tx <PRIORITY-LIST>}
...

Note: Up to three priority lists in the same command are supported, one each for rxtx, rx, and tx.

Description

On the 8320, flow-control enables negotiation of receive flow control on the current interface. The
switch advertises RX support to the link partner.

On the 8325, 8360, 9300, and 10000, flow-control enables negotiation of either receive-only flow
control or both receive and transmit flow control on the current interface. The switch advertises either
RX or RXTX support to the link partner. The final configuration is determined based on the capabilities of
both partners.

On the 8325, 8360, 9300, and 10000, flow-control priority enables priority-based flow control (PFC).
Multiple priorities are supported. Bidirectional (symmetric) PFC is configured with parameter priority
rxtx. Unidirectional (asymmetric) PFC is configured with either parameter priority rx or priority tx.

On the 8325, 8360, 9300, and 10000, when configuring PFC for multiple priority levels, the complete list
of priorities must be specified in a single command. Priorities cannot be added or subtracted using
separate commands.

Each invocation of this command replaces the previous configuration.

The no form of these commands disables any configured flow control on the selected interface.

Parameter

Description

rx

rxtx

rxtx [pool <POOL-NUM>]

priority rxtx

priority rx

priority tx

Enables the ability to cease and resume transmission when
receiving IEEE 802.3x LLFC pause frames on this interface.

(Applies to the 8360.) Enables the ability to honor received and to
transmit IEEE 802.3x LLFC pause frames to the remote device.

(Applies to the 8325, 9300, 10000.) rxtx enables the ability to
honor received and to transmit IEEE 802.3x LLFC pause frames to
the remote device.
pool <POOL-NUM> optionally selects the number of the lossless
pool used for buffering packets arriving on this interface. Default:
1. Range: 1 to 3.

(Applies to the 8325, 8360, 9300, 10000.) Enables the ability to
honor received and to transmit IEEE 802.1Qbb PFC pause frames
on the interface for the configured packet priority.

(Applies to the 8325, 9300, 10000.) Enables the ability to honor
received IEEE 802.1Qbb PFC pause frames on the interface for the
configured packet priorities. This can be useful for implementing
asymmetric PFC when it is desired to configure this only in the
receive direction.

(Applies to the 8325, 9300, 10000.) Enables the ability to transmit
IEEE 802.1Qbb PFC pause frames on the interface for the
configured packet priorities. This can be useful for implementing
asymmetric PFC when it is desired to configure this only in the
transmit direction.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

79

Parameter

<PRIORITY-LIST>

Usage (flow control)

Description

(Applies to the 8325, 8360, 9300, 10000.) Specifies a comma-
separated list of packet priorities for which PFC will operate.
Range: 0 to 7. Up to seven priorities (two on the 8360) can be
specified in the list.

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

Usage (priority-based flow control (PFC)) (Not applicable to the 8320)

n PFC will only operate correctly between interfaces with the same priority configuration. Traffic flow

will not be lossless between interfaces with different priorities or between interfaces where one has
PFC enabled and the other does not.

n On the 8325, 9300, and 10000, PFC takes effect after the configuration is saved and the switch is

restarted.

n On the 8325, 9300, and 10000, lossless pools must be created before configuring flow control on any
interface. For PFC (when the PFC mode includes TX), any priority to be configured for PFC must be
mapped to a lossless pool before it can be enabled for PFC. For link-level flow control, lossless pool 1
will be used by default if no pool is specified when enabling flow control on the interface. If a pool is
specified when enabling flow control on an interface, the specified pool must be created first before
enabling flow control.

n Any queue used by protocol or control traffic must not be configured for lossless behavior. Routing
protocols and VSX-synchronization messages use local-priority 7, therefore the CoS priority mapped
to local-priority 7 should not be used in any lossless configuration.

For example, in a default configuration, the CoS map assigns local-priority 7 to packets arriving with
VLAN priority 7. This means that lossless pools should not be configured to use priority 7, and that
any flow-control priority mode should not be configured on priority 7, since that VLAN priority
maps to local-priority 7.

n On the 8325, 9300, and 10000, whatever lossless pool(s) will be used for link-level flow control must

be created before configuring link-level flow control RXTX mode on any interface. Otherwise, a
message similar to the following will be displayed:

Lossless pool 1 must be configured using the 'qos pool' command before enabling
RXTX flow control.

n On the 8325, 9300, and 10000, link-level flow control RXTX mode is not subject to auto-negotiation. It
is recommended to configure PFC or link-level flow control RXTX mode and pools only once on a

Interface configuration | 80

runningsystem.Changingthepoolorflowcontrolconfigurationonarunningsystemwillcausea
briefdisruptionintraffic.Thereconfigurationalsoresultsinpacketlossinthedataflow.Thismay
affectone,multiple,orallportsdependingontheexistingconfigurationandchangesmadetoit.
n Onthe8360,PFCtakeseffectimmediatelyafterconfiguration.
n Onthe8360JL720A,PFCisnotsupportedonanylinkspeedbelow10Gbps.
Onthe8325,9300,and10000:
YoucanonlyapplythreeuniquecombinationsofPFCpriorityconfigurationacrossallportsofaswitch.
Forexample:
| flow-control | priority | 3   |     |     |
| ------------ | -------- | --- | --- | --- |
| flow-control | priority | 4,5 |     |     |
| flow-control | priority | 4   |     |     |
Thefirstthreeuniquecombinationsconfiguredacrossallportssortedinnumericalorderareacceptedand
applied.Ifyouattempttoconfigureafourthuniqueprioritycombination,thefollowingerrormessageis
displayed:
The number of unique priority-based flow control (PFC) configuration combinations
| cannot | be more than | 3.  |     |     |
| ------ | ------------ | --- | --- | --- |
NotethatportswithaPFCconfigurationthatcannotbeappliedcanstilllinkupbuttheywillnothaveanyflow
control.
Examples
EnablingsupportforRXflowcontrol:
| switch(config)#    |     | interface    | 1/1/1 |     |
| ------------------ | --- | ------------ | ----- | --- |
| switch(config-if)# |     | flow-control |       | rx  |
DisablingsupportforRXflowcontrol:
| switch(config)#    |     | interface       | 1/1/1 |     |
| ------------------ | --- | --------------- | ----- | --- |
| switch(config-if)# |     | no flow-control |       | rx  |
(Appliestothe8325,8360,9300,10000.)EnablingsupportforRXTXflowcontrol:
| switch(config)#    |     | interface    | 1/1/1 |      |
| ------------------ | --- | ------------ | ----- | ---- |
| switch(config-if)# |     | flow-control |       | rxtx |
(Appliestothe8325,8360,9300,10000.)DisablingsupportforRXTXflowcontrol:
| switch(config)#    |     | interface       | 1/1/1 |      |
| ------------------ | --- | --------------- | ----- | ---- |
| switch(config-if)# |     | no flow-control |       | rxtx |
81
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

(Appliestothe8325,9300,10000.)EnablingsupportforRXTXflowcontrolwithpoolsetting:
| switch(config)#    | interface    | 1/1/1 |           |     |
| ------------------ | ------------ | ----- | --------- | --- |
| switch(config-if)# | flow-control |       | rxtx pool | 2   |
(Appliestothe8325,9300,10000.)DisablingsupportforRXTXwithpoolsetting:
| switch(config)#    | interface       | 1/1/1 |           |     |
| ------------------ | --------------- | ----- | --------- | --- |
| switch(config-if)# | no flow-control |       | rxtx pool | 2   |
(Appliestothe8325,9300,10000.)EnablingsupportforpriorityRXflowcontrol:
| switch(config)#    | interface    | 1/1/1 |          |        |
| ------------------ | ------------ | ----- | -------- | ------ |
| switch(config-if)# | flow-control |       | priority | rx 3,4 |
(Appliestothe8325,9300,10000.)DisablingsupportforpriorityRXflowcontrol:
| switch(config)#    | interface       | 1/1/1 |          |        |
| ------------------ | --------------- | ----- | -------- | ------ |
| switch(config-if)# | no flow-control |       | priority | rx 3,4 |
(Appliestothe8325,8360,9300,10000.)EnablingsupportforpriorityRXTXandRXflowcontrol:
switch(config)#
|                    | interface    | 1/1/1 |          |                     |
| ------------------ | ------------ | ----- | -------- | ------------------- |
| switch(config-if)# | flow-control |       | priority | rxtx 3 rx 1,2,4,5,6 |
(Appliestothe8325,8360,9300,10000.)DisablingsupportforpriorityRXTXandRXflowcontrol:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)# no flow-control priority rxtx 3 rx 1,2,4,5,6
(Appliestothe8325,9300,10000.)EnablingsupportforpriorityTXflowcontrol:
| switch(config)#    | interface    | 1/1/1 |          |        |
| ------------------ | ------------ | ----- | -------- | ------ |
| switch(config-if)# | flow-control |       | priority | tx 3,4 |
(Appliestothe8325,9300,10000.)DisablingsupportforpriorityTXflowcontrol:
| switch(config)#    | interface       | 1/1/1 |          |        |
| ------------------ | --------------- | ----- | -------- | ------ |
| switch(config-if)# | no flow-control |       | priority | tx 3,4 |
(Appliestothe8325,8360,9300,10000.)EnablingsupportforpriorityRXTX,RX,andTXflowcontrol:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)# flow-control priority rxtx 3 rx 1,2,4 tx 5,6
Interfaceconfiguration|82

(Appliestothe8325,8360,9300,10000.)DisablingsupportforpriorityRXTX,RX,andTXflowcontrol:
| switch(config)# |     | interface | 1/1/1 |     |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)# no flow-control priority rxtx 3 rx 1,2,4 tx 5,6
| Command | History |     |     |                                                |     |     |     |
| ------- | ------- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| Release |         |     |     | Modification                                   |     |     |     |
| 10.10   |         |     |     | Adjustedtheprioritysyntax.AddedseparateRXandTX |     |     |     |
configurationforasymmetricPFC.Addedthepoolparameter.
| 10.09          |             |     |         | Supportforrxtxaddedto8325SwitchSeries.      |     |     |     |
| -------------- | ----------- | --- | ------- | ------------------------------------------- | --- | --- | --- |
| 10.08          |             |     |         | CommandenhancedtoconfiguretwoPFCpriorities. |     |     |     |
| 10.07orearlier |             |     |         | --                                          |     |     |     |
| Command        | Information |     |         |                                             |     |     |     |
| Platforms      | Command     |     | context | Authority                                   |     |     |     |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| flow-control |     | buffer | headroom |     |     |     |     |
| ------------ | --- | ------ | -------- | --- | --- | --- | --- |
flow-control buffer priority <PRIORITY> headroom <LIMIT> kbytes
| flow-control | buffer | llfc | headroom | <LIMIT> | kbytes |     |     |
| ------------ | ------ | ---- | -------- | ------- | ------ | --- | --- |
no flow-control buffer priority <PRIORITY> headroom <LIMIT> kbytes
| no flow-control |     | buffer | llfc headroom | <LIMIT> | kbytes |     |     |
| --------------- | --- | ------ | ------------- | ------- | ------ | --- | --- |
Description
Allowsuserconfigurationofper-priorityorLLFCRXTXheadroomlimitonaphysicalinterface.
Thenoformofthecommandresetsthelimittothedefaultvalue.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
priority <PRIORITY> Configuresbufferparametersforpriorityflowcontrol.Range:0to
7.
| llfc |     |     |     | Configuresbufferparametersforlink-levelflowcontrol. |     |     |     |
| ---- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
headroom <LIMIT> Specifiesthemaximumamountofheadroompoolbufferspace
thatisallowedtobeusedforin-flightpacketsthatarriveafter
flow-controlXOFFisasserted.Range:18to10240kilobytes.
Examples
Configuringaheadroomlimitof36kbytesforPFCpriority4traffic:
| switch(config)# |     | interface | 1/1/1 |     |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)#
|     |     |     | flow-control | buffer | priority | 4 headroom | 36 kbytes |
| --- | --- | --- | ------------ | ------ | -------- | ---------- | --------- |
83
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |

Configuringaheadroomlimitof36kbytesforLLFCRXTXtraffic:
| switch(config)#    |     | interface |              | 1/1/1 |             |          |     |           |
| ------------------ | --- | --------- | ------------ | ----- | ----------- | -------- | --- | --------- |
| switch(config-if)# |     |           | flow-control |       | buffer llfc | headroom |     | 36 kbytes |
Resettingtheheadroomlimittodefaultvalue:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- | --- |
switch(config-if)# no flow-control buffer priority 4 headroom 36 kbytes
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- | --- |
switch(config-if)# no flow-control buffer llfc headroom 36 kbytes
| Command   | History     |     |         |     |                                    |     |     |     |
| --------- | ----------- | --- | ------- | --- | ---------------------------------- | --- | --- | --- |
| Release   |             |     |         |     | Modification                       |     |     |     |
| 10.11     |             |     |         |     | Addedsupportfor9300seriesswitches. |     |     |     |
| 10.10     |             |     |         |     | CommandIntroduced.                 |     |     |     |
| Command   | Information |     |         |     |                                    |     |     |     |
| Platforms | Command     |     | context |     | Authority                          |     |     |     |
config-if
8325 Administratorsorlocalusergroupmemberswithexecutionrights
| 9300 |     |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- | --- |
10000
| flow-control |        | buffer   | xoff | dynamic    |         |         |         |     |
| ------------ | ------ | -------- | ---- | ---------- | ------- | ------- | ------- | --- |
| flow-control | buffer | priority |      | <PRIORITY> | xoff    | dynamic | <ALPHA> |     |
| flow-control | buffer | llfc     | xoff | dynamic    | <ALPHA> |         |         |     |
no flow-control buffer priority <PRIORITY> xoff dynamic <ALPHA>
| no flow-control |     | buffer | llfc | xoff dynamic | <ALPHA> |     |     |     |
| --------------- | --- | ------ | ---- | ------------ | ------- | --- | --- | --- |
Description
Allowsuserconfigurationofper-priorityorLLFCRXTXdynamicXOFFlimitsonaphysicalinterface.
Thenoformofthecommandresetsthethresholdtothedefaultvalue.
| Parameter |            |     |     |     | Description |     |     |     |
| --------- | ---------- | --- | --- | --- | ----------- | --- | --- | --- |
| priority  | <PRIORITY> |     |     |     |             |     |     |     |
Configuresbufferparametersforpriorityflowcontrol.Range:0to
7.
| llfc |     |     |     |     | Configuresbufferparametersforlink-levelflowcontrol. |     |     |     |
| ---- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
<ALPHA>
Specifiesthescalefactorusedtocomputetheinstantaneous
bufferlimitbasedontheinstantaneousfreespace.Range:-7to3.
Examples
Interfaceconfiguration|84

ConfiguringthedynamicXOFFlimitof-3foringressPFCpriority5traffic:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
switch(config-if)# flow-control buffer priority 5 xoff dynamic -3
ConfiguringthedynamicXOFFlimitof-3foringresstrafficonanLLFCRXTXport:
| switch(config)#    |     | interface |              | 1/1/1 |             |              |     |
| ------------------ | --- | --------- | ------------ | ----- | ----------- | ------------ | --- |
| switch(config-if)# |     |           | flow-control |       | buffer llfc | xoff dynamic | -3  |
Resettingthexoffdynamiclimittothedefault:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
switch(config-if)# no flow-control buffer priority 5 xoff dynamic
| switch(config)#    |             | interface |                 | 1/1/1 |                                    |                   |     |
| ------------------ | ----------- | --------- | --------------- | ----- | ---------------------------------- | ----------------- | --- |
| switch(config-if)# |             |           | no flow-control |       | buffer                             | llfc xoff dynamic |     |
| Command            | History     |           |                 |       |                                    |                   |     |
| Release            |             |           |                 |       | Modification                       |                   |     |
| 10.11              |             |           |                 |       | Addedsupportfor9300seriesswitches. |                   |     |
| 10.10              |             |           |                 |       | CommandIntroduced.                 |                   |     |
| Command            | Information |           |                 |       |                                    |                   |     |
| Platforms          | Command     |           | context         |       | Authority                          |                   |     |
8325 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 9300 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
10000
| flow-control |     | buffer | xoff | static |     |     |     |
| ------------ | --- | ------ | ---- | ------ | --- | --- | --- |
flow-control buffer priority <PRIORITY> xoff static <LIMIT> kbytes
| flow-control | buffer | llfc | xoff | static | <LIMIT> | kbytes |     |
| ------------ | ------ | ---- | ---- | ------ | ------- | ------ | --- |
no flow-control buffer priority <PRIORITY> xoff static <LIMIT> kbytes
| no flow-control |     | buffer | llfc | xoff static | <LIMIT> | kbytes |     |
| --------------- | --- | ------ | ---- | ----------- | ------- | ------ | --- |
Description
Allowsuserconfigurationofper-priorityorLLFCRXTXstaticXOFFlimitsonaphysicalinterface.
Thenoformresetsthethresholdtothedefaultvalue.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
priority <PRIORITY> Configuresbufferparametersforpriorityflowcontrol.Range:0to
7.
85
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |

| Parameter |     |     |     |     | Description                                         |     |     |
| --------- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- |
| llfc      |     |     |     |     | Configuresbufferparametersforlink-levelflowcontrol. |     |     |
<LIMIT> Specifiestheabsolutelimitprogrammedfortheportorpriority.
Whenthein-useamountreachesthislimit,theXOFFisasserted.
Range:36to20000kilobyteson8325and10000seriesswitches.
Range:36to40000kilobyteson9300seriesswitches.
Examples
ConfiguringtheXOFFstaticlimitof128kbytesforPFCpriority6traffic:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
switch(config-if)# flow-control buffer priority 6 xoff static 128 kbytes
ConfiguringtheXOFFstaticlimitof128kbytesforLLFCRXTXtraffic:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
switch(config-if)# flow-control buffer llfc xoff static 128 kbytes
Resettingthexoffstaticlimittothedefault:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
switch(config-if)# no flow-control buffer priority 6 xoff static
| switch(config)#    |             | interface |                 | 1/1/1 |                                    |      |             |
| ------------------ | ----------- | --------- | --------------- | ----- | ---------------------------------- | ---- | ----------- |
| switch(config-if)# |             |           | no flow-control |       | buffer                             | llfc | xoff static |
| Command            | History     |           |                 |       |                                    |      |             |
| Release            |             |           |                 |       | Modification                       |      |             |
| 10.11              |             |           |                 |       | Addedsupportfor9300seriesswitches. |      |             |
| 10.10              |             |           |                 |       | CommandIntroduced.                 |      |             |
| Command            | Information |           |                 |       |                                    |      |             |
| Platforms          | Command     |           | context         |       | Authority                          |      |             |
config-if
8325 Administratorsorlocalusergroupmemberswithexecutionrights
| 9300 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
10000
| flow-control    |        | buffer   | xon      |            |        |             |                |
| --------------- | ------ | -------- | -------- | ---------- | ------ | ----------- | -------------- |
| flow-control    | buffer | priority |          | <PRIORITY> |        | xon <VALUE> | kbytes         |
| flow-control    | buffer | llfc     | xon      | <VALUE>    | kbytes |             |                |
| no flow-control |        | buffer   | priority | <PRIORITY> |        | xon         | <VALUE> kbytes |
| no flow-control |        | buffer   | llfc xon | <VALUE>    |        | kbytes      |                |
Interfaceconfiguration|86

Description
Allowsuserconfigurationofper-priorityorLLFCRXTXdynamicXON deltaonaphysicalinterface.
ThenoformofthecommandresetstheXONdeltatothedefaultvalue.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
priority <PRIORITY> Configuresbufferparametersforpriorityflowcontrol.Range:0to
7.
| llfc    |     |     |     | Configuresbufferparametersforlink-levelflowcontrol. |     |
| ------- | --- | --- | --- | --------------------------------------------------- | --- |
| <VALUE> |     |     |     | SpecifiestheoffsetvaluebelowtheXOFFlimitwhereXONis  |     |
assertedandpackettransmissionresumes.
Range:1to20000kilobyteson8300and10000seriesswitches.
Range:1to40000kilobyteson9300seriesswitches.
Examples
ConfiguringtheXONdeltaof24kbytesforPFCpriority4traffic:
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# flow-control buffer priority 4 xon 24 kbytes
ConfiguringtheXONdeltaof24kbytesforLLFCRXTXtraffic:
| switch(config)#    |     | interface    | 1/1/1 |             |               |
| ------------------ | --- | ------------ | ----- | ----------- | ------------- |
| switch(config-if)# |     | flow-control |       | buffer llfc | xon 24 kbytes |
Resettingthexondeltatothedefaultvalue:
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# no flow-control buffer priority 4 xon 24 kbytes
| switch(config)#     |         | interface       | 1/1/1 |                                    |                    |
| ------------------- | ------- | --------------- | ----- | ---------------------------------- | ------------------ |
| switch(config-if)#  |         | no flow-control |       | buffer                             | llfc xon 24 kbytes |
| Command History     |         |                 |       |                                    |                    |
| Release             |         |                 |       | Modification                       |                    |
| 10.11               |         |                 |       | Addedsupportfor9300seriesswitches. |                    |
| 10.10               |         |                 |       | CommandIntroduced.                 |                    |
| Command Information |         |                 |       |                                    |                    |
| Platforms           | Command | context         |       | Authority                          |                    |
8325 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 9300 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
10000
87
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| flow-control          | watchdog |     |     |
| --------------------- | -------- | --- | --- |
| flow-control watchdog |          |     |     |
| no flow-control       | watchdog |     |     |
Description
Enablesflowcontrolwatchdogonaphysicalinterface.
Whenanexcessiveamountoflosslesstrafficstopstransmitting,problematiclosslessbuffercongestion
occursthroughoutthenetwork.Topreventthesituation,egresslosslessqueuesaremonitoredto
detectwhennotransmissionshaveoccurredforagloballyspecifieddetectiontimeout.Whenthe
conditionisdetected,theflowcontrolwatchdogtriggersontheaffectedqueueresultinginthe
followingactions:
n Thewatchdogtimeoutcounterontheinterfaceisincremented.
n Allpacketsoccupyingtheaffectedqueuearediscarded.
n Newpacketarrivalsdestinedfortheaffectedqueuearediscarded.
Aftertheconfiguredresumeintervalhaselapsedsincethetrigger,thequeueisreturnedtonormal
operation.
Thenoformofthiscommanddisablesflowcontrolwatchdogonaphysicalinterface.
FlowcontrolwatchdogisonlysupportedoninterfacesconfiguredwithPFC.Link-levelflowcontrolisnot
compatiblewithflowcontrolwatchdog.
Whenflowcontrolwatchdogisenabled,itisactiveonalllosslessqueuesoftheport.
Todeterminewhethertheflowcontrolwatchdogisenabledonaninterface,ortoseethenumberoftimesthe
watchdoghasbeentriggered,usetheshow interface flow-controlcommand.
Thedetectionandresumeintervalsmustbeconfiguredfromtheglobalconfigurationcontext.
Examples
Enablingflowcontrolwatchonaninterface:
| switch(config)#    | interface    | 1/1/1 |          |
| ------------------ | ------------ | ----- | -------- |
| switch(config-if)# | flow-control |       | watchdog |
Disablingflowcontrolwatchonaninterface:
| switch(config)#    | interface       | 1/1/1 |          |
| ------------------ | --------------- | ----- | -------- |
| switch(config-if)# | no flow-control |       | watchdog |
Command History
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
Command Information
Interfaceconfiguration|88

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
8325 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 9300 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
10000
| flow-control | watchdog |     | timeout | resume |     |     |
| ------------ | -------- | --- | ------- | ------ | --- | --- |
flow-control watchdog timeout <MILLISECONDS> resume <MILLISECONDS>
no flow-control watchdog timeout <MILLISECONDS> resume <MILLISECONDS>
Description
Configuresglobalflowcontrolwatchdogparameters,detectiontimeandresumetime.Theparameters
areappliedtoallinterfacesthathaveflowcontrolwatchdogenabledwithcommandflow-control
watchdog.
Thenoformofthiscommandclearstheglobalconfigurationparametersforflowcontrolwatchdog,
restoringtimeoutandresumetimetotheplatformdefaults.
Flowcontrolwatchdogmustbeenabledonspecifiedinterfaces.
Theconfiguredtimingparametersareroundedtowhatthehardwaresupports.Usecommandshow flow
controltoshowtheappliedvalues.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
timeout <MILLISECONDS> Specifiestheamountoftimeinmilliseconds,thataqueuemust
bepausedforwatchdogtotrigger.Range:10to1500
milliseconds.Default:100milliseconds.
| resume <MILLISECONDS> |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
Specifiesthedurationoftimeinmilliseconds,thataqueue
remainsinthetriggeredstate.Range:1to100000milliseconds.
Default:100milliseconds.
Examples
Configuringflowcontrolwatchdogglobalparameters:
| switch(config)# | flow-control |     | watchdog | timeout | 100 resume | 60  |
| --------------- | ------------ | --- | -------- | ------- | ---------- | --- |
Removingflowcontrolwatchdogglobalparameters:
| switch(config)#     | no  | flow-control |     | watchdog timeout  | 100 resume | 60  |
| ------------------- | --- | ------------ | --- | ----------------- | ---------- | --- |
| Command History     |     |              |     |                   |            |     |
| Release             |     |              |     | Modification      |            |     |
| 10.08               |     |              |     | Commandintroduced |            |     |
| Command Information |     |              |     |                   |            |     |
89
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8325 config Administratorsorlocalusergroupmemberswithexecutionrights
| 9300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
10000
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Interfaceconfiguration|90

Examples
| switch#         | config    |          |     |
| --------------- | --------- | -------- | --- |
| switch(config)# | interface | loopback | 1   |
switch(config-loopback-if)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
9300
10000
| interface      | vlan           |     |     |
| -------------- | -------------- | --- | --- |
| interface vlan | <VLAN-ID>      |     |     |
| no interface   | vlan <VLAN-ID> |     |     |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-
if-vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
| Parameter |     |     | Description                      |
| --------- | --- | --- | -------------------------------- |
| <VLAN-ID> |     |     | SpecifiestheloopbackinterfaceID. |
| none      |     |     | DonotreserveanyinternalVLANs.    |
Examples
| switch#                 | config    |      |     |
| ----------------------- | --------- | ---- | --- |
| switch(config)#         | vlan      | 10   |     |
| switch(config-vlan-10)# |           | exit |     |
| switch(config)#         | interface | vlan | 10  |
switch(config-if-vlan)#
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
| 10.07orearlier  |     |     | --           |
91
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Command   | Information |     |         |     |           |     |
| --------- | ----------- | --- | ------- | --- | --------- | --- |
| Platforms | Command     |     | context |     | Authority |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip address
| ip address    | <IPV4-ADDR>/<MASK> |     |     | [secondary] |             |     |
| ------------- | ------------------ | --- | --- | ----------- | ----------- | --- |
| no ip address | <IPV4-ADDR>/<MASK> |     |     |             | [secondary] |     |
Description
SetsanIPv4addressforthecurrentlayer3interface.
ThenoformofthiscommandremovestheIPv4addressfromtheinterface.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
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
| switch(config)#         |     | interface |     | vlan       | 10               |     |
| ----------------------- | --- | --------- | --- | ---------- | ---------------- | --- |
| switch(config-if-vlan)# |     |           |     | ip address | 192.168.199.1/24 |     |
RemovingtheIPaddress192.168.199.1withamaskof24bitsfrominterfaceVLAN10:
Interfaceconfiguration|92

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
besentorreceivedbytheinterface.ThisvalueshouldbelessthanorequaltotheoverallMTUforthe
interface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.Thiscommandisonlyallowed
whenroutingisenabledontheinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE> SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
SettingtheIPMTUto576bytes:
| switch(config-if)# |     | ip mtu 576 |     |
| ------------------ | --- | ---------- | --- |
SettingtheIPMTUtothedefaultvalue:
| switch(config-if)# |     | no ip mtu |     |
| ------------------ | --- | --------- | --- |
SettingtheIPMTUvalueonasubinterface:
| switch(config)# | interface | 1/1/1.10 |     |
| --------------- | --------- | -------- | --- |
switch(config-subif)#
ip mtu 6000
Usage
93
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

TheIP MTUvalueforsubinterfacemustbelessthanorequaltotheparentMTUforthesubinterface.
ThesubinterfaceusesitsIPMTUvalueandnottheparentIPMTUvalue.
| Command History     |         |         |                           |
| ------------------- | ------- | ------- | ------------------------- |
| Release             |         |         | Modification              |
| 10.08               |         |         | Subinterfacesupportadded. |
| 10.07orearlier      |         |         | --                        |
| Command Information |         |         |                           |
| Platforms           | Command | context | Authority                 |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |
| --- | -------------- | --- | --------------- |
config-subif
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
Interfaceconfiguration|94

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedservice.
TheIPaddressmustbedefinedontheswitch,anditmustexist
onthespecifiedVRF(whichisthedefaultVRF,ifthevrfoption
isnotused).SpecifytheaddressinIPv4format(x.x.x.x),where
xisadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |     |
| -------------- | --- | --- | ----------------------- | --- |
Examples
SettingtheIPv4address10.10.10.5astheglobalsinglesourceaddress:
switch# config
| switch(config)# | ip source-interface |     | all 10.10.10.5 |     |
| --------------- | ------------------- | --- | -------------- | --- |
SettingthesecondaryIPv4address10.10.10.5oninterface1/1/1astheglobalsinglesourceaddress:
switch# config
| switch(config)#    | interface           | 1/1/1         |                |           |
| ------------------ | ------------------- | ------------- | -------------- | --------- |
| switch(config-if)# | ip address          | 10.10.10.1/24 |                |           |
| switch(config-if)# | ip address          | 10.10.10.5/24 |                | secondary |
| switch(config)#    | exit                |               |                |           |
| switch(config)#    | ip source-interface |               | all 10.10.10.5 |           |
Settingtheaddress10.10.10.25onVRFsflow-vrfoninterface1/1/2asthesinglesourceaddressfor
sFlow:
| switch(config)#     | vrf sflow-vrf |                  |     |     |
| ------------------- | ------------- | ---------------- | --- | --- |
| switch(config-vrf)# | exit          |                  |     |     |
| switch(config)#     | interface     | 1/1/2            |     |     |
| switch(config-if)#  | no shutdown   |                  |     |     |
| switch(config-if)#  | vrf           | attach sflow-vrf |     |     |
| switch(config-if)#  | ip address    | 10.10.10.25/24   |     |     |
| switch(config-if)#  | exit          |                  |     |     |
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)# | no ip source-interface |     | all | 10.10.10.5 |
| --------------- | ---------------------- | --- | --- | ---------- |
Command History
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
Command Information
95
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK>{eui64 |     | | [tag <ID>]} |
| --------------- | ------------------------ | --- | ------------- |
| no ipv6 address | <IPV6-ADDR>/<MASK>       |     |               |
Description
SetsanIPv6addressontheinterface.
ThenoformofthiscommandremovestheIPv6addressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-
localaddressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6 address
link-localcommand.
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
| eui64 |     |     | ConfiguretheIPv6addressintheEUI-64bitformat. |
| ----- | --- | --- | -------------------------------------------- |
tag <ID>
Configureroutetagforconnectedroutes.Range:0to
4294967295.Default:0.
Examples
SettingtheIPv6address2001:0db8:85a3::8a2e:0370:7334withamaskof24bits:
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
RemovingtheIPaddress2001:0db8:85a3::8a2e:0370:7334withmaskof24bits:
switch(config-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
| Command | History |     |     |
| ------- | ------- | --- | --- |
Interfaceconfiguration|96

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 source-interface
ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay
| simplivity | dns | all} {interface <IFNAME> | <IPV6-ADDR>} [vrf <VRF-NAME>]
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | SetsasinglesourceIPaddressforaspecificprotocol.Theall
ntp | syslog | ubt | dhcp-relay | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
| simplivity | | dns | | all | nothaveanaddressset. |
| ---------- | ----- | ----- | -------------------- |
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
| switch#         | config |                     |                    |
| --------------- | ------ | ------------------- | ------------------ |
| switch(config)# |        | ip source-interface | all 2001:DB8::1/32 |
97
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

ConfiguringtheIPv6address2001:DB8::1onVRFsflow-vrfoninterface1/1/2asthesinglesource
addressforsFlow:
| switch(config)#     |     | vrf sflow-vrf |         |                |     |
| ------------------- | --- | ------------- | ------- | -------------- | --- |
| switch(config-vrf)# |     | exit          |         |                |     |
| switch(config)#     |     | interface     | 1/1/2   |                |     |
| switch(config-if)#  |     | no shutdown   |         |                |     |
| switch(config-if)#  |     | vrf           | attach  | sflow-vrf      |     |
| switch(config-if)#  |     | ipv6          | address | 2001:DB8::1/32 |     |
| switch(config-if)#  |     | exit          |         |                |     |
switch(config)# ip source-interface sflow interface 1/1/2 vrf sflow-vrf
StopthesourceIPaddressfromusingtheIPaddressoninterface1/1/1onVRFone.
switch(config)# no ip source-interface all interface 1/1/1 vrf one
ClearthesourceIPaddress2001:DB8::1.
| switch(config)#     |         | no ip source-interface |     |              | all 2001:DB8::1 |
| ------------------- | ------- | ---------------------- | --- | ------------ | --------------- |
| Command History     |         |                        |     |              |                 |
| Release             |         |                        |     | Modification |                 |
| 10.07orearlier      |         |                        |     | --           |                 |
| Command Information |         |                        |     |              |                 |
| Platforms           | Command | context                |     | Authority    |                 |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
l3-counters
| l3-counters    | [rx | tx] |       |     |     |     |
| -------------- | --------- | ----- | --- | --- | --- |
| no l3-counters | [rx       | | tx] |     |     |     |
Description
Enablescountersonalayer3interface.Bydefault,allinterfacesarelayer3.Tochangealayer2
interfacetolayer3,usetheroutingcommand.
Thenoformofthiscommand,withnospecification,disablesbothtransmitandreceivecountersona
layer3interface.Todisabletransmit(tx)orreceive(rx)countersonly,specifythecountertypeyou
wanttodisable.
| Parameter |     |     |     | Description                |     |
| --------- | --- | --- | --- | -------------------------- | --- |
| rx        |     |     |     | Specifiesreceivecounters.  |     |
| tx        |     |     |     | Specifiestransmitcounters. |     |
Interfaceconfiguration|98

Examples
Enablinglayer3transmitcountersoninterface1/1/1:
switch(config)#
|                    |     | interface   | 1/1/1 |     |     |
| ------------------ | --- | ----------- | ----- | --- | --- |
| switch(config-if)# |     | l3-counters |       | tx  |     |
Disablinglayer3transmitandreceivecountersoninterface1/1/2:
| switch(config)#    |     | interface      | 1/1/2 |     |     |
| ------------------ | --- | -------------- | ----- | --- | --- |
| switch(config-if)# |     | no l3-counters |       |     |     |
Layer3countersonsubinterfacesareonlysupportedontheAruba8360switchseries.
Enablinglayer3countersonsubinterface1/1/1.10:
| switch(config)#       |     | interface   | 1/1/1.10 |     |     |
| --------------------- | --- | ----------- | -------- | --- | --- |
| switch(config-subif)# |     | l3-counters |          |     |     |
Disablinglayer3countersonsubinterface1/1/1.10:
| switch(config)#       |     | interface | 1/1/1.10    |     |     |
| --------------------- | --- | --------- | ----------- | --- | --- |
| switch(config-subif)# |     | no        | l3-counters |     |     |
Enablinglayer3receivecountersonsubinterface1/1/1.10:
| switch(config)#       |     | interface   | 1/1/1.10 |     |     |
| --------------------- | --- | ----------- | -------- | --- | --- |
| switch(config-subif)# |     | l3-counters |          |     | rx  |
Disablinglayer3transmitcountersonsubinterface1/1/1.10:
| switch(config)#       |         | interface | 1/1/1.10    |     |                                          |
| --------------------- | ------- | --------- | ----------- | --- | ---------------------------------------- |
| switch(config-subif)# |         | no        | l3-counters |     | tx                                       |
| Command History       |         |           |             |     |                                          |
| Release               |         |           |             |     | Modification                             |
| 10.08                 |         |           |             |     | Addedsupportfor13countersonsubinterfaces |
| 10.07orearlier        |         |           |             |     | --                                       |
| Command Information   |         |           |             |     |                                          |
| Platforms             | Command | context   |             |     | Authority                                |
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-subif |     |     |     | forthiscommand. |
| ---- | ------------ | --- | --- | --- | --------------- |
99
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8360
9300
10000
mtu
mtu <VALUE>
no mtu
Description
SetstheMTU(maximumtransmissionunit)foraninterface.Thisdefinesthemaximumsizeofalayer2
(Ethernet)frame.FrameslargerthantheMTU(1500bytesbydefault)aredroppedandcauseanICMP
fragmentation-neededmessagetobesentbacktotheoriginator.
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
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Interfaceconfiguration|100

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

101

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
Interfaceconfiguration|102

| Release             |         |         | Modification                         |
| ------------------- | ------- | ------- | ------------------------------------ |
| 10.10               |         |         | Addedoptionalparameters:attach,copy. |
| 10.09               |         |         | Commandintroduced.                   |
| Command Information |         |         |                                      |
| Platforms           | Command | context | Authority                            |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
9300
10000
show allow-unsupported-transceiver
103
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

show allow-unsupported-transceiver
Description
Displaysconfigurationandstatusofunsupportedtransceivers.
Examples
Showingunallowedunsupportedtransceivers:
| switch(config)#   |          | show         | allow-unsupported-transceiver |     |                |
| ----------------- | -------- | ------------ | ----------------------------- | --- | -------------- |
| Allow unsupported |          | transceivers |                               |     | : no           |
| Logging           | interval |              |                               |     | : 1440 minutes |
---------------------------------------------
| Port | Type |     |     | Status |     |
| ---- | ---- | --- | --- | ------ | --- |
---------------------------------------------
| 1/1/31 | SFP-SX     |     |     | unsupported |     |
| ------ | ---------- | --- | --- | ----------- | --- |
| 1/1/32 | SFP-1G-BXD |     |     | unsupported |     |
| 1/1/2  | SFP28DAC3  |     |     | unsupported |     |
Showingallowedunsupportedtransceivers:
| switch#           | show allow-unsupported-transceiver |              |     |     |                |
| ----------------- | ---------------------------------- | ------------ | --- | --- | -------------- |
| Allow unsupported |                                    | transceivers |     |     | : yes          |
| Logging           | interval                           |              |     |     | : 1440 minutes |
---------------------------------------------
| Port | Type |     |     | Status |     |
| ---- | ---- | --- | --- | ------ | --- |
---------------------------------------------
| 1/1/31         | SFP-SX      |     |         | unsupported-allowed |              |
| -------------- | ----------- | --- | ------- | ------------------- | ------------ |
| 1/1/32         | SFP-1G-BXD  |     |         | unsupported-allowed |              |
| 1/1/2          | SFP28DAC3   |     |         | unsupported         |              |
| Command        | History     |     |         |                     |              |
| Release        |             |     |         |                     | Modification |
| 10.07orearlier |             |     |         |                     | --           |
| Command        | Information |     |         |                     |              |
| Platforms      | Command     |     | context |                     | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface |                       |     |     |     |                    |
| -------------- | --------------------- | --- | --- | --- | ------------------ |
| show interface | [<IFNNAME>|<IFRANGE>] |     |     |     | [brief | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] |     | monitor |     | [human-readable] |
| -------------- | ----------- | --- | ------- | --- | ---------------- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief]
show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]
| show interface | lag   | [<LAG-ID>] |     | monitor | [human-readable] |
| -------------- | ----- | ---------- | --- | ------- | ---------------- |
| show interface | vxlan | <VXLAN-ID> |     | [brief  | | physical]      |
Interfaceconfiguration|104

| show interface | vxlan <VXLAN-ID> | [brief | | physical] |     |
| -------------- | ---------------- | ------ | ----------- | --- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     | Description                                    |     |     |
| --------- | --- | ---------------------------------------------- | --- | --- |
| <IFNAME>  |     | Specifiesainterfacename.                       |     |     |
| <IFRANGE> |     | Specifiestheportidentifierrange.               |     |     |
| brief     |     | Showsbriefinfointabularformat.                 |     |     |
| physical  |     | Showsthephysicalconnectioninfointabularformat. |     |     |
| extended  |     | Showsadditionalstatistics.                     |     |     |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
non-zero
Showsonlynonzerostatistics.
| LAG |     | ShowsLAGinterfaceinformation. |     |     |
| --- | --- | ----------------------------- | --- | --- |
monitor
Continuouslymonitorinterfacestatistics.
| LOOPBACK |     | Showsloopbackinterfaceinformation. |     |     |
| -------- | --- | ---------------------------------- | --- | --- |
TUNNEL
Showstunnelinterfaceinformation.
| VLAN |     | ShowsVLANinterfaceinformation. |     |     |
| ---- | --- | ------------------------------ | --- | --- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
| <LOOPBACK-ID> |     | SpecifiestheLOOPBACKnumber.Range:0-255 |     |     |
| ------------- | --- | -------------------------------------- | --- | --- |
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
| <VLAN-ID> |     | SpecifiestheVLANID.Range:1-4094 |     |     |
| --------- | --- | ------------------------------- | --- | --- |
VXLAN
ShowstheVXLANinterfaceinformation.
| <VXLAN-ID> |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |
| ---------- | --- | ---------------------------------------------- | --- | --- |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport(thepersonaitemisonly
availableonthe10000SwitchSeries):
| switch#           | show interface | 1/1/1             |                 |           |
| ----------------- | -------------- | ----------------- | --------------- | --------- |
| Interface         | 1/1/1 is up    |                   |                 |           |
| Admin state       | is up          |                   |                 |           |
| Link state:       | up for         | 2 days (since Sun | Jun 21 05:30:22 | UTC 2020) |
| Link transitions: | 1              |                   |                 |           |
| Description:      | backup         | data center link  |                 |           |
| Persona:          | access         |                   |                 |           |
105
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Hardware: | Ethernet, | MAC | Address: | 70:72:cf:fd:e7:b4 |     |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |         |     |     |       |         |
| ---------------- | ---- | ----------- | --- | ------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |         |     |     |       |         |
| Auto-negotiation |      | is on       |     |         |     |     |       |         |
| Flow-control:    |      | off         |     |         |     |     |       |         |
| Error-control:   |      | off         |     |         |     |     |       |         |
| MDI mode:        | MDIX |             |     |         |     |     |       |         |
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
| switch(config-if)# |       | show  | interface | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |       |     |     |     |     |
...
| Auto-negotiation |     | is on | with | downshift | active |     |     |     |
| ---------------- | --- | ----- | ---- | --------- | ------ | --- | --- | --- |
ShowinginformationwhentheinterfaceisshutdownduringaVSX split(thepersonaitemisonly
availableonthe10000SwitchSeries):
| switch(config-if)# |       | show     | interface | 1/1/1  |     |     |     |     |
| ------------------ | ----- | -------- | --------- | ------ | --- | --- | --- | --- |
| Interface          | 1/1/1 | is down  |           |        |     |     |     |     |
| Admin state        | is    | up       |           |        |     |     |     |     |
| State information: |       | Disabled |           | by VSX |     |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
Interfaceconfiguration|106

| Link transitions: |     | 0   |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Persona:  | access    |     |          |                   |     |     |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- | --- |
| Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |     |     |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |                 |     |         |     |     |       |         |     |
| ---------------- | --------------- | --------------- | --- | ------- | --- | --- | ----- | ------- | --- |
| Speed 0          | Mb/s            |                 |     |         |     |     |       |         |     |
| Auto-negotiation |                 | is off          |     |         |     |     |       |         |     |
| Flow-control:    |                 | off             |     |         |     |     |       |         |     |
| Error-control:   |                 | off             |     |         |     |     |       |         |     |
| VLAN Mode:       | native-untagged |                 |     |         |     |     |       |         |     |
| Native           | VLAN:           | 1               |     |         |     |     |       |         |     |
| Allowed          | VLAN            | List: 1502-1505 |     |         |     |     |       |         |     |
| Rate collection  |                 | interval:       | 300 | seconds |     |     |       |         |     |
| Rate             |                 |                 |     | RX      |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| ----------- | --- | --- | --- | ---- | --- | ---- | --- | ----- | ---- |
| KPkts /     | sec |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Unicast     |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Multicast   |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Broadcast   |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Utilization |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Statistic   |     |     |     | RX   |     | TX   |     | Total |      |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 0   |     | 0   |     |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     | 0   |     | 0   |     |     | 0   |
| Multicast    |     |     |     | 0   |     | 0   |     |     | 0   |
| Broadcast    |     |     |     | 0   |     | 0   |     |     | 0   |
| Bytes        |     |     |     | 0   |     | 0   |     |     | 0   |
| Jumbos       |     |     |     | 0   |     | 0   |     |     | 0   |
| Dropped      |     |     |     | 0   |     | 0   |     |     | 0   |
| Pause Frames |     |     |     | 0   |     | 0   |     |     | 0   |
| Errors       |     |     |     | 0   |     | 0   |     |     | 0   |
| CRC/FCS      |     |     |     | 0   |     | n/a |     |     | 0   |
| Collision    |     |     |     | n/a |     | 0   |     |     | 0   |
| Runts        |     |     |     | 0   |     | n/a |     |     | 0   |
| Giants       |     |     |     | 0   |     | n/a |     |     | 0   |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| switch(config-if)# |       | show  | interface | 1/1/1 monitor |     |     |       |         |     |
| ------------------ | ----- | ----- | --------- | ------------- | --- | --- | ----- | ------- | --- |
| Interface          | 1/1/1 | is up |           |               |     |     |       |         |     |
| Rate               |       |       |           | RX            |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| MBits /     | sec |     |     | 30196.43 | 30196.43 |       |     | 60392.85  |      |
| ----------- | --- | --- | --- | -------- | -------- | ----- | --- | --------- | ---- |
| MPkts /     | sec |     |     | 58977.39 | 58977.40 |       |     | 117954.79 |      |
| Unicast     |     |     |     | 0.00     |          | 0.00  |     |           | 0.00 |
| Multicast   |     |     |     | 58977.39 | 58977.40 |       |     | 117954.79 |      |
| Broadcast   |     |     |     | 0.00     |          | 0.00  |     |           | 0.00 |
| Utilization | %   |     |     | 75.49    |          | 75.49 |     | 150.98    |      |
107
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Statistic |     |     |     | RX  |     | TX  | Total | (RX+TX) |
| --------- | --- | --- | --- | --- | --- | --- | ----- | ------- |
---------------- -------------------- -------------------- --------------------
| Packets   |                |            | 4756527649   |     | 4756527865   |     | 9513055514   |            |
| --------- | -------------- | ---------- | ------------ | --- | ------------ | --- | ------------ | ---------- |
| Unicast   |                |            |              | 0   |              | 0   |              | 0          |
| Multicast |                |            | 4756527649   |     | 4756527865   |     | 9513055514   |            |
| Broadcast |                |            |              | 2   |              | 0   |              | 2          |
| Bytes     |                |            | 304417778668 |     | 304417795428 |     | 608835574096 |            |
| Jumbos    |                |            |              | 0   |              | 0   |              | 0          |
| Dropped   |                |            |              | 0   | 19028847730  |     | 19028847730  |            |
| Pause     | Frames         |            |              | 0   |              | 0   |              | 0          |
| Errors    |                |            |              | 0   |              | 0   |              | 0          |
| CRC/FCS   |                |            |              | 0   |              | n/a |              | 0          |
|           |                |            |              |     |              |     | help:        | ?, quit: q |
| Help for  | Interface      | Monitor    |              |     |              |     |              |            |
| h Toggle  | human-readable |            | mode         |     |              |     |              |            |
| c Clear   | interface      | statistics |              |     |              |     |              |            |
| Does      | not apply      | to         | rates        |     |              |     |              |            |
| Arrows,   | PgUp, PgDn,    | Home,      | End          |     |              |     |              |            |
| Navigate  | interface      |            | statistics   |     |              |     |              |            |
Delay: 2
|     |     |     |     |     |     |     | help: | ?, quit: q |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsisbetween
zeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |       |         |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | ----- | ------- |
| Interface          | 1/1/1 | is up |           |                      |     |     |       |         |
| Rate               |       |       |           | RX                   |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Bits /      | sec |     |     | 3M  |     | 3M  |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts /      | sec |     |     | 316 |     | 316 |     | 633   |
| Unicast     |     |     |     | 319 |     | 319 |     | 638   |
| Multicast   |     |     |     | 0   |     | 0   |     | 0     |
| Broadcast   |     |     |     | 0   |     | 0   |     | 0     |
| Utilization | %   |     |     | < 1 |     | < 1 |     | < 1   |
| Statistic   |     |     |     | RX  |     | TX  |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets   |     |     |     | 577K |     | 577K |     | 1M  |
| --------- | --- | --- | --- | ---- | --- | ---- | --- | --- |
| Unicast   |     |     |     | 577K |     | 577K |     | 1M  |
| Multicast |     |     |     | 0    |     | 51   |     | 51  |
| Broadcast |     |     |     | 0    |     | 15   |     | 15  |
| Bytes     |     |     |     | 744M |     | 745M |     | 1G  |
| Jumbos    |     |     |     | 0    |     | 0    |     | 0   |
Interfaceconfiguration|108

| Dropped      |     |     | 0   | 0   | 0   |
| ------------ | --- | --- | --- | --- | --- |
| Filtered     |     |     | 0   | 0   | 0   |
| Pause Frames |     |     | 0   | 0   | 0   |
| Errors       |     |     | 0   | 0   | 0   |
| CRC/FCS      |     |     | 0   | n/a | 0   |
| Collision    |     |     | n/a | 0   | 0   |
| Runts        |     |     | 0   | n/a | 0   |
| Giants       |     |     | 0   | n/a | 0   |
...
| Command History |     |     |              |     |     |
| --------------- | --- | --- | ------------ | --- | --- |
| Release         |     |     | Modification |     |     |
10.11
Addedmonitorparameter.
| 10.10               |         |         | Addedhuman-readableparameter.                    |     |     |
| ------------------- | ------- | ------- | ------------------------------------------------ | --- | --- |
| 10.09               |         |         | Addedpersonainformationforthe10000 SwitchSeries. |     |     |
| 10.07orearlier      |         |         | --                                               |     |     |
| Command Information |         |         |                                                  |     |     |
| Platforms           | Command | context | Authority                                        |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface | dom              |     |                     |     |     |
| -------------- | ---------------- | --- | ------------------- | --- | --- |
| show interface | [<INTERFACE-ID>] | dom | [detail] [vsx-peer] |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+,QSFP+).
ThisinformationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter      |     |     | Description                                   |     |     |
| -------------- | --- | --- | --------------------------------------------- | --- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |
| detail         |     |     | Showdetailedinformation.                      |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
109
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| switch# | show interface | dom |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
Port Type Channel Temperature Voltage Tx Bias Rx Power Tx Power
|     |     | (Celsius) | (Volts) | (mA) | (mW/dBm) | (mW/dBm) |
| --- | --- | --------- | ------- | ---- | -------- | -------- |
----------------------------------------------------------------------------------
| 1/1/1               | SFP+SR   | 47.65   | 3.31         | 8.40 | 0.08, -10.96 | 0.63, -2.49 |
| ------------------- | -------- | ------- | ------------ | ---- | ------------ | ----------- |
| 1/1/2               | SFP+SR   | n/a     | n/a          | n/a  | n/a          | n/a         |
| 1/1/3               | SFP+DA3  | 42.10   | 3.24         | n/a  | n/a          | n/a         |
| 1/1/4               | QSFP+SR4 | 1 44.46 | 3.30         | 6.12 | 0.08, -10.96 | 0.63, -1.95 |
|                     |          | 2 44.46 | 3.30         | 6.04 | 0.08, -10.96 | 0.63, -2.00 |
|                     |          | 3 44.46 | 3.30         | 6.51 | 0.08, -10.96 | 0.60, -2.16 |
|                     |          | 4 44.46 | 3.30         | 6.19 | 0.08, -10.96 | 0.63, -1.94 |
| Command History     |          |         |              |      |              |             |
| Release             |          |         | Modification |      |              |             |
| 10.07orearlier      |          |         | --           |      |              |             |
| Command Information |          |         |              |      |              |             |
| Platforms           | Command  | context | Authority    |      |              |             |
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
Interfaceconfiguration|110

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
111
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

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
Interfaceconfiguration|112

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
113
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

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
Interfaceconfiguration|114

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
OperatorsorAdministratorsorlocalusergroupmemberswith
| Allplatforms | Operator(>)orManager |     |                                                       |
| ------------ | -------------------- | --- | ----------------------------------------------------- |
|              | (#)                  |     | executionrightsforthiscommand.Operatorscanexecutethis |
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
115
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Showing statistics of all interfaces in the human-readable format:

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

Showing monitor statistics:

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

Interface configuration | 116

Showingmonitorerrorstatisticsinhuman-readableformat:
| Command History |     |     |                       |
| --------------- | --- | --- | --------------------- |
| Release         |     |     | Modification          |
| 10.11           |     |     | Addedmoitorparameter. |
10.10
Addedhuman-readableparameter.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface | transceiver |     |     |
| -------------- | ----------- | --- | --- |
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations] [vsx-peer]
Description
117
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfor
differenttransceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPE
andthird-partytransceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskinthe
output.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
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
| Temperature | : 47.65C  |           |     |     |     |
| ----------- | --------- | --------- | --- | --- | --- |
| Voltage     | : 3.31V   |           |     |     |     |
| Tx Bias     | : 8.40mA  |           |     |     |     |
| Rx Power    | : 0.08mW, | -10.96dBm |     |     |     |
| Tx Power    | : 0.56mW, | -2.49dBm  |     |     |     |
| Recent      | Alarms :  |           |     |     |     |
Interfaceconfiguration|118

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
| 1       | 6.12           | 0.00, -inf | 0.63, -1.95 |     |     |
| ------- | -------------- | ---------- | ----------- | --- | --- |
| 2       | 6.04           | 0.00, -inf | 0.63, -2.00 |     |     |
| 3       | 6.51           | 0.00, -inf | 0.60, -2.16 |     |     |
| 4       | 6.19           | 0.00, -inf | 0.63, -1.94 |     |     |
| Recent  | Alarms :       |            |             |     |     |
| Channel | 1 :            |            |             |     |     |
| Rx      | power low      | alarm      |             |     |     |
| Rx      | power low      | warning    |             |     |     |
| Channel | 2 :            |            |             |     |     |
| Rx      | power low      | alarm      |             |     |     |
| Rx      | power low      | warning    |             |     |     |
| Channel | 3 :            |            |             |     |     |
| Rx      | power low      | alarm      |             |     |     |
| Rx      | power low      | warning    |             |     |     |
| Channel | 4 :            |            |             |     |     |
| Rx      | power low      | alarm      |             |     |     |
| Rx      | power low      | warning    |             |     |     |
| Recent  | Errors :       |            |             |     |     |
| Channel | 1 :            |            |             |     |     |
| Rx      | Loss of Signal |            |             |     |     |
| Channel | 2 :            |            |             |     |     |
| Rx      | Loss of Signal |            |             |     |     |
| Channel | 3 :            |            |             |     |     |
| Rx      | Loss of Signal |            |             |     |     |
119
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Channel     | 4 :               |                  |     |     |     |
| ----------- | ----------------- | ---------------- | --- | --- | --- |
|             | Rx Loss of Signal |                  |     |     |     |
| Transceiver | in 1/2/2          |                  |     |     |     |
| Interface   | Name              | : 1/2/2          |     |     |     |
| Type        |                   | : unknown        |     |     |     |
| Connector   | Type              | : ??             |     |     |     |
| Wavelength  |                   | : ??             |     |     |     |
| Transfer    | Distance          | : ??             |     |     |     |
| Diagnostic  | Support           | : ??             |     |     |     |
| Product     | Number            | : ??             |     |     |     |
| Serial      | Number            | : ??             |     |     |     |
| Part        | Number            | : ??             |     |     |     |
| Transceiver | in 1/3/1          |                  |     |     |     |
| Interface   | Name              | : 1/3/1          |     |     |     |
| Type        |                   | : SFP28DAC3      |     |     |     |
| Connector   | Type              | : Copper Pigtail |     |     |     |
Transfer Distance : 0.00km (SMF), 0m (OM1), 0m (OM2), 0m (OM3)
| Diagnostic | Support | : None       |     |     |     |
| ---------- | ------- | ------------ | --- | --- | --- |
| Product    | Number  | : 844477-B21 |     |     |     |
| Serial     | Number  | : MYxxxxxxx  |     |     |     |
| Part       | Number  | : 77fc-7ce7  |     |     |     |
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
| Recent      | Errors:     |         |     |     |     |
| Rx loss     | of signal   |         |     |     |     |
Showingtransceiverthreshold-violations:
switch(config)# show interface transceiver threshold-violations
-----------------------------------------------------
| Port | Type | Channel Type(s) | of  | Recent |     |
| ---- | ---- | --------------- | --- | ------ | --- |
Threshold Violation(s)
Interfaceconfiguration|120

-----------------------------------------------------
| 1/1/1          | SFP+SR      |             |         | Tx bias      | high      | warning     |     |     |
| -------------- | ----------- | ----------- | ------- | ------------ | --------- | ----------- | --- | --- |
|                |             |             |         | 50.52        | mA >      | 40.00 mA    |     |     |
| 1/1/2          | SFP+ER*     |             |         | ??           |           |             |     |     |
| 1/2/1          | QSFP+SR4    |             | 1       | Tx power     | low       | alarm       |     |     |
|                |             |             |         | -17.00       | dBm       | < -0.50 dBm |     |     |
|                |             |             | 2       | Tx bias      | low       | warning     |     |     |
|                |             |             |         | 3.12         | mA < 4.00 | mA          |     |     |
| 1/2/2          | QSFP+ER4*   |             |         | ??           |           |             |     |     |
| 1/3/1          | SFP28DAC3   |             |         | n/a          |           |             |     |     |
| * unsupported  |             | transceiver |         |              |           |             |     |     |
| Command        | History     |             |         |              |           |             |     |     |
| Release        |             |             |         | Modification |           |             |     |     |
| 10.07orearlier |             |             |         | --           |           |             |     |     |
| Command        | Information |             |         |              |           |             |     |     |
| Platforms      | Command     |             | context | Authority    |           |             |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                       | utilization |     |             |     |            |     |     |
| -------------- | --------------------- | ----------- | --- | ----------- | --- | ---------- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |             |     | utilization |     | [non-zero] |     |     |
Description
Displaysphysicalportthroughputandutilization.
| Parameter   |     |     |     | Description                      |     |     |     |     |
| ----------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- |
| <IFNAME>    |     |     |     | Specifiesaninterfacename.        |     |     |     |     |
| <IFRANGE>   |     |     |     | Specifiestheportidentifierrange. |     |     |     |     |
| utilization |     |     |     | Displaysutilizationstatistics.   |     |     |     |     |
| non-zero    |     |     |     | Displaysnon-zerostatistics       |     |     |     |     |
Examples
Thefollowingexampleshowsportutilizationofallinterfaces:
| switch# | show | interface | utilization |     |     |     |     |     |
| ------- | ---- | --------- | ----------- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|------
---------------------|----------------------
|               |     | Interval | |   |     | RX  | |   | TX  | |   |
| ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| Total (RX+TX) |     |          | |   |     |     |     |     |     |
121
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |

Interface seconds | Mbps KPkt/s Util % | Mbps KPkt/s Util % |
| Mbps | KPkt/s | Util % | Description |     |     |     |     |
| ---- | ------ | -------------------- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|------
---------------------|----------------------
| 1/1/1          |             | 300       | 9578.02               | 788.70 95.78   | 25.70 45.89    | 0.26  |
| -------------- | ----------- | --------- | --------------------- | -------------- | -------------- | ----- |
| 9603.72        | 834.59      | 96.04     | Aruba-AP              |                |                |       |
| 1/1/2          |             | 300       | 25.71                 | 45.90 0.26     | 9581.09 788.96 | 95.81 |
| 9606.80        | 834.86      | 96.07     | Aruba2530-AP-conce... |                |                |       |
| 1/1/3          | - lag123    | 300       | 0.00                  | 0.00 0.00      | 0.00 0.00      | 0.00  |
| 0.00           | 0.00        | 0.00 ISL: | SWRTS-0064-1          |                |                |       |
| 1/1/4          |             | 300       | 9261.79               | 804.52 92.62   | 9496.70 823.97 | 94.97 |
| 18758.50       | 1628.48     | 187.58    | Backup                | data center... |                |       |
| 1/1/5          |             | 300       | 9496.70               | 823.97 94.97   | 9261.79 804.52 | 92.62 |
| 18758.50       | 1628.48     | 187.58    | --                    |                |                |       |
| Command        | History     |           |                       |                |                |       |
| Release        |             |           |                       | Modification   |                |       |
| 10.07orearlier |             |           |                       | --             |                |       |
| Command        | Information |           |                       |                |                |       |
| Platforms      | Command     | context   |                       | Authority      |                |       |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ip           | interface |                |            |     |     |     |
| ----------------- | --------- | -------------- | ---------- | --- | --- | --- |
| show ip interface |           | <INTERFACE-ID> | [vsx-peer] |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv4interface.Notethefollowingcaveatsforthe
8325,10000Seriesswitches:
n Whenthiscommandisissuedforasubinterface,theoutputofthecommanddisplaysonlythe
aggregatepacketcountofL3packetspassingthroughtheswitch.
n Whenthiscommandisissuedforasubinterface,theoutputofthiscommanddoesnotdisplayL3
counters.
Iftheselectedsubinterfaceisshut,theL2counterwillberesetto0.Whenthesubinterfaceis
n
reenabled,theL2counterwillberesetto0.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Interfaceconfiguration|122

| switch#      | show ip interface |     | 1/1/1    |                   |
| ------------ | ----------------- | --- | -------- | ----------------- |
| Interface    | 1/1/1 is          | up  |          |                   |
| Admin        | state is up       |     |          |                   |
| Hardware:    | Ethernet,         | MAC | Address: | 70:72:cf:fd:e7:b4 |
| IPv4 address | 192.168.1.1/24    |     |          |                   |
MTU 1500
RX
|     | 0 packets, | 0   | bytes |     |
| --- | ---------- | --- | ----- | --- |
TX
|             | 0 packets,     | 0     | bytes       |     |
| ----------- | -------------- | ----- | ----------- | --- |
| switch#     | show interface |       | <intfid>.id |     |
| Interface   | 1/1/14.1       | is up |             |     |
| Admin state | is up          |       |             |     |
| IP MTU      | 1500           |       |             |     |
Description:
| Hardware:     | Ethernet,      | MAC   | Address:   | b8:6a:97:22:2f:42 |
| ------------- | -------------- | ----- | ---------- | ----------------- |
| Encapsulation | dot1q          | ID:   | 20         |                   |
| IPv4 address  | 30.0.0.1/24    |       |            |                   |
| L3 Counters:  | Rx Disabled,   |       | Tx Disable |                   |
| switch#       | show interface |       | lag2.1     |                   |
| Interface     | lag2.1         | is up |            |                   |
| Admin state   | is up          |       |            |                   |
| IP MTU        | 1500           |       |            |                   |
Description:
| Hardware:      | Ethernet,    | MAC     | Address:    | b8:6a:97:22:2f:42 |
| -------------- | ------------ | ------- | ----------- | ----------------- |
| Encapsulation  | dot1q        | ID:     | 30          |                   |
| L3 Counters:   | Rx Disabled, |         | Tx Disabled |                   |
| Command        | History      |         |             |                   |
| Release        |              |         |             | Modification      |
| 10.07orearlier |              |         |             | --                |
| Command        | Information  |         |             |                   |
| Platforms      | Command      | context |             | Authority         |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip | source-interface |     |     |     |
| ------- | ---------------- | --- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
123
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- |

Parameter Description
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitches
donothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.This
parameterisavailableonswitchesthatsupportVSX.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch#          | show | ip source-interface |     | sflow       |
| ---------------- | ---- | ------------------- | --- | ----------- |
| Source-interface |      | Configuration       |     | Information |
----------------------------------------
| Protocol |     | Source           | Interface  |     |
| -------- | --- | ---------------- | ---------- | --- |
| -------- |     | ---------------- |            |     |
| sflow    |     |                  | 10.10.10.1 |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
switch#
|                  | show | ip source-interface |     | all         |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show      | ipv6      | interface      |     |            |
| --------- | --------- | -------------- | --- | ---------- |
| show ipv6 | interface | <INTERFACE-ID> |     | [vsx-peer] |
Description
Interfaceconfiguration|124

ShowsstatusandconfigurationinformationforanIPv6interface.Notethefollowingcaveatsforthe
8325,10000Seriesswitches:
n Whenthiscommandisissuedforasubinterface,theoutputofthecommanddisplaysonlythe
aggregatepacketcountofL3packetspassingthroughtheswitch.
n Whenthiscommandisissuedforasubinterface,theoutputofthiscommanddoesnotdisplayL3
counters.
n Iftheselectedsubinterfaceisshut,theL2counterwillberesetto0.Whenthesubinterfaceis
reenabled,theL2counterwillberesetto0.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<INTERFACE-ID> SpecifiesaninterfaceID.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#   | show  | ipv6  | interface | 1/1/1 |     |     |     |     |
| --------- | ----- | ----- | --------- | ----- | --- | --- | --- | --- |
| Interface | 1/1/1 | is    | up        |       |     |     |     |     |
| Admin     | state | is up |           |       |     |     |     |     |
IPv6 address:
| 2001:0db8:85a3:0000:0000:8a2e:0370:7334/24 |     |     |     |     |     |     | [VALID] |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- |
IPv6 link-local address: fe80::1e98:ecff:fee3:e800/64 (default)[VALID]
| IPv6 virtual    |     | address  | configured:     |         | none    |         |                |     |
| --------------- | --- | -------- | --------------- | ------- | ------- | ------- | -------------- | --- |
| IPv6 multicast  |     | routing: |                 | disable |         |         |                |     |
| IPv6 Forwarding |     | feature: |                 | enabled |         |         |                |     |
| IPv6 multicast  |     | groups   | locally         |         | joined: |         |                |     |
| ff02::ff70:7334 |     |          | ff02::ffe3:e800 |         |         | ff02::1 | ff02::1:ff00:0 |     |
ff02::2
| IPv6 multicast |          | (S,G)   | entries |             | joined: | none |     |     |
| -------------- | -------- | ------- | ------- | ----------- | ------- | ---- | --- | --- |
| IPv6 MTU:      | 1524     | (using  | link    | MTU)        |         |      |     |     |
| IPv6 unicast   |          | reverse | path    | forwarding: |         | none |     |     |
| IPv6 load      | sharing: |         | none    |             |         |      |     |     |
RX
|     | 0   | packets, | 0 bytes |     |     |     |     |     |
| --- | --- | -------- | ------- | --- | --- | --- | --- | --- |
TX
|             | 0        | packets, | 0 bytes   |             |     |     |     |     |
| ----------- | -------- | -------- | --------- | ----------- | --- | --- | --- | --- |
| switch#     | show     | ipv6     | interface | <intfid>.id |     |     |     |     |
| Interface   | 1/1/14.1 |          | is up     |             |     |     |     |     |
| Admin state |          | is up    |           |             |     |     |     |     |
IPv6 address:
| 30::1/64        | [VALID]           |          |             |                             |         |     |                |         |
| --------------- | ----------------- | -------- | ----------- | --------------------------- | ------- | --- | -------------- | ------- |
| IPv6 link-local |                   | address: |             | fe80::b86a:97c0:122:2f42/64 |         |     |                | [VALID] |
| IPv6 virtual    |                   | address  | configured: |                             | none    |     |                |         |
| IPv6 multicast  |                   | routing: |             | disable                     |         |     |                |         |
| IPv6 Forwarding |                   | feature: |             | enabled                     |         |     |                |         |
| IPv6 multicast  |                   | groups   | locally     |                             | joined: |     |                |         |
| ff02::1         | ff02::1:ff22:2f42 |          |             | ff02::1:ff00:1              |         |     | ff02::1:ff00:0 |         |
ff02::2
| IPv6 multicast |      | (S,G) | entries | joined: |     | none |     |     |
| -------------- | ---- | ----- | ------- | ------- | --- | ---- | --- | --- |
| IPv6 MTU       | 1500 |       |         |         |     |      |     |     |
125
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| IPv6 unicast  |          | reverse | path      | forwarding: |     | none |     |     |
| ------------- | -------- | ------- | --------- | ----------- | --- | ---- | --- | --- |
| IPv6 load     | sharing: |         | none      |             |     |      |     |     |
| Encapsulation |          | dot1q   | ID:       | 20          |     |      |     |     |
| switch#       | show     | ipv6    | interface | lag2.1      |     |      |     |     |
| Interface     | lag2.1   |         | is up     |             |     |      |     |     |
| Admin state   |          | is up   |           |             |     |      |     |     |
IPv6 address:
| 40::1/64        | [VALID]           |          |             |                             |         |     |                |         |
| --------------- | ----------------- | -------- | ----------- | --------------------------- | ------- | --- | -------------- | ------- |
| IPv6 link-local |                   | address: |             | fe80::b86a:97c0:122:2f42/64 |         |     |                | [VALID] |
| IPv6 virtual    |                   | address  | configured: |                             | none    |     |                |         |
| IPv6 multicast  |                   | routing: |             | disable                     |         |     |                |         |
| IPv6 Forwarding |                   | feature: |             | enabled                     |         |     |                |         |
| IPv6 multicast  |                   | groups   | locally     |                             | joined: |     |                |         |
| ff02::1         | ff02::1:ff22:2f42 |          |             | ff02::1:ff00:1              |         |     | ff02::1:ff00:0 |         |
ff02::2
| IPv6 multicast |             | (S,G)   | entries | joined:     |              | none |     |     |
| -------------- | ----------- | ------- | ------- | ----------- | ------------ | ---- | --- | --- |
| IPv6 MTU       | 1500        |         |         |             |              |      |     |     |
| IPv6 unicast   |             | reverse | path    | forwarding: |              | none |     |     |
| IPv6 load      | sharing:    |         | none    |             |              |      |     |     |
| Encapsulation  |             | dot1q   | ID:     | 30          |              |      |     |     |
| Command        | History     |         |         |             |              |      |     |     |
| Release        |             |         |         |             | Modification |      |     |     |
| 10.07orearlier |             |         |         |             | --           |      |     |     |
| Command        | Information |         |         |             |              |      |     |     |
| Platforms      |             | Command | context |             | Authority    |      |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ipv6 | source-interface |     |     |     |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
[vsx-peer]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesthenameofaVRF. |     |     |
| -------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
Interfaceconfiguration|126

Parameter Description
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitches
donothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.This
parameterisavailableonswitchesthatsupportVSX.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch#          | show ipv6 | source-interface | sflow       |
| ---------------- | --------- | ---------------- | ----------- |
| Source-interface |           | Configuration    | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| sflow    |     | 2001:DB8::1      |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show ipv6 | source-interface | all         |
| ---------------- | --------- | ---------------- | ----------- |
| Source-interface |           | Configuration    | Information |
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
127
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

| switch(config-if)# |     | shutdown |     |
| ------------------ | --- | -------- | --- |
Enablinganinterface:
| switch(config-if)#  |         | no shutdown |              |
| ------------------- | ------- | ----------- | ------------ |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
speed
speed {<SPEED> [override] | <SPEED-DUPLEX> | auto [<SPEED>] [override]}
no speed
Description
Configuresthelinkspeed,duplex,andauto-negotiationsettingsforaninterface.
Thenoformofthiscommandremovestheconfigurationsandreturnstothedefaults.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
Speed
Configuresinterfacespeed,duplex,andauto-negotiation.
| 10-full |     |     | 10Mbps,fullduplex,noauto-negotiation |
| ------- | --- | --- | ------------------------------------ |
10-half
10Mbps,halfduplex,noauto-negotiation
| 100-full |     |     | 100Mbps,fullduplex,noauto-negotiation |
| -------- | --- | --- | ------------------------------------- |
100-half
100Mbps,halfduplex,noauto-negotiation
| 1000-full |     |     | 1000Mbps,fullduplex,noauto-negotiation |
| --------- | --- | --- | -------------------------------------- |
10g
10Gbps,fullduplex,noauto-negotiation
| 25g |     |     | 25Gbps,fullduplex,noauto-negotiation |
| --- | --- | --- | ------------------------------------ |
40g
40Gbps,fullduplex,noauto-negotiation
| 50g |     |     | 50Gbps,fullduplex,noauto-negotiation |
| --- | --- | --- | ------------------------------------ |
Interfaceconfiguration|128

Parameter

Description

100g

200g

400g

auto

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

200g

400g

override

Usage

100 Gbps, full duplex, no auto-negotiation

200 Gbps, full duplex, no auto-negotiation

NOTE: Not applicable for override.

400 Gbps, full duplex, no auto-negotiation

NOTE: Not applicable for override.

Auto-negotiate speed and duplex. More than one speed can be
set at a time.

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

Allow interface to link at 200 Gbps.

Allow interface to link at 400 Gbps.

Override the detected transceiver speed and use the configured
speed.

The following options can be configured for an interface. The option available is based on the interface
type.
speed <SPEED-DUPLEX>

Uses a fixed speed and duplex mode with no auto-negotiation. Half-duplex is only supported for 10
Mbps and 100 Mbps link speeds.

speed <SPEED>

Uses a fixed speed with no auto-negotiation. If the currently installed transceiver does not support
the speed, the setting is ignored and the port will use the highest speed that is supported.

speed <SPEED> override

Uses a fixed speed with no auto-negotiation. If the currently installed transceiver does not support
the speed, attempt to use it anyway. This may or may not work, depending on the transceiver.

speed auto

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

129

Usesauto-negotiationandoffersallspeedssupportedbytheportandtransceiver.Thisisthe
default.Ifthelinktechnologydoesnotsupportauto-negotiationthissettingisignored,andtheport
usesthehighestpossiblefixedspeed.
speed auto <SPEED>
Usesauto-negotiationandoffersthespecifiedspeedsonly.Forportsthatsupportpluggable
transceivers,onlyspeedssupportedbythetransceiverareofferedandotherspeedsareignored.If
thelinktechnologydoesnotsupportauto-negotiation,thissettingisignoredandtheportusesthe
highestpossiblefixedspeed.
| speed auto <SPEED> | override |     |
| ------------------ | -------- | --- |
Usesauto-negotiationandoffersonlythespecifiedspeed.Ifthecurrentlyinstalledtransceiverdoes
notsupportauto-negotiation,attempttouseitanyway.Thismayormaynotworkdependingonthe
transceiver.
n Overridesupportisnotavailableonopticaltransceivers.
n Speedoverrideandauto-negotiationoverridearenotsupportedonsplitports.
Auto-negotiationcannotbeenabledona10G-DAC.
n
Examples
Configuringaninterfacetooperateatafixedspeedof1000Mbpswithfullduplexandnoauto-
negotiation:
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | speed     | 1000-full |
Configuringaninterfacetooperateatafixedspeedof10Gbpswithnoauto-negotiation:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | speed     | 10g   |
Configuringaninterfacetoauto-negotiateandadvertiseonly1Gbpsand2.5Gbpsspeeds:
| switch(config)#    | interface | 1/1/1        |
| ------------------ | --------- | ------------ |
| switch(config-if)# | speed     | auto 1g 2.5g |
Configuringaninterfacetooverridethedetectedtransceiverspeedandusetheconfiguredspeedifthe
installedtransceiverdoesnotsupportauto-negotiation:
| switch(config)#    | interface | 1/1/1             |
| ------------------ | --------- | ----------------- |
| switch(config-if)# | speed     | auto 50g override |
Configuringaninterfacetousedefaultsettingsforspeed,duplex,andauto-negotiation:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | no speed  |       |
Command History
Interfaceconfiguration|130

| Release |     |     | Modification |     |     |
| ------- | --- | --- | ------------ | --- | --- |
10.11
|     |     |     | speed <SPEED> | overrideandspeed | auto <SPEED> |
| --- | --- | --- | ------------- | ---------------- | ------------ |
overrideareadded.Thisisavailableonlyon8360,8325,and
10000SwitchSeries.
| 10.09.0001     |             |         | SpeedsnotsupportedbyhardwarehiddenbyCLI. |     |     |
| -------------- | ----------- | ------- | ---------------------------------------- | --- | --- |
| 10.07orearlier |             |         | --                                       |     |     |
| Command        | Information |         |                                          |     |     |
| Platforms      | Command     | context | Authority                                |     |     |
8325 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8360 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
10000
| system    | interface-group |               |               |     |     |
| --------- | --------------- | ------------- | ------------- | --- | --- |
| system    | interface-group | <GROUP> speed | <SPEED>       |     |     |
| no system | interface-group | <GROUP>       | speed <SPEED> |     |     |
Description
Configuresthespeedforaninterfacegroup.Afterchanginggroupspeed,onlytransceiverscompatible
withthenewspeedwillbeenabled.
n Allspeed-mismatchedinterfacesinthegroupwillbedisabled.
n Thiscommandcaninterruptactivenetworklinks,userconfirmationisrequiredtoproceed.
Thenoformofthiscommandresetsthespecifiedinterfacegrouptoitsdefault.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<GROUP>
Specifiestheinterfacegrouptoconfigure.
| <SPEED> |     |     | Configurestransceiverspeed(10g,25gor50g)foragroup. |     |     |
| ------- | --- | --- | -------------------------------------------------- | --- | --- |
Defaultis25g(seetheTransceiverGuideforfurtherdetail).
Configurestransceiverspeed(10gor25g)foragroup.
Defaultis25g(seetheTransceiverGuideforfurtherdetail).
On8325SwitchSeries:
n 10gallows1Gbpsor10Gbpstransceiversonly.
n 25gallows25Gbpstransceiversonly.
On9300SwitchSeries:
n 10gallows1Gbpsor10Gbpstransceiversonly.
n 25gallows25Gbpstransceiversonly.
On8360SwitchSeries:
131
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
25gallows1Gbps,10Gbpsor25Gbpstransceiversonly.
n
n 50gallows50Gbpstransceiversonly.
NOTE:On(8360)JL717CandJL719C:
n 10gallows1Gbpsand10Gbpstransceiversonly.
n 25gallows25Gbpstransceiversonly.
Examples
Configuringinterfacegroup1toallow10Gbpsandslowertransceivers:
| switch(config)# | system | interface-group | 1 speed 10g |
| --------------- | ------ | --------------- | ----------- |
Changing the group speed will disable all member interfaces that do not match the
new speed.
| Continue            | (y/n)? y |         |                                      |
| ------------------- | -------- | ------- | ------------------------------------ |
| Command History     |          |         |                                      |
| Release             |          |         | Modification                         |
| 10.10.1000          |          |         | Commandintroducedon9300Switchseries. |
| 10.07orearlier      |          |         | --                                   |
| Command Information |          |         |                                      |
| Platforms           | Command  | context | Authority                            |
8325 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 8360 | (#) |     | forthiscommand. |
| ---- | --- | --- | --------------- |
9300
Interfaceconfiguration|132

Chapter 6

Subinterfaces

Subinterfaces

A subinterface is a virtual interface created by dividing one physical interface into multiple logical
interfaces. Subinterfaces use the parent physical interface for sending and receiving data.

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

For the 8325 and 10000 Switch series, IVRL subinterfaces are not supported.

Configuring subinterfaces

n Subinterfaces can be configured for physical ports, split children of physical ports and L3 LAG interfaces.

n Subinterfaces on multiple ports can be assigned the same VLAN ID (there is no bridging between

subinterfaces or between subinterfaces and SVIs) using encapsulation vlan-idencapsulation vlan-
id. Each subinterface is considered to be in a separate bridge domain.

n The IP-MTU of a subinterface can be configured independent of the parent port's IP-MTU configuration.

Procedure

One router with one physical interface needs to be connected to two IP networks:

1. Create two subinterfaces within the physical interface.

2. Assign each subinterface an IP address within each subnet.

3. Route packets between the two subnets.

Limitations

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

133

n Subinterfaces can only be configured on L3 ports with routing enabled.

n A subinterface cannot be a member of a LAG.

n An L3 parent interface with subinterfaces cannot be a member of a LAG.

n An L3 parent interface with subinterfaces cannot be used for L3 services (for example IP address

configuration is not supported on an L3 interface if the interface is configured with subinterfaces).

n On physical interfaces, each subinterface must have a unique encapsulation ID.

n BFD and IPDB are not supported on subinterfaces.

Subinterface in a router-on-a-stick deployment

n Top-of-rack switch/router with an L3 interface connected to the trunk port of an L2 switch.

n Routing tables configured to forward outgoing traffic through a subinterface while applying a VLAN

ID tag.

n All outgoing traffic from the L3 interface is tagged with a VLAN ID which enables the switch to

forward traffic through different VLANs.

n Top-of-rack switch/router with an L3 interface connected to the trunk port of an L3 interface.

n Routing tables configured to forward outgoing traffic through a subinterface while applying a VLAN

ID tag.

n All outgoing traffic from the L3 interface is tagged with a VLAN ID which enables the switch to

forward traffic through different VLANs.

Subinterface commands

Configuration of system internal-vlan-range to 2000-3200 is required on the 8325 and 10000 switch
series for scaled subinterfaces. Refer to the L2 Bridging Guide for more information on system internal-
vlan-range.

encapsulation dot1q

Subinterfaces | 134

| encapsulation    | dot1q <VLAN-ID> |           |     |
| ---------------- | --------------- | --------- | --- |
| no encapsulation | dot1q           | <VLAN-ID> |     |
Description
Configures802.1Qencapsulationonasubinterface.
Thenoformofthiscommandremoves802.1Qencapsulationonasubinterface.
| Parameter |     |     | Description                   |
| --------- | --- | --- | ----------------------------- |
| <VLAN-ID> |     |     | SpecifiesencapsulationVLANID. |
Range1to4094.
NOTE:TheencapsulationVLANID shouldbeuniquewithinanL3
LAGsubinterface.ThesameencapsulationVLANIDcanbe
configuredamongdifferentparentinterfaces,butthe
encapsulationVLANIDshouldnotbeconfiguredintheinternal
VLANrange.(EncapsulationVLANIDsandstaticVLANsareentirely
differentanddonotcoincide.)
Usage
Associatesan802.1QVLANID withasubinterface.
Examples
Configuring802.1Qencapsulationonasubinterface:
| switch(config)#       | interface | 1/1/1.201     |          |
| --------------------- | --------- | ------------- | -------- |
| switch(config-subif)# |           | encapsulation | dot1q 10 |
Removing802.1Qencapsulationonasubinterface:
| switch(config-subif)# |         | no encapsulation | dot1q 10                                    |
| --------------------- | ------- | ---------------- | ------------------------------------------- |
| Command History       |         |                  |                                             |
| Release               |         |                  | Modification                                |
| 10.11                 |         |                  | Commandintroducedfor8325,10000switchseries. |
| 10.08                 |         |                  | Commandintroducedforthe8360switchseries.    |
| Command Information   |         |                  |                                             |
| Platforms             | Command | context          | Authority                                   |
config-subif
8325 Administratorsorlocalusergroupmemberswithexecutionrights
| 8360 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
10000
interface
| interface <IFNAME>.<ID> |     |     |     |
| ----------------------- | --- | --- | --- |
135
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| no interface <IFNAME>.<ID>  |               |     |
| --------------------------- | ------------- | --- |
| interface lag <LAGNUM>.<ID> |               |     |
| no interface lag            | <LAGNUM>.<ID> |     |
Description
CreatesasubinterfaceonanL3interfaceandenterssubinterfaceconfigurationmode.Thesubinterface
nameconsistsoftheparentinterfacename(forexample,1/1/1)followedbyaperiodandauniqueID
number.
ThenoformofthesecommandsdeletesasubinterfacefromanL3interface.
8325and10000SwitchseriesrequireaninternalVLAN foreverysubinterface,inadditiontotheinternalVLANs
usedforotherpurposes.Forexample,tosupport1024subinterfaces,aninternalVLANrangethatisatleastthat
largemustbereservedusingthesystem internal-vlan-rangecommand.8325and10000Seriesswitches
supportamaximumof1024subinterfacesresources.
BFDsessionsarenotsupportedonsubinterfaceson8325and10000Switchseries.Useswitchvirtualinterfaces
(SVIs)toconfigureaBFDsessionontheseswitchmodels.
Parameter Description
<IFNAME> SpecifiesL3interfacename.
<ID> SpecifiessubinterfaceID.Range1to4094.
<LAGNUM> SpecifiesL3LAGinterfacenumber.
Usage
TocreateaLAGsubinterface,theparentLAGmustexistbeforecreatingthesubinterface.
EachLAGsubinterfacerequiresfourinternalVLANs.YoucanconfigureacombinationofL3LAG
subinterfacesandphysicalinterfacesubinterfaces.EachL3LAGconsumesfoursub-interfaceresources,
andinthisLAGtherecanbemaximumoffourLAGmemberinterfaces.Eachphysicalinterfacesub-
interfaceconsumesonesub-interfaceresource.
Examples
CreatingasubinterfaceonL3interface1/1/1.201andenteringsubinterfaceconfigurationmode:
| switch(config)# | interface | 1/1/1.201 |
| --------------- | --------- | --------- |
switch(config-subif)#
DeletingsubinterfaceonL3interface1/1/1.201:
| switch(config)# | no interface | 1/1/1.201 |
| --------------- | ------------ | --------- |
CreatingasubinterfaceonanL3LAGportandenteringsubinterfaceconfigurationmode:
| switch(config)#    | interface | lag 1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | interface | lag 1.201 |
Subinterfaces|136

switch(config-subif)#
DeletingsubinterfaceonanL3LAG port:
| switch(config)#     | no      | interface | lag | 1.201                                         |     |     |
| ------------------- | ------- | --------- | --- | --------------------------------------------- | --- | --- |
| Command History     |         |           |     |                                               |     |     |
| Release             |         |           |     | Modification                                  |     |     |
| 10.11               |         |           |     | Commandintroducedfor8325and10000switchseries. |     |     |
| 10.08               |         |           |     | Commandintroducedforthe8360switchseries.      |     |     |
| Command Information |         |           |     |                                               |     |     |
| Platforms           | Command | context   |     | Authority                                     |     |     |
8325 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8360
10000
| show capacities | subinterface |     |     |     |     |     |
| --------------- | ------------ | --- | --- | --- | --- | --- |
| show capacities | subinterface |     |     |     |     |     |
Description
Displaysmaximumsubinterfacecapacity.
Examples
Showingmaximumsubinterfacecapacity:
| switch#            | show capacities | subinterface |              |     |     |     |
| ------------------ | --------------- | ------------ | ------------ | --- | --- | --- |
| System Capacities: |                 | Filter       | Subinterface |     |     |     |
| Capacities         | Name            |              |              |     |     |     |
Value
----------------------------------------------------------------------------------
-
| Maximum | number of | LAG subinterfaces |     |     | for the entire | system |
| ------- | --------- | ----------------- | --- | --- | -------------- | ------ |
256
| Maximum | number of | LAG members | when | the | LAG has subinterfaces |     |
| ------- | --------- | ----------- | ---- | --- | --------------------- | --- |
4
| Maximum | number of | normal subinterfaces |     |     | for the entire | system |
| ------- | --------- | -------------------- | --- | --- | -------------- | ------ |
1024
Maximum number of subinterface resources for the entire system (normal+(4*LAG)
1024
| Command History |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
137
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

| Release   |             |     |         |     | Modification                                  |     |     |
| --------- | ----------- | --- | ------- | --- | --------------------------------------------- | --- | --- |
| 10.11     |             |     |         |     | Commandintroducedfor8325and10000switchseries. |     |     |
| 10.08     |             |     |         |     | Commandintroducedforthe8360switchseries.      |     |     |
| Command   | Information |     |         |     |                                               |     |     |
| Platforms | Command     |     | context |     | Authority                                     |     |     |
8325 Operator(>)orManager AuditorsorAdministratorsorlocalusergroupmemberswith
8360 (#) executionrightsforthiscommand.Auditorscanexecutethis
| 10000 |     |     |     |     | commandfromtheauditorcontext(auditor>)only. |     |     |
| ----- | --- | --- | --- | --- | ------------------------------------------- | --- | --- |
show interface
| show interface | <IFNAME>.<ID> |               |     |     |     |     |     |
| -------------- | ------------- | ------------- | --- | --- | --- | --- | --- |
| show interface | lag           | <LAGNUM>.<ID> |     |     |     |     |     |
Description
Displaysasubinterfaceconfiguration.
| Parameter |     |     |     |     | Description                    |     |     |
| --------- | --- | --- | --- | --- | ------------------------------ | --- | --- |
| <IFNAME>  |     |     |     |     | SpecifiesL3interfacename.      |     |     |
| <ID>      |     |     |     |     | SpecifiessubinterfaceID.       |     |     |
| <LAGNUM>  |     |     |     |     | SpecifiesL3LAGinterfacenumber. |     |     |
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
| switch#     | show interface |         | lag1.1 |     |     |     |     |
| ----------- | -------------- | ------- | ------ | --- | --- | --- | --- |
| Interface   | lag1.1         | is down |        |     |     |     |     |
| Admin state | is up          |         |        |     |     |     |     |
Description:
| Hardware:     | Ethernet, | MAC | Address: |     | 38:21:c7:5a:80:80 |     |     |
| ------------- | --------- | --- | -------- | --- | ----------------- | --- | --- |
| Encapsulation | dot1Q     | ID: | 2        |     |                   |     |     |
Subinterfaces|138

| Statistic |     |     | RX  | TX  | Total |
| --------- | --- | --- | --- | --- | ----- |
---------------- -------------------- -------------------- --------------------
| L3 Packets          |         |         | 0                                             | 0   | 0   |
| ------------------- | ------- | ------- | --------------------------------------------- | --- | --- |
| L3 Bytes            |         |         | 0                                             | 0   | 0   |
| Command History     |         |         |                                               |     |     |
| Release             |         |         | Modification                                  |     |     |
| 10.11               |         |         | Commandintroducedfor8325and10000switchseries. |     |     |
| 10.08               |         |         | Commandintroducedforthe8360switchseries.      |     |     |
| Command Information |         |         |                                               |     |     |
| Platforms           | Command | context | Authority                                     |     |     |
8325 Operator(>)orManager AuditorsorAdministratorsorlocalusergroupmemberswith
8360 (#) executionrightsforthiscommand.Auditorscanexecutethis
| 10000 |     |     | commandfromtheauditorcontext(auditor>)only. |     |     |
| ----- | --- | --- | ------------------------------------------- | --- | --- |
139
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

Chapter 7
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
| Source-interface       | selection  |           | commands         |     |     |     |
| ---------------------- | ---------- | --------- | ---------------- | --- | --- | --- |
| ip source-interface    | (protocol  |           | <ip-addr>)       |     |     |     |
| ip source-interface    | <PROTOCOL> | <IP-ADDR> | [vrf <VRF-NAME>] |     |     |     |
| no ip source-interface | <PROTOCOL> | <IP-ADDR> | [vrf <VRF-NAME>] |     |     |     |
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
140
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

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
Sourceinterfaceselection|141

| switch(config)#     | no      | ip source-interface | dns 10.1.1.2 | vrf green |
| ------------------- | ------- | ------------------- | ------------ | --------- |
| Command History     |         |                     |              |           |
| Release             |         |                     | Modification |           |
| 10.07orearlier      |         |                     | --           |           |
| Command Information |         |                     |              |           |
| Platforms           | Command | context             | Authority    |           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
142
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 source-interface
| ipv6 source-interface |     |            | <PROTOCOL> | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |     |
| --------------------- | --- | ---------- | ---------- | ----------- | --- | ---------------- | --- |
| no source-interface   |     | <PROTOCOL> |            | <IPV6-ADDR> |     | [vrf <VRF-NAME>] |     |
Description
Configuresthesource-interfaceIPv6addresstouseforthespecifiedprotocol.IfaVRFisnotgiven,the
defaultVRFapplies.
Thenoformofthiscommandremovesthespecifiedprotocolconfiguration.
Sourceinterfaceselection|143

| Parameter  |     |     | Description                      |     |
| ---------- | --- | --- | -------------------------------- | --- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoconfigure. |     |
all:Selectsallprotocolssupportedbythiscommand.
n
n central:SelectsArubaCentral.
n ntp:SelectsNTP.
n radius:Selectsradius.
n sflow:SelectssFLow.
n syslog:Selectssyslog.
n tacacs:SelectsTACACS.
n tftp:SelectsTFTP.
<IPV6-ADDR>
SpecifiestheIPv6address.
| vrf <VRF-NAME> |     |     | SpecifiestheVRF name. |     |
| -------------- | --- | --- | --------------------- | --- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
144
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

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

Source interface selection | 145

switch(config)# no ipv6 source-interface tftp interface 1/1/2 vrf green
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip source-interface |     |     |     |
| ------------------------ | --- | --- | --- |
show ip source-interface <PROTOCOL> [vrf <VRF-NAME> | all-vrfs]
Description
DisplaysthesourceinterfaceinformationforallVRFsoraspecificVRF.
IfaVRF isnotspecified,thedefaultisdisplayed.
| Parameter  |     |     | Description                 |
| ---------- | --- | --- | --------------------------- |
| <PROTOCOL> |     |     | Specifiestheprotocoltoshow. |
all
Showsthesourceinterfaceconfigurationforallother
protocols.
central
ShowsthesourceinterfaceconfigurationforAruba
Central.
dhcp relay
ShowsthesourceinterfaceconfigurationforDHCP
relay.
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
146
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter      |     |     | Description                                     |     |
| -------------- | --- | --- | ----------------------------------------------- | --- |
| vrf <VRF-NAME> |     |     | SpecifiestheVRF name.                           |     |
| all-vrfs       |     |     | ShowsthesourceinterfaceconfigurationforallVRFs. |     |
Examples
Displayingallsource-interfaceprotocolconfigurationsforVRF red:
| switch#          | show ip source-interface |     | all vrf red |     |
| ---------------- | ------------------------ | --- | ----------- | --- |
| Source-interface | Configuration            |     | Information |     |
---------------------------------------------------------------
| Protocol | Src-Interface |     | Src-IP | VRF |
| -------- | ------------- | --- | ------ | --- |
---------------------------------------------------------------
| all | 1/1/1 |     |     | red |
| --- | ----- | --- | --- | --- |
switch#
Displayingallsource-interfaceprotocolconfigurationsfordefaultVRF:
| switch#          | show ip source-interface |     | all         |     |
| ---------------- | ------------------------ | --- | ----------- | --- |
| Source-interface | Configuration            |     | Information |     |
-------------------------------------------------------------------
| Protocol | Src-Interface |     | Src-IP | VRF |
| -------- | ------------- | --- | ------ | --- |
-------------------------------------------------------------------
| all |     |     | 1.1.1.1 | default |
| --- | --- | --- | ------- | ------- |
switch#
Displaying allsource-interfaceprotocolconfigurationsforallVRFs:
| switch#          | show ip source-interface |     | all all-vrfs |     |
| ---------------- | ------------------------ | --- | ------------ | --- |
| Source-interface | Configuration            |     | Information  |     |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ipv6 | source-interface |     |     |     |
| --------- | ---------------- | --- | --- | --- |
Sourceinterfaceselection|147

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
148
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

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
| Command History     |         |     |         |     |              |     |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- | --- |
| Release             |         |     |         |     | Modification |     |     |     |
| 10.07orearlier      |         |     |         |     | --           |     |     |     |
| Command Information |         |     |         |     |              |     |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show running-config
show running-config
Description
Displaysthecurrentrunningconfiguration.
Examples
Displayingtherunningconfiguration(onlyitemsofinteresttosourceinterfaceselectionareshownin
thisexampleoutputcommand):
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
Sourceinterfaceselection|149

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
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
150
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Chapter 8

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

151

Precision time protocol (PTP)

Chapter 9

Precision time protocol (PTP)

PTP is available on the Aruba 8360 Switch Series (excluding JL706A and JL707A).

If PTP is configured on MACsec-supported ports, the switch can experience higher jitter or lower PTP accuracy.

Precision Time Protocol (PTP) is defined in the IEEE 1588 standard (Standard for a Precision Clock
Synchronization Protocol for Networked Measurement and Control Systems). PTP synchronizes clocks in
packet-based networks that include distributed device clocks of varying precision and stability. On a
local area network, it achieves clock accuracy in the sub-microsecond range, making it suitable for
measurement and control systems. PTP is currently employed to synchronize financial transactions,
mobile phone tower transmissions, and networks that require precise timing but lack access to satellite
navigation signals.

PTP clocks
A PTP network consists of PTP-enabled devices and devices that are not using PTP. The PTP-enabled
devices typically consist of clock-aware devices such as ordinary clocks (which are usually single-port
end-stations) and one or more grandsource clocks, transparent clocks, and boundary clocks (multi-port
L2/L3 time-aware devices).

The basic clock node types include:

Grandsource clock—A grandsource clock is the primary source of time for the downstream devices.
This is a device with greater clock quality which may have direct access to a reference clock.

Ordinary clock—An ordinary clock is a single port end-station (which can include a GM as the
originating PTP time-aware device).

Transparent clock—A transparent clock can have multiple network port connections but it does not act
as either a clock-source or a clock-sink. Rather, it updates the correction field within the PTP event
messages (SYNC/FOLLOW_UP, DELAY_REQUEST) to compensate for the transit time delay. Transparent
clocks compensate for switch latency and jitter, making network devices appear transparent to other
PTP time-aware devices. They help in reducing the end-station time errors and improving
synchronization quality. But a transparent clock itself does not synchronize its time.

There are two types of transparent clocks:

n End-to-End (E2E) transparent clock—Updates the correctionField field in the PTP messages with

the total time the PTP packet was resident in the network device. This is called resident time
correction.

n Peer-to-Peer (P2P) transparent clock—Updates the correctionField field in the PTP messages

with the sum of upstream link delay and the resident time. The upstream link delay is the estimated
packet propagation delay between the upstream neighbor P2P clock and the local transparent clock.

Boundary clock—A boundary clock implements a local PTP clock where one port acts as clock-sink
which synchronizes itself with the clock-source while other ports act as clock-source ports to its
downstream clock-aware devices. The clock-source port is used to redistribute the clock to another set

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

152

of clock-sinks. Boundary clocks can also use E2E or P2P delay-mechanism, and can be configured based
on the selected PTP profile. The best clock source algorithm is used by the boundary clock to select the
best or most precise configured acceptable clock-source clock.

Based on hardware capability, the switch supports either boundary clock, transparent clock, or both
modes.

Best clock-source algorithm

The best clock-source algorithm helps in choosing the source of timing on your network. It runs
independently on each clock in a domain. This algorithm specifies the way that a local clock can
determine which of all the clocks (including itself) is the best. Since it runs continuously, it continually re-
adapts to changes in the network or the clocks.

Each clock sends a message to the network describing its own properties. The best clock-source
algorithm running in the clock compares these properties to determine the best clock.

The comparisons of attributes happens with the following precedence :

1. Priority1: user configurable absolute priority

2. ClockClass: Attribute defining a clock’s TAI traceability

3. Time Source: Attribute defining the accuracy of a clock

4. Variance: An attribute defining the precision of a clock

5. Priority2: This is a user configurable designation that provides finer grained ordering among
otherwise equivalent clocks

6. Clock Identity : A tiebreaker consisting of the MAC address of the clock

In addition to this precedence order, the distance measured by the number of boundary clocks between
the local clock and the best clock is used when two Announce messages reflect the same best clock.
The distance is indicated in the stepsRemoved field of announce messages.

PTP network diagram
The following diagram illustrates how the various PTP clock nodes are connected and how the timing
information flows from the origin to the end-stations to achieve the time synchronization. This diagram
depicts the PTP clocks in a source-sink hierarchy.

Precision time protocol (PTP) | 153

| Figure        | 1 ExamplePTPnetworkwithclocksinasource-sinkhierarchy |             |       |          |
| ------------- | ---------------------------------------------------- | ----------- | ----- | -------- |
| Configuration | examples                                             |             |       |          |
| Configuring   | an end-to-end                                        | transparent | clock | (TC E2E) |
FollowthesestepstoconfiguretheE2Etransparentclock:
1. Configurethemandatorycommands:
a. ConfigurethePTPmodeandthedelaymechanism.
b. ConfigurethePTPclock-stepmode.
c. Configurethetransportprotocol.
d. ConfigurePTPglobally.
Switch config:
|     | switch(config)#     | ptp profile        | 1588v2      |            |
| --- | ------------------- | ------------------ | ----------- | ---------- |
|     | switch(config-ptp)# | mode               | transparent | end-to-end |
|     | switch(config-ptp)# | clock-step         | one-step    |            |
|     | switch(config-ptp)# | transport-protocol |             | ethernet   |
|     | switch(config-ptp)# | enable             |             |            |
2. EnablePTPontheconnectedinterfaces:
|     | switch(config)#    | int 1/1/1  |     |     |
| --- | ------------------ | ---------- | --- | --- |
|     | switch(config-if)# | ptp enable |     |     |
|     | switch(config-if)# | int 1/1/2  |     |     |
|     | switch(config-if)# | ptp enable |     |     |
154
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Configuring | an end-to-end | boundary | clock | (BC | E2E) |
| ----------- | ------------- | -------- | ----- | --- | ---- |
Followthesestepstoconfiguretheend-to-endboundaryclock:
1. CreatethePTPcontextusingthespecifiedprofile.
|     | switch(config)# | ptp profile | 1588v2 |     |     |
| --- | --------------- | ----------- | ------ | --- | --- |
switch(config-ptp)#
2. Configurethemandatorycommands:
a. ConfigurethePTPmode.
b. ConfigurethePTPclock-stepmode.
c. Configurethetransportprotocol.
d. ConfigurePTPglobally.
|     | switch(config-ptp)# | mode               | boundary | end-to-end |          |
| --- | ------------------- | ------------------ | -------- | ---------- | -------- |
|     | switch(config-ptp)# | clock-step         |          | one-step   |          |
|     | switch(config-ptp)# | transport-protocol |          |            | ethernet |
|     | switch(config-ptp)# | enable             |          |            |          |
3. Configuretheoptionalcommandswhichparticipateinthebestclocksourcealgorithm:
a. Configurepriority1value.
b. Configurepriority2value.
|     | switch(config-ptp)# | priority1 | 1   |     |     |
| --- | ------------------- | --------- | --- | --- | --- |
switch(config-ptp)#
|     |     | priority2 | 10  |     |     |
| --- | --- | --------- | --- | --- | --- |
4. EnablePTPontheconnectedinterfaces:
|     | switch(config)# | int 1/1/1 |     |     |     |
| --- | --------------- | --------- | --- | --- | --- |
switch(config-if)#
ptp enable
|     | switch(config-if)# | int 1/1/2  |     |     |     |
| --- | ------------------ | ---------- | --- | --- | --- |
|     | switch(config-if)# | ptp enable |     |     |     |
5. Optional:changingpacketintervalrateforvariousPTPparameters:
|          | switch(config-if)# | ptp sync-interval      |     |     | 1588v2 1  |
| -------- | ------------------ | ---------------------- | --- | --- | --------- |
|          | switch(config-if)# | ptp announce-interval  |     |     | 1588v2 -5 |
|          | switch(config-if)# | ptp announce-timeout   |     |     | 1588v2 4  |
|          | switch(config-if)# | ptp delay-req-interval |     |     | 1588v2 -3 |
| Hardware | considerations     |                        |     |     |           |
PTP issupportedonbreakoutcablesandSubinterfaces.PTPconnectionsthroughaQSA28(QSFP28to
SFPadapter)transceiversarenotsupported.DACsarenotsupportedforusethroughQSA28adapters.
(RefertotheTransceiverGuideforfurtherinformation.)
PTPClientsconnectedto1GbpsXCVRsonan8360SwitchactingasthePTPboundaryclockorPTP
transparentclockwillhaveaslightlyhigheroffsetwhenthereisbackgrounddatatrafficbetween
clients.ThisisaknownlimitationspecificallytoClientsconnectedonlyon1GbpslinksontheAruba
Precisiontimeprotocol(PTP)|155

8360SwitchSeries.Clientsconnectedonhigherspeedlinks(10/25/40/50/100)Gbpswillnotbe
impacted.
UseofthirdpartytransceiversmayintroduceunknownlatencyandhaveaneffectontheaccuracyofPTP
deployments.
| Configuration |      |                 |               | recommendations |     |                 |       |     |
| ------------- | ---- | --------------- | ------------- | --------------- | --- | --------------- | ----- | --- |
| PTP           | CoPP | class           | configuration |                 |     | recommendations |       |     |
| Configuration |      | recommendations |               |                 | for | a boundary      | clock |     |
ThePTPCoPPclassmustbeadjustedbasedonthenumberofclientsassociatedwiththeboundary
clockandtheconfiguredpacketrate.Forexample,ifthereare1000clientswithaconfiguredpacketrate
of2pps,andadefaultCoPPlimitof1000,packetdropswillbeobserved.InsuchinstancestheCoPP
limitshouldbeincreasedtomorethan2000.
Theshow copp statistics class ptpcommandcanbeusedtomonitorwhethertheCoPPpolicy
mustbeadjusted.Forexample:
| Statistics   |          | for   | CoPP      | policy   | 'default': |       |                 |     |
| ------------ | -------- | ----- | --------- | -------- | ---------- | ----- | --------------- | --- |
| Class:       |          | ptp   |           |          |            |       |                 |     |
| Description: |          |       | Precision | Time     | Protocol   | (PTP) | .               |     |
|              | priority |       |           |          | : 5        |       |                 |     |
|              | rate     | (pps) |           |          | : 1000     |       |                 |     |
|              | burst    | size  | (pkts)    |          | : 250      |       |                 |     |
|              | packets  |       | passed    | : 611153 |            |       | packets dropped | : 0 |
IncreasingthePTPCoPPvaluesmayhelpinscalingtheclientsbutneedstobeplannedandconfiguredproperly
soastonottoimpactotherprotocols.
QoS prioritization configuration recommendations for a transparent clock
| class     |       | ip PTP  |         |        |                |       |     |     |
| --------- | ----- | ------- | ------- | ------ | -------------- | ----- | --- | --- |
|           | 10    | match   | udp any | any    | eq 319         | count |     |     |
| policy    |       | PTP-POL |         |        |                |       |     |     |
|           | 10    | class   | ip PTP  | action | local-priority |       | 6   |     |
| policy    |       | test    |         |        |                |       |     |     |
| interface |       | lag     | 240     |        |                |       |     |     |
|           | apply | policy  | PTP-POL |        | in             |       |     |     |
| interface |       | 1/1/26  |         |        |                |       |     |     |
|           | apply | policy  | PTP-POL |        | in             |       |     |     |
| interface |       | 2/1/26  |         |        |                |       |     |     |
|           | apply | policy  | PTP-POL |        | in             |       |     |     |
PTPEventmessagescarryingacriticaltimestampuseUDPport319.
| General |     | guidelines |     | for | PTP | IPv4 multicast |     |     |
| ------- | --- | ---------- | --- | --- | --- | -------------- | --- | --- |
156
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

n For IP multicast-based PTP time distribution, it is recommended to use PIM Sparse-Mode.

n When connecting transparent clock (TC) and boundary clock (BC), ensure that the TC becomes the DR

by setting the DR priority.

n Ensure the mroutes are programmed on TCs so that there is reachability for PTP streams from the

upstream.

n Configure static-igmp groups on TCs if the clients themselves cannot send IGMP joins for the PTP

multicast group.

n The QoS trust dscp command needs to be explicitly configured on all non-BC switches in the

network to ensure that the incoming DSCP value of PTP traffic is honored.

n If Peer-to-Peer (P2P) does not happen with the immediate peer (for example some configurations
with Unicast mode that skip over intermediate-nodes, which could be one or more Transparent
Clocks) the offsets may go high.

Use cases

Use case: PTP – IPv4 over L2 spine leaf topology

Figure 2 Grand clock source connected to boundary clock (spines), followed by transparent clock leaves

The following considerations and best practices apply to this use case illustrated in the above topology:

n Configure candidate-RP on switches that are connected to a grand clock source. The candidate-RP

needs to be configured on the BC1 Spine A and BC2 Spine B.

n When the PTP clients are not capable of sending IGMP joins, be sure to configure ip igmp static-

group 224.0.1.129 on the VLAN interface of a TC, where PTP is configured.

In this case, it is an L2 switch in leaf so ip igmp snooping enable also needs to be configured on the
transparent clock VLAN interface.

n Ensure that ip source-interface ptp is configured on both BC switches on the VLAN interface

where PTP is configured.

n Ensure that spanning tree is enabled to avoid unwanted loops.

n In this use case topology, It is recommended to have VRRP on boundary clock switches to have L3

redundancy for PTP end clients.

Precision time protocol (PTP) | 157

Use case: PTP – L3 spine leaf topology

Figure 3 Grand clock source connected to transparent clock, followed by boundary clock spines and
boundary clock leaves

The following considerations and best practices apply to this use case illustrated in the above topology:

n Configure candidate-RP on switches which are connected to a grand clock source. Candidate-RP

needs to be configured on TC1 and TC2. Each candidate-RP controls multicast traffic forwarding for
one or more multicast groups.

n Configure higher DR priority on switches in which candidate-RP is configured. The DR priority needs

to be configured on the TC1 and TC2 on the BC facing ports.

n When the PTP clients are not capable of sending IGMP joins, ensure that ip igmp static-group

224.0.1.129 is configured on all PTP-enabled interfaces of a TC.

n The igmp static-group configuration is not needed on BC switches. In this case, it is an L3 network

so ip igmp enable also needs to be configured on all PTP-enabled L3 interfaces of the TC.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

158

PTP commands
| clear     | ptp statistics |     |            |     |
| --------- | -------------- | --- | ---------- | --- |
| clear ptp | statisctics    |     | [<IFNAME>] |     |
Description
ClearsPTPcountersforthegiveninterface.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<IFNAME>
Optional:Specifiestheinterfacename.
Examples
ClearingPTPcountersforthegiveninterface:
| switch#   | clear       | ptp     | statistics | 1/1/8              |
| --------- | ----------- | ------- | ---------- | ------------------ |
| switch#   | clear       | ptp     | statistics | lag1               |
| switch#   | clear       | ptp     | statistics |                    |
| Command   | History     |         |            |                    |
| Release   |             |         |            | Modification       |
| 10.08     |             |         |            | Commandintroduced. |
| Command   | Information |         |            |                    |
| Platforms |             | Command | context    | Authority          |
8360 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
clock-domain
| clock-domain | <DOMAIN-NUMBER> |     |     |     |
| ------------ | --------------- | --- | --- | --- |
no clock-domain
Description
ConfiguresthePTPclockdomaintoaspecifiedvalue.
ThenoformofthiscommandremovesthePTPdomainconfigurationofthePTPclock.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<DOMAIN-NUMBER> SetsthePTPclockdomain.Range:0to254.Valueconfigurable
subjecttolimitsestablishedbythePTPprofile.
Precisiontimeprotocol(PTP)|159

Usage
n Theone-stepend-to-endtransparentclockworksacrossdomains.
n Forboundaryclocks,theclock-domainhastobeidenticalwiththedomainusedinthenetwork.
n AllPTPdevicesmustbewithinsamedomaintobeabletosyncwitheachother.
n ThiscommandisonlyenabledinthePTPprofilecontext.
n ForPTPtransparentclock,youmustconfigurethesameclock-domainasonclientsandGMto
synchronize.
Examples
EnteringthePTPprofilecontextandsettingthePTPclockdomainvalue:
| switch(config)# | ptp | profile aes-r16 |     |
| --------------- | --- | --------------- | --- |
switch(config-ptp)#
| switch(config-ptp)#clock-domain |     |     | 4   |
| ------------------------------- | --- | --- | --- |
switch(config-ptp)#
RemovingthePTPclockdomainvalue:
| switch(config-ptp)# |     | no clock-domain |     |
| ------------------- | --- | --------------- | --- |
switch(config-ptp)#
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.08               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
clock-step
| clock-step {one-step|two-step} |     |     |     |
| ------------------------------ | --- | --- | --- |
no clock-step
Description
Configurestheclockstepmodethatdetermineswhentheegress-timeinformationissent.
The8360SwitchSeriessupportsbothone-stepandtwo-stepmodesforboundaryclocks.For
transparentclocks,onlyone-stepmodeissupported.
ThenoformofthiscommandremovesthePTPclock-stepconfigurationofthePTPclock.
160
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     | Description                                        |
| --------- | --- | --- | -------------------------------------------------- |
| one-step  |     |     | SetsthePTPclock-stepmodetoone-stepmessaginginwhich |
egress-timeinformationissentalongwiththeSYNCmessage.
| two-step |     |     | SetsthePTPclock-stepmodetotwo-stepmessaginginwhich |
| -------- | --- | --- | -------------------------------------------------- |
egress-timeinformationissentasubsequentfollow-upmessage
withtheegresstimestampofthepreviouslysentSYNCmessage.
Usage
n MandatorycommandtostartthePTP clock.
n Boundaryclockscaninter-operatewithdifferentstepmodesupstreamordownstream.
Example
Settingtheclock-stepmodetoone-stepmessaging:
| switch(config-ptp)# |     | clock-step | one-step |
| ------------------- | --- | ---------- | -------- |
Removingtheclock-stepmodeconfiguration:
| switch(config-ptp)# |     | no clock-step |     |
| ------------------- | --- | ------------- | --- |
Settingtheclock-stepmodetotwo-stepmessaging:
switch(config-ptp)#
|                     |         | clock-step | two-step           |
| ------------------- | ------- | ---------- | ------------------ |
| Command History     |         |            |                    |
| Release             |         |            | Modification       |
| 10.08               |         |            | Commandintroduced. |
| Command Information |         |            |                    |
| Platforms           | Command | context    | Authority          |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
enable
enable
no enable
Description
EnablesthePTPprofileglobally.However,thePTPclockisstartedonlywhenallthemandatory
commandsareset.
ThenoformofthiscommanddisablesthePTPprofileglobally.
Precisiontimeprotocol(PTP)|161

Usage
MandatorycommandtostartthePTPclock.
Examples
EnablingthePTPprofile:
| switch(config)#     | ptp | profile | 1588v2 |     |
| ------------------- | --- | ------- | ------ | --- |
| switch(config-ptp)# |     | enable  |        |     |
DisablingthePTPprofile:
| switch(config)#     | ptp     | profile   | 1588v2             |     |
| ------------------- | ------- | --------- | ------------------ | --- |
| switch(config-ptp)# |         | no enable |                    |     |
| Command History     |         |           |                    |     |
| Release             |         |           | Modification       |     |
| 10.08               |         |           | Commandintroduced. |     |
| Command Information |         |           |                    |     |
| Platforms           | Command | context   | Authority          |     |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip source-interface
ip source-interface {ptp | all} interface <IFNAME> [vrf <VRF-NAME>
| ip source-interface | {ptp | | all} | <IPV4-ADDR> | [vrf <VRF-NAME>] |
| ------------------- | ---- | ------ | ----------- | ---------------- |
no ip source-interface {ptp | all} interface <IFNAME> [vrf <VRF-NAME>
no ip source-interface {ptp | all} <IPV4-ADDR> [vrf <VRF-NAME>]
Description
ConfiguresthesourceIPaddresstobeusedwhensendingPTPmessages.Usetheptpkeywordtoset
sourceIPaddressspecifictothePTPfeature.Ifthefeature-specificconfigurationisnotavailable,the
sourceIPaddresscorrespondingtothealloptionwillbeused.
ThenoformofthiscommandremovestheconfigurationofthesourceIPaddressusedbythePTP
feature.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ptp
SelectsthePTPprotocol.
| all       |           |     | Selectsallprotocolsthatcanbeconfiguredbythiscommand. |     |
| --------- | --------- | --- | ---------------------------------------------------- | --- |
| interface | <IF-NAME> |     |                                                      |     |
SpecifiesthenameoftheinterfacefromwhichthesourceIP
addressisobtained.TheinterfacemusthaveavalidIPaddress
assignedtoit.
162
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
IftheinterfacehasbothaprimaryandsecondaryIPaddress,the
primaryIPaddressisused.
| vrf <VRF-NAME> |     |     |     |     | SpecifiestheVRF name. |     |
| -------------- | --- | --- | --- | --- | --------------------- | --- |
<IPV4-ADDR>
SpecifiesthesourceIPv4addresstobeused.
TheIPaddressmustbedefinedontheswitch,anditmustexiston
thespecifiedVRF(whichisthedefaultVRF,ifthevrfoptionisnot
used).SpecifytheaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
Usage
n ThiscommandmustbeconfiguredontheswitchwhenPTPisenabledonVLAN trunkoraccessports,
andthetransportprotocolisIPv4.
n InthecurrentversionofPTP,onlythedefaultVRFissupported.
n Thiscommandisnotapplicabletotheend-to-endtransparentclock.
Examples
ConfiguringthesourceIPaddressforsendingPTPmessages:
| switch(config)# |             | ip  | source-interface |     | ptp interface      | 1/1/1  |
| --------------- | ----------- | --- | ---------------- | --- | ------------------ | ------ |
| switch(config)# |             | ip  | source-interface |     | ptp 10.10.10.1     |        |
| switch(config)# |             | ip  | source-interface |     | ptp interface      | vlan10 |
| Command         | History     |     |                  |     |                    |        |
| Release         |             |     |                  |     | Modification       |        |
| 10.08           |             |     |                  |     | Commandintroduced. |        |
| Command         | Information |     |                  |     |                    |        |
| Platforms       | Command     |     | context          |     | Authority          |        |
config
8360 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mode
| mode boundary       | {end-to-end |             | | peer-to-peer} |                 |               |     |
| ------------------- | ----------- | ----------- | --------------- | --------------- | ------------- | --- |
| no mode boundary    |             | {end-to-end |                 | | peer-to-peer} |               |     |
| mode transparent    |             | {end-to-end |                 | | peer-to-peer} |               |     |
| no mode transparent |             | {end-to-end |                 | |               | peer-to-peer} |     |
no mode
Description
ConfigurestheswitchPTPclockmode,eitherboundaryortransparent,withadelay-requestmechanism
ofeitherend-to-endorpeer-to-peer.Adeviceintransparentclockmodedoesnotsynchronize
(syntonize)itselftoagrandsourceclock.
ThenoformofthiscommandunconfiguresthePTPclockmodeanddelay-requestmechanism.
Precisiontimeprotocol(PTP)|163

| Parameter   |     | Description                                 |
| ----------- | --- | ------------------------------------------- |
| boundary    |     | Selectsboundaryclockmode.                   |
| transparent |     | Selectstransparentclockmode.                |
| end-to-end  |     | Selectstheend-to-enddelay-requestmechanism. |
peer-to-peer Selectsthepeer-to-peerdelay-requestmechanism.Not
supportedwithVSF.
Examples
ConfiguringPTPboundaryclockmodewiththeend-to-enddelay-requestmechanism:
| switch(config-ptp)# | mode boundary | end-to-end |
| ------------------- | ------------- | ---------- |
UnconfiguringPTPboundaryclockmodewiththeend-to-enddelay-requestmechanism:
| switch(config-ptp)# | no mode boundary | end-to-end |
| ------------------- | ---------------- | ---------- |
ConfiguringPTPboundaryclockmodewiththepeer-to-peerdelay-requestmechanism:
| switch(config-ptp)# | mode boundary | peer-to-peer |
| ------------------- | ------------- | ------------ |
UnconfiguringPTPboundaryclockmodewiththepeer-to-peerdelay-requestmechanism:
| switch(config-ptp)# | no mode boundary | peer-to-peer |
| ------------------- | ---------------- | ------------ |
ConfiguringPTPtransparentwiththeend-to-enddelay-requestmechanism:
| switch(config-ptp)# | mode transparent | end-to-end |
| ------------------- | ---------------- | ---------- |
UnconfiguringPTPtransparentwiththeend-to-enddelay-requestmechanism:
| switch(config-ptp)# | no mode transparent | end-to-end |
| ------------------- | ------------------- | ---------- |
ConfiguringPTPtransparentwiththepeer-to-peerdelay-requestmechanism:
| switch(config-ptp)# | mode transparent | peer-to-peer |
| ------------------- | ---------------- | ------------ |
UnconfiguringPTPtransparentwiththepeer-to-peerdelay-requestmechanism:
| switch(config-ptp)# | no mode transparent | peer-to-peer |
| ------------------- | ------------------- | ------------ |
Command History
164
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release |     |     | Modification |
| ------- | --- | --- | ------------ |
10.11
Addedsupportforthepeer-to-peerdelay-requestmechanism.
| 10.08               |         |         | Commandintroduced. |
| ------------------- | ------- | ------- | ------------------ |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
priority1
| priority1 <PRIORITY> |     |     |     |
| -------------------- | --- | --- | --- |
no priority1
Description
ConfiguresthePTPclockpriority1valueofthedevice.Thisvalueisoperationalwhenthedeviceisin
boundaryclockmodeandparticipatingintheBestClockSourceAlgorithm(BMCA).Thisvalueisusedto
indicateprioritytoitsdownstreamclock-awaredevices.
ThenoformofthiscommandremovesthePTPpriority1configurationofthePTPclockandsetsitto
thedefaultvalueof128.
| Parameter  |     |     | Description                      |
| ---------- | --- | --- | -------------------------------- |
| <PRIORITY> |     |     | Setsthepriorityvalue.Default128. |
Usage
Thisvaluecanbeconfiguredonlyfortheboundaryclock.
Examples
ConfiguringPTPpriority1value:
| switch(config-ptp)# |     | priority1 129 |     |
| ------------------- | --- | ------------- | --- |
RemovingPTPpriority1configuration:
| switch(config-ptp)# |     | no priority1 |                    |
| ------------------- | --- | ------------ | ------------------ |
| Command History     |     |              |                    |
| Release             |     |              | Modification       |
| 10.08               |     |              | Commandintroduced. |
| Command Information |     |              |                    |
Precisiontimeprotocol(PTP)|165

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
priority2
| priority2 <PRIORITY> |            |     |     |     |
| -------------------- | ---------- | --- | --- | --- |
| no priority2         | <PRIORITY> |     |     |     |
Description
ConfiguresthePTPclockpriority2valueofthedevice.Thisvalueisoperationalwhenthedeviceisin
boundaryclockmodeandparticipatingintheBestClockSourceAlgorithm(BMCA).Thisvalueisusedto
indicateprioritytoitsdownstreamclock-awaredevices.
ThenoformofthiscommandremovesthePTPpriority2configurationofthePTPclockandsetsitto
thedefaultvalueof128.
| Parameter  |     |     | Description                      |     |
| ---------- | --- | --- | -------------------------------- | --- |
| <PRIORITY> |     |     | Setsthepriorityvalue.Default128. |     |
Usage
Thisvaluecanbeconfiguredonlyfortheboundaryclock.
Examples
ConfiguringPTPpriority1value:
| switch(config-ptp)# |     | priority2 | 129 |     |
| ------------------- | --- | --------- | --- | --- |
RemovingPTPpriority2configuration:
| switch(config-ptp)# |         | no priority2 |                    |     |
| ------------------- | ------- | ------------ | ------------------ | --- |
| Command History     |         |              |                    |     |
| Release             |         |              | Modification       |     |
| 10.08               |         |              | Commandintroduced. |     |
| Command Information |         |              |                    |     |
| Platforms           | Command | context      | Authority          |     |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp announce-interval
ptp announce-interval {1588v2| aes67 | aes-r16 | smpte} <LOG-SECONDS>
| no ptp announce-interval |     | {1588v2| | aes67 | aes-r16 | | smpte} |
| ------------------------ | --- | -------- | --------------- | -------- |
166
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

Description
SetstheannouncemessagetransmitintervalonaPTP-enabledinterfaceforaspecificPTPprofile.
ThenoformofthiscommandremovestheannouncemessagetransmitintervalconfigurationonaPTP-
enabledinterfaceandsetsaprofilespecificdefaultvalue.
| Parameter |     |     |     | Description                                   |     |
| --------- | --- | --- | --- | --------------------------------------------- | --- |
| 1588v2    |     |     |     | SpecifiesthePTP1588v2profiletimers.Default:1. |     |
aes67
SpecifiesthePTPAES67profiletimers.Default:1.
| aes-r16 |     |     |     | SpecifiesthePTPAES-R16profiletimers.Default:1. |     |
| ------- | --- | --- | --- | ---------------------------------------------- | --- |
smpte
SpecifiesthePTPSMTPEprofiletimers.Default:-2.
| <LOG-SECONDS> |     |     |     | Setstheannouncemessageintervalinlogseconds. |     |
| ------------- | --- | --- | --- | ------------------------------------------- | --- |
Usage
Thisvaluecanbeconfiguredonlyfortheboundaryclock.
Examples
SettingthePTPAES67profiletimers:
| switch(config)#    |     | interface | 1/1/1             |     |         |
| ------------------ | --- | --------- | ----------------- | --- | ------- |
| switch(config-if)# |     | ptp       | announce-interval |     | aes67 2 |
RemovingthePTPAES67profiletimerconfiguration:
| switch(config)#     |         | interface | 1/1/1             |                    |       |
| ------------------- | ------- | --------- | ----------------- | ------------------ | ----- |
| switch(config-if)#  |         | no ptp    | announce-interval |                    | aes67 |
| Command History     |         |           |                   |                    |       |
| Release             |         |           |                   | Modification       |       |
| 10.08               |         |           |                   | Commandintroduced. |       |
| Command Information |         |           |                   |                    |       |
| Platforms           | Command | context   |                   | Authority          |       |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp announce-timeout
| ptp announce-timeout    |     | {1588v2| | aes67 | | aes-r16 | | smpte} <COUNT> |
| ----------------------- | --- | -------- | ----- | --------- | ---------------- |
| no ptp announce-timeout |     | {1588v2| |       | aes67 |   | aes-r16 | smpte} |
Description
SetstheannouncemessagereceipttimeoutonaPTP-enabledinterfaceforaspecificPTPprofile.
Precisiontimeprotocol(PTP)|167

ThenoformofthiscommandresetstheannouncemessagereceipttimeoutconfigurationonaPTP-
enabledinterfaceandsetsaprofile-specificdefaultvalue.
| Parameter |     |     |     | Description                                   |     |
| --------- | --- | --- | --- | --------------------------------------------- | --- |
| 1588v2    |     |     |     | SpecifiesthePTP1588v2profiletimers.Default:3. |     |
aes67
SpecifiesthePTPAES67profiletimers.Default:3.
| aes-r16 |     |     |     | SpecifiesthePTPAES-R16profiletimers.Default:3. |     |
| ------- | --- | --- | --- | ---------------------------------------------- | --- |
smpte
SpecifiesthePTPSMTPEprofiletimers.Default:3.
| <LOG-SECONDS> |     |     |     | Specifiesthenumberofannouncementintervals. |     |
| ------------- | --- | --- | --- | ------------------------------------------ | --- |
Usage
Thisvaluecanbeconfiguredonlyfortheboundaryclock.
Examples
SettingthePTPAES67profiletimer:
| switch(config)#    |     | interface | 1/1/1            |     |         |
| ------------------ | --- | --------- | ---------------- | --- | ------- |
| switch(config-if)# |     | ptp       | announce-timeout |     | aes67 4 |
ResettingthePTPAES67profiletimer:
| switch(config)#      |         | interface | 1/1/1            |                    |       |
| -------------------- | ------- | --------- | ---------------- | ------------------ | ----- |
| switch(config-if)#no |         | ptp       | announce-timeout |                    | aes67 |
| Command History      |         |           |                  |                    |       |
| Release              |         |           |                  | Modification       |       |
| 10.08                |         |           |                  | Commandintroduced. |       |
| Command Information  |         |           |                  |                    |       |
| Platforms            | Command | context   |                  | Authority          |       |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp clock-source-only
ptp clock-source-only
no ptp clock-source-only
Description
ConfiguresthePTPportstatetoclock_sourcestate.Thisprohibitstheportfromenteringintoaclock_
sinkorpassivestate.
168
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

Thenoformofthiscommandremovestheclock_sourcestateconfigurationontheportandreturnsit
tonormalBMCAoperation.
Usage
Thiscanonlybeconfiguredfortheboundaryclock.
Examples
Configuringtheclock_sourceonlyrolefortheport:
| switch(config)#    | interface | 1/1/1                 |     |     |
| ------------------ | --------- | --------------------- | --- | --- |
| switch(config-if)# |           | ptp clock-source-only |     |     |
Removingtheconfigurationofclock_sourceonlyrolefortheport:
| switch(config)#     | interface | 1/1/1                    |                    |     |
| ------------------- | --------- | ------------------------ | ------------------ | --- |
| switch(config-if)#  |           | no ptp clock-source-only |                    |     |
| Command History     |           |                          |                    |     |
| Release             |           |                          | Modification       |     |
| 10.10               |           |                          | Commandintroduced. |     |
| Command Information |           |                          |                    |     |
| Platforms           | Command   | context                  | Authority          |     |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp delay-req-interval
ptp delay-req-interval {1588v2 | aes67 | aes-r16 | smpte} <LOG-SECONDS>
| no ptp delay-req-interval |     | {1588v2 | | aes67 | aes-r16 | | smpte} |
| ------------------------- | --- | ------- | ----------------- | -------- |
Description
Setsthedelay_reqmessagetransmitintervalonaPTP-enabledinterfaceforaspecificPTPprofile.
Thenoformofthiscommandremovesthedelay_reqmessagetransmitintervalconfigurationonaPTP-
enabledinterfaceandsetsaprofilespecificdefaultvalue.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
1588v2
SpecifiesthePTP1588v2profiletimers.Default0.
| aes67 |     |     | SpecifiesthePTPAES67profiletimers.Default0. |     |
| ----- | --- | --- | ------------------------------------------- | --- |
aes-r16
SpecifiesthePTPAES-R16profiletimers.Default0.
| smpte |     |     | SpecifiesthePTPSMTPEprofiletimers.Default-3. |     |
| ----- | --- | --- | -------------------------------------------- | --- |
<LOG-SECONDS>
Setsthedelay_reqmessageintervalinlogseconds.
Precisiontimeprotocol(PTP)|169

Usage
n Usethiscommandforend-to-end(E2E)modeandusecommandptp pdelay-intervalforpeer-to-
peermode.
n Thiscommandisonlyforboundaryclock.
Examples
SettingthePTPAES67profiletimers:
| switch(config)#    | interface | 1/1/1                  |     |         |
| ------------------ | --------- | ---------------------- | --- | ------- |
| switch(config-if)# |           | ptp delay-req-interval |     | aes67 2 |
RemovingthePTPAES67profiletimerconfiguration:
| switch(config)#     | interface | 1/1/1                     |                    |       |
| ------------------- | --------- | ------------------------- | ------------------ | ----- |
| switch(config-if)#  |           | no ptp delay-req-interval |                    | aes67 |
| Command History     |           |                           |                    |       |
| Release             |           |                           | Modification       |       |
| 10.08               |           |                           | Commandintroduced. |       |
| Command Information |           |                           |                    |       |
| Platforms           | Command   | context                   | Authority          |       |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp enable
ptp enable
no ptp enable
Description
EnablesPTPontheinterface.ThenoformofthiscommanddisablesPTPontheinterface.
Examples
EnablingPTPonaphysicalinterface:
| switch(config)#    | interface | 1/1/1      |     |     |
| ------------------ | --------- | ---------- | --- | --- |
| switch(config-if)# |           | ptp enable |     |     |
DisablingPTPontheinterfacecontext:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
no ptp enable
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
170
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Release   |             |     |         | Modification       |
| --------- | ----------- | --- | ------- | ------------------ |
| 10.08     |             |     |         | Commandintroduced. |
| Command   | Information |     |         |                    |
| Platforms | Command     |     | context | Authority          |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp lag-role
| ptp lag-role | {primary |     | | secondary} |     |
| ------------ | -------- | --- | ------------ | --- |
no ptp lag-role
Description
ConfiguresthePTProleforthememberinterfacesofaLinkAggregation(LAG).Whentherearetwoor
morememberinterfacesforaLAG,onlyonelinkcanbeconfiguredasprimaryandonlyoneotherlink
canbeconfiguredassecondary.TheprimarymemberinterfaceisusedfortransmittingthePTPpackets
generatedbytheboundaryclock.Whentheprimarymembergoesdown,thesecondarymemberis
usedforPTPpackettransmission.Ifbothprimaryandsecondarymembersgodown,PTPdoesnotflip
overtotheotherlinksoftheLAG.
ThenoformofthiscommandremovesthePTProleconfigurationfortheLAGmemberinterface.
Thiscommandisnotsupportedwhenconfiguredasatransparentclock.
| Parameter |     |     |     | Description                                        |
| --------- | --- | --- | --- | -------------------------------------------------- |
| primary   |     |     |     | SetstheprimaryPTPlag-rolefortheLAGmemberinterface. |
secondary
SetsthesecondaryPTPlag-rolefortheLAGmemberinterface.
Usage
n LAG rolesmustbeconfiguredforboundaryclock.
n FortheprimaryorsecondaryLAGroles,ensurethatthesamelinkportsareconfiguredonbothends
oftheLAG.
Examples
SettingtheprimaryPTPlag-rolefortheLAGmemberinterface:
| switch(config)#    |     | interface | 1/1/1        |         |
| ------------------ | --- | --------- | ------------ | ------- |
| switch(config-if)# |     |           | ptp lag-role | primary |
SettingthesecondaryPTPlag-rolefortheLAGmemberinterface:
Precisiontimeprotocol(PTP)|171

| switch(config)# | interface | 1/1/2 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|     |     | ptp lag-role | secondary |     |
| --- | --- | ------------ | --------- | --- |
RemovingthePTPlag-roleconfigurationfortheLAGmemberinterface:
| switch(config)#     | interface | 1/1/1           |                    |     |
| ------------------- | --------- | --------------- | ------------------ | --- |
| switch(config-if)#  |           | no ptp lag-role |                    |     |
| Command History     |           |                 |                    |     |
| Release             |           |                 | Modification       |     |
| 10.08               |           |                 | Commandintroduced. |     |
| Command Information |           |                 |                    |     |
| Platforms           | Command   | context         | Authority          |     |
config-if
8360 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp pdelay-req-interval
ptp pdelay-req-interval {1588v2 | aes67 | aes-r16 | smpte} <LOG-SECONDS>
| no ptp pdelay-req-interval |     | {1588v2 | | aes67 | aes-r16 | | smpte} |
| -------------------------- | --- | ------- | ----------------- | -------- |
Description
Setsthepdelay_reqmessagetransmitintervalonaPTP-enabledinterfaceforaspecificPTPprofile.
Thenoformofthiscommandremovesthepdelay_reqmessagetransmitintervalconfigurationona
PTP-enabledinterfaceandsetsaprofilespecificdefaultvalue.
| Parameter     |     |     | Description                                   |     |
| ------------- | --- | --- | --------------------------------------------- | --- |
| 1588v2        |     |     | SpecifiesthePTP1588v2profiletimers.Default0.  |     |
| aes67         |     |     | SpecifiesthePTPAES67profiletimers.Default0.   |     |
| aes-r16       |     |     | SpecifiesthePTPAES-R16profiletimers.Default0. |     |
| smpte         |     |     | SpecifiesthePTPSMTPEprofiletimers.Default-3.  |     |
| <LOG-SECONDS> |     |     | Setsthedelay_reqmessageintervalinlogseconds.  |     |
Usage
n Usethiscommandforpeer-to-peer(P2P)modeandusecommandptp delay-intervalforend-to-
end(E2E)mode.
Examples
SettingthePTPAES67profiletimers:
172
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|     |     | ptp pdelay-req-interval |     | aes67 1 |
| --- | --- | ----------------------- | --- | ------- |
RemovingthePTPAES67profiletimerconfiguration:
| switch(config)#    | interface | 1/1/1                      |     |       |
| ------------------ | --------- | -------------------------- | --- | ----- |
| switch(config-if)# |           | no ptp pdelay-req-interval |     | aes67 |
SettingthePTPsmpteprofiletimers:
| switch(config)#    | interface | 1/1/1                   |     |         |
| ------------------ | --------- | ----------------------- | --- | ------- |
| switch(config-if)# |           | ptp pdelay-req-interval |     | smpte 1 |
RemovingthePTPsmpteprofiletimerconfiguration:
| switch(config)#     | interface | 1/1/1                      |                    |       |
| ------------------- | --------- | -------------------------- | ------------------ | ----- |
| switch(config-if)#  |           | no ptp pdelay-req-interval |                    | smpte |
| Command History     |           |                            |                    |       |
| Release             |           |                            | Modification       |       |
| 10.11               |           |                            | Commandintroduced. |       |
| Command Information |           |                            |                    |       |
| Platforms           | Command   | context                    | Authority          |       |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ptp peer    | ip              |     |     |     |
| ----------- | --------------- | --- | --- | --- |
| ptp peer ip | <IP-ADDRESS>    |     |     |     |
| no ptp peer | ip <IP-ADDRESS> |     |     |     |
Description
ConfiguresdestinationIPaddressesfortheinterfacesinunicasttransmission.Thenoformofthis
commandremovesthePTPdestinationIPaddressconfigurationfortheinterfacesinunicast
transmission.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ip <IP-ADDRESS>
SpecifiesthepeerIPv4address.Syntax:A.B.C.D
Usage
n Thiscommandhasnoeffectwhenconfiguredasatransparentclock.
Example
Precisiontimeprotocol(PTP)|173

| Configuringptp     | peer        | ipontheinterface: |          |       |                    |
| ------------------ | ----------- | ----------------- | -------- | ----- | ------------------ |
| switch(config)#    |             | interface         |          | 1/1/1 |                    |
| switch(config-if)# |             |                   | ptp peer | ip    | 10.0.0.1           |
| Removingptp        | peer        | ipontheinterface: |          |       |                    |
| switch(config-if)# |             |                   | no ptp   | peer  | ip 10.0.0.1        |
| Command            | History     |                   |          |       |                    |
| Release            |             |                   |          |       | Modification       |
| 10.08              |             |                   |          |       | Commandintroduced. |
| Command            | Information |                   |          |       |                    |
| Platforms          | Command     |                   | context  |       | Authority          |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp profile
| ptp profile | {<PROFILE |     | NAME>} |     |     |
| ----------- | --------- | --- | ------ | --- | --- |
no PTP profile
Description
EntersthePTPcontexttoconfigurethePTPprofileinwhichthedevicewilloperate.
ConfigurePTPprofilebeforeconfiguringmodeorotherprofile-specificparameters.Thedevicecanbe
operatinginanyoneprofileatagivenpointoftime.ThenoformofthiscommandremovesthePTP
profileconfigurationinwhichthedevicewilloperate.ThiscommandclearsthePTPprofileandall
parametersrelatedtothatprofile.
| Parameter |       |     |     |     | Description                                              |
| --------- | ----- | --- | --- | --- | -------------------------------------------------------- |
| <PROFILE  | NAME> |     |     |     | Specifiestheprofiletobeused.Profilesinclude:             |
|           |       |     |     |     | n 1588v2: SpecifiestheIEEE1588-2008profiletobeused.      |
|           |       |     |     |     | n aes-r16: SpecifiestheIEEEAES-R16-2016profiletobeused.  |
|           |       |     |     |     | n aes67:SpecifiestheIEEEAES67profiletobeused.            |
|           |       |     |     |     | n smpte: SpecifiestheIEEESMPTE-ST-2059-2profiletobeused. |
Usage
ConfigurePTPprofilebeforeconfiguringmodeorotherprofile-specificparameters.
Example
ConfiguringPTPprofiles:
| switch(config)# |     | ptp | profile | 1588v2 |     |
| --------------- | --- | --- | ------- | ------ | --- |
174
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

ConfiguringmorethanonePTPprofile:
| switch(config)#     |     | ptp | profile 1588v2 |     |
| ------------------- | --- | --- | -------------- | --- |
| switch(config-ptp)# |     |     | exit           |     |
| switch(config)#     |     | ptp | profile smpte  |     |
switch(config-ptp)#
The existing profile must be removed using the 'no ptp profile' command before
| configuring | a   | different | profile. |     |
| ----------- | --- | --------- | -------- | --- |
RemovingthePTPprofile:
| switch(config-ptp)# |         |     | no ptp profile |                    |
| ------------------- | ------- | --- | -------------- | ------------------ |
| Command History     |         |     |                |                    |
| Release             |         |     |                | Modification       |
| 10.08               |         |     |                | Commandintroduced. |
| Command Information |         |     |                |                    |
| Platforms           | Command |     | context        | Authority          |
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp sync-interval
| ptp sync-interval {1588v2| |     |         | aes67 | | smpte} <LOG-SECONDS> |
| -------------------------- | --- | ------- | ------- | -------------------- |
| no ptp sync-interval       |     | {1588v2 | | aes67 | | smpte}             |
Description
SetsthesyncmessagetransmitintervalonaPTP-enabledinterfaceforaspecificPTPprofile.
ThenoformofthiscommandremovesthesyncmessagetransmitintervalconfigurationonaPTP
enabledinterfaceandsetsittoaprofile-specificdefaultvalue.
| Parameter |     |     |     | Description                                  |
| --------- | --- | --- | --- | -------------------------------------------- |
| 1588v2    |     |     |     | SpecifiesthePTP1588v2profiletimers.Default0. |
aes67
SpecifiesthePTPAES67profiletimers.Default-3.
| smpte |     |     |     | SpecifiesthePTPSMTPEprofiletimers.Default-3 |
| ----- | --- | --- | --- | ------------------------------------------- |
<LOG-SECONDS>
Setsthesyncmessageintervalinlogseconds.
Examples
SettingthePTP1588v2syncinterval:
Precisiontimeprotocol(PTP)|175

| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|     |     | ptp | sync-interval |     | 1588v2 2 |
| --- | --- | --- | ------------- | --- | -------- |
SettingthePTPAES67syncinterval:
| switch(config)#    |     | interface | 1/1/1         |     |          |
| ------------------ | --- | --------- | ------------- | --- | -------- |
| switch(config-if)# |     | ptp       | sync-interval |     | aes67 -2 |
RemovingthePTP AES67syncinterval:
| switch(config)#     |         | interface | 1/1/1         |                    |       |
| ------------------- | ------- | --------- | ------------- | ------------------ | ----- |
| switch(config-if)#  |         | no ptp    | sync-interval |                    | aes67 |
| Command History     |         |           |               |                    |       |
| Release             |         |           |               | Modification       |       |
| 10.08               |         |           |               | Commandintroduced. |       |
| Command Information |         |           |               |                    |       |
| Platforms           | Command | context   |               | Authority          |       |
8360 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ptp vlan
| ptp vlan <VLAN-ID> |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
no ptp vlan
Description
ConfiguresaVLANforPTPmessages.ItisnecessarywhentheboundaryclockportisaVLANtrunkL2
interface(no routing).ThenoformofthiscommandremovestheVLANconfigurationforPTP
messages.
| Parameter |     |     |     | Description                  |     |
| --------- | --- | --- | --- | ---------------------------- | --- |
| <VLAN-ID> |     |     |     | SpecifiesaVLAN.Range:1-4094. |     |
Usage
n Thisconfigurationhasnobearingontheone-steptransparentclock.
n Inboundaryclockmode,onlyPTPpacketsinPTPVLANareprocessed;PTPpacketsfromotherVLANs
aredropped.
n ptp vlanshouldbeconfiguredoninterfacesonlywhenthespecificVLANisatrunk/taggedmember
ofthatport.Thisconfigurationshouldnotbeperformedonanaccessport.
Examples
ConfiguringaspecificVLANforPTP messages:
176
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
|     |     |     | ptp vlan 4 |     |
| --- | --- | --- | ---------- | --- |
RemovingtheVLANconfigurationforPTPmessages:
| switch(config)#    |             | interface | 1/1/1       |                    |
| ------------------ | ----------- | --------- | ----------- | ------------------ |
| switch(config-if)# |             |           | no ptp vlan |                    |
| Command            | History     |           |             |                    |
| Release            |             |           |             | Modification       |
| 10.08              |             |           |             | Commandintroduced. |
| Command            | Information |           |             |                    |
| Platforms          | Command     |           | context     | Authority          |
config-if
8360 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ptp       | clock |     |     |     |
| -------------- | ----- | --- | --- | --- |
| show ptp clock |       |     |     |     |
Description
ShowsPTPclock-relatedinformation.
Example
ShowingPTPtransparentclockinformation:
| switch#         | show              | ptp clock |          |               |
| --------------- | ----------------- | --------- | -------- | ------------- |
| PTP Profile     |                   |           |          | : smpte       |
| PTP Mode        |                   |           |          | : transparent |
| Delay Mechanism |                   |           |          | : end-to-end  |
| Clock Identity  |                   |           |          | : NA          |
| Network         | Transport         |           | Protocol | : ipv4        |
| Clock Step      |                   |           |          | : One         |
| Clock Domain    |                   |           |          | : NA          |
| Number          | of PTP            | Ports     |          | : 1           |
| Priority1       |                   |           |          | : NA          |
| Priority2       |                   |           |          | : NA          |
| Clock Quality   |                   | :         |          |               |
| Class           |                   |           |          | : NA          |
| Accuracy        |                   |           |          | : NA          |
| Offset          | (log              | variance) |          | : NA          |
| Offset          | From Clock-Source |           |          | : NA          |
| Mean Delay      |                   |           |          | : NA          |
| Steps Removed   |                   |           |          | : NA          |
ShowingPTPboundaryclockinformation:
Precisiontimeprotocol(PTP)|177

| switch#     | show ptp          | clock    |                           |     |     |
| ----------- | ----------------- | -------- | ------------------------- | --- | --- |
| PTP Profile |                   |          | : aes67                   |     |     |
| PTP Mode    |                   |          | : boundary                |     |     |
| Delay       | Mechanism         |          | : end-to-end              |     |     |
| Clock       | Identity          |          | : 00:fd:45:ff:fe:68:f3:00 |     |     |
| Network     | Transport         | Protocol | : ipv4                    |     |     |
| Clock       | Step              |          | : Two                     |     |     |
| Clock       | Domain            |          | : 0                       |     |     |
| Number      | of PTP Ports      |          | : 3                       |     |     |
| Priority1   |                   |          | : 128                     |     |     |
| Priority2   |                   |          | : 128                     |     |     |
| Clock       | Quality :         |          |                           |     |     |
| Class       |                   |          | : 248                     |     |     |
| Accuracy    |                   |          | : 49                      |     |     |
| Offset      | (log variance)    |          | : 52592                   |     |     |
| Offset      | From Clock-Source |          | : - 0.000000006           |     | (s) |
| Mean Delay  |                   |          | : + 0.000000277           |     | (s) |
| Steps       | Removed           |          | : 1                       |     |     |
| Command     | History           |          |                           |     |     |
| Release     |                   |          | Modification              |     |     |
| 10.08       |                   |          | Commandintroduced.        |     |     |
| Command     | Information       |          |                           |     |     |
| Platforms   | Command           | context  | Authority                 |     |     |
8360 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show ptp                       | foreign-clock-sources |     |     |     |     |
| ------------------------------ | --------------------- | --- | --- | --- | --- |
| show ptp foreign-clock-sources |                       |     |     |     |     |
Description
Showsthepriority1,priority2,class,accuracy,offset-scaled-log-variance(OSLV),andstepsremoved
informationforforeignclock-sourcenodes.
Example
ShowingPTPforeignclock-sourceinformation:
| switch(config-if)#               | show          | ptp foreign-clock-sources |     |     |     |
| -------------------------------- | ------------- | ------------------------- | --- | --- | --- |
| P1=Priority1,                    | P2=Priority2, | C=Class, A=Accuracy,      |     |     |     |
| OSLV=Offset-scaled-log-variance, |               | SR=Steps-removed          |     |     |     |
---------- -------------------------------- ------------------------ ---- ---- ---- ---- ------ ---
| Interface | Foreign Port | ID  | Clock Source ID | P1 P2 | C A OSLV SR |
| --------- | ------------ | --- | --------------- | ----- | ----------- |
---------- -------------------------------- ------------------------ ---- ---- ---- ---- ------ ---
1/1/4 00:00:00:00:00:00:00:01(0x0001) 00:00:00:00:00:00:00:01 0 0 6 35 0 1
1/1/5 b4:99:ba:ff:fe:54:2b:00(0x0002) 00:00:00:00:00:00:00:01 0 0 6 35 0 2
178
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

| Command   | History     |     |         |     |                    |     |     |
| --------- | ----------- | --- | ------- | --- | ------------------ | --- | --- |
| Release   |             |     |         |     | Modification       |     |     |
| 10.08     |             |     |         |     | Commandintroduced. |     |     |
| Command   | Information |     |         |     |                    |     |     |
| Platforms | Command     |     | context |     | Authority          |     |     |
8360 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show ptp           | interface |           |     |           |     |     |     |
| ------------------ | --------- | --------- | --- | --------- | --- | --- | --- |
| show ptp interface |           | [<IFNAME> |     | | [brief] |     |     |     |
Description
ShowsPTPport-relatedinformation.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<IFNAME>
Specifiestheinterfacename.
| brief |     |     |     |     | Showsinformationinabriefformat. |     |     |
| ----- | --- | --- | --- | --- | ------------------------------- | --- | --- |
Examples
ShowingPTPportinformationwhentheswitchisactingasatransparentclock:
| switch#         | show     | ptp interface |            | 1/1/1 |       |                           |          |
| --------------- | -------- | ------------- | ---------- | ----- | ----- | ------------------------- | -------- |
| Port Identity   |          |               |            |       |       | : 00:00:00:00:00:00:00:00 | (0x0000) |
| Port Number     |          |               |            |       |       | : 0                       |          |
| PTP Version     |          |               |            |       |       | : 2                       |          |
| PTP Enable      |          |               |            |       |       | : Enabled                 |          |
| PTP Transport   |          |               |            |       |       | : ipv4                    |          |
| Port State      |          |               |            |       |       | : Disabled                |          |
| Delay Mechanism |          |               |            |       |       | : peer-to-peer            |          |
| Announce        | Interval |               | (log mean) |       |       | : 0                       |          |
| Announce        | Receipt  | Timeout       |            |       |       | : 0                       |          |
| Sync Interval   |          | (log          | mean)      |       |       | : 0                       |          |
| Sync Timeout    |          |               |            |       |       | : NA                      |          |
| Delay Request   |          | Interval      | (log       | mean) |       | : NA                      |          |
| Peer Delay      | Request  |               | Interval   | (log  | mean) | : 0                       |          |
| Mean Path       | Delay    |               |            |       |       | : 0 (ns)                  |          |
switch#
| switch#         | show | ptp interface |     | lag20 |     |              |     |
| --------------- | ---- | ------------- | --- | ----- | --- | ------------ | --- |
| Port Identity   |      |               |     |       |     | : NA         |     |
| Port Number     |      |               |     |       |     | : NA         |     |
| PTP Version     |      |               |     |       |     | : 2          |     |
| PTP Enable      |      |               |     |       |     | : Enabled    |     |
| Transport       | of   | PTP           |     |       |     | : ipv4       |     |
| Port State      |      |               |     |       |     | : NA         |     |
| Delay Mechanism |      |               |     |       |     | : end-to-end |     |
Precisiontimeprotocol(PTP)|179

| Announce      | Interval (log mean) |            | : NA     |     |
| ------------- | ------------------- | ---------- | -------- | --- |
| Announce      | Receipt Timeout     |            | : NA     |     |
| Sync Interval | (log mean)          |            | : NA     |     |
| Sync Timeout  |                     |            | : NA     |     |
| Delay Request | Interval (log       | mean)      | : N      |     |
| Peer Delay    | Request Interval    | (log mean) | : 0      |     |
| Mean Path     | Delay               |            | : 0 (ns) |     |
switch#
ShowingPTPportinformationwhentheswitchisactingasaboundaryclock:
| switch#         | show ptp interface  | 1/1/1      |                           |                |
| --------------- | ------------------- | ---------- | ------------------------- | -------------- |
| Interface       | : 1/1/1             |            |                           |                |
| Port Identity   |                     |            | : 88:3a:30:ff:fe:05:c9:80 | (port: 0x0002) |
| Port Number     |                     |            | : 2                       |                |
| PTP Version     |                     |            | : 2                       |                |
| PTP Enable      |                     |            | : Enabled                 |                |
| Transport       | of PTP              |            | : ethernet                |                |
| Port State      |                     |            | : Clock Source            |                |
| Delay Mechanism |                     |            | : end-to-end              |                |
| Announce        | Interval (log mean) |            | : 0                       |                |
| Announce        | Receipt Timeout     |            | : 3                       |                |
| Sync Interval   | (log mean)          |            | : -3                      |                |
| Sync Timeout    |                     |            | : NA                      |                |
| Delay Request   | Interval (log       | mean)      | : 0                       |                |
| Peer Delay      | Request Interval    | (log mean) | : 0                       |                |
| Mean Path       | Delay               |            | : 0 (ns)                  |                |
| switch#         | show ptp interface  | lag1       |                           |                |
| Port Identity   |                     |            | : 00:fd:45:ff:fe:68:f3:00 | (port: 0x0002) |
| Port Number     |                     |            | : 2                       |                |
| PTP Version     |                     |            | : 2                       |                |
| PTP Enable      |                     |            | : Enabled                 |                |
| Transport       | of PTP              |            | : ipv4                    |                |
| Port State      |                     |            | : Clock Source            |                |
| Delay Mechanism |                     |            | : end-to-end              |                |
| Announce        | Interval (log mean) |            | : 0                       |                |
| Announce        | Receipt Timeout     |            | : 3                       |                |
| Sync Interval   | (log mean)          |            | : -3                      |                |
| Sync Timeout    |                     |            | : NA                      |                |
| Delay Request   | Interval (log       | mean)      | : -3                      |                |
| Peer Delay      | Request Interval    | (log mean) | : 0                       |                |
| Mean Path       | Delay               |            | : 0 (ns)                  |                |
| Primary         | Interface           |            | : 1/1/5                   |                |
| Secondary       | Interface           |            | : 1/1/6                   |                |
| switch#         | show ptp interface  |            |                           |                |
| Interface       | lag20:              |            |                           |                |
| Port Identity   |                     |            | : 00:fd:45:ff:fe:68:f3:00 | (port: 0x0002) |
| Port Number     |                     |            | : 2                       |                |
| PTP Version     |                     |            | : 2                       |                |
| PTP Enable      |                     |            | : Enabled                 |                |
| Transport       | of PTP              |            | : ipv4                    |                |
| Port State      |                     |            | : Clock Source            |                |
| Delay Mechanism |                     |            | : end-to-end              |                |
| Announce        | Interval (log mean) |            | : 0                       |                |
| Announce        | Receipt Timeout     |            | : 3                       |                |
| Sync Interval   | (log mean)          |            | : -3                      |                |
| Sync Timeout    |                     |            | : NA                      |                |
| Delay Request   | Interval (log       | mean)      | : -3                      |                |
| Peer Delay      | Request Interval    | (log mean) | : 0                       |                |
180
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Mean Path       | Delay               |            | : 0 (ns)                  |                |
| --------------- | ------------------- | ---------- | ------------------------- | -------------- |
| Primary         | Interface           |            | : 1/1/5                   |                |
| Secondary       | Interface           |            | : 1/1/6                   |                |
| Member          | Interface 1/1/5:    |            |                           |                |
| Port Identity   |                     |            | : 00:fd:45:ff:fe:68:f3:00 | (port: 0x0002) |
| Port Number     |                     |            | : 2                       |                |
| PTP Version     |                     |            | : 2                       |                |
| PTP Enable      |                     |            | : Enabled                 |                |
| Transport       | of PTP              |            | : ipv4                    |                |
| Port State      |                     |            | : Running                 |                |
| Delay Mechanism |                     |            | : end-to-end              |                |
| Announce        | Interval (log mean) |            | : 0                       |                |
| Announce        | Receipt Timeout     |            | : 3                       |                |
| Sync Interval   | (log mean)          |            | : -3                      |                |
| Sync Timeout    |                     |            | : NA                      |                |
| Delay Request   | Interval (log       | mean)      | : -3                      |                |
| Peer Delay      | Request Interval    | (log mean) | : 0                       |                |
| Mean Path       | Delay               |            | : 0 (ns)                  |                |
| Member          | Interface 1/1/6:    |            |                           |                |
| Port Identity   |                     |            | : 00:fd:45:ff:fe:68:f3:00 | (port: 0x0003) |
| Port Number     |                     |            | : 3                       |                |
| PTP Version     |                     |            | : 2                       |                |
| PTP Enable      |                     |            | : Enabled                 |                |
| Transport       | of PTP              |            | : ipv4                    |                |
| Port State      |                     |            | : Not Running             |                |
| Delay Mechanism |                     |            | : end-to-end              |                |
| Announce        | Interval (log mean) |            | : 0                       |                |
| Announce        | Receipt Timeout     |            | : 3                       |                |
| Sync Interval   | (log mean)          |            | : -3                      |                |
| Sync Timeout    |                     |            | : NA                      |                |
| Delay Request   | Interval (log       | mean)      | : -3                      |                |
| Peer Delay      | Request Interval    | (log mean) | : 0                       |                |
| Mean Path       | Delay               |            | : 0 (ns)                  |                |
| Interface       | 1/1/15:             |            |                           |                |
| Port Identity   |                     |            | : 00:fd:45:ff:fe:68:f3:00 | (port: 0x0001) |
| Port Number     |                     |            | : 1                       |                |
| PTP Version     |                     |            | : 2                       |                |
| PTP Enable      |                     |            | : Enabled                 |                |
| Transport       | of PTP              |            | : ipv4                    |                |
| Port State      |                     |            | : Clock Sink              |                |
| Delay Mechanism |                     |            | : end-to-end              |                |
| Announce        | Interval (log mean) |            | : 0                       |                |
| Announce        | Receipt Timeout     |            | : 3                       |                |
| Sync Interval   | (log mean)          |            | : -3                      |                |
| Sync Timeout    |                     |            | : NA                      |                |
| Delay Request   | Interval (log       | mean)      | : -3                      |                |
| Peer Delay      | Request Interval    | (log mean) | : 0                       |                |
| Mean Path       | Delay               |            | : 0 (ns)                  |                |
ShowingPTPportinformation(inbriefform)whentheswitchisactingasaboundaryclock:
| switch#   | show ptp interface | brief |     |     |
| --------- | ------------------ | ----- | --- | --- |
| Interface | PTP State          |       |     |     |
--------------------------
| 1/1/11 | Clock Sink   |     |     |     |
| ------ | ------------ | --- | --- | --- |
| 1/1/12 | Clock Source |     |     |     |
| 1/1/15 | Clock Source |     |     |     |
| 1/1/16 | Clock Source |     |     |     |
Precisiontimeprotocol(PTP)|181

ShowingPTPportinformationinbriefformat:
| switch#   | show ptp interface |     | brief |     |     |
| --------- | ------------------ | --- | ----- | --- | --- |
| Interface | PTP State          |     |       |     |     |
-------------------------
| 1/1/11              | Clock   | Source  |     |                    |     |
| ------------------- | ------- | ------- | --- | ------------------ | --- |
| 1/1/12              | Clock   | Sink    |     |                    |     |
| 1/1/13              | Passive |         |     |                    |     |
| Command History     |         |         |     |                    |     |
| Release             |         |         |     | Modification       |     |
| 10.08               |         |         |     | Commandintroduced. |     |
| Command Information |         |         |     |                    |     |
| Platforms           | Command | context |     | Authority          |     |
8360 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show ptp        | parent |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- |
| show ptp parent |        |     |     |     |     |
Description
ShowsparentnodeinformationforthePTPdevice.
Example
ShowingPTPparentnodeinformation:
| switch#      | show ptp parent |     |     |     |     |
| ------------ | --------------- | --- | --- | --- | --- |
| PTP Parent   | Properties      |     |     |     |     |
| Parent Clock |                 |     |     |     |     |
----------------------------
| Parent Clock | Identity      |       |           |       | : 00:00:00:00:00:00:00:01 |
| ------------ | ------------- | ----- | --------- | ----- | ------------------------- |
| Parent Port  | Number        |       |           |       | : 0x0001                  |
| Observed     | Parent Offset | (log  | variance) |       | : 65535                   |
| Observed     | Parent Clock  | Phase | Change    | Rate: | 2147483647                |
| Grandsource  | Clock         |       |           |       |                           |
----------------------------
| Grandsource     | Clock          | Identity |     |     | : 00:00:00:00:00:00:00:01 |
| --------------- | -------------- | -------- | --- | --- | ------------------------- |
| Grandsource     | Clock          | Quality  |     |     |                           |
| Class           |                |          |     |     | : 6                       |
| Accuracy        |                |          |     |     | : 35                      |
| Offset          | (log variance) |          |     |     | : 0                       |
| Priority1       |                |          |     |     | : 0                       |
| Priority2       |                |          |     |     | : 0                       |
| Command History |                |          |     |     |                           |
182
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| Release             |         |         | Modification       |           |     |     |
| ------------------- | ------- | ------- | ------------------ | --------- | --- | --- |
| 10.08               |         |         | Commandintroduced. |           |     |     |
| Command Information |         |         |                    |           |     |     |
| Platforms           | Command | context |                    | Authority |     |     |
8360 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show ptp            | statistics |     |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- | --- |
| show ptp statistics | [<IFNAME>] |     |     |     |     |     |
Description
ShowsPTPportstatistics.
| Parameter |     |     | Description                         |     |     |     |
| --------- | --- | --- | ----------------------------------- | --- | --- | --- |
| <IFNAME>  |     |     | Optional.Specifiestheinterfacename. |     |     |     |
Examples
ShowingPTPportstatistics:
| switch# show       | ptp statistics |         |              |                   |              |     |
| ------------------ | -------------- | ------- | ------------ | ----------------- | ------------ | --- |
| PTP Interface      | Statistics     |         |              |                   |              |     |
|                    | Received       | Packets | Sent Packets | Discarded Packets | Lost Packets |     |
| Interface:         | 1/1/15         |         |              |                   |              |     |
| Announce           |                | 0       |              | 1019              | 0            | 0   |
| Sync               |                | 0       |              | 2038              | 0            | 0   |
| Signaling          |                | 0       |              | 0                 | 0            | 0   |
| DelayReq           |                | 0       |              | 0                 | 0            | 0   |
| DelayResp          |                | 0       |              | 0                 | 0            | 0   |
| FollowUp           |                | 0       |              | 0                 | 0            | 0   |
| PdelayReq          |                | 81957   | 655750       |                   | 0            | 0   |
| PdelayResp         |                | 655750  |              | 81957             | 0            | 0   |
| PdelayRespFollowUp |                | 655749  |              | 81957             | 0            | 0   |
| Management         |                | 0       |              | 0                 | 0            | 0   |
|                    | Received       | Packets | Sent Packets | Discarded Packets | Lost Packets |     |
| Interface:         | 1/1/16         |         |              |                   |              |     |
| Announce           |                | 0       |              | 1019              | 0            | 0   |
| Sync               |                | 0       |              | 2038              | 0            | 0   |
| Signaling          |                | 0       |              | 0                 | 0            | 0   |
| DelayReq           |                | 0       |              | 0                 | 0            | 0   |
| DelayResp          |                | 0       |              | 0                 | 0            | 0   |
| FollowUp           |                | 0       |              | 0                 | 0            | 0   |
| PdelayReq          |                | 81957   | 655750       |                   | 0            | 0   |
| PdelayResp         |                | 655750  |              | 81957             | 0            | 0   |
| PdelayRespFollowUp |                | 655749  |              | 81957             | 0            | 0   |
| Management         |                | 0       |              | 0                 | 0            | 0   |
Precisiontimeprotocol(PTP)|183

ShowingPTPportstatisticsforthespecifiedinterface:
|           | switch# show       | ptp         | statistics | 1/1/15  |      |                    |                   |              |     |
| --------- | ------------------ | ----------- | ---------- | ------- | ---- | ------------------ | ----------------- | ------------ | --- |
|           | PTP Interface      | Statistics  |            |         |      |                    |                   |              |     |
|           |                    |             | Received   | Packets | Sent | Packets            | Discarded Packets | Lost Packets |     |
|           | Interface:         | 1/1/15      |            |         |      |                    |                   |              |     |
|           | Announce           |             |            |         | 0    | 1024               |                   | 0            | 0   |
|           | Sync               |             |            |         | 0    | 2048               |                   | 0            | 0   |
|           | Signaling          |             |            |         | 0    | 0                  |                   | 0            | 0   |
|           | DelayReq           |             |            |         | 0    | 0                  |                   | 0            | 0   |
|           | DelayResp          |             |            |         | 0    | 0                  |                   | 0            | 0   |
|           | FollowUp           |             |            |         | 0    | 0                  |                   | 0            | 0   |
|           | PdelayReq          |             |            | 81957   |      | 655750             |                   | 0            | 0   |
|           | PdelayResp         |             |            | 655750  |      | 81957              |                   | 0            | 0   |
|           | PdelayRespFollowUp |             |            | 655749  |      | 81957              |                   | 0            | 0   |
|           | Management         |             |            |         | 0    | 0                  |                   | 0            | 0   |
| Command   |                    | History     |            |         |      |                    |                   |              |     |
| Release   |                    |             |            |         |      | Modification       |                   |              |     |
| 10.08     |                    |             |            |         |      | Commandintroduced. |                   |              |     |
| Command   |                    | Information |            |         |      |                    |                   |              |     |
| Platforms |                    | Command     |            | context |      | Authority          |                   |              |     |
8360 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ptp               | time-property |     |     |     |     |     |     |     |
| ---- | ----------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| show | ptp time-property |               |     |     |     |     |     |     |     |
Description
ShowsPTPclock-timepropertiesforthePTPdevice.
Example
ShowingPTPclocktimeproperties:
|     | switch    | # show | ptp      | time-property |     |     |     |     |     |
| --- | --------- | ------ | -------- | ------------- | --- | --- | --- | --- | --- |
|     | PTP Clock | Time   | Property |               |     |     |     |     |     |
----------------------------
|         | Current         | UTC Offset |           | Valid | : FALSE |     |     |     |     |
| ------- | --------------- | ---------- | --------- | ----- | ------- | --- | --- | --- | --- |
|         | Current         | UTC Offset |           |       | : 37    |     |     |     |     |
|         | Leap59          |            |           |       | : FALSE |     |     |     |     |
|         | Leap61          |            |           |       | : FALSE |     |     |     |     |
|         | Time Traceable  |            |           |       | : FALSE |     |     |     |     |
|         | Frequency       | Traceable  |           |       | : FALSE |     |     |     |     |
|         | PTP Timescale   |            |           |       | : FALSE |     |     |     |     |
|         | Synchronization |            | Uncertain |       | : FALSE |     |     |     |     |
|         | Time Source     |            |           |       | : 160   |     |     |     |     |
| Command |                 | History    |           |       |         |     |     |     |     |
184
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.08               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8360 Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show running-config |     | ptp |     |
| ------------------- | --- | --- | --- |
| show running-config | ptp |     |     |
Description
ShowsPTPrunningconfigurationrelatedinformation.
Example
ShowingPTPrunningconfigurationinformation:
| switch#     | show running-config |     | ptp |
| ----------- | ------------------- | --- | --- |
| ptp profile | smpte               |     |     |
enable
clock-step two-step
transport-protocol ipv4
mode boundary peer-to-peer
| interface | 1/1/15 |     |     |
| --------- | ------ | --- | --- |
no shutdown
ip address 30.1.1.1/16
ptp enable
| Command History     |         |         |                                                     |
| ------------------- | ------- | ------- | --------------------------------------------------- |
| Release             |         |         | Modification                                        |
| 10.08orlater        |         |         | Commandintroduced.                                  |
| Command Information |         |         |                                                     |
| Platforms           | Command | context | Authority                                           |
| 8360                |         |         | AuditorsorAdministratorsorlocalusergroupmemberswith |
Manager(#)
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
transport-protocol
| transport-protocol | {ethernet |     | | ipv4} |
| ------------------ | --------- | --- | ------- |
no transport-protocol
Precisiontimeprotocol(PTP)|185

Description
SetsthetransportprotocolforPTPpackets.InthecaseofIPv4,theUDPcheck-sumisreset.Thereisno
defaulttransport-protocol.Thenoformofthiscommanddisconnectstheclockfromitssource.
| Parameter |     |     | Description                                    |
| --------- | --- | --- | ---------------------------------------------- |
| ethernet  |     |     | SpecifiestheEthernet(Layer2)transportprotocol. |
| ipv4      |     |     | SpecifiestheIPv4transportprotocol.             |
Usage
MandatorycommandtostartthePTPclock.
Example
SettingtheEthernettransportprotocolforPTPpackets:
| switch(config-ptp)# |     | transport-protocol | ethernet |
| ------------------- | --- | ------------------ | -------- |
RemovingthetransportprotocolforPTPpackets:
| switch(config-ptp)# |         | no transport-protocol |                    |
| ------------------- | ------- | --------------------- | ------------------ |
| Command History     |         |                       |                    |
| Release             |         |                       | Modification       |
| 10.08               |         |                       | Commandintroduced. |
| Command Information |         |                       |                    |
| Platforms           | Command | context               | Authority          |
8360 config-ptp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
186
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Chapter 10
|     |     |     | Configuration | and firmware |
| --- | --- | --- | ------------- | ------------ |
management
| Configuration | and firmware  | management |     |     |
| ------------- | ------------- | ---------- | --- | --- |
| Upgrade       | and downgrade | scenarios  |     |     |
UpgradeanddowngradescenariosareprovidedbytheConfiguration MigrationFramework(CMF).
Upgrades
Allupgradescenariosaresupportedandconfigurationismigrated.
Downgrades
Thefollowingscenarioissupported:
1.Createacheckpointbeforeupgrading.
2.Upgrade.
3.Performconfigchanges.
4.Setthestartupconfigurationtothecheckpointcreatedinstep1.
5.Downgrade
Configurationchangesthatoccurafterthecheckpointinstep1willbelostduringthedowngrade.
Limitations
ThefollowingarethelimitationsofupgradeanddowngradescenariosprovidedbyCMF.
| Table 1: Configurationfromandtothesamebuild |     |            |           |           |
| ------------------------------------------- | --- | ---------- | --------- | --------- |
| From/to                                     |     | Checkpoint | Running   | Startup   |
| Checkpoint                                  |     | N/A        | Supported | Supported |
| Running                                     |     | Supported  |           | Supported |
N/A
| Startup                                                      |     | Supported  | Supported | N/A       |
| ------------------------------------------------------------ | --- | ---------- | --------- | --------- |
| ConfigfromURLinCLIFormat                                     |     | Supported  | Supported | Supported |
| ConfigfromURLinJSONFormat                                    |     | Supported  | Supported | Supported |
| Table 2: Configurationfromanolderbuildtoanewerbuild(upgrade) |     |            |           |           |
| From/to                                                      |     | Checkpoint | Running   | Startup   |
ConfigfromURLinCLIFormat Notsupported Notsupported Notsupported
187
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| From/to |     | Checkpoint | Running | Startup |
| ------- | --- | ---------- | ------- | ------- |
ConfigfromURLinJSONFormat Notsupported Notsupported Notsupported
| Startup  |                                                       | Notsupported | Supported | Supported |
| -------- | ----------------------------------------------------- | ------------ | --------- | --------- |
| Table 3: | Configurationfromanewerbuildtoanolderbuild(downgrade) |              |           |           |
| From/to  |                                                       | Checkpoint   | Running   | Startup   |
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
change,thetimeoutcounterisrestarted.Ifthetimeoutexpireswithnoadditionalconfiguration
changesbeingmade,theswitchgeneratesanewcheckpoint.
Configurationandfirmwaremanagement |188

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

1. Enable the checkpoint auto mode.

2. To save the configuration, enter the checkpoint auto confirm command before the specified

time set in step 1.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

189

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
<TIME-LAPSE-INTERVAL>
Specifiesthetimelapseintervalinminutes.Range:1to60.
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
switch#
|            | checkpoint auto confirm |         |
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
| Command        | History     |              |
| -------------- | ----------- | ------------ |
| Release        |             | Modification |
| 10.07orearlier |             | --           |
| Command        | Information |              |
Configurationandfirmwaremanagement |190

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| checkpoint      | auto    | confirm |     |
| --------------- | ------- | ------- | --- |
| checkpoint auto | confirm |         |     |
Description
Signalstotheswitchtosavetherunningconfigurationusedduringtheautocheckpointmode.This
commandalsoendstheautocheckpointmode.
Usage
Tosavetheruntimecheckpointpermanently,runthecheckpoint auto confirmcommandduringthe
timelapsevaluesetbythecheckpoint auto <TIME-LAPSE-INTERVAL>command.Thegenerated
checkpointnamewillbeintheformatAUTO<YYYYMMDDHHMMSS>.Ifthecheckpoint auto confirm
commandisnotenteredduringthespecifiedtimelapseinterval,thepreviousruntimeconfigurationis
restored.
Examples
Confirmingtheautocheckpoint:
| switch#             | checkpoint | auto confirm |              |
| ------------------- | ---------- | ------------ | ------------ |
| Command History     |            |              |              |
| Release             |            |              | Modification |
| 10.07orearlier      |            |              | --           |
| Command Information |            |              |              |
| Platforms           | Command    | context      | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| checkpoint | diff |     |     |
| ---------- | ---- | --- | --- |
checkpoint diff {<CHECKPOINT-NAME1> | running-config | startup-config}
| {<CHECKPOINT-NAME2> |     | | running-config | | startup-config} |
| ------------------- | --- | ---------------- | ----------------- |
Description
Showsthedifferenceinconfigurationbetweentwoconfigurations.Comparecheckpoints,therunning
configuration,orthestartupconfiguration.
191
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Parameter Description
{<CHECKPOINT-NAME1> | running-config | startup-config} Selectseitheracheckpoint,the
runningconfiguration,orthe
startupconfigurationasthe
baseline.
{<CHECKPOINT-NAME2> | running-config | startup-config} Selectseitheracheckpoint,the
runningconfiguration,orthe
startupconfigurationtocompare.
Usability
| Theoutputofthecheckpoint |     | diffcommandhasseveralsymbols: |
| ------------------------ | --- | ----------------------------- |
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
Configurationandfirmwaremanagement |192

| interface   | 1/1/1      |              |     |
| ----------- | ---------- | ------------ | --- |
| no shutdown |            |              |     |
| ip address  | 1.0.0.1/24 |              |     |
| interface   | 1/1/2      |              |     |
| no shutdown |            |              |     |
| ip address  | 2.0.0.1/24 |              |     |
| switch#     | checkpoint | diff cp1 cp2 |     |
--- /tmp/chkpt11501550258421 2017-08-01 01:17:38.420514016 +0000
+++ /tmp/chkpt21501550258421 2017-08-01 01:17:38.420514016 +0000
| @@ -9,7 | +9,7 @@ |     |     |
| ------- | ------- | --- | --- |
!
!
!
| -vlan 1,200         |                    |         |              |
| ------------------- | ------------------ | ------- | ------------ |
| +vlan 1,200,300     |                    |         |              |
| interface           | 1/1/1              |         |              |
| no                  | shutdown           |         |              |
| ip                  | address 1.0.0.1/24 |         |              |
| Command History     |                    |         |              |
| Release             |                    |         | Modification |
| 10.07orearlier      |                    |         | --           |
| Command Information |                    |         |              |
| Platforms           | Command            | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Amaximumof32systemcheckpointscanbecreated.Beyondthislimit,thenewestsystemcheckpoint
replacestheoldestsystemcheckpoint.
193
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Examples
Enablingsystemcheckpoints:
switch(config)#
|     |     | checkpoint |     | post-configuration |     |     |
| --- | --- | ---------- | --- | ------------------ | --- | --- |
Disablingsystemcheckpoints:
| switch(config)# |             | no  | checkpoint | post-configuration |              |     |
| --------------- | ----------- | --- | ---------- | ------------------ | ------------ | --- |
| Command         | History     |     |            |                    |              |     |
| Release         |             |     |            |                    | Modification |     |
| 10.07orearlier  |             |     |            |                    | --           |     |
| Command         | Information |     |            |                    |              |     |
| Platforms       | Command     |     | context    |                    | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config)# |         | no  | checkpoint | post-configuration |     | timeout 1 |
| --------------- | ------- | --- | ---------- | ------------------ | --- | --------- |
| Command         | History |     |            |                    |     |           |
Configurationandfirmwaremanagement |194

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| checkpoint | rename                       |     |                       |
| ---------- | ---------------------------- | --- | --------------------- |
| checkpoint | rename <OLD-CHECKPOINT-NAME> |     | <NEW-CHECKPOINT-NAME> |
Description
Renamesanexistingcheckpoint.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<OLD-CHECKPOINT-NAME>
Specifiesthenameofanexistingcheckpointtoberenamed.
<NEW-CHECKPOINT-NAME> Specifiesthenewnameforthecheckpoint.Thecheckpointname
canbealphanumeric.Itcanalsocontainunderscores(_)and
dashes(-).
NOTE:
DonotstartthecheckpointnamewithCPCbecauseitisusedforsystem-
generatedcheckpoints.
Examples
Renamingcheckpointckpt1tocfg001:
| switch#        | checkpoint  | rename ckpt1 | cfg001       |
| -------------- | ----------- | ------------ | ------------ |
| Command        | History     |              |              |
| Release        |             |              | Modification |
| 10.07orearlier |             |              | --           |
| Command        | Information |              |              |
| Platforms      | Command     | context      | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| checkpoint | rollback |                    |                   |
| ---------- | -------- | ------------------ | ----------------- |
| checkpoint | rollback | {<CHECKPOINT-NAME> | | startup-config} |
195
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

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
switch#
|     | checkpoint | rollback startup-config |     |     |
| --- | ---------- | ----------------------- | --- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy checkpoint |     | <CHECKPOINT-NAME> |     | <REMOTE-URL> |
| --------------- | --- | ----------------- | --- | ------------ |
copy checkpoint <CHECKPOINT-NAME> <REMOTE-URL> [vrf <VRF-NAME>]
Description
Copiesacheckpointconfigurationtoaremotelocationasafile.Theconfigurationisexportedin
checkpointformat,whichincludesswitchconfigurationandrelevantmetadata.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<CHECKPOINT-NAME>
Specifiesthenameofacheckpoint.
<REMOTE-URL> Specifiestheremotedestinationandfilenameusingthesyntax:
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
Configurationandfirmwaremanagement |196

| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy checkpoint |     | <CHECKPOINT-NAME> |     | {running-config |     | | startup- |
| --------------- | --- | ----------------- | --- | --------------- | --- | ---------- |
config}
copy checkpoint <CHECKPOINT-NAME> {running-config | startup-config}
Description
Copiesanexistingcheckpointconfigurationtotherunningconfigurationortothestartupconfiguration.
197
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

| Parameter         |     |     | Description                             |     |
| ----------------- | --- | --- | --------------------------------------- | --- |
| <CHECKPOINT-NAME> |     |     | Specifiesthenameofanexistingcheckpoint. |     |
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationreceivesthecopiedcheckpointconfiguration.If
thestartupconfigurationisalreadypresent,thecommand
overwritesthestartupconfiguration.
Examples
Copyingckpt1checkpointtotherunningconfiguration:
| switch# | copy checkpoint | ckpt1 | running-config |     |
| ------- | --------------- | ----- | -------------- | --- |
Success
Copyingckpt1checkpointtothestartupconfiguration:
| switch# | copy checkpoint | ckpt1 | startup-config |     |
| ------- | --------------- | ----- | -------------- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy checkpoint |                   | <CHECKPOINT-NAME> |               | <STORAGE-URL> |
| --------------- | ----------------- | ----------------- | ------------- | ------------- |
| copy checkpoint | <CHECKPOINT-NAME> |                   | <STORAGE-URL> |               |
Description
CopiesanexistingcheckpointconfigurationtoaUSBdrive.Thefileformatisdefinedwhenthe
checkpointwascreated.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<CHECKPOINT-NAME>
Specifiesthenameofthecheckpointtocopy.Thecheckpoint
namecanbealphanumeric.Itcanalsocontainunderscores(_)
anddashes(-).
<STORAGE-URL>> SpecifiesthenameofthetargetfileontheUSBdriveusingthe
followingsyntax:usb:/<FILE>
TheUSBdrivemustbeformattedwiththeFATfilesystem.
Examples
Configurationandfirmwaremanagement |198

CopyingthetestcheckpointtothetestCheckfileontheUSBdrive:
| switch# | copy checkpoint | test usb:/testCheck |     |
| ------- | --------------- | ------------------- | --- |
Success
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
DonotstartthecheckpointnamewithCPCbecauseitisusedforsystem-
generatedcheckpoints.
| vrf <VRF-NAME> |     |     | SpecifiesaVRFname.Default:default. |
| -------------- | --- | --- | ---------------------------------- |
Examples
Copyingacheckpointformatfiletocheckpointckpt5onthedefaultVRF:
199
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| switch# | copy tftp://192.168.1.10/ckptmeta |     |     | checkpoint | ckpt5 |
| ------- | --------------------------------- | --- | --- | ---------- | ----- |
######################################################################### 100.0%
100.0%
Success
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy <REMOTE-URL> |     | {running-config |     | | startup-config} |     |
| ----------------- | --- | --------------- | --- | ----------------- | --- |
copy <REMOTE-URL> {running-config | startup-config } [vrf <VRF-NAME>]
Description
Copiesaremotefilecontainingaswitchconfigurationtotherunningconfigurationortothestartup
configuration.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<REMOTE-URL>
Specifiesaremotefilewiththefollowingsyntax:
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
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |     |
| -------------- | --- | --- | --------------------------------------- | --- | --- |
Usage
Theswitchcopiesonlycertainfiletypes.Theformatofthefileisautomaticallydetectedfromcontents
ofthefile.Thestartup-configoptiononlysupportstheJSONfileformatandcheckpoints,butthe
running-configoptionsupportstheJSONandCLIfileformatsandcheckpoints.
WhenafileoftheCLIformatiscopied,itoverwritestherunningconfiguration.TheCLIcommanddoes
notcleartherunningconfigurationbeforeapplyingtheCLIcommands.AlloftheCLIcommandsinthe
fileareappliedline-by-line.IfaparticularCLIcommandfails,theswitchlogsthefailureanditcontinues
Configurationandfirmwaremanagement |200

tothenextlineintheCLIconfiguration.Theeventlog(show events -d hpe-config)provides
informationastowhichcommandfailed.
Examples
CopyingaJSONformatfiletotherunningconfiguration:
| switch# | copy tftp://192.168.1.10/runjson |     |     | running-config |
| ------- | -------------------------------- | --- | --- | -------------- |
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Success
CopyingaCLIformatfiletotherunningconfigurationwithanerrorinthefile:
| switch# | copy tftp://192.168.1.10/runcli |     |     | running-config |
| ------- | ------------------------------- | --- | --- | -------------- |
######################################################################### 100.0%
Configuration may take several minutes to complete according to configuration file
size
--0%----10%----20%----30%----40%----50%----60%----70%----80%----90%----100%--
Some of the configuration lines from the file were NOT applied. Use 'show
| events | -d hpe-config' | for more | info. |     |
| ------ | -------------- | -------- | ----- | --- |
CopyingaCLIformatfiletothestartupconfiguration:
| switch# | copy tftp://192.168.1.10/startjson |     |     | startup-config |
| ------- | ---------------------------------- | --- | --- | -------------- |
######################################################################### 100.0%
100.0%
Success
Copyinganunsupportedfileformattothestartupconfiguration:
| switch# | copy tftp://192.168.1.10/startfile |     |     | startup-config |
| ------- | ---------------------------------- | --- | --- | -------------- |
######################################################################### 100.0%
100.0%
| unsupported    | file format |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Command        | History     |         |              |     |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
201
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

copy running-config {startup-config | checkpoint <CHECKPOINT-
NAME>}
copy running-config {startup-config | checkpoint <CHECKPOINT-NAME>}
Description
Copiestherunningconfigurationtothestartupconfigurationortoanewcheckpoint.Ifthestartup
configurationisalreadypresent,thecommandoverwritestheexistingstartupconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
startup-config Specifiesthatthestartupconfigurationreceivesacopyofthe
runningconfiguration.
checkpoint <CHECKPOINT-NAME> Specifiesthenameofanewcheckpointtoreceiveacopyofthe
runningconfiguration.Thecheckpointnamecanbecomprisedof
alphanumericcharacter,underscores(_)anddashes(-),andmust
be32charactersorfewer.
NOTE:DonotstartthecheckpointnamewithCPCbecauseitis
usedforsystem-generatedcheckpoints.
Examples
Copyingtherunningconfigurationtothestartupconfiguration:
| switch# | copy running-config | startup-config |     |     |
| ------- | ------------------- | -------------- | --- | --- |
Success
Copyingtherunningconfigurationtoanewcheckpointnamedckpt1:
| switch# | copy running-config | checkpoint | ckpt1 |     |
| ------- | ------------------- | ---------- | ----- | --- |
Success
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| copy {running-config |     | | startup-config} |     | <REMOTE-URL> |
| -------------------- | --- | ----------------- | --- | ------------ |
copy {running-config | startup-config} <REMOTE-URL> {cli | json} [vrf <VRF-NAME>]
Description
Configurationandfirmwaremanagement |202

CopiestherunningconfigurationorthestartupconfigurationtoaremotefileineitherCLIorJSON
format.
Parameter Description
{running-config | startup-config} Selectswhethertherunningconfigurationorthestartup
configurationiscopiedtoaremotefile.
<REMOTE-URL> Specifiestheremotefileusingthesyntax:
TFTPformat:
tftp://<IP-ADDR>[:<PORT-NUM>]
[;blocksize=<Value>]/<FILENAME>
SFTPformat:
sftp://<USERNAME>@<IP-ADDR>
[:<PORT-NUM>]/<FILENAME>
SCPformat:
scp://USER@{IP|HOST}[:PORT]/FILE
{cli | json} Selectstheremotefileformat:P:CLIorJSON.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
Examples
CopyingarunningconfigurationtoaremotefileinCLIformat:
| switch# | copy running-config | tftp://192.168.1.10/runcli | cli |
| ------- | ------------------- | -------------------------- | --- |
######################################################################### 100.0%
Success
CopyingarunningconfigurationtoaremotefileinJSONformat:
| switch# | copy running-config | tftp://192.168.1.10/runjson | json |
| ------- | ------------------- | --------------------------- | ---- |
######################################################################### 100.0%
Success
CopyingastartupconfigurationtoaremotefileinCLIformat:
switch# copy startup-config sftp://root@192.168.1.10/startcli cli
| root@192.168.1.10's | password:        |                   |     |
| ------------------- | ---------------- | ----------------- | --- |
| sftp> put           | /tmp/startcli    | startcli          |     |
| Uploading           | /tmp/startcli    | to /root/startcli |     |
| Connected           | to 192.168.1.10. |                   |     |
Success
CopyingastartupconfigurationtoaremotefileinJSONformat:
switch# copy startup-config sftp://root@192.168.1.10/startjson json
| root@192.168.1.10's | password:        |                    |     |
| ------------------- | ---------------- | ------------------ | --- |
| sftp> put           | /tmp/startjson   | startjson          |     |
| Uploading           | /tmp/startjson   | to /root/startjson |     |
| Connected           | to 192.168.1.10. |                    |     |
Success
| Command | History |     |     |
| ------- | ------- | --- | --- |
203
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy {running-config |     | |   | startup-config} |     | <STORAGE-URL> |
| -------------------- | --- | --- | --------------- | --- | ------------- |
copy {running-config | startup-config} <STORAGE-URL> {cli | json}
Description
CopiestherunningconfigurationorastartupconfigurationtoaUSBdrive.
| Parameter       |                   |     | Description |     |     |
| --------------- | ----------------- | --- | ----------- | --- | --- |
| {running-config | | startup-config} |     |             |     |     |
Selectstherunningconfigurationorthestartupconfiguration
tobecopiedtotheswitchUSBdrive.
<STORAGE-URL> Specifiesaremotefilewiththefollowingsyntax:usb:/<file>
| {cli | json} |     |     | Selectstheformatoftheremotefile:CLIorJSON. |     |     |
| ------------ | --- | --- | ------------------------------------------ | --- | --- |
Usage
TheswitchsupportsJSONandCLIfileformatswhencopyingtherunningorstartingconfigurationtothe
USBdrive.TheUSBdrivemustbeformattedwiththeFATfilesystem.
TheUSBdrivemustbeenabledandmountedwiththefollowingcommands:
| switch(config)# | usb       |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- |
| switch(config)# | end       |     |     |     |     |
| switch#         | usb mount |     |     |     |     |
Examples
CopyingarunningconfigurationtoafilenamedrunCLIontheUSBdrive:
| switch# | copy running-config |     | usb:/runCLI | cli |     |
| ------- | ------------------- | --- | ----------- | --- | --- |
Success
CopyingastartupconfigurationtoafilenamedstartCLIontheUSBdrive:
| switch# | copy startup-config |     | usb:/startCLI | cli |     |
| ------- | ------------------- | --- | ------------- | --- | --- |
Success
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Configurationandfirmwaremanagement |204

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy startup-config |                | running-config |     |
| ------------------- | -------------- | -------------- | --- |
| copy startup-config | running-config |                |     |
Description
Copiesthestartupconfigurationtotherunningconfiguration.
Examples
| switch# | copy startup-config | running-config |     |
| ------- | ------------------- | -------------- | --- |
Success
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
205
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Parameter

running-config

startup-config

checkpoint <CHECKPOINT-NAME>

Description

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
Do not start the checkpoint name with CPC because it is used for system-

generated checkpoints.

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

switch# copy usb:/testCheck checkpoint abc
Success

Command History

Configuration and firmware management | 206

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
erase
erase
| checkpoint | <checkpont-name>      |     |     |
| ---------- | --------------------- | --- | --- |
| core-dump  | all|daemon|dsm|kernel |     |     |
startup-config
all
Description
Deletesanexistingcheckpoint,startupconfiguration,orcore-dump.
| Parameter  |                   |     | Description |
| ---------- | ----------------- | --- | ----------- |
| checkpoint | <CHECKPOINT-NAME> |     |             |
Specifiesthenameofacheckpoint.
| core-dump  |               |     | Eraseoneofthefollowingsetsofcore-dumpfiles: |
| ---------- | ------------- | --- | ------------------------------------------- |
| all|daemon | <daemon-name> |     |                                             |
n all:Eraseallcore-dumpfiles.
|dsm |kernel
n daemon<daemon-name>:Erasedaemoncore-dumpfiles.
n dsm:Erasecord-dumpfilesfortheDistributed-services-
module.
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
| switch# | erase checkpoint | all |     |
| ------- | ---------------- | --- | --- |
207
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Command        | History     |         |                              |
| -------------- | ----------- | ------- | ---------------------------- |
| Release        |             |         | Modification                 |
| 10.09.0020     |             |         | Thedsmparameterisintroduced. |
| 10.07orearlier |             |         | --                           |
| Command        | Information |         |                              |
| Platforms      | Command     | context | Authority                    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| !Version             | AOS-CX PL.10.07.0000K-75-g55e5193 |         |                     |
| -------------------- | --------------------------------- | ------- | ------------------- |
| !export-password:    |                                   | default |                     |
| lacp system-priority |                                   | 65535   |                     |
| user admin           | group administrators              |         | password ciphertext |
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
| interface | lag 128 |     |     |
| --------- | ------- | --- | --- |
no shutdown
Configurationandfirmwaremanagement |208

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
!
!

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

209

| https-server | vrf | default |     |     |
| ------------ | --- | ------- | --- | --- |
Showingtheconfigurationoftheckpt1checkpointinJSONformat:
| switch#    | show checkpoint | ckpt1 | json |     |
| ---------- | --------------- | ----- | ---- | --- |
| Checkpoint | configuration:  |       |      |     |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| [cli | json]      |     |     |                                    |     |
SelectseithertheCLIorJSONformat.
Examples
ShowingacheckpointSHA-256hashinJSONformat:
Configurationandfirmwaremanagement |210

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
211
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show checkpoint
show checkpoint
Description
Showsadetailedlistofallsavedcheckpoints.
Examples
Showingadetailedlistofallsavedcheckpoints:
| switch#         | show checkpoint |     |                           |               |                        |
| --------------- | --------------- | --- | ------------------------- | ------------- | ---------------------- |
| NAME            | TYPE            |     | WRITER DATE(YYYY/MM/DD)   | IMAGE         | VERSION                |
| ckpt1           | checkpoint      |     | User 2017-02-23T00:10:02Z | XX.01.01.000X |                        |
| ckpt2           | checkpoint      |     | User 2017-03-08T18:10:01Z | XX.01.01.000X |                        |
| ckpt3           | checkpoint      |     | User 2017-03-09T23:11:02Z | XX.01.01.000X |                        |
| ckpt4           | checkpoint      |     | User 2017-03-11T00:00:03Z | XX.01.01.000X |                        |
| ckpt5           | latest          |     | User 2017-03-14T01:12:27Z | XX.01.01.000X |                        |
| Command History |                 |     |                           |               |                        |
| Release         |                 |     | Modification              |               |                        |
| 10.08           |                 |     | Commandsyntaxshow         | checkpoint    | list allisreplacedwith |
show checkpoint.
| 10.07orearlier      |         |         | --        |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Command Information |         |         |           |     |     |
| Platforms           | Command | context | Authority |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show checkpoint |                   | date |            |     |     |
| --------------- | ----------------- | ---- | ---------- | --- | --- |
| show checkpoint | date <START-DATE> |      | <END-DATE> |     |     |
Description
Showsdetailedlistofallsavedcheckpointscreatedwithinthespecifieddaterange.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Configurationandfirmwaremanagement |212

| Parameter |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
<END-DATE> Specifiestheendingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Examples
Showingadetailedlistofsavedcheckpointsforaspecificdaterange:
| switch#             | show checkpoint |            | date | 2017-03-08        | 2017-03-12                   |            |               |            |         |
| ------------------- | --------------- | ---------- | ---- | ----------------- | ---------------------------- | ---------- | ------------- | ---------- | ------- |
| NAME                |                 | TYPE       |      | WRITER            | DATE(YYYY/MM/DD)             |            | IMAGE         | VERSION    |         |
| ckpt2               |                 | checkpoint |      | User              | 2017-03-08T18:10:01Z         |            | XX.01.01.000X |            |         |
| ckpt3               |                 | checkpoint |      | User              | 2017-03-09T23:11:02Z         |            | XX.01.01.000X |            |         |
| ckpt4               |                 | checkpoint |      | User              | 2017-03-11T00:00:03Z         |            | XX.01.01.000X |            |         |
| Command History     |                 |            |      |                   |                              |            |               |            |         |
| Release             |                 |            |      | Modification      |                              |            |               |            |         |
| 10.08               |                 |            |      | Commandsyntaxshow |                              | checkpoint | list          | date       | <START- |
|                     |                 |            |      | DATE>             | <END-DATE>isreplacedwithshow |            |               | checkpoint | date    |
|                     |                 |            |      | <START-DATE>      | <END-DATE>                   |            |               |            |         |
| 10.07orearlier      |                 |            |      | --                |                              |            |               |            |         |
| Command Information |                 |            |      |                   |                              |            |               |            |         |
| Platforms           | Command         | context    |      | Authority         |                              |            |               |            |         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show running-config |     |           | hash |       |     |     |     |     |     |
| ------------------- | --- | --------- | ---- | ----- | --- | --- | --- | --- | --- |
| show running-config |     | hash [cli | |    | json] |     |     |     |     |     |
Description
Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutput
formatisnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     | Description |     |     |     |     |     |
| ------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
| [cli | json] |     |     |     |             |     |     |     |     |     |
SelectseithertheCLIorJSONformat.
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
| switch#     | show running-config |           | hash | cli |     |     |     |     |     |
| ----------- | ------------------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| Calculating | the hash:           | [Success] |      |     |     |     |     |     |     |
213
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |

| SHA-256 | hash of the | config | in CLI | format: |
| ------- | ----------- | ------ | ------ | ------- |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Showingthestartup-configcheckpointSHA-256hashinCLIformat:
| switch#     | show startup-config |           | hash   | cli     |
| ----------- | ------------------- | --------- | ------ | ------- |
| Calculating | the hash:           | [Success] |        |         |
| SHA-256     | hash of the         | config    | in CLI | format: |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,     | etc.). |     |     |     |
| --------------- | ------ | --- | --- | --- |
| Command History |        |     |     |     |
Configurationandfirmwaremanagement |214

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
write memory
write memory
Description
Savestherunningconfigurationtothestartupconfiguration.Itisanaliasofthecommand copy
running-config startup-config.Ifthestartupconfigurationisalreadypresent,thiscommand
overwritesthestartupconfiguration.
Examples
| switch# | write memory |     |     |
| ------- | ------------ | --- | --- |
Success
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Boot commands |     |     |     |
| ------------- | --- | --- | --- |
boot set-default
| boot set-default | {primary | | secondary} |     |
| ---------------- | -------- | ------------ | --- |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
215
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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
primary
Selectstheprimaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetoprimary
forfuturereboots.
secondary
Selectsthesecondaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetosecondary
forfuturereboots.
serviceos
Selectstheserviceoperatingsystemforthisreboot.Doesnot
changetheconfigureddefaultoperatingsystemimage.The
serviceoperatingsystemactsasastandalonebootloaderand
recoveryOSforswitchesrunningtheAOS-CXoperatingsystem
andisusedinrarecaseswhentroubleshootingaswitch.
Usage
Configurationandfirmwaremanagement |216

Thiscommandrebootstheentiresystem.Ifyoudonotselectoneoftheoptionalparameters,the
systemrebootsfromtheconfigureddefaultbootimage.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Choosingoneoftheoptionalparametersaffectsthesettingforthedefaultbootimage:
n Ifyouselecttheprimaryorsecondaryoptionalparameter,thatimagebecomestheconfigured
defaultbootimageforfuturesystemreboots.Thecommandfailsiftheswitchisnotabletosetthe
operatingsystemimagetotheimageyouselected.
Youcanusetheboot set-defaultcommandtochangetheconfigureddefaultoperatingsystem
image.
n Ifyouselectserviceosastheoptionalparameter,theconfigureddefaultbootimageremainsthe
same,andthesystemrebootsallmanagementmoduleswiththeserviceoperatingsystem.
Iftheconfigurationoftheswitchhaschangedsincethelastreboot,whenyouexecutetheboot
system
commandyouarepromptedtosavetheconfigurationandyouarepromptedtoconfirmthereboot
operation.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,theboot systemcommandisaborted.
Examples
Rebootingthesystemfromtheconfigureddefaultoperatingsystemimage:
| switch# | boot system  |             |               |        |
| ------- | ------------ | ----------- | ------------- | ------ |
| Do you  | want to save | the current | configuration | (y/n)? |
y
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
217
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

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
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
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
Configurationandfirmwaremanagement |218

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
219
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Configurationandfirmwaremanagement |220

| Uploading      | primary.swi | to /users/swuser/00_10_00_0002.swi |              |          |       |
| -------------- | ----------- | ---------------------------------- | ------------ | -------- | ----- |
| primary.swi    |             |                                    | 100% 179MB   | 35.8MB/s | 00:05 |
| Command        | History     |                                    |              |          |       |
| Release        |             |                                    | Modification |          |       |
| 10.07orearlier |             |                                    | --           |          |       |
| Command        | Information |                                    |              |          |       |
| Platforms      | Command     | context                            | Authority    |          |       |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
221
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
{hot-patch|primary|secondary} Selectaprimaryorsecondaryimageprofileforreceivingthe
downloadedfirmware.Required.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |
| -------------- | --- | --- | --------------------------------------- |
TFTP usage
Configurationandfirmwaremanagement |222

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

223

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy secondary | primary |     |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- | --- |
| copy secondary | primary |     |     |     |     |     |     |
Description
Copiesthefirmwareimagefromthesecondarytotheprimarylocation.
Examples
| switch#     | copy secondary | primary          |             |     |     |     |     |
| ----------- | -------------- | ---------------- | ----------- | --- | --- | --- | --- |
| The primary | image          | will be deleted. |             |     |     |     |     |
| Continue    | (y/n)? y       |                  |             |     |     |     |     |
| Verifying   | and writing    | system           | firmware... |     |     |     |     |
switch# copy sftp://stor@192.22.1.0/im-switch.swi primary vrf mgmt
| The primary | image    | will be deleted. |     |     |     |     |     |
| ----------- | -------- | ---------------- | --- | --- | --- | --- | --- |
| Continue    | (y/n)? y |                  |     |     |     |     |     |
The authenticity of host '192.22.1.0 (192.22.1.0)' can't be established.
ECDSA key fingerprint is SHA256:MyI1xbdKnehYut0NLfL69gDpNzCmZqBVvBaRR46m7o8.
| Are you | sure you want | to continue | connecting | (yes/no)? | yes |     |     |
| ------- | ------------- | ----------- | ---------- | --------- | --- | --- | --- |
Warning: Permanently added '192.22.1.0' (ECDSA) to the list of known hosts.
| stor@192.22.1.0's      |                        | password: |                              |                |     |       |     |
| ---------------------- | ---------------------- | --------- | ---------------------------- | -------------- | --- | ----- | --- |
| Connected              | to 192.22.1.0.         |           |                              |                |     |       |     |
| sftp> get              | c8d5b9f-topflite.swi   |           | c8d5b9f-topflite.swi.dnld    |                |     |       |     |
| Fetching               | /home/dr/im-switch.swi |           | to c8d5b9f-topflite.swi.dnld |                |     |       |     |
| /home/dr/im-switch.swi |                        |           | 100%                         | 226MB 56.6MB/s |     | 00:04 |     |
| Verifying              | and writing            | system    | firmware...                  |                |     |       |     |
| Command                | History                |           |                              |                |     |       |     |
Configurationandfirmwaremanagement |224

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
n InaUSBstoragedevice:usb:/a.txt
n InadirectoryofaUSBstoragedevice:usb:/dir/a.txt
Examples
| switch#        | copy usb:/11.10.00.0002.swi |                    | primary      |
| -------------- | --------------------------- | ------------------ | ------------ |
| The primary    | image                       | will be deleted.   |              |
| Continue       | (y/n)? y                    |                    |              |
| Verifying      | and writing                 | system firmware... |              |
| Command        | History                     |                    |              |
| Release        |                             |                    | Modification |
| 10.07orearlier |                             |                    | --           |
| Command        | Information                 |                    |              |
225
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

Configuration and firmware management | 226

Chapter 11

Dynamic Segmentation

Dynamic Segmentation

For information on dynamic segmentation, view the Security Guide.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

227

Chapter 12

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

n Enables SNMP on the out-of-band management interface (VRF mgmt).

n Sets the contact, location, and description for the switch to: JaniceM, Building2, LabSwitch.

n Sets the community string to Lab8899X.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

228

| switch(config)# | snmp-server | vrf mgmt |     |     |
| --------------- | ----------- | -------- | --- | --- |
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
SNMP|229

Chapter 13

Aruba Central integration

Aruba Central integration

The Aruba Central network management solution, a software-as-a-service subscription in the cloud,
provides streamlined management of multiple network devices. AOS-CX switches are able to talk to
Aruba Central and utilize cloud-based management functionality. Cloud-based management
functionality allows for the deployment of network devices at sites with no or few dedicated IT personnel
(branch offices, retail stores, and so forth). AOS-CX switches utilize secure communication protocols to
connect to the Aruba Central cloud portal, and can coexist with corporate security standards, such as
those mandating the use of firewalls.

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

If switch is unable to connect to Activate server, it retries to establish connection in exponential back off
of 1s, 2s, 8s, 16s, 32s, 64s, 128s, and 256s. After the maximum back off of 256s, switch retries happen for
every 5 minutes.

If the Network Time Protocol (NTP) is not enabled on the switch, it will synchronize the system time with the

Activate server.

Custom CA certificate
To use custom CA certificate to connect to Aruba Central, AOS-CX switch downloads the certificate from
Aruba Activate server.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

230

n If there is no custom CA provided by Aruba Activate, the CA certificate present in the device is used.

n Duplicate CA certificates from Aruba Activate server will be ignored.

n If CA certificate is absent in consecutive responses from Aruba Activate server, the installed custom CA

certificate in device will be removed.

n Switch will have only one custom CA certificate installed from Aruba Activate Server.

n The certificate installed from Aruba Activate server will not be displayed in the show commands.

Support mode in Aruba Central
When the AOS-CX switch is managed by Aruba Central, the switch configuration cannot be modified
using other interfaces such as CLI or Web UI. The following command categories are blocked:

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

n All configuration commands except the aruba-central command

In cases where a maintenance or troubleshooting activity requires configuration updates, aruba-central
support-mode can be enabled to allow these operations.

The aruba-central support-mode enable or disable operation is effective only in the CLI session where it is

executed and does not impact the other CLI sessions.

If the user tries to execute any command that is not allowed, an Invalid input: error message is
displayed.

Aruba Central commands

aruba-central
aruba-central
no aruba-central

Description

Creates or enters the Aruba Central configuration context (config-aruba-central).

Example

Administrators or local user group members with execution rights for this command.

Creating the Aruba Central configuration context:

Aruba Central integration | 231

| switch(config)# | aruba-central |     |     |
| --------------- | ------------- | --- | --- |
switch(config-aruba-central)#
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
| aruba-central    | support-mode |     |     |
| ---------------- | ------------ | --- | --- |
| aruba-central    | support-mode |     |     |
| no aruba-central | support-mode |     |     |
Description
Allowsthedevicetobewritableforalloperationsin ArubaCentrallockoutmodefortroubleshooting.
Thenoformofthiscommanddisablesthisactivity.
Support-modeisdisabledbydefaultwhentheswitchismanagedbyArubaCentral.Thiscommandisonly
effectiveintheCLI sessionwhereitisexecuted.
Examples
ConfiguringthedevicetobewritableforalloperationsinArubaCentrallockoutmode:
| switch# | aruba-central | support-mode |     |
| ------- | ------------- | ------------ | --- |
switch#
RemovingtheconfigurationthatallowsthedevicetobewritableforalloperationsinArubaCentral
lockoutmode:
| switch# | no aruba-central | support-mode |     |
| ------- | ---------------- | ------------ | --- |
switch#
| Command        | History |     |              |
| -------------- | ------- | --- | ------------ |
| Release        |         |     | Modification |
| 10.07orearlier |         |     | --           |
232
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
| configuration-lockout    |     |         | central | managed |
| ------------------------ | --- | ------- | ------- | ------- |
| configuration-lockout    |     | central | managed |         |
| no configuration-lockout |     | central | managed |         |
Description
ConfiguresthedevicetoonlybewritablefromArubaCentral.ArubaCentralwillbetheonlyagentthat
canadd,modify,ordeleteconfigurationsonthedevice.Thenoformofthiscommanddisablesthis
feature.
ThenoformofthiscommandisonlyavailablewhenthedeviceisdisconnectedfromArubaCentral.
Usage
TheAOS-CXswitchconnectstoArubaCentralineitheroftwomodes:monitorormanaged.Whenthe
deviceisconnectedinmonitormode,ArubaCentralmonitorstheconfigurationsontheswitch.When
thedeviceisconnectedinmanagedmode,theconfiguration-lockout central managedcommand
doesnotallowconfigurationchangesfromotherinterfacessuchasCLIorWebUI.
Examples
ConfiguringthedevicetoonlybewritablefromArubaCentral:
switch(config)#
|               |                            | configuration-lockout |     | central managed |
| ------------- | -------------------------- | --------------------- | --- | --------------- |
| switch#       | show configuration-lockout |                       |     |                 |
| configuration | lockout                    |                       |     |                 |
---------------------
| central: | managed           |        |        |                |
| -------- | ----------------- | ------ | ------ | -------------- |
| switch#  | sh aruba-central  |        |        |                |
| Central  | admin state       |        |        | :enable        |
| Central  | location          |        |        | :20.0.0.2:8083 |
| VRF for  | connection        |        |        | :default       |
| Central  | connection        | status |        | :connected     |
| Central  | source            |        |        | :cli           |
| Central  | source connection |        | status | :connected     |
Central source last connected on :Tue Feb 9 17:53:13 UTC 2021
| Activate        | Server | URL |     | :devices-v2.arubanetworks.com |
| --------------- | ------ | --- | --- | ----------------------------- |
| CLI location    |        |     |     | :20.0.2:8083                  |
| CLI VRF         |        |     |     | :default                      |
| switch(config)# |        | end |     |                               |
| Command History |        |     |     |                               |
ArubaCentralintegration|233

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
9300
10000
disable
disable
Description
DisablesconnectiontoArubaCentralserver.
Whentheconnectionisdisabled,theswitchdoesnotattempttoconnecttotheArubaCentralserveror
fetchcentrallocationfromanyofthethreesources(CLI/ArubaActivate/DHCP).Italsodisconnectsany
activeconnectiontotheArubaCentralserver.
Example
switch(config-aruba-central)#
disable
switch(config-aruba-central)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config-aruba-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
9300
10000
enable
enable
Description
234
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config-aruba-central Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
location-override
| location-override | <location> | [vrf <VRF-NAME>] |     |
| ----------------- | ---------- | ---------------- | --- |
no location-override
Description
Whenlocationandvrfareconfigured,theswitchoverridesexistingconnectionstoArubaCentral.The
switchattemptstoestablishconnectiontoArubaCentralwiththespecifiedlocationandVRFwith
highestpriority.
ThenoformofthiscommandremoveslocationoverridevaluesfromtheArubaCentralconfiguration
context.
| Parameter  |     |     | Description                |
| ---------- | --- | --- | -------------------------- |
| <location> |     |     | Specifiesoneofthesevalues: |
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
ArubaCentralintegration|235

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
Examples
ConfiguringlocationoverridewithlocationandVRF:
switch(config-aruba-central)# location-override aruba-central.com vrf default
switch(config-aruba-central)#
Configuringlocationoverridewithlocationonly:
switch(config-aruba-central)# location-override aruba-central.com
switch(config-aruba-central)#
RemovinglocationoverridevaluesfromtheArubaCentralconfigurationcontext:
| switch(config-aruba-central)# |     | no  | location-override |
| ----------------------------- | --- | --- | ----------------- |
switch(config-aruba-central)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config-aruba-central
| 8320 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 8325 |     |     | rightsforthiscommand.                              |
8360
9300
10000
show aruba-central
show aruba-central
Description
ShowsinformationaboutArubaCentralconnectionandthestatusoftheActivateserverconnection.
Examples
ExampleofaswitchthathastheArubaCentralconnection:
236
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| switch#              | show aruba-central |           |         |              |                      |
| -------------------- | ------------------ | --------- | ------- | ------------ | -------------------- |
| Central              | admin state        |           |         |              | :enabled             |
| Central              | location           |           |         |              | : N/A                |
| VRF for              | connection         |           |         |              | : N/A                |
| Central              | connection         | status    |         |              | : N/A                |
| Central              | source             |           |         |              | : dhcp               |
| Central              | source connection  |           | status  |              | : connection_failure |
| Central              | source last        | connected |         | on           | : N/A                |
| System time          | synchronized       |           | from    | Activate     | : True               |
| Activate             | server             | URL       |         |              | : 172.17.0.1         |
| CLI location         |                    |           |         |              | : N/A                |
| CLI VRF              |                    |           |         |              | : N/A                |
| Source IP            |                    |           |         |              | : N/A                |
| Source IP Overridden |                    |           |         |              | : false              |
| Central              | support            | mode      |         |              | : disabled           |
| Command History      |                    |           |         |              |                      |
| Release              |                    |           |         | Modification |                      |
| 10.07orearlier       |                    |           |         | --           |                      |
| Command Information  |                    |           |         |              |                      |
| Platforms            | Command            |           | context | Authority    |                      |
8320 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8325 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8360 |     |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | --- | ------------------------------------- | --- |
9300
10000
| show running-config |     |                 | current-context |     |     |
| ------------------- | --- | --------------- | --------------- | --- | --- |
| show running-config |     | current-context |                 |     |     |
Description
Showstherunningconfigurationforthecurrent-context.IfuserisinthecontextofAruba-Central
(config-aruba-central),thenArubaCentralrunningconfigurationisdisplayed.
Examples
ShowstherunningconfigurationofArubaCentral:
switch(config-aruba-central)# show running-config current-context
aruba-central
disable
| Command History |     |     |     |              |     |
| --------------- | --- | --- | --- | ------------ | --- |
| Release         |     |     |     | Modification |     |
| 10.07orearlier  |     |     |     | --           |     |
ArubaCentralintegration|237

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8320 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 8325 | (#) |     |     |
| ---- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
8360
9300
10000
238
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Chapter 14

Port filtering

Port filtering

Port filtering is a feature in which packets that are ingressed through a source port can be blocked for
egressing on a specific set of ports.

Figure 4 Port Filter Application

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
updated with the new sets of egress ports/LAGs that are to be blocked for egressing and that are not a
part of its previous configuration. Duplicate updates on an existing port filter configuration are ignored.

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

239

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
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
config-lag-if
forthiscommand.
show portfilter
Portfiltering|240

| show portfilter | [<IFNAME>][vsx-peer] |     |
| --------------- | -------------------- | --- |
Description
Displaysfiltersettingsforallinterfacesoraspecificinterface.
Parameter Description
<IFNAME> Specifiestheingressinterfacename.
Specifiesoneofthesevalues:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
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
241
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Portfiltering|242

Chapter 15

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

243

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
DNS|244

Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | domain-name |     |               |     |       |            |     |
| --------- | ----------- | --- | ------------- | --- | ----- | ---------- | --- |
| ip dns    | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.
Bydefault,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip
dns domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
245
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

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
| switch(config)# |             | no      | ip dns  | domain-name | domain.com   |     |
| --------------- | ----------- | ------- | ------- | ----------- | ------------ | --- |
| Command         | History     |         |         |             |              |     |
| Release         |             |         |         |             | Modification |     |
| 10.07orearlier  |             |         |         |             | --           |     |
| Command         | Information |         |         |             |              |     |
| Platforms       |             | Command | context |             | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
DNS|246

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
247
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip dns |                            |     |     |     |
| ----------- | -------------------------- | --- | --- | --- |
| show ip dns | [vrf <VRF-NAME>][vsx-peer] |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow ip dns
command.
| switch(config)# | ip  | dns domain-name    | domain.com  |         |
| --------------- | --- | ------------------ | ----------- | ------- |
| switch(config)# | ip  | dns domain-list    | domain5.com |         |
| switch(config)# | ip  | dns domain-list    | domain8.com |         |
| switch(config)# | ip  | dns server-address |             | 4.4.4.4 |
| switch(config)# | ip  | dns server-address |             | 6.6.6.6 |
DNS|248

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
| host3   |         | 5.5.5.5 |     |     |     |     |     |
| ------- | ------- | ------- | --- | --- | --- | --- | --- |
| host3   |         | c::12   |     |     |     |     |     |
| Command | History |         |     |     |     |     |     |
249
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|250

Device discovery and configuration

Chapter 16

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

251

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

Device discovery and configuration | 252

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

253

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

Device discovery and configuration | 254

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
| switch#             | clear lldp | neighbors |              |
| ------------------- | ---------- | --------- | ------------ |
| Command History     |            |           |              |
| Release             |            |           | Modification |
| 10.07orearlier      |            |           | --           |
| Command Information |            |           |              |
| Platforms           | Command    | context   | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| clear lldp statistics |     |     |     |
| --------------------- | --- | --- | --- |
| clear lldp statistics |     |     |     |
Description
ClearsallLLDPneighborstatistics.
Examples
255
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

ClearingallLLDPneighborstatistics:
| switch#             | clear lldp | statistics |              |
| ------------------- | ---------- | ---------- | ------------ |
| Command History     |            |            |              |
| Release             |            |            | Modification |
| 10.07orearlier      |            |            | --           |
| Command Information |            |            |              |
| Platforms           | Command    | context    | Authority    |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Devicediscoveryandconfiguration|256

lldp dot3
| lldp dot3 {poe | | macphy} |         |     |
| -------------- | --------- | ------- | --- |
| no lldp dot3   | {poe |    | macphy} |     |
Description
Setsthe802.3TLVstobeadvertised.Bydefault,advertisementofbothPOEandMAC/PHYTLVsis
enabled.NotsupportedontheOOBMinterface.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
poe
SpecifiesadvertisementofpoweroverEthernetdatalink
classification.
macphy Specifiesadvertisementofmediaaccesscontrolandphysicallayer
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
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp dot3 mfs |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 mfs |     |     |     |
| no lldp dot3  | mfs |     |     |
Description
Enablesthe802.3TLVlistinLLDP toadvertiseformaximumframesize(MFS).Enabledbydefault.
ThenoformofthiscommanddisablestheadvertisementofmaximumframesizeTLVs.
Examples
EnablingadvertisementofmaximumframesizeTLVs:
257
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
|     |     | lldp | dot3 | mfs |
| --- | --- | ---- | ---- | --- |
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
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp holdtime-multiplier
| lldp holdtime-multiplier |     | <multiplier> |     |     |
| ------------------------ | --- | ------------ | --- | --- |
no lldp holdtime-multiplier
Description
SetstheholdtimeTTLmultipliervaluethatisusedtocalculatetheLLDPTime-to-Livevalue.Time-to-Live
definesthelengthoftimethatneighborsconsiderLLDPinformationsentbythisagentasvalid.When
Time-to-Liveexpires,theinformationisdeletedbytheneighbor.Time-to-liveiscalculatedbymultiplying
| holdtimebythevalueoflldp |     |     | timer. |     |
| ------------------------ | --- | --- | ------ | --- |
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
Settingtheholdtimeto8timesofthevalueoflldptimer:
Devicediscoveryandconfiguration|258

| switch(config)# | lldp | holdtime-multiplier | 8   |     |
| --------------- | ---- | ------------------- | --- | --- |
Settingtheholdtimetothedefaultvalueof4timesofthevalueoflldptimer:
| switch(config)#     | no      | lldp holdtime-multiplier |              |     |
| ------------------- | ------- | ------------------------ | ------------ | --- |
| Command History     |         |                          |              |     |
| Release             |         |                          | Modification |     |
| 10.07orearlier      |         |                          | --           |     |
| Command Information |         |                          |              |     |
| Platforms           | Command | context                  | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp management-ipv4-address
| lldp management-ipv4-address |     | <IPV4-ADDR> |     |     |
| ---------------------------- | --- | ----------- | --- | --- |
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
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesthemanagementaddressoftheswitchasanIPv4format
(x.x.x.x),wherexisadecimalvaluefrom0to255.
Examples
Settingthemanagementaddressto10.10.10.2:
| switch(config)# | lldp | management-ipv4-address |     | 10.10.10.2 |
| --------------- | ---- | ----------------------- | --- | ---------- |
Removingthemanagementaddress:
| switch(config)# | no  | lldp management-ipv4-address |     |     |
| --------------- | --- | ---------------------------- | --- | --- |
259
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp management-ipv6-address
| lldp management-ipv6-address |     | <IPV6-ADDR> |     |
| ---------------------------- | --- | ----------- | --- |
no lldp management-ipv6-address
Description
DefinestheIPv6managementaddressoftheswitch.Themanagementaddressisencapsulatedinthe
managementaddressTLV.
IfyoudonotdefineanLLDPmanagementaddress,thenLLDPusesoneofthefollowing(inorder):
n IPaddressoftheport
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
Devicediscoveryandconfiguration|260

| Command   | Information |         |           |     |     |     |
| --------- | ----------- | ------- | --------- | --- | --- | --- |
| Platforms | Command     | context | Authority |     |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp med
lldp med [poe [priority-override] | capability | network-policy]
| no med [poe | [priority-override] |     | | capability | | network-policy] |     |     |
| ----------- | ------------------- | --- | ------------ | ----------------- | --- | --- |
Description
ConfiguressupportfortheLLDP-MEDTLV.LLDP-MED(mediaendpointdevices)isanextensiontoLLDP
developedbyTIAtosupportinteroperabilitybetweenVoIPendpointdevicesandothernetworkingend-
devices.TheswitchonlysendstheLLDPMEDTLVafterreceivingaMEDTLVfromandconnected
endpointdevice.
NotsupportedontheOOBMinterface.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
poe [priority-override] SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
|     |     |     | dot3 | poeandlldp | med poeareenabled,thelldp | dot3 poe3 |
| --- | --- | --- | ---- | ---------- | ------------------------- | --------- |
settingtakesprecedence.Default:enabled.
| capability |     |     | SpecifiesadvertisementofsupportedLLDPMEDTLVs.The |     |     |     |
| ---------- | --- | --- | ------------------------------------------------ | --- | --- | --- |
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
| switch(config-if)# |     | lldp med | network-policy |     |     |     |
| ------------------ | --- | -------- | -------------- | --- | --- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |         | no lldp | med network-policy |     |     |     |
| ------------------ | ------- | ------- | ------------------ | --- | --- | --- |
| Command            | History |         |                    |     |     |     |
| Release            |         |         | Modification       |     |     |     |
| 10.07orearlier     |         |         | --                 |     |     |     |
261
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| Command Information |         |     |         |           |     |     |
| ------------------- | ------- | --- | ------- | --------- | --- | --- |
| Platforms           | Command |     | context | Authority |     |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp med-location
| lldp med-location | {civic-addr |     | | elin-addr |     | }   |     |
| ----------------- | ----------- | --- | ----------- | --- | --- | --- |
| no med-location   | {civic-addr |     | | elin-addr |     | }   |     |
Description
ConfiguressupportfortheLLDP-MEDTLV.Supportsonlycivicaddressandemergencylocation
informationnumber(ELIN).Coordinate-basedlocationisnotsupported.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter  |     |     |     | Description                           |     |     |
| ---------- | --- | --- | --- | ------------------------------------- | --- | --- |
| civic-addr |     |     |     | ConfigurestheLLDPMEDciviclocationTLV. |     |     |
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
DisablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# no lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
| Command History     |     |     |     |              |     |     |
| ------------------- | --- | --- | --- | ------------ | --- | --- |
| Release             |     |     |     | Modification |     |     |
| 10.07orearlier      |     |     |     | --           |     |     |
| Command Information |     |     |     |              |     |     |
Devicediscoveryandconfiguration|262

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp receive
lldp receive
no lldp receive
Description
EnablesreceptionofLLDPinformationonaninterface.Bydefault,LLDPreceptionisenabledonall
activeinterfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablesreceptionofLLDPinformationonaninterface.
Examples
EnablingLLDPreceptiononinterface1/1/1:
switch(config)#
|                    | interface | 1/1/1        |     |
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
| Platforms           | Command   | context         | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp reinit
263
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| lldp reinit | <TIME> |     |     |
| ----------- | ------ | --- | --- |
no lldp reinit
Description
Setstheamountoftime(inseconds)towaitbeforeperformingLLDPinitializationonaninterface.
Thenoformofthiscommandsetsthereinitializationtimetoitsdefaultvalueof2seconds.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp select-tlv
| lldp select-tlv    | <TLV-NAME> |     |     |
| ------------------ | ---------- | --- | --- |
| no lldp select-tlv | <TLV-NAME> |     |     |
Description
SelectsaTLVthattheLLDPagentwillsendandreceive.Bydefault,allsupportedTLVsaresentand
received.
ThenoformofthiscommandstopstheLLDPagentfromsendingandreceivingaspecificTLV.
Devicediscoveryandconfiguration|264

LLDP supports Organization Unique Identifiers (OUI) with the following Organization-specific TLVs:

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

n system-capabilities: Select system-capabilities

TLV.

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

265

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
txdelay=2
n lldp
Whencopyingasavedconfigurationtotherunningconfiguration,thevalueforlldp timerisappliedbefore
thevalueoflldp txdelay.Thiscanresultinaconfigurationerrorifthesavedconfigurationhasavalueof
lldp timerthatisnotfourtimesthevalueoflldp txdelayintherunningconfiguration.
Forexample,ifthesavedconfigurationhasthesettings:
| n lldp timer=16  |     |     |     |
| ---------------- | --- | --- | --- |
| n lldp txdelay=4 |     |     |     |
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
Examples
Settingtheupdateintervalto7seconds:
| switch(config)# | lldp | timer 7 |     |
| --------------- | ---- | ------- | --- |
Devicediscoveryandconfiguration|266

Settingtheupdateintervaltothedefaultvalueof30seconds:
| switch(config)#     | no      | lldp timer |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp transmit
lldp transsmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionisenabled
onallactiveinterfaces,includingtheOOBMinterface.
ThenoformofthiscommanddisablestransmissionofLLDPinformationonaninterface.
Examples
EnablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1          |     |
| ------------------ | --------- | -------------- | --- |
| switch(config-if)# |           | lldp transsmit |     |
DisablingLLDPtransmissiononinterface1/1/1:
| switch(config)#    | interface | 1/1/1             |     |
| ------------------ | --------- | ----------------- | --- |
| switch(config-if)# |           | no lldp transsmit |     |
EnablingLLDPtransmissionontheOOBMinterface:
switch(config)#
|                    | interface | mgmt           |     |
| ------------------ | --------- | -------------- | --- |
| switch(config-if)# |           | lldp transsmit |     |
DisablingLLDPtransmissionontheOOBMinterface:
| switch(config)#    | interface | mgmt              |     |
| ------------------ | --------- | ----------------- | --- |
| switch(config-if)# |           | no lldp transsmit |     |
| Command History    |           |                   |     |
267
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp trap enable |     |     |     |
| ---------------- | --- | --- | --- |
| lldp trap enable |     |     |     |
Devicediscoveryandconfiguration|268

| no lldp trap | enable |     |     |
| ------------ | ------ | --- | --- |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenot
requiredtobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | lldp trap | enable |
| --------------- | --- | --------- | ------ |
EnablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | lldp | trap enable |
| ------------------ | --- | ---- | ----------- |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp | trap enable |
| --------------- | --- | ------- | ----------- |
DisablingLLDPtrapgenerationoninterfacelevel:
switch(config-if)#
|     |     | no lldp | trap enable |
| --- | --- | ------- | ----------- |
DisplayingLLDPglobalconfiguration:
| switch#     | show          | lldp configuration |     |
| ----------- | ------------- | ------------------ | --- |
| LLDP Global | Configuration |                    |     |
=========================
| LLDP Enabled  |         |                | : No |
| ------------- | ------- | -------------- | ---- |
| LLDP Transmit |         | Interval       | : 30 |
| LLDP Hold     | Time    | Multiplier     | : 4  |
| LLDP Transmit |         | Delay Interval | : 2  |
| LLDP Reinit   | Timer   | Interval       | : 2  |
| LLDP Trap     | Enabled |                | : No |
TLVs Advertised
===============
| Management | Address |     |     |
| ---------- | ------- | --- | --- |
Port Description
Port VLAN-ID
System Description
System Name
269
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

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
=======================
| PORT | TX-ENABLED | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt    | Yes     | Yes | Yes |
| ------- | ------- | --- | --- |
| Command | History |     |     |
Devicediscoveryandconfiguration|270

| Release        |             |         |         |     | Modification |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show lldp | configuration |     |                            |     |     |     |
| --------- | ------------- | --- | -------------------------- | --- | --- | --- |
| show lldp | configuration |     | [<INTERFACE-ID>][vsx-peer] |     |     |     |
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
271
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

| 1/1/2 |     | Yes |     |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- | --- |
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
Example
Showingconfigurationsettingsforallinterfaces:
Devicediscoveryandconfiguration|272

| switch#     | show lldp     | configuration | mgmt |     |
| ----------- | ------------- | ------------- | ---- | --- |
| LLDP Global | Configuration |               |      |     |
=========================
| LLDP Enabled  |                 |          | : Yes |     |
| ------------- | --------------- | -------- | ----- | --- |
| LLDP Transmit | Interval        |          | : 30  |     |
| LLDP Hold     | Time Multiplier |          | : 4   |     |
| LLDP Transmit | Delay           | Interval | : 2   |     |
| LLDP Reinit   | Timer           | Interval | : 2   |     |
| LLDP Trap     | Enabled         |          | : Yes |     |
| LLDP Port     | Configuration   |          |       |     |
=======================
| PORT | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt           | Yes         |         | Yes          | Yes |
| -------------- | ----------- | ------- | ------------ | --- |
| Command        | History     |         |              |     |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
| show lldp | local-device           |     |     |     |
| --------- | ---------------------- | --- | --- | --- |
| show lldp | local-device[vsx-peer] |     |     |     |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsare
configuredonanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDson
accessinterfaces.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingglobalLLDPinformationonly(allportsincludingOOBMportareadministrativelydown):
273
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |

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
| Port VLAN         | ID  | : 1              |     |
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
Devicediscoveryandconfiguration|274

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
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
<INTERFACE-NAME>
Specifiestheinterfaceforwhichtoshowinformationfor
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
275
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

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
| Neighbor | Port               | VLAN ID   | : 1                 |        |     |
| Neighbor | Port               | VLAN Name | : DEFAULT_VLAN_1    |        |     |
| Neighbor | Port               | MFS       | : 1500              |        |     |
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
| Neighbor      | Port               | VLAN ID      | : 1                 |      |     |
| Neighbor      | Port               | VLAN Name    | : DEFAULT_VLAN_1    |      |     |
| Neighbor      | Port               | MFS          | : 1500              |      |     |
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
Devicediscoveryandconfiguration|276

Showinginformationforinterface1/1/1whenithasmultipleneighbors(displaysamaximumoffour):
| switch# show          | lldp neighbor-info | 1/1/1    |     |
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
277
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

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
| switch# |          | show lldp | neighbor-info | detail |     |
| ------- | -------- | --------- | ------------- | ------ | --- |
| LLDP    | Neighbor |           | Information   |        |     |
=========================
| Total | Neighbor |     | Entries          | : 6 |     |
| ----- | -------- | --- | ---------------- | --- | --- |
| Total | Neighbor |     | Entries Deleted  | : 2 |     |
| Total | Neighbor |     | Entries Dropped  | : 0 |     |
| Total | Neighbor |     | Entries Aged-Out | : 2 |     |
--------------------------------------------------------------------------------
| Port     |     |                     |           | : 1/1/1             |        |
| -------- | --- | ------------------- | --------- | ------------------- | ------ |
| Neighbor |     | Entries             |           | : 1                 |        |
| Neighbor |     | Entries             | Deleted   | : 0                 |        |
| Neighbor |     | Entries             | Dropped   | : 0                 |        |
| Neighbor |     | Entries             | Aged-Out  | : 0                 |        |
| Neighbor |     | Chassis-Name        |           | : 6300              |        |
| Neighbor |     | Chassis-Description |           | : Aruba             | ...    |
| Neighbor |     | Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor |     | Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis  |     | Capabilities        | Available | : Bridge,           | Router |
| Chassis  |     | Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor |     | Port-ID             |           | : 1/1/4             |        |
| Neighbor |     | Port-Desc           |           | : 1/1/4             |        |
| Neighbor |     | Port                | VLAN ID   | : 1                 |        |
| Neighbor |     | Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
Devicediscoveryandconfiguration|278

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
279
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Port     |     |                     |           | : 1/1/46            |        |
| -------- | --- | ------------------- | --------- | ------------------- | ------ |
| Neighbor |     | Entries             |           | : 1                 |        |
| Neighbor |     | Entries             | Deleted   | : 0                 |        |
| Neighbor |     | Entries             | Dropped   | : 0                 |        |
| Neighbor |     | Entries             | Aged-Out  | : 0                 |        |
| Neighbor |     | Chassis-Name        |           | : 6300              |        |
| Neighbor |     | Chassis-Description |           | : Aruba             | ...    |
| Neighbor |     | Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor |     | Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis  |     | Capabilities        | Available | : Bridge,           | Router |
| Chassis  |     | Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor |     | Port-ID             |           | : 1/1/19            |        |
| Neighbor |     | Port-Desc           |           | : 1/1/19            |        |
| Neighbor |     | Port                | VLAN ID   | : 1                 |        |
| Neighbor |     | Port                | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor |     | Port                | MFS       | : 1500              |        |
| TTL      |     |                     |           | : 120               |        |
| Neighbor |     | Mac-Phy             | details   |                     |        |
| Neighbor |     | Auto-neg            | Supported | : true              |        |
| Neighbor |     | Auto-Neg            | Enabled   | : true              |        |
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
| Chassis        |             | Cap                 |          |                     |     |
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
Devicediscoveryandconfiguration|280

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
281
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor       |             | Chassis-ID         |           |     | : 1c:98:ec:fe:25:03 |        |
| -------------- | ----------- | ------------------ | --------- | --- | ------------------- | ------ |
| Neighbor       |             | Management-Address |           |     | : 10.1.1.5          |        |
| Chassis        |             | Capabilities       | Available |     | : Bridge,           | Router |
| Chassis        |             | Capabilities       | Enabled   |     | : Bridge,           | Router |
| Neighbor       |             | Port-ID            |           |     | : 1/1/1             |        |
| Neighbor       |             | Port-Desc          |           |     | : 1/1/1             |        |
| TTL            |             |                    |           |     | : 120               |        |
| Command        | History     |                    |           |     |                     |        |
| Release        |             |                    |           |     | Modification        |        |
| 10.07orearlier |             |                    |           |     | --                  |        |
| Command        | Information |                    |           |     |                     |        |
| Platforms      |             | Command            | context   |     | Authority           |        |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
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
| switch# |        | show lldp  | statistics |     |     |     |
| ------- | ------ | ---------- | ---------- | --- | --- | --- |
| LLDP    | Global | Statistics |            |     |     |     |
======================
| Total | Packets |              | Transmitted  |           | :   | 19  |
| ----- | ------- | ------------ | ------------ | --------- | --- | --- |
| Total | Packets |              | Received     |           | :   | 19  |
| Total | Packets |              | Received And | Discarded | :   | 0   |
| Total | TLVs    | Unrecognized |              |           | :   | 0   |
Devicediscoveryandconfiguration|282

| LLDP | Port | Statistics |     |     |     |     |
| ---- | ---- | ---------- | --- | --- | --- | --- |
====================
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
283
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| switch# | show lldp | statistics | mgmt |     |
| ------- | --------- | ---------- | ---- | --- |
LLDP Statistics
===============
| Port Name           |             |                  |     | : mgmt       |
| ------------------- | ----------- | ---------------- | --- | ------------ |
| Packets             | Transmitted |                  |     | : 20         |
| Packets             | Received    |                  |     | : 23         |
| Packets             | Received    | And Discarded    |     | : 0          |
| Packets             | Received    | And Unrecognized |     | : 0          |
| Command History     |             |                  |     |              |
| Release             |             |                  |     | Modification |
| 10.07orearlier      |             |                  |     | --           |
| Command Information |             |                  |     |              |
| Platforms           | Command     | context          |     | Authority    |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
8360
9300
10000
| show lldp tlv           |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
| show lldp tlv[vsx-peer] |     |     |     |     |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# | show lldp | tlv |     |     |
| ------- | --------- | --- | --- | --- |
TLVs Advertised
===============
| Management | Address |     |     |     |
| ---------- | ------- | --- | --- | --- |
Port Description
Port VLAN-ID
| System Capabilities |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
| System Description  |     |     |     |     |
| System Name         |     |     |     |     |
Devicediscoveryandconfiguration|284

| VLAN | Name |     |     |
| ---- | ---- | --- | --- |
MFS
OUI
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| Cisco | Discovery | Protocol | (CDP) |
| ----- | --------- | -------- | ----- |
CiscoDiscoveryProtocol(CDP)isaproprietarylayer2protocolsupportedbymostCiscodevices.Itis
usedtoexchangeinformation,suchassoftwareversion,devicecapabilities,andvoiceVLAN
information,betweendirectlyconnecteddevices,suchasaVoIPphoneandaswitch.
CDP support
Bydefault,CDPisenabledoneachactiveswitchport.Thisisaread-onlycapability,whichmeansthe
switchcanreceiveandstoreinformationaboutadjacentCDPdevices,butdoesnotgenerateCDP
packets(exceptwhencommunicatingwithCiscoIPphones.)
TheswitchsupportsCDPv2onlyanddoesnotsupportSNMPMIBtraps.
WhenaCDP-enabledportreceivesaCDPpacketfromanotherCDPdevice,itentersdataforthatdevice
intotheCDPNeighborstable,alongwiththeportnumberonwhichthedatawasreceived.Itdoesnot
forwardthepacket.Theswitchalsoperiodicallypurgesthetableofanyentriesthathaveexpired.(The
holdtimeforanydataentryintheswitchCDPNeighborstableisconfiguredinthedevicetransmitting
theCDPpacketandcannotbecontrolledintheswitchreceivingthepacket.)Aswitchreviewsthelistof
CDPneighborentrieseverythreesecondsandpurgesanyexpiredentries.
| Support | for legacy Cisco | IP phones |     |
| ------- | ---------------- | --------- | --- |
AutoconfigurationoflegacyCiscoIPphonesfortaggedvoiceVLANsupportrequiresCDPv2.
Oninitialboot-up,andsometimesperiodically,aCiscophonequeriestheswitchandadvertises
informationaboutitselfusingCDPv2.WhentheswitchreceivestheVoIPVLANQueryTLV(type0x0f)
fromthephone,theswitchimmediatelyrespondswiththevoiceVLANIDinareplypacketusingthe
VoIPVLANReplyTLV(type0x0e).ThisenablestheCiscophonetobootproperlyandsendtrafficonthe
advertisedvoiceVLANID.
TheswitchCDPpacketincludestheseTLVs:
n CDPVersion:2
CDPTTL:180seconds
n
n Checksum
285
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | --- | ----------------------------- | --- |

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

switch(config)# cdp

Disabling CDP globally:

switch(config)# no cdp

Enabling CDP on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# cdp

Disabling CDP on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no cdp

Command History

Release

10.07 or earlier

Command Information

Modification

--

Device discovery and configuration | 286

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|                    | config-if |     | forthiscommand. |
| ------------------ | --------- | --- | --------------- |
| clear cdp counters |           |     |                 |
| clear cdp counters |           |     |                 |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| clear cdp neighbor-info |     |     |     |
| ----------------------- | --- | --- | --- |
| clear cdp neighbor-info |     |     |     |
Description
ClearsCDPneighborinformation.
Examples
ClearingCDPneighborinformation:
| switch(config)      | clear | neighbor-info |              |
| ------------------- | ----- | ------------- | ------------ |
| Command History     |       |               |              |
| Release             |       |               | Modification |
| 10.07orearlier      |       |               | --           |
| Command Information |       |               |              |
287
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show cdp neighbor-info |     |                |     |
| ---------------------- | --- | -------------- | --- |
| show cdp neighbor-info |     | <INTERFACE-ID> |     |
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
Devicediscoveryandconfiguration|288

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
| switch(config)# | show        | cdp neighbor-info   |              | 1/1/1 |     |
| --------------- | ----------- | ------------------- | ------------ | ----- | --- |
| Local Port      | : 1/1/1     |                     |              |       |     |
| MAC             |             | : 3c:a8:2a:7b:6b:2b |              |       |     |
| Device ID       |             | : SEPd4adbd2a30d6   |              |       |     |
| Address         |             | : 2.71.0.230        |              |       |     |
| Platform        |             | : Cisco             | IP Phone     | 3905  |     |
| Duplex          |             | : full              |              |       |     |
| Capability      |             | : host              |              |       |     |
| Voice VLAN      | Support     | : Yes               |              |       |     |
| Neighbor        | Port-ID     | : Port 1            |              |       |     |
| Command         | History     |                     |              |       |     |
| Release         |             |                     | Modification |       |     |
| 10.07orearlier  |             |                     | --           |       |     |
| Command         | Information |                     |              |       |     |
| Platforms       | Command     | context             | Authority    |       |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show cdp traffic       |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- |
| show cdp neighbor-info |     |     |     |     |     |
Description
ShowsCDPstatisticsforeachinterface.
Examples
ShowingCDPtrafficstatistics:
| switch(config)# | show | cdp traffic |     |     |     |
| --------------- | ---- | ----------- | --- | --- | --- |
CDP Statistics
====================
289
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Devicediscoveryandconfiguration|290

Chapter 17

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

Description

43

43 suboption 144

43 suboption 145

Vendor Specific Information

Name of the configuration file

Name of the firmware image file

43 suboption 146

FQDN or IPv4 address of the Aruba Central on-premise server

43 suboption 148

FQDN or IPv4 address of the HTTP Proxy

60

Vendor Class Identifier (VCI)

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

291

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

Zero Touch Provisioning | 292

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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

293

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

Zero Touch Provisioning | 294

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
295
| AOS-CX10.11FundamentalsGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

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
ZeroTouchProvisioning|296

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
297
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| switch#         | show ztp information |         |                     |                  |               |          |
| --------------- | -------------------- | ------- | ------------------- | ---------------- | ------------- | -------- |
| TFTP Server     |                      |         | : 10.0.0.2          |                  |               |          |
| Image File      |                      |         | : TL_10_02_0001.swi |                  |               |          |
| Configuration   | File                 |         | : ztp.cfg           |                  |               |          |
| Status          |                      |         | : Failed            | - Custom startup | configuration | detected |
| Aruba Central   | Location             |         | : NA                |                  |               |          |
| Aruba Central   | Shared               | Token   | : NA                |                  |               |          |
| Force-Provision |                      |         | : Disabled          |                  |               |          |
| HTTP Proxy      | Location             |         | : NA                |                  |               |          |
| Command         | History              |         |                     |                  |               |          |
| Release         |                      |         | Modification        |                  |               |          |
| 10.07orearlier  |                      |         | --                  |                  |               |          |
| Command         | Information          |         |                     |                  |               |          |
| Platforms       | Command              | context | Authority           |                  |               |          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| ztp force | provision |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- |
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
| switch#         | configure | terminal        |     |     |     |     |
| --------------- | --------- | --------------- | --- | --- | --- | --- |
| switch(config)# | ztp       | force-provision |     |     |     |     |
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
switch#
show ztp information
| TFTP Server   |          |     | : 10.0.0.2          |     |     |     |
| ------------- | -------- | --- | ------------------- | --- | --- | --- |
| Image File    |          |     | : TL_10_02_0001.swi |     |     |     |
| Configuration | File     |     | : ztp.cfg           |     |     |     |
| Status        |          |     | : Success           |     |     |     |
| Aruba Central | Location |     | : NA                |     |     |     |
ZeroTouchProvisioning|298

| Aruba Central   | Shared   | Token | : NA      |
| --------------- | -------- | ----- | --------- |
| Force-Provision |          |       | : Enabled |
| HTTP Proxy      | Location |       | : NA      |
Inthefollowingexample,force-provisionisdisabled.
| switch#         | configure | terminal            |     |
| --------------- | --------- | ------------------- | --- |
| switch(config)# | no        | ztp force-provision |     |
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
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |
| --- | --- | --- | --------------- |
299
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Chapter 18
|                   |         |          | Switch   | system | and hardware | commands |
| ----------------- | ------- | -------- | -------- | ------ | ------------ | -------- |
| Switch system     | and     | hardware | commands |        |              |          |
| bluetooth         | disable |          |          |        |              |          |
| bluetooth disable |         |          |          |        |              |          |
| no bluetooth      | disable |          |          |        |              |          |
Description
DisablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesbothBluetoothClassicand
BluetoothLowEnergy(BLE).Bluetoothisenabledbydefault.
ThenoformofthiscommandenablestheBluetoothfeatureontheswitch.
Example
DisablingBluetoothontheswitch.<XXXX>istheswitchplatformand<NNNNNNNNNN>isthedevice
identifier.
| switch(config)# | bluetooth      |                       | disable |     |     |     |
| --------------- | -------------- | --------------------- | ------- | --- | --- | --- |
| switch#         | show bluetooth |                       |         |     |     |     |
| Enabled         |                | : No                  |         |     |     |     |
| Device name     |                | : <XXXX>-<NNNNNNNNNN> |         |     |     |     |
switch(config)#
|     | show | running-config |     |     |     |     |
| --- | ---- | -------------- | --- | --- | --- | --- |
...
| bluetooth | disabled |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- |
...
| Command History     |         |         |     |              |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- |
| Release             |         |         |     | Modification |     |     |
| 10.07orearlier      |         |         |     | --           |     |     |
| Command Information |         |         |     |              |     |     |
| Platforms           | Command | context |     | Authority    |     |     |
config
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
8360
9300
10000
| bluetooth        | enable |     |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- | --- |
| bluetooth enable |        |     |     |     |     |     |
| no bluetooth     | enable |     |     |     |     |     |
300
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

Description
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
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
9300
10000
clear events
clear events
Description
Clearsupeventlogs.Usingtheshow eventscommandwillonlydisplaythelogsgeneratedafterthe
clear eventscommand.
Examples
Clearingallgeneratedeventlogs:
| switch# | show events |     |     |
| ------- | ----------- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
Switchsystemandhardwarecommands|301

2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 27 |
| ----------- | ------------- | ---------- | ----- |
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to
36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 49 |
| ----------- | ------------- | ---------- | ----- |
| switch#     | clear events  |            |       |
| switch#     | show events   |            |       |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| clear ip        | errors |     |     |
| --------------- | ------ | --- | --- |
| clear ip errors |        |     |     |
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
| Command        | History |     |              |
| -------------- | ------- | --- | ------------ |
| Release        |         |     | Modification |
| 10.07orearlier |         |     | --           |
302
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Command   | Information |         |         |     |           |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- |
| Platforms |             | Command | context |     | Authority |     |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
| console    | baud-rate |         |     |     |     |     |
| ---------- | --------- | ------- | --- | --- | --- | --- |
| console    | baud-rate | <SPEED> |     |     |     |     |
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
| switch(config)# |     | console |     | baud-rate | 9600 |     |
| --------------- | --- | ------- | --- | --------- | ---- | --- |
This command will configure the baud rate immediately for the active serial
console session. After the command is executed the user will be prompted to
re-login. The serial console will be inaccessible until the terminal client
| settings | are    | updated | to  | match the | baud rate | of the switch. |
| -------- | ------ | ------- | --- | --------- | --------- | -------------- |
| Continue | (y/n)? | y       |     |           |           |                |
Resettingtheconsoleporttoitsdefaultspeed115200bps:
| switch(config)# |             | no  | console | baud-rate |                   |     |
| --------------- | ----------- | --- | ------- | --------- | ----------------- | --- |
| Command         | History     |     |         |           |                   |     |
| Release         |             |     |         |           | Modification      |     |
| 10.08           |             |     |         |           | Commandintroduced |     |
| Command         | Information |     |         |           |                   |     |
Switchsystemandhardwarecommands|303

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch#         | show domain-name |             |     |
| --------------- | ---------------- | ----------- | --- |
| switch#         | config           |             |     |
| switch(config)# | domain-name      | example.com |     |
| switch(config)# | show             | domain-name |     |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
304
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

hostname
| hostname <HOSTNAME> |              |     |     |
| ------------------- | ------------ | --- | --- |
| no hostname         | [<HOSTNAME>] |     |     |
Description
Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
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
| switch#           | config   |               |     |
| ----------------- | -------- | ------------- | --- |
| switch(config)#   | hostname | myswitch      |     |
| myswitch(config)# |          | show hostname |     |
myswitch
Settingthehostnametothedefaultvalue:
| myswitch(config)# |     | no hostname |     |
| ----------------- | --- | ----------- | --- |
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
led locator
led locator {on | off | flashing | slow_blink | fast_blink | half_bright}
no led locator {on | off | flashing |slow_blink | fast_blink | half_bright}
Description
SetsthestateofthelocatorLED.
Switchsystemandhardwarecommands|305

| Parameter   |     |     | Description                            |
| ----------- | --- | --- | -------------------------------------- |
| on          |     |     | TurnsontheLED.                         |
| off         |     |     | TurnsofftheLED,whichisthedefaultvalue. |
| flashing    |     |     | SetstheLEDtoblinkonandoffrepeatedly.   |
| slow_blink  |     |     | SetstheLEDtoslowblinkonandoff.         |
| fast_blink  |     |     | SetstheLEDtofastblinkonandoff.         |
| half_bright |     |     | SetstheLEDintensitytohalfbright.       |
Example
SettingthestateofthelocatorLED:
| switch#             | led locator | flashing |              |
| ------------------- | ----------- | -------- | ------------ |
| Command History     |             |          |              |
| Release             |             |          | Modification |
| 10.07orearlier      |             |          | --           |
| Command Information |             |          |              |
| Platforms           | Command     | context  | Authority    |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
9300
10000
mtrace
mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
[vrf <VRF-NAME>]
Description
TracesthespecifiedIPv4sourceandgroupaddresses.
| Parameter       |     |     | Description                           |
| --------------- | --- | --- | ------------------------------------- |
| IPV4-SRC-ADDR   |     |     | SpecifiesthesourceIPv4addresstotrace. |
| IPV4-GROUP-ADDR |     |     | SpecifiesthegroupIPv4addresstotrace.  |
lhr <IPV4-LHR-ADDR> Specifiesthelasthoprouteraddressfromwhichtostartthetrace.
306
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
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
8320 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 8325 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
8360
9300
10000
Switchsystemandhardwarecommands|307

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
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : No                  |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
| Command     | History        |                       |     |     |     |
308
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
8320 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8360
9300
10000
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
Switchsystemandhardwarecommands|309

Examples
Showingtheboothistoryoftheactivemanagementmodule:
switch#
show boot-history
| Management | module |     |     |
| ---------- | ------ | --- | --- |
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
| Command        | History     |     |              |
| -------------- | ----------- | --- | ------------ |
| Release        |             |     | Modification |
| 10.07orearlier |             |     | --           |
| Command        | Information |     |              |
310
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |     |     |     |
| --------- | ------- | ------- | --------- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show capacities |           |            |     |     |     |     |
| --------------- | --------- | ---------- | --- | --- | --- | --- |
| show capacities | <FEATURE> | [vsx-peer] |     |     |     |     |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description                             |     |     |     |
| --------- | --- | --- | --------------------------------------- | --- | --- | --- |
| <FEATURE> |     |     | Specifiesafeature.Forexample,aaaorvrrp. |     |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
ShowingallavailablecapacitiesforBGP:
| switch#            | show capacities | bgp    |     |     |     |       |
| ------------------ | --------------- | ------ | --- | --- | --- | ----- |
| System Capacities: |                 | Filter | BGP |     |     |       |
| Capacities         | Name            |        |     |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | AS numbers | in as-path | attribute |     |     |
| ------- | --------- | ---------- | ---------- | --------- | --- | --- |
32
...
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring |           |     |     |       |
| ------------------ | --------------- | --------- | --------- | --- | --- | ----- |
| System Capacities: |                 | Filter    | Mirroring |     |     |       |
| Capacities         | Name            |           |           |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | Mirror Sessions | configurable |     | in a system |     |
| ------- | --------- | --------------- | ------------ | --- | ----------- | --- |
4
| Maximum | number of | enabled | Mirror Sessions | in  | a system |     |
| ------- | --------- | ------- | --------------- | --- | -------- | --- |
4
Switchsystemandhardwarecommands|311

ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp   |      |     |       |
| ------------------ | --------------- | ------ | ---- | --- | ----- |
| System Capacities: |                 | Filter | MSTP |     |       |
| Capacities         | Name            |        |      |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | mstp instances | configurable | in a system |     |
| ------- | --------- | -------------- | ------------ | ----------- | --- |
64
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities | vlan-count |            |     |       |
| ------------------ | --------------- | ---------- | ---------- | --- | ----- |
| System Capacities: |                 | Filter     | VLAN Count |     |       |
| Capacities         | Name            |            |            |     | Value |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities-status |     |           |            |     |     |
| ---------------------- | --- | --------- | ---------- | --- | --- |
| show capacities-status |     | <FEATURE> | [vsx-peer] |     |     |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<FEATURE>
Specifiesthefeature,forexampleaaaorvrrpforwhichto
displaycapacities,values,andstatus.Required.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
312
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- |

Showingthesystemcapacitiesstatusforallfeatures:
| switch#    | show capacities-status |        |     |     |     |     |               |
| ---------- | ---------------------- | ------ | --- | --- | --- | --- | ------------- |
| System     | Capacities             | Status |     |     |     |     |               |
| Capacities | Status                 | Name   |     |     |     |     | Value Maximum |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
Switchsystemandhardwarecommands|313

| switch#             | show console |         |                   |
| ------------------- | ------------ | ------- | ----------------- |
| Baud Rate:          | 9600         |         |                   |
| Command History     |              |         |                   |
| Release             |              |         | Modification      |
| 10.08               |              |         | Commandintroduced |
| Command Information |              |         |                   |
| Platforms           | Command      | context | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show core-dump
| show core-dump | all |     |     |
| -------------- | --- | --- | --- |
Description
Showscoredumpinformationaboutthespecifiedmodule.Whennoparametersarespecified,shows
onlythecoredumpsgeneratedinthecurrentbootofthemanagementmodule.Whentheall
parameterisspecified,showsallavailablecoredumps.
| Parameter |     |     | Description                 |
| --------- | --- | --- | --------------------------- |
| all       |     |     | Showsallavailablecoredumps. |
Usage
Whennoparametersarespecified,theshow core-dumpcommandshowsonlythecoredumps
generatedinthecurrentbootofthemanagementmodule.Youcanusethiscommandtodetermine
whenanycrashesareoccurringinthecurrentboot.
Ifnocoredumpshaveoccurred,thefollowingmessageisdisplayed:No core dumps are present
Toshowcoredumpinformationforthestandbymanagementmodule,youmustusethestandby
commandtoswitchtothestandbymanagementmoduleandthenexecutetheshow core-dump
command.
Intheoutput,themeaningoftheinformationisthefollowing:
Daemon Name
Identifiesnameofthedaemonforwhichthereisdumpinformation.
| Instance ID |     |     |     |
| ----------- | --- | --- | --- |
IdentifiesthespecificinstanceofthedaemonshownintheDaemon Namecolumn.
Present
Indicatesthestatusofthecoredump:
Yes
Thecoredumphascompletedandavailableforcopying.
In Progress
Coredumpgenerationisinprogress.Donotattempttocopythiscoredump.
Timestamp
314
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Indicatesthetimethedaemoncrashoccurred.Thetimeisthelocaltimeusingthetimezoneconfiguredonthe
switch.
Build ID
Identifiesadditionalinformationaboutthesoftwareimageassociatedwiththedaemon.
Examples
Showingcoredumpinformationforthecurrentbootoftheactivemanagementmoduleonly:
| switch# | show core-dump |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
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
| switch# | show core-dump | all |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show domain-name
| show domain-name | [vsx-peer] |     |     |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- | --- | --- |
Switchsystemandhardwarecommands|315

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
| switch#         | show domain-name |             |     |
| --------------- | ---------------- | ----------- | --- |
| switch#         | config           |             |     |
| switch(config)# | domain-name      | example.com |     |
| switch(config)# | show             | domain-name |     |
example.com
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show environment |                | fan |     |
| ---------------- | -------------- | --- | --- |
| show environment | fan [vsx-peer] |     |     |
Description
Showsthestatusinformationforallfansandfantrays(ifpresent)inthesystem.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
316
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

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

Showing output for a system without a fan tray:

switch# show environment fan

Serial Number Speed

Fan information
---------------------------------------------------------------
Fan
---------------------------------------------------------------
1
2
3

front-to-back
front-to-back
front-to-back

SGXXXXXXXXXX
SGXXXXXXXXXX
SGXXXXXXXXXX

slow
normal
medium

6000
8000
11000

Direction

ok
ok
ok

Status

RPM

Switch system and hardware commands | 317

| 4 SGXXXXXXXXXX |     | fast front-to-back |     | ok    | 14000 |
| -------------- | --- | ------------------ | --- | ----- | ----- |
| 5 SGXXXXXXXXXX |     | max front-to-back  |     | fault | 16500 |
| 6 N/A          |     | N/A N/A            |     | empty |       |
...
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |     | led        |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- |
| show environment | led | [vsx-peer] |     |     |     |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingstateandstatusforLED:
| switch# | show environment | led    |     |     |     |
| ------- | ---------------- | ------ | --- | --- | --- |
| Name    | State            | Status |     |     |     |
-----------------------------------
| locator             | flashing | ok  |              |     |     |
| ------------------- | -------- | --- | ------------ | --- | --- |
| Command History     |          |     |              |     |     |
| Release             |          |     | Modification |     |     |
| 10.07orearlier      |          |     | --           |     |     |
| Command Information |          |     |              |     |     |
318
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
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
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Switchsystemandhardwarecommands|319

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show environment |             | temperature |            |
| ---------------- | ----------- | ----------- | ---------- |
| show environment | temperature | [detail]    | [vsx-peer] |
Description
Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
detail
Showsdetailedinformationfromeachtemperaturesensor.
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
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
| 10.07orearlier  |     |     | --           |
320
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Command   |     | Information |     |         |           |
| --------- | --- | ----------- | --- | ------- | --------- |
| Platforms |     | Command     |     | context | Authority |
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
ShowstheeventlogsforthespecifiedeventID.EventID
range:101through99999.
-s {emergency | alert | critical | Showstheeventlogsforthespecifiedseverity.Selectthe
|     | error | | warning | |   | notice | | severityfromthefollowinglist: |
| --- | ----- | --------- | --- | -------- | ----------------------------- |
|     | info  | | debug}  |     |          |                               |
n emergency:Displayseventlogswithseverityemergency
only.
n alert:Displayseventlogswithseverityalertandabove.
n critical:Displayseventlogswithseveritycriticaland
above.
n error:Displayseventlogswithseverityerrorandabove.
n warning:Displayseventlogswithseveritywarningand
above.
n notice:Displayseventlogswithseveritynoticeand
above.
n info:Displayseventlogswithseverityinfoandabove.
n debug:Displayseventlogswithallseverities.
| -r  |     |     |     |     | Showsthemostrecenteventlogsfirst.                  |
| --- | --- | --- | --- | --- | -------------------------------------------------- |
| -a  |     |     |     |     | Showsalleventlogs,includingthoseeventsfromprevious |
boots.
| -n  | <COUNT> |     |     |     | Displaysthespecifiednumberofeventlogs. |
| --- | ------- | --- | --- | --- | -------------------------------------- |
-c {lldp | ospf | ...} Showstheeventlogsforthespecifiedeventcategory.Enter
show event -cforafulllistingofsupportedcategorieswith
descriptions.
Switchsystemandhardwarecommands|321

Parameter Description
| -d {lldpd | | bgpd | fand | | ...} |
| --------- | ------------- | ------ |
Showstheeventlogsforthespecifiedprocess.Entershow
event -dforafulllistingofsupporteddaemonswith
descriptions.
Examples
Showingeventlogs:
| switch# | show events |     |
| ------- | ----------- | --- |
---------------------------------------------------
| show | event logs |     |
| ---- | ---------- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up  | for bridge_normal | interface |
| --- | ----------------- | --------- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
| in  | Hardware |     |
| --- | -------- | --- |
Showingthemostrecenteventlogsfirst:
| switch# | show events | -r  |
| ------- | ----------- | --- |
---------------------------------------------------
| show | event logs |     |
| ---- | ---------- | --- |
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
| in  | Hardware |     |
| --- | -------- | --- |
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up  | for bridge_normal | interface |
| --- | ----------------- | --------- |
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingalleventlogs:
| switch# | show events | -a  |
| ------- | ----------- | --- |
---------------------------------------------------
| show | event logs |     |
| ---- | ---------- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to
| up  | for bridge_normal | interface |
| --- | ----------------- | --------- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1
| in  | Hardware |     |
| --- | -------- | --- |
ShowingeventlogsrelatedtoLACP:
| switch# | show events | -c lacp |
| ------- | ----------- | ------- |
---------------------------------------------------
| show | event logs |     |
| ---- | ---------- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
322
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |
| ----------------------------- | ----------------------------- | --- |

Showingeventlogsasperthespecifiedmember/slotID:
| switch# | show events | -i 1/1 |     |     |
| ------- | ----------- | ------ | --- | --- |
---------------------------------------------------
| show event | logs |     |     |     |
| ---------- | ---- | --- | --- | --- |
---------------------------------------------------
2017-08-17:22:32:25.743991|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll | interval | is changed | to 313 |
| ----------- | ---- | -------- | ---------- | ------ |
2017-08-17:22:33:01.692860|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll | interval | is changed | to 23 |
| ----------- | ---- | -------- | ---------- | ----- |
2017-08-17:22:33:06.181436|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll | interval | is changed | to 512 |
| ----------- | ---- | -------- | ---------- | ------ |
2017-08-17:22:33:06.181436|systemd-coredump|1201|LOG_CRIT|LC|1/1|hpe-sysmond
| crashed | due to | signal:11 |     |     |
| ------- | ------ | --------- | --- | --- |
Showingeventlogsasperthespecifiedprocess:
| switch# | show events | -d lacpd |     |     |
| ------- | ----------- | -------- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |     |
| ---------- | ---- | --- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Displayingthespecifiednumberofeventlogs:
| switch# | show events | -n 5 |     |     |
| ------- | ----------- | ---- | --- | --- |
---------------------------------------------------
| show event | logs |     |     |     |
| ---------- | ---- | --- | --- | --- |
---------------------------------------------------
2018-03-21:06:12:15.500603|arpmgrd|6101|LOG_INFO|AMM|-|ARPMGRD daemon has started
2018-03-21:06:12:17.734405|lldpd|109|LOG_INFO|AMM|-|Configured LLDP tx-delay to 2
2018-03-21:06:12:17.740517|lacpd|1307|LOG_INFO|AMM|-|LACP system ID set to
70:72:cf:d4:34:42
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
show hostname
Switchsystemandhardwarecommands|323

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
| switch# | show hostname |     |     |
| ------- | ------------- | --- | --- |
switch
| switch#           | config   |               |     |
| ----------------- | -------- | ------------- | --- |
| switch(config)#   | hostname | myswitch      |     |
| myswitch(config)# |          | show hostname |     |
myswitch
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
324
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

Showingtheprimaryandsecondaryimagesona8320switch:
| switch# | show images |     |     |
| ------- | ----------- | --- | --- |
---------------------------------------------------------------------------
| AOS-CX | Primary Image |     |     |
| ------ | ------------- | --- | --- |
---------------------------------------------------------------------------
| Version | : TL.10.05.0001I |              |     |
| ------- | ---------------- | ------------ | --- |
| Size    | : 405 MB         |              |     |
| Date    | : 2020-04-23     | 02:49:04 PDT |     |
SHA-256 : 7efe86a445e87e40f47de156add25720b7277cae1a8db2f9c4ea5f49e74f2a5a
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
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show ip        | errors     |     |     |
| -------------- | ---------- | --- | --- |
| show ip errors | [vsx-peer] |     |     |
Description
ShowsIPerrorstatisticsforpacketsreceivedbytheswitchsincetheswitchwaslastbooted.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Switchsystemandhardwarecommands|325

Usage
IPerrorinfoaboutreceivedpacketsiscollectedfromeachactivelinecardontheswitchandis
preservedduringfailoverevents.Errorcountsareclearedwhentheswitchisrebooted.
Dropreasonsarethefollowing:
| n Malformed | packet |     |     |
| ----------- | ------ | --- | --- |
ThepacketdoesnotconformtoTCP/IPprotocolstandardssuchaspacketlengthorinternetheaderlength.
Alargenumberofmalformedpacketscanindicatethattherearehardwaremalfunctionssuchasloosecables,
networkcardmalfunctions,orthataDOS(denialofservice)attackisoccurring.
| n IP address | error |     |     |
| ------------ | ----- | --- | --- |
ThepackethasanerrorinthedestinationorsourceIPaddress.ExamplesofIPaddresserrorsincludethe
following:
o ThesourceIPaddressanddestinationIPaddressarethesame.
o ThereisnodestinationIPaddress.
o ThesourceIPaddressisamulticastIPaddress.
o
TheforwardingheaderofanIPv6addressisempty.
o ThereisnosourceIPaddressforanIPv6packet.
| n Invalid TTLs |     |     |     |
| -------------- | --- | --- | --- |
TheTTL(timetolive)valueofthepacketreachedzero.Thepacketwasdiscardedbecauseittraversedthe
maximumnumberofhopspermittedbytheTTLvalue.
TTLsareusedtopreventpacketsfrombeingcirculatedonthenetworkendlessly.
Example
Showingiperrorstatisticsforpacketsreceivedbytheswitch:
switch#
show ip errors
----------------------------------
| Drop reason |     | Packets |     |
| ----------- | --- | ------- | --- |
----------------------------------
| Malformed  | packets |     | 1   |
| ---------- | ------- | --- | --- |
| IP address | errors  |     | 10  |
...
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
8320 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8325 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8360 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
9300
10000
show module
326
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

show module [vsx-peer]

Description

Shows information about installed line modules and management modules.

Although this switch does not have removable modules, this command will still return information about the

switch, referring to management modules and line modules.

Parameter

vsx-peer

Usage

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

Identifies and shows status information about the line modules and management modules that are
installed in the switch.

To show the configuration information—if any—associated with that line module slot, use the show
running-configuration command.

Status is one of the following values:
Active
This switch is the active management module.
Standby

This switch is the standby management module.

Deinitializing
The switch is being deinitialized.
Diagnostic
The switch is in a state used for troubleshooting.
Down
The switch is physically present but is powered down.
Empty

The switch hardware is not installed in the chassis.

Failed
The switch has experienced an error and failed.
Failover

This switch is a fabric module or a line module, and it is in the process of connecting to the new
active management module during a management module failover event.

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

Switch system and hardware commands | 327

| switch(config)# | show    | module |     |     |     |
| --------------- | ------- | ------ | --- | --- | --- |
| Management      | Modules |        |     |     |     |
==================
| Product     |             |     |     | Serial |        |
| ----------- | ----------- | --- | --- | ------ | ------ |
| Name Number | Description |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL581A   | 8320 | Mgmt Mod |     | TW87KCW00X | Ready |
| ------------ | ---- | -------- | --- | ---------- | ----- |
| Line Modules |      |          |     |            |       |
============
| Product     |             |     |     | Serial |        |
| ----------- | ----------- | --- | --- | ------ | ------ |
| Name Number | Description |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL581A          | 8320    |         |              | TW87KCW00X | Ready |
| ------------------- | ------- | ------- | ------------ | ---------- | ----- |
| Command History     |         |         |              |            |       |
| Release             |         |         | Modification |            |       |
| 10.07orearlier      |         |         | --           |            |       |
| Command Information |         |         |              |            |       |
| Platforms           | Command | context | Authority    |            |       |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |             |     |                  |     |     |
| ------------------- | ----------- | --- | ---------------- | --- | --- |
| show running-config | [<FEATURE>] |     | [all] [vsx-peer] |     |     |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).Whenthejsonparameteris
used,thevsx-peerparameterisnotapplicable.
| all |     |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |     |     |
| --- | --- | --- | ------------------------------------------------------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
328
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- | --- |

Showingthecurrentrunningconfiguration:
| switch> show           | running-config |     |     |     |
| ---------------------- | -------------- | --- | --- | --- |
| Current configuration: |                |     |     |     |
!
| !Version AOS-CX |     | 10.0X.XXXX |     |     |
| --------------- | --- | ---------- | --- | --- |
!
lldp enable
| linecard-module |     | LC1 part-number |     | JL363A |
| --------------- | --- | --------------- | --- | ------ |
vrf green
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
| vrf attach    |        | green        |     |     |
| ------------- | ------ | ------------ | --- | --- |
| ip address    |        | 20.0.0.44/24 |     |     |
| ip ospf       | 1 area | 0.0.0.0      |     |     |
| ip pim-sparse |        | enable       |     |     |
| interface     | vlan30 |              |     |     |
no shutdown
| vrf attach    |        | green          |     |     |
| ------------- | ------ | -------------- | --- | --- |
| ip address    |        | 30.0.0.44/24   |     |     |
| ip ospf       | 1 area | 0.0.0.0        |     |     |
| ip pim-sparse |        | enable         |     |     |
| ip pim-sparse |        | hello-interval |     | 100 |
Showingthecurrentrunningconfigurationinjsonformat:
| switch> show          | running-config |     | json  |     |
| --------------------- | -------------- | --- | ----- | --- |
| Running-configuration |                | in  | JSON: |     |
{
Switchsystemandhardwarecommands|329

"Monitoring_Policy_Script": {

"system_resource_monitor_mm1.1.0": {

"Monitoring_Policy_Instance": {

mm1.1.0.default": {

"system_resource_monitor_mm1.1.0/system_resource_monitor_

"name": "system_resource_monitor_mm1.1.0.default",
"origin": "system",
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

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

330

Showthecurrentrunningconfigurationwithdefaultvalues:
| switch(config)# | snmp-server    |                | vrf | mgmt |
| --------------- | -------------- | -------------- | --- | ---- |
| switch(config)# | show           | running-config |     |      |
| Current         | configuration: |                |     |      |
!
| !Version    | AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| led locator | on                                            |     |     |     |
!
!
!
!
| snmp-server | vrf mgmt |     |     |     |
| ----------- | -------- | --- | --- | --- |
!
!
!
!
!
vlan 1
switch(config)#
switch(config)#
| switch(config)# | show           | running-config |     | all |
| --------------- | -------------- | -------------- | --- | --- |
| Current         | configuration: |                |     |     |
!
| !Version    | AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| led locator | on                                            |     |     |     |
!
!
!
!
| snmp-server | vrf mgmt   |        |     |     |
| ----------- | ---------- | ------ | --- | --- |
| snmp-server | agent-port | 161    |     |     |
| snmp-server | community  | public |     |     |
!
!
!
!
!
vlan 1
switch(config)#
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show running-config |                 |     | current-context |     |
| ------------------- | --------------- | --- | --------------- | --- |
| show running-config | current-context |     |                 |     |
Description
Switchsystemandhardwarecommands|331

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
switch(config-external-storage-nasfiles)# show running-config current-context
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
332
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| switch(config-vsx)# |     | show run | current-context |
| ------------------- | --- | -------- | --------------- |
vsx
| inter-switch-link |             | 1/1/1   |              |
| ----------------- | ----------- | ------- | ------------ |
| role              | secondary   |         |              |
| vsx-sync          | sflow       | time    |              |
| Command           | History     |         |              |
| Release           |             |         | Modification |
| 10.07orearlier    |             |         | --           |
| Command           | Information |         |              |
| Platforms         | Command     | context | Authority    |
Allplatforms configorachildof Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
config.SeeUsage.
show startup-config
| show startup-config | [json] |     |     |
| ------------------- | ------ | --- | --- |
Description
Showsthecontentsofthestartupconfiguration.
Switchesinthefactory-defaultconfigurationdonothaveastartupconfigurationtodisplay.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
json
DisplayoutputinJSONformat.
Examples
Showingthestartup-configurationinnon-JSONformatforan8320switch:
| Leaf2(config)# | show           | startup-config |     |
| -------------- | -------------- | -------------- | --- |
| Startup        | configuration: |                |     |
!
| !Version   | AOS-CX TL.xx.xx.xxxx |     |                     |
| ---------- | -------------------- | --- | ------------------- |
| hostname   | Leaf2                |     |                     |
| user admin | group administrators |     | password ciphertext |
AQBapaGi+KZp4g8gw63UqK+zCtvO5zigFLv2DFBEH+lztqjdYgAAABwrJ+5GayUWArgv9tVFo9AzMY6gmI
7x/
KBEkGBJDXjpFson2qM83CXBUI673qWHDQ0pEIZXeuig0XogCVuId4oZiQVZlOe2MfxnqZL+E9hXaMNVowB
wbD0
cli-session
| timeout | 0   |     |     |
| ------- | --- | --- | --- |
!
Switchsystemandhardwarecommands|333

!
!
| ssh server | vrf mgmt |     |     |
| ---------- | -------- | --- | --- |
Showingthestartup-configurationinJSONformat:
| switch# | show startup-config | json |     |
| ------- | ------------------- | ---- | --- |
| Startup | configuration:      |      |     |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show system
| show system | [vsx-peer] |     |     |
| ----------- | ---------- | --- | --- |
Description
Showsgeneralstatusinformationaboutthesystem.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemContact,SystemLocation,andSystemDescriptioncanbesetwiththesnmp-servercommand.
Examples
ShowingsysteminformationfortheVSXprimaryandsecondary(peer)switchonan8320:
334
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| vsx-primary#       | show       | system           |     |      |
| ------------------ | ---------- | ---------------- | --- | ---- |
| Hostname           |            | : vsx-primary    |     |      |
| System Description |            | : TL.10.xx.xxxxx |     |      |
| System Contact     |            | :                |     |      |
| System Location    |            | :                |     |      |
| Vendor             |            | : Aruba          |     |      |
| Product            | Name       | : JL479A         |     | 8320 |
| Chassis            | Serial Nbr | : TW82K7200Q     |     |      |
| Base MAC           | Address    | : 98f2b3-68792e  |     |      |
Version : TL.10.xx.xxxxx
AOS-CX
| Time Zone           |            | : UTC            |          |              |
| ------------------- | ---------- | ---------------- | -------- | ------------ |
| Up Time             |            | : 19             | hours,   | 51 minutes   |
| CPU Util            | (%)        | : 50             |          |              |
| Memory Usage        | (%)        | : 36             |          |              |
| vsx-primary#        | show       | system           | vsx-peer |              |
| Hostname            |            | : vsx-secondary  |          |              |
| System Description  |            | : TL.10.xx.xxxxx |          |              |
| System Contact      |            | :                |          |              |
| System Location     |            | :                |          |              |
| Vendor              |            | : Aruba          |          |              |
| Product             | Name       | : JL479A         |          | 8320         |
| Chassis             | Serial Nbr | : TW73JQH024     |          |              |
| Base MAC            | Address    | : e0071b-cb72e4  |          |              |
| AOS-CX Version      | :          | TL.10.xx.xxxxx   |          |              |
| Time Zone           |            | : UTC            |          |              |
| Up Time             |            | : 21             | hours,   | 23 minutes   |
| CPU Util            | (%)        | : 14             |          |              |
| Memory Usage        | (%)        | : 36             |          |              |
| Command History     |            |                  |          |              |
| Release             |            |                  |          | Modification |
| 10.07orearlier      |            |                  |          | --           |
| Command Information |            |                  |          |              |
| Platforms           | Command    |                  | context  | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show system |     | resource-utilization |     |     |
| ----------- | --- | -------------------- | --- | --- |
show system resource-utilization [daemon <DAEMON-NAME>] [vsx-peer]
Description
ShowsinformationabouttheusageofsystemresourcessuchasCPU,memory,andopenfile
descriptors.
Switchsystemandhardwarecommands|335

| Parameter |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
daemon <DAEMON-NAME> Showsthefilteredresourceutilizationdatafortheprocess
|     |     |     |     | specifiedby<DAEMON-NAME> |     |     | only. |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | ----- | --- | --- |
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
NOTE:
|     |     |     |     | Foralistofdaemonsthatlogevents,entershow |     |     |     | events | -d ?froma |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ------ | --------- |
switchpromptinthemanager(#)context.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingallsystemresourceutilizationdata:
| switch# show | system | resource-utilization |     |     |     |     |     |     |     |
| ------------ | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- |
System Resources:
| Processes:       | 70   |              |     |     |        |          |           |     |     |
| ---------------- | ---- | ------------ | --- | --- | ------ | -------- | --------- | --- | --- |
| CPU usage(%):    | 20   |              |     |     |        |          |           |     |     |
| Memory usage(%): |      | 25           |     |     |        |          |           |     |     |
| Open FD's:       | 1024 |              |     |     |        |          |           |     |     |
| Process          |      | CPU Usage(%) |     |     | Memory | Usage(%) | Open FD's |     |     |
-----------------------------------------------------------------------
| pmd         |     | 2   |     |     | 1   |     | 14  |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hpe-sysmond |     | 1   |     |     | 2   |     | 11  |     |     |
| hpe-mgmdd   |     | 0   |     |     | 1   |     | 5   |     |     |
...
Showingtheresourceutilizationdataforthepmdprocess:
| switch# show | system | resource-utilization |     |     | daemon       | pmd  |      |     |     |
| ------------ | ------ | -------------------- | --- | --- | ------------ | ---- | ---- | --- | --- |
| Process      |        | CPU Usage            |     |     | Memory Usage | Open | FD's |     |     |
-----------------------------------------------------------------------
| pmd |     | 2   |     |     | 1   | 14  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# show    | system      | resource-utilization |      |      |              |          |     |     |     |
| --------------- | ----------- | -------------------- | ---- | ---- | ------------ | -------- | --- | --- | --- |
| System resource | utilization |                      | data | poll | is currently | disabled |     |     |     |
Showingresourceutilizationdataforalinemodule:
| switch# show    | system      | resource-utilization |     |           | module  | 1/1 |     |     |     |
| --------------- | ----------- | -------------------- | --- | --------- | ------- | --- | --- | --- | --- |
| System Resource | utilization |                      | for | line card | module: | 1/1 |     |     |     |
| CPU usage(%):   | 0           |                      |     |           |         |     |     |     |     |
336
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Memory         | usage(%): 35 |         |              |
| -------------- | ------------ | ------- | ------------ |
| Open           | FD's: 512    |         |              |
| Command        | History      |         |              |
| Release        |              |         | Modification |
| 10.07orearlier |              |         | --           |
| Command        | Information  |         |              |
| Platforms      | Command      | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
n Thetimeconsumedtoexecutethecommand.
n Thelistoffailedshowcommands,ifany.
Togetacopyofthelocaltextfilecontentcreatedwiththeshowtechcommandthatisusedwiththe
| local-fileparameter,usethecopy |     | show-tech | local-filecommand. |
| ------------------------------ | --- | --------- | ------------------ |
Example
Showingthebasicsetofsysteminformation:
Switchsystemandhardwarecommands|337

| switch# | show tech | basic |     |
| ------- | --------- | ----- | --- |
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
| no core | dumps are | present |     |
| ------- | --------- | ------- | --- |
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
| switch# | show tech | basic local-file |     |
| ------- | --------- | ---------------- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
| to copy-out    | this file.  |         |              |
| -------------- | ----------- | ------- | ------------ |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show usb
| show usb [vsx-peer] |     |     |     |
| ------------------- | --- | --- | --- |
Description
ShowstheUSBportconfigurationandmountsettings.
338
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
IfUSBhasnotbeenenabled:
| switch>  | show usb |     |     |
| -------- | -------- | --- | --- |
| Enabled: | No       |     |     |
| Mounted: | No       |     |     |
IfUSBhasbeenenabled,butnodevicehasbeenmounted:
| switch>  | show usb |     |     |
| -------- | -------- | --- | --- |
| Enabled: | Yes      |     |     |
| Mounted: | No       |     |     |
IfUSBhasbeenenabledandadevicemounted:
| switch>             | show usb |         |              |
| ------------------- | -------- | ------- | ------------ |
| Enabled:            | Yes      |         |              |
| Mounted:            | Yes      |         |              |
| Command History     |          |         |              |
| Release             |          |         | Modification |
| 10.07orearlier      |          |         | --           |
| Command Information |          |         |              |
| Platforms           | Command  | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show usb             | file-system |     |     |
| -------------------- | ----------- | --- | --- |
| show usb file-system | [<PATH>]    |     |     |
Description
ShowsdirectorylistingsforamountedUSBdevice.Whenenteredwithoutthe<PATH>parameterthe
topleveldirectorytreeisshown.
Switchsystemandhardwarecommands|339

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<PATH> Specifiesthefilepathtoshow.Aleading"/"inthepathisoptional.
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
340
AOS-CX10.11FundamentalsGuide| (83xx,9300,10000SwitchSeries)

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show version
| show version | [vsx-peer] |     |     |
| ------------ | ---------- | --- | --- |
Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingversioninformationforan8320switch:
| switch(config)# | show | version |     |
| --------------- | ---- | ------- | --- |
-----------------------------------------------------------------------------
AOS-CX
(c) Copyright 2017-2022 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version        | : TL.xx.xx.xxxx                               |                 |              |
| -------------- | --------------------------------------------- | --------------- | ------------ |
| Build Date     | : 2022-05-27                                  | 17:00:46        | PDT          |
| Build ID       | : AOS-CX:xx.xx.xxxx:feb590a400a5:201908201736 |                 |              |
| Build SHA      | : feb590a400a57ed818b01614f92010d74fbc9a4b    |                 |              |
| Active Image   | : secondary                                   |                 |              |
| Service        | OS Version                                    | : TL.01.03.0008 |              |
| BIOS Version   |                                               | : TL-01-0013    |              |
| Command        | History                                       |                 |              |
| Release        |                                               |                 | Modification |
| 10.07orearlier |                                               |                 | --           |
| Command        | Information                                   |                 |              |
Switchsystemandhardwarecommands|341

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
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
<SECONDS>
Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Example
Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |             | system | resource-utilization |              | poll-interval | 20  |
| --------------- | ----------- | ------ | -------------------- | ------------ | ------------- | --- |
| Command         | History     |        |                      |              |               |     |
| Release         |             |        |                      | Modification |               |     |
| 10.07orearlier  |             |        |                      | --           |               |     |
| Command         | Information |        |                      |              |               |     |
| Platforms       | Command     |        | context              | Authority    |               |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
top cpu
top cpu
Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch# | top cpu |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
342
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| Tasks: | 76 total, |     | 2 running, | 74  | sleeping, |     | 0 stopped, | 0 zombie |     |
| ------ | --------- | --- | ---------- | --- | --------- | --- | ---------- | -------- | --- |
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used, 661948 buff/cache
| KiB Swap: |     | 0   | total,  |     | 0 free, |     | 0      | used, 2859196 | avail Mem     |
| --------- | --- | --- | ------- | --- | ------- | --- | ------ | ------------- | ------------- |
| PID USER  |     | PRI | NI VIRT |     | RES     | SHR | S %CPU | %MEM          | TIME+ COMMAND |
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
| Tasks: | 76 total, |     | 2 running, | 74  | sleeping, |     | 0 stopped, | 0 zombie |     |
| ------ | --------- | --- | ---------- | --- | --------- | --- | ---------- | -------- | --- |
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used, 661948 buff/cache
| KiB Swap: |     | 0   | total,  |     | 0 free, |     | 0      | used, 2859196 | avail Mem     |
| --------- | --- | --- | ------- | --- | ------- | --- | ------ | ------------- | ------------- |
| PID USER  |     | PRI | NI VIRT |     | RES     | SHR | S %CPU | %MEM          | TIME+ COMMAND |
...
| Command        | History     |     |     |     |              |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| Release        |             |     |     |     | Modification |     |     |     |     |
| 10.07orearlier |             |     |     |     | --           |     |     |     |     |
| Command        | Information |     |     |     |              |     |     |     |     |
Switchsystemandhardwarecommands|343

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| usb mount    | | unmount |     |     |
| ------------ | --------- | --- | --- |
| usb {mount | | unmount}  |     |     |
Description
EnablesordisablestheinsertedUSBdrive.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
mount
EnablestheinsertedUSBdrive.
344
| AOS-CX10.11FundamentalsGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| ----------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
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
| switch# | usb mount |     |     |
| ------- | --------- | --- | --- |
UnmountingaUSBdrive:
switch#
usb unmount
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Switchsystemandhardwarecommands|345

Support and Other Resources

Chapter 19

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

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
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

AOS-CX 10.11 Fundamentals Guide | (83xx, 9300, 10000 Switch Series)

346

Aruba Hardware
Documentation
and Translations
Portal

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

Aruba software

https://asp.arubanetworks.com/downloads

Software
licensing

End-of-Life
information

https://lms.arubanetworks.com/

https://www.arubanetworks.com/support-services/end-of-life/

Aruba Developer
Hub

https://developer.arubanetworks.com/

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

Regulatory Information
To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Support and Other Resources | 347

| Additional | regulatory | information |
| ---------- | ---------- | ----------- |
Arubaiscommittedtoprovidingourcustomerswithinformationaboutthechemicalsubstancesinour
productsasneededtocomplywithlegalrequirements,environmentaldata(companyprograms,
productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSandWEEE).For
moreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
Arubaiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpusimprovethe
documentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback(docsfeedback-
switching@hpe.com).Whensubmittingyourfeedback,includethedocumenttitle,partnumber,edition,
andpublicationdatelocatedonthefrontcoverofthedocument.Foronlinehelpcontent,includethe
productname,productversion,helpedition,andpublicationdatelocatedonthelegalnoticespage.
348
| AOS-CX10.11FundamentalsGuide| |     | (83xx,9300,10000SwitchSeries) |
| ----------------------------- | --- | ----------------------------- |