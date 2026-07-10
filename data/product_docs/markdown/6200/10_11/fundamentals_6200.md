AOS-CX 10.11 Fundamentals
Guide

6200 Switch Series

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
| About this                                   | document                                       | 10  |
| Applicableproducts                           |                                                | 10  |
| Latestversionavailableonline                 |                                                | 10  |
| Commandsyntaxnotationconventions             |                                                | 10  |
| Abouttheexamples                             |                                                | 11  |
| Identifyingswitchportsandinterfaces          |                                                | 11  |
| About AOS-CX                                 |                                                | 13  |
| AOS-CXsystemdatabases                        |                                                | 13  |
| ArubaNetworkAnalyticsEngineintroduction      |                                                | 13  |
| AOS-CXCLI                                    |                                                | 14  |
| ArubaCXmobileapp                             |                                                | 14  |
| ArubaNetEdit                                 |                                                | 14  |
| Ansiblemodules                               |                                                | 15  |
| AOS-CXWebUI                                  |                                                | 15  |
| AOS-CXRESTAPI                                |                                                | 15  |
| In-bandandout-of-bandmanagement              |                                                | 15  |
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
|                                              | ConfigureusingDHCPorstaticIP                   | 25  |
|                                              | Loggingintotheswitchforthefirsttime            | 25  |
|                                              | SettingswitchtimeusingtheNTPclient             | 26  |
| Configuringbanners                           |                                                | 27  |
| UsingtheWebUI                                |                                                | 27  |
| Configuringthemanagementinterface            |                                                | 28  |
| Restoringtheswitchtofactorydefaultsettings   |                                                | 29  |
| Managementinterfacecommands                  |                                                | 30  |
|                                              | default-gateway                                | 30  |
|                                              | ipstatic                                       | 31  |
|                                              | nameserver                                     | 32  |
|                                              | showinterfacemgmt                              | 33  |
| NTPcommands                                  |                                                | 34  |
|                                              | ntpauthentication                              | 34  |
|                                              | ntpauthentication-key                          | 35  |
|                                              | ntpdisable                                     | 36  |
|                                              | ntpenable                                      | 36  |
3
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

|                               | ntpserver                                | 37  |
| ----------------------------- | ---------------------------------------- | --- |
|                               | ntptrusted-key                           | 39  |
|                               | ntpvrf                                   | 40  |
|                               | showntpassociations                      | 41  |
|                               | showntpauthentication-keys               | 42  |
|                               | showntpservers                           | 42  |
|                               | showntpstatistics                        | 43  |
|                               | showntpstatus                            | 44  |
| Telnet                        | access                                   | 46  |
| Telnetcommands                |                                          | 46  |
|                               | showtelnetserver                         | 46  |
|                               | showtelnetserversessions                 | 47  |
|                               | telnetserver                             | 48  |
| Interface                     | configuration                            | 49  |
| Configuringalayer2interface   |                                          | 49  |
| SinglesourceIPaddress         |                                          | 49  |
| Unsupportedtransceiversupport |                                          | 49  |
| Configuringaninterfacepersona |                                          | 50  |
|                               | Modes                                    | 51  |
|                               | Predefinedandcustompersonanames          | 51  |
|                               | Creatingandconfiguringaninterfacepersona | 51  |
|                               | Examples                                 | 52  |
| Monitormode                   |                                          | 52  |
| Interfacecommands             |                                          | 53  |
|                               | allow-unsupported-transceiver            | 53  |
|                               | defaultinterface                         | 54  |
|                               | description                              | 55  |
|                               | energy-efficient-ethernet                | 56  |
|                               | flow-control                             | 56  |
|                               | interface                                | 58  |
|                               | interfaceloopback                        | 58  |
|                               | interfacevlan                            | 59  |
|                               | ipaddress                                | 60  |
|                               | ipmtu                                    | 61  |
|                               | ipsource-interface                       | 61  |
|                               | ipv6address                              | 62  |
|                               | ipv6source-interface                     | 63  |
|                               | mtu                                      | 65  |
|                               | persona                                  | 66  |
|                               | routing                                  | 68  |
|                               | showallow-unsupported-transceiver        | 69  |
|                               | showinterface                            | 70  |
|                               | showinterfacedom                         | 74  |
|                               | showinterfaceenergy-efficientethernet    | 75  |
|                               | showinterfaceflow-control                | 76  |
|                               | showinterfacestatistics                  | 80  |
|                               | showinterfacetransceiver                 | 83  |
|                               | showinterfaceutilization                 | 87  |
|                               | showipinterface                          | 88  |
|                               | showipsource-interface                   | 89  |
|                               | showipv6interface                        | 90  |
|                               | showipv6source-interface                 | 91  |
|                               | shutdown                                 | 92  |
|                               | speed                                    | 93  |
Contents|4

| Source interface                                | selection    |            | 96  |
| ----------------------------------------------- | ------------ | ---------- | --- |
| Source-interfaceselectioncommands               |              |            | 96  |
| ipsource-interface(protocol<ip-addr>)           |              |            | 96  |
| ipsource-interface                              |              |            | 98  |
| ipv6source-interface                            |              |            | 99  |
| ipv6source-interface                            |              |            | 101 |
| showipsource-interface                          |              |            | 102 |
| showipv6source-interface                        |              |            | 103 |
| showrunning-config                              |              |            | 105 |
| VLANs                                           |              |            | 107 |
| Configuration                                   | and firmware | management | 108 |
| Upgradeanddowngradescenarios                    |              |            | 108 |
| Upgrades                                        |              |            | 108 |
| Downgrades                                      |              |            | 108 |
| Limitations                                     |              |            | 108 |
| Checkpoints                                     |              |            | 109 |
| Checkpointtypes                                 |              |            | 109 |
| Maximumnumberofcheckpoints                      |              |            | 109 |
| Usergeneratedcheckpoints                        |              |            | 109 |
| Systemgeneratedcheckpoints                      |              |            | 109 |
| Supportedremotefileformats                      |              |            | 110 |
| Rollback                                        |              |            | 110 |
| Checkpointautomode                              |              |            | 110 |
| Testingaswitchconfigurationincheckpointautomode |              |            | 110 |
| Checkpointcommands                              |              |            | 111 |
| checkpointauto                                  |              |            | 111 |
| checkpointautoconfirm                           |              |            | 112 |
| checkpointdiff                                  |              |            | 112 |
| checkpointpost-configuration                    |              |            | 114 |
| checkpointpost-configurationtimeout             |              |            | 115 |
| checkpointrename                                |              |            | 116 |
| checkpointrollback                              |              |            | 116 |
| copycheckpoint<CHECKPOINT-NAME><REMOTE-URL>     |              |            | 117 |
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config} 118
| copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>    |     |     | 119 |
| ----------------------------------------------- | --- | --- | --- |
| copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>     |     |     | 120 |
| copy<REMOTE-URL>{running-config|startup-config} |     |     | 121 |
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>} 123
| copy{running-config|startup-config}<REMOTE-URL>  |     |     | 123 |
| ------------------------------------------------ | --- | --- | --- |
| copy{running-config|startup-config}<STORAGE-URL> |     |     | 125 |
| copystartup-configrunning-config                 |     |     | 126 |
| copy<STORAGE-URL>running-config                  |     |     | 126 |
| erase                                            |     |     | 128 |
| showcheckpoint<CHECKPOINT-NAME>                  |     |     | 129 |
| showcheckpoint<CHECKPOINT-NAME>hash              |     |     | 131 |
| showcheckpointpost-configuration                 |     |     | 132 |
| showcheckpoint                                   |     |     | 132 |
| showcheckpointdate                               |     |     | 133 |
| showrunning-confighash                           |     |     | 134 |
| showstartup-confighash                           |     |     | 135 |
| writememory                                      |     |     | 136 |
| Bootcommands                                     |     |     | 136 |
| bootset-default                                  |     |     | 136 |
| bootsystem                                       |     |     | 137 |
5
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

|                            | showboot-history                                   | 139 |
| -------------------------- | -------------------------------------------------- | --- |
| Firmwaremanagementcommands |                                                    | 140 |
|                            | copy{primary|secondary}<REMOTE-URL>                | 141 |
|                            | copy{primary|secondary}<FIRMWARE-FILENAME>         | 142 |
|                            | copyprimarysecondary                               | 142 |
|                            | copy<REMOTE-URL>                                   | 143 |
|                            | copysecondaryprimary                               | 145 |
|                            | copy<STORAGE-URL>                                  | 145 |
| Dynamic                    | Segmentation                                       | 147 |
| SNMP                       |                                                    | 148 |
| ConfiguringSNMP            |                                                    | 148 |
| Aruba                      | Central integration                                | 150 |
| ConnectingtoArubaCentral   |                                                    | 150 |
| CustomCAcertificate        |                                                    | 150 |
| SupportmodeinArubaCentral  |                                                    | 151 |
| ArubaCentralcommands       |                                                    | 151 |
|                            | aruba-central                                      | 151 |
|                            | aruba-centralsupport-mode                          | 152 |
|                            | configuration-lockoutcentralmanaged                | 153 |
|                            | disable                                            | 154 |
|                            | enable                                             | 154 |
|                            | location-override                                  | 155 |
|                            | showaruba-central                                  | 156 |
|                            | showrunning-configcurrent-context                  | 157 |
| Port filtering             |                                                    | 158 |
| Portfilteringcommands      |                                                    | 158 |
|                            | portfilter                                         | 158 |
|                            | showportfilter                                     | 159 |
| DNS                        |                                                    | 162 |
| DNSclient                  |                                                    | 162 |
| ConfiguringtheDNSclient    |                                                    | 162 |
| DNSclientcommands          |                                                    | 163 |
|                            | ipdnsdomain-list                                   | 163 |
|                            | ipdnsdomain-name                                   | 164 |
|                            | ipdnshost                                          | 165 |
|                            | ipdnsserveraddress                                 | 166 |
|                            | showipdns                                          | 167 |
| Device                     | discovery and configuration                        | 168 |
| Deviceprofiles             |                                                    | 168 |
|                            | ConfiguringadeviceprofileforLLDP                   | 169 |
|                            | ConfiguringadeviceprofileforCDP                    | 169 |
|                            | ConfiguringadeviceprofileforlocalMACmatch          | 169 |
|                            | Deviceprofilecommands                              | 170 |
|                            | aaaauthenticationport-accessallow-cdp-bpdu         | 170 |
|                            | aaaauthenticationport-accessallow-cdp-proxy-logoff | 171 |
|                            | aaaauthenticationport-accessallow-lldp-bpdu        | 172 |
|                            | associatecdp-group                                 | 173 |
|                            | associatelldp-group                                | 174 |
|                            | associatemac-group                                 | 175 |
|                            | associaterole                                      | 176 |
|                            | disable                                            | 177 |
Contents|6

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

177
178
179
180
184
185
186
188
192
193
194
195
195
197
198
200
200
200
201
201
202
202
203
204
204
205
206
207
208
209
210
211
211
213
214
215
215
218
219
220
222
225
228
229
230
231
232
232
232
233
233
234
234
235
236

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

7

| Zero Touch                              | Provisioning       |           |          | 238 |
| --------------------------------------- | ------------------ | --------- | -------- | --- |
| ZTPsupport                              |                    |           |          | 238 |
| SettingupZTPonatrustednetwork           |                    |           |          | 239 |
| ZTPprocessduringswitchboot              |                    |           |          | 240 |
| ZTPVSFswitchoversupport                 |                    |           |          | 241 |
| ZTPcommands                             |                    |           |          | 241 |
|                                         | showztpinformation |           |          | 241 |
|                                         | ztpforceprovision  |           |          | 245 |
| Switch                                  | system and         | hardware  | commands | 247 |
| bluetoothdisable                        |                    |           |          | 247 |
| bluetoothenable                         |                    |           |          | 247 |
| clearevents                             |                    |           |          | 248 |
| cleariperrors                           |                    |           |          | 249 |
| consolebaud-rate                        |                    |           |          | 250 |
| domain-name                             |                    |           |          | 251 |
| hostname                                |                    |           |          | 251 |
| mtrace                                  |                    |           |          | 252 |
| showbluetooth                           |                    |           |          | 254 |
| showboot-history                        |                    |           |          | 255 |
| showcapacities                          |                    |           |          | 257 |
| showcapacities-status                   |                    |           |          | 258 |
| showconsole                             |                    |           |          | 259 |
| showcore-dump                           |                    |           |          | 259 |
| showdomain-name                         |                    |           |          | 261 |
| showenvironmentfan                      |                    |           |          | 262 |
| showenvironmentled                      |                    |           |          | 263 |
| showenvironmentpower-supply             |                    |           |          | 264 |
| showenvironmenttemperature              |                    |           |          | 265 |
| showevents                              |                    |           |          | 266 |
| showhostname                            |                    |           |          | 269 |
| showimages                              |                    |           |          | 270 |
| showiperrors                            |                    |           |          | 271 |
| showmodule                              |                    |           |          | 272 |
| showrunning-config                      |                    |           |          | 273 |
| showrunning-configcurrent-context       |                    |           |          | 277 |
| showstartup-config                      |                    |           |          | 278 |
| showsystem                              |                    |           |          | 279 |
| showsystemresource-utilization          |                    |           |          | 280 |
| showtech                                |                    |           |          | 281 |
| showusb                                 |                    |           |          | 283 |
| showusbfile-system                      |                    |           |          | 284 |
| showversion                             |                    |           |          | 285 |
| systemresource-utilizationpoll-interval |                    |           |          | 286 |
| topcpu                                  |                    |           |          | 286 |
| topmemory                               |                    |           |          | 287 |
| usb                                     |                    |           |          | 288 |
| usbmount|unmount                        |                    |           |          | 288 |
| Support                                 | and Other          | Resources |          | 290 |
| AccessingArubaSupport                   |                    |           |          | 290 |
| AccessingUpdates                        |                    |           |          | 291 |
|                                         | ArubaSupportPortal |           |          | 291 |
|                                         | MyNetworking       |           |          | 291 |
| WarrantyInformation                     |                    |           |          | 291 |
| RegulatoryInformation                   |                    |           |          | 291 |
Contents|8

Documentation Feedback

292

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

9

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A,R8Q67A,R8Q68A,R8Q69A,R8Q70A,
R8Q71A,R8V08A,R8V09A,R8V10A,R8V11A,R8V12A,R8Q72A)
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
<example-text> substitutewithanactualvalueinacommandorincode:
n
n <example-text>
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
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
10
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |
| ----------------------------- | --- | ------------------ | --- |

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
| On the 6200 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|11

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

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

Aruba Network Analytics Engine introduction

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

13

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

About AOS-CX | 14

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

15

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

1. Connect the network to a data port.

See the Installation Guide for switch to determine the location of the switch ports.

2.

If the switch is powered on, power off the switch.

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image
is being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

Initial configuration using the Aruba CX mobile app

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

19

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

Initial Configuration | 20

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

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

Procedure

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

23

1. ConnecttheUSB-CportontheswitchtotheUSB-CportonthecomputerusingaUSB-Ccable.
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
| Switch(config)#:    |     | interface   | 1/1/1    |         |            |      |
| ------------------- | --- | ----------- | -------- | ------- | ---------- | ---- |
| Switch(config-if)#: |     | description |          | IN-BAND | Management | Port |
| Switch(config-if)#: |     | vlan        | access   | 1       |            |      |
| Switch(config-if)#: |     | no          | shutdown |         |            |      |
| Switch(config-if)#: |     | end         |          |         |            |      |
Switch#
!
| Switch(config)#: |     | interface | vlan | 1   |     |     |
| ---------------- | --- | --------- | ---- | --- | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | ip dhcp     |     |     |     |
| ------------------------ | --- | --- | ----------- | --- | --- | --- |
| Switch(config-if-vlan)#: |     |     | no shutdown |     |     |     |
| Switch(config-if-vlan)#: |     |     | end         |     |     |     |
Switch#
!
WithoutDHCPConfiguration
| switch#:                | config |      |             |            |      |     |
| ----------------------- | ------ | ---- | ----------- | ---------- | ---- | --- |
| switch(config)#:        |        | vlan | 1           |            |      |     |
| Switch(config-vlan-1)#: |        |      | description | Management | VLAN |     |
| Switch(config-vlan-1)#: |        |      | end         |            |      |     |
Switch#
!
| Switch(config)#:    |     | interface   | 1/1/1    |         |            |      |
| ------------------- | --- | ----------- | -------- | ------- | ---------- | ---- |
| Switch(config-if)#: |     | description |          | IN-BAND | Management | Port |
| Switch(config-if)#: |     | vlan        | access   | 1       |            |      |
| Switch(config-if)#: |     | no          | shutdown |         |            |      |
| Switch(config-if)#: |     | end         |          |         |            |      |
Switch#
!
| Switch(config)#: |     | interface | vlan | 1   |     |     |
| ---------------- | --- | --------- | ---- | --- | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | no ip       | dhcp            |     |     |
| ------------------------ | --- | --- | ----------- | --------------- | --- | --- |
| Switch(config-if-vlan)#: |     |     | ip address  | 192.168.10.1/24 |     |     |
| Switch(config-if-vlan)#: |     |     | no shutdown |                 |     |     |
| Switch(config-if-vlan)#: |     |     | end         |                 |     |     |
Switch#
| Logging | into the | switch | for | the first | time |     |
| ------- | -------- | ------ | --- | --------- | ---- | --- |
25
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- |

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
switch# config
switch(config)#
| Setting | switch | time | using the | NTP client |     |
| ------- | ------ | ---- | --------- | ---------- | --- |
Prerequisites
n TheIPaddressordomainnameofanNTPserver.
n IftheNTPserverusesauthentication,obtainthepasswordrequiredtocommunicatewiththeNTP
server.
Procedure
1. IftheNTPserverrequiresauthentication,definetheauthenticationkeyfortheNTPclientwiththe
| commandntp                               |     | authentication. |     |     |         |
| ---------------------------------------- | --- | --------------- | --- | --- | ------- |
| 2. ConfigureanNTPserverwiththecommandntp |     |                 |     |     | server. |
3. Bydefault,NTPtrafficissentonthedefaultVRF.IfyouwanttosendNTPtrafficonthe
| managementVRF,usethecommandntp |     |     |     | vrf. |     |
| ------------------------------ | --- | --- | --- | ---- | --- |
4. ReviewyourNTPconfigurationsettingswiththecommandsshow ntp serversandshow ntp
status.
5. Seethecurrentswitchtime,date,andtimezonewiththecommandshow clock.
Example
InitialConfiguration |26

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
|       | Banner  | updated | successfully! |     |     |     |     |     |     |     |
| ----- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Using | the Web |         | UI            |     |     |     |     |     |     |     |
TheWebUIisdisabledbydefault.Followthesestepstoenableitonthemanagementportandlogin.
TheWebUIisenabledbydefaultonthedefaultVRF.
Prerequisites
n AconnectiontotheswitchCLI.
Procedure
27
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
1. Switchtothemanagementinterfacecontextwiththecommandinterface mgmt.
2. Bydefault,themanagementinterfaceonthemanagementportisenabled.Ifitwasdisabled,re-
|     | enableitwiththecommandno |     | shutdown. |     |     |
| --- | ------------------------ | --- | --------- | --- | --- |
3. Usethecommandip dhcptoconfigurethemanagementinterfacetoautomaticallyobtainan
addressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastaticIPv4or
IPv6address,defaultgateway,andDNSserverwiththecommandsip address,ipv6 address,ip
static,default-gateway,andnameserver.
4. SSHisenabledbydefaultonthemanagementVRF.Ifdisabled,enableSSHwiththecommand
|     | ssh server | vrf mgmt. |     |     |     |
| --- | ---------- | --------- | --- | --- | --- |
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
| switch(config)#         |     | interface | mgmt        |                   |     |
| ----------------------- | --- | --------- | ----------- | ----------------- | --- |
| switch(config-if-mgmt)# |     |           | no shutdown |                   |     |
| switch(config-if-mgmt)# |     |           | ip static   | 198.168.100.10/24 |     |
InitialConfiguration |28

| switch(config-if-mgmt)# |     |     |        | default-gateway |     |                 | 198.168.100.200 |         |     |          |     |
| ----------------------- | --- | --- | ------ | --------------- | --- | --------------- | --------------- | ------- | --- | -------- | --- |
| switch(config-if-mgmt)# |     |     |        | nameserver      |     | 198.168.100.201 |                 |         |     |          |     |
| Restoring               |     | the | switch |                 | to  | factory         |                 | default |     | settings |     |
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
<REMOTE-
URL> running-configorcopy <STORAGE-URL> running-configfollowedbycopy running-
|     | config | startup-config. |     |     |     |     |     |     |     |     |     |
| --- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Example
Backinguptherunningconfigurationtoafileonaremoteserver(usingTFTP),resettingtheswitchtoits
factorydefaultstate,andthenrestoringthesavedconfiguration.
switch# copy running-config tftp://192.168.1.10/backup_cfg json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     |     | Dload |     | Upload | Total | Spent | Left Speed |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------ | ----- | ----- | ---------- |
100 10340 0 0 100 10340 0 1329k --:--:-- --:--:-- --:--:-- 1329k
100 10340 0 0 100 10340 0 1313k --:--:-- --:--:-- --:--:-- 1313k
switch#
switch#
| switch# |     | erase | all zeroize |     |     |     |     |     |     |     |     |
| ------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
This will securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the
| switch   | unavailable |         |         | until  | the zeroization  |        |     | is complete. |           |     |     |
| -------- | ----------- | ------- | ------- | ------ | ---------------- | ------ | --- | ------------ | --------- | --- | --- |
| This     | should      | take    | several |        | minutes          | to     | one | hour to      | complete. |     |     |
| Continue |             | (y/n)?  | y       |        |                  |        |     |              |           |     |     |
| The      | system      | is      | going   | down   | for zeroization. |        |     |              |           |     |     |
| [        | OK ]        | Stopped | PSPO    | Module | Daemon.          |        |     |              |           |     |     |
| [        | OK ]        | Stopped | AOS-CX  | Switch |                  | Daemon | for | BCM.         |           |     |     |
...
| [         | OK ]     | Stopped      | Remount |                                                   | Root | and Kernel |     | File | Systems. |     |     |
| --------- | -------- | ------------ | ------- | ------------------------------------------------- | ---- | ---------- | --- | ---- | -------- | --- | --- |
| [         | OK ]     | Reached      | target  | Shutdown.                                         |      |            |     |      |          |     |     |
| reboot:   |          | Restarting   |         | system                                            |      |            |     |      |          |     |     |
| Press     | Esc      | for          | boot    | options                                           |      |            |     |      |          |     |     |
| ServiceOS |          | Information: |         |                                                   |      |            |     |      |          |     |     |
|           | Version: |              |         | GT.01.03.0006                                     |      |            |     |      |          |     |     |
|           | Build    | Date:        |         | 2018-10-30                                        |      | 14:20:44   |     | PDT  |          |     |     |
|           | Build    | ID:          |         | ServiceOS:GT.01.03.0006:8ee0faaa52da:201810301420 |      |            |     |      |          |     |     |
29
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |

|     | SHA: |     |     | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx |     |     |     |     |     |
| --- | ---- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
...
|     | ################         |          | Preparing                                      |                 | for zeroization                   |                         | ################# |            |     |
| --- | ------------------------ | -------- | ---------------------------------------------- | --------------- | --------------------------------- | ----------------------- | ----------------- | ---------- | --- |
|     | ################         |          | Storage                                        | zeroization     |                                   | ####################### |                   |            |     |
|     | ################         |          | WARNING:                                       | DO              | NOT POWER                         |                         | OFF UNTIL         | ########## |     |
|     | ################         |          |                                                | ZEROIZATION     |                                   | IS                      | COMPLETE          | ########## |     |
|     | ################         |          | This                                           | should          | take                              | several                 | minutes           | ########## |     |
|     | ################         |          | to one                                         | hour            | to complete                       |                         |                   | ########## |     |
|     | ################         |          | Restoring                                      |                 | files ########################### |                         |                   |            |     |
|     | Boot Profiles:           |          |                                                |                 |                                   |                         |                   |            |     |
|     | 0. Service               | OS       | Console                                        |                 |                                   |                         |                   |            |     |
|     | 1. Primary               | Software | Image                                          | [XL.10.02.0010] |                                   |                         |                   |            |     |
|     | 2. Secondary             | Software |                                                | Image           | [XL.10.02.0010]                   |                         |                   |            |     |
|     | Select profile(primary): |          |                                                |                 |                                   |                         |                   |            |     |
|     | Booting                  | primary  | software                                       | image...        |                                   |                         |                   |            |     |
|     | Verifying                | Image... |                                                |                 |                                   |                         |                   |            |     |
|     | Image Info:              |          |                                                |                 |                                   |                         |                   |            |     |
|     |                          | Name:    | AOS-CX                                         |                 |                                   |                         |                   |            |     |
|     | Version:                 |          | XL.10.02.0010                                  |                 |                                   |                         |                   |            |     |
|     | Build                    | Id:      | AOS-CX:XL.10.02.0010:feaf5b9b7f09:201901292014 |                 |                                   |                         |                   |            |     |
|     | Build                    | Date:    | 2019-01-29                                     | 12:43:50        |                                   | PST                     |                   |            |     |
|     | Extracting               | Image... |                                                |                 |                                   |                         |                   |            |     |
|     | Loading                  | Image... |                                                |                 |                                   |                         |                   |            |     |
Done.
|     | kexec_core: | Starting     | new | kernel |     |     |     |     |     |
| --- | ----------- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
|     | System is   | initializing |     |        |     |     |     |     |     |
fips_post_check[5473]: FIPS_POST: Cryptographic selftest started...SUCCESS
|     | [  OK ] | Started | Login | banner | readiness |     | check. |     |     |
| --- | ------- | ------- | ----- | ------ | --------- | --- | ------ | --- | --- |
...
|     | 8400X login: | admin |     |     |     |     |     |     |     |
| --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Password:
switch#
switch#
switch# copy tftp://192.168.1.10/backup_cfg running-config json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     | Dload |     | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ----------- | ---------- |
100 10340 100 10340 0 0 2858k 0 --:--:-- --:--:-- --:--:-- 2858k
100 10340 100 10340 0 0 2804k 0 --:--:-- --:--:-- --:--:-- 2804k
Large configuration changes will take time to process, please be patient.
switch#
switch#
|     | switch# | copy running-config |     |     | startup-config |     |     |     |     |
| --- | ------- | ------------------- | --- | --- | -------------- | --- | --- | --- | --- |
Large configuration changes will take time to process, please be patient.
switch#
| Management |     |     | interface |     | commands |     |     |     |     |
| ---------- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- |
default-gateway
| default-gateway |                 | <IP-ADDR> |           |     |     |     |     |     |     |
| --------------- | --------------- | --------- | --------- | --- | --- | --- | --- | --- | --- |
| no              | default-gateway |           | <IP-ADDR> |     |     |     |     |     |     |
InitialConfiguration |30

Description
AssignsanIPv4orIPv6defaultgatewaytothemanagementinterface.AnIPv4defaultgatewaycanonly
beconfiguredifastaticIPv4addresswasassignedtothemanagementinterface.AnIPv6default
gatewaycanonlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.The
defaultgatewayshouldbeonthesamenetworksegment.
Thenoformofthiscommandremovesthedefaultgatewayfromthemanagementinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Examples
SettingadefaultgatewaywiththeIPv4addressof198.168.5.1:
| switch(config)#         | interface | mgmt            |             |
| ----------------------- | --------- | --------------- | ----------- |
| switch(config-if-mgmt)# |           | default-gateway | 198.168.5.1 |
SettinganIPv6addressof2001:DB8::1:
| switch(config)#         | interface | mgmt            |              |
| ----------------------- | --------- | --------------- | ------------ |
| switch(config-if-mgmt)# |           | default-gateway | 2001:DB8::1  |
| Command History         |           |                 |              |
| Release                 |           |                 | Modification |
| 10.07orearlier          |           |                 | --           |
| Command Information     |           |                 |              |
| Platforms               | Command   | context         | Authority    |
6200 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip static
| ip static <IP-ADDR>/<MASK> |                  |     |     |
| -------------------------- | ---------------- | --- | --- |
| no ip static               | <IP-ADDR>/<MASK> |     |     |
Description
AssignsanIPv4orIPv6addresstothemanagementinterface.
ThenoformofthiscommandremovestheIPaddressfromthemanagementinterfaceandsetsthe
interfacetooperateasaDHCPclient.
31
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| <MASK> |     |     |     |     | SpecifiesthenumberofbitsinanIPv4orIPv6addressmaskin |     |
| ------ | --- | --- | --- | --- | --------------------------------------------------- | --- |
CIDRformat(x),wherexisadecimalnumberfrom0to32for
IPv4,and0to128forIPv6.
Examples
SettinganIPv4addressof198.51.100.1withamaskof24bits:
| switch(config)#         |     | interface |     | mgmt   |                 |     |
| ----------------------- | --- | --------- | --- | ------ | --------------- | --- |
| switch(config-if-mgmt)# |     |           | ip  | static | 198.51.100.1/24 |     |
SettinganIPv6addressof2001:DB8::1withamaskof32bits:
| switch(config)#         |             | interface |         | mgmt   |                |     |
| ----------------------- | ----------- | --------- | ------- | ------ | -------------- | --- |
| switch(config-if-mgmt)# |             |           | ip      | static | 2001:DB8::1/32 |     |
| Command                 | History     |           |         |        |                |     |
| Release                 |             |           |         |        | Modification   |     |
| 10.07orearlier          |             |           |         |        | --             |     |
| Command                 | Information |           |         |        |                |     |
| Platforms               | Command     |           | context |        | Authority      |     |
config-if-mgmt
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
InitialConfiguration |32

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
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
| switch(config)#         | interface | mgmt       |             |             |
| ----------------------- | --------- | ---------- | ----------- | ----------- |
| switch(config-if-mgmt)# |           | nameserver | 198.168.5.1 | 198.168.5.2 |
SettingprimaryandsecondaryDNSserverswiththeIPv6addressesof2001:DB8::1and2001:DB8::2:
| switch(config)#         | interface | mgmt       |              |             |
| ----------------------- | --------- | ---------- | ------------ | ----------- |
| switch(config-if-mgmt)# |           | nameserver | 2001:DB8::1  | 2001:DB8::2 |
| Command History         |           |            |              |             |
| Release                 |           |            | Modification |             |
| 10.07orearlier          |           |            | --           |             |
| Command Information     |           |            |              |             |
| Platforms               | Command   | context    | Authority    |             |
6200 config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface | mgmt |     |     |     |
| -------------- | ---- | --- | --- | --- |
| show interface | mgmt |     |     |     |
Description
Showsstatusandconfigurationinformationforthemanagementinterface.
Example
| switch# | show interface | mgmt |          |     |
| ------- | -------------- | ---- | -------- | --- |
| Address | Mode           |      | : static |     |
| Admin   | State          |      | : up     |     |
33
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

| Mac Address              |            |                 | : 02:42:ac:11:00:02          |
| ------------------------ | ---------- | --------------- | ---------------------------- |
| IPv4 address/subnet-mask |            |                 | : 192.168.1.10/16            |
| Default                  | gateway    | IPv4            | : 192.168.1.1                |
| IPv6 address/prefix      |            |                 | : 2001:db8:0:1::129/64       |
| IPv6 link                | local      | address/prefix: | fe80::7272:cfff:fefd:e485/64 |
| Default                  | gateway    | IPv6            | : 2001:db8:0:1::1            |
| Primary                  | Nameserver |                 | : 2001::1                    |
| Secondary                | Nameserver |                 | : 2001::2                    |
| Command History          |            |                 |                              |
| Release                  |            |                 | Modification                 |
| 10.07orearlier           |            |                 | --                           |
| Command Information      |            |                 |                              |
| Platforms                | Command    | context         | Authority                    |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
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
| switch(config)# | ntp | authentication |     |
| --------------- | --- | -------------- | --- |
Disablingauthenticationsupport:
| switch(config)#     | no  | ntp authentication |              |
| ------------------- | --- | ------------------ | ------------ |
| Command History     |     |                    |              |
| Release             |     |                    | Modification |
| 10.07orearlier      |     |                    | --           |
| Command Information |     |                    |              |
InitialConfiguration |34

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp authentication-key
| ntp authentication-key    |     | <KEY-ID>  | {md5 | |          | sha1}           |     |
| ------------------------- | --- | --------- | ---- | ---------- | --------------- | --- |
| [{ <PLAINTXT-KEY>         |     | [trusted] | |    | ciphertext | <ENCRYPTED-KEY> | }]  |
| no ntp authentication-key |     | <KEY-ID>  |      | {md5       | | sha1}         |     |
| [{ <PLAINTXT-KEY>         |     | [trusted] | |    | ciphertext | <ENCRYPTED-KEY> | }]  |
Description
DefinesanauthenticationkeythatisusedtosecuretheexchangewithanNTPtimeserver.This
commandprovidesprotectionagainstaccidentallysynchronizingtoatimesourcethatisnottrusted.
Thenoformofthiscommandremovestheauthenticationkey.
| Parameter |     |     |     | Description                                     |     |     |
| --------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| <KEY-ID>  |     |     |     | SpecifiestheauthenticationkeyID.Range:1to65534. |     |     |
| md5       |     |     |     | SelectsMD5keyencryption.                        |     |     |
| sha1      |     |     |     | SpecifiesSHA1keyencryption.                     |     |     |
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
Whenthekeyisnotprovidedonthecommandline,plaintextkey
promptingoccursuponpressingEnter,followedbypromptingasto
whetherthekeyistobetrusted.Theenteredkeycharactersaremasked
withasterisks.
Examples
Definingkey10withMD5encryptionandaprovidedplaintexttrustedkey:
switch(config)#
|     |     | ntp authentication-key |     |     | 10 md5 F82#450b | trusted |
| --- | --- | ---------------------- | --- | --- | --------------- | ------- |
Definingkey5withSHA1encryptionandapromptedplaintexttrustedkey:
35
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- |

| switch(config)# |     | ntp            | authentication-key |      |     | 5 sha1 |
| --------------- | --- | -------------- | ------------------ | ---- | --- | ------ |
| Enter the       | NTP | authentication |                    | key: |     |        |
*********
| Re-Enter  | the | NTP authentication |            |        | key: | ********* |
| --------- | --- | ------------------ | ---------- | ------ | ---- | --------- |
| Configure | the | key                | as trusted | (y/n)? |      | y         |
Removingkey10:
| switch(config)# |             | no  | ntp authentication-key |     |              | 10  |
| --------------- | ----------- | --- | ---------------------- | --- | ------------ | --- |
| Command         | History     |     |                        |     |              |     |
| Release         |             |     |                        |     | Modification |     |
| 10.07orearlier  |             |     |                        |     | --           |     |
| Command         | Information |     |                        |     |              |     |
| Platforms       | Command     |     | context                |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp disable
ntp disable
Description
DisablestheNTPclientontheswitch.TheNTPclientisdisabledbydefault.
Examples
DisablingtheNTPclient.
| switch(config)# |             | ntp | disable |     |              |     |
| --------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Command         | History     |     |         |     |              |     |
| Release         |             |     |         |     | Modification |     |
| 10.07orearlier  |             |     |         |     | --           |     |
| Command         | Information |     |         |     |              |     |
| Platforms       | Command     |     | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp enable
InitialConfiguration |36

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
| switch(config)#     | no      | ntp enable |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
37
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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

Specifies the minimum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 6 (64 seconds).

Specifies the maximum polling interval in seconds, as a power of
2. Range: 4 to 17. Default: 10 (1024 seconds).

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

NTP uses a stratum to describe the distance between a network device and an authoritative time
source:

n A stratum 1 time server is directly attached to an authoritative time source (such as a radio or atomic

clock or a GPS time source).

n A stratum 2 NTP server receives its time through NTP from a stratum 1 time server.

When using multiple servers with same stratum setting, the best practice to configure a preferred
server, so NTP will attempt to use the preferred server as the primary NTP connection. If a preferred

Initial Configuration | 38

serverisnotmanuallysetwhenNTPisenabled,theconfiguredserverwiththeloweststratumwill
automaticallybesetasthepreferredserver.Ifthereareserverswiththesamestratum,thisautoprefer
statuswillpreventAOS-CXfromtogglingbetweendifferentserversastheprimaryserver.Autoprefer
selectionofserverswithsamestratum(ifnotmanuallyselected)maychangeafterreconfiguringthe
switch,orafterexecutingtherebootcommand.
Examples
Definingthentpserverpool.ntp.org,usingiburst,andNTPversion4.
| switch(config)# | ntp | server | pool.ntp.org | iburst version | 4   |
| --------------- | --- | ------ | ------------ | -------------- | --- |
Removingthentpserverpool.ntp.org.
| switch(config)# | no  | ntp server | pool.ntp.org |     |     |
| --------------- | --- | ---------- | ------------ | --- | --- |
Definingthentpservermy-ntp.mydomain.comandmakesitthepreferredserver.
| switch(config)#     | ntp     | server  | my-ntp.mydomain.com | prefer |     |
| ------------------- | ------- | ------- | ------------------- | ------ | --- |
| Command History     |         |         |                     |        |     |
| Release             |         |         | Modification        |        |     |
| 10.07orearlier      |         |         | --                  |        |     |
| Command Information |         |         |                     |        |     |
| Platforms           | Command | context | Authority           |        |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp trusted-key
| ntp trusted-key    | <KEY-ID> |     |     |     |     |
| ------------------ | -------- | --- | --- | --- | --- |
| no ntp trusted-key | <KEY-ID> |     |     |     |     |
Description
Setsakeyastrusted.WhenNTPauthenticationisenabled,theswitchonlysynchronizeswithtime
serversthattransmitpacketscontainingatrustedkey.
Thenoformofthiscommandremovesthetrusteddesignationfromakey.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<KEY-ID> Specifiestheidentificationnumberofthekeytosetastrusted.
Range:1to65534.
Examples
Definingkey10asatrustedkey.
39
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ntp vrf
ntp vrf <VRF-NAME>
| no ntp vrf <VRF-NAME> |     |     |     |
| --------------------- | --- | --- | --- |
Description
SpecifiestheVRFonwhichtheNTPclientcommunicateswithanNTPserver.
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
| switch(config)# | no  | ntp vrf |     |
| --------------- | --- | ------- | --- |
| Command History |     |         |     |
InitialConfiguration |40

| Release             |         |         | Modification |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ntp              | associations |     |     |     |     |     |
| --------------------- | ------------ | --- | --- | --- | --- | --- |
| show ntp associations |              |     |     |     |     |     |
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
o *:Remotepeerorserverpresentlyusedasaprimaryreference
o o:PPSpeer(whenthepreferpeerisvalid)
n ID:Servernumber.
n NAME:NTPserverFQDN/IPaddress(Onlythefirst24charactersofthenamearedisplayed).
n REMOTE:RemoteserverIPaddress.
n REF_ID:ReferenceIDfortheremoteserver(CanbeanIPaddress).
ST:(Stratum)NumberofhopsbetweentheNTPclientandthereferenceclock.
n
n LAST:Timesincethelastpacketwasreceivedinsecondsunlessanotherunitisindicated.
n POLL:Interval(inseconds)betweenNTPpollpackets.Maximum(1024)reachedasserverandclient
sync.
n REACH:8-bitoctalnumberthatdisplaysstatusofthelasteightNTPmessages(377=allmessages
received).
Example
| switch# | show ntp associations |     |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------
| ID  | NAME |     | REMOTE | REF-ID | ST LAST POLL | REACH |
| --- | ---- | --- | ------ | ------ | ------------ | ----- |
----------------------------------------------------------------------
| 1                  | 192.0.1.1 |              | 192.0.1.1 | .INIT. | 16 -     | 64 0 |
| ------------------ | --------- | ------------ | --------- | ------ | -------- | ---- |
| * 2 time.apple.com |           | 17.253.2.253 |           | .GPSs. | 2 70 128 | 377  |
----------------------------------------------------------------------
41
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- | --- |

| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp                     | authentication-keys |     |     |
| ---------------------------- | ------------------- | --- | --- |
| show ntp authentication-keys |                     |     |     |
Description
Showsthecurrentlydefinedauthenticationkeys.
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ntp         | servers |     |     |
| ---------------- | ------- | --- | --- |
| show ntp servers |         |     |     |
Description
ShowsallconfiguredNTPservers,includinganyDHCPservers,defaultpoolserversoranyserverwith
| thestatusauto | prefer. |     |     |
| ------------- | ------- | --- | --- |
Example
InitialConfiguration |42

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
| show | ntp statistics |     |     |     |
| ---- | -------------- | --- | --- | --- |
| show | ntp statistics |     |     |     |
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
Rate-limitedpkts:Numberofpacketsdiscardedduetoratelimitation.
n
n KODpkts:NumberofKissofDeathpacketssent.
Examples
| switch(config)# |                   | show ntp statistics |     |     |
| --------------- | ----------------- | ------------------- | --- | --- |
|                 |                   | Rx-pkts 100         |     |     |
| Current         | Version           | Rx-pkts 80          |     |     |
|                 | Old Version       | Rx-pkts 20          |     |     |
|                 |                   | Err-pkts 2          |     |     |
|                 | Auth-failed-pkts  | 1                   |     |     |
|                 | Declined-pkts     | 0                   |     |     |
|                 | Restricted-pkts   | 0                   |     |     |
|                 | Rate-limited-pkts | 0                   |     |     |
|                 |                   | KoD-pkts 0          |     |     |
43
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | ------------------ | --- | --- |

| Command        | History     |     |         |     |     |              |     |     |
| -------------- | ----------- | --- | ------- | --- | --- | ------------ | --- | --- |
| Release        |             |     |         |     |     | Modification |     |     |
| 10.07orearlier |             |     |         |     |     | --           |     |     |
| Command        | Information |     |         |     |     |              |     |     |
| Platforms      | Command     |     | context |     |     | Authority    |     |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp        | status |     |     |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| show ntp status |        |     |     |     |     |     |     |     |
Description
ShowsthestatusofNTPontheswitch.
Examples
DisplayingthestatusinformationwhentheswitchisnotsyncedtoanNTPserver:
| switch#            | show ntp    | status  |             |        |         |          |              |     |
| ------------------ | ----------- | ------- | ----------- | ------ | ------- | -------- | ------------ | --- |
| NTP is             | enabled.    |         |             |        |         |          |              |     |
| NTP authentication |             |         | is enabled. |        |         |          |              |     |
| NTP is             | using the   | default |             | VRF    | for NTP | server   | connections. |     |
| Wed Nov            | 23 23:29:10 |         | PDT         | 2016   |         |          |              |     |
| NTP uptime:        | 187         | days,   | 1           | hours, | 37      | minutes, | 48 seconds   |     |
| Not synchronized   |             | with    | an          | NTP    | server. |          |              |     |
DisplayingthestatusinformationwhentheswitchissyncedtoanNTPserver:
| switch#            | show ntp    | status    |             |              |             |              |              |     |
| ------------------ | ----------- | --------- | ----------- | ------------ | ----------- | ------------ | ------------ | --- |
| NTP is             | enabled.    |           |             |              |             |              |              |     |
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
InitialConfiguration |44

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
45
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
| Command    | History     |         |         |     |                                                   |
| ---------- | ----------- | ------- | ------- | --- | ------------------------------------------------- |
| Release    |             |         |         |     | Modification                                      |
| 10.08.1021 |             |         |         |     | Commandintroducedonthe6200,6300,6400SwitchSeries. |
| Command    | Information |         |         |     |                                                   |
| Platforms  |             | Command | context |     | Authority                                         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
46
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
|            | Server IP   | : 20.1.1.1                                        |     |
| ---------- | ----------- | ------------------------------------------------- | --- |
|            | Client IP   | : 20.1.1.2                                        |     |
|            | Client Port | : 58837                                           |     |
| Command    | History     |                                                   |     |
| Release    |             | Modification                                      |     |
| 10.08.1021 |             | Commandintroducedonthe6200,6300,6400SwitchSeries. |     |
Telnetaccess|47

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
| switch(config)# |             | telnet | server  | vrf mgmt                                          |
| --------------- | ----------- | ------ | ------- | ------------------------------------------------- |
| Command         | History     |        |         |                                                   |
| Release         |             |        |         | Modification                                      |
| 10.08.1021      |             |        |         | Commandintroducedonthe6200,6300,6400SwitchSeries. |
| Command         | Information |        |         |                                                   |
| Platforms       | Command     |        | context | Authority                                         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
48
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | ------------------ | --- | --- |

Chapter 5

Interface configuration

Interface configuration

Configuring a layer 2 interface

Procedure

1. Change to the interface configuration context for the interface with the command interface.

2. Set the interface MTU (maximum transmission unit) with the command mtu.

3. Review interface configuration settings with the command show interface.

Example

switch(config)# interface 1/1/1
switch(config-if)# mtu 1900

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

n Non-Aruba branded products

n HPE branded products that were designed for non-AOS-CX switch models (e.g. Comware)

n HPE branded products designated for use in HPE Compute Servers or Storage

n Transceivers originally designated for use in Aruba WLAN controllers or former Mobility Access Switch

(MAS) products

n End-of-life Aruba Transceivers

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

49

Theunsupportedtransceivermode(UT-mode)isdesignedtoallowthepossibleuseofthese
unsupportedproducts.Notallunsupportedproductscanberecognizedandenabled;theymaybe
unabletobeidentified(donotfollowtheproperMSAstandardsforidentification).Theseunsupported
transceiverproductsareenabledonlyonabest-effortbasisandtherearenoguaranteesimpliedfor
theircontinuedoperation.
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
Interfaceconfiguration|50

link-poe
| lldp dot3 | eee                     |     |     |     |     |     |     |
| --------- | ----------------------- | --- | --- | --- | --- | --- | --- |
| lldp dot3 | poe                     |     |     |     |     |     |     |
| lldp med  | poe                     |     |     |     |     |     |     |
| lldp med  | poe [priority-override] |     |     |     |     |     |     |
persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
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
uplink
n
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
51
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

5. Applythepersonaconfigurationtotheinterfaceandsetthemodewiththecommandpersona
custom <PERSONA-NAME> <mode>.Notethat<custom>isanoptionalargument,requiredonlyif
thepersonaisnotoneofthepredefinednames(neitheruplinknoraccess).
Forinformationonthisfeature,seetherelatedvideoontheArubaAirHeadsBroadcastingChannel.
Examples
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
Interfaceconfiguration|52

| Interface | commands |     |     |     |
| --------- | -------- | --- | --- | --- |
allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver
Description
Allowsunsupportedtransceiverstobeenabledorestablishconnections.Transceiverswithspeedsupto
100Gareenabledbythiscommand.
AsofAOS-CX10.06.0100,thiscommandisenabledbydefault,allowingtheuseofthirdpartytransceiver
productswithoutaddingthecommandintheconfiguration.Disablingthiscommandwiththenoformwillnow
disablethecommandintherunningandstoredconfigurations.
Thenoformofthiscommanddisallowsusingunsupportedtransceivers.
| Parameter |     |     | Description                                        |     |
| --------- | --- | --- | -------------------------------------------------- | --- |
| confirm   |     |     | Specifiesthatunsupportedtransceiverwarningsaretobe |     |
automaticallyconfirmed.
| log-interval | none |     | Disablesunsupportedtransceiverlogging. |     |
| ------------ | ---- | --- | -------------------------------------- | --- |
log-interval <INTERVAL> Setstheunsupportedtransceiverloggingintervalinminutes.
Default:1440minutes.Range:1440to10080minutes.
Usage
Whennoneoftheparametersarespecifieditwilldisplayawarningmessagetoacceptthewarranty
terms.Withconfirmoptionthewarningmessageisdisplayedbuttheuserisnotpromptedto(y/n)
answering.Warrantytermsmustbeagreedtoaspartofenablementandthesupportisonbesteffort
basis.
Examples
Allowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | allow-unsupported-transceiver |     |     |     |
| --------------- | ----------------------------- | --- | --- | --- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
| Do you agree | and do you | want to | continue (y/n)? | y   |
| ------------ | ---------- | ------- | --------------- | --- |
Allowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | allow-unsupported-transceiver |     |     | confirm |
| --------------- | ----------------------------- | --- | --- | ------- |
Warning: The use of unsupported transceivers, DACs, and AOCs is at your
own risk and may void support and warranty. Please see HPE Warranty terms
and conditions.
Configuringunsupportedtransceiverloggingwithanintervalofevery48hours:
53
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

switch(config)# allow-unsupported-transceiver log-interval 2880
Disablingunsupportedtransceiverlogging:
switch(config)# allow-unsupported-transceiver log-interval none
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no  | allow-unsupported-transceiver |     |     |
| --------------- | --- | ----------------------------- | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
| Continue    | (y/n)?      |               |           |       |
y
Disallowingunsupportedtransceiverswithconfirmationincommandsyntax:
| switch(config)# | no  | allow-unsupported-transceiver |     | confirm |
| --------------- | --- | ----------------------------- | --- | ------- |
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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Interfaceconfiguration|54

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
| SettingthedescriptionforaninterfacetoDataLink |     |             |          | 01: |
| --------------------------------------------- | --- | ----------- | -------- | --- |
| switch(config-if)#                            |     | description | DataLink | 01  |
Removingthedescriptionforaninterface.
| switch(config-if)# |     | no description |     |     |
| ------------------ | --- | -------------- | --- | --- |
| Command History    |     |                |     |     |
55
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
flow-control
| flow-control    | rxtx |     |     |
| --------------- | ---- | --- | --- |
| no flow-control | rxtx |     |     |
Description
Interfaceconfiguration|56

Commandflow-controlenablesnegotiationofIEEE802.3xlink-levelflowcontrolonthecurrent
interface.Theswitchadvertiseslink-levelflowcontrolsupporttothelinkpartner.Thefinalconfiguration
isdeterminedbasedonthecapabilitiesofbothpartners.
Eachinvocationofthiscommandreplacesthepreviousconfiguration.
Thenoformofthesecommandsdisablesanyconfiguredflowcontrolontheselectedinterface.
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
| switch(config-if)# |     | flow-control |       | rxtx |
DisablingsupportforRXTXflowcontrol:
| switch(config)#     |         | interface       | 1/1/1 |              |
| ------------------- | ------- | --------------- | ----- | ------------ |
| switch(config-if)#  |         | no flow-control |       | rxtx         |
| Command History     |         |                 |       |              |
| Release             |         |                 |       | Modification |
| 10.07orearlier      |         |                 |       | --           |
| Command Information |         |                 |       |              |
| Platforms           | Command | context         |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
57
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | ------------------ | --- | --- |

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
Examples
Interfaceconfiguration|58

| switch# | config |     |     |
| ------- | ------ | --- | --- |
switch(config)#
|     | interface | loopback | 1   |
| --- | --------- | -------- | --- |
switch(config-loopback-if)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
59
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip address
| ip address    | <IPV4-ADDR>/<MASK> |     |     | [secondary] |     |
| ------------- | ------------------ | --- | --- | ----------- | --- |
| no ip address | <IPV4-ADDR>/<MASK> |     |     | [secondary] |     |
Description
SetsanIPv4addressforthecurrentlayer3interface.
ThenoformofthiscommandremovestheIPv4addressfromtheinterface.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| <MASK> |     |     |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
| secondary |     |     |     |     | SpecifiesasecondaryIPaddress. |
| --------- | --- | --- | --- | --- | ----------------------------- |
Examples
AssigningtheIPaddress192.168.199.1withamaskof24bitstointerfaceVLAN10:
| switch(config)#         |     | interface |     | vlan       | 10               |
| ----------------------- | --- | --------- | --- | ---------- | ---------------- |
| switch(config-if-vlan)# |     |           |     | ip address | 192.168.199.1/24 |
RemovingtheIPaddress192.168.199.1withamaskof24bitsfrominterfaceVLAN10:
| switch(config)# |     | interface |     | vlan | 10  |
| --------------- | --- | --------- | --- | ---- | --- |
switch(config-if-vlan)#
|                |             |     |         | no ip address | 192.168.199.1/24 |
| -------------- | ----------- | --- | ------- | ------------- | ---------------- |
| Command        | History     |     |         |               |                  |
| Release        |             |     |         |               | Modification     |
| 10.07orearlier |             |     |         |               | --               |
| Command        | Information |     |         |               |                  |
| Platforms      | Command     |     | context |               | Authority        |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Interfaceconfiguration|60

ip mtu
ip mtu <VALUE>
no ip mtu
Description
SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthatcan
besentorreceivedbytheinterface.ThisvalueshouldbelessthanorequaltotheoverallMTUforthe
interface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE> SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
Examples
SettingtheIPMTUto576bytes:
| switch(config-if-vlan)# |         | ip mtu  | 576                       |
| ----------------------- | ------- | ------- | ------------------------- |
| Command History         |         |         |                           |
| Release                 |         |         | Modification              |
| 10.08                   |         |         | Subinterfacesupportadded. |
| 10.07orearlier          |         |         | --                        |
| Command Information     |         |         |                           |
| Platforms               | Command | context | Authority                 |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
61
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
TheIPaddressmustbedefinedontheswitch,anditmustexist
onthespecifiedVRF(whichisthedefaultVRF,ifthevrfoption
isnotused).SpecifytheaddressinIPv4format(x.x.x.x),where
xisadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |
| -------------- | --- | --- | ----------------------- |
Examples
SettingtheIPv4address10.10.10.5astheglobalsinglesourceaddress:
| switch#         | config |                     |                |
| --------------- | ------ | ------------------- | -------------- |
| switch(config)# |        | ip source-interface | all 10.10.10.5 |
ClearingtheglobalsinglesourceIPaddress10.10.10.5:
| switch(config)# |             | no ip source-interface | all 10.10.10.5 |
| --------------- | ----------- | ---------------------- | -------------- |
| Command         | History     |                        |                |
| Release         |             |                        | Modification   |
| 10.07orearlier  |             |                        | --             |
| Command         | Information |                        |                |
| Platforms       | Command     | context                | Authority      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK>{eui64 |                    | | [tag <ID>]} |
| --------------- | ------------------------ | ------------------ | ------------- |
| no ipv6 address |                          | <IPV6-ADDR>/<MASK> |               |
Description
SetsanIPv6addressontheinterface.
Interfaceconfiguration|62

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
switch(config-if)#
|     |     | ipv6 address | 2001:0db8:85a3::8a2e:0370:7334/24 |
| --- | --- | ------------ | --------------------------------- |
RemovingtheIPaddress2001:0db8:85a3::8a2e:0370:7334withmaskof24bits:
switch(config-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 source-interface
ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-relay
| simplivity | dns | all} {interface <IFNAME> | <IPV6-ADDR>} [vrf <VRF-NAME>]
63
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
| simplivity | | dns | | all |     | nothaveanaddressset. |
| ---------- | ----- | ----- | --- | -------------------- |
interface <IFNAME> Specifiesthenameoftheinterfacefromwhichthespecified
protocolobtainsitssourceIPaddress.
<IPV6-ADDR> SpecifiesthesourceIPaddresstouseforthespecifiedprotocol.
TheIPaddressmustbedefinedontheswitch,anditmustexist
onthespecifiedVRF(whichisthedefaultVRF,ifthevrfoption
isnotused).SpecifytheIPaddressinIPv6format
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
Interfaceconfiguration|64

ClearthesourceIPaddress2001:DB8::1.
| switch(config)#     | no      | ip source-interface | all 2001:DB8::1 |
| ------------------- | ------- | ------------------- | --------------- |
| Command History     |         |                     |                 |
| Release             |         |                     | Modification    |
| 10.07orearlier      |         |                     | --              |
| Command Information |         |                     |                 |
| Platforms           | Command | context             | Authority       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE>
SpecifiestheMTUinbytes.Range:46to9198.Default:1500.
Examples
SettingtheMTUoninterface1/1/1to1000bytes:
| switch(config)#    | interface | 1/1/1      |     |
| ------------------ | --------- | ---------- | --- |
| switch(config-if)# |           | no routing |     |
| switch(config-if)# |           | mtu 1000   |     |
SettingtheMTUoninterface1/1/1tothedefaultvalue:
| switch(config)#    | interface | 1/1/1      |     |
| ------------------ | --------- | ---------- | --- |
| switch(config-if)# |           | no routing |     |
| switch(config-if)# |           | no mtu     |     |
65
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
persona
persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
no persona {access | uplink | custom <PERSONA-NAME>} [copy | attach]
Description
Associatesoneofthreepersonatypeswithaninterfacetoclassifythepurposeorroleofaninterface.
Onthe10000SwitchSeries,“access”personaportsaretypicallyconnectedtoworkloads/VMs,andthe
“uplink”(fabric)personaportsareconnectedtothecore/spine.
Thenoformofthiscommandremovestheinterfacepersona.
| Parameter |     |     | Description                  |
| --------- | --- | --- | ---------------------------- |
| access    |     |     | Selectstheaccesspersonatype. |
| uplink    |     |     | Selectstheuplinkpersonatype. |
custom <PERSONA-NAME> Selectsthecustompersonatypewithauser-providedname.
Range:1to64printableASCIIcharactersincludingspace.
copy
Specifiesthemode:copiessettingsfromthepersonainterfaceof
thesamename.
| attach |     |     | Specifiesthemode:attachesthespecifiedinterfacetothe |
| ------ | --- | --- | --------------------------------------------------- |
personainterfaceofthesamename.
Usage
n Ifthemodeisspecified,eithercopyorattach,theinterfaceconfigurationisdependentonthe
interfacetemplatewhosenameis"access","uplink",or"<PERSONA-NAME>".Ontheotherhand,ifthe
modeisnotspecified,thenthepersonaisjustalabelintheinterface,anditsconfigurationisnot
modifiedeveniftheinterfacepersonaexists.Whenconfiguringthemode,oneofthefollowing
optionsispossible:
o Thecopyoptionperformsaone-timecopyofthetemplateinterface.Subsequentchangestothe
templatearenotcopiedandthe'persona'settingisjustalabel.Ifthemodeissettocopyandthe
interfacepersonadoesnotexist,thentheCLIcommandfailswiththemessage"Interfacepersona
notfound".
o Theattachoptionperformsacopyofthetemplateinterface,andsubsequentchangestothe
templateinterfaceconfigurationareimmediatelyappliedtoallattachedinterfaces.Thetemplate
Interfaceconfiguration|66

interfacedoesnotneedtoexistbeforeattachingotherinterfacestoit.Afterattachingatemplate,
thecopiedsettingscanbemodifiedforanindividualinterface.However,anychangeinthe
attachedtemplatewilloverwritethemodifiedvalueswiththenewtemplatevalues.
n Whenamodeisspecified,itshouldmatchaninterfacecreatedwiththecommandinterfacepersona
<PERSONA-NAME>.Theonlyexceptiontothisruleiswhenthemodeissettoattachandthepersona
doesnotalreadyexist.
n Themodeisonlyavailabletobeconfiguredforaninterfacethatmeetsthefollowingconditions:
o
IS aphysicalinterface
o IS NOTaLAGmember
o IS NOTapersonainterface
Examples
Configuringanaccesspersona:
| switch(config)#    | interface | 1/1/1  |     |
| ------------------ | --------- | ------ | --- |
| switch(config-if)# | persona   | access |     |
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
| switch(config-if)# | vlan        | access 100     |     |
| switch(config-if)# | exit        |                |     |
2.Applyingtheconfigurationfromthepersonanamed"mypersona"withcopymode:
| switch(config)#    | interface | 1/1/1            |      |
| ------------------ | --------- | ---------------- | ---- |
| switch(config-if)# | persona   | custom mypersona | copy |
| switch(config-if)# | exit      |                  |      |
Attachingacustompersonanamenamed"mypersona"toseveralinterfacessimultaneously:
1.Configuringaninterfacepersonanamed"mypersona":
67
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| switch(config)#    |     | interface   | persona         | mypersona |     |
| ------------------ | --- | ----------- | --------------- | --------- | --- |
| switch(config-if)# |     | no shutdown |                 |           |     |
| switch(config-if)# |     | vrf         | attach upstream |           |     |
| switch(config-if)# |     | exit        |                 |           |     |
2.Applyingthe"mypersona"configurationwithattachmode:
| switch(config)#     |         | interface | 1/1/1-1/1/24 |                                      |        |
| ------------------- | ------- | --------- | ------------ | ------------------------------------ | ------ |
| switch(config-if)#  |         | persona   | custom       | mypersona                            | attach |
| switch(config-if)#  |         | exit      |              |                                      |        |
| Command History     |         |           |              |                                      |        |
| Release             |         |           |              | Modification                         |        |
| 10.10               |         |           |              | Addedoptionalparameters:attach,copy. |        |
| 10.09               |         |           |              | Commandintroduced.                   |        |
| Command Information |         |           |              |                                      |        |
| Platforms           | Command | context   |              | Authority                            |        |
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
Examples
Enablingroutingsupportonaninterface:
| switch(config-if)# |     | routing |     |     |     |
| ------------------ | --- | ------- | --- | --- | --- |
Disablingroutingsupportonaninterface:
| switch(config-if)# |     | no routing |     |     |     |
| ------------------ | --- | ---------- | --- | --- | --- |
| Command History    |     |            |     |     |     |
Interfaceconfiguration|68

| Release        |             |         |     | Modification |
| -------------- | ----------- | ------- | --- | ------------ |
| 10.07orearlier |             |         |     | --           |
| Command        | Information |         |     |              |
| Platforms      | Command     | context |     | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
69
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | ------------------ | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| extended  |     |     | Showsadditionalstatistics.                     |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero      |     |     | Showsonlynonzerostatistics.                    |
| ------------- | --- | --- | ---------------------------------------------- |
| LAG           |     |     | ShowsLAGinterfaceinformation.                  |
| monitor       |     |     | Continuouslymonitorinterfacestatistics.        |
| LOOPBACK      |     |     | Showsloopbackinterfaceinformation.             |
| TUNNEL        |     |     | Showstunnelinterfaceinformation.               |
| VLAN          |     |     | ShowsVLANinterfaceinformation.                 |
| <LAG-ID>      |     |     | SpecifiestheLAGnumber.Range:1-256              |
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |
| <TUNNEL-ID>   |     |     | SpecifiesthetunnelID.Range:1-255               |
| <VLAN-ID>     |     |     | SpecifiestheVLANID.Range:1-4094                |
| VXLAN         |     |     | ShowstheVXLANinterfaceinformation.             |
| <VXLAN-ID>    |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |
Examples
Interfaceconfiguration|70

Showinginformationwheninterface1/1/1isconfigured:
| switch#     | show interface |       | 1/1/1 |     |     |     |     |     |     |
| ----------- | -------------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
| Interface   | 1/1/1          | is up |       |     |     |     |     |     |     |
| Admin state | is             | up    |       |     |     |     |     |     |     |
Link state: up for 1 minute (since Thu Nov 26 10:26:34 UTC 2020)
| Link transitions: |     | 3   |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, |     | MAC Address: |     | 88:3a:30:47:d1:df |     |     |     |     |
| --------- | --------- | --- | ------------ | --- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | cos             |           |     |             |         |     |     |       |         |
| ---------------- | --------------- | --------- | --- | ----------- | ------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s            |           |     |             |         |     |     |       |         |
| Auto-negotiation |                 | is        | on  |             |         |     |     |       |         |
| Energy-Efficient |                 | Ethernet  |     | is disabled |         |     |     |       |         |
| Flow-control:    |                 | off       |     |             |         |     |     |       |         |
| Error-control:   |                 | off       |     |             |         |     |     |       |         |
| MDI mode:        | MDIX            |           |     |             |         |     |     |       |         |
| VLAN Mode:       | native-untagged |           |     |             |         |     |     |       |         |
| Native           | VLAN:           | 1         |     |             |         |     |     |       |         |
| Allowed          | VLAN            | List:     | all |             |         |     |     |       |         |
| Rate collection  |                 | interval: |     | 300         | seconds |     |     |       |         |
| Rates            |                 |           |     |             | RX      |     | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization | %   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistics  |     |     |     |     | RX   |     | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets      |     |     |     |     | 0   |     | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     |     | 0   |     | 0   |     | 0   |
| Multicast    |     |     |     |     | 0   |     | 0   |     | 0   |
| Broadcast    |     |     |     |     | 0   |     | 0   |     | 0   |
| Bytes        |     |     |     |     | 0   |     | 0   |     | 0   |
| Jumbos       |     |     |     |     | 0   |     | 0   |     | 0   |
| Dropped      |     |     |     |     | 0   |     | 0   |     | 0   |
| Filtered     |     |     |     |     | 0   |     | 0   |     | 0   |
| Pause Frames |     |     |     |     | 0   |     | 0   |     | 0   |
| Errors       |     |     |     |     | 0   |     | 0   |     | 0   |
| CRC/FCS      |     |     |     |     | 0   |     | n/a |     | 0   |
| Collision    |     |     |     |     | n/a |     | 0   |     | 0   |
| Runts        |     |     |     |     | 0   |     | n/a |     | 0   |
| Giants       |     |     |     |     | 0   |     | n/a |     | 0   |
Showinginformationwhentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface |     | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | --- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |     |       |     |     |     |     |
...
| Auto-negotiation |     | is  | on with | downshift |     | active |     |     |     |
| ---------------- | --- | --- | ------- | --------- | --- | ------ | --- | --- | --- |
Showinginformationwhentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
71
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |     |     |
...
| Energy-Efficient |     |     | Ethernet | is  | enabled and | active |     |     |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
ShowinginformationwhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 | physical |     |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------------------------------------
|        |     |        |           | Link   | Admin       |     | Speed       |          |        | Flow-Control |          |     |
| ------ | --- | ------ | --------- | ------ | ----------- | --- | ----------- | -------- | ------ | ------------ | -------- | --- |
|        | EEE |        | PoE Power |        |             |     | Port        |          |        |              |          |     |
| Port   |     | Type   |           | Status | Config      |     | Status      | | Config | Status |              | | Config |     |
| Status | |   | Config | (Watts)   | State  | Information |     | Description |          |        |              |          |     |
----------------------------------------------------------------------------------
----------------------------------------------------------
| 1/1/1 |     | 1GbT |     | up          | up  |     | 1G  | auto | off |     | off |     |
| ----- | --- | ---- | --- | ----------- | --- | --- | --- | ---- | --- | --- | --- | --- |
| on    |     | on   | --  | 10M/100M/1G |     |     | --  |      |     |     |     |     |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| switch(config-if)# |     |       | show  | interface | 1/1/1 | monitor |     |     |     |       |         |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | ------- | --- | --- | --- | ----- | ------- | --- |
| Interface          |     | 1/1/1 | is up |           |       |         |     |     |     |       |         |     |
| Rate               |     |       |       |           | RX    |         |     | TX  |     | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| MBits       | /         | sec |     |     | 30196.43 |     |     | 30196.43 |     |       | 60392.85  |      |
| ----------- | --------- | --- | --- | --- | -------- | --- | --- | -------- | --- | ----- | --------- | ---- |
| MPkts       | /         | sec |     |     | 58977.39 |     |     | 58977.40 |     |       | 117954.79 |      |
|             | Unicast   |     |     |     | 0.00     |     |     | 0.00     |     |       |           | 0.00 |
|             | Multicast |     |     |     | 58977.39 |     |     | 58977.40 |     |       | 117954.79 |      |
|             | Broadcast |     |     |     | 0.00     |     |     | 0.00     |     |       |           | 0.00 |
| Utilization |           | %   |     |     | 75.49    |     |     | 75.49    |     |       | 150.98    |      |
| Statistic   |           |     |     |     | RX       |     |     | TX       |     | Total | (RX+TX)   |      |
---------------- -------------------- -------------------- --------------------
| Packets |           |           |         | 4756527649   |     |     | 4756527865   |     |     | 9513055514   |     |         |
| ------- | --------- | --------- | ------- | ------------ | --- | --- | ------------ | --- | --- | ------------ | --- | ------- |
|         | Unicast   |           |         |              | 0   |     |              | 0   |     |              |     | 0       |
|         | Multicast |           |         | 4756527649   |     |     | 4756527865   |     |     | 9513055514   |     |         |
|         | Broadcast |           |         |              | 2   |     |              | 0   |     |              |     | 2       |
| Bytes   |           |           |         | 304417778668 |     |     | 304417795428 |     |     | 608835574096 |     |         |
| Jumbos  |           |           |         |              | 0   |     |              | 0   |     |              |     | 0       |
| Dropped |           |           |         |              | 0   |     | 19028847730  |     |     | 19028847730  |     |         |
| Pause   | Frames    |           |         |              | 0   |     |              | 0   |     |              |     | 0       |
| Errors  |           |           |         |              | 0   |     |              | 0   |     |              |     | 0       |
|         | CRC/FCS   |           |         |              | 0   |     |              | n/a |     |              |     | 0       |
|         |           |           |         |              |     |     |              |     |     | help:        | ?,  | quit: q |
| Help    | for       | Interface | Monitor |              |     |     |              |     |     |              |     |         |
Interfaceconfiguration|72

| h Toggle | human-readable |            | mode       |     |     |     |     |
| -------- | -------------- | ---------- | ---------- | --- | --- | --- | --- |
| c Clear  | interface      | statistics |            |     |     |     |     |
| Does     | not apply      | to         | rates      |     |     |     |     |
| Arrows,  | PgUp, PgDn,    | Home,      | End        |     |     |     |     |
| Navigate | interface      |            | statistics |     |     |     |     |
Delay: 2
|     |     |     |     |     |     | help: | ?, quit: q |
| --- | --- | --- | --- | --- | --- | ----- | ---------- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsisbetween
zeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |       |         |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | ----- | ------- |
| Interface          | 1/1/1 | is up |           |                      |     |       |         |
| Rate               |       |       |           | RX                   | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Bits /      | sec |     |     | 3M  | 3M  |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts /      | sec |     |     | 316 | 316 |     | 633   |
| Unicast     |     |     |     | 319 | 319 |     | 638   |
| Multicast   |     |     |     | 0   | 0   |     | 0     |
| Broadcast   |     |     |     | 0   | 0   |     | 0     |
| Utilization | %   |     |     | < 1 | < 1 |     | < 1   |
| Statistic   |     |     |     | RX  | TX  |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets   |        |     |     | 577K | 577K |     | 1M  |
| --------- | ------ | --- | --- | ---- | ---- | --- | --- |
| Unicast   |        |     |     | 577K | 577K |     | 1M  |
| Multicast |        |     |     | 0    | 51   |     | 51  |
| Broadcast |        |     |     | 0    | 15   |     | 15  |
| Bytes     |        |     |     | 744M | 745M |     | 1G  |
| Jumbos    |        |     |     | 0    | 0    |     | 0   |
| Dropped   |        |     |     | 0    | 0    |     | 0   |
| Filtered  |        |     |     | 0    | 0    |     | 0   |
| Pause     | Frames |     |     | 0    | 0    |     | 0   |
| Errors    |        |     |     | 0    | 0    |     | 0   |
| CRC/FCS   |        |     |     | 0    | n/a  |     | 0   |
| Collision |        |     |     | n/a  | 0    |     | 0   |
| Runts     |        |     |     | 0    | n/a  |     | 0   |
| Giants    |        |     |     | 0    | n/a  |     | 0   |
...
| Command | History |     |     |                        |     |     |     |
| ------- | ------- | --- | --- | ---------------------- | --- | --- | --- |
| Release |         |     |     | Modification           |     |     |     |
| 10.11   |         |     |     | Addedmonitorparameter. |     |     |     |
73
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Release |     |     |     | Modification |     |     |
| ------- | --- | --- | --- | ------------ | --- | --- |
10.10
Addedhuman-readableparameter.
| 10.07orearlier      |         |         |     | --        |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- |
| Command Information |         |         |     |           |     |     |
| Platforms           | Command | context |     | Authority |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show interface |                  | dom |     |          |     |     |
| -------------- | ---------------- | --- | --- | -------- | --- | --- |
| show interface | [<INTERFACE-ID>] |     | dom | [detail] |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+,QSFP+).
ThisinformationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port.
| detail |     |     |     | Showdetailedinformation. |     |     |
| ------ | --- | --- | --- | ------------------------ | --- | --- |
Example
| switch# | show interface | dom |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
Port Type Channel Temperature Voltage Tx Bias Rx Power Tx Power
|     |     |     | (Celsius) | (Volts) (mA) | (mW/dBm) | (mW/dBm) |
| --- | --- | --- | --------- | ------------ | -------- | -------- |
----------------------------------------------------------------------------------
| 1/1/1               | SFP+SR   |     | 47.65 | 3.31 8.40    | 0.08, -10.96 | 0.63, -2.49 |
| ------------------- | -------- | --- | ----- | ------------ | ------------ | ----------- |
| 1/1/2               | SFP+SR   |     | n/a   | n/a n/a      | n/a          | n/a         |
| 1/1/3               | SFP+DA3  |     | 42.10 | 3.24 n/a     | n/a          | n/a         |
| 1/1/4               | QSFP+SR4 | 1   | 44.46 | 3.30 6.12    | 0.08, -10.96 | 0.63, -1.95 |
|                     |          | 2   | 44.46 | 3.30 6.04    | 0.08, -10.96 | 0.63, -2.00 |
|                     |          | 3   | 44.46 | 3.30 6.51    | 0.08, -10.96 | 0.60, -2.16 |
|                     |          | 4   | 44.46 | 3.30 6.19    | 0.08, -10.96 | 0.63, -1.94 |
| Command History     |          |     |       |              |              |             |
| Release             |          |     |       | Modification |              |             |
| 10.07orearlier      |          |     |       | --           |              |             |
| Command Information |          |     |       |              |              |             |
Interfaceconfiguration|74

| Platforms |     | Command |     | context | Authority |     |     |     |
| --------- | --- | ------- | --- | ------- | --------- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | interface |                      | energy-efficient |     |                           | ethernet |     |     |
| ---- | --------- | -------------------- | ---------------- | --- | ------------------------- | -------- | --- | --- |
| show | interface | [<IFNAME>|<IFRANGE>] |                  |     | energy-efficient-ethernet |          |     |     |
Description
DisplaysEnergy-EfficientEthernetinformationfortheinterface.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<IFNAME> Specifiesthenameofaninterfaceontheswitch.Usetheformat
member/slot/port(forexample,1/1/1).
<IFRANGE> Specifiestheportidentifierrangeofaninterfaceontheswitch.
Usetheformatmember/slot/port(forexample,1/1/1).
Example
ThefollowingexampleshowswhentheinterfacesareEnergy-EfficientEthernetcapable
|     | switch# | show | interface | energy-efficient-ethernet |     |     |     |     |
| --- | ------- | ---- | --------- | ------------------------- | --- | --- | --- | --- |
-------------------------------------------------------------------
|     | Port | Enabled |     | Negotiated | Speed  |     | TX Wake  | RX Wake   |
| --- | ---- | ------- | --- | ---------- | ------ | --- | -------- | --------- |
|     |      |         |     |            | (MB/s) |     | Time(us) | Time (us) |
-------------------------------------------------------------------
|     | 1/1/1 | no  |     | no  | --   |     | --  | --  |
| --- | ----- | --- | --- | --- | ---- | --- | --- | --- |
|     | 1/1/2 | yes |     | yes | 100  |     | 36  | 36  |
|     | 1/1/3 | yes |     | yes | 1000 |     | 17  | 17  |
|     | 1/1/4 | no  |     | no  | --   |     | --  | --  |
|     | 1/1/5 | yes |     | no  | 1000 |     | --  | --  |
ThefollowingexampleshowswhentheinterfaceisnotEnergy-EfficientEthernetcapable:
|                | switch#     | show  | interface | 1/1/1       | energy-efficient-ethernet |     |     |     |
| -------------- | ----------- | ----- | --------- | ----------- | ------------------------- | --- | --- | --- |
|                | Port        | 1/1/1 | does      | not support | Energy-Efficient-Ethernet |     |     |     |
| Command        | History     |       |           |             |                           |     |     |     |
| Release        |             |       |           |             | Modification              |     |     |     |
| 10.07orearlier |             |       |           |             | --                        |     |     |     |
| Command        | Information |       |           |             |                           |     |     |     |
75
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface | flow-control          |     |              |          |
| -------------- | --------------------- | --- | ------------ | -------- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | flow-control | [detail] |
Description
Showstheflowcontrolconfiguration,status,andstatisticsofthespecifiedinterfaceforinterfaceson
whichflowcontrolisenabled.
Ifdetailisnotspecified,thiscommandshowsasummaryofallflowcontrolledinterfaceswithoneinterfaceper
line.Ifdetailisspecified,thiscommandshowsflowcontroldetailedstatistics.
AsofAOS-CX10.10,theseparateshow flow-controlcommandhasbeenremoved,withitbeingeffectively
replacedbythiscommand.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IFNNAME>|<IFRANGE> Specifiestheinterface(port)nameorrange.Whennointerface
rangeisspecified,onlyinterfaceswithflowcontrolenabledinthe
configurationorstatusareshown.
| detail |     |     | Showsdetailedinformation. |     |
| ------ | --- | --- | ------------------------- | --- |
Examples
Showingsummaryflowcontrolinformation:
| switch#     | show interface                        | flow-control |     |     |
| ----------- | ------------------------------------- | ------------ | --- | --- |
| ----------- | ------------------------------------- |              |     |     |
| Port        | Flow                                  |              |     |     |
Control
| ----------- | ------------------------------------- |         |     |     |
| ----------- | ------------------------------------- | ------- | --- | --- |
| 1/1/1       | config:                               | llfc rx |     |     |
|             | status:                               | llfc rx |     |     |
| 1/1/2       | config:                               | llfc rx |     |     |
|             | status:                               | none    |     |     |
ShowingsummaryflowcontrolinformationwithPFC:
| switch#     | show interface                        | flow-control |     |     |
| ----------- | ------------------------------------- | ------------ | --- | --- |
| ----------- | ------------------------------------- |              |     |     |
| Port        | Flow                                  |              |     |     |
Control
| ----------- | ------------------------------------- |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- |
Interfaceconfiguration|76

| 1/1/1 | config: | pfc rxtx-1,2 |     |     |     |
| ----- | ------- | ------------ | --- | --- | --- |
|       | status: | pfc rxtx-1,2 |     |     |     |
| 1/1/2 | config: | pfc rxtx-5   |     |     |     |
|       | status: | none         |     |     |     |
ShowingsummaryflowcontrolinformationwithPFC:
| switch# show | interface | flow-control     |     |     |     |
| ------------ | --------- | ---------------- | --- | --- | --- |
| Flow Control | Watchdog  | Settings         |     |     |     |
| Trigger      | Timeout:  | 100 milliseconds |     |     |     |
| Resume       | Time:     | 100 milliseconds |     |     |     |
----------- ------------------------------------- ------------- --------
| Port | Flow    |     |     | Watchdog | Watchdog |
| ---- | ------- | --- | --- | -------- | -------- |
|      | Control |     |     | Status   | Timeouts |
----------- ------------------------------------- ------------- --------
| 1/1/1    | config: | llfc rx      |     |              |      |
| -------- | ------- | ------------ | --- | ------------ | ---- |
|          | status: | llfc rx      |     |              |      |
| 1/1/2    | config: | llfc rx      |     | incompatible | 0    |
|          | status: | llfc rx      |     |              |      |
| 1/1/10   | config: | pfc rxtx-1,2 |     | enabled      | 1234 |
|          | status: | pfc rxtx-1,2 |     |              |      |
| 1/1/12   | config: | pfc rxtx-1,2 |     | error        | 0    |
|          | status: | pfc rxtx-1,2 |     |              |      |
| 1/1/32:4 | config: | pfc rxtx-5   |     |              |      |
|          | status: | pfc rxtx-5   |     |              |      |
Showingsummaryflowcontrolinformationwheretheconfigurationdoesnotmatchstatusduetoa
rebootrequiredtoapplyPFCconfigurationinhardware:
| switch# show | interface | flow-control     |              |          |     |
| ------------ | --------- | ---------------- | ------------ | -------- | --- |
| Flow Control | Watchdog  | Settings         |              |          |     |
| Trigger      | Timeout:  | 100 milliseconds | (actual: not | applied) |     |
| Resume       | Time:     | 100 milliseconds | (actual: not | applied) |     |
----------- ------------------------------------- ------------- --------
| Port | Flow    |     |     | Watchdog | Watchdog |
| ---- | ------- | --- | --- | -------- | -------- |
|      | Control |     |     | Status   | Timeouts |
----------- ------------------------------------- ------------- --------
| 1/1/1    | config: | llfc rx      |     |              |      |
| -------- | ------- | ------------ | --- | ------------ | ---- |
|          | status: | llfc rx      |     |              |      |
| 1/1/2    | config: | llfc rx      |     | incompatible | 0    |
|          | status: | llfc rx      |     |              |      |
| 1/1/10   | config: | pfc rxtx-1,2 |     | pending      | 1234 |
|          | status: | none         |     |              |      |
| 1/1/12   | config: | pfc rxtx-1,2 |     | pending      | 0    |
|          | status: | none         |     |              |      |
| 1/1/32:4 | config: | pfc rxtx-5   |     |              |      |
|          | status: | none         |     |              |      |
ShowingdetailedflowcontrolinformationwithRXflowcontrolenabled:
77
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | llfc   | rx                   |     |     |
| -------------------- | ------ | -------------------- | --- | --- |
| Statistics           |        |                      | RX  |     |
| -------------------- |        | -------------------- |     |     |
| Dot3 Pause           | Frames |                      | 0   |     |
ShowingdetailedflowcontrolinformationwithRXflowcontrolenabled:
| switch# show | interface | 1/1/1 flow-control | detail |     |
| ------------ | --------- | ------------------ | ------ | --- |
| Interface    | 1/1/1 is  | up                 |        |     |
| Admin state  | is up     |                    |        |     |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:        | llfc      | rx                   |     |     |
| -------------------- | --------- | -------------------- | --- | --- |
| Flow-control         | watchdog: | disabled             |     |     |
| Statistics           |           |                      | RX  |     |
| -------------------- |           | -------------------- |     |     |
| Dot3 Pause           | Frames    |                      | 0   |     |
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
Interfaceconfiguration|78

| Priority    | 7 Pauses |     | 0   | 0   |
| ----------- | -------- | --- | --- | --- |
| Total Pause | Frames   |     | 0   | 0   |
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
| Total                | Pause Frames      |                      | 0                    | 0   |
| Queue                | Watchdog          | Timeouts             |                      |     |
| ------------         | ----------------- |                      |                      |     |
| Queue                | 0                 | 0                    |                      |     |
| Queue                | 1                 | 0                    |                      |     |
| Queue                | 2                 | 0                    |                      |     |
| Queue                | 3                 | 0                    |                      |     |
| Queue                | 4                 | 0                    |                      |     |
| Queue                | 5                 | 0                    |                      |     |
| Queue                | 6                 | 0                    |                      |     |
| Queue                | 7                 | 0                    |                      |     |
79
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butitcouldnotbeappliedbecausetheconfiguredflowcontrolmodeisnotcompatiblewithwatchdog:
| switch#     | show interface | 1/1/1 flow-control | detail |
| ----------- | -------------- | ------------------ | ------ |
| Interface   | 1/1/1 is       | up                 |        |
| Admin state | is up          |                    |        |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control: | llfc      | rx           |     |
| ------------- | --------- | ------------ | --- |
| Flow-control  | watchdog: | incompatible |     |
Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butcouldnotbeappliedbecauseacompatibleflowcontrolmodefirstrequiresareboot:
| switch#     | show interface | 1/1/1 flow-control | detail |
| ----------- | -------------- | ------------------ | ------ |
| Interface   | 1/1/1 is       | up                 |        |
| Admin state | is up          |                    |        |
Link state: up for 3 minutes (since Thu Apr 07 16:38:02 UTC 2022)
| Flow-control:       | off       |         |                                                 |
| ------------------- | --------- | ------- | ----------------------------------------------- |
| Flow-control        | watchdog: | pending |                                                 |
| Command History     |           |         |                                                 |
| Release             |           |         | Modification                                    |
| 10.10               |           |         | Examplesupdatedwithnewandchangedoutputelements. |
| 10.08               |           |         | Commandintroduced.                              |
| Command Information |           |         |                                                 |
| Platforms           | Command   | context | Authority                                       |
Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
Allplatforms
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
Interfaceconfiguration|80

Parameter

<IFNAME>

<IFRANGE>

LAG

<LAG-ID>

VXLAN

<VXLAN-ID>

monitor

human-readable

non-zero

Examples

Showing statistics of all interfaces:

Description

Specifies a interface name.

Specifies the port identifier range.

Shows LAG interface information.

Specifies the LAG number. Range: 1-256

Shows the VXLAN interface information.

Specifies the VXLAN interface identifier. Default: 1

Continuously monitor interface statistics.

Shows statistics rounded to the nearest power of 1000, for
example, 1K, 345M, 2G.

Shows only non zero statistics.

Showing statistics of all interfaces with only non-zero statistics:

Showing statistics of all interfaces in the human-readable format:

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

81

Showing monitor statistics:

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

Showing monitor error statistics in human-readable format:

Interface configuration | 82

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
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show interface | transceiver |     |     |
| -------------- | ----------- | --- | --- |
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations]
Description
Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfor
differenttransceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPE
andthird-partytransceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskinthe
output.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
| detail               |     |     | Showdetailedinformationfortheinterfaces. |
| -------------------- | --- | --- | ---------------------------------------- |
| threshold-violations |     |     | Showthresholdviolationsfortransceivers.  |
Example
Showingsummarytransceiverinformationwithidentificationofunsupportedtransceivers:
83
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| switch(config)# |     | show | interface | transceiver |     |     |     |
| --------------- | --- | ---- | --------- | ----------- | --- | --- | --- |
-------------------------------------------------------------------
| Port | Type |     | Product |     | Serial |     | Part   |
| ---- | ---- | --- | ------- | --- | ------ | --- | ------ |
|      |      |     | Number  |     | Number |     | Number |
-------------------------------------------------------------------
| 1/1/1         | SFP+SR    |             | J9150A     |     | MYxxxxxxxx |     | 1990-3657 |
| ------------- | --------- | ----------- | ---------- | --- | ---------- | --- | --------- |
| 1/1/2         | SFP+ER*   |             | --         |     | --         |     | --        |
| 1/2/1         | QSFP+SR4  |             | JH233A     |     | MYxxxxxxxx |     | 2005-1234 |
| 1/2/2         | QSFP+ER4* |             | --         |     | --         |     | --        |
| 1/3/1         | SFP28DAC3 |             | 844477-B21 |     | MYxxxxxxxx |     | 77fc-7ce7 |
| * unsupported |           | transceiver |            |     |            |     |           |
Showingdetailedtransceiverinformation:
| switch(config)# |     | show     | interface | transceiver |     | detail |     |
| --------------- | --- | -------- | --------- | ----------- | --- | ------ | --- |
| Transceiver     |     | in 1/1/1 |           |             |     |        |     |
| Interface       |     | Name     | : 1/1/1   |             |     |        |     |
| Type            |     |          | : SFP+SR  |             |     |        |     |
| Connector       |     | Type     | : LC      |             |     |        |     |
| Wavelength      |     |          | : 850nm   |             |     |        |     |
Transfer Distance : 0m (SMF), 30m (OM1), 80m (OM2), 300m (OM3)
| Diagnostic |        | Support | : DOM       |     |     |     |     |
| ---------- | ------ | ------- | ----------- | --- | --- | --- | --- |
| Product    | Number |         | : J9150A    |     |     |     |     |
| Serial     | Number |         | : MYxxxxxxx |     |     |     |     |
| Part       | Number |         | : 1990-3657 |     |     |     |     |
Status
| Temperature |        | : 47.65C    |             |     |        |           |            |
| ----------- | ------ | ----------- | ----------- | --- | ------ | --------- | ---------- |
| Voltage     |        | : 3.31V     |             |     |        |           |            |
| Tx Bias     |        | : 8.40mA    |             |     |        |           |            |
| Rx Power    |        | : 0.08mW,   | -10.96dBm   |     |        |           |            |
| Tx Power    |        | : 0.56mW,   | -2.49dBm    |     |        |           |            |
| Recent      | Alarms | :           |             |     |        |           |            |
| Rx          | power  | low alarm   |             |     |        |           |            |
| Rx          | power  | low warning |             |     |        |           |            |
| Recent      | Errors | :           |             |     |        |           |            |
| Rx          | loss   | of signal   |             |     |        |           |            |
| Transceiver |        | in 1/1/2    |             |     |        |           |            |
| Interface   |        | Name        | : 1/1/2     |     |        |           |            |
| Type        |        |             | : unknown   |     |        |           |            |
| Connector   |        | Type        | : ??        |     |        |           |            |
| Wavelength  |        |             | : ??        |     |        |           |            |
| Transfer    |        | Distance    | : ??        |     |        |           |            |
| Diagnostic  |        | Support     | : ??        |     |        |           |            |
| Product     | Number |             | : ??        |     |        |           |            |
| Serial      | Number |             | : ??        |     |        |           |            |
| Part        | Number |             | : ??        |     |        |           |            |
| Transceiver |        | in 1/2/1    |             |     |        |           |            |
| Interface   |        | Name        | : 1/2/1     |     |        |           |            |
| Type        |        |             | : QSFP+SR4  |     |        |           |            |
| Connector   |        | Type        | : MPO       |     |        |           |            |
| Wavelength  |        |             | : 850nm     |     |        |           |            |
| Transfer    |        | Distance    | : 0m (SMF), | 0m  | (OM1), | 0m (OM2), | 100m (OM3) |
| Diagnostic  |        | Support     | : DOM       |     |        |           |            |
| Product     | Number |             | : JH233A    |     |        |           |            |
| Serial      | Number |             | : MYxxxxxxx |     |        |           |            |
Interfaceconfiguration|84

| Part Number |     | : 2005-1234 |     |
| ----------- | --- | ----------- | --- |
Status
| Temperature | : 44.46C |     |     |
| ----------- | -------- | --- | --- |
| Voltage     | : 3.30V  |     |     |
----------------------------------------------
|          | Tx Bias | Rx Power | Tx Power |
| -------- | ------- | -------- | -------- |
| Channel# | (mA)    | (mW/dBm) | (mW/dBm) |
----------------------------------------------
| 1           | 6.12              | 0.00, -inf  | 0.63, -1.95 |
| ----------- | ----------------- | ----------- | ----------- |
| 2           | 6.04              | 0.00, -inf  | 0.63, -2.00 |
| 3           | 6.51              | 0.00, -inf  | 0.60, -2.16 |
| 4           | 6.19              | 0.00, -inf  | 0.63, -1.94 |
| Recent      | Alarms :          |             |             |
| Channel     | 1 :               |             |             |
| Rx          | power low alarm   |             |             |
| Rx          | power low warning |             |             |
| Channel     | 2 :               |             |             |
| Rx          | power low alarm   |             |             |
| Rx          | power low warning |             |             |
| Channel     | 3 :               |             |             |
| Rx          | power low alarm   |             |             |
| Rx          | power low warning |             |             |
| Channel     | 4 :               |             |             |
| Rx          | power low alarm   |             |             |
| Rx          | power low warning |             |             |
| Recent      | Errors :          |             |             |
| Channel     | 1 :               |             |             |
| Rx          | Loss of Signal    |             |             |
| Channel     | 2 :               |             |             |
| Rx          | Loss of Signal    |             |             |
| Channel     | 3 :               |             |             |
| Rx          | Loss of Signal    |             |             |
| Channel     | 4 :               |             |             |
| Rx          | Loss of Signal    |             |             |
| Transceiver | in 1/2/2          |             |             |
| Interface   | Name              | : 1/2/2     |             |
| Type        |                   | : unknown   |             |
| Connector   | Type              | : ??        |             |
| Wavelength  |                   | : ??        |             |
| Transfer    | Distance          | : ??        |             |
| Diagnostic  | Support           | : ??        |             |
| Product     | Number            | : ??        |             |
| Serial      | Number            | : ??        |             |
| Part Number |                   | : ??        |             |
| Transceiver | in 1/3/1          |             |             |
| Interface   | Name              | : 1/3/1     |             |
| Type        |                   | : SFP28DAC3 |             |
| Connector   | Type              | : Copper    | Pigtail     |
Transfer Distance : 0.00km (SMF), 0m (OM1), 0m (OM2), 0m (OM3)
| Diagnostic  | Support | : None       |     |
| ----------- | ------- | ------------ | --- |
| Product     | Number  | : 844477-B21 |     |
| Serial      | Number  | : MYxxxxxxx  |     |
| Part Number |         | : 77fc-7ce7  |     |
Showingdetailedtransceiverinformationwithidentificationofunsupportedtransceivers:
85
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
| 1/1/1          | SFP+SR      |     | Tx bias      | high      | warning     |     |
| -------------- | ----------- | --- | ------------ | --------- | ----------- | --- |
|                |             |     | 50.52        | mA >      | 40.00 mA    |     |
| 1/1/2          | SFP+ER*     |     | ??           |           |             |     |
| 1/2/1          | QSFP+SR4    | 1   | Tx power     | low       | alarm       |     |
|                |             |     | -17.00       | dBm       | < -0.50 dBm |     |
|                |             | 2   | Tx bias      | low       | warning     |     |
|                |             |     | 3.12         | mA < 4.00 | mA          |     |
| 1/2/2          | QSFP+ER4*   |     | ??           |           |             |     |
| 1/3/1          | SFP28DAC3   |     | n/a          |           |             |     |
| * unsupported  | transceiver |     |              |           |             |     |
| Command        | History     |     |              |           |             |     |
| Release        |             |     | Modification |           |             |     |
| 10.07orearlier |             |     | --           |           |             |     |
| Command        | Information |     |              |           |             |     |
Interfaceconfiguration|86

| Platforms | Command |     | context |     | Authority |     |     |     |     |     |
| --------- | ------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                       | utilization |     |     |             |            |     |     |     |     |
| -------------- | --------------------- | ----------- | --- | --- | ----------- | ---------- | --- | --- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |             |     |     | utilization | [non-zero] |     |     |     |     |
Description
Displaysphysicalportthroughputandutilization.
| Parameter |     |     |     |     | Description               |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
| <IFNAME>  |     |     |     |     | Specifiesaninterfacename. |     |     |     |     |     |
<IFRANGE>
Specifiestheportidentifierrange.
| utilization |     |     |     |     | Displaysutilizationstatistics. |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
non-zero
Displaysnon-zerostatistics
Examples
Thefollowingexampleshowsportutilizationofallinterfaces:
| switch# | show | interface | utilization |     |     |     |     |     |     |     |
| ------- | ---- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|------
---------------------|----------------------
|               |     | Interval | |   |     | RX  |     | |   | TX  |     | |   |
| ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total (RX+TX) |     |          | |   |     |     |     |     |     |     |     |
Interface seconds | Mbps KPkt/s Util % | Mbps KPkt/s Util % |
| Mbps | KPkt/s | Util | % | Description |     |     |     |     |     |     |     |
| ---- | ------ | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|------
---------------------|----------------------
| 1/1/1          |             |     | 300 9578.02 |                       | 788.70         | 95.78 | 25.70          | 45.89 | 0.26  |     |
| -------------- | ----------- | --- | ----------- | --------------------- | -------------- | ----- | -------------- | ----- | ----- | --- |
| 9603.72        | 834.59      |     | 96.04       | Aruba-AP              |                |       |                |       |       |     |
| 1/1/2          |             |     | 300         | 25.71                 | 45.90          | 0.26  | 9581.09 788.96 |       | 95.81 |     |
| 9606.80        | 834.86      |     | 96.07       | Aruba2530-AP-conce... |                |       |                |       |       |     |
| 1/1/3          | - lag123    |     | 300         | 0.00                  | 0.00           | 0.00  | 0.00           | 0.00  | 0.00  |     |
| 0.00           | 0.00        |     | 0.00 ISL:   | SWRTS-0064-1          |                |       |                |       |       |     |
| 1/1/4          |             |     | 300 9261.79 |                       | 804.52         | 92.62 | 9496.70 823.97 |       | 94.97 |     |
| 18758.50       | 1628.48     |     | 187.58      | Backup                | data center... |       |                |       |       |     |
| 1/1/5          |             |     | 300 9496.70 |                       | 823.97         | 94.97 | 9261.79 804.52 |       | 92.62 |     |
| 18758.50       | 1628.48     |     | 187.58      | --                    |                |       |                |       |       |     |
| Command        | History     |     |             |                       |                |       |                |       |       |     |
| Release        |             |     |             |                       | Modification   |       |                |       |       |     |
| 10.07orearlier |             |     |             |                       | --             |       |                |       |       |     |
| Command        | Information |     |             |                       |                |       |                |       |       |     |
87
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show ip           | interface      |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
| show ip interface | <INTERFACE-ID> |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
Example
switch#
|              | show ip interface |     | 1/1/1    |                   |
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
| Hardware:     | Ethernet,    | MAC | Address:    | b8:6a:97:22:2f:42 |
| ------------- | ------------ | --- | ----------- | ----------------- |
| Encapsulation | dot1q        | ID: | 30          |                   |
| L3 Counters:  | Rx Disabled, |     | Tx Disabled |                   |
| Command       | History      |     |             |                   |
Interfaceconfiguration|88

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
Description
ShowssinglesourceIPaddressconfigurationsettings.
Parameter Description
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME> SpecifiesthenameofaVRF.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
| switch#          | show ip | source-interface | sflow       |
| ---------------- | ------- | ---------------- | ----------- |
| Source-interface |         | Configuration    | Information |
----------------------------------------
| Protocol |     | Source Interface |     |
| -------- | --- | ---------------- | --- |
| -------- |     | ---------------- |     |
| sflow    |     | 10.10.10.1       |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show ip | source-interface | all         |
| ---------------- | ------- | ---------------- | ----------- |
| Source-interface |         | Configuration    | Information |
----------------------------------------
| Protocol        |     | Source Interface |     |
| --------------- | --- | ---------------- | --- |
| --------        |     | ---------------- |     |
| all             |     | 1/1/1            |     |
| Command History |     |                  |     |
89
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |
| ----------------------------- | --- | ------------------ | --- |

| Release        |     |             |     |         |     | Modification |     |     |
| -------------- | --- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |     |             |     |         |     | --           |     |     |
| Command        |     | Information |     |         |     |              |     |     |
| Platforms      |     | Command     |     | context |     | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ipv6 | interface |                |     |     |     |     |     |
| ---- | ---- | --------- | -------------- | --- | --- | --- | --- | --- |
| show | ipv6 | interface | <INTERFACE-ID> |     |     |     |     |     |
Description
ShowsstatusandconfigurationinformationforanIPv6interface.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
SpecifiesaninterfaceID.Format:member/slot/port.
Examples
| switch#   |                                            | show  | ipv6  | interface | 1/1/1 |     |         |     |
| --------- | ------------------------------------------ | ----- | ----- | --------- | ----- | --- | ------- | --- |
| Interface |                                            | 1/1/1 | is    | up        |       |     |         |     |
|           | Admin                                      | state | is up |           |       |     |         |     |
|           | IPv6 address:                              |       |       |           |       |     |         |     |
|           | 2001:0db8:85a3:0000:0000:8a2e:0370:7334/24 |       |       |           |       |     | [VALID] |     |
IPv6 link-local address: fe80::1e98:ecff:fee3:e800/64 (default)[VALID]
|     | IPv6 virtual    |     | address  | configured:     |         | none    |                        |     |
| --- | --------------- | --- | -------- | --------------- | ------- | ------- | ---------------------- | --- |
|     | IPv6 multicast  |     | routing: |                 | disable |         |                        |     |
|     | IPv6 Forwarding |     | feature: |                 | enabled |         |                        |     |
|     | IPv6 multicast  |     | groups   | locally         |         | joined: |                        |     |
|     | ff02::ff70:7334 |     |          | ff02::ffe3:e800 |         |         | ff02::1 ff02::1:ff00:0 |     |
ff02::2
|     | IPv6 multicast |          | (S,G)   | entries |             | joined: | none |     |
| --- | -------------- | -------- | ------- | ------- | ----------- | ------- | ---- | --- |
|     | IPv6 MTU:      | 1524     | (using  | link    | MTU)        |         |      |     |
|     | IPv6 unicast   |          | reverse | path    | forwarding: |         | none |     |
|     | IPv6 load      | sharing: |         | none    |             |         |      |     |
RX
|     |     | 0 packets, |     | 0 bytes |     |     |     |     |
| --- | --- | ---------- | --- | ------- | --- | --- | --- | --- |
TX
|           |            | 0 packets, |          | 0 bytes     |                             |      |     |         |
| --------- | ---------- | ---------- | -------- | ----------- | --------------------------- | ---- | --- | ------- |
| switch#   |            | show       | ipv6     | interface   | <intfid>.id                 |      |     |         |
| Interface |            | 1/1/14.1   |          | is up       |                             |      |     |         |
| Admin     | state      | is         | up       |             |                             |      |     |         |
| IPv6      | address:   |            |          |             |                             |      |     |         |
| 30::1/64  |            | [VALID]    |          |             |                             |      |     |         |
| IPv6      | link-local |            | address: |             | fe80::b86a:97c0:122:2f42/64 |      |     | [VALID] |
| IPv6      | virtual    |            | address  | configured: |                             | none |     |         |
| IPv6      | multicast  |            | routing: |             | disable                     |      |     |         |
| IPv6      | Forwarding |            | feature: |             | enabled                     |      |     |         |
Interfaceconfiguration|90

| IPv6 multicast |                   | groups | locally |                | joined: |     |                |     |
| -------------- | ----------------- | ------ | ------- | -------------- | ------- | --- | -------------- | --- |
| ff02::1        | ff02::1:ff22:2f42 |        |         | ff02::1:ff00:1 |         |     | ff02::1:ff00:0 |     |
ff02::2
| IPv6 multicast |          | (S,G)   | entries   | joined:     |     | none |     |     |
| -------------- | -------- | ------- | --------- | ----------- | --- | ---- | --- | --- |
| IPv6 MTU       | 1500     |         |           |             |     |      |     |     |
| IPv6 unicast   |          | reverse | path      | forwarding: |     | none |     |     |
| IPv6 load      | sharing: |         | none      |             |     |      |     |     |
| Encapsulation  |          | dot1q   | ID:       | 20          |     |      |     |     |
| switch#        | show     | ipv6    | interface | lag2.1      |     |      |     |     |
| Interface      | lag2.1   |         | is up     |             |     |      |     |     |
| Admin state    |          | is up   |           |             |     |      |     |     |
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
Description
ShowssinglesourceIPaddressconfigurationsettings.
91
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

Parameter Description
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME> SpecifiesthenameofaVRF.
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
Interfaceconfiguration|92

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
speed
| speed {<SPEED> | | <SPEED-DUPLEX> | | auto | [<SPEED>] | }   |
| -------------- | ---------------- | ------ | --------- | --- |
no speed
Description
Configuresthelinkspeed,duplex,andauto-negotiationsettingsforaninterface.
Thenoformofthiscommandremovestheconfigurationsandreturnstothedefaults.
| Parameter |     |     | Description                                          |     |
| --------- | --- | --- | ---------------------------------------------------- | --- |
| Speed     |     |     | Configuresinterfacespeed,duplex,andauto-negotiation. |     |
10-full
10Mbps,fullduplex,noauto-negotiation
| 10-half |     |     | 10Mbps,halfduplex,noauto-negotiation |     |
| ------- | --- | --- | ------------------------------------ | --- |
100-full
100Mbps,fullduplex,noauto-negotiation
| 100-half |     |     | 100Mbps,halfduplex,noauto-negotiation |     |
| -------- | --- | --- | ------------------------------------- | --- |
1000-full
1000Mbps,fullduplex,noauto-negotiation
| 10g |     |     | 10Gbps,fullduplex,noauto-negotiation |     |
| --- | --- | --- | ------------------------------------ | --- |
25g
25Gbps,fullduplex,noauto-negotiation
| 40g |     |     | 40Gbps,fullduplex,noauto-negotiation |     |
| --- | --- | --- | ------------------------------------ | --- |
93
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

Parameter

Description

50g

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

Usage

50 Gbps, full duplex, no auto-negotiation

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

The following options can be configured for an interface. The option available is based on the interface
type.
speed <SPEED-DUPLEX>

Uses a fixed speed and duplex mode with no auto-negotiation. Half-duplex is only supported for 10
Mbps and 100 Mbps link speeds.

speed <SPEED>

Uses a fixed speed with no auto-negotiation. If the currently installed transceiver does not support
the speed, the setting is ignored and the port will use the highest speed that is supported.

speed auto

Uses auto-negotiation and offers all speeds supported by the port and transceiver. This is the
default. If the link technology does not support auto-negotiation this setting is ignored, and the port
uses the highest possible fixed speed.

speed auto <SPEED>

Interface configuration | 94

Usesauto-negotiationandoffersthespecifiedspeedsonly.Forportsthatsupportpluggable
transceivers,onlyspeedssupportedbythetransceiverareofferedandotherspeedsareignored.If
thelinktechnologydoesnotsupportauto-negotiation,thissettingisignoredandtheportusesthe
highestpossiblefixedspeed.
Examples
Configuringaninterfacetooperateatafixedspeedof1000Mbpswithfullduplexandnoauto-
negotiation:
| switch(config)#    |     | interface | 1/1/1     |     |
| ------------------ | --- | --------- | --------- | --- |
| switch(config-if)# |     | speed     | 1000-full |     |
Configuringaninterfacetooperateatafixedspeedof10Gbpswithnoauto-negotiation:
| switch(config)#    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | speed     | 10g   |     |
Configuringaninterfacetoauto-negotiateandadvertiseonly1Gbpsand2.5Gbpsspeeds:
| switch(config)#    |     | interface | 1/1/1   |      |
| ------------------ | --- | --------- | ------- | ---- |
| switch(config-if)# |     | speed     | auto 1g | 2.5g |
Configuringaninterfacetooverridethedetectedtransceiverspeedandusetheconfiguredspeedifthe
installedtransceiverdoesnotsupportauto-negotiation:
| switch(config)#    |     | interface | 1/1/1    |          |
| ------------------ | --- | --------- | -------- | -------- |
| switch(config-if)# |     | speed     | auto 50g | override |
Configuringaninterfacetousedefaultsettingsforspeed,duplex,andauto-negotiation:
| switch(config)#     |         | interface | 1/1/1 |                                          |
| ------------------- | ------- | --------- | ----- | ---------------------------------------- |
| switch(config-if)#  |         | no speed  |       |                                          |
| Command History     |         |           |       |                                          |
| Release             |         |           |       | Modification                             |
| 10.09.0001          |         |           |       | SpeedsnotsupportedbyhardwarehiddenbyCLI. |
| 10.07orearlier      |         |           |       | --                                       |
| Command Information |         |           |       |                                          |
| Platforms           | Command | context   |       | Authority                                |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
95
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | ------------------ | --- | --- |

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
96
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- | --- |

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
Sourceinterfaceselection|97

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
98
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

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
Sourceinterfaceselection|99

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
100
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

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

Source interface selection | 101

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
102
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
106
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

107

Chapter 8
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
108
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

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
Configurationandfirmwaremanagement |109

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

110

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
Configurationandfirmwaremanagement |111

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
112
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
Configurationandfirmwaremanagement |113

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
114
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
Configurationandfirmwaremanagement |115

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
116
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |
| ----------------------------- | --- | ------------------ | --- |

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
Configurationandfirmwaremanagement |117

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
118
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- | --- |

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
Configurationandfirmwaremanagement |119

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
120
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
Configurationandfirmwaremanagement |121

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
122
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

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
Configurationandfirmwaremanagement |123

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
124
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
Configurationandfirmwaremanagement |125

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
126
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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

Configuration and firmware management | 127

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
| Parameter  |                   |     | Description |
| ---------- | ----------------- | --- | ----------- |
| checkpoint | <CHECKPOINT-NAME> |     |             |
Specifiesthenameofacheckpoint.
| core-dump  |               |     | Eraseoneofthefollowingsetsofcore-dumpfiles: |
| ---------- | ------------- | --- | ------------------------------------------- |
| all|daemon | <daemon-name> |     |                                             |
n all:Eraseallcore-dumpfiles.
|kernel
n daemon<daemon-name>:Erasedaemoncore-dumpfiles.
n kerne:lErasethekernelcore-dump.
vsfErasedaemoncore-dumpfilesforVSF.
n
| startup-config |     |     | Specifiesthestartupconfiguration. |
| -------------- | --- | --- | --------------------------------- |
all
Specifiesallcheckpoints.
Examples
Erasingcheckpointckpt1:
switch#
|     | erase checkpoint | ckpt1 |     |
| --- | ---------------- | ----- | --- |
Erasingthestartupconfiguration:
| switch# | erase startup-config |     |     |
| ------- | -------------------- | --- | --- |
Erasingallcheckpoints:
| switch#         | erase checkpoint | all |     |
| --------------- | ---------------- | --- | --- |
| Command History |                  |     |     |
128
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show checkpoint |                   | <CHECKPOINT-NAME> |        |
| --------------- | ----------------- | ----------------- | ------ |
| show checkpoint | <CHECKPOINT-NAME> |                   | [json] |
Description
Showstheconfigurationofacheckpoint.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<CHECKPOINT-NAME>
Specifiesthenameofacheckpoint.
| [json] |     |     | SpecifiesthattheoutputisdisplayedinJSONformat. |
| ------ | --- | --- | ---------------------------------------------- |
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
vlan access 1
| interface | lag 129 |     |     |
| --------- | ------- | --- | --- |
shutdown
vlan access 1
Configurationandfirmwaremanagement |129

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
https-server vrf default

Showing the configuration of the ckpt1 checkpoint in JSON format:

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

130

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
| [cli | json]      |     |     | SelectseithertheCLIorJSONformat.   |     |
Examples
ShowingacheckpointSHA-256hashinJSONformat:
| switch#     | show checkpoint | ckpt1           | hash json |     |
| ----------- | --------------- | --------------- | --------- | --- |
| Calculating | the             | hash: [Success] |           |     |
The SHA-256 hash of the checkpoint in JSON format, created in image XX.10.08.xxxx:
cc7a57a9bbb4e6600d3b4180296a35f6af9e797ce9c439955dfe5de58b06da9e
Configurationandfirmwaremanagement |131

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
| Platforms      | Command     | context   | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show checkpoint
show checkpoint
132
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

Description
Showsadetailedlistofallsavedcheckpoints.
Examples
Showingadetailedlistofallsavedcheckpoints:
| switch#             | show checkpoint |         |                   |                      |            |                        |
| ------------------- | --------------- | ------- | ----------------- | -------------------- | ---------- | ---------------------- |
| NAME                | TYPE            |         | WRITER            | DATE(YYYY/MM/DD)     |            | IMAGE VERSION          |
| ckpt1               | checkpoint      |         | User              | 2017-02-23T00:10:02Z |            | XX.01.01.000X          |
| ckpt2               | checkpoint      |         | User              | 2017-03-08T18:10:01Z |            | XX.01.01.000X          |
| ckpt3               | checkpoint      |         | User              | 2017-03-09T23:11:02Z |            | XX.01.01.000X          |
| ckpt4               | checkpoint      |         | User              | 2017-03-11T00:00:03Z |            | XX.01.01.000X          |
| ckpt5               | latest          |         | User              | 2017-03-14T01:12:27Z |            | XX.01.01.000X          |
| Command History     |                 |         |                   |                      |            |                        |
| Release             |                 |         | Modification      |                      |            |                        |
| 10.08               |                 |         | Commandsyntaxshow |                      | checkpoint | list allisreplacedwith |
|                     |                 |         | show              | checkpoint.          |            |                        |
| 10.07orearlier      |                 |         | --                |                      |            |                        |
| Command Information |                 |         |                   |                      |            |                        |
| Platforms           | Command         | context | Authority         |                      |            |                        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show checkpoint |                   | date |            |     |     |     |
| --------------- | ----------------- | ---- | ---------- | --- | --- | --- |
| show checkpoint | date <START-DATE> |      | <END-DATE> |     |     |     |
Description
Showsdetailedlistofallsavedcheckpointscreatedwithinthespecifieddaterange.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<START-DATE> Specifiesthestartingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
<END-DATE> Specifiestheendingdatefortherangeofsavedcheckpointsto
show.Format:YYYY-MM-DD.
Examples
Showingadetailedlistofsavedcheckpointsforaspecificdaterange:
| switch# | show checkpoint | date | 2017-03-08 | 2017-03-12 |     |     |
| ------- | --------------- | ---- | ---------- | ---------- | --- | --- |
Configurationandfirmwaremanagement |133

| NAME                |         |     | TYPE       |     | WRITER DATE(YYYY/MM/DD)            |            | IMAGE         | VERSION    |         |      |
| ------------------- | ------- | --- | ---------- | --- | ---------------------------------- | ---------- | ------------- | ---------- | ------- | ---- |
| ckpt2               |         |     | checkpoint |     | User 2017-03-08T18:10:01Z          |            | XX.01.01.000X |            |         |      |
| ckpt3               |         |     | checkpoint |     | User 2017-03-09T23:11:02Z          |            | XX.01.01.000X |            |         |      |
| ckpt4               |         |     | checkpoint |     | User 2017-03-11T00:00:03Z          |            | XX.01.01.000X |            |         |      |
| Command History     |         |     |            |     |                                    |            |               |            |         |      |
| Release             |         |     |            |     | Modification                       |            |               |            |         |      |
| 10.08               |         |     |            |     | Commandsyntaxshow                  | checkpoint | list          | date       | <START- |      |
|                     |         |     |            |     | DATE> <END-DATE>isreplacedwithshow |            |               | checkpoint |         | date |
|                     |         |     |            |     | <START-DATE> <END-DATE>            |            |               |            |         |      |
| 10.07orearlier      |         |     |            |     | --                                 |            |               |            |         |      |
| Command Information |         |     |            |     |                                    |            |               |            |         |      |
| Platforms           | Command |     | context    |     | Authority                          |            |               |            |         |      |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show running-config |     |      |      | hash |       |     |     |     |     |     |
| ------------------- | --- | ---- | ---- | ---- | ----- | --- | --- | --- | --- | --- |
| show running-config |     | hash | [cli | |    | json] |     |     |     |     |     |
Description
Showstherunning-configcheckpointhash,calculatedwiththeSHA-256algorithm.Whentheoutput
formatisnotspecified,theCLIformatisused.Thisenablesyoutodeterminewhethertherehasbeena
configurationchangesinceaprevioushashwascalculated.
| Parameter    |     |     |     |     | Description                      |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| [cli | json] |     |     |     |     | SelectseithertheCLIorJSONformat. |     |     |     |     |     |
Examples
Showingtherunning-configcheckpointSHA-256hashinCLIformat:
| switch#     | show | running-config |           | hash | cli         |     |     |     |     |     |
| ----------- | ---- | -------------- | --------- | ---- | ----------- | --- | --- | --- | --- | --- |
| Calculating | the  | hash:          | [Success] |      |             |     |     |     |     |     |
| SHA-256     | hash | of the         | config    | in   | CLI format: |     |     |     |     |     |
8db4e7e10f4b7f1a6ab17ad2b4efe0e72f1849103eaf43da62aa1d715075b89e
This hash is only valid for comparison to a baseline hash if the configuration has
not been explicitly changed (such as with a CLI command, REST operation, etc.)
or implicitly changed (such as by changing a hardware module, upgrading the
| SW version,     | etc.). |     |     |     |     |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Command History |        |     |     |     |     |     |     |     |     |     |
134
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |

| Release             |         |         |     | Modification      |
| ------------------- | ------- | ------- | --- | ----------------- |
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
| SW version,         | etc.).  |         |     |                   |
| ------------------- | ------- | ------- | --- | ----------------- |
| Command History     |         |         |     |                   |
| Release             |         |         |     | Modification      |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Configurationandfirmwaremanagement |135

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
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| primary   |     |     | Selectstheprimarynetworkoperatingsystemimage.   |
| secondary |     |     | Selectsthesecondarynetworkoperatingsystemimage. |
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch#         | boot set-default | primary         |     |
| --------------- | ---------------- | --------------- | --- |
| Default         | boot image       | set to primary. |     |
| Command History |                  |                 |     |
136
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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

Configuration and firmware management | 137

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
| until the | process      | is complete.  |               |                |
| Continue  | (y/n)? n     |               |               |                |
Reboot aborted.
switch#
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
138
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| Index : | 3                                  |     |     |
| ------- | ---------------------------------- | --- | --- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |     |     |
Configurationandfirmwaremanagement |139

| Current | Boot, up for                       | 22       | hrs 12    | mins | 22 secs          |
| ------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Firmware | management |     |     | commands |     |
| -------- | ---------- | --- | --- | -------- | --- |
140
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

| copy {primary | | secondary} |              | <REMOTE-URL>     |     |     |
| ------------- | ------------ | ------------ | ---------------- | --- | --- |
| copy {primary | | secondary} | <REMOTE-URL> | [vrf <VRF-NAME>] |     |     |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Configurationandfirmwaremanagement |141

| copy {primary |     | | secondary} |                     | <FIRMWARE-FILENAME> |
| ------------- | --- | ------------ | ------------------- | ------------------- |
| copy {primary | |   | secondary}   | <FIRMWARE-FILENAME> |                     |
Description
CopiesafirmwareimagetoUSBstorage.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
{primary | secondary} Selectstheprimaryorsecondaryimagefromwhichtocopythe
firmware.Required
<FIRMWARE-FILENAME> SpecifiesthenameofthefirmwarefiletocreateontheUSB
storagedevice.Prefixthefilenamewithusb:/.Forexample:
usb:/firmware_v1.2.3.swi
Forinformationonhowtoformatthepathtoafirmwarefileona
USBdrive,seeUSBURL.
Examples
| switch#        | copy        | primary | usb:/11.10.00.0002.swi |              |
| -------------- | ----------- | ------- | ---------------------- | ------------ |
| Command        | History     |         |                        |              |
| Release        |             |         |                        | Modification |
| 10.07orearlier |             |         |                        | --           |
| Command        | Information |         |                        |              |
| Platforms      | Command     |         | context                | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| copy primary |           | secondary |     |     |
| ------------ | --------- | --------- | --- | --- |
| copy primary | secondary |           |     |     |
Description
Copiesthefirmwareimagefromtheprimarytothesecondarylocation.
Examples
| switch#       | copy    | primary | secondary          |     |
| ------------- | ------- | ------- | ------------------ | --- |
| The secondary |         | image   | will be deleted.   |     |
| Continue      | (y/n)?  | y       |                    |     |
| Verifying     | and     | writing | system firmware... |     |
| Command       | History |         |                    |     |
142
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | ------------------ | --- | --- |

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

copy <REMOTE-URL>
copy <REMOTE-URL> {hot-patch|primary|secondary} [vrf <VRF-NAME>]

Description

Downloads a firmware image from a TFTP or SFTP server.

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

Select a primary or secondary image profile for receiving the
downloaded firmware. Required.

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

n the port number of the server and blocksize in the URL:

tftp://192.0.2.1:12;blocksize=1462/a.txt

To specify a file in a directory of URL: tftp://192.0.2.1/dir/a.txt

SFTP usage

Configuration and firmware management | 143

Tospecify:
n AURLwithanIPv4address:sftp://user@192.0.2.1/a.txt
n AURLwithanIPv6address:sftp://user@[2000::2]/a.txt
n AURLwithahostname:sftp://user@hpe.com/a.txt
n SFTPportnumberofaserverintheURL:sftp://user@192.0.2.1:12/a.txt
n AfileinadirectoryofURL:sftp://user@192.0.2.1/dir/a.txt
n TospecifyafilewithabsolutepathintheURL:sftp://user@192.0.2.1//home/user/a.txt
SCP Usage
Tospecify:
AusernamewithanIP address:scp://user@192.0.2.1:12/a.txt
n
n Ausernamewitharemotehost:scp://user@hpe.com/a.txt
Examples
TFTPdownloadforprimarysoftwareimage:
switch#
|             | copy tftp://192.10.12.0/ss.10.a0.0001.swi |             | primary |     |     |
| ----------- | ----------------------------------------- | ----------- | ------- | --- | --- |
| The primary | image will                                | be deleted. |         |     |     |
| Continue    | (y/n)? y                                  |             |         |     |     |
######################################################################### 100.0%
| Verifying | and writing | system firmware... |     |     |     |
| --------- | ----------- | ------------------ | --- | --- | --- |
SFTPdownload:
switch# copy sftp://swuser@192.10.12.0/ss.10.00.0002.swi primary
| The primary | image will | be deleted. |     |     |     |
| ----------- | ---------- | ----------- | --- | --- | --- |
| Continue    | (y/n)? y   |             |     |     |     |
The authenticity of host '192.10.12.0 (192.10.12.0)' can't be established.
ECDSA key fingerprint is SHA256:L64khLwlyLgXlARKRMiwcAAK8oRaQ8C0oWP+PkGBXHY.
| Are you | sure you want | to continue connecting | (yes/no)? | yes |     |
| ------- | ------------- | ---------------------- | --------- | --- | --- |
Warning: Permanently added '192.10.12.0' (ECDSA) to the list of known hosts.
| swuser@192.10.12.0's |                 | password: |     |     |     |
| -------------------- | --------------- | --------- | --- | --- | --- |
| Connected            | to 192.10.12.0. |           |     |     |     |
Fetching /users/swuser/ss.10.00.0002.swi to ss.10.00.0002.swi.dnld
| /users/swuser/ss.10.00.0002.swi |             |                    | 100% | 179MB 25.6MB/s | 00:07 |
| ------------------------------- | ----------- | ------------------ | ---- | -------------- | ----- |
| Verifying                       | and writing | system firmware... |      |                |       |
| Command                         | History     |                    |      |                |       |
Release Modification
10.07orearlier --
| Command | Information |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- |
144
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Platforms | Command | context | Authority |     |     |     |     |
| --------- | ------- | ------- | --------- | --- | --- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
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
| Are you | sure you want | to continue | connecting |     | (yes/no)? | yes |     |
| ------- | ------------- | ----------- | ---------- | --- | --------- | --- | --- |
Warning: Permanently added '192.22.1.0' (ECDSA) to the list of known hosts.
| stor@192.22.1.0's      |                        | password: |                           |                           |                |     |       |
| ---------------------- | ---------------------- | --------- | ------------------------- | ------------------------- | -------------- | --- | ----- |
| Connected              | to 192.22.1.0.         |           |                           |                           |                |     |       |
| sftp> get              | c8d5b9f-topflite.swi   |           | c8d5b9f-topflite.swi.dnld |                           |                |     |       |
| Fetching               | /home/dr/im-switch.swi |           | to                        | c8d5b9f-topflite.swi.dnld |                |     |       |
| /home/dr/im-switch.swi |                        |           |                           | 100%                      | 226MB 56.6MB/s |     | 00:04 |
| Verifying              | and writing            | system    | firmware...               |                           |                |     |       |
| Command                | History                |           |                           |                           |                |     |       |
| Release                |                        |           | Modification              |                           |                |     |       |
| 10.07orearlier         |                        |           | --                        |                           |                |     |       |
| Command                | Information            |           |                           |                           |                |     |       |
| Platforms              | Command                | context   | Authority                 |                           |                |     |       |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
copy <STORAGE-URL>
| copy <STORAGE-URL> | {primary|secondary} |     |     |     |     |     |     |
| ------------------ | ------------------- | --- | --- | --- | --- | --- | --- |
Description
Configurationandfirmwaremanagement |145

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
| Platforms      | Command                     | context            | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
146
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

Chapter 9

Dynamic Segmentation

Dynamic Segmentation

For information on dynamic segmentation, view the Security Guide.

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

147

Chapter 10

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

148

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
SNMP|149

Chapter 11

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

150

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

n vsf

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

Aruba Central integration | 151

CreatingtheArubaCentralconfigurationcontext:
| switch(config)# | aruba-central |     |     |
| --------------- | ------------- | --- | --- |
switch(config-aruba-central)#
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Command        | History     |     |              |
| -------------- | ----------- | --- | ------------ |
| Release        |             |     | Modification |
| 10.07orearlier |             |     | --           |
| Command        | Information |     |              |
152
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
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
| switch(config)# |                            | configuration-lockout |     | central managed |
| --------------- | -------------------------- | --------------------- | --- | --------------- |
| switch#         | show configuration-lockout |                       |     |                 |
| configuration   | lockout                    |                       |     |                 |
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
| Activate            | Server | URL |     | :devices-v2.arubanetworks.com |
| ------------------- | ------ | --- | --- | ----------------------------- |
| CLI location        |        |     |     | :20.0.2:8083                  |
| CLI VRF             |        |     |     | :default                      |
| switch(config)#     |        | end |     |                               |
| Command History     |        |     |     |                               |
| Release             |        |     |     | Modification                  |
| 10.07orearlier      |        |     |     | --                            |
| Command Information |        |     |     |                               |
ArubaCentralintegration|153

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
disable
disable
Description
DisablesconnectiontoArubaCentralserver.
Whentheconnectionisdisabled,theswitchdoesnotattempttoconnecttotheArubaCentralserveror
fetchcentrallocationfromanyofthethreesources(CLI/ArubaActivate/DHCP).Italsodisconnectsany
activeconnectiontotheArubaCentralserver.
Example
| switch(config-aruba-central)# |     | disable |     |
| ----------------------------- | --- | ------- | --- |
switch(config-aruba-central)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-aruba-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
enable
enable
Description
EnablesconnectiontoArubaCentralserver.Whentheconnectionisenabled,theswitchattemptsto
downloadthelocationoftheArubaCentralserverinoneofthefollowingwaysatstartupandafterthe
connectionislost:
n Usingcommand-lineinterface(CLI).
n ConnectingtoArubaActivateserver.
n UsingDHCPoptionsprovidedduringZTP.
DHCPserversprovidetheoptionsrequestedbythedevicetoconnecttoCentral,CentralOn-premise
managment,ortheTFTPserver.
Examples
154
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| switch(config-aruba-central)# |     | enable |     |
| ----------------------------- | --- | ------ | --- |
switch(config-aruba-central)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-aruba-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
ArubaCentralintegration|155

RemovinglocationoverridevaluesfromtheArubaCentralconfigurationcontext:
| switch(config-aruba-central)# |     |     |     | no  | location-override |     |
| ----------------------------- | --- | --- | --- | --- | ----------------- | --- |
switch(config-aruba-central)#
| Command History     |         |     |         |     |              |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| Release             |         |     |         |     | Modification |     |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
6200 config-aruba-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show aruba-central
show aruba-central
Description
ShowsinformationaboutArubaCentralconnectionandthestatusoftheActivateserverconnection.
Examples
ExampleofaswitchthathastheArubaCentralconnection:
| switch#              | show aruba-central |           |        |          |              |                      |
| -------------------- | ------------------ | --------- | ------ | -------- | ------------ | -------------------- |
| Central              | admin state        |           |        |          |              | :enabled             |
| Central              | location           |           |        |          |              | : N/A                |
| VRF for              | connection         |           |        |          |              | : N/A                |
| Central              | connection         | status    |        |          |              | : N/A                |
| Central              | source             |           |        |          |              | : dhcp               |
| Central              | source connection  |           | status |          |              | : connection_failure |
| Central              | source last        | connected |        | on       |              | : N/A                |
| System time          | synchronized       |           | from   | Activate |              | : True               |
| Activate             | server             | URL       |        |          |              | : 172.17.0.1         |
| CLI location         |                    |           |        |          |              | : N/A                |
| CLI VRF              |                    |           |        |          |              | : N/A                |
| Source IP            |                    |           |        |          |              | : N/A                |
| Source IP Overridden |                    |           |        |          |              | : false              |
| Central              | support            | mode      |        |          |              | : disabled           |
| Command History      |                    |           |        |          |              |                      |
| Release              |                    |           |        |          | Modification |                      |
| 10.07orearlier       |                    |           |        |          | --           |                      |
| Command Information  |                    |           |        |          |              |                      |
156
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Platforms | Command | context | Authority                                            |
| --------- | ------- | ------- | ---------------------------------------------------- |
| 6200      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show running-config |                 | current-context |     |
| ------------------- | --------------- | --------------- | --- |
| show running-config | current-context |                 |     |
Description
Showstherunningconfigurationforthecurrent-context.IfuserisinthecontextofAruba-Central
(config-aruba-central),thenArubaCentralrunningconfigurationisdisplayed.
Examples
ShowstherunningconfigurationofArubaCentral:
switch(config-aruba-central)# show running-config current-context
aruba-central
disable
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
ArubaCentralintegration|157

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

158

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
Portfiltering|159

| show portfilter | [<IFNAME>] |     |
| --------------- | ---------- | --- |
Description
Displaysfiltersettingsforallinterfacesoraspecificinterface.
Parameter Description
<IFNAME> Specifiestheingressinterfacename.
Specifiesoneofthesevalues:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
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
160
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Portfiltering|161

Chapter 13

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

162

| switch(config)# |     | ip dns | domain-name | switch.com |
| --------------- | --- | ------ | ----------- | ---------- |
switch(config)#
|                 |                 | ip dns | server-address | 1.1.1.1 |
| --------------- | --------------- | ------ | -------------- | ------- |
| switch(config)# |                 | ip dns | host myhost1   | 3.3.3.3 |
| switch(config)# |                 | exit   |                |         |
| switch#         | show            | ip dns |                |         |
| VRF             | Name : vrf_mgmt |        |                |         |
| Host            | Name            |        |                | Address |
--------------------------------------------------------------------------------
| VRF    | Name : vrf_default |              |     |         |
| ------ | ------------------ | ------------ | --- | ------- |
| Domain | Name               | : switch.com |     |         |
| DNS    | Domain list        | :            |     |         |
| Name   | Server(s)          | : 1.1.1.1    |     |         |
| Host   | Name               |              |     | Address |
--------------------------------------------------------------------------------
myhost1
| DNS       | client      | commands      |      |                  |
| --------- | ----------- | ------------- | ---- | ---------------- |
| ip dns    | domain-list |               |      |                  |
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | <VRF-NAME>]      |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf <VRF-NAME>] |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
| vrf <VRF-NAME> |     |     |     | SpecifiesaVRFname.Default:default. |
| -------------- | --- | --- | --- | ---------------------------------- |
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     | ip dns | domain-list | domain1.com |
| --------------- | --- | ------ | ----------- | ----------- |
| switch(config)# |     | ip dns | domain-list | domain2.com |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |         | no ip dns | domain-list | domain1.com |
| --------------- | ------- | --------- | ----------- | ----------- |
| Command         | History |           |             |             |
DNS|163

| Release        |             |         |         |     | Modification |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
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
| switch(config)# |             |     | no ip dns | domain-name |              | domain.com |     |
| --------------- | ----------- | --- | --------- | ----------- | ------------ | ---------- | --- |
| Command         | History     |     |           |             |              |            |     |
| Release         |             |     |           |             | Modification |            |     |
| 10.07orearlier  |             |     |           |             | --           |            |     |
| Command         | Information |     |           |             |              |            |     |
164
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

| Platforms |     | Command | context |     | Authority |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| ThisexampledefinesanIPv4addressof     |             |     |        |            | 3.3.3.3forhost1.  |     |       |
| ------------------------------------- | ----------- | --- | ------ | ---------- | ----------------- | --- | ----- |
| switch(config)#                       |             | ip  | dns    | host host1 | 3.3.3.3           |     |       |
| ThisexampledefinesanIPv6addressofb::5 |             |     |        |            | forhost 1.        |     |       |
| switch(config)#                       |             | ip  | dns    | host host1 | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |             |     |        |            | host 1withaddress |     | b::5. |
| switch(config)#                       |             | no  | ip dns | host       | host1 b::5        |     |       |
| Command                               | History     |     |        |            |                   |     |       |
| Release                               |             |     |        |            | Modification      |     |       |
| 10.07orearlier                        |             |     |        |            | --                |     |       |
| Command                               | Information |     |        |            |                   |     |       |
DNS|165

| Platforms |     | Command | context |     | Authority |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- |
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
switch(config)#
|     |     |     | ip dns | server-address |     | a::1 |     |
| --- | --- | --- | ------ | -------------- | --- | ---- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)# |             |     | no ip dns | server-address |              | a::1 |     |
| --------------- | ----------- | --- | --------- | -------------- | ------------ | ---- | --- |
| Command         | History     |     |           |                |              |      |     |
| Release         |             |     |           |                | Modification |      |     |
| 10.07orearlier  |             |     |           |                | --           |      |     |
| Command         | Information |     |           |                |              |      |     |
166
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip dns |      |             |     |     |     |
| ----------- | ---- | ----------- | --- | --- | --- |
| show ip dns | [vrf | <VRF-NAME>] |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
| switch(config)# |     | ip  | dns domain-name |     | domain.com  |
| --------------- | --- | --- | --------------- | --- | ----------- |
| switch(config)# |     | ip  | dns domain-list |     | domain5.com |
| switch(config)# |     | ip  | dns domain-list |     | domain8.com |
switch(config)#
|                 |           | ip         | dns server-address |         | 4.4.4.4     |
| --------------- | --------- | ---------- | ------------------ | ------- | ----------- |
| switch(config)# |           | ip         | dns server-address |         | 6.6.6.6     |
| switch(config)# |           | ip         | dns host           | host3   | 5.5.5.5     |
| switch(config)# |           | ip         | dns host           | host3   | c::12       |
| switch#         | show      | ip dns     |                    |         |             |
| VRF Name        | : default |            |                    |         |             |
| Domain Name     | :         | domain.com |                    |         |             |
| DNS Domain      | list      | :          | domain5.com,       |         | domain8.com |
| Name Server(s)  |           | : 4.4.4.4, |                    | 6.6.6.6 |             |
| Host Name       |           | Address    |                    |         |             |
-------------------------------
| host3          |             | 5.5.5.5 |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| host3          |             | c::12   |         |     |              |
| Command        | History     |         |         |     |              |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      | Command     |         | context |     | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|167

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
RADIUS server and Aruba ClearPass Policy Manager. Local MAC match feature is useful when you do not
want to afford RADIUS infrastructure or when you want to use local authentication as a backup method
in case the RADIUS server is unreachable.

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

168

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
Devicediscoveryandconfiguration|169

1. CreateaMACgroupwiththemac-groupcommand.
2. DefinerulesforaddingdevicestoaMACgroupwiththematch (for MAC groups)command.
3. DefinerulesforignoringdevicessothattheyarenotaddedtoaMACgroupwiththeignore
(for
|     | MAC groups)command. |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
4. Createadeviceprofilewiththeport-access device-profilecommand.
5. AssociateaMACgroupwithadeviceprofilewiththeassociate mac-groupcommand.
6. Addaroletoadeviceprofilewiththeassociate rolecommand.Makesurethattheroleis
alreadycreated.Forinformationonhowtocreatearole,seeportaccessroleinformationinthe
SecurityGuide.
7. Enableadeviceprofilewiththeenablecommand.
| Device | profile        |     | commands    |     |                |
| ------ | -------------- | --- | ----------- | --- | -------------- |
| aaa    | authentication |     | port-access |     | allow-cdp-bpdu |
| aaa    | authentication |     | port-access |     | allow-cdp-bpdu |
| no aaa | authentication |     | port-access |     | allow-cdp-bpdu |
Description
AllowsallpacketsrelatedtotheCDP(CiscoDiscoveryProtocol)BPDU(BridgeProtocolDataUnit)ona
secureport.
ThenoformofthiscommandblockstheCDPBPDUonasecureport.Onanonsecureport,the
commandhasnoeffect.
Examples
AllowingaCDPBPDUonsecureport1/1/1:
| switch(config)# |     |     | interface | 1/1/1 |     |
| --------------- | --- | --- | --------- | ----- | --- |
switch(config-if)# aaa authentication port-access allow-cdp-bpdu
| switch(config-if)# |                |     | do  | show | running-config |
| ------------------ | -------------- | --- | --- | ---- | -------------- |
| Current            | configuration: |     |     |      |                |
!
| !Version |         | AOS-CX | 10.0X.0000 |     |     |
| -------- | ------- | ------ | ---------- | --- | --- |
| led      | locator | on     |            |     |     |
!
!
| vlan | 1              |     |             |     |          |
| ---- | -------------- | --- | ----------- | --- | -------- |
| aaa  | authentication |     | port-access |     | mac-auth |
enable
| aaa | authentication |     | port-access |     | dot1x authenticator |
| --- | -------------- | --- | ----------- | --- | ------------------- |
enable
| interface |     | 1/1/1 |     |     |     |
| --------- | --- | ----- | --- | --- | --- |
no shutdown
|     | vlan               | access | 1   |             |                |
| --- | ------------------ | ------ | --- | ----------- | -------------- |
|     | aaa authentication |        |     | port-access | allow-cdp-bpdu |
|     | aaa authentication |        |     | port-access | mac-auth       |
enable
|     | aaa authentication |     |     | port-access | dot1x authenticator |
| --- | ------------------ | --- | --- | ----------- | ------------------- |
enable
switch(config-if)# do show port-access device-profile interface all
| Port | 1/1/1,    | Neighbor-Mac |     | 00:0c:29:9e:d1:20 |     |
| ---- | --------- | ------------ | --- | ----------------- | --- |
|      | Profile   | Name         | :   | access_switches   |     |
|      | LLDP      | Group        | :   |                   |     |
|      | CDP Group |              | :   | aruba-ap_cdp      |     |
170
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- |

Role
Status
Failure Reason

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

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6200

config-if

Administrators or local user group members with execution rights
for this command.

aaa authentication port-access allow-cdp-proxy-logoff

aaa authentication port-access allow-cdp-proxy-logoff
no aaa authentication port-access allow-cdp-proxy-logoff

Description

Allows a client to be logged off from the system via a special TLV in the CDP packet. By default, proxy
logoff via CDP packet support is disabled. When allow-cdp-proxy-logoff is enabled, TLV received from
CDP packets corresponding to logoff processing will be read and logoff is issued to the clients. This only
works on client authentication enabled ports and aaa authentication port-access allow-cdp-bpdu
must be enabled to process .

Examples

Allowing a client to be logged off from the system via a special TLV in the CDP packet:

Device discovery and configuration | 171

| switch(config)# |     |     | interface |     | 1/1/1 |     |     |     |     |
| --------------- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
switch(config-if)#
|                    |     |       |     | aaa authentication |                |     | port-access | allow-cdp-proxy-logoff |     |
| ------------------ | --- | ----- | --- | ------------------ | -------------- | --- | ----------- | ---------------------- | --- |
| switch(config-if)# |     |       |     | show               | running-config |     | interface   | 1/1/1                  |     |
| interface          |     | 1/1/1 |     |                    |                |     |             |                        |     |
no shutdown
|     | vlan | access         | 1   |             |     |                        |               |     |     |
| --- | ---- | -------------- | --- | ----------- | --- | ---------------------- | ------------- | --- | --- |
|     | aaa  | authentication |     | port-access |     | allow-cdp-bpdu         |               |     |     |
|     | aaa  | authentication |     | port-access |     | allow-cdp-proxy-logoff |               |     |     |
|     | aaa  | authentication |     | port-access |     | allow                  | client-limit  |     | 2   |
|     | aaa  | authentication |     | port-access |     | dot1x                  | authenticator |     |     |
enable
|     | aaa | authentication |     | port-accss |     | mac-auth |     |     |     |
| --- | --- | -------------- | --- | ---------- | --- | -------- | --- | --- | --- |
enable
exit
| Command    | History     |         |     |         |     |                    |     |     |     |
| ---------- | ----------- | ------- | --- | ------- | --- | ------------------ | --- | --- | --- |
| Release    |             |         |     |         |     | Modification       |     |     |     |
| 10.09.1000 |             |         |     |         |     | Commandintroduced. |     |     |     |
| Command    | Information |         |     |         |     |                    |     |     |     |
| Platforms  |             | Command |     | context |     | Authority          |     |     |     |
config-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| aaa    | authentication |     | port-access |             | allow-lldp-bpdu |                 |     |     |     |
| ------ | -------------- | --- | ----------- | ----------- | --------------- | --------------- | --- | --- | --- |
| aaa    | authentication |     | port-access |             | allow-lldp-bpdu |                 |     |     |     |
| no aaa | authentication |     |             | port-access |                 | allow-lldp-bpdu |     |     |     |
Description
AllowsallpacketsrelatedtotheLLDPBPDU(BridgeProtocolDataUnit)onasecureport.
ThenoformofthiscommandblockstheLLDPBPDUonasecureport.Onanonsecureport,the
commandhasnoeffect.
Examples
AllowinganLLDPBPDUonsecureport1/1/1:
| switch(config)# |     |     | interface |     | 1/1/1 |     |     |     |     |
| --------------- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
switch(config-if)# aaa authentication port-access allow-lldp-bpdu
| switch(config-if)# |     |                |     | do show | running-config |     |     |     |     |
| ------------------ | --- | -------------- | --- | ------- | -------------- | --- | --- | --- | --- |
| Current            |     | configuration: |     |         |                |     |     |     |     |
!
| !Version |         | AOS-CX | 10.0X.0000 |     |     |     |     |     |     |
| -------- | ------- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
| led      | locator | on     |            |     |     |     |     |     |     |
!
!
| vlan | 1              |     |     |             |     |          |     |     |     |
| ---- | -------------- | --- | --- | ----------- | --- | -------- | --- | --- | --- |
| aaa  | authentication |     |     | port-access |     | mac-auth |     |     |     |
enable
172
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

interface 1/1/1
no shutdown
vlan access 1

aaa authentication port-access allow-lldp-bpdu
aaa authentication port-access mac-auth

enable

switch(config-if)# do show port-access device-profile interface all
Port 1/1/1, Neighbor-Mac 00:0c:29:9e:d1:20

Profile Name
LLDP Group
CDP Group
Role
Status
Failure Reason

: access_switches
: 2920-grp
:
: local_2920_role
: Profile Applied
:

Blocking LLDP BPDU on secure port 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no aaa authentication port-access allow-lldp-bpdu
switch(config-if)# do show running-config
Current configuration:
!
!Version AOS-CX 10.0X.0000led locator on
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

6200

config-if

Administrators or local user group members with execution rights
for this command.

associate cdp-group

associate cdp-group <GROUP-NAME>
no associate cdp-group <GROUP-NAME>

Description

Associates a CDP (Cisco Discovery Protocol) group with a device profile. A maximum of two CDP groups
can be associated with a device profile.

Device discovery and configuration | 173

ThenoformofthiscommandremovesaCDPgroupfromadeviceprofile.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME> SpecifiesthenameoftheCDPgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheCDPgroupmy-cdp-groupwiththedeviceprofileprofile01:
| switch(config)# |     |     | port-access | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | -------------- | --- | --------- | --- |
switch(config-device-profile)#
|     |     |     |     | associate |     | cdp-group | my-cdp-group |
| --- | --- | --- | --- | --------- | --- | --------- | ------------ |
RemovingtheCDPgroupmy-cdp-groupfromthedeviceprofileprofile01:
| switch(config)# |     |     | port-access | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | -------------- | --- | --------- | --- |
switch(config-device-profile)# no associate cdp-group my-cdp-group
| Command        | History     |         |         |     |              |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |         |     | Modification |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
config-device-profile
| 6200 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- |
rightsforthiscommand.
| associate    | lldp-group |            |              |     |     |     |     |
| ------------ | ---------- | ---------- | ------------ | --- | --- | --- | --- |
| associate    | lldp-group |            | <GROUP-NAME> |     |     |     |     |
| no associate |            | lldp-group | <GROUP-NAME> |     |     |     |     |
Description
AssociatesanLLDPgroupwithadeviceprofile.AmaximumoftwoLLDPgroupscanbeassociatedwith
adeviceprofile
ThenoformofthiscommandremovesanLLDPgroupfromadeviceprofile.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME>
SpecifiesthenameoftheLLDPgrouptoassociatewiththedevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheLLDPgroupmy-lldp-groupwiththedeviceprofileprofile01:
174
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

| switch(config)# |     |     | port-access |     | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | --- | -------------- | --- | --------- | --- |
switch(config-device-profile)#
|     |     |     |     |     | associate |     | lldp-group | my-lldp-group |
| --- | --- | --- | --- | --- | --------- | --- | ---------- | ------------- |
RemovingtheLLDPgroupmy-lldp-groupfromthedeviceprofileprofile01:
| switch(config)# |     |     | port-access |     | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | --- | -------------- | --- | --------- | --- |
switch(config-device-profile)# no associate lldp-group my-lldp-group
| Command        | History     |         |     |         |     |              |     |     |
| -------------- | ----------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |     |         |     | Modification |     |     |
| 10.07orearlier |             |         |     |         |     | --           |     |     |
| Command        | Information |         |     |         |     |              |     |     |
| Platforms      |             | Command |     | context |     | Authority    |     |     |
config-device-profile
| 6200 |     |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |
| ---- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- |
rightsforthiscommand.
| associate    | mac-group |           |              |              |     |     |     |     |
| ------------ | --------- | --------- | ------------ | ------------ | --- | --- | --- | --- |
| associate    | mac-group |           | <GROUP-NAME> |              |     |     |     |     |
| no associate |           | mac-group |              | <GROUP-NAME> |     |     |     |     |
Description
AssociatesaMACgroupwithadeviceprofile.AmaximumoftwoMACgroupscanbeassociatedwitha
deviceprofile.
ThenoformofthiscommandremovesaMACgroupfromadeviceprofile.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<GROUP-NAME>
SpecifiesthenameoftheMACgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheMACgroupmac01-groupwiththedeviceprofileprofile01:
switch(config)#
|                                |     |     | port-access |     | device-profile |     | profile01 |             |
| ------------------------------ | --- | --- | ----------- | --- | -------------- | --- | --------- | ----------- |
| switch(config-device-profile)# |     |     |             |     | associate      |     | mac-group | mac01-group |
RemovingtheMACgroupmac01-groupfromthedeviceprofileprofile01:
| switch(config)# |     |     | port-access |     | device-profile |     | profile01 |     |
| --------------- | --- | --- | ----------- | --- | -------------- | --- | --------- | --- |
switch(config-device-profile)# no associate mac-group mac01-group
| Command | History |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Devicediscoveryandconfiguration|175

| Release             |         |         |     | Modification |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6200 config-device-profile Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| associate role |                  |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- |
| associate role | <ROLE-NAME>      |     |     |     |     |
| no associate   | role <ROLE-NAME> |     |     |     |     |
Description
Associatesarolewithadeviceprofile.Onlyonerolecanbeassociatedwithadeviceprofile.For
informationonhowtoconfigurearole,seetheportaccessroleinformationintheSecurityGuide.
Thenoformofthiscommandremovesarolefromadeviceprofile.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<ROLE-NAME> Specifiesthenameoftheroletoassociatewiththedeviceprofile.
Range:1to64alphanumericcharacters.
Examples
Associatingtherolemy-rolewiththedeviceprofileprofile01:
| switch(config)#                | port-access |     | device-profile |     | profile01    |
| ------------------------------ | ----------- | --- | -------------- | --- | ------------ |
| switch(config-device-profile)# |             |     | associate      |     | role my-role |
Removingtherolemy-rolefromthedeviceprofileprofile01:
| switch(config)#                | port-access |         | device-profile |              | profile01    |
| ------------------------------ | ----------- | ------- | -------------- | ------------ | ------------ |
| switch(config-device-profile)# |             |         | no             | associate    | role my-role |
| Command History                |             |         |                |              |              |
| Release                        |             |         |                | Modification |              |
| 10.07orearlier                 |             |         |                | --           |              |
| Command Information            |             |         |                |              |              |
| Platforms                      | Command     | context |                | Authority    |              |
6200 config-device-profile Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
176
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

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
| switch(config)#                | port-access | device-profile | profile01    |
| ------------------------------ | ----------- | -------------- | ------------ |
| switch(config-device-profile)# |             | no             | disable      |
| Command History                |             |                |              |
| Release                        |             |                | Modification |
| 10.07orearlier                 |             |                | --           |
| Command Information            |             |                |              |
| Platforms                      | Command     | context        | Authority    |
6200 config-device-profile Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
enable
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
Devicediscoveryandconfiguration|177

| switch(config)# | port-access |     | device-profile |     | profile01 |
| --------------- | ----------- | --- | -------------- | --- | --------- |
switch(config-device-profile)#
no enable
| Command History     |         |         |     |              |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| Release             |         |         |     | Modification |     |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6200 config-device-profile Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ignore (for CDP | groups) |     |     |     |     |
| --------------- | ------- | --- | --- | --- | --- |
ignore [seq <SEQ-NUM>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- |
no ignore [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- |
Description
DefinesaruletoignoredevicesforaCDP(CiscoDiscoveryProtocol)group.Upto64match/ignorerules
canbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaCDPgroup.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
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
Examples
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01intheplatform
TLV:
| switch(config)#           | port-access |     | cdp-group       | grp01 |            |
| ------------------------- | ----------- | --- | --------------- | ----- | ---------- |
| switch(config-cdp-group)# |             |     | ignore platform |       | PLATFORM01 |
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsSWVERSIONinsoftware
versionTLV:
178
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

| switch(config)# | port-access |     | cdp-group | grp01 |
| --------------- | ----------- | --- | --------- | ----- |
switch(config-cdp-group)#
|     |     |     | ignore | sw-version SWVERSION |
| --- | --- | --- | ------ | -------------------- |
Removingtherulethatmatchesthesequencenumber25fromtheCDPgroupnamedgrp01.
| switch(config)#           | port-access |         | cdp-group | grp01        |
| ------------------------- | ----------- | ------- | --------- | ------------ |
| switch(config-cdp-group)# |             |         | no ignore | seq 25       |
| Command History           |             |         |           |              |
| Release                   |             |         |           | Modification |
| 10.07orearlier            |             |         |           | --           |
| Command Information       |             |         |           |              |
| Platforms                 | Command     | context |           | Authority    |
config-cdp-group
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ignore (for LLDP | groups) |     |     |     |
| ---------------- | ------- | --- | --- | --- |
ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> |     | [type | <KEY> [value <VALUE>]]} |
| ---------- | ------------ | --- | ----- | ----------------------- |
no ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> |     | [type | <KEY> [value <VALUE>]]} |
| ---------- | ------------ | --- | ----- | ----------------------- |
Description
DefinesaruletoignoredevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedfora
group.
ThenoformofthiscommandremovesaruleforignoringdevicesfromanLLDPgroup.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
| sys-desc <SYS-DESC> |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname <SYS-NAME> SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY>    |     |     |     | SpecifiesthevendorOUIsubtypekey.Optional.      |
| ------------- | --- | --- | --- | ---------------------------------------------- |
| value <VALUE> |     |     |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |
alphanumericcharacters.
Devicediscoveryandconfiguration|179

Examples
AddingaruletotheLLDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01inthesystem
descriptionTLV:
| switch(config)#            | port-access |     | lldp-group |          | grp01      |
| -------------------------- | ----------- | --- | ---------- | -------- | ---------- |
| switch(config-lldp-group)# |             |     | ignore     | sys-desc | PLATFORM01 |
Removingtherulethatmatchesthesequencenumber25fromtheLLDPgroupnamedgrp01.
| switch(config)#            | port-access |         | lldp-group |              | grp01 |
| -------------------------- | ----------- | ------- | ---------- | ------------ | ----- |
| switch(config-lldp-group)# |             |         | no match   | seq          | 25    |
| Command History            |             |         |            |              |       |
| Release                    |             |         |            | Modification |       |
| 10.07orearlier             |             |         |            | --           |       |
| Command Information        |             |         |            |              |       |
| Platforms                  | Command     | context |            | Authority    |       |
6200 config-lldp-group Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ignore (for MAC | groups) |     |     |     |     |
| --------------- | ------- | --- | --- | --- | --- |
[seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
DefinesaruletoignoredevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddress
mask,orMACOrganizationalUniqueIdentifier(OUI).Upto64ignorerulescanbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaMACgroup.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheentrysequenceIDoftheruletocreateormodifya
MACgroup.IfnoIDisspecifiedwhenaddingarule,anIDis
automaticallyassignedinincrementsof10intheorderinwhich
rulesareadded.Whenmorethanonerulematchesthecommand
entered,therulewiththelowestIDtakesprecedence.Range:1to
4294967295.
| mac <MAC-ADDR> |     |     |     | SpecifiestheMACaddressofthedevicetoignore. |     |
| -------------- | --- | --- | --- | ------------------------------------------ | --- |
mac-mask <MAC-MASK> SpecifiestheMACaddressmasktoignoredevicesinthatrange.
SupportedMACaddressmasks:/32and/40.
mac-oui <MAC-OUI> SpecifiestheMACOUItoignoredevicesinthatrange.Supports
MACOUIaddressofmaximumlengthof24bits.
180
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

Usage
Toachievetherequiredconfigurationofmatchesfordevices,itisrecommendedtofirstignorethe
devicesthatyoudonotwanttoadd.Thenmatchthecriteriafortherestofthedevicesthatyouwantto
addtotheMACgroup.
Forexample,ifyouwanttoignoreaspecificdevicebutaddalltheotherdevicesthatbelongtoaMAC
OUI,thenyoumustfirstconfiguretheignorecriteriawithalowersequencenumber.Andthen
configurematchcriteriawithahighersequencenumber.
Examples
AddingaruletotheMACgroupgrp01toignoreadevicebasedonMACaddress,butmatchallother
devicesbelongingtoaMACOUI:
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
```
AddingaruletotheMACgroupgrp01toignoredevicesbasedonMACaddressmask,butmatchall
otherdevicesbelongingtoaMACOUI:
| switch(config)#           | mac-group | grp01           |                |
| ------------------------- | --------- | --------------- | -------------- |
| switch(config-mac-group)# |           | ignore mac-mask | 1a:2b:3c:4d/32 |
| switch(config-mac-group)# |           | match mac-oui   | 1a:2b:3c       |
| switch(config-mac-group)# |           | exit            |                |
| switch(config)#           | do show   | running-config  |                |
Current configuration:
!
| !Version | Virtual.10.0X.0001 |     |     |
| -------- | ------------------ | --- | --- |
AOS-CX
| !export-password: | default |     |     |
| ----------------- | ------- | --- | --- |
| led locator on    |         |     |     |
!
!
Devicediscoveryandconfiguration|181

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
| switch(config)#           | mac-group | grp03          |          |
| ------------------------- | --------- | -------------- | -------- |
| switch(config-mac-group)# |           | ignore mac-oui | 81:cd:93 |
AddingaruletotheMACgroupgrp01thatignoresdeviceswithasequencenumberandbasedonMAC
address:
| switch(config)#           | mac-group | grp01         |                       |
| ------------------------- | --------- | ------------- | --------------------- |
| switch(config-mac-group)# |           | seq 10 ignore | mac b2:c3:44:12:78:11 |
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
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |                       |     |     |
| --------------- | --------------------- | --- | --- |
| seq 10 ignore   | mac b2:c3:44:12:78:11 |     |     |
182
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

```
RemovingtherulefromtheMACgroupgrp01basedonsequencenumber:
| switch(config)#           | mac-group | grp01          |        |     |
| ------------------------- | --------- | -------------- | ------ | --- |
| switch(config-mac-group)# |           | no ignore      | seq 10 |     |
| switch(config-mac-group)# |           | exit           |        |     |
| switch(config)#           | do show   | running-config |        |     |
Current configuration:
!
| !Version | Virtual.10.0X.0001 |     |     |     |
| -------- | ------------------ | --- | --- | --- |
AOS-CX
| !export-password: | default |     |     |     |
| ----------------- | ------- | --- | --- | --- |
| led locator on    |         |     |     |     |
!
!
vlan 1
| interface mgmt |     |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |     |
| --------------- | --- | --- | --- | --- |
```
AddingaruletotheMACgroupgrp01thatignoresdeviceswithMACentrysequencenumberand
basedonMACOUI:
switch(config)#
|                           | mac-group | grp01  |                              |          |
| ------------------------- | --------- | ------ | ---------------------------- | -------- |
| switch(config-mac-group)# |           | seq 10 | ignore mac b2:c3:44:12:78:11 |          |
| switch(config-mac-group)# |           | seq 20 | ignore mac-oui               | 1a:2b:3c |
switch(config-mac-group)# seq 30 ignore mac-mask 71:14:89:f3/32
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
| mac-group grp01 |          |                   |     |     |
| --------------- | -------- | ----------------- | --- | --- |
| seq 10 ignore   | mac      | b2:c3:44:12:78:11 |     |     |
| seq 20 ignore   | mac-oui  | 1a:2b:3c          |     |     |
| seq 30 ignore   | mac-mask | 71:14:89:f3/32    |     |     |
```
RemovingtherulefromtheMACgroupgrp01basedonsequencenumberandMACOUI:
| switch(config)#           | mac-group | grp01          |                   |          |
| ------------------------- | --------- | -------------- | ----------------- | -------- |
| switch(config-mac-group)# |           | no seq         | 20 ignore mac-oui | 1a:2b:3c |
| switch(config-mac-group)# |           | exit           |                   |          |
| switch(config)#           | do show   | running-config |                   |          |
Devicediscoveryandconfiguration|183

| Current | configuration: |     |     |
| ------- | -------------- | --- | --- |
!
| !Version          | AOS-CX Virtual.10.0X.0001 |         |     |
| ----------------- | ------------------------- | ------- | --- |
| !export-password: |                           | default |     |
| led locator       | on                        |         |     |
!
!
vlan 1
| interface   | mgmt      |                         |     |
| ----------- | --------- | ----------------------- | --- |
| no shutdown |           |                         |     |
| ip dhcp     |           |                         |     |
| mac-group   | grp01     |                         |     |
| seq         | 10 ignore | mac b2:c3:44:12:78:11   |     |
| seq         | 30 ignore | mac-mask 71:14:89:f3/32 |     |
```
Removingtherulethatmatchesthesequencenumber25fromtheMACgroupnamedgrp01.
| switch(config)#           | mac-group | grp01     |              |
| ------------------------- | --------- | --------- | ------------ |
| switch(config-mac-group)# |           | no ignore | seq 25       |
| Command History           |           |           |              |
| Release                   |           |           | Modification |
| 10.07orearlier            |           |           | --           |
| Command Information       |           |           |              |
| Platforms                 | Command   | context   | Authority    |
6200 config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
184
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

CreatingaMACgroupnamedgrp01:
| switch(config)#           | mac-group |     | grp01 |
| ------------------------- | --------- | --- | ----- |
| switch(config-mac-group)# |           |     | exit  |
RemovingaMACgroupnamedgrp01:
| switch(config)#     | no      | mac-group | grp01        |
| ------------------- | ------- | --------- | ------------ |
| Command History     |         |           |              |
| Release             |         |           | Modification |
| 10.07orearlier      |         |           | --           |
| Command Information |         |           |              |
| Platforms           | Command | context   | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| match (for CDP | groups) |     |     |
| -------------- | ------- | --- | --- |
match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |
| ---------------- | --- | ---------- | --- |
no match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |
| ---------------- | --- | ---------- | --- |
Description
DefinesaruletomatchdevicesforaCDPgroup.Amaximumof32CDPgroupscanbeconfiguredon
theswitch.Upto64matchorignorerulescanbedefinedforeachgroup.
ThenoformofthiscommandremovesaruleforaddingdevicestoaCDPgroup.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
platform <PLATFORM> Specifiesthehardwareormodeldetailsoftheneighbor.Range:1
to128alphanumericcharacters.
| sw-version | <SWVERSION> |     |     |
| ---------- | ----------- | --- | --- |
Specifiesthesoftwareversionoftheneighbor.Range:1to128
alphanumericcharacters.
voice-vlan-query <VLAN-ID> SpecifiestheVLANqueryvalueoftheneighbor.Range:1to
65535.
Examples
Devicediscoveryandconfiguration|185

AddingrulestomatchaCiscodevicewithaspecificsoftwareversiononVLAN512totheCDPgroup
grp01:
| switch(config)#           |     |     | port-access | cdp-group |                  | grp01     |     |
| ------------------------- | --- | --- | ----------- | --------- | ---------------- | --------- | --- |
| switch(config-cdp-group)# |     |     |             | match     | platform         | CISCO     |     |
| switch(config-cdp-group)# |     |     |             | match     | sw-version       | 11.2(12)P |     |
| switch(config-cdp-group)# |     |     |             | match     | voice-vlan-query |           | 512 |
switch(config-cdp-group)# match seq 50 platform cisco sw-version 11.2(12)P voice-
| vlan-query                |     | 512            |         |                |     |     |     |
| ------------------------- | --- | -------------- | ------- | -------------- | --- | --- | --- |
| switch(config-cdp-group)# |     |                |         | exit           |     |     |     |
| switch(config)#           |     |                | do show | running-config |     |     |     |
| Current                   |     | configuration: |         |                |     |     |     |
!
| !Version          |         | AOS-CX | Virtual.10.0X.000 |     |     |     |     |
| ----------------- | ------- | ------ | ----------------- | --- | --- | --- | --- |
| !export-password: |         |        | default           |     |     |     |     |
| led               | locator | on     |                   |     |     |     |     |
!
!
vlan 1
| port-access |     | cdp-group |                  | grp01     |     |     |     |
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
| switch(config)# |     |     | port-access | cdp-group |     | grp01 |     |
| --------------- | --- | --- | ----------- | --------- | --- | ----- | --- |
switch(config-cdp-group)#
|                |             |         |         | match | vendor-oui   | 000b86 |     |
| -------------- | ----------- | ------- | ------- | ----- | ------------ | ------ | --- |
| Command        | History     |         |         |       |              |        |     |
| Release        |             |         |         |       | Modification |        |     |
| 10.07orearlier |             |         |         |       | --           |        |     |
| Command        | Information |         |         |       |              |        |     |
| Platforms      |             | Command | context |       | Authority    |        |     |
6200 config-cdp-group Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| match | (for LLDP | groups) |     |     |     |     |     |
| ----- | --------- | ------- | --- | --- | --- | --- | --- |
match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
|     | vendor-oui | <VENDOR-OUI> |     | [type | <KEY> | [value <VALUE>]]} |     |
| --- | ---------- | ------------ | --- | ----- | ----- | ----------------- | --- |
no match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
|     | vendor-oui | <VENDOR-OUI> |     | [type | <KEY> | [value <VALUE>]]} |     |
| --- | ---------- | ------------ | --- | ----- | ----- | ----------------- | --- |
186
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

Description
DefinesaruletomatchdevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedfora
group.
Thenoformofthiscommandremovesarule.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname <SYS-NAME>
SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
| type <KEY>    |     | SpecifiesthevendorOUIsubtypekey.               |     |
| ------------- | --- | ---------------------------------------------- | --- |
| value <VALUE> |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |     |
alphanumericcharacters.
Examples
AddingrulesthatmatchtheLLDPsystemdescriptionArubaSwitchandsystemnameArubatothe
LLDPgroupnamedgrp01:
| switch(config)#            | port-access | lldp-group     | grp01       |
| -------------------------- | ----------- | -------------- | ----------- |
| switch(config-lldp-group)# |             | match sys-desc | ArubaSwitch |
| switch(config-lldp-group)# |             | match sysname  | Aruba       |
| switch(config)#            | do show     | running-config |             |
| Current configuration:     |             |                |             |
!
| !Version          | AOS-CX Virtual.10.0X.000 |     |     |
| ----------------- | ------------------------ | --- | --- |
| !export-password: | default                  |     |     |
| led locator       | on                       |     |     |
!
!
vlan 1
| port-access | lldp-group        | grp01       |     |
| ----------- | ----------------- | ----------- | --- |
| seq         | 10 match sys-desc | ArubaSwitch |     |
| seq         | 20 match sysname  | Aruba       |     |
Removingarulethatmatchesthesequencenumber25fromanLLDPgroupnamedgrp01:
| switch(config)#            | port-access | lldp-group | grp01  |
| -------------------------- | ----------- | ---------- | ------ |
| switch(config-lldp-group)# |             | no match   | seq 25 |
Addingarulethatmatchesthevalueofvendor-OUI000b86withtypeof1totheLLDPgroupnamed
grp01:
Devicediscoveryandconfiguration|187

| switch(config)# | port-access |     | lldp-group | grp01 |     |
| --------------- | ----------- | --- | ---------- | ----- | --- |
switch(config-lldp-group)#
|     |     |     | match vendor-oui | 000b86 type | 1   |
| --- | --- | --- | ---------------- | ----------- | --- |
Addingarulethatmatchesthevalueofvendor-OUI000c34totheLLDPgroupnamedgrp01:
| switch(config)#            | port-access |         | lldp-group       | grp01  |     |
| -------------------------- | ----------- | ------- | ---------------- | ------ | --- |
| switch(config-lldp-group)# |             |         | match vendor-oui | 000c34 |     |
| Command History            |             |         |                  |        |     |
| Release                    |             |         | Modification     |        |     |
| 10.07orearlier             |             |         | --               |        |     |
| Command Information        |             |         |                  |        |     |
| Platforms                  | Command     | context | Authority        |        |     |
config-lldp-group
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| match (for MAC | groups) |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- |
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
client-limitcommand.Forinformationaboutthiscommand,seethe
| authentication | port-access |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- |
SecurityGuideforyourswitch.
188
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

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
mac-mask <MAC-MASK>
SpecifiestheMACaddressmasktoadddevicesinthatrange.
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
| switch(config)#           | mac-group | grp03         |          |
| ------------------------- | --------- | ------------- | -------- |
| switch(config-mac-group)# |           | match mac-oui | 81:cd:93 |
| switch(config-mac-group)# |           | exit          |          |
AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress:
| switch(config)#           | mac-group | grp01          |                             |
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
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
Devicediscoveryandconfiguration|189

| mac-group grp01 |                       |     |     |     |
| --------------- | --------------------- | --- | --- | --- |
| seq 10 match    | mac b2:c3:44:12:78:11 |     |     |     |
```
RemovingdevicesfromtheMACgroupgrp01basedonsequencenumber:
| switch(config)#           | mac-group | grp01          |        |     |
| ------------------------- | --------- | -------------- | ------ | --- |
| switch(config-mac-group)# |           | no match       | seq 10 |     |
| switch(config-mac-group)# |           | exit           |        |     |
| switch(config)#           | do show   | running-config |        |     |
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
| switch(config)#           | mac-group | grp01  |                  |          |
| ------------------------- | --------- | ------ | ---------------- | -------- |
| switch(config-mac-group)# |           | no seq | 20 match mac-oui | 1a:2b:3c |
190
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| switch(config-mac-group)# |     | exit |
| ------------------------- | --- | ---- |
switch(config)#
|     | do show | running-config |
| --- | ------- | -------------- |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |
| ----------------- | ------------------ | --- |
| !export-password: | default            |     |
| led locator on    |                    |     |
!
!
vlan 1
interface
mgmt
no shutdown
ip dhcp
| mac-group grp01 |                       |                |
| --------------- | --------------------- | -------------- |
| seq 10 match    | mac b2:c3:44:12:78:11 |                |
| seq 30 match    | mac-mask              | 71:14:89:f3/32 |
```
AddingdevicestotheMACgroupgrp03withMACentrysequencenumberandbasedonMACaddress
mask:
| switch(config)# | mac-group | grp03 |
| --------------- | --------- | ----- |
switch(config-mac-group)# seq 10 match mac-mask 10:14:a3:b7:55/40
| switch(config-mac-group)# |     | exit |
| ------------------------- | --- | ---- |
switch(config)#
|     | do show | running-config |
| --- | ------- | -------------- |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |
| ----------------- | ------------------ | --- |
| !export-password: | default            |     |
| led locator on    |                    |     |
!
!
vlan 1
interface
mgmt
no shutdown
ip dhcp
| mac-group grp03 |          |                   |
| --------------- | -------- | ----------------- |
| seq 10 match    | mac-mask | 10:14:a3:b7:55/40 |
```
RemovingdevicesfromtheMACgroupgrp03basedonMACaddressmask:
| switch(config)# | mac-group | grp03 |
| --------------- | --------- | ----- |
switch(config-mac-group)# no seq 10 match mac-mask 10:14:a3:b7:55/40
switch(config-mac-group)#
exit
| switch(config)# | do show | running-config |
| --------------- | ------- | -------------- |
Current configuration:
!
| !Version AOS-CX   | Virtual.10.0X.0001 |     |
| ----------------- | ------------------ | --- |
| !export-password: | default            |     |
| led locator on    |                    |     |
!
!
vlan 1
| interface mgmt |     |     |
| -------------- | --- | --- |
no shutdown
Devicediscoveryandconfiguration|191

ip dhcp
| mac-group | grp03 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
```
| Command        | History     |     |         |     |              |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| Release        |             |     |         |     | Modification |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |
| Command        | Information |     |         |     |              |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |
6200 config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| port-access    | cdp-group |     |                  |     |     |     |     |
| -------------- | --------- | --- | ---------------- | --- | --- | --- | --- |
| port-access    | cdp-group |     | <CDP-GROUP-NAME> |     |     |     |     |
| no port-access | cdp-group |     | <CDP-GROUP-NAME> |     |     |     |     |
Description
CreatesaCDP(CiscoDiscoveryProtocol)groupormodifiesanexistingCDPgroup.ACDPGroupisused
toclassifyconnecteddevicesbasedontheCDPpacketdetailsadvertisedbythedevice.Amaximumof
32CDPgroupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesaCDPgroup.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<CDP-GROUP-NAME> SpecifiesthenameoftheCDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
Examples
CreatingaCDPgroupnamedgrp01:
| switch(config)#           |     | port-access |     | cdp-group |                  | grp01     |     |
| ------------------------- | --- | ----------- | --- | --------- | ---------------- | --------- | --- |
| switch(config-cdp-group)# |     |             |     | match     | platform         | CISCO     |     |
| switch(config-cdp-group)# |     |             |     | match     | sw-version       | 11.2(12)P |     |
| switch(config-cdp-group)# |     |             |     | match     | voice-vlan-query |           | 512 |
switch(config-cdp-group)# seq 50 match platform cisco sw-version 11.2(12)P voice-
| vlan-query                | 512            |     |                     |      |     |     |     |
| ------------------------- | -------------- | --- | ------------------- | ---- | --- | --- | --- |
| switch(config-cdp-group)# |                |     |                     | exit |     |     |     |
| switch(config)#           |                | do  | show running-config |      |     |     |     |
| Current                   | configuration: |     |                     |      |     |     |     |
!
| !Version          | AOS-CX | Virtual.10.0X.000 |         |     |     |     |     |
| ----------------- | ------ | ----------------- | ------- | --- | --- | --- | --- |
| !export-password: |        |                   | default |     |     |     |     |
| led locator       | on     |                   |         |     |     |     |     |
!
!
192
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

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

6200

config

Administrators or local user group members with execution rights
for this command.

port-access device-profile

port-access device-profile <DEVICE-PROFILE-NAME>
no port-access device-profile <DEVICE-PROFILE-NAME>

Description

Creates a new device profile and switches to the config-device-profile context. A maximum of 32
device profiles can be created.

The no form of this command removes a device profile.

Parameter

Description

<DEVICE-PROFILE-NAME>

Specifies the name of a device profile. Range: 1 to 32
alphanumeric characters.

Examples

Creating a device profile named profile01:

switch(config)# port-access device-profile profile01
switch(config-device-profile)#

Removing a device profile named profile01:

switch(config)# no port-access device-profile profile01

Command History

Device discovery and configuration | 193

| Release        |             |     |         |     | Modification |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| port-access | device-profile |     |     | mode block-until-profile-applied |     |     |
| ----------- | -------------- | --- | --- | -------------------------------- | --- | --- |
Youmustconfigurethismodeindeviceprofileonlyonstandaloneportswherethereisnosecurityconfigured
andwhenyounotwanttheporttobeofflineuntiloneclientisonboarded.
| port-access    | device-profile |     |     | mode block-until-profile-applied |                             |     |
| -------------- | -------------- | --- | --- | -------------------------------- | --------------------------- | --- |
| no port-access | device-profile |     |     | mode                             | block-until-profile-applied |     |
Description
Configurestheswitchtoblocktheportuntilaprofilematchoccursforadevice.Thisconfigurationis
requiredwhennosecurityfeatureisenabledontheport.
YoumustenablethismodeorsecurityontheportforlocalMACmatchfeaturetooperate.Youmust
notenablebothfeaturesonthesameportatthesametime.
YoumustnotcombineanyotherAAAconfigurationswiththeblock-until-profile-appliedmode.
ThenoformofthiscommandremovesaruleforaddingdevicestoaMACgroup.
Example
Configuringblock-until-profileappliedmodeonport1/1/1:
| switch(config)#    |     | interface |             | 1/1/1 |                |     |
| ------------------ | --- | --------- | ----------- | ----- | -------------- | --- |
| switch(config-if)# |     |           | port-access |       | device-profile |     |
switch(config-if-deviceprofile)# mode block-until-profile-applied
| switch(config-if-deviceprofile)# |                         |     |         |     | end          |                                           |
| -------------------------------- | ----------------------- | --- | ------- | --- | ------------ | ----------------------------------------- |
| Command                          | History                 |     |         |     |              |                                           |
| Release                          |                         |     |         |     | Modification |                                           |
| 10.07orearlier                   |                         |     |         |     | --           |                                           |
| Command                          | Information             |     |         |     |              |                                           |
| Platforms                        | Command                 |     | context |     |              | Authority                                 |
| 6200                             | config-if               |     |         |     |              | Administratorsorlocalusergroupmemberswith |
|                                  | config-if-deviceprofile |     |         |     |              | executionrightsforthiscommand.            |
194
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- |

port-access lldp-group

port-access lldp-group <LLDP-GROUP-NAME>
no port-access lldp-group <LLDP-GROUP-NAME>

Description

Creates an LLDP group or modifies an existing LLDP group. An LLDP group is used to classify connected
devices based on the LLDP type-length-values (TLVs) advertised by the device. A maximum of 32 LLDP
groups can be configured on the switch. Each group accepts 64 match/ignore commands.

The no form of this command removes an LLDP group.

Parameter

Description

<LLDP-GROUP-NAME>

Specifies the name of the LLDP group to create or modify. The
maximum number of characters supported is 32. Required.

Examples

Creating an LLDP group named grp01:

switch(config)# port-access lldp-group grp01
switch(config-lldp-group)#

Removing an LLDP group named grp01:

switch(config)# no port-access lldp-group grp01

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

show port-access device-profile

show port-access device-profile [[interface {all | <INTERFACE-ID>}
[client-status <MAC-ADDR>]] | name <DEVICE-PROFILE-NAME>]

Description

Shows the client status for a specific MAC address or profile name.

Device discovery and configuration | 195

| Parameter      |                   |     | Description |     |
| -------------- | ----------------- | --- | ----------- | --- |
| interface {all | | <INTERFACE-ID>} |     |             |     |
Selectallforallinterfacesorspecifythenameofaninterfacein
theformat:member/slot/port.
| client-status | <MAC-ADDR> |     |     |     |
| ------------- | ---------- | --- | --- | --- |
SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.
name <DEVICE-PROFILE-NAME> Specifiesthenameofthedeviceprofile.
Examples
Showingtheappliedstateofthedeviceprofiles:
| switch# show | port-access | device-profile                     |     |     |
| ------------ | ----------- | ---------------------------------- | --- | --- |
| Profile      | Name        | : accesspoints                     |     |     |
| LLDP         | Groups      | : 2920-grp                         |     |     |
| CDP Groups   |             | :                                  |     |     |
| MAC Groups   |             | : 2920-mac-grp1,2920-iot-grp2      |     |     |
| Role         |             | : local_role_1                     |     |     |
| State        |             | : Enabled                          |     |     |
| Profile      | Name        | : access_switches                  |     |     |
| LLDP         | Groups      | : 2920-grp                         |     |     |
| CDP Groups   |             | :                                  |     |     |
| MAC Groups   |             | :                                  |     |     |
| Role         |             | : local_2920_role                  |     |     |
| State        |             | : Enabled                          |     |     |
| Profile      | Name        | : iot_devices                      |     |     |
| LLDP         | Groups      | :                                  |     |     |
| CDP Groups   |             | :                                  |     |     |
| MAC Groups   |             | : iot_camera-grp1,iot_sensors-grp1 |     |     |
| Role         |             | : local_2920_role                  |     |     |
| State        |             | : Enabled                          |     |     |
| Profile      | Name        | : lobbyaps                         |     |     |
| LLDP         | Groups      | :                                  |     |     |
| CDP Groups   |             | : lobby_ap_cdp_grp                 |     |     |
| MAC Groups   |             | :                                  |     |     |
| Role         |             | : test_ap_role                     |     |     |
| State        |             | : Disabled                         |     |     |
Showingtheappliedstateofthedeviceprofileoninterface1/1/3:
switch# show port-access device-profile interface 1/1/3 client-status
00:0c:29:9e:d1:20
| Port 1/1/3, | Neighbor-Mac | 00:0c:29:9e:d1:20 |              |            |
| ----------- | ------------ | ----------------- | ------------ | ---------- |
| Profile     | Name         | : lobbyaps        |              |            |
| LLDP        | Group        | :                 |              |            |
| CDP Group   |              | : aruba-ap_cdp    |              |            |
| MAC Group   |              | :                 |              |            |
| Role        |              | : test_ap_role    |              |            |
| Status      |              | : Failed          |              |            |
| Failure     | Reason       | : Failed          | to apply MAC | based VLAN |
Showingtheappliedstateofaspecificdeviceprofile:
196
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| switch#             | show port-access | device-profile     | name         | lldp-group |
| ------------------- | ---------------- | ------------------ | ------------ | ---------- |
| Profile             | Name             | : lldp-group       |              |            |
| LLDP                | Groups           | :                  |              |            |
| CDP                 | Groups           | :                  |              |            |
| MAC                 | Groups           | : pc-behind-phone, |              | lldp       |
| Role                |                  | : auth_role        |              |            |
| State               |                  | : Enabled          |              |            |
| Command History     |                  |                    |              |            |
| Release             |                  |                    | Modification |            |
| 10.07orearlier      |                  |                    | --           |            |
| Command Information |                  |                    |              |            |
| Platforms           | Command          | context            | Authority    |            |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Packet boundaries
WhenmultipleLLDPdevicesaredirectlyconnected,anoutboundLLDPpackettravelsonlytothenext
LLDPdevice.AnLLDP-capabledevicedoesnotforwardLLDPpacketstoanyotherdevices,regardlessof
whethertheyareLLDP-enabled.
AninterveninghuborrepeaterforwardstheLLDPpacketsitreceivesinthesamemannerasanyother
multicastpacketsitreceives.Therefore,twoLLDPswitchesjoinedbyahuborrepeaterhandleLLDP
trafficinthesamewaythattheywouldifdirectlyconnected.
Anyintervening802.1DdeviceorLayer-3devicethatiseitherLLDP-unawareorhasdisabledLLDP
operationdropsthepacket.
LLDP-MED
Devicediscoveryandconfiguration|197

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

198

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

n Chassis-ID: Base MAC address of the switch.

n Port-ID: Port number of the physical port.

n Time-to-Live (TTL): Length of time an LLDP neighbor retains advertised data before discarding it.

n System capabilities: Identifies the primary switch capabilities (bridge, router). Identifies the primary

switch functions that are enabled, such as routing.

n System description: Includes switch model name and running software version, and ROM version.

n System name: Name assigned to the switch.

n Management address: Default address selection method unless an optional address is configured.

n Port description: Physical port identifier.

Device discovery and configuration | 199

n PortVLANID:OnanL2port,containsaccessornativeVLANID.OnanL3port,containsavalueof0.
TrunkallowedVLANsinformationarenotadvertisedaspartofthePortVLANIDTLV.(Notsupported
ontheOOBMinterface)
n PortVLANName:AccessornativeVLANname.Enabledbydefault.
n PortMFS:MaximumFrameSize.Enabledbydefault.
| LLDP MED | support |     |
| -------- | ------- | --- |
LLDP-MEDinteroperateswithdirectlyconnectedIPtelephony(endpoint)clientsandprovidesthe
followingfeatures:
n AdvertisementofthevoiceVLANconfiguredontheinterfacewhichisusedbyconnectedIP
telephony(endpoint)clients.
n Advertisementoftheconfiguredlocationontheswitchthatcanbeusedbytheconnectedendpoint.
n Supportforthefast-startcapability
LLDP-MEDisintendedforusewithVoIPendpointsandisnotdesignedtosupportlinksbetweennetwork
infrastructuredevices(suchasswitch-to-switchorswitch-to-routerlinks).
LLDP EEE
EnergyEfficientEthernet(EEE)isamechanismdefinedbyIEEE802.3az,whichisanextensionof802.3
IEEEstandards.EEEdefinessupportforthedevicetooperateintheLowPowerIdle(LPI)modeduring
lowlinkutilization.Thisallowsbothsidesofalinktodisableorturnoffrespectivetransmit/receive
circuitrytosavepower.EEEusesLLDPforexchangingoptimalsetofparametersforbothdevices.
Guidelines
n AnLLDPmustnotcontainmorethanoneEEETLV.
n LLDPmayormaynotbeenabledontheinterfacessupportingEEE.IfLLDPisnotenabled,itmight
notbeintheoptimaloperationalmode.
n EEETLVshouldnotbeexchangeduntilitnegotiatesfromL1anditdetectspeerEEEcapabilities.
n EEETLVisdisabledbydefaultandenabledonlywhenEEEisactive.
n EEEandEEETLVexchangecanbeenabledordisabledattheinterfacelevel.
| Configuring | the LLDP | agent |
| ----------- | -------- | ----- |
Procedure
1. Bydefault,theLLDPagentisenabledonallactiveinterfaces.IfLLDPwasdisabled,enableitwith
thecommandlldp.
2. Bydefault,theLLDPagenttransmitsandreceiveonallinterfaces.TocustomizeLLDPbehavioron
aspecificinterface,usethecommandslldp transmitandlldp receive.
3. Bydefault,theLLDPagentsetsthemanagementaddressinallTLVsinthefollowingorder:
| a. LLDPmanagementIPaddress.     |     |     |
| ------------------------------- | --- | --- |
| b. LoopbackinterfaceIP.         |     |     |
| c. ROP(L3ports)orSVI(L2ports).  |     |     |
| d. OOBM(ManagementinterfaceIP). |     |     |
| e. BaseMAC.                     |     |     |
200
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |
| ----------------------------- | ------------------ | --- |

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

Device discovery and configuration | 201

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| switch(config)# | no  | lldp |     |
| --------------- | --- | ---- | --- |
202
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp dot3
| lldp dot3 {poe | | macphy}      |     |     |
| -------------- | -------------- | --- | --- |
| no lldp dot3   | {poe | macphy} |     |     |
Description
Setsthe802.3TLVstobeadvertised.Bydefault,advertisementofbothPOEandMAC/PHYTLVsis
enabled.NotsupportedontheOOBMinterface.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     |     | Description                                       |
| --------- | --- | --- | ------------------------------------------------- |
| poe       |     |     | SpecifiesadvertisementofpoweroverEthernetdatalink |
classification.
macphy
Specifiesadvertisementofmediaaccesscontrolandphysical
layerinformation.
Examples
EnablingadvertisementofthePOETLV:
switch(config-if)#
lldp dot3 poe
DisablingadvertisementofthePOETLV:
| switch(config-if)#  |     | no lldp dot3 | poe          |
| ------------------- | --- | ------------ | ------------ |
| Command History     |     |              |              |
| Release             |     |              | Modification |
| 10.07orearlier      |     |              | --           |
| Command Information |     |              |              |
Devicediscoveryandconfiguration|203

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp dot3 eee |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 eee |     |     |     |
| no lldp dot3  | eee |     |     |
Description
Setsthe802.3TLVsforEnergy-EfficientEthernet(EEE) tobeadvertised.Bydefault,advertisementofEEE
TLVsisenabled.NotsupportedontheOOBMinterface.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
| Parameter |     |     | Description                              |
| --------- | --- | --- | ---------------------------------------- |
| eee       |     |     | Specifiesadvertisementof802.3TLVsforEEE. |
Examples
EnablingadvertisementoftheEEETLVs:
| switch(config-if)# |     | lldp dot3 | eee |
| ------------------ | --- | --------- | --- |
DisablingadvertisementoftheEEETLVs:
| switch(config-if)#  |         | no lldp | dot3 eee     |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp dot3 mfs |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 mfs |     |     |     |
| no lldp dot3  | mfs |     |     |
Description
Enablesthe802.3TLVlistinLLDP toadvertiseformaximumframesize(MFS).Enabledbydefault.
ThenoformofthiscommanddisablestheadvertisementofmaximumframesizeTLVs.
204
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |
| ----------------------------- | --- | ------------------ | --- |

Examples
EnablingadvertisementofmaximumframesizeTLVs:
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
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
Devicediscoveryandconfiguration|205

Settingtheholdtimeto8timesofthevalueoflldptimer:
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
n IPaddressoftheport
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
206
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

| switch(config)#     | no      | lldp management-ipv4-address |              |
| ------------------- | ------- | ---------------------------- | ------------ |
| Command History     |         |                              |              |
| Release             |         |                              | Modification |
| 10.07orearlier      |         |                              | --           |
| Command Information |         |                              |              |
| Platforms           | Command | context                      | Authority    |
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
BaseMACaddressoftheswitch
n
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
| switch(config)# | no  | lldp management-ipv6-address |     |
| --------------- | --- | ---------------------------- | --- |
| Command History |     |                              |     |
Devicediscoveryandconfiguration|207

| Release        |             |         | Modification |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
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
| switch(config-if)# |     | lldp med | network-policy |     |     |     |
| ------------------ | --- | -------- | -------------- | --- | --- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |         | no lldp | med network-policy |     |     |     |
| ------------------ | ------- | ------- | ------------------ | --- | --- | --- |
| Command            | History |         |                    |     |     |     |
208
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Release             |         |     |         | Modification |     |     |
| ------------------- | ------- | --- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |     |         | --           |     |     |
| Command Information |         |     |         |              |     |     |
| Platforms           | Command |     | context | Authority    |     |     |
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
elin-addr
ConfiguressupportfortheLLDPMEDemergencylocationTLV.
Examples
EnablingsupportfortheLLDPMEDemergencylocationTLV:
switch(config-if)#
|     |     | lldp | med-location |     | elin-addr | gher |
| --- | --- | ---- | ------------ | --- | --------- | ---- |
DisablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | no  | lldp med-location |     | elin-addr | gher |
| ------------------ | --- | --- | ----------------- | --- | --------- | ---- |
EnablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
DisablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# no lldp med-location civic-addr US 1 4 ret 6 tyu 7 tiyuo
| Command History |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
Devicediscoveryandconfiguration|209

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
210
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lldp reinit
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
Devicediscoveryandconfiguration|211

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

212

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
Devicediscoveryandconfiguration|213

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
214
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
Devicediscoveryandconfiguration|215

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
216
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
Devicediscoveryandconfiguration|217

| Release        |             |         |         |     | Modification |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show lldp | configuration |     |                  |     |     |     |
| --------- | ------------- | --- | ---------------- | --- | --- | --- |
| show lldp | configuration |     | [<INTERFACE-ID>] |     |     |     |
Description
ShowsLLDPconfigurationsettingsforallinterfacesoraspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |
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
218
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- |

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
| switch# |        | show lldp     | configuration |     | mgmt |     |
| ------- | ------ | ------------- | ------------- | --- | ---- | --- |
| LLDP    | Global | Configuration |               |     |      |     |
=========================
| LLDP | Enabled  |                 |     | :   | Yes |     |
| ---- | -------- | --------------- | --- | --- | --- | --- |
| LLDP | Transmit | Interval        |     | :   | 30  |     |
| LLDP | Hold     | Time Multiplier |     | :   | 4   |     |
Devicediscoveryandconfiguration|219

| LLDP Transmit |               | Delay | Interval | :   | 2   |     |
| ------------- | ------------- | ----- | -------- | --- | --- | --- |
| LLDP Reinit   |               | Timer | Interval | :   | 2   |     |
| LLDP Trap     | Enabled       |       |          | :   | Yes |     |
| LLDP Port     | Configuration |       |          |     |     |     |
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
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | local-device |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- |
| show lldp | local-device |     |     |     |     |     |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsare
configuredonanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDson
accessinterfaces.
Example
ShowingglobalLLDPinformationonly(allportsincludingOOBMportareadministrativelydown):
| switch# | show | lldp | local-device |     |     |     |
| ------- | ---- | ---- | ------------ | --- | --- | --- |
| Global  | Data |      |              |     |     |     |
===========
| Chassis-ID   |             |           | : 1c:98:ec:e3:45:00 |     |                            |     |
| ------------ | ----------- | --------- | ------------------- | --- | -------------------------- | --- |
| System       | Name        |           | : switch            |     |                            |     |
| System       | Description |           | : Aruba             |     | JL375A 8400X XL.01.01.0001 |     |
| Management   | Address     |           | : 192.168.10.1      |     |                            |     |
| Capabilities |             | Available | : Bridge,           |     | Router                     |     |
| Capabilities |             | Enabled   | : Bridge,           |     | Router                     |     |
| TTL          |             |           | : 120               |     |                            |     |
Showingallportsexcept1/1/11andOOBMasadministrativelydown:
220
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- |

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
| Port-ID        |             | :   | 1/1/11    |              |
| -------------- | ----------- | --- | --------- | ------------ |
| Port-Desc      |             | :   | "1/1/11"  |              |
| Port VLAN      | ID          | :   | 100       |              |
| Parent         | Interface   | :   | interface | 1/1/11       |
| Command        | History     |     |           |              |
| Release        |             |     |           | Modification |
| 10.07orearlier |             |     |           | --           |
| Command        | Information |     |           |              |
Devicediscoveryandconfiguration|221

| Platforms |     | Command | context | Authority |     |     |
| --------- | --- | ------- | ------- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
<INTERFACE-NAME>
Specifiestheinterfaceforwhichtoshowinformationfor
neighboringdevices.Usetheformatmember/slot/port(for
example,1/3/1).
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
| switch#  | show | lldp         | neighbor-info | 1/3/1                  |     |     |
| -------- | ---- | ------------ | ------------- | ---------------------- | --- | --- |
| Port     |      |              |               | : 1/1/1                |     |     |
| Neighbor |      | Entries      |               | : 1                    |     |     |
| Neighbor |      | Entries      | Deleted       | : 0                    |     |     |
| Neighbor |      | Entries      | Dropped       | : 0                    |     |     |
| Neighbor |      | Entries      | Aged-Out      | : 0                    |     |     |
| Neighbor |      | Chassis-Name |               | : HP-3800-24G-PoEP-2XG |     |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor |              | Chassis-ID         |           | : 10:60:4b:39:3e:80 |        |     |
| -------- | ------------ | ------------------ | --------- | ------------------- | ------ | --- |
| Neighbor |              | Management-Address |           | : 192.168.1.1       |        |     |
| Chassis  | Capabilities |                    | Available | : Bridge,           | Router |     |
222
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- |

| Chassis  | Capabilities | Enabled   | : Bridge         |     |
| -------- | ------------ | --------- | ---------------- | --- |
| Neighbor | Port-ID      |           | : 1/1/1          |     |
| Neighbor | Port-Desc    |           | : 1/1/1          |     |
| Neighbor | Port         | VLAN ID   | : 1              |     |
| Neighbor | Port         | VLAN Name | : DEFAULT_VLAN_1 |     |
| Neighbor | Port         | MFS       | : 1500           |     |
| TTL      |              |           | : 120            |     |
Showinginformationforinterface1/3/10whentheneighborsendsaDOT3powerTLV:
| switch#  | show lldp    | neighbor-info | 1/3/10              |     |
| -------- | ------------ | ------------- | ------------------- | --- |
| Port     |              |               | : 1/3/10            |     |
| Neighbor | Entries      |               | : 1                 |     |
| Neighbor | Entries      | Deleted       | : 0                 |     |
| Neighbor | Entries      | Dropped       | : 0                 |     |
| Neighbor | Entries      | Aged-Out      | : 0                 |     |
| Neighbor | Chassis-Name |               | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor      | Chassis-ID         |              | : 84:d4:7e:ce:5d:68 |      |
| ------------- | ------------------ | ------------ | ------------------- | ---- |
| Neighbor      | Management-Address |              | : 169.254.41.250    |      |
| Chassis       | Capabilities       | Available    | : Bridge,           | WLAN |
| Chassis       | Capabilities       | Enabled      | : WLAN              |      |
| Neighbor      | Port-ID            |              | : 84:d4:7e:ce:5d:68 |      |
| Neighbor      | Port-Desc          |              | : eth0              |      |
| TTL           |                    |              | : 120               |      |
| Neighbor      | Port               | VLAN ID      | : 1                 |      |
| Neighbor      | Port               | VLAN Name    | : DEFAULT_VLAN_1    |      |
| Neighbor      | Port               | MFS          | : 1500              |      |
| Neighbor      | PoE information    |              | : DOT3              |      |
| Neighbor      | Power              | Type         | : TYPE2             | PD   |
| Neighbor      | Power              | Priority     | : Unkown            |      |
| Neighbor      | Power              | Source       | : Primary           |      |
| PD Requested  | Power              | Value        | : 25.0              | W    |
| PSE Allocated |                    | Power Value: | 25.0 W              |      |
| Neighbor      | Power              | Supported    | : Yes               |      |
| Neighbor      | Power              | Enabled      | : Yes               |      |
| Neighbor      | Power              | Class        | : 5                 |      |
| Neighbor      | Power              | Paircontrol  | : No                |      |
| PSE Power     | Pairs              |              | : Signal            |      |
Showinginformationforinterface1/1/1whenithasmultipleneighbors(displaysamaximumoffour):
| switch#  | show lldp    | neighbor-info | 1/1/1    |     |
| -------- | ------------ | ------------- | -------- | --- |
| Port     |              |               | : 1/1/1  |     |
| Neighbor | Entries      |               | : 4      |     |
| Neighbor | Entries      | Deleted       | : 0      |     |
| Neighbor | Entries      | Dropped       | : 0      |     |
| Neighbor | Entries      | Aged-Out      | : 0      |     |
| Neighbor | Chassis-Name |               | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |           | : 1c:98:ec:fe:25:00 |        |
| -------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor | Management-Address |           | : 10.1.1.2          |        |
| Chassis  | Capabilities       | Available | : Bridge,           | Router |
| Chassis  | Capabilities       | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |           | : 1/1/1             |        |
| Neighbor | Port               | VLAN ID   | : 1                 |        |
| Neighbor | Port               | VLAN Name | : DEFAULT_VLAN_1    |        |
Devicediscoveryandconfiguration|223

| Neighbor Port         | MFS | : 1500   |     |
| --------------------- | --- | -------- | --- |
| TTL                   |     | : 120    |     |
| Neighbor Chassis-Name |     | : switch |     |
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
Showingneighborinformationforinterface1/3/2whenithasEEEenabledandsuccessfullyauto-
negotiated:
| switch# show                 | lldp neighbor-info | 1/3/2               |                        |
| ---------------------------- | ------------------ | ------------------- | ---------------------- |
| Port                         |                    | : 1/3/2             |                        |
| Neighbor Entries             |                    | : 1                 |                        |
| Neighbor Entries             | Deleted            | : 1                 |                        |
| Neighbor Entries             | Dropped            | : 0                 |                        |
| Neighbor Entries             | Aged-Out           | : 1                 |                        |
| Neighbor Chassis-Name        |                    | : BLDG01-F1-6300    |                        |
| Neighbor Chassis-Description |                    | : Aruba             | JL668A FL.10.07.0001BN |
| Neighbor Chassis-ID          |                    | : 88:3a:30:92:a5:c0 |                        |
| Neighbor Management-Address  |                    | : 10.6.9.15         |                        |
| Chassis Capabilities         | Available          | : Bridge,           | Router                 |
| Chassis Capabilities         | Enabled            | : Bridge,           | Router                 |
| Neighbor Port-ID             |                    | : 1/1/1             |                        |
| Neighbor Port-Desc           |                    | : 1/1/1             |                        |
| Neighbor Port                | VLAN ID            | : 1                 |                        |
| Neighbor Port                | VLAN Name          | : DEFAULT_VLAN_1    |                        |
| Neighbor Port                | MFS                | : 1500              |                        |
| TTL                          |                    | : 120               |                        |
224
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Neighbor |     | Mac-Phy  | details   |        |
| -------- | --- | -------- | --------- | ------ |
| Neighbor |     | Auto-neg | Supported | : true |
| Neighbor |     | Auto-Neg | Enabled   | : true |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor       |             | MAU type        |         | : 1000 BASETFD |
| -------------- | ----------- | --------------- | ------- | -------------- |
| Neighbor       |             | EEE information |         | : DOT3         |
| Neighbor       |             | TX Wake         | time    | : 17 us        |
| Neighbor       |             | RX Wake         | time    | : 17 us        |
| Neighbor       |             | Fallback        | time    | : 17 us        |
| Neighbor       |             | TX Echo         | time    | : 17 us        |
| Neighbor       |             | RX Echo         | time    | : 17 us        |
| Command        | History     |                 |         |                |
| Release        |             |                 |         | Modification   |
| 10.07orearlier |             |                 |         | --             |
| Command        | Information |                 |         |                |
| Platforms      |             | Command         | context | Authority      |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     | detail |     |
| --------- | ------------- | --- | ------ | --- |
| show lldp | neighbor-info |     | detail |     |
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
| Port     |     |         |          | : 1/1/1 |
| -------- | --- | ------- | -------- | ------- |
| Neighbor |     | Entries |          | : 1     |
| Neighbor |     | Entries | Deleted  | : 0     |
| Neighbor |     | Entries | Dropped  | : 0     |
| Neighbor |     | Entries | Aged-Out | : 0     |
Devicediscoveryandconfiguration|225

| Neighbor Chassis-Name        |           | : 6300              |        |
| ---------------------------- | --------- | ------------------- | ------ |
| Neighbor Chassis-Description |           | : Aruba             | ...    |
| Neighbor Chassis-ID          |           | : 38:11:17:1a:d5:00 |        |
| Neighbor Management-Address  |           | : 38:11:17:1a:d5:00 |        |
| Chassis Capabilities         | Available | : Bridge,           | Router |
| Chassis Capabilities         | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID             |           | : 1/1/4             |        |
| Neighbor Port-Desc           |           | : 1/1/4             |        |
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
226
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

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
| Command History              |          |                     |     |
| Release                      |          | Modification        |     |
| 10.07orearlier               |          | --                  |     |
| Command Information          |          |                     |     |
Devicediscoveryandconfiguration|227

| Platforms |     | Command | context | Authority |     |
| --------- | --- | ------- | ------- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     | mgmt |     |     |
| --------- | ------------- | --- | ---- | --- | --- |
| show lldp | neighbor-info |     | mgmt |     |     |
Description
DisplaysinformationaboutneighboringdevicesconnectedtotheOOBMinterface.
Examples
ShowingLLDPinformationfortheOOBMinterface:
| switch#  |     | show lldp    | neighbor-info | mgmt                   |     |
| -------- | --- | ------------ | ------------- | ---------------------- | --- |
| Port     |     |              |               | : mgmt                 |     |
| Neighbor |     | Entries      |               | : 1                    |     |
| Neighbor |     | Entries      | Deleted       | : 0                    |     |
| Neighbor |     | Entries      | Dropped       | : 0                    |     |
| Neighbor |     | Entries      | Aged-Out      | : 0                    |     |
| Neighbor |     | Chassis-Name |               | : HP-3800-24G-PoEP-2XG |     |
Neighbor Chassis-Description : HP J9587A 3800-24G-PoE+-2XG Switch, revision...
| Neighbor |     | Chassis-ID         |           | : 10:60:4b:39:3e:80 |        |
| -------- | --- | ------------------ | --------- | ------------------- | ------ |
| Neighbor |     | Management-Address |           | : 192.168.1.1       |        |
| Chassis  |     | Capabilities       | Available | : Bridge,           | Router |
| Chassis  |     | Capabilities       | Enabled   | : Bridge            |        |
| Neighbor |     | Port-ID            |           | : mgmt              |        |
| Neighbor |     | Port-Desc          |           | : mgmt              |        |
| TTL      |     |                    |           | : 120               |        |
ShowingLLDPinformationfortheOOBMinterfacewhentherearefourneighbors:
| switch#  |     | show lldp    | neighbor-info | mgmt     |     |
| -------- | --- | ------------ | ------------- | -------- | --- |
| Port     |     |              |               | : mgmt   |     |
| Neighbor |     | Entries      |               | : 4      |     |
| Neighbor |     | Entries      | Deleted       | : 0      |     |
| Neighbor |     | Entries      | Dropped       | : 0      |     |
| Neighbor |     | Entries      | Aged-Out      | : 0      |     |
| Neighbor |     | Chassis-Name |               | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor |     | Chassis-ID         |           | : 1c:98:ec:fe:25:00 |        |
| -------- | --- | ------------------ | --------- | ------------------- | ------ |
| Neighbor |     | Management-Address |           | : 10.1.1.2          |        |
| Chassis  |     | Capabilities       | Available | : Bridge,           | Router |
| Chassis  |     | Capabilities       | Enabled   | : Bridge,           | Router |
| Neighbor |     | Port-ID            |           | : 1/1/1             |        |
| Neighbor |     | Port-Desc          |           | : 1/1/1             |        |
| TTL      |     |                    |           | : 120               |        |
| Neighbor |     | Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor |     | Chassis-ID         |           | : 1c:98:ec:fe:25:01 |        |
| -------- | --- | ------------------ | --------- | ------------------- | ------ |
| Neighbor |     | Management-Address |           | : 10.1.1.3          |        |
| Chassis  |     | Capabilities       | Available | : Bridge,           | Router |
| Chassis  |     | Capabilities       | Enabled   | : Bridge,           | Router |
228
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- |

| Neighbor | Port-ID      |     | : 1/1/1  |     |
| -------- | ------------ | --- | -------- | --- |
| Neighbor | Port-Desc    |     | : 1/1/1  |     |
| TTL      |              |     | : 120    |     |
| Neighbor | Chassis-Name |     | : switch |     |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |           | : 1c:98:ec:fe:25:02 |        |
| -------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor | Management-Address |           | : 10.1.1.4          |        |
| Chassis  | Capabilities       | Available | : Bridge,           | Router |
| Chassis  | Capabilities       | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |           | : 1/1/1             |        |
| TTL      |                    |           | : 120               |        |
| Neighbor | Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : Aruba JL375A 8400X XL.01.01.0001
| Neighbor       | Chassis-ID         |           | : 1c:98:ec:fe:25:03 |        |
| -------------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor       | Management-Address |           | : 10.1.1.5          |        |
| Chassis        | Capabilities       | Available | : Bridge,           | Router |
| Chassis        | Capabilities       | Enabled   | : Bridge,           | Router |
| Neighbor       | Port-ID            |           | : 1/1/1             |        |
| Neighbor       | Port-Desc          |           | : 1/1/1             |        |
| TTL            |                    |           | : 120               |        |
| Command        | History            |           |                     |        |
| Release        |                    |           | Modification        |        |
| 10.07orearlier |                    |           | --                  |        |
| Command        | Information        |           |                     |        |
| Platforms      | Command            | context   | Authority           |        |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | statistics |                  |     |     |
| --------- | ---------- | ---------------- | --- | --- |
| show lldp | statistics | [<INTERFACE-ID>] |     |     |
Description
ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
| Parameter      |     |     | Description                                   |     |
| -------------- | --- | --- | --------------------------------------------- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |     |
Example
Showingglobalstatisticsforallinterfaces:
Devicediscoveryandconfiguration|229

| switch# |        | show       | lldp | statistics |     |     |     |     |
| ------- | ------ | ---------- | ---- | ---------- | --- | --- | --- | --- |
| LLDP    | Global | Statistics |      |            |     |     |     |     |
======================
| Total | Packets |              | Transmitted |     |           | : 19 |     |     |
| ----- | ------- | ------------ | ----------- | --- | --------- | ---- | --- | --- |
| Total | Packets |              | Received    |     |           | : 19 |     |     |
| Total | Packets |              | Received    | And | Discarded | : 0  |     |     |
| Total | TLVs    | Unrecognized |             |     |           | : 0  |     |     |
| LLDP  | Port    | Statistics   |             |     |           |      |     |     |
====================
| PORT-ID |     |     | TX-PACKETS |     | RX-PACKETS |     | RX-DISCARDED | TLVS-UNKNOWN |
| ------- | --- | --- | ---------- | --- | ---------- | --- | ------------ | ------------ |
-------------------------------------------------------------------------
| 1/1/1 |     |     | 7   |     | 7   |     | 0   | 0   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/1/2 |     |     | 7   |     | 7   |     | 0   | 0   |
| 1/1/3 |     |     | 0   |     | 0   |     | 0   | 0   |
| 1/1/4 |     |     | 0   |     | 0   |     | 0   | 0   |
| 1/1/5 |     |     | 0   |     | 0   |     | 0   | 0   |
...
| mgmt |     |     | 5   |     | 5   |     | 0   | 0   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
```
Showingstatisticsforinterface1/1/1:
| switch# |            | show | lldp | statistics | 1/1/1 |     |     |     |
| ------- | ---------- | ---- | ---- | ---------- | ----- | --- | --- | --- |
| LLDP    | Statistics |      |      |            |       |     |     |     |
===============
| Port           | Name        |             |     |              |     | : 1/1/1      |     |     |
| -------------- | ----------- | ----------- | --- | ------------ | --- | ------------ | --- | --- |
| Packets        |             | Transmitted |     |              |     | : 159        |     |     |
| Packets        |             | Received    |     |              |     | : 163        |     |     |
| Packets        |             | Received    | And | Discarded    |     | : 0          |     |     |
| Packets        |             | Received    | And | Unrecognized |     | : 0          |     |     |
| Command        | History     |             |     |              |     |              |     |     |
| Release        |             |             |     |              |     | Modification |     |     |
| 10.07orearlier |             |             |     |              |     | --           |     |     |
| Command        | Information |             |     |              |     |              |     |     |
| Platforms      |             | Command     |     | context      |     | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | statistics |     | mgmt |     |     |     |     |     |
| --------- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
| show lldp | statistics |     | mgmt |     |     |     |     |     |
Description
ShowsLLDPstatisticsfortheOOBMinterface.
230
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

Example
ShowingLLDPstatisticsfortheOOBMinterface:
switch#
|     | show lldp | statistics | mgmt |
| --- | --------- | ---------- | ---- |
LLDP Statistics
===============
| Port           | Name        |                  | : mgmt       |
| -------------- | ----------- | ---------------- | ------------ |
| Packets        | Transmitted |                  | : 20         |
| Packets        | Received    |                  | : 23         |
| Packets        | Received    | And Discarded    | : 0          |
| Packets        | Received    | And Unrecognized | : 0          |
| Command        | History     |                  |              |
| Release        |             |                  | Modification |
| 10.07orearlier |             |                  | --           |
| Command        | Information |                  |              |
| Platforms      | Command     | context          | Authority    |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | tlv |     |     |
| --------- | --- | --- | --- |
| show lldp | tlv |     |     |
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
| System | Capabilities |     |     |
| ------ | ------------ | --- | --- |
| System | Description  |     |     |
| System | Name         |     |     |
VLAN Name
MFS
OUI
| Command | History |     |     |
| ------- | ------- | --- | --- |
Devicediscoveryandconfiguration|231

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

232

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
| switch(config)#    | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
| switch(config-if)# |           | cdp   |     |
DisablingCDPoninterface1/1/1:
| switch(config)#     | interface | 1/1/1   |              |
| ------------------- | --------- | ------- | ------------ |
| switch(config-if)#  |           | no cdp  |              |
| Command History     |           |         |              |
| Release             |           |         | Modification |
| 10.07orearlier      |           |         | --           |
| Command Information |           |         |              |
| Platforms           | Command   | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|                    | config-if |     | forthiscommand. |
| ------------------ | --------- | --- | --------------- |
| clear cdp counters |           |     |                 |
| clear cdp counters |           |     |                 |
Devicediscoveryandconfiguration|233

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
| switch(config)      | clear   | neighbor-info |              |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show cdp
show cdp
234
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
| Parameter      |     |     | Description                                   |
| -------------- | --- | --- | --------------------------------------------- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port. |
Examples
ShowingallCDPneighborinformation:
Devicediscoveryandconfiguration|235

| switch(config)# |        | show | cdp neighbor-info |     |          |            |     |
| --------------- | ------ | ---- | ----------------- | --- | -------- | ---------- | --- |
| Port            | Device |      | ID                |     | Platform | Capability |     |
-------------------------------------------------------------------------------
| 1/1/1 | myswitch |     |     |     | cisco WS-C2950-12 | SI  |     |
| ----- | -------- | --- | --- | --- | ----------------- | --- | --- |
ShowingCDPinformationforinterface1/1/1:
| switch(config)# |             | show  | cdp neighbor-info   |          | 1/1/1        |     |     |
| --------------- | ----------- | ----- | ------------------- | -------- | ------------ | --- | --- |
| Local Port      | :           | 1/1/1 |                     |          |              |     |     |
| MAC             |             |       | : 3c:a8:2a:7b:6b:2b |          |              |     |     |
| Device ID       |             |       | : SEPd4adbd2a30d6   |          |              |     |     |
| Address         |             |       | : 2.71.0.230        |          |              |     |     |
| Platform        |             |       | : Cisco             | IP Phone | 3905         |     |     |
| Duplex          |             |       | : full              |          |              |     |     |
| Capability      |             |       | : host              |          |              |     |     |
| Voice VLAN      | Support     |       | : Yes               |          |              |     |     |
| Neighbor        | Port-ID     |       | : Port 1            |          |              |     |     |
| Command         | History     |       |                     |          |              |     |     |
| Release         |             |       |                     |          | Modification |     |     |
| 10.07orearlier  |             |       |                     |          | --           |     |     |
| Command         | Information |       |                     |          |              |     |     |
| Platforms       | Command     |       | context             |          | Authority    |     |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show cdp traffic       |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| show cdp neighbor-info |     |     |     |     |     |     |     |
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
| 1/1/1   |         | 0   |     |     | 4   | 0   |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
| 1/1/2   |         | 0   |     |     | 0   | 0   |     |
| 1/1/3   |         | 0   |     |     | 2   | 0   |     |
| 1/1/4   |         | 0   |     |     | 0   | 0   |     |
| 1/1/5   |         | 0   |     |     | 0   | 0   |     |
| Command | History |     |     |     |     |     |     |
236
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Devicediscoveryandconfiguration|237

Chapter 15

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

238

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

Switches support provisioning through a network connected to a data port or through a network
connected to the management port.

3. Publish the configuration files and image files to the TFTP server. You need to know the locations
of the files and the IP address of the TFTP server when you set up the vendor class options on the
DHCP server.

4. On the DHCP server, set up vendor classes for each switch model you plan to provision. To do

this you need the following information:

Zero Touch Provisioning | 239

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

On switches that support ZTP operations on data ports, the switch also sends out a DHCP
discovery from all data ports in the default VLAN.

The switch waits to receive DHCP options indefinitely or until the running configuration is
modified. If a DHCP IP address is received but no DHCP options are received, the switch waits an
additional minute before ending the ZTP operation.

On switches that support ZTP operations on data ports, DHCP options received on the
management port have priority over DHCP options received on data ports:

n If DHCP options are received on the management port before being received on a data port,

the switch processes those options immediately.

n If DHCP options are received on a data port, the switch waits an additional 30 seconds for
options to be received on the management port. If no DHCP options are received on the
management port during those 30 seconds, the switch processes the DHCP options it received
on the data port.

After the ZTP operation ends, there is no automatic retry. You can either attempt to boot the
switch with the factory default configuration again, configure the switch at the installation site, or
use the ZTP force-provision CLI to trigger the ZTP process, ignoring the present running
configuration of the switch.

n Once force-provision is enabled, new DHCP requests are sent from the switch. Disabling force-

provision does not stop the DHCP already in progress, but only changes the switch

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

240

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

Zero Touch Provisioning | 241

Shows information about Zero Touch Provisioning (ZTP) operations performed on the switch.

Usage

When a switch configured to use ZTP is booted from a factory default configuration, the switch contacts
a DHCP server, which offers options for obtaining files used to provision the switch:

n The IP address of the TFTP server

n The name of the image file

n The name of the configuration file

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

Examples

Showing switch image download in progress after receiving ZTP options:

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

242

| switch#         | show ztp information |                                |         |          |                  |
| --------------- | -------------------- | ------------------------------ | ------- | -------- | ---------------- |
| TFTP Server     |                      | : 10.0.0.2                     |         |          |                  |
| Image File      |                      | : TL_10_02_0001.swi            |         |          |                  |
| Configuration   | File                 | : config_file                  |         |          |                  |
| ZTP Status      |                      | : In-progress                  | - Image | download | and verification |
| Aruba Central   | Location             | : secure.arubanetworks.com     |         |          |                  |
| Aruba Central   | Shared Token         | : aruba123                     |         |          |                  |
| Force-Provision |                      | : Disabled                     |         |          |                  |
| HTTP Proxy      | Location             | : http.proxy.arubanetworks.com |         |          |                  |
ShowingswitchimagedownloadfailureafterreceivingZTPoptions:
switch#
show ztp information
| TFTP Server     |              | : 10.0.0.2                     |          |             |       |
| --------------- | ------------ | ------------------------------ | -------- | ----------- | ----- |
| Image File      |              | : TL_10_02_0001.swi            |          |             |       |
| Configuration   | File         | : config_file                  |          |             |       |
| ZTP Status      |              | : Failed                       | - Unable | to download | image |
| Aruba Central   | Location     | : secure.arubanetworks.com     |          |             |       |
| Aruba Central   | Shared Token | : aruba123                     |          |             |       |
| Force-Provision |              | : Disabled                     |          |             |       |
| HTTP Proxy      | Location     | : http.proxy.arubanetworks.com |          |             |       |
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
Showingswitchfailuretoupdatestart-upconfrigurationafterdownloadingconfigurationreceivedfrom
ZTPoptions:
switch#
show ztp information
| TFTP Server   |      | : 10.0.0.2          |     |     |     |
| ------------- | ---- | ------------------- | --- | --- | --- |
| Image File    |      | : TL_10_02_0001.swi |     |     |     |
| Configuration | File | : config_file       |     |     |     |
ZTP Status : Failed - Could not copy to start-up configuration
| Aruba Central | Location | : secure.arubanetworks.com |     |     |     |
| ------------- | -------- | -------------------------- | --- | --- | --- |
ZeroTouchProvisioning|243

| Aruba Central   | Shared Token | : aruba123                     |     |     |
| --------------- | ------------ | ------------------------------ | --- | --- |
| Force-Provision |              | : Disabled                     |     |     |
| HTTP Proxy      | Location     | : http.proxy.arubanetworks.com |     |     |
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
| VSF-10-Mbr##  | show ztp information |      |     |     |
| ------------- | -------------------- | ---- | --- | --- |
| TFTP Server   |                      | : NA |     |     |
| Image File    |                      | : NA |     |     |
| Configuration | File                 | : NA |     |     |
Status : Failed - Timed out while waiting to receive ZTP options
244
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Aruba Central   | Location |       | : NA       |     |     |     |
| --------------- | -------- | ----- | ---------- | --- | --- | --- |
| Aruba Central   | Shared   | Token | : NA       |     |     |     |
| Force-Provision |          |       | : Disabled |     |     |     |
| HTTP Proxy      | Location |       | : NA       |     |     |     |
VSF-10-Mbr#
Inthefollowingexample,theZTPoperationwasstoppedbecausetheswitchwasbootedfroma
configurationthatwasnotthefactorydefaultconfiguration.
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
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
switch#
configure terminal
| switch(config)# | ztp | force-provision |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- |
ZeroTouchProvisioning|245

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
246
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

Chapter 16
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
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| bluetooth        | enable |     |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- | --- |
| bluetooth enable |        |     |     |     |     |     |
| no bluetooth     | enable |     |     |     |     |     |
Description
247
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- | --- |

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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 27 |
| ----------- | ------------- | ---------- | ----- |
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to
36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
Switchsystemandhardwarecommands|248

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
switch#
show ip errors
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
249
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
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
| switch(config)# |             | no      | console | baud-rate |                   |     |
| --------------- | ----------- | ------- | ------- | --------- | ----------------- | --- |
| Command         | History     |         |         |           |                   |     |
| Release         |             |         |         |           | Modification      |     |
| 10.08           |             |         |         |           | Commandintroduced |     |
| Command         | Information |         |         |           |                   |     |
| Platforms       |             | Command | context |           | Authority         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Switchsystemandhardwarecommands|250

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
hostname
| hostname <HOSTNAME> |              |     |     |
| ------------------- | ------------ | --- | --- |
| no hostname         | [<HOSTNAME>] |     |     |
Description
251
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
| switch#         | config   |          |     |
| --------------- | -------- | -------- | --- |
| switch(config)# | hostname | myswitch |     |
myswitch(config)#
|     |     | show hostname |     |
| --- | --- | ------------- | --- |
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
mtrace
mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
[vrf <VRF-NAME>]
Description
TracesthespecifiedIPv4sourceandgroupaddresses.
| Parameter     |     |     | Description                           |
| ------------- | --- | --- | ------------------------------------- |
| IPV4-SRC-ADDR |     |     | SpecifiesthesourceIPv4addresstotrace. |
Switchsystemandhardwarecommands|252

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
| -1 30.0.0.1    | PIM         | 0 ms |     |     |              |     |     |
| -------------- | ----------- | ---- | --- | --- | ------------ | --- | --- |
| -2 40.0.0.1    | PIM         | 2 ms |     |     |              |     |     |
| -3 50.0.0.1    | PIM         | 100  | ms  |     |              |     |     |
| -4 60.0.0.1    | PIM         | 156  | ms  |     |              |     |     |
| -5 200.0.0.1   | PIM         | 123  | ms  |     |              |     |     |
| Command        | History     |      |     |     |              |     |     |
| Release        |             |      |     |     | Modification |     |     |
| 10.07orearlier |             |      |     |     | --           |     |     |
| Command        | Information |      |     |     |              |     |     |
253
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
6200 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show bluetooth
show bluetooth
Description
ShowsgeneralstatusinformationabouttheBluetoothwirelessmanagementfeatureontheswitch.
Usage
Thiscommandshowsstatusinformationaboutthefollowing:
n TheUSBBluetoothadapter
ClientsconnectedusingBluetooth
n
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
Switchsystemandhardwarecommands|254

| switch#        | show bluetooth |                       |              |
| -------------- | -------------- | --------------------- | ------------ |
| Enabled        |                | : No                  |              |
| Device         | name           | : <XXXX>-<NNNNNNNNNN> |              |
| Command        | History        |                       |              |
| Release        |                |                       | Modification |
| 10.07orearlier |                |                       | --           |
| Command        | Information    |                       |              |
| Platforms      | Command        | context               | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
all
Showsbootinformationfortheactivemanagementmoduleand
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
255
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

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
Switchsystemandhardwarecommands|256

| Release        |             |         | Modification |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show capacities
| show capacities | <FEATURE> |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<FEATURE>
Specifiesafeature.Forexample,aaa.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring        |     |     |       |
| ------------------ | --------------- | ---------------- | --- | --- | ----- |
| System Capacities: |                 | Filter Mirroring |     |     |       |
| Capacities         | Name            |                  |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | Mirror Sessions | configurable | in a system |     |
| ------- | --------- | --------------- | ------------ | ----------- | --- |
4
| Maximum | number of | enabled Mirror | Sessions | in a system |     |
| ------- | --------- | -------------- | -------- | ----------- | --- |
4
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp        |     |     |       |
| ------------------ | --------------- | ----------- | --- | --- | ----- |
| System Capacities: |                 | Filter MSTP |     |     |       |
| Capacities         | Name            |             |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | mstp instances | configurable | in a system |     |
| ------- | --------- | -------------- | ------------ | ----------- | --- |
64
257
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

ShowingallavailablecapacitiesforVLANcount:
| switch#    | show        | capacities | vlan-count  |       |     |     |       |
| ---------- | ----------- | ---------- | ----------- | ----- | --- | --- | ----- |
| System     | Capacities: |            | Filter VLAN | Count |     |     |       |
| Capacities | Name        |            |             |       |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number | of  | VLANs supported | in  | the system |     |     |
| ------- | ------ | --- | --------------- | --- | ---------- | --- | --- |
4094
| Command        | History     |         |         |              |     |     |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         |         | Modification |     |     |     |
| 10.07orearlier |             |         |         | --           |     |     |     |
| Command        | Information |         |         |              |     |     |     |
| Platforms      |             | Command | context | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show capacities-status
| show capacities-status |     |     | <FEATURE> |     |     |     |     |
| ---------------------- | --- | --- | --------- | --- | --- | --- | --- |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<FEATURE>
Specifiesthefeature,forexampleaaaforwhichtodisplay
capacities,values,andstatus.Required.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
| switch#    | show       | capacities-status |        |     |     |               |     |
| ---------- | ---------- | ----------------- | ------ | --- | --- | ------------- | --- |
| System     | Capacities |                   | Status |     |     |               |     |
| Capacities | Status     |                   | Name   |     |     | Value Maximum |     |
------------------------------------------------------------------------------
| Number | of active          | gateway | mac        | addresses | in a system | 0 16 |     |
| ------ | ------------------ | ------- | ---------- | --------- | ----------- | ---- | --- |
| Number | of aspath-lists    |         | configured |           |             | 0 64 |     |
| Number | of community-lists |         | configured |           |             | 0 64 |     |
...
| Command | History |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
Switchsystemandhardwarecommands|258

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Showingtheconsoleportcurrentspeed:
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
259
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

Parameter Description
all Showsallavailablecoredumps.
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
Instance ID
IdentifiesthespecificinstanceofthedaemonshownintheDaemon Namecolumn.
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
| hpe-sysmond | 513  | Yes | 2017-07-31 | 13:58:05 | e70f101 |
| ----------- | ---- | --- | ---------- | -------- | ------- |
| hpe-tempd   | 1048 | Yes | 2017-08-13 | 13:31:53 | e70f101 |
| hpe-tempd   | 1052 | Yes | 2017-08-13 | 13:41:44 | e70f101 |
Switchsystemandhardwarecommands|260

| Line Module | core-dumps |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- |
=============================================================================
| Line Module | : 1/1 |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- |
=============================================================================
| dune_agent_0 |     | 18958 | Yes | 2017-08-12 | 11:50:17 | e70f101 |
| ------------ | --- | ----- | --- | ---------- | -------- | ------- |
| dune_agent_0 |     | 18842 | Yes | 2017-08-12 | 11:50:09 | e70f101 |
=============================================================================
| Total number | of core | dumps : | 5   |     |     |     |
| ------------ | ------- | ------- | --- | --- | --- | --- |
=============================================================================
| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
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
| switch#         | show domain-name |             |     |     |     |     |
| --------------- | ---------------- | ----------- | --- | --- | --- | --- |
| switch#         | config           |             |     |     |     |     |
| switch(config)# | domain-name      | example.com |     |     |     |     |
| switch(config)# | show             | domain-name |     |     |     |     |
example.com
switch(config)#
| Command History     |     |     |              |     |     |     |
| ------------------- | --- | --- | ------------ | --- | --- | --- |
| Release             |     |     | Modification |     |     |     |
| 10.07orearlier      |     |     | --           |     |     |     |
| Command Information |     |     |              |     |     |     |
261
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- | --- |

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

show environment fan
show environment fan [vsf]

Description

Shows the status information for all fans and fan trays (if present) in the system.

Parameter

vsf

Usage

Description

Shows output from the VSF member-id on switches that
support VSF.

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

Switch system and hardware commands | 262

Thefanisoperatingnormally.
fault
Thefanisinafaultstate.
empty
Thefanisnotinstalled.
Examples
Showingoutputforasystemwithoutafantray:
| switch# | show environment | fan |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
Fan information
---------------------------------------------------------------
| Fan Serial | Number | Speed Direction |     | Status | RPM |
| ---------- | ------ | --------------- | --- | ------ | --- |
---------------------------------------------------------------
| 1 SGXXXXXXXXXX |     | slow front-to-back   |     | ok    | 6000  |
| -------------- | --- | -------------------- | --- | ----- | ----- |
| 2 SGXXXXXXXXXX |     | normal front-to-back |     | ok    | 8000  |
| 3 SGXXXXXXXXXX |     | medium front-to-back |     | ok    | 11000 |
| 4 SGXXXXXXXXXX |     | fast front-to-back   |     | ok    | 14000 |
| 5 SGXXXXXXXXXX |     | max front-to-back    |     | fault | 16500 |
| 6 N/A          |     | N/A N/A              |     | empty |       |
...
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |     | led         |     |     |     |
| ---------------- | --- | ----------- | --- | --- | --- |
| show environment | led | <MEMBER-ID> |     |     |     |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<MEMBER-ID>
ShowsoutputfromthespecifiedVSFmemberID on
switchesthatsupportVSF.
Example
ShowingstateandstatusforLED:
263
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- |

| switch#  | show environment | led    |     |
| -------- | ---------------- | ------ | --- |
| Mbr/Name | State            | Status |     |
-------------------------------
| 1/locator           | off     | ok      |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show environment |              | power-supply |     |
| ---------------- | ------------ | ------------ | --- |
| show environment | power-supply | [vsf]        |     |
Description
Showsstatusinformationaboutallpowersuppliesintheswitch.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| vsf       |     |     | ShowsoutputfromtheVSFmember-idonswitchesthatsupport |
VSF.
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
Switchsystemandhardwarecommands|264

| Output | fault |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
Thepowersupplyhasafaultconditiononitsoutput.
Warning
Thepowersupplyisnotoperatingnormally.
| Wattage Maximum |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Showsthemaximumamountofwattagethatthepowersupplycanprovide.
Example
Showingtheoutputwhenonlyonepowersupplyisinstalledintheswitch:
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
| show environment |             |     | temperature |       |     |
| ---------------- | ----------- | --- | ----------- | ----- | --- |
| show environment | temperature |     | [detail]    | [vsf] |     |
Description
Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
| Parameter |     |     |     | Description                                         |     |
| --------- | --- | --- | --- | --------------------------------------------------- | --- |
| detail    |     |     |     | Showsdetailedinformationfromeachtemperaturesensor.  |     |
| vsf       |     |     |     | ShowsoutputfromtheVSFmember-idonswitchesthatsupport |     |
VSF
Usage
TemperaturesareshowninCelsius.
Validvaluesforstatusarethefollowing:
normal
Sensoriswithinnominaltemperaturerange.
min
Lowesttemperaturefromthissensor.
max
265
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- |

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
Showingdetailedtemperatureinformationfora6200switch:
| switch#     | show environment | temperature |     |     |     |
| ----------- | ---------------- | ----------- | --- | --- | --- |
| Temperature | information      |             |     |     |     |
------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     |     | Module Type | temperature | Status |
| --------------- | --- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-PHY-01-08            |             |         | line-card-module  | 51.00 C | normal |
| ------------------------ | ----------- | ------- | ----------------- | ------- | ------ |
| 1/1-PHY-09-16            |             |         | line-card-module  | 48.00 C | normal |
| 1/1-PHY-17-24            |             |         | line-card-module  | 50.00 C | normal |
| 1/1-PHY-25-32            |             |         | line-card-module  | 52.00 C | normal |
| 1/1-PHY-33-40            |             |         | line-card-module  | 53.00 C | normal |
| 1/1-PHY-41-48            |             |         | line-card-module  | 54.00 C | normal |
| 1/1-Switch-ASIC-Internal |             |         | line-card-module  | 63.25 C | normal |
| 1/1-CPU                  |             |         | management-module | 47.56 C | normal |
| 1/1-CPU-Zone-0           |             |         | management-module | 46.00 C | normal |
| 1/1-CPU-Zone-1           |             |         | management-module | 46.00 C | normal |
| 1/1-CPU-Zone-2           |             |         | management-module | 46.00 C | normal |
| 1/1-CPU-Zone-3           |             |         | management-module | 47.00 C | normal |
| 1/1-CPU-Zone-4           |             |         | management-module | 47.00 C | normal |
| 1/1-DDR                  |             |         | management-module | 37.75 C | normal |
| 1/1-DDR-Inlet            |             |         | management-module | 30.69 C | normal |
| 1/1-Inlet-Air            |             |         | management-module | 22.00 C | normal |
| 1/1-Switch-ASIC-Remote   |             |         | management-module | 64.06 C | normal |
| Command                  | History     |         |                   |         |        |
| Release                  |             |         | Modification      |         |        |
| 10.07orearlier           |             |         | --                |         |        |
| Command                  | Information |         |                   |         |        |
| Platforms                | Command     | context | Authority         |         |        |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show        | events          |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- |
| show events | [ -e <EVENT-ID> | |   |     |     |     |
-s {emergency | alert | critical | error | warning | notice | info | debug} |
-r |
Switchsystemandhardwarecommands|266

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
| -n <COUNT> |     |     | Displaysthespecifiednumberofeventlogs. |
| ---------- | --- | --- | -------------------------------------- |
-i <MEMBER-SLOT> Ona6200:ShowstheeventlogsforthespecifiedVSFmember
ID.
-m {active | standby} Ona6200:Showstheeventlogsforthespecifiedrole.
SelectingactivedisplaystheeventlogfortheVSFconductor
roleandstandbydisplayseventlogsfortheVSFstandbyrole.
-c {lldp | ospf | ...} Showstheeventlogsforthespecifiedeventcategory.Enter
show event -cforafulllistingofsupportedcategorieswith
descriptions.
-d {lldpd | bgpd | fand | ...} Showstheeventlogsforthespecifiedprocess.Entershow
event -dforafulllistingofsupporteddaemonswith
descriptions.
Examples
Showingeventlogs:
267
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

| switch# show | events |     |     |
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
Showingthemostrecenteventlogsfirst:
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
Switchsystemandhardwarecommands|268

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
show hostname
Description
Showsthecurrenthostname.
Example
Settingandshowingthehostname:
269
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

| switch# | show hostname |     |     |
| ------- | ------------- | --- | --- |
switch
| switch#           | config   |               |     |
| ----------------- | -------- | ------------- | --- |
| switch(config)#   | hostname | myswitch      |     |
| myswitch(config)# |          | show hostname |     |
myswitch
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show images
show images
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
Example
Showingtheprimaryandsecondaryimagesona6200switch:
| switch(config)# | show | images |     |
| --------------- | ---- | ------ | --- |
---------------------------------------------------------------------------
| AOS-CX | Primary Image |     |     |
| ------ | ------------- | --- | --- |
---------------------------------------------------------------------------
| Version | : ML.10.06.0001AAE-54-g89a7618 |              |     |
| ------- | ------------------------------ | ------------ | --- |
| Size    | : 446 MB                       |              |     |
| Date    | : 2020-04-27                   | 16:50:39 PDT |     |
SHA-256 : 2e6261e26591f9a6b94be28b0890de521f0869a9dbc378659fc33d7c40fd12fc
---------------------------------------------------------------------------
| AOS-CX | Secondary Image |     |     |
| ------ | --------------- | --- | --- |
---------------------------------------------------------------------------
| Version | : ML.10.06.0001AAE-54-g89a7618 |              |     |
| ------- | ------------------------------ | ------------ | --- |
| Size    | : 446 MB                       |              |     |
| Date    | : 2020-04-27                   | 16:50:39 PDT |     |
SHA-256 : 2e6261e26591f9a6b94be28b0890de521f0869a9dbc378659fc33d7c40fd12fc
| Default | Image : primary |     |     |
| ------- | --------------- | --- | --- |
------------------------------------------------------
| Management | Module | 1/1 (Active) |     |
| ---------- | ------ | ------------ | --- |
------------------------------------------------------
| Active | Image | : primary |     |
| ------ | ----- | --------- | --- |
Switchsystemandhardwarecommands|270

| Service        | OS Version  | : ML.01.05.0001-internal |              |
| -------------- | ----------- | ------------------------ | ------------ |
| BIOS Version   |             | : FL.01.0003             |              |
| Command        | History     |                          |              |
| Release        |             |                          | Modification |
| 10.07orearlier |             |                          | --           |
| Command        | Information |                          |              |
| Platforms      | Command     | context                  | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show ip | errors |     |     |
| ------- | ------ | --- | --- |
show ip errors
Description
ShowsIPerrorstatisticsforpacketsreceivedbytheswitchsincetheswitchwaslastbooted.
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
o TheforwardingheaderofanIPv6addressisempty.
o ThereisnosourceIPaddressforanIPv6packet.
| n Invalid | TTLs |     |     |
| --------- | ---- | --- | --- |
TheTTL(timetolive)valueofthepacketreachedzero.Thepacketwasdiscardedbecauseittraversedthe
maximumnumberofhopspermittedbytheTTLvalue.
TTLsareusedtopreventpacketsfrombeingcirculatedonthenetworkendlessly.
Example
Showingiperrorstatisticsforpacketsreceivedbytheswitch:
271
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |
| ----------------------------- | --- | ------------------ | --- |

| switch# | show ip errors |     |     |
| ------- | -------------- | --- | --- |
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
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show module
show module
Description
Showsinformationaboutinstalledlinemodulesandmanagementmodules.
Althoughthisswitchdoesnothaveremovablemodules,thiscommandwillstillreturninformationaboutthe
switch,referringtomanagementmodulesandlinemodules.
Usage
Identifiesandshowsstatusinformationaboutthelinemodulesandmanagementmodulesthatare
installedintheswitch.
Toshowtheconfigurationinformation—ifany—associatedwiththatlinemoduleslot,usetheshow
running-configurationcommand.
Statusisoneofthefollowingvalues:
Active
Thisswitchistheactivemanagementmodule.
Standby
Thisswitchisthestandbymanagementmodule.
Deinitializing
Theswitchisbeingdeinitialized.
Diagnostic
Theswitchisinastateusedfortroubleshooting.
Down
Theswitchisphysicallypresentbutispowereddown.
Empty
Theswitchhardwareisnotinstalledinthechassis.
Failed
Switchsystemandhardwarecommands|272

Theswitchhasexperiencedanerrorandfailed.
Failover
Thisswitchisafabricmoduleoralinemodule,anditisintheprocessofconnectingtothenew
activemanagementmoduleduringamanagementmodulefailoverevent.
Initializing
Theswitchisbeinginitialized.
Present
Theswitchhardwareisinstalledinthechassis.
Ready
Theswitchisavailableforuse.
Updating
Afirmwareupdateisbeingappliedtotheswitch.
Examples
Showingallinstalledmodules:
| switch#    | show module |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
| Management | Modules     |     |     |     |     |     |
==================
| Product     |             |     |     |     | Serial |        |
| ----------- | ----------- | --- | --- | --- | ------ | ------ |
| Name Number | Description |     |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
1/1 JL727A 6200F 48G CL4 4SFP+370W Swch SG0ZKW600P Active (local)
| Line Modules |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
============
| Product     |             |     |     |     | Serial |        |
| ----------- | ----------- | --- | --- | --- | ------ | ------ |
| Name Number | Description |     |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL727A          | 6200F   | 48G CL4 | 4SFP+370W | Swch         | SG0ZKW600P | Ready |
| ------------------- | ------- | ------- | --------- | ------------ | ---------- | ----- |
| Command History     |         |         |           |              |            |       |
| Release             |         |         |           | Modification |            |       |
| 10.07orearlier      |         |         |           | --           |            |       |
| Command Information |         |         |           |              |            |       |
| Platforms           | Command | context |           | Authority    |            |       |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |             |     |       |     |     |     |
| ------------------- | ----------- | --- | ----- | --- | --- | --- |
| show running-config | [<FEATURE>] |     | [all] |     |     |     |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
273
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- | --- | --- |

| Parameter |     | Description |
| --------- | --- | ----------- |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).
| all |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |
| --- | --- | ------------------------------------------------------- |
Examples
Showingthecurrentrunningconfiguration:
| switch> show | running-config |     |
| ------------ | -------------- | --- |
Current configuration:
!
| !Version AOS-CX | 10.0X.XXXX |     |
| --------------- | ---------- | --- |
!
lldp enable
| linecard-module | LC1 part-number | JL363A |
| --------------- | --------------- | ------ |
vrf default
!
!
!
!
!
!
| aaa authentication | login default    | local |
| ------------------ | ---------------- | ----- |
| aaa authorization  | commands default | none  |
!
!
!
!
| router ospf 1  | vrf green |     |
| -------------- | --------- | --- |
| area 0.0.0.0   |           |     |
| router pim vrf | green     |     |
enable
| rp-address | 30.0.0.4 |     |
| ---------- | -------- | --- |
vlan 1
no shutdown
vlan 20
no shutdown
vlan 30
no shutdown
| interface 1/1/1 |     |     |
| --------------- | --- | --- |
no shutdown
no routing
| vlan access      | 30  |     |
| ---------------- | --- | --- |
| interface 1/1/32 |     |     |
no shutdown
no routing
| vlan access               | 20  |     |
| ------------------------- | --- | --- |
| interface bridge_normal-1 |     |     |
no shutdown
| interface bridge_normal-2 |     |     |
| ------------------------- | --- | --- |
no shutdown
| interface vlan20 |     |     |
| ---------------- | --- | --- |
no shutdown
| vrf attach    | green        |     |
| ------------- | ------------ | --- |
| ip address    | 20.0.0.44/24 |     |
| ip ospf 1     | area 0.0.0.0 |     |
| ip pim-sparse | enable       |     |
Switchsystemandhardwarecommands|274

| interface vlan30 |     |     |
| ---------------- | --- | --- |
no shutdown
| vrf attach    | green          |     |
| ------------- | -------------- | --- |
| ip address    | 30.0.0.44/24   |     |
| ip ospf 1     | area 0.0.0.0   |     |
| ip pim-sparse | enable         |     |
| ip pim-sparse | hello-interval | 100 |
Showingthecurrentrunningconfigurationinjsonformat:
switch>
| show                  | running-config json |     |
| --------------------- | ------------------- | --- |
| Running-configuration | in JSON:            |     |
{
| "Monitoring_Policy_Script": |     | {   |
| --------------------------- | --- | --- |
"system_resource_monitor_mm1.1.0": {
"Monitoring_Policy_Instance": {
"system_resource_monitor_mm1.1.0/system_resource_monitor_
| mm1.1.0.default": | {                                                  |           |
| ----------------- | -------------------------------------------------- | --------- |
|                   | "name": "system_resource_monitor_mm1.1.0.default", |           |
|                   | "origin":                                          | "system", |
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
Showthecurrentrunningconfigurationwithoutdefaultvalues:
| switch(config)# | show running-config |     |
| --------------- | ------------------- | --- |
Current configuration:
!
| !Version AOS-CX | Virtual.10.04.0000-6523-gbb15c03~dirty |     |
| --------------- | -------------------------------------- | --- |
| led locator on  |                                        |     |
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
| switch(config)# | show running-config | all |
| --------------- | ------------------- | --- |
Current configuration:
275
AOS-CX10.11FundamentalsGuide| (6200SwitchSeries)

!
| !Version    | AOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| led locator | on                                            |     |     |
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
Showthecurrentrunningconfigurationwithdefaultvalues:
| switch(config)#        | snmp-server | vrf mgmt       |     |
| ---------------------- | ----------- | -------------- | --- |
| switch(config)#        | show        | running-config |     |
| Current configuration: |             |                |     |
!
| !Version | Virtual.10.04.0000-6523-gbb15c03~dirty |     |     |
| -------- | -------------------------------------- | --- | --- |
AOS-CX
| led locator | on  |     |     |
| ----------- | --- | --- | --- |
!
!
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
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Switchsystemandhardwarecommands|276

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show running-config |                 | current-context |     |     |
| ------------------- | --------------- | --------------- | --- | --- |
| show running-config | current-context |                 |     |     |
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
| switch(config-if)# |         | show running-config | current-context |     |
| ------------------ | ------- | ------------------- | --------------- | --- |
| interface          | 1/1/1   |                     |                 |     |
| no shutdown        |         |                     |                 |     |
| description        | Example | interface           |                 |     |
| vlan access        | 1       |                     |                 |     |
exit
Showingthecurrentrunningconfigurationforthemanagementinterface:
| switch(config-if-mgmt)# |             | show running-config |     | current-context |
| ----------------------- | ----------- | ------------------- | --- | --------------- |
| interface               | mgmt        |                     |     |                 |
| no shutdown             |             |                     |     |                 |
| ip static               | 10.0.0.1/24 |                     |     |                 |
| default-gateway         |             | 10.0.0.8            |     |                 |
| nameserver              | 10.0.0.1    |                     |     |                 |
Showingtherunningconfigurationfortheexternalstoragesharenamednasfiles:
277
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |

switch(config-external-storage-nasfiles)# show running-config current-context
| external-storage | nasfiles    |     |     |
| ---------------- | ----------- | --- | --- |
| address          | 192.168.0.1 |     |     |
| vrf default      |             |     |     |
| username         | nasuser     |     |     |
| password         | ciphertext  |     |     |
AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
| type      | scp       |     |     |
| --------- | --------- | --- | --- |
| directory | /home/nas |     |     |
enable
switch(config-external-storage-nasfiles)#
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
configorachildof
forthiscommand.
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
Showingthestartup-configurationinnon-JSONformatfora6200switch:
| switch# | show startup-config |     |     |
| ------- | ------------------- | --- | --- |
| Startup | configuration:      |     |     |
!
| !Version | ML.10.05.0001L |     |     |
| -------- | -------------- | --- | --- |
AOS-CX
| !export-password: |     | default |     |
| ----------------- | --- | ------- | --- |
no lldp
| user admin | group administrators |     | password ciphertext |
| ---------- | -------------------- | --- | ------------------- |
AQBapeGVVYk45m4sYxZDE6ufzB2CWmH2wDncy5Can9iEFZjmYgAAAMl31OWIxExNwi3xahHktOL681amYg
Switchsystemandhardwarecommands|278

/yg2ezRrlbMUtlU7fVlASiVbmIq8gVUj01Q4STp9/su3pnopopuWPxwk765zqofKyhL0E0Gj9yhoxCeZfy
NeNpNbm6upKjC5LrfZt9
cli-session
| timeout | 0   |     |     |
| ------- | --- | --- | --- |
!
!
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
show system
Description
Showsgeneralstatusinformationaboutthesystem.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemContact,SystemLocation,andSystemDescriptioncanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformation:
| switch(config)# | show | system   |     |
| --------------- | ---- | -------- | --- |
| Hostname        |      | : switch |     |
279
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| System         | Description | : ML.10.xx.xxxxx |              |            |             |     |     |
| -------------- | ----------- | ---------------- | ------------ | ---------- | ----------- | --- | --- |
| System         | Contact     | :                |              |            |             |     |     |
| System         | Location    | :                |              |            |             |     |     |
| Vendor         |             | : Aruba          |              |            |             |     |     |
| Product        | Name        | : JL659A         | 6300M 48SR5  | CL6 PoE    | 4SFP56 Swch |     |     |
| Chassis        | Serial Nbr  | : ID9ZKHN090     |              |            |             |     |     |
| Base           | MAC Address | : 9020c2-245080  |              |            |             |     |     |
| AOS-CX         | Version :   | FL.10.xx.xxxx    |              |            |             |     |     |
| Time           | Zone        | : UTC            |              |            |             |     |     |
| Up Time        |             | : 5 days,        | 15 hours,    | 33 minutes |             |     |     |
| CPU Util       | (%)         | : 21             |              |            |             |     |     |
| Memory         | Usage (%)   | : 19             |              |            |             |     |     |
| Command        | History     |                  |              |            |             |     |     |
| Release        |             |                  | Modification |            |             |     |     |
| 10.07orearlier |             |                  | --           |            |             |     |     |
| Command        | Information |                  |              |            |             |     |     |
| Platforms      | Command     | context          | Authority    |            |             |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show        | system               | resource-utilization |         |               |        |     |     |
| ----------- | -------------------- | -------------------- | ------- | ------------- | ------ | --- | --- |
| show system | resource-utilization |                      | [daemon | <DAEMON-NAME> | | all] |     |     |
Description
ShowsinformationabouttheusageofsystemresourcessuchasCPU,memory,andopenfile
descriptors.
| Parameter |               |     | Description |     |     |     |     |
| --------- | ------------- | --- | ----------- | --- | --- | --- | --- |
| daemon    | <DAEMON-NAME> |     |             |     |     |     |     |
Showsthefilteredresourceutilizationdatafortheprocess
|     |     |     | specifiedby<DAEMON-NAME> |     | only. |     |     |
| --- | --- | --- | ------------------------ | --- | ----- | --- | --- |
vrf <VRF-NAME>
SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
NOTE:
|     |     |     | Foralistofdaemonsthatlogevents,entershow |     |     | events | -d ?froma |
| --- | --- | --- | ---------------------------------------- | --- | --- | ------ | --------- |
switchpromptinthemanager(#)context.
all
ShowsutilizationinformationforallVSFmembers.
Examples
Switchsystemandhardwarecommands|280

Showingallsystemresourceutilizationdata:
| switch#    |            | show system | resource-utilization |          |     |        |     |          |           |
| ---------- | ---------- | ----------- | -------------------- | -------- | --- | ------ | --- | -------- | --------- |
| System     | Resources: |             |                      |          |     |        |     |          |           |
| Processes: |            | 70          |                      |          |     |        |     |          |           |
| CPU        | usage(%):  | 20          |                      |          |     |        |     |          |           |
| Memory     | usage(%):  |             | 25                   |          |     |        |     |          |           |
| Open       | FD's:      | 1024        |                      |          |     |        |     |          |           |
| Process    |            |             | CPU                  | Usage(%) |     | Memory |     | Usage(%) | Open FD's |
-----------------------------------------------------------------------
| pmd         |     |     |     | 2   |     |     | 1   |     | 14  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hpe-sysmond |     |     |     | 1   |     |     | 2   |     | 11  |
| hpe-mgmdd   |     |     |     | 0   |     |     | 1   |     | 5   |
...
Showingtheresourceutilizationdataforthepmdprocess:
| switch# |     | show system | resource-utilization |       |     | daemon |       | pmd  |      |
| ------- | --- | ----------- | -------------------- | ----- | --- | ------ | ----- | ---- | ---- |
| Process |     |             | CPU                  | Usage |     | Memory | Usage | Open | FD's |
-----------------------------------------------------------------------
| pmd |     |     |     | 2   |     | 1   |     | 14  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# |          | show system | resource-utilization |      |      |              |     |          |     |
| ------- | -------- | ----------- | -------------------- | ---- | ---- | ------------ | --- | -------- | --- |
| System  | resource | utilization |                      | data | poll | is currently |     | disabled |     |
Showingresourceutilizationdataforalinemodule:
| switch#        |             | show system | resource-utilization |     |              | module  |     | 1/1 |     |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show      | tech   |              |     |              |     |     |     |     |     |
| --------- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- |
| show tech | [basic | | <FEATURE>] |     | [local-file] |     |     |     |     |     |
281
| AOS-CX10.11FundamentalsGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

Description
Showsdetailedinformationaboutswitchfeaturesbyautomaticallyrunningtheshowcommands
associatedwiththefeature.Ifnoparametersarespecified,theshow techcommandshowsinformation
aboutallswitchfeatures.Technicalsupportpersonnelusetheoutputfromthiscommandfor
troubleshooting.
| Parameter |     |     | Description                             |
| --------- | --- | --- | --------------------------------------- |
| basic     |     |     | Specifiesshowingabasicsetofinformation. |
<FEATURE>
Specifiesthenameofafeature.Foralistoffeaturenames,enter
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
Thelistoffailedshowcommands,ifany.
n
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
Switchsystemandhardwarecommands|282

Directingtheoutputoftheshow tech basiccommandtothelocaltextfile:
| switch# | show tech | basic local-file |     |
| ------- | --------- | ---------------- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
| to copy-out         | this file. |         |              |
| ------------------- | ---------- | ------- | ------------ |
| Command History     |            |         |              |
| Release             |            |         | Modification |
| 10.07orearlier      |            |         | --           |
| Command Information |            |         |              |
| Platforms           | Command    | context | Authority    |
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
| switch>  | show usb |     |     |
| -------- | -------- | --- | --- |
| Enabled: | Yes      |     |     |
| Mounted: | No       |     |     |
IfUSBhasbeenenabledandadevicemounted:
| switch>         | show usb |     |     |
| --------------- | -------- | --- | --- |
| Enabled:        | Yes      |     |     |
| Mounted:        | Yes      |     |     |
| Command History |          |     |     |
283
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Release        |             |         | Modification |     |
| -------------- | ----------- | ------- | ------------ | --- |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show usb             | file-system |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| show usb file-system | [<PATH>]    |     |     |     |
Description
ShowsdirectorylistingsforamountedUSBdevice.Whenenteredwithoutthe<PATH>parameterthe
topleveldirectorytreeisshown.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PATH>
Specifiesthefilepathtoshow.Aleading"/"inthepathisoptional.
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
Switchsystemandhardwarecommands|284

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
show version
Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
Example
Showingversioninformation:
| switch(config)# | show | version |     |
| --------------- | ---- | ------- | --- |
-----------------------------------------------------------------------------
AOS-CX
(c) Copyright 2017-2022 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version      | : ML.xx.xx.xxxx                                  |     |              |
| ------------ | ------------------------------------------------ | --- | ------------ |
| Build Date   | : 2022-05-27                                     |     | 17:00:46 PDT |
| Build ID     | : AOS-CX:ML.xx.xx.xxxx:85c3c2f3d59e:201910222335 |     |              |
| Build SHA    | : 85c3c2f3d59ec8318ba97178fad387aecb671b33       |     |              |
| Active Image | : secondary                                      |     |              |
285
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

| Service        | OS Version  |     | : ML.01.05.0001 |              |     |     |
| -------------- | ----------- | --- | --------------- | ------------ | --- | --- |
| BIOS           | Version     |     | : ML.01.0001    |              |     |     |
| Command        | History     |     |                 |              |     |     |
| Release        |             |     |                 | Modification |     |     |
| 10.07orearlier |             |     |                 | --           |     |     |
| Command        | Information |     |                 |              |     |     |
| Platforms      | Command     |     | context         | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
top cpu
Switchsystemandhardwarecommands|286

top cpu
Description
ShowsCPUutilizationinformation.
Example
ShowingtopCPUinformation:
| switch# | top cpu |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
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
| Command | History |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
287
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |     |
| ----------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| usb mount    | | unmount |     |     |
| ------------ | --------- | --- | --- |
| usb {mount | | unmount}  |     |     |
Description
Switchsystemandhardwarecommands|288

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
| switch# | usb mount |     |     |
| ------- | --------- | --- | --- |
UnmountingaUSBdrive:
| switch#             | usb unmount |         |              |
| ------------------- | ----------- | ------- | ------------ |
| Command History     |             |         |              |
| Release             |             |         | Modification |
| 10.07orearlier      |             |         | --           |
| Command Information |             |         |              |
| Platforms           | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
289
| AOS-CX10.11FundamentalsGuide| | (6200SwitchSeries) |     |     |
| ----------------------------- | ------------------ | --- | --- |

Support and Other Resources

Chapter 17

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

AOS-CX 10.11 Fundamentals Guide | (6200 Switch Series)

290

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

Support and Other Resources | 291

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
292
| AOS-CX10.11FundamentalsGuide| |     | (6200SwitchSeries) |
| ----------------------------- | --- | ------------------ |