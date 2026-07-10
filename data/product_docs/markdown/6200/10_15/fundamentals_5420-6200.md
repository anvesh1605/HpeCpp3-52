AOS-CX 10.15.xxxx
Fundamentals Guide

5420, 6200 Switch Series

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

3

Contents
| About this                           | document | 11  |
| ------------------------------------ | -------- | --- |
| Applicableproducts                   |          | 11  |
| Latestversionavailableonline         |          | 11  |
| Commandsyntaxnotationconventions     |          | 11  |
| Abouttheexamples                     |          | 12  |
| Identifyingswitchportsandinterfaces  |          | 12  |
| About AOS-CX                         |          | 14  |
| AOS-CXsystemdatabases                |          | 14  |
| NetworkAnalyticsEngineintroduction   |          | 15  |
| AOS-CXCLI                            |          | 15  |
| HPEArubaNetworkingInstallermobileapp |          | 15  |
| HPE ArubaNetworkingNetEdit           |          | 15  |
| Ansiblemodules                       |          | 16  |
| AOS-CXWebUI                          |          | 16  |
| AOS-CXRESTAPI                        |          | 16  |
| In-bandandout-of-bandmanagement      |          | 16  |
| SNMP-basedmanagementsupport          |          | 17  |
| Useraccounts                         |          | 17  |
| Initial Configuration                |          | 18  |
| InitialconfigurationusingZTP         |          | 18  |
InitialconfigurationusingtheHPEArubaNetworkingInstallermobileapp 19
|                                            | TroubleshootingBluetoothconnections            | 20  |
| ------------------------------------------ | ---------------------------------------------- | --- |
|                                            | BluetoothconnectionIPaddresses                 | 20  |
|                                            | Bluetoothisconnectedbuttheswitchisnotreachable | 21  |
|                                            | Bluetoothisnotconnected                        | 21  |
| InitialconfigurationusingtheCLI            |                                                | 24  |
|                                            | Connectingtotheconsoleport                     | 24  |
|                                            | Connectingtothemanagementport                  | 25  |
|                                            | ConfigureusingDHCPorstaticIP                   | 26  |
|                                            | Loggingintotheswitchforthefirsttime            | 27  |
|                                            | SettingswitchtimeusingtheNTPclient             | 27  |
| Configuringbanners                         |                                                | 28  |
| UsingtheWebUI                              |                                                | 28  |
| Configuringthemanagementinterface          |                                                | 29  |
| Restoringtheswitchtofactorydefaultsettings |                                                | 30  |
| Managementinterfacecommands                |                                                | 31  |
|                                            | default-gateway                                | 31  |
|                                            | ipstatic                                       | 32  |
|                                            | nameserver                                     | 33  |
|                                            | showinterfacemgmt                              | 34  |
| NTPcommands                                |                                                | 35  |
|                                            | ntpauthentication                              | 35  |
|                                            | ntpauthentication-key                          | 36  |
|                                            | ntpdisable                                     | 37  |
|                                            | ntpenable                                      | 37  |
|                                            | ntpserver                                      | 38  |
|                                            | ntptrusted-key                                 | 40  |
4
AOS-CX10.15.xxxxFundamentalsGuide| (5420,6200SwitchSeries)

|                               | ntpvrf                                   | 41  |
| ----------------------------- | ---------------------------------------- | --- |
|                               | showntpassociations                      | 42  |
|                               | showntpauthentication-keys               | 43  |
|                               | showntpservers                           | 43  |
|                               | showntpstatistics                        | 44  |
|                               | showntpstatus                            | 45  |
| Telnet                        | access                                   | 47  |
| Telnetcommands                |                                          | 47  |
|                               | showtelnetserver                         | 47  |
|                               | showtelnetserversessions                 | 48  |
|                               | telnetserver                             | 49  |
| Interface                     | configuration                            | 50  |
| Configuringalayer2interface   |                                          | 50  |
| SinglesourceIPaddress         |                                          | 50  |
| Unsupportedtransceiversupport |                                          | 50  |
| Configuringaninterfacepersona |                                          | 51  |
|                               | Modes                                    | 52  |
|                               | Predefinedandcustompersonanames          | 52  |
|                               | Creatingandconfiguringaninterfacepersona | 52  |
|                               | Examples                                 | 53  |
| Monitormode                   |                                          | 53  |
| Interfacecommands             |                                          | 54  |
|                               | allow-unsupported-transceiver            | 54  |
|                               | defaultinterface                         | 55  |
|                               | description(interface)                   | 56  |
|                               | energy-efficient-ethernet                | 57  |
|                               | flow-control                             | 57  |
|                               | interface(port)                          | 59  |
|                               | interfaceloopback                        | 59  |
|                               | interfacevlan                            | 60  |
|                               | ipaddress(interface)                     | 61  |
|                               | ipmtu                                    | 61  |
|                               | ipsource-interface                       | 62  |
|                               | iptcpmss                                 | 63  |
|                               | ipunnumbered                             | 64  |
|                               | ipv6address                              | 66  |
|                               | ipv6source-interface                     | 67  |
|                               | ipv6tcpmss                               | 69  |
|                               | mtu                                      | 70  |
|                               | persona                                  | 71  |
|                               | rate-interval                            | 73  |
|                               | routing(interface)                       | 74  |
|                               | showallow-unsupported-transceiver        | 75  |
|                               | showinterface                            | 76  |
|                               | showinterfacedom                         | 82  |
|                               | showinterfaceenergy-efficientethernet    | 83  |
|                               | showinterfaceflow-control                | 84  |
|                               | showinterfacelink-diagnostics            | 88  |
|                               | showinterfacestatistics                  | 91  |
|                               | showinterfacetransceiver                 | 94  |
|                               | showinterfaceutilization                 | 98  |
|                               | showipinterface                          | 99  |
|                               | showipsource-interface                   | 100 |
|                               | showipv6interface                        | 101 |
|5

|                                   | showipv6source-interface                        |              |            | 102 |
| --------------------------------- | ----------------------------------------------- | ------------ | ---------- | --- |
|                                   | shutdown(interface)                             |              |            | 103 |
|                                   | speed                                           |              |            | 104 |
| Source                            | interface                                       | selection    |            | 108 |
| Source-interfaceselectioncommands |                                                 |              |            | 108 |
|                                   | ipsource-interface(protocol<ip-addr>)           |              |            | 108 |
|                                   | ipsource-interface                              |              |            | 110 |
|                                   | ipv6source-interface (<protocol><ip-addr>)      |              |            | 112 |
|                                   | ipv6source-interfacedns                         |              |            | 113 |
|                                   | ipv6source-interface                            |              |            | 115 |
|                                   | showipsource-interface                          |              |            | 117 |
|                                   | showipv6source-interface                        |              |            | 119 |
|                                   | showrunning-config                              |              |            | 121 |
| VLANs                             |                                                 |              |            | 123 |
| Configuration                     |                                                 | and firmware | management | 124 |
| Upgradeanddowngradescenarios      |                                                 |              |            | 124 |
|                                   | Upgrades                                        |              |            | 124 |
|                                   | Downgrades                                      |              |            | 124 |
|                                   | Limitations                                     |              |            | 124 |
| Hot-patchsoftware                 |                                                 |              |            | 125 |
| Checkpoints                       |                                                 |              |            | 127 |
|                                   | Checkpointtypes                                 |              |            | 127 |
|                                   | Maximumnumberofcheckpoints                      |              |            | 127 |
|                                   | Usergeneratedcheckpoints                        |              |            | 127 |
|                                   | Systemgeneratedcheckpoints                      |              |            | 127 |
|                                   | Supportedremotefileformats                      |              |            | 127 |
|                                   | Rollback                                        |              |            | 128 |
|                                   | Checkpointautomode                              |              |            | 128 |
|                                   | Testingaswitchconfigurationincheckpointautomode |              |            | 128 |
| Checkpointcommands                |                                                 |              |            | 128 |
|                                   | checkpointauto                                  |              |            | 128 |
|                                   | checkpointautoconfirm                           |              |            | 129 |
|                                   | checkpointdiff                                  |              |            | 130 |
|                                   | checkpointpost-configuration                    |              |            | 132 |
|                                   | checkpointpost-configurationtimeout             |              |            | 133 |
|                                   | checkpointrename                                |              |            | 134 |
|                                   | checkpointrollback                              |              |            | 135 |
|                                   | copycheckpoint<CHECKPOINT-NAME><REMOTE-URL>     |              |            | 135 |
copycheckpoint<CHECKPOINT-NAME>{running-config|startup-config} 136
|     | copycheckpoint<CHECKPOINT-NAME><STORAGE-URL>  |     |     | 137 |
| --- | --------------------------------------------- | --- | --- | --- |
|     | copy<REMOTE-URL>checkpoint<CHECKPOINT-NAME>   |     |     | 138 |
|     | copy<REMOTE-URL>startup-config|running-config |     |     | 139 |
copyrunning-config{startup-config|checkpoint<CHECKPOINT-NAME>} 141
|     | copy{running-config|startup-config}<REMOTE-URL>  |     |     | 142 |
| --- | ------------------------------------------------ | --- | --- | --- |
|     | copy{running-config|startup-config}<STORAGE-URL> |     |     | 143 |
|     | copystartup-configrunning-config                 |     |     | 144 |
|     | copy<STORAGE-URL>running-config                  |     |     | 145 |
|     | erase                                            |     |     | 146 |
|     | showcheckpoint<CHECKPOINT-NAME>                  |     |     | 147 |
|     | showcheckpoint<CHECKPOINT-NAME>hash              |     |     | 150 |
|     | showcheckpointpost-configuration                 |     |     | 150 |
|     | showcheckpoint                                   |     |     | 151 |
|     | showcheckpointdate                               |     |     | 152 |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 6

|                                         | showrunning-confighash                     |         |             | 152 |
| --------------------------------------- | ------------------------------------------ | ------- | ----------- | --- |
|                                         | showstartup-confighash                     |         |             | 153 |
|                                         | writememory                                |         |             | 154 |
| Bootcommands                            |                                            |         |             | 155 |
|                                         | bootset-default                            |         |             | 155 |
|                                         | bootsystem                                 |         |             | 155 |
|                                         | showboot-history                           |         |             | 157 |
| Firmwaremanagementcommands              |                                            |         |             | 160 |
|                                         | copy{primary|secondary}<REMOTE-URL>        |         |             | 160 |
|                                         | copy{primary|secondary}<FIRMWARE-FILENAME> |         |             | 161 |
|                                         | copyprimarysecondary                       |         |             | 162 |
|                                         | copy<REMOTE-URL>                           |         |             | 162 |
|                                         | copysecondaryprimary                       |         |             | 164 |
|                                         | copy<STORAGE-URL>                          |         |             | 165 |
|                                         | copyhot-patch                              |         |             | 166 |
|                                         | hot-patch                                  |         |             | 167 |
|                                         | showhot-patch                              |         |             | 168 |
| Dynamic                                 | Segmentation                               |         |             | 170 |
| SNMP                                    |                                            |         |             | 171 |
| ConfiguringSNMP                         |                                            |         |             | 171 |
| HPE Aruba                               | Networking                                 | Central | integration | 173 |
| ConnectingtoHPE ArubaNetworkingCentral  |                                            |         |             | 173 |
| CustomCAcertificate                     |                                            |         |             | 173 |
| SupportmodeinHPE ArubaNetworkingCentral |                                            |         |             | 174 |
| OneTouchProvisioning                    |                                            |         |             | 174 |
| HPE ArubaNetworkingCentralcommands      |                                            |         |             | 176 |
|                                         | hpe-anw-central                            |         |             | 176 |
|                                         | hpe-anw-centralsupport-mode                |         |             | 176 |
|                                         | configuration-lockoutcentralmanaged        |         |             | 177 |
|                                         | diag-dumprestbasic                         |         |             | 178 |
|                                         | disable                                    |         |             | 179 |
|                                         | enable(HPE ArubaNetworkingCentral)         |         |             | 180 |
|                                         | location-override                          |         |             | 181 |
|                                         | location-override-alternative              |         |             | 182 |
|                                         | showhpe-anw-central                        |         |             | 184 |
|                                         | showrunning-configcurrent-context          |         |             | 187 |
| Port filtering                          |                                            |         |             | 188 |
| Portfilteringcommands                   |                                            |         |             | 188 |
|                                         | portfilter                                 |         |             | 188 |
|                                         | showportfilter                             |         |             | 190 |
| DNS                                     |                                            |         |             | 192 |
| Configuration                           |                                            |         |             | 192 |
| DNSclient                               |                                            |         |             | 192 |
| ConfiguringtheDNSclient                 |                                            |         |             | 192 |
| DNSclientcommands                       |                                            |         |             | 193 |
|                                         | ipdnsdomain-list                           |         |             | 193 |
|                                         | ipdnsdomain-name                           |         |             | 194 |
|                                         | ipdnshost                                  |         |             | 195 |
|                                         | ipdnsserveraddress                         |         |             | 196 |
|                                         | showipdns                                  |         |             | 197 |
|7

| Device         | discovery                                                | and configuration | 199 |
| -------------- | -------------------------------------------------------- | ----------------- | --- |
| Deviceprofiles |                                                          |                   | 199 |
|                | ConfiguringadeviceprofileforLLDP                         |                   | 200 |
|                | ConfiguringadeviceprofileforCDP                          |                   | 200 |
|                | ConfiguringadeviceprofileforlocalMACmatch                |                   | 200 |
|                | DeviceProfileUsageConsiderations                         |                   | 201 |
|                | Deviceprofilecommands                                    |                   | 202 |
|                | aaaauthenticationport-accessallow-cdp-auth               |                   | 202 |
|                | aaaauthenticationport-accessallow-cdp-bpdu               |                   | 203 |
|                | aaaauthenticationport-accessallow-cdp-proxy-logoff       |                   | 204 |
|                | aaaauthenticationport-accessallow-lldp-bpdu              |                   | 205 |
|                | associatecdp-group                                       |                   | 207 |
|                | associatelldp-group                                      |                   | 208 |
|                | associatemac-group                                       |                   | 208 |
|                | associaterole                                            |                   | 209 |
|                | disable(port-accessdevice-profile)                       |                   | 210 |
|                | enable(port-accessdevice-profile)                        |                   | 211 |
|                | ignore(forCDPgroups)                                     |                   | 211 |
|                | ignore(forLLDPgroups)                                    |                   | 212 |
|                | ignore(forMACgroups)                                     |                   | 214 |
|                | mac-group                                                |                   | 218 |
|                | match(forCDPgroups)                                      |                   | 218 |
|                | match(forLLDPgroups)                                     |                   | 220 |
|                | match(forMACgroups)                                      |                   | 221 |
|                | port-accesscdp-group                                     |                   | 225 |
|                | port-accessdevice-profile                                |                   | 226 |
|                | port-accessdevice-profilemodeblock-until-profile-applied |                   | 228 |
|                | port-accesslldp-group                                    |                   | 228 |
|                | showport-accessdevice-profile                            |                   | 229 |
| LLDP           |                                                          |                   | 231 |
|                | LLDPagent                                                |                   | 231 |
|                | LLDPMEDsupport                                           |                   | 233 |
|                | LLDPEEE                                                  |                   | 234 |
|                | ConfiguringtheLLDPagent                                  |                   | 234 |
|                | LLDPcommands                                             |                   | 235 |
|                | clearlldpneighbors                                       |                   | 235 |
|                | clearlldpstatistics                                      |                   | 235 |
|                | lldp                                                     |                   | 236 |
|                | lldpdot3                                                 |                   | 237 |
|                | lldpdot3eee                                              |                   | 237 |
|                | lldpdot3mfs                                              |                   | 238 |
|                | lldpholdtime-multiplier                                  |                   | 239 |
|                | lldpmanagement-addressvlan                               |                   | 240 |
|                | lldpmanagement-ip-address                                |                   | 241 |
|                | lldpmanagement-ipv6-address                              |                   | 242 |
|                | lldpmed                                                  |                   | 242 |
|                | lldpmedlocation                                          |                   | 243 |
|                | lldpreceive                                              |                   | 245 |
|                | lldpreinit                                               |                   | 246 |
|                | lldpselect-tlv                                           |                   | 247 |
|                | lldptimer                                                |                   | 248 |
|                | lldptlv-enable                                           |                   | 250 |
|                | lldptransmit                                             |                   | 250 |
|                | lldptxdelay                                              |                   | 251 |
|                | lldptrapenable                                           |                   | 252 |
|                | showlldpconfiguration                                    |                   | 254 |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 8

|                                                     | showlldpconfigurationmgmt   |              |          | 256 |
| --------------------------------------------------- | --------------------------- | ------------ | -------- | --- |
|                                                     | showlldplocal-device        |              |          | 257 |
|                                                     | showlldpneighbor-info       |              |          | 258 |
|                                                     | showlldpneighbor-infodetail |              |          | 262 |
|                                                     | showlldpneighbor-infomgmt   |              |          | 264 |
|                                                     | showlldpstatistics          |              |          | 266 |
|                                                     | showlldpstatisticsmgmt      |              |          | 267 |
|                                                     | showlldptlv                 |              |          | 268 |
| CiscoDiscoveryProtocol(CDP)                         |                             |              |          | 268 |
|                                                     | CDPsupport                  |              |          | 269 |
|                                                     | CDPcommands                 |              |          | 269 |
|                                                     | cdp(global)                 |              |          | 269 |
|                                                     | clearcdpcounters            |              |          | 270 |
|                                                     | clearcdpneighbor-info       |              |          | 271 |
|                                                     | showcdp                     |              |          | 271 |
|                                                     | showcdpneighbor-info        |              |          | 272 |
|                                                     | showcdptraffic              |              |          | 273 |
|                                                     | showcdpvoice-vlanmode       |              |          | 274 |
| Zero                                                | Touch Provisioning          |              |          | 275 |
| ZTPconnectionpriorities                             |                             |              |          | 275 |
| ZTPsupport                                          |                             |              |          | 275 |
| SettingupZTPonatrustednetwork                       |                             |              |          | 277 |
| ZTPprocessduringswitchboot                          |                             |              |          | 278 |
| ZTPVSFswitchoversupport                             |                             |              |          | 279 |
| ZTPcommands                                         |                             |              |          | 279 |
|                                                     | showztpinformation          |              |          | 279 |
|                                                     | ztpforceprovision           |              |          | 281 |
| Switch                                              | system                      | and hardware | commands | 284 |
| allow-non-failsafe-updates                          |                             |              |          | 284 |
| bluetoothdisable                                    |                             |              |          | 285 |
| bluetoothenable                                     |                             |              |          | 285 |
| clearevents                                         |                             |              |          | 286 |
| cleariperrors                                       |                             |              |          | 287 |
| consolebaud-rate                                    |                             |              |          | 288 |
| domain-name                                         |                             |              |          | 288 |
| front-panel-securityfactory-reset                   |                             |              |          | 289 |
| hostname                                            |                             |              |          | 290 |
| mtrace                                              |                             |              |          | 291 |
| powerconsumption-average-period                     |                             |              |          | 292 |
| showbluetooth                                       |                             |              |          | 293 |
| showboot-history                                    |                             |              |          | 294 |
| showcapacities                                      |                             |              |          | 297 |
| showcapacities-status                               |                             |              |          | 299 |
| showconsole                                         |                             |              |          | 299 |
| showcore-dump                                       |                             |              |          | 300 |
| showdeprecatedcommands                              |                             |              |          | 302 |
| showdomain-name                                     |                             |              |          | 303 |
| showenvironmentfan                                  |                             |              |          | 303 |
| showenvironmentled                                  |                             |              |          | 305 |
| showenvironmentpower-consumption                    |                             |              |          | 305 |
| showenvironmentpower-consumptionpower-over-ethernet |                             |              |          | 308 |
| showenvironmentpower-supply                         |                             |              |          | 312 |
| showenvironmenttemperature                          |                             |              |          | 313 |
| showevents                                          |                             |              |          | 315 |
|9

| showfront-panel-securitystatus          |           |           | 318 |
| --------------------------------------- | --------- | --------- | --- |
| showhostname                            |           |           | 319 |
| showimages                              |           |           | 319 |
| showiperrors                            |           |           | 320 |
| showmodule                              |           |           | 322 |
| showrunning-config                      |           |           | 324 |
| showrunning-configcurrent-context       |           |           | 327 |
| showstartup-config                      |           |           | 328 |
| showsystem                              |           |           | 330 |
| showsystemresource-utilization          |           |           | 331 |
| showtech                                |           |           | 335 |
| showusb                                 |           |           | 336 |
| showusbfile-system                      |           |           | 337 |
| showversion                             |           |           | 338 |
| systemresource-utilizationpoll-interval |           |           | 339 |
| topcpu                                  |           |           | 340 |
| topmemory                               |           |           | 341 |
| usb                                     |           |           | 341 |
| usbmount|unmount                        |           |           | 342 |
| Support                                 | and Other | Resources | 344 |
| AccessingHPE ArubaNetworkingSupport     |           |           | 344 |
| AccessingUpdates                        |           |           | 345 |
| WarrantyInformation                     |           |           | 345 |
| RegulatoryInformation                   |           |           | 345 |
| DocumentationFeedback                   |           |           | 345 |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 10

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A, S0U61A,
S0U62A, S0U66A, S0U68A)

n HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A,
R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B,
JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,
S0M89A,  S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

11

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
format: member/slot/port.

On the HPE Aruba Networking 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

13

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

14

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

HPE Aruba Networking Installer mobile app

The HPE Aruba Networking Installer mobile app enables you to use a mobile device to configure or
access a supported AOS-CX switch. You can connect to the switch through Bluetooth or Wi-Fi.

You can use this application to do the following:

n Connect to the switch for the first time and configure basic operational settings—all without

requiring you to connect a terminal emulator to the console port.

n View and change the configuration of individual switch features or settings.

n Manage the running configuration and startup configuration of the switch, including the following:

o Transferring files between the switch and your mobile device

o Sharing configuration files from your mobile device

o Copying the running configuration to the startup configuration

n Access the switch CLI.

Refer to the HPE Aruba Networking Installer mobile app datasheet for more information.

HPE Aruba Networking NetEdit

HPE Aruba Networking NetEdit enables the automation of multidevice configuration change workflows
without the overhead of programming.

The key capabilities of NetEdit include the following:

n Intelligent configuration with validation for consistency and compliance

n Time savings by simultaneously viewing and editing multiple configurations

n Customized validation tests for corporate compliance and network design

About AOS-CX | 15

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

In-band and out-of-band management

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

16

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

n Connect to the switch wirelessly with a mobile device through Bluetooth, and use the HPE Aruba
Networking Installer Mobile App to deploy an initial configuration from a provided template. The
template you choose during the deployment process determines how the management interface is
configured. Optionally, as the final deployment step, you can select to import the switch into NetEdit
through a WiFI connection to the NetEdit server.

Alternatively, you can use the HPE Aruba Networking Installer Mobile App to manually configure switch
settings and features for a subset of the features you can configure using the CLI. You can also access
the CLI through the mobile application.

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

18

3. Power on the switch. During the ZTP operation, the switch might reboot if a new firmware image
is being installed. ZTP goes to "Failed" state if the switch receives DHCP IP for vlan1 and does not
receive any ZTP options within 60 seconds.

Initial configuration using the HPE Aruba Networking
Installer mobile app

This procedure describes how to use your mobile device to connect to the Bluetooth interface of the
switch to connect to the switch for the first time so that you can configure basic operational settings
using the HPE Aruba Networking Installer mobile app.

Prerequisites

n You have obtained the USB Bluetooth adapter that was shipped with the switch. Information about
the make and model of the supported adapter is included in the information about the HPE Aruba
Networking Installer mobile app in the Apple Store or Google Play.

n The HPE Aruba Networking Installer mobile app must be installed on your mobile device.

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

Initial Configuration | 19

For example: 8325-987654X1234567 or 8320-AB12CDE123

A switch supports one active Bluetooth connection at a time.

On some Android devices, you might need to change the settings of the paired device to specify
that it be used for Internet access.

3. Open the HPE Aruba Networking Installer mobile app on your mobile device.

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
configuration is complete. For more information about what you can configure using the HPE
Aruba Networking Installer mobile app, see the online help for the application.

Troubleshooting Bluetooth connections

Bluetooth connection IP addresses

The Bluetooth connection uses IP addresses in the 192.168.99.0/24 subnet.

Switch

192.168.99.1

Mobile device

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

20

192.168.99.10

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

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
module is the module in slot 5 (HPE Aruba Networking 8400 switches) or slot 1 (HPE Aruba Networking
6400 switches).

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

24

n Aswitchinstalledasdescribedinitshardwareinstallationguide.
n Acomputerwithterminalemulationsoftware.
Procedure
1. ConnecttheUSB-CportontheswitchtotheUSB-CportonthecomputerusingaUSB-Ccable.
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
InitialConfiguration |25

2. UseanEthernetcabletoconnectthemanagementporttoyournetwork.
3. UseanEthernetcabletoconnectyourcomputertothesamenetwork.
4. StartyourSSHclientsoftwareandconfigureanewsessionusingtheaddressassignedtothe
managementinterface.(IfthemanagementinterfaceissettooperateasaDHCPclient,retrieve
theIPaddressassignedtothemanagementinterfacefromyourDHCPserver.)
5. Startthesession.Iftheconnectionissuccessful,youarepromptedtologin.
| Configure | using DHCP | or  | static | IP  |     |
| --------- | ---------- | --- | ------ | --- | --- |
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
| Switch(config)#:    |     | interface   | 1/1/1    |                    |      |
| ------------------- | --- | ----------- | -------- | ------------------ | ---- |
| Switch(config-if)#: |     | description |          | IN-BAND Management | Port |
| Switch(config-if)#: |     | vlan        | access   | 1                  |      |
| Switch(config-if)#: |     | no          | shutdown |                    |      |
| Switch(config-if)#: |     | end         |          |                    |      |
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
| Switch(config)#:    |     | interface   | 1/1/1    |                    |      |
| ------------------- | --- | ----------- | -------- | ------------------ | ---- |
| Switch(config-if)#: |     | description |          | IN-BAND Management | Port |
| Switch(config-if)#: |     | vlan        | access   | 1                  |      |
| Switch(config-if)#: |     | no          | shutdown |                    |      |
| Switch(config-if)#: |     | end         |          |                    |      |
Switch#
!
| Switch(config)#: |     | interface | vlan | 1   |     |
| ---------------- | --- | --------- | ---- | --- | --- |
Switch(config-if-vlan)#: description IN-BAND Management Interface
| Switch(config-if-vlan)#: |     |     | no ip       | dhcp            |     |
| ------------------------ | --- | --- | ----------- | --------------- | --- |
| Switch(config-if-vlan)#: |     |     | ip address  | 192.168.10.1/24 |     |
| Switch(config-if-vlan)#: |     |     | no shutdown |                 |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 26

| Switch(config-if-vlan)#: |     |     | end |     |     |
| ------------------------ | --- | --- | --- | --- | --- |
Switch#
| Logging | into | the switch | for | the first | time |
| ------- | ---- | ---------- | --- | --------- | ---- |
Thefirsttimeyoulogintotheswitchyoumustusethedefaultadministratoraccount.Thisaccounthas
nopassword,soyouwillbepromptedonlogintodefineonetosafeguardtheswitch.
Procedure
1. Whenpromptedtologin,specifyadmin.Whenpromptedforthepassword,pressENTER.(By
default,nopasswordisdefined.)
Forexample:
switch login:
admin
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
TheIPaddressordomainnameofanNTPserver.
n
n IftheNTPserverusesauthentication,obtainthepasswordrequiredtocommunicatewiththeNTP
server.
Procedure
1. IftheNTPserverrequiresauthentication,definetheauthenticationkeyfortheNTPclientwiththe
|     | commandntp                            | authentication. |     |     |         |
| --- | ------------------------------------- | --------------- | --- | --- | ------- |
| 2.  | ConfigureanNTPserverwiththecommandntp |                 |     |     | server. |
InitialConfiguration |27

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
|       | Banner  | updated | successfully! |     |     |     |     |     |     |     |
| ----- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Using | the Web |         | UI            |     |     |     |     |     |     |     |
TheWebUIisdisabledbydefault.Followthesestepstoenableitonthemanagementportandlogin.
TheWebUIisenabledbydefaultonthedefaultVRF.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 28

Prerequisites
n AconnectiontotheswitchCLI.
Procedure
1. LogintotheCLI.
2. SwitchtoconfigcontextandenabletheWebUIonthemanagementportVRFwiththecommand
|     | https-server | vrf | mgmt. |     |
| --- | ------------ | --- | ----- | --- |
Forexample:
|     | switch#         | config |              |          |
| --- | --------------- | ------ | ------------ | -------- |
|     | switch(config)# |        | https-server | vrf mgmt |
3. StartyourwebbrowserandentertheIPaddressofthemanagementportintheaddressbar,
|     | Forexample: | https://192.168.1.1 |     |     |
| --- | ----------- | ------------------- | --- | --- |
4. TheWebUIstartsandyouarepromptedtologin.
| Configuring |     | the | management | interface |
| ----------- | --- | --- | ---------- | --------- |
Prerequisites
Aconnectiontotheconsoleport.
Procedure
1. Switchtothemanagementinterfacecontextwiththecommandinterface mgmt.
2. Bydefault,themanagementinterfaceonthemanagementportisenabled.Ifitwasdisabled,re-
|     | enableitwiththecommandno |     | shutdown. |     |
| --- | ------------------------ | --- | --------- | --- |
3. Usethecommandip dhcptoconfigurethemanagementinterfacetoautomaticallyobtainan
addressfromaDHCPserveronthenetwork(factorydefaultsetting).Or,assignastaticIPv4or
IPv6address,defaultgateway,andDNSserverwiththecommandsip address,ipv6 address,ip
static,default-gateway,andnameserver.
4. SSHisenabledbydefaultonthemanagementVRF.Ifdisabled,enableSSHwiththecommand
|     | ssh server | vrf mgmt. |     |     |
| --- | ---------- | --------- | --- | --- |
Examples
ThisexampleenablesthemanagementinterfacewithdynamicaddressingusingDHCP:
| switch(config)#         |     | interface | mgmt        |     |
| ----------------------- | --- | --------- | ----------- | --- |
| switch(config-if-mgmt)# |     |           | no shutdown |     |
| switch(config-if-mgmt)# |     |           | ip dhcp     |     |
Thisexampleenablesthemanagementinterfacewithstaticaddressingcreatingthefollowing
configuration:
SetsastaticIPv4addressof198.168.100.10withamaskof24bits.
n
n Setsthedefaultgatewayto198.168.100.200.
n SetstheDNSserverto198.168.100.201.
InitialConfiguration |29

| switch(config)# |     | interface |     | mgmt |     |     |     |     |     |
| --------------- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
switch(config-if-mgmt)#
no shutdown
| switch(config-if-mgmt)# |     |        | ip              | static | 198.168.100.10/24 |                 |     |          |     |
| ----------------------- | --- | ------ | --------------- | ------ | ----------------- | --------------- | --- | -------- | --- |
| switch(config-if-mgmt)# |     |        | default-gateway |        |                   | 198.168.100.200 |     |          |     |
| switch(config-if-mgmt)# |     |        | nameserver      |        | 198.168.100.201   |                 |     |          |     |
| Restoring               | the | switch |                 | to     | factory           | default         |     | settings |     |
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
switch# copy running-config tftp://192.168.1.10/backup_cfg json vrf mgmt
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
| [  OK ]            | Stopped | AOS-CX     | Switch  |              | Daemon | for BCM.     |              |     |     |
...
| [  OK ]   | Stopped      | Remount      | Root      | and | Kernel | File | Systems. |     |     |
| --------- | ------------ | ------------ | --------- | --- | ------ | ---- | -------- | --- | --- |
| [  OK ]   | Reached      | target       | Shutdown. |     |        |      |          |     |     |
| reboot:   | Restarting   | system       |           |     |        |      |          |     |     |
| Press Esc | for          | boot options |           |     |        |      |          |     |     |
| ServiceOS | Information: |              |           |     |        |      |          |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 30

|     | Version: |       |     | GT.01.03.0006                                     |     |          |     |     |     |     |
| --- | -------- | ----- | --- | ------------------------------------------------- | --- | -------- | --- | --- | --- | --- |
|     | Build    | Date: |     | 2018-10-30                                        |     | 14:20:44 |     | PDT |     |     |
|     | Build    | ID:   |     | ServiceOS:GT.01.03.0006:8ee0faaa52da:201810301420 |     |          |     |     |     |     |
|     | SHA:     |       |     | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx          |     |          |     |     |     |     |
...
|     | ################         |          | Preparing                                      |        | for             | zeroization                 |                         | ################# |            |     |
| --- | ------------------------ | -------- | ---------------------------------------------- | ------ | --------------- | --------------------------- | ----------------------- | ----------------- | ---------- | --- |
|     | ################         |          | Storage                                        |        | zeroization     |                             | ####################### |                   |            |     |
|     | ################         |          | WARNING:                                       |        | DO NOT          | POWER                       | OFF                     | UNTIL             | ########## |     |
|     | ################         |          |                                                |        | ZEROIZATION     |                             | IS                      | COMPLETE          | ########## |     |
|     | ################         |          | This                                           | should | take            | several                     |                         | minutes           | ########## |     |
|     | ################         |          | to                                             | one    | hour to         | complete                    |                         |                   | ########## |     |
|     | ################         |          | Restoring                                      |        | files           | ########################### |                         |                   |            |     |
|     | Boot Profiles:           |          |                                                |        |                 |                             |                         |                   |            |     |
|     | 0. Service               | OS       | Console                                        |        |                 |                             |                         |                   |            |     |
|     | 1. Primary               | Software |                                                | Image  | [XL.10.02.0010] |                             |                         |                   |            |     |
|     | 2. Secondary             | Software |                                                | Image  | [XL.10.02.0010] |                             |                         |                   |            |     |
|     | Select profile(primary): |          |                                                |        |                 |                             |                         |                   |            |     |
|     | Booting                  | primary  | software                                       |        | image...        |                             |                         |                   |            |     |
|     | Verifying                | Image... |                                                |        |                 |                             |                         |                   |            |     |
|     | Image Info:              |          |                                                |        |                 |                             |                         |                   |            |     |
|     |                          | Name:    | AOS-CX                                         |        |                 |                             |                         |                   |            |     |
|     | Version:                 |          | XL.10.02.0010                                  |        |                 |                             |                         |                   |            |     |
|     | Build                    | Id:      | AOS-CX:XL.10.02.0010:feaf5b9b7f09:201901292014 |        |                 |                             |                         |                   |            |     |
|     | Build                    | Date:    | 2019-01-29                                     |        | 12:43:50        | PST                         |                         |                   |            |     |
|     | Extracting               | Image... |                                                |        |                 |                             |                         |                   |            |     |
|     | Loading                  | Image... |                                                |        |                 |                             |                         |                   |            |     |
Done.
|     | kexec_core: | Starting     |     | new | kernel |     |     |     |     |     |
| --- | ----------- | ------------ | --- | --- | ------ | --- | --- | --- | --- | --- |
|     | System is   | initializing |     |     |        |     |     |     |     |     |
fips_post_check[5473]: FIPS_POST: Cryptographic selftest started...SUCCESS
|     | [  OK ] | Started | Login | banner |     | readiness |     | check. |     |     |
| --- | ------- | ------- | ----- | ------ | --- | --------- | --- | ------ | --- | --- |
...
|     | 8400X login: | admin |     |     |     |     |     |     |     |     |
| --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Password:
switch#
switch#
switch# copy tftp://192.168.1.10/backup_cfg running-config json vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     |     | Dload |     | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------ | ----------- | ---------- |
100 10340 100 10340 0 0 2858k 0 --:--:-- --:--:-- --:--:-- 2858k
100 10340 100 10340 0 0 2804k 0 --:--:-- --:--:-- --:--:-- 2804k
Large configuration changes will take time to process, please be patient.
switch#
switch#
|     | switch# | copy running-config |     |     | startup-config |     |     |     |     |     |
| --- | ------- | ------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Large configuration changes will take time to process, please be patient.
switch#
| Management |     |     | interface |     |     | commands |     |     |     |     |
| ---------- | --- | --- | --------- | --- | --- | -------- | --- | --- | --- | --- |
default-gateway
InitialConfiguration |31

| default-gateway    | <IP-ADDR> |     |     |
| ------------------ | --------- | --- | --- |
| no default-gateway | <IP-ADDR> |     |     |
Description
AssignsanIPv4orIPv6defaultgatewaytothemanagementinterface.AnIPv4defaultgatewaycanonly
beconfiguredifastaticIPv4addresswasassignedtothemanagementinterface.AnIPv6default
gatewaycanonlybeconfiguredifastaticIPv6addresswasassignedtothemanagementinterface.The
defaultgatewayshouldbeonthesamenetworksegment.
Thenoformofthiscommandremovesthedefaultgatewayfromthemanagementinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
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
5420 config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
ip static
| ip static <IP-ADDR>/<MASK> |                  |     |     |
| -------------------------- | ---------------- | --- | --- |
| no ip static               | <IP-ADDR>/<MASK> |     |     |
Description
AssignsanIPv4orIPv6addresstothemanagementinterface.
ThenoformofthiscommandremovestheIPaddressfromthemanagementinterfaceandsetsthe
interfacetooperateasaDHCPclient.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 32

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
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
5420 config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------------- | --- |
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
InitialConfiguration |33

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
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
5420 config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
| 6200           |      |     | rightsforthiscommand. |     |
| -------------- | ---- | --- | --------------------- | --- |
| show interface | mgmt |     |                       |     |
| show interface | mgmt |     |                       |     |
Description
Showsstatusandconfigurationinformationforthemanagementinterface.
Example
| switch# show | interface | mgmt |                     |     |
| ------------ | --------- | ---- | ------------------- | --- |
| Address      | Mode      |      | : static            |     |
| Admin State  |           |      | : up                |     |
| Mac Address  |           |      | : 02:42:ac:11:00:02 |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 34

| IPv4 address/subnet-mask |                       |         | : 192.168.1.10/16            |
| ------------------------ | --------------------- | ------- | ---------------------------- |
| Default                  | gateway IPv4          |         | : 192.168.1.1                |
| IPv6 address/prefix      |                       |         | : 2001:db8:0:1::129/64       |
| IPv6 link                | local address/prefix: |         | fe80::7272:cfff:fefd:e485/64 |
| Default                  | gateway IPv6          |         | : 2001:db8:0:1::1            |
| Primary                  | Nameserver            |         | : 2001::1                    |
| Secondary                | Nameserver            |         | : 2001::2                    |
| Command History          |                       |         |                              |
| Release                  |                       |         | Modification                 |
| 10.07orearlier           |                       |         | --                           |
| Command Information      |                       |         |                              |
| Platforms                | Command               | context | Authority                    |
5420 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 6200 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
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
InitialConfiguration |35

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Whenthekeyisnotprovidedonthecommandline,
plaintextkeypromptingoccursuponpressingEnter,
followedbypromptingastowhetherthekeyistobe
trusted.Theenteredkeycharactersaremaskedwith
asterisks.
Examples
Definingkey10withMD5encryptionandaprovidedplaintexttrustedkey:
| switch(config)# |     | ntp authentication-key |     |     | 10 md5 F82#450b | trusted |
| --------------- | --- | ---------------------- | --- | --- | --------------- | ------- |
Definingkey5withSHA1encryptionandapromptedplaintexttrustedkey:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 36

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
|                |             | ntp | disable |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Command        | History     |     |         |     |              |     |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp enable
ntp enable
InitialConfiguration |37

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 38

Parameter

Description

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

key <KEY-NUM>

minpoll <MIN-NUM>

maxpoll <MAX-NUM>

burst

iburst

prefer

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

Initial Configuration | 39

Examples
Definingthentpserverpool.ntp.org,usingiburst,andNTPversion4.
switch(config)#
|     | ntp | server | pool.ntp.org | iburst | version | 4   |
| --- | --- | ------ | ------------ | ------ | ------- | --- |
Removingthentpserverpool.ntp.org.
| switch(config)# | no  | ntp server | pool.ntp.org |     |     |     |
| --------------- | --- | ---------- | ------------ | --- | --- | --- |
Definingthentpservermy-ntp.mydomain.comandmakesitthepreferredserver.
| switch(config)#     | ntp     | server  | my-ntp.mydomain.com |     | prefer |     |
| ------------------- | ------- | ------- | ------------------- | --- | ------ | --- |
| Command History     |         |         |                     |     |        |     |
| Release             |         |         | Modification        |     |        |     |
| 10.07orearlier      |         |         | --                  |     |        |     |
| Command Information |         |         |                     |     |        |     |
| Platforms           | Command | context | Authority           |     |        |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ntp trusted-key
| ntp trusted-key    | <KEY-ID> |     |     |     |     |     |
| ------------------ | -------- | --- | --- | --- | --- | --- |
| no ntp trusted-key | <KEY-ID> |     |     |     |     |     |
Description
Setsakeyastrusted.WhenNTPauthenticationisenabled,theswitchonlysynchronizeswithtime
serversthattransmitpacketscontainingatrustedkey.
Thenoformofthiscommandremovesthetrusteddesignationfromakey.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<KEY-ID> Specifiestheidentificationnumberofthekeytosetastrusted.
Range:1to65534.
Examples
Definingkey10asatrustedkey.
| switch(config)# | ntp | trusted-key | 10  |     |     |     |
| --------------- | --- | ----------- | --- | --- | --- | --- |
Removingtrusteddesignationfromkey10:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 40

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
| switch(config)#     | no  | ntp vrf |              |
| ------------------- | --- | ------- | ------------ |
| Command History     |     |         |              |
| Release             |     |         | Modification |
| 10.07orearlier      |     |         | --           |
| Command Information |     |         |              |
InitialConfiguration |41

| Platforms | Command | context | Authority |     |     |     |
| --------- | ------- | ------- | --------- | --- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ntp | associations |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- |
show ntp associations
Description
ShowsthestatusoftheconnectiontoeachNTPserver.Thefollowinginformationisdisplayedforeach
server:
n Tallycode:ThefirstcharacteristheTallycode:
o
(blank):Nostateinformationavailable(e.g.non-respondingserver)
o x:Outoftolerance(discardedbyintersectionalgorithm)
o .:Discardedbytableoverflow(notused)
o
-:Outoftolerance(discardedbytheclusteralgorithm)
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
| switch# show | ntp associations |     |     |     |     |     |
| ------------ | ---------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------
| ID  | NAME |     | REMOTE | REF-ID | ST LAST POLL | REACH |
| --- | ---- | --- | ------ | ------ | ------------ | ----- |
----------------------------------------------------------------------
| 1                  | 192.0.1.1 |              | 192.0.1.1 | .INIT. | 16 -     | 64 0 |
| ------------------ | --------- | ------------ | --------- | ------ | -------- | ---- |
| * 2 time.apple.com |           | 17.253.2.253 |           | .GPSs. | 2 70 128 | 377  |
----------------------------------------------------------------------
| Command History |     |     |              |     |     |     |
| --------------- | --- | --- | ------------ | --- | --- | --- |
| Release         |     |     | Modification |     |     |     |
| 10.07orearlier  |     |     | --           |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 42

| Command   | Information |         |         |           |     |
| --------- | ----------- | ------- | ------- | --------- | --- |
| Platforms |             | Command | context | Authority |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | ntp | authentication-keys |     |     |     |
| ---- | --- | ------------------- | --- | --- | --- |
show ntp authentication-keys
Description
Showsthecurrentlydefinedauthenticationkeys.
Examples
| switch# | show | ntp | authentication-keys |     |     |
| ------- | ---- | --- | ------------------- | --- | --- |
--------------------------------
| Auth | key | Trusted | MD5 password |     |     |
| ---- | --- | ------- | ------------ | --- | --- |
--------------------------------
| 10             |             | No      | ********** |              |     |
| -------------- | ----------- | ------- | ---------- | ------------ | --- |
| 20             |             | Yes     | ********** |              |     |
| Command        | History     |         |            |              |     |
| Release        |             |         |            | Modification |     |
| 10.07orearlier |             |         |            | --           |     |
| Command        | Information |         |            |              |     |
| Platforms      |             | Command | context    | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ntp | servers |     |     |     |
| ---- | --- | ------- | --- | --- | --- |
show ntp servers
Description
ShowsallconfiguredNTPservers,includinganyDHCPservers,defaultpoolserversoranyserverwith
| thestatusauto |     | prefer. |     |     |     |
| ------------- | --- | ------- | --- | --- | --- |
Example
| switch# | show | ntp | servers |     |     |
| ------- | ---- | --- | ------- | --- | --- |
------------------------------------------------
|     | NTP | SERVER KEYID | MINPOLL | MAXPOLL OPTION | VER |
| --- | --- | ------------ | ------- | -------------- | --- |
------------------------------------------------
|     | 192.0.1.18 |     | -   | 5 10 iburst | 3   |
| --- | ---------- | --- | --- | ----------- | --- |
|     | 192.0.1.19 |     | -   | 6 10 none   | 4   |
InitialConfiguration |43

| 192.0.1.20 |     | - 6 | 8 burst | 3 prefer |
| ---------- | --- | --- | ------- | -------- |
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
Examples
| switch(config)#   | show          | ntp statistics |     |     |
| ----------------- | ------------- | -------------- | --- | --- |
|                   | Rx-pkts       | 100            |     |     |
| Current Version   | Rx-pkts       | 80             |     |     |
| Old Version       | Rx-pkts       | 20             |     |     |
|                   | Err-pkts      | 2              |     |     |
| Auth-failed-pkts  |               | 1              |     |     |
|                   | Declined-pkts | 0              |     |     |
| Restricted-pkts   |               | 0              |     |     |
| Rate-limited-pkts |               | 0              |     |     |
|                   | KoD-pkts      | 0              |     |     |
| Command History   |               |                |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 44

| Release        |             |     |         |     |     | Modification |     |     |
| -------------- | ----------- | --- | ------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |             |     |         |     |     | --           |     |     |
| Command        | Information |     |         |     |     |              |     |     |
| Platforms      | Command     |     | context |     |     | Authority    |     |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ntp | status |     |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
show ntp status
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
| Command            | Information |           |             |              |             |              |              |     |
InitialConfiguration |45

Platforms

Command context

Authority

All platforms

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

46

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
| Command    | History     |         |         |     |                                                   |
| ---------- | ----------- | ------- | ------- | --- | ------------------------------------------------- |
| Release    |             |         |         |     | Modification                                      |
| 10.08.1021 |             |         |         |     | Commandintroducedonthe6200,6300,6400SwitchSeries. |
| Command    | Information |         |         |     |                                                   |
| Platforms  |             | Command | context |     | Authority                                         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
47
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries)

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
|            | Server IP   | : 20.1.1.1                                        |     |
| ---------- | ----------- | ------------------------------------------------- | --- |
|            | Client IP   | : 20.1.1.2                                        |     |
|            | Client Port | : 58837                                           |     |
| Command    | History     |                                                   |     |
| Release    |             | Modification                                      |     |
| 10.08.1021 |             | Commandintroducedonthe6200,6300,6400SwitchSeries. |     |
Telnetaccess|48

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
| switch(config)# |             | telnet | server  | vrf mgmt                                          |
| --------------- | ----------- | ------ | ------- | ------------------------------------------------- |
| Command         | History     |        |         |                                                   |
| Release         |             |        |         | Modification                                      |
| 10.08.1021      |             |        |         | Commandintroducedonthe6200,6300,6400SwitchSeries. |
| Command         | Information |        |         |                                                   |
| Platforms       | Command     |        | context | Authority                                         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 49

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

n Non-HPE Aruba Networking branded products

n HPE branded products that were designed for non-AOS-CX switch models (e.g. Comware)

n HPE branded products designated for use in HPE Compute Servers or Storage

n Transceivers originally designated for use in HPE Aruba Networking WLAN controllers or former

Mobility Access Switch (MAS) products

n End-of-life HPE Aruba Networking Transceivers

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

50

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
Interfaceconfiguration|51

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 52

5. Applythepersonaconfigurationtotheinterfaceandsetthemodewiththecommandpersona
custom <PERSONA-NAME> <mode>.Notethat<custom>isanoptionalargument,required
onlyifthepersonaisnotoneofthepredefinednames(neitheruplinknoraccess).
Forinformationonthisfeature,seetherelatedvideoontheAirHeadsBroadcastingChannel.
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
Interfaceconfiguration|53

Interface commands

allow-unsupported-transceiver
allow-unsupported-transceiver [confirm | log-interval {none | <INTERVAL>}]
no allow-unsupported-transceiver

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

54

switch(config)# allow-unsupported-transceiver log-interval 2880
Disablingunsupportedtransceiverlogging:
switch(config)# allow-unsupported-transceiver log-interval none
Disallowingunsupportedtransceiverswithfollow-upconfirmation:
| switch(config)# | no  | allow-unsupported-transceivers |     |     |
| --------------- | --- | ------------------------------ | --- | --- |
Warning: Unsupported transceivers, DACs, and AOCs will be disabled,
which could impact network connectivity. Use 'show allow-unsupported-transceiver'
| to identify | unsupported | transceivers, | DACs, and | AOCs. |
| ----------- | ----------- | ------------- | --------- | ----- |
| Ccontinue   | (y/n)?      |               |           |       |
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
5420 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6200
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
Interfaceconfiguration|55

Examples
Resettinganinterface:
| switch(config)# | default |         |           |       |
| --------------- | ------- | ------- | --------- | ----- |
|                 |         | default | interface | 1/1/1 |
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
| switch(config-if)# |     | no description |     |     |
| ------------------ | --- | -------------- | --- | --- |
| Command History    |     |                |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 56

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
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
config
| 5420 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 6200 |     |     | rightsforthiscommand.                              |
flow-control
| flow-control    | rxtx |     |     |
| --------------- | ---- | --- | --- |
| no flow-control | rxtx |     |     |
Description
Interfaceconfiguration|57

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
| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
|     |     | flow-control |     | txrx |
| --- | --- | ------------ | --- | ---- |
DisablingsupportforRXTXflowcontrol:
| switch(config)#     |         | interface       | 1/1/1 |              |
| ------------------- | ------- | --------------- | ----- | ------------ |
| switch(config-if)#  |         | no flow-control |       | txrx         |
| Command History     |         |                 |       |              |
| Release             |         |                 |       | Modification |
| 10.07orearlier      |         |                 |       | --           |
| Command Information |         |                 |       |              |
| Platforms           | Command | context         |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 58

| interface            | (port) |     |     |
| -------------------- | ------ | --- | --- |
| interface <PORT-NUM> |        |     |     |
Description
Switchestotheconfig-ifcontextforaphysicalport.Thisiswhereyoudefinetheconfigurationsettings
forthelogicalinterfaceassociatedwiththephysicalport.
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
Examples
| switch# config  |           |          |     |
| --------------- | --------- | -------- | --- |
| switch(config)# | interface | loopback | 1   |
Interfaceconfiguration|59

switch(config-loopback-if)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200           |                |     | rightsforthiscommand. |
| -------------- | -------------- | --- | --------------------- |
| interface      | vlan           |     |                       |
| interface vlan | <VLAN-ID>      |     |                       |
| no interface   | vlan <VLAN-ID> |     |                       |
Description
CreatesaninterfaceVLANalsoknowasanSVI(switchedvirtualinterface)andchangestotheconfig-if-
vlancontext.ThespecifiedVLANmustalreadybedefinedontheswitch.
ThenoformofthiscommanddeletesaninterfaceVLAN.
| Parameter |     |     | Description                      |
| --------- | --- | --- | -------------------------------- |
| <VLAN-ID> |     |     | SpecifiestheloopbackinterfaceID. |
DonotreserveanyinternalVLANs.
none
Examples
| switch# config          |           |      |     |
| ----------------------- | --------- | ---- | --- |
| switch(config)#         | vlan      | 10   |     |
| switch(config-vlan-10)# |           | exit |     |
| switch(config)#         | interface | vlan | 10  |
switch(config-if-vlan)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 60

| ip address    | (interface)      |     |     |             |     |
| ------------- | ---------------- | --- | --- | ----------- | --- |
| ip address    | <IP-ADDR>/<MASK> |     |     | [secondary] |     |
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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip mtu
ip mtu <VALUE>
no ip mtu
Description
Interfaceconfiguration|61

SetstheIPMTU(maximumtransmissionunit)foraninterface.ThisdefinesthelargestIPpacketthatcan
besentorreceivedbytheinterface.ThisvalueshouldbelessthanorequaltotheoverallMTUforthe
interface.
ThenoformofthiscommandsetstheIPMTUtothedefaultvalue1500.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VALUE>
SpecifiestheIPMTUinbytes.Range:68to9198.Default:1500.
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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 62

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
ntp | syslog | ubt | dhcp-relay | optionsetsaglobaladdressthatappliestoallprotocolsthatdo
simplivity | dns | all nothaveanaddressset.ForDHCPrelay,theaddressisusedas
boththesourceIPandGIADDR.
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
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |
| -------------- | --- | --- | ----------------------- |
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
| ip tcp mss <VALUE> |         |     |     |
| ------------------ | ------- | --- | --- |
| no ip tcp mss      | <VALUE> |     |     |
Description
SetstheTCP(TransmissionControlProtocol)MSS(MaximumSegmentSize)foraninterface.When
configured,theMSS optionintheTCPheaderissetintheTCP handshakefornegotiationduring
connectionestablishment.OncetheTCPsessionisestablished,changingtheTCP MSSvalueonthe
interfacewillnotaffecttheexistingsession.
Interfaceconfiguration|63

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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip unnumbered
| ip unnumbered    | <ifname> |     |     |     |
| ---------------- | -------- | --- | --- | --- |
| no ip unnumbered | <ifname> |     |     |     |
Description
TheIPunnumberedfeatureallowstheswitchtoprocessIPpacketswithoutconfiguringauniqueIP
addressonaninterfacebytellingtheroutertousetheIPaddressofanotherselectedinterfaceasthe
addressforthatlink.Onceset,thisportwillborrowtheuser-configuredprimaryIPv4addressfroman
lenderinterfaceandusethatIP addressinitsL3controlplaneexchange.
ThenoversionofthiscommandremovesIPunnumberedsupportforthisport.Onceunset,thisport
willremoveborrowedIPv4address.
| Parameter |     |     |     | Description        |
| --------- | --- | --- | --- | ------------------ |
| <Ifname > |     |     |     | Nameoftheinterface |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 64

Usage
TheportwhereIPunnumberedisconfiguredisknownastheborrowerinterface.Onlyroute-onlyports
canborrowanaddress.
Theporttheaddressisborrowedfromisknownasthelenderinterface.Onlyaloopbackinterfacecan
beusedasalenderinterface.Theunnumberedinterfaceandlenderinterfacemustbelongtothesame
VRF.Additionally,thelenderinterfaceforanIPunnumberedinterfacecannotitselfconfiguredas
unnumbered.
Thefollowingcaveatsapplytothisfeature:
n OnlytheprimaryIPv4addresscanbeborrowedonanIPunnumberedinterface.Youcannot
configureasecondaryIPaddressforaninterfacethatisalreadyconfiguredasanIPunnumbered
interface.
n IfanIPaddressisconfiguredonaninterfacethatisalreadyconfiguredasanIPunnumbered
interface,itwillfunctionasanormalIPinterface.
n AnIPv6unnumberedconfigurationontheinterfaceisnotsupported.Ifip unnumberedisenabled
ontheinterface,onlytheIPv4addressisborrowed.However,AnyIPv6configurationscanco-exist
withanipunnumberedinterface.
n AnIPunnumberedinterfacecannothavemultiplelenderinterfacesforthesameaddressfamily.
Theip unnumberedcommandrequiresthattheinterfaceborrowingtheaddressisaroutedport.
n
TheIP unnumberedfeatureisonlysupportedondevicesconnectedwithpoint-to-pointinterfaces.
n AnunnumberedIPaddresscannotbeusedastunnelsource.
TheunnumberedinterfaceandlenderinterfacemustbelongtothesameVRF.
n
n DeletingalenderinterfaceremovesalltheassociatedIPunnumberedreferences.
Examples
ConfiguringIPunnumberedforaroute-onlyport:
| switch(config)#    | interface     | 1/1/1 |           |     |
| ------------------ | ------------- | ----- | --------- | --- |
| switch(config-if)# | ip unnumbered |       | loopback1 |     |
ThefollowingexamplesremovesIPunnumberedsupportforthisport.Onceunset,thisportwill
removetheborrowedIPv4address.
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
or
| switch(config)#    | interface  | 1/1/1 |              |     |
| ------------------ | ---------- | ----- | ------------ | --- |
| switch(config-if)# | ip address |       | 10.16.1.1/24 |     |
Interfaceconfiguration|65

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

5420
6200

config-if

Administrators or local user group members with execution
rights for this command.

ipv6 address
ipv6 address <IPV6-ADDR>/<MASK>{eui64 | [tag <ID>]}
no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets an IPv6 address on the interface.

The no form of this command removes the IPv6 address on the interface.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

66

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
no ipv6 source-interface {sflow | tftp | radius | tacacs | ntp | syslog | ubt | dhcp-
relay | simplivity | dns | all} [interface <IFNAME> | <IPV6-ADDR>] [vrf <VRF-NAME>]
Interfaceconfiguration|67

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 68

| switch(config)#     |         | no ip source-interface |     |              | all 2001:DB8::1 |
| ------------------- | ------- | ---------------------- | --- | ------------ | --------------- |
| Command History     |         |                        |     |              |                 |
| Release             |         |                        |     | Modification |                 |
| 10.07orearlier      |         |                        |     | --           |                 |
| Command Information |         |                        |     |              |                 |
| Platforms           | Command | context                |     | Authority    |                 |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<VALUE>
SpecifiestheIPv6TCPMSSinbytes.Range:68to65495.
Examples
ConfiguringtheIPv6TCPMSSfortheinterface:
| switch(config)#    |     | interface | 1/1/1   |      |     |
| ------------------ | --- | --------- | ------- | ---- | --- |
| switch(config-if)# |     | ipv6      | tcp mss | 1440 |     |
RemovingtheIPv6TCPMSSconfigurationfromtheinterface:
| switch(config)#    |     | interface | 1/1/1 |          |     |
| ------------------ | --- | --------- | ----- | -------- | --- |
| switch(config-if)# |     | no ipv6   | tcp   | mss 1440 |     |
| Command History    |     |           |       |          |     |
Interfaceconfiguration|69

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.14.1000          |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 70

Platforms

Command context

Authority

All platforms

config-if

Administrators or local user group members with execution
rights for this command.

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

Interface configuration | 71

n Themodeisonlyavailabletobeconfiguredforaninterfacethatmeetsthefollowingconditions:
o IS aphysicalinterface
o IS NOTaLAGmember
o IS NOTapersonainterface
Examples
Configuringanaccesspersona:
| switch(config)#    | interface | 1/1/1  |     |     |
| ------------------ | --------- | ------ | --- | --- |
| switch(config-if)# | persona   | access |     |     |
Configuringanuplinkpersona:
| switch(config)#    | interface | 1/1/1  |     |     |
| ------------------ | --------- | ------ | --- | --- |
| switch(config-if)# | persona   | uplink |     |     |
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
| switch(config)#    | interface | 1/1/1  |           |      |
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 72

2.Applyingthe"mypersona"configurationwithattachmode:
| switch(config)#     |         | interface 1/1/1-1/1/24 |                                      |        |
| ------------------- | ------- | ---------------------- | ------------------------------------ | ------ |
| switch(config-if)#  |         | persona custom         | mypersona                            | attach |
| switch(config-if)#  |         | exit                   |                                      |        |
| Command History     |         |                        |                                      |        |
| Release             |         |                        | Modification                         |        |
| 10.10               |         |                        | Addedoptionalparameters:attach,copy. |        |
| 10.09               |         |                        | Commandintroduced.                   |        |
| Command Information |         |                        |                                      |        |
| Platforms           | Command | context                | Authority                            |        |
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
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<VALUE>
Thestatisticsratecollectionintervalinseconds.Thesupported
rangeis5-300seconds,wherethenumberofsecondsisa
multipleoffive.
Examples
Settingtheratecollectionintervalto50seconds
| switch(config)#    |     | interface 1/1/1 |     |     |
| ------------------ | --- | --------------- | --- | --- |
| switch(config-if)# |     | rate-interval   | 50  |     |
Settingtheratecollectionintervaltothedefaultvalue:
| switch(config-if)# |     | no rate-interval |     |     |
| ------------------ | --- | ---------------- | --- | --- |
Interfaceconfiguration|73

Thefollowingexampleshowsthecommand-lineinterfacewarningthatappearswhileconfiguringan
invalidrate-interval.
| switch(config)#    |      | interface | 1/1/1    |       |
| ------------------ | ---- | --------- | -------- | ----- |
| switch(config-if)# |      | rate      | interval | 6     |
| The interval       | must | be a      | multiple | of 5. |
Usage
Theratecollectionintervalmustbeconfiguredinthemultiplesof5.Anyothervaluewillberejectedand
theCLIwilldisplaytheerrormessage,The interval must be a multiple of 5.
| Command History     |         |         |     |                                             |
| ------------------- | ------- | ------- | --- | ------------------------------------------- |
| Release             |         |         |     | Modification                                |
| 10.12.1000          |         |         |     | Commandsupportedonallplatforms.             |
| 10.12               |         |         |     | CommandIntroducedon6300and8360Switchseries. |
| Command Information |         |         |     |                                             |
| Platforms           | Command | context |     | Authority                                   |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| routing (interface) |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
routing
no routing
Description
Enablesroutingsupportonaninterface,creatingaL3(layer3)interfaceonwhichtheswitchcanroute
IPv4/IPv6traffictootherdevices.
Bydefault,routingisdisabledonallinterfaces.
Thenoformofthiscommanddisablesroutingsupportonaninterface,creatingaL2(layer2)interface.
Ifyouenablethisconfiguration,collectionofflowtrackingstatisticsisdisabled.
Examples
Enablingroutingsupportonaninterface:
| switch(config-if)# |     | routing |     |     |
| ------------------ | --- | ------- | --- | --- |
Disablingroutingsupportonaninterface:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 74

| switch(config-if)# |             | no routing |     |              |
| ------------------ | ----------- | ---------- | --- | ------------ |
| Command            | History     |            |     |              |
| Release            |             |            |     | Modification |
| 10.07orearlier     |             |            |     | --           |
| Command            | Information |            |     |              |
| Platforms          | Command     | context    |     | Authority    |
5420 config-if Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
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
| 1/1/31         | SFP-SX     |     | unsupported-allowed |              |
| -------------- | ---------- | --- | ------------------- | ------------ |
| 1/1/32         | SFP-1G-BXD |     | unsupported-allowed |              |
| 1/1/2          | SFP28DAC3  |     | unsupported         |              |
| Command        | History    |     |                     |              |
| Release        |            |     |                     | Modification |
| 10.07orearlier |            |     |                     | --           |
Interfaceconfiguration|75

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
| Parameter |     |     | Description              |
| --------- | --- | --- | ------------------------ |
| <IFNAME>  |     |     | Specifiesainterfacename. |
<IFRANGE>
Specifiestheportidentifierrange.
| brief |     |     | Showsbriefinfointabularformat. |
| ----- | --- | --- | ------------------------------ |
physical
Showsthephysicalconnectioninfointabularformat.
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
| non-zero |     |     | Showsonlynonzerostatistics.             |
| -------- | --- | --- | --------------------------------------- |
| LAG      |     |     | ShowsLAGinterfaceinformation.           |
| monitor  |     |     | Continuouslymonitorinterfacestatistics. |
| LOOPBACK |     |     | Showsloopbackinterfaceinformation.      |
| TUNNEL   |     |     | Showstunnelinterfaceinformation.        |
| VLAN     |     |     | ShowsVLANinterfaceinformation.          |
| <LAG-ID> |     |     | SpecifiestheLAGnumber.Range:1-256       |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 76

| Parameter     |     |     |     | Description                                    |     |     |     |     |
| ------------- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
| <LOOPBACK-ID> |     |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |     |     |     |     |
| <TUNNEL-ID>   |     |     |     | SpecifiesthetunnelID.Range:1-255               |     |     |     |     |
| <VLAN-ID>     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |     |     |     |
| VXLAN         |     |     |     | ShowstheVXLANinterfaceinformation.             |     |     |     |     |
| <VXLAN-ID>    |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |     |     |
Examples
Showinginformationwheninterface1/1/1isconfigured:
| MDI mode:       | MDIX            |           |     |         |     |     |       |         |
| --------------- | --------------- | --------- | --- | ------- | --- | --- | ----- | ------- |
| VLAN Mode:      | native-untagged |           |     |         |     |     |       |         |
| Native VLAN:    | 1               |           |     |         |     |     |       |         |
| Allowed VLAN    | List:           | all       |     |         |     |     |       |         |
| Rate collection |                 | interval: | 300 | seconds |     |     |       |         |
| Rates           |                 |           |     | RX      |     | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits / sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts / sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
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
| Errors       |     |     |     | 0   |     | 0   |     | 0   |
| CRC/FCS      |     |     |     | 0   |     | n/a |     | 0   |
| Collision    |     |     |     | n/a |     | 0   |     | 0   |
| Runts        |     |     |     | 0   |     | n/a |     | 0   |
| Giants       |     |     |     | 0   |     | n/a |     | 0   |
Showinginformationwhentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |       |     |     |     |     |
...
| Auto-negotiation |     | is on | with | downshift | active |     |     |     |
| ---------------- | --- | ----- | ---- | --------- | ------ | --- | --- | --- |
Showinginformationwhentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
Interfaceconfiguration|77

| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |     |
...
| Energy-Efficient |     |     | Ethernet | is  | enabled and | active |     |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
ShowinginformationwhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 | physical |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | ----- | -------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------------------------------------
|        |     |          |           | Link   | Admin       |     |             | Speed    |        | Flow-Control |        |
| ------ | --- | -------- | --------- | ------ | ----------- | --- | ----------- | -------- | ------ | ------------ | ------ |
|        | EEE |          | PoE Power |        |             |     | Port        |          |        |              |        |
| Port   |     |          | Type      | Status | Config      |     | Status      | | Config | Status | |            | Config |
| Status |     | | Config | (Watts)   | State  | Information |     | Description |          |        |              |        |
----------------------------------------------------------------------------------
----------------------------------------------------------
| 1/1/1 |     |     | 1GbT | up          | up  |     | 1G  | auto | off |     | off |
| ----- | --- | --- | ---- | ----------- | --- | --- | --- | ---- | --- | --- | --- |
| on    |     | on  | --   | 10M/100M/1G |     |     | --  |      |     |     |     |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| Interface |     | 1/1/1 | is up |     |     |     |     |     |     |       |         |
| --------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | ----- | ------- |
| Rate      |     |       |       |     | RX  |     |     | TX  |     | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| MBits       | /   | sec |     |     | 30196.43 |     |     | 30196.43 |     | 60392.85  |         |
| ----------- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --------- | ------- |
| MPkts       | /   | sec |     |     | 58977.39 |     |     | 58977.40 |     | 117954.79 |         |
| Unicast     |     |     |     |     | 0.00     |     |     | 0.00     |     |           | 0.00    |
| Multicast   |     |     |     |     | 58977.39 |     |     | 58977.40 |     | 117954.79 |         |
| Broadcast   |     |     |     |     | 0.00     |     |     | 0.00     |     |           | 0.00    |
| Utilization |     |     | %   |     | 75.49    |     |     | 75.49    |     |           | 150.98  |
| Statistic   |     |     |     |     | RX       |     |     | TX       |     | Total     | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Packets   |        |                |             | 4756527649   |     |     | 4756527865   |     |     | 9513055514   |     |
| --------- | ------ | -------------- | ----------- | ------------ | --- | --- | ------------ | --- | --- | ------------ | --- |
| Unicast   |        |                |             |              | 0   |     |              | 0   |     |              | 0   |
| Multicast |        |                |             | 4756527649   |     |     | 4756527865   |     |     | 9513055514   |     |
| Broadcast |        |                |             |              | 2   |     |              | 0   |     |              | 2   |
| Bytes     |        |                |             | 304417778668 |     |     | 304417795428 |     |     | 608835574096 |     |
| Jumbos    |        |                |             |              | 0   |     |              | 0   |     |              | 0   |
| Dropped   |        |                |             |              | 0   |     | 19028847730  |     |     | 19028847730  |     |
| Pause     | Frames |                |             |              | 0   |     |              | 0   |     |              | 0   |
| Errors    |        |                |             |              | 0   |     |              | 0   |     |              | 0   |
| CRC/FCS   |        |                |             |              | 0   |     |              | n/a |     |              | 0   |
| help:     | ?,     | quit:          | q           |              |     |     |              |     |     |              |     |
| Help      | for    | Interface      | Monitor     |              |     |     |              |     |     |              |     |
| h         | Toggle | human-readable |             | mode         |     |     |              |     |     |              |     |
| c         | Clear  | interface      | statistics  |              |     |     |              |     |     |              |     |
| Does      | not    | apply          | to rates    |              |     |     |              |     |     |              |     |
| Arrows,   |        | PgUp,          | PgDn, Home, | End          |     |     |              |     |     |              |     |
| Navigate  |        | interface      | statistics  |              |     |     |              |     |     |              |     |
Delay: 2
| help: | ?,  | quit: | q   |     |     |     |     |     |     |     |     |
| ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 78

Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the<1symbolforUtilizationindicatesthattheamountofpacketsisbetweenzero
andone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |       |         |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | ----- | ------- |
| Interface          | 1/1/1 | is up |           |                      |     |     |       |         |
| Rate               |       |       |           | RX                   |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Bits / sec  |     |     |     | 3M  |     | 3M  |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts / sec  |     |     |     | 316 |     | 316 |     | 633   |
| Unicast     |     |     |     | 319 |     | 319 |     | 638   |
| Multicast   |     |     |     | 0   |     | 0   |     | 0     |
| Broadcast   |     |     |     | 0   |     | 0   |     | 0     |
| Utilization | %   |     |     | < 1 |     | < 1 |     | < 1   |
| Statistic   |     |     |     | RX  |     | TX  |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 577K |     | 577K |     | 1M  |
| ------------ | --- | --- | --- | ---- | --- | ---- | --- | --- |
| Unicast      |     |     |     | 577K |     | 577K |     | 1M  |
| Multicast    |     |     |     | 0    |     | 51   |     | 51  |
| Broadcast    |     |     |     | 0    |     | 15   |     | 15  |
| Bytes        |     |     |     | 744M |     | 745M |     | 1G  |
| Jumbos       |     |     |     | 0    |     | 0    |     | 0   |
| Dropped      |     |     |     | 0    |     | 0    |     | 0   |
| Filtered     |     |     |     | 0    |     | 0    |     | 0   |
| Pause Frames |     |     |     | 0    |     | 0    |     | 0   |
| Errors       |     |     |     | 0    |     | 0    |     | 0   |
| CRC/FCS      |     |     |     | 0    |     | n/a  |     | 0   |
| Collision    |     |     |     | n/a  |     | 0    |     | 0   |
| Runts        |     |     |     | 0    |     | n/a  |     | 0   |
| Giants       |     |     |     | 0    |     | n/a  |     | 0   |
Showinginformationaboutextendedcounters:
Theoutputoftheshow interface extendedcommandvariesdependingontheswitchmodeland
configuration.
| switch(config-if)# |     | show | interface | 1/1/17 extended |     |     |     |     |
| ------------------ | --- | ---- | --------- | --------------- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Interface | 1/1/17 |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Statistics |     |     |     |     | Value |     |     |     |
| ---------- | --- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Tp | Port In         | Frames |         |     | 547   |     |     |     |
| -------- | --------------- | ------ | ------- | --- | ----- | --- | --- | --- |
| Dot1d Tp | Port Out        | Frames |         |     | 608   |     |     |     |
| Dot3 In  | Pause Frames    |        |         |     | 0     |     |     |     |
| Dot3 Out | Pause Frames    |        |         |     | 0     |     |     |     |
| Ethernet | Stats Broadcast |        | Packets |     | 19    |     |     |     |
| Ethernet | Stats Bytes     |        |         |     | 40162 |     |     |     |
| Ethernet | Stats Packets   |        |         |     | 342   |     |     |     |
...
-------------------------------------------------------------------
| Error-Statistics |     |     |     |     | Value |     |     |     |
| ---------------- | --- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Base | Port | MTU Exceeded | Discards |     | 0   |     |     |     |
| ---------- | ---- | ------------ | -------- | --- | --- | --- | --- | --- |
Interfaceconfiguration|79

| Dot3 Control | In Unknown  | Opcodes      |        | 0   |     |     |
| ------------ | ----------- | ------------ | ------ | --- | --- | --- |
| Dot3 Stats   | Alignment   | Errors       |        | 0   |     |     |
| Dot3 Stats   | FCS Errors  |              |        | 0   |     |     |
| Dot3 Stats   | Frame Too   | Longs        |        | 0   |     |     |
| Dot3 Stats   | Internal    | Mac Transmit | Errors | 0   |     |     |
| Ethernet     | RX Oversize | Packets      |        | 0   |     |     |
...
Showinginterfacelink-status:
| switch# | show interface | link-status |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------
| Port | Type |     | Physical   | Link        | Last   |     |
| ---- | ---- | --- | ---------- | ----------- | ------ | --- |
|      |      |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/1    | 1G-BT     |     | down | 0   | --       |                 |
| -------- | --------- | --- | ---- | --- | -------- | --------------- |
| 1/1/2    | 1G-BT     |     | up   | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |      |     |          |                 |
| 1/1/3    | 1G-BT     |     | up   | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |      |     |          |                 |
| 1/1/4    | --        |     | down | 0   | --       |                 |
| 1/1/5    | --        |     | down | 0   | --       |                 |
Showinginterfaceloopback1link-status:
-------------------------------------------------------------
|      |      |     | Physical   | Link        | Last   |     |
| ---- | ---- | --- | ---------- | ----------- | ------ | --- |
| Port | Type |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| loopback1 | --  |     | up  | --  | --  |     |
| --------- | --- | --- | --- | --- | --- | --- |
Showinginterface1/1/2-1/1/3link-status:
-------------------------------------------------------------
|      |      |     | Physical   | Link        | Last   |     |
| ---- | ---- | --- | ---------- | ----------- | ------ | --- |
| Port | Type |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/2    | 1G-BT     |     | up  | 1   | 1 minute | ago (Fri Mar 09 |
| -------- | --------- | --- | --- | --- | -------- | --------------- |
| 12:36:56 | UTC 2018) |     |     |     |          |                 |
| 1/1/3    | 1G-BT     |     | up  | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |     |     |          |                 |
Showinginterfacelink-status:
| switch# | show interface | link-status |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Port | Type |     | Physical   | Link        | Link Flaps | Last   |
| ---- | ---- | --- | ---------- | ----------- | ---------- | ------ |
|      |      |     | Link State | Transitions | Ignored    | Change |
-------------------------------------------------------------------------
| 1/1/1    | 1G-BT       |           | down | 0   | 0   | --           |
| -------- | ----------- | --------- | ---- | --- | --- | ------------ |
| 1/1/2    | 1G-BT       |           | up   | 1   | 0   | 1 minute ago |
| (Fri Mar | 09 12:36:56 | UTC 2018) |      |     |     |              |
| 1/1/3    | 1G-BT       |           | up   | 1   | 0   | 1 minute ago |
| (Fri Mar | 09 12:36:56 | UTC 2018) |      |     |     |              |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 80

| 1/1/4 |     | --  |     |     | down |     | 0   | 0   | --  |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| 1/1/5 |     | --  |     |     | down |     | 0   | 0   | --  |     |
Showingstateinformationwheninterfaceisblocked:
| 8360(config-if)#   |       |       | show interface |     | 1/1/1 |     |     |     |     |     |
| ------------------ | ----- | ----- | -------------- | --- | ----- | --- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is    | up (Blocked)   |     |       |     |     |     |     |     |
| Admin state        |       | is up |                |     |       |     |     |     |     |     |
| State information: |       |       | Blocked        | by  | UDLD  |     |     |     |     |     |
Link state: up for 1 minute (since Mon Jun 10 09:25:27 UTC 2024)
| Link transitions: |     |     | 1   |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
Persona:
| Hardware: | Ethernet, |     | MAC | Address: |     | 00:fd:45:67:85:91 |     |     |     |     |
| --------- | --------- | --- | --- | -------- | --- | ----------------- | --- | --- | --- | --- |
MTU 1500
| Type 10G-LR |     | / 10G | SFP+ | LR  |     |     |     |     |     |     |
| ----------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
Full-duplex
| qos trust        | none   |           |        |     |         |     |     |     |       |         |
| ---------------- | ------ | --------- | ------ | --- | ------- | --- | --- | --- | ----- | ------- |
| Speed 10000      |        | Mb/s      |        |     |         |     |     |     |       |         |
| Auto-negotiation |        |           | is off |     |         |     |     |     |       |         |
| Flow-control:    |        | off       |        |     |         |     |     |     |       |         |
| Error-control:   |        | off       |        |     |         |     |     |     |       |         |
| VLAN Mode:       | access |           |        |     |         |     |     |     |       |         |
| Access           | VLAN:  | 1         |        |     |         |     |     |     |       |         |
| Rate collection  |        | interval: |        | 300 | seconds |     |     |     |       |         |
| Rate             |        |           |        |     |         | RX  |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization |     | %   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistic   |     |     |     |     |     | RX   |     | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |         |     |     |     |     | 15                                              |     | 15   |     | 30   |
| ------------ | ------- | --- | --- | --- | --- | ----------------------------------------------- | --- | ---- | --- | ---- |
| Unicast      |         |     |     |     |     | 12                                              |     | 12   |     | 24   |
| Multicast    |         |     |     |     |     | 3                                               |     | 3    |     | 6    |
| Broadcast    |         |     |     |     |     | 0                                               |     | 0    |     | 0    |
| Bytes        |         |     |     |     |     | 1350                                            |     | 1350 |     | 2700 |
| Jumbos       |         |     |     |     |     | 0                                               |     | 0    |     | 0    |
| Dropped      |         |     |     |     |     | 0                                               |     | 0    |     | 0    |
| Pause Frames |         |     |     |     |     | 0                                               |     | 0    |     | 0    |
| Errors       |         |     |     |     |     | 0                                               |     | 0    |     | 0    |
| CRC/FCS      |         |     |     |     |     | 0                                               |     | n/a  |     | 0    |
| Collision    |         |     |     |     |     | n/a                                             |     | 0    |     | 0    |
| Runts        |         |     |     |     |     | 0                                               |     | n/a  |     | 0    |
| Giants       |         |     |     |     |     | 0                                               |     | n/a  |     | 0    |
| Command      | History |     |     |     |     |                                                 |     |      |     |      |
| Release      |         |     |     |     |     | Modification                                    |     |      |     |      |
| 10.15        |         |     |     |     |     | Addedstateinformationwhenportgoesintodownstate. |     |      |     |      |
10.11
Addedmonitorparameter.
Interfaceconfiguration|81

| Release             |         |         |     | Modification                  |     |     |
| ------------------- | ------- | ------- | --- | ----------------------------- | --- | --- |
| 10.10               |         |         |     | Addedhuman-readableparameter. |     |     |
| 10.07orearlier      |         |         |     | --                            |     |     |
| Command Information |         |         |     |                               |     |     |
| Platforms           | Command | context |     | Authority                     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface |                  | dom |     |          |     |     |
| -------------- | ---------------- | --- | --- | -------- | --- | --- |
| show interface | [<INTERFACE-ID>] |     | dom | [detail] |     |     |
Description
Showsdiagnosticsinformationandalarm/warningflagsfortheopticaltransceivers(SFP,SFP+,QSFP+).
ThisinformationisknownasDOM(DigitalOpticalMonitoring).DOMinformationalsoconsistsofvendor
determinedthresholdswhichtriggerhigh/lowalarmsandwarningflags.
| Parameter      |     |     |     | Description                                   |     |     |
| -------------- | --- | --- | --- | --------------------------------------------- | --- | --- |
| <INTERFACE-ID> |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |
detail
Showdetailedinformation.
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
| 2                   |          |     | 44.46 | 3.30 6.04    | 0.08, -10.96 | 0.63, -2.00 |
| 3                   |          |     | 44.46 | 3.30 6.51    | 0.08, -10.96 | 0.60, -2.16 |
| 4                   |          |     | 44.46 | 3.30 6.19    | 0.08, -10.96 | 0.63, -1.94 |
| Command History     |          |     |       |              |              |             |
| Release             |          |     |       | Modification |              |             |
| 10.07orearlier      |          |     |       | --           |              |             |
| Command Information |          |     |       |              |              |             |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 82

| Platforms | Command |     | context |     | Authority |     |     |     |
| --------- | ------- | --- | ------- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                      | energy-efficient |     |     |                           | ethernet |     |     |
| -------------- | -------------------- | ---------------- | --- | --- | ------------------------- | -------- | --- | --- |
| show interface | [<IFNAME>|<IFRANGE>] |                  |     |     | energy-efficient-ethernet |          |     |     |
Description
DisplaysEnergy-EfficientEthernetinformationfortheinterface.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<IFNAME> Specifiesthenameofaninterfaceontheswitch.Usetheformat
member/slot/port(forexample,1/1/1).
<IFRANGE> Specifiestheportidentifierrangeofaninterfaceontheswitch.
Usetheformatmember/slot/port(forexample,1/1/1).
Example
ThefollowingexampleshowswhentheinterfacesareEnergy-EfficientEthernetcapable.
| switch# | show | interface | energy-efficient-ethernet |     |     |     |     |     |
| ------- | ---- | --------- | ------------------------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Port | Enabled |     | Negotiated |     | Speed  |     | TX Wake  | RX Wake   |
| ---- | ------- | --- | ---------- | --- | ------ | --- | -------- | --------- |
|      |         |     |            |     | (MB/s) |     | Time(us) | Time (us) |
-------------------------------------------------------------------
| 1/1/1 | no  |     | no  |     | --   |     | --  | --  |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- |
| 1/1/2 | yes |     | yes |     | 100  |     | 36  | 36  |
| 1/1/3 | yes |     | yes |     | 1000 |     | 17  | 17  |
| 1/1/4 | no  |     | no  |     | --   |     | --  | --  |
| 1/1/5 | yes |     | no  |     | 1000 |     | --  | --  |
ThefollowingexampleshowswhentheinterfaceisnotEnergy-EfficientEthernetcapable:
| switch#        | show        | interface | 1/1/1   | energy-efficient-ethernet |              |     |     |     |
| -------------- | ----------- | --------- | ------- | ------------------------- | ------------ | --- | --- | --- |
| Port 1/1/1     | does        | not       | support | Energy-Efficient-Ethernet |              |     |     |     |
| Command        | History     |           |         |                           |              |     |     |     |
| Release        |             |           |         |                           | Modification |     |     |     |
| 10.07orearlier |             |           |         |                           | --           |     |     |     |
| Command        | Information |           |         |                           |              |     |     |     |
Interfaceconfiguration|83

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
5420 config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6200 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show interface | flow-control          |     |              |          |
| -------------- | --------------------- | --- | ------------ | -------- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | flow-control | [detail] |
Description
Showstheflowcontrolconfiguration,status,andstatisticsofthespecifiedinterfaceforinterfaceson
whichflowcontrolisenabled.
Ifdetailisnotspecified,thiscommandshowsasummaryofallflowcontrolledinterfaceswithoneinterfaceper
line.Ifdetailisspecified,thiscommandshowsflowcontroldetailedstatistics.
AsofAOS-CX10.10,theseparateshowflow-controlcommandhasbeenremoved,withitbeingeffectively
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
| ----------- | ------------------------------------- |              |     |     |
| ----------- | ------------------------------------- | ------------ | --- | --- |
| 1/1/1       | config:                               | pfc rxtx-1,2 |     |     |
|             | status:                               | pfc rxtx-1,2 |     |     |
| 1/1/2       | config:                               | pfc rxtx-5   |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 84

|     | status: | none |     |     |     |     |     |
| --- | ------- | ---- | --- | --- | --- | --- | --- |
ShowingsummaryflowcontrolinformationwithPFC:
| switch# show | interface |     | flow-control     |     |     |     |     |
| ------------ | --------- | --- | ---------------- | --- | --- | --- | --- |
| Flow Control | Watchdog  |     | Settings         |     |     |     |     |
| Trigger      | Timeout:  |     | 100 milliseconds |     |     |     |     |
| Resume       | Time:     |     | 100 milliseconds |     |     |     |     |
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
| 1/1/10   | config: | pfc  | rxtx-1,2 |     | enabled      |     | 1234 |
|          | status: | pfc  | rxtx-1,2 |     |              |     |      |
| 1/1/12   | config: | pfc  | rxtx-1,2 |     | error        |     | 0    |
|          | status: | pfc  | rxtx-1,2 |     |              |     |      |
| 1/1/32:4 | config: | pfc  | rxtx-5   |     |              |     |      |
|          | status: | pfc  | rxtx-5   |     |              |     |      |
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
| Flow-control: | llfc | rx  |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- | --- |
Interfaceconfiguration|85

| Statistics           |        |                      | RX  |     |
| -------------------- | ------ | -------------------- | --- | --- |
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
| Priority             | 7 Pauses |                      | 0                    | 0   |
| Total Pause          | Frames   |                      | 0                    | 0   |
ShowingdetailedflowcontrolinformationwithPFCenabledandflowcontrolwatchdogdisabled:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 86

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
| Priority             | 5 Pauses  |                      | 0                    | 0   |
| Priority             | 6 Pauses  |                      | 0                    | 0   |
| Priority             | 7 Pauses  |                      | 0                    | 0   |
| Total Pause          | Frames    |                      | 0                    | 0   |
| Interface            | 1/1/1 is  | up                   |                      |     |
| Admin state          | is up     |                      |                      |     |
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
Interfaceconfiguration|87

| Queue 1 |     |     | 0   |     |
| ------- | --- | --- | --- | --- |
| Queue 2 |     |     | 0   |     |
| Queue 3 |     |     | 0   |     |
| Queue 4 |     |     | 0   |     |
| Queue 5 |     |     | 0   |     |
| Queue 6 |     |     | 0   |     |
| Queue 7 |     |     | 0   |     |
Showingdetailedflowcontrolinformationwhenflowcontrolwatchdogisenabledintheconfiguration
butitcouldnotbeappliedbecausetheconfiguredflowcontrolmodeisnotcompatiblewithwatchdog:
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 88

| Parameter        |     | Description                      |     |     |     |     |
| ---------------- | --- | -------------------------------- | --- | --- | --- | --- |
| <IFNAME>         |     | Specifiesainterfacename.         |     |     |     |     |
| <IFRANGE>        |     | Specifiestheportidentifierrange. |     |     |     |     |
| link-diagnostics |     | Showslinkdiagnosticsinformation. |     |     |     |     |
Examples
Showinginterfaceinformationfor1/1/12linkdiagnostics:
| switch# | show interface | 1/1/12 link-diagnostics |     |     |     |     |
| ------- | -------------- | ----------------------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| Interface | 1/1/12 | Current State |     | Changes | Last Change |     |
| --------- | ------ | ------------- | --- | ------- | ----------- | --- |
----------------------------------------------------------------------------------
| Port Status |        | Waiting for | link |     |     |     |
| ----------- | ------ | ----------- | ---- | --- | --- | --- |
| Link Down   | Reason | Local fault |      |     |     |     |
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
| Interface | 1/1/12 | Current State |     | Changes | Last Change |     |
| --------- | ------ | ------------- | --- | ------- | ----------- | --- |
----------------------------------------------------------------------------------
| Port Status |        | Link up |     |     |     |     |
| ----------- | ------ | ------- | --- | --- | --- | --- |
| Link Down   | Reason | --      |     |     |     |     |
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
Interfaceconfiguration|89

| No RX Lock  |                 | --        |     | 2   | 22 seconds |     |
| ----------- | --------------- | --------- | --- | --- | ---------- | --- |
| ago (Tue    | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Remote      | Fault           | --        |     | 2   | 21 seconds |     |
| ago (Tue    | Nov 14 14:30:49 | UTC 2023) |     |     |            |     |
| Local Fault |                 | --        |     | 2   | 22 seconds |     |
| ago (Tue    | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Link        | State           | Up        |     | 1   | 16 seconds |     |
| ago (Tue    | Nov 14 14:30:54 | UTC 2023) |     |     |            |     |
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
| No RX          | Lock            | --        |     | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Remote         | Fault           | --        |     | 2   | 21 seconds |     |
| ago (Tue       | Nov 14 14:30:49 | UTC 2023) |     |     |            |     |
| Local          | Fault           | --        |     | 2   | 22 seconds |     |
| ago (Tue       | Nov 14 14:30:48 | UTC 2023) |     |     |            |     |
| Link State     |                 | Up        |     | 1   | 16 seconds |     |
| ago (Tue       | Nov 14 14:30:54 | UTC 2023) |     |     |            |     |
--------------------------------------------------------------------------------
| Interface | 1/1/8 | Current | State | Changes | Last Change |     |
| --------- | ----- | ------- | ----- | ------- | ----------- | --- |
--------------------------------------------------------------------------------
| Port Status |        | Link | up  |     |     |     |
| ----------- | ------ | ---- | --- | --- | --- | --- |
| Link Down   | Reason | --   |     |     |     |     |
Transceiver
| No transceiver |             | --        |     | 0   | --         |     |
| -------------- | ----------- | --------- | --- | --- | ---------- | --- |
| TX Fault       |             | --        |     | 0   | --         |     |
| Transceiver    | error       | --        |     | 0   | --         |     |
| System         | error       | --        |     | 0   | --         |     |
| DOM error      |             | --        |     | 0   | --         |     |
| Configuring    | transceiver | --        |     | 0   | --         |     |
| Transceiver    | disabled    | --        |     | 0   | --         |     |
| Transceiver    | unsupported | --        |     | 0   | --         |     |
| MAC and        | PHY         |           |     |     |            |     |
| TX Disabled    |             | --        |     | 2   | 22 seconds | ago |
| (Tue Nov       | 14 14:30:48 | UTC 2023) |     |     |            |     |
| Autoneg        | Incomplete  | --        |     | 0   | --         |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 90

| No Signal   | Detected    | --        |                    | 2   | 22 seconds | ago |
| ----------- | ----------- | --------- | ------------------ | --- | ---------- | --- |
| (Tue Nov    | 14 14:30:48 | UTC 2023) |                    |     |            |     |
| No RX Lock  |             | --        |                    | 2   | 22 seconds | ago |
| (Tue Nov    | 14 14:30:48 | UTC 2023) |                    |     |            |     |
| Remote      | Fault       | --        |                    | 2   | 21 seconds | ago |
| (Tue Nov    | 14 14:30:49 | UTC 2023) |                    |     |            |     |
| Local Fault |             | --        |                    | 2   | 22 seconds | ago |
| (Tue Nov    | 14 14:30:48 | UTC 2023) |                    |     |            |     |
| Link State  |             | Up        |                    | 1   | 16 seconds | ago |
| (Tue Nov    | 14 14:30:54 | UTC 2023) |                    |     |            |     |
| Command     | History     |           |                    |     |            |     |
| Release     |             |           | Modification       |     |            |     |
| 10.14       |             |           | Commandintroduced. |     |            |     |
| Command     | Information |           |                    |     |            |     |
| Platforms   | Command     | context   | Authority          |     |            |     |
OperatorsorAdministratorsorlocalusergroupmemberswith
| 9300P | Operator(>)orManager |     |                                                       |     |     |     |
| ----- | -------------------- | --- | ----------------------------------------------------- | --- | --- | --- |
|       | (#)                  |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
commandfromtheoperatorcontext(>)only.
| show interface | statistics |     |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- | --- |
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
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE> |     |     | Specifiestheportidentifierrange. |     |     |     |
| --------- | --- | --- | -------------------------------- | --- | --- | --- |
LAG
ShowsLAGinterfaceinformation.
| <LAG-ID> |     |     | SpecifiestheLAGnumber.Range:1-256 |     |     |     |
| -------- | --- | --- | --------------------------------- | --- | --- | --- |
VXLAN
ShowstheVXLANinterfaceinformation.
| <VXLAN-ID> |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |     |
| ---------- | --- | --- | ---------------------------------------------- | --- | --- | --- |
Interfaceconfiguration|91

Parameter

monitor

human-readable

non-zero

Examples

Showing statistics of all interfaces:

Description

Continuously monitor interface statistics.

Shows statistics rounded to the nearest power of 1000, for
example, 1K, 345M, 2G.

Shows only non zero statistics.

Showing statistics of all interfaces with only non-zero statistics:

Showing statistics of all interfaces in the human-readable format:

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

92

Showing monitor statistics:

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

Showing monitor error statistics in human-readable format:

Interface configuration | 93

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
show interface [<INTERFACE-ID>] transceiver [detail | threshold-violations]
Description
Displaysinformationabouttransceiverspresentintheswitch.Theinformationshownvariesfor
differenttransceivertypesandmanufacturers.OnlybasicinformationisshownforunsupportedHPE
andthird-partytransceiversinstalledintheswitchandtheyarealsoidentifiedwithanasteriskinthe
output.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 94

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameorrangeofaninterfaceontheswitch.Usethe
formatmember/slot/port(forexample,1/3/1).
detail
Showdetailedinformationfortheinterfaces.
| threshold-violations |     |     | Showthresholdviolationsfortransceivers. |     |     |
| -------------------- | --- | --- | --------------------------------------- | --- | --- |
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
| Temperature | : 47.65C    |           |     |     |     |
| ----------- | ----------- | --------- | --- | --- | --- |
| Voltage     | : 3.31V     |           |     |     |     |
| Tx Bias     | : 8.40mA    |           |     |     |     |
| Rx Power    | : 0.08mW,   | -10.96dBm |     |     |     |
| Tx Power    | : 0.56mW,   | -2.49dBm  |     |     |     |
| Recent      | Alarms :    |           |     |     |     |
| Rx power    | low alarm   |           |     |     |     |
| Rx power    | low warning |           |     |     |     |
| Recent      | Errors :    |           |     |     |     |
| Rx loss     | of signal   |           |     |     |     |
| Transceiver | in 1/1/2    |           |     |     |     |
| Interface   | Name        | : 1/1/2   |     |     |     |
| Type        |             | : unknown |     |     |     |
| Connector   | Type        | : ??      |     |     |     |
| Wavelength  |             | : ??      |     |     |     |
| Transfer    | Distance    | : ??      |     |     |     |
Interfaceconfiguration|95

| Diagnostic  | Support  | : ??        |           |           |            |
| ----------- | -------- | ----------- | --------- | --------- | ---------- |
| Product     | Number   | : ??        |           |           |            |
|    Serial   | Number   | : ??        |           |           |            |
| Part        | Number   | : ??        |           |           |            |
| Transceiver | in 1/2/1 |             |           |           |            |
| Interface   | Name     | : 1/2/1     |           |           |            |
| Type        |          | : QSFP+SR4  |           |           |            |
| Connector   | Type     | : MPO       |           |           |            |
| Wavelength  |          | : 850nm     |           |           |            |
| Transfer    | Distance | : 0m (SMF), | 0m (OM1), | 0m (OM2), | 100m (OM3) |
| Diagnostic  | Support  | : DOM       |           |           |            |
| Product     | Number   | : JH233A    |           |           |            |
| Serial      | Number   | : MYxxxxxxx |           |           |            |
| Part        | Number   | : 2005-1234 |           |           |            |
Status
| Temperature | : 44.46C |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
| Voltage     | : 3.30V  |     |     |     |     |
----------------------------------------------
|          | Tx Bias | Rx Power | Tx Power |     |     |
| -------- | ------- | -------- | -------- | --- | --- |
| Channel# | (mA)    | (mW/dBm) | (mW/dBm) |     |     |
----------------------------------------------
| 1           | 6.12        | 0.00, -inf | 0.63, -1.95 |     |     |
| ----------- | ----------- | ---------- | ----------- | --- | --- |
| 2           | 6.04        | 0.00, -inf | 0.63, -2.00 |     |     |
| 3           | 6.51        | 0.00, -inf | 0.60, -2.16 |     |     |
| 4           | 6.19        | 0.00, -inf | 0.63, -1.94 |     |     |
| Recent      | Alarms :    |            |             |     |     |
| Channel     | 1 :         |            |             |     |     |
| Rx power    | low alarm   |            |             |     |     |
| Rx power    | low warning |            |             |     |     |
| Channel     | 2 :         |            |             |     |     |
| Rx power    | low alarm   |            |             |     |     |
| Rx power    | low warning |            |             |     |     |
| Channel     | 3 :         |            |             |     |     |
| Rx power    | low alarm   |            |             |     |     |
| Rx power    | low warning |            |             |     |     |
| Channel     | 4 :         |            |             |     |     |
| Rx power    | low alarm   |            |             |     |     |
| Rx power    | low warning |            |             |     |     |
| Recent      | Errors :    |            |             |     |     |
| Channel     | 1 :         |            |             |     |     |
| Rx Loss     | of Signal   |            |             |     |     |
| Channel     | 2 :         |            |             |     |     |
| Rx Loss     | of Signal   |            |             |     |     |
| Channel     | 3 :         |            |             |     |     |
| Rx Loss     | of Signal   |            |             |     |     |
| Channel     | 4 :         |            |             |     |     |
| Rx Loss     | of Signal   |            |             |     |     |
| Transceiver | in 1/2/2    |            |             |     |     |
| Interface   | Name        | : 1/2/2    |             |     |     |
| Type        |             | : unknown  |             |     |     |
| Connector   | Type        | : ??       |             |     |     |
| Wavelength  |             | : ??       |             |     |     |
| Transfer    | Distance    | : ??       |             |     |     |
| Diagnostic  | Support     | : ??       |             |     |     |
| Product     | Number      | : ??       |             |     |     |
| Serial      | Number      | : ??       |             |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 96

| Part        | Number   | : ??        |         |     |     |     |
| ----------- | -------- | ----------- | ------- | --- | --- | --- |
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
| 1/1/1         | SFP+SR      |     | Tx bias  | high | warning  |     |
| ------------- | ----------- | --- | -------- | ---- | -------- | --- |
|               |             |     | 50.52    | mA > | 40.00 mA |     |
| 1/1/2         | SFP+ER*     |     | ??       |      |          |     |
| 1/2/1         | QSFP+SR4    | 1   | Tx power | low  | alarm    |     |
|               |             |     | -17.00   | dBm  | < -0.50  | dBm |
|               |             | 2   | Tx bias  | low  | warning  |     |
|               |             |     | 3.12     | mA < | 4.00 mA  |     |
| 1/2/2         | QSFP+ER4*   |     | ??       |      |          |     |
| 1/3/1         | SFP28DAC3   |     | n/a      |      |          |     |
| * unsupported | transceiver |     |          |      |          |     |
| Command       | History     |     |          |      |          |     |
Interfaceconfiguration|97

| Release             |         |         |     | Modification |     |     |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier      |         |         |     | --           |     |     |     |     |
| Command Information |         |         |     |              |     |     |     |     |
| Platforms           | Command | context |     | Authority    |     |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show interface |                       | utilization |     |             |            |     |     |     |
| -------------- | --------------------- | ----------- | --- | ----------- | ---------- | --- | --- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |             |     | utilization | [non-zero] |     |     |     |
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
| switch# show | interface | utilization |     |     |     |     |     |     |
| ------------ | --------- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|----------------
-----------|----------------------
| Interval | |   | RX  |     | |   | TX  | | Total | (RX+TX) | |   |
| -------- | --- | --- | --- | --- | --- | ------- | ------- | --- |
Interface seconds | Mbps KPkt/s Util % | Mbps KPkt/s Util % | Mbps
| KPkt/s | Util % | | Description |     |     |     |     |     |     |
| ------ | -------- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------|------------------------|------------------------|----------------
-----------|----------------------
| 1/1/1           |           | 300 9578.02           |           | 788.70 | 95.78 25.70   | 45.89  | 0.26 9603.72   |     |
| --------------- | --------- | --------------------- | --------- | ------ | ------------- | ------ | -------------- | --- |
| 834.59          | 96.04     | Aruba-AP              |           |        |               |        |                |     |
| 1/1/2           |           | 300                   | 25.71     | 45.90  | 0.26 9581.09  | 788.96 | 95.81 9606.80  |     |
| 834.86          | 96.07     | Aruba2530-AP-conce... |           |        |               |        |                |     |
| 1/1/3 -         | lag123    | 300                   | 0.00      | 0.00   | 0.00 0.00     | 0.00   | 0.00 0.00      |     |
| 0.00            | 0.00 ISL: | SWRTS-0064-1          |           |        |               |        |                |     |
| 1/1/4           |           | 300 9261.79           |           | 804.52 | 92.62 9496.70 | 823.97 | 94.97 18758.50 |     |
| 1628.48         | 187.58    | Backup data           | center... |        |               |        |                |     |
| 1/1/5           |           | 300 9496.70           |           | 823.97 | 94.97 9261.79 | 804.52 | 92.62 18758.50 |     |
| 1628.48         | 187.58    | --                    |           |        |               |        |                |     |
| Command History |           |                       |           |        |               |        |                |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 98

| Release        |             |     |         | Modification |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |     |         | --           |     |     |
| Command        | Information |     |         |              |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show ip | interface |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
show ip interface <INTERFACE-ID>|{lag|loopback|vlan|tunnel <ID>}
Description
ShowsstatusandconfigurationinformationforanIPv4interface.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> Specifiesthenameofaninterface.Format:member/slot/port.
| lag <ID> |     |     |     | ShowLAGinterfaceinformation,where<ID>is1-256. |     |     |
| -------- | --- | --- | --- | --------------------------------------------- | --- | --- |
loopback <ID> Showloopbackinterfaceinformation,where<ID>is0-255.
| tunnel <ID> |     |     |     | Showtunnelinterfaceinformation,where<ID>is1-255. |     |     |
| ----------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| vlan <ID>   |     |     |     | ShowVLANinterfaceinformation,where<ID>is1-4094.  |     |     |
Example
| switch#      | show ip interface |     | 1/1/1      |                   |     |       |
| ------------ | ----------------- | --- | ---------- | ----------------- | --- | ----- |
| Interface    | 1/1/1 is          | up  |            |                   |     |       |
| Admin state  | is up             |     |            |                   |     |       |
| Hardware:    | Ethernet,         | MAC | Address:   | 70:72:cf:fd:e7:b4 |     |       |
| IP MTU       | 1500              |     |            |                   |     |       |
| IP TCP       | MSS 1460          |     |            |                   |     |       |
| IPv4 address | 192.168.1.1/24    |     |            |                   |     |       |
| L3 Counters: | Rx Enabled,       |     | Tx Enabled |                   |     |       |
| Statistic    |                   |     |            | RX                | TX  | Total |
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
Interfaceconfiguration|99

| L3 Counters: | Rx             | Disabled, | Tx          | Disabled     |
| ------------ | -------------- | --------- | ----------- | ------------ |
| switch#      | show ip        | interface | loopback    | 1            |
| Interface    | loopback1      |           | is up       |              |
| Admin state  | is             | up        |             |              |
| Hardware:    | Loopback       |           |             |              |
| IP Directed  | Broadcast      |           | is Disabled |              |
| IPv4 address | 192.168.1.1/24 |           |             |              |
| Command      | History        |           |             |              |
| Release      |                |           |             | Modification |
10.14.1000 CommandoutputcandisplayinformationforanIPunnumbered
interfaceandIPTCPMSSconfiguration.
| 10.07orearlier |             |     |         | --        |
| -------------- | ----------- | --- | ------- | --------- |
| Command        | Information |     |         |           |
| Platforms      | Command     |     | context | Authority |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ip | source-interface |     |     |     |
| ------- | ---------------- | --- | --- | --- |
show ip source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME> SpecifiesthenameofaVRF.
Examples
Showing single source IP address configuration settings for sFlow:
| switch#          | show ip | source-interface |     | sflow       |
| ---------------- | ------- | ---------------- | --- | ----------- |
| Source-interface |         | Configuration    |     | Information |
----------------------------------------
| Protocol |     | Source           | Interface |     |
| -------- | --- | ---------------- | --------- | --- |
| -------- |     | ---------------- |           |     |
| sflow    |     | 10.10.10.1       |           |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 100

switch# show ip source-interface all
Source-interface Configuration Information
----------------------------------------
Protocol
--------
all

Source Interface
----------------
1/1/1

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
show ipv6 interface <INTERFACE-ID>

Description

Shows status and configuration information for an IPv6 interface.

Parameter

<INTERFACE-ID>

Examples

Description

Specifies an interface ID. Format: member/slot/port.

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
IPv6 TCP MSS 1440
IPv6 unicast reverse path forwarding: none
IPv6 load sharing: none
RX

TX

0 packets, 0 bytes

0 packets, 0 bytes

Interface configuration | 101

| switch#   |          | show       | ipv6 interface    |          | 1/1/14.1                    |                |     |                |         |
| --------- | -------- | ---------- | ----------------- | -------- | --------------------------- | -------------- | --- | -------------- | ------- |
| Interface |          | 1/1/14.1   |                   | is up    |                             |                |     |                |         |
|           | Admin    | state      | is up             |          |                             |                |     |                |         |
|           | IPv6     | address:   |                   |          |                             |                |     |                |         |
|           | 30::1/64 |            | [VALID]           |          |                             |                |     |                |         |
|           | IPv6     | link-local |                   | address: | fe80::b86a:97c0:122:2f42/64 |                |     |                | [VALID] |
|           | IPv6     | virtual    | address           |          | configured:                 | none           |     |                |         |
|           | IPv6     | multicast  |                   | routing: | disable                     |                |     |                |         |
|           | IPv6     | Forwarding |                   | feature: | enabled                     |                |     |                |         |
|           | IPv6     | multicast  |                   | groups   | locally                     | joined:        |     |                |         |
|           | ff02::1  |            | ff02::1:ff22:2f42 |          |                             | ff02::1:ff00:1 |     | ff02::1:ff00:0 |         |
ff02::2
|               | IPv6     | multicast  |                   | (S,G)    | entries                     | joined:        | none |                |         |
| ------------- | -------- | ---------- | ----------------- | -------- | --------------------------- | -------------- | ---- | -------------- | ------- |
|               | IPv6     | MTU        | 1500              |          |                             |                |      |                |         |
|               | IPv6     | TCP        | MSS 1440          |          |                             |                |      |                |         |
|               | IPv6     | unicast    | reverse           |          | path                        | forwarding:    | none |                |         |
|               | IPv6     | load       | sharing:          | none     |                             |                |      |                |         |
| Encapsulation |          |            | dot1q             | ID: 20   |                             |                |      |                |         |
| switch#       |          | show       | ipv6 interface    |          | lag2.1                      |                |      |                |         |
| Interface     |          | lag2.1     | is                | up       |                             |                |      |                |         |
|               | Admin    | state      | is up             |          |                             |                |      |                |         |
|               | IPv6     | address:   |                   |          |                             |                |      |                |         |
|               | 40::1/64 |            | [VALID]           |          |                             |                |      |                |         |
|               | IPv6     | link-local |                   | address: | fe80::b86a:97c0:122:2f42/64 |                |      |                | [VALID] |
|               | IPv6     | virtual    | address           |          | configured:                 | none           |      |                |         |
|               | IPv6     | multicast  |                   | routing: | disable                     |                |      |                |         |
|               | IPv6     | Forwarding |                   | feature: | enabled                     |                |      |                |         |
|               | IPv6     | multicast  |                   | groups   | locally                     | joined:        |      |                |         |
|               | ff02::1  |            | ff02::1:ff22:2f42 |          |                             | ff02::1:ff00:1 |      | ff02::1:ff00:0 |         |
ff02::2
|         | IPv6          | multicast |          | (S,G) | entries | joined:      | none |     |     |
| ------- | ------------- | --------- | -------- | ----- | ------- | ------------ | ---- | --- | --- |
|         | IPv6          | MTU       | 1500     |       |         |              |      |     |     |
|         | IPv6          | TCP       | MSS 1440 |       |         |              |      |     |     |
|         | IPv6          | unicast   | reverse  |       | path    | forwarding:  | none |     |     |
|         | IPv6          | load      | sharing: | none  |         |              |      |     |     |
|         | Encapsulation |           | dot1q    | ID:   | 30      |              |      |     |     |
| Command |               | History   |          |       |         |              |      |     |     |
| Release |               |           |          |       |         | Modification |      |     |     |
10.14.1000 CommandoutputcandisplayinformationforanIPunnumbered
interfaceandIPv6TCPMSSconfiguration.
| 10.07orearlier |     |             |     |         |     | --        |     |     |     |
| -------------- | --- | ----------- | --- | ------- | --- | --------- | --- | --- | --- |
| Command        |     | Information |     |         |     |           |     |     |     |
| Platforms      |     | Command     |     | context |     | Authority |     |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | ipv6 | source-interface |     |     |     |     |     |     |     |
| ---- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 102

show ipv6 source-interface {sflow | tftp | radius | tacacs | all} [vrf <VRF-NAME>]
Description
ShowssinglesourceIPaddressconfigurationsettings.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
sflow | tftp | radius | tacacs | all ShowssinglesourceIPaddressconfigurationsettingsfora
specificprotocol.Thealloptionshowstheglobalsetting
thatappliestoallprotocolsthatdonothaveanaddressset.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
Examples
ShowingsinglesourceIPaddressconfigurationsettingsforsFlow:
switch#
|                  | show | ipv6 | source-interface | sflow       |
| ---------------- | ---- | ---- | ---------------- | ----------- |
| Source-interface |      |      | Configuration    | Information |
----------------------------------------
| Protocol |     |     | Source Interface |     |
| -------- | --- | --- | ---------------- | --- |
| -------- |     |     | ---------------- |     |
| sflow    |     |     | 2001:DB8::1      |     |
ShowingsinglesourceIPaddressconfigurationsettingsforallprotocols:
| switch#          | show | ipv6 | source-interface | all         |
| ---------------- | ---- | ---- | ---------------- | ----------- |
| Source-interface |      |      | Configuration    | Information |
----------------------------------------
| Protocol       |             |         | Source Interface |              |
| -------------- | ----------- | ------- | ---------------- | ------------ |
| --------       |             |         | ---------------- |              |
| all            |             |         | 1/1/1            |              |
| Command        | History     |         |                  |              |
| Release        |             |         |                  | Modification |
| 10.07orearlier |             |         |                  | --           |
| Command        | Information |         |                  |              |
| Platforms      |             | Command | context          | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| shutdown |     | (interface) |     |     |
| -------- | --- | ----------- | --- | --- |
shutdown
no shutdown
Description
Interfaceconfiguration|103

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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| 10-full   |     |     | 10Mbps,fullduplex,noauto-negotiation                 |     |
10-half
10Mbps,halfduplex,noauto-negotiation
| 100-full |     |     | 100Mbps,fullduplex,noauto-negotiation |     |
| -------- | --- | --- | ------------------------------------- | --- |
100-half
100Mbps,halfduplex,noauto-negotiation
| 1000-full |     |     | 1000Mbps,fullduplex,noauto-negotiation |     |
| --------- | --- | --- | -------------------------------------- | --- |
10g
10Gbps,fullduplex,noauto-negotiation
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 104

Parameter

Description

25g

40g

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

25 Gbps, full duplex, no auto-negotiation

40 Gbps, full duplex, no auto-negotiation

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

Interface configuration | 105

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
Configuringaninterfacetousedefaultsettingsforspeed,duplex,andauto-negotiation:
| switch(config)#      | interface | 1/1/1 |
| -------------------- | --------- | ----- |
| switch(config-if)#no | speed     |       |
Command History
Release Modification
10.09.0001 SpeedsnotsupportedbyhardwarehiddenbyCLI.
10.07orearlier --
Command Information
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 106

Platforms

Command context

Authority

5420
6200

config-if

Administrators or local user group members with execution
rights for this command.

Interface configuration | 107

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
108
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries)

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
Sourceinterfaceselection|109

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
n ptp:SelectsPTP.
n radius:SelectsRADIUS.
n sflow:SelectssFLow.
n sftp-scp:SelectsSFTPandSCP.
ssh-client:SelectsSSHClient.
n
n syslog:Selectsthesourceforsyslogpackets.
n tacacs:SelectsthesourceforTACACSpackets.
n tftp:SelectsTFTP.
n ubt:SelectsUBT.
SpecifiestheVRF name.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 110

| Parameter      |     | Description                |     |
| -------------- | --- | -------------------------- | --- |
| <IFNAME>       |     | Specifiestheinterfacename. |     |
| <IP-ADDR>      |     | SpecifiestheIPv4address.   |     |
| vrf <VRF-NAME> |     | SpecifiestheVRF name.      |     |
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
Sourceinterfaceselection|111

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 112

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
Sourceinterfaceselection|113

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 114

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
Sourceinterfaceselection|115

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

116

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
Sourceinterfaceselection|117

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
ptp
ShowsthesourceinterfaceconfigurationforPTP.
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
| vrf <VRF-NAME> |     | SpecifiestheVRF name.                           |     |
| -------------- | --- | ----------------------------------------------- | --- |
| all-vrfs       |     | ShowsthesourceinterfaceconfigurationforallVRFs. |     |
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 118

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
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
Sourceinterfaceselection|119

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
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
| vrf <VRF-NAME> |     | SpecifiestheVRF name. |     |
| -------------- | --- | --------------------- | --- |
all-vrfs
ShowsthesourceinterfaceconfigurationforallVRF.
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
| switch# show | ipv6 source-interface | all all-vrfs |     |
| ------------ | --------------------- | ------------ | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 120

| Source-interface |     | Configuration | Information |     |     |
| ---------------- | --- | ------------- | ----------- | --- | --- |
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
| dns                 |         |         |     | 1::3                                            | blue    |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- | ------- |
| dns                 |         |         |     | 1::4                                            | default |
| dns                 |         |         |     | 1::2                                            | red     |
| Command History     |         |         |     |                                                 |         |
| Release             |         |         |     | Modification                                    |         |
| 10.13               |         |         |     | Addeddnsparameters.                             |         |
| 10.12.1000          |         |         |     | Added central,sftp-scp,andssh-clientparameters. |         |
| 10.07orearlier      |         |         |     | --                                              |         |
| Command Information |         |         |     |                                                 |         |
| Platforms           | Command | context |     | Authority                                       |         |
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
Sourceinterfaceselection|121

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 122

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

123

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
124
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries)

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

Configuration and firmware management | 125

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 126

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

Configuration and firmware management | 127

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 128

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
Configurationandfirmwaremanagement |129

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 130

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
Configurationandfirmwaremanagement |131

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 132

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
Configurationandfirmwaremanagement |133

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 134

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
Configurationandfirmwaremanagement |135

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 136

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
Configurationandfirmwaremanagement |137

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 138

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
Configurationandfirmwaremanagement |139

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

140

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
Configurationandfirmwaremanagement |141

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 142

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
Configurationandfirmwaremanagement |143

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 144

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
Configurationandfirmwaremanagement |145

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
| checkpoint | <checkpont-name>          |     |     |     |
| ---------- | ------------------------- | --- | --- | --- |
| core-dump  | all|daemon|dsm|kernel|vsf |     |     |     |
startup-config
all
Description
Deletesanexistingcheckpoint,startupconfiguration,orcore-dump.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 146

| Parameter  |                   |     | Description                                 |
| ---------- | ----------------- | --- | ------------------------------------------- |
| checkpoint | <CHECKPOINT-NAME> |     | Specifiesthenameofacheckpoint.              |
| core-dump  |                   |     | Eraseoneofthefollowingsetsofcore-dumpfiles: |
| all|daemon | <daemon-name>     |     |                                             |
n all:Eraseallcore-dumpfiles.
|kernel
n daemon<daemon-name>:Erasedaemoncore-dumpfiles.
n kerne:lErasethekernelcore-dump.
n vsfErasedaemoncore-dumpfilesforVSF.
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
Configurationandfirmwaremanagement |147

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 148

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
Configurationandfirmwaremanagement |149

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 150

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
Configurationandfirmwaremanagement |151

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 152

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
Configurationandfirmwaremanagement |153

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 154

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

Configuration and firmware management | 155

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 156

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
Configurationandfirmwaremanagement |157

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 158

| 02 Sep  | 23 02:50:02                        | : Switch boot | count is 1 |
| ------- | ---------------------------------- | ------------- | ---------- |
| Index : | 3                                  |               |            |
| Boot ID | : f00ba10c8c44457f83fee303d014a89a |               |            |
25 Aug 23 10:27:42 : Power on reset with 0x1, Version: FL.10.14.0000-1465-
g9df95249d06b0~dirty
| 25 Aug | 23 10:28:18 | : Switch | boot count is 3 |
| ------ | ----------- | -------- | --------------- |
25 Aug 23 10:29:02 : Primary overtemperature fault detected with 0x2 in PSU 1/1
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
switch#
| Management | module |     |     |
| ---------- | ------ | --- | --- |
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
| Management | module |     |     |
| ---------- | ------ | --- | --- |
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
Configurationandfirmwaremanagement |159

ThefollowingexampledisplaystheboothistoryfortheVSFmember2.
| switch# | show | boot-history |     | vsf | member | 2   |
| ------- | ---- | ------------ | --- | --- | ------ | --- |
Member-2
=========
| Index :        | 0                                  |         |          |           |       |                  |
| -------------- | ---------------------------------- | ------- | -------- | --------- | ----- | ---------------- |
| Boot ID        | : df99026c194a44f1944a3e7685fb4d90 |         |          |           |       |                  |
| Current        | Boot,                              | up for  | 3        | hrs 31    | mins  | 39 secs          |
| Index :        | 3                                  |         |          |           |       |                  |
| Boot ID        | : 7bf4104903fe4ad1ba4bce40e8099c76 |         |          |           |       |                  |
| 10 Aug         | 17 10:02:24                        |         | : Reboot | requested |       | through database |
| 10 Aug         | 17 10:02:13                        |         | : Switch | boot      | count | is 2             |
| Command        | History                            |         |          |           |       |                  |
| Release        |                                    |         |          |           |       | Modification     |
| 10.07orearlier |                                    |         |          |           |       | --               |
| Command        | Information                        |         |          |           |       |                  |
| Platforms      |                                    | Command | context  |           |       | Authority        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 160

Examples
TFTPupload:
switch#
|     | copy primary | tftp://192.0.2.0/00_10_00_0002.swi |     |     |     |
| --- | ------------ | ---------------------------------- | --- | --- | --- |
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
| switch# | copy primary | usb:/11.10.00.0002.swi |     |     |     |
| ------- | ------------ | ---------------------- | --- | --- | --- |
| Command | History      |                        |     |     |     |
Configurationandfirmwaremanagement |161

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 162

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

Configuration and firmware management | 163

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 164

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
Configurationandfirmwaremanagement |165

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 166

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
Configurationandfirmwaremanagement |167

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 168

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
Configurationandfirmwaremanagement |169

Chapter 9

Dynamic Segmentation

Dynamic Segmentation

For information on dynamic segmentation, view the Security Guide.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

170

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

171

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
SNMP|172

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

173

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

One Touch Provisioning

One Touch Provisioning (OTP) allows a switch to be provisioned on HPE Aruba Networking Central with
the minimum user configuration.

Configuring One Touch Provisioning

To provision a switch to HPE Aruba Networking Central by using an OTP scenario, you can configure:

n The HPE Aruba Networking Central Location

Following configurations can be done optionally:

HPE Aruba Networking Central integration | 174

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 175

n SupportforobtaningtheHPE ArubaNetworkingCentrallocationviaDHCP.
n SupportforconnectivitytoanHPE ArubaNetworkingCentralon-premiseinstance.
Supportability
Debugloggingcanbeenabledwiththefollowingcommand:
ThecentraldebuglogsarehelpfultodetermineconnectivityissueswithHPE ArubaNetworkingCentral.
| switch# debug | central    | all |         |          |
| ------------- | ---------- | --- | ------- | -------- |
| HPE Aruba     | Networking |     | Central | commands |
hpe-anw-central
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
| 10.07orearlier      |         |         | --        |     |
| ------------------- | ------- | ------- | --------- | --- |
| Command Information |         |         |           |     |
| Platforms           | Command | context | Authority |     |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200               |              |              | rightsforthiscommand. |     |
| ------------------ | ------------ | ------------ | --------------------- | --- |
| hpe-anw-central    |              | support-mode |                       |     |
| hpe-anw-central    | support-mode |              |                       |     |
| no hpe-anw-central | support-mode |              |                       |     |
Description
HPE ArubaNetworkingCentralintegration|176

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
| Command | History |     |                                                 |
| ------- | ------- | --- | ----------------------------------------------- |
| Release |         |     | Modification                                    |
| 10.15   |         |     | Commandsyntaxchangedfromaruba-centraltohpe-anw- |
central.
| 10.07orearlier |             |         | --        |
| -------------- | ----------- | ------- | --------- |
| Command        | Information |         |           |
| Platforms      | Command     | context | Authority |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200                     |     |                 | rightsforthiscommand. |
| ------------------------ | --- | --------------- | --------------------- |
| configuration-lockout    |     | central         | managed               |
| configuration-lockout    |     | central managed |                       |
| no configuration-lockout |     | central managed |                       |
Description
ConfiguresthedevicetoonlybewritablefromHPE ArubaNetworkingCentral.HPE ArubaNetworking
Centralwillbetheonlyagentthatcanadd,modify,ordeleteconfigurationsonthedevice.Thenoform
ofthiscommanddisablesthisfeature.
ThenoformofthiscommandisonlyavailablewhenthedeviceisdisconnectedfromHPE ArubaNetworking
Central.
Usage
TheAOS-CXswitchconnectstoHPE ArubaNetworkingCentralineitheroftwomodes:monitoror
managed.Whenthedeviceisconnectedinmonitormode,HPE ArubaNetworkingCentralmonitorsthe
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 177

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
| Activate            | Server  | URL     |     | :devices-v2.arubanetworks.com |
| ------------------- | ------- | ------- | --- | ----------------------------- |
| CLI location        |         |         |     | :20.0.2:8083                  |
| CLI VRF             |         |         |     | :default                      |
| switch(config)#     |         | end     |     |                               |
| Command History     |         |         |     |                               |
| Release             |         |         |     | Modification                  |
| 10.07orearlier      |         |         |     | --                            |
| Command Information |         |         |     |                               |
| Platforms           | Command | context |     | Authority                     |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200           |       |       |     | rightsforthiscommand. |
| -------------- | ----- | ----- | --- | --------------------- |
| diag-dump      | rest  | basic |     |                       |
| diag-dump rest | basic |       |     |                       |
Description
DisplayRESTpathsanddiagnosticsinformationfortheRESTfeature.Theoutputofthiscommand
includesdiagnosticsinformationforHPE ArubaNetworkingCentral.
Example
ThefollowingexampledisplaysjusttheCentral Countersportionoftheoutputforthiscommand.
| switch# diag-dump |     | rest | basic |     |
| ----------------- | --- | ---- | ----- | --- |
=========================================================================
HPE ArubaNetworkingCentralintegration|178

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
config
allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
disable
disable
Description
DisablesconnectiontoHPE ArubaNetworkingCentralserver.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 179

Whentheconnectionisdisabled,theswitchdoesnotattempttoconnecttotheHPE ArubaNetworking
Centralserverorfetchcentrallocationfromanyofthethreesources(CLI/HPEGreenLake/DHCP).Italso
disconnectsanyactiveconnectiontotheHPE ArubaNetworkingCentralserver.
Example
| switch(config-hpe-anw-central)# |     | disable |     |
| ------------------------------- | --- | ------- | --- |
switch(config-hpe-anw-central)#
| Command        | History     |              |           |
| -------------- | ----------- | ------------ | --------- |
| Release        |             | Modification |           |
| 10.07orearlier |             | --           |           |
| Command        | Information |              |           |
| Platforms      | Command     | context      | Authority |
5420 config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
| 6200   |            |            | rightsforthiscommand. |
| ------ | ---------- | ---------- | --------------------- |
| enable | (HPE Aruba | Networking | Central)              |
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
HPE ArubaNetworkingCentralintegration|180

| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
5420 config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
location-override
| location-override | <location> | [vrf <VRF-NAME>] |     |
| ----------------- | ---------- | ---------------- | --- |
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
WhenyouconfigureanIPv6addresswithaportnumber,specifytheaddresspartinsidesquarebrackets,
optionallyfollowedbytheportnumber,e.g.[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<location>
Specifiesoneofthesevalues:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
Examples
ConfiguringlocationoverridewithlocationandVRF:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 181

switch(config-hpe-anw-central)# location-override hpe-anw-central.com vrf default
switch(config-hpe-anw-central)#
switch(config-hpe-anw-central)# location-override hpe-anw-central.com vrf red
switch(config-hpe-anw-central)# location-override 10.0.0.1 vrf red
switch(config-hpe-anw-central)# location-override 10.0.0.1:443 vrf red
| switch(config-hpe-anw-central)#         |     | location-override |         |
| --------------------------------------- | --- | ----------------- | ------- |
| 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |                   | vrf red |
| switch(config-hpe-anw-central)#         |     | location-override |         |
[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443 vrf red
Configuringlocationoverridewithlocationonly:
switch(config-hpe-anw-central)#
location-override hpe-anw-central.com
switch(config-hpe-anw-central)#
RemovinglocationoverridevaluesfromtheHPE ArubaNetworkingCentralconfigurationcontext:
| switch(config-hpe-anw-central)# |     | no  | location-override |
| ------------------------------- | --- | --- | ----------------- |
switch(config-hpe-anw-central)#
| Command History     |         |                                       |           |
| ------------------- | ------- | ------------------------------------- | --------- |
| Release             |         | Modification                          |           |
| 10.13.1000          |         | CommandupdatedtoreflectaOTPscenario.. |           |
| 10.07orearlier      |         | --                                    |           |
| Command Information |         |                                       |           |
| Platforms           | Command | context                               | Authority |
Allplatforms config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
location-override-alternative
| location-override-alternative    |     | <LOCATION> | [vrf <VRF>] |
| -------------------------------- | --- | ---------- | ----------- |
| no location-override-alternative |     | <LOCATION> | [vrf <VRF>] |
Description
ConfiguresinformationaboutHPE ArubaNetworkingCentralconnectionwhenthealternativelocation
isused.
Thenoformofthiscommandremovesthelocation-override-alternativeconfiguration.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<LOCATION>
SpecifiestheHPE ArubaNetworkingCentrallocation.
| vrf <VRF> |     | SpecifiestheVRFusedtoconnecttoHPE ArubaNetworking |     |
| --------- | --- | ------------------------------------------------- | --- |
Central.
HPE ArubaNetworkingCentralintegration|182

Usage

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

Example of a configuration with location only:

switch(config-hpe-anw-central)# location-override-alternative hpe-anw-central.com
switch(config-hpe-anw-central)#

Example of removing the override configuration:

switch(config-hpe-anw-central)# no location-override-alternative
switch(config-hpe-anw-central)# location-override-alternative 10.0.0.1 vrf red
switch(config-hpe-anw-central)# location-override-alternative 10.0.0.1:443 vrf red
switch(config-hpe-anw-central)# location-override-alternative
2001:0db8:85a3:0000:0000:8a2e:0370:7334 vrf red
switch(config-hpe-anw-central)# location-override-alternative
[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443 vrf red

Command History

Release

10.13.1000

10.12.1000

Command Information

Modification

Command updated to reflect OTP scenario.

Command introduced.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

183

| Platforms |     | Command | context | Authority |
| --------- | --- | ------- | ------- | --------- |
Allplatforms config-hpe_anw-central Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show hpe-anw-central
show hpe-anw-central
Description
ShowsinformationaboutHPE ArubaNetworkingCentralconnectionandthestatusoftheActivate
serverconnection.
Examples
ExampleofaswitchthathastheHPE ArubaNetworkingCentralconnection:
| switch# | show       | hpe-anw-central |        |             |
| ------- | ---------- | --------------- | ------ | ----------- |
| Central | admin      | state           |        | : enabled   |
| Central | location   |                 |        | : 10.0.0.1  |
| VRF for | connection |                 |        | : mgmt      |
| Shared  | Token      |                 |        | : N/A       |
| Central | connection |                 | status | : connected |
| Central | source     |                 |        | : activate  |
| Central | source     | connection      | status | : connected |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
| Main location |               |              |               | : 10.0.0.1                     |
| ------------- | ------------- | ------------ | ------------- | ------------------------------ |
| Main VRF      |               |              |               | : mgmt                         |
| Alternative   |               | location     |               | : N/A                          |
| Alternative   |               | VRF          |               | : N/A                          |
| Activate      | Server        | URL          |               | : devices-v2.arubanetworks.com |
| System        | time          | synchronized | from Activate | : N/A                          |
| Source        | IP            |              |               | : N/A                          |
| Source        | IP Overridden |              |               | : False                        |
| Central       | support       | mode         |               | : disabled                     |
ExampleofaswitchwhenthemainCLIlocationisused:
| switch# | show       | hpe-anw-central |        |             |
| ------- | ---------- | --------------- | ------ | ----------- |
| Central | admin      | state           |        | : enabled   |
| Central | location   |                 |        | : 10.0.0.1  |
| VRF for | connection |                 |        | : mgmt      |
| Shared  | secret     |                 |        | : N/A       |
| Central | connection |                 | status | : connected |
| Central | source     |                 |        | : cli       |
| Central | source     | connection      | status | : connected |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
| Main location |               |              |               | : 10.0.0.1                     |
| ------------- | ------------- | ------------ | ------------- | ------------------------------ |
| Main VRF      |               |              |               | : mgmt                         |
| Alternative   |               | location     |               | : 20.0.0.1                     |
| Alternative   |               | VRF          |               | : default                      |
| Activate      | server        | URL          |               | : devices-v2.arubanetworks.com |
| System        | time          | synchronized | from Activate | : N/A                          |
| Source        | IP            |              |               | : N/A                          |
| Source        | IP Overridden |              |               | : False                        |
| Central       | support       | mode         |               | : disabled                     |
ExampleofaswitchwhenthealternativeCLI locationisused:
HPE ArubaNetworkingCentralintegration|184

| switch# show       | hpe-anw-central |        |        |             |
| ------------------ | --------------- | ------ | ------ | ----------- |
| Central admin      | state           |        |        | : enabled   |
| Central location   |                 |        |        | : 20.0.0.1  |
| VRF for connection |                 |        |        | : default   |
| Shared secret      |                 |        |        | : N/A       |
| Central connection |                 | status |        | : connected |
| Central source     |                 |        |        | : cli       |
| Central source     | connection      |        | status | : connected |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
| Main location        |              |        |               | : 10.0.0.1                     |
| -------------------- | ------------ | ------ | ------------- | ------------------------------ |
| Main VRF             |              |        |               | : mgmt                         |
| Alternative          | location     |        |               | : 20.0.0.1                     |
| Alternative          | VRF          |        |               | : default                      |
| Activate             | server       | URL    |               | : devices-v2.arubanetworks.com |
| System time          | synchronized |        | from Activate | : N/A                          |
| Source IP            |              |        |               | : N/A                          |
| Source IP Overridden |              |        |               | : False                        |
| Central support      |              | mode   |               | : disabled                     |
| Central admin        | state        |        |               | : enabled                      |
| Central location     |              |        |               | : 20.0.0.1                     |
| VRF for connection   |              |        |               | : default                      |
| Shared secret        |              |        |               | : N/A                          |
| Central connection   |              | status |               | : connected                    |
| Central source       |              |        |               | : cli                          |
| Central source       | connection   |        | status        | : connected                    |
Central source last connected on : Wed Jun 28 23:07:25 UTC 2023
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 185

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
| Main location        |                 |           |               | : N/A                          |
| Main VRF             |                 |           |               | : N/A                          |
| Alternative          | location        |           |               | : N/A                          |
| Alternative          | VRF             |           |               | : N/A                          |
| Activate             | server          | URL       |               | : devices-v2.arubanetworks.com |
| System time          | synchronized    |           | from Activate | : N/A                          |
| Source IP            |                 |           |               | : N/A                          |
| Source IP Overridden |                 |           |               | : False                        |
| Central support      |                 | mode      |               | : disabled                     |
Exampleofaswitchwhen HPE ArubaNetworkingCentralisnotreachable:
| switch# show       | hpe-anw-central |        |        |                 |
| ------------------ | --------------- | ------ | ------ | --------------- |
| Central admin      | state           |        |        | : enabled       |
| Central location   |                 |        |        | : N/A           |
| VRF for connection |                 |        |        | : N/A           |
| Shared secret      |                 |        |        | : N/A           |
| Central connection |                 | status |        | : not-reachable |
| Central source     |                 |        |        | : activate      |
| Central source     | connection      |        | status | : connected     |
Central source last connected on : Fri Jun 30 20:22:33 UTC 2023
| Main location        |              |      |               | : N/A                          |
| -------------------- | ------------ | ---- | ------------- | ------------------------------ |
| Main VRF             |              |      |               | : N/A                          |
| Alternative          | location     |      |               | : N/A                          |
| Alternative          | VRF          |      |               | : N/A                          |
| Activate             | server       | URL  |               | : devices-v2.arubanetworks.com |
| System time          | synchronized |      | from Activate | : N/A                          |
| Source IP            |              |      |               | : N/A                          |
| Source IP Overridden |              |      |               | : False                        |
| Central support      |              | mode |               | : disabled                     |
| Command History      |              |      |               |                                |
HPE ArubaNetworkingCentralintegration|186

| Release |     |     | Modification                                    |
| ------- | --- | --- | ----------------------------------------------- |
| 10.15   |     |     | Commandsyntaxchangedfromaruba-centraltohpe-anw- |
central.
| 10.12.1000          |         |         | Enhancedtosupportmorescenarios |
| ------------------- | ------- | ------- | ------------------------------ |
| 10.07orearlier      |         |         | --                             |
| Command Information |         |         |                                |
| Platforms           | Command | context | Authority                      |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show running-config |                 | current-context |     |
| ------------------- | --------------- | --------------- | --- |
| show running-config | current-context |                 |     |
Description
Showstherunningconfigurationforthecurrent-context.IfuserisinthecontextofHPE Aruba
NetworkingCentral(config-hpe-anw-central),thentheHPE ArubaNetworkingCentralrunning
configurationisdisplayed.
Examples
ShowstherunningconfigurationofHPE ArubaNetworkingCentral:
switch(config-hpe-anw-central)# show running-config current-context
hpe-anw-central
disable
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
5420 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6200 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 187

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

188

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
Portfiltering|189

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-lag-if |     | rightsforthiscommand. |
| --- | ------------- | --- | --------------------- |
show portfilter
| show portfilter | [<IFNAME>] |     |     |
| --------------- | ---------- | --- | --- |
Description
Displaysfiltersettingsforallinterfacesoraspecificinterface.
| Parameter |     |     | Description                       |
| --------- | --- | --- | --------------------------------- |
| <IFNAME>  |     |     | Specifiestheingressinterfacename. |
Specifiesoneofthesevalues:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 190

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Portfiltering|191

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

192

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
| switch(config)# |                 | ip dns domain-name    |         | switch.com |
| --------------- | --------------- | --------------------- | ------- | ---------- |
| switch(config)# |                 | ip dns server-address |         | 1.1.1.1    |
| switch(config)# |                 | ip dns host           | myhost1 | 3.3.3.3    |
| switch(config)# |                 | exit                  |         |            |
| switch#         | show            | ip dns                |         |            |
| VRF             | Name : vrf_mgmt |                       |         |            |
| Host            | Name            |                       |         | Address    |
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
DNS|193

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
Thisexampleremovestheentrydomain1.com.
| switch(config)# |             |         | no ip dns | domain-list |              | domain1.com |     |
| --------------- | ----------- | ------- | --------- | ----------- | ------------ | ----------- | --- |
| Command         | History     |         |           |             |              |             |     |
| Release         |             |         |           |             | Modification |             |     |
| 10.07orearlier  |             |         |           |             | --           |             |     |
| Command         | Information |         |           |             |              |             |     |
| Platforms       |             | Command | context   |             | Authority    |             |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 194

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
Examples
| ThisexampledefinesanIPv4addressof     |     |     |     |            | 3.3.3.3forhost1. |     |
| ------------------------------------- | --- | --- | --- | ---------- | ---------------- | --- |
| switch(config)#                       |     | ip  | dns | host host1 | 3.3.3.3          |     |
| ThisexampledefinesanIPv6addressofb::5 |     |     |     |            | forhost 1.       |     |
| switch(config)#                       |     | ip  | dns | host host1 | b::5             |     |
DNS|195

| Thisexampledefinesremovestheentryfor |             |         |           |      |       | host 1withaddress |     | b::5. |
| ------------------------------------ | ----------- | ------- | --------- | ---- | ----- | ----------------- | --- | ----- |
| switch(config)#                      |             |         | no ip dns | host | host1 | b::5              |     |       |
| Command                              | History     |         |           |      |       |                   |     |       |
| Release                              |             |         |           |      |       | Modification      |     |       |
| 10.07orearlier                       |             |         |           |      |       | --                |     |       |
| Command                              | Information |         |           |      |       |                   |     |       |
| Platforms                            |             | Command | context   |      |       | Authority         |     |       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
| switch(config)# |     |     | ip dns | server-address |     | 1.1.1.1 |     |     |
| --------------- | --- | --- | ------ | -------------- | --- | ------- | --- | --- |
Thisexampledefinesanameserverata::1.
| switch(config)# |     |     | ip dns | server-address |     | a::1 |     |     |
| --------------- | --- | --- | ------ | -------------- | --- | ---- | --- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)# |     |     | no ip dns | server-address |     | a::1 |     |     |
| --------------- | --- | --- | --------- | -------------- | --- | ---- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 196

| Command        | History     |     |         |     |              |
| -------------- | ----------- | --- | ------- | --- | ------------ |
| Release        |             |     |         |     | Modification |
| 10.07orearlier |             |     |         |     | --           |
| Command        | Information |     |         |     |              |
| Platforms      | Command     |     | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
|                 |           | ip             | dns server-address |         | 4.4.4.4     |
| --------------- | --------- | -------------- | ------------------ | ------- | ----------- |
| switch(config)# |           | ip             | dns server-address |         | 6.6.6.6     |
| switch(config)# |           | ip             | dns host           | host3   | 5.5.5.5     |
| switch(config)# |           | ip             | dns host           | host3   | c::12       |
| switch#         | show      | ip dns         |                    |         |             |
| VRF Name        | : default |                |                    |         |             |
| Domain Name     | :         | domain.com     |                    |         |             |
| DNS Domain      | list      | : domain5.com, |                    |         | domain8.com |
| Name Server(s)  |           | : 4.4.4.4,     |                    | 6.6.6.6 |             |
| Host Name       |           | Address        |                    |         |             |
-------------------------------
| host3 |     | 5.5.5.5 |     |     |     |
| ----- | --- | ------- | --- | --- | --- |
| host3 |     | c::12   |     |     |     |
DNS|197

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 198

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

199

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
Devicediscoveryandconfiguration|200

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

201

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
Devicediscoveryandconfiguration|202

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

5420
6200

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
CDP Group

: access_switches
:
: hpe-anw-ap_cdp

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

203

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

5420
6200

config-if
config-lag-if

Administrators or local user group members with execution
rights for this command.

aaa authentication port-access allow-cdp-proxy-logoff

aaa authentication port-access allow-cdp-proxy-logoff
no aaa authentication port-access allow-cdp-proxy-logoff

Description

Allows a client to be logged off from the system via a special TLV in the CDP packet. By default, proxy
logoff via CDP packet support is disabled. When allow-cdp-proxy-logoff is enabled, TLV received from
CDP packets corresponding to logoff processing will be read and logoff is issued to the clients. This only

Device discovery and configuration | 204

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
| 5420   |                |               |             |             |                 | Administratorsorlocalusergroupmemberswithexecution |     |     |     |
| ------ | -------------- | ------------- | ----------- | ----------- | --------------- | -------------------------------------------------- | --- | --- | --- |
| 6200   |                | config-lag-if |             |             |                 | rightsforthiscommand.                              |     |     |     |
| aaa    | authentication |               | port-access |             | allow-lldp-bpdu |                                                    |     |     |     |
| aaa    | authentication |               | port-access |             | allow-lldp-bpdu |                                                    |     |     |     |
| no aaa | authentication |               |             | port-access |                 | allow-lldp-bpdu                                    |     |     |     |
Description
AllowsallpacketsrelatedtotheLLDPBPDU(BridgeProtocolDataUnit)onasecureport.Thiscommand
canbeissuedfromtheinterface(config-if)orLinkAggregationGroup(config-lag-if)contexts.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 205

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
Devicediscoveryandconfiguration|206

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
| 5420         |           |               |              |              |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ------------ | --------- | ------------- | ------------ | ------------ | --- | -------------------------------------------------- | --- |
| 6200         |           | config-lag-if |              |              |     | rightsforthiscommand.                              |     |
| associate    | cdp-group |               |              |              |     |                                                    |     |
| associate    | cdp-group |               | <GROUP-NAME> |              |     |                                                    |     |
| no associate |           | cdp-group     |              | <GROUP-NAME> |     |                                                    |     |
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
switch(config)#
|     |     |     | port-access |     | device-profile |     | profile01 |
| --- | --- | --- | ----------- | --- | -------------- | --- | --------- |
switch(config-device-profile)# no associate cdp-group my-cdp-group
| Command        | History |     |     |     |     |              |     |
| -------------- | ------- | --- | --- | --- | --- | ------------ | --- |
| Release        |         |     |     |     |     | Modification |     |
| 10.07orearlier |         |     |     |     |     | --           |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 207

| Command   | Information |     |         |     |           |
| --------- | ----------- | --- | ------- | --- | --------- |
| Platforms | Command     |     | context |     | Authority |
config-device-profile
| 5420         |            |              |              |     | Administratorsorlocalusergroupmemberswithexecution |
| ------------ | ---------- | ------------ | ------------ | --- | -------------------------------------------------- |
| 6200         |            |              |              |     | rightsforthiscommand.                              |
| associate    | lldp-group |              |              |     |                                                    |
| associate    | lldp-group | <GROUP-NAME> |              |     |                                                    |
| no associate | lldp-group |              | <GROUP-NAME> |     |                                                    |
Description
AssociatesanLLDPgroupwithadeviceprofile.AmaximumoftwoLLDPgroupscanbeassociatedwith
adeviceprofile
ThenoformofthiscommandremovesanLLDPgroupfromadeviceprofile.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<GROUP-NAME> SpecifiesthenameoftheLLDPgrouptoassociatewiththedevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheLLDPgroupmy-lldp-groupwiththedeviceprofileprofile01:
| switch(config)# |     | port-access |     | device-profile | profile01 |
| --------------- | --- | ----------- | --- | -------------- | --------- |
switch(config-device-profile)# associate lldp-group my-lldp-group
RemovingtheLLDPgroupmy-lldp-groupfromthedeviceprofileprofile01:
switch(config)#
|     |     | port-access |     | device-profile | profile01 |
| --- | --- | ----------- | --- | -------------- | --------- |
switch(config-device-profile)# no associate lldp-group my-lldp-group
| Command        | History     |     |         |              |           |
| -------------- | ----------- | --- | ------- | ------------ | --------- |
| Release        |             |     |         | Modification |           |
| 10.07orearlier |             |     |         | --           |           |
| Command        | Information |     |         |              |           |
| Platforms      | Command     |     | context |              | Authority |
5420 config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6200         |           |              |              |     | rightsforthiscommand. |
| ------------ | --------- | ------------ | ------------ | --- | --------------------- |
| associate    | mac-group |              |              |     |                       |
| associate    | mac-group | <GROUP-NAME> |              |     |                       |
| no associate | mac-group |              | <GROUP-NAME> |     |                       |
Description
Devicediscoveryandconfiguration|208

AssociatesaMACgroupwithadeviceprofile.AmaximumoftwoMACgroupscanbeassociatedwitha
deviceprofile.
ThenoformofthiscommandremovesaMACgroupfromadeviceprofile.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<GROUP-NAME> SpecifiesthenameoftheMACgrouptoassociatewiththisdevice
profile.Range:1to32alphanumericcharacters.
Examples
AssociatingtheMACgroupmac01-groupwiththedeviceprofileprofile01:
| switch(config)#                | port-access |     | device-profile | profile01 |             |
| ------------------------------ | ----------- | --- | -------------- | --------- | ----------- |
| switch(config-device-profile)# |             |     | associate      | mac-group | mac01-group |
RemovingtheMACgroupmac01-groupfromthedeviceprofileprofile01:
| switch(config)# | port-access |     | device-profile | profile01 |     |
| --------------- | ----------- | --- | -------------- | --------- | --- |
switch(config-device-profile)# no associate mac-group mac01-group
| Command History     |         |         |              |           |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- |
| Release             |         |         | Modification |           |     |
| 10.07orearlier      |         |         | --           |           |     |
| Command Information |         |         |              |           |     |
| Platforms           | Command | context |              | Authority |     |
5420 config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6200           |                  |     |     | rightsforthiscommand. |     |
| -------------- | ---------------- | --- | --- | --------------------- | --- |
| associate role |                  |     |     |                       |     |
| associate role | <ROLE-NAME>      |     |     |                       |     |
| no associate   | role <ROLE-NAME> |     |     |                       |     |
Description
Associatesarolewithadeviceprofile.Onlyonerolecanbeassociatedwithadeviceprofile.For
informationonhowtoconfigurearole,seetheportaccessroleinformationintheSecurityGuide.
Thenoformofthiscommandremovesarolefromadeviceprofile.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<ROLE-NAME> Specifiesthenameoftheroletoassociatewiththedeviceprofile.
Range:1to64alphanumericcharacters.
Examples
Associatingtherolemy-rolewiththedeviceprofileprofile01:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 209

| switch(config)# | port-access |     | device-profile |     | profile01 |
| --------------- | ----------- | --- | -------------- | --- | --------- |
switch(config-device-profile)#
|     |     |     | associate |     | role my-role |
| --- | --- | --- | --------- | --- | ------------ |
Removingtherolemy-rolefromthedeviceprofileprofile01:
| switch(config)#                | port-access |         | device-profile |           | profile01    |
| ------------------------------ | ----------- | ------- | -------------- | --------- | ------------ |
| switch(config-device-profile)# |             |         | no             | associate | role my-role |
| Command History                |             |         |                |           |              |
| Release                        |             |         | Modification   |           |              |
| 10.07orearlier                 |             |         | --             |           |              |
| Command Information            |             |         |                |           |              |
| Platforms                      | Command     | context |                | Authority |              |
5420 config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6200                 |                 |     |     | rightsforthiscommand. |     |
| -------------------- | --------------- | --- | --- | --------------------- | --- |
| disable (port-access | device-profile) |     |     |                       |     |
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
| Command History                |             |     |                |         |           |
| Release                        |             |     | Modification   |         |           |
| 10.07orearlier                 |             |     | --             |         |           |
| Command Information            |             |     |                |         |           |
Devicediscoveryandconfiguration|210

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
5420 config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6200                |                 |     | rightsforthiscommand. |
| ------------------- | --------------- | --- | --------------------- |
| enable (port-access | device-profile) |     |                       |
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
5420 config-device-profile Administratorsorlocalusergroupmemberswithexecution
| 6200            |         |     | rightsforthiscommand. |
| --------------- | ------- | --- | --------------------- |
| ignore (for CDP | groups) |     |                       |
ignore [seq <SEQ-NUM>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |
| ---------------- | --- | ---------- | --- |
no ignore [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |
| ---------------- | --- | ---------- | --- |
Description
DefinesaruletoignoredevicesforaCDP(CiscoDiscoveryProtocol)group.Upto64match/ignorerules
canbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaCDPgroup.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 211

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
voice-vlan-query <VLAN-ID> SpecifiestheVLANqueryvalueoftheneighbor.Range:1to
65535.
Examples
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01intheplatform
TLV:
| switch(config)#           | port-access |     | cdp-group | grp01    |            |
| ------------------------- | ----------- | --- | --------- | -------- | ---------- |
| switch(config-cdp-group)# |             |     | ignore    | platform | PLATFORM01 |
AddingaruletotheCDPgroupgrp01thatignoresadevicethattransmitsSWVERSIONinsoftware
versionTLV:
| switch(config)#           | port-access |     | cdp-group | grp01      |           |
| ------------------------- | ----------- | --- | --------- | ---------- | --------- |
| switch(config-cdp-group)# |             |     | ignore    | sw-version | SWVERSION |
Removingtherulethatmatchesthesequencenumber25fromtheCDPgroupnamedgrp01.
| switch(config)#           | port-access |         | cdp-group | grp01        |     |
| ------------------------- | ----------- | ------- | --------- | ------------ | --- |
| switch(config-cdp-group)# |             |         | no ignore | seq          | 25  |
| Command History           |             |         |           |              |     |
| Release                   |             |         |           | Modification |     |
| 10.07orearlier            |             |         |           | --           |     |
| Command Information       |             |         |           |              |     |
| Platforms                 | Command     | context |           | Authority    |     |
5420 config-cdp-group Administratorsorlocalusergroupmemberswithexecution
| 6200             |         |     |     | rightsforthiscommand. |     |
| ---------------- | ------- | --- | --- | --------------------- | --- |
| ignore (for LLDP | groups) |     |     |                       |     |
ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> |     | [type | <KEY> [value | <VALUE>]]} |
| ---------- | ------------ | --- | ----- | ------------ | ---------- |
Devicediscoveryandconfiguration|212

no ignore [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type <KEY> | [value <VALUE>]]} |
| ---------- | ------------ | ----------- | ----------------- |
Description
DefinesaruletoignoredevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedfora
group.
ThenoformofthiscommandremovesaruleforignoringdevicesfromanLLDPgroup.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).
Range:1to256alphanumericcharacters.
sysname<SYS-NAME> SpecifiestheLLDPsystemnameTLV.Range:1to64alphanumeric
characters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
type <KEY>
SpecifiesthevendorOUIsubtypekey.Optional.
| value <VALUE> |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |     |
| ------------- | --- | ---------------------------------------------- | --- |
alphanumericcharacters.
Examples
AddingaruletotheLLDPgroupgrp01thatignoresadevicethattransmitsPLATFORM01inthesystem
descriptionTLV:
| switch(config)#            | port-access | lldp-group | grp01               |
| -------------------------- | ----------- | ---------- | ------------------- |
| switch(config-lldp-group)# |             | ignore     | sys-desc PLATFORM01 |
Removingtherulethatmatchesthesequencenumber25fromtheLLDPgroupnamedgrp01.
| switch(config)#            | port-access | lldp-group   | grp01  |
| -------------------------- | ----------- | ------------ | ------ |
| switch(config-lldp-group)# |             | no match     | seq 25 |
| Command History            |             |              |        |
| Release                    |             | Modification |        |
| 10.07orearlier             |             | --           |        |
| Command Information        |             |              |        |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 213

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
5420 config-lldp-group Administratorsorlocalusergroupmemberswithexecution
| 6200            |         |     | rightsforthiscommand. |     |
| --------------- | ------- | --- | --------------------- | --- |
| ignore (for MAC | groups) |     |                       |     |
[seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] ignore {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
DefinesaruletoignoredevicesforaMACgroupbasedonthecriteriaofMACaddress,MACaddress
mask,orMACOrganizationalUniqueIdentifier(OUI).Upto64ignorerulescanbedefinedforagroup.
ThenoformofthiscommandremovesaruleforignoringdevicesfromaMACgroup.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
seq <SEQ-ID> SpecifiestheentrysequenceIDoftheruletocreateormodifya
MACgroup.IfnoIDisspecifiedwhenaddingarule,anIDis
automaticallyassignedinincrementsof10intheorderinwhich
rulesareadded.Whenmorethanonerulematchesthecommand
entered,therulewiththelowestIDtakesprecedence.Range:1to
4294967295.
| mac <MAC-ADDR> |     |     | SpecifiestheMACaddressofthedevicetoignore. |     |
| -------------- | --- | --- | ------------------------------------------ | --- |
mac-mask <MAC-MASK> SpecifiestheMACaddressmasktoignoredevicesinthatrange.
SupportedMACaddressmasks:/32and/40.
mac-oui <MAC-OUI> SpecifiestheMACOUItoignoredevicesinthatrange.Supports
MACOUIaddressofmaximumlengthof24bits.
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
| switch(config)#           | mac-group | grp01               |         |                   |
| ------------------------- | --------- | ------------------- | ------- | ----------------- |
| switch(config-mac-group)# |           | ignore              | mac     | 1a:2b:3c:4d:5e:6f |
| switch(config-mac-group)# |           | match               | mac-oui | 1a:2b:3c          |
| switch(config-mac-group)# |           | exit                |         |                   |
| switch(config)#           | do        | show running-config |         |                   |
| Current configuration:    |           |                     |         |                   |
!
| !Version          | AOS-CX Virtual.10.0X.0001 |     |     |     |
| ----------------- | ------------------------- | --- | --- | --- |
| !export-password: | default                   |     |     |     |
Devicediscoveryandconfiguration|214

| led locator on |     |     |     |
| -------------- | --- | --- | --- |
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
switch(config-mac-group)#
|                           |         | match mac-oui  | 1a:2b:3c |
| ------------------------- | ------- | -------------- | -------- |
| switch(config-mac-group)# |         | exit           |          |
| switch(config)#           | do show | running-config |          |
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
| switch(config)# | mac-group | grp01 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|     |     | ignore mac 1a:2b:3c:4d:5e:6f |     |
| --- | --- | ---------------------------- | --- |
AddingaruletotheMACgroupgrp02thatignoresdevicesbasedonMACmask:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 215

| switch(config)# | mac-group | grp01 |     |
| --------------- | --------- | ----- | --- |
switch(config-mac-group)#
|                           |     | ignore | mac-mask 1a:2b:3c:4d:5e/40 |
| ------------------------- | --- | ------ | -------------------------- |
| switch(config-mac-group)# |     | ignore | mac-mask 18:e3:ab:73/32    |
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
| interface mgmt |     |     |     |
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
!
vlan 1
| interface mgmt |     |     |     |
| -------------- | --- | --- | --- |
no shutdown
ip dhcp
| mac-group grp01 |     |     |     |
| --------------- | --- | --- | --- |
```
AddingaruletotheMACgroupgrp01thatignoresdeviceswithMACentrysequencenumberand
basedonMACOUI:
Devicediscoveryandconfiguration|216

| switch(config)# | mac-group | grp01 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-mac-group)#
|                           |     | seq 10 | ignore mac b2:c3:44:12:78:11 |          |
| ------------------------- | --- | ------ | ---------------------------- | -------- |
| switch(config-mac-group)# |     | seq 20 | ignore mac-oui               | 1a:2b:3c |
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
| seq 30 ignore   | mac-mask | 71:14:89:f3/32    |     |     |
```
Removingtherulethatmatchesthesequencenumber25fromtheMACgroupnamedgrp01.
| switch(config)#           | mac-group | grp01     |        |     |
| ------------------------- | --------- | --------- | ------ | --- |
| switch(config-mac-group)# |           | no ignore | seq 25 |     |
Command History
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 217

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-mac-group
| 5420 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 6200 |     |     | rightsforthiscommand.                              |
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
| switch(config)#           | mac-group | grp01 |     |
| ------------------------- | --------- | ----- | --- |
| switch(config-mac-group)# |           | exit  |     |
RemovingaMACgroupnamedgrp01:
switch(config)#
|                     | no      | mac-group grp01 |              |
| ------------------- | ------- | --------------- | ------------ |
| Command History     |         |                 |              |
| Release             |         |                 | Modification |
| 10.07orearlier      |         |                 | --           |
| Command Information |         |                 |              |
| Platforms           | Command | context         | Authority    |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200           |         |     | rightsforthiscommand. |
| -------------- | ------- | --- | --------------------- |
| match (for CDP | groups) |     |                       |
match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
| voice-vlan-query |     | <VLAN-ID>} |     |
| ---------------- | --- | ---------- | --- |
Devicediscoveryandconfiguration|218

no match [seq <SEQ-ID>] {platform <PLATFORM> | sw-version <SWVERSION> |
|     | voice-vlan-query |     | <VLAN-ID>} |     |     |     |     |
| --- | ---------------- | --- | ---------- | --- | --- | --- | --- |
Description
DefinesaruletomatchdevicesforaCDPgroup.Amaximumof32CDPgroupscanbeconfiguredon
theswitch.Upto64matchorignorerulescanbedefinedforeachgroup.
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
voice-vlan-query <VLAN-ID> SpecifiestheVLANqueryvalueoftheneighbor.Range:1to65535.
Examples
AddingrulestomatchaCiscodevicewithaspecificsoftwareversiononVLAN512totheCDPgroup
grp01:
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 219

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
5420 config-cdp-group Administratorsorlocalusergroupmemberswithexecution
| 6200            |         |     | rightsforthiscommand. |
| --------------- | ------- | --- | --------------------- |
| match (for LLDP | groups) |     |                       |
match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type | <KEY> [value <VALUE>]]} |
| ---------- | ------------ | ----- | ----------------------- |
no match [seq <SEQ-ID>] {sys-desc <SYS-DESC> | sysname <SYS-NAME> |
| vendor-oui | <VENDOR-OUI> | [type | <KEY> [value <VALUE>]]} |
| ---------- | ------------ | ----- | ----------------------- |
Description
DefinesaruletomatchdevicesforanLLDPgroup.Upto64match/ignorerulescanbedefinedfora
group.
Thenoformofthiscommandremovesarule.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
seq <SEQ-ID> SpecifiestheIDoftheruletocreateormodify.IfnoIDisspecified
whenaddingarule,anIDisautomaticallyassignedinincrements
of10intheorderinwhichrulesareadded.Whenmorethanone
rulematchesthecommandentered,therulewiththelowestID
takesprecedence.
sys-desc <SYS-DESC> SpecifiestheLLDPsystemdescriptiontype-length-value(TLV).The
sys-descparameterbeconfiguredwithasubstringinsteadofa
completestringtomatch.Range:1to256alphanumeric
characters.
sysname <SYS-NAME> SpecifiestheLLDPsystemnameTLV.Thesysnameparameterbe
configuredwithasubstringinsteadofacompletestringtomatch.
Range:1to64alphanumericcharacters.
vendor-oui <VENDOR-OUI> SpecifiestheLLDPsystemvendorOUITLV.Range:1to6
alphanumericcharacters.
type <KEY>
SpecifiesthevendorOUIsubtypekey.
| value <VALUE> |     |     | SpecifiesthevendorOUIsubtypevalue.Range:1to256 |
| ------------- | --- | --- | ---------------------------------------------- |
alphanumericcharacters.
Examples
AddingrulesthatmatchtheLLDPsystemdescriptionHPE_ANW-SwitchandsystemnameHPE_ANWto
theLLDPgroupnamedgrp01:
Devicediscoveryandconfiguration|220

| switch(config)# | port-access |     | lldp-group |     | grp01 |     |
| --------------- | ----------- | --- | ---------- | --- | ----- | --- |
switch(config-lldp-group)#
|                            |     |                     | match | sys-desc | HPE_ANW-Switch |     |
| -------------------------- | --- | ------------------- | ----- | -------- | -------------- | --- |
| switch(config-lldp-group)# |     |                     | match | sysname  | HPE_ANW        |     |
| switch(config)#            | do  | show running-config |       |          |                |     |
| Current configuration:     |     |                     |       |          |                |     |
!
| !Version          | AOS-CX Virtual.10.0X.000 |     |     |     |     |     |
| ----------------- | ------------------------ | --- | --- | --- | --- | --- |
| !export-password: | default                  |     |     |     |     |     |
| led locator       | on                       |     |     |     |     |     |
!
!
vlan 1
| port-access | lldp-group        | grp01 |                |     |     |     |
| ----------- | ----------------- | ----- | -------------- | --- | --- | --- |
| seq         | 10 match sys-desc |       | HPE_ANW-Switch |     |     |     |
| seq         | 20 match sysname  |       | HPE_ANW        |     |     |     |
Removingarulethatmatchesthesequencenumber25fromanLLDPgroupnamedgrp01:
| switch(config)#            | port-access |     | lldp-group |     | grp01 |     |
| -------------------------- | ----------- | --- | ---------- | --- | ----- | --- |
| switch(config-lldp-group)# |             |     | no match   | seq | 25    |     |
Addingarulethatmatchesthevalueofvendor-OUI000b86withtypeof1totheLLDPgroupnamed
grp01:
| switch(config)#            | port-access |     | lldp-group |            | grp01       |     |
| -------------------------- | ----------- | --- | ---------- | ---------- | ----------- | --- |
| switch(config-lldp-group)# |             |     | match      | vendor-oui | 000b86 type | 1   |
Addingarulethatmatchesthevalueofvendor-OUI000c34totheLLDPgroupnamedgrp01:
| switch(config)#            | port-access |         | lldp-group |              | grp01  |     |
| -------------------------- | ----------- | ------- | ---------- | ------------ | ------ | --- |
| switch(config-lldp-group)# |             |         | match      | vendor-oui   | 000c34 |     |
| Command History            |             |         |            |              |        |     |
| Release                    |             |         |            | Modification |        |     |
| 10.07orearlier             |             |         |            | --           |        |     |
| Command Information        |             |         |            |              |        |     |
| Platforms                  | Command     | context |            | Authority    |        |     |
5420 config-lldp-group Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6200
| match (for MAC | groups) |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- |
[seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
no [seq <SEQ-ID>] match {mac <MAC-ADDR> | mac-mask <MAC-MASK> | mac-oui <MAC-OUI>}
Description
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 221

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
Devicediscoveryandconfiguration|222

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
AddingdevicestotheMACgroupgrp01withMACentrysequencenumberandbasedonMACaddress,
MACaddressmask,andMACOUI:
| switch(config)#           | mac-group | grp01          |                         |
| ------------------------- | --------- | -------------- | ----------------------- |
| switch(config-mac-group)# |           | seq 10 match   | mac b2:c3:44:12:78:11   |
| switch(config-mac-group)# |           | seq 20 match   | mac-oui 1a:2b:3c        |
| switch(config-mac-group)# |           | seq 30 match   | mac-mask 71:14:89:f3/32 |
| switch(config-mac-group)# |           | exit           |                         |
| switch(config)#           | do show   | running-config |                         |
Current configuration:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 223

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
| switch(config-mac-group)# |           | exit   |                  |          |
switch(config)#
|     | do show | running-config |     |     |
| --- | ------- | -------------- | --- | --- |
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
| switch(config-mac-group)# |     | exit |     |     |
| ------------------------- | --- | ---- | --- | --- |
switch(config)#
|     | do show | running-config |     |     |
| --- | ------- | -------------- | --- | --- |
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
Devicediscoveryandconfiguration|224

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
| !Version          | AOS-CX | Virtual.10.0X.0001 |         |     |
| ----------------- | ------ | ------------------ | ------- | --- |
| !export-password: |        |                    | default |     |
| led locator       | on     |                    |         |     |
!
!
| vlan      | 1    |     |     |     |
| --------- | ---- | --- | --- | --- |
| interface | mgmt |     |     |     |
no shutdown
ip dhcp
| mac-group | grp03 |     |     |     |
| --------- | ----- | --- | --- | --- |
```
| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
5420 config-mac-group Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6200
| port-access    | cdp-group |     |                  |     |
| -------------- | --------- | --- | ---------------- | --- |
| port-access    | cdp-group |     | <CDP-GROUP-NAME> |     |
| no port-access | cdp-group |     | <CDP-GROUP-NAME> |     |
Description
CreatesaCDP(CiscoDiscoveryProtocol)groupormodifiesanexistingCDPgroup.ACDPGroupisused
toclassifyconnecteddevicesbasedontheCDPpacketdetailsadvertisedbythedevice.Amaximumof
32CDPgroupscanbeconfiguredontheswitch.Eachgroupaccepts64match/ignorecommands.
ThenoformofthiscommandremovesaCDPgroup.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<CDP-GROUP-NAME> SpecifiesthenameoftheCDPgrouptocreateormodify.The
maximumnumberofcharacterssupportedis32.Required.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 225

Examples
CreatingaCDPgroupnamedgrp01:
switch(config)#
|                           |     |     | port-access |     | cdp-group |                  | grp01     |     |
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
| !Version          |         | AOS-CX | Virtual.10.0X.000 |     |     |     |     |     |
| ----------------- | ------- | ------ | ----------------- | --- | --- | --- | --- | --- |
| !export-password: |         |        | default           |     |     |     |     |     |
| led               | locator | on     |                   |     |     |     |     |     |
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
| switch(config)# |             |         | no port-access |         |     | cdp-group    | grp01 |     |
| --------------- | ----------- | ------- | -------------- | ------- | --- | ------------ | ----- | --- |
| Command         | History     |         |                |         |     |              |       |     |
| Release         |             |         |                |         |     | Modification |       |     |
| 10.07orearlier  |             |         |                |         |     | --           |       |     |
| Command         | Information |         |                |         |     |              |       |     |
| Platforms       |             | Command |                | context |     | Authority    |       |     |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200           |     |                |     |                       |                       | rightsforthiscommand. |     |     |
| -------------- | --- | -------------- | --- | --------------------- | --------------------- | --------------------- | --- | --- |
| port-access    |     | device-profile |     |                       |                       |                       |     |     |
| port-access    |     | device-profile |     | <DEVICE-PROFILE-NAME> |                       |                       |     |     |
| no port-access |     | device-profile |     |                       | <DEVICE-PROFILE-NAME> |                       |     |     |
Description
Createsanewdeviceprofileandswitchestotheconfig-device-profilecontext.Amaximumof32
deviceprofilescanbecreated.Thiscommandcanbeissuedfromtheinterface(config-if)orLink
AggregationGroup(config-lag-if)contexts.
Thenoformofthiscommandremovesadeviceprofile.
Devicediscoveryandconfiguration|226

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<DEVICE-PROFILE-NAME> Specifiesthenameofadeviceprofile.Range:1to32
alphanumericcharacters.
Usage
Whenmultipledeviceprofilesarecreatedontheswitchusingtheport-access device-profile <device-
profile-name>command,theswitchgoesthroughthelistofdeviceprofilesnamesinalphabetical
ordertofindthedeviceprofiletoassociatetoaclient.Forexample,iftheswitchhadthefollowing
configuration:
| port-access |           | device-profile |     | Switch |     |     |     |
| ----------- | --------- | -------------- | --- | ------ | --- | --- | --- |
|             | associate | lldp-group     |     | lldp1  |     |     |     |
| port-access |           | device-profile |     | AP     |     |     |     |
|             | associate | lldp-group     |     | lldp1  |     |     |     |
TheorderoftheattemptedmatchwouldbedeviceprofileAP,andthendeviceprofileSwitch.
Examples
Creatingadeviceprofilenamedprofile01:
| switch(config)# |     | port-access |     | device-profile |     | profile01 |     |
| --------------- | --- | ----------- | --- | -------------- | --- | --------- | --- |
switch(config-device-profile)#
Removingadeviceprofilenamedprofile01:
| switch(config)# |     | no  | port-access |     | device-profile | profile01 |     |
| --------------- | --- | --- | ----------- | --- | -------------- | --------- | --- |
Creatingadeviceprofilenamedprofile02onaLAGport:
| switch(config)#interface |     |     |             | lag 1 |                |     |           |
| ------------------------ | --- | --- | ----------- | ----- | -------------- | --- | --------- |
| switch(config-lag-if)#   |     |     | port-access |       | device-profile |     | profile01 |
switch(config-device-profile)#
| Command | History |     |     |     |                                                      |     |     |
| ------- | ------- | --- | --- | --- | ---------------------------------------------------- | --- | --- |
| Release |         |     |     |     | Modification                                         |     |     |
| 10.13   |         |     |     |     | ThiscommandcanbeissuedfromaLinkAggregationGroup(LAG) |     |     |
context.
| 10.07orearlier |             |         |         |     | --        |     |     |
| -------------- | ----------- | ------- | ------- | --- | --------- | --- | --- |
| Command        | Information |         |         |     |           |     |     |
| Platforms      |             | Command | context |     | Authority |     |     |
config
| 5420 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 227

| Platforms | Command   |     | context | Authority             |     |
| --------- | --------- | --- | ------- | --------------------- | --- |
| 6200      | config-if |     |         | rightsforthiscommand. |     |
config-lag-if
| port-access | device-profile |     | mode | block-until-profile-applied |     |
| ----------- | -------------- | --- | ---- | --------------------------- | --- |
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
| switch(config-if-deviceprofile)# |         |     |     | end                                                  |     |
| -------------------------------- | ------- | --- | --- | ---------------------------------------------------- | --- |
| Command                          | History |     |     |                                                      |     |
| Release                          |         |     |     | Modification                                         |     |
| 10.13                            |         |     |     | ThiscommandcanbeissuedfromaLinkAggregationGroup(LAG) |     |
context.
| 10.07orearlier |                         |     |         | --  |                                           |
| -------------- | ----------------------- | --- | ------- | --- | ----------------------------------------- |
| Command        | Information             |     |         |     |                                           |
| Platforms      | Command                 |     | context |     | Authority                                 |
| 5420           | config-if               |     |         |     | Administratorsorlocalusergroupmemberswith |
| 6200           | config-if-deviceprofile |     |         |     | executionrightsforthiscommand.            |
config-lag-if
| port-access    | lldp-group |     |                   |     |     |
| -------------- | ---------- | --- | ----------------- | --- | --- |
| port-access    | lldp-group |     | <LLDP-GROUP-NAME> |     |     |
| no port-access | lldp-group |     | <LLDP-GROUP-NAME> |     |     |
Devicediscoveryandconfiguration|228

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
| switch(config)# | port-access |     | lldp-group |     | grp01 |
| --------------- | ----------- | --- | ---------- | --- | ----- |
switch(config-lldp-group)#
RemovinganLLDPgroupnamedgrp01:
| switch(config)#     | no      | port-access |     | lldp-group   | grp01 |
| ------------------- | ------- | ----------- | --- | ------------ | ----- |
| Command History     |         |             |     |              |       |
| Release             |         |             |     | Modification |       |
| 10.07orearlier      |         |             |     | --           |       |
| Command Information |         |             |     |              |       |
| Platforms           | Command | context     |     | Authority    |       |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200             |                |     |     | rightsforthiscommand. |     |
| ---------------- | -------------- | --- | --- | --------------------- | --- |
| show port-access | device-profile |     |     |                       |     |
show port-access device-profile [[interface {all | <INTERFACE-ID>}
| [client-status | <MAC-ADDR>]] |     | |   | name <DEVICE-PROFILE-NAME>] |     |
| -------------- | ------------ | --- | --- | --------------------------- | --- |
Description
ShowstheclientstatusforaspecificMACaddressorprofilename.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
interface {all | <INTERFACE-ID>} Selectallforallinterfacesorspecifythenameofaninterfacein
theformat:member/slot/port.
client-status <MAC-ADDR> SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.
name <DEVICE-PROFILE-NAME>
Specifiesthenameofthedeviceprofile.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 229

Examples
Showingtheappliedstateofthedeviceprofiles:
switch#
| show       | port-access |                                    | device-profile |     |     |     |
| ---------- | ----------- | ---------------------------------- | -------------- | --- | --- | --- |
| Profile    | Name        | : accesspoints                     |                |     |     |     |
| LLDP       | Groups      | : 2920-grp                         |                |     |     |     |
| CDP Groups |             | :                                  |                |     |     |     |
| MAC Groups |             | : 2920-mac-grp1,2920-iot-grp2      |                |     |     |     |
| Role       |             | : local_role_1                     |                |     |     |     |
| State      |             | : Enabled                          |                |     |     |     |
| Profile    | Name        | : access_switches                  |                |     |     |     |
| LLDP       | Groups      | : 2920-grp                         |                |     |     |     |
| CDP Groups |             | :                                  |                |     |     |     |
| MAC Groups |             | :                                  |                |     |     |     |
| Role       |             | : local_2920_role                  |                |     |     |     |
| State      |             | : Enabled                          |                |     |     |     |
| Profile    | Name        | : iot_devices                      |                |     |     |     |
| LLDP       | Groups      | :                                  |                |     |     |     |
| CDP Groups |             | :                                  |                |     |     |     |
| MAC Groups |             | : iot_camera-grp1,iot_sensors-grp1 |                |     |     |     |
| Role       |             | : local_2920_role                  |                |     |     |     |
| State      |             | : Enabled                          |                |     |     |     |
| Profile    | Name        | : lobbyaps                         |                |     |     |     |
| LLDP       | Groups      | :                                  |                |     |     |     |
| CDP Groups |             | : lobby_ap_cdp_grp                 |                |     |     |     |
| MAC Groups |             | :                                  |                |     |     |     |
| Role       |             | : test_ap_role                     |                |     |     |     |
| State      |             | : Disabled                         |                |     |     |     |
Showingtheappliedstateofthedeviceprofileoninterface1/1/3:
switch# show port-access device-profile interface 1/1/3 client-status
00:0c:29:9e:d1:20
| Port 1/1/3, | Neighbor-Mac |                  | 00:0c:29:9e:d1:20 |          |           |      |
| ----------- | ------------ | ---------------- | ----------------- | -------- | --------- | ---- |
| Profile     | Name         | : lobbyaps       |                   |          |           |      |
| LLDP        | Group        | :                |                   |          |           |      |
| CDP Group   |              | : hpe-anw-ap_cdp |                   |          |           |      |
| MAC Group   |              | :                |                   |          |           |      |
| Role        |              | : test_ap_role   |                   |          |           |      |
| Status      |              | : Failed         |                   |          |           |      |
| Failure     | Reason       | : Failed         |                   | to apply | MAC based | VLAN |
Showingtheappliedstateofaspecificdeviceprofile:
| switch# show    | port-access |     | device-profile |                  | name | lldp-group |
| --------------- | ----------- | --- | -------------- | ---------------- | ---- | ---------- |
| Profile         | Name        |     | :              | lldp-group       |      |            |
| LLDP            | Groups      |     | :              |                  |      |            |
| CDP Groups      |             |     | :              |                  |      |            |
| MAC Groups      |             |     | :              | pc-behind-phone, |      | lldp       |
| Role            |             |     | :              | auth_role        |      |            |
| State           |             |     | :              | Enabled          |      |            |
| Command History |             |     |                |                  |      |            |
Devicediscoveryandconfiguration|230

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

5420
6200

Manager (#)

Administrators or local user group members with execution
rights for this command.

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

231

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

Device discovery and configuration | 232

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

233

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

Device discovery and configuration | 234

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 235

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
Devicediscoveryandconfiguration|236

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
| lldp dot3 eee |     |     |     |
| ------------- | --- | --- | --- |
| lldp dot3 eee |     |     |     |
| no lldp dot3  | eee |     |     |
Description
Setsthe802.3TLVsforEnergy-EfficientEthernet(EEE) tobeadvertised.Bydefault,advertisementofEEE
TLVsisenabled.NotsupportedontheOOBMinterface.
Thenoformofthiscommanddisablesadvertisementof802.3TLVs.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 237

| Parameter |     |     |     | Description                              |
| --------- | --- | --- | --- | ---------------------------------------- |
| eee       |     |     |     | Specifiesadvertisementof802.3TLVsforEEE. |
Examples
EnablingadvertisementoftheEEETLVs:
| switch(config-if)# |     | lldp | dot3 | eee |
| ------------------ | --- | ---- | ---- | --- |
DisablingadvertisementoftheEEETLVs:
| switch(config-if)#  |         | no lldp | dot3 | eee          |
| ------------------- | ------- | ------- | ---- | ------------ |
| Command History     |         |         |      |              |
| Release             |         |         |      | Modification |
| 10.07orearlier      |         |         |      | --           |
| Command Information |         |         |      |              |
| Platforms           | Command | context |      | Authority    |
config-if
| 5420          |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ------------- | --- | --- | --- | -------------------------------------------------- |
| 6200          |     |     |     | rightsforthiscommand.                              |
| lldp dot3 mfs |     |     |     |                                                    |
| lldp dot3 mfs |     |     |     |                                                    |
| no lldp dot3  | mfs |     |     |                                                    |
Description
Enablesthe802.3TLVlistinLLDP toadvertiseformaximumframesize(MFS).Enabledbydefault.
ThenoformofthiscommanddisablestheadvertisementofmaximumframesizeTLVs.
Examples
EnablingadvertisementofmaximumframesizeTLVs:
| switch(config)#    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | lldp      | dot3  | mfs |
DisablingadvertisementofmaximumframesizeTLVs:
| switch(config)#    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | no lldp   | dot3  | mfs |
Devicediscoveryandconfiguration|238

| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.11               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<multiplier>
SpecifiestheTTLmultiplierintherangeof2to10.Default:4.
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
| switch(config)# | no  | lldp holdtime-multiplier |     |
| --------------- | --- | ------------------------ | --- |
| Command History |     |                          |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 239

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
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
Route-only-portIP address(Layer-3interface)orIPaddressoftheSVI(Layer-2interface).
n
n OOBMIPaddress.
n BaseMACaddressoftheswitch.
| Parameter |     |     | Description         |     |
| --------- | --- | --- | ------------------- | --- |
| <VLAN-ID> |     |     | SpecifiestheVLANID. |     |
Examples
SettingthemanagementauthorityforVLAN10:
| switch(config)# | lldp | management-address |     | vlan 10 |
| --------------- | ---- | ------------------ | --- | ------- |
RemovingthemanagementauthorityforVLAN10:
| switch(config)#     | no  | lldp management-address |                    | vlan 10 |
| ------------------- | --- | ----------------------- | ------------------ | ------- |
| Command History     |     |                         |                    |         |
| Release             |     |                         | Modification       |         |
| 10.12               |     |                         | Commandintroduced. |         |
| Command Information |     |                         |                    |         |
Devicediscoveryandconfiguration|240

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiesthemanagementaddressoftheswitchasanIPv4format
(x.x.x.x),wherexisadecimalvaluefrom0to255.
Examples
Settingthemanagementaddressto10.10.10.2:
| switch(config)# | lldp | management-ip-address | 10.10.10.2 |
| --------------- | ---- | --------------------- | ---------- |
Removingthemanagementaddress:
| switch(config)# | no  | lldp management-ip-address |                                                  |
| --------------- | --- | -------------------------- | ------------------------------------------------ |
| Command History |     |                            |                                                  |
| Release         |     |                            | Modification                                     |
| 10.14           |     |                            | Themanagement-ipv4-addresskeywordisdeprecatedand |
replacedwithmanagement-ip-address.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 241

lldp management-ipv6-address
| lldp management-ipv6-address    |     | <IPV6-ADDR> |     |
| ------------------------------- | --- | ----------- | --- |
| no lldp management-ipv6-address |     |             |     |
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
| switch(config)# | no          | lldp management-ipv6-address |              |
| --------------- | ----------- | ---------------------------- | ------------ |
| Command         | History     |                              |              |
| Release         |             |                              | Modification |
| 10.07orearlier  |             |                              | --           |
| Command         | Information |                              |              |
| Platforms       | Command     | context                      | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp med
lldp med [poe [priority-override] | capability | network-policy]
| no med [poe | [priority-override] | |   | capability | network-policy] |
| ----------- | ------------------- | --- | ---------------------------- |
Description
Devicediscoveryandconfiguration|242

ConfiguressupportfortheLLDP-MEDTLV.LLDP-MED(mediaendpointdevices)isanextensiontoLLDP
developedbyTIAtosupportinteroperabilitybetweenVoIPendpointdevicesandothernetworkingend-
devices.TheswitchonlysendstheLLDPMEDTLVafterreceivingaMEDTLVfromandconnected
endpointdevice.
NotsupportedontheOOBMinterface.
ThenoformofthiscommanddisablessupportfortheLLDPMEDTLV.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
poe [priority-override]
SpecifiesadvertisementofpoweroverEthernetdatalink
classification.Thepriority-overrideoptionoverridesuser-
configuredportpriorityforPoweroverEthernet.Whenbothlldp
dot3poeandlldpmedpoeareenabled,thelldpdot3poe3
settingtakesprecedence.Default:enabled.
| capability |     |     |     | SpecifiesadvertisementofsupportedLLDPMEDTLVs.The |     |
| ---------- | --- | --- | --- | ------------------------------------------------ | --- |
capabilityTLVisalwayssentwithotherMEDTLVs,thereforeit
cannotbedisabledwhenotherMEDTLVsareenabled.Default:
enabled.
network-policy Networkpolicydiscoveryletsendpointsandnetworkdevices
advertisetheirVLANIDs,andIEEE802.1p(PCPandDSCP)values
forvoiceapplications.ThisTLVisonlysentwhenavoiceVLAN
policyispresent.Default:enabled.
Examples
EnablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)# |     | lldp | med | network-policy |     |
| ------------------ | --- | ---- | --- | -------------- | --- |
DisablingadvertisementofthenetworkpolicyTLV:
| switch(config-if)#  |         | no  | lldp med | network-policy |     |
| ------------------- | ------- | --- | -------- | -------------- | --- |
| Command History     |         |     |          |                |     |
| Release             |         |     |          | Modification   |     |
| 10.07orearlier      |         |     |          | --             |     |
| Command Information |         |     |          |                |     |
| Platforms           | Command |     | context  | Authority      |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp med location |             |     |           |           |     |
| ----------------- | ----------- | --- | --------- | --------- | --- |
| lldp med location | {civic-addr |     |           | elin-addr | }   |
| no med location   | {civic-addr |     | elin-addr |           | }   |
Description
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 243

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

n 19: house number

n 20: house number suffix

n 21: landmark or vanity

n 22: location

n 23: name

n 24: postal/zip code

n 25: building (structure)

n 26: unit (apartment, suite)

Device discovery and configuration | 244

n 27:floor
n 28:room
29:typeofplace
n
n 30:postalcommunityname
n 31:postofficebox
n 32:additionalcode13203000003
n 33:seat(desk,cubicleworkstation)
n 34:primaryroadname35roadsection
n 36:branchroadname
n 37:sub-branchroadname
n 38:streetnamepre-modifier
n 39:streetnamepost-modifier
Examples
EnablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | lldp med location | elin-addr | 408-555-1212 |
| ------------------ | --- | ----------------- | --------- | ------------ |
DisablingsupportfortheLLDPMEDemergencylocationTLV:
| switch(config-if)# |     | no lldp med | location elin-addr | 408-555-1212 |
| ------------------ | --- | ----------- | ------------------ | ------------ |
EnablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# lldp med location civic-addr US 1 19 123 6 Fake 18 Street
DisablingsupportfortheLLDPMEDcivicaddressTLV:
switch(config-if)# no lldp med location civic-addr US 1 19 123 6 Fake 18 Street
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp receive
lldp receive
no lldp receive
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 245

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
Devicediscoveryandconfiguration|246

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 247

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
management-address: Selectionisbasedonpriority
n
inthefollowinglist(forexampleiffirstTLVnameisn't
selected,thenextwillbe,progressingthroughthislist
untilaselectionismade):
1. IPv4orIPV6managementaddress.
2. IPaddressofthelowestconfiguredloopback
interface.
3. Iflayer3,thentheroute-onlyportIPaddress.If
layer2,theIPaddressoftheSVI.
4. OOBMinterfaceIPaddress.
5. BaseMACaddressoftheswitch.
n port-description: Selectport-descriptionTLV.
n port-vlan-id: Selectport-vlan-idTLV.
n port-vlan-name: Selectport-vlan-nameTLV.
n system-capabilities: Selectsystem-capabilitiesTLV.
system-description: Selectsystem-descriptionTLV.
n
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lldp timer
| lldp timer <TIME> |     |     |     |
| ----------------- | --- | --- | --- |
no lldp timer
Description
Devicediscoveryandconfiguration|248

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

Modification

--

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

249

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
ip <X.X.X.X> SpecifyanIPaddressinIPv4format(X.X.X.X),whereXisa
decimalnumberfrom0to255.
ipv6 <X:X::X:X>
SpecifyanIPaddressinIPv6format(X:X::X:X),whereXisa
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
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.14.1000          |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
5420 config-if Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
lldp transmit
Devicediscoveryandconfiguration|250

lldp transmit
no lldp transmit
Description
EnablestransmissionofLLDPinformationonspecificinterface.Bydefault,LLDPtransmissionisenabled
onallactiveinterfaces,includingtheOOBMinterface.
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
| switch(config)#     | interface | mgmt             |              |
| ------------------- | --------- | ---------------- | ------------ |
| switch(config-if)#  |           | no lldp transmit |              |
| Command History     |           |                  |              |
| Release             |           |                  | Modification |
| 10.07orearlier      |           |                  | --           |
| Command Information |           |                  |              |
| Platforms           | Command   | context          | Authority    |
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 251

Thenoformofthiscommandsetsthedelaytimetoitsdefaultvalueof2seconds.
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
Devicediscoveryandconfiguration|252

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 253

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
Devicediscoveryandconfiguration|254

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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 255

| Command | History |     |     |     |              |     |
| ------- | ------- | --- | --- | --- | ------------ | --- |
| Release |         |     |     |     | Modification |     |
10.14.1000 WhendisplayingtheLLDP configurationforaspecificinterface,
theoutputofthiscommanddisplaysanyconfiguredmanagement
IPaddresses.
| 10.07orearlier |             |         |         |     | --        |     |
| -------------- | ----------- | ------- | ------- | --- | --------- | --- |
| Command        | Information |         |         |     |           |     |
| Platforms      |             | Command | context |     | Authority |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
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
| mgmt           |             | Yes |     |     | Yes          | Yes |
| -------------- | ----------- | --- | --- | --- | ------------ | --- |
| Command        | History     |     |     |     |              |     |
| Release        |             |     |     |     | Modification |     |
| 10.07orearlier |             |     |     |     | --           |     |
| Command        | Information |     |     |     |              |     |
Devicediscoveryandconfiguration|256

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
5420 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 6200 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show lldp | local-device |     |     |     |
| --------- | ------------ | --- | --- | --- |
| show lldp | local-device |     |     |     |
Description
ShowsglobalLLDPinformationadvertisedbytheswitch,aswellasport-baseddata.IfVLANsare
configuredonanyactiveinterfaces,theVLANIDisonlyshownfortrunknativeoruntaggedVLANIDson
accessinterfaces.
Example
ShowingglobalLLDPinformationonly(allportsincludingOOBMportareadministrativelydown):
| switch# | show lldp | local-device |     |     |
| ------- | --------- | ------------ | --- | --- |
| Global  | Data      |              |     |     |
===========
| Chassis-ID   |             | : 1c:98:ec:e3:45:00 |              |               |
| ------------ | ----------- | ------------------- | ------------ | ------------- |
| System       | Name        | : switch            |              |               |
| System       | Description | : HPE ANW           | JL375A 8400X | XL.01.01.0001 |
| Management   | Address     | : 192.168.10.1      |              |               |
| Capabilities | Available   | : Bridge,           | Router       |               |
| Capabilities | Enabled     | : Bridge,           | Router       |               |
| TTL          |             | : 120               |              |               |
Showingallportsexcept1/1/11andOOBMasadministrativelydown:
switch#
|        | show lldp | local-device |     |     |
| ------ | --------- | ------------ | --- | --- |
| Global | Data      |              |     |     |
===========
| Chassis-ID   |             | : 1c:98:ec:e3:45:00 |        |     |
| ------------ | ----------- | ------------------- | ------ | --- |
| System       | Name        | : switch            |        |     |
| System       | Description | : HPE ANW           |        |     |
| Management   | Address     | : 192.168.10.1      |        |     |
| Capabilities | Available   | : Bridge,           | Router |     |
| Capabilities | Enabled     | : Bridge,           | Router |     |
| TTL          |             | : 120               |        |     |
| Port Based   | Data        |                     |        |     |
===============
| Port-ID           |     | : 1/1/11         |     |     |
| ----------------- | --- | ---------------- | --- | --- |
| Port-Desc         |     | : "1/1/11"       |     |     |
| Port Mgmt-Address |     | : 164.254.21.220 |     |     |
| Port VLAN         | ID  | : 1              |     |     |
| Port-ID           |     | : mgmt           |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 257

| Port-Desc |              |     | :   | "mgmt"         |     |
| --------- | ------------ | --- | --- | -------------- | --- |
| Port      | Mgmt-Address |     | :   | 164.254.21.220 |     |
Inthisexample,alltheportsexcept1/1/11areadministrativelydown,andVLANID100isconfiguredon
thisaccessinterface.
| switch# |      | show lldp | local-device |     |     |
| ------- | ---- | --------- | ------------ | --- | --- |
| Global  | Data |           |              |     |     |
===========
| Chassis-ID   |             |           |     | : 1c:98:ec:e3:45:00 |        |
| ------------ | ----------- | --------- | --- | ------------------- | ------ |
| System       | Name        |           |     | : switch            |        |
| System       | Description |           |     | : HPE               | ANW    |
| Management   |             | Address   |     | : 192.168.10.1      |        |
| Capabilities |             | Available |     | : Bridge,           | Router |
| Capabilities |             | Enabled   |     | : Bridge,           | Router |
| TTL          |             |           |     | : 120               |        |
| Port         | Based       | Data      |     |                     |        |
===============
| Port-ID        |             |         | :   | 1/1/11    |              |
| -------------- | ----------- | ------- | --- | --------- | ------------ |
| Port-Desc      |             |         | :   | "1/1/11"  |              |
| Port           | VLAN        | ID      | :   | 100       |              |
| Parent         | Interface   |         | :   | interface | 1/1/11       |
| Command        | History     |         |     |           |              |
| Release        |             |         |     |           | Modification |
| 10.07orearlier |             |         |     |           | --           |
| Command        | Information |         |     |           |              |
| Platforms      |             | Command |     | context   | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     |     |                    |     |
| --------- | ------------- | --- | --- | ------------------ | --- |
| show lldp | neighbor-info |     |     | [<INTERFACE-NAME>] |     |
Description
Displaysinformationaboutneighboringdevicesforallinterfacesorforaspecificinterface.The
informationdisplayedvariesdependingonthetypeofneighborconnectedandthetypeofTLVssentby
theneighbor.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<INTERFACE-NAME> Specifiestheinterfaceforwhichtoshowinformationfor
Devicediscoveryandconfiguration|258

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
neighboringdevices.Usetheformatmember/slot/port(for
example,1/3/1).
Examples
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
| Neighbor             | Port VLAN ID       | : 1                 |        |     |
| Neighbor             | Port VLAN Name     | : DEFAULT_VLAN_1    |        |     |
| Neighbor             | Port MFS           | : 1500              |        |     |
| TTL                  |                    | : 120               |        |     |
Showinginformationforinterface1/3/10whentheneighborsendsaDOT3powerTLV:
| switch# show | lldp neighbor-info | 1/3/10   |     |     |
| ------------ | ------------------ | -------- | --- | --- |
| Port         |                    | : 1/3/10 |     |     |
| Neighbor     | Entries            | : 1      |     |     |
| Neighbor     | Entries Deleted    | : 0      |     |     |
| Neighbor     | Entries Dropped    | : 0      |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 259

| Neighbor | Entries      | Aged-Out | : 0                 |     |
| -------- | ------------ | -------- | ------------------- | --- |
| Neighbor | Chassis-Name |          | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version HPE_ANW IAP
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
Neighbor Chassis-Description : hpe_anw JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |           | : 1c:98:ec:fe:25:00 |        |
| -------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor | Management-Address |           | : 10.1.1.2          |        |
| Chassis  | Capabilities       | Available | : Bridge,           | Router |
| Chassis  | Capabilities       | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |           | : 1/1/1             |        |
| Neighbor | Port               | VLAN ID   | : 1                 |        |
| Neighbor | Port               | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor | Port               | MFS       | : 1500              |        |
| TTL      |                    |           | : 120               |        |
| Neighbor | Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : hpe_anw JL375A 8400X XL.01.01.0001
| Neighbor | Chassis-ID         |           | : 1c:98:ec:fe:25:01 |        |
| -------- | ------------------ | --------- | ------------------- | ------ |
| Neighbor | Management-Address |           | : 10.1.1.3          |        |
| Chassis  | Capabilities       | Available | : Bridge,           | Router |
| Chassis  | Capabilities       | Enabled   | : Bridge,           | Router |
| Neighbor | Port-ID            |           | : 1/1/1             |        |
| Neighbor | Port-Desc          |           | : 1/1/1             |        |
| Neighbor | Port               | VLAN ID   | : 1                 |        |
| Neighbor | Port               | VLAN Name | : DEFAULT_VLAN_1    |        |
| Neighbor | Port               | MFS       | : 1500              |        |
| TTL      |                    |           | : 120               |        |
| Neighbor | Chassis-Name       |           | : switch            |        |
Devicediscoveryandconfiguration|260

Neighbor Chassis-Description : HPE ANW JL375A 8400X XL.01.01.0001
| Neighbor             | Chassis-ID         | : 1c:98:ec:fe:25:02 |        |
| -------------------- | ------------------ | ------------------- | ------ |
| Neighbor             | Management-Address | : 10.1.1.4          |        |
| Chassis Capabilities | Available          | : Bridge,           | Router |
| Chassis Capabilities | Enabled            | : Bridge,           | Router |
| Neighbor             | Port-ID            | : 1/1/1             |        |
| Neighbor             | Port-Desc          | : 1/1/1             |        |
| Neighbor             | Port VLAN ID       | : 50                |        |
| Neighbor             | Port VLAN Name     | : VLAN_50           |        |
| Neighbor             | Port MFS           | : 1500              |        |
| TTL                  |                    | : 120               |        |
| Neighbor             | Chassis-Name       | : switch            |        |
Neighbor Chassis-Description : hpe_anw JL375A 8400X XL.01.01.0001
| Neighbor             | Chassis-ID         | : 1c:98:ec:fe:25:03 |        |
| -------------------- | ------------------ | ------------------- | ------ |
| Neighbor             | Management-Address | : 10.1.1.5          |        |
| Chassis Capabilities | Available          | : Bridge,           | Router |
| Chassis Capabilities | Enabled            | : Bridge,           | Router |
| Neighbor             | Port-ID            | : 1/1/1             |        |
| Neighbor             | Port-Desc          | : 1/1/1             |        |
| Neighbor             | Port VLAN ID       | : 100               |        |
| Neighbor             | Port VLAN Name     | : VLAN_100          |        |
| Neighbor             | Port MFS           | : 1500              |        |
| TTL                  |                    | : 120               |        |
Showingneighborinformationforinterface1/3/2whenithasEEEenabledandsuccessfullyauto-
negotiated:
| switch# show         | lldp neighbor-info  | 1/3/2               |                      |
| -------------------- | ------------------- | ------------------- | -------------------- |
| Port                 |                     | : 1/3/2             |                      |
| Neighbor             | Entries             | : 1                 |                      |
| Neighbor             | Entries Deleted     | : 1                 |                      |
| Neighbor             | Entries Dropped     | : 0                 |                      |
| Neighbor             | Entries Aged-Out    | : 1                 |                      |
| Neighbor             | Chassis-Name        | : BLDG01-F1-6300    |                      |
| Neighbor             | Chassis-Description | : hpe_anw           | JL668A FL.10.15.0001 |
| Neighbor             | Chassis-ID          | : 88:3a:30:92:a5:c0 |                      |
| Neighbor             | Management-Address  | : 10.6.9.15         |                      |
| Chassis Capabilities | Available           | : Bridge,           | Router               |
| Chassis Capabilities | Enabled             | : Bridge,           | Router               |
| Neighbor             | Port-ID             | : 1/1/1             |                      |
| Neighbor             | Port-Desc           | : 1/1/1             |                      |
| Neighbor             | Port VLAN ID        | : 1                 |                      |
| Neighbor             | Port VLAN Name      | : DEFAULT_VLAN_1    |                      |
| Neighbor             | Port MFS            | : 1500              |                      |
| TTL                  |                     | : 120               |                      |
| Neighbor             | Mac-Phy details     |                     |                      |
| Neighbor             | Auto-neg Supported  | : true              |                      |
| Neighbor             | Auto-Neg Enabled    | : true              |                      |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
| Neighbor | MAU type        | : 1000  | BASETFD |
| -------- | --------------- | ------- | ------- |
| Neighbor | EEE information | : DOT3  |         |
| Neighbor | TX Wake time    | : 17 us |         |
| Neighbor | RX Wake time    | : 17 us |         |
| Neighbor | Fallback time   | : 17 us |         |
| Neighbor | TX Echo time    | : 17 us |         |
| Neighbor | RX Echo time    | : 17 us |         |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 261

| Command        | History     |         |     |         |              |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- |
| Release        |             |         |     |         | Modification |     |
| 10.07orearlier |             |         |     |         | --           |     |
| Command        | Information |         |     |         |              |     |
| Platforms      |             | Command |     | context | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp | neighbor-info |     |     | detail |     |     |
| --------- | ------------- | --- | --- | ------ | --- | --- |
| show lldp | neighbor-info |     |     | detail |     |     |
Description
ShowsdetailedLLDPneighborinformationforallLLDPneighborconnectedinterfaces.
Examples
ShowingdetailedLLDPinformationforallinterfaces:
| switch# | show     | lldp | neighbor-info |     | detail |     |
| ------- | -------- | ---- | ------------- | --- | ------ | --- |
| LLDP    | Neighbor |      | Information   |     |        |     |
=========================
| Total | Neighbor |     | Entries |          | : 6 |     |
| ----- | -------- | --- | ------- | -------- | --- | --- |
| Total | Neighbor |     | Entries | Deleted  | : 2 |     |
| Total | Neighbor |     | Entries | Dropped  | : 0 |     |
| Total | Neighbor |     | Entries | Aged-Out | : 2 |     |
--------------------------------------------------------------------------------
| Port     |              |                     |           |           | : 1/1/1             |        |
| -------- | ------------ | ------------------- | --------- | --------- | ------------------- | ------ |
| Neighbor |              | Entries             |           |           | : 1                 |        |
| Neighbor |              | Entries             | Deleted   |           | : 0                 |        |
| Neighbor |              | Entries             | Dropped   |           | : 0                 |        |
| Neighbor |              | Entries             | Aged-Out  |           | : 0                 |        |
| Neighbor |              | Chassis-Name        |           |           | : 6300              |        |
| Neighbor |              | Chassis-Description |           |           | : hpe_anw           | ...    |
| Neighbor |              | Chassis-ID          |           |           | : 38:11:17:1a:d5:00 |        |
| Neighbor |              | Management-Address  |           |           | : 38:11:17:1a:d5:00 |        |
| Chassis  | Capabilities |                     |           | Available | : Bridge,           | Router |
| Chassis  | Capabilities |                     |           | Enabled   | : Bridge,           | Router |
| Neighbor |              | Port-ID             |           |           | : 1/1/4             |        |
| Neighbor |              | Port-Desc           |           |           | : 1/1/4             |        |
| Neighbor |              | Port                | VLAN      | ID        | : 1                 |        |
| Neighbor |              | Port                | VLAN      | Name      | : DEFAULT_VLAN_1    |        |
| Neighbor |              | Port                | MFS       |           | : 1500              |        |
| TTL      |              |                     |           |           | : 120               |        |
| Neighbor |              | Mac-Phy             | details   |           |                     |        |
| Neighbor |              | Auto-neg            | Supported |           | : true              |        |
| Neighbor |              | Auto-Neg            | Enabled   |           | : true              |        |
Neighbor Auto-Neg Advertised : 1000 BASE_TFD, 100 BASE_T4, 10 BASET_FD
Devicediscoveryandconfiguration|262

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
| Port                  |          | : 1/1/46 |     |
| --------------------- | -------- | -------- | --- |
| Neighbor Entries      |          | : 1      |     |
| Neighbor Entries      | Deleted  | : 0      |     |
| Neighbor Entries      | Dropped  | : 0      |     |
| Neighbor Entries      | Aged-Out | : 0      |     |
| Neighbor Chassis-Name |          | : 6300   |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 263

| Neighbor |              | Chassis-Description |           | : hpe_anw           | ...    |
| -------- | ------------ | ------------------- | --------- | ------------------- | ------ |
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
| Neighbor       |             | Chassis-Description |          | : hpe_anw           | ... |
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
Devicediscoveryandconfiguration|264

| switch# show          | lldp neighbor-info | mgmt                   |     |
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
Neighbor Chassis-Description : HPE ANW JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:00 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.2          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : HPE ANW JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:01 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.3          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : HPE ANW JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:02 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.4          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
| Chassis Capabilities        | Enabled   | : Bridge,           | Router |
| Neighbor Port-ID            |           | : 1/1/1             |        |
| Neighbor Port-Desc          |           | : 1/1/1             |        |
| TTL                         |           | : 120               |        |
| Neighbor Chassis-Name       |           | : switch            |        |
Neighbor Chassis-Description : HPE ANW JL375A 8400X XL.01.01.0001
| Neighbor Chassis-ID         |           | : 1c:98:ec:fe:25:03 |        |
| --------------------------- | --------- | ------------------- | ------ |
| Neighbor Management-Address |           | : 10.1.1.5          |        |
| Chassis Capabilities        | Available | : Bridge,           | Router |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 265

| Chassis        | Capabilities |           | Enabled |     | : Bridge,    | Router |     |
| -------------- | ------------ | --------- | ------- | --- | ------------ | ------ | --- |
| Neighbor       |              | Port-ID   |         |     | : 1/1/1      |        |     |
| Neighbor       |              | Port-Desc |         |     | : 1/1/1      |        |     |
| TTL            |              |           |         |     | : 120        |        |     |
| Command        | History      |           |         |     |              |        |     |
| Release        |              |           |         |     | Modification |        |     |
| 10.07orearlier |              |           |         |     | --           |        |     |
| Command        | Information  |           |         |     |              |        |     |
| Platforms      |              | Command   | context |     | Authority    |        |     |
5420 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
6200
commandfromtheoperatorcontext(>)only.
| show lldp | statistics |     |                  |     |     |     |     |
| --------- | ---------- | --- | ---------------- | --- | --- | --- | --- |
| show lldp | statistics |     | [<INTERFACE-ID>] |     |     |     |     |
Description
ShowsglobalLLDPstatisticsorstatisticsforaspecificinterface.
| Parameter      |     |     |     |     | Description                                   |     |     |
| -------------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |
Example
Showingglobalstatisticsforallinterfaces:
| switch# | show   | lldp       | statistics |     |     |     |     |
| ------- | ------ | ---------- | ---------- | --- | --- | --- | --- |
| LLDP    | Global | Statistics |            |     |     |     |     |
======================
| Total | Packets |              | Transmitted  |           | :   | 19  |     |
| ----- | ------- | ------------ | ------------ | --------- | --- | --- | --- |
| Total | Packets |              | Received     |           | :   | 19  |     |
| Total | Packets |              | Received And | Discarded | :   | 0   |     |
| Total | TLVs    | Unrecognized |              |           | :   | 0   |     |
| LLDP  | Port    | Statistics   |              |           |     |     |     |
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
Devicediscoveryandconfiguration|266

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
| Port    | Name        |     |              | : mgmt |     |     |
| ------- | ----------- | --- | ------------ | ------ | --- | --- |
| Packets | Transmitted |     |              | : 20   |     |     |
| Packets | Received    |     |              | : 23   |     |     |
| Packets | Received    | And | Discarded    | : 0    |     |     |
| Packets | Received    | And | Unrecognized | : 0    |     |     |
| Command | History     |     |              |        |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 267

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
5420 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 6200 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show lldp tlv |     |     |     |
| ------------- | --- | --- | --- |
| show lldp tlv |     |     |     |
Description
ShowstheLLDPTLVsthatareconfiguredforsendandreceive.
Example
| switch# show    | lldp tlv |     |     |
| --------------- | -------- | --- | --- |
| TLVs Advertised |          |     |     |
===============
| Management          | Address |     |     |
| ------------------- | ------- | --- | --- |
| Port Description    |         |     |     |
| Port VLAN-ID        |         |     |     |
| System Capabilities |         |     |     |
| System Description  |         |     |     |
| System Name         |         |     |     |
| VLAN Name           |         |     |     |
MFS
OUI
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| Cisco Discovery |     | Protocol | (CDP) |
| --------------- | --- | -------- | ----- |
Devicediscoveryandconfiguration|268

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

Configures CDP support globally on all active interfaces or on a specific interface. By default, CDP is
enabled on all active interfaces.

When CDP is enabled, the switch adds entries to its CDP Neighbors table for any CDP packets it receives
from neighboring CDP devices.

When CDP is disabled, the CDP Neighbors table is cleared and the switch drops all inbound CDP packets
without entering the data in the CDP Neighbors table.

The no form of this command disables CDP support globally on all active interfaces or on a specific
interface.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

269

Examples
EnablingCDPglobally:
switch(config)#
cdp
DisablingCDPglobally:
| switch(config)# | no  | cdp |     |
| --------------- | --- | --- | --- |
EnablingCDPoninterface1/1/1:
| switch(config)#    | interface | 1/1/1s |     |
| ------------------ | --------- | ------ | --- |
| switch(config-if)# |           | cdp    |     |
DisablingCDPoninterface1/1/1:
switch(config)#
|                     | interface | 1/1/1   |              |
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
ClearingCDPcounters:
| switch(config)  | clear | cdp counters |              |
| --------------- | ----- | ------------ | ------------ |
| Command History |       |              |              |
| Release         |       |              | Modification |
| 10.07orearlier  |       |              | --           |
Devicediscoveryandconfiguration|270

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
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
ShowsCDPinformationforallinterfaces.
Examples
ShowingCDPinformation:
switch(config)#
|            | show        | cdp |     |
| ---------- | ----------- | --- | --- |
| CDP Global | Information |     |     |
======================
| CDP      | : Enabled      |         |     |
| -------- | -------------- | ------- | --- |
| CDP Mode | : Rx           | only    |     |
| CDP Hold | Time : 180     | seconds |     |
| Port     | CDP            |         |     |
| -------- | -------------- |         |     |
| 1/1/1    | Enabled        |         |     |
| 1/1/2    | Enabled        |         |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 271

| 1/1/3               | Enabled |         |     |              |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- |
| 1/1/4               | Enabled |         |     |              |     |     |
| 1/1/5               | Enabled |         |     |              |     |     |
| 1/1/6               | Enabled |         |     |              |     |     |
| 1/1/7               | Enabled |         |     |              |     |     |
| 1/1/8               | Enabled |         |     |              |     |     |
| 1/1/9               | Enabled |         |     |              |     |     |
| 1/1/10              | Enabled |         |     |              |     |     |
| Command History     |         |         |     |              |     |     |
| Release             |         |         |     | Modification |     |     |
| 10.07orearlier      |         |         |     | --           |     |     |
| Command Information |         |         |     |              |     |     |
| Platforms           | Command | context |     | Authority    |     |     |
config
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp neighbor-info |     |                |     |     |     |     |
| ---------------------- | --- | -------------- | --- | --- | --- | --- |
| show cdp neighbor-info |     | <INTERFACE-ID> |     |     |     |     |
Description
ShowsCDPinformationforallneighborsorforCDPinformationonaspecificinterface.
| Parameter      |     |     |     | Description                                   |     |     |
| -------------- | --- | --- | --- | --------------------------------------------- | --- | --- |
| <INTERFACE-ID> |     |     |     | Specifiesaninterface.Format:member/slot/port. |     |     |
Examples
ShowingallCDPneighborinformation:
| switch(config)# |         | show cdp | neighbor-info |     |          |            |
| --------------- | ------- | -------- | ------------- | --- | -------- | ---------- |
| Total Neighbor  | Entries |          | : 1           |     |          |            |
| Port            | Device  | ID       |               |     | Platform | Capability |
---------------------------------------------------------------------------
| 1/1/1 | HPE_ANW-3810M-24G-1-slot... |     |     |     | HPE ANW Sw | S   |
| ----- | --------------------------- | --- | --- | --- | ---------- | --- |
ShowingCDPinformationforinterface1/1/1:
| switch(config)# |     | show cdp                                  | neighbor-info |     | 1/1/1 |     |
| --------------- | --- | ----------------------------------------- | ------------- | --- | ----- | --- |
| Local Port      |     | : 1/1/1                                   |               |     |       |     |
| MAC             |     | : 70:10:6f:86:78:7f                       |               |     |       |     |
| Device ID       |     | : HPE_ANW-3810M-24G-1-slot(70106f-867800) |               |     |       |     |
| Address         |     | : 127.0.0.1                               |               |     |       |     |
| Platform        |     | : HPE ANW                                 | Sw            |     |       |     |
| Duplex          |     | : half                                    |               |     |       |     |
Devicediscoveryandconfiguration|272

| Version        |             | :   | Revision | KB.16.07.0002, |              | ROM KB.16.01.... |     |     |
| -------------- | ----------- | --- | -------- | -------------- | ------------ | ---------------- | --- | --- |
| Capability     |             | :   | switch   |                |              |                  |     |     |
| Native VLAN    |             | :   | 1        |                |              |                  |     |     |
| Voice VLAN     | Support     | :   | No       |                |              |                  |     |     |
| Neighbor       | Port-ID     | :   | 1        |                |              |                  |     |     |
| Command        | History     |     |          |                |              |                  |     |     |
| Release        |             |     |          |                | Modification |                  |     |     |
| 10.07orearlier |             |     |          |                | --           |                  |     |     |
| Command        | Information |     |          |                |              |                  |     |     |
| Platforms      | Command     |     | context  |                | Authority    |                  |     |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show cdp traffic |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
show cdp traffic
Description
ShowsCDPstatisticsforeachinterface.
Examples
ShowingCDPtrafficstatistics:
| switch(config)# |     | show | cdp traffic |     |     |     |     |     |
| --------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- |
CDP Statistics
====================
| Port | Transmitted |     | Frames |     | Received | Frames | Discarded | Frames |
| ---- | ----------- | --- | ------ | --- | -------- | ------ | --------- | ------ |
--------------------------------------------------------------------------------
| 1/1/1          | 0           |     |         |     | 4            |     | 0   |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- |
| 1/1/2          | 0           |     |         |     | 0            |     | 0   |     |
| 1/1/3          | 0           |     |         |     | 2            |     | 0   |     |
| 1/1/4          | 0           |     |         |     | 0            |     | 0   |     |
| 1/1/5          | 0           |     |         |     | 0            |     | 0   |     |
| Command        | History     |     |         |     |              |     |     |     |
| Release        |             |     |         |     | Modification |     |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |     |
| Command        | Information |     |         |     |              |     |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |     |
config
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 273

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
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Devicediscoveryandconfiguration|274

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

o Aruba Central on-premise can manage AOS-CX switches on supported models through DHCP ZTP

using two approaches:

l On the DHCP server, configure DHCP option-60 as "ArubaInstantAP" 90 and provide the value
in option-43 in the format <group-details>, <aruba-central-on-prem-ip-or-fqdn>, <shared-token>.

l On the DHCP server, configure DHCP option-60 as HPE vendor VCI and provide the value in

option-43 in the tag-length-value (TLV) format. Next, enter the Aruba Central on-premise fully

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

275

qualified domain name (FQDN) or IPv4 address as the value for sub-option code 146 using the
format: <group-details>, <aruba-central-on-prem-ip-or-fqdn>, <shared-token>.

Supported ZTP options from a DHCPv4 server are:

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

FQDN or IPv4 or IPv6 address of the HTTP Proxy

60

66

67

Vendor Class Identifier (VCI)

IPv4 or IPv6 address of the TFTP or HTTP server (Specifying a
host name instead of an IP address is not supported.)

Name of the configuration file (Option 43 suboption 144 takes
precedence over this option.)

Unique ZTP IPv6 options can be sent from the DHCPv6 Server based on MAC address of the switch or
based on the DHCP Vendor class Identifier of the switch. Supported ZTP options from a DHCPv6 server
are:

DHCP option

59

Description

IPv6 address of the TFTP/HTTP server. The image file name also
can be given in this URL or in the VCA option-17.

NOTE: the boot file URL will support TFTPv6 Server or HTTP Server
option with IPv6 address or FQDN name.

17 suboption 145

17 suboption 144

Name of the image file.

Name of the configuration file.

The switch supports the following standards:

n RFC 2131, Dynamic Host Configuration Protocol.

n RFC 2132, DHCP Options and BOOTP Vendor Extensions. Support is limited to the options listed in the

table "Supported DHCP options for ZTP on AOS-CX."

n RFC 5970, DHCPv6 Options for Network Boot. Support is limited to the options listed in the table

"Supported DHCP options for ZTP on AOS-CX."

Hewlett Packard Enterprise recommends that you implement ZTP in a secure and private environment.
Any public access can compromise the security of the switch, as follows:

Zero Touch Provisioning | 276

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

2. Set up a TFTP or HTTP server and record its IPv4 or IPv6 address. The address is required when

you set up the DHCP server. The switch must be able to reach the TFTP or HTTP server and DHCP
server, either on the same subnet, or on a remote subnet via DHCP relay.

Switches support provisioning through a network connected to a data port or through a network
connected to the management port.

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

277

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

Zero Touch Provisioning | 278

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

279

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

Either the file transfer of the firmware image file failed, or the firmware image file is invalid
(an error occurred while verifying the image).

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

Failed - Invalid
image file
received

Failed - HTTP

The HTTP server is not reachable at the specified IP address

server

unreachable

In the case of reconnection, connect with a main or alternative location to the COP instance as a user. The

current connection is shown in the Central location field.

Scenario 1: If the location the device is currently connected on is updated, the system reconnects in order to

connect with the new location.

Scenario 2: If the location in which the device is not currently connected on is updated, the DUT does not go

through the reconnection process.

Examples

Showing switch image and config download from an IPv4 TFTP server in progress after receiving
ZTP options:

Zero Touch Provisioning | 280

| switch#         | show ztp information |                  |     |                     |         |                           |
| --------------- | -------------------- | ---------------- | --- | ------------------- | ------- | ------------------------- |
| TFTP Server     |                      |                  |     | : 10.0.0.2          |         |                           |
| Image File      |                      |                  |     | : TL_10_02_0001.swi |         |                           |
| Configuration   | File                 |                  |     | : ztp.cfg           |         |                           |
| ZTP Status      |                      |                  |     | : In-progress       | - Image | download and verification |
| HPE ANW         | Central Location     |                  |     | : NA                |         |                           |
| Alternative     | HPE ANW              | Central Location |     | : NA                |         |                           |
| HPE ANW         | Central Shared       | Token            |     | : NA                |         |                           |
| Force-Provision |                      |                  |     | : Enabled           |         |                           |
| HTTP Proxy      | Location             |                  |     | : NA                |         |                           |
ShowingswitchimagedownloadfailurefromanIPv4TFTPserverbecausetheserverwasunreachable
| switch#         | show ztp information |                  |     |                     |               |             |
| --------------- | -------------------- | ---------------- | --- | ------------------- | ------------- | ----------- |
| TFTP Server     |                      |                  |     | : 10.0.0.2          |               |             |
| Image File      |                      |                  |     | : TL_10_02_0001.swi |               |             |
| Configuration   | File                 |                  |     | : ztpv6.cfg         |               |             |
| ZTP Status      |                      |                  |     | : Failed            | - TFTP server | unreachable |
| HPE ANW         | Central Location     |                  |     | : NA                |               |             |
| Alternative     | HPE ANW              | Central Location |     | : NA                |               |             |
| HPE ANW         | Central Shared       | Token            |     | : NA                |               |             |
| Force-Provision |                      |                  |     | : Enabled           |               |             |
| HTTP Proxy      | Location             |                  |     | : NA                |               |             |
ShowingasuccessfulswitchconfigurationdownloadfromanIPv6HTTPserver
| switch#         | show ztp information |                  |              |                     |     |     |
| --------------- | -------------------- | ---------------- | ------------ | ------------------- | --- | --- |
| HTTP Server     |                      |                  |              | : http://[2001::50] |     |     |
| Image File      |                      |                  |              | : TL_10_15_0001.swi |     |     |
| Configuration   | File                 |                  |              | : config_file       |     |     |
| ZTP Status      |                      |                  |              | : Success           |     |     |
| HPE ANW         | Central Location     |                  |              | : NA                |     |     |
| Alternative     | HPE ANW              | Central Location |              | : NA                |     |     |
| HPE ANW         | Central Shared       | Token            |              | : NA                |     |     |
| Force-Provision |                      |                  |              | : Enabled           |     |     |
| HTTP Proxy      | Location             |                  |              | : NA                |     |     |
| Command         | History              |                  |              |                     |     |     |
| Release         |                      |                  | Modification |                     |     |     |
| 10.07orearlier  |                      |                  | --           |                     |     |     |
| Command         | Information          |                  |              |                     |     |     |
| Platforms       | Command              | context          | Authority    |                     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| ztp force | provision |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- |
ztp force-provision
no ztp force-provision
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 281

Description
Startson-demandZTP.
Usage
DHCPoptionsreceivedareprocessedindependentofthecurrentstateofconfigurationontheswitch.
PreviousZTPTFTPServer,ImageFile,ConfigurationFile,HPE ArubaNetworkingCentralLocation,and
HTTPProxylocationoptionsareclearedandtheswitchsendsaDHCPrequest.
Examples
Inthefollowingexample,force-provisionisenabled.
| switch#         | configure terminal  |     |
| --------------- | ------------------- | --- |
| switch(config)# | ztp force-provision |     |
Inthefollowingexample,force-provisionstatusischeckedwhileenabled.
| switch#         | show ztp information |                     |
| --------------- | -------------------- | ------------------- |
| TFTP Server     |                      | : 10.0.0.2          |
| Image File      |                      | : TL_10_02_0001.swi |
| Configuration   | File                 | : ztp.cfg           |
| Status          |                      | : Success           |
| HPE ANW         | Central Location     | : NA                |
| HPE ANW         | Central Shared Token | : NA                |
| Force-Provision |                      | : Enabled           |
| HTTP Proxy      | Location             | : NA                |
Inthefollowingexample,force-provisionisdisabled.
switch#
configure terminal
| switch(config)# | no ztp force-provision |     |
| --------------- | ---------------------- | --- |
Inthefollowingexample,force-provisionstatusischeckedwhiledisabled.
| switch#         | show ztp information |                     |
| --------------- | -------------------- | ------------------- |
| TFTP Server     |                      | : 10.0.0.2          |
| Image File      |                      | : TL_10_02_0001.swi |
| Configuration   | File                 | : ztp.cfg           |
| Status          |                      | : Success           |
| HPE ANW         | Central Location     | : NA                |
| HPE ANW         | Central Shared Token | : NA                |
| Force-Provision |                      | : Disabled          |
| HTTP Proxy      | Location             | : NA                |
| Command         | History              |                     |
Release Modification
10.07orearlier --
| Command | Information |     |
| ------- | ----------- | --- |
ZeroTouchProvisioning|282

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Administrators or local user group members with execution
rights for this command.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

283

Chapter 16
|               |     |          |     | Switch   | system | and | hardware | commands |
| ------------- | --- | -------- | --- | -------- | ------ | --- | -------- | -------- |
| Switch system | and | hardware |     | commands |        |     |          |          |
allow-non-failsafe-updates
Syntaxfor10.15.1010andlaterreleases:allow-non-failsafe-updates <num_minutes>
Syntaxfor10.15.0001-10.15.1000:allow-unsafe-updates <num_minutes>
Description
Allownon-failsafeupdatesofprogrammabledevicesforthespecifiednumberofminutes,orenter0to
disallowunsafeupdates.Themaximumpermittedvalueis120minutes.
Example
Thefollowingexamplewillenablenon-failsafeupdatesofprogrammabledevicesforthenext30
minutes.
| switch(config)# |     | allow- |     | non-failsafe-updates |     | 30  |     |     |
| --------------- | --- | ------ | --- | -------------------- | --- | --- | --- | --- |
This command will enable non-failsafe updates of programmable devices for
the next 30 minutes. You will first need to wait for all line and fabric
modules to reach the ready state, and then reboot the switch to begin applying any
needed
updates. Ensure that the switch will not lose power, be rebooted again, or have
any
modules removed until all updates have finished and all line and fabric modules
have
| returned | to the | ready | state |     |     |     |     |     |
| -------- | ------ | ----- | ----- | --- | --- | --- | --- | --- |
WARNING: Interrupting these updates may make the product unusable!
| Continue        | [y/n] | ? y |           |                                                  |         |           |            |     |
| --------------- | ----- | --- | --------- | ------------------------------------------------ | ------- | --------- | ---------- | --- |
| Unsafe updates  |       |     | : allowed | (less                                            | than 30 | minute(s) | remaining) |     |
| Command History |       |     |           |                                                  |         |           |            |     |
| Release         |       |     |           | Modification                                     |         |           |            |     |
| 10.15.1010      |       |     |           | Thesyntaxofthiscommandischangedfromallow-unsafe- |         |           |            |     |
updatestoallow-non-failsafe-updates.
| 10.07orearlier      |     |     |     | --  |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Command Information |     |     |     |     |     |     |     |     |
284
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries)

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| bluetooth         | disable |     |     |
| ----------------- | ------- | --- | --- |
| bluetooth disable |         |     |     |
| no bluetooth      | disable |     |     |
Description
DisablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesbothBluetoothClassicand
BluetoothLowEnergy(BLE).Bluetoothisenabledbydefault.
ThenoformofthiscommandenablestheBluetoothfeatureontheswitch.
Example
DisablingBluetoothontheswitch.<XXXX>istheswitchplatformand<NNNNNNNNNN>isthedevice
identifier.
| switch(config)# | bluetooth | disable               |     |
| --------------- | --------- | --------------------- | --- |
| switch# show    | bluetooth |                       |     |
| Enabled         |           | : No                  |     |
| Device name     |           | : <XXXX>-<NNNNNNNNNN> |     |
| switch(config)# | show      | running-config        |     |
...
| bluetooth | disabled |     |     |
| --------- | -------- | --- | --- |
...
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200             |        |     | rightsforthiscommand. |
| ---------------- | ------ | --- | --------------------- |
| bluetooth        | enable |     |                       |
| bluetooth enable |        |     |                       |
| no bluetooth     | enable |     |                       |
Description
ThiscommandenablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesboth
BluetoothClassicandBluetoothLowEnergy(BLE).
Default:Bluetoothisenabledbydefault.
Switchsystemandhardwarecommands|285

ThenoformofthiscommanddisablestheBluetoothfeatureontheswitch.
Usage
ThedefaultconfigurationoftheBluetoothfeatureisenabled.Theoutputoftheshow
running-config
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
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
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
| utilization   | poll interval | is changed | to 49 |
| ------------- | ------------- | ---------- | ----- |
| switch# clear | events        |            |       |
| switch# show  | events        |            |       |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 286

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
| Command        | History     |         |                                                    |
| -------------- | ----------- | ------- | -------------------------------------------------- |
| Release        |             |         | Modification                                       |
| 10.07orearlier |             |         | --                                                 |
| Command        | Information |         |                                                    |
| Platforms      | Command     | context | Authority                                          |
| 5420           |             |         | Administratorsorlocalusergroupmemberswithexecution |
Manager(#)
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
Switchsystemandhardwarecommands|287

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
domain-name
| domain-name    | <NAME> |          |     |     |     |     |
| -------------- | ------ | -------- | --- | --- | --- | --- |
| no domain-name |        | [<NAME>] |     |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 288

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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| front-panel-security    |               | factory-reset |     |
| ----------------------- | ------------- | ------------- | --- |
| front-panel-security    | factory-reset |               |     |
| no front-panel-security |               | factory-reset |     |
Description
Enablethefront-panel factory-resetfeaturetoallowafactoryresetviatheresetbuttononthefront
paneloftheswitch,withoutconsoleaccess.Oncethefeatureisenabled,thissettingwillbesaved
acrossreboots,untilafactory-resetisperformed.Thenoformofthiscommanddisablesthefront-
panelfactory-resetfeatureafterithasbeenenabled.Thisfeatureisdisabledbydefault.
Switchsystemandhardwarecommands|289

Usage
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
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
hostname
hostname <HOSTNAME>
| no hostname | [<HOSTNAME>] |     |     |
| ----------- | ------------ | --- | --- |
Description
Setsthehostnameoftheswitch.
Thenoformofthiscommandsetsthehostnametothedefaultvalue,whichisswitch.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 290

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
mtrace
mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
[vrf <VRF-NAME>]
Description
TracesthespecifiedIPv4sourceandgroupaddresses.
| Parameter     |     |     | Description                           |
| ------------- | --- | --- | ------------------------------------- |
| IPV4-SRC-ADDR |     |     | SpecifiesthesourceIPv4addresstotrace. |
IPV4-GROUP-ADDR
SpecifiesthegroupIPv4addresstotrace.
lhr <IPV4-LHR-ADDR> Specifiesthelasthoprouteraddressfromwhichtostartthetrace.
Switchsystemandhardwarecommands|291

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
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200  |                            |     |     |     | rightsforthiscommand. |     |     |
| ----- | -------------------------- | --- | --- | --- | --------------------- | --- | --- |
| power | consumption-average-period |     |     |     |                       |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 292

| power consumption-average-period |     | <PERIOD-IN-SECONDS> |     |     |
| -------------------------------- | --- | ------------------- | --- | --- |
Description
Configuresatimeperiodforaveragepowerconsumptioninseconds.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PERIOD-IN-SECONDS> Specifiestheperiodinsecondsforaveragepowerconsumed.
Range:60-3600.Default:600
Formoreinformationonthisfeature,seethevideoAOS-CX10.14ReleaseUpdate:Sustainability
Update.
Example
Configuringatimeperiodof60secondsforaveragepowerconsumption:
| switch(config)#     | power   | consumption-average-period |                    | 60  |
| ------------------- | ------- | -------------------------- | ------------------ | --- |
| Command History     |         |                            |                    |     |
| Release             |         |                            | Modification       |     |
| 10.13               |         |                            | Commandintroduced. |     |
| Command Information |         |                            |                    |     |
| Platforms           | Command | context                    | Authority          |     |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
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
Thedevicenamegiventotheswitchincludestheswitchserialnumbertouniquelyidentifytheswitch
whilepairingwithamobiledevice.
Switchsystemandhardwarecommands|293

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
| switch#        | show bluetooth |                       |              |     |     |
| -------------- | -------------- | --------------------- | ------------ | --- | --- |
| Enabled        |                | : No                  |              |     |     |
| Device name    |                | : <XXXX>-<NNNNNNNNNN> |              |     |     |
| Command        | History        |                       |              |     |     |
| Release        |                |                       | Modification |     |     |
| 10.07orearlier |                |                       | --           |     |     |
| Command        | Information    |                       |              |     |     |
| Platforms      | Command        | context               | Authority    |     |     |
5420 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6200 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show boot-history |           |        |          |     |     |
| ----------------- | --------- | ------ | -------- | --- | --- |
| show boot-history | [all|{vsf | member | <1-10>}] |     |     |
Description
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 294

Shows boot history information. When no parameters are specified, shows the most recent information
about the current boot operation, and the three previous boot operations for the switch. When the all
parameter is specified, the output of this command shows the boot information for the active
management module.

.

To view boot-history on a standby, the command must be sent on the conductor console.

Parameter

all

Description

Optional. Shows boot information for the active management
module.

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

Switch system and hardware commands | 295

| switch#    | show boot-history |     |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
| Management | module            |     |     |     |     |
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 296

| Index :     | 2                                  |          |           |     |                  |
| ----------- | ---------------------------------- | -------- | --------- | --- | ---------------- |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |          |           |     |                  |
| 07 Aug      | 18 16:28:01                        | : Reboot | requested |     | through database |
| Index :     | 1                                  |          |           |     |                  |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |          |           |     |                  |
| 07 Aug      | 18 14:08:46                        | : Reboot | requested |     | through database |
| Index :     | 0                                  |          |           |     |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |          |           |     |                  |
| 07 Aug      | 18 13:00:46                        | : Reboot | requested |     | through database |
| Line module | 1/1                                |          |           |     |                  |
=================
| Index : | 3           |              |     |         |     |
| ------- | ----------- | ------------ | --- | ------- | --- |
| 10 Aug  | 17 12:45:46 | : dune_agent |     | crashed |     |
...
ThefollowingexampledisplaystheboothistoryfortheVSFmember2.
| switch# | show boot-history |     | vsf | member | 2   |
| ------- | ----------------- | --- | --- | ------ | --- |
Member-2
=========
| Index :        | 0                                  |          |           |       |                  |
| -------------- | ---------------------------------- | -------- | --------- | ----- | ---------------- |
| Boot ID        | : df99026c194a44f1944a3e7685fb4d90 |          |           |       |                  |
| Current        | Boot, up for                       | 3        | hrs 31    | mins  | 39 secs          |
| Index :        | 3                                  |          |           |       |                  |
| Boot ID        | : 7bf4104903fe4ad1ba4bce40e8099c76 |          |           |       |                  |
| 10 Aug         | 17 10:02:24                        | : Reboot | requested |       | through database |
| 10 Aug         | 17 10:02:13                        | : Switch | boot      | count | is 2             |
| Command        | History                            |          |           |       |                  |
| Release        |                                    |          |           |       | Modification     |
| 10.07orearlier |                                    |          |           |       | --               |
| Command        | Information                        |          |           |       |                  |
| Platforms      | Command                            | context  |           |       | Authority        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show capacities
| show capacities | <FEATURE> |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
Switchsystemandhardwarecommands|297

| Parameter |     |     |     | Description                       |     |     |
| --------- | --- | --- | --- | --------------------------------- | --- | --- |
| <FEATURE> |     |     |     | Specifiesafeature.Forexample,aaa. |     |     |
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities |        | mirroring |     |     |       |
| ------------------ | --------------- | ------ | --------- | --- | --- | ----- |
| System Capacities: |                 | Filter | Mirroring |     |     |       |
| Capacities         | Name            |        |           |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | Mirror | Sessions | configurable | in a system |     |
| ------- | --------- | ------ | -------- | ------------ | ----------- | --- |
4
| Maximum | number of | enabled | Mirror | Sessions | in a system |     |
| ------- | --------- | ------- | ------ | -------- | ----------- | --- |
4
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities |        | mstp |     |     |       |
| ------------------ | --------------- | ------ | ---- | --- | --- | ----- |
| System Capacities: |                 | Filter | MSTP |     |     |       |
| Capacities         | Name            |        |      |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | mstp | instances | configurable | in a system |     |
| ------- | --------- | ---- | --------- | ------------ | ----------- | --- |
64
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities |        | vlan-count |       |     |       |
| ------------------ | --------------- | ------ | ---------- | ----- | --- | ----- |
| System Capacities: |                 | Filter | VLAN       | Count |     |       |
| Capacities         | Name            |        |            |       |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of | VLANs | supported | in the | system |     |
| ------- | --------- | ----- | --------- | ------ | ------ | --- |
4094
| Command        | History     |     |     |              |     |     |
| -------------- | ----------- | --- | --- | ------------ | --- | --- |
| Release        |             |     |     | Modification |     |     |
| 10.07orearlier |             |     |     | --           |     |     |
| Command        | Information |     |     |              |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 298

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show capacities-status
| show capacities-status |     | <FEATURE> |     |     |
| ---------------------- | --- | --------- | --- | --- |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<FEATURE> Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplay
capacities,values,andstatus.Required.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
| switch#    | show capacities-status |     |     |               |
| ---------- | ---------------------- | --- | --- | ------------- |
| System     | Capacities Status      |     |     |               |
| Capacities | Status Name            |     |     | Value Maximum |
------------------------------------------------------------------------------
| Number | of active gateway  | mac addresses | in a system | 0 16 |
| ------ | ------------------ | ------------- | ----------- | ---- |
| Number | of aspath-lists    | configured    |             | 0 64 |
| Number | of community-lists | configured    |             | 0 64 |
...
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
show console
show console
Description
Showstheserialconsoleportcurrentspeed.
Examples
Switchsystemandhardwarecommands|299

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
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
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
Instance ID
IdentifiesthespecificinstanceofthedaemonshownintheDaemonNamecolumn.
Present
Indicatesthestatusofthecoredump:
Yes
Thecoredumphascompletedandavailableforcopying.
In Progress
Coredumpgenerationisinprogress.Donotattempttocopythiscoredump.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 300

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
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Release Modification
10.07orearlier --
| Command Information |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
Switchsystemandhardwarecommands|301

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show deprecated          |     | commands    |     |     |     |     |
| ------------------------ | --- | ----------- | --- | --- | --- | --- |
| show deprecated-commands |     | [<feature>] |     |     |     |     |
Description
ShowsthelistofCLIcommandsthatwillbedeprecatedinafuturereleasealongwiththenewformof
thesamecommandwhichisrecommendedforuse.
Boththecommandoptionswillbesupporteduntilacertainrelease,afterwhichonlythenewer
replacementcommandwillbesupported.
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
| switch# show | deprecated-commands |            |     | vsf       |     |     |
| ------------ | ------------------- | ---------- | --- | --------- | --- | --- |
| Feature vsf  | has no              | deprecated |     | commands. |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 302

| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.14               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show environment |           | fan |     |
| ---------------- | --------- | --- | --- |
| show environment | fan [vsf] |     |     |
Switchsystemandhardwarecommands|303

Description
Showsthestatusinformationforallfansandfantrays(ifpresent)inthesystem.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
vsf
ShowsoutputfromtheVSFmember-idonswitchesthat
supportVSF.
Usage
Forfantrays,Statusisoneofthefollowingvalues:
n ready:Thefantrayisoperatingnormally.
n fault:Thefantrayisinafaultevent.Thestatusofthefantraydoesnotindicatethestatusoffans.
n empty:Thefantrayisnotinstalledinthesystem.
Forfans:
Speed :Indicates the relative speed of the fan based on the nominal speed range of the
| fan. Values | are:   |                |         |           |                |         |         |        |
| ----------- | ------ | -------------- | ------- | --------- | -------------- | ------- | ------- | ------ |
| Slow:The    | fan is | running        | at      | less than | 25% of         | its     | maximum | speed. |
| Normal:The  | fan    | is running     | at      | 25-49%    | of its         | maximum | speed.  |        |
| Medium:The  | fan    | is running     | at      | 50-74%    | of its         | maximum | speed.  |        |
| Fast:The    | fan is | running        | at      | 75-99%    | of its maximum |         | speed.  |        |
| Max:The     | fan is | running        | at 100% | of        | its maximum    | speed.  |         |        |
| N/A:The     | fan is | not installed. |         |           |                |         |         |        |
Direction: The direction of airflow through the fan. Values are:
front-to-back:Air flows from the front of the system to the back of the system.
| N/A:The           | fan is  | not installed. |            |           |                 |     |     |     |
| ----------------- | ------- | -------------- | ---------- | --------- | --------------- | --- | --- | --- |
| Status: Fan       | status. | Values         | are:       |           |                 |     |     |     |
| uninitialized:The |         | fan            | has not    | completed | initialization. |     |     |     |
| ok: The           | fan is  | operating      | normally.  |           |                 |     |     |     |
| fault:            | The fan | is in          | a fault    | state.    |                 |     |     |     |
| empty:            | The fan | is not         | installed. |           |                 |     |     |     |
Examples
Showingoutputforasystemwithoutafantray:
| switch#         | show environment |     | fan |     |     |     |     |     |
| --------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| Fan information |                  |     |     |     |     |     |     |     |
---------------------------------------------------------------
| Fan | Serial Number |     | Speed | Direction |     | Status |     | RPM |
| --- | ------------- | --- | ----- | --------- | --- | ------ | --- | --- |
---------------------------------------------------------------
| 1   | SGXXXXXXXXXX |     | slow   | front-to-back |     | ok    |     | 6000  |
| --- | ------------ | --- | ------ | ------------- | --- | ----- | --- | ----- |
| 2   | SGXXXXXXXXXX |     | normal | front-to-back |     | ok    |     | 8000  |
| 3   | SGXXXXXXXXXX |     | medium | front-to-back |     | ok    |     | 11000 |
| 4   | SGXXXXXXXXXX |     | fast   | front-to-back |     | ok    |     | 14000 |
| 5   | SGXXXXXXXXXX |     | max    | front-to-back |     | fault |     | 16500 |
| 6   | N/A          |     | N/A    | N/A           |     | empty |     |       |
...
| Command | History |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 304

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show environment |                 | led |     |
| ---------------- | --------------- | --- | --- |
| show environment | led <MEMBER-ID> |     |     |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
| Parameter   |     |     | Description                               |
| ----------- | --- | --- | ----------------------------------------- |
| <MEMBER-ID> |     |     | ShowsoutputfromthespecifiedVSFmemberID on |
switchesthatsupportVSF.
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
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show environment |                   | power-consumption |                    |
| ---------------- | ----------------- | ----------------- | ------------------ |
| show environment | power-consumption |                   | [detail]           |
| show environment | power-consumption |                   | member <MEMBER-ID> |
Switchsystemandhardwarecommands|305

Description
Displayspowerconsumptioninformation.
| Parameter   |     |     | Description                                   |     |     |     |
| ----------- | --- | --- | --------------------------------------------- | --- | --- | --- |
| [detail}    |     |     | Displaysdetailedpowerconsumptioninformation.  |     |     |     |
| <MEMBER-ID> |     |     | ForVSFsupportedplatformsonly.Displaysthepower |     |     |     |
consumptioninformationforthespecifiedVSF member. Range:1-
10.
Usage
Powerconsumedvaluesareupdatedevery5seconds.Thetotalpowerconsumedisthetotalpower
usedinachassis.Thepowerconsumedaverageiscalculatedfromthetotalpowerconsumedasa
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
n powertotal:totalpowerconsumption
averagepower:averagefortotalpowerconsumptionthatiscalculatedoveragivenperiod
n
n averageperiod:timetocalculatepoweraverage
Example
Showingthepowerconsumptionfora1RUswitch:
| switch# show      | environment | power-consumption |               |           |            |         |
| ----------------- | ----------- | ----------------- | ------------- | --------- | ---------- | ------- |
| Power Consumption | Averaging   | Period            | : 600 seconds |           |            |         |
|                   |             |                   | Power         | Usage (W) | PSU Output | (W)     |
| Name Description  |             |                   | Instant       | Average   | Instant    | Average |
----------------------------------------------------------------------------
| 1 8360-32Y4C | v2 Switch |     | 120.00 | 111.16 | 111.00 | 102.62 |
| ------------ | --------- | --- | ------ | ------ | ------ | ------ |
ShowingthepowerconsumptionforaVSFstack:
| switch# show      | environment | power-consumption |               |           |            |     |
| ----------------- | ----------- | ----------------- | ------------- | --------- | ---------- | --- |
| Power Consumption | Averaging   | Period            | : 600 seconds |           |            |     |
|                   |             |                   | Power         | Usage (W) | PSU Output | (W) |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 306

Name Description
----------------------------------------------------------------------------
1
2

6200M 24G 4SFP+ Sw
6200M 24G 4SFP+ Sw

311.50
275.50

349.62
299.50

350.00
300.00

300.00
280.00

Average

Instant

Instant

Average

Showing the power consumption for a switch where input reading is not supported:

switch# show environment power-consumption

Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

Name Description
----------------------------------------------------------------------------
1

6200M 24G 4SFP+ Sw

Instant

Average

Average

Instant

321.00

330.30

N/A

N/A

Showing the power consumption for a switch with multiple line cards, in brief:

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

798.00

900.00

905.62

803.23

Showing the power consumption for a switch with multiple line cards, in detail:

switch# show environment power-consumption detail
Power Consumption Averaging Period : 600 seconds

Power Usage (W)

PSU Output (W)

1499.99

Average

1300.67

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

Switch system and hardware commands | 307

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

Average

Average

Instant

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

275.50

300.00

299.50

280.00

Showing the power consumption for VSF invalid member:

switch# show environment power-consumption member 5
Member 5 is not present

Command History

Release

10.14.1000

10.13

Command Information

Modification

Introduced enhancement to power consumption and power
consumption average.

Command introduced.

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Administrators or local user group members with execution
rights for this command.

show environment power-consumption power-over-
ethernet
show environment power consumption power-over-ethernet

show environment power-consumption power-over-ethernet detail <DETAIL>

show environment power-consumption power-over-ethernet member <MEMBER-ID>

show environment power-consumption power-over-ethernet interface <INTERFACE>

Description

Displays the PoE power consumption information.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

308

| Parameter |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- |
| <DETAIL>  |     |     |     | DisplaysdetailedPoEpowerconsumptioninformation.   |     |
| <ARG-1>   |     |     |     | ForVSFsupportedplatformsonly.DisplaystheVSFmember |     |
command.
| <ARG-2> |     |     |     | ForVSFsupportedplatformsonly.Displaysthepower |     |
| ------- | --- | --- | --- | --------------------------------------------- | --- |
consumptioninformationforthespecifiedVSF member. Range:1-
10.
| INTERFACE |     |     |     | DisplaystheinterfacenamewithPoEcapability.       |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- |
| <MEMBER>  |     |     |     | ForVSFsupportedplatformsonly.DisplaysthePoEpower |     |
consumptionforastackmember.
Usage
ForeachPoEcapablemodule,thePoEpowerconsumedisdisplayed.PoEpowerconsumedvaluesare
collectedonceeverysamplingperiodandtheaveragevalueiscalculatedovertheaverageperiod.The
totalpowerconsumedisthetotalpowerofthePoEdevicesinachassis.TheaveragePoEpower
consumediscalculatedfromthetotalPoEpowerconsumedasarunningaverageoveraperiodoftime.
Thedefaultaverageperiodis10minutes.Theminimumaverageperiodcanbesetto60secondsand
maximumto3600seconds.Theaverageperiodcanbeconfiguredusingpower consumption-average-
period.ForVSFplatforms,thiscommanddisplaysthePoEpowerconsumedforallmembers.
Thefollowinginformationisprovidedforsummaryofpowerconsumption:
n linemodule-PoEpowerusedbylinemodule
n chassismodule-PoEpowerusedbychassismodule
PoEPowertotal-totalPoEpowerconsumption
n
n PoEPoweraverage-averagefortotalPoEpowerconsumptionthatiscalculatedoveragivenperiod
n averageperiod-timetocalculatepoweraverage
Example
ShowingthePOEinstantaneouspowerconsumptionforaswitch,inbrief:
| switch#           | show environment |           | power-consumption |       | power-over-ethernet |
| ----------------- | ---------------- | --------- | ----------------- | ----- | ------------------- |
| Power Consumption |                  | Averaging | Period            | : 600 | seconds             |
|                   |                  |           |                   | PoE   | Average             |
| Name Description  |                  |           |                   |       | Usage (W)           |
--------------------------------------------------
| 1 6300M | 48SR10 | CL8 | PoE 4p100G | Sw  | 401.41 |
| ------- | ------ | --- | ---------- | --- | ------ |
ShowingthePOEpowerconsumptionforaVSFstack,inbrief:
| switch#           | show environment |           | power-consumption |       | power-over-ethernet |
| ----------------- | ---------------- | --------- | ----------------- | ----- | ------------------- |
| Power Consumption |                  | Averaging | Period            | : 120 | seconds             |
|                   |                  |           |                   | PoE   | Average             |
| Name Description  |                  |           |                   |       | Usage (W)           |
Switchsystemandhardwarecommands|309

--------------------------------------------------
| 1 6300M | 24SR5 | CL6 | PoE        | 4SFP56 | Swc  | 23.86  |
| ------- | ----- | --- | ---------- | ------ | ---- | ------ |
| 2 6300M | 48G   | CL4 | PoE 4SFP56 |        | Swch | 11.27  |
| 3 6300F | 24G   | CL4 | PoE 4SFP56 |        | Sw   | 197.60 |
ShowingthePOEpowerconsumptionforachassis,inbrief:
| switch#           | show | environment |           | power-consumption |       | power-over-ethernet |
| ----------------- | ---- | ----------- | --------- | ----------------- | ----- | ------------------- |
| Power Consumption |      |             | Averaging | Period            | : 600 | seconds             |
|                   |      |             |           |                   | PoE   | Average             |
| Name Description  |      |             |           |                   |       | Usage (W)           |
--------------------------------------------------
| 1 6405 | Chassis |     |     |     |     | 120.11 |
| ------ | ------- | --- | --- | --- | --- | ------ |
ShowingthePOEpowerconsumptionforastandaloneswitch,indetail:
switch# show environment power-consumption power-over-ethernet detail
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 310

ShowingthePOEpowerconsumptionfor3memberVSFstack,indetail:
switch# show environment power-consumption power-over-ethernet detail
| Power Consumption |     |     | Averaging | Period : | 120 seconds |
| ----------------- | --- | --- | --------- | -------- | ----------- |
PoE Average
| Name Description |     |     |     |     | Usage (W) |
| ---------------- | --- | --- | --- | --- | --------- |
--------------------------------------------------
| 1 6300M | 24SR5         | CL6 | PoE        | 4SFP56 Swc | 24.09  |
| ------- | ------------- | --- | ---------- | ---------- | ------ |
| 2 6300M | 48G           | CL4 | PoE 4SFP56 | Swch       | 11.26  |
| 3 6300F | 24G           | CL4 | PoE 4SFP56 | Sw         | 197.60 |
| PoE     | Instantaneous |     |            | Average    |        |
| Port    | Power         |     | (W) Power  | (W)        |        |
-----------------------------------
| 1/1/1 |     | 1.54 |     | 1.54 |     |
| ----- | --- | ---- | --- | ---- | --- |
| 1/1/2 |     | 0.00 |     | 0.00 |     |
...
| 2/1/1 |     | 3.21 |     | 3.21 |     |
| ----- | --- | ---- | --- | ---- | --- |
| 2/1/2 |     | 0.00 |     | 0.00 |     |
ShowingthePOEpowerconsumptionforVSFmember3:
switch# show environment power-consumption power-over-ethernet member 3
| Power Consumption |     |     | Averaging | Period : | 120 seconds |
| ----------------- | --- | --- | --------- | -------- | ----------- |
PoE Average
| Name Description |     |     |     |     | Usage (W) |
| ---------------- | --- | --- | --- | --- | --------- |
--------------------------------------------------
| 3 6300F | 24G           | CL4 | PoE 4SFP56 | Sw      | 197.60 |
| ------- | ------------- | --- | ---------- | ------- | ------ |
| PoE     | Instantaneous |     |            | Average |        |
| Port    | Power         |     | (W) Power  | (W)     |        |
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
| Power Consumption |               |     | Averaging | Period : | 60 seconds |
| ----------------- | ------------- | --- | --------- | -------- | ---------- |
| PoE               | Instantaneous |     |           | Average  |            |
Switchsystemandhardwarecommands|311

| Port | Power | (W) | Power (W) |     |     |
| ---- | ----- | --- | --------- | --- | --- |
-----------------------------------
| 3/1/1 |     | 14.07 | 14.07 |     |     |
| ----- | --- | ----- | ----- | --- | --- |
Showingtherangeofinterfaces:
switch# show environment power-consumption power-over-ethernet interface 3/1/1-
3/1/3,3/1/15
| Power Consumption |       | Averaging | Period    | :   | 60 seconds |
| ----------------- | ----- | --------- | --------- | --- | ---------- |
| PoE Instantaneous |       |           | Average   |     |            |
| Port              | Power | (W)       | Power (W) |     |            |
-----------------------------------
| 3/1/1               |         | 14.07 | 14.07   |                    |     |
| ------------------- | ------- | ----- | ------- | ------------------ | --- |
| 3/1/2               |         | 14.44 | 14.44   |                    |     |
| 3/1/3               |         | 14.09 | 14.09   |                    |     |
| 3/1/15              |         | 14.44 | 14.44   |                    |     |
| Command History     |         |       |         |                    |     |
| Release             |         |       |         | Modification       |     |
| 10.14.1000          |         |       |         | Commandintroduced. |     |
| Command Information |         |       |         |                    |     |
| Platforms           | Command |       | context | Authority          |     |
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|                  | (#)          |     |              | rightsforthiscommand. |     |
| ---------------- | ------------ | --- | ------------ | --------------------- | --- |
| show environment |              |     | power-supply |                       |     |
| show environment | power-supply |     | [vsf]        |                       |     |
Description
Showsstatusinformationaboutallpowersuppliesintheswitch.
| Parameter |     |     |     | Description                                         |     |
| --------- | --- | --- | --- | --------------------------------------------------- | --- |
| vsf       |     |     |     | ShowsoutputfromtheVSFmember-idonswitchesthatsupport |     |
VSF.
Usage
Thefollowinginformationisprovidedforeachpowersupply:
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
Mbr/PSU
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 312

| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
Showsthememberandslotnumberofthepowersupply.
| Product       | Number | Showstheproductnumberofthepowersupply. |     |     |     |
| ------------- | ------ | -------------------------------------- | --- | --- | --- |
| Serial Number |        |                                        |     |     |     |
Showstheserialnumberofthepowersupply,whichuniquelyidentifiesthepower
supply.
| PSU Status |     | Thestatusofthepowersupply.Valuesare: |     |     |     |
| ---------- | --- | ------------------------------------ | --- | --- | --- |
n OK:Powersupplyisoperatingnormally.
n OK*:Powersupplyisoperatingnormally,butitistheonlypowersupplyinthe
chassis.Onepowersupplyisnotsufficienttosupplyfullpowertotheswitch.When
thisvalueisshown,theoutputofthecommandalsoshowsamessageattheendof
thedisplayeddata.
n Absent:Nopowersupplyisinstalledinthespecifiedslot.
n Inputfault:Thepowersupplyhasafaultconditiononitsinput.
n Outputfault:Thepowersupplyhasafaultconditiononitsoutput.
n Warning:Thepowersupplyisnotoperatingnormally.
n WattageMaximum:Showsthemaximumamountofwattagethatthepower
supplycanprovide.
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
Switchsystemandhardwarecommands|313

Showsthetemperatureinformationfromsensorsintheswitchthataffectfancontrol.
Parameter Description
detail Showsdetailedinformationfromeachtemperaturesensor.
vsf ShowsoutputfromtheVSFmember-idonswitchesthatsupport
VSF
Usage
TemperaturesareshowninCelsius.
Validvaluesforstatusarethefollowing:\
Parameter Description
normal
Sensoriswithinnominaltemperaturerange.
max Highesttemperaturefromthissensor.
low_critical
Lowestthresholdtemperatureforthissensor.
critical Highestthresholdtemperatureforthissensor.
fault
Faulteventforthissensor.
emergency OvertemperatureeventforOvertemperatureeventforthis
sensor.
Examples
Showingdetailedtemperatureinformationfora5420or6200switch:
| switch# show | environment | temperature |     |     |
| ------------ | ----------- | ----------- | --- | --- |
| Temperature  | information |             |     |     |
------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     | Module Type | temperature | Status |
| --------------- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-PHY-01-08            |     | line-card-module  | 51.00 C | normal |
| ------------------------ | --- | ----------------- | ------- | ------ |
| 1/1-PHY-09-16            |     | line-card-module  | 48.00 C | normal |
| 1/1-PHY-17-24            |     | line-card-module  | 50.00 C | normal |
| 1/1-PHY-25-32            |     | line-card-module  | 52.00 C | normal |
| 1/1-PHY-33-40            |     | line-card-module  | 53.00 C | normal |
| 1/1-PHY-41-48            |     | line-card-module  | 54.00 C | normal |
| 1/1-Switch-ASIC-Internal |     | line-card-module  | 63.25 C | normal |
| 1/1-CPU                  |     | management-module | 47.56 C | normal |
| 1/1-CPU-Zone-0           |     | management-module | 46.00 C | normal |
| 1/1-CPU-Zone-1           |     | management-module | 46.00 C | normal |
| 1/1-CPU-Zone-2           |     | management-module | 46.00 C | normal |
| 1/1-CPU-Zone-3           |     | management-module | 47.00 C | normal |
| 1/1-CPU-Zone-4           |     | management-module | 47.00 C | normal |
| 1/1-DDR                  |     | management-module | 37.75 C | normal |
| 1/1-DDR-Inlet            |     | management-module | 30.69 C | normal |
| 1/1-Inlet-Air            |     | management-module | 22.00 C | normal |
| 1/1-Switch-ASIC-Remote   |     | management-module | 64.06 C | normal |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 314

| Command        |     | History     |     |         |              |
| -------------- | --- | ----------- | --- | ------- | ------------ |
| Release        |     |             |     |         | Modification |
| 10.07orearlier |     |             |     |         | --           |
| Command        |     | Information |     |         |              |
| Platforms      |     | Command     |     | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
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
-e <EVENT-ID> ShowstheeventlogsforthespecifiedeventID.EventID
range:101through99999.
| -s  | {emergency | | alert |     | | critical | |   |
| --- | ---------- | ------- | --- | ---------- | --- |
Showstheeventlogsforthespecifiedseverity.Selectthe
|     | error | | warning | |   | notice | | severityfromthefollowinglist: |
| --- | ----- | --------- | --- | -------- | ----------------------------- |
info | debug} n emergency:Displayseventlogswithseverityemergency
only.
n alert:Displayseventlogswithseverityalertandabove.
n critical:Displayseventlogswithseveritycriticalandabove.
n error:Displayseventlogswithseverityerrorandabove.
n warning:Displayseventlogswithseveritywarningand
above.
n notice:Displayseventlogswithseveritynoticeandabove.
n info:Displayseventlogswithseverityinfoandabove.
n debug:Displayseventlogswithallseverities.
| -r  |     |     |     |     | Showsthemostrecenteventlogsfirst.                  |
| --- | --- | --- | --- | --- | -------------------------------------------------- |
| -a  |     |     |     |     | Showsalleventlogs,includingthoseeventsfromprevious |
boots.
| -n  | <COUNT> |     |     |     | Displaysthespecifiednumberofeventlogs. |
| --- | ------- | --- | --- | --- | -------------------------------------- |
Switchsystemandhardwarecommands|315

Parameter Description
-i <MEMBER-SLOT> Ona5420or6200:ShowstheeventlogsforthespecifiedVSF
memberID.
| -m {active | | standby} |     |
| ---------- | ---------- | --- |
Ona5420or6200:Showstheeventlogsforthespecifiedrole.
SelectingactivedisplaystheeventlogfortheVSFconductor
roleandstandbydisplayseventlogsfortheVSFstandbyrole.
-c {lldp | ospf | ...} Showstheeventlogsforthespecifiedeventcategory.Enter
showevent-cforafulllistingofsupportedcategorieswith
descriptions.
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 316

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
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889
| Command History     |     |              |     |
| ------------------- | --- | ------------ | --- |
| Release             |     | Modification |     |
| 10.07orearlier      |     | --           |     |
| Command Information |     |              |     |
Switchsystemandhardwarecommands|317

| Platforms |     | Command |     | context |     | Authority |     |     |
| --------- | --- | ------- | --- | ------- | --- | --------- | --- | --- |
Allplatforms Manager(#) AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
| show | front-panel-security |     |     |        |     | status |     |     |
| ---- | -------------------- | --- | --- | ------ | --- | ------ | --- | --- |
| show | front-panel-security |     |     | status |     |        |     |     |
Description
Displaystheconfigurationstatusofthefrontpanelfactoryresetfeatureandthetimestampofthefirst
occurrenceoffactoryresetusingtheresetbutton.
Example
Displaysthestatusofthefrontpanelfactoryresetfeature:
| switch# | show  | front-panel-security |       |     |     | status |           |     |
| ------- | ----- | -------------------- | ----- | --- | --- | ------ | --------- | --- |
| Front   | panel | factory              | reset |     |     |        | : enabled |     |
First occurrence of front-panel factory reset : Wed 2023-09-06 02:57:50 +08
Displaysthestatusofthefrontpanelfactoryresetfeature:
| switch# | show       | front-panel-security |                |     |         | status |           |                 |
| ------- | ---------- | -------------------- | -------------- | --- | ------- | ------ | --------- | --------------- |
| Front   | panel      | factory              | reset          |     |         |        | : enabled | but unsupported |
| First   | occurrence |                      | of front-panel |     | factory | reset  | : NA      |                 |
Ifthestatusofthefeatureisdisplayedasenabled but unsupported,thenusersshouldissuethe
allow-unsafe-updatescommandandreboottheswitch.
| switch#         | config |     |                      |     |     |     |     |     |
| --------------- | ------ | --- | -------------------- | --- | --- | --- | --- | --- |
| switch(config)# |        |     | allow-unsafe-updates |     |     | 30  |     |     |
This command will enable non-failsafe updates of programmable devices for
the next 30 minutes. You will first need to wait for all line and fabric
modules to reach the ready state, and then reboot the switch to begin
applying any needed updates. Ensure that the switch will not lose power,
be rebooted again, or have any modules removed until all updates have
finished and all line and fabric modules have returned to the ready state.
WARNING: Interrupting these updates may make the product unusable!
| Continue   |         | (y/n)?  | y   |           |     |                                            |              |            |
| ---------- | ------- | ------- | --- | --------- | --- | ------------------------------------------ | ------------ | ---------- |
|            | Unsafe  | updates |     | : allowed |     | (less than                                 | 30 minute(s) | remaining) |
| Command    | History |         |     |           |     |                                            |              |            |
| Release    |         |         |     |           |     | Modification                               |              |            |
| 10.14.1000 |         |         |     |           |     | Commandsupportedon4100and6200SwitchSeries. |              |            |
| 10.13.1000 |         |         |     |           |     | Commandintroduced                          |              |            |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 318

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
show hostname
show hostname
Description
Showsthecurrenthostname.
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
show images
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
Example
Showingtheprimaryandsecondaryimagesona6200switch:
| switch(config)# | show | images |     |
| --------------- | ---- | ------ | --- |
---------------------------------------------------------------------------
| AOS-CX Primary | Image |     |     |
| -------------- | ----- | --- | --- |
---------------------------------------------------------------------------
Switchsystemandhardwarecommands|319

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
| Active         | Image       | : primary                |              |
| -------------- | ----------- | ------------------------ | ------------ |
| Service        | OS Version  | : ML.01.05.0001-internal |              |
| BIOS Version   |             | : FL.01.0003             |              |
| Command        | History     |                          |              |
| Release        |             |                          | Modification |
| 10.07orearlier |             |                          | --           |
| Command        | Information |                          |              |
| Platforms      | Command     | context                  | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
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
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 320

IPerrorinfoaboutreceivedpacketsiscollectedfromeachactivelinecardontheswitchandis
preservedduringfailoverevents.Errorcountsareclearedwhentheswitchisrebooted.
Dropreasonsmayincludethefollowing:
| n Malformed | packet |     |     |     |
| ----------- | ------ | --- | --- | --- |
ThepacketdoesnotconformtoTCP/IPprotocolstandardssuchaspacketlengthorinternetheader
length.
Alargenumberofmalformedpacketscanindicatethattherearehardwaremalfunctionssuchas
loosecables,networkcardmalfunctions,orthataDOS(denialofservice)attackisoccurring.
| IP address | error |     |     |     |
| ---------- | ----- | --- | --- | --- |
n
ThepackethasanerrorinthedestinationorsourceIPaddress.ExamplesofIPaddresserrors
includethefollowing:
o ThesourceIPaddressanddestinationIPaddressarethesame.
o ThereisnodestinationIPaddress.
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
Switchsystemandhardwarecommands|321

| switch#     | show ip errors | all-vrfs  |     |     |
| ----------- | -------------- | --------- | --- | --- |
| System-wide | (hardware)     | IP errors |     |     |
--------------------------------------------------
| Drop reason |     |     |     | Packets |
| ----------- | --- | --- | --- | ------- |
--------------------------------------------------
| Malformed  | packets    |           |     | 1   |
| ---------- | ---------- | --------- | --- | --- |
| IP address | errors     |           |     | 10  |
| Per-VRF    | (software) | IP errors |     |     |
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
red
| IPv4 maximum | transmission | unit |     | 3   |
| ------------ | ------------ | ---- | --- | --- |
| IPv4 time    | to live      |      |     | 7   |
| IPv6 maximum | transmission | unit |     | 0   |
| IPv6 hop     | limit        |      |     | 6   |
blue
| IPv4 maximum | transmission | unit |     | 0   |
| ------------ | ------------ | ---- | --- | --- |
| IPv4 time    | to live      |      |     | 1   |
| IPv6 maximum | transmission | unit |     | 0   |
| IPv6 hop     | limit        |      |     | 6   |
...
| Command    | History |     |                                                  |     |
| ---------- | ------- | --- | ------------------------------------------------ | --- |
| Release    |         |     | Modification                                     |     |
| 10.14.1000 |         |     | CommandupdatedtodisplaybothhardwareandsoftwareIP |     |
errorsinthecommandoutput.
| 10.07orearlier |             |         | --        |     |
| -------------- | ----------- | ------- | --------- | --- |
| Command        | Information |         |           |     |
| Platforms      | Command     | context | Authority |     |
5420 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6200 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show module
show module
Description
Showsinformationaboutinstalledlinemodulesandmanagementmodules.
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 322

Although this switch does not have removable modules, this command will still return information about the

switch, referring to management modules and line modules.

Usage

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

Showing all installed modules on a 6200 switch:

switch# show module

Management Modules
==================

Product

Name Number
---- ------- -------------------------------------- ---------- ----------------
1/1

6200F 48G CL4 4SFP+370W Swch

SG0ZKW600P Active (local)

Description

JL727A

Status

Serial
Number

Line Modules
============

Product

Name Number

Description

Serial
Number

Status

Switch system and hardware commands | 323

---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL727A          |         | 6200F | 48G CL4 | 4SFP+370W | Swch         | SG0ZKW600P | Ready |
| ------------------- | ------- | ----- | ------- | --------- | ------------ | ---------- | ----- |
| Command History     |         |       |         |           |              |            |       |
| Release             |         |       |         |           | Modification |            |       |
| 10.07orearlier      |         |       |         |           | --           |            |       |
| Command Information |         |       |         |           |              |            |       |
| Platforms           | Command |       | context |           | Authority    |            |       |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show running-config |     |             |     |       |     |     |     |
| ------------------- | --- | ----------- | --- | ----- | --- | --- | --- |
| show running-config |     | [<FEATURE>] |     | [all] |     |     |     |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<FEATURE> Specifiesthenameofafeature.Foralistoffeaturenames,enter
theshow running-configcommand,followedbyaspace,
followedbyaquestionmark(?).
| all |     |     |     |     | Showsalldefaultvaluesforthecurrentrunningconfiguration. |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- |
Examples
Showingthecurrentrunningconfiguration:
| switch> show           |     | running-config |     |     |     |     |     |
| ---------------------- | --- | -------------- | --- | --- | --- | --- | --- |
| Current configuration: |     |                |     |     |     |     |     |
!
| !Version | AOS-CX | 10.0X.XXXX |     |     |     |     |     |
| -------- | ------ | ---------- | --- | --- | --- | --- | --- |
!
| lldp enable     |     |     |             |     |        |     |     |
| --------------- | --- | --- | ----------- | --- | ------ | --- | --- |
| linecard-module |     | LC1 | part-number |     | JL363A |     |     |
vrf default
!
!
!
!
!
!
| aaa authentication |     |          | login | default | local |     |     |
| ------------------ | --- | -------- | ----- | ------- | ----- | --- | --- |
| aaa authorization  |     | commands |       | default | none  |     |     |
!
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 324

!
!
!
| router ospf  | 1 vrf green |     |
| ------------ | ----------- | --- |
| area 0.0.0.0 |             |     |
| router pim   | vrf green   |     |
enable
| rp-address | 30.0.0.4 |     |
| ---------- | -------- | --- |
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
Switchsystemandhardwarecommands|325

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
!

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

326

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
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
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
Switchsystemandhardwarecommands|327

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
switch(config-external-storage-nasfiles)# show running-config current-context
| external-storage | nasfiles    |     |     |     |
| ---------------- | ----------- | --- | --- | --- |
| address          | 192.168.0.1 |     |     |     |
| vrf default      |             |     |     |     |
| username         | nasuser     |     |     |     |
| password         | ciphertext  |     |     |     |
AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
| type scp  |           |     |     |     |
| --------- | --------- | --- | --- | --- |
| directory | /home/nas |     |     |     |
enable
switch(config-external-storage-nasfiles)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms configorachildof Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
config.SeeUsage.
show startup-config
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 328

| show startup-config | [json] |     |
| ------------------- | ------ | --- |
Description
Showsthecontentsofthestartupconfiguration.
Switchesinthefactory-defaultconfigurationdonothaveastartupconfigurationtodisplay.
| Parameter |     | Description                |
| --------- | --- | -------------------------- |
| json      |     | DisplayoutputinJSONformat. |
Examples
Showingthestartup-configurationinnon-JSONformatfora6200switch:
| switch# | show startup-config |     |
| ------- | ------------------- | --- |
| Startup | configuration:      |     |
!
| !Version          | AOS-CX ML.10.05.0001L |     |
| ----------------- | --------------------- | --- |
| !export-password: | default               |     |
no lldp
| user admin | group administrators | password ciphertext |
| ---------- | -------------------- | ------------------- |
AQBapeGVVYk45m4sYxZDE6ufzB2CWmH2wDncy5Can9iEFZjmYgAAAMl31OWIxExNwi3xahHktOL681amYg
/yg2ezRrlbMUtlU7fVlASiVbmIq8gVUj01Q4STp9/su3pnopopuWPxwk765zqofKyhL0E0Gj9yhoxCeZfy
NeNpNbm6upKjC5LrfZt9
cli-session
| timeout | 0   |     |
| ------- | --- | --- |
!
!
Showingthestartup-configurationinnon-JSONformatfora5420switch:
| switch# | show startup-config |     |
| ------- | ------------------- | --- |
| Startup | configuration:      |     |
!
| !Version          | AOS-CX BL.10.15.0001L |     |
| ----------------- | --------------------- | --- |
| !export-password: | default               |     |
no lldp
| user admin | group administrators | password ciphertext |
| ---------- | -------------------- | ------------------- |
Pxwk76ofKyhm4sYxZDE6ufzBCWmH2wDncyCan9iEFZjmYgAAAMl31OWIxExNwi3xahHktOL681amYg/yg2
ezRrlbMUjmYgAlASiVbmIq8gVUj01Q4STp9/su3pnopopuWPxwk765zqLE0Gj9yhoxCeZfyNeNpNbm6upK
jC5LrfZt9
cli-session
| timeout | 0   |     |
| ------- | --- | --- |
!
!
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
Switchsystemandhardwarecommands|329

},
|     | "none": | {             |        |     |
| --- | ------- | ------------- | ------ | --- |
|     |         | "group_name": | "none" |     |
}
},
...
| Command        | History     |         |         |              |
| -------------- | ----------- | ------- | ------- | ------------ |
| Release        |             |         |         | Modification |
| 10.07orearlier |             |         |         | --           |
| Command        | Information |         |         |              |
| Platforms      |             | Command | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| show        | system     |     |                  |     |
| ----------- | ---------- | --- | ---------------- | --- |
| show system | [serviceos |     | password-prompt] |     |
Description
Showsgeneralstatusinformationaboutthesystem.
| Parameter |                 |     |     | Description |
| --------- | --------------- | --- | --- | ----------- |
| serviceos | password-prompt |     |     |             |
ShowstheServiceOSpasswordpromptstatus.
Usage
CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemDescription,SystemContact,andSystemLocationcanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformation:
| switch#  | show        | system |                 |             |
| -------- | ----------- | ------ | --------------- | ----------- |
| Hostname |             |        | : switch        |             |
| System   | Description |        | : switch        | description |
| System   | Contact     |        | : contact       |             |
| System   | Location    |        | : location      |             |
| Vendor   |             |        | : Aruba         |             |
| Product  | Name        |        | : Xxxxxx        | ...         |
| Chassis  | Serial      | Nbr    | : XXXXXXXXXX    |             |
| Base     | MAC Address |        | : xxxxxx-xxxxxx |             |
| AOS-CX   | Version     |        | : XX.99.99.9999 |             |
| Time     | Zone        |        | : UTC           |             |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 330

| Up Time      |               | : 1 week, | 5 hours, | 28 minutes |     |     |     |
| ------------ | ------------- | --------- | -------- | ---------- | --- | --- | --- |
| CPU Util     | (%)           | : 5       |          |            |     |     |     |
| CPU Util     | (% avg 1 min) | : 11      |          |            |     |     |     |
| CPU Util     | (% avg 5 min) | : 10      |          |            |     |     |     |
| Memory Usage | (%)           | : 35      |          |            |     |     |     |
ShowingtheServiceOSpasswordpromptstatus:
| switch# show     | system   | serviceos | password-prompt |             |              |             |     |
| ---------------- | -------- | --------- | --------------- | ----------- | ------------ | ----------- | --- |
| password-prompt: | disabled |           |                 |             |              |             |     |
| Command History  |          |           |                 |             |              |             |     |
| Release          |          |           | Modification    |             |              |             |     |
| 10.12            |          |           | AddedCPU        | Util (% avg | 1 min)andCPU | Util (% avg | 5   |
min).
| 10.07orearlier      |         |         | --        |     |     |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- | --- | --- |
| Command Information |         |         |           |     |     |     |     |
| Platforms           | Command | context | Authority |     |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show system | resource-utilization |     |     |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | --- | --- | --- |
show system resource-utilization [all | daemon <DAEMON-NAME>] |
| standby | | member | <MEMBER-NUM>] |     |     |     |     |     |
| ------- | -------- | ------------- | --- | --- | --- | --- | --- |
Description
Showsthesystemresourceutilizationdata.
| Parameter |     | Description                                        |     |     |     |     |     |
| --------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| all       |     | Showstheresourceutilizationdatafortheentireswitch. |     |     |     |     |     |
daemon <DAEMON-NAME> Showsonlytheresourceutilizationdatafortheprocessidentifiedby
<DAEMON-NAME>.
standby Showsonlytheresourceutilizationdataforthestandbymanagement
module.
member <MEMBER-NUM> ShowsonlytheresourceutilizationdatafortheVSFmemberidentifiedby
<MEMBER-NUM>.
Usage
Switchsystemandhardwarecommands|331

Foralistofdaemonsthatlogevents,entershow events -d ?fromaswitchpromptinthemanager(#)
context.
Examples
Showingsystemresourceutilizationdata:
| switch# show | system resource-utilization |     |     |     |     |
| ------------ | --------------------------- | --- | --- | --- | --- |
System Resources:
| Processes       |              |           | : 144  |     |     |
| --------------- | ------------ | --------- | ------ | --- | --- |
| CPU usage(%)    |              |           | : 10   |     |     |
| CPU usage(%     | average over | 1 minute) | : 11   |     |     |
| CPU usage(%     | average over | 5 minute) | : 15   |     |     |
| Memory usage(%) |              |           | : 22   |     |     |
| Open FD's       |              |           | : 1358 |     |     |
Storage 1: Endurance utilization = 10-20% (mmc-type-a), 0-10% (mmc-type-b),
| Health            | = normal   |              |            |          |           |
| ----------------- | ---------- | ------------ | ---------- | -------- | --------- |
| Data written      | to various | partitions   | since boot |          |           |
| Nos               | : 5 MB     |              |            |          |           |
| Log               | : 1 MB     |              |            |          |           |
| Coredump          | : 23 MB    |              |            |          |           |
| Security          | : 2 MB     |              |            |          |           |
| Selftest          | : 405 KB   |              |            |          |           |
| Swap              | : 14 MB    |              |            |          |           |
| Storage partition | usage(%)   |              |            |          |           |
| Nos               | : 5        |              |            |          |           |
| Log               | : 60       |              |            |          |           |
| Coredump          | : 23       |              |            |          |           |
| Security          | : 2        |              |            |          |           |
| Selftest          | : 1        |              |            |          |           |
| Swap              | : 0        |              |            |          |           |
| Process           |            | CPU Usage(%) | Memory     | Usage(%) | Open FD's |
--------------------------------------------------------------------------
| hpe-sysmond |     | 1   |     | 2   | 11  |
| ----------- | --- | --- | --- | --- | --- |
| hpe-mgmdd   |     | 0   |     | 1   | 5   |
...
Attemptingtoshowresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
| switch# show    | system resource-utilization |      |                   |          |     |
| --------------- | --------------------------- | ---- | ----------------- | -------- | --- |
| System resource | utilization                 | data | poll is currently | disabled |     |
Showingtheresourceutilizationdataforaparticularprocess:
| switch# show | system resource-utilization |              | daemon | hpe-sysmond |           |
| ------------ | --------------------------- | ------------ | ------ | ----------- | --------- |
| Process      |                             | CPU Usage(%) | Memory | Usage(%)    | Open FD's |
--------------------------------------------------------------------------
| hpe-sysmond |     | 1   |     | 2   | 11  |
| ----------- | --- | --- | --- | --- | --- |
ShowingresourceutilizationdataforallVSFmembers:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 332

aaa
ShowingresourceutilizationdataforaparticularVSFmember:
| switch# show | system | resource-utilization |     |     | member 2 |     |
| ------------ | ------ | -------------------- | --- | --- | -------- | --- |
--------------------------------------------------------------------------
| Resource | utilization | data | for vsf | member | 2   |     |
| -------- | ----------- | ---- | ------- | ------ | --- | --- |
--------------------------------------------------------------------------
System Resources:
| Processes       |         |      |           | : 244  |     |     |
| --------------- | ------- | ---- | --------- | ------ | --- | --- |
| CPU usage(%)    |         |      |           | : 10   |     |     |
| CPU usage(%     | average | over | 1 minute) | : 11   |     |     |
| CPU usage(%     | average | over | 5 minute) | : 15   |     |     |
| Memory usage(%) |         |      |           | : 11   |     |     |
| Open FD's       |         |      |           | : 1854 |     |     |
Storage 1: Endurance utilization = 0-10% (mmc-type-a), 0-10% (mmc-type-b),
| Health            | = normal   |            |          |        |          |           |
| ----------------- | ---------- | ---------- | -------- | ------ | -------- | --------- |
| Data written      | to various | partitions |          | since  | boot     |           |
| Nos               | : 15 MB    |            |          |        |          |           |
| Log               | : 1 MB     |            |          |        |          |           |
| Coredump          | : 23 MB    |            |          |        |          |           |
| Security          | : 2 MB     |            |          |        |          |           |
| Selftest          | : 0 KB     |            |          |        |          |           |
| Swap              | : 0 MB     |            |          |        |          |           |
| Storage partition |            | usage(%)   |          |        |          |           |
| Nos               | : 5        |            |          |        |          |           |
| Log               | : 60       |            |          |        |          |           |
| Coredump          | : 23       |            |          |        |          |           |
| Security          | : 2        |            |          |        |          |           |
| Selftest          | : 1        |            |          |        |          |           |
| Swap              | : 0        |            |          |        |          |           |
| Process           |            | CPU        | Usage(%) | Memory | Usage(%) | Open FD's |
--------------------------------------------------------------------------
| (sd-pam) |     |     | 0   |     | 0   | 7   |
| -------- | --- | --- | --- | --- | --- | --- |
| agetty   |     |     | 0   |     | 0   | 4   |
| ata_sff  |     |     | 0   |     | 0   | 0   |
...
| switch# show | system | resource-utilization |     |     | all |     |
| ------------ | ------ | -------------------- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| Resource | utilization | data | for vsf | member | 1   |     |
| -------- | ----------- | ---- | ------- | ------ | --- | --- |
--------------------------------------------------------------------------
System Resources:
| Processes       |         |      |           | : 244  |     |     |
| --------------- | ------- | ---- | --------- | ------ | --- | --- |
| CPU usage(%)    |         |      |           | : 10   |     |     |
| CPU usage(%     | average | over | 1 minute) | : 11   |     |     |
| CPU usage(%     | average | over | 5 minute) | : 15   |     |     |
| Memory usage(%) |         |      |           | : 11   |     |     |
| Open FD's       |         |      |           | : 1854 |     |     |
Storage 1: Endurance utilization = 0-10% (mmc-type-a), 0-10% (mmc-type-b),
| Health | = normal |     |     |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- |
Switchsystemandhardwarecommands|333

| Data written      | to various | partitions |          | since | boot            |     |           |
| ----------------- | ---------- | ---------- | -------- | ----- | --------------- | --- | --------- |
| Nos               | : 15 MB    |            |          |       |                 |     |           |
| Log               | : 1 MB     |            |          |       |                 |     |           |
| Coredump          | : 23 MB    |            |          |       |                 |     |           |
| Security          | : 2 MB     |            |          |       |                 |     |           |
| Selftest          | : 405 KB   |            |          |       |                 |     |           |
| Swap              | : 14 MB    |            |          |       |                 |     |           |
| Storage partition |            | usage(%)   |          |       |                 |     |           |
| Nos               | : 5        |            |          |       |                 |     |           |
| Log               | : 60       |            |          |       |                 |     |           |
| Coredump          | : 23       |            |          |       |                 |     |           |
| Security          | : 2        |            |          |       |                 |     |           |
| Selftest          | : 1        |            |          |       |                 |     |           |
| Swap              | : 0        |            |          |       |                 |     |           |
| Process           |            | CPU        | Usage(%) |       | Memory Usage(%) |     | Open FD's |
--------------------------------------------------------------------------
| (sd-pam) |     | 0   |     |     | 0   |     | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
aaa
| utilspamcfg |     | 0   |     |     | 1   | 10  |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| Resource | utilization | data | for vsf | member | 2   |     |     |
| -------- | ----------- | ---- | ------- | ------ | --- | --- | --- |
--------------------------------------------------------------------------
System Resources:
| Processes       |         |      |           | :   | 244  |     |     |
| --------------- | ------- | ---- | --------- | --- | ---- | --- | --- |
| CPU usage(%)    |         |      |           | :   | 10   |     |     |
| CPU usage(%     | average | over | 1 minute) | :   | 11   |     |     |
| CPU usage(%     | average | over | 5 minute) | :   | 15   |     |     |
| Memory usage(%) |         |      |           | :   | 11   |     |     |
| Open FD's       |         |      |           | :   | 1854 |     |     |
Storage 1: Endurance utilization = 0-10% (mmc-type-a), 0-10% (mmc-type-b),
| Health            | = normal   |            |          |       |                 |     |           |
| ----------------- | ---------- | ---------- | -------- | ----- | --------------- | --- | --------- |
| Data written      | to various | partitions |          | since | boot            |     |           |
| Nos               | : 15 MB    |            |          |       |                 |     |           |
| Log               | : 1 MB     |            |          |       |                 |     |           |
| Coredump          | : 23 MB    |            |          |       |                 |     |           |
| Security          | : 2 MB     |            |          |       |                 |     |           |
| Selftest          | : 0 KB     |            |          |       |                 |     |           |
| Swap              | : 0 MB     |            |          |       |                 |     |           |
| Storage partition |            | usage(%)   |          |       |                 |     |           |
| Nos               | : 5        |            |          |       |                 |     |           |
| Log               | : 60       |            |          |       |                 |     |           |
| Coredump          | : 23       |            |          |       |                 |     |           |
| Security          | : 2        |            |          |       |                 |     |           |
| Selftest          | : 1        |            |          |       |                 |     |           |
| Swap              | : 0        |            |          |       |                 |     |           |
| Process           |            | CPU        | Usage(%) |       | Memory Usage(%) |     | Open FD's |
--------------------------------------------------------------------------
| (sd-pam)        |     |     | 0   |     | 0   |     | 7   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
| agetty          |     |     | 0   |     | 0   |     | 4   |
| ata_sff         |     |     | 0   |     | 0   |     | 0   |
| Command History |     |     |     |     |     |     |     |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 334

| Release |     |     | Modification                                    |
| ------- | --- | --- | ----------------------------------------------- |
| 10.12   |     |     | TheoutputofthiscommandincludesCPUusage(%average |
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
| Parameter |     |     | Description                             |
| --------- | --- | --- | --------------------------------------- |
| basic     |     |     | Specifiesshowingabasicsetofinformation. |
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
| switch# | show tech basic |     |     |
| ------- | --------------- | --- | --- |
=============================================================
Switchsystemandhardwarecommands|335

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
show usb
show usb
Description
ShowstheUSBportconfigurationandmountsettings.
Examples
IfUSBhasnotbeenenabled:
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 336

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
Usage
Addingaleading"/"asthefirstcharacterofthe<PATH>parameterisoptional.
Attemptingtoenter'..'asanypartofthe<PATH>willgenerateaninvalidpathargumenterror.Only
fully-qualifiedpathnamesaresupported.
Examples
Showingthetopleveldirectorytree:
Switchsystemandhardwarecommands|337

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
| switch#        | show usb file-system |         | dir1/../..   |     |
| -------------- | -------------------- | ------- | ------------ | --- |
| Invalid        | path argument        |         |              |     |
| Command        | History              |         |              |     |
| Release        |                      |         | Modification |     |
| 10.07orearlier |                      |         | --           |     |
| Command        | Information          |         |              |     |
| Platforms      | Command              | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show version
show version
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 338

Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
Example
Showingversioninformationfora6200switch:
| switch(config)# | show | version |     |     |     |
| --------------- | ---- | ------- | --- | --- | --- |
-----------------------------------------------------------------------------
AOS-CX
(c) Copyright 2017-2022 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version | : ML.xx.xx.xxxx                                     |                 |     |     |     |
| ------- | --------------------------------------------------- | --------------- | --- | --- | --- |
| Build   | Date : 2022-05-27                                   | 17:00:46        | PDT |     |     |
| Build   | ID : AOS-CX:ML.xx.xx.xxxx:85c3c2f3d59e:201910222335 |                 |     |     |     |
| Build   | SHA : 85c3c2f3d59ec8318ba97178fad387aecb671b33      |                 |     |     |     |
| Active  | Image : secondary                                   |                 |     |     |     |
| Service | OS Version                                          | : ML.01.05.0001 |     |     |     |
| BIOS    | Version                                             | : ML.01.0001    |     |     |     |
Showingversioninformationfora5420switch:
| switch(config)# | show | version |     |     |     |
| --------------- | ---- | ------- | --- | --- | --- |
-----------------------------------------------------------------------------
AOS-CX
| (c) Copyright | 2024 | Hewlett Packard | Enterprise | Development | LP  |
| ------------- | ---- | --------------- | ---------- | ----------- | --- |
-----------------------------------------------------------------------------
| Version        | : BL.xx.xx.xxxx                                     |                 |              |     |     |
| -------------- | --------------------------------------------------- | --------------- | ------------ | --- | --- |
| Build          | Date : 2024-11-11                                   | 17:00:46        | PDT          |     |     |
| Build          | ID : AOS-CX:BL.xx.xx.xxxx:85c3c2f3d59e:201910222335 |                 |              |     |     |
| Build          | SHA : 97178fd59ec8318ba97178fad387aecb671b33        |                 |              |     |     |
| Active         | Image : secondary                                   |                 |              |     |     |
| Service        | OS Version                                          | : BL.0X.XX.XXXX |              |     |     |
| BIOS           | Version                                             | : BL.XX.XXXXX   |              |     |     |
| Command        | History                                             |                 |              |     |     |
| Release        |                                                     |                 | Modification |     |     |
| 10.07orearlier |                                                     |                 | --           |     |     |
| Command        | Information                                         |                 |              |     |     |
| Platforms      | Command                                             | context         | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| system                      | resource-utilization |               | poll-interval |     |     |
| --------------------------- | -------------------- | ------------- | ------------- | --- | --- |
| system resource-utilization |                      | poll-interval | <SECONDS>     |     |     |
Switchsystemandhardwarecommands|339

Description
ConfiguresthepollingintervalforsystemresourceinformationcollectionandrecordingsuchasCPU
andmemoryusage.
| Parameter |     |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
<SECONDS> Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Example
Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |             | system | resource-utilization |     |              |     | poll-interval |     | 20  |     |
| --------------- | ----------- | ------ | -------------------- | --- | ------------ | --- | ------------- | --- | --- | --- |
| Command         | History     |        |                      |     |              |     |               |     |     |     |
| Release         |             |        |                      |     | Modification |     |               |     |     |     |
| 10.07orearlier  |             |        |                      |     | --           |     |               |     |     |     |
| Command         | Information |        |                      |     |              |     |               |     |     |     |
| Platforms       | Command     |        | context              |     | Authority    |     |               |     |     |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
| Command | History |     |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 340

| Release        |             |     |         |     | Modification |     |     |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- |
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
Switchsystemandhardwarecommands|341

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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
mount
EnablestheinsertedUSBdrive.
| unmount |     |     | DisablestheinsertedUSBdriveinpreparationforremoval. |
| ------- | --- | --- | --------------------------------------------------- |
Usage
IfUSBhasbeenenabledintheconfiguration,theUSBportontheactivemanagementmoduleis
availableformountingaUSBdrive.TheUSBportonthestandbymanagementmoduleisnotavailable.
AninsertedUSBdrivemustbemountedeachtimetheswitchbootsorfailsovertoadifferent
managementmodule.
AUSBdrivemustbeunmountedbeforeremoval.
ThesupportedUSBfilesystemsareFAT16andFAT32.
Examples
AOS-CX10.15.xxxxFundamentalsGuide|(5420,6200SwitchSeries) 342

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
Switchsystemandhardwarecommands|343

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

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

344

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
SupportandOtherResources|345

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.15.xxxx Fundamentals Guide | (5420, 6200 Switch Series)

346