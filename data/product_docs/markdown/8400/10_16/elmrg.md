AOS-CX 10.16.xxxx Event Log
Message Reference Guide

All Switch Series

Published: October 2025

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

Notices

The information contained herein is subject to change without notice. The only warranties for Hewlett Packard
Enterprise products and services are set forth in the express warranty statements accompanying such products
and services. Nothing herein should be construed as constituting an additional warranty. Hewlett Packard
Enterprise shall not be liable for technical or editorial errors or omissions contained herein.
Confidential computer software. Valid license from Hewlett Packard Enterprise required for possession, use, or
copying. Consistent with FAR 12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the U.S. Government under vendor's
standard commercial license.

| 2

Links to third-party websites take you outside the Hewlett Packard Enterprise website. Hewlett Packard Enterprise
has no control over and is not responsible for information outside the Hewlett Packard Enterprise website.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

3

Contents
| About                               | this       | document   |        |            |        |        |              | 12  |
| ----------------------------------- | ---------- | ---------- | ------ | ---------- | ------ | ------ | ------------ | --- |
| Applicableproducts                  |            |            |        |            |        |        |              | 12  |
| Latestversionavailableonline        |            |            |        |            |        |        |              | 13  |
| Commandsyntaxnotationconventions    |            |            |        |            |        |        |              | 13  |
| Abouttheexamples                    |            |            |        |            |        |        |              | 13  |
| Identifyingswitchportsandinterfaces |            |            |        |            |        |        |              | 14  |
| Identifyingmodularswitchcomponents  |            |            |        |            |        |        |              | 15  |
| EventLogMessageFormat               |            |            |        |            |        |        |              | 16  |
| AAA events                          |            |            |        |            |        |        |              | 18  |
| Accounting                          |            | events     |        |            |        |        |              | 20  |
| ACLs                                | events     |            |        |            |        |        |              | 21  |
| Alarm                               | events     |            |        |            |        |        |              | 22  |
| ARC events                          |            |            |        |            |        |        |              | 24  |
| ARP security                        |            | events     |        |            |        |        |              | 27  |
| ASIC table                          |            | full       | error  | for        | L3PD   | events |              | 28  |
| BFD events                          |            |            |        |            |        |        |              | 31  |
| BGP events                          |            |            |        |            |        |        |              | 36  |
| Bidirectional                       |            | PIM        |        | (PIM-BIDI) |        | events |              | 41  |
| Bluetooth                           |            | Management |        |            | events |        |              | 43  |
| CDP events                          |            |            |        |            |        |        |              | 45  |
| Central                             | Source     |            | events |            |        |        |              | 47  |
| Client                              | insight    |            | events |            |        |        |              | 49  |
| Certificate                         |            | management |        |            | events |        |              | 52  |
| Config                              | Management |            |        | events     |        |        |              | 57  |
| Config                              | validator  |            | events |            |        |        |              | 59  |
| Connectivity                        |            | Fault      |        | Management |        |        | (CFM) events | 60  |
| Console                             | events     |            |        |            |        |        |              | 61  |
5
AOS-CX10.16.xxxxEventLogMessageReferenceGuide| (AllSwitchSeries)

| Container   |                | manager     |            | events   |        |        | 63  |
| ----------- | -------------- | ----------- | ---------- | -------- | ------ | ------ | --- |
| CoPP        | events         |             |            |          |        |        | 66  |
| CPU_RX      | events         |             |            |          |        |        | 69  |
| Credential  |                | Manager     |            | events   |        |        | 70  |
| CX LMS      | events         |             |            |          |        |        | 72  |
| Device      | fingerprinting |             |            | events   |        |        | 74  |
| DHCP        | Relay          | events      |            |          |        |        | 75  |
| DHCP        | server         | events      |            |          |        |        | 76  |
| DHCPv4      |                | snooping    | events     |          |        |        | 79  |
| DHCPv6      |                | Relay       | events     |          |        |        | 84  |
| DHCPv6      |                | snooping    | events     |          |        |        | 85  |
| Discovery   |                | and         | Capability | Exchange | (DCBx) | events | 90  |
| Distributed |                | services    |            | events   |        |        | 92  |
| DNS         | client         | events      |            |          |        |        | 93  |
| Dot1x       | supplicant     |             | events     |          |        |        | 94  |
| Download    |                | events      |            |          |        |        | 95  |
| DPSE        | daemon         | events      |            |          |        |        | 98  |
| ECMP        | events         |             |            |          |        |        | 100 |
| ERPS        | events         |             |            |          |        |        | 102 |
| EVPN        | events         |             |            |          |        |        | 106 |
| External    |                | Storage     | events     |          |        |        | 113 |
| Fan events  |                |             |            |          |        |        | 115 |
| Fault       | monitor        |             | events     |          |        |        | 120 |
| Feature     |                | Pack events |            |          |        |        | 122 |
| FIB events  |                |             |            |          |        |        | 125 |
| Firmware    |                | Update      | events     |          |        |        | 127 |
|6

| Forwarding    |             | and           | Queuing   |               | for Time-Sensitive |        | Streams | (FQTSS) |     |
| ------------- | ----------- | ------------- | --------- | ------------- | ------------------ | ------ | ------- | ------- | --- |
| events        |             |               |           |               |                    |        |         |         | 130 |
| Hardware      |             | Health        |           | Monitor       | events             |        |         |         | 132 |
| Hardware      |             | switch        |           | controller    | sync               | events |         |         | 138 |
| Hot Patch     |             | events        |           |               |                    |        |         |         | 141 |
| HTTPS         | Server      | events        |           |               |                    |        |         |         | 147 |
| Inband        | Flow        | Analyzer      |           |               | (IFA) events       |        |         |         | 148 |
| Injected      | Views       |               |           |               |                    |        |         |         | 153 |
| In-System     |             | Programming   |           |               | events             |        |         |         | 154 |
| Interface     |             | and           | Interface |               | Diagnostic         | events |         |         | 157 |
| Internal      | storage     |               | events    |               |                    |        |         |         | 160 |
| IP Flow       | Information |               |           | Export        | events             |        |         |         | 161 |
| IP Flow       | Monitoring  |               |           | Advertisement |                    | events |         |         | 162 |
| IP source     |             | lockdown      |           | events        |                    |        |         |         | 164 |
| IP tunnels    |             | events        |           |               |                    |        |         |         | 166 |
| IP-SLA        | events      |               |           |               |                    |        |         |         | 170 |
| IPSec         | tunnel      | offload       |           | events        |                    |        |         |         | 172 |
| IPv6          | Router      | Advertisement |           |               | events             |        |         |         | 173 |
| IRDP          | events      |               |           |               |                    |        |         |         | 178 |
| ISSU          | events      |               |           |               |                    |        |         |         | 179 |
| Job scheduler |             |               | events    |               |                    |        |         |         | 182 |
| L3 Encap      |             | capacity      |           | events        |                    |        |         |         | 183 |
| L3 Resource   |             | Manager       |           |               | events             |        |         |         | 184 |
| LACP          | events      |               |           |               |                    |        |         |         | 186 |
| LAG events    |             |               |           |               |                    |        |         |         | 192 |
| Launch        | Daemon      |               | (LaunchD) |               | events             |        |         |         | 195 |
| Layer         | 3 Interface |               |           | events        |                    |        |         |         | 196 |
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries) 7

| LED events     |          |            |         |               |        |        |        | 203 |
| -------------- | -------- | ---------- | ------- | ------------- | ------ | ------ | ------ | --- |
| LLDP           | events   |            |         |               |        |        |        | 204 |
| Loop           | Protect  | events     |         |               |        |        |        | 207 |
| Loopback       |          | events     |         |               |        |        |        | 210 |
| MAC            | address  | management |         |               | events |        |        | 211 |
| MAC            | Address  | mode       |         | configuration |        | events |        | 214 |
| MAC            | Learning |            | events  |               |        |        |        | 216 |
| MACsec         | events   |            |         |               |        |        |        | 218 |
| Management     |          | events     |         |               |        |        |        | 221 |
| MDNS           | events   |            |         |               |        |        |        | 224 |
| MGMD           | events   |            |         |               |        |        |        | 225 |
| Mirroring      |          | events     |         |               |        |        |        | 231 |
| Mirror-on-drop |          |            | events  |               |        |        |        | 232 |
| Module         | events   |            |         |               |        |        |        | 233 |
| MPLS           | events   |            |         |               |        |        |        | 242 |
| MSDP           | events   |            |         |               |        |        |        | 243 |
| Message        | Session  |            | Relay   | Protocol      |        | events |        | 245 |
| Multicast      |          | HelperD    | events  |               |        |        |        | 248 |
| Multicast      |          | Traffic    | Manager |               | events |        |        | 251 |
| Message        | Session  |            | Relay   | Protocol      |        | (MSRP) | events | 252 |
| MVRP           | events   |            |         |               |        |        |        | 256 |
| NAE            | Agents   | events     |         |               |        |        |        | 258 |
| NAE            | events   |            |         |               |        |        |        | 259 |
| NAE            | script   | generation |         | events        |        |        |        | 262 |
| NAE            | Scripts  | events     |         |               |        |        |        | 263 |
| ND snooping    |          | events     |         |               |        |        |        | 266 |
| NDM            | events   |            |         |               |        |        |        | 268 |
|8

| NTP         | events     |                   |          |        |               |        | 275 |
| ----------- | ---------- | ----------------- | -------- | ------ | ------------- | ------ | --- |
| OSPFv2      | events     |                   |          |        |               |        | 277 |
| OSPFv3      | events     |                   |          |        |               |        | 280 |
| Packet      | capture    |                   | events   |        |               |        | 281 |
| Password    |            | Reset             | events   |        |               |        | 285 |
| PIM         | events     |                   |          |        |               |        | 286 |
| Policies    | events     |                   |          |        |               |        | 293 |
| Port        | access     | events            |          |        |               |        | 294 |
| Port        | access     | application-based |          |        | policy events |        | 302 |
| Port        | access     | group             | based    | policy | events        |        | 303 |
| Port        | access     | roles             | events   |        |               |        | 305 |
| Port        | events     |                   |          |        |               |        | 306 |
| Port        | security   | events            |          |        |               |        | 308 |
| Port        | Statistics | events            |          |        |               |        | 309 |
| Power       | events     |                   |          |        |               |        | 310 |
| Power       | over       | Ethernet          | events   |        |               |        | 316 |
| PTP events  |            |                   |          |        |               |        | 325 |
| Proxy       | ARP        | events            |          |        |               |        | 331 |
| QoS         | ASIC       | Provider          | events   |        |               |        | 332 |
| Quality     | of         | Service           | events   |        |               |        | 334 |
| Queue       | Monitoring |                   | events   |        |               |        | 334 |
| Rapid       | per        | VLAN              | Spanning | Tree   | Protocol      | events | 336 |
| RBAC        | events     |                   |          |        |               |        | 340 |
| Redundant   |            | Management        |          | events |               |        | 341 |
| Replication |            | Manager           | events   |        |               |        | 343 |
| REST        | events     |                   |          |        |               |        | 344 |
| Self Test   |            | events            |          |        |               |        | 358 |
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries) 9

| Self Test      |            | Monitor |           | events    |              | 359 |
| -------------- | ---------- | ------- | --------- | --------- | ------------ | --- |
| sFlow          | events     |         |           |           |              | 360 |
| SFTP           | Client     | events  |           |           |              | 367 |
| Smartlink      |            | events  |           |           |              | 368 |
| SNMP           | events     |         |           |           |              | 369 |
| SSH client     |            | events  |           |           |              | 372 |
| SSH server     |            | events  |           |           |              | 373 |
| Supportability |            |         | events    |           |              | 378 |
| SynchE         | events     |         |           |           |              | 384 |
| SYS events     |            |         |           |           |              | 389 |
| SYSMON         |            | events  |           |           |              | 392 |
| TCAM           | events     |         |           |           |              | 394 |
| TCAM           | events     |         |           |           |              | 397 |
| Telnet         | server     |         | events    |           |              | 401 |
| Temperature    |            |         | events    |           |              | 403 |
| Time           | management |         |           | events    |              | 406 |
| TPM            | events     |         |           |           |              | 407 |
| Traffic        | Insight    |         | events    |           |              | 408 |
| Transceiver    |            |         | events    |           |              | 410 |
| UDLD           | events     |         |           |           |              | 414 |
| UDP            | Broadcast  |         | Forwarder |           | events       | 416 |
| UFD            | events     |         |           |           |              | 417 |
| User           | management |         |           | events    |              | 418 |
| User-based     |            | tunnels |           | events    |              | 420 |
| Virtual        | Switching  |         |           | Extension | (VSX) events | 428 |
| Virtual        | Switching  |         |           | Framework | (VSF) events | 436 |
| VLAN           | events     |         |           |           |              | 448 |
|10

| VLAN                               | Interface | events       |           | 454 |
| ---------------------------------- | --------- | ------------ | --------- | --- |
| VRF events                         |           |              |           | 455 |
| VRF Manager                        |           | events       |           | 456 |
| VRRP                               | events    |              |           | 457 |
| VSX Sync                           | events    |              |           | 464 |
| VXLAN                              | agent     | events       |           | 465 |
| VXLAN                              | events    |              |           | 466 |
| Zero                               | touch     | provisioning | events    | 471 |
| Support                            | and       | Other        | Resources | 477 |
| AccessingHPEArubaNetworkingSupport |           |              |           | 477 |
| AccessingUpdates                   |           |              |           | 478 |
| Warrantyinformation                |           |              |           | 478 |
| RegulatoryInformation              |           |              |           | 478 |
| Documentationfeedback              |           |              |           | 478 |
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries) 11

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

n HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A,

S4R20A, S4R21A, S4R22A, S4R23A, S4R24A, S4R25A, S4R26A, S4R27A, S4R28, S4R29A)

n HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A, S0U61A,
S0U62A, S0U66A, S0U68A)

n HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A,
R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B,
JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,
S0M89A,  S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

n HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A,

JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A, S3L75A,
S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A, S4P47A, S4P48A)

n HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,
R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

n HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

n HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

n HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

n HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C,
JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

n HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

n HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

n HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

n HPE Aruba Networking 10040 Switch Series (S4R58A, S4R59A)

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

12

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
n <example-text>
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ------------------------------------------------------------ | --- |
example-text
n
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
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
| …or |     | Ellipsis:                                                |     |
... n Incodeandscreenexamples,averticalorhorizontalellipsisindicatesan
omissionofinformation.
|     |     | n Insyntaxusingbracketsandbraces,anellipsisindicatesitemsthatcanbe |     |
| --- | --- | ------------------------------------------------------------------ | --- |
repeated.Whenanitemfollowedbyellipsesisenclosedinbrackets,zero
ormoreitemscanbespecified.
| About | the examples |     |     |
| ----- | ------------ | --- | --- |
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchor
environment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understanding | the | CLI prompts |     |
| ------------- | --- | ----------- | --- |
Aboutthisdocument|13

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
format: member/slot/port.

On the HPE Aruba Networking 4100i Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

14

On the HPE Aruba Networking 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the HPE Aruba Networking 8xxx, 93xx, and 10xxx Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on

member 1.

On the HPE Aruba Networking 8400 Switch Series

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

About this document | 15

n Fansareontherearoftheswitchandarelabeledinsoftwareas:member/tray/fan:
o member:1.
o tray:1to4.
o fan:1to4.
n Fabricmodulesarenotlabeledontheswitchbutarelabeledinsoftwareintheformat:
member/module:
o member:1.
o
member:1or2.
n Thedisplaymoduleontherearoftheswitchisnotlabeledwithamemberorslotnumber.
| Event Log | Message | Format |
| --------- | ------- | ------ |
Theeventlogmessagesgeneratedbyaswitchincludeitsorigin,severity,ID,modulerole,andmoduleID.The
followingtableliststheeventlogmessagefieldsanditsdescriptions.
Table1:EventLogMessageFields
| Field         |     | Description                                      |
| ------------- | --- | ------------------------------------------------ |
| Messageorigin |     | Theoriginmessageoftheevent.                      |
| EventID       |     | TheuniqueeventIDofthelogmessage.                 |
| Severity      |     | Theseverityofthelogmessage.                      |
| ModuleRole    |     | Themodulerolefromwhichthelogmessagewasgenerated. |
| ModuleID      |     | ThemoduleID fromwhichthelogmessagewasgenerated.  |
| Message       |     | Theeventlogmessage.                              |
Theseverityofanyeventlogmessageindicatesthenatureoftheeventandtheactiontheuserisrequiredto
perform.Thefollowingtableliststhesupportedseveritiesanditsindications.
Table2:EventLogSeverities
| Severity | Description                      |     |
| -------- | -------------------------------- | --- |
| DEBUG    | Debugmessages                    |     |
| INFO     | Informationalmessages            |     |
| NOTICE   | Anissuewithasignificantcondition |     |
| WARN     | Warningcondition                 |     |
| ERR      | Anerrorinthesystem               |     |
| CRI      | Criticalcondition                |     |
| ALERT    | Immediateactionneeded            |     |
| EMERG    | Systemisunusable                 |     |
Listedbelowarethemodulerolesanditsdescriptionsgeneratedbytheeventlogmessages:
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries) 16

n AMM — Active Management Module

n SMM — Standby Management Module

n UMM — Unassigned Management Module

n LC —Line card

For event logs generated during an early boot or when the module role is not determined by the chassis switch, the
module role will be set to UMM. After the module role is determined, the event logs are updated with AMM or
SMM.
Listed below are the module roles and its descriptions generated by the event log messages for a VSF stack:

n CDTR—Conductor

n STBY—Standby

n MMBR—Member

n UKWN—Unknown

For event logs generated during VSF discovery or when the VSF role is not determined by the VSF stack , the module
role will be set to UKWN. After the VSF role is determined, the event logs are updated either with CDTR, STBY, or
MMBR.

About this document | 17

Chapter 2

AAA events

AAA events

The following are the events related to AAA.

Event ID: 2301

Message

Category

Severity

AAA <aaa_config_type> update: <aaa_config_event>

AAA

Info

Description

Logs AAA Authentication/Authorization/Accounting/fail-through

Event ID: 2302

Message

Category

Severity

TACACS <tacacs_type> <tacacs_action>: <tacacs_event>

AAA

Info

Description

Logs TACACS+ server update, server group update and global default update

Event ID: 2303

Message

Category

Severity

RADIUS <radius_type> <radius_action>: <radius_event>

AAA

Info

Description

Logs RADIUS server update, server group update and global default update

Event ID: 2304

Message

Category

Severity

RADIUS Server with Address:<server_address>, Authport:<server_authport>, VRF_ID:<server_
vrfid> is "<status>"

AAA

Info

Description

Logs changes in RADIUS server reachability status

Event ID: 2305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

18

Message

Category

Severity

TACACS server host <server_address> port <server_port> vrf <server_vrf> <status>

AAA

Info

Description

Logs changes in TACACS server reachability status

Event ID: 2306

Message

Category

Severity

RADIUS Server route with Address:<server_address>, VRF_ID:<server_vrfid> is "<status>"

AAA

Info

Description

Logs changes in RADIUS server route reachability status

Event ID: 2307

Message

Category

Severity

Decrypted TACACS passkey length {key_length} exceeded the maximum allowed
plaintext key length {max_key_length}

AAA

Error

Description

Decrypted TACACS server key length exceeded the maximum length allowed

AAA events | 19

Chapter 3

Accounting events

Accounting events

The following are the events related to accounting.

Event ID: 13101

Message

SSH session from {ip_address} for user {user_name} closed due to inactivity.'

Category

Accounting

Severity

Info

Description

Logs a message when a SSH session timed out due to the session being idle

Event ID: 13102

Message

TELNET session from <ip_address> with User <user_name> timed out due to idle timeout.

Category

Accounting

Severity

Info

Description

Logs a message when a TELNET session timed out due to the session being idle

Event ID: 13103

Message

CONSOLE session from <ip_address> with User <user_name> timed out due to idle
timeout.

Category

Accounting

Severity

Info

Description

Logs a message when a CONSOLE session timed out due to the session being idle

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

20

Chapter 4

ACLs events

ACLs events

The following are the events related to ACLs.

Event ID: 10001

Message

Category

Severity

<log>

ACLs

Info

Description

ACL log

Event ID: 10002

Message

Category

Severity

ACL {acl_name} ({acl_type}) {interface_name} ({direction}): {hit_delta} {ace_string}

ACLs

Info

Description

ACL log statistics

Event ID: 10003

Message

Category

Severity

ACL <acl_type> <acl_name> failed to apply on <application>

ACLs

Error

Description

ACL application failure

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

21

Chapter 5

Alarm events

Alarm events

The following are the events related to alarm.

Event ID: 11701

Message

Input alarm <id> config change: name: <name>, relay: <relay>, log_and_trap: <log_and_
trap>, trigger: <trigger>

Category

Alarm

Severity

Information

Description

Event reported when there is a change in input alarm configuration.

Event ID: 11702

Message

System alarm (<type>) config change: relay: <relay>, log_and_trap: <log_and_trap>

Category

Alarm

Severity

Information

Description

Event reported when there is a change in system alarm configuration.

Event ID: 11703

Message

System alarm <name> has activated through log-and-trap': yes

Category

Alarm

Severity

Information

Description

Event reported when system alarm has activated

Event ID: 11704

Message

Input alarm <name> has activated through log-and-trap, triggered at <trigger>': yes

Category

Alarm

Severity

Information

Description

Event reported when input alarm has activated

Event ID: 11705

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

22

Message

Snooze alarm activated, disabling relay function for <length> min': yes

Category

Alarm

Severity

Information

Description

Event reported when alarm snooze timer has activated

Event ID: 11706

Message

Snooze alarm has expired': yes

Category

Alarm

Severity

Information

Description

Event reported when alarm snooze timer has expired

Event ID: 11707

Message

Alarm relay function is re-enabled': yes

Category

Alarm

Severity

Information

Description

Event reported when alarm relay function is re-enabled

Event ID: 11708

Message

Snooze alarm repeats, disabling relay function for <length> min': yes

Category

Alarm

Severity

Information

Description

Event reported when alarm snooze timer repeats

Event ID: 11709

Message

System alarm <name> has activated through relay

Category

Alarm

Severity

Information

Description

Event reported when system alarm has activated through relay

Event ID: 11710

Message

Input alarm <name> has activated through relay, triggered at <trigger>

Alarm events | 23

Category

Alarm

Severity

Information

Description

Event reported when input alarm has activated through relay

ARC events
The following are the events related to Application Recognition and Control (ARC).

Event ID: 14101

Message

Category

Severity

<log>App Recognition feature has been {status} - event_name: ARCD_LC_STATUS_CHANGE

ARC

Info

Description

Log event that indicates global configuration for App Recognition feature

Event ID: 14102

Message

Category

Severity

Linecard {node_id} is {status} - event_name: ARCD_BULK_SYN_RECEIVE

ARC

Info

Description

linecard up event

Event ID: 14103

Message

Category

Severity

BULK SYNC event received from linecard {node_id} - event_name: ARCD_BULK_SYN_ALL_
SENT

ARC

Info

Description

Bulk sync event received

Event ID: 14104

Message

Category

Severity

BULK SYNC ALL request sent to all LC - event_name: ARCD_PUBLISHER_STATUS_CHANGE

ARC

Info

Description

bulk sync all event sent!

Event ID: 14105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

24

Message

Category

Severity

ARCD Publisher is {status} - event_name: ARCD_FLUSH_TIMER

ARC

Info

Description

ARCD Publisher status

Event ID: 14106

Message

Category

Severity

FLUSH timer on LC {node_id} is {status}. - event_name: ARCD_OVERFLOW_HIGH_
THRESHOLD

ARC

Info

Description

flush timer start/expire status!

Event ID: 14107

Message

Category

Severity

IP Flow table utilization has exceeded high threshold on linecard {node_id} - event_name:
ARCD_OVERFLOW_LOW_THRESHOLD

ARC

Info

Description

IP Flow table utilization reached high threshold on a LC

Event ID: 14108

Message

Category

Severity

IP Flow table utilization back to lower threshold on linecard {node_id} - event_name:
ARCD_GLOBAL_STATUS_CHANGE

ARC

Info

Description

IP Flow table utilization back to lower threshold on a LC

Event ID: 14109

Message

Category

Severity

App Recognition feature has been {status} - event_name: ARCD_FEATURE_PACK_HONOR_
MODE

ARC

Info

Description

Log event that indicates global configuration for App Recognition feature

Event ID: 14110

ARC events | 25

Message

Category

Severity

App Recognition is operating without a valid feature pack is_security_log : yes

ARC

Warning

Description

Log event that indicates App Recognition feature is operating without a valid feature pack

Event ID: 14111

Message

Category

Severity

Description

App Recognition is blocked due to invalid or missing feature pack is_security_log : yes

ARC

Warning

Log event that indicates App Recognition feature is not blocked due to invalid or missing
feature pack

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

26

Chapter 6

ARP security events

ARP security events

The following are the events related to ARP security.

Event ID: 10401

Message

ARP inspection <status> on vlan <vlan_id>.

Category

ARP security

Severity

Information

Description

ARP inspection configuration on VLAN

Event ID: 10402

Message

ARP inspection <status> on port <port_name>.

Category

ARP security

Severity

Information

Description

ARP inspection port mode configuration

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

27

Chapter 7
|            |            |          | ASIC table | full error | for L3PD | events |
| ---------- | ---------- | -------- | ---------- | ---------- | -------- | ------ |
| ASIC table | full error | for L3PD | events     |            |          |        |
ThefollowingaretheeventsrelatedtoASICtablefullerrorforL3PD.
| Event ID: | 10801 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Neighboraddfailureduetoneighborhardwarefull.'throttle_count:1
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- |
| Severity |     | Error                     |     |     |     |     |
Description HardwaretableforNEIGHBORentriesarefull,nonewneighborswillbeadded.
| Event ID: | 10802 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Routeaddfailureduetoroutehardwarefull'throttle_count:1
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- |
| Severity |     | Error                     |     |     |     |     |
Description HardwaretableforROUTEentriesarefull,nonewroutewillbeadded.
| Event ID: | 10803 |                                         |     |     |     |     |
| --------- | ----- | --------------------------------------- | --- | --- | --- | --- |
| Message   |       | SelfIPaddfailureduetoselfiphardwarefull |     |     |     |     |
| Category  |       | ASICtablefullerrorforL3PD               |     |     |     |     |
| Severity  |       | Error                                   |     |     |     |     |
Description HardwaretableforSELFIPentriesarefull,nonewselfipwillbeadded.
| Event ID:   | 10804 |                                                 |     |     |     |     |
| ----------- | ----- | ----------------------------------------------- | --- | --- | --- | --- |
| Message     |       | RouterMAClimitexceeded.FailedtoprogramMAC:{mac} |     |     |     |     |
| Category    |       | ASICtablefullerrorforL3PD                       |     |     |     |     |
| Severity    |       | Info                                            |     |     |     |     |
| Description |       | RouterMAClimitexceeded,MACcannotbeprogrammed    |     |     |     |     |
| Event ID:   | 10805 |                                                 |     |     |     |     |
28
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

Error parsing LIST_ROUTE_IPV4_PREFIX in customer_override.yaml file

ASIC table full error for L3PD

Warning

Description

Error parsing LIST_ROUTE_IPV4_PREFIX in customer_override.yaml file

Event ID: 10806

Message

Category

Severity

Error parsing LIST_ROUTE_IPV6_PREFIX in customer_override.yaml file

ASIC table full error for L3PD

Warning

Description

Error parsing LIST_ROUTE_IPV6_PREFIX in customer_override.yaml file

Event ID: 10807

Message

Category

Severity

Using configured IPv4 prefix-priority list <prefix_list>.

ASIC table full error for L3PD

Info

Description

Log configured ip prefix-priority list.

Event ID: 10808

Message

Category

Severity

Using configured IPv6 prefix-priority list <prefix_list>.

ASIC table full error for L3PD

Info

Description

Log configured ipv6 prefix-priority list.

Event ID: 10809

Message

Category

Severity

HW programming failed for IPv4 prefix-priority <route_prefix>

ASIC table full error for L3PD

Error

Description

Logs failure while configuring hardware for ipv4 prefix-priority.

Event ID: 10810

Message

HW programming failed for IPv6 prefix-priority <route_prefix>

ASIC table full error for L3PD events | 29

Category

ASIC table full error for L3PD

Severity

Error

Description

Logs failure while configuring hardware for ipv6 prefix-priority.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

30

Chapter 8

BFD events

BFD events

The following are the events related to BFD.

Event ID: 7301

Message

Category

Severity

BFD was enabled

BFD

Info

Description

Event raised when BFD is enabled globally

Event ID: 7302

Message

Category

Severity

BFD was disabled

BFD

Info

Description

Event raised when BFD is disabled globally

Event ID: 7303

Message

Category

Severity

BFD echo was enabled

BFD

Info

Description

Event raised when BFD echo is enabled globally

Event ID: 7304

Message

Category

Severity

BFD echo was disabled

BFD

Info

Description

Event raised when BFD is disabled globally

Event ID: 7305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

31

Message

Category

Severity

BFD echo was enabled on interface <intf>

BFD

Info

Description

Event raised when BFD echo is enabled on an interface

Event ID: 7306

Message

Category

Severity

BFD echo was disabled on interface <intf>

BFD

Info

Description

Event raised when BFD is disabled on an interface

Event ID: 7307

Message

Category

Severity

BFD session is up. session_id=<session_id>, vrf=<vrf>, op_mode=<op_mode>, src_
port=<src_port>, dest_ip=<dest_ip>, local_state=<local_state>, local_diag=<local_diag>,
remote_state=<remote_state>, remote_diag=<remote_diag>

BFD

Info

Description

Event raised when a BFD session state becomes up

Event ID: 7308

Message

Category

Severity

BFD session is down. session_id=<session_id>, vrf=<vrf>, op_mode=<op_mode>, src_
port=<src_port>, dest_ip=<dest_ip>, local_state=<local_state>, local_diag=<local_diag>,
remote_state=<remote_state>, remote_diag=<remote_diag>

BFD

Info

Description

Event raised when a BFD session state becomes down

Event ID: 7309

Message

Category

Severity

BFD session is administratively down. session_id=<session_id>, vrf=<vrf>, op_mode=<op_
mode>, src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_state>, local_diag=<local_
diag>, remote_state=<remote_state>, remote_diag=<remote_diag>

BFD

Info

Description

Event raised when a BFD session is administratively down

BFD events | 32

Event ID: 7310

Message

Category

Severity

BFD session was created without a source port

BFD

Info

Description

Event raised when a BFD session is created without a source port

Event ID: 7311

Message

Category

Severity

Port <name> can forward BFD traffic

BFD

Info

Description

Event raised when a port used by BFD session can forward traffic

Event ID: 7312

Message

Category

Severity

Port <name> can not forward BFD traffic

BFD

Info

Description

Event raised when a port used by BFD session can not forward traffic

Event ID: 7313

Message

Category

Severity

BFD sessions maximum active capacity reached

BFD

Info

Description

Event raised when the maximum number of active BFD sessions is reached

Event ID: 7314

Message

The echo function for the BFD session <session_id> will not become active until a global
echo source IP address is configured

Category

BFD

Severity

Warning

Description

Event raised when an Echo session is created without a valid echo_source IP address
configured

Event ID: 7315

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

33

Message

Category

Severity

BFD session is unidirectional. session_id=<session_id>, vrf=<vrf>, op_mode=<op_mode>,
src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_state>, local_diag=<local_diag>,
remote_state=<remote_state>, remote_diag=<remote_diag>

BFD

Error

Description

Event raised when a BFD session state becomes unidirectional

Event ID: 7316

Message

BFD echo cannot be enabled on tunnels. interface=<intf>

Category

BFD

Severity

Warning

Description

Event raised when BFD echo is enabled on a Tunnel interface

Event ID: 7317

Message

BFD echo is not supported on IPv6 sessions

Category

BFD

Severity

Warning

Description

Event raised when BFD echo is enabled for a session using IPv6

Event ID: 7318

Message

IP Version mismatch for BFD. session_id=<session_id>, vrf=<vrf>, op_mode=<op_mode>,
src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_state>, local_diag=<local_diag>,
remote_state=<remote_state>, remote_diag=<remote_diag>, from=<from>, ip_version=<ip_
version>, Invalid IP address: <addr>

Category

Severity

BFD

Error

Description

"Event raised when SRC or DST IP Version doesn't match the session's IP Version"

Event ID: 7319

Message

BFD single-hop is not supported on interface <intf>

Category

BFD

Severity

Warning

Description

"Event raised when a BFD single-hop session source port is a loopback"

Event ID: 7320

BFD events | 34

Message

BFD session interval override not supported for protocol <from>

Category

BFD

Severity

Warning

Description

"Event raised when a BFD session specifies an interval for a protocol that does not
support override"

Event ID: 7321

Message

BFD session <direction> interval override of <requested_interval> ms is out of bounds for
protocol <from>, using <applied_interval> ms instead

Category

BFD

Severity

Warning

Description

"Event raised when a BFD session specifies an interval outside the specified bounds"

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

35

Chapter 9

BGP events

BGP events

The following are the events related to BGP.

Event ID: 2901

Message

Category

Severity

<remote-addr>: Peer up. vrf-name: <vrf-name>

BGP

Info

Description

Logs the changes in BGP connection state.

Event ID: 2902

Message

Category

Severity

<remote-addr>: Peer down. error-code: <error-code>, error-sub-code: <error-subcode>. vrf-
name: <vrf-name>

BGP

Info

Description

Logs the failure in BGP connection state changes.

Event ID: 2903

Message

Category

Severity

<remote-addr>: Peer has received prefix equal to Maximum Prefix value configured. vrf-
name: <vrf-name>

BGP

Info

Description

Trap when the number of received prefix reaches the maximum prefix value.

Event ID: 2904

Message

Category

Severity

<remote-addr>: Peer has received prefix equal to Threshold value configured. vrf-name:
<vrf-name>

BGP

Info

Description

Trap when the number of received prefix reached the threshold value.

Event ID: 2905

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

36

Message

Category

Severity

BGP AS <as_number> configured. vrf-name: <vrf-name>

BGP

Info

Description

Logs BGP enable event.

Event ID: 2906

Message

Category

Severity

BGP AS <as_number> unconfigured. vrf-name: <vrf-name>

BGP

Info

Description

Logs BGP disable event.

Event ID: 2907

Message

Category

Severity

BGP router-id changed: {ip} vrf-name: {vrf-name}

BGP

Info

Description

Logs BGP router-id changed.

Event ID: 2908

Message

Category

Severity

<remote_addr>: Peer configured, AS <remote_as>. vrf-name: <vrf-name>

BGP

Info

Description

Logs creation of BGP peer.

Event ID: 2909

Message

Category

Severity

<remote_addr>: User reset request. vrf-name: <vrf-name>

BGP

Info

Description

Logs BGP peer session reset event.

Event ID: 2910

Message

<remote_addr>: Peer password changed. vrf-name: <vrf-name>

BGP events | 37

Category

Severity

BGP

Info

Description

Logs BGP peer password change event.

Event ID: 2911

Message

Category

Severity

<remote_addr>: Peer deleted. vrf-name: <vrf-name>

BGP

Info

Description

Logs deletion of BGP peer.

Event ID: 2912

Message

Category

Severity

<remote_addr>: Peer admin disabled. vrf-name: <vrf-name>

BGP

Info

Description

Logs BGP peer admin disable event

Event ID: 2913

Message

Category

Severity

<remote_addr>: Peer admin enabled. vrf-name: <vrf-name>

BGP

Info

Description

Logs BGP peer admin enable event.

Event ID: 2914

Message

Category

Severity

<remote_addr>: Peer remote-as changed to <remote_as>. vrf-name: <vrf-name>

BGP

Info

Description

Logs BGP peer remote-as change event.

Event ID: 2915

Message

<remote_addr>: Peer local-as changed to <local_as>. vrf-name: <vrf-name>

Category

BGP

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

38

Severity

Info

Description

BGP peer local-as change event.

Event ID: 2916

Message

Category

Severity

<remote_addr>: Peer source-address changed to <src_ipaddr>. vrf-name: <vrf-name>

BGP

Info

Description

Logs peer source address change event.

Event ID: 2917

Message

Category

Severity

<remote_addr>: Peer remove-private-as configuration changed. vrf-name: <vrf-name>

BGP

Info

Description

Logs configuration of peer remove-private-as.

Event ID: 2918

Message

Category

Severity

<bgp_id>: BGP identifier sent by Peer <remote_addr> matches ours. BGP session may not
established. vrf-name: <vrf-name>

BGP

Info

Description

Logs peer identifier has been matched with local identifier.

Event ID: 2919

Message

Category

Severity

The BGP RIB has reached the threshold limit of <threshold_limit> for VRF <vrf-name>': yes

BGP

Critical

Description

Trap when the rib size reaches the threshold value.

Event ID: 2920

Message

<pg_name>: Peer-group configured with remote-as <remote_as>. vrf-name: <vrf-name>

Category

BGP

BGP events | 39

Severity

Info

Description

Logs BGP peer-group remote-as configuration event.

Event ID: 2921

Message

Category

Severity

<remote_addr>: Peer ignore-leading-as configuration changed. vrf-name: <vrf-name>

BGP

Info

Description

Logs configuration of peer ignore-leading-as.

Event ID: 2922

Message

Category

Severity

{remote_addr}: Neighbor added to Peer group {peer-grp} vrf-name: {vrf-name}

BGP

Info

Description

Logs neighbor addition to peer group.

Event ID: 2923

Message

Category

Severity

{remote_addr}: Neighbor deleted from Peer group {peer-grp} vrf-name: {vrf-name}

BGP

Info

Description

Logs neighbor deletion from peer grou

Event ID: 2924

Message

Category

Severity

Logs if dynamic tunnel bridging mode ibgp-ebgp was enabled and broadcast group is
being configured in a route-map.

BGP

Error

Description

Dynamic tunnel bridging ibgp-ebgp mode is enabled, Please disable it.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

40

Chapter 10
|               |                | Bidirectional | PIM (PIM-BIDI) | events |
| ------------- | -------------- | ------------- | -------------- | ------ |
| Bidirectional | PIM (PIM-BIDI) | events        |                |        |
bi-directional
ThefollowingaretheeventsrelatedtobidirectionalPIM.
| Event ID: 15301 |                                                   |     |     |     |
| --------------- | ------------------------------------------------- | --- | --- | --- |
| Message         | Routerpim{status}onvrf{vrf_name}                  |     |     |     |
| Category        | BidirectionalPIM                                  |     |     |     |
| Severity        | Information                                       |     |     |     |
| Description     | ThislogeventinformsaboutrouterPIMstatusofaVRF.    |     |     |     |
| Event ID: 15302 |                                                   |     |     |     |
| Message         | Interface{if_name}state{state}                    |     |     |     |
| Category        | BidirectionalPIM                                  |     |     |     |
| Severity        | Information                                       |     |     |     |
| Description     | Thislogeventinformsaboutinterfacestatus           |     |     |     |
| Event ID: 15303 |                                                   |     |     |     |
| Message         | DroppingPacketoninterface{if_index},Dueto{reason} |     |     |     |
| Category        | BidirectionalPIM                                  |     |     |     |
| Severity        | Error                                             |     |     |     |
| Description     | Thislogeventinformsaboutdroppingpacket            |     |     |     |
| Event ID: 15304 |                                                   |     |     |     |
| Message         | PIMBidi{state}onInterface{if_name}                |     |     |     |
| Category        | BidirectionalPIM                                  |     |     |     |
| Severity        | Information                                       |     |     |     |
| Description     | ThislogeventinformsaboutPIMBidistateoninterface   |     |     |     |
| Event ID: 15305 |                                                   |     |     |     |
41
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

PIM Bidi Neighbor {ip_address} is {state} on Interface {if_name}

Bidirectional PIM

Information

Description

This log event informs about the creation and deletion of a PIM Bidi Neighbor

Event ID: 15306

Message

PIM Bidi formed Neighborship with Non PIM Bidi Neighbor {ip_address} on Interface {if_
name}

Category

Bidirectional PIM

Severity

Error

Description

This log event informs about Non Bidir PIM Neighbor.

Event ID: 15307

Message

PIM Bidi Resource utilization of {capacity_name} has reached 90 percent of the
supported limits on the system.

Category

Bidirectional PIM

Severity

Info

Description

This log event informs the user that Bidir PIM resource utilization has reached 90 percent
of the supported limits.

Event ID: 15308

Message

PIM Bidi Resource utilization of {capacity_name} has dropped below 90 percent of the
supported limits on the system.

Category

Bidirectional PIM

Severity

Info

Description

This log event informs the user that Bidir PIM resource utilization drops below 90 percent
of the supported limits.

Event ID: 15309

Message

PIM Bidi Resource utilization of {capacity_name} has reached maximum of the supported
limits on the system.

Category

Bidirectional PIM

Severity

Info

Description

This log event informs the user that Bidir PIM resource utilization has exceeded the
supported limits

Bidirectional PIM (PIM-BIDI) events | 42

Chapter 11
|           |            |        | Bluetooth | Management | events |
| --------- | ---------- | ------ | --------- | ---------- | ------ |
| Bluetooth | Management | events |           |            |        |
ThefollowingaretheeventsrelatedtoBluetoothmanagement.
| Event ID: | 8001 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Bluetoothhasbeen<enabled_disabled>
Category BluetoothManagement
Severity Info
Description EventraisedwhenBluetoothisenabledordisabled
| Event ID: | 8002 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Bluetoothunabletotrustpairingdevice
Category BluetoothManagement
Severity Warning
Description EventraisedwhenBluetoothisunabletotrustpairingdevice
| Event ID: | 8003 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Bluetoothadapter<inserted_removed>
Category BluetoothManagement
Severity Info
Description EventraisedwhenbtdreceivessignalforBluetoothadapterevent
| Event ID: | 8004 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Bluetoothdevice<connected_disconnected>:<mac_address>
Category BluetoothManagement
Severity Info
Description EventraisedwhenbtdreceivessignalforBluetoothdeviceevent
| Event ID: | 8005 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
43
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Bluetooth device rejected because another device is already connected

Category

Bluetooth Management

Severity

Warning

Description

Event raised when btd disconnects a newly paried device because another device is
already connected

Bluetooth Management events | 44

Chapter 12

CDP events

CDP events

The following are the events related to CDP.

Event ID: 8901

Message

CDP Enabled

Category

CDP

Severity

Information

Description

Logs CDP enabled

Event ID: 8902

Message

CDP Disabled

Category

CDP

Severity

Information

Description

Logs CDP disbled

Event ID: 8903

Message

CDP neighbor <mac> is added on <interface>

Category

CDP

Severity

Information

Description

Log to indicate CDP neighbor addition

Event ID: 8904

Message

CDP neighbor <mac> is updated on <interface>' throttle_count: 100

Category

CDP

Severity

Information

Description

Log to indicate CDP neighbour modification

Event ID: 8905

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

45

Message

CDP neighbor <mac> is deleted on <interface>

Category

CDP

Severity

Information

Description

Log to indicate CDP neighbor deletion

Event ID: 8906

Message

All CDP neighbor info cleared

Category

CDP

Severity

Information

Description

Log to indicate all CDP neighbor info is cleared

CDP events | 46

Chapter 13

Central Source events

Central Source events

The following are the events related to an HPE Aruba Networking Central source.

Event ID: 14601

Message

Category

Severity

Activate server {activate_address} is reachable via VRF {vrf}.

CENTRALSOURCE

Info

Description

Activate server is reachable via an active VRF.

Event ID: 14602

Message

Received certificate from Activate server, processing with certificate manager. Certificate
length: {cert_length}.

Category

CENTRALSOURCE

Severity

Info

Description

Activate server sent a CA certificate to be installed.

Event ID: 14603

Message

HPE Aruba Networking Central location {central_location} successfully fetched from
{central_source} via VRF {vrf}

Category

CENTRALSOURCE

Severity

Info

Description

HPE Aruba Networking Central location successfully fetched from Central Source
(CLI/DHCP/Activate Server) via VRF.

Event ID: 14604

Message

Unable to fetch HPE Aruba Networking Central location from Central Source
(CLI/DHCP/Activate Server).

Category

CENTRALSOURCE

Severity

Info

Description

Unable to fetch HPE Aruba Networking Central location {central_location} from {central_
source} via VRF {vrf}.

Event ID: 14605

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

47

Message

Category

Severity

Switch time is synced with Activate Server.

CENTRALSOURCE

Info

Description

Switch time is synced with Activate Server {activate_address}.

Event ID: 14606

Message

Category

Severity

Switch time is synced with NTP Servers.

CENTRALSOURCE

Info

Description

Switch time is synced with NTP Servers.

Central Source events | 48

Chapter 14

Client insight events

Client insight events

The following are the events related to client insight.

Event ID: 14301

Message

Client {mac} successfully on-boarded on VLAN {vlans}. Client on-boarding started at {ob_
start_ts}; L2 complete at {l2_end_ts}; L3 complete at {l3_end_ts} is_security_log : no

Category

Client Insight

Severity

Info

Description

Client on-boarding successful

Event ID: 14302

Message

Client {mac} partial success while on-boarding on VLAN {vlans}. L2 status:{l2_ob_state} L3
status:{l3_ob_state}. Client on-boarding started at {ob_start_ts};L2 complete at {l2_end_
ts}; L3 complete at {l3_end_ts}. is_security_log : no

Category

Client Insight

Severity

Info

Description

Client on-boarding partially success

Event ID: 14303

Message

Client {mac} failed to on-board with status: {onboarding_status} reason_code: {failure_
phase_id} is_security_log : no

Category

Client Insight

Severity

Info

Description

Client on-boarding failed

Event ID: 14304

Message

Maximum system wide client limit {client-number} reached. throttle_time : 15 throttle_
count : 1 is_security_log: no

Category

Client Insight

Severity

Info

Description

Maximum system wide client limit reached

Event ID: 14305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

49

Message

Client {mac} successfully on-boarded on VLAN {vlans}; Client on-boarding started at {ob_
start_ts}; L2 complete at {l2_end_ts}; L3 complete at {l3_end_ts}; ARP to GW response
received at {arp_end_ts}; DNS on-boarding to {dns_server_ip} completed at {dns_end_ts}
is_security_log : no

Category

Client Insight

Severity

Info

Description

Client on-boarding successful

Event ID: 14306

Message

Client {mac} on-boarded on VLANs {vlans} and failed on VLANs {failed_vlans}; Client on-
boarding started at {ob_start_ts}; L2 complete at {l2_end_ts}; L3 complete at {l3_end_ts};
ARP to GW response received at {arp_end_ts}; DNS on-boarding to {dns_server_ip}
completed at {dns_end_ts}; L2 status {l2_ob_state} failure_reason_code - {l2_failure_
reason}; L3 status {l3_ob_state} failure_reason_code - {l3_failure_reason}; DNS on-
boarding status {dns_status} failure_reason_code - {dns_failure_reason}

Category

Client Insight

Severity

Info

Description

Client on-boarding partially success

Event ID: 14307

Message

Client {mac} failed to on-board with status: {onboarding_status} in failure phase: {failure_
phase_id} with reason: {failure_reason} is_security_log : no

Category

Client Insight

Severity

Info

Description

Client on-boarding failed

Event ID: 14308

Message

Client {mac} on-boarded on VLAN {vlans} and failed on VLANs {failed_vlans} Port {port}
auth-status {auth-status} auth-type {auth-type} auth-latency {auth-latency} dot1x-auth-
failure-reason {dot1x-auth-failure-reason} mac-auth-failure-reason {mac-auth-failure-
reason} radius-server {radius-server} assigned-role {assigned-role} assigned-role-type
{assigned-role-type}

Category

Client Insight

Severity

Info

Description

Client L2 on-boarding details

Event ID: 14309

Message

Client {mac} on-boarded on VLAN {successfulvlan} Port {port} dhcpv4-status {dhcpv4-
status} dhcpv4-failure-reason {dhcpv4-failure-reason} dhcpv4-server{dhcpv4-server}

Client insight events | 50

dhcpv4-client {dhcpv4-client} dhcpv4-latency {dhcpv4-latency}

Category

Client Insight

Severity

Info

Description

Client DHCPV4 on-boarding details

Event ID: 14310

Message

Client {mac} on-boarded on VLAN {successfulvlan} Port {port} dhcpv6-status {dhcpv6-
status} dhcpv6-failure-reason {dhcpv6-failure-reason} dhcpv6-server{dhcpv6-server}
dhcpv6-client {dhcpv6-client} dhcpv6-latency {dhcpv6-latency}

Category

Client Insight

Severity

Info

Description

Client DHCPV6 on-boarding details

Event ID: 14311

Message

Client {mac} on-boarded on Port {port} dns-status {dns-status} dns-failure-reason {dns-
failure-reason} dns-server {dns-server} dns-latency {dns-latency}

Category

Client Insight

Severity

Info

Description

Client DNS on-boarding details

Event ID: 14312

Message

Client {mac} on-boarded on VLAN {vlan} Port {port} arp-gw-status {arp-status} arp-gw-
failure-reason {arp-failure-reason} gateway {arp-gw} arp-gw-latency {arp-latency}

Category

Client Insight

Severity

Info

Description

Client DNS on-boarding details

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

51

Chapter 15
|             |            |        | Certificate | management | events |
| ----------- | ---------- | ------ | ----------- | ---------- | ------ |
| Certificate | management | events |             |            |        |
Thefollowingaretheeventsrelatedtocertificatemanagement.
| Event ID: | 7701 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
TAProfile<name>created
| Category    | Certificatemanagement                     |     |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- | --- |
| Severity    | Info                                      |     |     |     |     |
| Description | Eventraisedwhenataprofileiscreated        |     |     |     |     |
| Event ID:   | 7702                                      |     |     |     |     |
| Message     | TAProfile<name>deleted                    |     |     |     |     |
| Category    | Certificatemanagement                     |     |     |     |     |
| Severity    | Info                                      |     |     |     |     |
| Description | Eventraisedwhenataprofileisremoved        |     |     |     |     |
| Event ID:   | 7703                                      |     |     |     |     |
| Message     | Leafcertificate<name>imported             |     |     |     |     |
| Category    | Certificatemanagement                     |     |     |     |     |
| Severity    | Info                                      |     |     |     |     |
| Description | Eventraisedwhenaleafcertificateisimported |     |     |     |     |
| Event ID:   | 7704                                      |     |     |     |     |
Message
Leafcertificate<name>deleted
| Category    | Certificatemanagement                    |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Info                                     |     |     |     |     |
| Description | Eventraisedwhenaleafcertificateisdeleted |     |     |     |     |
| Event ID:   | 7705                                     |     |     |     |     |
52
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Certificate <name> will expire within <days> days

Category

Certificate management

Severity

Warning

Description

Event raised when an installed certifiate will expire within 60 days

Event ID: 7706

Message

Certificate <name> has not yet reached its start date

Category

Certificate management

Severity

Warning

Description

Event raised when an installed certifiate is not yet past its start date

Event ID: 7707

Message

Certificate <name> has expired and can no longer be used

Category

Certificate management

Severity

Warning

Description

Event raised when an installed certifiate has expired

Event ID: 7708

Message

Certificate <name> verified and accepted' throttle_count: 100

Category

Certificate management

Severity

Info

Description

Event raised when a certificate chain is verified

Event ID: 7709

Message

Certificate <name> rejected due to verification failure (<error>)' throttle_count: 100

Category

Certificate management

Severity

Warning

Description

Event raised when a certificate chain is rejected

Event ID: 7710

Message

Certificate signing request <name> created

Certificate management events | 53

Category

Certificate management

Severity

Info

Description

Event raised when a certificate signing request is created on the switch

Event ID: 7711

Message

Self-signed certificate <name> created

Category

Certificate management

Severity

Info

Description

Event raised when a self-signed certificate is created on the switch

Event ID: 7712

Message

Application association with the <name> certificate is not permitted

Category

Certificate management

Severity

Error

Description

Event raised when an invalid certificate association is made

Event ID: 7713

Message

Certificate <name> failed OCSP verification (<status>), but was accepted because OCSP
enforcement is set to optional.' throttle_count: 100

Category

Certificate management

Severity

Warning

Description

Event raised when a certificate is verified due to optional OCSP enforcement

Event ID: 7714

Message

CA certificates successfully downloaded from EST server <name>

Category

Certificate management

Severity

Info

Description

Event raised when CA certificates were successfully downloaded from an EST server

Event ID: 7715

Message

Failed to download CA certificates from EST server <name>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

54

Category

Certificate management

Severity

Error

Description

Event raised when CA certificates could not be downloaded from an EST server

Event ID: 7716

Message

Certificate <name> successfully enrolled by EST server <est_name>

Category

Certificate management

Severity

Info

Description

Event raised when a certificate is successfully enrolled with EST

Event ID: 7717

Message

Failed to enroll certificate <name> with EST server <est_name>

Category

Certificate management

Severity

Error

Description

Event raised when certificate enrollment with an EST server fails

Event ID: 7718

Message

Certificate <name> successfully reenrolled by EST server <est_name>

Category

Certificate management

Severity

Info

Description

Event raised when a certificate is successfully reenrolled with EST

Event ID: 7719

Message

Failed to reenroll certificate <name> with EST server <est_name>

Category

Certificate management

Severity

Error

Description

Event raised when certificate reenrollment with an EST server fails

Event ID: 7720

Message

Certificate <name> is not set for signing purpose

Category

Certificate management

Certificate management events | 55

Severity

Warning

Description

Event raised when a signer certifiate is not set for signing

Event ID: 7721

Message

Certificate <name> is invalid or malformed

Category

Certificate management

Severity

Warning

Description

Event raised when an installed certifiate is invalid or malformed

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

56

Chapter 16

Config Management events

Config Management events

The following are the events related to config management.

Event ID: 6801

Message

Copying configs from: <from> to: <to>

Category

Config Management

Severity

Information

Description

Logs a message when configs copying from one format to another

Event ID: 6802

Message

Error while copying configs. Error: <error>

Category

Config Management

Severity

Error

Description

Logs a message when copying config has some error

Event ID: 6803

Message

<type>:<value>

Category

Config Management

Severity

Information

Description

Logs a message when config validation prunes tables/columns in startup-config or when
errors are encountered

Event ID: 6804

Message

Error while copying configs. Error: <error>

Category

Config Management

Severity

Error

Description

Logs a message when copying config to shadowdb has some error

Event ID: 6805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

57

Message

Information while copying configs. Info: <info>

Category

Config Management

Severity

Information

Description

Logs a message when copying config has some information

Config Management events | 58

Chapter 17

Config validator events

Config validator events

The following are the events related to configuration validation.

Event ID: 13401

Message

Category

Severity

Config {name} failed to validate. Reason {reason}

Config Validator

Error

Description

Failed to validate configuration

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

59

Chapter 18
|              | Connectivity     | Fault Management | (CFM) events |
| ------------ | ---------------- | ---------------- | ------------ |
| Connectivity | Fault Management | (CFM) events     |              |
ThefollowingaretheeventsrelatedtoConnectivityFaultManagement(CFM).
| Event ID: 11601 |     |     |     |
| --------------- | --- | --- | --- |
Message
ConnectionlostforMaintenanceEndpoint<id>on<interface>.
| Category | ConnectivityFaultManagement(CFM) |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Error                            |     |     |
Description EventreportedwhenconnectionislostontheMaintanenceEndpoint.
| Event ID: 11602 |     |     |     |
| --------------- | --- | --- | --- |
Message ConnectionrestoredforMaintenanceEndpoint<id>on<interface>.
| Category | ConnectivityFaultManagement(CFM) |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description EventreportedwhenconnectionisrestoredontheMaintanenceEndpoint.
60
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 19

Console events

Console events

The following are the events related to console.

Event ID: 13001

Message

User <user_name> logged in from <ip_address> through CONSOLE session.

Category

Console

Severity

Info

Description

Logs a message when a user login is successful

Event ID: 13002

Message

User <user_name> login from <ip_address> for CONSOLE session has failed.

Category

Console

Severity

Error

Description

Logs a message when a user login fails

Event ID: 13003

Message

User <user_name> logged out of CONSOLE session from <ip_address>.

Category

Console

Severity

Info

Description

Logs a message when a user logs out of a session

Event ID: 13004

Message

Category

Severity

Description

Event ID: 13005

CONSOLE session from User <user_name> is closed because maximum number of
sessions per user is reached.

Console

Warning

Logs a message when a user tries to login while maximum number of sessions per user
are reached.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

61

Message

Category

Severity

Description

User {user_name} login from {ip_address} for CONSOLE session has failed since the user
is trying to login through an interface which is not allowed. Allowed interfaces are:
{mgmt_intf}

Console

Warning

Logs a message when a user login fails since the access through this management
interface is not allowed

Console events | 62

Chapter 20
|           |         |        | Container | manager | events |
| --------- | ------- | ------ | --------- | ------- | ------ |
| Container | manager | events |           |         |        |
Thefollowingaretheeventsrelatedtocontainermanager.
| Event ID:   | 11801 |                                         |     |     |     |
| ----------- | ----- | --------------------------------------- | --- | --- | --- |
| Message     |       | Container<name>created                  |     |     |     |
| Category    |       | Containermanager                        |     |     |     |
| Severity    |       | Info                                    |     |     |     |
| Description |       | Eventreportedwhencontaineriscreated     |     |     |     |
| Event ID:   | 11802 |                                         |     |     |     |
| Message     |       | Container<name>removed                  |     |     |     |
| Category    |       | Containermanager                        |     |     |     |
| Severity    |       | Info                                    |     |     |     |
| Description |       | Eventreportedwhencontainerisremoved     |     |     |     |
| Event ID:   | 11803 |                                         |     |     |     |
| Message     |       | Container<name>isstarted.               |     |     |     |
| Category    |       | Containermanager                        |     |     |     |
| Severity    |       | Info                                    |     |     |     |
| Description |       | Eventreportedwhencontainerisoperational |     |     |     |
| Event ID:   | 11804 |                                         |     |     |     |
Message Endpointhasbeenexecutedforcontainer{name}withparameters:{params}
| Category |     | Containermanager |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Info             |     |     |     |
Description Eventreportedwhencontainerexeccommandhasbeenrunwithadditionalparameters.
| Event ID: | 11805 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
63
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

Endpoint has been executed for container {name} with no parameters.

Container manager

Info

Description

Event reported when container exec command has been run with no parameters.

Event ID: 11806

Message

Category

Severity

Container {name} stopped

Container manager

Info

Description

Event reported when container is stopped.

Event ID: 11807

Message

Category

Severity

Container {name} image signature verified and accepted

Container manager

Info

Description

Event reported when container image signature is verified and accepted.

Event ID: 11808

Message

Category

Severity

Container {name} image failed signature verification

Container manager

Info

Description

EEvent reported when container image failed signature verification.

Event ID: 11809

Message

Category

Severity

Description

Event ID: 11810

Container {name} image is unsigned and not allowed in enhanced secure mode

Container manager

Error

Event reported when container image is unsigned and not allowed in enhanced secure
mode.

Message

Container {name} image is unsigned and allowed by the user configuration

Container manager events | 64

Category

Container manager

Severity

Warning

Description

Event reported when container image is unsigned and allowed by the user configuration.

Event ID: 11811

Message

Category

Severity

Description

Container {name} image is unsigned and not allowed by the user configuration

Container manager

Warning

Event reported when container image is unsigned and not allowed by the user
configuration.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

65

Chapter 21

CoPP events

CoPP events

The following are the events related to control plane policing.

Event ID: 1501

Message

Category

Severity

COPP initialization failed

CoPP

Error

Description

Logs COPP initialization failure.

Event ID: 1502

Message

Category

Severity

COPP initialization successful

CoPP

Info

Description

Logs COPP initialization success.

Event ID: 1503

Message

Category

Severity

Ingress FP Group create failed

CoPP

Error

Description

Logs ingress field processor group creation failure.

Event ID: 1504

Message

Category

Severity

Egress FP Group create failed

CoPP

Error

Description

Logs egress field processor group creation failure.

Event ID: 1505

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

66

Message

Category

Severity

Programming defaults failed

CoPP

Error

Description

Logs failure for initialization of default values.

Event ID: 1506

Message

Category

Severity

Packet class programming failed for <class>

CoPP

Error

Description

Logs failure of programming queue for a CoPP packet class.

Event ID: 1507

Message

Category

Severity

Failed to program ingress field processor rule for <class>

CoPP

Error

Description

Logs failure of programming ingress field processor for a COPP class.

Event ID: 1508

Message

Category

Severity

Failed to program egress rule for <class>

CoPP

Error

Description

Logs failure of programming egress field processor for a COPP class.

Event ID: 1509

Message

Category

Severity

CoPP initial initialization failed on slot <slot>

CoPP

Error

Description

Logs CoPP initial initialization failure on a slot.

Event ID: 1510

Message

CoPP final initialization failed on slot <slot>

CoPP events | 67

Category

Severity

CoPP

Error

Description

Logs CoPP final initialization failure on a slot.

Event ID: 1511

Message

Category

Severity

CoPP deinitialization failed on slot <slot>

CoPP

Error

Description

Logs CoPP deinitialization failure on a slot.

Event ID: 1512

Message

Category

Severity

Failed to configure hardware for CoPP on slot <slot> class <class>

CoPP

Error

Description

Logs failure while configuring hardware on a slot for a CoPP class.

Event ID: 1513

Message

Category

Severity

Failed to retrieve CoPP statistics from slot <slot> class <class>

CoPP

Error

Description

Logs failure while retrieving statistics on a slot for a CoPP class.

Event ID: 1514

Message

Category

Severity

CoPP final initialization failed.

CoPP

Error

Description

Logs CoPP final initialization failure.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

68

Chapter 22

CPU_RX events

CPU_RX events

The following are the events related to CPU_RX.

Event ID: 7501

Message

Kernel filter "<action>" failed on unit <unit> for <filter_description>

Category

CPU_RX

Severity

Information

Description

Event raised when a kernel filter cannot be created or deleted

Event ID: 7502

Message

Cannot create kernel filter on unit <unit> for <filter_description>. All filters are in use.
Configuring fewer per-port features can help with this issue.

Category

CPU_RX

Severity

Error

Description

Event raised when a kernel filter cannot be created because all filters are in use

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

69

Chapter 23
|            |         |        | Credential | Manager | events |
| ---------- | ------- | ------ | ---------- | ------- | ------ |
| Credential | Manager | events |            |         |        |
Thefollowingaretheeventsrelatedtocredentialmanager.
| Event ID: | 6501 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Aninternalerroroccurredwhilereadingtheexportpasswordanddefaultexport
passwordwasusedinstead.
| Category |     | CredentialManager |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- |
| Severity |     | Warning           |     |     |     |
Description Warnstheuserthatexportpasswordfilewascorruptedanddefaultpasswdwasused
instead.
| Event ID: | 6502 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Acriticalsystemfilehasbeencorrupted.Pleaseconfigureyourexportpasswordtothe
oneusedbyyourmostrecentconfigurationexportandimportyourmostrecent
configuration.
| Category |     | CredentialManager |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- |
| Severity |     | Warning           |     |     |     |
Description Warnstheuserthatthechassissecrethasbeencorrupted.
| Event ID: | 6504 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Self-signedcertificatesuccessfullycreatedforthehttps-server.
| Category |     | CredentialManager |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- |
| Severity |     | Info              |     |     |     |
Description Logsamessagewhentheself-signedcertiscreatedbycredmgr.
| Event ID: | 6505 |                                       |     |     |     |
| --------- | ---- | ------------------------------------- | --- | --- | --- |
| Message   |      | UseradminpasswordchangedfromServiceOS |     |     |     |
| Category  |      | CredentialManager                     |     |     |     |
| Severity  |      | Info                                  |     |     |     |
Description LogsamessagewhenauserchangesadminpasswordfromServiceOS
| Event ID: | 6506 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
70
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

SSH authorized keys were added for user <user>

Category

Credential Manager

Severity

Info

Description

Logs a message when SSH authorized keys are added for a user

Event ID: 6507

Message

Failed to write SSH authorized keys for user <user>

Category

Credential Manager

Severity

Error

Description

Logs a message after a failure to write SSH authorized keys for a user

Event ID: 6508

Message

SSH authorized keys deleted for user <user>

Category

Credential Manager

Severity

Info

Description

Logs a message afte deleting SSH authorized keys for a user

Event ID: 6509

Message

User <user> has configured an invalid SSH authorized key with key identifier <key-id>

Category

Credential Manager

Severity

Error

Description

Logs a message when SSH authorized key fails validation chack

Credential Manager events | 71

Chapter 24

CX LMS events

CX LMS events

The following are the events related to AOS-CX Feature Pack management.

Event ID: 15001

Message

Feature pack cloud-managed mode is enabled, LMS server will be used for feature pack
management

Category

CX_LMS

Severity

Info

Description

Event raised when the feature pack managament mode is set to cloud-managed

Event ID: 15002

Message

Feature pack cloud-managed mode is disabled, LMS server will no longer be used for
feature pack management

Category

CX_LMS

Severity

Info

Description

Event raised when the feature pack managament mode is set to anything different from
cloud-managed

Event ID: 15003

Message

Category

Severity

Feature pack validation with the LMS server triggered

CX_LMS

Info

Description

Event raised when a new feature pack validation process using LMS server is triggered

Event ID: 15004

Message

Category

Severity

CX-LMS has successfully installed a new feature pack file in the system

CX_LMS

Info

Description

Event raised when CX-LMS succesfully installs a new feature pack file in the switch.

Event ID: 15005

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

72

Message

Category

Severity

CX-LMS has successfully validated the system license

CX_LMS

Info

Description

Event raised when CX-LMS succesfully validates the feature pack in the switch.

Event ID: 15006

Message

Category

Severity

CX-LMS failed to validate the system license

CX_LMS

Error

Description

Event raised when CX-LMS fails to validate a feature pack for the switch.

CX LMS events | 73

Chapter 25

Device fingerprinting events

Device fingerprinting events

The following are the events related to device fingerprinting.

Event ID: 12401

Message

Reached the maximum number of clients limit on the switch for device fingerprinting.

Category

Device fingerprinting

Severity

Warning

Description

Log the event when the maximum client limit for device fingerprinting is reached on the
switch.

Event ID: 12402

Message

Reached the maximum clients limit of <client_limit> on the interface <interface> for device
fingerprinting.

Category

Device fingerprinting

Severity

Warning

Description

Log the event when the per port clients limit for device fingerprinting is reached.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

74

Chapter 26

DHCP Relay events

DHCP Relay events

The following are the events related to DHCP relay.

Event ID: 3401

Message

DHCP Relay Enabled

Category

DHCP Relay

Severity

Information

Description

This command enables the DHCP Relay feature in the device.

Event ID: 3402

Message

DHCP Relay Disabled

Category

DHCP Relay

Severity

Information

Description

This command disables the DHCP Relay feature in the device.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

75

Chapter 27

DHCP server events

DHCP server events

The following are the events related to DHCP server.

Event ID: 1901

Message

DHCP Lease added <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Information

Description

Logs DHCP lease addition

Event ID: 1902

Message

DHCP Lease deleted <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Information

Description

Logs DHCP lease deletion

Event ID: 1903

Message

DHCP Lease updated <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Information

Description

Logs DHCP lease updation

Event ID: 1904

Message

DHCP Lease addition failed <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Error

Description

Logs failure in DHCP lease addition

Event ID: 1905

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

76

Message

DHCP Lease deletion failed <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Error

Description

Logs failure in DHCP lease deletion

Event ID: 1906

Message

DHCP Lease update failed <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Error

Description

Logs failure in DHCP lease updation

Event ID: 1907

Message

DHCP server enabled on VRF <vrf_name>

Category

DHCP server

Severity

Information

Description

Event raised when DHCP server gets enabled on the VRF

Event ID: 1908

Message

DHCP server disabled on VRF <vrf_name>

Category

DHCP server

Severity

Information

Description

Event raised when DHCP server gets disabled on the VRF

Event ID: 1909

Message

Invalid DHCP configuration: <config> provided on DHCP Server instance running on VRF
<vrf_name>. Ignoring this config.

Category

DHCP server

Severity

Error

Description

Event raised when user configures an invalid DHCP configuration

Event ID: 1910

DHCP server events | 77

Message

DHCP Server Lease cleared on vrf <vrf>.

Category

DHCP server

Severity

Information

Description

Event raised when DHCP Server Lease on the VRF is cleared

Event ID: 1911

Message

DHCPv6 Server Lease cleared on vrf <vrf>.

Category

DHCP server

Severity

Information

Description

Event raised when DHCPv6 Server Lease on the VRF is cleared

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

78

Chapter 28
|        |          |        | DHCPv4 | snooping | events |
| ------ | -------- | ------ | ------ | -------- | ------ |
| DHCPv4 | snooping | events |        |          |        |
ThefollowingaretheeventsrelatedtoDHCPv4snooping:
| Event | ID: 8202 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message
Clientpacketdestinedtountrustedport<port>dropped.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketdroppedwhilepacketdestinedtountrustedport.
| Event | ID: 8204 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Receiveduntrustedrelayinfofromclient<mac>onport<port>.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketreceivedwithuntrustedrelayinfo.
| Event | ID: 8205 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Clientaddress<client_mac>notequaltosourceMAC<source_mac>detectedonport
<port>.
| Category    |          | DHCPv4snooping                                |     |     |     |
| ----------- | -------- | --------------------------------------------- | --- | --- | --- |
| Severity    |          | Warning                                       |     |     |     |
| Description |          | LogeventwhenclientaddressnotequaltosourceMAC. |     |     |     |
| Event       | ID: 8206 |                                               |     |     |     |
Message Bindingfor<ip_address>:<mac>existsonport<existing_port>.Droppingreleaserequest
receivedforthebindingon<new_port>.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenreleasepacketreceivedonincorrectport.
| Event | ID: 8207 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
79
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

The dynamic binding for <mac> on port <port> was replaced with a manual binding.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when dynamic binding for a port was replaced with a manual binding.

Event ID: 8208

Message

Drop request from <mac> for already assigned address <ip_address>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop client request for already assigned ip.

Event ID: 8209

Message

Drop offer from <server_ip_address> of already assigned address <lease_ip_address> to
<mac>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop server offer for already assigned ip.

Event ID: 8210

Message

Drop offer from <server_ip_address> of <lease_ip_address> address is illegal.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop server offer for illegal ip.

Event ID: 8211

Message

Maximum bindings limit reached on port <port>, dropping request from <mac>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when binding limit reached on port.

Event ID: 8212

DHCPv4 snooping events | 80

Message

All the dynamic binding entries were cleared.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when all dynamic binding entries are cleared.

Event ID: 8213

Message

Dynamic binding entries on the port <port> were cleared.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when all dynamic binding entries on a port are cleared.

Event ID: 8214

Message

Dynamic binding entries on the VLAN <vid> were cleared.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when all dynamic binding entries on a vlan are cleared.

Event ID: 8215

Message

Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when a specific dynamic binding entry on a vlan is cleared.

Event ID: 8216

Message

Failed to import dynamic ip binding entries from external storage. volume: <volume_
name>, filename: <file_name>.

Category

DHCPv4 snooping

Severity

Error

Description

Log event when failed to import dynamic ip binding entries from external storage.

Event ID: 8217

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

81

Message

Failed to import dynamic ip binding entries from local storage. filepath: <file_path>.

Category

DHCPv4 snooping

Severity

Error

Description

Log event when failed to import dynamic ip binding entries from local storage.

Event ID: 8218

Message

Flash-storage is active for DHCPv4-Snooping.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when flash-storage becomes active after external-storage unconfiguration.

Event ID: 8219

Message

Successfully imported <bindings_imported> dynamic ip binding entries from external
storage. volume: <volume_name>, filename: <file_name>.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when dynamic ip binding entries from external storage are successfully
imported.

Event ID: 8220

Message

Successfully imported <bindings_imported> dynamic ip binding entries from local storage.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when dynamic ip binding entries from local storage are successfully imported.

Event ID: 8221

Message

Client {mac} on vlan {vid}, port {port} received {client_ip} from server {server_ip} with
lease {lease}. Nameserver:{nameserver_ip}, Gateway:{gateway_ip}.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when a client receives IP from DHCP server along with static attributes.

Event ID: 8222

DHCPv4 snooping events | 82

Message

Category

Severity

Client {mac} on vlan {vid}, port {port} released {client_ip}.

DHCPv4 snooping

Info

Description

Log event when a client releases

Event ID: 8223

Message

Category

Severity

Client {mac} on vlan {vid}, port {port} lease period expired for {client_ip}.

DHCPv4 snooping

Info

Description

Log event when a client's lease period expires.

Event ID: 8224

Message

Client {mac} on vlan {vid}, port {port} with {client_ip}. Client attributes updated: Gateway
{gateway_ip}, Nameserver {nameserver_ip}, Lease period {lease}.

Category

DHCPv4 snooping

Severity

Info

Description

Log event when a client's static attributes are updated.

Event ID: 8225

Message

DHCPv4-Snooping dropped DHCP {message_type} packet received on untrusted port
{port} from {server_ip}

Category

DHCPv4 snooping

Severity

Warning

Description

DHCP server packet received on an untrusted port.

Event ID: 8226

Message

DHCPv4-Snooping dropped DHCP {message_type} packet received from unauthorized
server {server_ip} on trusted port {port}

Category

DHCPv4 snooping

Severity

Warning

Description

An unauthorized server detected on a trusted port.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

83

Chapter 29

DHCPv6 Relay events

DHCPv6 Relay events

The following are the events related to DHCPv6 relay.

Event ID: 3301

Message

DHCPv6 Relay Enabled

Category

DHCPv6 Relay

Severity

Information

Description

This command enables the DHCPv6 Relay feature in the device.

Event ID: 3302

Message

DHCPv6 Relay Disabled

Category

DHCPv6 Relay

Severity

Information

Description

This command disables the DHCPv6 Relay feature in the device.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

84

Chapter 30
|        |          |        | DHCPv6 | snooping | events |
| ------ | -------- | ------ | ------ | -------- | ------ |
| DHCPv6 | snooping | events |        |          |        |
ThefollowingaretheeventsrelatedtoDHCPv6snooping.
| Event | ID: 8302 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message
Clientpacketdestinedtountrustedport<port>dropped.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketdroppedwhilepacketdestinedtountrustedport.
| Event | ID: 8304 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Receiveduntrustedrelayinfofromclient<mac>onport<port>.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketreceivedwithuntrustedrelayinfo.
| Event | ID: 8305 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Bindingfor<ipv6_address>:<mac>existsonport<existing_port>.Droppingreleaserequest
receivedforthebindingon<new_port>.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenreleasepacketreceivedonincorrectport.
| Event | ID: 8306 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Thedynamicbindingfor<mac>onport<port>wasreplacedwithamanualbinding.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhendynamicbindingforaportwasreplacedwithamanualbinding.
| Event | ID: 8307 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
85
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Drop request from <mac> for already assigned address <ipv6_address>.

Category

DHCPv6 snooping

Severity

Warning

Description

Log event when drop client request for already assigned ip.

Event ID: 8308

Message

Maximum bindings limit reached on port <port>, dropping request from <mac>.

Category

DHCPv6 snooping

Severity

Warning

Description

Log event when binding limit reached on port.

Event ID: 8309

Message

All the dynamic binding entries were cleared.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when all dynamic binding entries are cleared.

Event ID: 8310

Message

Dynamic binding entries on the port <port> were cleared.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when all dynamic binding entries on a port are cleared.

Event ID: 8311

Message

Dynamic binding entries on the VLAN <vid> were cleared.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when all dynamic binding entries on a vlan are cleared.

Event ID: 8312

Message

Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.

DHCPv6 snooping events | 86

Category

DHCPv6 snooping

Severity

Info

Description

Log event when a specific dynamic binding entry on a vlan is cleared.

Event ID: 8313

Message

Failed to import dynamic ip binding entries from external storage. volume":" <volume_
name>, filename":" <file_name>.

Category

DHCPv6 snooping

Severity

Error

Description

Log event when import of dynamic binding entries from external storage is failed.

Event ID: 8314

Message

Failed to import dynamic ip binding entries from local storage. filepath":" <file_path>.

Category

DHCPv6 snooping

Severity

Error

Description

Log event when import of dynamic binding entries from local storage is failed.

Event ID: 8315

Message

Flash-storage is active for DHCPv6-Snooping.

Category

DHCPv6 snooping

Severity

Warning

Description

Log event when flash-storage becomes active after external-storage unconfiguration.

Event ID: 8316

Message

Successfully imported <bindings_imported> dynamic ip binding entries from external
storage. volume: <volume_name>, filename: <file_name>.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when dynamic ip binding entries from external storage are successfully
imported.

Event ID: 8317

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

87

Message

Successfully imported <bindings_imported> dynamic ip binding entries from local storage.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when dynamic ip binding entries from local storage are successfully imported.

Event ID: 8318

Message

Client {mac} on vlan {vid}, port {port} received {client_ip} from server {server_ip} with
lease {lease}. Nameserver:{nameserver_ip}.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when a client receives IPv6 address from DHCP server along with static
attributes

Event ID: 8319

Message

Category

Severity

Client {mac} on vlan {vid}, port {port} released {client_ip}.

DHCPv6 snooping

Info

Description

Log event when a client releases IPv6 address.

Event ID: 8320

Message

Category

Severity

Client {mac} on vlan {vid}, port {port} lease period expired for {client_ip}.

DHCPv6 snooping

Info

Description

Log event when a client's lease period expires.

Event ID: 8321

Message

Client {mac} on vlan {vid}, port {port} with {client_ip}. Client attributes updated:
Nameserver {nameserver_ip}, Lease period {lease}.

Category

DHCPv6 snooping

Severity

Info

Description

Log event when a client's static attributes are updated.

Event ID: 8322

DHCPv6 snooping events | 88

Message

DHCPv6-Snooping dropped DHCP {message_type} packet received on untrusted port
{port} from {server_ip}

Category

DHCPv6 snooping

Severity

Warning

Description

Log event when a server packet is dropped on untrusted port

Event ID: 8323

Message

DHCPv6-Snooping dropped {message_type} packet received from unauthorized server
{server_ip} on trusted port {port}.

Category

DHCPv6 snooping

Severity

Warning

Description

Log event when packet unauthorized server is dropped.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

89

|           |                |          |               |          | Chapter | 31     |
| --------- | -------------- | -------- | ------------- | -------- | ------- | ------ |
|           | Discovery      | and      | Capability    | Exchange | (DCBx)  | events |
| Discovery | and Capability | Exchange | (DCBx) events |          |         |        |
ThefollowingaretheeventsrelatedtoDCBx.
| Event ID: | 9201 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message
DCBXEnabled
Category DicoveryandCapabilityExchange(DCBx)
Severity Info
Description LogseventwhenDCBXisgloballyenabled
| Event ID: | 9202 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message DCBXDisabled
Category DicoveryandCapabilityExchange(DCBx)
Severity Info
Description LogeventwhenDCBXisgloballydisabled
| Event ID: | 9203 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message DCBXisenabledoninterface<intf_name>
Category DicoveryandCapabilityExchange(DCBx)
Severity Info
Description LogeventwhenDCBXisenabledontheinterface
| Event ID: | 9204 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message
DCBXisdisabledoninterface<intf_name>
Category DicoveryandCapabilityExchange(DCBx)
Severity Info
Description LogeventwhenDCBXisdisabledontheinterface
| Event ID: | 9205 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
90
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

DCBX status active on interface <intf_name>

Category

Dicovery and Capability Exchange (DCBx)

Severity

Info

Description

Log event when DCBX oper status is active on an interface

Event ID: 9206

Message

DCBX status inactive on interface <intf_name>

Category

Dicovery and Capability Exchange (DCBx)

Severity

Info

Description

Log event when DCBX oper status is inactive on an interface

Event ID: 9207

Message

PFC TLV status active on interface <intf_name>

Category

Dicovery and Capability Exchange (DCBx)

Severity

Info

Description

Log event when PFC TLVs are active on an interface

Event ID: 9208

Message

PFC TLV status inactive on interface <intf_name>

Category

Dicovery and Capability Exchange (DCBx)

Severity

Info

Description

Log event when PFC TLVs are inactive on an interface

Event ID: 9209

Message

PFC TLV status priority mismatch on interface <intf_name>

Category

Dicovery and Capability Exchange (DCBx)

Severity

Warning

Description

Log event when there is PFC TLV priority mismatch on an interface

Discovery and Capability Exchange (DCBx) events | 91

|             |          |        |             | Chapter  | 32     |
| ----------- | -------- | ------ | ----------- | -------- | ------ |
|             |          |        | Distributed | services | events |
| Distributed | services | events |             |          |        |
Thefollowingaretheeventsrelatedtodistributedservicesonthe10000Switchseries.
| Event ID:   | 13901 |                                                      |     |     |     |
| ----------- | ----- | ---------------------------------------------------- | --- | --- | --- |
| Message     |       | ChassisRebootRequested:{reason}                      |     |     |     |
| Category    |       | DistributedServices                                  |     |     |     |
| Severity    |       | Warning                                              |     |     |     |
| Description |       | Logeventthatindicatesthechassisrequiresareboot.      |     |     |     |
| Event ID:   | 13902 |                                                      |     |     |     |
| Message     |       | DistributedServicesAdmissionRejected.Reason:{reason} |     |     |     |
| Category    |       | DistributedServices                                  |     |     |     |
| Severity    |       | Warning                                              |     |     |     |
Description LogeventthatindicatesadmissiontoPSMwasrejected.'event_description_template
| Event ID: | 13903 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message
PSMcoordinatesmismatch.Activecoordinates:{active_coordinates},Configured
coordinates:{configured_coordinates}.
| Category    |     | DistributedServices                            |     |     |     |
| ----------- | --- | ---------------------------------------------- | --- | --- | --- |
| Severity    |     | Warning                                        |     |     |     |
| Description |     | LogeventthatindicatesmismatchofPSMcoordinates. |     |     |     |
92
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 33

DNS client events

DNS client events

The following are the events related to DNS client.

Event ID: 11901

Message

<type> event for VRF <vrf_name>

Category

DNS client

Severity

Information

Description

Event reported when DNS event triggered

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

93

Chapter 34

Dot1x supplicant events

Dot1x supplicant events

The following are the events related to dot1x supplicant.

Event ID: 12301

Message

802.1X supplicant has blocked the interface <ifname>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant is blocking the interface on the data-plane.

Event ID: 12302

Message

802.1X supplicant has unblocked the interface <ifname>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant is opening the interface on the data-plane.

Event ID: 12303

Message

802.1X supplicant PAE restarted on interface <ifname> due to change in policy <policy>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant PAE is restarted due to a change in the policy used on the interface.

Event ID: 12304

Message

802.1X supplicant is not supported on the port <port>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant is enabled on a port that is not supported (Ex: LAG, ROP).

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

94

Chapter 35

Download events

Download events

The following are the events related to file download actions.

Event ID: 14501

Message

Category

Severity

File download started from {url}

DNLD

Info

Description

Indicates that a file download has been started

Event ID: 14502

Message

Category

Severity

File download complete from {url}

DNLD

Info

Description

Indicates that a file has been successfully downloaded

Event ID: 14503

Message

Category

Severity

File download aborted from {url}

DNLD

Info

Description

Indicates that a file download has been aborted

Event ID: 14504

Message

Category

Severity

File download failed from {url} with error code: {error}, {desc}

DNLD

Info

Description

Indicates that a file download has failed

Event ID: 14505

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

95

Message

Category

Severity

File upload started to {url}

DNLD

Info

Description

Indicates that a file upload has been started

Event ID: 14506

Message

Category

Severity

File upload complete to {url}

DNLD

Info

Description

Indicates that a file has been successfully uploaded

Event ID: 14507

Message

Category

Severity

File upload aborted to {url}

DNLD

Info

Description

Indicates that a file upload has been aborted

Event ID: 14508

Message

Category

Severity

File upload failed to {url} with error code: {error}, {desc}

DNLD

Info

Description

Indicates that a file upload has failed

Event ID: 14509

Message

Category

Severity

File download retrying from {url}

DNLD

Info

Description

Indicates that a file download has been retried

Event ID: 14510

Message

File upload retrying from {url}

Download events | 96

Category

Severity

DNLD

Info

Description

Indicates that a file upload has been retried

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

97

Chapter 36

DPSE daemon events

DPSE daemon events

The following are the events related to the DPSE daemon.

Event ID: 10901

Message

Line card module {linecard_name} triggered backplane enhanced sequence recovery

Category

Back Plane Sequence Events (DPSE)

Severity

Critical

Description

A line card hit a backplane sequence error that triggered a recovery operation

Event ID: 10902

Message

HA event triggered backplane sequence recovery

Category

Back Plane Sequence Events (DPSE)

Severity

Info

Description

A backplane sequence reset was triggered due to an HA event

Event ID: 10903

Message

HA event completed backplane sequence recovery

Category

Back Plane Sequence Events (DPSE)

Severity

Info

Description

The system completed a backplane sequence reset triggered by an HA event

Event ID: 10904

Message

Line card module {linecard_name} triggered backplane enhanced sequence recovery

Category

Back Plane Sequence Events (DPSE)

Severity

Critical

Description

The system completed backplane sequence recovery triggered by line card error

Event ID: 10905

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

98

Message

No active modules have been detected in the system.

Category

Back Plane Sequence Events (DPSE)

Severity

Info

Description

No active modules have been detected in the system.

Event ID: 10906

Message

Control Plane (<operation_name>) failure during (<plugin_name>) configuration

Category

Back Plane Sequence Events (DPSE)

Severity

Critical

Description

An ops-switchd plugin failed executing an operation

DPSE daemon events | 99

Chapter 37

ECMP events

ECMP events

The following are the events related to ECMP.

Event ID: 1801

Message

Category

Severity

Failed to update ecmp object for route <route>, error: <err>

ECMP

Error

Description

logs errors while creating ecmp group.

Event ID: 1802

Message

Update ecmp object for route <route>

Category

ECMP

Severity

Information

Description

logs while creating ecmp group.

Event ID: 1803

Message

Category

Severity

Failed to delete ecmp egress object <egressid>, error: <err>

ECMP

Error

Description

logs errors while deleting ecmp group.

Event ID: 1804

Message

Delete ecmp egress object <egressid>

Category

ECMP

Severity

Information

Description

logs while deleting ecmp group.

Event ID: 1805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

100

Message

Category

Severity

ECMP error: <err>

ECMP

Error

Description

logs for ECMP setup errors.

ECMP events | 101

Chapter 38

ERPS events

ERPS events

The following are the events related to ERPS.

Event ID: 8501

Message

Expected R-APS packets not received on <ifID> in ring <ringID> with control VLAN <ccvlan>

Category

ERPS

Severity

Warning

Description

Log event when RAPS messages are not received for a certain time interval

Event ID: 8502

Message

Misconfiguration detected on ring <ringID> with control VLAN <ccvlan>. Another node in
the ring with mac <node> is also operating as an RPL owner

Category

ERPS

Severity

Warning

Description

Log event when a ring misconfiguration happens

Event ID: 8503

Message

Operational state of the ring <ringID>, instance <instanceID> changed to <state>

Category

ERPS

Severity

Information

Description

Log state transition of ring instance

Event ID: 8504

Message

<interfaceName> is not an L2 port

Category

ERPS

Severity

Information

Description

Log event when ring is configured with a non-L2 port

Event ID: 8505

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

102

Message

<interfaceName> is already associated with <portName> of ERPS ring <ringID>

Category

ERPS

Severity

Information

Description

Log event when an interface which is already associated to a ring port is getting mapped
to other ring port as well

Event ID: 8506

Message

Configured control-channel VLAN <ccVlan> is already protected by ERPS ring <ringID>,
instance <instanceID>

Category

ERPS

Severity

Information

Description

Log event when control-channel VLAN is part of the protected-vlans

Event ID: 8507

Message

VLAN <ccVlan> is already configured as control-channel for instance <instanceID> of ring
<ringID>

Category

ERPS

Severity

Information

Description

Log event when control-channel VLAN overlaps with another control-channel of same
ring

Event ID: 8508

Message

Vlan <dataVlan> is already part of the protected VLAN set of ring <ringID> instance
<instanceID>

Category

ERPS

Severity

Information

Description

Log event when protected-vlan(s) overlap

Event ID: 8509

Message

Control VLAN must not be same on parent and sub rings

Category

ERPS

Severity

Information

Description

Log event when same control-channel VLAN is configured on both major and sub-rings

Event ID: 8510

ERPS events | 103

Message

Parent-ring <ringID> is same as sub-ring

Category

ERPS

Severity

Information

Description

Log event when parent-ring id is configured to be the same as sub-ring

Event ID: 8511

Message

VLAN <vlanID> in the protected VLANs list is also configured as the control-channel

Category

ERPS

Severity

Information

Description

Log event when VLAN from the protected-vlans list is already configured as control-
channel VLAN

Event ID: 8512

Message

<portName> is already configured as RPL port for instance <instanceID>

Category

ERPS

Severity

Information

Description

Log event if the same ring port is configured as RPL port for more than one instance

Event ID: 8513

Message

RPL configuration is not allowed on ISL port <interfaceName>

Category

ERPS

Severity

Information

Description

Log event if ring port which is also an ISL is being configured as RPL

Event ID: 8514

Message

Protected VLAN set of instance in sub-ring should map to same instance in the parent
ring

Category

ERPS

Severity

Information

Description

Log event if protected-vlan set of sub-ring is not a subset of the major-ring

Event ID: 8515

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

104

Message

Operational state of the ring <ringID>, instance <instanceID> changed to Initializing with
reason <reason>

Category

ERPS

Severity

Information

Description

Log transition of state of ring instance to initializing and the reason for it

ERPS events | 105

Chapter 39

EVPN events

EVPN events

The following are the events related to EVPN.

Event ID: 9501

Message

Category

Severity

EVPN EVI: <evi> created

EVPN

Info

Description

Logs EVPN EVI create event.

Event ID: 9502

Message

Category

Severity

EVPN EVI: <evi> deleted

EVPN

Info

Description

Logs EVPN EVI delete event.

Event ID: 9503

Message

Category

Severity

EVPN RD: <rd> updated for EVI: <evi>

EVPN

Info

Description

Logs EVPN RD update event for an EVI.

Event ID: 9504

Message

Category

Severity

EVPN RD deleted for EVI: <evi>

EVPN

Info

Description

Logs EVPN RD delete event for an EVI.

Event ID: 9505

Message

EVPN RT: <rt> created for EVI: <evi>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

106

Category

Severity

EVPN

Info

Description

Logs EVPN RT create event for an EVI.

Event ID: 9506

Message

Category

Severity

EVPN RT: <rt> deleted for EVI: <evi>

EVPN

Info

Description

Logs EVPN RT delete event for an EVI.

Event ID: 9507

Message

Category

Severity

EVPN RT: <rt> updated for EVI: <evi>

EVPN

Info

Description

Logs EVPN RT update event for an EVI.

Event ID: 9508

Message

Category

Severity

VNI: <vni> is added for EVPN Peer VTEP: <vtep_ip>

EVPN

Info

Description

Logs EVPN VTEP VNI add event.

Event ID: 9509

Message

Category

Severity

VNI: <vni> is deleted for EVPN Peer VTEP: <vtep_ip>

EVPN

Info

Description

Logs EVPN VTEP VNI delete event.

Event ID: 9510

Message

EVPN static MAC conflict <action>, MAC: <mac_addr>, IP address: <ip_addr>, VTEP: <vtep_
ip>

Category

EVPN

EVPN events | 107

Severity

Error

Description

Logs EVPN static MAC conflict event.

Event ID: 9511

Message

Category

Severity

EVPN static MAC conflict <action>, MAC: <mac_addr>

EVPN

Error

Description

Logs EVPN static MAC conflict event.

Event ID: 9512

Message

Category

Severity

EVPN duplicate MAC dampening <action>, MAC: <mac_addr>

EVPN

Error

Description

Logs EVPN duplicate MAC dampening event.

Event ID: 9513

Message

Category

Severity

EVPN VRF: <vrf> created

EVPN

Info

Description

Logs EVPN VRF create event.

Event ID: 9514

Message

Category

Severity

EVPN VRF: <vrf> deleted

EVPN

Info

Description

Logs EVPN VRF delete event.

Event ID: 9515

Message

Category

Severity

EVPN RD: <rd> updated for VRF: <vrf>

EVPN

Info

Description

Logs EVPN VRF RD update event.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

108

Event ID: 9516

Message

Category

Severity

EVPN RT: <rt> created for VRF: <vrf>

EVPN

Info

Description

Logs EVPN VRF RT create event.

Event ID: 9517

Message

Category

Severity

EVPN RT {rt_type}: {rt} deleted for VRF: {vrf}

EVPN

Info

Description

Logs EVPN VRF RT delete event.

Event ID: 9518

Message

Category

Severity

EVPN RT {rt_type}: {rt} deleted for VRF: {vrf}

EVPN

Info

Description

Logs EVPN VRF RT update event.

Event ID: 9519

Message

Category

Severity

EVPN dynamic vxlan tunnel briding mode ibgp-ebgp enabled

EVPN

Info

Description

Log event when dynamic vxlan tunnel briding mode ibgp-ebgp is enabled

Event ID: 9520

Message

Category

Severity

EVPN dynamic vxlan tunnel briding mode ibgp-ebgp disabled

EVPN

Info

Description

Log event when dynamic vxlan tunnel briding mode ibgp-ebgp is disabled

Event ID: 9521

EVPN events | 109

Message

Category

Severity

EVPN VLAN Aware Bundle : {bundle_name} created.

EVPN

Info

Description

Log event when EVPN VLAN Aware bundle created

Event ID: 9522

Message

Category

Severity

EVPN VLAN Aware Bundle : {bundle_name} deleted.

EVPN

Info

Description

Log event when EVPN VLAN Aware bundle deleted

Event ID: 9523

Message

Category

Severity

EVPN VLAN Aware Bundle : {bundle_name} disabled.

EVPN

Info

Description

Log event when EVPN VLAN Aware bundle disabled

Event ID: 9524

Message

Category

Severity

EVPN VLAN Aware Bundle : {bundle_name} enabled.

EVPN

Info

Description

Log event when EVPN VLAN Aware bundle enabled

Event ID: 9525

Message

Category

Severity

EVPN EVI : {evi} updated with ethernet-tag : {eth_tag}.

EVPN

Info

Description

Log event when VLAN ethernet-tag is updated

Event ID: 9526

Message

EVPN duplicate IP dampening {action}, MAC: {mac_addr}, IP address: {ip_addr}, VTEP:
{vtep_ip}

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

110

Category

Severity

EVPN

Info

Description

Logs EVPN duplicate IP dampening event.

Event ID: 9527

Message

Category

Severity

EVPN EVI: RT {rtt} {rt} updated for EVI: {evi}

EVPN

Info

Description

Logs EVPN RT update event for an EVI.

Event ID: 9528

Message

Category

Severity

Description

Event ID: 9529

Message

Category

Severity

A route-map exists with broadcast group config, please unconfigure it

EVPN

Info

Logs event when a route-map exists with broadcast group and dynamic bridging ibgp-
ebgp mode is being configured.

EVPN Ethernet Segment with ESI {esi} is created.

EVPN

Info

Description

Log event when EVPN Ethernet Segment created

Event ID: 9530

Message

Category

Severity

EVPN Ethernet Segment with ESI {esi} is deleted.

EVPN

Info

Description

Log event when EVPN Ethernet Segment deleted

Event ID: 9531

Message

EVPN RT auto mode legacy created for EVI: {evi}.

Category

EVPN

EVPN events | 111

Severity

Info

Description

Logs EVPN RT auto mode create event for an EVI.

Event ID: 9532

Message

Category

Severity

EVPN RT auto mode legacy deleted for EVI: {evi}.

EVPN

Info

Description

Logs EVPN RT auto mode delete event for an EVI.

Event ID: 9533

Message

Category

Severity

EVPN_MHM: More than one ES member learnt {num_es_members}.

EVPN

Warning

Description

Logs event when more than one ES member is learnt.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

112

Chapter 40

External Storage events

External Storage events

The following are the events related to external storage.

Event ID: 7801

Message

Share <name> mount failure' throttle_count: 10

Category

External Storage

Severity

Error

Description

Event raised when a share fails to mount

Event ID: 7802

Message

Share <name> dismount failure

Category

External Storage

Severity

Error

Description

Event raised when a share fails to dismount

Event ID: 7803

Message

Share <name> is mounted

Category

External Storage

Severity

Information

Description

Event raised when a share mounts

Event ID: 7804

Message

Share <name> is dismounted

Category

External Storage

Severity

Information

Description

Event raised when a share dismounts

Event ID: 7805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

113

Message

Share <name> mount is aborted

Category

External Storage

Severity

Error

Description

Event raised when a mount times out or aborts due to a config change

Event ID: 7806

Message

USB device <status>.

Category

External Storage

Severity

Information

Description

USB device mounted or unmounted.

External Storage events | 114

Chapter 41

Fan events

Fan events

The following are the events related to fan.

Event ID: 201

Message

Category

Severity

There are <count> total fans in subsystem <subsystem>.

Fan

Info

Description

Log the total number of fans in the subsystem

Event ID: 202

Message

Category

Severity

Subsystem <subsystem> setting fan speed control register to <speedval>: <value>.

Fan

Info

Description

Log the fan speed set

Event ID: 203

Message

Category

Severity

Air flow direction: <value>.

Fan

Info

Description

Log the air flow direction

Event ID: 204

Message

Category

Severity

Fan tray <FT_Name> was removed.

Fan

Info

Description

Log event when a fan tray is removed from the chassis

Event ID: 205

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

115

Message

Category

Severity

Fan tray <FT_Name> was inserted.

Fan

Info

Description

Log event when a fan tray is inserted into the chassis

Event ID: 206

Message

Category

Severity

Fan module <FMod_Name> was removed.

Fan

Info

Description

Log event when a fan module is removed from a fan tray

Event ID: 207

Message

Category

Severity

Fan module <FMod_Name> was inserted.

Fan

Info

Description

Log event when a fan module is inserted into a fan tray

Event ID: 208

Message

Category

Severity

Fan tray {FT_Name} is not supported by the system. Please insert a supported fan tray.
Refer to the Installation Guide for supported configurations.

Fan

Error

Description

Log event when an unsupported fan tray is inserted

Event ID: 209

Message

Shutting down system now because <num_of_failure> <failure_type> <compare_mode> limit
of <num_of_failure_limit>': yes

Category

Fan

Severity

Emergency

Description

Log error when system shutdown is initiated due to critical fan faults

Event ID: 211

Fan events | 116

Message

Category

Severity

Shutting down system in <seconds> seconds because <num_of_failure> <failure_type>
<compare_mode> limit of <num_of_failure_limit>

Fan

Alert

Description

Log error when the number of failures exceed the allowable limit

Event ID: 212

Message

Category

Severity

System shutdown timer is cancelled.': yes

Fan

Info

Description

Log event when the shutdown timer is cancelled

Event ID: 213

Message

Category

Severity

<num_of_failure> <failure_type> in the system.': yes

Fan

Error

Description

Log error when there are fan faults

Event ID: 214

Message

Category

Severity

<function>: Fan <fan_name> faulted, reason: <reason>.': yes

Fan

Error

Description

List out the faulty or missing fan names

Event ID: 215

Message

Category

Severity

<FanName> fan is <FanStatus>.

Fan

Info

Description

Log the fan status

Event ID: 216

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

117

Message

Category

Severity

Status of fan <FanName> has changed from <OldStatus> to <NewStatus>.

Fan

Info

Description

Log the change in fan status

Event ID: 217

Message

Operational fan count below minimum. <FanCount> fans operating, but <FanMinimum>
are required.

Category

Fan

Severity

Warning

Description

Log when minimum number of fans are not present.

Event ID: 218

Message

Category

Severity

Fan speed index for thermal zone <ZoneIdx> is <FanSpdIdxStatus>.

Fan

Info

Description

Log when the fan speed index changes to and from the maximum for each thermal zone

Event ID: 219

Message

Category

Severity

Fan tray <FT_Name> powered <Status>.

Fan

Info

Description

Log event when a fan tray is powered on or off

Event ID: 220

Message

Category

Severity

Fan tray <FT_Name> airflow is <FT_Dir>.

Fan

Info

Description

Log event when a fan tray is inserted specifying its airflow direction

Event ID: 221

Message

<FT_air_curr> airflow fan tray <FT_Name> unsupported; this system requires <FT_air_req>

Fan events | 118

Category

Severity

airflow.

Fan

Error

Description

Log event when a fan tray airflow is not matching with system airflow

Event ID: 222

Message

Category

Severity

<num_of_failure> <failure_type> <compare_mode> limit of <num_of_failure_limit>': yes

Fan

Error

Description

Log error when number of faulty/supported fans does not meet the allowable limit

Event ID: 223

Message

Category

Severity

Fan tray <FT_Name> FRU EPPROM is incorrectly programmed.

Fan

Error

Description

Log when fan tray SKU ID in FRU is mismatched

Event ID: 224

Message

Category

Severity

<FT_air_curr> airflow fan tray <FT_Name> disabled; this system requires <FT_air_req>
airflow.

Fan

Error

Description

Log event when a fan tray airflow is not matching with system airflow and is disabled

Event ID: 225

Message

Category

Severity

fan tray <FT_Name> misconfigured; this fan tray has been <En_Dis>.

Fan

Info

Description

Log event when a misconfigured fan tray is enabled or disabled

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

119

Chapter 42

Fault monitor events

Fault monitor events

The following are the events related to fault monitor.

Event ID: 11101

Message

Interface <interface>: <fault> fault detected': yes

Category

Fault monitor

Severity

Warning

Description

Logs event when a fault is detected on an interface.

Event ID: 11102

Message

Interface <interface>: <fault> fault detected and port disabled': yes

Category

Fault monitor

Severity

Warning

Description

Logs event and shutdown the interface when a fault is detected on an interface.

Event ID: 11103

Message

Interface <interface>: <fault> fault re-enable time expired, port enabled': yes

Category

Fault monitor

Severity

Info

Description

Interface is auto-enabled on timer expiry.

Event ID: 11104

Message

Interface <interface>: <fault> fault disable cancelled due to configuration change': yes

Category

Fault monitor

Severity

Info

Description

Interface is auto-enabled on profile configuration change.

Event ID: 11105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

120

Message

Admin state changed and interface: <interface> is auto-enabled': yes

Category

Fault monitor

Severity

Info

Description

Interface is auto-enabled on admin state change.

Event ID: 11106

Message

Interface <interface>: <fault> fault detected, port is already disabled by another fault.': yes

Category

Fault monitor

Severity

Warning

Description

Logs event when disabling of a faulty interface failed.

Event ID: 11107

Message

MAC Lockout packet drop detected for {mac} as destination address with packet count:
{da_diff_count}.

Category

Fault monitor

Severity

Info

Description

Logs event when a packet drop is detected for MAC Lockout MAC as source address.

Event ID: 11108

Message

MAC Lockout packet drop detected for {mac} as destination address with packet count:
{da_diff_count}.

Category

Fault monitor

Severity

Info

Description

Logs event when a packet drop is detected for MAC Lockout MAC as destination address.

Event ID: 11109

Message

MAC Lockout packet drop detected for {mac} as source & destination address with
source packet count: {sa_diff_count} and destination packet count: {da_diff_count}.

Category

Fault monitor

Severity

Info

Description

Logs event when a packet drop is detected for MAC Lockout.

Fault monitor events | 121

Chapter 43

Feature Pack events

Feature Pack events

The following are the events related to CX Advanced and CX Premium feature packs.

Event ID: 14401

Message

Category

Severity

{feature_pack_name} installed

Feature Pack

Info

Description

Event raised when a feature pack is installed

Event ID: 14402

Message

Category

Severity

{feature_pack_name} erased.

Feature Pack

Info

Description

Event raised when a feature pack is erased.

Event ID: 14403

Message

Category

Severity

{feature_pack_name} expired on {expiry_date}.

Feature Pack

Warning

Description

Event raised when a feature pack expires

Event ID: 14404

Message

Feature pack {parameter_type} {subscription_parameter} does not match device
{parameter_type} {device_parameter}

Category

Feature Pack

Severity

Warning

Description

Event raised when a feature pack serial number or MAC address does not match that of
the device

Event ID: 14405

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

122

Message

Category

Severity

Event raised when a feature pack file downloads successfully

Feature Pack

Info

Description

Feature pack file download success

Event ID: 14406

Message

Category

Severity

Feature pack file download failure

Feature Pack

Warning

Description

Event raised when a feature pack file download fails

Event ID: 14407

Message

Category

Severity

Description

Event ID: 14408

Feature pack subscription through HPE Aruba Networking Central is {connection_state}

Feature Pack

Info

Event raised when a feature pack subscription through HPE Aruba Networking Central
becomes connected or disconnected

Message

VSF member serial number {device_serial} not subscribed as part of installed feature
pack

Category

Feature Pack

Severity

Warning

Description

Event raised when a VSF member is not subscribed as part of the installed feature pack

Event ID: 14409

Message

Category

Severity

Feature {feature_name} is operating in honor mode without a valid feature pack.

Feature Pack

Warning

Description

Periodic event raised to indicate that a feature is operating in honor mode

Event ID: 14410

Message

Connection to feature pack server lost and subscription for {feature_pack_name} cannot

Feature Pack events | 123

be validated. Subscribed features will continue to operate in honor mode.

Category

Feature Pack

Severity

Warning

Description

Event raised when a connection to the feature pack server has been lost and the feature
pack subscription cannot be validated

Event ID: 14411

Message

No feature pack is installed. This device requires an Advanced or Premium feature pack
to use advanced or premium features.

Category

Feature Pack

Severity

Warning

Description

Event raised to indicate that the device requires a feature pack

Event ID: 14412

Message

Advanced feature pack installed. This system requires a Premium feature pack to use all
features.

Category

Feature Pack

Severity

Warning

Description

Event raised to indicate that a higher feature pack tier is available and necessary to
enable higher tier features

Event ID: 14413

Message

Category

Severity

Software feature pack {feature_pack_name} revoked by the server.

Feature Pack

Info

Description

Event raised when a feature pack is revoked by the feature pack server.

Event ID: 14414

Message

Feature pack mode {feature_pack_mode} does not match installed feature pack type
{feature_pack_type}.

Category

Feature Pack

Severity

Warning

Description

Event raised when the feature pack mode configured does not match the feature pack
type installed on the device.

Event ID: 14415

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

124

Message

Cloud-managed mode is enabled. A feature pack server will be used for feature pack
management.

Category

Feature Pack

Severity

Info

Description

Event raised when the feature pack management mode is set to cloud-managed

Event ID: 14416

Message

Cloud-managed mode is disabled. A feature pack server will no longer be used for
feature pack management.

Category

Feature Pack

Severity

Info

Description

Event raised when the management mode is different than cloud-managed

Event ID: 14417

Message

Category

Severity

The feature pack has been successfully validated by the server

Feature Pack

Info

Description

Event raised when the feature pack was successfully validated by the server

Event ID: 14418

Message

Category

Severity

Feature pack server failed to validate the installed feature pack

Feature Pack

Error

Description

Event raised when there is an error validating a feature pack by the server

Event ID: 14419

Message

One or more advanced features have been blocked due to an invalid or missing feature-
pack. Check show feature-pack for details.

Category

Feature Pack

Severity

Warning

Description

Event raised when an invalid or missing feature pack blocks one or more features from
operating

FIB events
The following are the events related to Forwarding Information Base (FIB) management.

FIB events | 125

Event ID: 16501

Message

Max protected nexthops capacity ({max_capacity}) has been reached

Category

FIB

Severity

Warning

Description

Log event to indicate that the max protected nexthops capacity has been reached

Event ID: 16502

Message

Category

Severity

Failed to allocate index for protected nexthop

FIB

Info

Description

Log event to indicate failure when allocating an index for protected nexthop

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

126

Chapter 44

Firmware Update events

Firmware Update events

The following are the events related to firmware update.

Event ID: 4401

Message

User <user>: <image_profile> image updated via <dnld_type> from <host>. Firmware
version, Before Update: <before> After Update: <after>

Category

Firmware Update

Severity

Info

Description

Indicates that the switch firmware was succesfully updated from a remote source

Event ID: 4402

Message

User <user>: <image_profile> image updated via <dnld_type>. Firmware version, Before
Update: <before> After Update: <after>

Category

Firmware Update

Severity

Info

Description

Indicates that the switch firmware was succesfully updated from a local source

Event ID: 4403

Message

User <user>: <image_profile> image update failed via <dnld_type> from <host>

Category

Firmware Update

Severity

Error

Description

Indicates that a switch firmware update failed from a remote source

Event ID: 4404

Message

User <user>: <image_profile> image update failed via <dnld_type>

Category

Firmware Update

Severity

Error

Description

Indicates that a switch firmware update failed from a local source

Event ID: 4405

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

127

Message

Firmware image signature not valid

Category

Firmware Update

Severity

Error

Description

Indicates that the signature verification check during a switch firmware or hot-patch
download failed

Event ID: 4406

Message

Firmware image is not compatible with hardware

Category

Firmware Update

Severity

Error

Description

Indicates that the signature verification check during a switch firmware or hot-patch
download failed

Event ID: 4407

Message

Firmware image is invalid

Category

Firmware Update

Severity

Error

Description

Indicates that the signature verification check during a switch firmware or hot-patch
download failed

Event ID: 4408

Message

Category

Severity

User {user}: hot-patch "{hotpatch_name}" downloaded via {dnld_type} from {host

Firmware Update

Info

Description

Indicates that a hot-patch image was downloaded succesfully from a remote sour

Event ID: 4409

Message

Category

Severity

User {user}: hot-patch "{hotpatch_name}" downloaded via {dnld_type}.

Firmware Update

Info

Description

Indicates that a hot-patch image was downloaded succesfully from a local source

Event ID: 4410

Firmware Update events | 128

Message

Category

Severity

User {user}: hot-patch "{hotpatch_name}" download failed via {dnld_type} from {host}

Firmware Update

Info

Description

Indicates that a hot-patch image download failed from a remote source

Event ID: 4411

Message

Category

Severity

User {user}: hot-patch "{hotpatch_name}" download failed via {dnld_type}

Firmware Update

Info

Description

Indicates that a hot-patch image download failed from a local source

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

129

Chapter 45
| Forwarding | and Queuing | for Time-Sensitive | Streams | (FQTSS) |
| ---------- | ----------- | ------------------ | ------- | ------- |
Forwarding and Queuing for Time-Sensitive Streams (FQTSS) events
Thefollowingaretheeventsrelatedtodistributedservicesonthe10000Switchseries.
Event ID: 15701
| Message  | {cache_type}cacheentrywithkey{key}is{event} |     |     |     |
| -------- | ------------------------------------------- | --- | --- | --- |
| Category | FQTSS                                       |     |     |     |
| Severity | Info                                        |     |     |     |
Description Eventreportedwhenport-streamcacheiscreatedordeleted.
Event ID: 15702
Message Port{port_name}stateischangedfrom{port_state_old}to{port_state_new}
| Category    | FQTSS                             |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Info                              |     |     |     |
| Description | Eventreportedwhenportstatechanges |     |     |     |
Event ID: 15703
Message Stream{streamid}stateischangedfrom{stream_state_old}to{stream_state_new}
| Category    | FQTSS                               |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Info                                |     |     |     |
| Description | Eventreportedwhenstreamstatechanges |     |     |     |
Event ID: 15704
Message Stream{streamid}stateonport{port_name}ischangedfrom{port_stream_state_old}to
{port_stream_state_new}
| Category    | FQTSS                                    |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Info                                     |     |     |     |
| Description | Eventreportedwhenport-streamstatechanges |     |     |     |
Event ID: 15705
130
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

Port HW Resources updated on {port_name} on {request_type} with values: classA_ded
{classA_ded} classB_ded {classB_ded} classA_max {classA_max} classB_max {classB_max}

FQTSS

Info

Description

Event reported when stream needs a hardware resource.

Event ID: 15706

Message

Category

Severity

{resource_type} {key} failed during {request_type} with {reason}

FQTSS

Info

Description

Event reported when failure occurs for port or stream entities.

Event ID: 15707

Message

Category

Severity

Stream {stream_id} on port {port_name} failed during {request_type} with {reason}

FQTSS

Info

Description

Event reported when failure occurs for port-stream entities

Forwarding and Queuing for Time-Sensitive Streams (FQTSS) events | 131

|          |                |        |          |        | Chapter | 46     |
| -------- | -------------- | ------ | -------- | ------ | ------- | ------ |
|          |                |        | Hardware | Health | Monitor | events |
| Hardware | Health Monitor | events |          |        |         |        |
Thefollowingaretheeventsrelatedtohardwarehealthmonitor.
| Event ID: | 3001 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message
Diagnostic<test_name>failedwitherrorcode<error_code>onmanagementmodule
<slot>':yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinmanagementmodule
| Event ID: | 3002 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message
Diagnostic<test_name>failedwitherrorcode<error_code>onlinecard<slot>':yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinlinecard
| Event ID: | 3003 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Diagnostic<test_name>failedwitherrorcode<error_code>onfabriccard<slot>':yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinfabriccard
| Event ID: | 3004 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Diagnostic<test_name>failedwitherrorcode<error_code>onfantray<slot>':yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinfantray
| Event ID: | 3005 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
132
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Diagnostic <test_name> failed with error code <error_code> on rear display card <slot>':
yes

Category

Hardware Health Monitor

Severity

Error

Description

Event raised when hardware diagnostics detects error in rear display card

Event ID: 3006

Message

Diagnostic <test_name> failed with error code <error_code> for the system': yes

Category

Hardware Health Monitor

Severity

Error

Description

Event raised when hardware diagnostics detects error in the system

Event ID: 3007

Message

There are <origin> happening on <location>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Logs MCE BUS error

Event ID: 3008

Message

There are IO errors on <location> from <seg>:<bus>:<device>:<function>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Logs MCE IO error

Event ID: 3009

Message

There are unknown errors on <location> from <status>:<addr>:<misc>:<mcgstatus>:<cap>':
yes

Category

Hardware Health Monitor

Severity

Info

Description

Logs MCE unknown error

Event ID: 3010

Hardware Health Monitor events | 133

Message

CPUs <cpus> L<level> <type> cache error detected. CPUs <offlined> offlined': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Logs CPU cache error

Event ID: 3011

Message

Socket <socket> correctable memory error count <cecount> exceeded threshold
<threshold>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when socket correctable memory error count is exceeded threshold

Event ID: 3012

Message

Module <channel> correctable memory error count <cecount> exceeded threshold
<threshold>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when module correctable memory error count is exceeded threshold

Event ID: 3013

Message

Page <page> correctable memory error count <cecount> exceeded threshold <threshold>
and <offlined>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when page correctable memory error count is exceeded threshold

Event ID: 3013

Message

Page <page> correctable memory error count <cecount> exceeded threshold <threshold>
and <offlined>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when page correctable memory error count is exceeded threshold

Event ID: 3014

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

134

Message

Diagnostic {test_name} failed with error code {error_code} on management module {slot}
and report as info

Category

Hardware Health Monitor

Severity

Info

Description

Event raised when hardware diagnostics detects error in management module and
report as inf

Event ID: 3015

Message

Diagnostic {test_name} failed with error code {error_code} on management module {slot}
and report as warning

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in management module and
report as warning

Event ID: 3016

Message

Diagnostic {test_name} failed with error code {error_code} on fabric card {slot} and
report as inf

Category

Hardware Health Monitor

Severity

Info

Description

Event raised when hardware diagnostics detects error in fabric card and report as inf

Event ID: 3017

Message

Diagnostic {test_name} failed with error code {error_code} on fabric card {slot} and
report as warnin

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in fabric card and report as
warning

Event ID: 3018

Message

Diagnostic {test_name} failed with error code {error_code} on line card {slot} and report
as info

Category

Hardware Health Monitor

Severity

Info

Description

Event raised when hardware diagnostics detects error in line card and report as info'

Hardware Health Monitor events | 135

Event ID: 3019

Message

Diagnostic {test_name} failed with error code {error_code} on line card {slot} and report
as warning

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in line card and report as warning

Event ID: 3020

Message

Diagnostic {test_name} failed with error code {error_code} on fan tray {slot} and report
as info

Category

Hardware Health Monitor

Severity

Info

Description

Event raised when hardware diagnostics detects error in fan tray and report as info

Event ID: 3021

Message

Diagnostic {test_name} failed with error code {error_code} on fan tray {slot} and report
as warning

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in fan tray and report as warning

Event ID: 3022

Message

Category

Severity

Diagnostic {test_name} failed with error code {error_code} on chassis {slot}

Hardware Health Monitor

Error

Description

Event raised when hardware diagnostics detects error in fan tray and report as warning

Event ID: 3023

Message

Diagnostic {test_name} failed with error code {error_code} on chassis {slot} and report as
warning

Category

Hardware Health Monitor

Severity

Info

Description

Event raised when hardware diagnostics detects error in chassis and report as info

Event ID: 3024

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

136

Message

Category

Severity

Diagnostic {test_name} failed with error code {error_code} on chassis {slot}

Hardware Health Monitor

Warning

Description

Event raised when hardware diagnostics detects error in chassis and report as warning

Event ID: 13801

Message

HW Fault (Error {error_code}) detected on the switch. {impact_statement}. Contact sup-
port for assistance.

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in Chassis

Event ID: 13802

Message

HW Fault (Error {error_code}) detected on the switch. {impact_statement}. Contact
support for assistance.

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics error detected in the system

Hardware Health Monitor events | 137

Chapter 47
|          |                   | Hardware    | switch | controller | sync events |
| -------- | ----------------- | ----------- | ------ | ---------- | ----------- |
| Hardware | switch controller | sync events |        |            |             |
Thefollowingaretheeventsrelatedtohardwareswitchcontroller.
| Event ID: | 8801 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
HardwareVTEPDBsetupiscompleted
Category Hardwareswitchcontrollersync
Severity Info
Description LogwhenhardwareVTEPDBsetupiscompleted
| Event ID: | 8802 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message PhysicalPort<port>iscreatedinHardwareVTEPDB
Category Hardwareswitchcontrollersync
Severity Info
Description LogwhenphysicalportiscreatedinhardwareVTEPDB
| Event ID: | 8803 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message PhysicalPort<port>isdeletedfromHardwareVTEPDB
Category Hardwareswitchcontrollersync
Severity Info
Description LogwhenphysicalportisdeletedfromhardwareVTEPDB
| Event ID: | 8804 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
HSCconfigurationiscompletedontheswitchandpushedtoHardwareVTEPDB
Category Hardwareswitchcontrollersync
Severity Info
Description LogswhenHSCconfigurationiscompletedontheswitchandpushedtoHardwareVTEP
DB
| Event ID: | 8805 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
138
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

HSC configuration is deleted from the switch and Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Info

Description

Logs when HSC configuration is deleted from the switch and Hardware VTEP DB

Event ID: 8806

Message

Local MAC <mac> learnt on VLAN <vlan> is updated in the Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Info

Description

Logs when local MAC learn on VLAN is updated in the Hardwar VTEP DB

Event ID: 8807

Message

Local MAC <mac> learnt on VLAN <vlan> is removed from the Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Info

Description

Logs when local MAC learnt on VLAN is removed from the Hardware VTEP DB

Event ID: 8808

Message

VXLAN IP <ip> is updated in the Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Info

Description

Logs when VXLAN IP is updated in the Hardware VTEP DB

Event ID: 8809

Message

VXLAN IP <ip> is removed from Switch and Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Info

Event ID: 8810

Message

Unicast Remote MAC <mac> learnt on VNI <vni> is added to the switch

Category

Hardware switch controller sync

Hardware switch controller sync events | 139

Severity

Info

Description

Logs when unicast remote MAC learnt on VNI is added to the switch

Event ID: 8811

Message

Unicast Remote MAC <mac> learnt on VNI <vni> is removed from the switch

Category

Hardware switch controller sync

Severity

Info

Description

Logs when unicast remote MAC learnt on VNI is removed from the switch

Event ID: 8812

Message

Tunnel <ip> is removed from Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Info

Description

Logs when tunnel is removed from Hardware VTEP DB

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

140

Chapter 48

Hot Patch events

Hot Patch events

The following are the events related to Hot Patch updates.

Event ID: 13201

Message

Hot-patch {patch_name} will be disabled upon reboot.

Category

Hot Patch

Severity

LOG_INFO

Description

Logs a message for the user to reboot the system in order to deactivate patch

Event ID: 13202

Message

Hot-patch {patch_name} added.

Category

Hot Patch

Severity

LOG_INFO

Description

New hot-patch file was detected.

-Event ID: 13203

Message

Hot-patch {patch_name} successfully applied.

Category

Hot Patch

Severity

LOG_INFO

Description

Hot-patch was applied to running system software.

Event ID: 13204

Message

Category

Severity

Hot-patch {patch_name} removed.

Hot Patch

LOG_INFO

Description

Hot-patch file deleted.

Event ID: 13205

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

141

Message

Hot-patch {patch_name} config mismatch, patch applied.

Category

Hot Patch

Severity

LOG_WARN

Description

Hot-patch config and filesystem do not agree.

Event ID: 13206

Message

Hot-patch {patch_name} is missing.

Category

Hot Patch

Severity

LOG_WARN

Description

Hot-patch is not found on the filesystem.

Event ID: 13207

Message

Hot-patch {patch_name} verification failed.

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch failed file verification.

Event ID: 13208

Message

Hot-patch {patch_name} failed to apply'

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch failed to apply to all required components.

Event ID: 13209

Message

Hot-patch {patch_name} image signature not valid.

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that a the signature verification check during a hot-patch download failed

Event ID: 13210

Message

Hot-patch {patch_name} image is not compatible with hardware.

Hot Patch events | 142

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that the hot-patch image downloaded is not compatible with hardware

Event ID: 13211

Message

Hot-patch {patch_name} image is not compatible with software.

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that the hot-patch image downloaded is not compatible with the current
software version

Event ID: 13212

Message

Hot-patch {patch_name} is invalid'

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that the hot-patch file downloaded for is not a valid image' event_description_
template:

Event ID: 13213

Message

Hot-patch {patch_name} was modified after it was parsed'

Category

Hot Patch

Severity

LOG_WARN

Description

Indicates that the hot-patch file was modified after parsing

Event ID: 13214

Message

Not enough disk space available to install hot-patch {patch_name}.

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that the hot-patch file could not be installed due to low disk space

Event ID: 13215

Message

Not enough memory available to install hot-patch {patch_name}'

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

143

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that the hot-patch file could not be installed due to low memory

Event ID: 13216

Message

Indicates that hot-patch install timed out.

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch {patch_name} install timed out.

Event ID: 13217

Message

Hot-patch {patch_name} could not be installed because a newer hot-patch has been, or
will be, installed'

Category

Hot Patch

Severity

LOG_WARN

Description

Indicates that the hot-patch file could not be installed because a newer hot-patch has
been, or will be, installed

Event ID: 13218

Message

Hot-patch {patch_name} could not be installed because another patch that is configured
to be installed has the same timestamp.

Category

Hot Patch

Severity

LOG_WARN

Description

Indicates that the hot-patch file could not be installed because another patch that is
configured to be installed has the same timestamp

Event ID: 13219

Message

Hot-patch {patch_name} verification timed out after {time_out} seconds.

Category

Hot Patch

Severity

LOG_ERR

Description

Indicates that hot-patch verification timed out.

Event ID: 13220

Hot Patch events | 144

Message

Hot-patch {patch_name} is applying.

Category

Hot Patch

Severity

LOG_INFO

Description

Indicates that a hot-patch is currently being applied.

Event ID: 13221

Message

Hot-patch {patch_name} is unapplying.

Category

Hot Patch

Severity

LOG_INFO

Description

Indicates that a hot-patch is currently being unapplied.

Event ID: 13222

Message

Hot-patch {patch_name} is not applied.

Category

Hot Patch

Severity

LOG_INFO

Description

Hot-patch unapplied on running system software.

Event ID: 13223

Message

Hot-patch {patch_name} failed to unapply. Reboot recommended.

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch failed to unapply on all required components.

Event ID: 13224

Message

Hot-patch {patch_name} failed to download'

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch failed to download.

Event ID: 13224

Message

Hot-patch {patch_name} failed to download'

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

145

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch failed to download.

Event ID: 13224

Message

Hot-patch {patch_name} failed to download'

Category

Hot Patch

Severity

LOG_ERR

Description

Hot-patch failed to download.

Event ID: 13225

Message

Hot-patch {patch_name} downloaded successfully'

Category

Hot Patch

Severity

LOG_INFO

Description

Hot-patch downloaded successfully.

Event ID: 13226

Message

Attempt to Hot-Patch {patch_name} on {ss_type}_{ss_name} at boot : "{status}"'

Category

Hot Patch

Severity

LOG_INFO

Description

Status of the Hot-patch attempted to be applied at boot

Hot Patch events | 146

Chapter 49

HTTPS Server events

HTTPS Server events

The following are the events related to HTTPS server.

Event ID: 5601

Message

User <user> has enabled <mode> for REST mode

Category

HTTPS Server

Severity

Information

Description

Logs a message when a user changes the status of the REST mode

Event ID: 5602

Message

User <user> has <status> HTTPS Server on VRF <vrf>

Category

HTTPS Server

Severity

Information

Description

Logs a message when a user enables/disables the https-server VRF configuration

Event ID: 5603

Message

User <user> closed all HTTPS sessions

Category

HTTPS Server

Severity

Information

Description

Logs a message when a user closes all HTTPS sessions

Event ID: 5604

Message

User <user> changed the HTTPS Server max user sessions amount to <sessions>

Category

HTTPS Server

Severity

Information

Description

Logs a message when a user changes the maximum amount of sessions per user

Event ID: 5605

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

147

Message User<user>changedtheHTTPSServeridletimeoutto<timeout>
| Category | HTTPSServer |     |
| -------- | ----------- | --- |
| Severity | Information |     |
Description Logsamessagewhenauserchangesthevalueofthesessionidletimeout
| Inband | Flow Analyzer | (IFA) events |
| ------ | ------------- | ------------ |
ThefollowingaretheeventsrelatedtoInbandFlowAnalyzer(IFA).
| Event ID: | 16401 |     |
| --------- | ----- | --- |
Message HONOR_MODE:InbandFlowAnalyzerisoperatingwithoutavalidfeaturepack.
| Category | IFA  |     |
| -------- | ---- | --- |
| Severity | INFO |     |
Description LogeventtoindicatethatInbandFlowAnalyzerfeatureisoperatingwithoutavalidfeature
pack
EventID:16402
Message STRICT_MODE:InbandFlowAnalyzerisblockedduetoinvalidormissingfeaturepack.
| Category | IFA  |     |
| -------- | ---- | --- |
| Severity | INFO |     |
Description LogeventtoindicatethatInbandFlowAnalyzerfeatureisblockedduetoinvalidormissing
featurepack
| Event ID: | 16403 |     |
| --------- | ----- | --- |
Message ACTIVE_MODE:InbandFlowAnalyzerisoperatingwithavalidfeaturepack.
| Category | IFA  |     |
| -------- | ---- | --- |
| Severity | INFO |     |
Description LogeventtoindicatethatInbandFlowAnalyzerfeatureisoperationalforavalidfeaturepack
| Event ID: | 16404 |     |
| --------- | ----- | --- |
Message InbandFlowAnalyzerInitiatormonitor{monitor_name}configurationisbeingappliedon
{context}for{ip_version}version.
| Category | IFA  |     |
| -------- | ---- | --- |
| Severity | INFO |     |
Description LogeventtoindicatethatanInbandFlowAnalyzerinitiatormonitorconfigisbeingapplied
InbandFlowAnalyzer(IFA)events|148

Event ID: 16405

Message

Inband Flow Analyzer {monitor_type} monitor for ip-all configuration is being applied.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer transit or terminator monitor config is being
applied

Event ID: 16406

Message

Inband Flow Analyzer Initiator monitor {monitor_name} is active on {context} for {ip_version}
version.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer initiator monitor is active

Event ID: 16407

Message

Inband Flow Analyzer {monitor_type} monitor is active for ip-all.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer transit or terminator monitor is active

Event ID: 16408

Message

Category

Severity

{error_type} Inband Flow Analyzer Initiator monitor {monitor_name} configuration failed to
apply on {context} for {ip_version} version, with reason {reason}.

IFA

ERR

Description

Log event to indicate that an Inband Flow Analyzer initiator monitor config failed

Event ID: 16409

Message

Category

Severity

{error_type} Inband Flow Analyzer {monitor_type} monitor configuration failed to apply for ip-
all, with reason {reason}.

IFA

ERR

Description

Log event to indicate that an Inband Flow Analyzer transit or terminator monitor config failed

Event ID: 16410

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

149

Message

Inband Flow Analyzer Initiator monitor {monitor_name} on {context} for {ip_version} version
destroy started.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer initiator monitor destroy started

Event ID: 16411

Message

Inband Flow Analyzer {monitor_type} monitor for ip-all destroy started.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer transit or terminator monitor destroy
started

Event ID: 16412

Message

Inband Flow Analyzer Initiator monitor {monitor_name} on {context} for {ip_version} version
destroy completed.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer initiator monitor destroy completed

Event ID: 16413

Message

Inband Flow Analyzer {monitor_type} monitor for ip-all destroy completed.

Category

IFA

Severity

INFO

Description

Log event to indicate that an Inband Flow Analyzer transit or terminator monitor destroy
completed

Event ID: 16414

Message

Inband Flow Analyzer {name} set to {value}.

Category

Severity

IFA

INFO

Description

Log event to indicate that an Inband Flow Analyzer setting value has been configured

Event ID: 16415

Inband Flow Analyzer (IFA) events | 150

Message

{error_type} Inband Flow Analyzer {name} failed to set value to {value} due to reason {reason}.

Category

Severity

IFA

ERR

Description

Log event to indicate that an Inband Flow Analyzer setting value failed to be configured

Event ID: 16416

Message

Category

Severity

Inband Flow Analyzer TOD sync started.

IFA

INFO

Description

Log event to indicate that Inband Flow Analyzer TOD sync started

Event ID: 16417

Message

Category

Severity

Inband Flow Analyzer TOD sync stopped.

IFA

INFO

Description

Log event to indicate that Inband Flow Analyzer TOD sync stopped

Event ID: 16418

Message

Category

Severity

Inband Flow Analyzer RX thread failed to start.

IFA

Error

Description

Logs event to indicate that Inband Flow Analyzer RX thread failed to start

Event ID: 16419

Message

Category

Severity

Inband Flow Analyzer RX thread failed to stop.

IFA

Error

Description

Log event to indicate that Inband Flow Analyzer RX thread failed to stop.

Event ID: 16420

Message

Inband Flow Analyzer add packet sniffer failed.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

151

Category

Severity

IFA

Error

Description

Logs event to indicate that Inband Flow Analyzer add packet sniffer failed.

Event ID: 16421

Message

Category

Severity

Description

Event ID: 16422

Message

Category

Severity

{error_type} Inband Flow Analyzer Initiator monitor "{monitor_name}" on {context} for {ip_
version} version, encountered an error on state {state}.

IFA

Error

Logs event to indicate that an Inband Flow Analyzer initiator monitor failed at a given
state.

{error_type} Inband Flow Analyzer {monitor_type} monitor, encountered an error on state
{state}

IFA

Error

Description

Logs event to indicate that an Inband Flow Analyzer monitor failed at a given state.

Inband Flow Analyzer (IFA) events | 152

Chapter 50

Injected Views

Injected Views

The following are the events related to injected views.

Event ID: 15801

Message

Category

Severity

Injected view {name} was loaded

Injected Views

Info

Description

Event reported when an injected view is loaded

Event ID: 15802

Message

Category

Severity

Injected view {name} was unloaded

Injected Views

Info

Description

Event reported when an injected view is unloaded

Event ID: 15803

Message

Category

Severity

Injected view {name} is in a failed state

Injected Views

Info

Description

Event reported when an injected view is in failed state

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

153

Chapter 51
|           |             |        | In-System | Programming | events |
| --------- | ----------- | ------ | --------- | ----------- | ------ |
| In-System | Programming | events |           |             |        |
Thefollowingaretheeventsrelatedtoin-systemprogramming.
| Event ID: | 7200 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Internalfatalerrorat<file>:<line>
Category In-SystemProgramming
Severity Error
Description ISPinternalfatalerror
| Event ID: | 7210 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Non-failsafeupdateneededfor<devspec>.Pleaseruntheallow-unsafe-updates
command
Category In-SystemProgramming
Severity Error
Description Anon-failsafedeviceupdateisneeded,buttheallow-unsafe-updatescommandhasnot
yetbeenrun
| Event ID: | 7211 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Donotinterruptnon-failsafeupdatefor<devspec>
Category In-SystemProgramming
Severity Error
Description Anon-failsafedeviceupdateisabouttostart,sodonotinterruptit
| Event ID: | 7212 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Startingupdatefor<devspec>fromversion<fromver>toversion<tover>
Category In-SystemProgramming
Severity Information
Description Adeviceupdateisabouttostart
| Event ID: | 7213 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
154
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Update successful for <devspec> from version <fromver> to version <tover>

Category

In-System Programming

Severity

Information

Description

A device update was successful or in some cases was successfully arranged to be
performed later

Event ID: 7214

Message

Update failed for <devspec>

Category

In-System Programming

Severity

Critical

Description

A device update failed

Event ID: 7215

Message

Deferred update for <devspec> will be performed after an automatic module reset

Category

In-System Programming

Severity

Information

Description

A device update was postponed until after an automatic reset of its module

Event ID: 7216

Message

Approximately <time> minute(s) remaining to update <numdevs> device(s) on <modspec>

Category

In-System Programming

Severity

Information

Description

Indicates the approximate remaining update time for a module

Event ID: 7217

Message

Insufficient redundant power is available to update <devspec>

Category

In-System Programming

Severity

Information

Description

Unable to update non-redundant power supply

Event ID: 7218

Message

Programmable device updates are pending that require a power cycle. Wait for all fabric

In-System Programming events | 155

and line modules to be ready, then power the system off and back on again

Category

In-System Programming

Severity

Information

Description

ISP needs the chassis power-cycled manually when it cannot be done automatically

Event ID: 7219

Message

Failed to write-protect <devspec> (pass <pass>)

Category

In-System Programming

Severity

Critical

Description

Failed to write-protect a module or device

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

156

Chapter 52
|           |               | Interface  | and Interface | Diagnostic | events |
| --------- | ------------- | ---------- | ------------- | ---------- | ------ |
| Interface | and Interface | Diagnostic | events        |            |        |
Thefollowingaretheeventsrelatedtointerface.
| Event ID: | 401 |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
Message
Interfaceport_adminsettoupfor<interface>interface
| Category    | Interface                                           |     |     |     |     |
| ----------- | --------------------------------------------------- | --- | --- | --- | --- |
| Severity    | Info                                                |     |     |     |     |
| Description | Logwheninterfaceport_adminsettoup                   |     |     |     |     |
| Event ID:   | 402                                                 |     |     |     |     |
| Message     | Interfaceport_adminsettodownfor<interface>interface |     |     |     |     |
| Category    | Interface                                           |     |     |     |     |
| Severity    | Info                                                |     |     |     |     |
| Description | Logwheninterfaceport_adminsettodown                 |     |     |     |     |
| Event ID:   | 403                                                 |     |     |     |     |
| Message     | Linkstatusforinterface{interface}is{state}          |     |     |     |     |
| Category    | Interface                                           |     |     |     |     |
| Severity    | Info                                                |     |     |     |     |
| Description | Logwheninterfacelinkstatusisup                      |     |     |     |     |
| Event ID:   | 404                                                 |     |     |     |     |
Message
Linkstatusforinterface{interface}is{state}
| Category    | Interface                        |     |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- | --- |
| Severity    | Info                             |     |     |     |     |
| Description | Logwheninterfacelinkstatusisdown |     |     |     |     |
| Event ID:   | 405                              |     |     |     |     |
157
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Reserved for future use

Category

Interface

Severity

Error

Event ID: 406

Message

Interface <interface> encountered a hardware error that caused a link reset

Category

Interface

Severity

Info

Description

Log when interface encountered an error that requires user intervention

Event ID: 407

Message

Interface <interface> downshifted to speed <port_speed> Mbps because link attempt
failed at higher speed.

Category

Interface

Severity

Info

Description

Log when interface encountered a downshift

Event ID: 408

Message

Category

Severity

Interface <interface> is down because MACsec and PFC features are mutually exclusive.

Interface

Warning

Description

Log when interface is down due to incompatible MACsec and PFC configuration

Event ID: 409

Message

Interface {interface} link reset ignored. {count} total link resets ignored for this interface

Category

Interface

Severity

Info

Description

Log when interface ignores a link reset'

Event ID: 410

Message

Interface {interface} cannot be enabled due to invalid configurationLogged when the
current profile does not support splitting

Interface and Interface Diagnostic events | 158

Category

Severity

Description

Event ID: 411

Message

Category

Severity

Interface

Warning

Logged when the interface cannot be enabled due to a configuration setting that is
incompatible with hardware

Logged when the current profile does not support splitting

Interface

Warning

Description

Logged when the current profile does not support splitting

Event ID: 14201

Message

Interface {interface}: unable to run cable diagnostic on VSF port

Category

Interface

Severity

Error

Description

Cable diagnostic test is unable to run on VSF port.

Event ID: 14202

Message

Interface {interface}: unable to run cable diagnostic on unsupported port.

Category

Interface

Severity

Error

Description

Cable diagnostic test is unable to run on unsupported port.

Event ID: 14203

Message

Interface {interface}: unable to run cable diagnostic when another diagnostic test is in
progress.

Category

Interface

Severity

Error

Description

Cable diagnostic test is unable to run due to another ongoing diagnostic test

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

159

Chapter 53

Internal storage events

Internal storage events

The following are the events related to internal storage.

Event ID: 9101

Message

Failed to report storage <name> details for module <module_num>. Error: <error>': yes

Category

Internal storage

Severity

Error

Description

Event raised when there is a storage reporting failure

Event ID: 9102

Message

Storage <name> health alert. Endurance utilization at <usage>% in module <module_
num>': yes

Category

Internal storage

Severity

Information

Description

Event raised when the storage health deteriorates

Event ID: 9103

Message

Storage <name> endurance utilization at <usage>% in module <module_num>': yes

Category

Internal storage

Severity

Information

Description

Event raised when there is a change in storage endurance

Event ID: 9104

Message

Storage <name> health alert. Endurance utilization at <usage>% in module <module_num>.
Failure is imminent. Please backup data': yes

Category

Internal storage

Severity

Error

Description

Event raised when storage failure is imminent

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

160

IP Flow Information Export events

Chapter 54

IP Flow Information Export events

The following are the events related to IP Flow Information Export (IPFIX).

Event ID: 15401

Message

Category

Severity

Description

Failed to enable the delivery of IPFIX flow telemetry packets to the CPU.

IPFIX

Error

Event raised when there is a failure to enable the delivery of IPFIX flow telemetry packets
to the CPU.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

161

Chapter 55
|                    | IP Flow       | Monitoring | Advertisement | events |
| ------------------ | ------------- | ---------- | ------------- | ------ |
| IP Flow Monitoring | Advertisement | events     |               |        |
ThefollowingaretheeventsrelatedtoIPFlowMonitoring(IPFM).
Event ID: 15101
| Message  | FlowTrackingfeaturehasbeen{status} |     |     |     |
| -------- | ---------------------------------- | --- | --- | --- |
| Category | IPFlowMonitoring                   |     |     |     |
| Severity | Info                               |     |     |     |
Description LogeventthatindicatesglobalconfigurationforFlowTrackingfeature
Event ID: 15102
| Message     | Linecard{node_id}is{status} |     |     |     |
| ----------- | --------------------------- | --- | --- | --- |
| Category    | IPFlowMonitoring            |     |     |     |
| Severity    | Info                        |     |     |     |
| Description | linecardupevent             |     |     |     |
Event ID: 15103
| Message     | BULKSYNCeventreceivedfromlinecard{name} |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Category    | IPFlowMonitoring                        |     |     |     |
| Severity    | Info                                    |     |     |     |
| Description | Bulksynceventreceived                   |     |     |     |
Event ID: 15104
| Message     | BULKSYNCALLrequestsenttoallLC |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Category    | IPFlowMonitoring              |     |     |     |
| Severity    | Info                          |     |     |     |
| Description | bulksyncalleventsent!         |     |     |     |
Event ID: 15105
162
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

IPFMD Publisher is {status}

IP Flow Monitoring

Info

Description

IPFMD Publisher status

Event ID: 15106

Message

Category

Severity

FLUSH timer on LC {node_id} is {status}.

IP Flow Monitoring

Info

Description

flush timer start/expire status!

Event ID: 15107

Message

Category

Severity

IP Flow table utilization has exceeded high threshold on linecard {name}.

IP Flow Monitoring

Info

Description

IP Flow table utilization reached high threshold on a LC

Event ID: 15108

Message

Category

Severity

IP Flow table utilization back to lower threshold on linecard {node_id}

IP Flow Monitoring

Info

Description

IP Flow table utilization back to lower threshold on a LC

IP Flow Monitoring Advertisement events | 163

Chapter 56
|           |          |        | IP source | lockdown | events |
| --------- | -------- | ------ | --------- | -------- | ------ |
| IP source | lockdown | events |           |          |        |
ThefollowingaretheeventsrelatedtoIPsourcelockdown.
| Event ID: | 9801 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
IPsource-lockdownresourceutilizationhasreached80percentofthesupportedlimitof
<max_supported_limit>onthesystem
| Category |     | IPsourcelockdown |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Warning          |     |     |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
reached80percentofthesupportedlimits
| Event ID: | 9802 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message IPsource-lockdownresourceutilizationhasexceededmaximumsupportedlimitof<max_
supported_limit>onthesystem.IPsource-lockdownfunctionalitywillnotworkfornew
entries
| Category |     | IPsourcelockdown |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Critical         |     |     |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
exceededthesupportedlimits
| Event ID: | 9803 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message IPsource-lockdownresourceutilizationhasreducedbelow80percentofthesupported
limitof<max_supported_limit>onthesystem
| Category |     | IPsourcelockdown |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Information      |     |     |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
reducedbelow80percentofthesupportedlimits
| Event ID: | 9804 |                                                    |     |     |     |
| --------- | ---- | -------------------------------------------------- | --- | --- | --- |
| Message   |      | IPv4source-lockdownisenabledoninterface<interface> |     |     |     |
| Category  |      | IPsourcelockdown                                   |     |     |     |
164
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Severity

Information

Description

Log event when IPV4_SOURCE_LOCKDOWN is enabled on an interface

Event ID: 9805

Message

IPv4 source-lockdown is disabled on interface <interface>

Category

IP source lockdown

Severity

Information

Description

Log event when IPV4_SOURCE_LOCKDOWN is disabled on an interface

Event ID: 9806

Message

IPv6 source-lockdown is enabled on interface <interface>

Category

IP source lockdown

Severity

Information

Description

Log event when IPV6_SOURCE_LOCKDOWN is enabled on an interface

Event ID: 9807

Message

IPv6 source-lockdown is disabled on interface <interface>

Category

IP source lockdown

Severity

Information

Description

Log event when IPV6_SOURCE_LOCKDOWN is disabled on an interface

IP source lockdown events | 165

Chapter 57

IP tunnels events

IP tunnels events

The following are the events related to IP tunnels.

Event ID: 9601

Message

Tunnel Creation Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_ip>)
Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel creation fails

Event ID: 9602

Message

Tunnel Created - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_ip>)
Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel created

Event ID: 9603

Message

Tunnel Deletion Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_ip>)
Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel deletion failed

Event ID: 9604

Message

Tunnel Deleted - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_ip>)
Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel deleted

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

166

Event ID: 9605

Message

Tunnel Modification Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_
ip>) Remote IP (<dst_ip>) TTL (<ttl>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel modification failed

Event ID: 9606

Message

Tunnel Source IP Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_
ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel source ip modified

Event ID: 9607

Message

Tunnel Destination IP Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP
(<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel destination ip modified

Event ID: 9608

Message

Tunnel TTL Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_ip>)
Remote IP (<dst_ip>) TTL (<ttl>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel TTL modified

Event ID: 9609

Message

Tunnel MTU Modification Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP
(<src_ip>) Remote IP (<dst_ip>) MTU (<ip_mtu>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel mtu modification failed

IP tunnels events | 167

Event ID: 9610

Message

Tunnel MTU Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_ip>)
Remote IP (<dst_ip>) MTU (<ip_mtu>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel mtu modified

Event ID: 9611

Message

Tunnel Nexthop Add Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP
(<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel nexthop add failed

Event ID: 9612

Message

Tunnel Nexthop Added - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_
ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets added

Event ID: 9613

Message

Tunnel Nexthop Modify Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP
(<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel nexthop modify failed

Event ID: 9614

Message

Tunnel Nexthop Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_
ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets modified

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

168

Event ID: 9615

Message

Tunnel Nexthop Delete Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP
(<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel nexthop delete failed

Event ID: 9616

Message

Tunnel Nexthop Deleted - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local IP (<src_
ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets deleted

IP tunnels events | 169

Chapter 58

IP-SLA events

IP-SLA events

The following are the events related to IP-SLA.

Event ID: 7401

Message

Category

Severity

IP-SLA session:<name> state changed to failed <state> due to reason <reason>

IP-SLA

Error

Description

Event raised when an IP-SLA session state is changed to any failed state

Event ID: 7402

Message

IP-SLA session:<name> state changed to <state> due to reason <reason>

Category

IP-SLA

Severity

Information

Description

Event raised when an IP-SLA session state is changed to any info state

Event ID: 7403

Message

IP-SLA <name>: <operation>

Category

IP-SLA

Severity

Information

Description

Event raised when an IP-SLA session is added or deleted

Event ID: 7404

Message

Category

Severity

IP-SLA session:<name> is incomplete to schedule

IP-SLA

Error

Description

Event raised when an IP-SLA incomple config is added

Event ID: 7405

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

170

Message

Category

Severity

IP-SLA session:<name> interface <interface> is not ready and SLA is disabled

IP-SLA

Error

Description

Event raised when an IP-SLA session stopped due to source IP or interface changes

Event ID: 7406

Message

Category

Severity

IP-SLA session:<name> interface <interface> is ready and SLA is enabled

IP-SLA

Error

Description

Event raised when an IP-SLA session started due to source IP or interface changes

Event ID: 7407

Message

Category

Severity

IP-SLA session:<name> failed to bind source, reason:<reason>

IP-SLA

Error

Description

Event raised when an IP-SLA session failed to bind source

Event ID: 7408

Message

Category

Severity

IP-SLA session:<name> failed to initialize socket, reason:<reason>

IP-SLA

Error

Description

Event raised when an IP-SLA session failed to initialize socket

IP-SLA events | 171

Chapter 59

IPSec tunnel offload events

IPSec tunnel offload events

The following are the events related to IPSec tunnel offload states.

Event ID: 14801

Message

Category

Severity

PSec tunnel is UP - Tunnel Id ({tunnel_id})

IPSEC_TUNNEL_OFFLOAD

Info

Description

Event raised when IPSec tunnel state is up

Event ID: 14802

Message

Category

Severity

IPSec tunnel is DOWN - Tunnel Id ({tunnel_id})

IPSEC_TUNNEL_OFFLOAD

Info

Description

Event raised when IPSec tunnel state is down

Event ID: 14803

Message

Category

Severity

IPSec Tunnel is down due to VSX passive mode - Tunnel ({tunnel_id})

IPSEC_TUNNEL_OFFLOAD

Info

Description

Event raised when IPSec tunnel state is down due to VSX passive mode

Event ID: 14804

Message

Route {prefix} is in no_hw_resource with nexthop as IPSec tunnel{tunnel_id} on vrf {vrf_
name}.

Category

IPSEC_TUNNEL_OFFLOAD

Severity

Error

Description

Event to indicate the IPSec Route which is in no_hw_resource state.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

172

Chapter 60
|             |               |        | IPv6 Router | Advertisement | events |
| ----------- | ------------- | ------ | ----------- | ------------- | ------ |
| IPv6 Router | Advertisement | events |             |               |        |
ThefollowingaretheeventsrelatedtoIPv6routeradvertisement.
| Event ID: 3901 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
Message
ipv6raenabledoninterface:<intf>
| Category       | IPv6RouterAdvertisement          |     |     |     |     |
| -------------- | -------------------------------- | --- | --- | --- | --- |
| Severity       | Information                      |     |     |     |     |
| Description    | Eventraisedwhenipv6raenabled     |     |     |     |     |
| Event ID: 3902 |                                  |     |     |     |     |
| Message        | ipv6radisabledoninterface:<intf> |     |     |     |     |
| Category       | IPv6RouterAdvertisement          |     |     |     |     |
| Severity       | Information                      |     |     |     |     |
| Description    | Eventraisedwhenipv6radisabled    |     |     |     |     |
| Event ID: 3903 |                                  |     |     |     |     |
Message DisabledsendingMTUinRouter-Advertisementmessageson<intf>
| Category       | IPv6RouterAdvertisement                      |     |     |     |     |
| -------------- | -------------------------------------------- | --- | --- | --- | --- |
| Severity       | Information                                  |     |     |     |     |
| Description    | Eventraisedwhenipv6rasuppressmtuisconfigured |     |     |     |     |
| Event ID: 3904 |                                              |     |     |     |     |
Message
EnabledsendingMTUinRouter-Advertisementmessageson<intf>
| Category       | IPv6RouterAdvertisement                    |     |     |     |     |
| -------------- | ------------------------------------------ | --- | --- | --- | --- |
| Severity       | Information                                |     |     |     |     |
| Description    | Eventraisedwhenipv6rasuppressmtuconfigured |     |     |     |     |
| Event ID: 3905 |                                            |     |     |     |     |
173
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Disabled sending RDNSS in Router-Advertisement messages on <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 ra suppress rdnss is configured

Event ID: 3906

Message

Enabled sending RDNSS in Router-Advertisement messages on <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 ra suppress rdnss is removed

Event ID: 3907

Message

Disabled sending DNSSL in Router-Advertisement messages on <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 ra suppress dnssl is configured

Event ID: 3908

Message

Enabled sending DNSSL in Router-Advertisement messages on <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 ra suppress dnssl is removed

Event ID: 3909

Message

Interface: <intf> is added to router discovery

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 ra interface is added

Event ID: 3910

Message

Interface: <intf> is deleted from router discovery

IPv6 Router Advertisement events | 174

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 ra interface is deleted

Event ID: 3911

Message

Added ipv6 prefix: <ipv6_addr>/<prefixlen> on interface: <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 address is added on interface

Event ID: 3912

Message

Deleted ipv6 prefix: <ipv6_addr>/<prefixlen> from interface: <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 address is deleted from interface

Event ID: 3913

Message

Added RA Prefix: <prefix> on interface: <intf> to prefix list

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RA Prefix is added on interface

Event ID: 3914

Message

Deleted RA Prefix: <prefix> on interface: <intf> from prefix list

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RA Prefix is deleted from interface

Event ID: 3915

Message

default prefix is configured on interface <intf>

Category

IPv6 Router Advertisement

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

175

Severity

Information

Description

Event raised when default prefix is configured

Event ID: 3916

Message

RDNSS is added on interface: <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RDNSS is added

Event ID: 3917

Message

RDNSS is deleted on interface: <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RDNSS is deleted

Event ID: 3918

Message

DNSSL is added on interface: <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when DNSSL is added

Event ID: 3919

Message

DNSSL is deleted on interface: <intf>

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when DNSSL is deleted

Event ID: 3920

Message

Added RA Route: <route> on interface: <intf> to route list

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RA Route is added on interface

IPv6 Router Advertisement events | 176

Event ID: 3921

Message

Deleted RA Route: <route> on interface: <intf> from route list

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RA Route is deleted from interface

Event ID: 3922

Message

Interface: <intf> has been configured with the invalid IPv6 nd ra maxInterval or
minInterval

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 nd ra maxInterval or minInterval is improper

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

177

Chapter 61

IRDP events

IRDP events

The following are the events related to IRDP.

Event ID: 3501

Message

IRDP enabled on interface <interface>

Category

IRDP

Severity

Information

Description

This command enables the IRDP (ICMP Router Discovery Protocol) feature on interface.

Event ID: 3502

Message

IRDP disabled on interface <interface>

Category

IRDP

Severity

Information

Description

This command disables the IRDP (ICMP Router Discovery Protocol) feature on interface.

Event ID: 3503

Message

Interface: <interface> has been configured with the invalid irdp holdtime or minInterval or
maxInterval

Category

IRDP

Severity

Information

Description

Event raised when irdp holdtime or maxInterval or minInterval is improper

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

178

Chapter 62

ISSU events

ISSU events

The following are the events related to In-Service Software Upgrade (ISSU) actions.

Event ID: 13501

Message

Severity

Category

{action} in-service software upgrade to {location} operating system image {version}'

INFO

ISSU

Description

Event to indicate ISSU has started or completed'

Event ID: 13502

Message

Severity

Category

In-service software upgrade started operation {operation}' ISSU_ERROR

INFO

ISSU

Description

Event to indicate progress of ISSU'

Event ID: 13503

Message

Severity

Category

{error_type} during ISSU operation {operation}'

CRIT

ISSU

Description

A critical error occurred during ISSU'

Event ID: 13504

Message

Severity

Category

ISSU {condition}: {reason_message}'

CRIT

ISSU

Description

Indicates the reason ISSU aborted or failed'

Event ID: 13505

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

179

Message

Severity

ISSU {condition}: Feature "{feature}" not ready: {not_ready_reason}'

CRIT , not_ready_reason

Category

ISSU

Description

Indicates ISSU was aborted due to a feature not being ready'

Event ID: 13506

Message

Severity

Category

ISSU {condition}: Feature "{feature}" failed to prepare for ISSU'

CRIT

ISSU

Description

Indicates ISSU was aborted due to a feature failing to prepare for ISSU'

Event ID: 13507

Message

Severity

Category

ISSU rollback timer has been started, {wait_time} minutes remaining before reboot'

INFO

ISSU

Description

Indicates ISSU rollback timer has been started'

Event ID: 13508

Message

Severity

Category

ISSU rollback timer is running, {wait_time} minutes remaining before reboot'

INFO

ISSU

Description

Indicates ISSU rollback timer is running'

Event ID: 13509

Message

Severity

ISSU has been accepted, the rollback timer has been stopped'

INFO

Description

Indicates last ISSU was accepted, and rollback timer will stop'

Category

ISSU

Event ID: 13510

Message

'ISSU rollback timer expired, booting system to previous software version

ISSU events | 180

Severity

Category

Description

Event ID: 13511

Message

Severity

Category

INFO

ISSU

Indicates ISSU rollback timer expired and the system will boot to previous software
version'

'ISSU rollback timer expired. WARNING: previous software version {previous_software_
version} was not found, booting system to active bank {active_bank} with {new_software_
version} software version. This may cause issues with the current configuration'

INFO

ISSU

Description

'Indicates ISSU rollback timer expired and the system boot to new software version'

Event ID: 13512

Message

Severity

Category

ISSU rollback timer has been recreated, {wait_time} minutes remaining before reboot.'

INFO

ISSU

Description

Indicates ISSU rollback timer is running after an ISSUd restart'

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

181

Chapter 63

Job scheduler events

Job scheduler events

The following are the events related to job scheduler.

Event ID: 12201

Message

Creating schedule <name>, trigger time(s): <start_datetime><details>

Category

Job scheduler (SCHEDULE)

Severity

Info

Description

Event reported when a schedule is created

Event ID: 12202

Message

Schedule <name> triggered, trigger_count: <trigger_count>

Category

Job scheduler (SCHEDULE)

Severity

Info

Description

Event reported when a schedule triggers

Event ID: 12203

Message

Timezone changed. Re-creating schedule <name>, trigger time(s): <start_
datetime><details>

Category

Job scheduler (SCHEDULE)

Severity

Info

Description

Event reported when the schedules are recreated due to timezone change.

Event ID: 13701

Message

Starting Job {job_name} due to Schedule {schedule_name}'s trigger

Category

Job scheduler (JOB)

Severity

Info

Description

Event reported when a job is executed

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

182

|          |          |        |          | Chapter  | 64     |
| -------- | -------- | ------ | -------- | -------- | ------ |
|          |          |        | L3 Encap | capacity | events |
| L3 Encap | capacity | events |          |          |        |
ThefollowingaretheeventsrelatedtoL3Encapcapacity.
| Event ID: | 10601 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message
L3resourcescriticalforneighborandrouteforwardingarelow.Used:<encaps_allocated>,
Available:<encaps_free>
| Category |     | L3Encapcapacity |     |     |     |
| -------- | --- | --------------- | --- | --- | --- |
| Severity |     | Warning         |     |     |     |
Description L3resourcesneededforneighborandrouteforwardingarerunninglow.Large-scale
neighbormovescouldcausetrafficloss.
| Event ID: | 10602 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message L3resourcescriticalforneighborandrouteforwardingareatsafelevels.Used:<encaps_
allocated>,Available:<encaps_free>
| Category |     | L3Encapcapacity |     |     |     |
| -------- | --- | --------------- | --- | --- | --- |
| Severity |     | Information     |     |     |     |
Description L3resourcesneededforneighborandrouteforwardingarebacktoasafelevel.
| Event ID: | 10603 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message OutofL3resourcescriticalforneighborandrouteforwarding.Used:<encaps_allocated>,
Available:<encaps_free>
| Category |     | L3Encapcapacity |     |     |     |
| -------- | --- | --------------- | --- | --- | --- |
| Severity |     | Error           |     |     |     |
Description L3resourcesneededforneighborandrouteforwardinghaverunout.Trafficlossis
imminent.
183
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 65
|             |         |        | L3 Resource | Manager | events |
| ----------- | ------- | ------ | ----------- | ------- | ------ |
| L3 Resource | Manager | events |             |         |        |
ThefollowingaretheeventsrelatedtoL3ResourceManager.
| Event ID: 11501 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message
IPv6routeprefix{prefix}isrecommendedfortransitnetworkuseonly.Thetrafficwould
besoftwarerouted.Routingperformancetolocaldestinationaddressesonthisnetwork
maybeimpacted.
| Category        | L3ResourceManager                   |     |     |     |     |
| --------------- | ----------------------------------- | --- | --- | --- | --- |
| Severity        | Warning                             |     |     |     |     |
| Description     | logswarningforrouteadditionattempt. |     |     |     |     |
| Event ID: 11502 |                                     |     |     |     |     |
Message "Exceededresource'<resource>'capacityadding<object>.Use'showcapacities-status'for
moreinformation."throttle_count:40
| Category        | L3ResourceManager                  |     |     |     |     |
| --------------- | ---------------------------------- | --- | --- | --- | --- |
| Severity        | Error                              |     |     |     |     |
| Description     | logserrorforrunningoutofresources. |     |     |     |     |
| Event ID: 11503 |                                    |     |     |     |     |
Message "Resource'<resource>'usageisat<percent>%ofcapacity.Use'showcapacities-status'for
moreinformation."throttle_count:40
| Category        | L3ResourceManager                           |     |     |     |     |
| --------------- | ------------------------------------------- | --- | --- | --- | --- |
| Severity        | Warning                                     |     |     |     |     |
| Description     | logswarningforhittingcertaincapacitylimits. |     |     |     |     |
| Event ID: 11504 |                                             |     |     |     |     |
Message OverlayECMProute{prefix}hasbeenprogrammedasasingleroute.
| Category | L3ResourceManager |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | --- |
| Severity | Info              |     |     |     |     |
Description logswarningwhenoverlayECMPgroupisprogrammedassingleroute.
| Event ID: 11505 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
184
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Traffic for IPv6 route prefix {prefix} will be software routed and performance impacted if
no other matching route prefixes from 0-64 for the same destination exist.

Category

L3 Resource Manager

Severity

Warning

Description

Logs warning that traffic might be routed in software for new route.

Event ID: 11506

Message

Category

Severity

Tunnel {vtep} resolved nexthop {nexthop} removed.

L3 Resource Manager

Info

Description

L3RM received event removing resolved nexthop from tunnel.

Event ID: 11507

Message

Category

Severity

Tunnel {vtep} resolved nexthop {nexthop} added.

L3 Resource Manager

Info

Description

L3RM received event adding resolved nexthop to tunnel.

L3 Resource Manager events | 185

Chapter 66

LACP events

LACP events

The following are the events related to LACP.

Event ID: 1301

Message

Category

Severity

Dynamic LAG <lag_id> created

LACP

Info

Description

Dynamic LAG has been created

Event ID: 1302

Message

Category

Severity

Dynamic LAG <lag_id> deleted

LACP

Info

Description

Dynamic LAG has been deleted

Event ID: 1303

Message

Category

Severity

Interface <intf_id> added to LAG <lag_id>. Existing configuration on interface <intf_id> will
be removed.

LACP

Info

Description

Log when interface has been added to LAG

Event ID: 1304

Message

Category

Severity

Interface <intf_id> removed from LAG <lag_id>. It will be set with default configuration
with admin down state.

LACP

Info

Description

Log when interface has been removed from LAG

Event ID: 1305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

186

Message

Category

Severity

LACP system priority set to <system_priority>

LACP

Info

Description

Log when LACP system priority is set

Event ID: 1306

Message

Category

Severity

LACP mode set to <lacp_mode> for LAG <lag_id>

LACP

Info

Description

Log when LACP mode is set

Event ID: 1307

Message

Category

Severity

LACP system ID set to <system_id>

LACP

Info

Description

Log when LACP system ID is set

Event ID: 1308

Message

Category

Severity

LACP rate set to <lacp_rate> for LAG <lag_id>

LACP

Info

Description

Log when LACP rate is set

Event ID: 1309

Message

Category

Severity

Partner is detected for interface <intf_id> LAG <lag_id>: <partner_sys_id>. Actor state:
<actor_state>, partner state <partner_state>

LACP

Info

Description

Log when LACP partner is detected

Event ID: 1310

Message

Partner is out of sync for interface <intf_id> LAG <lag_id>. Actor state: <actor_state>,

LACP events | 187

partner state <partner_state>

Category

LACP

Severity

Warning

Description

Log when LACP parter is out of sync

Event ID: 1311

Message

Partner is lost (timed out) for interface <intf_id> LAG <lag_id>. State: <fsm_state>

Category

LACP

Severity

Warning

Description

Log to indicate that LACP partner is lost

Event ID: 1312

Message

Category

Severity

Failed to create LAG <lag_id>

LACP

Error

Description

Log when LAG creation is failed

Event ID: 1313

Message

Category

Severity

LAG <lag_id> set as VSX

LACP

Info

Description

Log when VSX is created

Event ID: 1314

Message

Category

Severity

Description

Event ID: 1315

LAG <lag_id> not sending LACPDUs through interface <intf_id> because VSX information is
not complete

LACP

Info

Log when LAG is not sending LACPDUs through interface because VSX informationis
incomplete

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

188

Message

Category

Severity

LACP fallback mode set to <lacp_fallback_mode> for lag <lag_id>

LACP

Error

Description

Log when LACP fallback mode is set

Event ID: 1316

Message

Category

Severity

LACP fallback timeout set to <lacp_fallback_timeout> for lag <lag_id>

LACP

Error

Description

Log when LACP fallback timeout is set

Event ID: 1317

Message

Category

Severity

LACP fallback timeout <lacp_fallback_timeout> expired for lag <lag_id>

LACP

Error

Description

Log when LACP fallback timeout is expired

Event ID: 1318

Message

Category

Severity

Interface <intf_id> enabled by fallback for lag <lag_id>

LACP

Error

Description

Log when interface is enabled by fallback

Event ID: 1319

Message

Category

Severity

LAG global load balancing mode is set to <mode>

LACP

Info

Description

Logs to set global load balancing mode for LAG interfaces.

Event ID: 1320

Message

LAG load balancing mode is set to <mode> for lag <lag_id>

LACP events | 189

Category

Severity

LACP

Info

Description

Logs to set per port load balancing mode for LAG interface.

Event ID: 1321

Message

Category

Severity

LAG <lag_id> State change for interface <intf_id>: Actor state: <actor_state>, Partner state
<partner_state>

LACP

Info

Description

Logs that capture changes to LACP state for LAG interface.

Event ID: 1322

Message

Category

Severity

Description

Event ID: 1323

Message

Category

Severity

Interface <intf_name> cannot be part of Lag <lag_number>. Speed mismatched (Interface
speed <port_speed>Mbps Lag base speed <lag_speed>Mbps).' throttle_count: 100

LACP

Info

Logs to capture if LACP protocol does not allow interface to be part of lag due to speed
mismatch.

Fallback is <fallback> for LAG <lag_id>

LACP

Info

Description

Logs to capture if fallback is changed for LAG interface

Event ID: 1324

Message

Category

Severity

LACP Graceful Shut is initiated

LACP

Info

Description

Logs that caputre LACP Graceful Shut for LAG interface

Event ID: 1325

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

190

Message

Category

Severity

LACP Graceful Shut is completed

LACP

Info

Description

Logs that caputre LACP Graceful Shut for LAG interface

Event ID: 1326

Message

Category

Severity

Interface {intf_id} enabled by fallback-static for lag {lag_id}

LACP

Info

Description

Log when interface is enabled by fallback-static

Event ID: 1327

Message

Category

Severity

Interface {intf_id} disabled by fallback-static for lag {lag_id}

LACP

Info

Description

Log when interface is disabled by fallback-static

Event ID: 1328

Message

Category

Severity

Interface {intf_id} lag {lag_id} blocked as link partners on vsx primary and secondary
mismatch

LACP

Info

Description

Log when interface is blocked due to mismatching partner on the vsx interface

LACP events | 191

Chapter 67

LAG events

LAG events

The following are the events related to LAG.

Event ID: 1401

Message

Category

Severity

Trunk set succeeds unit <unit> lag_id <lag_id>

LAG

Info

Description

Logs the creation of trunk.

Event ID: 1402

Message

Category

Severity

Lag creation failed unit <unit> lag_id <lag_id> rc <rc> error <error>

LAG

Error

Description

Logs the failure of trunk creation.

Event ID: 1403

Message

Category

Severity

Destroy lag failed on unit <unit> lag_id <lag_id> rc <rc> error <error>

LAG

Error

Description

Logs the failure of trunk destroy.

Event ID: 1404

Message

Category

Severity

Trunk member add port succeeds on unit <unit> hw_port <hw_port> tid <tid>

LAG

Debug

Description

Logs the addition of port to trunk.

Event ID: 1405

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

192

Message

Category

Severity

Trunk port attach error on hw_port <hw_port> tid <tid> rc <rc> <error>

LAG

Error

Description

Logs the failure of addition of port to trunk.

Event ID: 1406

Message

Category

Severity

Failed to set egress enable on hw_port <hw_port> tid <tid> rc <rc> error <error>

LAG

Error

Description

Logs the failure to set egress enable.

Event ID: 1407

Message

Category

Severity

Failed to delete hw_port <hw_port> from tid <tid> rc <rc> error <error>

LAG

Error

Description

Logs the failure to delete a port.

Event ID: 1408

Message

Category

Severity

Trunk psc set failed on unit <unit> lag_id <lag_id> psc <psc> rc <rc> error <error>

LAG

Error

Description

Logs the failure to set port selection criteria.

Event ID: 1409

Message

Category

Severity

LAG <interface>, set to load balance mode to <mode>

LAG

Info

Description

logs to set load balancing mode for LAG L2/L3 interfaces.

Event ID: 1410

Message

Add port <port> to LAG <interface>

LAG events | 193

Category

Severity

LAG

Info

Description

logs to add port to LAG.

Event ID: 1411

Message

Category

Severity

Remove port <port> from LAG <interface>

LAG

Info

Description

logs to remove port from LAG.

Event ID: 1412

Message

Category

Severity

Add port <port> to vlan <vlan> for L3 LAG <interface>

LAG

Info

Description

logs to add port to L3 LAG.

Event ID: 1413

Message

Category

Severity

Remove port <port> to vlan <vlan> for L3 LAG <interface>

LAG

Info

Description

logs to remove port from LAG.

Event ID: 1414

Message

Category

Severity

Destroy L3 LAG interface <interface>

LAG

Info

Description

logs to destroy L3 LAG.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

194

Chapter 68
|               |           |        | Launch | Daemon | (LaunchD) | events |
| ------------- | --------- | ------ | ------ | ------ | --------- | ------ |
| Launch Daemon | (LaunchD) | events |        |        |           |        |
Thefollowingaretheeventsrelatedadaemonbeinglaunched.
Event ID: 14901
Message Allconfigurationconditionsaremettostart{daemon}daemon
| Category | LAUNCHD |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- |
| Severity | Info    |     |     |     |     |     |
Description Eventraisedwhenadaemonisstartedonconfigavailability
Event ID: 14902
| Message  | Failedtostart{daemon}daemon |     |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- | --- |
| Category | LAUNCHD                     |     |     |     |     |     |
| Severity | Error                       |     |     |     |     |     |
Description Eventraisedwhenadaemonfailedtostartonconfigavailability
Event ID: 14903
| Message     | Allconfigurationconditionsaremettostop{daemon}daemon |     |     |     |     |     |
| ----------- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
| Category    | LAUNCHD                                              |     |     |     |     |     |
| Severity    | Info                                                 |     |     |     |     |     |
| Description | Eventraisedwhenadaemonisstoppedonconfigremoval       |     |     |     |     |     |
Event ID: 14904
| Message  | Failedtodeletepathfilefor{daemon}daemon |     |     |     |     |     |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- |
| Category | LAUNCHD                                 |     |     |     |     |     |
| Severity | Error                                   |     |     |     |     |     |
Description Eventraisedwhenadaemonfailedtostoponconfigremoval
195
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 69

Layer 3 Interface events

Layer 3 Interface events

The following are the events related to layer 3 interface.

Event ID: 1701

Message

Category

Severity

L3-Interface <interface>, created

Layer 3 Interface

Info

Description

logs to create L3 interface.

Event ID: 1702

Message

Category

Severity

L3-Interface <interface>, deleted

Layer 3 Interface

Info

Description

logs to delete L3 interface.

Event ID: 1703

Message

Category

Severity

Interface <interface>, configured administratively <state>

Layer 3 Interface

Info

Description

logs for admin state of L3 interface.

Event ID: 1704

Message

Category

Severity

Failed to create <vlanid> for layer 3 interface <interface>

Layer 3 Interface

Error

Description

logs errors while creating vlan for layer 3 interfaces.

Event ID: 1705

Message

Failed to destroy layer 3 interface <interface> vlan <vlanid>, error: <err>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

196

Category

Layer 3 Interface

Severity

Error

Description

logs errors while destroying vlan for layer 3 interfaces.

Event ID: 1706

Message

Category

Severity

Failed to delete an l3 interface <interface>, error: <err>

Layer 3 Interface

Error

Description

logs errors while destroying layer 3 interface.

Event ID: 1707

Message

Category

Severity

Failed to add L3 host entry for ip <ipaddr>, error: <err>' throttle_count: 1

Layer 3 Interface

Error

Description

logs errors while adding l3 hosts.

Event ID: 1708

Message

Category

Severity

Added L3 host entry for ip <ipaddr>

Layer 3 Interface

Info

Description

logs while adding l3 hosts.

Event ID: 1709

Message

Category

Severity

Failed to delete L3 host entry for ip <ipaddr>, error: <err>

Layer 3 Interface

Error

Description

logs errors while deleting l3 hosts.

Event ID: 1710

Message

Category

Deleted L3 host entry for ip <ipaddr>

Layer 3 Interface

Layer 3 Interface events | 197

Severity

Info

Description

logs while deleting l3 hosts.

Event ID: 1711

Message

Category

Severity

Failed to get L3 host hit for ip <ipaddr>

Layer 3 Interface

Error

Description

logs errors to get L3 host hit for a specific ip.

Event ID: 1712

Message

Category

Severity

L3 interface error: <err>

Layer 3 Interface

Error

Description

logs for L3 setup errors.

Event ID: 1713

Message

Category

Severity

Added Nexthop <nexthop>, egress_id <egress_id>, for route <prefix>

Layer 3 Interface

Info

Description

logs for nexthop addition.

Event ID: 1714

Message

Category

Severity

Delete Nexthop <nexthop> for route <prefix>

Layer 3 Interface

Info

Description

logs for nexthop deletion.

Event ID: 1715

Message

Category

Severity

Added route <prefix>

Layer 3 Interface

Info

Description

logs for route addition.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

198

Event ID: 1716

Message

Category

Severity

Update: route state: <state>

Layer 3 Interface

Info

Description

logs for route update.

Event ID: 1717

Message

Category

Severity

Delete route <prefix>

Layer 3 Interface

Info

Description

logs for route deletion.

Event ID: 1718

Message

Category

Severity

Delete route <prefix>, error: <err>

Layer 3 Interface

Error

Description

logs error for route deletion.

Event ID: 1719

Message

Category

Severity

Add route <prefix>, error: <err>' throttle_count: 1

Layer 3 Interface

Error

Description

logs error for route aditiontion.

Event ID: 1720

Message

Category

Severity

Error creating egress object for port <port>, error: <err>

Layer 3 Interface

Error

Description

logs errors for egress object creation.

Event ID: 1721

Message

Created L3 egress ID <egress_id> for port <port> intf <intf>

Layer 3 Interface events | 199

Category

Layer 3 Interface

Severity

Info

Description

logs for egress object creation.

Event ID: 1722

Message

Category

Severity

Error deleting egress object for port <port>, error: <err>

Layer 3 Interface

Error

Description

logs errors for egress object deletion.

Event ID: 1723

Message

Category

Severity

Deleted L3 egress ID <egress_id> for port <port>

Layer 3 Interface

Info

Description

logs for egress object deletion.

Event ID: 1724

Message

Category

Severity

Interface <interface>, configured with ipv4 address <value>

Layer 3 Interface

Info

Description

logs for ipv4 address update on interface.

Event ID: 1725

Message

Category

Severity

Interface <interface>, configured with ipv6 address <value>

Layer 3 Interface

Info

Description

logs for ipv6 address update on interface.

Event ID: 1726

Message

Category

Interface <interface>, ipv4 address deleted <value>

Layer 3 Interface

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

200

Severity

Info

Description

logs for ipv4 address delete from interface.

Event ID: 1727

Message

Category

Severity

Interface <interface>, ipv6 address deleted <value>

Layer 3 Interface

Info

Description

logs for ipv6 address delete from interface.

Event ID: 1728

Message

Category

Severity

IPv6 Address Status: Interface <intf>, address <addr>, status <addr_status>

Layer 3 Interface

Info

Description

Event raised when ipv6 address status changes

Event ID: 1729

Message

Category

Severity

Interface <interface>, configured with secondary ipv4 address <value>

Layer 3 Interface

Info

Description

logs for secondary ipv4 address update on interface.

Event ID: 1730

Message

Category

Severity

Interface <interface>, secondary ipv4 address deleted <value>

Layer 3 Interface

Info

Description

logs for secondary ipv4 address delete from interface.

Event ID: 1731

Message

Category

Severity

IP MTU <mtu> not applied due to hardware resource limitation

Layer 3 Interface

Error

Description

Logs failure while configuring hardware for IPMTU.

Layer 3 Interface events | 201

Event ID: 1732

Message

IPv6 address {value} is not applied on interface {interface}, as only one global ipv6
address will be in effect.

Category

Layer 3 Interface

Severity

Error

Description

Logs failure while configuring more than one global ipv6 address on an interface.

Event ID: 15804

Message

Interface {ifname}, configured with ipv4 unnumbered address {ip-address}, lender
interface {lender_port_name}

Category

Layer 3 Interface

Severity

Info

Description

logs for ipv4 unnumbered address update on interface.

Event ID: 15805

Message

ipv4 unnumbered address {ip-address} deleted from interface {ifname}, lender interface
{lender_port_name}

Category

Layer 3 Interface

Severity

Info

Description

logs for ipv4 unnumbered address delete from interface.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

202

Chapter 70

LED events

LED events

The following are the events related to LED.

Event ID: 501

Message

There are <count> LED types in subsystem <subsystem>

Category

LED

Severity

Information

Description

Log about number of LED types in subsystem

Event ID: 502

Message

There are <count> LED configs in subsystem <subsystem>

Category

LED

Severity

Information

Description

Log about number of LED config in subsystem

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

203

Chapter 71

LLDP events

LLDP events

The following are the events related to LLDP.

Event ID: 101

Message

LLDP Enabled

Category

LLDP

Severity

Information

Description

Logs event when LLDP (Link Layer Discovery Protocol) feature is enabled in the switch.

Event ID: 102

Message

LLDP Disabled

Category

LLDP

Severity

Information

Description

Logs event when LLDP (Link Layer Discovery Protocol) feature is disabled in the switch.

Event ID: 103

Message

Configured LLDP tx-timer to <value>

Category

LLDP

Severity

Information

Description

Logs event when the LLDP status update interval is configured by the user.

Event ID: 104

Message

LLDP neighbor <chassisid> added on <interface>

Category

LLDP

Severity

Information

Description

Logs event when a new neighbor entry is added to the switch.

Event ID: 105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

204

Message

LLDP neighbor <chassisid> updated on <interface>' throttle_count: 100

Category

LLDP

Severity

Information

Description

Logs event when an existing neighbor entry is updated in the switch.

Event ID: 106

Message

LLDP neighbor <chassisid> deleted on <interface>

Category

LLDP

Severity

Information

Description

Logs event when an existing neighbor entry is deleted from switch.

Event ID: 107

Message

Configured LLDP Management IP <value>

Category

LLDP

Severity

Information

Description

Logs event when a new management IP address is configured by the user.

Event ID: 108

Message

Configured LLDP tx-hold to <hold>

Category

LLDP

Severity

Information

Description

Logs event when LLDP transmit multiplier value is configured by the user.

Event ID: 109

Message

Configured LLDP tx-delay to <value>

Category

LLDP

Severity

Information

Description

Logs event when LLDP transmit delay value is configured by the user.

Event ID: 110

Message

Configured LLDP reinit-delay to <value>

LLDP events | 205

Category

LLDP

Severity

Information

Description

Logs event when LLDP interface reinitialization value is configured by the user.

Event ID: 111

Message

LLDP statistics cleared

Category

LLDP

Severity

Information

Description

Logs event when LLDP statistics are cleared from the switch.

Event ID: 112

Message

LLDP neighbor info cleared

Category

LLDP

Severity

Information

Description

Logs event when LLDP neighbor information is cleared from the switch.

Event ID: 113

Message

PVID mismatch on <interface> pvid = <pvid>, Neighbor <chassisid> port_id = <ninterface>
pvid = <npvid>

Category

LLDP

Severity

Information

Description

Log event when the PVID mismatches between the switch and neighbor over an
interface.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

206

Chapter 72

Loop Protect events

Loop Protect events

The following are the events related to loop protect.

Event ID: 2801

Message

Port <portName> is disabled by Loop-protection after loop detection on VLAN <vlan>

Category

Loop Protect

Severity

Warning

Description

Logs port disabled by Loop protect

Event ID: 2802

Message

Ports TX <txportName> and RX <rxportName> are disabled by Loop-protect after loop
detection on VLAN <vlan>

Category

Loop Protect

Severity

Warning

Description

Logs port disabled by Loop protect

Event ID: 2803

Message

Loop detected on port <portName> on VLAN <vlan>

Category

Loop Protect

Severity

Warning

Description

Logs port which receives PDU of its own

Event ID: 2804

Message

Port <portName> enabled after disable time expired

Category

Loop Protect

Severity

Info

Description

Logs port enabled after disabled time expired

Event ID: 2805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

207

Message

Port <portName> added for loop-protection

Category

Loop Protect

Severity

Info

Description

Logs port added

Event ID: 2806

Message

Port <portName> deleted from loop-protection

Category

Loop Protect

Severity

Info

Description

Logs port deleted

Event ID: 2807

Message

Loop-Protection stats cleared for port <portName>

Category

Loop Protect

Severity

Info

Description

Loop-Protection stats cleared for port

Event ID: 2808

Message

Ports TX <txportName> and RX <rxportName> are involved during TX port disabling

Category

Loop Protect

Severity

Info

Description

Logs TX and RX ports after TX disabled by Loop protect

Event ID: 2809

Message

Category

Severity

Port {portName} is disabled by Loop-protection after loop detection on VLAN {vlan}

Loop Protect

Warning

Description

Logs port disabled by Loop protect

Event ID: 2810

Message

Ports TX {txportName} and RX {rxportName} are involved during RX port disabling

Loop Protect events | 208

Category

Loop Protect

Severity

Info

Description

Logs TX and RX ports after RX disabled by Loop protect

Event ID: 2811

Message

Category

Severity

Max vport limit {vportLimit} reached. Current vport {currvportCount}

Loop Protect

Info

Description

Logs max vport limit reached and Current vport count.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

209

Chapter 73

Loopback events

Loopback events

The following are the events related to loopback.

Event ID: 901

Message

Loopback Interface <interface>, created

Category

Loopback

Severity

Information

Description

Log when loopback interface is created

Event ID: 902

Message

Loopback Interface <interface>, deleted

Category

Loopback

Severity

Information

Description

Log when loopback interface is deleted

Event ID: 903

Message

Loopback Interface <interface>, configured administratively <state>

Category

Loopback

Severity

Information

Description

Log about loopback interface admin state

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

210

Chapter 74
|             |            |        | MAC address | management | events |
| ----------- | ---------- | ------ | ----------- | ---------- | ------ |
| MAC address | management | events |             |            |        |
ThefollowingaretheeventsrelatedtoMACaddressmanagement.
| Event ID: 4801 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
Message
MAC<mac>movedfromport<from-intf>toport<to-intf>onVLAN<vlan>
| Category       | MACaddressmanagement                          |     |     |     |     |
| -------------- | --------------------------------------------- | --- | --- | --- | --- |
| Severity       | Info                                          |     |     |     |     |
| Description    | EventraisedwhenL2macmove                      |     |     |     |     |
| Event ID: 4802 |                                               |     |     |     |     |
| Message        | AlldynamicMACaddressesonVLAN<vlan>wereflushed |     |     |     |     |
| Category       | MACaddressmanagement                          |     |     |     |     |
| Severity       | Info                                          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithvlandeleteeventorclearmac-address
commandfromvtysh
| Event ID: 4803 |                                               |     |     |     |     |
| -------------- | --------------------------------------------- | --- | --- | --- | --- |
| Message        | AlldynamicMACaddressesonport<intf>wereflushed |     |     |     |     |
| Category       | MACaddressmanagement                          |     |     |     |     |
| Severity       | Info                                          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithportmovetoL3eventorclearmac-
addresscommandfromvtysh
| Event ID: 4804 |                                               |     |     |     |     |
| -------------- | --------------------------------------------- | --- | --- | --- | --- |
| Message        | AlldynamicMACaddressesonport<intf>wereflushed |     |     |     |     |
| Category       | MACaddressmanagement                          |     |     |     |     |
| Severity       | Info                                          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithportdowneventorclearmac-address
commandfromvtysh
| Event ID: 4805 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
211
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

All dynamic MAC addresses on VLAN <vlan> were flushed

Category

MAC address management

Severity

Info

Description

Event raised when L2 MAC table is flushed with vlan down event or clear mac-address
command from vtysh

Event ID: 4806

Message

L2X thread not running. Attempting to recover

Category

MAC address management

Severity

Warning

Description

Event raised when BCM L2X thread is identified as not running

Event ID: 4807

Message

L2X thread recovered

Category

MAC address management

Severity

Warning

Description

Event raised when BCM L2X thread is successfully recovered

Event ID: 4808

Message

L2X thread recovery failed

Category

MAC address management

Severity

Error

Description

Event raised when BCM L2X thread is failed to be recovered

Event ID: 4809

Message

MAC hash collision occurred for MAC {mac} on VLAN {vlan}

Category

MAC address management

Severity

Error

Description

Logs warning that MAC hit a hash collision in SDK.

Event ID: 4810

Message

MAC-lockout automatically disabled because active-gateway extended-mac was enabled

MAC address management events | 212

Category

MAC address management

Severity

Warning

Description

Event raised when mac-lockout feature is disabled due to active-gateway extended-mac
feature being enabled.

Event ID: 4811

Message

Category

Severity

MAC-lockout is automatically enabled

MAC address management

Info

Description

Event raised when mac-lockout feature is enabled,

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

213

Chapter 75
|             |                    | MAC Address | mode | configuration | events |
| ----------- | ------------------ | ----------- | ---- | ------------- | ------ |
| MAC Address | mode configuration | events      |      |               |        |
ThefollowingaretheeventsrelatedtoMACAddressmodeconfiguration.
| Event ID: 11001 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message
TheMACAddressconfiguredmodechangedfrom<old_mode>to<new_mode>
| Category        | MACAddressmodeconfiguration                      |     |     |     |     |
| --------------- | ------------------------------------------------ | --- | --- | --- | --- |
| Severity        | Information                                      |     |     |     |     |
| Description     | LogeventwhentheMACAddressconfiguredmodeischanged |     |     |     |     |
| Event ID: 11002 |                                                  |     |     |     |     |
Message TheMACAddressoperationalmodechangedfrom<old_mode>to<new_mode>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Information                 |     |     |     |     |
Description LogeventwhentheMACAddressoperationalmodeischanged
| Event ID: 11003 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message StationMACaddfailureduetohardwarefull,mac=<mac>vlan=<vlan>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Error                       |     |     |     |     |
Description LogeventwhenalocalstationMACaddresscannotbeaddedbecausethetableisfull
| Event ID: 11004 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message
TheMACAddressoperationalmodechangedfrom<old_mode>to<new_mode>dueto
reachingSVIthreshold.Current=<current>Max=<max>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Error                       |     |     |     |     |
Description LogeventwhentheMACAddressoperationalmodeischangedduetooutofresources
| Event ID: 11005 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
214
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

Router mac={mac} add failed on vlan={vlan}. Reason={reason}, mode={mode}.

MAC Address mode configuration

Error

Description

Log event when a router MAC address addition failed.

MAC Address mode configuration events | 215

Chapter 76

MAC Learning events

MAC Learning events

The following are the events related to MAC learning.

Event ID: 4801

Message

MAC <mac> moved from port <from-intf> to port <to-intf> on VLAN <vlan>

Category

MAC Learning

Severity

Information

Description

Event raised when L2 mac move

Event ID: 4802

Message

All dynamic MAC addresses on VLAN <vlan> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with vlan delete event or clear mac-address
command from vtysh

Event ID: 4803

Message

All dynamic MAC addresses on port <intf> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with port move to L3 event or clear mac-
address command from vtysh

Event ID: 4804

Message

All dynamic MAC addresses on port <intf> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with port down event or clear mac-address
command from vtysh

Event ID: 4805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

216

Message

All dynamic MAC addresses on VLAN <vlan> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with vlan down event or clear mac-address
command from vtysh

MAC Learning events | 217

Chapter 77

MACsec events

MACsec events

The following are the events related to MACsec.

Event ID: 11201

Message

MACsec session established on Rx Secure Channel <sci> on interface <ifname>.

Category

MACsec

Severity

Info

Description

A MACsec session established on an interface.

Event ID: 11202

Message

MKA session secured for Connectivity Association <ckn> on interface <ifname>.

Category

MACsec

Severity

Info

Description

A Connectivity Association was successfully established on an interface.

Event ID: 11203

Message

Secure Association key updated for Connectivity Association <ckn> on interface <ifname> -
Latest AN/KN <latest_an>/<latest_kn>, Old AN/KN <old_an>/<old_kn>.

Category

MACsec

Severity

Info

Description

A new Secure Association key created for a Connectivity Association.

Event ID: 11204

Message

Possible replay attempt detected on the Secure Channel <sci>.

Category

MACsec

Severity

Info

Description

A possible replay attempt detected on a Secure Channel.

Event ID: 11205

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

218

Message

The data traffic on interface <ifname> is now secured by MACsec.

Category

MACsec

Severity

Info

Description

The data plane traffic on an interface is secured by MACsec.

Event ID: 11206

Message

The data traffic on interface <ifname> is no longer secured by MACsec.

Category

MACsec

Severity

Info

Description

The data plane traffic on an interface is not secured by MACsec anymore.

Event ID: 11207

Message

Interface {ifname} MACsec selftest failed - {reason}.

Category

MACsec

Severity

Error

Description

MACsec selftest failed for the specified interface.

Event ID: 11208

Message

MACsec frame with an unknown SCI detected on MACsec entity running on interface
{ifname} with port ID {id}

Category

MACsec

Severity

Info

Description

Detected a MACsec frame with unknown SCI on an interface with the specified port ID.

Event ID: 11209

Message

Suspending data delay protection for Connectivity Association {ckn} on interface {ifname}
during ISSU.

Category

MACsec

Severity

Info

Description

Data delay protection is suspended for the specified CKN on interface during ISSU.

Event ID: 11210

MACsec events | 219

Message

Resuming data delay protection for Connectivity Association {ckn} on interface {ifname}
post ISSU.

Category

MACsec

Severity

Info

Description

Data delay protection is resumed for the given CKN post ISSU.

Event ID: 11211

Message

ISSU aborted by MACsec. Reason - {reason}.

Category

MACsec

Severity

Info

Description

ISSU aborted by MACsec.

Event ID: 11212

Message

Interface {ifname} blocked by MACsec due to a misconfiguration. Reason - {reason}.

Category

MACsec

Severity

Error

Description

MACsec daemon blocked an interface due to a configuration error.

Event ID: 11213

Message

MACsec is disabled on port {name}. Additional licenses are needed to enable the
{feature} functionality on the port.

Category

MACsec

Severity

Error

Description

The port will remain blocked for both ingress and egress traffic till a valid license is not
installed.

Event ID: 11214

Message

MACsec is operational on port {name} without a valid license for {feature}.

Category

MACsec

Severity

Info

Description

MACsec is operational on the port in honor mode.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

220

Chapter 78

Management events

Management events

The following are the events related to management.

Event ID: 4301

Message

MGMT_INTF: <mgmt_intf_config_param>

Category

Management

Severity

Info

Description

Logs related to management interface configurations

Event ID: 4302

Message

MGMT_INTF: <mgmt_intf_config_err>

Category

Management

Severity

Error

Description

Logs related to management interface configurations error

Event ID: 4303

Message

MGMT_INTF: <mgmt_intf_config_crit>

Category

Management

Severity

Critical

Description

Logs related to management interface critical configurations

Event ID: 4304

Message

MGMT_INTF: <mgmt_intf_config_crit>

Category

Management

Severity

Critical

Description

Logs related to management interface critical configurations

Event ID: 4305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

221

Message

Category

Severity

MGMT_INTF: Stopped dhcp v4 client on interface {intf}

MGMT

Info

Description

Log event when DHCPv4 client is stopped on management interface

Event ID: 4306

Message

Category

Severity

MGMT_INTF: Started dhcp v6 client on interface {intf}

MGMT

Info

Description

Log event when DHCPv6 client is started on management interface

Event ID: 4307

Message

Category

Severity

MGMT_INTF: Stopped dhcp v6 client on interface {intf}

MGMT

Info

Description

Log event when DHCPv6 client is stopped on management interface

Event ID: 4308

Message

Category

Severity

MGMT_INTF: Starting the dhcp client due to link up (or) new link

MGMT

Info

Description

Log event when management interface link is UP or new link is added

Event ID: 4309

Message

Category

Severity

Description

Event ID: 4310

MGMT_INTF: Clearing the dhcp configuration due to link down (or) link remove

MGMT

Info

Log event when dhcp configurations are cleared on management interface when link
goes DOWN or link is removed

Message

MGMT_INTF: Configuring {ip_address} address on management interface failed due to
DAD failure

Management events | 222

Category

Severity

Description

Event ID: 4311

Message

Category

Severity

MGMT

Info

Log event when configuring ip address on management interface failed due to DAD
failure

MGMT_INTF: {mgmt_intf_config_param_dhcp}

MGMT

Info

Description

Logs related to management interface configurations learnt via DHCP

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

223

Chapter 79

MDNS events

MDNS events

The following are the events related to MDNS.

Event ID: 11401

Message

mDNS-SD enabled

Category

MDNS

Severity

Information

Description

Logs event when mDNS-SD feature is enabled in the switch.

Event ID: 11402

Message

mDNS-SD disabled

Category

MDNS

Severity

Information

Description

Logs event when mDNS-SD feature is disabled in the switch.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

224

Chapter 80

MGMD events

MGMD events

The following are the events related to MGMD.

Event ID: 2601

Message

Category

Severity

Failed to alloc a <pkt_type> pkt(interface <vlan>)

MGMD

Error

Description

This log event informs packet allocation failed in MGMD subsystem.

Event ID: 2602

Message

Category

Severity

Received IGMPv1 query from <ip_address> when the device is configured for IGMPv2.

MGMD

Info

Description

This log event used to log IGMP warning when IGMPv1 query is received.

Event ID: 2603

Message

Category

Severity

Unable to alloc a buf of size <size_value> for <sub_system>

MGMD

Error

Description

This log event informs the user that MGMD could not allocate memory.

Event ID: 2604

Message

Category

Severity

Interface <if_name>: Other Querier detected for <mgmd_type>

MGMD

Info

Description

This log event informs the user that IGMP/MLD detected other querier.

Event ID: 2605

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

225

Message

Category

Severity

<mgmd_type> Querier Election in progress for interface <if_name> with IP address <ip_
address>

MGMD

Info

Description

This log event informs the user that IGMP/MLD has started querier election on interface.

Event ID: 2606

Message

Category

Severity

Interface <if_name>: End <mgmd_type> Querier role

MGMD

Info

Description

This log event informs the user that IGMP/MLD ended querier role on interface.

Event ID: 2607

Message

Category

Severity

Interface <if_name>: Start <mgmd_type> Querier role addr: <ip_address>

MGMD

Info

Description

This log event informs the user that MGMD started querier role on interface.

Event ID: 2608

Message

Received packet from <ip_address>, type <type>, on invalid port <port>

Category

MGMD

Severity

Warning

Description

This log event informs the user that MGMD received packet on invalid port.

Event ID: 2609

Message

Category

Severity

Description

Event ID: 2610

Received IGMPv1 query from <ip_address> when the device is configured for IGMPv3.'
throttle_count: 1

MGMD

Info

This log event used to log IGMP warning when configured mode is IGMPv3 and IGMPv1
query is received.

MGMD events | 226

Message

Category

Severity

Description

Event ID: 2611

Message

Category

Severity

Received IGMPv2 query from <ip_address> when the device is configured for IGMPv3.'
throttle_count: 1

MGMD

Info

This log event used to log IGMP warning when configured mode is IGMPv3 and IGMPv2
query is received.

<mgmd_type> snooping is <status> on VLAN <vlan>

MGMD

Info

Description

This log event informs the user that IGMP/MLD status on VLAN.

Event ID: 2612

Message

Category

Severity

<mgmd_type> is <status> on Interface <if_name>

MGMD

Info

Description

This log event informs the user the IGMP/MLD status on the Interface.

Event ID: 2613

Message

Category

Severity

Port <port> on vlan <vlan> is set to <status> mode for <mgmd_type>.

MGMD

Info

Description

This log event informs the user that the port mode has changed.

Event ID: 2614

Message

Category

Severity

Description

Event ID: 2615

<mgmd_type> is not operational on VLAN <vlan> due to resource unavailability

MGMD

Error

This log event informs the user that the IGMP/MLD is disabled on a VLAN due to internal
errors.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

227

Message

Category

Severity

Description

Event ID: 2616

Message

Category

Severity

Description

Event ID: 2617

Message

Category

Severity

Description

Event ID: 2618

Message

Category

Severity

<mgmd_type> is not operational on interface <l3Port> due to resource unavailability

MGMD

Error

This log event informs the user that the IGMP/MLD is disabled on a L3 interface due to
internal errors.

IGMP/MLD Resource utilization has exceeded the supported limits on the system.
Membership reports for the new groups will be dropped.

MGMD

Info

This log event informs the user that MGMD resource utilization has exceeded the
supported limits

IGMP/MLD Resource utilization has reached 90 percent of the supported limits on the
system.

MGMD

Info

This log event informs the user that MGMD resource utilization has reached 90 percent
of the supported limits

<mgmd_type> snooping is <status> on VLAN <vlan>.

MGMD

Info

Description

This log event informs the user that whether IGMP/MLD snooping is operational.

Event ID: 2619

Message

Category

Severity

Received IGMPv3 query from <ip_address> when the device is configured for IGMPv2.'
throttle_count: 1

MGMD

Info

Description

This log event used to log IGMP warning when IGMPv2 query is received.

MGMD events | 228

Event ID: 2620

Message

Category

Severity

Description

Event ID: 2621

Message

Category

Severity

Description

Event ID: 2622

Message

Category

Severity

Received MLDV1 query from <ip_address> when the device is configured for MLDV2.'
throttle_count: 1

MGMD

Info

This log event used to log MLD warning when configured mode is MLDV2 and MLDV1
query is received.

Received MLDV2 query from <ip_address> when the device is configured for MLDV1.'
throttle_count: 1

MGMD

Info

This log event used to log MLD warning when configured mode is MLDv2 and MLDv1
query is received.

Flood mode is temporarily activated on ERPS ports <port0> and <port1> as ring state for
ring id <ring_id> changed to <state>.

MGMD

Info

Description

This log event used to log if ERPS Ring state changed to idle or protection.

Event ID: 2623

Message

Category

Severity

Remote IDL connection established.

MGMD

Info

Description

This log event is used to indicate remote IDL connection is established

Event ID: 2624

Message

Category

Severity

Querier functionality offloaded to VSX peer.

MGMD

Info

Description

This log event is used to indicate that querier is offloaded.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

229

Event ID: 2625

Message

Category

Severity

IGMPv2 packet received for group address {ip_address} in SSM range which is not part of
SSM map.

MGMD

Info

Description

This log event is used to identify IGMPv2 packet in ssm-range but not in ssm-map.

Event ID: 2626

Message

Category

Severity

MLDv1 packet received for group address {ip_address} in SSM range which is not part of
SSM map.

MGMD

Info

Description

This log event is used to identify MLDv1 packet in ssm-range but not in ssm-map.

Event ID: 2627

Message

Category

Severity

SSM-map {acl_name} applied to {protocol} interface {port_name}

MGMD

Info

Description

This log event is used to identify that ssm-map ACL is applied to particular interface.

Event ID: 2628

Message

Category

Severity

IGMP/MLD internal queue limit exceeded. Needs admin intervention.

MGMD

Alert

Description

This log event is used to intimate the user that IGMP/MLD control packet queue is full.

MGMD events | 230

Chapter 81

Mirroring events

Mirroring events

The following are the events related to mirroring.

Event ID: 6701

Message

Failed to create mirror session <number>

Category

Mirroring

Severity

Error

Description

Logs a message when the creation of a mirror session fails

Event ID: 6702

Message

Mirror session <number> created

Category

Mirroring

Severity

Information

Description

Logs a message when the creation of a mirror session succeeds

Event ID: 6703

Message

Failed to delete mirror session <number>

Category

Mirroring

Severity

Error

Description

Logs a message when the deletion of a mirror session fails

Event ID: 6704

Message

Mirror session <number> deleted

Category

Mirroring

Severity

Information

Description

Logs a message when mirror session is successfully deleted

Event ID: 6705

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

231

Message

Failed to update mirror session <number>

Category

Mirroring

Severity

Error

Description

Logs a message when an update of a mirror session fails

Event ID: 6706

Message

Mirror session <number> updated

Category

Mirroring

Severity

Information

Description

Logs a message when the update of a mirror session succeeds

Mirror-on-drop events
The following are the events related to the mirror-on-drop feature.

Event ID: 16301

Message

HONOR_MODE: Mirror On Drop is operating without a valid feature pack.

Category

Mirror on drop

Severity

Info

Description

Log event to indicate that the Mirror On Drop feature is operating without a valid feature
pack.

Event ID: 16302

Message

STRICT_MODE: Mirror On Drop is blocked due to invalid or missing feature pack.

Category

Mirror on drop

Severity

Info

Description

Log event to indicate that the Mirror On Drop feature is blocked due to invalid or missing
feature pack

Event ID: 16303

Message

ACTIVE_MODE: Mirror On Drop is operating with valid feature pack.

Category

Mirror on drop

Severity

Info

Description

Log event to indicate that the Mirror On Drop feature is operational for valid feature pack

Mirror-on-drop events | 232

Chapter 82

Module events

Module events

The following are the events related to modules.

Event ID: 3201

Message

Category

Severity

<type> module <name> inserted': yes

Module

Info

Description

Indicates that the module has been physically inserted

Event ID: 3202

Message

Category

Severity

<type> module <name> removed': yes

Module

Warning

Description

Indicates that the module has been physically removed

Event ID: 3203

Message

Category

Severity

Initiating <type> module <name> reboot': yes

Module

Info

Description

Indicates that the module is about to reboot

Event ID: 3204

Message

Category

Severity

<type> module <name> is ready

Module

Info

Description

Indicates that the module is initialized and ready

Event ID: 3205

Message

<type> module <name> is down: <reason>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

233

Category

Module

Severity

Info

Description

Indicates that the module is down

Event ID: 3206

Message

Category

Severity

<type> module <name> is in diagnostics mode

Module

Info

Description

Indicates that a module is in diagnostics mode

Event ID: 3207

Message

Category

Severity

<type> module <name> has failed: <reason>': yes

Module

Error

Description

Indicates that a module has failed

Event ID: 3208

Message

Category

Severity

<type> module <name> admin state set to up

Module

Info

Description

Indicates that the module administrative state is set to up

Event ID: 3209

Message

Category

Severity

<type> module <name> admin state set to down

Module

Info

Description

Indicates that the module administrative state is set to down

Event ID: 3210

Message

Category

<type> module <name> admin state set to diagnostics

Module

Module events | 234

Severity

Info

Description

Indicates that the module administrative state is set to diagnostics

Event ID: 3211

Message

Category

Severity

<type> module <name> ISP passed

Module

Info

Description

Indicates that ISP has passed for the module

Event ID: 3212

Message

Category

Severity

<type> module <name> ISP failed': yes

Module

Error

Description

Indicates that ISP has failed for the module

Event ID: 3213

Message

Category

Severity

<type> module <name> ISP skipped

Module

Warning

Description

Indicates that ISP has been skipped for the module

Event ID: 3214

Message

Category

Severity

<type> module <name> has enabled standby power

Module

Info

Description

Indicates that the module is in standby (low-power) mode

Event ID: 3215

Message

Category

Severity

<type> module <name> is requesting to power on with priority <priority>

Module

Info

Description

Indicates that the module is requesting to power on

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

235

Event ID: 3216

Message

Category

Severity

<type> module <name> power request has been granted

Module

Info

Description

Indicates that the power request for the module has been granted

Event ID: 3217

Message

Category

Severity

<type> module <name> power request has been denied

Module

Warning

Description

Indicates that the power request for the module has been denied

Event ID: 3218

Message

Category

Severity

<type> module <name> enabling main power

Module

Info

Description

Indicates that main power for the module is being enabled

Event ID: 3219

Message

Category

Severity

<type> module <name> main power enabled

Module

Info

Description

Indicates that main power for the module has been enabled

Event ID: 3220

Message

Category

Severity

<type> module <name> main power failed': yes

Module

Error

Description

Indicates that main power for the module has failed

Event ID: 3221

Message

<type> module <name> device initialization started

Module events | 236

Category

Module

Severity

Info

Description

Indicates that device initialization for the module has started

Event ID: 3222

Message

Category

Severity

<type> module <name> device initialization passed

Module

Info

Description

Indicates that device initialization for the module has passed

Event ID: 3223

Message

Category

Severity

<type> module <name> device initialization failed: <reason>': yes

Module

Error

Description

Indicates that device initialization for the module has failed

Event ID: 3224

Message

Category

Severity

<type> module <name> ASIC initialization started

Module

Info

Description

Indicates that an ASIC for the module is being initialized

Event ID: 3225

Message

Category

Severity

<type> module <name> ASIC initialization completed

Module

Info

Description

Indicates that ASIC initialization for the module has completed

Event ID: 3226

Message

Category

<type> module <name> ASIC initialization failed: <reason>': yes

Module

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

237

Severity

Error

Description

Indicates that ASIC initialization for the module has failed

Event ID: 3227

Message

Category

Severity

<type> module <name> ASIC deinitialization started

Module

Info

Description

Indicates that an ASIC for the module is being deinitialized

Event ID: 3228

Message

Category

Severity

<type> module <name> ASIC deinitialization completed

Module

Info

Description

Indicates that ASIC deinitialization for the module has completed

Event ID: 3229

Message

Category

Severity

<type> module <name> ASIC denitialization failed: <reason>': yes

Module

Error

Description

Indicates that ASIC deinitialization for the module has failed

Event ID: 3230

Message

Category

Severity

<name> is starting zeroization': yes

Module

Info

Description

Indicates that the module is about to start zeroization

Event ID: 3231

Message

Category

Severity

<name> zeroization completed.

Module

Info

Description

Indicates that the module zeroization has completed

Module events | 238

Event ID: 3232

Message

Category

Severity

<name> zeroization failed.': yes

Module

Error

Description

Indicates that the module zeroization failed to complete

Event ID: 3233

Message

Category

Severity

<type> module <name> configured with product number <part_number>

Module

Info

Description

Indicates that the module has been configured

Event ID: 3234

Message

Category

Severity

<type> module <name> has been unconfigured

Module

Info

Description

Indicates that the module has been unconfigured

Event ID: 3235

Message

Category

Severity

<type> module <name> initiating failover

Module

Info

Description

Indicates that the module has started failover

Event ID: 3236

Message

Category

Severity

<type> module <name> failover completed

Module

Info

Description

Indicates that the module has completed failover

Event ID: 3237

Message

<type> module <name> initiating ISP

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

239

Category

Module

Severity

Info

Description

Indicates that ISP has started for the module

Event ID: 3238

Message

Category

Severity

<type> module <name> enabling front-end power

Module

Info

Description

Indicates that front-end power is being enabled

Event ID: 3239

Message

Category

Severity

<type> module <name> disabling front-end power: <reason>

Module

Warning

Description

Indicates that front-end power is being disabled

Event ID: 3240

Message

Category

Severity

<type> module <name> has persistent hardware error

Module

Error

Description

Indicates that persistent hardware error has occurred

Event ID: 3241

Message

Category

Severity

{name} is starting zeroization and setting enhanced secure mode

Module

Info

Description

Indicates that the module is about to start zeroization and setting enhanced secure mode

Event ID: 3242

Message

Category

{name} zeroization completed and enhanced secure mode set.

Module

Module events | 240

Severity

Info

Description

Indicates that the module zeroization has completed and enhanced secure mode s

Event ID: 3243

Message

Category

Severity

{name} zeroization failed.

Module

Info

Description

Indicates that the module zeroization failed to complete

Event ID: 3244

Message

Category

Severity

{name} Front-panel factory-reset is now {status}

Module

Info

Description

Indicates that the module front-panel factory-reset configuration has been changed.

Event ID: 3245

Message

Category

Severity

Description

Event ID: 3246

Message

Category

Severity

{name} Front-panel factory-reset is NOT supported with current system recipe.

Module

Info

Indicates that the module does not support front-panel factory-reset with current system
recipe.

Config compatability allowed between modules {old_part} and {new_part}

Module

Info

Description

Indicates that config was kept between part number changes

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

241

Chapter 83

MPLS events

MPLS events

The following are the events related to MPLS.

Event ID: 13301

Message

Category

Severity

MPLS LDP session with local identifier <local_ldp_id> and peer identifier <peer_ldp_id> has
come up.

MPLS

Info

Description

Logs a message when an LDP neighbor comes up

Event ID: 13302

Message

Category

Severity

MPLS LDP session with local identifier <local_ldp_id> and peer identifier <peer_ldp_id> has
gone down.

MPLS

Info

Description

Logs a message when an LDP neighbor goes down

Event ID: 13303

Message

Category

Severity

MPLS Graceful Restart process started

MPLS

Info

Description

Logs the start of MPLS Graceful Restart.

Event ID: 13304

Message

Category

Severity

MPLS Graceful Restart process is complete

MPLS

Error

Description

Logs the end of MPLS Graceful Restart.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

242

Chapter 84

MSDP events

MSDP events

The following are the events related to MSDP.

Event ID: 8601

Message

Category

Severity

Router MSDP is <status> on VRF <vrf_name>

MSDP

Info

Description

Router msdp configuration status

Event ID: 8602

Message

Category

Severity

Forwarding state of interface <if_name> has been changed to <state>

MSDP

Info

Description

MSDP Source Interface operational status

Event ID: 8603

Message

Category

Severity

MSDP Peer <peer_ip>(<tcp_entity>) with connection source <if_name> has entered <state>
state

MSDP

Info

Description

Logs the changes in MSDP Peer connection state.

Event ID: 8604

Message

Category

Severity

Port <port> is <status> to MSDP Peer <peer_ip>

MSDP

Info

Description

Log event when port is added or deleted for a peer.

Event ID: 8606

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

243

Message

Category

Severity

{status} peer {peer_ip} on VRF {vrf_name} with connect source {if_name}

MSDP

Info

Description

Log event when peer is enabled or disabled

Event ID: 8607

Message

Category

Severity

Start <tcp_entity> role for MSDP peer <peer_ip>

MSDP

Info

Description

Log event when client or server is elected

Event ID: 8608

Message

Category

Severity

Finish packet was received on MSDP Peer <peer_ip>

MSDP

Info

Description

Log event when TCP final packet is received.

Event ID: 8609

Message

Failed to add SA Cache entry: S=<src_ip>, G=<grp_ip>, R=<rp_ip> for Peer <peer_ip> as
MSDP SA Cache Limit is reached

Category

MSDP

Severity

Warning

Description

Log event when MSDP SA cache limit is reached.

Event ID: 8610

Message

Category

Severity

Hold timer expired for MSDP peer {peer_ip} on VRF {vrf_name}

MSDP

Info

Description

Log event when MSDP peer hold timer expired

MSDP events | 244

Chapter 85
|         |               |          | Message | Session | Relay Protocol | events |
| ------- | ------------- | -------- | ------- | ------- | -------------- | ------ |
| Message | Session Relay | Protocol | events  |         |                |        |
ThefollowingaretheeventsrelatedtoMessageSessionRelayProtocol(MSRP).
| Event ID:   | 15501                                      |     |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- | --- |
| Message     | MSRPstream{streamid}createdonport{name}    |     |     |     |     |     |
| Category    | MessageSessionRelayProtocol                |     |     |     |     |     |
| Severity    | Info                                       |     |     |     |     |     |
| Description | EventreportedwhenMSRPstreamiscreated       |     |     |     |     |     |
| Event ID:   | 15502                                      |     |     |     |     |     |
| Message     | MSRPstream{streamid}deleted                |     |     |     |     |     |
| Category    | MessageSessionRelayProtocol                |     |     |     |     |     |
| Severity    | Info                                       |     |     |     |     |     |
| Description | EventreportedwhenMSRPstreamisdeleted       |     |     |     |     |     |
| Event ID:   | 15503                                      |     |     |     |     |     |
| Message     | MSRPisactiveonport{port}                   |     |     |     |     |     |
| Category    | MessageSessionRelayProtocol                |     |     |     |     |     |
| Severity    | Info                                       |     |     |     |     |     |
| Description | EventreportedwhenMSRPbecomesactiveonport   |     |     |     |     |     |
| Event ID:   | 15504                                      |     |     |     |     |     |
| Message     | MSRPisinactiveonport{port}dueto{status}    |     |     |     |     |     |
| Category    | MessageSessionRelayProtocol                |     |     |     |     |     |
| Severity    | Info                                       |     |     |     |     |     |
| Description | EventreportedwhenMSRPbecomesinactiveonport |     |     |     |     |     |
| Event ID:   | 15505                                      |     |     |     |     |     |
245
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

MSRP Stream {streamid} Talker has left

Message Session Relay Protocol

Info

Description

Event reported when MSRP Talker leave

Event ID: 15506

Message

Category

Severity

MSRP Stream {streamid} Listener connected on port {name} has left

Message Session Relay Protocol

Info

Description

Event reported when MSRP Listener leave

Event ID: 15507

Message

Category

Severity

Resource allocation status for stream {streamid} on port {name} is {status}

Message Session Relay Protocol

Info

Description

Event reported when resource allocation status is updated for an MSRP stream

Event ID: 15508

Message

Category

Severity

Resource de-allocated for stream {streamid} on port {name}

Message Session Relay Protocol

Info

Description

Event reported when resource de allocated for an MSRP stream

Event ID: 15509

Message

Category

Severity

Resource allocation requested for stream {streamid} on port {name}

Message Session Relay Protocol

Info

Description

Event reported when resource allocation requested for an MSRP stream

Event ID: 15510

Message

Resource de-allocation requested for stream {streamid} on port {name} due to {reason}

Message Session Relay Protocol events | 246

Category

Message Session Relay Protocol

Severity

Info

Description

Event reported when resource de alloc requested for an MSRP stream

Event ID: 15511

Message

MSRP Listener added with declaration-type {decl_type} for stream {streamid} on port
{name}

Category

Message Session Relay Protocol

Severity

Info

Description

Event reported when listener gets added for an MSRP stream

Event ID: 15512

Message

MSRP Listener declaration-type changed to {decl_type} for stream {streamid} on port
{name}

Category

Message Session Relay Protocol

Severity

Info

Description

Event reported when listener declaration-type changes for an MSRP stream

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

247

|           |         |        |           | Chapter | 86     |
| --------- | ------- | ------ | --------- | ------- | ------ |
|           |         |        | Multicast | HelperD | events |
| Multicast | HelperD | events |           |         |        |
ThefollowingaretheeventsrelatedtoMulticastHelperD.
| Event ID: | 15901 |                                          |     |     |     |
| --------- | ----- | ---------------------------------------- | --- | --- | --- |
| Message   |       | {rep_mode}vxlanreplicationmodeis{status} |     |     |     |
| Category  |       | MulticastHelperD                         |     |     |     |
| Severity  |       | Info                                     |     |     |     |
Description Eventraisedwhenvxlanreplicationmodeisconfiguredorapplied
| Event ID: | 15902 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Underlaymulticastvxlanreplicationfloodgrouprangeissetto{flood_group_range}
| Category |     | MulticastHelperD |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Info             |     |     |     |
Description Eventraisedwhenunderlaymulticastvxlanreplicationfloodgrouprangeisset
| Event ID: | 15903 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Underlaymulticastvxlanreplicationforvni{vni_id}floodgroupipissetto{flood_group_
ip}via{ip_assign_method}
| Category |     | MulticastHelperD |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Info             |     |     |     |
Description Eventraisedwhenunderlaymulticastvxlanreplicationfloodgroupipisset
| Event ID: | 15904 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Underlaymulticastvxlanreplicationtunnel{encap_type}pim_bidirstateforfloodgroup
{flood_group_ip}is{state}
| Category |     | MulticastHelperD |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- |
| Severity |     | Info             |     |     |     |
Description Eventraisedwhenunderlaymulticastvxlanreplicationtunnelpimbidirstatechanges
| Event ID: | 15905 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
248
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Underlay multicast vxlan replication tunnel {encap_type} pim_bidir underlay l3 port for
flood group {flood_group_ip} is set to {ulay_l3_port}

Category

Multicast HelperD

Severity

Info

Description

Event raised when underlay multicast vxlan replication tunnel pim bidir underlay l3 port
is updated

Event ID: 15906

Message

Underlay multicast vxlan replication tunnel encapsulation underlay l2 port for flood
group {flood_group_ip} is set to {ulay_l2_port}

Category

Multicast HelperD

Severity

Info

Description

Event raised when underlay multicast vxlan replication tunnel underlay l2 port is updated

Event ID: 15907

Message

Underlay multicast vxlan replication tunnel {encap_type} hardware status for flood group
{flood_group_ip} is {hw_status}

Category

Multicast HelperD

Severity

Info

Description

Event raised when underlay multicast vxlan replication tunnel hardware status is
updated

Event ID: 15908

Message

Underlay multicast vxlan replication tunnel encapsulation isl forwarding rule for flood
group {flood_group_ip} is set to {isl_rule}

Category

Multicast HelperD

Severity

Info

Description

Event raised when underlay multicast vxlan replication tunnel encap isl forwarding rule is
updated

Event ID: 15909

Message

Category

Severity

Event raised when error occurs while changing the vxlan replication mode

Multicast HelperD

Error

Description

Error while changing the replication mode to {rep_mode}

Event ID: 15910

Multicast HelperD events | 249

Message

Category

Severity

Description

Event ID: 15911

Message

Category

Severity

Underlay-multicast flood group range given {flood_group_range} is invalid

Multicast HelperD

Error

Event raised when given flood group range for unerlay multicast vxlan replication mode
is invalid

Underlay-multicast flood group ip {flood_group_ip} is invalid

Multicast HelperD

Error

Description

Event raised when given flood group ip for unerlay multicast vxlan replication is invalid

Event ID: 15912

Message

Underlay multicast vxlan replication tunnel {encap_type} operational state for flood
group {flood_group_ip} is {oper_state}

Category

Multicast HelperD

Severity

Info

Description

Event raised when underlay multicast vxlan replication tunnel operational state is
updated

Event ID: 15913

Message

Resource exhausted for underlay multicast vxlan replication for override group ip
{override_group_ip}

Category

Multicast HelperD

Severity

Error

Description

Event raised when resource exhausted for underlay multicast vxlan replication.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

250

Multicast Traffic Manager events

Chapter 87

Multicast Traffic Manager events

The following are the events related to Multicast Traffic Manager.

Event ID: 4001

Message

The Multicast L3 Bridge Control Forwarding entries limit was reached: <limit>' throttle_
count: 100

Category

Multicast Traffic Manager

Severity

Warning

Description

Event raised when the maximum number of multicast L3 Bridge Control Forwarding
entries is reached

Event ID: 4002

Message

{mgmd_type} snooping filter unknown mcast feature will be {status}.

Category

Multicast Traffic Manager

Severity

Info

Description

Logged when mgmd snooping filter unknown mcast feature enablement or removal
status in MTM

Event ID: 4003

Message

Failed to {status} {mgmd_type} snooping filter unknown mcast feature.

Category

Multicast Traffic Manager

Severity

Error

Description

Logged when error occurs while updating mgmd snooping filter unknown mcast entry
into cpurx table.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

251

|         |         |                |         |                | Chapter | 88     |
| ------- | ------- | -------------- | ------- | -------------- | ------- | ------ |
|         |         | Message        | Session | Relay Protocol | (MSRP)  | events |
| Message | Session | Relay Protocol | (MSRP)  | events         |         |        |
ThefollowingaretheeventsrelatedtoMessageSessionRelayProtocol(MSRP).
| Event ID: | 2001 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message
MSTPEnabled
| Category |     | Multiplespanningtreeprotocol |     |     |     |     |
| -------- | --- | ---------------------------- | --- | --- | --- | --- |
| Severity |     | Info                         |     |     |     |     |
Description ThiscommandenablestheMSTP(MultipleSpanning-treeProtocol)featureinthedevice.
| Event ID: | 2002 |                              |     |     |     |     |
| --------- | ---- | ---------------------------- | --- | --- | --- | --- |
| Message   |      | MSTPDisabled                 |     |     |     |     |
| Category  |      | Multiplespanningtreeprotocol |     |     |     |     |
| Severity  |      | Info                         |     |     |     |     |
Description ThiscommanddisablestheMSTP(MultipleSpanning-treeProtocol)featureinthedevice.
| Event ID: | 2003 |                                   |     |     |     |     |
| --------- | ---- | --------------------------------- | --- | --- | --- | --- |
| Message   |      | <config_parameter>shouldbe<value> |     |     |     |     |
| Category  |      | Multiplespanningtreeprotocol      |     |     |     |     |
| Severity  |      | Warning                           |     |     |     |     |
Description ThislogeventinformstheuserthattheMSTPconfigparameterisbad
| Event ID: | 2004 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message
BPDUhas<config_parameter>fromport<value>
| Category |     | Multiplespanningtreeprotocol |     |     |     |     |
| -------- | --- | ---------------------------- | --- | --- | --- | --- |
| Severity |     | Warning                      |     |     |     |     |
Description ThislogeventinformstheuserthattheSwitchreceivedaBPDUwithabadconfig
| Event ID: | 2005 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
252
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Bad reconfiguration request: <reconfig_parameter>

Category

Multiple spanning tree protocol

Severity

Warning

Description

This log event informs the user that the MSTP reconfig parameter is bad

Event ID: 2006

Message

<proto> - Root changed from <old_priority>: <old_mac> to <new_priority>: <new_mac>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the MSTP root has changed

Event ID: 2007

Message

Port <port> disabled - BPDU received on protected port

Category

Multiple spanning tree protocol

Severity

Warning

Description

This log event informs the user that BPDU was received on protected port

Event ID: 2008

Message

<proto> starved for <pkt_type> on port <port> from <priority_mac>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the Rx queue is starved in the paticular port

Event ID: 2009

Message

BPDU loss- port <port> moved to inconsistent state for <proto>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the port is in inconsistent state

Event ID: 2010

Message

Port <port> moved out of inconsistent state for <proto>

Message Session Relay Protocol (MSRP) events | 253

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the MSTP is out of inconsistent state

Event ID: 2011

Message

Topology Change received on port <port> for <proto> from source: <mac>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the MSTP topology change is received

Event ID: 2012

Message

<proto> - Topology Change generated on port <port> going in to <state>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the MSTP topology change is generated

Event ID: 2013

Message

BPDU received on admin edge port <port>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that a BPDU was received on admin edge port

Event ID: 2014

Message

Port <port> blocked on CIST

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the CIST port is blocked

Event ID: 2015

Message

Port <port> unblocked on CIST

Category

Multiple spanning tree protocol

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

254

Severity

Info

Description

This log event informs the user that the CIST port is unblocked

Event ID: 2016

Message

Port <port> blocked on MST<instance>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the MSTI port is blocked

Event ID: 2017

Message

Port <port> unblocked on MST<instance>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the MSTI port is unblocked

Event ID: 2018

Message

<proto> Root Port changed from <old_port> to <new_port>

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the root port is changed

Event ID: 2019

Message

spanning tree mode changed from <old_mode> to <new_mode>, it will trigger the
reconvergence

Category

Multiple spanning tree protocol

Severity

Info

Description

This log event informs the user that the spanning tree mode is changed.

Message Session Relay Protocol (MSRP) events | 255

Chapter 89

MVRP events

MVRP events

The following are the events related to MVRP.

Event ID: 3101

Message

MVRP enabled on port <port>

Category

MVRP

Severity

Information

Description

This command enables the MVRP (Multiple VLAN Registration Protocol) feature on
interface.

Event ID: 3102

Message

MVRP disabled on port <port>

Category

MVRP

Severity

Information

Description

This command disables the MVRP (Multiple VLAN Registration Protocol) feature on
interface.

Event ID: 3103

Message

MVRP failed to create VLAN <vlan>. Maximum VLANs <max_vlan> already created'
throttle_count: 100

Category

MVRP

Severity

Information

Description

This log event informs user that the vlan create is failed.

Event ID: 3104

Message

MVRP statistics have been cleared for port <port>

Category

MVRP

Severity

Information

Description

This log event informs user that the mvrp statistics have been cleared.

Event ID: 3105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

256

Message

MVRP statistics have been cleared for <port> ports

Category

MVRP

Severity

Information

Description

This log event informs user that the mvrp statistics have been cleared.

MVRP events | 257

Chapter 90

NAE Agents events

NAE Agents events

The following are the events related to NAE agents.

Event ID: 6901

Message

An action has been triggered by the NAE agent <name>': yes

Category

NAE Agents

Severity

Info

Description

Action has been triggered by an NAE agent

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

258

Chapter 91

NAE events

NAE events

The following are the events related to Network Analytics Engine.

Event ID: 6001

Message

NAE agent <name> started to collect samples from <uri>.

Category

NAE

Severity

Information

Description

NAE agent started to collect samples.

Event ID: 6002

Message

NAE agent <name> stopped to collect samples from <uri>.

Category

NAE

Severity

Information

Description

NAE agent stooped to collect samples.

Event ID: 6003

Message

Category

Severity

NAE agent <name> with URI <uri> has error and cannot collect samples.

NAE

Error

Description

NAE agent with URI has error and cannot collect samples.

Event ID: 6004

Message

NAE agent <name> is watching for condition <condition>.

Category

NAE

Severity

Information

Description

NAE agent is watching for condition.

Event ID: 6005

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

259

Message

NAE agent <name> stopped to watch for condition <condition>.

Category

NAE

Severity

Information

Description

NAE agent stopped to watch for condition.

Event ID: 6006

Message

Category

Severity

NAE agent <name> with condition <condition> has error and is not watched.

NAE

Error

Description

NAE agent with condition has error and is not watched.

Event ID: 6007

Message

NAE agent <name> generated an alert based on condition <condition>.

Category

NAE

Severity

Information

Description

NAE agent generated an alert based on condition.

Event ID: 6008

Message

NAE experiencing a spike in data points to process for NAE monitor <monitorName>. NAE
will temporarily stop monitoring new data points for <monitorName>.

Category

NAE

Severity

Warning

Description

NAE experiencing a spike in data points to process. Temporarily disabling processing
updates from specific NAE monitor.

Event ID: 6009

Message

NAE resuming to monitor data points from NAE monitor <monitorName>

Category

NAE

Severity

Information

Description

NAE resuming to monitor data points from specific NAE monitor.

Event ID: 6010

NAE events | 260

Message

User <user> has cleard NAE time series database

Category

NAE

Severity

Information

Description

Logs a message when a user clears the NAE time series database

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

261

Chapter 92
|            |            |        | NAE script | generation | events |
| ---------- | ---------- | ------ | ---------- | ---------- | ------ |
| NAE script | generation | events |            |            |        |
ThefollowingaretheeventsrelatedtoNAEscriptgeneration.
| Event ID: | 12701 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message
NAEagent<agent>creationfailed.Reason<reason>
| Category    | NAEscriptgeneration    |     |     |     |     |
| ----------- | ---------------------- | --- | --- | --- | --- |
| Severity    | Error                  |     |     |     |     |
| Description | NAEagentcreationfailed |     |     |     |     |
262
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 93

NAE Scripts events

NAE Scripts events

The following are the events related to Network Analytics Engine scripts.

Event ID: 5501

Message

NAE script <name> has been validated.

Category

NAE Scripts

Severity

Information

Description

NAE script has been validated.

Event ID: 5502

Message

Error found in NAE Script <name>.

Category

NAE Scripts

Severity

Error

Description

Error found in NAE Script.

Event ID: 5503

Message

Error found in NAE Agent <name>.

Category

NAE Scripts

Severity

Error

Description

Error found in NAE Agent.

Event ID: 5504

Message

Error executing NAE action <action_type> belonging to condition <condition> and agent
<agent> due to <description>.

Category

NAE Scripts

Severity

Error

Description

NAE Action error.

Event ID: 5505

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

263

Message

NAE Script <name> has been created by the system.

Category

NAE Scripts

Severity

Information

Description

NAE Script has been created by the system.

Event ID: 5506

Message

NAE Agent <name> has been created by the system.

Category

NAE Scripts

Severity

Information

Description

NAE Agent has been created by the system.

Event ID: 5507

Message

<msg>

Category

NAE Scripts

Severity

Information

Description

Log event when instantiated from active NAE agent.

Event ID: 5508

Message

<msg>

Category

NAE Scripts

Severity

Information

Description

Log event when instantiated from active NAE agent.

Event ID: 5509

Message

<msg>

Category

NAE Scripts

Severity

Critical

Description

Log event when instantiated from active NAE agent.

Event ID: 5510

Message

<msg>

NAE Scripts events | 264

| Category    | NAEScripts                                  |            |
| ----------- | ------------------------------------------- | ---------- |
| Severity    | Error                                       |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5511                                    |            |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Warning                                     |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5512 (Severity:                         | Emergency) |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Emergency                                   |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5513 (Severity:                         | Emergency) |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Emergency                                   |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5514                                    |            |
Message
<msg>
| Category    | NAEScripts                                  |     |
| ----------- | ------------------------------------------- | --- |
| Severity    | Debug                                       |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries) 265

Chapter 94

ND snooping events

ND snooping events

The following are the events related to ND snooping.

Event ID: 8401

Message

All the dynamic binding entries were cleared.

Category

ND snooping

Severity

Information

Description

Log event when all dynamic binding entries are cleared.

Event ID: 8402

Message

Dynamic binding entries on the port <port> were cleared.

Category

ND snooping

Severity

Information

Description

Log event when all dynamic binding entries on a port are cleared.

Event ID: 8403

Message

Dynamic binding entries on the VLAN <vid> were cleared.

Category

ND snooping

Severity

Information

Description

Log event when all dynamic binding entries on a vlan are cleared.

Event ID: 8404

Message

Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.

Category

ND snooping

Severity

Information

Description

Log event when a specific dynamic binding entry on a vlan is cleared.

Event ID: 8405

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

266

Message

ND packet of type=<type> received on port:<port> vlan:<vlan> with src_mac:<src_mac> is
<status>. count=<count>

Category

ND snooping

Severity

Information

Description

Log event when ND packet received on port.

ND snooping events | 267

Chapter 95

NDM events

NDM events

The following are the events related to NDM.

Event ID: 6101

Message

Category

Severity

Static Neighbor <ip> created on Port <port>, VRF <vrf> mac <mac>

NDM

Info

Description

Static neighbor created

Event ID: 6102

Message

Category

Severity

Static Neighbor <ip> deleted on Port <port>, VRF <vrf> and mac <mac>

NDM

Info

Description

Static neighbor deleted

Event ID: 6103

Message

Category

Severity

Static Neighbor <ip> modified on Port <port> and VRF <vrf> from mac <old_mac> to new
mac <new_mac>

NDM

Info

Description

Static neighbor modified

Event ID: 6104

Message

Category

Severity

IPDB neighbor <ip> added in port <port>, VRF <vrf>

NDM

Info

Description

IPDB neighbor added to the neighbor Table

Event ID: 6105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

268

Message

Category

Severity

IPDB Neighbor <ip> Deleted

NDM

Info

Description

IPDB neighbor deleted from the neighbor Table

Event ID: 6106

Message

Category

Severity

Clear all Arp entries requested on Port <port> and VRF <vrf>

NDM

Info

Description

Clear all arp entries requested on Specific Port

Event ID: 6107

Message

Category

Severity

Clear all VSX Peer ARP entries requested on Port <port> and vrf <vrf>

NDM

Info

Description

Clear all VSX Peer ARP entries requested on Specific Port

Event ID: 6108

Message

Category

Severity

Clear all Arp entries requested on VRF <vrf>

NDM

Info

Description

Clear all arp entries requested on Specific VRF

Event ID: 6109

Message

Category

Severity

Clear all VSX Peer Arp entries requested on VRF <vrf>

NDM

Info

Description

Clear all VSX Peer arp entries requested on Specific VRF

Event ID: 6110

Message

Clear all Arp entries requested

NDM events | 269

Category

Severity

NDM

Info

Description

Clear all arp entries requested

Event ID: 6111

Message

Category

Severity

Clear all VSX Peer Arp entries requested

NDM

Info

Description

Clear all VSX Peer arp entries requested

Event ID: 6112

Message

Category

Severity

EVPN Virtual Tunnel EndPoint Neighbor <ip> added to Port<port> on VRF <vrf>

NDM

Info

Description

EVPN Virtual Tunnel EndPoint Neighbor added to the neighbor table

Event ID: 6113

Message

Category

Severity

EVPN Virtual Tunnel EndPoint Neighbor <ip> updated on Port<port> and VRF <vrf> with
mac <mac>

NDM

Info

Description

EVPN Virtual Tunnel EndPoint Neighbor Updated in the neighbor table

Event ID: 6114

Message

Category

Severity

EVPN VTEP Neighbor <ip> deleted from Port<port> and VRF <vrf>

NDM

Info

Description

EVPN VTEP Neighbor deleted from the neighbor table

Event ID: 6115

Message

Management Role set to <role>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

270

Category

Severity

NDM

Info

Description

Processing Redundancy management

Event ID: 6116

Message

Category

Severity

Management role changed from old <role1> to new role <role2>

NDM

Info

Description

Management role changed to new role

Event ID: 6117

Message

Category

Severity

IPv4 neighbor ageout time changed to <time> seconds on port <port>

NDM

Info

Description

IPv4 neighbor ageout time changed to new value

Event ID: 6118

Message

Category

Severity

IPv6 neighbor ageout time changed to <time> seconds on port <port>

NDM

Info

Description

IPv6 neighbor ageout time changed to new value

Event ID: 6119

Message

Category

Severity

VSX neighbor datapath init sync status is neighbor sync completed

NDM

Info

Description

VSX neighbor datapath init sync status is neighbor sync completed

Event ID: 6120

Message

VSX neighbor datapath init sync status is neighbor sync in progress

Category

NDM

NDM events | 271

Severity

Info

Description

VSX neighbor datapath init sync status is neighbor sync in progress

Event ID: 6121

Message

Category

Severity

static neighbor <ip> add failed, Subnet match failed

NDM

Error

Description

Static Neighbor add failed, subnet not matched

Event ID: 6122

Message

Category

Severity

static neighbor <ip> add failed, it is own ip

NDM

Error

Description

Static Neighbor add failed, it is own ip

Event ID: 6123

Message

Category

Severity

static neighbor <ip> Subnet match add failed, port is down

NDM

Error

Description

Static Neighbor add failed, port is down

Event ID: 6124

Message

Category

Severity

Neighbor table VSX peer DB connection terminated

NDM

Info

Description

Neighbor table VSX peer DB connection terminated

Event ID: 6125

Message

Category

Severity

Neighbor table VSX peer DB connection established

NDM

Info

Description

Neighbor table VSX peer DB connection established

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

272

Event ID: 6126

Message

Category

Severity

VSX Peer IP <ip> added the port <port> and VRF <vrf>

NDM

Info

Description

VSX Peer IP added in port vsxPeerIpCache

Event ID: 6127

Message

Category

Severity

VSX Peer IP <ip> deleted from the port <port> and VRF <vrf>

NDM

Info

Description

VSX Peer IP deleted in port vsxPeerIpCache

Event ID: 6128

Message

Category

Severity

Proxy arp enabled for the port <port>

NDM

Info

Description

Proxy arp enabled for the given interface

Event ID: 6129

Message

Category

Severity

Proxy arp disabled for the port <port>

NDM

Info

Description

Proxy arp diabled for the given interface

Event ID: 6130

Message

Category

Severity

Neighbor <ip> modified on Port <port> and VRF <vrf> from mac <old_mac> to new mac
<new_mac>

NDM

Info

Description

Neighbor modified

Event ID: 6131

NDM events | 273

Message

Category

Severity

Neighbor Discovery daemon started

NDM

Info

Description

Neighbor Discovery daemon started

Event ID: 6132

Message

Category

Severity

Duplicate IPv6 address {ip} is detected on interface {port} with a MAC address of {mac}

NDM

Error

Description

Duplicate IP detected from ARP reply

Event ID: 6133

Message

Category

Severity

Duplicate IPv6 address <ip> is detected on port <port> with a MAC address of <mac>

NDM

Error

Description

Duplicate IPv6 address detected from Neighbour advertisement

Event ID: 6134

Message

Category

Severity

Duplicate IPv4 address <ip> is detected on port <port> with a MAC address of <mac>'
throttle_count: 40

NDM

Error

Description

Duplicate IP detected from ARP request

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

274

Chapter 96

NTP events

NTP events

The following are the events related to NTP.

Event ID: 1101

Message

NTP Association <event>: <server> <server_info>

Category

NTP

Severity

Information

Description

Logs NTP Association configuration changes

Event ID: 1102

Message

NTP Trusted keys <trusted_keys> and Untrusted keys <untrusted_keys>

Category

NTP

Severity

Information

Description

Logs NTP Trusted and Untrusted authentication-keys

Event ID: 1103

Message

NTP Authentication state change: <old> -> <new>

Category

NTP

Severity

Information

Description

Logs NTP Authentication state changes

Event ID: 1104

Message

NTP VRF state change: <old> -> <new>

Category

NTP

Severity

Information

Description

Logs NTP VRF configuration state changes

Event ID: 1105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

275

Message

NTP primary server connection established to <server>

Category

NTP

Severity

Information

Description

Logs NTP primary server connection established state change

Event ID: 1106

Message

NTP primary server connection lost to <server>

Category

NTP

Severity

Information

Description

Logs NTP primary server connection lost state change

Event ID: 1107

Message

NTP enable state change: <old> -> <new>

Category

NTP

Severity

Information

Description

Event raised when NTP is changed to enabled or disabled

NTP events | 276

Chapter 97

OSPFv2 events

OSPFv2 events

The following are the events related to OSPFv2.

Event ID: 2401

Message

AdjChg: Nbr <router-id> on <ospf-interface>(<area>): <old_state> -> <new_state>

Category

OSPFv2

Severity

Info

Description

Logs the changes in OSPFv2 neighbour state machine.

Event ID: 2402

Message

Interface <interface>(<area>) changed from <old_state> to <new_state>, input: <input>

Category

OSPFv2

Severity

Info

Description

Logs the changes in the interface FSM state.

Event ID: 2403

Message

<event> with <destination> <nexthops>

Category

OSPFv2

Severity

Info

Description

Logs OSPFv2 route add and delete.

Event ID: 2404

Message

AdjChg: Nbr <router-id> on <ospf-interface>: <state> -> <next_state> (<event>)

Category

OSPFv2

Severity

Info

Description

Logs the changes in OSPFv2 neighbour state machine.

Event ID: 2405

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

277

Message

Router-id updated from <old> to <new>

Category

OSPFv2

Severity

Info

Description

Logs the changes in the router-id.

Event ID: 2406

Message

Category

Severity

Failed to <action> <rule> error: <err>

OSPFv2

Error

Description

Logs errors for OSPFv2 FP creation/installation.

Event ID: 2407

Message

OSPF all routers field entry added: group_id=<group_id> fp_id=<fp_id> stat_id=<stats_id>

Category

OSPFv2

Severity

Info

Description

Logs for OSPFv2 FP creation/installation.

Event ID: 2408

Message

OSPF designated routers field entry added: group_id=<group_id> fp_id=<fp_id> stat_
id=<stats_id>

Category

OSPFv2

Severity

Info

Description

Logs for OSPFv2 DR FP creation/installation.

Event ID: 2409

Message

Graceful Restart state changed, <old_state> -> <new_state>, reason: <reason>

Category

OSPFv2

Severity

Info

Description

Logs the changes of OSPFv2 Graceful Restart state.

Event ID: 2410

OSPFv2 events | 278

Message

Category

Severity

Duplicate router-id for <ospf-interface> from source <source-ip>

OSPFv2

Error

Description

Logs when router-id is duplicate.

Event ID: 2411

Message

Distance External <external>, Inter-area <inter>, and Intra-area <intra> applied to all the
OSPF processes {process-id} in <vrf> VRF

Category

OSPFv2

Severity

Info

Description

Logs the changes of OSPFv2 distance.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

279

Chapter 98

OSPFv3 events

OSPFv3 events

The following are the events related to OSPFv3.

Event ID: 4901

Message

Category

Severity

Failed to <action> <rule> error: <err>

OSPFv3

Error

Description

Logs errors for OSPFv3 FP creation/installation.

Event ID: 4902

Message

OSPF3 all routers field entry added: group_id=<group_id> fp_id=<fp_id> stat_id=<stats_id>

Category

OSPFv3

Severity

Info

Description

Logs for OSPFv3 FP creation/installation.

Event ID: 4903

Message

OSPF3 designated routers field entry added: group_id=<group_id> fp_id=<fp_id> stat_
id=<stats_id>

Category

OSPFv3

Severity

Info

Description

Logs for OSPFv3 DR FP creation/installation.

Event ID: 4904

Message

AdjChg: Nbr<router-id> on interface <link-local> on <interface>(<area>): <old_state> ->
<new_state>

Category

OSPFv3

Severity

Info

Description

Logs the changes in OSPFv3 neighbour state machine.

Event ID: 4905

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

280

Message Interface<link-local>on<interface>(<area>)changedfrom<old_state>to<new_state>,
input:<input>
| Category    | OSPFv3                                |     |
| ----------- | ------------------------------------- | --- |
| Severity    | Info                                  |     |
| Description | LogsthechangesintheinterfaceFSMstate. |     |
| Event ID:   | 4906                                  |     |
Message GracefulRestartstatechanged,<old_state>-><new_state>,reason:<reason>
| Category    | OSPFv3                                      |     |
| ----------- | ------------------------------------------- | --- |
| Severity    | Info                                        |     |
| Description | LogsthechangesofOSPFv3GracefulRestartstate. |     |
| Event ID:   | 4907                                        |     |
Message
Duplicaterouter-idfor<link-local>fromsource<source-ip>
| Category    | OSPFv3                        |     |
| ----------- | ----------------------------- | --- |
| Severity    | Error                         |     |
| Description | Logswhenrouter-idisduplicate. |     |
| Event ID:   | 4908                          |     |
Message DistanceExternal<external>,Inter-area<inter>,andIntra-area<intra>appliedtoallthe
{OSPFv3process-id}processesin<vrf>VRF
| Category    | OSPFv3                          |        |
| ----------- | ------------------------------- | ------ |
| Severity    | Info                            |        |
| Description | LogsthechangesofOSPFv3distance. |        |
| Packet      | capture                         | events |
Thefollowingaretheeventsrelatedtopacketcapturesessions.
| Event ID:   | 15201                                        |     |
| ----------- | -------------------------------------------- | --- |
| Message     | capturefailedtostartthesession{session_name} |     |
| Category    | Packetcapture                                |     |
| Severity    | Error                                        |     |
| Description | Eventraisedwhenpacketcaptureisfailedtostart  |     |
Packetcaptureevents|281

Event ID: 15202

Message

Category

Severity

Packet capture failed to stop the session {session_name}

Packet capture

Error

Description

Event raised when packet capture is failed to stop

Event ID: 15203

Message

Category

Severity

Packet capture started for the session {session_name}

Packet capture

Info

Description

Event raised when packet capture is started

Event ID: 15204

Message

Category

Severity

Packet capture stopped for the session {session_name}

Packet capture

Info

Description

Event raised when packet capture is stopped

Event ID: 15205

Message

Category

Severity

Packet capture session {session_name} client state set to initializing

Packet capture

Info

Description

Packet capture session row client state set to initializing

Event ID: 15206

Message

Category

Severity

Packet capture session {session_name} client state set to in-progress

Packet capture

Info

Description

acket capture session row client state set to in-progress

Event ID: 15207

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

282

Message

Category

Severity

acket capture session {session_name} client state set to completed

Packet capture

Info

Description

Packet capture session row client state set to completed

Event ID: 15208

Message

Category

Severity

Packet capture session {session_name} client state set to hw failed

Packet capture

Error

Description

Packet capture session row client state set to hw failed

Event ID: 15209

Message

Category

Severity

Packet capture session {session_name} client state set to connection failed

Packet capture

Error

Description

Packet capture session row client state set to conection failed

Event ID: 15210

Message

Category

Severity

Packet capture session {session_name} hw programmed is {value}

Packet capture

Info

Description

Packet capture session row hw programmed value

Event ID: 15211

Message

Category

Severity

Packet capture session {session_name} max timeout reached

Packet capture

Info

Description

Packet capture session row client state set to completed due to max time out

Event ID: 15212

Message

Packet capture session {session_name} max packet transmitted

Packet capture events | 283

Category

Packet capture

Severity

Info

Description

Packet capture session row client state set to completed due to max packet transmitted

Event ID: 15213

Message

Category

Severity

Packet capture configuration error for session {session_name}, reason : {reason}

Packet capture

Error

Description

Event raised when packet capture configuration is invalid

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

284

Chapter 99

Password Reset events

Password Reset events

The following are the events related to password reset.

Event ID: 5901

Message

Password reset succeeded for admin user.

Category

Password Reset

Severity

Information

Description

Log message when admin user password reset is successful

Event ID: 5902

Message

Password reset failed for admin user.

Category

Password Reset

Severity

Information

Description

Log message when admin user password reset fails

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

285

Chapter 100

PIM events

PIM events

The following are the events related to PIM.

Event ID: 5101

Message

Category

Severity

Failed to send <pkt_type> packet on Interface <InterfaceName>' throttle_count: 100

PIM

Error

Description

Send error packet

Event ID: 5102

Message

Category

Severity

PIM interface <InterfaceName> is configured with IP <ip_address>

PIM

Info

Description

Pim IP config

Event ID: 5103

Message

Category

Severity

Packet dropped from <ip_address> on interface <InterfaceName> <error> <value>' throttle_
count: 100

PIM

Error

Description

Packet dropped

Event ID: 5104

Message

Category

Severity

Received packet from router <ip_address>, unkwn pkt type <pkt_type>' throttle_count: 100

PIM

Error

Description

Received packet from router

Event ID: 5105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

286

Message

Category

Severity

Failed to add flow <dip0>.<dip1>.<dip2>.<dip3>, <sip0>.<sip1>.<sip2>.<sip3> (<status>
<srcport> <srcvid> <totalvid> <flowtype> <callerid>)

PIM

Error

Description

Failed to add flow

Event ID: 5106

Message

Category

Severity

Failed to remove flow g <dip0>.<dip1>.<dip2>.<dip3>, s <sip0>, <sip1>.<sip2>.<sip3>
(<status> <srcport> <srcvid> <flowtype> <callerid>)

PIM

Error

Description

Failed to remove flow for Hardware

Event ID: 5107

Message

Failed to add a mroute for s=<source>, g=<group> on interface <interfaceName> as the
configured mroute limits are reached' throttle_count: 100

Category

PIM

Severity

Warning

Description

Failed to program mroute as the limits are reached

Event ID: 5108

Message

Failed to add a mroute for s=<source>, g=<group> on interface <interfaceName> as the
configured sources per group limit is reached' throttle_count: 100

Category

PIM

Severity

Warning

Description

Failed to program mroute as the sources per group limit is reached

Event ID: 5109

Message

Category

Severity

This router is elected as the <ip_version> <state> for interface <ifname>

PIM

Info

Description

PIM DR election log

Event ID: 5110

PIM events | 287

Message

Category

Severity

<type> <reason> failed with Fd: <fd> on Port: <port>. Error description: <err>

PIM

Error

Description

Multicast socket creation error

Event ID: 5111

Message

Category

Severity

OVSDB operation failed with <err>' throttle_count: 100

PIM

Error

Description

DB Operation failed

Event ID: 5112

Message

Category

Severity

New Elected BSR for VRF <vrf_name> is <ebsr_ip> with priority <priority>

PIM

Info

Description

Elected BSR

Event ID: 5113

Message

Category

Severity

Elected BSR removed on VRF <vrf_name>

PIM

Info

Description

Elected BSR removed

Event ID: 5114

Message

Category

Severity

Candidate BSR <ip_address> with priority <priority> is <status> on interface <ifname>

PIM

Info

Description

Configured candidate BSR

Event ID: 5115

Message

PIM Neighbor <neighbor_ip> is <event> on interface <ifname>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

288

Category

Severity

PIM

Info

Description

Neighbor status

Event ID: 5116

Message

<pkt> packet is discarded on interface <ifname>. Reason: <reason>' throttle_count: 100

Category

PIM

Severity

Warning

Description

Packet drop

Event ID: 5117

Message

Category

Severity

Forwarding state has changed to <state> on <ip_version> enabled interface <ifname>

PIM

Info

Description

Interface operational status

Event ID: 5118

Message

Category

Severity

<pim_version> <mode> mode is <status> on interface <ifname>

PIM

Info

Description

Interface PIM mode

Event ID: 5119

Message

Category

Severity

Router <pim_version> is <mode> on VRF <vrfname>

PIM

Info

Description

Router pim configuration status

Event ID: 5120

Message

Candidate RP <ip_address> is <event> on VRF <vrf_name>

Category

PIM

PIM events | 289

Severity

Info

Description

Learnt or removed candidate RP

Event ID: 5121

Message

Category

Severity

Software Packet Queue <limit> threshold value <val> reached. Queue size: <qsize>

PIM

Info

Description

Software Packet Queue reaches threshold

Event ID: 5122

Message

Category

Severity

This router is elected as the <ip_version> VSX <state> for interface <ifname>

PIM

Info

Description

PIM VSX DR Election log

Event ID: 5123

Message

Category

Severity

VSX ISL Status changed to <isl_status>

PIM

Info

Description

VSX ISL Status update log

Event ID: 5124

Message

Category

Severity

Candidate RP <ip_address> is configured on interface <ifname>

PIM

Info

Description

Configured candidate RP

Event ID: 5125

Message

Category

Severity

BFD Session created for neighbor <ip_address> on interface <ifname>

PIM

Info

Description

BFD Session created

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

290

Event ID: 5126

Message

Category

Severity

BFD Session deleted for neighbor <ip_address> on interface <ifname>

PIM

Info

Description

BFD Session deleted

Event ID: 5127

Message

Category

Severity

Description

Event ID: 5128

Message

Category

Severity

Description

Event ID: 5129

Message

Category

Severity

Description

Event ID: 5130

Message

Category

Severity

PIM Resource utilization of <capacity_type> has reached/exceeded the supported limits on
the system.

PIM

Info

This log event informs the user that PIM resource utilization has exceeded the supported
limits

PIM Resource utilization of <capacity_type> has reached 90 percent of the supported
limits on the system.

PIM

Info

This log event informs the user that PIM resource utilization has reached 90 percent of
the supported limits

PIM Resource utilization of <capacity_type> has dropped below 90 percent of the
supported limits on the system.

PIM

Info

This log event informs the user that PIM resource utilization drops below 90 percent of
the supported limits

Router <pim_version> PIM-SSM is <mode> on VRF <vrfname>

PIM

Info

PIM events | 291

Description

Router PIM-SSM configuration status

Event ID: 5131

Message

Category

Severity

Router <pim_version> PIM-SSM range ACL is <mode> on VRF <vrfname>

PIM

Info

Description

Router PIM-SSM range ACL configuration status

Event ID: 5132

Message

Category

Severity

Description

Event ID: 5133

Message

Category

Severity

Vxlan-tunnel configured with {mode} mode. Border router functionality is {status} on this
router.

PIM

Info

The dynamic VXLAN tunnel bridging mode configured and the Border Gateway status
with respect to PIM.

PIM NSF timer {status} {action_str}

PIM

Info

Description

PIM NSF timer status

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

292

Chapter 101

Policies events

Policies events

The following are the events related to policies.

Event ID: 10101

Message

Category

Severity

Policy <policy_name> failed to apply on <application>

Policies

Error

Description

Policy application failure

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

293

Chapter 102

Port access events

Port access events

The following are the events related to port access.

Event ID: 10501

Message

Category

Severity

Client <mac_address> was logged-off administratively through command-line interface

Port access

Info

Description

Client was logged-off administratively through command-line interface

Event ID: 10502

Message

Category

Severity

Port <port> is blocked by port-access

Port access

Info

Description

The port is blocked by port-access daemon

Event ID: 10503

Message

Category

Severity

Port <port> is unblocked by port-access

Port access

Info

Description

The port is unblocked by port-access daemon

Event ID: 10504

Message

Clients were logged-off on the port <port> due to a change in authentication mode from
<device/client> to client/device>

Category

Port access

Severity

Info

Description

The authentication mode associated with the port is changed

Event ID: 10505

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

294

Message

Clients were logged-off on the port <port> due to a change in client limit from <old_limit>
to <new_limit>

Category

Port access

Severity

Info

Description

The client limit associated with the port is changed

Event ID: 10506

Message

Category

Severity

The name associated with VLAN <vlan_id> changed from <old_name> to <new_name>

Port access

Info

Description

The name associated with a VLAN in use by port-access daemon changed

Event ID: 10507

Message

Clients using policy <policy_name> were logged-off due to a configuration change in the
policy

Category

Port access

Severity

Info

Description

The policy configuration is updated by the user

Event ID: 10508

Message

Category

Severity

Description

Event ID: 10509

Message

Category

Severity

VLAN conflict detected on port <port-name>

Port access

Error

VLAN is configured as Trunk for some clients and access for others. This could potentially
result in traffic loss

Client limit exceeded on port <port>, caused by an unauthenticated client <mac_addr>

Port access

Error

Description

Log event when an intruder is detected on the port

Event ID: 10510

Port access events | 295

Message

All clients except client with MAC address <mac_addr> logged-off on the port <port> due
to a change in authentication mode from <old_mode> to <new_mode>

Category

Port access

Severity

Info

Description

The authentication mode associated with the port is changed

Event ID: 10511

Message

All clients except client with MAC address <mac_addr> logged-off on the port <port> due
to a proxy-logoff request

Category

Port access

Severity

Info

Description

Clients were logged off due to proxy logoff

Event ID: 10512

Message

Category

Severity

Client with MAC address <mac_addr> learnt on port <port-name>

Port access

Info

Description

Received a client for authentication/authorization on secure port

Event ID: 10513

Message

Category

Severity

Client with MAC address <mac_addr> deleted on port <port-name>

Port access

Info

Description

Deleted a port-access client

Event ID: 10514

Message

Client with MAC address <mac_addr> authorized on port <port-name> with role <role-
name>

Category

Port access

Severity

Info

Description

Client authorized with role

Event ID: 10515

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

296

Message

Client with MAC address <mac_addr> on port <port-name> failed <auth-method>
authentication with reason <failure-reason>

Category

Port access

Severity

Info

Description

Client has failed authentication

Event ID: 10516

Message

Client with MAC address <mac_addr> on port <if_name> triggered for MAC authentication
request with ID <request_id>

Category

Port access

Severity

Info

Description

MAC authentication request sent for client

Event ID: 10517

Message

Client with MAC address <mac_addr> on port <if-name> received response for MAC-
Authentication request ID <request-id> as <response>

Category

Port access

Severity

Info

Description

MAC authentication response received for client

Event ID: 10518

Message

Client with MAC address <mac_addr> on port <if-name> triggered for 802.1x
authentication request with ID <request-id>

Category

Port access

Severity

Info

Description

802.1x Authentication response received for client

Event ID: 10519

Message

Client with MAC address <mac_addr> on port <if-name> received response for 802.1x
authentication request ID <request-id> as <response>

Category

Port access

Severity

Info

Description

802.1x Authentication response received for client

Event ID: 10520

Port access events | 297

Message

Reached the maximum cached-clients limit of <limit> on the switch for Limited Auth-
Survivability

Category

Port access

Severity

Info

Description

Port Access cached-client maximum limit reached

Event ID: 10521

Message

Category

Severity

Restored <num-cached-clients> cached-clients from persistent-storage after reboot

Port access

Info

Description

Cached-Clients were recovered from persistent-storage

Event ID: 10522

Message

Category

Severity

Interface <if-name> is flapped by port-access as port of a CoA request

Port access

Info

Description

The port is flapped by port-access daemon

Event ID: 10523

Message

Category

Severity

Interface <if-name> is disabled by port-access as port of a CoA request

Port access

Info

Description

The port is disabled by port-access daemon

Event ID: 10524

Message

<request_pkt> request received for client with MAC address <mac_addr> on port <if-
name> from dyn-authorization client <address> on vrf <vrf-name>

Category

Port access

Severity

Info

Description

Disconnect/CoA request received from dyn-authorization client

Event ID: 10525

Message

<request_pkt> request received from <address> on VRF <vrf_name> for client with MAC

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

298

address <mac_addr> on port <if-name> is successfully processed

Category

Port access

Severity

Info

Description

Disconnect/CoA request request is handled successfully

Event ID: 10526

Message

<request_pkt> request received from <address> on VRF <vrf_name> for client with MAC
address <mac_addr> on port <if-name> failed to process with error <error_cause>

Category

Port access

Severity

Info

Description

Disconnect/CoA request request is failed

Event ID: 10527

Message

MAC Authentication triggered for client <mac_addr> on port <if_name> with ID <request_
id> to server <ip:port, proto, vrf {vrf_name}>

Category

Port access

Severity

Info

Description

MAC Authentication reuqest sent for client

Event ID: 10528

Message

MAC Authentication succeeded for client <mac_addr> on port <if_name> with ID <request_
id> to server <ip:port, proto, vrf {vrf_name}>

Category

Port access

Severity

Info

Description

MAC Authentication response received for client

Event ID: 10529

Message

MAC Authentication failed with reason <response> for client <mac_addr> on port <if_
name> with ID <request_id> from servers <server_list>

Category

Port access

Severity

Info

Description

MAC Authentication response received for client

Event ID: 10530

Port access events | 299

Message

802.1x Authentication triggered for client <mac_addr> on port <if_name> with ID <request_
id> to server <ip:port, proto, vrf {vrf_name}>

Category

Port access

Severity

Info

Description

802.1x Authentication request sent for client

Event ID: 10531

Message

802.1x Authentication succeeded for client <mac_addr> on port <if_name> with ID
<request_id> from server <ip:port, proto, vrf {vrf_name}>

Category

Port access

Severity

Info

Description

802.1x Authentication response sent for client

Event ID: 10532

Message

802.1x Authentication failed with reason <response> for client <mac_addr> on port <if_
name> with ID <request_id> from servers <server_list>

Category

Port access

Severity

Info

Description

802.1x Authentication response received for client

Event ID: 10533

Message

Category

Severity

Interface <if_name> is blocked by port-access

Port access

Info

Description

The interface is blocked by port-access daemon

Event ID: 10534

Message

Category

Severity

Interface <if_name> is unblocked by port-access

Port access

Info

Description

The interface is unblocked by port-access daemon

Event ID: 10535

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

300

Message

Policy {policy_name} is of type {feature} and a valid feature pack is required to use the
policy. All clients associated with this policy will be unauthorized until a valid feature pack
is installed.

Category

Port access

Severity

Error

Description

The feature has invalid or missing feature pack and it will not operate until a valid feature
pack is installed

Event ID: 10536

Message

Policy {policy_name} is of type {feature} and a valid feature pack is required to use the
policy. The policy is currently in use without a valid feature pack.

Category

Port access

Severity

Warning

Description

The feature doesn't have valid feature pack but it will operate normally.

Event ID: 10537

Message

Failed to apply flow monitor {monitor_name} in role {role_name} on port {port_name}.
Flow monitor is not supported on LAG ports.

Category

Port access

Severity

Info

Description

Flow monitor is applied on a LAG port via a role. LAG ports do not support flow monitors.

Port access events | 301

|             |                   |             |                   | Chapter | 103    |
| ----------- | ----------------- | ----------- | ----------------- | ------- | ------ |
|             |                   | Port access | application-based | policy  | events |
| Port access | application-based | policy      | events            |         |        |
Thefollowingaretheeventsrelatedtoportaccessapplication-basedpolicies(ABPs).
| Event ID: | 14701 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Configurationchangeinthepolicy{pac_abp_name}{operation}
| Category    | PORT_ACCESS_ABP                                   |     |     |     |     |
| ----------- | ------------------------------------------------- | --- | --- | --- | --- |
| Severity    | Info                                              |     |     |     |     |
| Description | Userupdatedtheapplicationbasedpolicyconfiguratio. |     |     |     |     |
| Event ID:   | 14702                                             |     |     |     |     |
Message onfigurationupdateinthepolicyduetoclasschange{pac_abp_name}{operation}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Severity | Error           |     |     |     |     |
Description Userupdatedtheapplicationbasedpolicyclassconfiguration
| Event ID: | 14703 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Triggerreceivedto{operation}policy:{pac_abp_name}forclient:{client}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Severity | Info            |     |     |     |     |
Description Theapplicationbasedpolicyapplying/unapplyingforclient
| Event ID: | 14704 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Triggerreceivedto{operation}policy:{pac_abp_name}forclient:{client}is{result}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Severity | Error           |     |     |     |     |
Description Triggerreceivedto{operation}policy:{pac_abp_name}forclient:{client}
302
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

|             |             |               |       |       | Chapter | 104    |
| ----------- | ----------- | ------------- | ----- | ----- | ------- | ------ |
|             |             | Port access   | group | based | policy  | events |
| Port access | group based | policy events |       |       |         |        |
Thefollowingaretheeventsrelatedtoportaccessgroupbasedpolicy.
| Event ID: | 12601 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message
Configurationchangeinthepolicy<pac_gbp_name><operation>
| Category | Portaccessgroupbasedpolicy |     |     |     |     |     |
| -------- | -------------------------- | --- | --- | --- | --- | --- |
| Severity | Information                |     |     |     |     |     |
Description Thegroupbasedpolicyconfigurationisupdatedbytheuser
| Event ID: | 12602 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Configurationupdateinthepolicyduetoclasschange<pac_gbp_name><operation>
| Category | Portaccessgroupbasedpolicy |     |     |     |     |     |
| -------- | -------------------------- | --- | --- | --- | --- | --- |
| Severity | Information                |     |     |     |     |     |
Description Thegroupbasedpolicyclassconfigurationisupdatedbytheuser
| Event ID: | 12603 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Triggerreceivedto<operation>policy:<pac_gbp_name>forclient:<client>
| Category    | Portaccessgroupbasedpolicy                      |     |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |     |     |
| Description | Thegroupbasedpolicyapplying/unapplyingforclient |     |     |     |     |     |
| Event ID:   | 12604                                           |     |     |     |     |     |
Message
Triggerreceivedto<operation>policy:<pac_gbp_name>forclient:<client>is<result>
| Category    | Portaccessgroupbasedpolicy                      |     |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |     |     |
| Description | Thegroupbasedpolicyapply/unapplyforclientresult |     |     |     |     |     |
| Event ID:   | 12605                                           |     |     |     |     |     |
303
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Trigger received on <operation> of line_card: <line_card> to <action> policy: <pac_gbp_
name>

Category

Port access group based policy

Severity

Information

Description

The group based policy apply/unapply on new linecard

Event ID: 12606

Message

Trigger received on <operation> of line_card: <line_card> to <action> policy: <pac_gbp_
name> is <result>

Category

Port access group based policy

Severity

Information

Description

The group based policy apply/unapply on new linecard result

Port access group based policy events | 304

Chapter 105

Port access roles events

Port access roles events

The following are the events related to port access roles.

Event ID: 9301

Message

Failed to apply ClearPass role - <cprole_error_string>

Category

Port access roles

Severity

Error

Description

Logs an event if there are errors when applying a ClearPass role

Event ID: 9302

Message

Failed to create the role - <role_name>, maximum limit reached' throttle_count: 100

Category

Port access roles

Severity

Error

Description

Logs an event if the maximum limit is reached while creating a Port Access Role

Event ID: 9303

Message

A local user role with name {role_name} already exists and conflicts with the newly
inserted ClearPass role

Category

Port access roles

Severity

Warning

Description

Warns a user when local user role is already existing.

Event ID: 9304

Message

A ClearPass role with name {role_name} already exists and conflicts with the newly
inserted {role_type} role.

Category

Port access roles

Severity

Warning

Description

Warns a user when a ClearPass role is already existing.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

305

Chapter 106

Port events

Port events

The following are the events related to port.

Event ID: 601

Message

Category

Severity

Netlink socket creation failed <error>

Port

Info

Description

Log when netlink socket creation failed

Event ID: 602

Message

Category

Severity

Netlink socket bind failed <error>

Port

Info

Description

Log when netlink socket bind failed

Event ID: 603

Message

Category

Severity

Netlink failed to set mtu <mtu> for interface <interface>

Port

Info

Description

Log when netlink failed to set mtu for interface

Event ID: 604

Message

Category

Severity

Netlink failed to bring <status> the interface <interface>

Port

Info

Description

Log when netlink failed to change the interface status

Event ID: 605

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

306

Message

Category

Severity

Unknown internal vlan policy <policy>

Port

Info

Description

Unknown internal vlan policy

Event ID: 606

Message

Category

Severity

Error allocating internal vlan for port <vlan>

Port

Info

Description

Log when allocation failed for internal vlan for port

Event ID: 607

Message

Category

Severity

Overlapping networks observed for <ip_address>

Port

Error

Description

Log when a duplicate address is received on a port

Event ID: 608

Message

Category

Severity

Description

Event ID: 609

Message

Category

Severity

Description

Interface {port} is down due to PVLAN hardware resource allocation failure

Port

Info

This log event informs the user that interface is down due to PVLAN hardware resource
allocation failure

Interface {port} is recovered from PVLAN hardware resource allocation failure

Port

Info

This log event informs the user that the interface has recovered from hardware resource
allocation failure

Port events | 307

Chapter 107

Port security events

Port security events

The following are the events related to port security.

Event ID: 9401

Message

Client limit exceeded on port <if_name>, caused by an unauthorized client <mac_addr>'
throttle_count: 30: yes

Category

Port security

Severity

Info

Description

Client is trying to get access on a port security enabled port

Event ID: 9402

Message

Port security sticky client move violation triggered on port <port> for client with MAC
address <mac_addr>.' throttle_count: 30: yes

Category

Port security

Severity

Info

Description

Client, which has been programmed as sticky client on a port, tried to connect on
different port

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

308

Chapter 108

Port Statistics events

Port Statistics events

The following are the events related to port statistics.

Event ID: 6601

Message

Failed to create layer 3 IPv4 RX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv4 RX counter fails

Event ID: 6602

Message

Failed to create layer 3 IPv6 RX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv6 RX counter fails

Event ID: 6603

Message

Failed to create layer 3 IPv4 TX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv4 TX counter fails

Event ID: 6604

Message

Failed to create layer 3 IPv6 TX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv6 TX counter fails

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

309

Chapter 109

Power events

Power events

The following are the events related to power.

Event ID: 301

Message

Category

Severity

PSU <name> changed state to <state>

Power

Info

Description

Log the change in PSU status.

Event ID: 302

Message

PSUs inserted in the system are of <Type> types. This is <Support> configuration.

Category

Power

Severity

Warning

Description

Log the identification of mixed PSU types

Event ID: 303

Message

Category

Severity

PSU <name> encountered a warning. Total warning count: <warnings>

Power

Error

Description

Log the warnings encountered by the PSU

Event ID: 304

Message

Category

Severity

PSU <name> faulted. Total fault count: <failures>

Power

Error

Description

Log the failures encountered by the PSU

Event ID: 305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

310

Message

PSU <name>: Internal communication <status>

Category

Power

Severity

Warning

Description

Log PSU internal communication failure

Event ID: 306

Message

PSU <name>: Fan-<fanidx> <status>

Category

Power

Severity

Warning

Description

Log PSU fan fault

Event ID: 307

Message

PSU <name>: <sensorid> sensor <status> threshold limit

Category

Power

Severity

Warning

Description

Log when PSU temperature sensor exceeded threshold

Event ID: 308

Message

Category

Severity

PSU <name> has shutdown due to over temperature in <sensorid> sensor

Power

Error

Description

Log when PSU temperature sensor triggered PSU shutdown

Event ID: 309

Message

PSU <name>: Output current <status> threshold limit

Category

Power

Severity

Warning

Description

Log when PSU output current exceeds threshold

Event ID: 310

Message

PSU <name> has shutdown due to output overcurrent

Power events | 311

Category

Severity

Power

Error

Description

Log when PSU output current triggered PSU shutdown

Event ID: 311

Message

Category

Severity

PSU <name> has shutdown due to output overvoltage

Power

Error

Description

Log when PSU output voltage triggered PSU shutdown

Event ID: 312

Message

Category

Severity

PSU Redundancy set to <redund>

Power

Info

Description

Log a change in the PSU redundancy user configuration

Event ID: 313

Message

Category

Severity

PSU Redundancy operating at <redund>

Power

Info

Description

Log a change in the PSU redundancy operational state

Event ID: 314

Message

Category

Severity

Description

Event ID: 315

PSU <name> disabled: PSU airflow does not match system-airflow

Power

Error

Log when PSU is disabled due to airflow direction mismatch, recorded periodically for
each PSU'

Message

PSU <name> disabled: PSU communication error

Category

Power

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

312

Severity

Error

Description

Log when PSU is disabled due to communication error

Event ID: 316

Message

<type> module <name> denied power due to insufficient power. Configured PoE power
can be deconfigured to allow card to be granted power.

Category

Power

Severity

Warning

Description

There is insufficient power to power a card. Power can be removed from configured PoE
PDs to be able to power the card.

Event ID: 317

Message

PSU <name> disabled: PSU inserted is not supported by the system

Category

Power

Severity

Warning

Description

Log when PSU is disabled due to an unsupported PSU

Event ID: 318

Message

Category

Severity

Power over Ethernet status has faulted

Power

Error

Description

Log 54V Power over Ethernet status fault

Event ID: 319

Message

Category

Severity

Power over Ethernet status is good

Power

Info

Description

Log 54V Power over Ethernet status is good

Event ID: 320

Message

PSU <name> <alert> occurred

Category

Power

Power events | 313

Severity

Error

Description

Log when PSU voltage alert occurs

Event ID: 321

Message

Category

Severity

PSU <name> <alert> recovered

Power

Info

Description

Log when PSU voltage alert recovers

Event ID: 322

Message

Invalid PoE power configuration, using default maximum PoE power

Category

Power

Severity

Warning

Description

Log when configured PoE power is invalid

Event ID: 323

Message

Category

Severity

PSU {name} is not supported by the system. Please insert a supported PSU. Refer to the
Installation Guide for supported configurations.

Power

Error

Description

Log event for an unsupported PSU, recorded periodically for each PSU

Event ID: 324

Message

Category

Severity

PSU {name} encountered {fault} fault with 0x{status} during previous boot.

Power

Info

Description

Log PSU fault event in previous boot

Event ID: 325

Message

'PSU {name} disabled: PSU input type {input_type} does not match existing input type
{existing_type}'

Category

Power

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

314

Severity

Error

Description

Log when PSU is disabled due to input type mismatch, recorded periodically for each PSU

Power events | 315

Chapter 110
|            |          |        | Power | over Ethernet | events |
| ---------- | -------- | ------ | ----- | ------------- | ------ |
| Power over | Ethernet | events |       |               |        |
ThefollowingaretheeventsrelatedtopoweroverEthernet.
| Event ID: | 7901 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Detectedpowereddeviceoninterface<interface_name>.Type:<pd_type>,Class:<pd_class>
| Category    | PoweroverEthernet                            |     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                                  |     |     |     |     |
| Description | Detectedpowereddeviceoninterface.Type,Class. |     |     |     |     |
| Event ID:   | 7902                                         |     |     |     |     |
Message Powereddevicepowerdeliveryoninterface<interface_name>
| Category    | PoweroverEthernet                                   |     |     |     |     |
| ----------- | --------------------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                                         |     |     |     |     |
| Description | Powereddevicepowerdeliveryoninterface.              |     |     |     |     |
| Event ID:   | 7903                                                |     |     |     |     |
| Message     | Powereddevicepowerdeniedoninterface<interface_name> |     |     |     |     |
| Category    | PoweroverEthernet                                   |     |     |     |     |
| Severity    | Warning                                             |     |     |     |     |
| Description | Powereddevicepowerdeniedoninterface.                |     |     |     |     |
| Event ID:   | 7904                                                |     |     |     |     |
Message
Powereddevicefaultoninterface<interface_name>.Faulttype<fault_type>
| Category    | PoweroverEthernet                        |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                  |     |     |     |     |
| Description | Powereddevicefaultoninterface.Faulttype. |     |     |     |     |
| Event ID:   | 7905                                     |     |     |     |     |
316
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Powered device disconnected on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface.

Event ID: 7906

Message

PoE disabled on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

PoE disabled on interface

Event ID: 7907

Message

Powered device mps absent on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device mps absent on interface

Event ID: 7908

Message

Detected dual signature powered device on interface <interface_name>. Type:<pd_type>,
ClassA:<paira_class>, ClassB:<pairb_class>

Category

Power over Ethernet

Severity

Information

Description

Detected dual signature powered device on interface. Type, ClassA, ClassB

Event ID: 7909

Message

Dual signature powered device power delivery on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device power delivery on interface.

Event ID: 7910

Message

Dual signature powered device fault on interface <interface_name> pair <pair>. Fault type

Power over Ethernet events | 317

<fault_type>

Category

Power over Ethernet

Severity

Warning

Description

Dual signature powered device fault on interface. Fault type.

Event ID: 7911

Message

Dual signature powered device mps absent on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device mps absent on interface

Event ID: 7912

Message

Powered device FET bad fault recovered on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device FET bad fault recovered on interface

Event ID: 7913

Message

Powered device FET bad fault recovery failed on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device FET bad fault recovery failed on interface

Event ID: 7914

Message

Powered device got class demoted on interface <interface_name>. Requested_class <req_
class> Assigned_class <assigned_class>

Category

Power over Ethernet

Severity

Information

Description

Powered device got class demoted on interface

Event ID: 7915

Message

Dual signature powered device got class demoted on interface <interface_name>.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

318

Requested_classA <req_class_A> Requested_classB <req_class_B> Assigned_classA
<assigned_class_A> Assigned_classB <assigned_class_B>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device got class demoted on interface

Event ID: 7916

Message

Powered device pre std detect enabled on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device pre std detect enabled on interface

Event ID: 7917

Message

PoE usage exceeded threshold limit of <threshold_limit>

Category

Power over Ethernet

Severity

Information

Description

PoE usage exceeded threshold limit

Event ID: 7918

Message

PoE controller <cntrl_name> got into fault

Category

Power over Ethernet

Severity

Information

Description

PoE controller got into fault

Event ID: 7919

Message

PoE controller <cntrl_name> got reset

Category

Power over Ethernet

Severity

Information

Description

PoE controller got reset

Event ID: 7920

Message

Powered device got class promoted on interface <interface_name>.Requested_class <req_

Power over Ethernet events | 319

class> Assigned_class <assigned_class>

Category

Power over Ethernet

Severity

Information

Description

Powered device got class promoted

Event ID: 7921

Message

Dual signature powered device got class promoted on interface <interface_
name>.Requested_classA <req_class_A> Requested_classB <req_class_B> Assigned_classA
<assigned_class_A> Assigned_classB <assigned_class_B>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device got class promoted

Event ID: 7922

Message

Powered device is drawing power more than its class on interface <interface_name>,
type:<pd_type> class:<pd_class> power:<power> is exceeding the max average power of
the PD class. Check the PD max power draw, cabling type and length to improve
interoperability

Category

Power over Ethernet

Severity

Information

Description

Powered device is drawing power more than its class

Event ID: 7923

Message

Powered device UVLO fault on interface <interface_name>, will attempt to recover itself by
toggling power

Category

Power over Ethernet

Severity

Information

Description

Powered device UVLO fault on interface

Event ID: 7924

Message

Powered device FET BAD fault on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device FET BAD fault

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

320

Event ID: 7925

Message

Dual signature powered device is drawing power more than its class on interface
<interface_name>, type:<pd_type> classA:<paira_class> classB:<pairb_class> power:<power>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device is drawing power more than its class

Event ID: 7926

Message

PoE usage is below threshold of <threshold_limit>

Category

Power over Ethernet

Severity

Information

Description

PoE usage is below threshold

Event ID: 7927

Message

Total power drawn: <power_drawn>W by powered device is exceeding the total available
PoE power:<power_available>W. Check the PD max power draw, cabling type and length
to avoid system crowbar.

Category

Power over Ethernet

Severity

Warning

Description

PoE drawn power is more than available PoE power

Event ID: 7928

Message

Powered device invalid signature indication on interface <interface_name>.

Category

Power over Ethernet

Severity

Warning

Description

Powered device invalid signature indication

Event ID: 7929

Message

PoE hardware access daemon exiting

Category

Power over Ethernet

Severity

Information

Description

PoE hardware access daemon exiting

Event ID: 7930

Power over Ethernet events | 321

Message

POE proto daemon exiting

Category

Power over Ethernet

Severity

Information

Description

POE proto daemon exiting

Event ID: 7931

Message

Always-on PoE detected a powered device on interface <interface_name> and delivered
power

Category

Power over Ethernet

Severity

Information

Description

Always-on PoE detected a powered device on interface

Event ID: 7932

Message

Powered device disconnected on interface <interface_name> due to LLDP dot3 disable

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface due to LLDP dot3 disable

Event ID: 7933

Message

Subsystem <subsys_name> came up with quick PoE

Category

Power over Ethernet

Severity

Information

Description

Subsystem came up with quick PoE

Event ID: 7934

Message

Quick PoE detected a powered device on interface <interface_name> and delivered power

Category

Power over Ethernet

Severity

Information

Description

Quick PoE detected a powered device on interface

Event ID: 7935

Message

Powered device denied on interface <interface_name> of line module with Quick PoE

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

322

enabled. Remove device to avoid crowbar on reboot.

Category

Power over Ethernet

Severity

Warning

Description

Powered device denied on interface of line module with Quick PoE enabled.

Event ID: 7936

Message

Powered device demoted on interface <interface_name> of line module with Quick PoE
enabled. Remove device to avoid crowbar on reboot.

Category

Power over Ethernet

Severity

Warning

Description

Powered device demoted on interface of line module with Quick PoE enabled

Event ID: 7937

Message

PoE disable ignored on interface <interface_name> because Quick PoE is enabled

Category

Power over Ethernet

Severity

Warning

Description

PoE disable ignored on interface because Quick PoE is enabled

Event ID: 7938

Message

PoE assigned class configuration is ignored on interface <interface_name> because Quick
PoE is enabled

Category

Power over Ethernet

Severity

Warning

Description

PoE assigned class configuration is ignored on interface because Quick PoE is enabled

Event ID: 7939

Message

Powered device requested power down on interface <interface_name> <duration>

Category

Power over Ethernet

Severity

Information

Description

Powered device requested power down on interface.

Event ID: 7940

Power over Ethernet events | 323

Message

Powered device disconnected on interface <interface_name> due to pd-class-override
config change

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface due to pd-class-override config change

Event ID: 7941

Message

Powered device disconnected on interface <interface_name> due to power-pairs config
change

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface due to power-pairs config change

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

324

Chapter 111

PTP events

PTP events

The following are the events related to PTP.

Event ID: 12101

Message

Category

Severity

PTP <type> <delay_mechanism> <clock_step> clock started with profile <profile> and
transport <transport>.

PTP

Info

Description

Event reported when PTP clock is started.

Event ID: 12102

Message

Category

Severity

PTP clock stopped. Reason: <reason>

PTP

Info

Description

Event reported when PTP clock is stopped.

Event ID: 12103

Message

Category

Severity

Interface <name> enabled for PTP exchange.

PTP

Info

Description

Event reported when PTP port is enabled for tx and rx.

Event ID: 12104

Message

Category

Severity

Interface <name> disabled for PTP exchange. Reason: <reason>

PTP

Info

Description

Event reported when PTP enabled port is disabled.

Event ID: 12105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

325

Message

Category

Severity

PTP clock is in <state> state

PTP

Info

Description

Event reported for different PTP clock state.

Event ID: 12106

Message

Category

Severity

Interface {name} is in {state} state{reason}

PTP

Info

Description

Event reported for different PTP port state.

Event ID: 12107

Message

Category

Severity

New GrandSource/Parent is selected: Parent: <parent>, GrandSource: <grandsource>,
Quality: <quality>, Priority1: <priority1>, Priority2: <priority2>

PTP

Info

Description

Event reported when PTP parent is updated/modified.

Event ID: 12108

Message

Category

Severity

PTP operational log_announce_interval is changed to <value> on interface <name> for
profile <profile>

PTP

Info

Description

Event reported when PTP log announce interval is modified.

Event ID: 12109

Message

Category

Severity

PTP operational log_min_pdelay_request_interval is changed to <value> on interface
<name> for profile <profile>

PTP

Info

Description

Event reported when PTP log min pdelay request interval is modified.

Event ID: 12110

PTP events | 326

Message

Category

Severity

PTP operational log_min_delay_request_interval is changed to <value> on interface
<name> for profile <profile>

PTP

Info

Description

Event reported when PTP log min delay request interval is modified.

Event ID: 12111

Message

Category

Severity

PTP operational sync_request_timeout is changed to <value> on interface <name> for
profile <profile>

PTP

Info

Description

Event reported when PTP sync request timeout is modified.

Event ID: 12112

Message

Category

Severity

PTP operational sync_interval is changed to <value> on interface <name> for profile
<profile>

PTP

Info

Description

Event reported when PTP sync interval is modified.

Event ID: 12113

Message

Category

Severity

PTP operational announce_request_timeout is changed to <value> on interface <name>
for profile <profile>

PTP

Info

Description

Event reported when PTP announce request timeout is modified.

Event ID: 12114

Message

Category

Severity

PTP config invalid. Reason: <reason>

PTP

Info

Description

Event reported if PTP configuration is invalid.

Event ID: 12115

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

327

Message

Category

Severity

PTP domain modified from <old> to <new> value

PTP

Info

Description

Event reported if PTP domain configuration is modified.

Event ID: 12116

Message

Category

Severity

PTP vlan modified from <old> to <new> on port <port>

PTP

Info

Description

Event reported if PTP vlan configuration is modified.

Event ID: 12117

Message

Category

Severity

PTP source_ip_interface <action>. Port: <value>

PTP

Info

Description

Event reported if PTP source_ip_interface configuration is modified.

Event ID: 12118

Message

Category

Severity

PTP source_ip <action>. IP: <value>

PTP

Info

Description

Event reported if PTP source_ip configuration is modified.

Event ID: 12119

Message

Category

Severity

PTP offset has reached beyond the threshold {low_limit} < {curr_offset} < {high_limit}

PTP

Warning

Description

Event reported if PTP offset goes beyond the threshold value.

Event ID: 12120

Message

PTP offset has reached below the threshold {low_limit} < {curr_offset} < {high_limit}

PTP events | 328

Category

PTP

Severity

Warning

Description

Event reported if PTP offset is within the threshold value.

Event ID: 12121

Message

PTP may not work as expected when PTP clock is BC and enabled on MCLAG {int_name}-
{lag_name}.

Category

PTP

Severity

Warning

Description

Event reported if PTP clock is BC and PTP enabled on MCLAG.

Event ID: 12122

Message

PTP Unicast and Multicast are both configured. Only Unicast will be honored. If Multicast
operation is desired, remove all PTP Unicast configuration.

Category

PTP

Severity

Warning

Description

Event reported if conflicting PTP Unicast and PTP Multicast are both configured.

Event ID: 12123

Message

Category

Severity

PTP daemon {action}: {daemon_service_description}.

PTP

Info

Description

Event reported when a PTP-related daemon has changed its state.

Event ID: 12124

Message

Category

Severity

PTP IP-DSCP value for event message modified to {event} on port {port}.

PTP

Info

Description

Event reported if PTP ip-dscp event message configuration is modified.

Event ID: 12125

Message

PTP IP-DSCP value for general message modified to {general} on port {port}

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

329

Category

PTP

Severity

Warning

Description

Event reported if PTP ip-dscp general message configuration is modified.

Event ID: 12126

Message

Category

Severity

PTP Port clock source only {action} on {port}

PTP

Warning

Description

Event reported if PTP clock source only configuration is modified.

PTP events | 330

Chapter 112

Proxy ARP events

Proxy ARP events

The following are the events related to proxy ARP.

Event ID: 4205

Message

Local proxy ARP enabled for port <port> on vrf <vrf>

Category

Proxy ARP

Severity

Information

Description

Logs a message when the feature is enabled for a port inside a VRF

Event ID: 4206

Message

Local proxy ARP disabled for port <port> on vrf <vrf>

Category

Proxy ARP

Severity

Information

Description

Logs a message when the feature is disabled for a port inside a VRF

Event ID: 4207

Message

Failed to enable local proxy ARP for port <port> on vrf <vrf>

Category

Proxy ARP

Severity

Error

Description

Logs a message when the feature enable fails for a port inside a VRF

Event ID: 4208

Message

Failed to disable local proxy ARP for port <port> on vrf <vrf>

Category

Proxy ARP

Severity

Error

Description

Logs a message when the feature disable fails for a port inside a VRF

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

331

|          |          |        |          | Chapter  | 113    |
| -------- | -------- | ------ | -------- | -------- | ------ |
|          |          |        | QoS ASIC | Provider | events |
| QoS ASIC | Provider | events |          |          |        |
ThefollowingaretheeventsrelatedtoqualityofserviceASICprovider.
| Event ID: | 5801 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
QoSfailedinitialinitializationforslot<local_slot>.Error:<error>
| Category    |      | QoSASICProvider                |     |     |     |
| ----------- | ---- | ------------------------------ | --- | --- | --- |
| Severity    |      | Warning                        |     |     |     |
| Description |      | QoSinitialinitializationfailed |     |     |     |
| Event ID:   | 5802 |                                |     |     |     |
Message QoSfailedfinalinitializationonnewslot<new_slot>forpeerslot<existing_slot>
| Category    |      | QoSASICProvider                        |     |     |     |
| ----------- | ---- | -------------------------------------- | --- | --- | --- |
| Severity    |      | Critical                               |     |     |     |
| Description |      | QoSfinalinitializationfailedfornewslot |     |     |     |
| Event ID:   | 5803 |                                        |     |     |     |
| Message     |      | QoSerroraftercardremovalfromslot<slot> |     |     |     |
| Category    |      | QoSASICProvider                        |     |     |     |
| Severity    |      | Error                                  |     |     |     |
| Description |      | QoSerroraftercardremoval               |     |     |     |
| Event ID:   | 5804 |                                        |     |     |     |
Message
ErrorduringQoSfeatureconfiguration:<error_string>
| Category    |      | QoSASICProvider                             |     |     |     |
| ----------- | ---- | ------------------------------------------- | --- | --- | --- |
| Severity    |      | Error                                       |     |     |     |
| Description |      | ErrorwhileattemptingQoSfeatureconfiguration |     |     |     |
| Event ID:   | 5805 |                                             |     |     |     |
332
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Error during QoS HW configuration: <error_string> error <val>

Category

QoS ASIC Provider

Severity

Error

Description

Error while attempting QoS HW configuration

Event ID: 5806

Message

Port: <port_name> PFC priority <pri> using queue <queue> should not be sharing the
queue with other local-priorities

Category

QoS ASIC Provider

Severity

Warning

Description

Warning PFC priority sharing a queue

Event ID: 5807

Message

QoS de-initialization not executed after card removal from slot {slot}

Category

QoS ASIC Provider

Severity

Error

Description

QoS de-initialization not executed after card removal

QoS ASIC Provider events | 333

Chapter 114
|         |                   |     | Quality | of Service | events |
| ------- | ----------------- | --- | ------- | ---------- | ------ |
| Quality | of Service events |     |         |            |        |
Thefollowingaretheeventsrelatedtoqualityofservice.
| Event ID: | 5701 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message QoSfailedtoretrievedefaultinformation.Error:<error>
Category QualityofService
Severity Info
Description QoSfailedtoretrievedefaultconfiguration
| Event ID: | 5702 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message QoSerror:<error_string>
Category QualityofService
Severity Error
Description QoSerroroccurred
| Event ID: | 5703 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message ThePFCconfigurationforinterface<ifname>exceedsthesystemlimitof<limit>unique
combinationsandwasnotapplied
Category QualityofService
Severity Warning
Description Loggedwhentherearemoreuniquecombinationsofflowcontrolledprioritiesthanthe
systemallows.
| Event ID: | 5704 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message QoSwarning:{warning_string}
Category QualityofService
Severity Warning
Description Logswarningeventwhenthreshold-profileisenabledonportandifportotherthan
thresholdprofileenabledhavetrustmodeascosornone.
| Queue | Monitoring | events |     |     |     |
| ----- | ---------- | ------ | --- | --- | --- |
334
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

The following are the events related to queue monitoring (QTP).

Event ID: 16101

Message

Category

Severity

Description

Event ID: 16102

Message

Category

Severity

Description

Event ID: 16103

Message

Category

Severity

HONOR_MODE: Queue Monitoring is operating without a valid feature pack.

QTP

Info

Log event to indicate that the Queue Monitor feature is operating without a valid feature
pack

STRICT_MODE: Queue Monitoring is blocked due to invalid or missing feature pack.

QTP

Info

Log event to indicate that the Queue Monitoring feature is blocked due to invalid or
missing feature pack

Log event to indicate that the Queue Monitoring feature is operational for valid feature
pack

QTP

Info

Description

ACTIVE_MODE: Queue Monitoring is operating with valid feature pack.

Queue Monitoring events | 335

Chapter 115
|           |      | Rapid    | per VLAN      | Spanning | Tree Protocol | events |
| --------- | ---- | -------- | ------------- | -------- | ------------- | ------ |
| Rapid per | VLAN | Spanning | Tree Protocol | events   |               |        |
ThefollowingaretheeventsrelatedtorapidperVLANspanningtreeprotocol.
| Event ID: | 5001 |                                  |     |     |     |     |
| --------- | ---- | -------------------------------- | --- | --- | --- | --- |
| Message   |      | RPVSTEnabled                     |     |     |     |     |
| Category  |      | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| Severity  |      | Info                             |     |     |     |     |
Description ThislogeventindicatesthatRPVSThasbeenenabledontheswitch.
| Event ID: | 5002 |                                  |     |     |     |     |
| --------- | ---- | -------------------------------- | --- | --- | --- | --- |
| Message   |      | RPVSTDisabled                    |     |     |     |     |
| Category  |      | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| Severity  |      | Info                             |     |     |     |     |
Description ThislogeventindicatesthatRPVSThasbeendisabledontheswitch.
| Event ID: | 5003 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message RPVST-Rootchangedfrom<old_priority>:<old_mac>to<new_priority>:<new_mac>on
VLAN<vlan>.
| Category |     | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| -------- | --- | -------------------------------- | --- | --- | --- | --- |
| Severity |     | Info                             |     |     |     |     |
Description ThislogeventindicatesthatRPVSTrootonaVLANhaschanged
| Event ID: | 5004 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Port<port>disabled-BPDUreceivedonprotectedportonVLAN<vlan>.
| Category |     | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| -------- | --- | -------------------------------- | --- | --- | --- | --- |
| Severity |     | Warning                          |     |     |     |     |
Description ThislogeventinformstheuserBPDUreceivedonprotectedport
| Event ID: | 5005 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
336
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Category

Severity

<proto> starved for <pkt_type> on port <port> from <priority_mac> on VLAN <vlan>.

Rapid per VLAN Spanning Tree Protocol

Info

Description

This log event informs the user that the Rx is starved in paticular port

Event ID: 5006

Message

Category

Severity

Topology change received on port <port> from source: <mac> on VLAN <vlan>.

Rapid per VLAN Spanning Tree Protocol

Info

Description

This log event informs the user that the RPVST topology change is received

Event ID: 5007

Message

Category

Severity

Topology change generated on port <port> on VLAN <vlan>.

Rapid per VLAN Spanning Tree Protocol

Info

Description

This log event informs the user that the RPVST topology change is generated

Event ID: 5008

Message

Category

Severity

Port <port> blocked on RPVST <instance>

Rapid per VLAN Spanning Tree Protocol

Warning

Description

This log event informs the user that the port is blocked on the instance

Event ID: 5009

Message

Category

Severity

Port <port> unblocked on RPVST <instance>

Rapid per VLAN Spanning Tree Protocol

Warning

Description

This log event informs the user that the port is unblocked on the instance

Event ID: 5010

Message

Root port changed from <old_port> to <new_port> on VLAN <vlan>.

Rapid per VLAN Spanning Tree Protocol events | 337

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Info

Description

This log event informs the user that the root port is changed

Event ID: 5011

Message

PVID mismatch detected on <interface> with pvid = <pvid>, Neighbor pvid = <npvid>'
throttle_count: 100

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Info

Description

Log event when the PVID mismatches between the switch and neighbor over an interface

Event ID: 5012

Message

spanning tree mode changed from <old_mode> to <new_mode>, it will trigger the
reconvergence

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Info

Description

This log event informs the user that the spanning tree mode is changed.

Event ID: 5013

Message

Current Virtual Ports <Current_Virtual_Ports> exceeds the max supported limit <Maximum_
Virtual_Ports>

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Info

Description

Log event when the current virtual port count crosses the maximum allowed value

Event ID: 5014

Message

Category

Severity

AUTO RPVST Enabled

Rapid per VLAN Spanning Tree Protocol

Info

Description

RPVST AUTO VLAN is enabled.

Event ID: 5015

Message

AUTO RPVST Disabled

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

338

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Info

Description

RPVST AUTO VLAN is disabled.

Event ID: 5016

Message

Category

Severity

AUTO RPVST NO-VPORT-LIMIT Enabled

Rapid per VLAN Spanning Tree Protocol

Info

Description

RPVST AUTO VLAN NO-VPORT-LIMIT is enabled.

Event ID: 5017

Message

Category

Severity

AUTO RPVST NO-VPORT-LIMIT Disabled

Rapid per VLAN Spanning Tree Protocol

Info

Description

RPVST AUTO VLAN NO-VPORT-LIMIT is disabled.

Event ID: 5018

Message

The current virtual port count for RPVST AUTO VLAN has exceeded the maximum
supported system limit {lvlan}

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Warning

Description

RPVST AUTO VLAN Instance Creation is limited, Current VPORTs exceed the maximum
supported system limit

Rapid per VLAN Spanning Tree Protocol events | 339

Chapter 116

RBAC events

RBAC events

The following are the events related to RBAC.

Event ID: 10301

Message

Local authorization has been <tac_status>d

Category

RBAC

Severity

Information

Description

Log event when local tac_plus server has been started

Event ID: 10302

Message

Category

Severity

Failed to <tac_status> local authorization

RBAC

Error

Description

Log event when local tac_plus server failed to start

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

340

Chapter 117
|           |            |        | Redundant | Management | events |
| --------- | ---------- | ------ | --------- | ---------- | ------ |
| Redundant | Management | events |           |            |        |
Thefollowingaretheeventsrelatedtoredundantmanagement.
| Event ID: | 2201 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Failoverdetected:Reason<reason>
| Category    | RedundantManagement                            |     |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |     |
| Description | Thislogeventinformsthatfailovereventisdetected |     |     |     |     |
| Event ID:   | 2202                                           |     |     |     |     |
Message Lost<mgmt_module>asStandbyManagementModule,redundancydisabled
| Category | RedundantManagement |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
| Severity | Information         |     |     |     |     |
Description Thislogeventinformsthatstandbymgmtmodulehasbeenremoved
| Event ID: | 2203                                           |     |     |     |     |
| --------- | ---------------------------------------------- | --- | --- | --- | --- |
| Message   | DetectedtheremovaloftheStandbyManagementModule |     |     |     |     |
| Category  | RedundantManagement                            |     |     |     |     |
| Severity  | Information                                    |     |     |     |     |
Description Thislogeventinformsthatstandbymgmtmodulehasbeenremoved
| Event ID: | 2204 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
<mgmt_module>isActive
| Category | RedundantManagement |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
| Severity | Information         |     |     |     |     |
Description ThislogeventinformsaboutthestatusofActivemgmtmodule
| Event ID: | 2205 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
341
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

<mgmt_module> is Standby

Category

Redundant Management

Severity

Information

Description

This log event informs about the status of Standby mgmt module

Event ID: 2206

Message

Detected <mgmt_module> as Standby Management Module, redundancy enabled

Category

Redundant Management

Severity

Information

Description

This log event informs that standby mgmt module is added to the system

Event ID: 2207

Message

Remote Standby Management module recover detected. Reason: Heartbeat loss

Category

Redundant Management

Severity

Information

Description

This log event informs the user that Active mgmt module has detected heartbeat loss

Event ID: 2208

Message

<mgmt_module> is waiting for filesync

Category

Redundant Management

Severity

Information

Description

This log event informs the user that filesync is in progress

Event ID: 2209

Message

<mgmt_module> is starting ISSU operation

Category

Redundant Management

Severity

Information

Description

This log event informs the user that an ISSU operation has begun

Redundant Management events | 342

|             |         |        |             | Chapter | 118    |
| ----------- | ------- | ------ | ----------- | ------- | ------ |
|             |         |        | Replication | Manager | events |
| Replication | Manager | events |             |         |        |
Thefollowingaretheeventsrelatedtoreplicationmanager.
| Event ID: | 2701 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
Allbitmapshavebeenallocated
| Category    | ReplicationManager                       |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                  |     |     |     |     |
| Description | Logtoindicateallbitmapshavebeenallocated |     |     |     |     |
| Event ID:   | 2702                                     |     |     |     |     |
| Message     | Over80percentofbitmapshavebeenallocated  |     |     |     |     |
| Category    | ReplicationManager                       |     |     |     |     |
| Severity    | Warning                                  |     |     |     |     |
Description Logtoindicateover80percentofbitmapshavebeenallocated
| Event ID: | 2705 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message MulticastL3BridgeControlForwardingentrywithuuid<uuid_str>hasnoreferencetoa
VLAN
| Category | ReplicationManager |     |     |     |     |
| -------- | ------------------ | --- | --- | --- | --- |
| Severity | Warning            |     |     |     |     |
Description LogindicatesMutlicastL3BridgeControlForwardingentrywithuuidhasnoreferenceto
aVLAN
343
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 119

REST events

REST events

The following are the events related to REST.

Event ID: 4601

Message

Category

Severity

Authentication failed for user <user> in session <sessionid>

REST

Error

Description

logs a failed authentication attempt of a user via REST

Event ID: 4602

Message

Category

Severity

Authentication succeeded for user <user> in session <sessionid>

REST

Info

Description

logs a successful authentication attempt of a user via REST

Event ID: 4603

Message

Category

Severity

Conflict in authorization configuration. Existing config::URL(<match>), type(<value>) New
config::(<url>), type(<autztype>)

REST

Critical

Description

logs an authorization configuration conflict

Event ID: 4606

Message

Category

Severity

Authorization failed for user <user>, for resource <resource>, with action <action>

REST

Error

Description

logs a failed authorization attempt of a user via REST

Event ID: 4607

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

344

Message

Category

Severity

Authorization succeeded for user <user>, for resource <resource>, with action <action>

REST

Info

Description

logs a successful authorization attempt of a user via REST

Event ID: 4608

Message

Category

Severity

Authorization allowed for user <user>, for resource <resource>, with action <action>

REST

Info

Description

logs an allowed authorization attempt of a user via REST

Event ID: 4609

Message

Category

Severity

User <user> added <added_user> with role <added_user_role>

REST

Info

Description

logs a successful add of a user via REST

Event ID: 4610

Message

Category

Severity

User <user> deleted <deleted_user>

REST

Info

Description

logs a successful deletion of a user via REST

Event ID: 4611

Message

Category

Severity

User <user> successfully changed password

REST

Info

Description

logs a successful password change for a user via REST

Event ID: 4612

Message

User <user> password change failed

REST events | 345

Category

REST

Severity

Warning

Description

logs an unsuccessful password change for a user via REST

Event ID: 4613

Message

Category

Severity

<user> has written a new switch configuration to <config_name>

REST

Info

Description

logs a success config write operation

Event ID: 4614

Message

Category

Severity

<user> has copied switch configuration <from_name> to <to_name>

REST

Info

Description

logs a success copy of saved

Event ID: 4615

Message

Category

Severity

<user> has configured <dns_nameserver> DNS nameserver to <dns>

REST

Info

Description

logs a success when the nameserver is written to ovsdb

Event ID: 4616

Message

Category

Severity

<user> has deleted all DNS nameservers

REST

Info

Description

logs a success when the nameserver is deleted from ovsdb

Event ID: 4617

Message

<user> created <uri>

Category

REST

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

346

Severity

Info

Description

A user has successfully created a new resource in OVSDB.

Event ID: 4618

Message

Category

Severity

<user> deleted <uri>

REST

Info

Description

A user has successfully deleted a resource in OVSDB.

Event ID: 4619

Message

Category

Severity

<user> modified <uri>

REST

Info

Description

A user has successfully modified a resource in OVSDB.

Event ID: 4620

Message

Category

Severity

User: <user> added subscriber: <subscriber>.

REST

Info

Description

A user has added new notification subscriber.

Event ID: 4621

Message

Category

Severity

User: <user> removed subscriber: <subscriber>.

REST

Info

Description

A user has removed notification subscriber.

Event ID: 4622

Message

Category

Severity

Subscriber: <subscriber> added subscription: <subscription>.

REST

Info

Description

A subscriber has added new subscription.

REST events | 347

Event ID: 4623

Message

Category

Severity

Subscriber: <subscriber> removed subscription: <subscription>.

REST

Info

Description

A subscriber has removed subscription.

Event ID: 4624

Message

Unable to add new subscriber. Max number of subscribers has been reached.

Category

REST

Severity

Warning

Description

Unable to add new subscriber as max number reached.

Event ID: 4625

Message

Unable to add new subscription. Max number of subscriptions for <subscriber> has been
reached.

Category

REST

Severity

Warning

Description

Unable to add new subscription as max number reached for the specified subscriber.

Event ID: 4626

Message

Category

Severity

NAE Script <name> has been created by user <user>.

REST

Info

Description

NAE Script has been created successfully.

Event ID: 4627

Message

Category

Severity

NAE Script <name> has been deleted by user <user>.

REST

Info

Description

NAE Script has been deleted successfully.

Event ID: 4628

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

348

Message

Category

Severity

NAE Agent <name> has been created by user <user>.

REST

Info

Description

NAE Agent has been created successfully.

Event ID: 4629

Message

Category

Severity

NAE Agent <name> has been updated by user <user>.

REST

Info

Description

NAE Agent has been updated successfully.

Event ID: 4630

Message

Category

Severity

NAE Agent <name> has been deleted by user <user>.

REST

Info

Description

NAE Agent has been deleted successfully.

Event ID: 4631

Message

Category

Severity

Error rebooting switch, reboot command: <command>, error received: <error>

REST

Error

Description

Logs an error if a reboot fails.

Event ID: 4632

Message

Category

Severity

Connection to HPE Aruba Networking Central on location <central_location> on VRF <vrf>
with Source IP <source_ip> has been successfully established.

REST

Info

Description

Connection is established with HPE Aruba Networking Central.

Event ID: 4633

Message

Connection to HPE Aruba Networking Central on location <central_location> on VRF <vrf>

REST events | 349

and Source IP <source_ip> has been closed by HPE Aruba Networking Central. Requesting
new HPE Aruba Networking Central location from CLI/DHCP/Activate.

REST

Info

Connection to HPE Aruba Networking Central has been closed by HPE Aruba Networking
Central. Request to get new location from CLI/DHCP/Activate.

Connection to HPE Aruba Networking Central on location <central_location> on VRF <vrf>
and Source IP <source_ip> has been closed by HPE Aruba Networking Central. Trying to
reconnect.

REST

Info

Connection to HPE Aruba Networking Central has been closed by HPE Aruba Networking
Central. Trying to reconnect.

Received HPE Aruba Networking Central location <central_location> on VRF <vrf> with
Source IP <source_ip>

REST

Info

Category

Severity

Description

Event ID: 4634

Message

Category

Severity

Description

Event ID: 4635

Message

Category

Severity

Description

Received new HPE Aruba Networking Central location.

Event ID: 4636

Message

Category

Severity

Description

Event ID: 4637

Message

Received new HPE Aruba Networking Central location. Closing existing connection with
HPE Aruba Networking Central on location <central_location> on VRF <vrf> with Source IP
<source_ip>.

REST

Info

Received new HPE Aruba Networking Central location. Closing existing connection with
HPE Aruba Networking Central.

Internal error. Closing connection to HPE Aruba Networking Central on location <central_
location> on VRF <vrf> with Source IP <source_ip>.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

350

Category

Severity

REST

Error

Description

Internal error. Closing connection to HPE Aruba Networking Central.

Event ID: 4638

Message

Category

Severity

Description

Event ID: 4639

Message

Category

Severity

Waiting for HPE Aruba Networking Central location from CLI/DHCP/Activate Server.

REST

Info

Waiting for HPE Aruba Networking Central location from Central Source
(CLI/DHCP/Activate Server).

Connecting to HPE Aruba Networking Central on location <central_location> on VRF <vrf>
with Source IP <source_ip>.

REST

Info

Description

Connecting to HPE Aruba Networking Central.

Event ID: 4640

Message

Category

Severity

Failed to connect to HPE Aruba Networking Central on location <central_location> on VRF
<vrf> with Source IP <source_ip>

REST

Error

Description

Failed to connect to HPE Aruba Networking Central.

Event ID: 4641

Message

Category

Severity

HPE Aruba Networking Central is disabled.

REST

Info

Description

The HPE Aruba Networking Central feature is disabled.

Event ID: 4642

Message

HPE Aruba Networking Central is disabled. Closing connection to HPE Aruba Networking

REST events | 351

Central on location <central_location> on VRF <vrf> with Source IP <source_ip>

Category

Severity

REST

Info

Description

The HPE Aruba Networking Central feature is disabled.

Event ID: 4643

Message

Category

Severity

HPE Aruba Networking Central is enabled.

REST

Info

Description

The HPE Aruba Networking Central feature is enabled.

Event ID: 4645

Message

Category

Severity

Activate server <activate_address> is reachable via VRF <vrf>.

REST

Info

Description

Activate server is reachable via an active VRF.

Event ID: 4646

Message

Category

Severity

Activate server <activate_address> is not reachable through any supported VRF.

REST

Info

Description

Activate server is not reachable through any supported VRF.

Event ID: 4647

Message

Category

Severity

Switch time is synced with NTP Servers.

REST

Info

Description

Switch time is synced with NTP Servers.

Event ID: 4648

Message

Switch time is synced with Activate Server <activate_address>.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

352

Category

Severity

REST

Info

Description

Switch time is synced with Activate Server.

Event ID: 4649

Message

Category

Severity

Unable to sync switch time with Activate Server <activate_address> via VRF <vrf>.

REST

Error

Description

Unable to sync switch time with Activate Server.

Event ID: 4650

Message

Category

Severity

Description

Event ID: 4651

Message

Category

Severity

Description

Event ID: 4652

Message

Unable to fetch HPE Aruba Networking Central location <central_location> from <central_
source> via VRF <vrf>.

REST

Info

Unable to fetch HPE Aruba Networking Central location from Central Source
(CLI/DHCP/Activate Server).

HPE Aruba Networking Central location <central_location> successfully fetched from
<central_source> via VRF <vrf>

REST

Info

HPE Aruba Networking Central location successfully fetched from Central Source
(CLI/DHCP/Activate Server) via VRF.

Central connected, any config change through rest <rest_operation> operation may not be
persistent. If Central reapplies the config, change could be overwritten

Category

REST

Severity

Warning

Description

Central connected, any config change through rest may not be persistent, Central can
overwrite the change

Event ID: 4653

REST events | 353

Message

Category

Severity

User <user> has configured <mode> for configuration lockout

REST

Info

Description

Logs a message when a user changes the REST configuration lockout mode

Event ID: 4654

Message

Category

Severity

Description

Event ID: 4655

Message

Category

Severity

HPE Aruba Networking Central support mode is <mode> for a vtysh session

REST

Info

Logs a message when a HPE Aruba Networking Central support mode is enabled or
disabled

User <user_name> logged in from <identity> through REST session

REST

Info

Description

Logs a message when a user login is successful

Event ID: 4656

Message

Category

Severity

User <user_name> login from <identity> for REST session has failed

REST

Error

Description

Logs a message when a user login fails

Event ID: 4657

Message

Category

Severity

User <user_name> logged out of REST session from <identity>

REST

Info

Description

Logs a message when a user logs out of a session

Event ID: 4658

Message

REST session from <identity> with User <user_name> is rejected because maximum

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

354

session limit is reached

Category

REST

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached

Event ID: 4659

Message

Category

Severity

{user_agent} session from {identity} with User {user_name} timed out due to idle timeout

REST

Info

Description

Logs a message when a REST session timed out due to the session being idle

Event ID: 4660

Message

Category

Severity

REST server is enabled on VRF <vrf_name>

REST

Info

Description

Logs a message when the REST server is enabled on a VRF

Event ID: 4661

Message

Category

Severity

REST server is disabled on VRF <vrf_name>

REST

Info

Description

Logs a message when the REST server is disabled on a VRF

Event ID: 4662

Message

Category

Severity

Description

Event ID: 4663

User {user_name} login from {ip_address} for REST session has failed since the user is
trying to login through an interface which is not allowed. Allowed interfaces are: {mgmt_
intf}

REST

Error

Logs a message when a user login fails since the access through this management
interface is not allowed.

REST events | 355

Message

Category

Severity

Starting HTTPS firmware upgrade via: {interface}

REST

Info

Description

Logs a message when a firmware upgrade is executed from a management interface

Event ID: 4664

Message

Category

Severity

REST API and Notifications server is ready to serve requests.

REST

Info

Description

Logs a message when the REST API and Notifications server is ready to serve requests.

Event ID: 4665

Message

Category

Severity

Pagination session created with ID: {page_session_id}

REST

Info

Description

Logs a message when a pagination session is created.

Event ID: 4666

Message

Category

Severity

REST

Info

Description

Logs a message when a pagination session is deleted.

Event ID: 4667

Message

Category

Severity

Subscription created with ID: {subscription_id} URI: {uri} Interval: {interval}

REST

Info

Description

Logs a message when a notification subscription is created.

Event ID: 4668

Message

Subscription deleted with ID: {subscription_id} URI: {uri} Interval: {interval}

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

356

Category

Severity

REST

Info

Description

Logs a message when a notification subscription is deleted.

Event ID: 466x

Message

Category

Severity

Description

REST

Info

REST events | 357

Chapter 120

Self Test events

Self Test events

The following are the events related to self test.

Event ID: 4501

Message

Selftest has started on subsystem <subsystem>

Category

Self Test

Severity

Information

Description

logs the start of selftest on a particular subsystem

Event ID: 4502

Message

Selftest has completed on subsystem <subsystem>

Category

Self Test

Severity

Information

Description

logs the completion of selftest on a particular subsystem

Event ID: 4503

Message

Selftest has failed on subsystem <subsystem> with error code <value>': yes

Category

Self Test

Severity

Error

Description

logs the selftest failure of a particular subsystem

Event ID: 4504

Message

Selftest has failed on <stack>/<slot>/<interface> with error code <value>': yes

Category

Self Test

Severity

Error

Description

logs the port selftest failure on a given subsystem

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

358

|           |         |        |           | Chapter | 121    |
| --------- | ------- | ------ | --------- | ------- | ------ |
|           |         |        | Self Test | Monitor | events |
| Self Test | Monitor | events |           |         |        |
Thefollowingaretheeventsrelatedtocryptographicself-testmonitor.
| Event ID:   | 16001 |                                                 |     |     |     |
| ----------- | ----- | ----------------------------------------------- | --- | --- | --- |
| Message     |       | TheFIPSPOSTservicehasreportedaself-testfailure. |     |     |     |
| Category    |       | SelfTestMonitor                                 |     |     |     |
| Severity    |       | Emergency                                       |     |     |     |
| Description |       | LogswhenafailureisreportedbytheFIPSPOSTservice. |     |     |     |
| Event ID:   | 16002 |                                                 |     |     |     |
| Message     |       | JitterEntropyhasreportedaself-testfailure.      |     |     |     |
| Category    |       | SelfTestMonitor                                 |     |     |     |
| Severity    |       | Emergency                                       |     |     |     |
Description LogswhenafailureisreportedbyaJitterEntropyself-test.
| Event ID: | 16003 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message Thecryptographicself-testmonitorhasdetectedareportedtestfailure.Theself-test
modehasbeenconfiguredtofail-secure.Theswitchwillberebooted.
| Category |     | SelfTestMonitor |     |     |     |
| -------- | --- | --------------- | --- | --- | --- |
| Severity |     | Emergency       |     |     |     |
Description Logsafail-secureeventfromthecryptographicself-testmonito
359
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 122

sFlow events

sFlow events

The following are the events related to sFlow.

Event ID: 1001

Message

Category

Severity

Failed to <operation> host sFlow agent: <error>

sFlow

Error

Description

Log a failure when trying to start/stop/restart host sFlow daemon.

Event ID: 1002

Message

Category

Severity

Failed to <operation> host sFlow configuration file <file>: <error>

sFlow

Error

Description

Log a failure when trying to read/write to host sFlow configuration file.

Event ID: 1003

Message

Category

Severity

Failed to <operation> sFlow configuration from bridge <bridge>: <error>

sFlow

Error

Description

Log a failure when trying to configure sFlow on SIM OVS.

Event ID: 1004

Message

Category

Severity

Failed to delete all iptable rules: <error>

sFlow

Error

Description

Log a failure when trying to delete all iptable rules added for sFlow.

Event ID: 1005

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

360

Message

Category

Severity

Failed to <operation> <chain> iptable rules for <port>: <error>

sFlow

Error

Description

Log a failure when trying to add/delete an iptable rule for sFlow.

Event ID: 1006

Message

Category

Severity

sFlow initialization failed.

sFlow

Error

Description

Logs an error if sFlow initialization fails.

Event ID: 1007

Message

Category

Severity

Invalid packet sent by ASIC in sFlow callback.

sFlow

Error

Description

Logs an error for an invalid packet in sFlow callback.

Event ID: 1008

Message

Category

Severity

Unable to get netdev for interface <interface>

sFlow

Error

Description

Logs an error if an interface does not have a netdev class.

Event ID: 1009

Message

Category

Severity

Failed to create KNET filter as description is blank

sFlow

Error

Description

Logs an error if the descrption to create a filter is blank.

Event ID: 1010

Message

Failed to create KNET filter for: <desc>

sFlow events | 361

Category

Severity

sFlow

Error

Description

Logs an error if sFlow KNET filter creation fails.

Event ID: 1011

Message

Category

Severity

The received sampled packet is null

sFlow

Error

Description

Logs an error if sampled packet is null.

Event ID: 1012

Message

Category

Severity

The sFlow agent is not initialized

sFlow

Error

Description

Logs an error if sFlow agent is not initialized.

Event ID: 1013

Message

Category

Severity

The sFlow sampler is not initialized

sFlow

Error

Description

Logs an error if sFlow sampler is not initialized.

Event ID: 1014

Message

Category

Severity

Cannot enable/disable sFlow on an invalid port: <port>

sFlow

Error

Description

Logs an error if sFlow is enabled/disabled on an invalid port.

Event ID: 1015

Message

sFlow sampler is not available on port: <port>

Category

sFlow

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

362

Severity

Error

Description

Logs an error if sFlow sampler is missing on a port.

Event ID: 1016

Message

Category

Severity

sFlow receiver is not available

sFlow

Error

Description

Logs an error if sFlow receiver is not available.

Event ID: 1017

Message

Category

Severity

Failed to retrieve port configuration: <error>

sFlow

Error

Description

Logs an error if port configuration is not available.

Event ID: 1018

Message

Category

Severity

Failed to set sampling rate on port <port>: <error>

sFlow

Error

Description

Logs an error if setting a sampling rate on a port fails.

Event ID: 1019

Message

Category

Severity

Failed to get sampling rate on port <port>: <error>

sFlow

Error

Description

Logs an error if unable to retrieve sampling rate on a port.

Event ID: 1020

Message

Category

Severity

Invalid agent interface IP address: <ip_address>

sFlow

Error

Description

Logs an error in case of invalid agent interface IP address configuration.

sFlow events | 363

Event ID: 1021

Message

Category

Severity

Invalid collector IP address: <ip_address>

sFlow

Error

Description

Logs an error in case of invalid collector IP address configuration.

Event ID: 1022

Message

Category

Severity

Failed to get interface statistics for unit <unit> port <port>: <error>

sFlow

Error

Description

Logs an error if unable to retrieve interface statistics.

Event ID: 1023

Message

sFlow agent created.

Category

sFlow

Severity

Information

Description

Logs creation of sFlow agent.

Event ID: 1024

Message

sFlow agent deleted.

Category

sFlow

Severity

Information

Description

Logs deletion of sFlow agent.

Event ID: 1025

Message

Changed sFlow sampling rate from <old_rate> to <new_rate>.

Category

sFlow

Severity

Information

Description

Logs a change in sFlow sampling rate.

Event ID: 1026

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

364

Message

Set sFlow agents header len to <hdrlen>.

Category

sFlow

Severity

Information

Description

Logs sFlow agents header length event.

Event ID: 1027

Message

Set sFlow agents IP to <ip_addr>.

Category

sFlow

Severity

Information

Description

Logs setting IP address to sFlow agent.

Event ID: 1028

Message

Set max datagram size on sFlow agent to <dgramsize>.

Category

sFlow

Severity

Information

Description

Log setting max datagram size on sFlow agent.

Event ID: 1029

Message

Add sFlow poller on <port_name> with ifIndex <ifIndex> at interval <intvl>.

Category

sFlow

Severity

Information

Description

Add sFlow poller on a port.

Event ID: 1030

Message

Remove sFlow poller on <ifIndex>.

Category

sFlow

Severity

Information

Description

Delete sFlow poller on a port.

Event ID: 1031

Message

Set polling interval of <intvl> on sFlow agent.

sFlow events | 365

Category

sFlow

Severity

Information

Description

Set polling interval for sFlow agent.

Event ID: 1032

Message

sFlow sampling mode set to <mode>.

Category

sFlow

Severity

Information

Description

Logs change in sFlow mode.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

366

Chapter 123

SFTP Client events

SFTP Client events

The following are the events related to SFTP client.

Event ID: 5301

Message

SFTP file transfer from <from> to <to> completed.

Category

SFTP Client

Severity

Information

Description

SFTP file transfer completed

Event ID: 5302

Message

SFTP file transfer from <from> to <to> failed - <status>.

Category

SFTP Client

Severity

Information

Description

SFTP file transfer failed

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

367

Chapter 124

Smartlink events

Smartlink events

The following are the events related to smartlink.

Event ID: 11301

Message

Flush message received on <ifName> with control VLAN <id>

Category

Smartlink

Severity

Information

Description

Event raised when flush message received on interface with control vlan

Event ID: 11302

Message

Active link of the smartlink group <id> changed to <ifName>

Category

Smartlink

Severity

Information

Description

Event raised when active link changed in the smartlink group

Event ID: 11303

Message

Backup link of the smartlink group <id> changed to <ifName>

Category

Smartlink

Severity

Information

Description

Event raised when backup link changed in the smartlink group

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

368

Chapter 125

SNMP events

SNMP events

The following are the events related to SNMP.

Event ID: 7101

Message

Snmp agent is up and running in namespace <vrf>

Category

SNMP

Severity

Information

Description

SNMP agent is enabled.

Event ID: 7102

Message

Snmp sub agent is up and running in namespace <vrf>

Category

SNMP

Severity

Information

Description

SNMP sub agent is enabled.

Event ID: 7103

Message

Snmp agent is disabled for namespace <vrf>

Category

SNMP

Severity

Information

Description

SNMP agent is disabled.

Event ID: 7104

Message

Snmp sub agent is disabled for namespace <vrf>

Category

SNMP

Severity

Information

Description

SNMP sub agent is disabled.

Event ID: 7105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

369

Message

Failed to poll snmp

Category

SNMP

Severity

Information

Description

SNMP poll thread creation failed.

Event ID: 7106

Message

Snmp and credential manager integration failed

Category

SNMP

Severity

Information

Description

SNMP failed to synchronize with credential manager

Event ID: 7107

Message

Snmp system now configured

Category

SNMP

Severity

Information

Description

SNMP system is configured.

Event ID: 7108

Message

Snmp and database Integration has been initialized

Category

SNMP

Severity

Information

Description

Snmp successfully synchronized with database

Event ID: 7109

Message

Successfully initialized all SNMP plugins

Category

SNMP

Severity

Information

Description

SNMP plugins successfully initialized.

Event ID: 7110

Message

Destroyed all SNMP plugins

SNMP events | 370

Category

SNMP

Severity

Information

Description

SNMP plugin successfully deinitialized.

Event ID: 7111

Message

SNMP cache sync on-demand is set to: <truth_value>

Category

SNMP

Severity

Information

Description

SNMP on demand idl sync.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

371

Chapter 126

SSH client events

SSH client events

The following are the events related to SSH client.

Event ID: 9001

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> is established for user <username>
over port <port_num>

Category

SSH client

Severity

Information

Description

SSH client session is successful.

Event ID: 9002

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> over port <port_num> is denied

Category

SSH client

Severity

Error

Description

SSH client session is denied

Event ID: 9003

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> is succesfully closed for user
<username> over port <port_num>

Category

SSH client

Severity

Information

Description

SSH client session is successful.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

372

Chapter 127

SSH server events

SSH server events

The following are the events related to SSH server.

Event ID: 5201

Message

SSH host-key <key_name> is installed.

Category

SSH server

Severity

Info

Description

Logs a message when the SSH host-key generated

Event ID: 5202

Message

SSH server is enabled on VRF <vrf_name>.

Category

SSH server

Severity

Info

Description

Logs a message when the SSH server is enabled on a VRF

Event ID: 5203

Message

SSH server is disabled on VRF <vrf_name>.

Category

SSH server

Severity

Info

Description

Logs a message when the SSH server is disabled on a VRF

Event ID: 5204

Message

SSH client-public-key <key_name> was installed for the user <username>.

Category

SSH server

Severity

Info

Description

Logs a message when add ssh client-public-key into authorized_keys file

Event ID: 5205

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

373

Message

SSH client-public-key <key_name> was removed for the user <username>.

Category

SSH server

Severity

Info

Description

Logs a message when delete ssh client-public-key into authorized_keys file

Event ID: 5207

Message

An internal error occurred while reading the SSH host-key <key_name>.

Category

SSH server

Severity

Info

Description

Logs a message when the SSH host-key is corrupted

Event ID: 5208

Message

Failed to enable SSH server on VRF <vrf_name>. Admin password is not set.

Category

SSH server

Severity

Error

Description

Logs a message when a user tries to enable SSH server without setting admin password

Event ID: 5209

Message

User <user_name> logged in from <ip_address> through SSH session.

Category

SSH server

Severity

Info

Description

Logs a message when a user login is successful

Event ID: 5210

Message

User {user_name} login from {ip_address} for SSH session failed during password based
authentication.

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails

Event ID: 5211

SSH server events | 374

Message

User <user_name> logged out of SSH session from <ip_address>.

Category

SSH server

Severity

Info

Description

Logs a message when a user logs out of a session

Event ID: 5212

Message

SSH session from <ip_address> is rejected because maximum number of SSH sessions is
reached.

Category

SSH server

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached.

Event ID: 5213

Message

SSH session from user {user_name} closed because maximum number of sessions per
user is reached.

Category

SSH server

Severity

Warning

Description

Logs a message when a user session is closed while maximum number of sessions per
user are reached.

Event ID: 5214

Message

SSH session from {ip_address} denied due to host key verification failure.

Category

SSH server

Severity

Warning

Description

Logs a message when a user session is closed due to host key failure.

Event ID: 5215

Message

SSH session from {ip_address} for user {user_name} denied. The allowed user
management interfaces are: {mgmt_intf

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails since the access through this management
interface is not allowed

Event ID: 5216

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

375

Message

SSH session from {ip_address} for user {user_name} rejected due to failed public key
validation

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails due to public key failure

Event ID: 5217

Message

Category

Severity

SSH server on VRF {vrf_name} is in an error state.

SSH server

Error

Description

Logs a message when SSH server goes into an error state.

Event ID: 5218

Message

Category

Severity

Converting configured SSH server allow-list entry {original_ip} to CIDR format ({new_ip})

SSH server

Info

Description

Logs a message when SSH server converts an IP address to CIDR format.

Event ID: 5219

Message

Failed to convert configured SSH server allow-list entry {original_ip} to CIDR format, using
original address as-is

Category

SSH server

Severity

Error

Description

Logs a message when SSH server fails to convert an IP address to CIDR format.

Event ID: 5220

Message

RADIUS authorize-only request failed for SSH session from {ip_address} for user {user_
name}.

Category

SSH server

Severity

Error

Description

Logs a message when SSH connection fails due to authorize-only attempt.

Event ID: 5221

SSH server events | 376

Message

SSH session from {ip_address} denied because username {user_name} not found in
authenticating certificate Common Name or User Principal Name fields.

Category

SSH server

Severity

Error

Description

Logs a message when the authenticating username was searched for and not found in
the authenticating certificate.

Event ID: 5222

Message

Category

Severity

SSH session from {ip_address} for user {user_name} denied by SSH server allow-list

SSH server

Error

Description

Logs a message when the authenticating IP is denied due to the SSH server allow list.

Event ID: 5223

Message

Category

Severity

Logs a message when an empty SSH allow-list has been enabled.

SSH server

Warning

Description

An empty SSH allow-list has been enabled and all new SSH connections will be denie

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

377

Chapter 128

Supportability events

Supportability events

The following are the events related to supportability.

Event ID: 1201

Message

<process> crashed due to <signal>,<timestamp>

Category

Supportability

Severity

Critical

Description

A daemon has crashed and generated core dump

Event ID: 1202

Message

Kernel panic occurred

Category

Supportability

Severity

Error

Description

Logs kernel crash

Event ID: 1203

Message

Kernel failed to compress vmcore. Error log:<err_desc>

Category

Supportability

Severity

Error

Description

Logs kernel failed to compress vmcore

Event ID: 1204

Message

Kernel panic occurred and secondary kernel failed to save uncompressed core. Error
log:<err_desc>

Category

Supportability

Severity

Error

Description

Logs kernel panic occurred and secondary kernel core failed to save uncompressed core

Event ID: 1205

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

378

Message Kernelpanicoccurredandsystemisrestoredbacktonormalstate
| Category    | Supportability          |     |
| ----------- | ----------------------- | --- |
| Severity    | Error                   |     |
| Description | Logskernelpanicoccurred |     |
| Event       | ID: 1206                |     |
Message
Modulerebooted.Reason:<reason>,Boot-ID:<boot_id>
| Category    | Supportability                           |     |
| ----------- | ---------------------------------------- | --- |
| Severity    | Info                                     |     |
| Description | Logsrebootinformation                    |     |
| Event       | ID: 1207                                 |     |
| Message     | Availablesystemmemoryisbacktonormalstate |     |
| Category    | Supportability                           |     |
| Severity    | Warning                                  |     |
Description Eventraisedwhenavailablesystemmemoryisrestoredtonormallevel.
| Event | ID: 1208 |     |
| ----- | -------- | --- |
Message Highsystemmemoryusagedetected.Highmemoryusagedaemonsare<daemons>
| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Error          |     |
Description Eventraisedwhensystemmemoryusagegoesbeyondhighthreshold.
| Event    | ID: 1209 (Severity:                       | Emergency) |
| -------- | ----------------------------------------- | ---------- |
| Message  | Availablesystemmemoryiscriticallylow':yes |            |
| Category | Supportability                            |            |
| Severity | Emergency                                 |            |
Description Eventraisedwhensystemmemoryusagecrossescriticalthreshold.
| Event   | ID: 1210                                |     |
| ------- | --------------------------------------- | --- |
| Message | Memoryreservationforrebootlibraryfailed |     |
Supportabilityevents|379

| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Warning        |     |
Description Eventraisedwhenmemoryreservationforrebootlibraryfails.
| Event       | ID: 1211 (Severity:                       | Emergency) |
| ----------- | ----------------------------------------- | ---------- |
| Message     | Unabletogetcurrentsystemmemoryusage       |            |
| Category    | Supportability                            |            |
| Severity    | Emergency                                 |            |
| Description | Eventraisedwhensystemmemoryreadisfailing. |            |
| Event       | ID: 1212 (Severity:                       | Emergency) |
Message Availablesystemmemoryiscriticallylow.Rebootwillbetriggeredsoon.
| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Emergency      |     |
Description Availablememoryiscriticallylow,systemwillberebooted.
| Event | ID: 1213 |     |
| ----- | -------- | --- |
Message RMONalarm<index>-Risingthresholdvalueof<threshold>reachedfor<oid>.
| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Info           |     |
Description Eventraisedwhenthesampledvaluehasreachedtherisingthreshold.
| Event | ID: 1214 |     |
| ----- | -------- | --- |
Message
RMONalarm<index>-Fallingthresholdvalueof<threshold>reachedfor<oid>.
| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Info           |     |
Description Eventraisedwhenthesampledvaluehasreachedthefallingthreshold.
| Event    | ID: 1215                         |     |
| -------- | -------------------------------- | --- |
| Message  | <process>exiting.Reason:<reason> |     |
| Category | Supportability                   |     |
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries) 380

| Severity    | Error                                              |            |
| ----------- | -------------------------------------------------- | ---------- |
| Description | Aprocessisexitingduetoanunrecoverableerror         |            |
| Event       | ID: 1216 (Severity:                                | Emergency) |
| Message     | <process>exiting.Reason:<reason>                   |            |
| Category    | Supportability                                     |            |
| Severity    | Emergency                                          |            |
| Description | Acriticalprocessisexitingduetoanunrecoverableerror |            |
| Event       | ID: 1217                                           |            |
| Message     | Coredump(s)aredeletedbyuser                        |            |
| Category    | Supportability                                     |            |
| Severity    | Info                                               |            |
| Description | Coredump(s)aredeletedbyuser                        |            |
| Event       | ID: 1218                                           |            |
Message
Remoteloggingto<remote_host>over<vrf>vrfadded.
| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Info           |     |
Description Eventraisedwhenanewsyslogserverisaddedforremotelogging.
| Event    | ID: 1219                                         |     |
| -------- | ------------------------------------------------ | --- |
| Message  | Remoteloggingto<remote_host>over<vrf>vrfremoved. |     |
| Category | Supportability                                   |     |
| Severity | Info                                             |     |
Description Eventraisedwhenasyslogserverisremovedfromremotelogging.
| Event | ID: 1220 |     |
| ----- | -------- | --- |
Message Configurationofremoteloggingto<remote_host>over<vrf>vrfmodified.
| Category | Supportability |     |
| -------- | -------------- | --- |
| Severity | Info           |     |
Description Eventraisedwhenanexistingsyslogserverconfigurationismodified.
Supportabilityevents|381

Event ID: 1221

Message

Watchdog timeout is increased due to high memory usage

Category

Supportability

Severity

Info

Description

Event raised when available RAM memory goes below the threshold and watchdog
timeout is increased.

Event ID: 1222

Message

Watchdog timeout is restored to default value

Category

Supportability

Severity

Info

Description

Event raised when the available RAM memory is restored to normal range and the
watchdog timeout is restored to default value.

Event ID: 1223

Message

The <log_type> buffer is almost full.': yes

Category

Supportability

Severity

Warning

Description

Event raised the log buffer is almost full. User can copy these logs before the logs being
overwritten.

Event ID: 1224

Message

The <log_type> buffer has wrapped, older logs will be overwritten.': yes

Category

Supportability

Severity

Warning

Description

Event raised the log buffer has wrapped; older logs will be overwritten.

Event ID: 1225

Message

Collection of support-files named <name> of type <type> is requested for the module
<module>.

Category

Supportability

Severity

Info

Description

Event raised when suppuort-files collection is requested.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

382

Event ID: 1226

Message

Support-files named <name> is requested for deletion.

Category

Supportability

Severity

Info

Description

Event raised when a requst recived to delete given support-files.

Event ID: 1227

Message

Support-files named <name> is deleted.

Category

Supportability

Severity

Info

Description

Event raised when suppuort-files is deleted.

Event ID: 1228

Message

Collection of support-files named <name> failed due to <reason>.

Category

Supportability

Severity

Error

Description

Event raised when collection support-files failed.

Event ID: 1229

Message

Deletion of support-files named <name> failed due to <reason>.

Category

Supportability

Severity

Error

Description

Event raised when failed to delete a given support-files.

Event ID: 1230

Message

Collection of support-files named <name> is <state>.

Category

Supportability

Severity

Info

Description

Event raised when collection of support-files state changes.

Event ID: 1231

Supportability events | 383

Message

Syslog client restarted due to configuration change.

Category

Supportability

Severity

Info

Description

Event raised when remote syslog is restarted due to configuration change.

Event ID: 1232

Message

The security log buffer is cleared

Category

Supportability

Severity

Info

Description

Event raised as the security log buffer is cleared

Event ID: 1233

Message

Starting System Logging Service.

Category

Supportability

Severity

Info

Description

Event raised when remote syslog is starting

Event ID: 1234

Message

Started System Logging Service.

Category

Supportability

Severity

Info

Description

Event raised when remote syslog is started

Event ID: 1235

Message

Switch boot count is : {boot_count_status}

Category

Supportability

Severity

Info

Description

Logs reboot count information

SynchE events
The following are the events related to synchE.

Event ID: 16201

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

384

Message

Category

Severity

SyncE is globally enabled.

SynchE

Info

Description

Event reported when SyncE is globally enabled.

Event ID: 16202

Message

Category

Severity

SyncE is globally disabled.

SynchE

Info

Description

Event reported when SyncE is globally disabled.

Event ID: 16203

Message

Category

Severity

SyncE network option is set to {option}.

SynchE

Info

Description

Event reported when SyncE network option is set.

Event ID: 16204

Message

Category

Severity

SyncE hold off time is set to {value}.

SynchE

Info

Description

Event reported when SyncE hold off time is set.

Event ID: 16205

Message

Category

Severity

SyncE wait to restore time is set to {value}.

SynchE

Info

Description

Event reported when SyncE wait to restore is set.

Event ID: 16206

Message

Category

SyncE quality mode is disabled.

SynchE

SynchE events | 385

Severity

Info

Description

Event reported when SyncE quality mode is disabled.

Event ID: 16207

Message

Category

Severity

SyncE quality mode is enabled.

SynchE

Info

Description

Event reported when SyncE quality mode is enabled.

Event ID: 16208

Message

Category

Severity

ESMC is enabled on port {name}.

SynchE

Info

Description

Event reported when ESMC is enabled on a port.

Event ID: 16209

Message

Category

Severity

ESMC is disabled on port {name}.

SynchE

Info

Description

Event reported when ESMC is disabled on a port.

Event ID: 16210

Message

Category

Severity

SyncE priority on port {name} is set to {value}.

SynchE

Info

Description

Event reported when SyncE priority is set on a port.

Event ID: 16211

Message

Category

Severity

SyncE priority {value} is not unique.

SynchE

ERR

Description

Event reported when SyncE priority being set is not unique.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

386

Event ID: 16212

Message

Category

Severity

SyncE initial quality level on port {name} is set to {quality}.

SynchE

Info

Description

Event reported when SyncE initial quality level is set on a port.

Event ID: 16213

Message

Category

Severity

Description

Event ID: 16214

Message

Category

Severity

SyncE initial quality level {quality} is not valid for network option {option}.

SynchE

ERR

Event reported when the initial quality level for SyncE that is set on a port is not valid for
the network option configured.

SyncE transmit-only is set on port {name}.

SynchE

ERR

Description

Event reported when SyncE transmit only is set on a port.

Event ID: 16215

Message

Category

Severity

Port {name} is selected as SyncE primary port.

SynchE

Info

Description

Event reported when SyncE primary port is selected.

Event ID: 16216

Message

Category

Severity

Port {name} is selected as SyncE secondary port.

SynchE

Info

Description

Event reported when SyncE secondary port is selected.

Event ID: 16217

SynchE events | 387

Message

Category

Severity

Description

Event ID: 16218

Message

Category

Severity

SyncE Port {name} has not received any ESMC packets for {timeout} seconds.

SynchE

WARN

Event reported when SyncE Port ESMC message is not received during the timeout
window.

SyncE Port {name} status has changed, state {state}, QL {quality}.

SynchE

Info

Description

Event reported when SyncE Port status changes.

Event ID: 16219

Message

Category

Severity

SyncE DPLL clock state has changed to {dpll_state}.

SynchE

Info

Description

Event reported when SyncE DPLL clock status changes.

Event ID: 16220

Message

Category

Severity

SyncE not enabled on port {name} - a unique priority must be configured when ESMC is
enabled.

SynchE

ERR

Description

Event reported when SyncE priority port is not set and ESMC is enabled.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

388

Chapter 129

SYS events

SYS events

The following are the events related to SYS.

Event ID: 701

Message

Category

Severity

Failed to read FRU data from base system

SYS

Info

Description

Log when failed to read FRU data from base system

Event ID: 702

Message

Category

Severity

Failed to read FRU header

SYS

Info

Description

Log when failed to read FRU header

Event ID: 703

Message

Category

Severity

Error reading FRU EEPROM Header

SYS

Info

Description

log when FRU EEPROM Header failed

Event ID: 704

Message

Category

Severity

Failed to intialize devices

SYS

Info

Description

Log when failed to intialize devices

Event ID: 705

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

389

Message

Category

Severity

Failed to allocate memory for <value>

SYS

Info

Description

Log when failed to allocate memory

Event ID: 706

Message

Category

Severity

Initiating system reboot

SYS

Info

Description

Indicates that the chassis is about to reboot.

Event ID: 707

Message

Category

Severity

Initiating chassis thermal reboot

SYS

Error

Description

Indicates that the chassis experienced a thermal event and will reboot

Event ID: 708

Message

Category

Severity

Invalid Device Version Programmed. Please check MFG data programmed on the device.

SYS

Error

Description

Indicates invalid device version is programmed on the device

Event ID: 709

Message

Category

Severity

Failed to read assembly revision

SYS

Error

Description

Indicates device has failed to read assembly revision that is programmed

Event ID: 710

Message

The system has entered the recovery console

SYS events | 390

Category

Severity

SYS

Info

Description

Indicates that the system has entered the recovery console

Event ID: 711

Message

Category

Severity

Detected DDR errors during uboot BIST, module {module} reported {error_sbe}

SYS

Info

Description

ndicates that the system has detected DDR errors during uboot BIST

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

391

Chapter 130

SYSMON events

SYSMON events

The following are the events related to SYSMON.

Event ID: 6301

Message

System resource utilization poll interval is changed to <poll>' throttle_count: 40

Category

SYSMON

Severity

Information

Description

System resource utilization poll change event

Event ID: 6302

Message

Category

Severity

Failed to read system memory usage for module <module_num>

SYSMON

Warning

Description

Warns a user when system memory usage read failed

Event ID: 6303

Message

Current system memory usage for module <module_num> is <mem_usage>%

Category

SYSMON

Severity

Information

Description

Reports current system memory usage in percentage

Event ID: 6304

Message

Category

Severity

Storage utilization for <partition_name> partition is at <utilization>% in module <module_
name>': yes

SYSMON

Warning

Description

Warns a user when the storage utilization has exceeded the warning limit.

Event ID: 6305

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

392

Message

Storage <partition_name> partition high utilization alert. Utilization is at <utilization>% in
module <module_name>': yes

Category

SYSMON

Severity

Error

Description

Raises high storage utilization alert when the utilization crosses higher utilization limit.

Event ID: 6306

Message

Category

Severity

Excessive write to <partition_name> partition in module <module_name> observed. <mem_
usage>GB written over past <unit_count> <unit>': yes

SYSMON

Warning

Description

Warns a user when higher write to the storage observed

Event ID: 6307

Message

Category

Severity

Excessive write to swap in module <module_name> observed. <mem_usage>GB written
over past <unit_count> <unit>': yes

SYSMON

Warning

Description

Warns a user when higher write to the swap observed.

Event ID: 6308

Message

Excessive write to <partition_name> partition in module <module_name> observed. <mem_
usage>GB written over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Error

Description

Warns a user when excessive write to the storage observed

Event ID: 6309

Message

Excessive write to swap in module <module_name> observed. <mem_usage>GB written
over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Error

Description

Warns a user when excessive write to the swap observed.

SYSMON events | 393

Chapter 131

TCAM events

TCAM events

The following are the events related to TCAM.

Event ID: 10201

Message

Category

Severity

"Policer installation has failed"

TCAM

Error

Description

Policer installation failure

Event ID: 10202

Message

Category

Severity

"TCAM entry installation has failed in table <table_name>"

TCAM

Error

Description

TCAM entry installation failure

Event ID: 10203

Message

Category

Severity

"Installation of TCAM table <table_name> has failed"

TCAM

Error

Description

TCAM table installation failure

Event ID: 10204

Message

Category

Severity

"High-capacity TCAM/LPM entry installation failed in table <table_name>"

TCAM

Error

Description

High-capacity TCAM/LPM entry installation failure

Event ID: 10205

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

394

Message

Category

Severity

"High-capacity TCAM/LPM table <table_name> installation failed"

TCAM

Error

Description

High-capacity TCAM/LPM table installation failure

Event ID: 10206

Message

Category

Severity

"Counter installation has failed"

TCAM

Error

Description

TCAM Counter installation failure

Event ID: 10207

Message

Category

Severity

"Range Checker installation has failed"

TCAM

Error

Description

TCAM Range Checker installation failure

Event ID: 10208

Message

Category

Severity

"Policer uninstallation has failed"

TCAM

Error

Description

Policer uninstallation failure

Event ID: 10209

Message

Category

Severity

"TCAM entry uninstallation has failed in table <table_name>"

TCAM

Error

Description

TCAM entry uninstallation failure

Event ID: 10210

Message

"High-capacity TCAM/LPM entry uninstallation failed in table <table_name>"

TCAM events | 395

Category

Severity

TCAM

Error

Description

High-capacity TCAM/LPM entry uninstallation failure

Event ID: 10211

Message

Category

Severity

"High-capacity TCAM/LPM table uninstallation failed"

TCAM

Error

Description

High-capacity TCAM/LPM table uninstallation failure

Event ID: 10212

Message

Category

Severity

"Counter uninstallation has failed"

TCAM

Error

Description

TCAM Counter uninstallation failure

Event ID: 10213

Message

Category

Severity

"Range Checker uninstallation has failed"

TCAM

Error

Description

TCAM Range Checker uninstallation failure

Event ID: 10214

Message

Category

Severity

"TCAM Context Group selectors have been exhausted"

TCAM

Error

Description

TCAM Context Group selectors have been exhausted

Event ID: 10215

Message

"TCAM Context Group IDs have been exhausted"

Category

TCAM

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

396

Severity

Error

Description

TCAM Context Group IDs have been exhausted

TCAM events
The following are the events related to TCAM.

Event ID: 10201

Message

Category

Severity

"Policer installation has failed"

TCAM

Error

Description

Policer installation failure

Event ID: 10202

Message

Category

Severity

"TCAM entry installation has failed in table <table_name>"

TCAM

Error

Description

TCAM entry installation failure

Event ID: 10203

Message

Category

Severity

"Installation of TCAM table <table_name> has failed"

TCAM

Error

Description

TCAM table installation failure

Event ID: 10204

Message

Category

Severity

"High-capacity TCAM/LPM entry installation failed in table <table_name>"

TCAM

Error

Description

High-capacity TCAM/LPM entry installation failure

Event ID: 10205

Message

"High-capacity TCAM/LPM table <table_name> installation failed"

TCAM events | 397

Category

Severity

TCAM

Error

Description

High-capacity TCAM/LPM table installation failure

Event ID: 10206

Message

Category

Severity

"Counter installation has failed"

TCAM

Error

Description

TCAM Counter installation failure

Event ID: 10207

Message

Category

Severity

"Range Checker installation has failed"

TCAM

Error

Description

TCAM Range Checker installation failure

Event ID: 10208

Message

Category

Severity

"Policer uninstallation has failed"

TCAM

Error

Description

Policer uninstallation failure

Event ID: 10209

Message

Category

Severity

"TCAM entry uninstallation has failed in table <table_name>"

TCAM

Error

Description

TCAM entry uninstallation failure

Event ID: 10210

Message

"High-capacity TCAM/LPM entry uninstallation failed in table <table_name>"

Category

TCAM

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

398

Severity

Error

Description

High-capacity TCAM/LPM entry uninstallation failure

Event ID: 10211

Message

Category

Severity

"High-capacity TCAM/LPM table uninstallation failed"

TCAM

Error

Description

High-capacity TCAM/LPM table uninstallation failure

Event ID: 10212

Message

Category

Severity

"Counter uninstallation has failed"

TCAM

Error

Description

TCAM Counter uninstallation failure

Event ID: 10213

Message

Category

Severity

"Range Checker uninstallation has failed"

TCAM

Error

Description

TCAM Range Checker uninstallation failure

Event ID: 10214

Message

Category

Severity

"TCAM Context Group selectors have been exhausted"

TCAM

Error

Description

TCAM Context Group selectors have been exhausted

Event ID: 10215

Message

Category

Severity

"TCAM Context Group IDs have been exhausted"

TCAM

Error

Description

TCAM Context Group IDs have been exhausted

TCAM events | 399

Event ID: 10216

Message

Category

Severity

Policer resources have been exhausted.

TCAM

Error

Description

Policer resources have been exhausted.

Event ID: 10217

Message

Category

Severity

TCAM entries have been exhausted.

TCAM

Error

Description

TCAM entries have been exhausted.

Event ID: 10218

Message

Category

Severity

TCAM tables have been exhausted.

TCAM

Error

Description

TCAM tables have been exhausted.

Event ID: 10219

Message

Category

Severity

TCAM ranges have been exhausted.

TCAM

Error

Description

TCAM ranges have been exhausted.

Event ID: 10220

Message

Category

Severity

TCAM counters have been exhausted.

TCAM

Error

Description

TCAM counters have been exhausted.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

400

Chapter 132

Telnet server events

Telnet server events

The following are the events related to telnet server.

Event ID: 12901

Message

TELNET server is enabled on VRF <vrf_name>.

Category

Telnet server

Severity

Info

Description

Logs a message when the Telnet server is enabled on a VRF

Event ID: 12902

Message

TELNET server is disabled on VRF <vrf_name>.

Category

Telnet server

Severity

Info

Description

Logs a message when the Telnet server is disabled on a VRF

Event ID: 12903

Message

Failed to enable Telnet server on VRF <vrf_name>. Admin password is not set.

Category

Telnet server

Severity

Error

Description

Logs a message when a user tries to enable Telnet server without setting admin
password

Event ID: 12904

Message

User <user_name> logged in from <ip_address> through TELNET session.

Category

Telnet server

Severity

Info

Description

Logs a message when a user login is successful

Event ID: 12905

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

401

Message

User <user_name> login from <ip_address> for TELNET session has failed.

Category

Telnet server

Severity

Error

Description

Logs a message when a user login fails

Event ID: 12906

Message

User <user_name> logged out of TELNET session from <ip_address>.

Category

Telnet server

Severity

Info

Description

Logs a message when a user logs out of a session

Event ID: 12907

Message

TELNET session from <ip_address> is rejected because maximum number of TELNET
sessions is reached.

Category

Telnet server

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached.

Event ID: 12908

Message

TELNET session from User <user_name> is closed because maximum number of sessions
per user is reached.

Category

Telnet server

Severity

Warning

Description

Logs a message when a user session is closed when maximum number of sessions per
user are reached.

Event ID: 12908

Message

User {user_name} login from {ip_address} for TELNET session has failed since the user is
trying to login through an interface which is not allowed. Allowed interfaces are: {mgmt_
intf}

Category

Telnet server

Severity

Error

Description

Logs a message when a user login fails since the access through this management
interface is not allowed

Telnet server events | 402

Chapter 133

Temperature events

Temperature events

The following are the events related to temperature.

Event ID: 801

Message

Unrecognized sensor type <type>

Category

Temperature

Severity

Warning

Description

Log event when sensor type is unrecognized

Event ID: 802

Message

Module <module> shutdown initiated for sensor <name> with critical temperature, <temp>
degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is above the critical threshold

Event ID: 803

Message

Over-temperature for sensor <name>, <temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is above the over-temperature threshold

Event ID: 804

Message

Sensor <name> back to safe temperature, <temp> degC.

Category

Temperature

Severity

Information

Description

Log event when a sensor returns to safe operating conditions

Event ID: 805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

403

Message

System derate changed from <old> to <new>

Category

Temperature

Severity

Information

Description

Log when the system derate changes.

Event ID: 806

Message

Ambient temperature for sensor <name> above <temp> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is above the ambient temperature limits.

Event ID: 807

Message

Ambient temperature for sensor <name> back to safe temperature, between <t_low> and
<t_high> degC

Category

Temperature

Severity

Information

Description

Log when ambient temperature returns to safe operating conditions.

Event ID: 808

Message

Sensor <name> <limit_type> limit configuration <status>

Category

Temperature

Severity

Information

Description

Log failures in configuring sensor temperature warning/critical limits.

Event ID: 809

Message

Ambient temperature <temp> degC is above the commercial grade transceiver limit of
<limit_high> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is above commercial grade transceiver upper limit when
non-industrial transceivers are installed.

Event ID: 810

Temperature events | 404

Message

Ambient temperature <temp> degC is below the commercial grade transceiver range of
<limit_low> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is below commercial grade transceiver lower limit when
non-industrial transceivers are installed.

Event ID: 811

Message

Ambient temperature <temp> degC returned to within the commercial grade transceiver
range of <limit_low>-<limit_high> degC

Category

Temperature

Severity

Information

Description

Log when ambient temperature returns to commercial grade transceiver range when
non-industrial transceivers are installed.

Event ID: 812

Message

Ambient temperature for sensor <name> below <temp> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is below the ambient temperature limits.

Event ID: 813

Message

Under-temperature for sensor <name>, <temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is below the under-temperature threshold

Event ID: 814

Message

Module <module> shutdown initiated for sensor <name> with low critical temperature,
<temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is below the low critical threshold

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

405

Chapter 134

Time management events

Time management events

The following are the events related to time management.

Event ID: 6201

Message

System timezone changed from <oldtz> to <newtz>

Category

Time management

Severity

Information

Description

Change the system timezone

Event ID: 6202

Message

System date/time changed from <old_time> to <new_time>

Category

Time management

Severity

Information

Description

Change the system date/time

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

406

Chapter 135

TPM events

TPM events

The following are the events related to the TPM Daemon.

Event ID: 13601

Message

Category

Severity

TPM_Sign requested by {process_name} was successful

TPM Daemon

Info

Description

Indicates a TPM_Sign operation was successfully executed

Event ID: 13602

Message

Category

Severity

TPM_Sign requested by {process_name} failed with code {reason}

TPM Daemon

Error

Description

Indicates a TPM_Sign operation failed

Event ID: 13603

Message

Category

Severity

TPM selftest errors occurred on the current boot

TPM Daemon

Error

Description

Indicates a TPM selftest error occurred on the current boot

Event ID: 13604

Message

Category

Severity

Description

Rebooted {reboot_num} times to retry TPM selftests

TPM Daemon

Error

Indicates the system was rebooted some number of time to recovery from a TPM selftest
error

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

407

Chapter 136

Traffic Insight events

Traffic Insight events

The following are the events related to Traffic Insight.

Event ID: 14001

Message

Category

Severity

Instance {instance_name} created

Traffic Insight

Info

Description

Event indicates new traffic insight instance is created.

Event ID: 14002

Message

Category

Severity

Instance {instance_name} deleted

Traffic Insight

Info

Description

Event indicates traffic insight instance is deleted.

Event ID: 14003

Message

Top-N flows running-statistics cleared for the monitor {monitor_name} and instance
{instance_name}

Category

Traffic Insight

Severity

Info

Description

Flow running-statistics timeout expired.

Event ID: 14004

Message

Top-N flows aggregate-statistics cleared for the monitor {monitor_name} and instance
{instance_name}

Category

Traffic Insight

Severity

Info

Description

Flow aggregate-statistics timeout expired.

Event ID: 14005

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

408

Message

Category

Severity

Traffic Insight instance {instance_name} enabled

Traffic Insight

Info

Description

Event indicates traffic insight instance is enabled.

Event ID: 14006

Message

Category

Severity

Traffic Insight instance {instance_name} disabled

Traffic Insight

Info

Description

Event indicates traffic insight instance is disabled.

Event ID: 14007

Message

Ignoring the flow for monitor {monitor_name} instance {instance_name}, maximum
application flow cache limit reached

Category

Traffic Insight

Severity

Info

Description

Event indicates maximum application flow cache limit reached for a traffic insight
instance.

Event ID: 14008

Message

DNS Average Latency statistics cache cleared for the monitor {monitor_name} and
instance {instance_name}

Category

Traffic Insight

Severity

Info

Description

Event indicates DNS average latency statistics cache gets cleared after the timeout.

Event ID: 14009

Message

Category

Severity

Description

14009

Traffic Insight

Info

Event indicates maximum flow count reached for raw-flows flow monitor for a traffic
insight instance.

Traffic Insight events | 409

Chapter 137

Transceiver events

Transceiver events

The following are the events related to transceiver.

Event ID: 3801

Message

allow-unsupported-transceiver feature enabled

Category

Transceiver

Severity

Info

Description

Event raised when unsupported transceiver mode is enabled

Event ID: 3802

Message

allow-unsupported-transceiver feature disabled

Category

Transceiver

Severity

Info

Description

Event raised when unsupported transceiver mode is disabled

Event ID: 3803

Message

allow-unsupported-transceiver feature enabled: Unsupported transceivers found in: <list>

Category

Transceiver

Severity

Info

Description

Event raised to list unsupported transceivers in unsupported transceiver mode

Event ID: 3804

Message

Transceiver hot-swap insert for interface <interface>

Category

Transceiver

Severity

Info

Description

Event raised to indicate transceiver hotswap insertion

Event ID: 3805

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

410

Message

Transceiver hot-swap remove for interface <interface>

Category

Transceiver

Severity

Info

Description

Event raised to indicate transceiver hotswap removal

Event ID: 3806

Message

Interface <interface> transceiver attempted link recovery <count> times' throttle_count:
100

Category

Transceiver

Severity

Warning

Description

Event raised to indicate transceiver link recovery attempts

Event ID: 3807

Message

<path>

Category

Transceiver

Severity

Info

Description

Event raised to indicate detection path of unsupported transceivers

Event ID: 3808

Message

Transceiver <xcvr_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Info

Description

Event raised to indicate status of transceivers that are allowed to be operational and its
reason

Event ID: 3809

Message

Transceiver <xcvr_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate status of transceivers that are not allowed to be operational and
its reason

Event ID: 3810

Transceiver events | 411

Message

Unknown transceiver inserted in interface <interface>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate an unknown transceiver was inserted

Event ID: 3811

Message

Transceiver in <interface> is incompatible with the interface group speed

Category

Transceiver

Severity

Warning

Description

Event raised to indicate a transceiver was inserted in a port that is a member of a group
configured to operate at a different speed

Event ID: 3812

Message

Adapter <adapter_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Info

Description

Event raised to indicate status of adapters that are allowed to be operational and its
reason

Event ID: 3813

Message

Adapter <adapter_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate status of adapters that are not allowed to be operational and its
reason

Event ID: 3814

Message

Category

Severity

Interface {interface} transceiver disabled - {disabled_reason}

Transceiver

Warning

Description

Logged when the transceiver inserted in the interface is disabled

Event ID: 3815

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

412

Message

Category

Severity

Interface {interface} transceiver enabled

Transceiver

Info

Description

Logged when a previously disabled transceiver is enabled

Transceiver events | 413

Chapter 138

UDLD events

UDLD events

The following are the events related to UDLD.

Event ID: 4101

Message

Category

Severity

UDLD is enabled on interface: <intf>

UDLD

Info

Description

Event raised when UDLD is enabled

Event ID: 4102

Message

Category

Severity

UDLD is disabled on interface: <intf>

UDLD

Info

Description

Event raised when UDLD is disabled

Event ID: 4103

Message

Category

Severity

UDLD interface <intf> is unblocked

UDLD

Info

Description

Event raised when UDLD sets the interface as unblocked

Event ID: 4104

Message

Category

Severity

UDLD interface <intf> is blocked

UDLD

Error

Description

Event raised when UDLD sets the interface as blocked

Event ID: 4105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

414

Message

Category

Severity

Description

Event ID: 4106

UDLD interface <intf> is undetermined

UDLD

Error

Event raised when UDLD moves from bidirectional state to undetermined (RFC5171
mode only)

Message

UDLD interface <intf> interval <intvl_a> clamped to <intvl_b>

Category

UDLD

Severity

Warning

Description

Logs a warning when UDLD clamps the interval when operating in RFC5171 mode

Event ID: 4107

Message

Category

Severity

UDLD link is enabled on interface: <intf>

UDLD

Info

Description

Event raised when UDLD link is enabled

Event ID: 4108

Message

Category

Severity

UDLD link is disabled on interface: <intf>

UDLD

Info

Description

Event raised when UDLD link is disabled

Event ID: 4109

Message

Category

Severity

UDLD interface <intf> is error-disabled

UDLD

Error

Description

Event raised when UDLD substate of the interface as err_disabled

UDLD events | 415

Chapter 139
|               |           |        | UDP Broadcast | Forwarder | events |
| ------------- | --------- | ------ | ------------- | --------- | ------ |
| UDP Broadcast | Forwarder | events |               |           |        |
ThefollowingaretheeventsrelatedtoUDPBroadcastForwarder.
Event ID: 3601
Message
UDPBroadcastForwarderEnabled
| Category | UDPBroadcastForwarder |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description ThiscommandenablestheUDPBroadcastForwarderfeatureinthedevice.
Event ID: 3602
| Message  | UDPBroadcastForwarderDisabled |     |     |     |     |
| -------- | ----------------------------- | --- | --- | --- | --- |
| Category | UDPBroadcastForwarder         |     |     |     |     |
| Severity | Information                   |     |     |     |     |
Description ThiscommanddisablestheUDPBroadcastForwarderfeatureinthedevice.
416
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 140

UFD events

UFD events

The following are the events related to UFD.

Event ID: 12001

Message

Category

Severity

Uplink Failure Detection session-id <id>, state changed from <from_state> to <to_state>.

UFD

Critical

Description

Event reported when Links-to-Disable go down.

Event ID: 12002

Message

Uplink Failure Detection session-id <id>, state changed from <from_state> to <to_state>.

Category

UFD

Severity

Information

Description

Event reported when Links-to-Disable ports are restored.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

417

Chapter 141

User management events

User management events

The following are the events related to user management.

Event ID: 4701

Message

User <user> added <added_user> with role <user_role>

Category

User management

Severity

Info

Description

Logs a message when a new user is added to the switch

Event ID: 4702

Message

User <user> deleted <deleted_user> with role <user_role>

Category

User management

Severity

Info

Description

Logs a message when a user is deleted from the switch

Event ID: 4703

Message

User <username> successfully changed password

Category

User management

Severity

Info

Description

Logs a message when a user changes his/her password

Event ID: 4704

Message

User <username> password change failed

Category

User management

Severity

Error

Description

Logs a message when a user fails to change his/her password

Event ID: 4705

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

418

Message

User <username> set export password

Category

User management

Severity

Info

Description

Logs a message when a user sets export password

Event ID: 4706

Message

User <username> restored default export password

Category

User management

Severity

Info

Description

Logs a message when a user restores default export password

Event ID: 4707

Message

Category

Severity

Logs a message when a user is locked out

User management

Info

Description

User {username} locked out from session {session}

User management events | 419

Chapter 142

User-based tunnels events

User-based tunnels events

The following are the events related to user-based tunnels.

Event ID: 9701

Message

Tunnel Node Server SAC (<sac_ip>) is selected as (<state>)

Category

User-based tunnels

Severity

Info

Description

Event raised when controller is selected as Active/Standby

Event ID: 9702

Message

Tunnel Node Server Heartbeat has failed for SAC (<sac_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when heartbeat not received from a SAC

Event ID: 9703

Message

Tunnel Node Server keepalive has failed for UAC (<uac_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when keepalive not received from a UAC

Event ID: 9704

Message

Tunnel Node Server SAC bootstrapping has reinitialized to (<sac_ip>)

Category

User-based tunnels

Severity

Info

Description

Event raised when SAC bootstapping to a SAC is re-initialized

Event ID: 9705

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

420

Message

Tunnel Node Server PAPI key has mismatched

Category

User-based tunnels

Severity

Error

Description

Event raised when papi msg key sent and received is different ({key_id})

Event ID: 9706

Message

Tunnel Node Server UAC node is down (<uac_ip>)

Category

User-based tunnels

Severity

Critical

Description

Event raised when UAC node is down

Event ID: 9707

Message

Tunnel is Created - Gre Key (<gre_key>) VRF (<vrf>) Source IP (<src_ip>) Destination IP (<dst_
ip>)

Category

User-based tunnels

Severity

Info

Description

Event raised when user based tunnel is created

Event ID: 9708

Message

Tunnel Creation has Failed - Gre Key (<gre_key>) VRF (<vrf>) Source IP (<src_ip>)
Destination IP (<dst_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when user based tunnel creation fails

Event ID: 9709

Message

Tunnel is Deleted - Tunnel Id (<tunnel_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised when user based tunnel is deleted

Event ID: 9710

User-based tunnels events | 421

Message

Tunnel Deletion has Failed - Tunnel Id (<tunnel_id>)

Category

User-based tunnels

Severity

Error

Description

Event raised when user based tunnel deletion fails

Event ID: 9711

Message

Tunnel is UP - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP (<src_ip>) Destination
IP (<dst_ip>)

Category

User-based tunnels

Severity

Info

Description

Event raised when user based tunnel state is up

Event ID: 9712

Message

Tunnel is DOWN - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP (<src_ip>)
Destination IP (<dst_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when user based tunnel state is down

Event ID: 9713

Message

Client (<client_mac>) is bound to tunnel id (<tunnel_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised when user is gets binded to tunnel

Event ID: 9714

Message

Client (<client_mac>) binding to tunnel id (<tunnel_id>) has failed

Category

User-based tunnels

Severity

Error

Description

Event raised when user bind to tunnel id failed

Event ID: 9715

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

422

Message

Client (<client_mac>) is removed from tunnel.

Category

User-based tunnels

Severity

Info

Description

Event raised when user is gets binded to tunnel

Event ID: 9716

Message

Client (<client_mac>) unbinding to tunnel id (<tunnel_id>) has failed

Category

User-based tunnels

Severity

Error

Description

Event raised when user unbind to tunnel id failed

Event ID: 9717

Message

Client (<client_mac>) is getting modified to bind to tunnel id (<tunnel_id>)' throttle_count:
100

Category

User-based tunnels

Severity

Info

Description

Event raised when already binded user to a tunnel gets modified

Event ID: 9718

Message

Modification of Client (<client_mac>) binded to (<tunnel_id>) has failed' throttle_count: 100

Category

User-based tunnels

Severity

Error

Description

Event raised when modification of already binded user to a tunnel fails

Event ID: 9719

Message

NFD port (<nfd_id>) is created for client (<client_mac>) vlan id (<vlan_id>) port (<port>)
ecmp id (<ecmp_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised on NFD port creation

Event ID: 9720

User-based tunnels events | 423

Message

NFD port (<nfd_id>) creation for client (<client_mac>) vlan id (<vlan_id>) port (<port>) ecmp
id (<ecmp_id>) has failed

Category

User-based tunnels

Severity

Error

Description

Event raised on NFD port creation failure

Event ID: 9721

Message

NFD port (<nfd_id>) is deleted for ecmp id(<ecmp_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised on NFD port deletion

Event ID: 9722

Message

NFD port (<nfd_id>) deletion for ecmp id (<ecmp_id>) has failed

Category

User-based tunnels

Severity

Error

Description

Event raised when NFD port deletion fails

Event ID: 9723

Message

ECMP group is created for ecmp id (<ecmp_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised on ECMP group creation

Event ID: 9724

Message

ECMP group creation for ecmp id (<ecmp_id>) has failed

Category

User-based tunnels

Severity

Error

Description

Event raised on ECMP group creation failure

Event ID: 9725

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

424

Message

ECMP group is deleted for ecmp id (<ecmp_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised on ECMP group deletion

Event ID: 9726

Message

ECMP group deletion for ecmp id(<ecmp_id>) has failed

Category

User-based tunnels

Severity

Error

Description

Event raised when ECMP group deletion fails

Event ID: 9727

Message

MDestRx Tunnel is Created - Gre Key (<gre_key>) VLAN (<vlan>) VRF (<vrf>) Source IP (<src_
ip>) Destination IP (<dst_ip>)

Category

User-based tunnels

Severity

Info

Description

Event raised when mdest rx user based tunnel is created

Event ID: 9728

Message

MDestRx Tunnel Creation has Failed - Gre Key (<gre_key>) VLAN (<vlan>) VRF (<vrf>) Source
IP (<src_ip>) Destination IP (<dst_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when mdest rx user based tunnel creation fails

Event ID: 9729

Message

MDest Rx Tunnel is Deleted - Tunnel Id (<tunnel_id>)

Category

User-based tunnels

Severity

Info

Description

Event raised when mdest rx user based tunnel is deleted

Event ID: 9730

User-based tunnels events | 425

Message

MDest Rx Tunnel Deletion has Failed - Tunnel Id (<tunnel_id>)

Category

User-based tunnels

Severity

Error

Description

Event raised when mdest rx user based tunnel deletion fails

Event ID: 9731

Message

MDestRx Tunnel is UP - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP (<src_ip>)
Destination IP (<dst_ip>)

Category

User-based tunnels

Severity

Info

Description

Event raised when mdest rx user based tunnel state is up

Event ID: 9732

Message

MDestRx Tunnel is DOWN - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP (<src_ip>)
Destination IP (<dst_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when mdest rx user based tunnel state is down

Event ID: 9733

Message

User bootstrap is failed for client (<mac_addr>) on port (<port>) due to <reason>.

Category

User-based tunnels

Severity

Error

Description

Event raised when user bootstrap is failed

Event ID: 9734

Message

Operational state of <zone> zone is UP.

Category

User-based tunnels

Severity

Info

Description

Event raised when zone operational state is up

Event ID: 9735

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

426

Message

Operational state of <zone> zone is DOWN due to <reason>.

Category

User-based tunnels

Severity

Warning

Description

Event raised when zone operational state is down

Event ID: 9736

Message

Tunnel Node Server WoL VLAN bootstrap {state} with controller {sac_ip}

Category

User-based tunnels

Severity

Info

Description

Event raised when WoL VLAN bootstrap response received from controller
(Active/Standby)

Event ID: 9737

Message

Tunnel Node Server WoL VLAN bootstrap failed due to incompatible controller ({sac_ip})
version {version}

Category

User-based tunnels

Severity

Info

Description

Event raised when controller version does not support WoL VLAN bootstrap

User-based tunnels events | 427

Chapter 143
|                   |           | Virtual      | Switching | Extension | (VSX) events |
| ----------------- | --------- | ------------ | --------- | --------- | ------------ |
| Virtual Switching | Extension | (VSX) events |           |           |              |
ThefollowingaretheeventsrelatedtoVSX.
Event ID: 7001
Message
VSXISLport<port>isdown
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Info                           |     |     |     |     |
| Description | VSXISLlinkisdown.              |     |     |     |     |
Event ID: 7002
| Message     | VSXISLport<port>isup           |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |     |
| Severity    | Info                           |     |     |     |     |
| Description | VSXISLlinkisup.                |     |     |     |     |
Event ID: 7003
| Message     | VSXISLport<port>isIn-Syncwiththepeer. |     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX)        |     |     |     |     |
| Severity    | Info                                  |     |     |     |     |
| Description | VSXISLisInSyncwiththepeer.            |     |     |     |     |
Event ID: 7004
Message
VSXISLport<port>isOut-Of-Syncwiththepeer:<reason>
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Error                          |     |     |     |     |
| Description | VSXISLisOut-Of-Syncwiththepeer |     |     |     |     |
Event ID: 7005
428
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

VSX Keepalive failed

Category

Virtual Switching Extension (VSX)

Severity

Warning

Description

VSX Keepalive is not able to reach the peer device

Event ID: 7006

Message

VSX Keepalive succeeded

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX Keepalive is able to reach the peer device

Event ID: 7007

Message

VSX role is primary

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Operational role of this device derived based on device priority of the 2 devices.

Event ID: 7008

Message

VSX role is secondary

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Operational role of this device derived based on device priority of the 2 devices.

Event ID: 7009

Message

VSX Software version mismatch: peer version <peer_sw_ver>, local version <local_sw_ver>

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX Software version mismatch: peer sw version is not same as local sw version.

Event ID: 7010

Message

VSX Device mismatch: peer device <peer_device_type>, local device <local_device_type>

Virtual Switching Extension (VSX) events | 429

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX Device type mismatch: peer device type is not same as local device type.

Event ID: 7011

Message

VSX <vsx_id> state local up, remote down

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX local up remote down.

Event ID: 7012

Message

VSX <vsx_id> state local down, remote up

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX local down remote up.

Event ID: 7013

Message

VSX <vsx_id> state local up, remote up

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX local up remote up.

Event ID: 7014

Message

VSX <vsx_id> state local down, remote down

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX local down remote down.

Event ID: 7015

Message

VSX ISL sliding window parameters are reset.

Category

Virtual Switching Extension (VSX)

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

430

Severity

Info

Description

VSX resetting the ISL protocol sliding window.

Event ID: 7016

Message

VSX own ISL hello packet received, ignoring the packet.

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX switch receives own ISL hello packet from network.

Event ID: 7017

Message

Rebooting the VSX <vsx_role> device with newly updated <bank_name> image.

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Switch reboot due to VSX software update.

Event ID: 7018

Message

VSX primary ISL version <primary_version> dose not match with VSX secondary ISL version
<secondary_version>. Performing a non-hitless image update.

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX inter-switch-link protocol version mismatch after secondary reboot.

Event ID: 7019

Message

VSX <vsx_role> image update failed due to <reason>.

Category

Virtual Switching Extension (VSX)

Severity

Error

Description

VSX image update failed.

Event ID: 7020

Message

ISL out-of-sync and keepalive is in established

Category

Virtual Switching Extension (VSX)

Virtual Switching Extension (VSX) events | 431

Severity

Info

Description

ISL out-of-sync and keepalive is in established, handled split brain

Event ID: 7021

Message

ISL out-of-sync and keepalive also failed

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

ISL out-of-sync and keepalive also failed

Event ID: 7022

Message

Linkup delay timer started

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Linkup delay timer started

Event ID: 7023

Message

Linkup delay timer expired

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Linkup delay timer expired

Event ID: 7024

Message

VSX <vsx_role> state changed from <prev_state> to <state>.

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX software update state change.

Event ID: 7025

Message

Bailout timer started

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Bailout timer started

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

432

Event ID: 7026

Message

Bailout timer expired

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Bailout timer expired

Event ID: 7027

Message

Bailout timer stopped

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Bailout timer stopped

Event ID: 7028

Message

Linkup-delay timer stopped

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

Linkup-delay timer stopped

Event ID: 7029

Message

VSX device roles are inconsistent: local VSX device role <local_vsx_role>, peer VSX device
role <peer_vsx_role>

Category

Virtual Switching Extension (VSX)

Severity

Error

Description

VSX device roles are said to be consistent only if one VSX device is configured as primary
and other VSX device is configured as secondary

Event ID: 7029

Message

VSX <vsx_role> state changed to <state>-<sub_state>.

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX software update sub-state change.

Event ID: 7030

Virtual Switching Extension (VSX) events | 433

Message

VSX Keepalive is configured without creating VRF

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VRF needs to be created before configuring VSX Keepalive

Event ID: 7031

Message

VSX Keepalive is configured without configuring IP address

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

IP address needs to be configured before configuring VSX Keepalive

Event ID: 7032

Message

Active-gateway is enabled on <port>. Cannot program Active-forwarding

Category

Virtual Switching Extension (VSX)

Severity

Error

Description

Failed to program active-forwarding.

Event ID: 7033

Message

Active-forwarding is enabled on <port>. Cannot program Active-gateway

Category

Virtual Switching Extension (VSX)

Severity

Error

Description

Failed to program active-gateway.

Event ID: 7034

Message

Netdev <ifname> configured with ipv4 address <value>

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

programmed active-gateway IP4 address successfully.

Event ID: 7035

Message

Netdev <ifname> configured with ipv6 address <value>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

434

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

programmed active-gateway IP6 address successfully.

Event ID: 7036

Message

Category

Severity

VSX {vsx_role} state changed to {state}-{sub_state}.

Virtual Switching Extension (VSX)

Info

Description

VSX software update sub-state change.

Event ID: 7037

Message

VSX secondary has better MCLAG state compared to VSX primary. MCLAGs and SVIs are
brought down on VSX primary.

Category

Virtual Switching Extension (VSX)

Severity

Info

Description

VSX split state is inversed.

Event ID: 7038

Message

Category

Severity

Description

Event ID: 7039

Message

Category

Severity

Active-gateway extended-mac automatically disabled because mac-lockout was enabled

Virtual Switching Extension (VSX)

Warning

Event raised when active-gateway extended-mac feature is disabled due to mac-lockout
feature being enabled

Active-gateway extended-mac is automatically enabled

Virtual Switching Extension (VSX)

Info

Description

Event raised when active-gateway extended-mac feature is enabled

Virtual Switching Extension (VSX) events | 435

Chapter 144
|                   |           | Virtual | Switching | Framework | (VSF) events |
| ----------------- | --------- | ------- | --------- | --------- | ------------ |
| Virtual Switching | Framework | (VSF)   | events    |           |              |
ThefollowingaretheeventsrelatedtoVSF.
Event ID: 9901
Message
Member<member_id>bootcomplete
| Category    | VirtualSwitchingFramework(VSF) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Info                           |     |     |     |     |
| Description | logeventformemberbootcomplete  |     |     |     |     |
Event ID: 9902
| Message     | Standby<member_id>bootcomplete |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |     |     |     |     |
| Severity    | Info                           |     |     |     |     |
| Description | logeventforstandbybootcomplete |     |     |     |     |
Event ID: 9903
| Message     | Conductor<member_id>bootcomplete |     |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)   |     |     |     |     |
| Severity    | Info                             |     |     |     |     |
| Description | logeventforConductorbootcomplete |     |     |     |     |
Event ID: 9905
Message
Resettingmember<member_id>
| Category    | VirtualSwitchingFramework(VSF)        |     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- |
| Severity    | Info                                  |     |     |     |     |
| Description | Eventlogindicatesthatmemberisreseting |     |     |     |     |
Event ID: 9906
436
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Member <member_id> conflict detected on link <link>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Event log for Failed processing Hello packet because of member number conflict

Event ID: 9907

Message

Incompatible version detected

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Event log for indicates that we got a packet with a diff proto ver

Event ID: 9908

Message

Topology is <topo_type>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

Event log indicates the current topology

Event ID: 9910

Message

Member <member_id> removed

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

Event log indicates the member has been removed due to user request

Event ID: 9911

Message

Maximum number of switches in the stack has reached. Cannot add MAC <mac_address>
product type <type>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Event log indicates that we would exceed the MAX switches if we add this new switch

Event ID: 9912

Virtual Switching Framework (VSF) events | 437

Message

Stack state is no-split with conductor id <member_id>' throttle_count: 100

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for stack state active

Event ID: 9913

Message

Lost member <member_id> with <reason>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Event log for lost member

Event ID: 9914

Message

Reboot of MAC <mac_address> status-<status>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

Event log for status of a reboot request

Event ID: 9915

Message

Member <member_id> elected as conductor reason-<reason>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for the switch won as conductor

Event ID: 9916

Message

Member <member_id> elected as standby reason-<reason>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for the switch won as standby

Event ID: 9917

Message

Switch with MAC <mac_address> cannot join stack due to incorrect product id <product_
id>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

438

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event for the member was not allowed to join due to a mismatched product-id

Event ID: 9919

Message

Found Unsupported switch with MAC <mac_address> and Product type <product_type>,
connected to switch with MAC <mac_addr> on stack port <port_id>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event for switch running on a different platform and trying to join the stack

Event ID: 9920

Message

Heart beat lost for member <member_id>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event for heart beat lost

Event ID: 9921

Message

OS version mismatch detected for member <member_id>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when os_version_mismatch happened on standby and member

Event ID: 9922

Message

Attempt to connect member <member_id> from a different stack

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when member attempt to connect to a different stack

Event ID: 9923

Message

VSF link <link> is up

Virtual Switching Framework (VSF) events | 439

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when vsf link is up

Event ID: 9924

Message

VSF link <link> is down

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when vsf link is down

Event ID: 9925

Message

Invalid MAC <mac_address> detected on link <link> with peer MAC <mac_add>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when different MAC address on the same link

Event ID: 9926

Message

2 member loop detected on ring topology

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when there is a 2 member loop in topology

Event ID: 9927

Message

Fragment with conductor <member_id> is Active' throttle_count: 100

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for active fragment

Event ID: 9928

Message

Fragment with conductor <member_id> is Inactive

Category

Virtual Switching Framework (VSF)

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

440

Severity

Info

Description

log event for Inactive fragment

Event ID: 9929

Message

Active fragment detection timeout

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for active stack detection timeout

Event ID: 9930

Message

Member <member_id> is configured as Secondary

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for standby configuration

Event ID: 9931

Message

Secondary configuration removed

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event for standby unconfiguration

Event ID: 9932

Message

Attempt to connect a member with MAC <mac_address> and product type <product_id>
having different airflows

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when Mater SKU device joins the stack

Event ID: 9933

Message

Peer timeout on interface <port_id>

Category

Virtual Switching Framework (VSF)

Virtual Switching Framework (VSF) events | 441

Severity

Warning

Description

log event for peer time out as it did not receive any packet

Event ID: 9934

Message

Loop detected on interface <port_id>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event for loop detection in link

Event ID: 9935

Message

Interface <port_id> detected a peer with a different VSF handshake version

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when peer switch is in different VSF handshake version

Event ID: 9936

Message

Interface <port_id> added to VSF link <link>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when interface added to a particular link

Event ID: 9937

Message

Interface <port_id> removed from VSF link <link>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when interface removed from a particular link

Event ID: 9938

Message

Switch with mac <mac_address> not able to autojoin as it is connected on interface <port>
which is a non default autojoin VSF interface

Category

Virtual Switching Framework (VSF)

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

442

Severity

Warning

Description

log event when the switch is not able to autojoin as it is connected with a non default VSF
interface

Event ID: 9939

Message

Switch with MAC <mac_address> not able to autojoin as it is connected to interface <port>
which is not provisioned on the conductor for member <member_id>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when there is an inconsistency detected between conductors provisioned VSF
link configuration and the interface on which switch is attempting to autojoin

Event ID: 9940

Message

Switch with MAC <mac_address> is not autojoin eligible

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when peer switch is not autojoin eligible

Event ID: 9941

Message

Switch with MAC <mac_address> attempting to autojoin via multiple interfaces

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when there is more than one interface physically connected to same switch VSF
link for autojoin

Event ID: 9942

Message

Switch with MAC <mac_address> failed to autojoin as there is no free member number
available

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log even when switch is not allowed to autojoin because of insufficient resources

Event ID: 9943

Message

Switch with mac <mac_address> failed to autojoin on link <link>, port <port>

Virtual Switching Framework (VSF) events | 443

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when two different switches are attempting to autojoin by connecting to the
same VSF link on the peer

Event ID: 9944

Message

Switch has VSF configurations present. Force autojoin will not take into effect. Remove all
VSF configurations followed by unconfiguring and reconfiguring force autojoin for it to
take into effect

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when VSF force autojoin fails as VSF configurations exists

Event ID: 9945

Message

VSF force autojoin enabled

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when VSF force autojoin is enabled

Event ID: 9946

Message

VSF force autojoin disabled

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when VSF force autojoin is disabled

Event ID: 9947

Message

Switch with MAC <mac_addr1> failed to autojoin. Connect the device <mac_addr2> to
member <mbr_id> link <link_id> to proceed

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when member connected to an unsupported interface

Event ID: 9948

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

444

Message

Interface <port_id> in VSF link <link> detected a peer with inconsistent VSF link
configuration

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when interface is in inconsistent link configuration error

Event ID: 9949

Message

Secondary member changed from <old_standby_id> to <new_standby_id>

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

log event when existing secondary changes to new specified secondary member

Event ID: 9950

Message

Switch with MAC {mac_addr} failed to autojoin as it is connected on interface {port_id}
which has MACsec configuration

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when a VSF interface is connected to another interface with MACsec
configuration

Event ID: 9951

Message

Bringing down MACsec configured interface {port_id} as it is added to a VSF link. VSF link
and MACsec configurations needs to be removed from the interface {port_id} and VSF
link needs to be reconfigured for it to take into effect

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when an interface with MACsec configuration is added to VSF link

Event ID: 9952

Message

Category

Severity

Switchover detected during ISSU operation: "{operation}"

Virtual Switching Framework (VSF)

Warning

Description

Log event when ISSU switchover is detected

Event ID: 9953

Virtual Switching Framework (VSF) events | 445

Message

Category

Severity

ISSU state failed for member {id} during ISSU operation: "{operation}"

Virtual Switching Framework (VSF)

Warning

Description

Log to indicate VSF_Member issu_state failed in conductor

Event ID: 9954

Message

VSF member {id} going out of stack during ISSU operation: "{operation}", rebooting the
stack

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log to indicate when standby/member goes out of the stack

Event ID: 9955

Message

Category

Severity

Unintentional failover detected during ISSU operation: "{operation}", rebooting the stack

Virtual Switching Framework (VSF)

Warning

Description

Log event when unintentional failover occurs during issu in_progress

Event ID: 9956

Message

Category

Severity

ISSU complete timer expired. Rebooting switch {id} during ISSU operation: "{operation}"

Virtual Switching Framework (VSF)

Warning

Description

Log event when ISSU timer expires before ISSU is complete

Event ID: 9957

Message

Member {member_id} interface {port_id} in VSF link {link} detected a peer {mac_address}
with incompatible product type {prod_type}

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when member attempt to connect to incompatible peer jtypes

Event ID: 9958

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

446

Message

Category

Severity

Egress port shape rate {lowest_speed} will be applied for all VSF interfaces

Virtual Switching Framework (VSF)

Warning

Description

Log event when port shape is updated with uniform speed

Event ID: 9959

Message

Category

Severity

Egress port shape rate {lowest_speed} applied for all VSF interfaces

Virtual Switching Framework (VSF)

Warning

Description

Log event when port shape is updated with uniform speed

Event ID: 9960

Message

Category

Severity

Egress port shape rate {lowest_speed} update is failed to apply for interface {if_name}

Virtual Switching Framework (VSF)

Warning

Description

Log event to capture the QOS applied failures.

Event ID: 9961

Message

Category

Severity

Egress shaping is disabled in the stack.

Virtual Switching Framework (VSF)

Info

Description

Log event to capture the vsf egress_shape unconfiguration

Event ID: 9962

Message

Egress shaping is enabled in the stack. When VSF interfaces are of different speeds, all
VSF interfaces in the stack will operate at a chosen common denominator speed when
there is atleast one active stack member of type S0E91A or S0X44A in the stack.

Category

Virtual Switching Framework (VSF)

Severity

Info

Description

Log event to capture the vsf egress_shape configuration.

Virtual Switching Framework (VSF) events | 447

Chapter 145

VLAN events

VLAN events

The following are the events related to VLAN.

Event ID: 2101

Message

Category

Severity

VLAN <vid> created in hardware

VLAN

Info

Description

This log event informs the user that VLAN is created in Hardware

Event ID: 2102

Message

Category

Severity

Failed to create VLAN <vid> in Hardware

VLAN

Error

Description

This log event informs the user that VLAN is not created in Hardware

Event ID: 2103

Message

Category

Severity

VLAN <vid> removed from hardware

VLAN

Info

Description

This log event informs the user that VLAN is removed from Hardware

Event ID: 2104

Message

Category

Severity

Failed to remove VLAN <vid> from hardware

VLAN

Error

Description

This log event informs the user that VLAN is not removed from Hardware

Event ID: 2105

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

448

Message

Category

Severity

Internal VLAN <vid> is allocated to port <port>

VLAN

Info

Description

This log event informs that internal VLAN is allocated to port

Event ID: 2106

Message

Category

Severity

Failed to allocate internal VLAN to port <port>

VLAN

Error

Description

This log event informs that internal VLAN is not allocated

Event ID: 2107

Message

Category

Severity

Description

Event ID: 2108

Message

Category

Severity

The mode for port <port> changed from <from> to <to> on VLAN <vid>

VLAN

Info

This log event informs that the port mode has changed from one of the trunk types to
access or vice versa

Created Mac based VLAN entry. VLAN <vid> is mapped to client <mac> on port <port>

VLAN

Info

Description

This log event informs the user that Mac based VLAN is created in Hardware

Event ID: 2109

Message

Category

Severity

Failed to create Mac based VLAN entry for <mac> with VLAN <vid> on port <port>

VLAN

Error

Description

This log event informs the user that Mac based VLAN is not created in Hardware

Event ID: 2110

VLAN events | 449

Message

Category

Severity

Deleted Mac based VLAN entry for <mac> with VLAN <vid> on port <port>

VLAN

Info

Description

This log event informs the user that MAC based VLAN is removed from Hardware

Event ID: 2111

Message

Category

Severity

Failed to remove Mac based VLAN entry for <mac> with VLAN <vid> on port <port>

VLAN

Error

Description

This log event informs the user that MAC based VLAN is not removed from Hardware

Event ID: 2112

Message

Category

Severity

Updated MAC based VLAN entry. VLAN <vid> is mapped to client <mac> on port <port>

VLAN

Info

Description

This log event informs the user that MAC based VLAN is updated in Hardware

Event ID: 2113

Message

Category

Severity

Failed to update Mac based VLAN entry for <mac> with VLAN <vid> on port <port>

VLAN

Error

Description

This log event informs the user that MAC based VLAN is not updated in Hardware

Event ID: 2114

Message

Category

Severity

Internal VLAN changed to <vlan>

VLAN

Info

Description

This log event informs that internal VLAN range is changed

Event ID: 2115

Message

VLAN <vid> is down due to pvlan misconfig reason <reason>

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

450

Category

Severity

VLAN

Info

Description

This log event informs the user that VLAN is down due to pvlan misconfig

Event ID: 2116

Message

Category

Severity

VLAN <vid> is recovered from pvlan misconfig

VLAN

Info

Description

This log event informs the user that VLAN is recovered from pvlan misconfig

Event ID: 2117

Message

Category

Severity

Remote node <remote_node> add for VLAN <vid> on node <local_node> failed

VLAN

Error

Description

This log event informs the user that remote node add for a vlan failed

Event ID: 2118

Message

Category

Severity

Remote node <remote_node> remove for VLAN <vid> on node <local_node> failed

VLAN

Error

Description

This log event informs the user that remote node remove for a vlan failed

Event ID: 2119

Message

VLAN translation rule addition failed for port:<port_name>, in_vlan:<orig_vlan>, out_
vlan:<trans_vlan>, reason=<rst>

Category

VLAN

Severity

LOG_INFO

Description

Logs a message when vlan translation rule addition failed in hardware

Event ID: 2120

Message

Category

{intf_name} is now an SVLAN customer-network interface.

VLAN

VLAN events | 451

Severity

LOG_INFO

Description

{intf_name} is now an SVLAN customer-network interface.

Event ID: 2121

Message

Category

Severity

'{intf_name} is now an SVLAN provider-network interface.'

VLAN

LOG_INFO

Description

Logs a message when port is part for QinQ provider-network

Event ID: 2122

Message

Category

Severity

'{intf_name} is no longer an SVLAN interface.'

VLAN

LOG_INFO

Description

'Logs a message when port is no longer part for QinQ' event_description_template:

Event ID: 2123

Message

Category

Severity

'Secondary VLAN {sec_vid} of type {sec_type} is associated to primary VLAN {prim_vid}'

VLAN

LOG_INFO

Description

'This log event informs the user that secondary VLAN is associated to a primary VLAN'

Event ID: 2124

Message

'Secondary VLAN {sec_vid} admin state {sec_admin} is ignored. Primary VLAN {prim_vid}
admin state ({prim_admin}) will be applied'

Category

VLAN

Severity

LOG_INFO

Description

'This log event informs the user that secondary VLAN admin state is ignored'

Event ID: 2125

Message

Category

'UUFB {port} enabled in hardware'

VLAN

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

452

Severity

LOG_INFO

Description

'This log event informs the user that UUFB has been enabled on a physical port'

Event ID: 2126

Message

Category

Severity

'UUFB {port} disabled in hardware'

VLAN

LOG_INFO

Description

'This log event informs the user that UUFB has been disabled on a physical port'

VLAN events | 453

Chapter 146

VLAN Interface events

VLAN Interface events

The following are the events related to VLAN interface.

Event ID: 1601

Message

Vlaninterface vlan<vlan>, failed to create an l3 interface, error: <err>

Category

VLAN Interface

Severity

Error

Description

logs errors while creating vlaninterface.

Event ID: 1602

Message

Vlan Interface <interface>, created

Category

VLAN Interface

Severity

Information

Description

logs to create vlan interface.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

454

Chapter 147

VRF events

VRF events

The following are the events related to VRF.

Event ID: 6401

Message

VRF with vrf name <vrf_name> is configured in the switch

Category

VRF

Severity

Information

Description

Logs a message when VRF is configured in the switch

Event ID: 6402

Message

Category

Severity

Failed to configure VRF with vrf name <vrf_name> in the switch

VRF

Error

Description

Logs a message when VRF configuration failed in the switch

Event ID: 6403

Message

VRF with vrf name <vrf_name> is deleted from the switch

Category

VRF

Severity

Information

Description

Logs a message when VRF is deleted from the switch

Event ID: 6404

Message

Category

Severity

Failed to delete VRF with vrf name <vrf_name> from the switch

VRF

Error

Description

Logs a message when VRF deletion failed in the switch

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

455

Chapter 148

VRF Manager events

VRF Manager events

The following are the events related to VRF Manager.

Event ID: 5401

Message

Created a vrf entity <vrf_entity>

Category

VRF Manager

Severity

Information

Event ID: 5402

Message

Deleted a vrf entity <vrf_entity>

Category

VRF Manager

Severity

Information

Event ID: 5403

Message

vrf entity creation failed <vrf_entity>

Category

VRF Manager

Severity

Error

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

456

Chapter 149

VRRP events

VRRP events

The following are the events related to VRRP.

Event ID: 3701

Message

Category

Severity

VRRP has been enabled on this router

VRRP

Info

Description

Logs VRRP global enable event

Event ID: 3702

Message

Category

Severity

VRRP has been disabled on this router

VRRP

Info

Description

Logs VRRP global disable event

Event ID: 3703

Message

Category

Severity

<inet_type> virtual router <vrid> on interface <interface> has taken owner IP

VRRP

Info

Description

Logs virtual router has taken control of owner IP

Event ID: 3704

Message

Category

Severity

<inet_type> virtual router <vrid> on interface <interface> has taken standby IP

VRRP

Info

Description

Logs virtual router has taken control of standby IP

Event ID: 3705

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

457

Message

Category

Severity

<inet_type> virtual router <vrid> on interface <interface> lost standby IP

VRRP

Info

Description

Logs virtual router has lost control of standby IP

Event ID: 3706

Message

Category

Severity

<inet_type> virtual router <vrid> created on interface <interface>

VRRP

Info

Description

Logs creation of virtual router on interface

Event ID: 3707

Message

Category

Severity

<inet_type> virtual router <vrid> deleted from interface <interface>

VRRP

Info

Description

Logs deletion of virtual router from interface

Event ID: 3708

Message

Category

Severity

<type> address <address> is added to virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs addition of IP address to virtual router

Event ID: 3709

Message

Category

Severity

<type> address <address> is deleted from virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs deletion of IP address from virtual router

Event ID: 3710

Message

<inet_type> virtual router <vrid> version changed to <value> on interface <interface>

VRRP events | 458

Category

Severity

VRRP

Info

Description

Logs version change for virtual router

Event ID: 3711

Message

Category

Severity

<inet_type> virtual router <vrid> advertisement interval has changed to <value>
milliseconds on interface <interface>

VRRP

Info

Description

Logs advertisement timer has changed for virtual router

Event ID: 3712

Message

Category

Severity

<inet_type> virtual router <vrid> preempt delay time has changed to <value> seconds on
interface <interface>

VRRP

Info

Description

Logs preempt delay timer has changed for virtual router

Event ID: 3713

Message

Category

Severity

<inet_type> virtual router <vrid> state change from <old_state> to <new_state> on interface
<interface>

VRRP

Info

Description

Logs state has changed for virtual router on interface

Event ID: 3714

Message

Category

Severity

Enabled preempt option for <inet_type> virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs preempt option has been enabled for virtual router

Event ID: 3715

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

459

Message

Category

Severity

Enabled virtual IP ping for <inet_type> virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs virtual IP ping has been enabled for virtual router

Event ID: 3716

Message

Category

Severity

Enabled <inet_type> virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs virtual router has been enabled on interface

Event ID: 3717

Message

Category

Severity

Disabled preempt option for <inet_type> virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs preempt option has been disabled for virtual router

Event ID: 3718

Message

Category

Severity

Disabled virtual IP ping for <inet_type> virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs virtual IP ping has been disabled for virtual router

Event ID: 3719

Message

Category

Severity

Disabled <inet_type> virtual router <vrid> on interface <interface>

VRRP

Info

Description

Logs virtual router has been disabled on interface

Event ID: 3720

Message

<inet_type> virtual router <vrid> priority changed to <value> on interface <interface>

VRRP events | 460

Category

Severity

VRRP

Info

Description

Logs priority has been changed for virtual router

Event ID: 3721

Message

Category

Severity

<inet_type> virtual router <vrid> mode changed to <value> on interface <interface>

VRRP

Info

Description

Logs virtual router mode has been changed

Event ID: 3722

Message

Category

Severity

Track object <track> is associated with <inet_type> virtual router <vrid>

VRRP

Info

Description

Logs track object has been associated with virtual router

Event ID: 3723

Message

Category

Severity

Track object <track> is de-associated from <inet_type> virtual router <vrid>

VRRP

Info

Description

Logs track object has been de-associated from virtual router

Event ID: 3724

Message

Category

Severity

Track object <track> is created

VRRP

Info

Description

Logs track object has been created

Event ID: 3725

Message

Track object <track> is deleted

Category

VRRP

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

461

Severity

Info

Description

Logs track object has been deleted

Event ID: 3726

Message

Category

Severity

Track object <track> state changed <old_state> to <new_state>

VRRP

Info

Description

Logs track object state change

Event ID: 3727

Message

Category

Severity

Track object <track> associated with interface <interface>

VRRP

Info

Description

Logs track object association with interface

Event ID: 3728

Message

Category

Severity

<inet_type> virtual router <vrid> recieved packet with authentication type mismatch on
interface <interface>

VRRP

Info

Description

Logs authentication failures on virtual router

Event ID: 3729

Message

Category

Severity

<inet_type> virtual router <vrid> recieved packet with authentication key mismatch on
interface <interface>

VRRP

Info

Description

Logs authentication failures on virtual router

Event ID: 3730

Message

Category

Enabled vrrpv3 checksum for {inet_type} virtual router {vrid} on interface {interface}

VRRP

VRRP events | 462

Severity

Info

Description

Logs vrrpv3 checksum has been enabled for virtual router

Event ID: 3731

Message

Category

Severity

Disabled vrrpv3 checksum for {inet_type} virtual router {vrid} on interface {interface}

VRRP

Info

Description

Logs vrrpv3 checksum has been disabled for virtual router

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

463

Chapter 150

VSX Sync events

VSX Sync events

The following are the events related to VSX sync.

Event ID: 7601

Message

Configuration sync error: <id>

Category

VSX Sync

Severity

Error

Description

Logs event when error in synchronizing config between two VSX peers

Event ID: 7602

Message

Configuration sync update: <id>

Category

VSX Sync

Severity

Information

Description

Logs event when there is an update for config sync

Event ID: 7603

Message

Configuration-persistence: <id>

Category

VSX Sync

Severity

Information

Description

Logs event when config is copied to startup-config on any of the VSX peer

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

464

Chapter 151

VXLAN agent events

VXLAN agent events

The following are the events related to VXLAN agent.

Event ID: 12501

Message

Netvp add failed for vni_id: <vni_id>, tunnel_id: <tunnel_id>, vlan: <vlan>.

Category

VXLAN agent

Severity

Error

Description

Event raised when netvp add fails in agent

Event ID: 12502

Message

Tunnel add failed for tunnel_id: <tunnel_id>, ecmp_id: <ecmp_id>.

Category

VXLAN agent

Severity

Error

Description

Event raised when tunnel add fails in agent

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

465

Chapter 152

VXLAN events

VXLAN events

The following are the events related to VXLAN.

Event ID: 8101

Message

Category

Severity

VNI id <vni_id> creation failed

VXLAN

Error

Description

Event raised when VNI creation fails

Event ID: 8102

Message

Category

Severity

VNI id <vni_id> created

VXLAN

Info

Description

Event raised when VNI created

Event ID: 8103

Message

Category

Severity

VNI id <vni_id> deletion fails

VXLAN

Error

Description

Event raised when VNI deletion fails

Event ID: 8104

Message

Category

Severity

VNI id <vni_id> has been deleted

VXLAN

Info

Description

Event raised when VNI is deleted

Event ID: 8105

Message

Vtep-Peer <vtep_peer> is created

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

466

Category

Severity

VXLAN

Info

Description

Event raised when Vtep-Peer is created

Event ID: 8106

Message

Category

Severity

Vtep-Peer <vtep_peer> has been deleted

VXLAN

Info

Description

Event raised when Vtep-Peer has been deleted

Event ID: 8107

Message

Category

Severity

Vtep-Peer <vtep_peer> deletion failed

VXLAN

Error

Description

Event raised when Vtep-Peer deletion fails

Event ID: 8108

Message

Category

Severity

Access-Port with vlan <vlan_id> and port <port_name> has been created

VXLAN

Info

Description

Event raised when Access-Port has been created

Event ID: 8109

Message

Category

Severity

Access-Port with port <port_name> and vlan <vlan_id> has been deleted

VXLAN

Info

Description

Event raised when Access-Port has been deleted

Event ID: 8110

Message

Category

Vtep-Peer <vtep> state is operational

VXLAN

VXLAN events | 467

Severity

Info

Description

Event raised when Vtep-Peer status is changed to operational

Event ID: 8111

Message

Category

Severity

Vtep-Peer <vtep> state is configuration_error

VXLAN

Info

Description

Event raised when Vtep-Peer status is changed to configuration error

Event ID: 8112

Message

Category

Severity

Vtep-Peer <vtep> state is no_hw_resources

VXLAN

Info

Description

Event raised when Vtep-Peer status is changed to no hardware resources

Event ID: 8113

Message

Category

Severity

Vtep-Peer <vtep> state is activating

VXLAN

Info

Description

Event raised when Vtep-Peer status is changed to activating

Event ID: 8114

Message

Category

Severity

Tunnel <remote_ip> added to hardware

VXLAN

Info

Description

Event raised when a VxLAN tunnel is added to hardware

Event ID: 8115

Message

Category

Severity

Tunnel <remote_ip> deleted from hardware

VXLAN

Info

Description

Event raised when a VxLAN tunnel is deleted from hardware

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

468

Event ID: 8116

Message

Category

Severity

Tunnel <remote_ip> delete deferred

VXLAN

Info

Description

Event raised when a VxLAN tunnel has its deletion deferred by L3PD

Event ID: 8117

Message

Category

Severity

Tunnel <remote_ip> deferred delete canceled

VXLAN

Info

Description

Event raised when a VxLAN tunnel has its deferred deletion canceled

Event ID: 8118

Message

Category

Severity

Event raised when vxlan interface admin state is changed.

VXLAN

Info

Description

Event raised when vxlan interface admin state is changed.

Event ID: 8119

Message

Category

Severity

Nexthop {action} received for tunnel {vtep_peer}

VXLAN

Info

Description

Event raised when nexthop operation add/delete/modify is triggered on a vtep-peer

Event ID: 8120

Message

Category

Severity

Tunnel {vtep_peer} forwarding_state is {state}

VXLAN

Info

Description

Event raised when Vtep-Peer forwarding_state is changed

Event ID: 8121

VXLAN events | 469

Message

Category

Severity

Unsupported underlay port {port} configured for tunnel {vtep_peer}

VXLAN

Error

Description

Event raised when unsupported underlay port configured as tunnel nexthop

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

470

Chapter 153
|            |              |        | Zero touch | provisioning | events |
| ---------- | ------------ | ------ | ---------- | ------------ | ------ |
| Zero touch | provisioning | events |            |              |        |
Thefollowingaretheeventsrelatedtozerotouchprovisioning.
| Event ID: | 8701 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message
ZTPservicehasstarted
| Category    | Zerotouchprovisioning                    |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Info                                     |     |     |     |     |
| Description | LogeventwhenZTPservicestarts             |     |     |     |     |
| Event ID:   | 8702                                     |     |     |     |     |
| Message     | ZTPservicehasstopped                     |     |     |     |     |
| Category    | Zerotouchprovisioning                    |     |     |     |     |
| Severity    | Info                                     |     |     |     |     |
| Description | LogeventwhenZTPservicestops              |     |     |     |     |
| Event ID:   | 8703                                     |     |     |     |     |
| Message     | ZTPservicestatuschangedtoin-progress     |     |     |     |     |
| Category    | Zerotouchprovisioning                    |     |     |     |     |
| Severity    | Info                                     |     |     |     |     |
| Description | LogeventwhenZTPchangestatustoin-progress |     |     |     |     |
| Event ID:   | 8704                                     |     |     |     |     |
Message
ZTPservicestatuschangedtosuccess
| Category    | Zerotouchprovisioning                |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- |
| Severity    | Info                                 |     |     |     |     |
| Description | LogeventwhenZTPchangestatustosuccess |     |     |     |     |
| Event ID:   | 8705                                 |     |     |     |     |
471
AOS-CX10.16.xxxxEventLogMessageReferenceGuide|(AllSwitchSeries)

Message

ZTP service status changed to failed because of invalid configuration file

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of invalid config file

Event ID: 8706

Message

ZTP service status changed to failed because of invalid image file

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of invalid image file

Event ID: 8707

Message

ZTP service status changed to failed because TFTP info is not available

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP fails because no TFTP info is available

Event ID: 8708

Message

ZTP service status changed to failed because TFTP server is not reachable

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP fails because TFTP server is not reachable

Event ID: 8709

Message

ZTP service status changed to failed because of non-default startup configuration

Category

Zero touch provisioning

Severity

Info

Description

Log event when ZTP failed because of non-default startup config

Event ID: 8710

Message

ZTP service status changed to failed because running configuration is modified

Zero touch provisioning events | 472

Category

Zero touch provisioning

Severity

Info

Description

Log event when ZTP failed because of modified running config

Event ID: 8711

Message

ZTP service status changed to failed because of timeout

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP failed because of timeout

Event ID: 8712

Message

ZTP: Image file not provided

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ZTP configurations - image file not provided

Event ID: 8713

Message

ZTP: Config file not provided

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - config file not provided

Event ID: 8714

Message

ZTP: TFTP server option not provided

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - TFTP server name not provided

Event ID: 8715

Message

ZTP: Exceeded max path length of TFTP server

Category

Zero touch provisioning

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

473

Severity

Error

Description

Logs related to ztp configurations - path length exceeded of TFTP server name

Event ID: 8718

Message

ZTP: Received TFTP server <tftp_ip> from dhcp server

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - TFTP IP received

Event ID: 8719

Message

ZTP: Received image file <image_file> from dhcp server

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - Image filename received

Event ID: 8720

Message

ZTP: Received config file <config_file> from dhcp server

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - Config filename received

Event ID: 8721

Message

ZTP: Received HPE Aruba Networking Central location <central_location> from DHCP
server

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - HPE Aruba Networking Central FQDN or IPv4 received

Event ID: 8723

Message

ZTP: HPE Aruba Networking Central location option not provided

Category

Zero touch provisioning

Zero touch provisioning events | 474

Severity

Info

Description

Logs related to ztp configurations - HPE Aruba Networking Central FQDN or IPv4 not
provided

Event ID: 8724

Message

ZTP: Received HTTP proxy location <http_proxy_location> from DHCP server.

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - HTTP proxy FQDN or IPv4 received

Event ID: 8726

Message

ZTP: HTTP proxy location was not received in the DHCP offer.

Category

Zero touch provisioning

Severity

Info

Description

Logs related to ztp configurations - HTTP Proxy FQDN or IPv4 not provided

Event ID: 8727

Message

ZTP service status changed to failed because <filename> file download encountered
unexpected error.

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of unexpected error in config/image file download

Event ID: 8728

Message

ZTP service status changed to failed because <filename> file did not get downloaded.

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of config/image file download error

Event ID: 8729

Message

ZTP service status changed to failed because the downloaded configuration could not be
copied to start-up configuration.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

475

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because downloaded config did not get copied to start-up
config

Event ID: 8730

Message

ZTP service status changed to failed because <filename> file download encountered
unexpected error. Reason: <reason>

Category

Zero touch provisioning

Severity

Error

Description

Log event when ZTP fails because of unexpected error in config file download

Event ID: 8731

Message

Received Alternative HPE Aruba Networking Central location {alt_aruba_central_loc} from
dhcp server.

Category

Zero touch provisioning

Severity

Info

Description

Log event when ZTP receives the Alternative HPE Aruba Networking Central location.

Zero touch provisioning events | 476

Chapter 154

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.hpe.com/us/en/networking/hpe-aruba-networking-
support-services.html

AOS-CX Switch Software Documentation
Portal

https://arubanetworking.hpe.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

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

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

477

HPEAruba https://arubanetworking.hpe.com/techdocs/hardware/DocumentationPortal/Content/home.
| Networking | htmm |     |
| ---------- | ---- | --- |
Hardware
Documentation
andTranslations
Portal
| HPEAruba | https://networkingsupport.hpe.com/downloads |     |
| -------- | ------------------------------------------- | --- |
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
YoucanaccessupdatesfromtheHPEArubaNetworkingSupportPortalat
https://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveHPEArubaNetworking
SupportPortalaccounttomanagesubscriptions).SecuritynoticesareviewablewithoutanHPEAruba
NetworkingSupportPortalaccount.
| Warranty | information |     |
| -------- | ----------- | --- |
Toviewwarrantyinformationforyourproduct,gotohttps://www.arubanetworks.com/support-services/product-
warranties/.
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
| Documentation |     | feedback |
| ------------- | --- | -------- |
Arubaiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpusimprovethedocumentation,
sendanyerrors,suggestions,orcommentstoDocumentationFeedback(docsfeedback-switching@hpe.com).When
submittingyourfeedback,includethedocumenttitle,partnumber,edition,andpublicationdatelocatedonthe
SupportandOtherResources|478

front cover of the document. For online help content, include the product name, product version, help edition, and
publication date located on the legal notices page.

AOS-CX 10.16.xxxx Event Log Message Reference Guide | (All Switch Series)

479